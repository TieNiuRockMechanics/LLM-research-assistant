---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "热循环作用下岩石损伤累积与饱和规律"
sources:
  - "2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected"
  - "2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica"
  - "2021-li-factors-affecting-pore-structure-of-granite-under-cyclic-heating-and-cooling-a-nuclear-m"
  - "2021-pai-an-investigation-on-the-deterioration-of-physical-and-mechanical-properties-of-granite"
  - "2020-zhao-exploratory-experimental-study-on-the-mechanical-properties-of-granite-subjected-to-cy"
  - "2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles"
  - "2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te"
  - "2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss"
  - "2022-ge-thermal-damage-and-mechanical-properties-of-high-temperature-sandstone-with-cyclic-heati"
  - "2024-harshini-australia-s-geothermal-frontier-unlocking-granite-s-energy-secrets"
  - "2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm"
  - "2023-zhu-a-comprehensive-review-on-mechanical-responses-of-granite-in-enhanced-geothermal-system"
---

# 热循环作用下岩石损伤累积与饱和规律

## Central Question

多次热-冷循环如何导致花岗岩和砂岩物理力学性质劣化？劣化速率和饱和趋势受哪些因素控制？
## Synthesis

循环加热-急冷实验表明，损伤主要在前5-10次循环内快速累积，随后增速趋缓甚至饱和。P波速度、孔隙度、强度等参数可用指数或对数函数拟合；抗拉强度对循环热损伤最敏感。首次冲击造成的裂纹网络为后续循环提供了应力释放空间，导致热应力水平下降（Kaiser效应）。当温度超过阈值（如>500°C）时，矿物相变和严重热失配可能导致损伤重新加速。这些规律为地热储层长期运营提供了评估依据。
## Evidence Chain

- 不同循环次数 (0–35 次) 对比实验 (Rong 2021; Junique 2021; Li 2021)
- 孔隙度、波速、AE 监测 (Pai 2021; Zhao 2020)
- NMR 与 CT 微结构变化追踪
- 2021-yu-mechanical-test, 2021-zhang-macroscopic-and-microscopic, 2023-cui-experimental-investigation均记录了花岗岩或砂岩在P波速度、强度随循环次数的前期剧降和后期趋缓。
- 2022-ge-thermal-damage和2022-cao-damage-deterioration研究长周期或高温水冷循环，指出在>600°C后，经典饱和趋势可能被打破，劣化重新加速。
- 2022-ge-thermal-damage引入的‘弹性核’概念提供了一个物理模型，解释了为何前期损伤集中于表面并逐步向内推进。
- Harshini (2024) 对 Harcourt 花岗岩 900 °C 循环 5 次发现强度首次降 55%，后续降速减缓。
- Xi (2024) 核磁共振显示孔隙度增长在 0–2 次循环达 133%，2–6 次仅 11.6%。
- Zhu (2023) 综述统计多组循环数据，证实前 5 次循环主导了劣化。
## Disagreements / Tensions

- 少数研究观察到 10 次循环后仍有缓慢劣化，可能与加热温度和冷却速率有关。
- 热强化现象（如 200–300 °C 时 UCS 短暂上升）在不同循环次数中也可能出现。
- 关于饱和循环数的界定：12 次、15 次或 20 次不等，取决于岩石类型和温度。
## Boundary Conditions

- 循环温度固定 (通常在 300–500 °C)，急冷介质为水或液氮；实验室无围压或低围压
- 升温速率 5–10 °C/min，保温 2–4 h
- 验证了花岗岩、砂岩；其他岩性数据不足
## Writing Uses

- 为干热岩储层寿命评估和循环注水方案优化提供依据
- 设计数值模型时简化损伤演化规律，只需考虑前几个循环即可
- 解释现场多次压裂后产能递减的内在物理原因
## Source Papers

- [2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected](../papers/2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected.md)
- [2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica](../papers/2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica.md)
- [2021-li-factors-affecting-pore-structure-of-granite-under-cyclic-heating-and-cooling-a-nuclear-m](../papers/2021-li-factors-affecting-pore-structure-of-granite-under-cyclic-heating-and-cooling-a-nuclear-m.md)
- [2021-pai-an-investigation-on-the-deterioration-of-physical-and-mechanical-properties-of-granite](../papers/2021-pai-an-investigation-on-the-deterioration-of-physical-and-mechanical-properties-of-granite.md)
- [2020-zhao-exploratory-experimental-study-on-the-mechanical-properties-of-granite-subjected-to-cy](../papers/2020-zhao-exploratory-experimental-study-on-the-mechanical-properties-of-granite-subjected-to-cy.md)
- [2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles](../papers/2021-yu-mechanical-test-of-granite-with-multiple-water-thermal-cycles.md)
- [2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te](../papers/2021-zhang-macroscopic-and-microscopic-experimental-research-on-granite-properties-after-high-te.md)
- [2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss](../papers/2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss.md)
- [2022-ge-thermal-damage-and-mechanical-properties-of-high-temperature-sandstone-with-cyclic-heati](../papers/2022-ge-thermal-damage-and-mechanical-properties-of-high-temperature-sandstone-with-cyclic-heati.md)
- [2024-harshini-australia-s-geothermal-frontier-unlocking-granite-s-energy-secrets](../papers/2024-harshini-australia-s-geothermal-frontier-unlocking-granite-s-energy-secrets.md)
- [2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm](../papers/2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm.md)
- [2023-zhu-a-comprehensive-review-on-mechanical-responses-of-granite-in-enhanced-geothermal-system](../papers/2023-zhu-a-comprehensive-review-on-mechanical-responses-of-granite-in-enhanced-geothermal-system.md)
