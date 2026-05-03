---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-li-experimental-studies-on-the-effect-of-cyclic-thermal-shock-and-cooling-methods-on-the-me"
title: "Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone."
status: "draft"
source_pdf: "data/papers/2022 - Experimental studies on the effect of cyclic thermal shock and cooling methods on the mechanical properties and fracture behavior of prefabricated fissured sandstone.pdf"
collections:
citation: "Li, Man, et al. \"Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone.\" *Theoretical and Applied Fracture Mechanics*, vol. 122, 2022, art. 103576. doi:10.1016/j.tafmec.2022.103576. Accessed 2026."
indexed_texts: "15"
indexed_chars: "71404"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:28:16"
---

# Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone.

## One-line Summary
研究循环热冲击次数和冷却方式（空气及不同温度水冷）对含预制裂隙砂岩力学性质和断裂行为的影响，发现峰值应力和弹性模量随冲击次数指数衰减，首次热冲击劣化最严重，水冷损害远大于空冷且水温越低损伤越显著，并提出了综合考虑冲击次数和水温的损伤经验公式。[Li 2022, pp. 1-2, 5-7, 7-7]

## Research Question
热冲击次数和冷却方式如何影响含单一预制裂隙砂岩的力学性质与断裂行为？如何定量评价地热储层砂岩在循环热冲击和不同冷却条件下的损伤演化？[Li 2022, pp. 1-2, 2-3]

## Study Area / Data
实验材料取自重庆九龙坡区的储层砂岩，整体均匀、无明显缺陷，密度为 2450 kg/m³。XRD 分析表明主要矿物组成为石英 40.90%、长石 24.92%、方解石 10.82%、粘土矿物 22.36%。按 ISRM 标准制备直径 50 mm、高 100 mm 的标准圆柱试样，并通过水射流切割技术预制一条与水平方向成 45° 倾角的单一裂隙。[Li 2022, pp. 2-3, 3-4]

## Methods
对含预制裂隙砂岩进行循环热冲击和单轴压缩试验。所有试样在马弗炉中以 5°C/min 升温至 400°C 并保温 2 小时，随后分别进行空气冷却（约 3 小时冷至室温）和蒸馏水冷却（水温 20°C、50°C、80°C，约 10 分钟冷透）。每种冷却方式下设置热冲击次数 1、4、8 次，另设未热冲击（0 次）组作为对照。试验前后测量 P 波速度，单轴压缩获取完整应力‑应变曲线，计算峰值应力和弹性模量，并观察试样表面裂纹及破坏模式。在 COMSOL Multiphysics 中模拟热冲击过程的温度场和应力场，用于分析传热系数与冷却水温的影响。[Li 2022, pp. 1-2, 2-3, 3-4, 4-5]

## Key Findings
1.  随着热冲击次数增加，裂隙砂岩 P 波速度逐渐降低；水冷下降幅度大于空冷，且水温越低降幅越大。8 次热冲击后，空冷、80°C 水冷、50°C 水冷、20°C 水冷下的 P 波速度分别降低 7.55%、15.99%、29.01%、33.71% [Li 2022, pp. 4-5]。
2.  峰值应力和弹性模量随热冲击次数呈良好的指数函数关系下降（R²>0.960）。首次热冲击对力学性质劣化最严重，超过 4 次后劣化显著减缓，峰值应力趋于恒定 [Li 2022, pp. 5-7]。
3.  与空气冷却相比，水冷却引起更大的力学性质衰退；冷却水温越低，热冲击效应越剧烈，损伤越显著 [Li 2022, pp. 1-2, 5-7]。
4.  提出一个同时考虑热冲击次数 N 和冷却水温 T 的损伤经验公式：D_E1 = (−0.001 T + 0.462) exp(0.057 N)，决定系数 R² = 0.945 [Li 2022, pp. 7-7]。
5.  热冲击后宏观裂纹观察显示，空冷下试样表面几乎无宏观裂纹；水冷后出现三类裂纹（不存在、少、多），低温和多次冲击下裂纹数量增多。单轴压缩过程中裂纹扩展分阶段，出现翼裂纹、反翼裂纹、剪切裂纹和拉剪混合裂纹，低水温和大冲击次数下试样表面剥落更广泛 [Li 2022, pp. 7-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| P 波速度随热冲击次数增加而降低；8 次后空冷降 7.55%，20°C 水冷降 33.71% | [Li 2022, pp. 4-5] | 含 45° 裂隙砂岩，加热至 400°C，不同冷却方式 | 水冷下降远大于空冷，水温越低下降越大 |
| 峰值应力、弹性模量与热冲击次数呈指数函数关系，R²>0.960；首次冲击后下降幅度最大 | [Li 2022, pp. 5-7] | 单轴压缩试验 | 首次冲击降幅占 8 次总降幅的 56%~74%（依冷却方式）；超过 4 次后趋于平缓 |
| 首次热冲击引起的峰值应力下降比例：空冷 63%，80°C 水冷 56%，50°C 水冷 74%，20°C 水冷 62% | [Li 2022, pp. 5-7] | 以第 8 次冲击时的值为基准 | 首次冲击造成的劣化占主要部分，水温效应并非单调，但整体低温损害更大 |
| 损伤经验公式 D_E1 = (−0.001T+0.462) exp(0.057N)，R²=0.945 | [Li 2022, pp. 7-7] | T 为冷却水温 (°C)；N 为热冲击次数；基于弹性模量损伤定义 | 适用于地热储层类似砂岩加热至 400°C 的情况 |
| 空冷后试样表面无宏观裂纹；水冷后出现分为不存在、少、多三类裂纹，低温和多次冲击下裂纹增多 | [Li 2022, pp. 7-7] | 热冲击后、加载前观察 | 80°C 水冷 1 次属“不存在”裂纹 |
| 加载过程中裂纹扩展分三阶段，出现翼裂纹（T3）、反翼裂纹、剪切裂纹（S1）、拉剪混合裂纹（TS），低水温和大冲击次数下剥落更严重 | [Li 2022, pp. 7-9] | 定性观察 | 为粗略定性分析，未定量描述 |

## Limitations
- 未从索引片段中确认试验的统计显著性检验和每组的平行试样数量。
- 破坏模式和表面裂纹分布仅为粗略定性分析，未进行定量表征 [Li 2022, pp. 7-9]。
- 数值模拟部分的温度场、应力场具体分布和验证数据在片段中未详细呈现 [Li 2022, pp. 2-3, 4-5]。
- 未涉及其他裂隙倾角、裂隙长度或多裂隙分布等几何参数的影响。
- 加热温度固定为 400°C，未考虑不同目标温度（例如接近石英相变温度 573°C 或方解石分解温度）的对比。

## Assumptions / Conditions
- **实验条件**：所有试样均加热至 400°C，升温速率 5°C/min，保温 2h；冷却介质为空气（自然冷却约 3h）或设定温度的蒸馏水（快速冷却约 10min）。裂隙倾角固定为 45° [Li 2022, pp. 3-4]。
- **损伤定义**：损伤变量 D_E1 基于弹性模量的变化定义，隐含材料损伤各向同性和模量退化的等效表征 [Li 2022, pp. 7-7]。
- **数值模拟**：假设岩石为连续介质，利用 COMSOL Multiphysics 求解传热与热应力耦合，并认为传热系数是影响热冲击强度的关键因素 [Li 2022, pp. 2-3, 4-5]。

## Key Variables / Parameters
- 热冲击次数 N（0, 1, 4, 8）
- 冷却方式：空气（室温约 20°C）、水温 T = 20°C、50°C、80°C
- P 波速度（m/s）
- 峰值应力（MPa）
- 弹性模量（GPa）
- 损伤变量 D_E1（基于弹性模量）
- 经验公式拟合参数 p, q, λ [Li 2022, pp. 7-7]
- 矿物成分含量（石英 40.90%，长石 24.92%，方解石 10.82%，粘土矿物 22.36%） [Li 2022, pp. 2-3]
- 预制裂隙倾角 β = 45° [Li 2022, pp. 2-3]

## Reusable Claims
1. 含 45° 裂隙砂岩在 400°C 加热后的循环热冲击下，峰值应力和弹性模量随热冲击次数呈指数衰减，首次冲击造成的劣化占总损伤的主要部分；当冲击次数超过 4 次后，力学性质劣化变得不显著。**条件**：空气或水冷却，单轴压缩。**限制**：仅针对该特定砂岩和裂隙几何，对其他岩性或裂隙配置需额外验证。[Li 2022, pp. 5-7]
2. 水冷却对该砂岩的损伤效果远大于空气冷却，且冷却水温越低，力学参数下降越剧烈。**证据**：8 次冲击后 20°C 水冷下 P 波速度下降 33.71%，而空冷仅 7.55%；峰值应力和弹性模量的变化趋势一致。**限制**：结论基于 400°C 加热和该矿物组分的砂岩。[Li 2022, pp. 4-5, 5-7]
3. 损伤经验模型 D_E1 = (−0.001T + 0.462) e^(0.057N) 可用来评估类似储层砂岩在循环热冲击和不同冷却水温下的损伤程度，拟合优度 R²=0.945。**条件**：砂岩加热至 400°C，T 为冷却水温 (°C)，N 为热冲击次数。**限制**：需在更广泛的温度和循环次数下验证，且未考虑升温阶段的影响。[Li 2022, pp. 7-7]

## Candidate Concepts
[[cyclic thermal shock]], [[prefabricated fissured sandstone]], [[geothermal energy]], [[thermal storage system]], [[mechanical properties degradation]], [[thermal cracking]], [[P-wave velocity]], [[damage variable]], [[cooling method]], [[water cooling vs air cooling]], [[fracture behavior]], [[wing crack]], [[shear crack]], [[spalling]], [[COMSOL Multiphysics simulation]], [[thermal stress]]

## Candidate Methods
[[uniaxial compression test]], [[cyclic thermal shock experiment]], [[water jet cutting]], [[muffle furnace heating]], [[P-wave velocity measurement]], [[empirical damage formula]], [[COMSOL thermomechanical simulation]], [[XRD analysis]]

## Connections To Other Work
- 片段中引用前人工作：Brotóns et al. 发现水冷使热处理石灰岩力学参数下降大于空冷；Kim et al. 通过 ANSYS 模拟指出热冲击在试样外表产生拉应力导致微裂纹；Shao et al. 提到粗粒花岗岩更易热开裂；Kumari et al. 发现热冲击增加花岗岩裂纹密度，水冷影响大于空冷；Liu et al. 研究了热循环和水‑热循环下砂岩性质变化 [Li 2022, pp. 2-2]。这些均被作者作为研究背景引用，但未从索引片段中确认其确切文献信息。
- 从研究主题可连接到 [[thermal damage in geothermal reservoirs]]、[[fractured rock mechanics]]、[[rapid cooling effect on rock strength]]、[[experimental rock mechanics]] 等方面的工作。

## Open Questions
- 不同预制裂隙倾角（如 0°、30°、60°）或裂隙长度、多条裂隙对热冲击下力学劣化和断裂行为的影响，未在片段中涉及。
- 加热温度高于 400°C（例如接近石英相变 573°C 或方解石分解温度）时的热冲击响应是否遵循类似的指数衰减规律，未从片段中确认。
- 超过 8 次热冲击的长期循环下，力学性质是否继续衰减或达到完全稳定的临界值，片段中仅观察到 4 次后趋缓，更长期行为未验证。
- 数值模拟得到的温度场和应力场与实验裂纹分布的定量对比未见报道，无法判断模拟的预测精度。

## Source Coverage
本页内容依据论文的 15 个索引片段，主要覆盖了摘要、引言、样品制备、热冲击步骤、部分结果（P 波速度、应力‑应变曲线、损伤公式、破坏模式定性描述）以及试验数据表等。片段偏向方法介绍和关键结果展示，对深入讨论、数值模拟的详细结果、裂纹定量分析（如裂纹长度、密度）以及可能存在的局限性讨论等信息可能缺失。因此，本页无法呈现论文的完整讨论与机理分析。
