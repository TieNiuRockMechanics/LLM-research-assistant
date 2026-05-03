---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "峰前脆性指数计算"
aliases:
  - "B_pre"
  - "brittleness index"
sources:
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
---

# 峰前脆性指数计算

## Purpose

基于应力-应变曲线，由强化模量 H 和杨氏模量 E 计算峰前脆性指数，评价热损伤对脆性的影响。
## Aliases

- B_pre
- brittleness index
## Workflow

从单轴压缩应力-应变曲线提取弹性模量 E 和峰前强化模量 H，计算 B_pre = (E-H)/H。
## Inputs

- 单轴压缩应力-应变曲线
## Outputs

- 峰前脆性指数
## Assumptions

- 岩石弹脆性行为适合此定义
## Strengths

- 简单
## Limitations

- 对曲线平滑敏感
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
