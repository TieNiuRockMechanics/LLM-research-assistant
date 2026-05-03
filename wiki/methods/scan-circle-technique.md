---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "扫描圆技术提取钻孔成像节理粗糙度"
aliases:
  - "scan circle technique from BHTV images"
sources:
  - "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
---

# 扫描圆技术提取钻孔成像节理粗糙度

## Purpose

利用钻孔电视成像的声学或光学图像，通过扫描圆技术高效、系统地提取岩体钻孔揭露的节理表面的粗糙度系数和方向各向异性。
## Aliases

- scan circle technique from BHTV images
## Workflow

在测井软件中识别节理的正弦迹线并定义参考线；沿着代表节理面的椭圆全周长垂直参考线放置短标尺条；提取这些标尺条范围内的正弦图像并将其拉直为二维粗糙度廓线；采用分规法计算各廓线的分形维数 D；利用先前标定的 D-JRC 多项式关系计算扫描圆（全圆或半圆）的 JRC 值。
## Inputs

- 钻孔电视成像数据
- 节理的产状和位置
## Outputs

- 平均 JRC（全圆扫描）
- JRC 各向异性范围（半圆扫描）
## Assumptions

- 节理剖面可以用分形几何描述
- 扫描圆的粗糙度能代表整个节理面的平均粗糙度
- 钻孔直径内的粗糙度信息能够外推反映更大尺度的粗糙度
## Strengths

- 高效，可批量化处理大量钻孔数据
- 能提供节理粗糙度的方向各向异性信息
## Limitations

- 受限于钻孔直径，只能表征小尺寸节理的粗糙度
- 高倾角节理可能出现图像错位
- JRC 与力学行为的关联是间接的（未与直接剪切试验标定）
## Related Concepts

- joint-roughness-coefficient
- fractal-dimension
## Source Papers

- [2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to](../papers/2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to.md)
