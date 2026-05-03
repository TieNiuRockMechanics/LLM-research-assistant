---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "地震接收函数偏移成像 (Seismic Receiver Function Migration)"
aliases:
  - "Seismic Receiver Function Migration"
  - "CCP stacking"
sources:
  - "2012-zhu-destruction-of-the-north-china-craton"
  - "2011-zhu-timing-scale-and-mechanism-of-the-destruction-of-the-north-china-craton"
---

# 地震接收函数偏移成像 (Seismic Receiver Function Migration)

## Purpose

通过密集地震台阵记录的远震体波波形，提取 P-S 转换波（接收函数），并对其进行共转换点偏移 (CCP stacking) 成二维或三维图像，用于高精度揭示地壳和上地幔的间断面（如莫霍面、岩石圈-软流圈界面）的深度与形态。
## Aliases

- Seismic Receiver Function Migration
- CCP stacking
## Workflow

对密集台阵记录的远震数据进行预处理和质量筛选；从记录的 P 波尾波中提取并分离 P-S 转换震相，得到径向-切向接收函数；利用已知的速度模型（如 IASP91）进行时深转换，将各台站的接收函数反投影到对应的地下转换点位置；进行共转换点叠加和偏移成像。
## Inputs

- 密集地震台阵记录的远震三分量波形数据
- 参考的一维或三维速度模型
## Outputs

- 地壳和上地幔间断面的二维或三维深度与振幅图像
## Assumptions

- 远震 P 波可近似看作入射到台站下方的平面波
- 接收到的能量变化主要来源于速度界面处的 P-S 模式转换
- 参考速度模型可基本反映研究区平均速度结构
## Strengths

- 能提供高分辨率的岩石圈结构图像，特别是在密集台阵下
## Limitations

- 成像分辨率受限于台站间距和频率
- 对台站左侧横向剧烈的速度不均一性会产生成像偏差
- 复杂地壳结构下多路径和散射效应会降低数据质量
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2012-zhu-destruction-of-the-north-china-craton](../papers/2012-zhu-destruction-of-the-north-china-craton.md)
- [2011-zhu-timing-scale-and-mechanism-of-the-destruction-of-the-north-china-craton](../papers/2011-zhu-timing-scale-and-mechanism-of-the-destruction-of-the-north-china-craton.md)
