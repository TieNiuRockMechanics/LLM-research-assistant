---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "顺序父子泊松点过程 DFN 生成"
aliases:
  - "sequential parent-daughter Poisson process for DFN"
sources:
  - "2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio"
---

# 顺序父子泊松点过程 DFN 生成

## Purpose

通过时间上的随机播种序列，在三维 DFN 生成中引入模拟力学作用的空间相关性和层次结构，使生成的网络具有丛集性、尺度不变的应力影区和应力集中区。
## Aliases

- sequential parent-daughter Poisson process for DFN
## Workflow

将断裂生成过程分为多个阶段；在每个阶段，使用非均匀泊松过程生成候选点；定义一个受已存在断裂控制的概率函数 Ps，在“应力影区”内降低接受概率，在“应力集中区”内提高接受概率；通过接受-拒绝法筛选候选点，确定本阶段的断裂位置、大小和方向；按顺序重复以上步骤，最终建立整个网络。
## Inputs

- 阶段数 s
- 应力影区和应力集中区的范围因子
- 应力影区和集中区的强度因子
## Outputs

- 具有特定空间分形维数和层次结构的 DFN 模型
## Assumptions

- 断裂可简化为平面圆盘
- 应力影区和集中区可用简化的对称椭球模型表示
- 断裂的生长和合并过程已由长度分布律隐性考虑
## Strengths

- 可引入物理上合理的空间相关性
- 通过少量参数即可调控网络的关联维数和连通性
## Limitations

- 计算成本随播种阶段数显著增加
- 应力区域模型过于简化，无法反映真实的非对称应力扰动效应
- 并未显式求解弹性力学方程
## Related Concepts

- discrete-fracture-network
## Source Papers

- [2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio](../papers/2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio.md)
