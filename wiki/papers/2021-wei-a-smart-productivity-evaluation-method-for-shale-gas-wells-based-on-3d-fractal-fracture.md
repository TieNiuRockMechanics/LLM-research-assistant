---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-wei-a-smart-productivity-evaluation-method-for-shale-gas-wells-based-on-3d-fractal-fracture"
title: "A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2021 - A smart productivity evaluation method for shale gas wells based on 3D fractal fracture network model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wei, Yunsheng, et al. \"A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model.\" *Petroleum Exploration and Development*, vol. 48, no. 4, Aug. 2021, pp. 911-922. 10.1016/S1876-3804(21)60076-9. Accessed 2026."
indexed_texts: "10"
indexed_chars: "49358"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "48291"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.978382"
coverage_status: "full-index"
source_signature: "90b3bce939952e2d3c1bd3bf54ad6ed97b491ab6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:52:44"
---

# A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model.

## One-line Summary
提出了一种融合三维分形离散裂缝网络(3D FDFN)生成、嵌入式离散裂缝模型(EDFM)流动模拟和基于多重代理的马尔科夫链蒙特卡洛(MCMC)智能历史拟合的页岩气井产能评价方法，实现关键参数反演与产能预测，现场应用显示高可信度[Wei 2021, pp. 1-2]。

## Research Question
页岩气藏体积压裂后形成的多尺度裂缝网络极其复杂，导致裂缝描述与模拟困难、气井产能预测精度低。解决该问题的三个关键条件：(1) 裂缝网络空间分布的合理表征；(2) 流体在裂缝网络中流动过程的准确模拟；(3) 气井生产历史数据的高效、精确拟合[Wei 2021, pp. 1-2]。

## Study Area / Data
以昭通地区一口页岩气水平井A为实例井。该井区天然裂缝以近南北、北西和北东走向为主，倾角平均80°，裂缝长度多小于100 m。页岩孔隙度5.5%–6.5%，原始基质渗透率约(1.0–10.0)×10⁻⁸ μm²。储层初始压力44.9 MPa，温度100 °C，水平段长1550 m，压裂段数16段，48簇。天然裂缝分形参数见表4，模型基本参数见表5[Wei 2021, pp. 7-8]。历史拟合使用日产气量、日产水量和井底流压等动态生产数据[Wei 2021, pp. 8-10]。

## Methods
1. **三维分形裂缝网络生成**：基于倍增级联过程生成三维分形离散裂缝网络(FDFN)，利用分形维数(Dc3D, Dl3D)和密度常数(α3D)控制裂缝长度、位置、走向的概率分布；通过面积等效法将圆盘模型修正为矩形，并验证生成算法与输入参数的一致性[Wei 2021, pp. 2-4]。
2. **嵌入式离散裂缝流动模拟(EDFM)**：在正交网格上通过虚拟裂缝网格处理非相邻网格连接对(NNC)的传导率，避免局部网格加密的复杂性，同时精确计算基质-裂缝与裂缝-裂缝间的流体传输。模型采用单孔隙–EDFM、BET多层吸附/兰氏等温吸附、气水两相Corey相对渗透率、应力敏感渗透率衰减、非平衡初始化以及黑油均质储层假设[Wei 2021, pp. 4-6]。通过对比LGR、PEBI和EDFM的计算结果，验证EDFM的精度与效率优势[Wei 2021, pp. 5-6]。
3. **智能历史拟合(AHM)**：基于神经网络代理和马尔科夫链蒙特卡洛(NN-MCMC)的辅助历史拟合方法，先通过正交试验设计生成初始样本并利用EDFM并行模拟，再训练代理模型进行MCMC采样，迭代筛选全局误差最小的参数组合，直至收敛[Wei 2021, pp. 6-8]。

## Key Findings
- 三维分形裂缝生成算法能够通过**分形参数**控制裂缝网络的整体分布，并与人工裂缝耦合表征页岩压裂后的多尺度复杂系统；相同分形参数的裂缝系统具有几乎相同的等效渗透率和动态响应[Wei 2021, pp. 1-2]。
- EDFM在模拟复杂裂缝网络时，比局部网格加密(LGR)和垂直平分(PEBI)方法**计算耗时更短**（120 s vs 257 s, 185 s），所需裂缝网格数更少（640 vs 2296, 1975），且与PEBI结果高度一致[Wei 2021, pp. 5-6]。
- 结合AHM的EDFM工作流能够有效降低储层与裂缝参数的不确定性，从325次模拟中筛选出75组历史拟合解，P50参数值见表7[Wei 2021, pp. 8-10]。
- 实例井20年累积产气量的P10–P90置信区间为(1.05–1.22)×10⁸ m³，最优解1.15×10⁸ m³；该结果与基于产量递减分析方法的解释结果（1.01×10⁸ m³）高度吻合，验证了方法的**高可信度**[Wei 2021, pp. 10]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 3D分形裂缝生成算法与输入参数一致性（Table 1） | [Wei 2021, pp. 4-5] | 2D验证：生成区域10 m×10 m，lmin=0.05 m，Dc=1.6，Dl=1.5，α=3.5，方位中值N43°E；匹配得Dc=1.51，Dl=1.52，α=3.35，方位中值N43.3°E | 算法可靠，可用于生成3D裂缝网络 |
| EDFM与PEBI模拟结果高度一致，且计算时间最短（120 s） | [Wei 2021, pp. 5-6] | 均质气藏，单相气，定井底压力1.5 MPa，20年；基础网格170×40×1 | EDFM比LGR(257 s)和PEBI(185 s)效率更高，裂缝网格数更少 |
| 历史拟合筛选出75组解，全局误差<50% | [Wei 2021, pp. 8-10] | 12步自动迭代，每步1000万个样本；匹配参数为日气产量、日水产量和井底流压 | 图10展示了拟合效果 |
| P50反演参数：裂缝半长99 m，基质渗透率0.45×10⁻⁷ μm²，簇效率79.5%等 | [Wei 2021, pp. 10] | 实例井A，昭通页岩气藏 | 见表7 |
| 20年累积产气量P10–P90：(1.05–1.22)×10⁸ m³，对比产量递减法结果1.01×10⁸ m³ | [Wei 2021, pp. 10] | 定井底流压1.5 MPa预测 | 两种方法结果高度相似，证明该方法可信 |

## Limitations
- 模型假设储层均质、各向同性，且采用黑油模型和单孔隙介质，忽略了实际页岩的强非均质性和复杂孔隙结构[Wei 2021, pp. 4-6]。
- 吸附气采用瞬时解吸模型和BET/Langmuir等温吸附，未考虑解吸时间效应；应力敏感性仅通过指数衰减方程描述人工裂缝[Wei 2021, pp. 5-6]。
- 历史拟合中未讨论天然裂缝的闭合或扩展等动态行为，且代理模型的精度受初始采样空间影响（未明确提及）。
- 天然裂缝采用矩形等效修正圆盘模型，与真实裂缝形态仍有差异[Wei 2021, pp. 2-4]。

## Assumptions / Conditions
1. 储层均质、水平、等厚，平面基质渗透率各向同性；垂向渗透率为平面渗透率的0.1倍[Wei 2021, pp. 4-5]。
2. 气体解吸由BET多层等温吸附模型（n=1时退化为Langmuir模型）描述[Wei 2021, pp. 5]。
3. 裂缝与基质中气水两相流，采用Corey相对渗透率模型；非平衡初始化，裂缝中水饱和度高于束缚水[Wei 2021, pp. 5]。
4. 人工裂缝渗透率随压力呈指数衰减（应力敏感）[Wei 2021, pp. 5-6]。
5. 流体为黑油，不考虑组分变化；考虑重力和毛管力，但气水两相间无质量传递[Wei 2021, pp. 5-6]。
6. EDFM中裂缝与基质的连接基于NNC传导率公式，忽略裂缝内温度变化[Wei 2021, pp. 5-6]。
7. 天然裂缝长度符合幂律分布，而非正态分布；裂缝产状由分形维数和密度常数控制[Wei 2021, pp. 2-3]。

## Key Variables / Parameters
- 分形参数：3D裂缝分布分形维数 Dc3D，3D裂缝长度分形维数 Dl3D，3D裂缝密度常数 α3D
- 裂缝几何参数：裂缝最小长度 lmin，模型尺度 L，矩形裂缝长度/高度比（2:1），裂缝走向、倾角的中值
- 储层物性参数：基质渗透率 K，基质孔隙度 φ，岩石压缩系数
- 压裂参数：有效裂缝半长，裂缝导流能力，簇效率，裂缝宽度 wf，裂缝渗透率衰减系数 γ
- 相渗参数：气和水的相对渗透率端点值 Krgo, Krwo，气和水的 Corey 指数 Ng, Nw
- 动态参数：井底流压，日产气量，日产水量，水饱和度
- 模型网格与效率参数：基础网格数，总网格数，裂缝网格数，迭代次数 Niter，时间步长，计算时间

## Reusable Claims
1. “三维分形裂缝生成方法能利用分形参数控制裂缝网络的整体分布，相同分形参数的裂缝系统具有几乎相同的流动能力（等效渗透率）”[Wei 2021, pp. 1-2]。**条件**：需提供可靠的 Dc3D、Dl3D 和 α3D 参数，且裂缝长度服从幂律分布。
2. “嵌入式离散裂缝模型(EDFM)在模拟复杂裂缝网络时，比LGR和PEBI具有更少的裂缝网格数（640 vs. 2296, 1975）和更短的计算时间（120 s vs. 257 s, 185 s）” [Wei 2021, pp. 5-6]。**条件**：在单层、正交基础网格，且裂缝间距和长度符合给定范围时有效；极端低渗情况可能需要更多网格。
3. “基于多重代理的MCMC智能历史拟合能够实现关键储层与裂缝参数的有效反演，降低预测不确定性”[Wei 2021, pp. 8-10]。**条件**：需要足量的历史生产数据（产气、产水、压力），且目标函数误差阈值与初始样本设计需合理。
4. “集成FDFN-EDFM-AHM的产能评价模型在实际页岩气井中预测的20年累积产气量与产量递减分析方法结果一致，证明具有高可信度”[Wei 2021, pp. 10]。**条件**：适用于裂缝发育、压裂后形成复杂网络的页岩气水平井，且已知天然裂缝分形统计特征。

## Candidate Concepts
- [[分形离散裂缝网络 (Fractal Discrete Fracture Network)]]
- [[嵌入式离散裂缝模型 (Embedded Discrete Fracture Model)]]
- [[辅助历史拟合 (Assisted History Matching)]]
- [[马尔科夫链蒙特卡洛 (MCMC)]]
- [[多重代理模拟 (Multiple Proxy-Based Surrogate)]]
- [[非相邻连接对 (Non-Neighboring Connection)]]
- [[分形维数 (Fractal Dimension)]]
- [[倍增级联过程 (Multiplicative Cascade Process)]]
- [[幂律长度分布 (Power-Law Length Distribution)]]

## Candidate Methods
- [[多重信息叠加算法]] (用于生成裂缝中心点分布)
- [[三维分形裂缝生成模块]] (基于Python)
- [[EDFM非相邻连接对传导率计算方法]]
- [[智能历史拟合工作流 (NN-MCMC)]]
- [[等效面积矩形修正法]] (将圆盘裂缝转换为矩形裂缝)
- [[正交试验设计采样法]] 用于初始参数组合
- [[神经网络代理模型]] 用于加速参数反演

## Connections To Other Work
- 与离散裂缝网络(DFN)建模相比，分形方法用分形维数替代均匀随机理论，更能表征天然裂缝的自相似性和非均质性 [Wei 2021, pp. 1-2]。
- EDFM技术相对于传统局部网格加密(LGR)和垂直平分(PEBI)方法在计算效率和复杂裂缝网络适应性上优势明显 [Wei 2021, pp. 5-6]，文中引用了Li & Lee (2008), Yu et al. (2017), Xu et al. (2019)等EDFM相关工作。
- 历史拟合方法对比了牛顿优化、粒子群、遗传算法等，指出基于智能算法的辅助历史匹配能降低人为主观性和计算量 [Wei 2021, pp. 2]。
- 在产能预测上，结果与多种产量递减模型分析的解释结果互为验证 [Wei 2021, pp. 10]，参考了Wei et al. (2021) 应力敏感裂缝井动态优化的工作。

## Open Questions
- 文中未讨论该方法在天然裂缝闭合、裂缝扩展等动态效应下的适用性；目前模型仅考虑固定裂缝属性 [Wei 2021, pp. 5-6]。
- 3D分形矩形裂缝模型与实际不规则裂缝形态的差异如何影响流动模拟精度未量化 [Wei 2021, pp. 2-4]。
- 智能历史拟合中代理模型的逼近误差随迭代增加是否可能引入偏差，以及最优迭代终止准则的确定尚待研究（文中未明确定义收敛准则）[Wei 2021, pp. 6-8]。
- 仅针对一口实例井验证，方法在其他页岩区块和不同压裂工艺条件下的普遍性仍需更多应用证明。

## Source Coverage
所有非空索引片段（共10个）均已处理，来源块覆盖率为100%（10/10），字符覆盖率为97.8%（48291/49358字符）。无片段遗漏。
