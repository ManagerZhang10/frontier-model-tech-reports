/* shared theme + TOC highlighter */
(function () {
  try {
    var t = localStorage.getItem("ftr-theme");
    if (t) document.documentElement.setAttribute("data-theme", t);
  } catch (e) {}
})();

document.addEventListener("DOMContentLoaded", function () {
  var root = document.documentElement,
      btn = document.getElementById("themeBtn"),
      lab = document.getElementById("themeLabel");
  function current() {
    var t = root.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function sync() { if (lab) lab.textContent = current() === "dark" ? "浅色" : "深色"; }
  if (btn) {
    btn.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("ftr-theme", next); } catch (e) {}
      sync();
    });
  }
  sync();

  var links = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  if (!links.length) return;
  var map = {};
  links.forEach(function (a) {
    var href = a.getAttribute("href") || "";
    if (href.charAt(0) === "#") map[href.slice(1)] = a;
  });
  var secs = links.map(function (a) {
    var href = a.getAttribute("href") || "";
    return href.charAt(0) === "#" ? document.getElementById(href.slice(1)) : null;
  }).filter(Boolean);
  function setActive(id) {
    links.forEach(function (a) { a.classList.remove("active"); });
    var a = map[id]; if (!a) return;
    a.classList.add("active");
    var toc = a.closest(".toc");
    if (toc && toc.scrollWidth > toc.clientWidth) {
      toc.scrollTo({ left: a.offsetLeft - 24, behavior: "smooth" });
    }
  }
  function onScroll() {
    var y = window.innerHeight * 0.3, cur = null;
    for (var i = 0; i < secs.length; i++) {
      if (secs[i].getBoundingClientRect().top - y <= 0) cur = secs[i].id;
    }
    setActive(cur);
  }
  var ticking = false;
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(function () { onScroll(); ticking = false; }); }
  }, { passive: true });
  onScroll();
});
