---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "圆形扫描窗法 (Circular Scanline Method)"
aliases:
  - "circular scanline"
  - "scanline window"
sources:
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
---

# 圆形扫描窗法 (Circular Scanline Method)

## Purpose

通过在图像上放置圆形采样窗，计算单位面积内裂隙总长度（P21）或数量（P20）。
## Aliases

- circular scanline
- scanline window
## Workflow

定义采样圆半径，系统覆盖图像，统计每个圆内裂隙长度或数量，计算均值及标准差。
## Inputs

- 裂隙迹线图
- 圆半径
## Outputs

- 裂缝强度 P21（或 P20）
## Assumptions

- 圆形窗无偏采样
- 裂隙迹线无重叠
## Strengths

- 操作简单，广泛使用
## Limitations

- 边界效应需校正
## Related Concepts

- fracture-intensity
## Source Papers

- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
