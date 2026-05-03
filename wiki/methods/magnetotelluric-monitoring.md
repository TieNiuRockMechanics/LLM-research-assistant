---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "大地电磁监测 (Magnetotelluric Monitoring)"
aliases:
  - "MT monitoring"
  - "Magnetotelluric"
sources:
  - "2017-thiel-electromagnetic-monitoring-of-hydraulic-fracturing-relationship-to-permeability-seism"
---

# 大地电磁监测 (Magnetotelluric Monitoring)

## Purpose

通过地表/井中布置的电磁台站测量天然场源，监测注水引起的电阻率变化以推断裂缝网络发展和流体运移。
## Aliases

- MT monitoring
- Magnetotelluric
## Workflow

采集压裂前后电磁时间序列；计算阻抗张量和相位张量；进行三维反演或概率反演提取电阻率变化；关联流体羽状体。
## Inputs

- 电场/磁场时间序列
- 地质电阻率模型
## Outputs

- 视电阻率变化图
- 相位残差张量方向
- 流体羽状体后验分布
## Assumptions

- 上覆地层电阻率不变
- 流体电阻率低于围岩
## Strengths

- 对深部裂缝连通性敏感
## Limitations

- 沉积盖层屏蔽效应
- 测量噪声影响
## Related Concepts

- percolation-threshold
- induced-seismicity
## Source Papers

- [2017-thiel-electromagnetic-monitoring-of-hydraulic-fracturing-relationship-to-permeability-seism](../papers/2017-thiel-electromagnetic-monitoring-of-hydraulic-fracturing-relationship-to-permeability-seism.md)
