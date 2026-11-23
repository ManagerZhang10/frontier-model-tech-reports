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
| LLM | [Nemotron 3](./reports/llm/nemotron-3/) | NVIDIA | 2025-12-24 | [arXiv:2512.20856](https://arxiv.org/abs/2512.20856) |
| LLM | [Ministral 3](./reports/llm/ministral-3/) | Mistral | 2026-01-13 | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |
| LLM | [Gemma 4](./reports/llm/gemma-4/) | Google DeepMind | 2026-07-02 | [arXiv:2607.02770](https://arxiv.org/abs/2607.02770) |
| LLM | [DeepSeek-V3.2](./reports/llm/deepseek-v3.2/) | DeepSeek | 2025-12-02 | [arXiv:2512.02556](https://arxiv.org/abs/2512.02556) |
| LLM | [MiMo-V2-Flash](./reports/llm/mimo-v2-flash/) | Xiaomi | 2026-01-06 | [arXiv:2601.02780](https://arxiv.org/abs/2601.02780) |
| LLM | [GLM-5](./reports/llm/glm-5/) | Zhipu AI | 2026-02-17 | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |
| LLM（原生多模态） | [ERNIE 5.0](./reports/llm/ernie-5/) | ERNIE Team, Baidu | 2026-02-04 | [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) |
| LLM | [Kimi K3](./reports/llm/kimi-k3/) | Kimi Team, Moonshot AI | 2026-07-27 | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) |
| LLM | [DeepSeek-V4](./reports/llm/deepseek-v4/) | DeepSeek | 2026-04-26 | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) |
| LLM | [DeepSeek-V4.1-Flash](./reports/llm/deepseek-v4.1-flash/) | DeepSeek | 2026-09-17 | [arXiv:2609.19969](https://arxiv.org/abs/2609.19969) |
| LLM | [MiniMax-M2 Series](./reports/llm/minimax-m2/) | MiniMax | 2026-05-26 | [arXiv:2605.26494](https://arxiv.org/abs/2605.26494) |
| LLM（稀疏注意力方法） | [MiniMax Sparse Attention (M3)](./reports/llm/minimax-msa-m3/) | MiniMax | 2026-06-11 | [arXiv:2606.13392](https://arxiv.org/abs/2606.13392) |
| LLM | [Nemotron 3.5 Super and Lightning](./reports/llm/nemotron-3.5-super/) | NVIDIA | 2026-10-28 | [arXiv:2610.38095](https://arxiv.org/abs/2610.38095) |
| LLM（模型卡） | [Seed2.0](./reports/llm/seed2.0/) | ByteDance Seed | 2026-06-30 | [arXiv:2607.00248](https://arxiv.org/abs/2607.00248) |
| LLM | [Olmo 3](./reports/llm/olmo-3/) | Ai2 / Olmo Team | 2025-12-15 | [arXiv:2512.13961](https://arxiv.org/abs/2512.13961) |
| VLM | [Qwen3-VL](./reports/vlm/qwen3-vl/) | Qwen Team | 2025-11-26 | [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) |
| VLM | [可灵：视频生成背后的多模态理解](./reports/vlm/kling-understanding/) | Kling Team, Kuaishou Technology | 2026-11-03 | [arXiv:2611.04916](https://arxiv.org/abs/2611.04916) |
| VLM | [Qwen3.5-Omni](./reports/vlm/qwen3.5-omni/) | Qwen Team | 2026-04-17 | [arXiv:2604.15804](https://arxiv.org/abs/2604.15804) |
| VLM | [Kimi K2.5](./reports/vlm/kimi-k2.5/) | Kimi Team, Moonshot AI | 2026-02-02 | [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) |
| VLM | [GLM-5V-Turbo](./reports/vlm/glm-5v-turbo/) | Z.ai & Tsinghua University | 2026-04-29 | [arXiv:2604.26752](https://arxiv.org/abs/2604.26752) |
| VLM | [STEP3-VL-10B](./reports/vlm/step3-vl-10b/) | StepFun | 2026-01-14 | [arXiv:2601.09668](https://arxiv.org/abs/2601.09668) |
| VLM | [Keye-VL-2.0](./reports/vlm/keye-vl-2.0/) | Keye Team, Kuaishou Group | 2026-06-09 | [arXiv:2606.10651](https://arxiv.org/abs/2606.10651) |
| VLM（Omni） | [Nemotron 3 Nano Omni](./reports/vlm/nemotron-3-nano-omni/) | NVIDIA | 2026-04-27 | [arXiv:2604.24954](https://arxiv.org/abs/2604.24954) |
| VLM（统一多模态） | [LongCat-Next](./reports/vlm/longcat-next/) | Meituan LongCat Team | 2026-03-29 | [arXiv:2603.27538](https://arxiv.org/abs/2603.27538) |
| LLM（短记） | [【短记】Gemini 3 Pro Model Card](./reports/llm/gemini-3-pro-card/) | Google DeepMind | 2025-11（目录取 2025-11-01） | [官方 PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf) |
| LLM（短记） | [【短记】GPT-5.5 System Card](./reports/llm/gpt-5.5-card/) | OpenAI | 2026-04-23 | [官方 PDF](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf) |
| LLM（短记） | [【短记】Claude Opus 5.5 System Card](./reports/llm/claude-opus-5.5-card/) | Anthropic | 2026-09-22 | [官方 PDF](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf) |
| LLM（短记） | [【短记】Qwen4-Max](./reports/llm/qwen4-max/) | Alibaba / Qwen | 2026-11-16 | [官方新闻稿](https://www.alibabagroup.com/en-US/document-2060139246777270272) |
| LLM（短记） | [【短记】GPT-6.2 Astra / Sol System Card](./reports/llm/gpt-6.2-card/) | OpenAI | 2026-11-17 | [官方 PDF](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf) |
| LLM（短记） | [【短记】Gemini 4 Neon Model Card](./reports/llm/gemini-4-neon-card/) | Google DeepMind | 2026-11-18（博客发布日；卡内仅标 2026-11） | [官方 PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf) |
| 图像生成 | [Z-Image](./reports/image/z-image/) | Alibaba Group / Z-Image Team | 2025-11-27 | [arXiv:2511.22699](https://arxiv.org/abs/2511.22699) |
| 图像生成（短记） | [【短记】FLUX.2](./reports/image/flux-2/) | Black Forest Labs | 2025-11-25 | [官方博客](https://bfl.ai/blog/flux-2) · [VAE 博文](https://bfl.ai/techblog/representation-comparison) |
| 图像生成 / 编辑 | [FireRed-Image-Edit](./reports/image/firered-image-edit/) | 小红书 Super Intelligence Team | 2026-02-12 | [arXiv:2602.13344](https://arxiv.org/abs/2602.13344) |
| 图像生成 / 编辑 | [Qwen-Image-2.0](./reports/image/qwen-image-2.0/) | Qwen Team | 2026-05-11 | [arXiv:2605.10730](https://arxiv.org/abs/2605.10730) |
| 图像生成 / 编辑 | [Wan-Image](./reports/image/wan-image/) | Wan Team, Alibaba Group | 2026-04-21 | [arXiv:2604.19858](https://arxiv.org/abs/2604.19858) |
| 图像生成 / 编辑 | [LongCat-Image](./reports/image/longcat-image/) | Meituan LongCat Team | 2025-12-08 | [arXiv:2512.07584](https://arxiv.org/abs/2512.07584) |
| 图像生成 | [ERNIE-Image](./reports/image/ernie-image/) | ERNIE Team, Baidu | 2026-05-25 | [arXiv:2605.25347](https://arxiv.org/abs/2605.25347) |
| 图像生成 / 编辑 | [Qwen-Image-2.0-RL](./reports/image/qwen-image-2.0-rl/) | Qwen Team | 2026-06-25 | [arXiv:2606.27608](https://arxiv.org/abs/2606.27608) |
| 统一多模态 | [InternVL-U](./reports/image/internvl-u/) | Shanghai AI Laboratory 等 | 2026-03-10 | [arXiv:2603.09877](https://arxiv.org/abs/2603.09877) |
| 图像评测基准 | [Qwen-Image-Bench](./reports/image/qwen-image-bench/) | Qwen Team | 2026-05-27 | [arXiv:2605.28091](https://arxiv.org/abs/2605.28091) |
| 视频生成 | [HunyuanVideo 1.5](./reports/video/hunyuanvideo-1.5/) | Tencent Hunyuan Foundation Model Team | 2025-11-24 | [arXiv:2511.18870](https://arxiv.org/abs/2511.18870) |
| 视频生成 | [Kling-Omni](./reports/video/kling-omni/) | Kling Team, Kuaishou Technology | 2025-12-18 | [arXiv:2512.16776](https://arxiv.org/abs/2512.16776) |
| 视频生成 | [Seedance 2.0](./reports/video/seedance-2.0/) | ByteDance Seed | 2026-04-15 | [arXiv:2604.14148](https://arxiv.org/abs/2604.14148) |
| 视频生成（音画联合） | [Seedance 1.5 pro](./reports/video/seedance-1.5-pro/) | ByteDance Seed | 2025-12-15 | [arXiv:2512.13507](https://arxiv.org/abs/2512.13507) |
| 视频生成（音画联合） | [LTX-2](./reports/video/ltx-2/) | Lightricks | 2026-01-06 | [arXiv:2601.03233](https://arxiv.org/abs/2601.03233) |
| 实时交互音视频 | [Wan-Streamer](./reports/video/wan-streamer/) | Wan Team, Alibaba Group | 2026-06-23 | [arXiv:2606.25041](https://arxiv.org/abs/2606.25041) |
| 世界模型 / 视频与动作 | [Cosmos 3](./reports/video/cosmos-3/) | NVIDIA | 2026-06-01 | [arXiv:2606.02800](https://arxiv.org/abs/2606.02800) |


更多候选见 [`CANDIDATES.md`](./CANDIDATES.md)。更新记录见 [`CHANGELOG.md`](./CHANGELOG.md)。

## 这个站点怎么做出来的

1. 从 arXiv（或厂商官方 PDF）下载技术报告，抽出文本，并从 PDF 中裁出关键原图。
2. 用统一的 HTML 提示词，由 Claude Code 根据原文起草图文深读。
3. 对照原文文本核对数字，修正不一致；发布日期一律采用 arXiv v1 的 published 日期。
4. 共享样式与主题脚本在 [`assets/`](./assets/)，每篇报告位于 `reports/<类别>/<slug>/`，可在 GitHub Pages 上独立打开。

欢迎指出事实错误或推荐下一篇应该覆盖的报告。
