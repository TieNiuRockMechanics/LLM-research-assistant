---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-wu-effect-of-flame-jet-induced-damage-on-physical-and-mechanical-properties-of-granite"
title: "Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite."
status: "draft"
source_pdf: "data/papers/2025 - Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wu, Yangchun, et al. \"Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 947–63. https://doi.org/10.1007/s00603-024-04155-3."
indexed_texts: "14"
indexed_chars: "68050"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:05:58"
---

# Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.

## One-line Summary
火焰射流会在花岗岩中引起随距离增大而减弱的物理力学性能劣化，损伤半径约70 mm，本文建立了描述这一现象的热剥落与热损伤模型。 [Wu 2025, pp. 1-2]

## Research Question
火焰射流辅助机械破岩是实现硬岩矿山非爆破连续机械化开采（NECMM）的重要方法，为有效应用该技术，亟需探明火焰射流后剥落坑围岩的物理力学性质变化规律与损伤范围。 [Wu 2025, pp. 1-2]

## Study Area / Data
所用花岗岩块体取自中国长沙，被加工为长250 mm × 高200 mm × 宽100 mm的长方体，完整性良好，无明显缺陷，并利用X射线荧光光谱（XRF）测定了其化学成分。 [Wu 2025, pp. 3-4] 热剥落试验采用丙烷‑氧气火焰，功率13.6 kW。 [Wu 2025, pp. 1-2, 3-4]

## Methods
试验总体流程如下：首先在花岗岩块体表面沿预设路径进行火焰射流热剥落（功率13.6 kW），随后自火焰射流路径起，按不同距离（0 mm、25 mm、50 mm、70 mm 等）钻取或切割试样。 [Wu 2025, pp. 1-2, 3-4, 4-6] 对取出的试样依次测量纵波速度 (Vp)、巴西劈裂抗拉强度 (BTS)、单轴抗压强度 (UCS)、杨氏模量 (E)，并同步采集声发射 (AE) 特征以及利用数字图像相关 (DIC) 技术获取表面应变场。 [Wu 2025, pp. 1-2, 4-6] AE 监测门限设为45 dB，所有试验加载速率均为 0.001 mm/s。 [Wu 2025, pp. 4-6] 除力学测试外，还基于热传导与热弹性方程，借助 COMSOL 软件对 Lyu et al. (2019) 的火焰射流试验进行了数值模拟，以分析岩石内部热应力分布。 [Wu 2025, pp. 11-12] 为量化损伤，定义了基于 Vp 和 E 的损伤因子 Dvp、DE，并将其与强度变化率进行对比。 [Wu 2025, pp. 9-11]

## Key Findings
1. **Vp 恢复**：随着距火焰射流路径距离增加，Vp 单调增大；70 mm 处 Vp 由 0 mm 处的 3263.9 m/s 上升至 3670.4 m/s（增幅 12.5%），已接近未处理试样的 3677.4 m/s。 [Wu 2025, pp. 4-6]
2. **BTS 变化**：BTS 同样随距离增加而增大，70 mm 处的 BTS 略低于未处理试样，据此估算损伤半径约为 70 mm。 [Wu 2025, pp. 6-8]
3. **UCS 与 E 的恢复**：UCS 从 0 mm 处的 98.14 MPa 增至 70 mm 处的 150.54 MPa（增加 52.40 MPa），E 从 6.62 GPa 增至 10.28 GPa；70 mm 处的 UCS（150.54 MPa）仍稍低于未处理试样（152.70 MPa），进一步支持损伤半径约 70 mm 的结论。 [Wu 2025, pp. 8-9]
4. **巴西劈裂声发射与 DIC 特征**：DIC 图像显示高应变区由圆盘中心向两端扩展，最终沿加载方向形成贯穿裂纹。峰荷附近 AE 计数突增，累积 AE 计数随距离增大（损伤减轻）而升高，由 0 mm 时的 45.85×10⁴ 增至 70 mm 时的 55.45×10⁴。 [Wu 2025, pp. 6-8]
5. **单轴压缩声发射特征**：距火焰路径越近（0 mm 和 25 mm），压实阶段的 AE 计数越密集，表明内部热致微裂纹越多。最大累积 AE 计数随距离增加而增大，从 0 mm 的 45.73×10⁵ 增至 70 mm 的 59.18×10⁵（增幅 29.4%），与巴西试验规律一致。 [Wu 2025, pp. 8-9]
6. **损伤因子评估**：基于 Vp 和 E 的损伤因子 Dvp 和 DE 与 UCS、BTS 的变化率趋势一致，能有效表征力学性能的劣化程度。 [Wu 2025, pp. 9-11]
7. **模型解释**：所建立的热剥落与热损伤模型能够较好地阐释距火焰路径不同距离处力学性质的差异。 [Wu 2025, pp. 1-2] 模型考虑了温度场瞬态分布、热应力及线弹性变形，并通过引用 Lyu et al. (2019) 的温度数据进行了验证性模拟。 [Wu 2025, pp. 11-12]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 火焰射流功率 13.6 kW | [Wu 2025, pp. 1-2] | 丙烷+氧气，花岗岩长方体 | 试验系统包含移动装置，射流路径在岩块正面 |
| 距射流路径 0 mm: Vp=3263.9 m/s; 70 mm: 3670.4 m/s; 未处理: 3677.4 m/s | [Wu 2025, pp. 4-6] | 纵波测试 | Vp 增幅12.5%，70 mm 处已接近未处理值 |
| BTS 随距离增加而上升，70 mm 处稍低于未处理试样（约7.67 MPa） | [Wu 2025, pp. 6-8] | 巴西劈裂试验 | 损伤半径≈70 mm |
| UCS: 0 mm→98.14 MPa, 70 mm→150.54 MPa; 未处理→152.70 MPa | [Wu 2025, pp. 8-9] | 单轴压缩 | E: 0 mm→6.62 GPa, 70 mm→10.28 GPa |
| 单轴压缩压实期 AE 在 0 和 25 mm 时密集，累积 AE 最大计数随距离增加 | [Wu 2025, pp. 8-9] | AE 门槛 45 dB, 加载率0.001 mm/s | 最大累积计数增幅29.4% |
| 巴西试验峰值时累积 AE 计数: 0 mm→45.85×10⁴, 70 mm→55.45×10⁴ | [Wu 2025, pp. 6-8] | AE 监测 | 距射流越近，累积 AE 越低 |
| 损伤因子 Dvp=1-(Vp(x)/Vp(x₀))², DE=1-E(x)/E(x₀) | [Wu 2025, pp. 9-11] | 以未处理试样为基准 x₀ | 与 UCS、BTS 变化率一致 |
| 温度场控制方程: ρC ∂T/∂t=∇·(λ∇T); 热通量 q=GP/(πr₀²) exp(-r²/r₀²) | [Wu 2025, pp. 11-12] | COMSOL 模拟，引用 Lyu et al. 2019 温度数据 | 边界含对流与辐射，ε=0.7, σs=5.67e-8 |
| 热剥落条件: 换热系数>500 W/(m²K)，表面温度>500°C (Kant and Rudolf von Rohr 2016) | [Wu 2025, pp. 2-3] | 文献条件，未在本文实测 | 本文试验未测表面温度 |

## Limitations
- 文内未实测岩石内部温度场，所用温度分布数据引用自 Lyu et al. (2019) 的试验，其有效性和适用性存在限制。 [Wu 2025, pp. 11-12]
- 损伤模型仅考虑温度场引起的热应力，明确忽略了高温可能诱发的化学变化，因此无法反映矿物相变等对力学性质的影响。 [Wu 2025, pp. 9-11]
- 损伤半径判定为“约 70 mm”，但 70 mm 处强度与模量仍略低于未处理试样，说明该距离仍存在极轻微的损伤，半径的准确边界未进一步精炼。
- 试验仅针对一种花岗岩，其矿物组成只给出了 XRF 图示，未从片段中确认推广至其他岩性的依据。
- 剥落坑尺寸与形状对围岩损伤分布的影响未详细分析；未从索引片段中确认是否对不同规格岩块或不同火焰参数做了敏感性研究。

## Assumptions / Conditions
- 岩石被视为线弹性材料，固体变形方程采用考虑温度项的线弹性本构。 [Wu 2025, pp. 11-12]
- 火焰射流试验通过设置起、止点在两侧堆叠的岩石上，保证热剥落仅发生在岩块正前方，避免侧壁效应。 [Wu 2025, pp. 3-4]
- 损伤评估主要依靠 Vp、E 等物理参数，并假定其变化主要由热致微裂纹引起，未考虑化学风化。
- 温度场模拟的边界条件包含对流换热与热辐射，辐射系数取 0.7，Stefan‑Boltzmann 常数取 5.67×10⁻⁸ W/(m²·K⁴)。 [Wu 2025, pp. 11-12]
- 试样加载速率恒定为 0.001 mm/s，声发射门槛 45 dB，适用于所有力学试验。 [Wu 2025, pp. 4-6]

## Key Variables / Parameters
- **物理力学参数**：Vp (P 波速度)、BTS (巴西劈裂抗拉强度)、UCS (单轴抗压强度)、E (杨氏模量)
- **空间变量**：x — 试样距火焰射流路径的距离 (mm)
- **损伤指标**：Dvp(x), DE(x)；强度变化率 δ(σc(x)), δ(σt(x))
- **声发射特征**：AE 计数、累积 AE 计数、压实阶段 AE 计数
- **热学、力学参数**：热导率 λ, 密度 ρ, 比热 C, 换热系数 h, 辐射系数 ε, 热膨胀系数 β, 剪切模量 G, 泊松比 μ
- **试验控制参数**：火焰功率 13.6 kW, 加载速率 0.001 mm/s, AE 门槛 45 dB
- **模型参数**：热通量 q 表达式中的 ℙ、r₀; 环境温度 Ta; 体积参考温度 Tref

## Reusable Claims
- 在 13.6 kW 火焰射流作用于长沙花岗岩的条件下，剥落坑周围的力学参数（Vp、BTS、UCS、E）随距射流路径距离增加而单调递增，损伤近似半径约 70 mm（以接近未处理试样的参数为判据）。 [Wu 2025, pp. 1-2, 4-6, 8-9]
- 可使用基于 Vp 的损伤因子 Dvp=1−[Vp(x)/Vp(x₀)]² 或基于 E 的损伤因子 DE=1−E(x)/E(x₀) 来量化热损伤，这两个因子与强度变化趋势一致，适用于快速评估劣化程度。 [Wu 2025, pp. 9-11]
- 单轴压缩声发射特征可揭示热损伤程度：距火焰路径越近，压实阶段的 AE 计数越密集，且全过程累积 AE 计数越低，反映热致微裂纹在加载初期被大量闭合。 [Wu 2025, pp. 8-9]
- 巴西劈裂试验中，高应变区由圆盘中心萌生并向两端扩展，最终形成沿加载方向的贯穿裂纹，这一过程可由 DIC 应变云图直观捕获。 [Wu 2025, pp. 6-8]

## Candidate Concepts
- [[thermal spallation]]
- [[flame jet rock breaking]]
- [[NECMM (Non-Explosive Continuous Mechanized Mining)]]
- [[thermal damage]]
- [[P-wave velocity damage factor]]
- [[acoustic emission in rock mechanics]]
- [[digital image correlation (DIC)]]
- [[Brazilian tensile strength]]
- [[uniaxial compressive strength]]
- [[thermal stress]]
- [[spalling pit surrounding rock]]

## Candidate Methods
- [[flame jet testing]]
- [[DIC strain field analysis]]
- [[AE monitoring during mechanical loading]]
- [[thermal spalling test on granite blocks]]
- [[COMSOL thermal-mechanical simulation]]
- [[damage factor derived from Vp and elastic modulus]]
- [[XRF mineral composition analysis]]

## Connections To Other Work
- 本文引用了 Kant and Rudolf von Rohr (2016) 关于热剥落所需换热系数 (>500 W/(m²K)) 及表面温度 (>500°C) 的判据，以及 Hu et al. (2019) 对不同岩石热剥落温度的结论。 [Wu 2025, pp. 2-3]
- 损伤区 Vp 与 BTS 随距离增加的趋势与 Sha et al. (2019) 的结果相似。 [Wu 2025, pp. 4-6]
- 温度场数值模拟直接使用了 Lyu et al. (2019) 的试验数据作为验证依据。 [Wu 2025, pp. 11-12]
- 从主题上可连接至 [[effect of high temperature on rock mechanical properties]]、[[thermal cracking in granite]]、[[non-explosive continuous mining technology]] 等方向。

## Open Questions
- 70 mm 损伤半径是否适用于不同矿物组成的花岗岩，或不同功率、不同加热时长的火焰射流？未从索引片段中确认。
- 若考虑高温引起的化学变化（如脱水、分解），热损伤模型应如何修正？未从索引片段中确认。
- 热剥落过程中，是否可能在 70 mm 以外形成微弱的亚临界裂纹扩展？损伤边界的精确判据是什么？未从索引片段中确认。
- 多次火焰射流循环或交替加载对损伤累积的影响如何？片段未涉及。

## Source Coverage
本页基于全部 14 个索引片段编写，覆盖了摘要、引言（文献背景与热剥落机制）、方法（试样制备、试验系统、力学与声发射/ DIC 测试）、主要结果（Vp、BTS、UCS、E、AE 特征、DIC 图像）以及部分模型描述和讨论。可提取到的量化数据、损伤因子公式和热力学方程均来自片段。然而，部分图表信息（如 XRF 成分详细数据、模拟温度场云图）未以文字形式呈现；论文的应用讨论（NECMM 工程实现）可能未被索引片段充分覆盖；温度场模型验证的具体对比结果也未在片段中给出细节。因此，本页在损伤模型验证、实际采矿工程适用性等方面可能仍欠缺信息。
