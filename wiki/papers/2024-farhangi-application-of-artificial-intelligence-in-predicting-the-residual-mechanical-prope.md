---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-farhangi-application-of-artificial-intelligence-in-predicting-the-residual-mechanical-prope"
title: "Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures."
status: "draft"
source_pdf: "data/papers/2024 - Application of artificial intelligence in predicting the residual mechanical properties of fiber reinforced concrete (FRC) after high temperatures.pdf"
collections:
  - "论文"
citation: "Farhangi, Visar, et al. \"Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures.\" *Construction and Building Materials*, vol. 411, 2024, 134609. Accessed 2026."
indexed_texts: "19"
indexed_chars: "93379"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "87776"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.939997"
coverage_status: "full-index"
source_signature: "5e5c8baeaa1710b8d296a98851f0c1b99a098ccb"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:12:53"
---

# Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures.

## One-line Summary
利用人工神经网络等AI模型，基于包含286组钢纤维和聚丙烯纤维增强混凝土（SFRC/PFRC）高温试验数据的综合数据集，预测了高温后FRC的残余力学性能，并开展了大规模概率失效分析，得出SFRC与PFRC的临界失效温度分别为550℃和430℃。 [Farhangi 2024, pp. 1-1] [Farhangi 2024, pp. 18-18]

## Research Question
如何利用人工智能方法，综合考虑混凝土配合比、纤维几何与力学特性及温度范围（100–1200℃），准确预测纤维增强混凝土（FRC）在高温后的残余抗压强度、抗拉强度与弹性模量？同时，如何通过概率模型量化不同纤维种类、水胶比、纤维体积率和长径比下的失效概率？ [Farhangi 2024, pp. 1-1] [Farhangi 2024, pp. 2-3] [Farhangi 2024, pp. 8-8]

## Study Area / Data
研究数据来源于系统的文献综述，构建了包含286组FRC样本的数据集，涵盖钢纤维（SFRC）和聚丙烯纤维（PFRC）两种类型。数据集按力学性能划分为6个子集：
- 抗压强度：SFRC 286个数据点，PFRC 114个数据点；
- 劈裂抗拉强度：SFRC 78个数据点，PFRC 100个数据点；
- 弹性模量：SFRC 85个数据点，PFRC 82个数据点。 [Farhangi 2024, pp. 3-3]
输入特征包括水（W）、胶凝材料（B）、碎石（G）、砂（S）、纤维掺量（F）、纤维长度（l）、直径（d）及温度（T），SFRC数据集额外包含纤维抗拉强度（fᵤ）。输出为相对于室温的残余力学性能比值（%）。室温下的力学性能范围：抗压强度15–113 MPa，抗拉强度2–10 MPa，弹性模量11–50 GPa。 [Farhangi 2024, pp. 3-3] [Farhangi 2024, pp. 3-4]
数据分布揭示了研究空白：纤维体积率大于0.8%且高长径比的试验不足；温度高于800℃的数据仅占总体的12.2%；低水胶比（<0.4）与高纤维掺量组合的数据少于20%。 [Farhangi 2024, pp. 3-3] [Farhangi 2024, pp. 3-5]

## Methods
采用多层感知器（MLP）构建AI模型，模型训练使用Levenberg-Marquardt算法，数据随机划分为70%训练、15%验证、15%测试。隐藏层采用TANSIG激活函数，输出层采用PURELIN函数。通过10折交叉验证与早停法确定最佳网络结构，例如SFRC抗压强度模型为9-6-1，PFRC抗压强度为8-15-1等。输入变量均线性归一化至[0,1]区间。 [Farhangi 2024, pp. 2-3] [Farhangi 2024, pp. 5-5] [Farhangi 2024, pp. 5-5]
模型性能以均方误差（MSE）和相关系数（R）评价，验证集MSE可低至4.08×10⁻⁴，R值均接近1。 [Farhangi 2024, pp. 5-6]
基于训练好的模型进行泛化分析，固定W/B=0.5，改变纤维掺量、直径、长度和温度，绘制等高线图以展示残余性能变化。同时，利用Garson因子进行敏感性分析，量化各输入特征的相对重要性。 [Farhangi 2024, pp. 5-6] [Farhangi 2024, pp. 6-8]
为进行概率建模，采用两种方法：1）基于统计的方法，将实验数据集按100℃间隔分段，拟合对数正态分布（Lognormal PDF），并通过Anderson-Darling、Kolmogorov-Smirnov等检验识别最优分布，建立μ与σ随温度的多项式回归方程；2）基于AI的概率方法，将纤维掺量、长度、直径、抗拉强度（仅钢纤维）及温度作为随机变量，执行100万次蒙特卡洛模拟，以残余抗压强度比<0.5为极限状态函数（LSF），计算失效概率P_f。 [Farhangi 2024, pp. 9-12] [Farhangi 2024, pp. 12-17] [Farhangi 2024, pp. 14-17]

## Key Findings
1. **模型精度**：AI模型对SFRC抗压、抗拉、弹性模量的MSE分别为0.0007、0.0023、0.0016；对PFRC的MSE分别为0.0008、0.0034、0.0022。 [Farhangi 2024, pp. 18-18]
2. **温度敏感性**：温度是影响最大的参数，PFRC对温度的敏感性高于SFRC（如抗压强度：PFRC 19.7% vs SFRC 15.8%）。 [Farhangi 2024, pp. 18-18] [Farhangi 2024, pp. 5-6]
3. **纤维几何效应**：钢纤维直径与长度的增加在所有温度下均提高残余抗压强度比；PP纤维含量高于4 kg/m³、长度超过18 mm时，可减缓强度下降速率。 [Farhangi 2024, pp. 6-8] [Farhangi 2024, pp. 18-18]
4. **抗压强度对比**：SFRC残余抗压强度平均比PFRC高6.3%。 [Farhangi 2024, pp. 18-18]
5. **抗拉强度行为**：600℃以下SFRC抗拉强度比（约1.1）高于PFRC（约0.7）；600℃以上PFRC表现更优。 [Farhangi 2024, pp. 18-18]
6. **弹性模量**：钢纤维掺量增加略微提升弹性模量（约束效应），钢纤维直径>0.8 mm时效果更明显；PP纤维在掺量>4 kg/m³且长度>18 mm时改善弹性模量。 [Farhangi 2024, pp. 8-11]
7. **概率失效分析**（基于AI模型与蒙特卡洛模拟）：
   - PFRC失效概率对水胶比、长径比和纤维掺量的依赖性较低，P_f约为50%；SFRC在水胶比0.4–0.5时失效概率最低。 [Farhangi 2024, pp. 14-17]
   - 随温度升高，两种FRC失效概率均增加；300–600℃间PFRC失效概率高于SFRC。 [Farhangi 2024, pp. 14-17]
   - 钢纤维长径比大于3时，P_f上升；PP纤维长径比大于1后，P_f几乎不变。 [Farhangi 2024, pp. 17-17]
   - 纤维掺量对P_f影响较小，但PP纤维掺量超过0.6%后失效风险略有降低。 [Farhangi 2024, pp. 17-18]
8. **临界温度**：以残余抗压强度比<0.5为失效准则，SFRC临界温度为550℃，PFRC为430℃。 [Farhangi 2024, pp. 17-18] [Farhangi 2024, pp. 18-18]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SFRC抗压模型MSE=0.0007，R=0.994 | [Farhangi 2024, pp. 5-6] | 9-6-1网络，LM训练，70/15/15划分 | 测试集MSE为0.0021 |
| PFRC抗压模型MSE=0.0008，R=0.993 | [Farhangi 2024, pp. 5-6] | 8-15-1网络 | 验证集MSE为0.0013 |
| 温度敏感性：PFRC抗压19.7% vs SFRC 15.8% | [Farhangi 2024, pp. 5-6] [Farhangi 2024, pp. 18-18] | Garson重要性分析 | 适用于弹性模量与抗拉趋势 |
| 钢纤维直径>1.2mm、长度>40mm时抗压强度比提升 | [Farhangi 2024, pp. 6-8] [Farhangi 2024, pp. 18-18] | W/B=0.5，所有温度 | 纤维互锁与桥接效应 |
| PP纤维掺量>4 kg/m³且长度>18mm时抗拉退化减缓 | [Farhangi 2024, pp. 8-8] | W/B=0.5 | 熔化后形成的微通道释放蒸汽压 |
| SFRC抗拉强度比600℃以下约1.1，PFRC约0.7 | [Farhangi 2024, pp. 18-18] | 室温至600℃ | 600℃以上PFRC反超 |
| 失效概率：PFRC几乎与W/B无关，P_f≈50% | [Farhangi 2024, pp. 14-17] | 基于100万次MC模拟 | SFRC在W/B 0.4-0.5最低 |
| 钢纤维长径比>3时P_f增加 | [Farhangi 2024, pp. 17-17] | W/B=0.5 | 约束效应减弱 |
| 临界失效温度：SFRC 550℃，PFRC 430℃ | [Farhangi 2024, pp. 17-18] | 强度比<0.5定义 | 基于广义模型，MSE 4.7%/4.9% |
| 数据集高温数据不足：800℃以上仅12.2% | [Farhangi 2024, pp. 3-3] | 文献综述统计 | 需更多高温实验 |

## Limitations
- 数据集规模有限，某些温度区间（如>800℃）数据点稀少，统计模型对此类区间预测精度受限。 [Farhangi 2024, pp. 10-11]
- 概率建模中，混凝土配比变量被视为确定性量，未纳入配比参数自身的变异性。 [Farhangi 2024, pp. 17-17]
- 模型一般化分析固定W/B=0.5，其他水胶比的交互效应未充分展开。 [Farhangi 2024, pp. 6-8]
- 当前研究仅针对钢纤维和聚丙烯纤维两种纤维类型，未涵盖其他纤维（如碳纤维、玄武岩纤维）。 [Farhangi 2024, pp. 17-18]
- 失效准则采用残余强度比<0.5的确定性限值，未考虑极限状态函数本身的不确定性。 [Farhangi 2024, pp. 12-14]

## Assumptions / Conditions
- 输入变量线性归一化至[0,1]区间，保留原始数据全部关系。 [Farhangi 2024, pp. 5-5]
- 纤维含量超过2%体积率或长径比大于200时，因成球效应未纳入泛化分析。 [Farhangi 2024, pp. 6-6]
- 概率分析时，对于SFRC选用的随机变量为纤维掺量、长度、直径、抗拉强度和温度；对于PFRC为纤维掺量、长度、直径和温度。 [Farhangi 2024, pp. 12-14]
- 失效定义沿用Eurocode 500℃等温线法的概念，假设500℃对应残余抗压强度比约0.5。 [Farhangi 2024, pp. 12-14]
- 统计概率模型仅适用于温度大于100℃的范围。 [Farhangi 2024, pp. 10-11]

## Key Variables / Parameters
- **输入变量**（SFRC 9个，PFRC 8个）：
  - 混凝土配合比：水（W，kg/m³）、胶凝材料（B，kg/m³）、粗骨料（G，kg/m³）、细骨料（S，kg/m³）
  - 纤维参数：纤维掺量（F，kg/m³）、纤维长度（l，mm）、纤维直径（d，mm）、纤维抗拉强度（fᵤ，MPa，仅SFRC）
  - 温度：T（℃）
- **输出目标**：残余力学性能比（相对于20℃）：
  - 抗压强度比（f_c/f_c20）
  - 抗拉强度比（f_t/f_t20）
  - 弹性模量比（E/E20）
- **概率变量**（AI-MC模拟）：
  - 随机变量：F, l, d, f_u (SFRC), T （均视作随机变量，服从特定分布）
  - 确定性变量：W, B, G, S
- **失效指标**：残余抗压强度比<0.5 [Farhangi 2024, pp. 3-3] [Farhangi 2024, pp. 12-14]

## Reusable Claims
- 在高温FRC领域，多层感知器配合Levenberg-Marquardt训练法可有效预测残余力学性能，但需确保数据集包含关键变量组合。 [Farhangi 2024, pp. 18-18]  
  条件：数据集需涵盖目标温度与纤维参数范围，并注意高纤维掺量（>0.8%）数据不足可能影响外推可靠性。
- 钢纤维对残余抗压和抗拉强度的改善优于聚丙烯纤维，但聚丙烯纤维在超过600℃后抗拉强度保持率更优，可归因于熔化通道缓解蒸汽压。 [Farhangi 2024, pp. 8-8] [Farhangi 2024, pp. 18-18]  
  条件：比较基于固定W/B=0.5与特定纤维几何参数，实际应用中需根据配合比微调。
- 基于广义AI模型的蒙特卡洛模拟可给出不同纤维类型与水胶比下的失效概率曲线，其中SFRC在W/B=0.4–0.5时失效概率较低。 [Farhangi 2024, pp. 16-17]  
  限制：失效准则为确定性强度比0.5，未考虑荷载效应随机性。
- SFRC的临界失效温度约550℃，PFRC约430℃，此结果与若干实验研究一致，可作为初步性能化防火设计的参考。 [Farhangi 2024, pp. 17-18]  
  条件：适用于普通强度FRC，纤维掺量与几何参数在常用范围内。

## Candidate Concepts
- [[纤维增强混凝土高温残余性能]]
- [[AI-based model (Multilayer Perceptron)]]
- [[Garson灵敏度分析]]
- [[失效概率Pf]]
- [[临界温度T_critical]]
- [[对数正态分布Lognormal PDF]]
- [[蒙特卡洛模拟 (Monte Carlo Simulation)]]
- [[Eurocode 500°C等温线法]]
- [[纤维桥接效应]]
- [[蒸汽压力释放机制]]

## Candidate Methods
- [[多层感知器 (MLP) 回归]]
- [[Levenberg-Marquardt训练算法]]
- [[交叉验证与早停法]]
- [[基于Garson权重的输入重要性分析]]
- [[统计概率密度拟合 (Anderson-Darling, K-S检验)]]
- [[基于神经网络代理模型的蒙特卡洛模拟]]
- [[极限状态函数法 (LSF) 失效概率计算]]

## Connections To Other Work
- 引用了Choi等人[15]的SDEM概率模型评估HPFRC拉伸行为，结果与本研究一致表明单段模型会高估抗拉强度，多段模型可改善预测；本研究的AI模型亦体现了多参数耦合的必要性。 [Farhangi 2024, pp. 1-2]
- 与Qureshi等人[17]的混凝土高温强度折减概率模型相呼应，该研究亦采用分段对统计方法拟合对数正态分布，本研究在此基础上进一步结合纤维参数进行概率分析。 [Farhangi 2024, pp. 2-2] [Farhangi 2024, pp. 8-9]
- 对比了Karaki和Naser[20]提出的混凝土与钢材温度依赖特性概率模型，本研究提出的方程（图14）同样可用于量化不确定性，但针对FRC专门化。 [Farhangi 2024, pp. 2-2]
- 还与Chen等人[8]对高温FRC抗压强度的深度学习预测结果相比较，该研究仅关注抗压强度且与Eurocode一致性良好，本研究扩展了力学性能种类和概率维度。 [Farhangi 2024, pp. 1-2]
- 实验数据中临界温度结果与Aslani和Kelin[75]、Behnood和Ghandehari[65]以及Pylia等人[87]的发现一致，验证了模型一般化能力的可靠性。 [Farhangi 2024, pp. 17-18]

## Open Questions
- 高达0.8%以上纤维掺量在高温下的实验数据缺失，如何通过补充系统性实验验证AI模型的泛化能力？ [Farhangi 2024, pp. 3-5] [Farhangi 2024, pp. 17-18]
- 低水胶比（<0.4）与高温（>800℃）组合的FRC爆裂行为未充分探索，现有模型能否可靠外推？ [Farhangi 2024, pp. 3-5]
- 当前概率模型将混凝土配合比作为确定性参数，若将其视为随机变量，失效概率会如何变化？ [Farhangi 2024, pp. 17-17]
- 是否可开发统一的概率材料模型，同时涵盖多种纤维类型（如碳纤维、玄武岩纤维）和更广的强度等级？ [Farhangi 2024, pp. 17-18]
- 如何将本研究的材料级概率模型集成到构件或结构系统的性能化防火分析中？ [Farhangi 2024, pp. 11-12]

## Source Coverage
所有提供的19个非空索引片段均已处理并编入本页面。索引片段总字符数93,379，实际编译使用87,776字符，覆盖比（按块）为1.0，按字符为0.94。所有片段来源均为Farhangi等2024年发表于*Construction and Building Materials*第411卷的论文。未引入外部信息。
