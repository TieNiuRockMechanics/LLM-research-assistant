---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "利用统计参数估算节理粗糙度系数 (Z₂ 法)"
aliases:
  - "Z2 method for JRC"
  - "Statistical parameter method for JRC"
sources:
  - "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
---

# 利用统计参数估算节理粗糙度系数 (Z₂ 法)

## Purpose

通过数字化节理剖面线，计算其统计几何参数（如均方根一阶导数 Z₂），并利用经验回归方程式快速估算 JRC 值。
## Aliases

- Z2 method for JRC
- Statistical parameter method for JRC
## Workflow

以固定采样间隔对节理剖面进行高精度数字化；对齐剖面（去除线性趋势）；计算一阶导数均方根 Z₂；将 Z₂ 代入预先建立的 JRC–Z₂ 幂律或多项式经验关系式，得到 JRC 估算值。
## Inputs

- 以固定间隔数字化节理剖面的坐标 (x, y)
## Outputs

- JRC 的估算值
## Assumptions

- 节理剖面可被视为二维且自仿射
- 估算关系式来源于对 Barton 标准剖面的回归分析
- 采样间隔决定了计算结果及其与回归公式的匹配度
## Strengths

- 计算效率高，易于自动化处理
- 比传统视觉对比法更为客观
## Limitations

- Z₂ 对采样间隔高度敏感，误用不同采样间隔的回归公式将导致显著误差
- 主要捕捉小尺度坡度信息，可能忽略剖面幅值（波状）对粗糙度的重要贡献
- 对特定天然节理可能存在系统性偏差
## Related Concepts

- joint-roughness-coefficient
## Source Papers

- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md)
