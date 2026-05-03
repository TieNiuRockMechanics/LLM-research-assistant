---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "水压致裂地应力测量"
aliases:
  - "hydrofracturing"
  - "HF stress measurement"
sources:
  - "1967-haimson-initiation-and-extension-of-hydraulic-fractures-in-rocks"
  - "1976-raleigh-the-rangely-field-an-experiment-in-earthquake-control-at-rangely-colorado"
  - "1996-genter-analysis-of-macroscopic-fractures-in-granite-in-the-hdr-geothermal-well-eps-1-soultz"
---

# 水压致裂地应力测量

## Purpose

直接测定深部绝对应力大小和方向。
## Aliases

- hydrofracturing
- HF stress measurement
## Workflow

封隔钻孔段，注水加压至岩石张裂，记录破裂压力、重张压力和关闭压力，推算最小水平主应力及方向。
## Inputs

- 封隔器
- 高压泵
- 压力传感器
## Outputs

- 最小水平主应力 S_hmin
- 最大水平主应力方向（通过印模或钻孔成像确定）
## Assumptions

- 垂直方向为主应力方向之一
- 岩石是均质、各向同性、线弹性
- 关闭压力等于 S_hmin
## Strengths

- 深部直接测量
- 可重复
## Limitations

- 成本高
- 解释需假设
- 深孔中方向获取困难
## Related Concepts

- in-situ-stress
- effective-stress
## Source Papers

- [1967-haimson-initiation-and-extension-of-hydraulic-fractures-in-rocks](../papers/1967-haimson-initiation-and-extension-of-hydraulic-fractures-in-rocks.md)
- [1976-raleigh-the-rangely-field-an-experiment-in-earthquake-control-at-rangely-colorado](../papers/1976-raleigh-the-rangely-field-an-experiment-in-earthquake-control-at-rangely-colorado.md)
- [1996-genter-analysis-of-macroscopic-fractures-in-granite-in-the-hdr-geothermal-well-eps-1-soultz](../papers/1996-genter-analysis-of-macroscopic-fractures-in-granite-in-the-hdr-geothermal-well-eps-1-soultz.md)
