---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "非参数方向-线性核密度估计"
aliases:
  - "Directional-linear KDE"
sources:
  - "2023-g-mez-a-non-parametric-discrete-fracture-network-model"
---

# 非参数方向-线性核密度估计

## Purpose

联合估计裂缝走向（或倾向/倾角）与迹线长度的概率密度函数，无需预设数据服从特定参数分布。
## Aliases

- Directional-linear KDE
## Workflow

使用 von Mises-Fisher 核函数描述方向数据、高斯核函数描述长度数据（经对数变换）；通过带宽选择器优化平滑程度；从估计出的联合密度函数中可直接采样用于生成 DFN 模型。
## Inputs

- 野外实测的裂缝产状和迹长数据集
## Outputs

- 方向-长度的联合概率密度函数
- 随机生成的裂缝样本
## Assumptions

- 观测数据是真实分布的代表性样本
- 方向与尺寸相互独立
## Strengths

- 可灵活处理多模态或复杂分布
- 无预设分布假设
## Limitations

- 最优带宽选择困难（尤其多模态方向）
- 需要较大样本量
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2023-g-mez-a-non-parametric-discrete-fracture-network-model](../papers/2023-g-mez-a-non-parametric-discrete-fracture-network-model.md)
