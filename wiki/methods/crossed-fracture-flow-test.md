---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "交叉裂隙流动实验"
aliases:
  - "crossed-fracture flow test"
sources:
  - "2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles"
---

# 交叉裂隙流动实验

## Purpose

通过对含有可控粗糙度的单个交叉裂隙模型进行水流-压差实验，配合高精度成像确定的机械隙宽，建立非线性流动（如 Forchheimer 定律）的定量判据及其与几何参数的关系。
## Aliases

- crossed-fracture flow test
## Workflow

制作具有已知交叉角和表面形貌的透明裂隙物理模型；按一个入口两个出口循环施加从低到高的流量，记录压力降和流量；用 Forchheimer 方程 J=AQ+BQ² 拟合数据；定义在压差中惯性项贡献达约 1% 时的临界水力梯度 Jc；改变机械隙宽、交叉数、粗糙度（JRC）进行数值实验。
## Inputs

- 可控表面形貌的裂隙模型
- 流量 Q
- 压力降 ΔP
## Outputs

- Forchheimer 系数 A, B
- 临界水力梯度 Jc
## Assumptions

- 层流，非线性仅由惯性项引起
- 隙宽在实验过程中不随压力变化
- Forchheimer 方程完全适合描述该流区
## Strengths

- 连接了微裂隙基本实验与网络级宏观非线性判据
- 提供了可工程直接参考的基于梯度而非雷诺数的判据
## Limitations

- 模型为二维，且只包含一个交叉点，与天然 DFN 的复杂性差距大
- 只对次级粗糙度（1st order）进行了建模，缺少天然裂缝的多尺度粗糙度叠加
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles](../papers/2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles.md)
