---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "核磁共振孔隙分析 (NMR Porosimetry)"
aliases:
  - "NMR T2 spectrum"
  - "核磁共振测孔"
  - "低场核磁共振"
sources:
  - "2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones"
  - "2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma"
  - "2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm"
---

# 核磁共振孔隙分析 (NMR Porosimetry)

## Purpose

基于氢质子弛豫时间分布获取岩心孔隙尺寸分布、可动流体饱和度及束缚水体积。
## Aliases

- NMR T2 spectrum
- 核磁共振测孔
- 低场核磁共振
## Workflow

饱和流体样品，施加射频脉冲，测量 CPMG 序列回波信号，反演 T₂ 谱；利用表面弛豫模型将 T₂ 转换为孔径。
## Inputs

- 饱和流体岩样
- 低场 NMR 仪
- 表面弛豫率 ρ₂
## Outputs

- T₂ 分布
- 可动流体孔隙度
- 束缚水饱和度
- 估算渗透率
## Assumptions

- 快速扩散限域
- 表面弛豫为主
- ρ₂ 为常数
## Strengths

- 无损快速，全孔尺寸覆盖
## Limitations

- 需标定表面弛豫率
- 对顺磁性矿物敏感
## Related Concepts

- pore-structure-evolution
- thermal-damage
## Source Papers

- [2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones](../papers/2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones.md)
- [2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma](../papers/2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma.md)
- [2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm](../papers/2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm.md)
