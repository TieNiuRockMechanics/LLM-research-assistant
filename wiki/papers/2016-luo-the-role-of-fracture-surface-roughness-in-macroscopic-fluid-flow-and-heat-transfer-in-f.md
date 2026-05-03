---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-luo-the-role-of-fracture-surface-roughness-in-macroscopic-fluid-flow-and-heat-transfer-in-f"
title: "The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2016 - The role of fracture surface roughness in macroscopic fluid flow and heat transfer in fractured rocks.pdf"
collections:
  - "zotero new"
  - "雷恩学派分形研究"
citation: "Luo, Shuang, et al. \"The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 87, 2016, pp. 29-38, doi:10.1016/j.ijrmms.2016.05.006."
indexed_texts: "8"
indexed_chars: "38845"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38981"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003501"
coverage_status: "full-index"
source_signature: "32e8c838e630506dd31e31aa340a873b657b38d1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:21:15"
---

# The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks.

## One-line Summary
裂隙表面粗糙度通过改变水力隙宽影响裂隙网络宏观流体流动与传热，其作用程度主要取决于所采用的机械‑水力隙宽经验模型，当使用预测显著减小水力隙宽的模型（如 Barton 模型）时影响至关重要。[Luo 2016, pp. 1-2, 9-10]

## Research Question
如何评估裂隙局部表面粗糙度在裂隙网络宏观尺度上对流体流动和传热过程的影响？特别是，基于现场粗糙度统计分布和不同机械‑水力隙宽关系，量化粗糙度分布类型（正态/对数正态）及隙宽比模型对宏观渗透性和热突破行为的作用。[Luo 2016, pp. 1-2]

## Study Area / Data
- **粗糙度数据**：来自瑞典 Oskarshamn/Forsmark 的 175 条裂隙样本（经直剪试验反算 JRC）和伊朗 Bakhtiary 大坝的 106 条裂隙/层面样本（基于分维数估算 JRC）[Luo 2016, pp. 2-3]。  
- **DFN 几何参数**：采用英国 Cumbria 的 Sella 场区统计几何参数，建立边长 5 m 的方形 DFN 模型，超过表征单元体（REV）尺寸。[Luo 2016, pp. 4-5]

## Methods
- **粗糙度分布拟合**：用卡方拟合优度检验确定最佳概率分布，Oskarshamn/Forsmark 数据符合正态分布（μ=7.5，σ=3.3），Bakhtiary 数据符合对数正态分布（μ=1.7，σ=0.5）[Luo 2016, pp. 2-3]。  
- **机械‑水力隙宽模型**：选用 Barton et al. 的 \( e/E = (JRC/2.5)^{1/2} \) 和 Li & Jiang (2013) 的模型（函数依赖于 \( Z_2 \) 及雷诺数），后者通过 Tse & Cruden 关系由 JRC 换算 \( Z_2 \)。[Luo 2016, pp. 3-4]  
- **DFN 建模与求解**：在 COMSOL Multiphysics 中构建二维 DFN 模型，忽略基质渗透性，假设单相流，采用有限元法求解裂隙内达西流及基质热传导方程，局部热平衡假设。[Luo 2016, pp. 4-5]  
- **参数设置**：机械隙宽固定为 6.5 μm、65 μm 和 650 μm；设置四种 JRC 配置（正态分布、对数正态分布、与正态同均值同方差的对数正态分布、零粗糙度平行板参考案例），每种 5 次实现，共 91 个模型。[Luo 2016, pp. 4-5]

## Key Findings
1. **JRC 分布与流动**：正态 JRC 分布的 DFN 模型渗透性低于对数正态分布的模型；当两种分布具有相同均值和方差时，流量差异减小。[Luo 2016, pp. 5-6, 9-10]
2. **e/E 模型的决定性作用**：使用 Barton 模型时，粗糙度导致总流量大幅下降（Case 1 降低 93.8%，Case 2 降低 71.7%，Case 3 降低 90.7%）；而 Li & Jiang 模型仅使流量减少约 6‑8%，影响可近似忽略。[Luo 2016, pp. 5-6, 9-10]
3. **机械隙宽依赖性**：Barton 模型中，机械隙宽越大粗糙度影响越小（650 μm 时几乎无影响）；Li & Jiang 模型的影响与机械隙宽无关。[Luo 2016, pp. 5-6]
4. **热传递行为**：Barton 模型导致更慢的热前缘移动和拖尾更明显的温度突破曲线，各实现间温度分布差异较大；Li & Jiang 模型下各实现几乎一致。[Luo 2016, pp. 6-9]
5. **实现的可变性**：Barton 模型下不同实现的流量变异系数可达 13%，需要多次实现反映行为；Li & Jiang 模型下变异系数仅约 0.2%，单次实现即可代表。[Luo 2016, pp. 5-6, 9-10]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Oskarshamn/Forsmark JRC 符合正态分布 N(7.5,3.3)，Bakhtiary 符合对数正态分布 LN(1.7,0.5) | [Luo 2016, pp. 2-3, Table 1] | 卡方检验显著性水平 10% | 两类裂隙岩体的粗糙度分布不相同 |
| Barton 模型使归一化总流量降低至 0.062‑0.283（E=65 μm），Li & Jiang 模型仅降至 0.92‑0.93 | [Luo 2016, pp. 5-6, Fig. 8] | DFN 边长 5 m，水平压力梯度 10^5 Pa/m | Barton 模型下 JRC 分布类型对流量更敏感 |
| Barton 模型下流量变异系数 9.2‑13.0%（E=6.5 μm），Li & Jiang 模型 0.2%（各 E） | [Luo 2016, pp. 5-6, Table 4] | 5 次实现统计 | 重复性需求取决于 e/E 模型 |
| 温度突破曲线在 Barton 模型下更平缓，热前缘移动更慢，且实现之间存在差异 | [Luo 2016, pp. 6-8, Fig. 10‑12] | 注入冷水 50 ℃，初始岩温 200 ℃ | 粗糙度通过改变流场影响热传递 |

## Limitations
- 模拟为二维，结论外推至三维需系统验证 [Luo 2016, pp. 9-10]。
- 未考虑裂隙粗糙度在实际力学过程中的动态变化、裂隙填充物以及热应力等因素 [Luo 2016, pp. 9-10]。
- 使用的机械‑水力隙宽关系基于等效流动计算，未显式考虑迂曲度，可能低估热交换面积 [Luo 2016, pp. 9-10]。
- JRC 分布仅基于两个特定场址数据，普适性有限 [Luo 2016, pp. 2-3]。

## Assumptions / Conditions
- 局部热平衡假设，基质完全不渗透 [Luo 2016, pp. 3-4]。
- 单相稳态流动，裂隙内沿横截面压力与温度均匀分布 [Luo 2016, pp. 3-4]。
- 各裂隙机械隙宽为恒定值（6.5/65/650 μm），水力隙宽由 JRC 通过经验关系换算 [Luo 2016, pp. 4-5]。
- Li & Jiang 模型仅在 JRC 0‑20 范围内适用，Barton 模型出现 e/E>1 时强制 e≤E [Luo 2016, pp. 4-5]。
- DFN 模型忽略孤立裂隙和死端，仅考虑连通网络 [Luo 2016, pp. 3-4]。
- 热边界：顶底绝热，右侧注入 50 ℃ 冷水，初始温度 200 ℃ [Luo 2016, pp. 5-6]。

## Key Variables / Parameters
- JRC 分布（正态/对数正态，均值和方差）
- 机械‑水力隙宽比 e/E 的经验模型（Barton 或 Li & Jiang）
- 机械隙宽 E（6.5、65、650 μm）
- DFN 几何（边长 5 m，源自 Sella 场地统计）
- 压力梯度（10^5 Pa/m）
- 流体与岩石热物性（动态粘度 0.001 Pa·s，比热容 4200 J/(kg·K) 等）[Luo 2016, pp. 5-6, Table 3]

## Reusable Claims
- 当采用 Barton 等预测显著水力隙宽折减的模型时，裂隙表面粗糙度对宏观流体流动和热传递有支配性影响，不可忽略。[Luo 2016, pp. 9-10]
- 若采用 Li & Jiang (2013) 模型，粗糙度对宏观流场和温度场的影响可视为一阶近似忽略，且模拟仅需少量实现。[Luo 2016, pp. 9-10]
- 真实裂隙网络的 JRC 分布因场地地质条件而异，无普适分布，需基于现场数据确定。[Luo 2016, pp. 2-3]
- 正态 JRC 分布的裂隙网络渗透性低于同均值同方差的对数正态分布网络，且对粗糙度参数变化更敏感。[Luo 2016, pp. 5-6]
- Barton 模型（1985）的 e/E 比依赖于机械隙宽，隙宽越大粗糙度影响越弱；Li & Jiang 模型则不依赖于 E。[Luo 2016, pp. 5-6]

## Candidate Concepts
- [[Joint Roughness Coefficient]]  
- [[hydraulic aperture]] / [[mechanical aperture]]  
- [[Discrete Fracture Network (DFN)]]  
- [[coupled fluid flow and heat transfer]]  
- [[Cubic law]]  
- [[e/E empirical model]]  
- [[channeling flow]]  
- [[breakthrough curve]]  
- [[chi-square goodness-of-fit]]  
- [[representative elementary volume (REV)]]

## Candidate Methods
- [[COMSOL Multiphysics FEM]]  
- [[chi-square test for probability distribution fitting]]  
- [[Barton’s e/E model]]  
- [[Li and Jiang’s e/E model]]  
- [[Darcy flow simulation in discrete fractures]]  
- [[local thermal equilibrium modeling]]  
- [[Monte Carlo realization of DFN]]

## Connections To Other Work
- 引用了 Grasselli 等人的三维粗糙度定量描述和 θ*max/(C+1) 参数 [Luo 2016, pp. 1-2]。
- 与 Zimmerman & Bodvarsson (1996)、Renshaw (1995)、Patir & Cheng (1978) 等机械‑水力隙宽模型进行对比 [Luo 2016, pp. 3-4, Table 2]。
- 采用 Barton (1973, 1977) 的 JRC 和剪切强度准则作为数据处理基础 [Luo 2016, pp. 2-3]。
- 参考 Min et al. (2004) 的 REV 概念用于模型尺寸确定 [Luo 2016, pp. 4-5]。
- 对比了 Fu et al. (2016) 关于热回收过程中通道流的研究 [Luo 2016, pp. 9-10]。
- 与 Lang et al. (2014) 的三维渗透张量研究相联系，指出二维结论的外推需验证 [Luo 2016, pp. 9-10]。

## Open Questions
- 二维模拟得到的结论在三维裂隙网络中是否仍然成立？[Luo 2016, pp. 9-10]
- 考虑裂隙粗糙度随法向应力、剪切位移等因素动态演化时，宏观流动与传热如何响应？[Luo 2016, pp. 9-10]
- 包含裂隙充填材料或热应力引起的隙宽变化时，现有机械‑水力关系是否仍适用？[Luo 2016, pp. 9-10]
- 引入迂曲度效应的定量模型能否修正热交换面积的低估？[Luo 2016, pp. 9-10]

## Source Coverage
所有 8 个非空索引片段均被处理并编入本页，总字符覆盖比率为 1.0035（索引文本 38,845 字符，编译文本 38,981 字符）。原始片段签名：32e8c838e630506dd31e31aa340a873b657b38d1。
