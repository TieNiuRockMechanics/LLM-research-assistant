---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-wu-effect-of-cooling-methods-on-mechanical-behaviors-and-thermal-damage-distributions-of-gr"
title: "Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations."
status: "draft"
source_pdf: "data/papers/2023 - Effect of cooling methods on mechanical behaviors and thermal damage distributions of granite Experiments and simulations.pdf"
collections:
  - "zotero new"
citation: "Wu, Yangchun, et al. \"Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations.\" *Geothermics*, vol. 114, 2023, 102796. doi:10.1016/j.geothermics.2023.102796. Accessed 2026."
indexed_texts: "14"
indexed_chars: "65529"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "61513"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.938714"
coverage_status: "full-index"
source_signature: "8fc3f1196e0fbd8bee359ffa7499604454b80931"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:24:34"
---

# Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations.

## One-line Summary
研究了缓慢加热后水冷与空气冷却对花岗岩力学性能劣化的根本原因，通过巴西劈裂试验、DIC、AE监测和COMSOL传热模拟，揭示了冷却方式通过改变温度梯度与热应力分布影响损伤机理，并提出高对流传热系数的工质可提升地热提取效率。[Wu 2023, pp. 1-2]

## Research Question
不同冷却方式（水冷 vs. 空气冷却）如何影响高温花岗岩的力学行为、温度场及热损伤空间分布？热应力与温度梯度在两种冷却条件下的控制因素有何差异？[Wu 2023, pp. 1-2, 2–3]

## Study Area / Data
- 岩石类型：长沙灰花岗岩，取自长沙某采石场，主要矿物为石英28.6%、长石55.1%、云母11.5%、绿泥石4.8% [Wu 2023, pp. 2-3]。
- 试样尺寸：巴西圆盘，直径50 mm，高25 mm，密度2.64–2.65 g/cm³ [Wu 2023, pp. 2-3]。
- 热处理范围：初始温度200–600℃（间隔100℃），升温速率2℃/min，保温3 h [Wu 2023, pp. 3-3]。
- 冷却条件：水冷（20℃水）和空气自然冷却，冷却过程中用红外测温枪记录表面温度曲线 [Wu 2023, pp. 3-3]。

## Methods
- 力学试验：伺服试验机实施巴西劈裂，加载速率0.015 mm/min；DIC系统以30 fps拍摄散斑场，计算表面应变；AE系统阈值40 dB记录声发射事件 [Wu 2023, pp. 3-3]。
- 物理性质测量：试验前后用高精度电子秤、游标卡尺和岩石超声波分析仪测定质量、体积及P波速度 [Wu 2023, pp. 3-3]。
- 数值模拟：采用COMSOL Multiphysics建立三维瞬态热‑力耦合模型，试样与实际尺寸一致。热膨胀系数服从随机正态分布（均值7×10⁻⁶ K⁻¹，标准差1×10⁻⁷）；水冷/空气冷的对流换热系数分别取850 W/(m²·K)和23 W/(m²·K) [Wu 2023, pp. 8-10]。模型假设：热导率、比热容不随温度变化，忽略内部热源，冷却介质温度恒定 [Wu 2023, pp. 6-8]。

## Key Findings
1. 同一初始温度下，水冷试样的抗拉强度低于空气冷却，且随温度升高两者均下降；水冷造成的热损伤更严重 [Wu 2023, pp. 5-6, 13–13]。
2. 水冷试样在压密阶段AE计数更密集；随温度升高，空气冷却累积AE计数递增，水冷累积AE计数先增后减（临界温度500–20℃），与脆‑延性转变点吻合 [Wu 2023, pp. 6-6, 13–13]。
3. 水冷条件下拉应力集中于试样表面，压应力位于内部，分布主要受温度梯度控制；空气冷却下应力分布随机，受矿物热膨胀系数非均质性主导 [Wu 2023, pp. 10-12, 13–13]。
4. 水冷热损伤集中在试样表面，空气冷却损伤呈随机散布，与CT观测结果一致 [Wu 2023, pp. 12-13]。
5. 岩石与冷却介质间的对流换热系数是决定温度梯度和应力分布的关键；选用高对流系数的工质有利于增强地热提取效率 [Wu 2023, pp. 13-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水冷600–20℃抗拉强度1.12 MPa，空气冷却2.28 MPa，分别较常温降低85.8%和71.2% | [Wu 2023, pp. 5-6] | 巴西劈裂，升温2℃/min，保温3h | 水冷强度更低，差异随温度扩大 |
| 600–20℃时水冷波速降低67.11%，空气冷却降低62.24% | [Wu 2023, pp. 3-5] | 相同热处理历史 | 波速下降反映热裂纹程度 |
| 水冷表面测量点A在600–20℃最大温度梯度116270℃/m，空气冷却仅1560℃/m | [Wu 2023, pp. 8-10] | 模拟结果，点A位置 | 温度梯度差异达74倍 |
| 600–20℃水冷50 s时中心‑表面温差317.9℃，空气冷却同期温差仅67.5℃ | [Wu 2023, pp. 8-10] | 数值模拟 | 水冷内部温度场极度不均匀 |
| 水冷表面最大拉应力从200–20℃的4.97 MPa升至600–20℃的16.14 MPa | [Wu 2023, pp. 10-12] | 模拟结果（σ_P） | 拉应力超过抗拉强度诱发裂纹 |
| 水冷累积AE计数500–20℃后下降，600–20℃失效时无突跳，显示延性破坏 | [Wu 2023, pp. 6-6] | AE监测，阈值40 dB | 脆‑延转变临界温度约500℃ |
| 空气冷却热损伤随机分布，水冷集中在表面，与Fan et al. (2020) CT图像吻合 | [Wu 2023, pp. 12-13] | 模拟与文献对比 | 证实温度梯度主导水冷损伤分布 |

## Limitations
- 数值模拟假设热导率、比热容及对流换热系数不随温度变化，可能影响高温段精度 [Wu 2023, pp. 6-8]。
- 热膨胀系数仅考虑矿物颗粒间的随机分布，未纳入矿物晶内各向异性 [Wu 2023, pp. 8-10]。
- 模型仅涵盖热传导和对流，忽略辐射散热以及冷却介质温度变化 [Wu 2023, pp. 6-8]。
- 试样视为均质连续体，未体现实际花岗岩的矿物结构与非连续原生裂隙 [Wu 2023, pp. 6-8]。
- 实验采用单一升温速率和保温时间，未探讨不同加热路径的影响 [Wu 2023, pp. 2-2]。

## Assumptions / Conditions
- 热膨胀系数满足COMSOL内置随机正态分布 [Wu 2023, pp. 8-10]。
- 冷却介质温度保持20℃恒定 [Wu 2023, pp. 8-10]。
- 热物理参数（γ, c）和对流换热系数（h）不随温度变化 [Wu 2023, pp. 6-8]。
- 岩石为各向同性线弹性材料，忽略塑性变形和蠕变 [Wu 2023, pp. 6-8]。
- 冷却过程中无内部热源，不考虑相变 [Wu 2023, pp. 6-8]。

## Key Variables / Parameters
- 独立变量：冷却方式（水冷、空气冷），初始目标温度（200, 300, 400, 500, 600℃）
- 实验因变量：抗拉强度 σ_t、波速 v_p、质量/体积/密度变化率、AE计数值与累积值、DIC表面应变场
- 模拟参数：对流换热系数（h_water=850 W/(m²·K)，h_air=23 W/(m²·K)）、热导率 γ、比热容 c=850 J/(kg·℃)、密度 ρ=2640 kg/m³、弹性模量9.3 GPa、泊松比0.25、热膨胀系数随机分布（均值7×10⁻⁶ K⁻¹，标准差1×10⁻⁷）
- 计算中间量：温度梯度 ∂T/∂n，应力 σ_P（压力应力），基于最大拉应力准则的热损伤分布

## Reusable Claims
- 在2℃/min加热至200–600℃并保温3 h后急冷，**水冷花岗岩抗拉强度总是低于空气冷却**，且差值随温度升高而增大（如600℃时强度分别为1.12 MPa和2.28 MPa）。条件：长沙灰花岗岩圆盘试样，巴西劈裂，水冷介质20℃。限制：未涉及循环热冲击；强度衰减路径可能受矿物组成影响。来源：[Wu 2023, pp. 5-6]。
- **水冷试样的压密阶段AE事件显著多于空气冷却**，表明冷却过程中已产生大量微裂纹。条件：巴西劈裂加载初期，AE阈值40 dB。限制：可能漏检极小尺度事件。来源：[Wu 2023, pp. 6-6]。
- **水冷条件下累积AE计数在500–20℃后下降**，预示破坏模式由脆性向延性转变，可作为热储层破裂行为预警指标。条件：水冷，温度≥500℃。限制：仅在巴西劈裂路径下验证。来源：[Wu 2023, pp. 6-6, 13–13]。
- **空气冷却时热应力主要由矿物热膨胀系数的不均匀分布决定**，导致损伤随机分布；**水冷时温度梯度主导**，损伤集中于表面。条件：花岗岩矿物组成同长沙灰。限制：未量化矿物各向异性贡献。来源：[Wu 2023, pp. 10-13]。
- **选用高对流换热系数的工质可大幅提高岩石内部温度梯度和热应力**，从而促进裂隙网络形成，利于增强型地热系统（EGS）产热效率。条件：高温花岗岩储层，注冷水作业。限制：现场需额外考虑围压、孔隙流体和尺度效应。来源：[Wu 2023, pp. 13-13]。

## Candidate Concepts
- [[thermal damage]]
- [[water cooling]] vs. [[air cooling]] (cooling method)
- [[Changsha gray granite]]
- [[convective heat transfer coefficient]]
- [[temperature gradient]]
- [[thermal stress]]
- [[thermal-mechanical coupling]]
- [[Brazilian splitting test]]
- [[Digital Image Correlation (DIC)]]
- [[Acoustic Emission (AE)]]
- [[brittle-ductile transition]]
- [[intergranular crack]] and [[transgranular crack]]
- [[Enhanced Geothermal System (EGS)]]
- [[heat conduction]] and [[convective heat transfer]]
- [[Fourier’s law]] and [[Newton’s law of cooling]]
- [[random heterogeneity of thermal expansion coefficient]]
- [[COMSOL Multiphysics]]
- [[porosity and permeability evolution]]

## Candidate Methods
- [[Brazilian splitting test for tensile strength]]
- [[Digital Image Correlation (DIC) surface strain mapping]]
- [[Acoustic Emission (AE) monitoring during loading]]
- [[infrared thermometer gun for transient surface temperature]]
- [[COMSOL Multiphysics heat transfer and solid mechanics simulation]]
- [[X-ray diffraction (XRD) for mineral composition]]
- [[ultrasonic P-wave velocity measurement]]
- [[MATLAB image segmentation and DIC computation]]
- [[normalized tensile strength]] δ = σ_t(T) / σ_t(T₀)

## Connections To Other Work
- **Jin et al. (2019)** 发现渗透率突变临界温度在快速冷却下为400℃、缓慢冷却下为500℃，与本文水冷损伤更早激增的趋势相符 [Wu 2023, pp. 2-2]。
- **Chen et al. (2017)** 提出5℃/min为北山花岗岩热损伤临界加热速率；本文采用2℃/min以避免加热损伤干扰 [Wu 2023, pp. 2-2]。
- **Zhu et al. (2021)** 和 **Sha et al. (2020)** 报道600℃水冷波速降低84.9%、70.76%，空气冷却降低73.9%、57.94%，本文趋势与之吻合 [Wu 2023, pp. 2-2, 3–5]。
- **Wu et al. (2019)** 指出>400℃时三种冷却方式抗拉强度顺序为水冷<空气<炉冷，与本文结果一致 [Wu 2023, pp. 2-2]。
- **Kumari et al. (2017)** 观察到水冷400℃时石英出现微裂纹，表面裂纹出现早于缓慢冷却，本文通过温度梯度分布解释了该现象 [Wu 2023, pp. 2-2]。
- **Fan et al. (2020)** 的CT图像显示快速冷却损伤集中于表面、缓慢冷却随机分散，本文的数值模拟再现了这一分布规律 [Wu 2023, pp. 12-13]。
- **Zhao et al. (2021)** 测量了水冷温度场并计算最大热应力41 MPa，但未给出应力方向与空间分布；本文填补了该空白 [Wu 2023, pp. 2-3, 10–12]。

## Open Questions
- 石英、长石、云母等矿物晶粒内部的各向异性热膨胀对局部热应力场的贡献尚未单独量化 [Wu 2023, pp. 2-3]。
- 多次“升温‑急冷”循环下的损伤累积规律和残余力学性质演变未涉及。
- 模拟未考虑热物理参数（γ, c, h）随温度的非线性变化，可能低估高温段损伤 [Wu 2023, pp. 6-8]。
- 仅针对均质花岗岩，其他岩性（如层理页岩、碳酸盐岩）的冷却响应差异有待研究。
- 现场尺度下围压、孔隙压力及裂隙流体的耦合作用尚需进一步分析 [Wu 2023, pp. 1-2]。
- 能否利用AE特征参数（如b值、能量分布）实时预测热破裂模式转变仍需探索。

## Source Coverage
全部14个非空索引片段均已处理并纳入本页面。索引文本总字符数65,529，编译后正文（不含量化引用标签）约61,513字符，字符覆盖率约93.87%。未丢弃或截断任何片段，所有来源标签[Wu 2023, pp. …]均完整保留。片段清单：[Wu 2023, pp. 1-2], [Wu 2023, pp. 2-2], [Wu 2023, pp. 2-3], [Wu 2023, pp. 3-3], [Wu 2023, pp. 3-5], [Wu 2023, pp. 5-6], [Wu 2023, pp. 6-6], [Wu 2023, pp. 6-8], [Wu 2023, pp. 8-10], [Wu 2023, pp. 10-12], [Wu 2023, pp. 12-13], [Wu 2023, pp. 13-13], [Wu 2023, pp. 13-14], [Wu 2023, pp. 14-14]。
