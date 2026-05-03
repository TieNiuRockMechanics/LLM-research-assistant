---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn"
title: "A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation."
status: "draft"
source_pdf: "data/papers/2025 - A back-propagation neural network optimized by genetic algorithm for rock joint roughness evaluation.pdf"
collections:
citation: "Song, Leibo, et al. \"A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 3054-72, doi:10.1016/j.jrmge.2024.10.022. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72693"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:51:56"
---

# A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation.

## One-line Summary
本文提出一种利用遗传算法优化的反向传播（GA-BP）神经网络评价岩石节理粗糙度系数（JRC）的新方法，通过五个统计参数捕捉节理表面形态的倾角、高度和背坡特征，以解决传统评价方法无法充分刻画复杂形态与粗糙度之间非线性关系的问题 [Song 2025, pp. 1-2]。

## Research Question
如何构建一种能够充分考虑节理表面三维形态特征及其方向依赖性的粗糙度评价方法，以更准确地预测JRC？传统2D参数（如Z₂、Rp）仅提供有限的几何信息，而3D参数在描述倾角、高度和背坡等方面的综合影响时仍存在局限，难以完整捕捉剪切行为与表面形态之间的非线性关系 [Song 2025, pp. 1-3]。

## Study Area / Data
- 实验剪切试验对象：四种锯齿状节理（A、B、C、D，用于分别研究倾角、高度和背坡特征的影响）以及一组天然节理（E，用于分析剪切方向的影响）[Song 2025, pp. 3-4]。
- 参数量化所用数据：105组数据集，每组包含平均倾角、中值倾角、平均高度、高度变异系数和背坡特征值（K）这五个统计参数及其对应的JRC值 [Song 2025, pp. 1-2]。
- 倾角分布验证数据：取自中国六个岩土工程现场（锦屏二级水电站、白鹤滩水电站、大石子山隧道、锦屏地下实验室、巴渝隧道、双江口水电站）的37个天然节理试样，分析区域统一标准化为100 mm × 100 mm以消除尺寸效应，验证视倾角的正态分布特性 [Song 2025, pp. 8-9]。
- 标准剖面参考：十条标准JRC剖面用于参数分析 [Song 2025, pp. 9-11]。

## Methods
- **定向剪切试验**：利用3D扫描与3D打印技术制备节理试样（配合比水泥∶砂∶水=1∶1∶0.2），在法向应力0.01 MPa至9.55 MPa下进行剪切试验，研究不同几何特征（倾角、高度、背坡、剪切方向）对剪切强度、剪胀和破坏特征的影响 [Song 2025, pp. 3-5]。
- **形态特征量化**：定义并计算五类简单统计参数，包括视倾角（平均倾角、中值倾角，基于2D和3D视倾角公式（1）（2））、高度特征（平均高度、高度变异系数，由相对高度公式（3）统计算得）以及背坡特征值（K，由正向与反向负向面积/体积之比K₂D、K₃D表征，公式（4）（5））[Song 2025, pp. 5-11]。
- **GA-BP神经网络建模**：使用包含输入层、隐蔽层和输出层的BP神经网络作为基础回归模型；因BP算法对初始权值敏感、易陷入局部极小，引入具有强全局搜索能力的遗传算法（GA）优化网络初始权值和阈值，构建GA-BP模型。利用105组数据集训练模型，将五类统计参数作为输入，预测输出JRC [Song 2025, pp. 11-12]。
  - 未从索引片段中确认GA-BP模型的具体网络结构（隐蔽层层数、神经元数）、GA参数（种群大小、交叉/变异方式）以及训练/测试集划分方式。

## Key Findings
- **倾角与高度效应的实验证据**：在相同法向应力下，倾角越大的锯齿节理获得的剪切强度越高；具有相同倾角但更大高度的节理会表现出更高的剪切强度峰值和更明显的剪胀，高度特征显著影响节理的破坏模式 [Song 2025, pp. 3-5]。
- **背坡特征的贡献**：在同样上倾角条件下，背坡面积（或体积）比例越大（即K值越大），剪切强度越高，表明背坡面对剪切阻力的贡献不可忽略 [Song 2025, pp. 11]。
- **方向依赖性与各向异性**：天然节理沿不同方向剪切时，其变形、强度和破坏特征表现出明显的方向性；平均倾角、中值倾角和K值均呈现方向性变化，三者的最大值方向通常一致，K值的最大值与最小值方向往往相反，可有效表征节理形态的各向异性 [Song 2025, pp. 5-8, 11-12]。
- **倾角分布规律**：37个天然节理的视倾角分布近似正态分布，支持使用平均值和期望值来描述倾角特征 [Song 2025, pp. 8-9]。
- **单一角度参数的不足**：分析十条标准JRC剖面的平均倾角和期望值发现，JRC增大时两者总体上升，但第4条剖面出现异常，表明仅靠倾角参数不足以完全评价粗糙度，必须结合高度与背坡特征 [Song 2025, pp. 9-11]。
- **GA-BP模型的适用性**：初步构建的GA-BP神经网络模型能够利用五类统计参数预测JRC，提供了刻画复杂节理形态与粗糙度非线性关系的新途径 [Song 2025, pp. 1-2]。未从索引片段中确认该模型的具体预测精度（如R²、RMSE）或与其他方法的对比结果。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 高倾角锯齿提供更大剪切强度，剪切位移-强度曲线和剪胀曲线表现出相应特征 | [Song 2025, pp. 3-4] | 锯齿节理A，法向应力0.01、0.05、1.0、2.0 MPa | 倾角越大，接触越充分，强度越高 |
| 同等倾角下，高度更大的节理（B比A）表现出更高的剪切强度峰值和更大的剪胀量 | [Song 2025, pp. 3-5] | 锯齿节理A与B对比，法向应力2.0 MPa（及其他应力） | 综合图3和图4（Liu et al., 2018b） |
| 背坡特征K值较大的锯齿节理（C，K=0.568）比较小的节理（D，K=0.399）剪切强度更高 | [Song 2025, pp. 11] | 锯齿节理C和D，上倾角相同（45°），法向应力0.5、1.0、8.0 MPa | K值由公式（4）（5）定义 |
| 天然节理在不同方向（0°、90°、180°、270°）剪切时，强度、变形和破坏特征存在显著差异 | [Song 2025, pp. 5-8] | 天然节理E，法向应力0.60~9.55 MPa | 证明方向性影响 |
| 37个天然节理的视倾角分布经检验与正态分布一致性高 | [Song 2025, pp. 8-9] | 六个工程现场试样，100 mm×100 mm区域 | 支持使用平均值和期望值表征倾角 |
| 十条标准JRC剖面的平均倾角和期望值总体上随JRC增大而增大，但第四剖面出现异常，单一倾角参数不足以完全预测JRC | [Song 2025, pp. 9-11] | 标准JRC剖面 | 图11；提示需要结合高度和背坡特征 |
| 平均倾角、中值倾角和K值均表现出方向性，最大K值与最大倾角方向一致，最大和最小K值方向往往相反 | [Song 2025, pp. 11-12] | 各类分析节理 | 可综合表征各向异性 |
| 基于105组包含五类统计参数与对应JRC的数据集，构建了GA-BP神经网络用于JRC预测 | [Song 2025, pp. 1-2] | 数据集来源未从片段完全确认 | 模型具体精度和验证细节未从索引片段确认 |

## Limitations
- 剪切试验仅基于四种锯齿节理和一种天然节理，所得结论的普适性受样本类型限制。
- GA-BP模型的预测性能（如误差指标、泛化能力）在提供的片段中未报告，无法评估其准确性和实用可靠性。
- 模型训练所用的105组数据集的具体组成（节理来源、JRC获取方式、是否涵盖足够多样的形态）未从索引片段中确认。
- 研究采用标准化100 mm × 100 mm区域以减少尺寸效应，但尺度对粗糙度参数的影响仍需进一步探讨。
- 所用五个统计参数虽综合了倾角、高度和背坡信息，但可能忽略其他影响剪切行为的形态特征（如表面曲率、起伏度等），其完备性需更多实验验证。
- 背坡特征值K与经典JRC的关系仅在有限的锯齿节理和标准剖面上进行过讨论，针对高度不规则天然节理的适用性尚需证实。

## Assumptions / Conditions
- 节理的剪切行为主要由倾角、高度和背坡三类几何特征控制，其他表面形态因素可视为次要。
- 视倾角服从正态分布，并且该分布特性在不同工程现场节理中普遍成立（通过37个试样验证，但样本规模有限）。
- 剪切过程中，背坡面能通过提供额外的抗剪面积/体积来贡献强度，这一机制在锯齿节理和天然节理中具有类似性。
- BP神经网络具备捕捉五类统计参数与JRC之间非线性映射的能力；引入GA优化初始权值和阈值可以避免局部极小，从而获得更稳定的预测模型。
- 试验采用3D扫描和3D打印技术复制的节理试样能够真实反映原始表面形态，且混凝土材料的力学性质可以代表典型岩石节理的剪切响应。
- 训练GA-BP模型所需的105组数据足以代表一定范围的节理形态及对应的JRC变化规律。

## Key Variables / Parameters
- JRC（节理粗糙度系数）
- 输入模型的特征参数：平均视倾角、中值视倾角、平均高度、高度变异系数、背坡特征值 K（含K₂D 和 K₃D）
- 视倾角计算公式：θ₂D公式（1）、θ₃D公式（2）
- 相对高度定义： h = yᵢ − yₘᵢₙ （公式（3））
- 背坡特征值定义：K₂D（公式（4））、K₃D（公式（5））
- 试验条件参数：法向应力 σₙ、剪切方向
- GA-BP神经网络相关参数（结构权值、阈值、GA的进化算子等；未从索引片段中确认具体数值）

## Reusable Claims
1. 若仅使用平均倾角或期望值来估算JRC，可能会在部分节理上产生较大偏差（如标准剖面第四条所示），因此需要同时纳入高度特征和背坡特征才能更全面地评价粗糙度。 [Song 2025, pp. 9-11]  
   **适用条件**：对具有显著高度变异和/或不对称形态的自然节理。  
   **限制**：证据主要来自十条标准剖面，天然节理上的一般性还需更多现场数据支撑。  
2. 在同样上倾角条件下，背坡特征值K越大（即背坡面积或体积占比越大），节理的抗剪强度越高。因此K可作为评价节理粗糙度方向依赖性的关键参数。 [Song 2025, pp. 11]  
   **适用条件**：剪切方向明确，且背坡面能够参与咬合与磨损的节理。  
   **限制**：目前仅在锯齿形节理C和D上进行了直接对比，对自然不规则节理仍需验证。  
3. 节理的平均视倾角、中值视倾角和背坡K值均表现出系统的方向性，三者的最大方向通常一致，可用于定量描述节理剪切行为的各向异性。 [Song 2025, pp. 11-12]  
   **适用条件**：基于3D扫描获取的连续表面数据，按不同方向提取参数进行分析。  
   **限制**：上述关系基于本研究所用节理，对于含有更复杂台阶状、波浪状形态的节理，各向异性方向性规律可能更复杂。  
4. GA-BP神经网络可以结合BP的非线性逼近能力和GA的全局寻优能力，用于建立节理统计参数到JRC的映射，为复杂表面粗糙度评价提供数据驱动方法。 [Song 2025, pp. 1-2, 11-12]  
   **适用条件**：具备充足且准确的参数‑JRC 配对数据集，输入参数应覆盖影响剪切行为的主要形态变量。  
   **限制**：模型的具体结构和训练策略未从索引片段中确认；实际应用中需校核模型的过拟合风险与对新节理类型的泛化能力。

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[genetic algorithm-optimized back-propagation neural network (GA-BP)]]
- [[rock joint shear strength]]
- [[apparent dip angle]]
- [[statistical parameters for joint roughness]]
- [[back slope morphological feature]]
- [[anisotropy of joint roughness]]
- [[directional dependence of joint behavior]]
- [[3D scanning in rock mechanics]]
- [[3D printing of joint specimens]]
- [[normal distribution of dip angles]]
- [[standard JRC profiles]]

## Candidate Methods
- [[back-propagation (BP) algorithm]]
- [[genetic algorithm (GA) optimization]]
- [[direct shear test on rock joints]]
- [[3D laser scanning of joint surfaces]]
- [[3D printing for physical joint modelling]]
- [[statistical parameter calculation from surface data]]
- [[apparent dip angle formulation]]
- [[height coefficient of variation]]
- [[K-value analysis for back slope features]]
- [[GA-BP neural network for regression]]

## Connections To Other Work
本研究在粗糙度参数化方面直接建立在已有的2D/3D统计参数工作之上，包括 Tse & Cruden (1979) 的Z₂、El‑Soudani (1978) 的Rp，以及 Belem et al. (2000)、Grasselli et al. (2002)、Tatone & Grasselli (2009) 和 Song et al. (2020) 等提出的3D参数概念 [Song 2025, pp. 2-3]。其中视倾角计算方法采用并拓展了 Grasselli et al. (2002) 的思路。实验制样方法参考了 Jiang et al. (2016) 和 Jiang & Song (2018) 的3D扫描‑打印流程 [Song 2025, pp. 2-3]。节理倾角分布规律的分析利用了国内多个大型水电和隧道工程的节理数据（如 Jiang et al. 2010、Jiang et al. 2019、Ran et al. 2017、Feng et al. 2018、Hu et al. 2020、Liang et al. 2020）[Song 2025, pp. 8-9]。从广泛主题上看，该工作可与 [[fracture network roughness characterization]]、[[machine learning in rock engineering]] 等方向连接，但具体文献联系未从索引片段中确认。

## Open Questions
- GA-BP模型的预测准确度（如决定系数、均方根误差）如何？是否已与传统的统计参数回归方法或纯BP网络进行过系统对比？
- 模型所依赖的105组数据集的来源和JRC标定方式是否具有充分的多样性和客观性？对未知天然节理的泛化能力是否经过独立验证？
- 所选的五个统计参数在包含高度复杂形态（例如多尺度起伏、阶梯状节理）的节理中是否依然足够？是否需要引入其他特征（如分形维数、曲率等）？
- 背坡特征值K对非锯齿、随机粗糙表面的意义是否与本文锯齿试验所得规律一致？是否存在其他等效表征方式？
- 本方法的尺寸敏感性如何？100 mm × 100 mm的标准化区是否适用于所有工程尺度的节理？更大的采样区域是否需要不同的参数统计方式？
- GA-BP模型的稳健性和可重复性如何？针对不同地质环境（如高应力、充填节理）是否需要重新训练或调整参数？

## Source Coverage
本页面依据15个索引片段编写，覆盖了论文的摘要、引言、试验设计与方案、形态特征的量化方法以及GA-BP网络的总体构建思路等部分。具体内容涉及节理试样制备、剪切试验方案、五类统计参数的定义和计算公式，以及37个天然节理倾角分布验证等实验细节。但索引片段未能提供完整的结果与讨论部分，尤其缺乏GA-BP模型训练和验证的性能指标、与现有方法的定量对比、典型案例的预测结果以及潜在误差分析。因此，本页中关于模型精度、泛化能力和实际工程适用性的判断均受限于片段覆盖范围，重要最终性能信息处于“未从索引片段中确认”状态。
