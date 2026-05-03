---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "PCAS 程序图像处理"
aliases:
  - "PCAS"
  - "Particle and Crack Analysis Software"
sources:
  - "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
---

# PCAS 程序图像处理

## Purpose

从裂缝迹线图中自动提取几何参数，如方位、长度、中心位置等。
## Aliases

- PCAS
- Particle and Crack Analysis Software
## Workflow

设置图像分辨率、颜色、透明度，PCAS 识别裂缝迹线，输出 23 个几何特征参数。
## Inputs

- 数字裂缝图像
- 像素参数
## Outputs

- 裂缝方向统计
- 迹长分布
- 中点坐标
## Assumptions

- 裂缝与背景对比度足够
- 图像预处理充分
## Strengths

- 可自动化处理大量图像
## Limitations

- 提取精度受图像质量影响
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre](../papers/2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre.md)
