---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "Lambda 方法估算 JRC"
aliases:
  - "λ method for JRC"
sources:
  - "2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces"
---

# Lambda 方法估算 JRC

## Purpose

提出一个结合了剖面幅值（h/L）和考虑剪切方向的修正均方根（Z'₂）的新粗糙度指数 λ，并将其转换为 JRC，旨在改善传统仅依赖倾角的方法在预测剪切强度时的偏差。
## Aliases

- λ method for JRC
## Workflow

计算平均线并测定平均起伏高度 h；计算仅考虑正倾角的修正均方根 Z'₂；计算粗糙度指数 λ = (h/L)^α * (Z'₂)^(1-α)，α=1/3；将 λ 代入逻辑函数 JRC = 40/(1+e^{-20λ}) – 20 得到估算值。
## Inputs

- 节理剖面的二维数字化坐标
- 剖面对应的剪切方向
## Outputs

- JRC 的估算值
- JRC 的上限和下限
## Assumptions

- 剪切过程中只有正对角度的微凸体被磨损或接触
- 平均线通过“累积宽度百分比=50%”的条件唯一确定
- α=1/3 基于已发表数据集验证
## Strengths

- 同时考虑了幅值和方向效应，物理意义更全面
- 在高水平应力下的剪切强度估计比纯 Z₂ 方法更准确
## Limitations

- λ 是基于经验的指数，确定方法依赖特定网络且有不确定度
- 目前只针对二维剖面的定向粗糙度评价
## Related Concepts

- joint-roughness-coefficient
## Source Papers

- [2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces](../papers/2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces.md)
