---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "二维粗糙度参数评价方法 (θ*max/(C+1)2D)"
aliases:
  - "θ*max/(C+1)2D method"
  - "2D roughness evaluation methodology"
sources:
  - "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
  - "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
---

# 二维粗糙度参数评价方法 (θ*max/(C+1)2D)

## Purpose

基于分析方向（即剪切方向）和倾角阈值概念，从二维节理剖面中提取与方向相关的粗糙度参数，更合理地量化各向异性节理的粗糙度。
## Aliases

- θ*max/(C+1)2D method
- 2D roughness evaluation methodology
## Workflow

对重对齐的剖面指定分析方向（正向或反向）；计算沿该方向各线段倾角 θ*；统计超过一系列递增倾角阈值的线段累计长度并归一化得 Ly*；用非线性最小二乘法将 Ly* 与 θ* 的累积分布拟合到方程 Ly*=L0((y*max – y*)/y*max)^C，得到参数 y*max/(C+1)2D。
## Inputs

- 沿特定方向提取的二维剖面坐标
## Outputs

- y*max/(C+1)2D 粗糙度参数
- 正向与反向的平均值
## Assumptions

- 剪切过程中只在正对剪切方向的倾角区域发生接触和磨损
- 累积分布可用指数形式方程拟合
## Strengths

- 考虑了剪切方向和粗糙度的各向异性，更贴近真实物理过程
- 参数值与 JRC 高相关
## Limitations

- 二维剖面可能高估或低估真实三维粗糙度
- 对采样间隔和数字化精度敏感
## Related Concepts

- joint-roughness-coefficient
## Source Papers

- [2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc](../papers/2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc.md)
- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md)
