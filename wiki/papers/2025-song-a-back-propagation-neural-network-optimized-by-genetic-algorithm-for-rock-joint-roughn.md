---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn"
title: "A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation."
status: "draft"
source_pdf: "data/papers/2025 - A back-propagation neural network optimized by genetic algorithm for rock joint roughness evaluation.pdf"
collections:
citation: "Song, Leibo, et al. \"A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 3054-72, doi:10.1016/j.jrmge.2024.10.022. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72693"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "73020"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004498"
coverage_status: "full-index"
source_signature: "35b61ff8fec0836d612f66f81c83a9aa7f019b46"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:07:11"
---

# A Back-Propagation Neural Network Optimized by Genetic Algorithm for Rock Joint Roughness Evaluation.

## One-line Summary
本文提出一种基于遗传算法优化反向传播（GA-BP）神经网络的方法，利用五个形态统计参数评估岩石节理粗糙度系数（JRC），相比传统统计参数法和分形参数法精度更高。

## Research Question
如何准确评价岩石节理的粗糙度系数（JRC），以更合理地反映节理表面复杂形态对剪切行为的影响？传统方法（对比法、反算法、统计参数法、分形参数法）或因主观性、或因不能充分捕捉二维/三维非线性关系而存在局限，因此需要一种能综合考虑多形态因素影响、具有更高预测精度的JRC评价方法。

## Study Area / Data
- **试样来源**：四个锯齿状节理（A、B、C、D）和一个天然节理（E）用于剪切试验，研究倾角、高度、背坡特征及剪切方向的影响 [Song 2025, pp. 2-3]。
- **天然节理数据库**：来自中国六个大型岩土工程现场：锦屏二级水电站、白鹤滩水电站、大石字山隧道、锦屏地下实验室、巴渝隧道和双江口水电站，共37个天然节理面 [Song 2025, pp. 8-9, 12-13]。
- **学习样本数据库**：共105组节理面点云数字信息，包含71组来自14位学者公开发表的数据（Barton and Choubey, 1977; Zhang et al., 2016; Song et al., 2017a, 2020; Wang et al., 2017; Liu et al., 2018b, 2019, 2023b; Zhou et al., 2018; Cui et al., 2019; Ban et al., 2020; Xu et al., 2020; Chen et al., 2021; Li et al., 2022），以及34组来自上述工程现场 [Song 2025, pp. 12-13]。
- **数据特征**：每组节理计算平均视倾角、视倾角期望值、平均高度、高度变异系数、背坡特征值K共五个统计参数，并确定对应的JRC值（部分由学者直接给出，部分通过反算法或统计参数法确定） [Song 2025, pp. 13-15]。
- **JRC值范围**：105个样本中绝大多数落在[0, 20]区间，与Barton标准剖面曲线公认范围一致 [Song 2025, pp. 13-15]。

## Methods
- **剪切试验**：利用三维扫描和3D打印技术制作锯齿节理及天然节理试样，采用RMT-150C岩石力学试验系统进行不同常法向应力下的直剪试验，探究倾角、高度、背坡形态和剪切方向对剪切行为的影响 [Song 2025, pp. 2-5]。
- **形态定量化**：
  - **倾角特征**：采用视倾角（2D和3D公式），对10条标准JRC曲线和37个天然节理进行概率分布分析，发现视倾角服从正态分布，选择平均视倾角和视倾角期望值作为量化指标 [Song 2025, pp. 5-9]。
  - **高度特征**：使用相对高度，Shapiro-Wilk检验表明高度分布不服从正态分布，最终选取平均高度和高度变异系数作为代表参数 [Song 2025, pp. 8-9]。
  - **背坡特征**：定义2D和3D背坡特征值K，反映负倾角面积（或体积）占比，其方向性与倾角参数呈现相反趋势 [Song 2025, pp. 9-11]。
  - **方向性**：计算37个天然节理在72个方向上的平均倾角、倾角期望和K值，三者均表现出显著各向异性，且最大/最小值方向对应剪切行为极值方向 [Song 2025, pp. 11-12]。
- **GA-BP神经网络模型构建**：
  - **网络结构**：输入层5节点（五个统计参数），单一隐含层6节点，输出层1节点（JRC）[Song 2025, pp. 12-15]。
  - **遗传算法优化**：种群规模61，进化代数200；选择、交叉（概率公式）、变异操作，以BP神经网络的MAE倒数作为适应度函数；优化初始权值阈值以避免局部极小 [Song 2025, pp. 11-13]。
  - **训练与测试**：从105组数据中抽取100组（含10条Barton标准曲线和70组随机节理）为训练集，剩余20组为测试集，重复随机划分10次；以RMSE、MAPE评估模型精度；训练中通过验证集提前停止防止过拟合 [Song 2025, pp. 15-16]。
- **对比验证**：利用训练好的GA-BP模型对5组额外节理（Ban et al. 2020; Wang et al. 2017; Chen et al. 2021）预测JRC，再结合JRC-JCS剪切强度公式估算不同法向应力下峰值抗剪强度，并与统计参数法（Z₂、θ*max/(C+1)）、分形参数法（D_Lee、D_AHD）的估算结果比较误差 [Song 2025, pp. 16-18]。

## Key Findings
1. **剪切行为的形态敏感性**：节理的变形与强度特征受表面倾角、高度和背坡形态的显著影响，并表现出方向依赖性；较大倾角、较高粗糙度起伏及更大背坡体积有利于增强接触，提高抗剪强度 [Song 2025, pp. 2-5, 17-18]。
2. **五参数定量方案**：平均视倾角、视倾角期望值、平均高度、高度变异系数以及背坡特征值K能够综合表征节理形态及其各向异性；视倾角服从正态分布，而高度不服从正态分布 [Song 2025, pp. 17-18]。
3. **GA-BP模型性能**：
   - 在100组训练-测试重复实验中，训练阶段RMSE围绕0.1波动，MAPE<1%；测试阶段最大误差多控制在3以内，RMSE约0.3，MAPE<6%；模型回归系数R>0.994，未出现明显过拟合 [Song 2025, pp. 15-16]。
   - 使用该模型估计JRC后反算的抗剪强度误差（最大15.91%，平均7.25%）显著低于统计参数Z₂（最大62.65%，平均27.97%）、θ*max/(C+1)（最大30.04%，平均11.74%）、分形参数D_Lee（最大42.98%，平均17.57%）和D_AHD（最大35.58%，平均16.56%）[Song 2025, pp. 16-18]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 节理剪切强度与峰值数目受法向应力和锯齿倾角控制；低法向应力下三个峰值对应60°、45°、30°顺序剪断，τp_1>τp_2>τp_3；较高法向应力下60°与45°同时接触剪断，仅出现两个峰值 | [Song 2025, pp. 3-4] | 锯齿节理A，法向应力0.01 MPa、0.05 MPa、1.0 MPa、2.0 MPa | 倾角特征直接影响剪切接触状态与强度 |
| 相同倾角时，锯齿高度加倍（节理B）使峰值剪切强度提高，剪胀量增大 | [Song 2025, pp. 4-5, 图3-4] | 节理A与B对比，法向应力2.0 MPa | 高度特征显著影响剪切强度与破坏模式 |
| 背坡形态差异导致节理C与D在法向应力≥1 MPa时抗剪强度差异（D-value）增大，且差异随法向应力增加而增大 | [Song 2025, pp. 5-6, 图5-6] | 背坡特征不同的锯齿节理C与D，法向应力0.5、1.0、8.0 MPa | 背坡在较高法向应力下参与剪切，贡献强度 |
| 天然节理E在不同剪切方向（0°、90°、180°、270°）下峰值及残余强度差异显著，90°方向最大，180°方向最小 | [Song 2025, pp. 6-7, 表3, 图7] | 天然节理，法向应力0.60 MPa、2.39 MPa、4.77 MPa、9.55 MPa | 方向性是评价节理地形不可忽略的因素 |
| 10条标准JRC剖面及37个天然节理的视倾角分布近似正态分布，但JRC值与平均/期望倾角并非单调正相关（如第4条剖面异常） | [Song 2025, pp. 7-9] | 点间距0.5 mm | 仅用单一倾角参数不足以全面评估粗糙度 |
| Shapiro-Wilk检验表明10条标准JRC曲线的高度分布p<0.05，否定正态性；37个天然节理中除BY-2D和JP-2U外均不符合正态分布 | [Song 2025, pp. 8-9, 表4, 图13] | 显著性水平0.05 | 高度特征不宜用正态分布描述 |
| 同一条节理在不同方向上的平均视倾角、倾角期望值具有相似的各向异性模式，而背坡特征K值的方向模式与之相反 | [Song 2025, pp. 11-12, 图16] | 37个天然节理72个方向分析 | 三个参数协同可表征节理各向异性 |
| GA-BP神经网络模型在100组随机训练-测试中RMSE约0.1（训练）、最大误差≤3（测试），MAPE<6%（测试） | [Song 2025, pp. 15-16] | 隐含层6节点，GA种群61，进化200代 | 模型稳定且精度较高 |
| 100组数据训练模型回归R值均>0.994，训练过程中误差经6次连续检验未下降即停止，未出现过拟合 | [Song 2025, pp. 15-16, 图22] | 采用验证集提前停止 | 模型泛化能力好 |
| GA-BP估算JRC所得抗剪强度平均误差7.25%，远低于统计参数（11.74%~27.97%）和分形参数（16.56%~17.57%） | [Song 2025, pp. 16-18, 图23] | 5组独立节理数据，法向应力若干水平 | 新方法在抗剪强度评价中更可靠 |

## Limitations
- 训练样本数量为105组，虽已覆盖多种节理类型，但仍可能未包含极端形态的节理，模型对未知样本的外推能力未经验证 [Song 2025, pp. 12-15]。
- 部分样本的JRC值是通过反算法或统计参数法间接确定的，这些JRC本身存在一定不确定性，可能影响模型训练标签的精度 [Song 2025, pp. 13-15]。
- 模型输入仅包含5个统计参数，未考虑尺度效应、节理壁面强度（JCS）等可能影响粗糙度感知的其它因素；抗剪强度验证仍依赖Barton JRC-JCS公式，其基本假设（如φb、JCS）在现场条件下可能难以准确获取 [Song 2025, pp. 2, 17]。
- 试验验证所用的节理材料为水泥砂浆，其力学性质与天然岩石有差异，模型在真实复杂岩体中的表现有待进一步检验 [Song 2025, pp. 3]。

## Assumptions / Conditions
- 节理视倾角近似服从正态分布，该假设经10条标准JRC曲线和37个天然节理检验成立 [Song 2025, pp. 7-9]。
- 背坡特征K值定义为负倾角对应的面积/体积占比，其数值越高表示背坡对剪切的贡献越大 [Song 2025, pp. 9-10]。
- GA-BP神经网络预测JRC时，默认输入的五参数与JRC之间存在可学习的非线性映射，且训练样本的JRC标签准确 [Song 2025, pp. 13-15]。
- 反算JRC时采用Barton JRC-JCS峰值抗剪强度公式（τp = σn·tan(φb + JRC·log10(JCS/σn))），并假设log10(JCS/σn)与剪切扩容角ip满足过原点的线性关系 [Song 2025, pp. 13-14]。
- 3D扫描点间距统一为0.5 mm，形态分析中未讨论点间距变化对参数及模型预测的影响 [Song 2025, pp. 7-8]。
- 模型训练时BP网络学习率设为0.01，迭代次数1000，误差容限1×10⁻⁶；遗传算法种群规模61，进化代数200 [Song 2025, pp. 15]。

## Key Variables / Parameters
- **输入变量（5个）**：平均视倾角，视倾角期望值，平均高度，高度变异系数，背坡特征值K（2D或3D）[Song 2025, pp. 9-11, 17]
- **输出变量**：节理粗糙度系数JRC [Song 2025, pp. 2, 15]
- **中间/关联变量**：法向应力σn，节理壁抗压强度JCS，基本摩擦角φb，峰值剪切强度τp，剪切扩容角ip [Song 2025, pp. 13-14]
- **对比验证用参数**：统计参数Z₂、θ*max/(C+1)；分形参数D_Lee、D_AHD [Song 2025, pp. 16-18]
- **网络结构参数**：输入层5节点，隐含层6节点（按经验公式确定），输出层1节点 [Song 2025, pp. 15]

## Reusable Claims
1. **关于形态参数选择**：在评价节理粗糙度时，平均视倾角、视倾角期望值、平均高度、高度变异系数和背坡特征值K是有效且能反映方向性的组合参数，可用于替代单一2D/3D统计参数 [Song 2025, pp. 17-18]。适用条件：具备高精度三维点云数据，且能计算视倾角和相对高度。
2. **关于倾角分布**：典型岩石节理的视倾角频率分布近似正态，因此平均视倾角和期望值是描述其分布的合适统计量 [Song 2025, pp. 8-9]。适用条件：节理面点云采样间距≤0.5 mm，节理形态无严重非均质性。
3. **关于高度分布**：多数节理的高度特征不服从正态分布，需采用中位数或变异系数等非参数描述 [Song 2025, pp. 9]。适用条件：经Shapiro-Wilk等正态性检验后不满足正态假设时。
4. **关于GA-BP模型精度**：利用上述五参数训练的GA-BP神经网络预测JRC，训练MSE<0.01，测试RMSE约为0.3，MAPE<6%，回归R>0.99，在不增加额外参数的情况下可避免明显过拟合 [Song 2025, pp. 15-16]。适用条件：数据库JRC值可靠，网络结构和GA超参按本文设定。
5. **关于抗剪强度评估**：基于GA-BP预测的JRC值，结合Barton JRC-JCS公式估算的抗剪强度，其平均误差为7.25%，显著低于用Z₂（27.97%）、θ*max/(C+1)（11.74%）、D_Lee（17.57%）和D_AHD（16.56%）估算的结果 [Song 2025, pp. 16-18]。此结论适用于与验证集相似的材料和节理类型，对其他岩体需谨慎外推。

## Candidate Concepts
- [[rock joint roughness coefficient (JRC)]]
- [[shear strength of rock joints]]
- [[apparent dip angle]]
- [[back slope feature (K)]]
- [[anisotropy of rock joints]]
- [[3D roughness parameter (θ*max/(C+1))]]
- [[fractal dimension (D_Lee, D_AHD)]]
- [[JRC-JCS shear strength criterion]]
- [[statistical parameter method for JRC]]
- [[back-calculation method for JRC]]
- [[genetic algorithm (GA)]]
- [[BP neural network]]
- [[overfitting in neural networks]]
- [[3D scanning and 3D printing in rock mechanics]]
- [[normal distribution assumption]]

## Candidate Methods
- [[genetic algorithm-optimized backpropagation (GA-BP) neural network]]
- [[statistical parameter quantification for joint roughness]]
- [[fractal parameter method for joint roughness]]
- [[back-calculation method using JRC-JCS model]]
- [[3D point cloud scanning and 3D printing for rock joint replicas]]
- [[direct shear test on rock joints under constant normal load (CNL)]]
- [[Shapiro-Wilk normality test]]
- [[regression analysis based on least squares]]
- [[root mean square error (RMSE) and mean absolute percentage error (MAPE) for model evaluation]]
- [[early stopping for neural network training]]

## Connections To Other Work
- **Barton (1973)、Barton & Choubey (1977) 的JRC-JCS模型**：本文继承其JRC概念和标准剖面曲线，并利用该公式进行抗剪强度反算与验证 [Song 2025, pp. 1-2, 13-14, 18]。
- **Tse & Cruden (1979) 的Z₂参数**：作为典型的2D统计参数，本文将其与另几个参数一同作为对比基线 [Song 2025, pp. 2, 16-17]。
- **Grasselli et al. (2002) 的视倾角及参数θ*max/(C+1)**：本文采用其视倾角定义，但注意到C=0时的局限性，改用Tatone & Grasselli (2010) 改进的参数θ*max/(C+1)作为对比方法之一 [Song 2025, pp. 2, 13-14, 16]。
- **3D统计参数研究**：Belem et al. (2000)、Tatone & Grasselli (2009)、Tang et al. (2012)、Sun et al. (2014)、Ge (2015)、Chen et al. (2016)、Ban et al. (2019)、Liu et al. (2018a, 2023a)、Song et al. (2020) 等提出的各类3D描述参数，均面临难以全面反映节理各向异性的局限，本文通过整合倾角、高度、背坡特征及方向性形成改进 [Song 2025, pp. 2-3]。
- **分形方法**：Lee et al. (1990) 的分形维数D_Lee和Ban et al. (2019) 的D_AHD用于对比，结果显示其抗剪强度误差显著大于GA-BP方法 [Song 2025, pp. 16-17]。
- **神经网络在岩石工程中的应用**：Ge et al. (2021) 使用BP神经网络和SVM研究微观结构对剪切行为的影响；Zhang et al. (2021) 用CNN预测岩爆特征；Fathipour-Azar (2022) 结合SVM-M5P-RF集成算法估算节理抗剪强度。本文在此基础上引入GA优化初始权值，提高了JRC预测的精度与稳定性 [Song 2025, pp. 2-3]。

## Open Questions
- 本文建立的GA-BP模型仅基于105组数据，其推广到更广泛节理类型（如充填节理、风化节理）的泛化能力尚需更大规模的数据库验证。
- 模型输入为五个人工选定的统计参数，是否可以结合自动特征提取方法（如CNN从点云直接学习）进一步减少人工干预？
- 点云扫描间距（0.5 mm）对参数计算及模型预测的敏感性如何？尺度效应在高度变异系数和背坡K中如何体现？
- 抗剪强度的最终评估仍依赖JRC-JCS经验公式，能否直接将GA-BP模型拓展到端到端的抗剪强度预测（即输入点云形态，输出τp）？
- 对不同岩石类型（硬度、各向异性程度）和不同边界条件（如常法向刚度CNS）的适用性未经验证。

## Source Coverage
本页面严格处理了全部15个非空索引片段（片段编号对应原文页码范围1-2, 2, 2-3, 3-5, 5-8, 8-9, 9-11, 11-12, 12-13, 13-15, 15-16, 16-18, 18, 18-19, 19）。覆盖率：片段数量100%（15/15），字符总数覆盖率100.45%（73,020/72,693）。所有陈述均来自提供的索引证据，未引入外部信息。
