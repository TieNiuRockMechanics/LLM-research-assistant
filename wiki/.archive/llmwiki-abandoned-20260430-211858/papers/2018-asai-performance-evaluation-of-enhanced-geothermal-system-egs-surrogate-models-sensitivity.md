---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-asai-performance-evaluation-of-enhanced-geothermal-system-egs-surrogate-models-sensitivity"
title: "Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters."
status: "draft"
source_pdf: "data/papers/2018 - Performance evaluation of enhanced geothermal system (EGS) Surrogate models, sensitivity study and ranking key parameters.pdf"
collections:
citation: "Asai, Pranay, et al. \"Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters.\" *Renewable Energy*, vol. 122, 2018, pp. 184-95, doi:10.1016/j.renene.2018.01.098."
indexed_texts: "12"
indexed_chars: "55773"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:13:20"
---

# Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters.

## One-line Summary
该研究基于FORGE场地数据，使用Box-Behnken实验设计建立二阶替代（代理）模型，评估了井间距、裂缝间距、井斜角、注入温度和注入速率五个关键参数对增强型地热系统（EGS）产出水温度及30年总热回收的影响，并对参数重要性进行了排序 [Asai 2018, pp. 1-2]。

## Research Question
如何量化并排序井间距、裂缝间距、井斜角、注入温度和注入速率这五个关键参数对双井EGS长期热回收性能（产出水温度和30年总热提取量）的影响？ [Asai 2018, pp. 1-2]。

## Study Area / Data
研究采用的数据基于美国犹他州FORGE（Frontier Observatory for Research in Geothermal Energy）场地的原位特性。该场地为花岗闪长岩储层，具有低孔隙度（1%或更低）、低渗透率（约5-30 mD），以及约60 °C/km的地温梯度。在真垂深2500米处的参考温度为200 °C。场地存在天然裂缝，但温度梯度表明其为传导型地热储层而非对流型。 [Asai 2018, pp. 3-4]。模拟设计了一个包含一口注入井、一口生产井和多级垂直水力裂缝的双井系统 [Asai 2018, pp. 2-3]。工作流体为水 [Asai 2018, pp. 2-3]。

## Methods
1.  **替代模型（代理模型）：** 开发了二阶多项式函数的替代模型，以对数变换后的产出水温度作为响应变量，五个关键参数作为自变量。模型形式为 \( \log(f(X_1, …, X_5)) = a_0 + \sum_{k=1}^{n} a_k X_k + \sum_{i=1}^{n} \sum_{j=i}^{n} a_{ij} X_i X_j \)。在0-30年的运行周期内，选取59个时间点，为每个时间点建立一个替代模型，最终通过插值和平滑得到整个温度剖面 [Asai 2018, pp. 4-5]。
2.  **实验设计：** 采用Box-Behnken方法设计模拟实验，该方法为三水平设计（最大值、中值、最小值），旨在减少所需模拟次数。为五个变量（除井斜角取倒数以线性化外）设计了41个模拟作为训练数据 [Asai 2018, pp. 5-5]。另设计了10个随机输入值的模拟作为测试数据，用以验证模型 [Asai 2018, pp. 5-5]。
3.  **模型评估：** 使用决定系数（R²）和归一化均方根误差（NRMSE）来衡量模型的拟合优度 [Asai 2018, pp. 1-2]。
4.  **敏感性分析与排序：** 利用训练好的替代模型，在保持其他参数为中值的条件下，逐一改变目标参数，分析其对产出水温度及热回收的影响。总热提取量 \( H \) 通过积分公式 \( H = \int_{0}^{t} Q \rho c_p (T_p - T_{inj}) dt \) 计算，其中 \( Q \) 为流量，\( \rho \) 为流体密度，\( c_p \) 为流体热容，\( T_p \) 为产出水温度，\( T_{inj} \) 为注入温度 [Asai 2018, pp. 5-7]。最终通过龙卷风图（tornado plot）展示各因素对总热回收影响的层次结构 [Asai 2018, pp. 1-2]。

## Key Findings
1.  **替代模型可靠性：** 建立的二阶替代模型能够较好地拟合训练数据和测试数据，可用于预测产出水温度剖面 [Asai 2018, pp. 5-7]。
2.  **井间距影响：** 在100米至300米研究范围内，较小的井间距（100米）导致产出水温度下降更快，但累计热回收量更少 [Asai 2018, pp. 5-7]。井间距越大，热突破时间越长，晚期产出水温度越高 [Asai 2018, pp. 5-7，根据片段推断]。
3.  **裂缝间距影响：** 未从索引片段中确认具体结论，但它是被研究的五个关键参数之一 [Asai 2018, pp. 1-2]。
4.  **井斜角影响：** 垂直井（井斜角90°，即水平井系统）的热性能优于倾斜井。在倾斜井系统中，裂缝位于不同温度区域，且包含在井间的岩石体积的平均温度较低，导致其效率不如水平井系统 [Asai 2018, pp. 7-9]。
5.  **注入温度影响：** 较低的注入温度（80 °C）会导致产出水温度更迅速的下降，但在30年的运行周期内能提取更多的总热量。因为温差是热交换的驱动力，更冷的注入水能更快速地提取储层热量 [Asai 2018, pp. 7-9]。
6.  **注入速率影响：** 注入流体速率与热提取速率成正比 [Asai 2018, pp. 7-9]。具体细节未从索引片段中确认。
7.  **参数排序：** 研究最后通过龙卷风图表示各因素对总热回收影响的相对重要性层次 [Asai 2018, pp. 1-2]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 基于FORGE场址低渗花岗闪长岩储层设计模拟 | [Asai 2018, pp. 3-4] | FORGE场地，真垂深2500m参考温度200°C，孔隙度<1%，渗透率5-30 mD | 为EGS模拟提供了真实地质背景 |
| 井间距从100m增至300m时，产出水温度下降更快，但累计热回收量更少 | [Asai 2018, pp. 5-7] | 其他参数（裂缝间距、井斜角、注入温度、注入速率）保持在各自的中值水平 | 替代模型生成的表面图分析结果 |
| 水平井系统（井斜角90°）的热性能优于倾斜井系统 | [Asai 2018, pp. 7-9] | 第一级裂缝位置（井趾处）固定 | 因为水平井系统中的裂缝处于相同温度区，且井间岩石体积的平均温度更高 |
| 注入温度80°C比120°C导致产出水温度下降更快，但30年总热回收量更高 | [Asai 2018, pp. 7-9] | 其他参数保持在中值 | 温差是热交换的驱动力，较低温度加快了热提取速率 |
| 替代模型为二阶多项式函数，共建立59个时间点模型 | [Asai 2018, pp. 4-5] | 0-30年运行周期，5个输入变量，包含二阶交互项 | 模型公式为 \( \log(f(...)) \) 形式，每个模型有21个系数 |
| 实验设计使用Box-Behnken方法，训练数据41组，测试数据10组 | [Asai 2018, pp. 5-5] | 5变量，3水平设计（每变量取最大值、中值、最小值） | 井斜角通过取倒数进行线性化 |

## Limitations
- **替代模型近似性：** 替代模型是对复杂数值模拟的简化近似，其预测能力受限于训练数据的范围和模型形式（二阶多项式） [Asai 2018, pp. 4-5]。
- **数值模拟假设：** 模拟行为基于FORGE场地的特定地质模型，其普遍性未经验证。模型假设了一个包含垂直水力裂缝的双井系统，实际裂缝网络的几何形态和分布可能更复杂 [Asai 2018, pp. 2-3]。
- **时间点离散化：** 虽然选择了59个时间点，但温度剖面的某些剧烈变化区域（如早期）可能未被完全捕捉，依赖于插值平滑 [Asai 2018, pp. 4-5]。
- **研究范围局限：** 研究仅考察了五个参数，且每个参数的变化范围有限（如井间距100-300米）。其他潜在重要参数（如储层渗透率、裂缝导流能力等）的影响未被涉及。评估的经济性也未考虑，将热回收等同于性能 [Asai 2018, pp. 5-7]。

## Assumptions / Conditions
- **储层条件：** 数值模拟基于FORGE场地的原位特性，属于传导型、低孔低渗的花岗闪长岩储层 [Asai 2018, pp. 3-4]。
- **系统构型：** 研究采用一个简化的双井EGS模型，包含一口注入井和一口生产井，通过多级垂直水力裂缝连接 [Asai 2018, pp. 2-3]。
- **流体性质：** 工作流体水在系统闭环中以液态形式运行，通过维持高压防止闪蒸和冷凝损失 [Asai 2018, pp. 2-3]。
- **实验设计范围：** 所有结论仅在所设定的参数水平（最小值、中值、最大值）范围内有效。例如，井斜角被转换为倒数以便线性插值于水平 [Asai 2018, pp. 5-5]。
- **参数独立性：** 进行单因素影响分析时，假设其他参数可以保持在各自的中值水平不变 [Asai 2018, pp. 5-7]。

## Key Variables / Parameters
- **输入变量（控制因素）：**
    - \( X_1 \)：井间距 (Well spacing, 100–300 m)
    - \( X_2 \)：裂缝间距 (Fracture spacing, 50–100 m)
    - \( X_3 \)：井斜角 (Angle of well inclination, 90°–45°, 使用1/degree进行编码)
    - \( X_4 \)：注入温度 (Injection temperature, 80–120 °C)
    - \( X_5 \)：总注入速率 (Total injection rate, 5000–10000 m³/day) [Asai 2018, pp. 5-7]
- **模型输出变量：**
    - \( f(...) \) / \( T_p \)：产出水温度 (Produced water temperature)，为时间函数 [Asai 2018, pp. 4-5]
- **性能评价指标：**
    - \( H \)：总热提取量 (Total Heat Extraction) [Asai 2018, pp. 5-7]
    - R²：决定系数 [Asai 2018, pp. 1-2]
    - NRMSE：归一化均方根误差 [Asai 2018, pp. 1-2]
- **公式物理参数：**
    - \( Q \)：流量，\( \rho \)：流体密度，\( c_p \)：流体热容 [Asai 2018, pp. 5-7]。

## Reusable Claims
- **Claim 1:** 对于基于犹他州FORGE场地的低渗传导型地热储层中的双井EGS系统，在100-300m范围内增加井间距，会减缓产出水温度的下降速率，并增加长期累计热回收量 [Asai 2018, pp. 5-7]。此结论基于其他参数（裂缝间距、井斜、注入温度、注入速率）保持在中值水平这一条件。
- **Claim 2:** 在井趾位置固定的情况下，水平生产井（井斜角90°）的EGS系统在热提取方面优于倾斜井系统，因为其裂缝处于相同温度区，且井间加热岩石体积的平均温度更高 [Asai 2018, pp. 7-9]。此条件适用于本研究的双井多级垂直裂缝构型。
- **Claim 3:** 虽然降低注入温度（如从120°C降至80°C）会加速产出水温度的下降，但由于增大了注入流体与储层岩石之间的温差（热交换驱动力），在30年运行周期内能实现更高的总热回收量 [Asai 2018, pp. 7-9]。此结论基于储层总可回收热量恒定的假设，并认为地面设备可以处理较低的产出温度。
- **Claim 4:** 使用Box-Behnken实验设计结合二阶多项式代理模型，可以有效减少评估EGS性能所需的计算密集型数值模拟次数，并可用于参数敏感性分析和排序 [Asai 2018, pp. 5-5]。

## Candidate Concepts
- [[EGS]]
- [[Surrogate model]]
- [[Sensitivity analysis]]
- [[Design of experiments (DOE)]]
- [[Box-Behnken design]]
- [[Heat recovery]]
- [[Doublet well system]]
- [[Hydraulic fracture]]
- [[Fracture spacing]]
- [[Well spacing]]

## Candidate Methods
- [[Box-Behnken Design]]
- [[Polynomial surrogate model]]
- [[Numerical simulation of EGS]]
- [[Sensitivity Study]]

## Connections To Other Work
- **从主题上连接：** 本文研究的双井、多级裂缝EGS构型及敏感性分析，可连接到更广泛的[[EGS]][[Numerical simulation]]和[[Optimization]]研究。文中提及的研究如[[triplet well layout]]的性能对比、[[fracture geometry]]影响、[[flow pattern]]对寿命的主导作用等，均为相关领域。
- **与本研究直接关联的引用工作：**
    - Frash et al. [6] 研究了双井/三井系统的钻井和井轨迹设计 [Asai 2018, pp. 2-2]。
    - Chen et al. [11] 对双井EGS进行了敏感性分析，结论指出热提取速率和系统寿命主要取决于储层中的流动模式 [Asai 2018, pp. 2-2]。
    - Xia et al. [14] 进行了裂缝间距、井斜角和注入流量的敏感性研究 [Asai 2018, pp. 2-2]。
    - Aliyu et al. [15] 考虑了注入流量、流体注入温度和横向井间距的影响 [Asai 2018, pp. 2-2]。

## Open Questions
- 未从索引片段中确认的替代模型在所有59个时间点和全参数空间内的具体R²和NRMSE拟合精度数值。
- 龙卷风图揭示的各参数对总热回收影响的具体排序（即哪个参数最重要）未在片段中明确。
- 裂缝间距的具体影响分析结果未在片段中出现。
- 注入速率对产出水温度和热回收的具体影响趋势和机制未在片段中详细说明。
- 文中所提到的“性能”评估是否包含经济性或其他非热力学指标，片段未直接说明。

## Source Coverage
本页内容依据所提供的12个索引片段整理而成。片段内容覆盖了论文的摘要、引言、方法论、部分结果和讨论，主要聚焦于研究背景、模型建立方法和主要因素影响分析。论文的“结果与讨论”章节中关于裂缝间距和注入速率的详细分析、参数排序的具体结果（龙卷风图）以及最终的结论部分未在索引片段中充分体现。
