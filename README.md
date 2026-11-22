# 前沿模型技术报告

各大厂前沿模型技术报告的**中文深读**（LLM / VLM / 图像生成 / 视频生成），图文并茂，持续更新。

**在线阅读：[GitHub Pages](https://managerzhang10.github.io/frontier-model-tech-reports/)** · 仓库：https://github.com/ManagerZhang10/frontier-model-tech-reports

每篇深读都按同一套格式来写，方便扫读：

- Hero 与徽章（开源情况、规模、类别）
- 速览卡与 TL;DR
- 架构、**数据（最细）**、训练配方、评测
- 新在哪
- **对图像编辑数据 / 评测 / caption 的启示**
- 局限与存疑（含原文前后不一致之处）
- 论文原图 + 出处标签（每个关键数字都标表号 / 图号 / 章节号）

## 已发布深读

页面上的卡片与筛选以 [`reports.json`](./reports.json) 为准，也会在本表同步。

| 类别 | 模型 | 厂商 | 日期 | 原文 |
| --- | --- | --- | --- | --- |
| VLM | [Qwen3-VL](./reports/vlm/qwen3-vl/) | Qwen Team | 2025-11-26 | [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) |
| 图像生成 | [Z-Image](./reports/image/z-image/) | Alibaba Group / Z-Image Team | 2025-11-27 | [arXiv:2511.22699](https://arxiv.org/abs/2511.22699) |
| 图像生成 / 编辑 | [FireRed-Image-Edit](./reports/image/firered-image-edit/) | 小红书 Super Intelligence Team | 2026-02-12 | [arXiv:2602.13344](https://arxiv.org/abs/2602.13344) |
| 图像生成 / 编辑 | [Qwen-Image-2.0](./reports/image/qwen-image-2.0/) | Qwen Team | 2026-05-11 | [arXiv:2605.10730](https://arxiv.org/abs/2605.10730) |
| 图像生成 / 编辑 | [Wan-Image](./reports/image/wan-image/) | Wan Team, Alibaba Group | 2026-04-21 | [arXiv:2604.19858](https://arxiv.org/abs/2604.19858) |
| 视频生成 | [HunyuanVideo 1.5](./reports/video/hunyuanvideo-1.5/) | Tencent Hunyuan Foundation Model Team | 2025-11-24 | [arXiv:2511.18870](https://arxiv.org/abs/2511.18870) |
| 视频生成 | [Kling-Omni](./reports/video/kling-omni/) | Kling Team, Kuaishou Technology | 2025-12-18 | [arXiv:2512.16776](https://arxiv.org/abs/2512.16776) |
| 视频生成 | [Seedance 2.0](./reports/video/seedance-2.0/) | ByteDance Seed | 2026-04-15 | [arXiv:2604.14148](https://arxiv.org/abs/2604.14148) |


更多候选见 [`CANDIDATES.md`](./CANDIDATES.md)。更新记录见 [`CHANGELOG.md`](./CHANGELOG.md)。

## 这个站点怎么做出来的

1. 从 arXiv（或厂商官方 PDF）下载技术报告，抽出文本，并从 PDF 中裁出关键原图。
2. 用统一的 HTML 提示词，由 Claude Code 根据原文起草图文深读。
3. 对照原文文本核对数字，修正不一致；发布日期一律采用 arXiv v1 的 published 日期。
4. 共享样式与主题脚本在 [`assets/`](./assets/)，每篇报告位于 `reports/<类别>/<slug>/`，可在 GitHub Pages 上独立打开。

欢迎指出事实错误或推荐下一篇应该覆盖的报告。
