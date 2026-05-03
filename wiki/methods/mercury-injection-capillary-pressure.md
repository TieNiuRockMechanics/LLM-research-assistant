---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "高压压汞法 (Mercury Injection Capillary Pressure, MICP)"
aliases:
  - "MICP"
  - "Mercury injection"
  - "压汞法"
sources:
  - "2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones"
---

# 高压压汞法 (Mercury Injection Capillary Pressure, MICP)

## Purpose

测量致密岩石的孔喉尺寸分布、排驱压力和总孔隙率。
## Aliases

- MICP
- Mercury injection
- 压汞法
## Workflow

将汞注入抽真空样品，记录压力与进汞量，利用 Washburn 方程转换为孔径分布。
## Inputs

- 进汞压力-体积数据
- 接触角
- 表面张力
## Outputs

- 孔喉半径分布
- 排驱压力 Pd
- 阈值压力
- 分选系数
## Assumptions

- 圆柱形毛细管模型
- 界面参数恒定
## Strengths

- 可覆盖纳米至微米孔喉
## Limitations

- 高压可能损伤岩心
- 无法区分孔与喉
## Related Concepts

- porosity
- pore-structure
## Source Papers

- [2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones](../papers/2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones.md)
