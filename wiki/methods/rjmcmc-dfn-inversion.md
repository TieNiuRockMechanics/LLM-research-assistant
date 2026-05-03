---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于可逆跳 MCMC 的 DFN 反演 (rjMCMC Inversion)"
aliases:
  - "transdimensional inversion"
  - "跨维反演法"
  - "rjMCMC"
sources:
  - "2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity"
  - "2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin"
---

# 基于可逆跳 MCMC 的 DFN 反演 (rjMCMC Inversion)

## Purpose

一种贝叶斯推断方法，用于在裂缝数量（即模型维度）未知的情况下，从稀疏观测数据（如压力、温度、微震事件）中反演离散裂缝网络的最可能几何和水力参数。
## Aliases

- transdimensional inversion
- 跨维反演法
- rjMCMC
## Workflow

在 MCMC 采样过程中，随机在添加一条裂缝、删除一条裂缝或更新现有裂缝参数三种操作之间跳跃；利用先验信息（如钻孔揭露的裂缝方位范围）和似然函数（模拟数据与观测数据的吻合度）来驱动搜索；最终生成一系列裂缝网络的概率分布图。
## Inputs

- 动态观测数据（如热突破曲线、微震事件分布）
- 先验地质信息（如最少裂缝数、方位约束）
## Outputs

- 裂缝出现的后验概率图
- 裂缝数量和几何参数的分布
## Assumptions

- 裂缝可简化为二维线或三维多边形
- 观测误差服从高斯分布
## Strengths

- 能在数据稀缺条件下进行推断
- 能同时量化裂缝几何和水力学参数的不确定性
## Limitations

- 计算成本高
- 在裂缝密集或观测误差大时反演非唯一性很强
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity](../papers/2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity.md)
- [2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin](../papers/2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin.md)
