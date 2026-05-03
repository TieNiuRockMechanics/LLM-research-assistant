---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "瞬态脉冲渗透率测试 (Transient Pulse Permeability)"
aliases:
  - "pulse-decay method"
  - "transient permeability test"
sources:
  - "2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto"
---

# 瞬态脉冲渗透率测试 (Transient Pulse Permeability)

## Purpose

测量低渗透岩石的气体/液体渗透率，通过上游压力衰减速率计算。
## Aliases

- pulse-decay method
- transient permeability test
## Workflow

上游充气至给定压力，打开阀门，记录上下游压力随时间变化，通过解析或数值拟合求解渗透率。
## Inputs

- 上下游压力
- 试样尺寸
- 气体粘度
## Outputs

- 渗透率 k
## Assumptions

- 等温
- 达西流
- 克林肯伯格效应可忽略或已校正
## Strengths

- 适用于超低渗岩石，测试时间相对较短
## Limitations

- 需要精确压力传感器
## Related Concepts

- permeability
## Source Papers

- [2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto](../papers/2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto.md)
