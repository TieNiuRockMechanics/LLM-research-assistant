---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "3D 打印裂隙试件制造"
aliases:
  - "3D printed fractures"
  - "三维打印裂隙样品"
sources:
  - "2018-ma-heat-transfer-by-water-flowing-through-rough-fractures-and-distribution-of-local-heat-tr"
  - "2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc"
---

# 3D 打印裂隙试件制造

## Purpose

制造具有精确预设粗糙度和几何形状的人工裂隙样品，用于流动与换热实验，确保可重复性。
## Aliases

- 3D printed fractures
- 三维打印裂隙样品
## Workflow

设计数字化粗糙裂隙模型（如给定 JRC 和隙宽）；通过 3D 打印制作模具或直接打印试件；浇铸水泥/树脂或直接使用打印件；组装形成可控裂隙进行实验。
## Inputs

- 表面粗糙度（JRC）
- 裂隙开度
- 3D 打印设备
## Outputs

- 可控粗糙度裂隙岩样
## Assumptions

- 打印精度足够反映设计粗糙度
## Strengths

- 可重复，粗糙度可控
## Limitations

- 材料可能不同于天然岩石
## Related Concepts

- joint-roughness-coefficient
## Source Papers

- [2018-ma-heat-transfer-by-water-flowing-through-rough-fractures-and-distribution-of-local-heat-tr](../papers/2018-ma-heat-transfer-by-water-flowing-through-rough-fractures-and-distribution-of-local-heat-tr.md)
- [2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc](../papers/2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc.md)
