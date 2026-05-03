---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "更新的 h–L 法"
aliases:
  - "updated h–L method for fractal dimension"
sources:
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
---

# 更新的 h–L 法

## Purpose

一种客观可编程的分形维数计算方法，用于表征节理剖面粗糙度，避免人工识别高阶凹凸体的主观性。
## Aliases

- updated h–L method for fractal dimension
## Workflow

去除剖面线性趋势，用最小二乘法拟合剖面并确定与剖面的所有交点；将剖面分割为若干小段，测量每段的基底长度 L 和极值振幅 h；取所有段的 h、L 平均值代入 D = log(4)/log(2[1+cos(arctan(2h/L))]) 计算分形维数。
## Inputs

- 节理剖面的二维数字化坐标
## Outputs

- 分形维数 Dh–L
## Assumptions

- 剖面在去除趋势后可视为自仿射分形
- 交点法确定的 h、L 平均值能表征整体粗糙度
## Strengths

- 客观、可重复性好
- 易于自动化
## Limitations

- 易受数字化噪声和重采样误差影响
- 目前限于实验室尺度和固定采样间隔
## Related Concepts

- fractal-dimension
- joint-roughness-coefficient
## Source Papers

- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
