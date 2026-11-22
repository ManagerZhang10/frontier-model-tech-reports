#!/usr/bin/env python3
"""Extract key paper figures: caption-located page crops + large embedded rasters."""
from __future__ import annotations
import json, os, re, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

Image.MAX_IMAGE_PIXELS = 200_000_000

def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)

def pdfinfo(pdf):
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace")
    pages = 0
    for line in out.splitlines():
        if line.startswith("Pages:"):
            pages = int(line.split(":")[1])
    return pages, out

def layout_text(pdf, dest):
    run(["pdftotext", "-layout", str(pdf), str(dest)])
    return Path(dest).read_text(encoding="utf-8", errors="replace")

def figure_pages(text):
    """Return list of (fig_num, page_1indexed, caption)."""
    pages = text.split("\x0c")
    found = []
    seen = set()
    for i, p in enumerate(pages, 1):
        for m in re.finditer(r'(?:^|\n)\s*(Figure|Fig\.?)\s+(\d+)(?:\s*[|:.\u2013\u2014-]\s*|\s+)(.+)', p):
            n = int(m.group(2))
            cap = " ".join(m.group(3).split())
            # stop caption at next figure/table or end of ~400 chars
            cap = re.split(r'\s+(?:Figure|Table|Fig\.)\s+\d+', cap)[0]
            cap = cap[:400].strip()
            if n in seen:
                continue
            seen.add(n)
            found.append((n, i, cap))
    return found

def content_bbox(im, white=250, pad=12):
    g = im.convert("L")
    w, h = g.size
    px = g.load()
    minx, miny, maxx, maxy = w, h, 0, 0
    found = False
    for y in range(h):
        for x in range(w):
            if px[x, y] < white:
                found = True
                if x < minx: minx = x
                if y < miny: miny = y
                if x > maxx: maxx = x
                if y > maxy: maxy = y
    if not found:
        return im
    minx = max(0, minx - pad); miny = max(0, miny - pad)
    maxx = min(w, maxx + pad + 1); maxy = min(h, maxy + pad + 1)
    return im.crop((minx, miny, maxx, maxy))

def row_ink(im, thresh=250):
    g = im.convert("L")
    w, h = g.size
    px = g.load()
    return [sum(1 for x in range(0, w, 2) if px[x, y] < thresh) for y in range(h)]

def crop_above_caption(im, caption_hint=None):
    """Crop the main figure block in the upper/mid page, excluding caption and body text."""
    rows = row_ink(im)
    h = len(rows)
    # Find the largest contiguous ink band in the top 70% that's not a thin text line
    bands = []
    inb = False
    s = 0
    for y, ink in enumerate(rows):
        if ink > 25 and not inb:
            inb = True
            s = y
        elif ink <= 25 and inb:
            inb = False
            bands.append((s, y, y - s, max(rows[s:y]) if y > s else 0))
    if inb:
        bands.append((s, h, h - s, max(rows[s:]) if h > s else 0))
    # Prefer tall bands in the upper portion (figures), skip tiny header lines
    fig_bands = [b for b in bands if b[2] >= 80 and b[0] < h * 0.75]
    if not fig_bands:
        fig_bands = [b for b in bands if b[2] >= 40]
    if not fig_bands:
        return content_bbox(im.crop((0, int(h * 0.08), im.size[0], int(h * 0.55))))
    # Merge consecutive figure-like bands (diagram + labels)
    # Take from first substantial band to last one before a long text block
    # Heuristic: pick the max-height band and expand to neighbors within 40px
    best = max(fig_bands, key=lambda b: b[2] * (1.0 if b[0] < h * 0.55 else 0.6))
    top, bot = best[0], best[1]
    for b in fig_bands:
        if b[1] >= top - 30 and b[0] <= bot + 30:
            top = min(top, b[0])
            bot = max(bot, b[1])
    # Don't include the very top running header if it's a thin band
    top = max(0, top - 8)
    bot = min(h, bot + 8)
    # Trim left/right white
    cropped = im.crop((0, top, im.size[0], bot))
    return content_bbox(cropped, pad=10)

def save_web(im, dest: Path, max_w=2200):
    im = im.convert("RGB")
    w, h = im.size
    if w > max_w:
        im = im.resize((max_w, int(h * max_w / w)), Image.Resampling.LANCZOS)
    # Choose jpeg for large photographic/complex, png for simple charts
    # Use jpeg if many unique colors
    dest = dest.with_suffix(".jpg")
    im.save(dest, quality=88, optimize=True, subsampling=0)
    # If jpeg is surprisingly large and image is chart-like, also try png
    return dest

def extract(pdf: Path, outdir: Path, dpi=180, max_figs=6):
    outdir.mkdir(parents=True, exist_ok=True)
    pages_n, _ = pdfinfo(pdf)
    with tempfile.TemporaryDirectory(prefix="figx-") as td:
        td = Path(td)
        layout_path = td / "layout.txt"
        text = layout_text(pdf, layout_path)
        figs = figure_pages(text)
        # Always consider page 1 as potential teaser (fig 0)
        targets = []
        if figs:
            # Prefer earlier figures (architecture) and mid result figures
            # Keep first 2, last 2, and largest-caption ones if many
            if len(figs) <= max_figs:
                chosen = figs
            else:
                first = figs[:2]
                rest = figs[2:]
                # also include any figure whose caption mentions architecture, pipeline, overview, result, comparison
                keys = re.compile(r'architect|pipeline|overview|framework|result|compar|ablation|data|training|qualitative', re.I)
                important = [f for f in rest if keys.search(f[2])]
                chosen = first + important
                # fill with remaining in order
                for f in rest:
                    if f not in chosen:
                        chosen.append(f)
                    if len(chosen) >= max_figs:
                        break
                chosen = chosen[:max_figs]
            targets = chosen
        else:
            targets = []

        manifest = []
        rendered = {}

        def render_page(pno):
            if pno in rendered:
                return rendered[pno]
            prefix = td / f"p{pno}"
            run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(pno), "-l", str(pno), str(pdf), str(prefix)])
            # pdftoppm names p{pno}-pno.png or p{pno}.png depending
            cands = list(prefix.parent.glob(prefix.name + "*.png"))
            if not cands:
                raise FileNotFoundError(f"no render for page {pno}")
            im = Image.open(cands[0])
            rendered[pno] = im
            return im

        # page 1 teaser if it has a large lower graphic
        try:
            im1 = render_page(1)
            rows = row_ink(im1)
            h = len(rows)
            # large ink in lower 45%
            lower = rows[int(h*0.50):]
            if lower and max(lower) > 80 and sum(1 for v in lower if v > 20) > 80:
                teaser = crop_above_caption(im1.crop((0, int(h*0.45), im1.size[0], int(h*0.98))))
                # skip if too small or almost blank
                if teaser.size[1] >= 120 and teaser.size[0] >= 400:
                    dest = save_web(teaser, outdir / "fig0-teaser")
                    manifest.append({"file": dest.name, "figure": "teaser", "page": 1,
                                     "caption_en": "First-page teaser / overview figure",
                                     "caption_note": "来源：论文首页图"})
        except Exception as e:
            print("teaser failed:", e, file=sys.stderr)

        for n, pno, cap in targets:
            try:
                im = render_page(pno)
                crop = crop_above_caption(im)
                if crop.size[0] < 200 or crop.size[1] < 80:
                    continue
                slug = f"fig{n}"
                dest = save_web(crop, outdir / slug)
                manifest.append({"file": dest.name, "figure": n, "page": pno,
                                 "caption_en": cap, "caption_note": f"来源：论文图 {n}"})
                print(f"  fig {n} p{pno} -> {dest.name} {Image.open(dest).size} {dest.stat().st_size}")
            except Exception as e:
                print(f"  fig {n} p{pno} FAILED: {e}", file=sys.stderr)

        (outdir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote {len(manifest)} figures to {outdir}")
        return manifest

if __name__ == "__main__":
    pdf = Path(sys.argv[1])
    out = Path(sys.argv[2])
    extract(pdf, out)
