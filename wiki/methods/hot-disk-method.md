---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "Hot Disk 瞬态平面热源法"
aliases:
  - "TPS method"
  - "Hot Disk transient plane source method"
sources:
  - "2019-sun-effect-of-high-temperatures-on-the-thermal-properties-of-granite"
---

# Hot Disk 瞬态平面热源法

## Purpose

同时测量岩石的导热系数和热扩散率，用于评估热性质劣化。
## Aliases

- TPS method
- Hot Disk transient plane source method
## Workflow

将平面热源夹在两块平整洁净试样之间，施加恒定功率，记录温升曲线，通过拟合解析模型求解导热系数和热扩散率。
## Inputs

- 加热功率
- 试样厚度
## Outputs

- 导热系数
- 热扩散率
- 体积比热
## Assumptions

- 试样均质
- 接触良好
## Strengths

- 快速，一次测多参数
## Limitations

- 对表面平整度要求高
## Related Concepts

- thermal-conductivity
## Source Papers

- [2019-sun-effect-of-high-temperatures-on-the-thermal-properties-of-granite](../papers/2019-sun-effect-of-high-temperatures-on-the-thermal-properties-of-granite.md)
