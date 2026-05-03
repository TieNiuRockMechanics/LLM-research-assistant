---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-deng-formation-mechanism-of-the-north-south-gravity-lineament-in-eastern-china"
title: "Formation Mechanism of the North–South Gravity Lineament in Eastern China."
status: "draft"
source_pdf: "data/papers/2021 - Formation mechanism of the North–South Gravity Lineament in eastern China.pdf"
collections:
  - "山西断裂地质构造"
citation: "Deng, Yangfan, et al. “Formation Mechanism of the North–South Gravity Lineament in Eastern China.” *Tectonophysics*, vol. 818, 2021, p. 229074."
indexed_texts: "13"
indexed_chars: "60990"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:48:19"
---

# Formation Mechanism of the North–South Gravity Lineament in Eastern China.

## One-line Summary
通过重力建模，本研究约束了中国东部南北重力线（NSGL）的形成机制，表明地壳厚度变化是主导因素，岩石圈地幔成分差异为次要因素，其根源可追溯到古太平洋板块俯冲导致的华北克拉通东部破坏 [Deng 2021, pp. 1-1].

## Research Question
陆内重力线（尤其是中国东部延伸超过4000公里的NSGL）的形成机制是什么？具体地壳厚度、地壳/上地幔成分以及地幔转换带中的滞留板块对观测到的布格重力异常的相对贡献如何？ [Deng 2021, pp. 1-1]

## Study Area / Data
- **研究区域**: 中国东部的南北重力线（NSGL），研究重点是其穿越华北克拉通（NCC）的狭窄部分。NSGL两侧的其他地质单元包括兴安岭、燕山、太行山、秦岭-大别造山带、武陵山以及松辽盆地等 [Deng 2021, pp. 2-2].
- **主要数据**:
  - **重力数据**: 来自地球重力模型（EGM2008），网格间距为2.5 × 2.5 arcmin，区域内数据标准差<5 mGal [Deng 2021, pp. 1-2].
  - **地壳厚度**: 来自横穿NCC的深地震测深（DSS）剖面结果 [Deng 2021, pp. 2-3]（如 Jia et al., 2014; Tian et al., 2014 [Deng 2021, pp. 2-4]）。
  - **岩石圈厚度**: 引用自 Wang et al. (2014) [Deng 2021, pp. 5-5].
  - **地幔成分**: 源自对NSGL两侧橄榄岩包体的Mg#（镁值）研究 [Deng 2021, pp. 5-5].

## Methods
- **重力建模**: 沿一条横穿NSGL的深地震测深（DSS）剖面进行2D多边棱柱体重力正演模拟，以计算不同源（莫霍面、地壳、岩石圈地幔、地幔转换带）的重力效应 [Deng 2021, pp. 1-1][Deng 2021, pp. 4-4].
- **密度-波速转换**: 采用Brocher (2005)的经验关系式，将地震P波速度（Vp）转换为地壳密度 [Deng 2021, pp. 4-4]:
  ```
  ρ (g/cm³) = 1.6612 * Vp - 0.4721 * Vp² + 0.0671 * Vp³ - 0.0043 * Vp⁴ + 0.000106 * Vp⁵
  ```
- **地幔成分分析**: 利用岩石圈地幔包体的Mg#差异来估算地幔密度差异 [Deng 2021, pp. 5-5].

## Key Findings
1.  **地壳厚度是主导因素**: 莫霍面深度变化是造成跨越NSGL重力异常侧向变化的首要原因。NSGL西部地壳厚（>35 km，南秦岭最厚可达~50 km），而东部较薄 [Deng 2021, pp. 2-2][Deng 2021, pp. 5-6].
2.  **岩石圈地幔成分是次要因素**: 仅凭岩石圈地幔密度差异无法产生观测到的NSGL重力模式，但其贡献趋势与观测一致。华北克拉通中部的幔源包体Mg#比东部高约2个单位，导致东部岩石圈地幔密度高出约0.025 g/cm³ [Deng 2021, pp. 5-5][Deng 2021, pp. 5-6].
3.  **形成机制**: NSGL的形成可归因于晚中生代华北克拉通东部的岩石圈减薄和地幔置换作用。这一过程导致NSGL两侧在地壳/岩石圈厚度和岩石圈地幔成分上出现侧向差异 [Deng 2021, pp. 1-1][Deng 2021, pp. 7-7].
4.  **根本驱动力**: 古太平洋板块的俯冲及其在地幔转换带内的滞留，形成了“大地幔楔（BMW）”结构。滞留板块脱水/脱碳释放的挥发分软化了上覆岩石圈，导致岩石圈减薄和克拉通破坏。NSGL代表了华北克拉通被破坏部分的西部边界 [Deng 2021, pp. 6-7][Deng 2021, pp. 7-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 仅考虑莫霍面起伏计算的重力异常与观测值最大偏差>50 mGal，东部偏低，西部偏高。 | [Deng 2021, pp. 4-4] | 模型假设：地幔密度均一（3.3 g/cm³）。 | 表明需要其他因素（如密度）来解释剩余的异常。 |
| 通过在地壳模型中东部增加0.1 g/cm³，西部减少密度，可以很好地拟合观测重力异常。 | [Deng 2021, pp. 4-5] | 模型调整。 | 证明地壳密度差异对NSGL重力模式有贡献。 |
| 华北克拉通中部的橄榄岩Mg#比东部高~2个单位，对应岩石圈地幔密度西低东高，差值约0.03 g/cm³。 | [Deng 2021, pp. 5-5] | 基于橄榄岩包体的化学成分研究。 | 这是岩石圈地幔成分贡献的定量证据。 |
| 仅考虑岩石圈地幔密度异常（东部+0.03 g/cm³）计算的模型重力异常，其趋势与NSGL观测值相似，但不能单独产生观测模式。 | [Deng 2021, pp. 5-6] | 地壳密度和软流圈密度设为恒定值。 | 表明岩石圈地幔成分变化的贡献是次要的。 |

## Limitations
- 重力模拟中假设地幔密度为均一值（3.3 g/cm³）以进行单因素分析 [Deng 2021, pp. 4-4].
- 文中提及地幔中密度相的存在可能被较低的温度所抵消，这表明温度场的分布是模型的一个潜在复杂性因素 [Deng 2021, pp. 6-6].
- 未从索引片段中确认模型对地幔转换带滞留板块的具体建模细节和其对重力场的最终贡献权重。
- 研究重点在华北克拉通（NCC）段，对于NSGL在东北和华南较宽段的形成机制解释可能不是完全适用 [Deng 2021, pp. 2-3].

## Assumptions / Conditions
- **重力建模**: 采用2D多边棱柱体方法，假设地壳密度可从P波速度通过Brocher (2005)的经验公式转换得到 [Deng 2021, pp. 4-4].
- **地幔密度**: 在单独分析莫霍面贡献时，假设地幔（包括岩石圈地幔和软流圈）密度均匀 [Deng 2021, pp. 4-4].
- **成分-密度关系**: 基于Mg#升高1单位对应密度降低约0.4%的经验关系 [Deng 2021, pp. 5-5] (Schutt and Lesher, 2010).
- **构造背景**: 假设晚中生代华北克拉通的破坏是NSGL形成的关键地质事件，并接受太平洋板块俯冲为其驱动力 [Deng 2021, pp. 6-6][Deng 2021, pp. 6-7].

## Key Variables / Parameters
- **布格重力异常 (Bouguer gravity anomaly)**: 单位mGal，NSGL两侧梯度>100 mGal / <100 km [Deng 2021, pp. 1-1].
- **地壳厚度 (Moho depth)**: NSGL以西>35 km，最厚约50 km；东部较薄 [Deng 2021, pp. 2-2].
- **地壳密度 (Crustal density)**: 由Vp经经验公式计算，为拟合重力场，模拟中需加入±0.1 g/cm³的局部密度异常 [Deng 2021, pp. 4-5].
- **岩石圈地幔Mg# (Lithospheric mantle Mg#)**: 镁值，中部NCC比东部NCC高约2个单位，作为地幔亏损/富集程度的指标 [Deng 2021, pp. 5-5].
- **岩石圈地幔密度 (Lithospheric mantle density)**: 东部NCC比西部约高0.03 g/cm³ [Deng 2021, pp. 5-5].
- **岩石圈厚度 (Lithospheric thickness)**: 东部ENCC约80 km，西部WNCC较厚 [Deng 2021, pp. 6-6].

## Reusable Claims
1.  **Claim**: 陆内南北重力线（NSGL）的形成，首要控制因素是地壳厚度的东西向差异，其次才是岩石圈地幔的成分（密度）差异 [Deng 2021, pp. 1-1][Deng 2021, pp. 5-6].
    - **Evidence**: 沿DSS剖面的重力正演模拟显示，莫霍面起伏会产生与NSGL模式相似的巨大重力异常，而仅使用报道的岩石圈地幔密度差异无法复现该模式。加入地壳密度异常后模型拟合良好 [Deng 2021, pp. 4-5][Deng 2021, pp. 5-6].
    - **Conditions**: 适用于NSGL横穿华北克拉通的狭窄段。重力模拟假设了布格异常主要源自地壳和上地幔的贡献。
    - **Limitations**: 该结论基于单条二维剖面的模拟，未考虑三维效应。局部地壳密度异常的具体分布和成因未详细阐明。

2.  **Claim**: 岩石圈地幔的密度差异可以通过橄榄岩的Mg#值差异来定量估算，并体现为布格重力异常的次要贡献 [Deng 2021, pp. 5-5].
    - **Evidence**: 根据包体研究，华北克拉通中部的Mg#比东部高~2单位，按Schutt and Lesher (2010)的关系式，这导致东部地幔密度比西部高约0.03 g/cm³。将这一密度差用于重力模拟，所产生的重力趋势与观测相同，但幅度上不是一个量级 [Deng 2021, pp. 5-6].
    - **Conditions**: 假设Mg#与密度的经验关系（1单位Mg#增加 ~ 密度降低0.4%）在此成立；假设包体数据能代表大尺度岩石圈地幔成分。
    - **Limitations**: 这是一个统计和简化假设，忽略了温度、挥发分和其他矿物相对密度的复杂影响。

3.  **Claim**: NSGL是华北克拉通东部在中生代被破坏的地表地质和地球物理响应边界，其根源在于古太平洋板块的俯冲 [Deng 2021, pp. 6-7][Deng 2021, pp. 7-7].
    - **Evidence**: NSGL与多种地质地球物理场突变界限重合，如岩石圈厚度、地壳厚度。这些变化以NSGL为界，东部表现为岩石圈减薄、地幔由难熔变富集、以及克拉通破坏的特征。西部古老的克拉通克拉通则保存完整。
    - **Conditions**: 此关联建立在地球物理观测（层析成像显示滞留板块的西缘与NSGL重合）和地质事件（晚中生代两期主要岩浆活动与俯冲及伸展对应）的基础之上 [Deng 2021, pp. 6-7].
    - **Limitations**: 滞留板块是“大地幔楔”结构的一部分，但其目前的成像可能是较新的特征（<30 Ma），与导致克拉通破坏的古老俯冲过程之间的具体演化关系仍在讨论中 [Deng 2021, pp. 7-7].

## Candidate Concepts
- [[intracontinental gravity lineament]]
- [[North-South Gravity Lineament (NSGL)]]
- [[Bouguer gravity anomaly]]
- [[North China Craton destruction]]
- [[big mantle wedge (BMW)]]
- [[stagnant slab]]
- [[mantle transition zone (MTZ)]]
- [[Mg# as mantle fertility indicator]]
- [[lithospheric thinning and replacement]]
- [[crustal isostasy]]

## Candidate Methods
- [[2D gravity forward modeling]]
- [[density conversion from Vp using Brocher (2005) formula]]
- [[analysis of mantle xenolith geochemistry]]
- [[deep seismic sounding (DSS) profile]]
- [[comparative geophysical-petrological analysis]]

## Connections To Other Work
- **地壳厚度**: 使用了 Jia et al. (2014) 和 Tian et al. (2014) 的DSS剖面结果来约束莫霍面深度 [Deng 2021, pp. 2-4].
- **岩石圈厚度**: 参考了 Wang et al. (2014) 的岩石圈厚度模型 [Deng 2021, pp. 5-5].
- **地幔成分**: 大量引用了关于NCC橄榄岩包体的研究以约束Mg#差异 [Deng 2021, pp. 5-5]，例如 (Polat et al., 2006; Zheng et al., 2007; Xu et al., 2008).
- **大地幔楔与滞留板片**: 将研究结果与此构造模型联系起来，引用了通过地震层析成像发现该结构的文献 [Deng 2021, pp. 6-7] (Zhao et al., 2004; Lei and Zhao, 2005).
- **华北克拉通破坏**: 此工作建立的NSGL形成机制是华北克拉通破坏研究的一个地球物理维度的补充，与Menzies et al. (1993), Griffin et al. (1998) 和 Xu (2001) 等人的克拉通破坏模型相联系 [Deng 2021, pp. 6-6].
- **方法连接**: 所使用的P波速度转密度公式源自 Brocher (2005) [Deng 2021, pp. 4-4]；Mg#与密度的关系参考了 Schutt and Lesher (2010) [Deng 2021, pp. 5-5].

## Open Questions
- 在东北和华南地区，NSGL变得宽阔而弥散，文中提出的以地壳厚度为主、地幔成分为辅的形成机制是否仍然适用？ [Deng 2021, pp. 1-2].
- 古老的、中生代的板块滞留过程如何与地震学成像显示的、可能较年轻（<30 Ma）的滞留板片结构在时间上演化并联系起来？ [Deng 2021, pp. 7-7].
- 未从索引片段中确认是否有对软流圈对流、地壳内局部密度异常体的成因进行更深入的探讨。

## Source Coverage
本页面基于该论文的13个索引片段生成。片段覆盖了摘要、引言、方法（重力数据、建模思路）、主要结果和讨论部分。内容足以勾勒出研究的核心科学问题、主要方法、关键发现和主导解释模型。特别是关于重力建模的过程、地壳厚度与地幔成分的定量贡献、以及地质成因解释的片段较为详细。然而，片段可能缺失了结果中的详细数值验证、更精细的敏感性测试、以及结论中对其他可能的次要因素（如沉积层、软流圈）的详尽讨论。因此，本总结可能未涵盖论文的全部论证细节，但已捕捉其核心论证链条。
