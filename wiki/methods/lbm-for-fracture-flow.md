---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "格子 Boltzmann 方法模拟裂隙流 (LBM for Fracture Flow)"
aliases:
  - "Lattice Boltzmann Method for fracture flow"
sources:
  - "2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur"
---

# 格子 Boltzmann 方法模拟裂隙流 (LBM for Fracture Flow)

## Purpose

通过求解介观尺度的 LBM 方法，模拟裂隙内部复杂流场，特别是由表面粗糙度引起的非线性流动和涡流。
## Aliases

- Lattice Boltzmann Method for fracture flow
## Workflow

建立包含高精度粗糙度的三维裂隙形貌模型；设定周期性边界条件驱动压力梯度；采用 D2Q9 LBM 结合 BGK 碰撞模型在 GPU 上进行大规模计算；输出流量、压力梯度及流线；通过与非线性的达西-福希海默或 Izbash 方程拟合计算有效隙宽和湍流指标。
## Inputs

- 高分辨率裂隙形貌几何体
- 流体密度和粘度
- 驱动力（如重力加速度）
## Outputs

- 有效水力隙宽
- Forchheimer 系数 (a₁, b) 或 Izbash 参数 (c, β)
- 涡流体积和位置分布
- 流线图
## Assumptions

- 二维模拟，侧壁影响可忽略
- 流体为不可压缩层流
- 周期性边界模拟无限长裂隙段
- BGK 碰撞模型能代表平均流动行为
## Strengths

- 高精度捕捉惯性和粗糙度导致的非线性流动及涡流动力学
- 天然适合大规模并行计算（GPU）
## Limitations

- 二维模拟无法处理三维接触点、交叉和通道化效应
- BGK 近似在部分参数范围内有数值误差
- 计算域尺寸受限
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur](../papers/2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur.md)
