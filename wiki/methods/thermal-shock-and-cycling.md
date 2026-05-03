---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "热冲击与循环热处理实验"
aliases:
  - "heating-cooling cycle treatment"
  - "HWCT"
  - "quenching experiment"
  - "water cooling test"
  - "LN2 cooling"
  - "冷热循环"
  - "淬火实验"
  - "液氮冷却"
sources:
  - "2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles"
  - "2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te"
  - "2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss"
  - "2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties"
  - "2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther"
  - "2023-wu-effect-of-cooling-methods-on-mechanical-behaviors-and-thermal-damage-distributions-of-gr"
  - "2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under"
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
  - "2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected"
  - "2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica"
---

# 热冲击与循环热处理实验

## Purpose

模拟地热储层或工程中反复冷热交替对岩石物理力学性质的劣化效应。包括缓慢冷却和快速急冷（水冷、液氮）。
## Aliases

- heating-cooling cycle treatment
- HWCT
- quenching experiment
- water cooling test
- LN2 cooling
- 冷热循环
- 淬火实验
- 液氮冷却
## Workflow

将试样以一定速率（如 5 °C/min）加热至目标温度（100–1000 °C），恒温一定时间；然后根据实验设计采用空气自然冷却、浸水急冷或液氮冷却；可重复该加热-冷却循环。测量处理前后的波速、强度、渗透率、孔隙度等变化。
## Inputs

- 加热温度
- 冷却介质（空气、水、液氮）
- 循环次数
## Outputs

- 质量损失率
- 体积膨胀率
- P 波速度降幅
- 单轴抗压强度衰减
- 渗透率增幅
- 裂隙密度
## Assumptions

- 升温足够平稳以避免额外热梯度损伤
- 冷却介质体积足够大以维持恒定温度
## Strengths

- 能有效再现热冲击累积损伤
- 实验周期相对较短
## Limitations

- 多为室内小尺度，难以模拟真实地应力场影响
- 冷却速率受设备与操作影响
- 忽略化学作用
## Related Concepts

- thermal-damage
- heating-cooling-cycle
- cyclic-thermal-shock
## Source Papers

- [2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles](../papers/2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles.md)
- [2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te](../papers/2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te.md)
- [2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss](../papers/2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss.md)
- [2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties](../papers/2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties.md)
- [2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther](../papers/2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther.md)
- [2023-wu-effect-of-cooling-methods-on-mechanical-behaviors-and-thermal-damage-distributions-of-gr](../papers/2023-wu-effect-of-cooling-methods-on-mechanical-behaviors-and-thermal-damage-distributions-of-gr.md)
- [2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under](../papers/2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
- [2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected](../papers/2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected.md)
- [2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica](../papers/2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica.md)
