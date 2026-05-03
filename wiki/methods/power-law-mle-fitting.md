---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "幂律分布最大似然估计拟合 (MLE for Power‑Law)"
aliases:
  - "MLE power-law fitting"
  - "最大似然估计幂律拟合"
sources:
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
---

# 幂律分布最大似然估计拟合 (MLE for Power‑Law)

## Purpose

用最大似然法估计裂缝长度幂律分布的标度指数 α 和最小长度 xmin。
## Aliases

- MLE power-law fitting
- 最大似然估计幂律拟合
## Workflow

设定 xmin 候选，计算似然函数，选择使似然最大或 KS 统计量最小的 xmin，提取 α。
## Inputs

- 裂缝长度数据
## Outputs

- α, xmin
- 拟合优度
## Assumptions

- 数据服从截断幂律分布
## Strengths

- 参数估计稳健
## Limitations

- 对小样本有偏
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
