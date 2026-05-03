---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "激光闪光法 (Laser Flash Analysis, LFA)"
aliases:
  - "LFA"
  - "激光闪射法"
sources:
  - "2017-kant-thermal-properties-of-central-aare-granite-for-temperatures-up-to-500-c-irreversible-c"
---

# 激光闪光法 (Laser Flash Analysis, LFA)

## Purpose

测量固体材料的热扩散系数，通过记录背面温升对脉冲激光的响应。
## Aliases

- LFA
- 激光闪射法
## Workflow

对薄盘试样正面发射激光脉冲，红外探测器记录背面温升，计算半温升时间 t1/2，按 α=0.1388 d²/t1/2 求得热扩散率。
## Inputs

- 激光能量
- 试样厚度
## Outputs

- 热扩散率 α
- 比热（需参比）
- 导热系数（计算）
## Assumptions

- 一维热传导
- 绝热边界
## Strengths

- 高精度
## Limitations

- 需要涂层保证吸收/发射
- 非透明试样适用性有限
## Related Concepts

- thermal-diffusivity
## Source Papers

- [2017-kant-thermal-properties-of-central-aare-granite-for-temperatures-up-to-500-c-irreversible-c](../papers/2017-kant-thermal-properties-of-central-aare-granite-for-temperatures-up-to-500-c-irreversible-c.md)
