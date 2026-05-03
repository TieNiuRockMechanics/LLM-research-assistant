---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-mirzaei-paiaman-a-new-approach-to-measure-wettability-by-relative-permeability-measurements"
title: "A New Approach to Measure Wettability by Relative Permeability Measurements."
status: "draft"
source_pdf: "data/papers/2022 - A new approach to measure wettability by relative permeability measurements.pdf"
collections:
citation: "Mirzaei-Paiaman, Abouzar, et al. \"A New Approach to Measure Wettability by Relative Permeability Measurements.\" *Journal of Petroleum Science and Engineering*, vol. 208, 2022, 109191. doi:10.1016/j.petrol.2021.109191. Accessed 2 Dec. 2026."
indexed_texts: "16"
indexed_chars: "79670"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "76287"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.957537"
coverage_status: "full-index"
source_signature: "5befd3664140606b54860cf370484eee84af11cc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:57:44"
---

# A New Approach to Measure Wettability by Relative Permeability Measurements.

## One-line Summary
本文基于油水相对渗透率曲线下方面积定义了一种新的润湿性指数（改进 Lak 指数），在二十块碳酸盐岩样品上验证了其适用性，并与 Amott‑Harvey、USBM 和 Lak 指数进行了对比，发现各类指数应互补使用。

## Research Question
如何仅利用相对渗透率测量数据，通过曲线包围面积定量表征多孔介质的平均润湿性，以克服现有经验指数（如 Amott‑Harvey、USBM）的局限，并为优先流动路径的润湿倾向提供更贴近流动过程的评价。

## Study Area / Data
**研究区**：  
- 数据集 1：中东某油田 Asmari 储层，岩性为灰岩和白云岩，含少量硬石膏、砂和伊利石，8 块深度 2775.7 m~2850.7 m 的柱塞样。  
- 数据集 2：中东另一油田 Fahlian 储层，岩性以灰岩为主，12 块深度 4017.2 m~4092 m 的柱塞样。  

**数据**：  
- 一次渗吸水驱油相对渗透率（非稳态）；一次渗吸和二次排替毛管压力（离心法）；岩石基本物性（氦孔隙度、空气渗透率、FZI*、GHE* 岩石类型）表 1，[Mirzaei 2022, pp. 5-6]。  
- 流体性质：模拟盐水（NaCl 190 g/L）、合成油（正癸烷）、脱气原油表 2，[Mirzaei 2022, pp. 6-7]。

## Methods
1. **样品制备与老化**：按 API RP40 清洗、干燥，用模拟盐水和脱气原油在 70 °C 下老化 15 天恢复原始润湿性[Mirzaei 2022, pp. 5-6]。  
2. **相对渗透率测试**：非稳态水驱油，采用 Jones & Roszelle（1978）图解法计算油水相对渗透率[Mirzaei 2022, pp. 6-7]。  
3. **毛管压力测试**：通过离心机进行强渗吸和二次排替，得到正负毛管压力曲线，用于计算 USBM 和 Amott 指数[Mirzaei 2022, pp. 7-8]。  
4. **新指数定义**：  
   - 由水相相对渗透率曲线下方面积 \(A_w\) 和油相曲线下方面积 \(A_o\)（从 \(S_{wir}\) 到 \(1-S_{or}\) 积分）构建改进 Lak 指数：  
     \[
     I_{ML} = \frac{A_o - A_w}{A_o + A_w}
     \]
     取值范围 \([-1, +1]\)，正值对应水湿，负值对应油湿[Mirzaei 2022, pp. 3-4]。  
5. **对比分析**：计算同一批样品的 Amott‑Harvey、USBM、Lak 和 \(I_{ML}\)，进行交会图和相关分析[Mirzaei 2022, pp. 8-9, 9‑11]。

## Key Findings
1. **润湿性状态**：测试的碳酸盐岩总体呈油湿特征，五个样品中仅第二数据集的样品 12 出现异常（Amott‑Harvey 负而其他指数正）[Mirzaei 2022, pp. 8-9, 9‑9]。  
2. **指数变化范围**：  
   - USBM 变化范围最宽（数据集 1：‑0.95 ~ ‑0.21；数据集 2：‑1.55 ~ 0.05）。  
   - 改进 Lak 指数变化范围最窄（数据集 1：‑0.41 ~ 0.00；数据集 2：‑0.49 ~ 0.20）。  
   - Amott‑Harvey 和 Lak 变化幅度居中且相近表 4 和表 5，[Mirzaei 2022, pp. 8, 9]。  
3. **指数间相关性**：  
   - 改进 Lak 与 Lak 相关性最高（数据集 1 \(R^2=0.66\)，数据集 2 \(R^2=0.85\)）。  
   - 改进 Lak 与 Amott‑Harvey 存在较好相关性（\(R^2=0.58\) 和 \(0.65\)）。  
   - USBM 与基于相对渗透率的指数相关性较差[Mirzaei 2022, pp. 8-9, 9‑11]。  
4. **深度变化**：在油柱段内，各指数随深度无明显单调趋势，但不同指数随深度变化的增减方向基本一致[Mirzaei 2022, pp. 9, 9‑11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 二十块碳酸盐岩的 Amott、USBM、Lak 和 \(I_{ML}\) 指数值均指向油湿（除样品 12 外）。 | [Mirzaei 2022, pp. 7-9] | 洗油恢复润湿性，非稳态水驱油相对渗透率，离心毛管压力。 | 样品来自两个油田的不同储层，岩性为灰岩/白云岩。 |
| \(I_{ML}\) 的变幅在所有指数中最小，而 USBM 最大。 | [Mirzaei 2022, pp. 8, 9] | 同上。 | 表明 \(I_{ML}\) 可能对润湿差异更“保守”。 |
| 改进 Lak 与 Lak 的相关系数 \(R^2\) 达 0.85（数据集 2）。 | [Mirzaei 2022, pp. 9-11] | 两者均源自相对渗透率分析。 | 二者走势高度一致但 \(I_{ML}\) 偏水湿一侧。 |
| Amott‑Harvey 在近中性润湿时可能不敏感，而 \(I_{ML}\)、Lak、USBM 能保持敏感。 | [Mirzaei 2022, pp. 11] | 理论论证，非本实验直接结论。 | 引自 Anderson (1986a,b)。 |
| 油水相对渗透率曲线下方面积的差异反映流体流动所需比功的大小。 | [Mirzaei 2022, pp. 4-5] | 基于 TEM‑function 的物理推演。 | 新指数的物理基础。 |

## Limitations
- **相对渗透率数据可靠性**：非稳态试验仅提供突破后的饱和度区间数据，若突破晚则难以计算曲线下面积；此时推荐使用 Lak 指数[Mirzaei 2022, pp. 11]。  
- **数据缺失处理**：非稳态试验近束缚水饱和度段数据缺失，需借助曲线拟合计算面积，尤其影响油相面积[Mirzaei 2022, pp. 11]。  
- **粘度影响未完全排除**：假设相对渗透率不受粘度显著影响，若粘度比变化大则建议使用同一数量级粘度比的数据[Mirzaei 2022, pp. 11]。  
- **不适用于所有岩样类型**：强非均质、裂缝性样品影响相对渗透率获取的准确性（未明确实验验证，但提及局限）。  
- **指数非绝对量度**：所有润湿性指数均不能独立作为绝对测量，需多种方法互补[Mirzaei 2022, pp. 11-12]。

## Assumptions / Conditions
- 采用一次渗吸相对渗透率（非稳态）可以近似反映稳态润湿性信息[Mirzaei 2022, pp. 6-7]。  
- 相对渗透率数据覆盖完整或大部分饱和度变化区间，以保证面积计算准确[Mirzaei 2022, pp. 3]。  
- 毛管末端效应已被抑制，实验选用的驱替速度基于无量纲毛管数确定[Mirzaei 2022, pp. 6]。  
- 归一化处理（\(I_{ML}\)）能消除孔隙网络几何和界面张力的影响[Mirzaei 2022, pp. 11]。  
- 试验流体粘度比保持在合理范围内，不会显著改变相对渗透率曲线特征[Mirzaei 2022, pp. 11]。

## Key Variables / Parameters
- \(I_{ML}\)：改进 Lak 润湿性指数，由 \(A_o\) 和 \(A_w\) 归一化差值决定。  
- \(A_o, A_w\)：油、水相对渗透率曲线从 \(S_{wir}\) 至 \(1-S_{or}\) 的积分面积。  
- \(S_{wir}, S_{or}\)：束缚水饱和度、残余油饱和度。  
- \(k_{rw\ @\ S_{or}}\)：残余油饱和度下的最大水相相对渗透率。  
- \(CS\)：相对渗透率曲线交点的水饱和度。  
- \(RCS\)：参考交点饱和度，\(RCS = 0.5 + S_{wir}/2 - S_{or}/2\)[Mirzaei 2022, pp. 3]。  
- \(W\)（USBM 指数）：\(W = \log_{10}(A_1/A_2)\)，\(A_1\)、\(A_2\) 分别为二次排替和强渗吸毛管压力曲线下方面积。  
- \(I_{AH}\)：Amott‑Harvey 指数，\(I_w - I_o\)。  
- \(I_L\)：Lak 指数，整合了改进 Craig 第二法则和最大水相渗透率判据。

## Reusable Claims
1. **\(I_{ML}\) 与润湿性关系**：在油水系统中，当 \(I_{ML} > 0\) 时为水湿，\(I_{ML} < 0\) 时为油湿，绝对值越大润湿性越强。该关系仅适用于从 \(S_{wir}\) 到 \(1-S_{or}\) 全覆盖的相对渗透率曲线[Mirzaei 2022, pp. 4]。  
2. **面积差异的物理意义**：水湿系统 \(A_w < A_o\)，油湿系统 \(A_w > A_o\)，因为润湿相在大孔隙壁面流动时能量耗散大，导致相对渗透率整体偏低[Mirzaei 2022, pp. 3-4]。  
3. **\(I_{ML}\) 变幅特征**：与 USBM、Amott‑Harvey 和 Lak 相比，\(I_{ML}\) 给出的润湿性变化范围更窄，可能对润湿差异的刻画更保守[Mirzaei 2022, pp. 8-9]。  
4. **指数间相关性**：\(I_{ML}\) 与 Lak 的相关性最好，与 Amott‑Harvey 次之，与 USBM 的相关性不稳定[Mirzaei 2022, pp. 8-9, 9‑11]。  
5. **互补使用原则**：任何单一指数都不能作为润湿性的绝对量度，建议同时采用多种指数综合判断[Mirzaei 2022, pp. 11-12]。  
6. **流动相关润湿性**：基于相对渗透率的指数反映的是优先参与流动的大孔道网络的润湿倾向，而非全孔隙空间的平均润湿性[Mirzaei 2022, pp. 9-10]。

## Candidate Concepts
- [[改进 Lak 润湿性指数]] (modified Lak wettability index)  
- [[一次渗吸相对渗透率]] (primary imbibition relative permeability)  
- [[参考交点饱和度 RCS]] (Reference Crossover Saturation)  
- [[动态空间]] (dynamic saturation change interval)  
- [[TEM‑function 真有效流度]] (True Effective Mobility)  
- [[非稳态相对渗透率]] (unsteady-state relative permeability)  
- [[自吸与强迫驱替毛管压力]] (spontaneous/forced capillary pressure)  
- [[润湿性互补分析]] (complementary wettability assessment)  
- [[孔隙尺度润湿性]] (pore-scale wettability)  
- [[FZI*]] 和 [[GHE* 岩石分类]]

## Candidate Methods
- [[非稳态水驱油相对渗透率测量]] (unsteady-state waterflood relative permeability measurement)  
- [[Jones‑Roszelle 图解法]] (Jones & Roszelle graphical method)  
- [[离心法毛管压力测试]] (centrifuge capillary pressure measurement)  
- [[改进 Lak 指数计算法]] (modified Lak index calculation from relative permeability)  
- [[Amott‑Harvey 指数计算]] (Amott-Harvey wettability index)  
- [[USBM 润湿性评价]] (USBM wettability index)  
- [[Lak 润湿性指数]] (Lak wettability index)  
- [[GHE* 岩石类型模版]] (Global Hydraulic Element template)  
- [[Soxhlet 抽提清洗]] 与 [[API RP40 岩心制备]]

## Connections To Other Work
- 本文提出的改进 Lak 指数直接继承并扩展了 Mirzaei‑Paiaman (2021) 的 Lak 指数（基于改进 Craig 第二法则与 Craig 第一法则的组合），将仅用若干特征点升级为运用整条相对渗透率曲线下方面积[Mirzaei 2022, pp. 3-4]。  
- 物理基础的阐释引用了 Mirzaei‑Paiaman et al. (2019) 的 TEM‑function 概念，将面积差异转化为流体流动所需比功的差异[Mirzaei 2022, pp. 4-5]。  
- 与经典润湿性指数（Amott 1959, Donaldson et al. 1969, Boneau & Clampitt 1977）进行系统比较，指出 USBM 与 Amott‑Harvey 只在某些系统中等价（Dixit et al. 1998, 2000）[Mirzaei 2022, pp. 8-9]。  
- 讨论了文献中关于粘度对相对渗透率影响的两类观点（Leverett 1939 等 vs Odeh 1959 等），建议保持粘度比在同一数量级以降低不确定性[Mirzaei 2022, pp. 11]。  
- 与基于自发渗吸体积的润湿性指数（Longeron et al. 1995, Ma et al. 1999 等）以及 NMR 润湿性方法（Chen et al. 2006, Strand et al. 2006 等）形成对比，突出相对渗透率方法无需额外实验的优势[Mirzaei 2022, pp. 2]。

## Open Questions
- 改进 Lak 指数在稳态相对渗透率数据上的表现是否与非稳态一致，尚缺少直接对比。  
- 当样品突破时间极晚（如致密岩）时，如何可靠地重构缺失段的相对渗透率以计算曲线下面积，文中仅建议采用曲线拟合，但未给出具体优选模型。  
- 文中假设归一化可消除界面张力与孔隙结构效应，但未通过不同界面张力系统进行验证。  
- 对于混合润湿性、分润湿性体系，基于整体面积平均的指数能否准确反映不同润湿相的占优规律，有待孔隙尺度的进一步研究。  
- 改进 Lak 指数与其他定量润湿性指标（例如接触角成像、NMR 润湿指数）的直接标定关系尚未建立。

## Source Coverage
所有非空索引片段已全部处理。共覆盖 16 个源片段（100%），字符覆盖比 95.75%，处理阶段为单次编译（single-pass-markdown），源签名 5befd3664140606b54860cf370484eee84af11cc。
