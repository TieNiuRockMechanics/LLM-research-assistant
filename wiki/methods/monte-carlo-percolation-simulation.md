---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "蒙特卡罗逾渗模拟"
aliases:
  - "Monte Carlo percolation"
sources:
  - "1997-bour-connectivity-of-random-fault-networks-following-a-power-law-fault-length-distribution"
  - "2003-darcel-connectivity-properties-of-two-dimensional-fracture-networks-with-stochastic-fractal"
  - "2003-nakaya-percolation-conditions-in-binary-fractal-fracture-networks-applications-to-rock-frac"
---

# 蒙特卡罗逾渗模拟

## Purpose

确定离散裂隙网络的连通概率和逾渗阈值。
## Aliases

- Monte Carlo percolation
## Workflow

生成随机裂隙网络，逐步增加裂隙数量或扩大系统尺寸，查找跨越团簇，统计连通概率。
## Inputs

- 裂隙长度、方位、密度分布函数
- 系统尺寸
## Outputs

- 逾渗概率 p
- 临界密度或尺寸
## Assumptions

- 裂隙为直线段或平面多边形
- 位置和方位随机分布
## Strengths

- 可处理复杂分布
## Limitations

- 计算量大，需大量实现以降低统计波动
## Related Concepts

- percolation-threshold
- discrete-fracture-network
## Source Papers

- [1997-bour-connectivity-of-random-fault-networks-following-a-power-law-fault-length-distribution](../papers/1997-bour-connectivity-of-random-fault-networks-following-a-power-law-fault-length-distribution.md)
- [2003-darcel-connectivity-properties-of-two-dimensional-fracture-networks-with-stochastic-fractal](../papers/2003-darcel-connectivity-properties-of-two-dimensional-fracture-networks-with-stochastic-fractal.md)
- [2003-nakaya-percolation-conditions-in-binary-fractal-fracture-networks-applications-to-rock-frac](../papers/2003-nakaya-percolation-conditions-in-binary-fractal-fracture-networks-applications-to-rock-frac.md)
