---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-mirzaei-paiaman-a-new-approach-to-measure-wettability-by-relative-permeability-measurements"
title: "A New Approach to Measure Wettability by Relative Permeability Measurements."
status: "draft"
source_pdf: "data/papers/2022 - A new approach to measure wettability by relative permeability measurements.pdf"
collections:
citation: "Mirzaei-Paiaman, Abouzar, et al. \"A New Approach to Measure Wettability by Relative Permeability Measurements.\" *Journal of Petroleum Science and Engineering*, vol. 208, 2022, 109191. doi:10.1016/j.petrol.2021.109191. Accessed 2 Dec. 2026."
indexed_texts: "16"
indexed_chars: "79670"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:37:05"
---

# A New Approach to Measure Wettability by Relative Permeability Measurements.

## One-line Summary
提出一种基于油水相对渗透率曲线下方面积的新润湿性指数（modified Lak），并在20个碳酸盐岩样品上验证其适用性 [Mirzaei 2022, pp.1-2]。

## Research Question
如何利用相对渗透率数据发展一种新的、更稳健的定量表征平均润湿性的方法，以克服传统Amott-Harvey和USBM指数的局限性 [Mirzaei 2022, pp.1-3]?

## Study Area / Data
- **岩石样品:** 20个圆柱形柱塞样品（直径1.5英寸，长度2英寸），取自全尺寸岩心，分属两个数据集 [Mirzaei 2022, pp.4-5]。
- **地质背景:** 第一个数据集包含8个样品，来自中东某油田的Asmari储层，岩性为非均质 [Mirzaei 2022, pp.5]。第二个数据集为碳酸盐岩[未从索引片段确认具体油田]。综合岩性为碳酸盐岩储层 [Mirzaei 2022, pp.1]。
- **岩石类型:** 基于FZI*值划分为多个GHE*类，样品分布在岩石类型3至6之间 [Mirzaei 2022, pp.5-6]。
- **实验流体:** 模拟盐水（NaCl溶液，矿化度190 g/L）；合成油（正癸烷）；储层死油（饱和分13.16%，芳香分75.03%，胶质10.80%，沥青质1.01%）[Mirzaei 2022, pp.6-7]。
- **实验条件:** 测试温度50°C（毛细管压力）和70°C（老化恢复润湿性）[Mirzaei 2022, pp.6-7]。

## Methods
- **实验流程:**
    1.  样品准备与饱和：水湿样品先饱和模拟盐水并浸泡至少10天以达到离子平衡 [Mirzaei 2022, pp.5]。
    2.  基础物性测量：测量盐水绝对渗透率；然后进行初次排驱水-油毛细管压力实验，获得完整的初次排驱毛管压力曲线 [Mirzaei 2022, pp.5-6]。
    3.  润湿性恢复：样品在残余水饱和度下，于70°C储层温度的死油中老化15天，期间冲洗原油两次以确保润湿性均匀改变 [Mirzaei 2022, pp.6]。
    4.  润湿性实验：老化后，进行初次渗吸相对渗透率测量，以及初次渗吸和二次排驱毛细管压力测量 [Mirzaei 2022, pp.1, 6]。
- **新方法原理:**
    - 理论依据：在油湿系统中，水的相对渗透率平均高于油；在水湿系统中则相反。因此，相对渗透率曲线下的面积（Ao 和 Aw）包含了润湿性信息 [Mirzaei 2022, pp.3-5]。
    - 物理类比：流动一个流体所需做的“比功”与相对渗透率成反比。分析曲线下方面积等同于分析流体流动所需的比功 [Mirzaei 2022, pp.4-5]。
- **新指数定义:**
    - **Modified Lak 指数 (I_{L-Modified}):** I_{L-Modified} = (Ao - Aw) / (Ao + Aw)。其中，Ao 和 Aw 分别是整个饱和度变化区间（S_{wir} 到 1 - S_{or}）内油和水的相对渗透率曲线下方面积 [Mirzaei 2022, pp.4]。
- **对比指数计算:**
    - **Amott-Harvey 指数 (I_AH):** I_AH = I_w - I_o，基于自发和强制渗吸/排驱的饱和度变化 [Mirzaei 2022, pp.2-3, 7]。
    - **USBM 指数 (W):** W = log(A1 / A2)，其中 A1 和 A2 分别是强制二次排驱和强制渗吸毛细管压力曲线下的面积 [Mirzaei 2022, pp.2-3, 7]。
    - **原始 Lak 指数 (I_L):** 基于 Craig 规则，利用相对渗透率曲线上的特定点（如 k_rw@S_or, CS）计算 [Mirzaei 2022, pp.3, 7]。

## Key Findings
- **总体润湿性:** 所有指数（USBM, Amott-Harvey, Lak, modified Lak）均预测所测试的碳酸盐岩样品为油湿 [Mirzaei 2022, pp.1-2]。
- **指数变异性:** USBM 指数对应的变化范围最广，而新提出的 modified Lak 指数变化范围最小。Amott-Harvey 和 Lak 指数的变化范围介于两者之间，且相似 [Mirzaei 2022, pp.1-2]。
- **理论观察:** 随着水湿性增强，相对渗透率曲线的交叉点向更高含水饱和度移动，接近 1 - S_or；随着油湿性增强，交叉点向更低含水饱和度移动，接近 S_wir [Mirzaei 2022, pp.3-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Modified Lak 指数 (I_{L-Modified}) 定义为 (Ao - Aw) / (Ao + Aw) | [Mirzaei 2022, pp.4] | 适用于计算水和油相对渗透率曲线下方面积 | Ao 和 Aw 的区域覆盖从 S_wir 到 1 - S_or 的整个饱和度变化区间。 |
| 所有测试的润湿性指数（USBM， Amott-Harvey， Lak， Modified Lak）均表明所测碳酸盐岩为油湿 | [Mirzaei 2022, pp.1-2] | 实验在20个碳酸盐岩样品上进行，流体为模拟盐水和储层死油/合成油 | 无。 |
| USBM 指数展示了最广的变化范围，而 Modified Lak 指数展示了最小的变化范围 | [Mirzaei 2022, pp.1-2] | 基于对20个样品的测量结果对比 | Amott-Harvey 和 Lak 指数变化范围相似，并介于 USBM 和 Modified Lak 之间。 |
| 水湿系统中，水相相对渗透率平均低于油相；在 RCS 处，水相相对渗透率应低于油相，且曲线交点位于 RCS 右侧 | [Mirzaei 2022, pp.3-4] | 这是基于水湿条件下水优先占据小孔隙和孔壁的流动行为分析 | RCS 指残余油和束缚水之间的中点饱和度。 |
| 油湿系统中，油相相对渗透率平均低于水相；在 RCS 处，油相相对渗透率应低于水相，且曲线交点位于 RCS 左侧 | [Mirzaei 2022, pp.3-4] | 这是基于油湿条件下油以薄膜形式在大孔隙壁上流动的分析 | 无。 |

## Limitations
- 该方法仅通过碳酸盐岩样品进行验证，其在其他岩性（如砂岩）中的适用性未从索引片段中确认。
- 实验流体和条件（如特定原油成分、温度、盐水组成）是特定的，该指数在不同流体-岩石体系中的表现需要通过更多实验来验证。
- 新提出的 modified Lak 指数基于相对渗透率曲线下面积的积分，因此其可靠性依赖于获得完整、高质量的非稳态相对渗透率数据。文中提到，这些数据可视为对稳态实验真实润湿性的估算 [Mirzaei 2022, pp.7]。

## Assumptions / Conditions
- **模型假设:** 该方法的核心假设是，润湿性可以通过流动过程中流体所需做的“比功”来反映，而该比功与相对渗透率成反比，并可由相对渗透率曲线下方面积来量化 [Mirzaei 2022, pp.4-5]。
- **实验条件:** 润湿性恢复过程假设在70°C下用死油老化15天能够有效恢复储层原始润湿状态 [Mirzaei 2022, pp.6]。
- **数据条件:** 计算新指数需要一次完整的渗吸相对渗透率曲线（从束缚水饱和度 S_wir 到残余油饱和度 S_or） [Mirzaei 2022, pp.4]。

## Key Variables / Parameters
- **I_{L-Modified}:** 修正的 Lak 润湿性指数 [Mirzaei 2022, pp.4]
- **A_o & A_w:** 分别为油和水的相对渗透率曲线在整个饱和度变化区间下的面积 [Mirzaei 2022, pp.4]
- **I_AH:** Amott-Harvey 润湿性指数 [Mirzaei 2022, pp.2]
- **USBM指数 (W):** W = log(A1/A2) [Mirzaei 2022, pp.3]
- **I_L:** 原始 Lak 润湿性指数 [Mirzaei 2022, pp.3]
- **CS:** 油水相对渗透率曲线交点处的含水饱和度 [Mirzaei 2022, pp.3]
- **k_rw@S_or:** 残余油饱和度下的水相相对渗透率（最大值）[Mirzaei 2022, pp.3]
- **RCS:** 残余油和束缚水之间的中间饱和度，即 (S_wir + (1 - S_or))/2 [Mirzaei 2022, pp.3]
- **S_wir:** 束缚水饱和度。**S_or:** 残余油饱和度。[Mirzaei 2022, pp.3]
- **FZI*:** 流动带指标，FZI* = 0.0314 * sqrt(K/φ) [Mirzaei 2022, pp.5]

## Reusable Claims
- **Claim 1:** 可以利用油水相对渗透率曲线下面积的差异来构建润湿性指数。[[new wettability index, modified Lak]] 定义为 I_{L-Modified} = (A_o - A_w) / (A_o + A_w)，该值在油湿时为负，在水湿时为正 [Mirzaei 2022, pp.4]。**限制:** 该指数的性能仅在碳酸盐岩上得到验证，其普适性有待考证。
- **Claim 2:** USBM 指数可能对润湿性的微小变化更敏感，表现为较大的数值范围；而新提出的 modified Lak 指数可能对[[heterogeneity]]或数据波动具有更强的鲁棒性，表现为更窄的变化范围 [Mirzaei 2022, pp.1-2]。**条件:** 这一结论是基于20个碳酸盐岩样品的实验结果。
- **Claim 3:** 在基于相对渗透率的润湿性分析中，随着[[water-wetness]]增强，油水相对渗透率曲线的交叉点向更高含水饱和度移动（接近 1 - S_or）；随着[[oil-wetness]]增强，交叉点向更低含水饱和度移动（接近 S_wir）[Mirzaei 2022, pp.3-4]。

## Candidate Concepts
- [[wettability]]
- [[relative permeability]]
- [[capillary pressure]]
- [[wettability index]]
- [[Amott-Harvey index]]
- [[USBM index]]
- [[Lak index]]
- [[carbonate reservoir]]
- [[porous media]]
- [[wettability alteration]]
- [[specific work]]

## Candidate Methods
- [[relative permeability measurement]]
- [[capillary pressure measurement (centrifuge)]]
- [[steady-state relative permeability]]
- [[unsteady-state relative permeability]]
- [[forced imbibition]]
- [[secondary drainage]]
- [[contact angle measurement]]
- [[wettability restoration (aging)]]
- [[core flooding]]

## Connections To Other Work
- 本研究继承并批判了传统润湿性表征方法，包括 Amott、Harvey 提出的 [[Amott-Harvey index]] 和 Donaldson 等人提出的 [[USBM index]] [Mirzaei 2022, pp.2-3]。
- 新提出的指数是对 [[Lak index]] 的改进，Lak 指数本身又是基于 [[Craig's rules of thumb]] 推导而来 [Mirzaei 2022, pp.3-4]。
- 关于润湿性对相对渗透率影响的定性描述，参考了 Brooks and Corey 等人的早期研究 [Mirzaei 2022, pp.3]。

## Open Questions
- 这个新的 modified Lak 指数在砂岩或其他非碳酸盐岩储层中的表现如何？其在更广泛岩石类型和流体组合中的普适性尚未确认。
- 相对渗透率测量通常具有滞后效应，该新指数对饱和度路径的依赖程度如何？当前实验仅覆盖了初次渗吸过程 [Mirzaei 2022, pp.1]。
- 指数变化范围小（稳健性）是否意味着在某些情况下（如接近中性润湿时）分辨率下降？
- 该指数如何与孔隙尺度的物理机制（如接触角、界面张力、孔隙结构）建立更直接的联系未在索引片段中深入讨论。
- 该新指数在预测[[CO2 storage]]、[[secondary oil recovery]]和[[tertiary oil recovery]]等实际工程过程中的表现如何，文中虽提及这些应用是重要的，但未给出基于新指数的预测或验证 [Mirzaei 2022, pp.1]。

## Source Coverage
- **依据片段:** 此 Wiki 页面严格依据16个索引片段编写。
- **覆盖范围:** 片段主要覆盖了论文的摘要、引言、问题陈述、核心理论部分、实验材料与方法以及初步的实验结果陈述。包含了详实的公式推导、实验流程和新旧指数对比的核心发现。
- **信息缺失提示:** 索引片段未覆盖论文的“结果与讨论”后部（如“correlations between different indices, and the change of wettability indices vs....”提到的相关性分析）、完整的“结论”部分、对未来工作的建议、所有作者的联系信息，以及图表的完整数据和详细分析。因此，本页面无法提供关于各指数间定量关系、讨论的全部细节以及作者声明的所有局限性和展望。
