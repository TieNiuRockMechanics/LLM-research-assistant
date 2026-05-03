---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "CT 射束硬化校正 (Beam Hardening Correction, BHC)"
aliases:
  - "radial BHA curve segmentation"
  - "spline-interpolated beam hardening correction"
  - "CT射束硬化校正"
sources:
  - "2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph"
  - "2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma"
---

# CT 射束硬化校正 (Beam Hardening Correction, BHC)

## Purpose

后处理方法，用于校正 X 射线 CT 中因多色射线引起的射束硬化伪影，提高图像质量和分割精度。
## Aliases

- radial BHA curve segmentation
- spline-interpolated beam hardening correction
- CT射束硬化校正
## Workflow

方法一（径向经验分割）：在重建图像上人为划分不同相，沿径向提取衰减值建立各相特有的 BHA 衰减曲线，用指数模型拟合，构建仿真均质柱体，通过差值图像分割各相。方法二（样条迭代优化）：由专家划定认为应均匀的 ROI，定义目标函数（ROI 内 CT 数标准差），通过迭代优化一个单调递增的三次样条线性化函数，使目标函数最小后应用于全数据。
## Inputs

- CT 重建图像（或原始投影）
- 专家定义的感兴趣区
## Outputs

- 校正后 CT 图像
- 各矿物相的分割图像
## Assumptions

- 样品为圆柱体（对于方法一）
- ROI 内衰减非均匀性主要由射束硬化引起
- 其它伪影可忽略或通过 ROI 选择避开
## Strengths

- 无需先验能谱或衰减系数信息
- 可处理复杂多相样品
## Limitations

- 方法一限于圆柱体
- 方法二依赖于专家经验，主观性强
- 会增加图像噪声
## Related Concepts

- beam-hardening-artifact
## Source Papers

- [2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph](../papers/2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph.md)
- [2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma](../papers/2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma.md)
