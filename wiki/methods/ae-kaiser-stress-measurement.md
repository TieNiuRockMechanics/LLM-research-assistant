---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "声发射 Kaiser 效应地应力测量"
aliases:
  - "AE method"
  - "Kaiser effect stress measurement"
sources:
  - "2004-li-北京房山花岗岩原地应力状态-ae-法估计"
---

# 声发射 Kaiser 效应地应力测量

## Purpose

利用岩石的 Kaiser 效应从定向岩芯估计原地应力大小和方向。
## Aliases

- AE method
- Kaiser effect stress measurement
## Workflow

在室内对定向岩芯施加单轴压力，通过重复加载差法识别 Kaiser 点，再通过多方向试件的最小二乘解得到应力张量。
## Inputs

- 定向岩芯
- 声发射传感器
## Outputs

- 原地应力大小和方向
## Assumptions

- Kaiser 效应仅响应历史最大压应力
- 实验室短期加载与地质长期作用等价
- 一个主应力垂直
## Strengths

- 室内测试，无需深孔操作
## Limitations

- Kaiser 点识别有时不明显，需重复加载
- 仅适用于硬岩
- 试件制备要求高
## Related Concepts

- ae-kaiser-effect
- in-situ-stress
## Source Papers

- [2004-li-北京房山花岗岩原地应力状态-ae-法估计](../papers/2004-li-北京房山花岗岩原地应力状态-ae-法估计.md)
