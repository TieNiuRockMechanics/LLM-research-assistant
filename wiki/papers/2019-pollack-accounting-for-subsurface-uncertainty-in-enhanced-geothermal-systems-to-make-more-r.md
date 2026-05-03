---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-pollack-accounting-for-subsurface-uncertainty-in-enhanced-geothermal-systems-to-make-more-r"
title: "Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions."
status: "draft"
source_pdf: "data/papers/2019 - Accounting for subsurface uncertainty in enhanced geothermal systems to make more robust techno-economic decisions.pdf"
collections:
citation: "Pollack, Ahinoam, and Tapan Mukerji. \"Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions.\" *Applied Energy*, vol. 254, 2019, p. 113666. doi:10.1016/j.apenergy.2019.113666."
indexed_texts: "17"
indexed_chars: "80639"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81056"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005171"
coverage_status: "full-index"
source_signature: "d05430c993c2a8aa1002702a60704d7d948fef69"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:36:05"
---

# Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions.

## One-line Summary

本研究对比了增强型地热系统（EGS）的单一模型优化（SM‑Opt）与多模型优化（MM‑Opt）两种工作流程，发现忽略地下不确定性会导致过于乐观的净现值（NPV）预测；而利用储层模型集合进行优化能够给出更现实的NPV中值及不确定性范围，并识别出对决策稳健性具有更高影响力的因素[Pollack 2019, pp. 1-2; pp. 12-13]。

## Research Question

在增强型地热系统中，工程决策（如井位布置、压裂间距、井径等）必须在缺乏完整地下信息的条件下做出。本文探讨的核心问题是：在不确定的储层条件下，应如何优化EGS的工程决策？具体而言，基于单一确定性储层模型的优化（SM‑Opt）与基于多储层模型集合的优化（MM‑Opt）在最优决策、预测净现值以及决策稳健性方面有何差异？[Pollack 2019, pp. 2-3; pp. 3-4]

## Study Area / Data

研究以加利福尼亚州Coso地热田西翼（West Flank of Coso Geothermal Field）为背景建立假设性EGS数值模型。Coso西翼基岩温度可达270 °C，但岩石致密不透水，尚未形成天然地热系统[Pollack 2019, pp. 4-5]。不确定的基质参数（渗透率、热容量、热导率、围岩孔隙度、断层周边热区宽度等）及其取值范围主要参考Blankenship等人的Coso场地勘探数据[Pollack 2019, pp. 4-5, Table 2]。水力裂缝特征（半长度、裂缝开度、长宽比等）的不确定性范围则依据文献中的实验与模拟结果设定，例如Groß Schönebeck的压裂数据、Hofmann与Reinicke的研究等[Pollack 2019, pp. 5-6, Table 3]。由于多段水力压裂在水平井中的地热应用尚未经过实际场地检验，本研究没有采用真实现场数据，而是利用合成模型进行水热流动模拟[Pollack 2019, pp. 13-14]。财务模型中使用的地热电力售价、钻井及压裂成本等参数亦源自公开文献或报告[Pollack 2019, pp. 8-9, Table 5]。

## Methods

本文采用两套并行的工作流程进行增强型地热系统的工程决策优化[Pollack 2019, pp. 4-5]：

1. **单一模型优化（SM‑Opt）**  
   - 以各不确定地下参数的平均值构建一个最具代表性的唯一储层模型（表2、表3的均值）。  
   - 利用粒子群优化算法（PSO）在该固定储层模型上搜索使20年运营期内的净现值（NPV）最大化的工程决策组合。PSO设置为种群规模10，认知和社会系数均为1.5，惯性权重0.72[Pollack 2019, pp. 4-5]。  
   - 对每组工程参数调用CMG STARS模拟器进行水热流动与能量生产模拟，计算相应的NPV。

2. **多模型优化（MM‑Opt）**  
   - 对表2和表3中的地下参数分布进行蒙特卡洛采样，同时对表4中的工程决策参数进行均匀采样，共生成1000组参数组合并构建相应的储层模型。  
   - 对每个模型进行20年水热模拟，依据模拟的产出流体温度和流量计算发电量和NPV。  
   - 通过K‑means聚类将模型分为高、低产能两组，利用基于距离的广义敏感性分析（Distance‑Based Generalized Sensitivity Analysis）评估各参数对NPV影响的相对重要性[Pollack 2019, pp. 9-10]。  
   - 构建NPV在各类工程决策条件下的概率密度函数（PDF），以中位数NPV的最高值作为该决策的稳健最优范围[Pollack 2019, pp. 10-11]。  

财务指标采用净现值，其计算考虑了电力销售收入、泵送寄生损耗、压裂与钻井成本以及折现率，并在20年评估期内进行折现汇总[Pollack 2019, pp. 6-7]。

## Key Findings

1. **NPV水平与不确定性**  
   SM‑Opt得到的最优工程决策组合对应的NPV为3270万美元。MM‑Opt最优决策组合下的NPV中位数仅为1100万美元，标准差为1500万美元，且整体先验模型的NPV中位数为 − 900万美元[Pollack 2019, pp. 9-11; pp. 12-13]。说明忽略地下不确定性会严重高估EGS的经济效益。

2. **工程决策的稳健性差异**  
   SM‑Opt给出的最优参数为：井长950 m、生产井泵功率917 kW、注采井距201 m、最大井口压力6.9 MPa、压裂间距10 m、生产井内径0.17 m、注入井内径0.28 m、井位与断层的相对位置0.67（即与断层相交）[Pollack 2019, pp. 9-9]。  
   MM‑Opt则表明：  
   - 压裂间距宜选10 m或15 m，进一步加密的收益提升有限；  
   - 注入井与生产井间距宜在155 –240 m之间；  
   - 生产井和注入井内径均应小于0.28 m（偏小为宜）；  
   - 决策“是否与断层相交”以相交为优；  
   - 对于泵功率和水平井长度，MM‑Opt未显示出明显偏好，说明在此不确定性范围内这些决策不敏感[Pollack 2019, pp. 11-12, Table 6]。  
   总体而言，两种方法得出的最优决策相似，但MM‑Opt额外提供了各参数的敏感性排序和不确定性区间，从而使决策更加稳健。

3. **敏感性排名**  
   对NPV影响最大的前三个参数依次为：平均裂缝开度、平均裂缝半长、断层周围热区宽度。这些均属于难以在工程上精确控制的地质不确定量。紧随其后的敏感参数包括裂缝间距、井与断层相对位置等工程可调量[Pollack 2019, pp. 9-10, Fig. 10]。裂缝开度和半长的高敏感性说明进一步提高压裂技术，以形成更长、更宽的水力裂缝，对于提升EGS经济性至关重要。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SM‑Opt最优NPV为3270万美元 | [Pollack 2019, pp. 9-9] | 单一代表性储层模型，PSO优化，20年运营，Coso场地参数均值 | 优化参数详见表6及其正文描述 |
| MM‑Opt最优决策组NPV中位数为1100万美元，标准差1500万美元 | [Pollack 2019, pp. 11-12, Fig. 15] | 1000组地下与工程参数蒙特卡洛抽样，Coso场地分布 | 整体先验模型NPV中位数为 − 9 百万美元 |
| SM‑Opt高估NPV，其最优值远高于MM‑Opt的中位数 | [Pollack 2019, pp. 12-13, Fig. 17] | 同一参数分布下两种优化流程比较 | SM‑Opt的最优值位于MM‑Opt相应压裂间距组的上四分位数之外 |
| 平均裂缝开度是影响NPV的最敏感地下参数 | [Pollack 2019, pp. 9-10, Fig. 10] | 基于1000个模拟结果的广义敏感性分析 | 裂缝开度和半长均属于工程难以直接控制的参数 |
| MM‑Opt显示对井长和泵功率无明确偏好 | [Pollack 2019, pp. 11-12, Table 6] | 在给定地下不确定性范围内 | 表明这些参数在稳健决策中可优先选择低成本方案 |
| 与断层相交的井位设计可提高NPV中位数 | [Pollack 2019, pp. 11-12, Fig. 13b] | 条件PDF分析，断层伴随高温热异常 | 尽管断层可能导致热短路，但附加的热能收益更为显著 |

## Limitations

- 水力裂缝被简化为薄层多孔介质，并未采用离散裂缝网络模型，也未模拟裂缝起裂与扩展过程；因此裂缝性质假设为随机变量，受未知自然参数的主导[Pollack 2019, pp. 4-5; pp. 5-6]。
- 天然断层的走向、倾角等几何不确定性未被纳入，且未考虑可能存在的未钻遇大型断层[Pollack 2019, pp. 5-6]。
- 经济模型未包含运营成本（如二元机组的使用成本），且假设EGS设施邻近已有地热电站，利用了其备用容量[Pollack 2019, pp. 8-9]。
- 所有模拟基于理论场地，并无实际多段压裂EGS运行数据验证，结论仅限于当前模型参数设定[Pollack 2019, pp. 13-14]。
- 模拟中假设局部热平衡，未来需探讨非平衡效应[Pollack 2019, pp. 4-5]。

## Assumptions / Conditions

- 研究场地为加利福尼亚州Coso地热田西翼的理论EGS，储层温度可达270 °C[Pollack 2019, pp. 4-5]。
- 地下参数的不确定性范围来源于该场地的勘探数据及文献调研，具体分布见表2和表3[Pollack 2019, pp. 4-6]。
- 水力裂缝特性主要由未知的地下条件（应力、天然裂缝等）控制，而非压裂工艺参数；因此裂缝长度、开度、长宽比等在各实现中作为随机变量[Pollack 2019, pp. 5-6]。
- 电力售价固定为0.076美元/kWh，折现率前两年15%后续7%，钻井和压裂成本参考页岩油气及地热行业数据[Pollack 2019, pp. 8-9, Table 5]。
- 注采井口压力和泵功率属于工程可调变量，其取值范围参考了现场设备能力（如Baker Hughes的泵规格）[Pollack 2019, Table 4]。

## Key Variables / Parameters

**不确定地下基质参数**（见表2）[Pollack 2019, pp. 4-5]：
- 基质渗透率（对数均匀分布，范围10⁻⁵ – 10⁻² mD）
- 岩石热容量（均匀分布，0.8 – 1.3 kJ/(kg·K)）
- 岩石热导率（均匀分布，2 – 4 W/(m·K)）
- 断层周围热区宽度（均匀分布，200 – 1000 m）
- 基质孔隙度（均匀分布，0.3 – 1.6%）

**不确定水力裂缝参数**（见表3）[Pollack 2019, pp. 5-6]：
- 平均裂缝半长（均匀分布，100 – 300 m）
- 平均裂缝开度（均匀分布，0.0005 – 0.0018 m）
- 平均裂缝长宽比（均匀分布，0.7 – 1.0）
- 裂缝向下延展与向上延展之比（均匀分布，0.7 – 0.95）
- 天然断层渗透率（对数均匀分布，10⁰ – 10⁵ mD）
- 天然断层孔隙度（均匀分布，0.05 – 0.3）
- 天然断层开度（均匀分布，0.01 – 1 m）

**工程决策参数**（见表4）[Pollack 2019, pp. 5-6]：
- 最大井口压力（0 – 15,000 kPa）
- 生产井泵功率（100 – 1500 kW）
- 注采井间距（70 – 325 m）
- 压裂间距（10 m, 15 m, 20 m, 25 m）
- 井长度（500 – 1000 m）
- 生产井与注入井内径（标准管径列表）
- 注入井相对断层的位置（−0.5 – 1.5，无量纲）

## Reusable Claims

1. 对于给定地下不确定性分布（对应Coso西翼条件），SM‑Opt优化得到的最优工程决策组合会导致NPV的高估，其数值（$32.7 M）远高于MM‑Opt稳健决策下的中位数（$11 M），说明忽略地下不确定性会给出过度乐观的预测[Pollack 2019, pp. 12-13; pp. 9-9; pp. 11-12]。
2. 平均裂缝开度和平均裂缝半长是影响EGS经济效益的首要参数，且都属于工程难以精确控制的因子，这表明改进压裂工艺以增加裂缝延伸范围是提高EGS经济性的关键方向[Pollack 2019, pp. 9-10]。
3. 在不确定环境下，压裂间距并非越密越好，MM‑Opt中10 m与15 m间距的NPV中位数相近，从而允许作业者避免不必要的高成本加密压裂[Pollack 2019, pp. 11-12, Fig. 17]。
4. 对于水平井长度和生产井泵功率，MM‑Opt未显示出明确的偏好，说明在该不确定性水平下这些参数对NPV不敏感，可优先采用低成本方案以降低初始投资[Pollack 2019, pp. 11-12, Table 6]。
5. 使注入井与已知的导热断层相交，虽然可能引入热短路风险，但断层周围的高温异常能带来额外热能，总体上提升了NPV中位数，是稳健的决策[Pollack 2019, pp. 11-12, Fig. 13b]。
6. 采用MM‑Opt方法不仅提供了稳健的工程参数范围，还给出NPV的不确定性区间和参数敏感性排序，比SM‑Opt能够更全面地支撑决策[Pollack 2019, pp. 12-13]。

## Candidate Concepts

- [[Enhanced Geothermal System (EGS)]]
- [[Single-Model Optimization (SM-Opt)]]
- [[Multiple Model Optimization (MM-Opt)]]
- [[Particle Swarm Optimization (PSO)]]
- [[Monte Carlo Optimization]]
- [[Net Present Value (NPV)]]
- [[Subsurface Uncertainty Quantification]]
- [[Distance-Based Generalized Sensitivity Analysis]]
- [[K-means clustering for performance classification]]
- [[Conditional probability density function (PDF) for decision analysis]]
- [[Fracture reservoir]]
- [[Thermal breakthrough]]
- [[Hydraulic fracturing in geothermal systems]]
- [[Coso geothermal field]]
- [[Robust decision-making under uncertainty]]

## Candidate Methods

- [[Particle Swarm Optimization (PSO)]]
- [[Monte Carlo sampling with brute-force exhaustive evaluation]]
- [[Hydro-thermal flow simulation with CMG STARS]]
- [[K-means clustering for classifying high/low NPV realizations]]
- [[Distance-Based Generalized Sensitivity Analysis]]
- [[Conditional PDF construction for engineering decision selection]]
- [[Numerical modeling of EGS with thin-layer fracture representation]]
- [[NPV-based techno-economic assessment]]

## Connections To Other Work

- 前人研究多集中于在固定储层模型上优化EGS设计（如Li等[5]的多裂缝效益、Asai等[6]的注采井距重要性、Song等[7]的多分支井配置），或在单一模型下探讨裂缝非均质性的影响（Doe等[8]、Guo等[9]）[Pollack 2019, pp. 3-4]。
- 另一方面，大量工作专注于运用随机反演、集合卡尔曼滤波等方法量化地热储层参数的不确定性（Vogt等[12,13,17]、Tompson等[14]、Mellors等[15]、Cui等[16]）[Pollack 2019, pp. 3-4]。
- 然而，将“工程决策优化”与“储层不确定性量化”相结合的工作甚少。本文通过并行比较SM‑Opt和MM‑Opt两种流程，填补了这一交叉缺口，并呼应了早期地热项目（如Fenton Hill、Rosemanowes）因忽视地下不确定性而导致决策失败的教训[Pollack 2019, pp. 3-4]。
- Hu等[10]和Hofmann等[11]的研究揭示了水力裂缝形态对应力非均质性和天然裂缝分布的敏感性，这与本文中裂缝半长和开度主导NPV的发现一致，进一步强调压裂过程与地下不确定性的耦合需要深入研究[Pollack 2019, pp. 3-4; pp. 9-10]。

## Open Questions

- 如何在真实的EGS压裂作业中通过压裂液、支撑剂选择等措施有效增大裂缝半长和开度，从而将本文识别的最敏感参数转化为可主动调节的工程变量？[Pollack 2019, pp. 9-10; pp. 14-15]
- 若考虑裂缝扩展模拟（耦合天然裂缝、断层及地应力）以及热应力等地质力学效应，裂缝性质的不确定性将如何演变，MM‑Opt所给出的稳健决策是否会发生偏移？[Pollack 2019, pp. 14-15]
- 本研究中部分工程参数（井长、泵功率）在MM‑Opt中表现为不敏感，该结论在更换另一个场地或不同成本结构时是否依然成立？需要进行成本敏感性分析[Pollack 2019, pp. 11-12]。
- 尚未回答页岩气型多段压裂水平井技术在真实地热条件（高温、硬岩）下的实际效果如何，以及能否采集到现场数据以验证或修正本研究的模型假设[Pollack 2019, pp. 13-14]。

## Source Coverage

本次编译严格基于所提供的全部17个非空索引片段（共80639个索引字符），所有片段均被处理和使用。源代码块与索引文本完全匹配，未遗漏任何内容。  
- 按代码块计覆盖率：1.0（17/17）  
- 按字符计覆盖率：1.005171（编译后总字符81056，覆盖率略超100%源于可能的空格/换行差异，但未引入原文之外的实质信息）[source signature: d05430c993c2a8aa1002702a60704d7d948fef69]。
