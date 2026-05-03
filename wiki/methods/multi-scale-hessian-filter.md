---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "多尺度 Hessian 裂隙滤波 (Multi‑scale Hessian Fracture Filter, MSHFF)"
aliases:
  - "MSHFF"
sources:
  - "2014-voorn-porosity-permeability-and-3d-fracture-network-characterisation-of-dolomite-reservoir"
---

# 多尺度 Hessian 裂隙滤波 (Multi‑scale Hessian Fracture Filter, MSHFF)

## Purpose

一种针对三维 CT 图像的图像增强与分割算法，专门用于检测和增强狭窄（亚体素）的裂隙或裂缝信号。
## Aliases

- MSHFF
## Workflow

在不同高斯平滑尺度 σ 下计算图像 Hessian 矩阵，根据特征值构建局部结构（板状、线状）的相似度函数；将不同尺度的相似度进行融合（如取最大值）；对增强后图像应用全局阈值分割出裂隙/孔隙体素；去除小尺寸噪声。
## Inputs

- 三维 CT 体数据
## Outputs

- 二值化的裂隙/孔隙分割掩膜
## Assumptions

- 图像噪声水平低，裂隙与基质有足够对比度
- 目标裂隙宽度位于所选高斯尺度范围内
- 裂隙可被建模为局部板状结构
## Strengths

- 能增强和检测宽度接近甚至低于分辨率的窄裂隙
- 对管状、片状结构的区分度较好
## Limitations

- 计算量大，耗时耗内存
- 阈值选择对分割结果敏感
- 对充填物或密度差小的裂隙无效
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2014-voorn-porosity-permeability-and-3d-fracture-network-characterisation-of-dolomite-reservoir](../papers/2014-voorn-porosity-permeability-and-3d-fracture-network-characterisation-of-dolomite-reservoir.md)
