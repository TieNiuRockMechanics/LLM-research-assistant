---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "裂缝骨架化与距离变换 (开度提取)"
aliases:
  - "skeletonization"
  - "distance transform"
sources:
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
---

# 裂缝骨架化与距离变换 (开度提取)

## Purpose

从二值裂缝图像中获取骨架，再通过距离变换计算每个像素处的裂缝开度。
## Aliases

- skeletonization
- distance transform
## Workflow

对裂缝二值图像细化得到骨架，对骨架像素应用欧氏距离变换，记录开度值。
## Inputs

- 裂缝二值图
## Outputs

- 开度分布
- 平均开度
- 变异系数 CV
## Assumptions

- 裂缝可细化为单像素宽线条
- 距离变换反映真实开度
## Strengths

- 可提取空间变异性
## Limitations

- 对二值化敏感
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
