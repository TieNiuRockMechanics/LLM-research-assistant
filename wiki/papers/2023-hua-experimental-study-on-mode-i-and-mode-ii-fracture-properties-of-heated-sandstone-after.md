---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-hua-experimental-study-on-mode-i-and-mode-ii-fracture-properties-of-heated-sandstone-after"
title: "Experimental Study on Mode I and Mode II Fracture Properties of Heated Sandstone after Two Different Cooling Treatments."
status: "draft"
source_pdf: "data/papers/2023 - Experimental study on mode I and mode II fracture properties of heated sandstone after two different cooling treatments.pdf"
collections:
  - "zotero new"
citation: "Hua, Wen, et al. \"Experimental Study on Mode I and Mode II Fracture Properties of Heated Sandstone after Two Different Cooling Treatments.\" *Geomechanics for Energy and the Environment*, vol. 34, 2023, p. 100448. *ScienceDirect*, www.elsevier.com/locate/gete. Accessed 2026."
indexed_texts: "15"
indexed_chars: "71581"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "71891"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004331"
coverage_status: "full-index"
source_signature: "7d8ea7c61374a748ef41a2b8c0a2f6c5726bdfed"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:33:57"
---

# Experimental Study on Mode I and Mode II Fracture Properties of Heated Sandstone after Two Different Cooling Treatments.

## One-line Summary
本研究通过CSTBD试样实验，探究了热砂岩在快速水冷和自然空冷两种方式下I型与II型断裂特性的劣化规律，发现快速水冷造成的损伤更为显著，且基于应变的广义最大切向应变(GMTSN)准则能更准确地预测实验结果。

## Research Question
加热后的砂岩在经过快速水冷和自然空冷两种不同处理后，其纯I型和纯II型断裂韧性将如何变化，其背后的降解损伤机制是什么，以及如何利用考虑T应力的修正断裂准则来评估这些实验结果？[Hua 2023, pp. 1-2]

## Study Area / Data
实验所用岩样为采自中国四川省资阳市的同一块青砂岩，具有优良的颗粒性和均质性，干密度2.24 g/cm³，含水量1.20%，抗拉强度2.68 MPa，泊松比0.21。主要矿物成分为钠长石、石英、钙沸石和斜绿泥石。[Hua 2023, pp. 2-3]

实验设置了25°C（室温）、100°C和300°C三个加热温度等级，并分别进行快速水冷和自然空冷两种处理。用于测量的试样为CSTBD（Cracked Straight-Through Brazilian Disk）试样，直径75 mm，厚度25 mm，裂纹长度38 mm（即a/R=0.5）。[Hua 2023, pp. 2-3]

## Methods
1.  **试样制备与处理**：将青砂岩加工成CSTBD试样。将试样置于烘箱中以3°C/min的速率分别加热至100°C和300°C，并恒温48小时。之后进行两种冷却处理：
    *   **快速水冷**：直接将加热后的试样放入水中，在大气条件下自然饱和72小时。
    *   **自然空冷**：将加热后的试样在空气中冷却至室温（约4小时），然后放入水中浸泡68小时，以保证与快速水冷处理总时间相同。
    所有试样从水中取出后，在大气环境中自然干燥240小时。[Hua 2023, pp. 3-4]
2.  **断裂韧性测试**：使用电子材料试验机，以0.05 mm/min的位移控制速率，对所有CSTBD试样进行加载直至最终破坏，记录载荷-位移曲线及峰值载荷。每组至少成功测试5个试样。[Hua 2023, pp. 3-4]
3.  **断裂韧性计算**：基于Dong et al. [40]推导的应力强度因子（SIFs）解析表达式（公式1和2），利用实验测得的峰值载荷和相应的无量纲SIFs (YI, YII) 计算纯I型和纯II型断裂韧性（KIC, KIIC）。[Hua 2023, pp. 2-4]
4.  **微观机制分析**：使用扫描电子显微镜（SEM）观察不同冷却处理后的砂岩试样表面的微形貌，分析其微观结构变化。[Hua 2023, pp. 6-6]
5.  **理论评估**：采用考虑T应力的修正断裂准则（GMTS, GMTSN, GMSED, GMERR）对实验测得的裂纹起裂角和断裂韧性比值（KIIC/KIC）进行理论预测，并与实验结果对比，以评估各准则的准确性。[Hua 2023, pp. 7-9]

## Key Findings
1.  **断裂韧性与温度呈负相关**：在两种冷却处理下，青砂岩的纯I型和纯II型断裂韧性均随温度升高而降低。与完整砂岩（25°C）相比，快速水冷后100°C和300°C的KIC分别降低了23.9%和32.1%，KIIC分别降低了24.6%和33.3%。自然空冷后，100°C和300°C的KIC分别降低了16.5%和23.4%，KIIC分别降低了17.3%和24.9%。[Hua 2023, pp. 4-6]
2.  **快速水冷的劣化效应更强**：在相同加热温度下，快速水冷处理的砂岩断裂韧性和峰值载荷均低于自然空冷处理。快速水冷对纯I型和纯II型断裂韧性的劣化损伤分别约为自然空冷的1.40倍和1.38倍。[Hua 2023, pp. 6-6]
3.  **KIIC和KIC之间存在优异的线性关系**：通过线性回归分析，得出了KIIC = 1.494KIC的拟合曲线。两种冷却方式对KIIC/KIC比值的影响无明显差异，且该比值随温度升高而略有下降（最大降幅不超过2.1%），可忽略不计。[Hua 2023, pp. 6-9]
4.  **GMTSN准则预测最准确**：与传统的仅考虑应力强度因子（SIFs）的断裂准则相比，考虑T应力的修正准则（GMTS, GMTSN, GMSED, GMERR）能提供更好的预测。其中，基于应变的GMTSN准则对纯II型裂纹起裂角和断裂韧性比值的预测值（分别为-54.06°和1.354）与实验值（分别为-51.80°和1.494）的相对误差最小，分别为4.4%和9.3%。[Hua 2023, pp. 9-10]
5.  **纯II型加载下为拉伸型破坏**：CSTBD试样在纯II型加载下，裂纹并非沿预置裂纹方向扩展，其轨迹发生偏折，呈现拉伸型破坏特征。两种冷却处理对裂纹起裂角几乎没有影响。[Hua 2023, pp. 3-4]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 快速水冷后，100°C和300°C的KIC分别降至0.251和0.224 MPa·m⁰·⁵；自然空冷后分别降至0.275和0.253 MPa·m⁰·⁵。 | [Hua 2023, pp. 4-6] | CSTBD试样，青砂岩，a/R=0.5 | 完整砂岩KIC为0.330 MPa·m⁰·⁵。 |
| 快速水冷后，100°C和300°C的KIIC分别降至0.375和0.332 MPa·m⁰·⁵；自然空冷后分别降至0.412和0.374 MPa·m⁰·⁵。 | [Hua 2023, pp. 6-6] | CSTBD试样，青砂岩，a/R=0.5 | 完整砂岩KIIC为0.498 MPa·m⁰·⁵。 |
| 实验测得KIIC与KIC的线性关系为KIIC = 1.494KIC。 | [Hua 2023, pp. 9-10] | 所有冷却处理后的青砂岩 | 拟合优度未明确指出，但描述为“优异的线性关系”。 |
| 快速水冷对KIC的劣化效应是自然空冷的1.40倍；对KIIC是1.38倍。 | [Hua 2023, pp. 6-6, 10-10] | CSTBD试样，青砂岩 | 结论（2）明确指出。 |
| 对于纯II型裂纹起裂角的预测，GMTSN准则的预测值 (-54.06°) 与实验值 (-51.80°) 相对误差最小 (4.4%)。 | [Hua 2023, pp. 9-10] | 考虑T应力的修正断裂准则 | 平面应变条件，泊松比ν=0.21，临界距离r0=2.20 mm。 |
| 纯II型加载下，裂纹起裂角为拉伸型破坏，且冷却处理对起裂角几乎无影响。 | [Hua 2023, pp. 3-4] | CSTBD试样，纯II型加载 | 快速水冷和自然空冷下的起裂角绝对值分别为51.60°和52.00°。 |
| 快速水冷造成的微观结构损伤（孔隙/微裂纹尺寸和数量、表面粗糙度）比自然空冷更严重。 | [Hua 2023, pp. 6-7] | SEM观察 | 这与断裂韧性测试结果一致。 |

## Limitations
1.  研究仅针对一种特定类型的青砂岩，结论向其他岩性的推广需谨慎。[Hua 2023, pp. 2-3]
2.  加热温度范围仅限于25-300°C，更高温度下的断裂特性变化规律未被探讨。[Hua 2023, pp. 3-3]
3.  实验在特定尺寸（直径75mm）的CSTBD试样上进行，断裂韧性的尺寸效应未被研究。[Hua 2023, pp. 3-3]
4.  T应力修正准则的评估主要集中在纯II型加载条件下的预测能力，对更广泛的混合模式加载的预测性能未充分展示。[Hua 2023, pp. 9-10]
5.  降解机制分析主要基于定性的SEM观察，缺乏对孔隙率、微裂纹密度等参数的定量统计。[Hua 2023, pp. 6-7]

## Assumptions / Conditions
1.  **试样均质性假设**：所选青砂岩被认为是“优良的颗粒性和均质性岩石”，这是所有实验数据可比性的基础。[Hua 2023, pp. 2-3]
2.  **临界距离统一值**：在计算理论预测值时，基于所有处理条件下的KIC和σt数据，通过线性回归（KIC = 0.1176σt）和公式（5）计算了一个统一的临界距离值r0 = 2.20 mm，忽略了不同冷却处理下r0的微小差异。[Hua 2023, pp. 7-8]
3.  **平面应变条件**：应用修正断裂准则进行计算时，采用了平面应变条件，泊松比取0.21。[Hua 2023, pp. 9-9, 11-11]
4.  **冷却过程控制**：为控制时间变量，自然空冷处理的试样在冷却后增加了一步68小时的浸泡过程，以匹配快速水冷处理中72小时的浸泡时间。这假设了额外的浸泡对“自然空冷”损伤的贡献可以忽略不计。[Hua 2023, pp. 3-4]
5.  **加热影响单一化**：在分析加热过程影响时，仅将温度视为主导因素，忽略了低加热速率可能带来的影响。[Hua 2023, pp. 6-7]

## Key Variables / Parameters
- **独立变量**：加热温度 (25, 100, 300 °C)；冷却处理方式 (快速水冷, 自然空冷)。
- **因变量**：纯I型断裂韧性 (KIC)；纯II型断裂韧性 (KIIC)；峰值载荷 (P)；抗拉强度 (σt)。
- **材料参数**：泊松比 (ν=0.21)；干密度 (2.24 g/cm³)；临界距离 (r0=2.20 mm)。
- **几何参数**：CSTBD试样直径 (D=75 mm)；厚度 (t=25 mm)；裂纹半长 (a=19 mm)；裂纹长度比 (a/R=0.5)；纯I型加载角 (β=0°)；纯II型加载角 (β=23°)。
- **断裂力学参数**：无量纲应力强度因子 (纯I型 YI=1.3844；纯II型 YII=2.1349)；无量纲T应力 (纯I型 T*=-5.790；纯II型 T*=-1.500)；双轴比 (纯I型 BI=-4.182；纯II型 BII=-0.703)。

## Reusable Claims
- **Claim 1**: 对于青砂岩，快速水冷处理比自然空冷处理对其I型和II型断裂韧性的劣化作用更显著，损伤程度约为1.4倍。这一结论的前提是加热温度在100-300°C范围内。 **[Hua 2023, pp. 6-6, 10-10]**
- **Claim 2**: 岩石的纯II型断裂韧性(KIIC)显著高于纯I型断裂韧性(KIC)，对于本研究中的青砂岩，在各种温度处理下，两者的比值(KIIC/KIC)保持在一个约为1.494的常数值附近，且不受冷却方式影响。 **[Hua 2023, pp. 6-9]**
- **Claim 3**: 在评估受温度损伤岩石的纯II型断裂行为时，基于应变的广义最大切向应变(GMTSN)准则，相较于GMTS、GMSED和GMERR等修正准则，能提供与实验数据最为一致的理论预测。这提示在模拟此类岩石的拉伸-剪切断裂时，应考虑应变和T应力的综合影响。 **[Hua 2023, pp. 9-10]**
- **Claim 4**: 快速水冷引起的热冲击是导致高温岩石力学性能劣化的主导因素，其机理在于加剧了矿物颗粒间的不协调变形，增加了孔隙和微裂纹的数量与尺寸，而自然空冷的主要损伤机制是温度和弱水-岩相互作用。 **[Hua 2023, pp. 6-7]**

## Candidate Concepts
- [[Heated Sandstone]]
- [[Mode I Fracture Toughness]]
- [[Mode II Fracture Toughness]]
- [[Cooling Treatment]]
- [[Rapid Water-Cooling]]
- [[Natural Air-Cooling]]
- [[Cracked Straight-Through Brazilian Disk (CSTBD)]]
- [[Degradation Mechanism]]
- [[Thermal Shock]]
- [[Fracture Criteria]]
- [[Generalized Maximum Tangential Strain (GMTSN)]]
- [[T-stress]]

## Candidate Methods
- [[CSTBD Fracture Toughness Testing]]
- [[Scanning Electron Microscopy (SEM) for Rock Microstructure]]
- [[Linear Regression for KIIC-KIC Relationship]]
- [[Modified Fracture Criteria Assessment]]
- [[Controlled Thermal Treatment and Cooling of Rock Samples]]

## Connections To Other Work
- **矿物组成与微观结构**：研究指出岩石的物理力学性质与其矿物组成和微观结构密切相关 [Hua 2023, pp. 1-1]，本研究中不同冷却处理导致的损伤差异通过SEM图像得到证实 [Hua 2023, pp. 6-7]。
- **不同冷却方式的对比研究**：本研究结论与Brotóns et al. (2013) 和Isaka et al. (2018) 的发现一致，即快速水冷比空气冷却能引起更显著的抗压强度和弹性模量降低 [Hua 2023, pp. 2-2]。与Kumari et al. (2017) 关于水冷导致热劣化更严重的结论也相符 [Hua 2023, pp. 2-2]。
- **CSTBD试样与断裂准则**：研究中使用的CSTBD应力强度因子公式来源于Dong et al. (2004) [Hua 2023, pp. 2-3]，T应力公式来源于Hua et al. (2015) [Hua 2023, pp. 7-7]。实验现象（纯II型加载下的拉伸破坏）与Hua et al. (2015, 2016) 和 Ayatollahi et al. (2008) 的研究结果类似 [Hua 2023, pp. 4-4]。GMTSN准则的优越性也与Wei et al. (2017) 和 Mirsayar et al. (2018) 的结论相呼应 [Hua 2023, pp. 9-9]。
- **温度对岩石性质的影响**：研究背景提及，温度对岩石物理力学性质（如P波、弹性模量、强度）的影响已在众多研究中被探讨，且存在一个与岩石类型相关的强度阈值 [Hua 2023, pp. 1-1]。本研究结果与之相印证。
- **水对岩石强度的影响**：降解机制分析中提到，较高的含水量会加剧温度对岩石强度的损伤效应 [Hua 2023, pp. 6-7]，这与Hua et al. (2017) 和Török & Vásárhelyi (2010) 的观点一致。

## Open Questions
- 当加热温度超过300°C时（如400°C、600°C、800°C），快速水冷与自然空冷对青砂岩断裂韧性的劣化差异是否会保持1.4倍的比例关系，或者会出现新的变化趋势？
- 在长期的水-岩相互作用或循环冷热条件下，两种冷却处理造成的微观结构损伤差异将如何演变，并对宏观力学性能产生怎样的影响？
- GMTSN准则在预测纯II型断裂行为时表现出色，但其预测能力是否同样适用于更广泛的混合模式（如I-II混合模式）以及其它类型的岩石（如花岗岩、石灰岩）？该准则中临界距离r0的物理意义及其在不同条件下的确定方法仍需深入探讨。

## Source Coverage
本文所有（15个）非空的索引片段均已处理并用于编译。源文本特征码为 `7d8ea7c61374a748ef41a2b8c0a2f6c5726bdfed`。区块覆盖率为 1.0，字符覆盖率为 1.004331。
