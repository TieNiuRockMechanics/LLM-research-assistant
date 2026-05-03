---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "多方向 JRC 各向异性测量与椭圆拟合"
aliases:
  - "multi-direction JRC measurement"
  - "ellipse fitting for JRC direction"
sources:
  - "2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using"
---

# 多方向 JRC 各向异性测量与椭圆拟合

## Purpose

在多个方向（如 18 个方向）上提取节理轮廓线计算 JRC，并通过最小二乘椭圆拟合确定最大/最小 JRC 值及其方向，全面分析粗糙度各向异性。
## Aliases

- multi-direction JRC measurement
- ellipse fitting for JRC direction
## Workflow

固定点云网格（如 0.1 mm），每隔一定角度（如 10°）提取一条轮廓线；用 Li & Zhang 公式计算每个方向的 JRC；将方向角与 JRC 值转为笛卡尔坐标，进行最小二乘椭圆拟合，提取半轴长度和方向。
## Inputs

- 节理点云
- 轮廓参数
## Outputs

- 方向性 JRC 序列
- 最大 JRC 值及方向
- 最小 JRC 值
## Assumptions

- Li & Zhang 公式不受采样间距影响
- JRC 各向异性可用椭圆近似
## Strengths

- 全面评估各向异性
## Limitations

- 仅有限方向可能遗漏细节
- 非线性强时椭圆拟合偏差大
## Related Concepts

- joint-roughness-coefficient
## Source Papers

- [2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using](../papers/2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using.md)
