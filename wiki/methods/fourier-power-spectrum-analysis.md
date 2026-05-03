---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "傅里叶功率谱分析 (Fourier Power Spectrum Analysis of Fault Roughness)"
aliases:
sources:
  - "2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales"
---

# 傅里叶功率谱分析 (Fourier Power Spectrum Analysis of Fault Roughness)

## Purpose

通过计算断层表面或地震破裂迹线的一维功率谱，定量分析其多尺度的自仿射粗糙度特征，提取 Hurst 指数和前置因子。
## Aliases

- not-confirmed-from-current-pages
## Workflow

使用 LiDAR 或激光轮廓仪获取断层表面高程数据，沿滑移和垂直滑移方向提取一维曲线；去趋势并加窗后计算傅里叶功率谱 P(k)，在对数坐标下拟合 P(k)∝k^{-1-2H} 得到 Hurst 指数 H。
## Inputs

- 断层表面或破裂迹线的高程数据（点云）
## Outputs

- 沿特定方向的 Hurst 指数 H
- 前置因子幅值 C
## Assumptions

- 断层表面在跨越几个量级上被假设为各向异性自仿射分形
- 去趋势和加窗过程对功率谱没有显著偏差
## Strengths

- 能处理从微米到公里九个数量级的数据集
- 清晰量化断层各向异性特征
## Limitations

- 米级中间尺度的数据缺失（“数据空白”）
- 对谱处理和配准参数敏感
## Related Concepts

- self-affine-roughness
## Source Papers

- [2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales](../papers/2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales.md)
