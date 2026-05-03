---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "平行板模型 / 立方定律 (Cubic Law)"
aliases:
  - "parallel plate model"
  - "cubic law"
sources:
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
---

# 平行板模型 / 立方定律 (Cubic Law)

## Purpose

采用恒定开度 b 或光滑平行板假设，利用 k = b²/12 快速估计单裂隙或网络等效渗透率。
## Aliases

- parallel plate model
- cubic law
## Workflow

假设每条裂缝为一对光滑平行板，由开度 b 按立方定律计算导水系数 T = b³/12μ；在 DFN 中合成等效渗透率张量。
## Inputs

- 裂缝网络几何
- 恒定开度 b（或分布）
## Outputs

- 等效渗透率 k 或导水系数 T
## Assumptions

- 裂缝壁光滑平行
- 层流达西流
- 忽略粗糙度和接触面积影响
## Strengths

- 计算快速
- 解析基础明确
## Limitations

- 忽略粗糙度、接触面积和非线性效应
- 不适用于变开度或复杂形貌的裂隙
## Related Concepts

- fracture-permeability
- cubic-law
## Source Papers

- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
