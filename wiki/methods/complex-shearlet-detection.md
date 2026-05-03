---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于复剪切波变换的裂缝迹线自动检测"
aliases:
  - "complex shearlet transform"
sources:
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
---

# 基于复剪切波变换的裂缝迹线自动检测

## Purpose

从灰度裂缝图像中自动提取裂缝骨架，生成矢量裂缝迹线。
## Aliases

- complex shearlet transform
## Workflow

对图像进行复剪切波分解，多尺度边缘检测，阈值分割（Otsu），细化骨架，导出线段。
## Inputs

- 裂缝灰度图
## Outputs

- 裂缝迹线段
## Assumptions

- 裂缝与背景对比鲜明
## Strengths

- 自动、多尺度
## Limitations

- 可能漏检或过分割
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
