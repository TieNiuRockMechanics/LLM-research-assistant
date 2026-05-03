---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "扫描线裂隙测量 (Scanline Survey)"
aliases:
  - "scanline survey"
sources:
  - "1984-kulatilake-sampling-bias-on-orientation-of-discontinuities"
  - "1997-genter-comparative-analysis-of-direct-core-and-indirect-borehole-imaging-tools-collection-o"
  - "2004-sisavath-geometry-percolation-and-transport-properties-of-fracture-networks-derived-from-li"
  - "2006-ortega-a-scale-independent-approach-to-fracture-intensity-and-average-spacing-measurement"
---

# 扫描线裂隙测量 (Scanline Survey)

## Purpose

沿测线记录裂隙的产状、宽度和位置，用于推算裂隙密度和间距分布。
## Aliases

- scanline survey
## Workflow

在露头或钻孔壁上布设测线，记录与测线相交的裂隙参数。
## Inputs

- 测线位置
- 罗盘、尺子或钻孔成像
## Outputs

- 裂隙频率（P10）
- 间距分布
- 产状分布
## Assumptions

- 测线垂直于优势裂隙组
- 裂隙完全穿透测线观察面
## Strengths

- 快速、成本低
## Limitations

- 一维采样，受定向偏差和尺寸偏差影响严重
- 需校正截断和删失
## Related Concepts

- orientation-bias
- truncation-bias
## Source Papers

- [1984-kulatilake-sampling-bias-on-orientation-of-discontinuities](../papers/1984-kulatilake-sampling-bias-on-orientation-of-discontinuities.md)
- [1997-genter-comparative-analysis-of-direct-core-and-indirect-borehole-imaging-tools-collection-o](../papers/1997-genter-comparative-analysis-of-direct-core-and-indirect-borehole-imaging-tools-collection-o.md)
- [2004-sisavath-geometry-percolation-and-transport-properties-of-fracture-networks-derived-from-li](../papers/2004-sisavath-geometry-percolation-and-transport-properties-of-fracture-networks-derived-from-li.md)
- [2006-ortega-a-scale-independent-approach-to-fracture-intensity-and-average-spacing-measurement](../papers/2006-ortega-a-scale-independent-approach-to-fracture-intensity-and-average-spacing-measurement.md)
