---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-zhou-thermal-experiments-for-fractured-rock-characterization-theoretical-analysis-and-inver"
title: "Thermal Experiments for Fractured Rock Characterization: Theoretical Analysis and Inverse Modeling."
status: "draft"
source_pdf: "data/papers/2021 - Thermal Experiments for Fractured Rock Characterization Theoretical Analysis and Inverse Modeling.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Zhou, Zitong, et al. \"Thermal Experiments for Fractured Rock Characterization: Theoretical Analysis and Inverse Modeling.\" *Water Resources Research*, vol. 57, 2021, doi:10.1029/2021WR030608."
indexed_texts: "15"
indexed_chars: "70944"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "70572"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.994756"
coverage_status: "full-index"
source_signature: "3c6e15334afedc35a231322d1182020213838b0e"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:50:36"
---

# Thermal Experiments for Fractured Rock Characterization: Theoretical Analysis and Inverse Modeling.

## One-line Summary
本文开发了一种基于深度神经网络替代模型的贝叶斯反演方法，用于从跨孔热示踪实验数据中推断离散裂缝网络（DFN）的两个统计参数：裂缝密度和分形维数，并通过合成实验验证了方法的有效性 [Zhou 2021, pp. 1-2]。

## Research Question
如何利用跨孔热实验中的热突破曲线数据来估计离散裂缝网络的统计参数，特别是裂缝密度 \( C \) 和分形维数 \( D \)？[Zhou 2021, pp. 2-3]

## Study Area / Data
研究基于合成热示踪实验，在 100×100 m² 的二维域内生成离散裂缝网络，裂缝方向为 25° 和 145°，裂缝孔径固定为 5×10⁻⁴ m [Zhou 2021, pp. 3-4]。裂缝网络参数 \( C \) 和 \( D \) 的生成范围分别为 \( C \in [2.5, 6.5] \) 和 \( D \in [1.0, 1.3] \)，这些范围基于现场观测和先前数值研究 [Zhou 2021, pp. 8-9]。合成数据通过注入 100 个粒子生成热突破时间的累积分布函数（CDF），未考虑测量误差 [Zhou 2021, pp. 5-6]。附录 A 中提供了来自 Bonnet et al. (2001) 的现场尺度裂缝网络观测数据，用于推导先验概率密度函数 [Zhou 2021, pp. 14-18]。

## Methods
- **正向模型**：采用 Watanabe 和 Takahashi (1995) 的分形模型描述 DFN，通过幂律关系 \( N_r = C r^{-D} \) 关联裂缝数量与相对长度 [Zhou 2021, pp. 3-4]。流体流动被建模为单相稳态层流，假设基质不渗透，通过泊肃叶定律计算裂缝中的流速 [Zhou 2021, pp. 4-5]。热传输采用基于粒子的方法，结合裂缝中的一维对流和基质中的一维热传导，在裂缝交叉点假设完全混合 [Zhou 2021, pp. 4-5]。正向模型用于计算热粒子到达时间的累积分布函数，并转换为逆累积分布函数（iCDF）[Zhou 2021, pp. 5-6]。
- **神经网络替代模型**：部署全连接神经网络（FCNN）作为正向模型的替代，以降低计算成本 [Zhou 2021, pp. 5-6]。FCNN 输入为扩展的参数向量 \( \mathbf{m}_{\text{NN}} = (C, D, C^{1/D}, C^{-D}, CD, 1/D)^\top \)，输出为 iCDF 的离散值，使用 Hellinger 距离作为损失函数，并通过 Adam 优化器进行训练 [Zhou 2021, pp. 6-8]。训练数据由 10⁴ 个参数对生成，其中 8000 用于训练，2000 用于测试，最优 FCNN 结构有六层隐藏层 [Zhou 2021, pp. 8-11]。
- **贝叶斯反演**：采用贝叶斯更新框架，通过网格搜索探索参数空间；先验信息可调节，通过超参数 \( \gamma \in [0,1] \) 控制先验权重 [Zhou 2021, pp. 6-8]。在无先验信息（\( \gamma = 0 \)）时，似然函数基于预测 iCDF 与观测 iCDF 的 Hellinger 距离，并假设高斯分布 [Zhou 2021, pp. 6-7]。引入两种先验：现场数据的相关先验和基于网络连接性的先验，后者通过 20 次随机实现中联通网络的数量定义 [Zhou 2021, pp. 11-14]。

## Key Findings
- 神经网络替代模型可准确估计给定参数 \( (C, D) \) 下热突破时间的平均 iCDF，且计算速度比正向物理模型快 4 个数量级（网络训练时间约 37,340 秒，执行时间 1.26 秒，而物理模型 10⁴ 次运行需 1.312×10⁸ 秒）[Zhou 2021, pp. 11-12]。
- 裂缝密度 \( C \) 受数据良好约束，可被精确估计；而分形维数 \( D \) 的推断较为困难 [Zhou 2021, pp. 11]。
- 加入先验信息（如现场数据相关或网络连接性）可锐化后验概率密度函数，减少高概率参数区域 [Zhou 2021, pp. 11-14]。
- 连接性先验比相关先验更有效，能确保真实参数值位于高概率区域内 [Zhou 2021, pp. 12-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 神经网络替代模型可将反向问题计算成本降低 4 个数量级 | [Zhou 2021, pp. 11-12] | 基于 FCNN 替代正向模型；训练数据 10⁴ 个样本 | 训练时间 37,340 秒，物理模型 10⁴ 次运行需 1.312×10⁸ 秒 |
| 裂缝密度 \( C \) 比分形维数 \( D \) 更易从热突破数据中推断 | [Zhou 2021, pp. 11] | 无先验贝叶斯反演；参数范围 \( C \in [2.5, 6.5] \), \( D \in [1.0, 1.3] \) | \( C \) 影响空间范围，\( D \) 影响长度分布 |
| 连接性先验改善 \( D \) 的推断，且真实参数值位于高概率区域 | [Zhou 2021, pp. 12-14] | 先验基于 20 次随机实现中联通网络数量；\( \gamma = 0.5 \) 或 1.0 | 比无先验或相关先验更锐化后验 |
| 粒子方法可高效模拟 DFN 中热传输，平均模拟时间 ≤ 1 秒 | [Zhou 2021, pp. 8-9] | 参数 \( N_{\text{part}} = 100 \), \( p_{\text{lim}} = 0.5 \)；20 次随机实现 | 权衡计算时间与精度 |

## Limitations
- 研究限于二维离散裂缝网络，具有两个未知参数；扩展到三维和更多参数不需要重大实现工作，但未验证 [Zhou 2021, pp. 14]。
- 神经网络替代模型的精度和鲁棒性在近似 iCDF 方面缺乏系统分析；超参数调整耗时 [Zhou 2021, pp. 14]。
- 方法直接应用于其他热实验可能存在问题，若实验设置与本研究差异较大，需要迁移学习 [Zhou 2021, pp. 14]。

## Assumptions / Conditions
- 岩石基质对流体不渗透；流体为稳态层流 [Zhou 2021, pp. 4-5]。
- 裂缝交叉点假设完全混合，粒子进入裂缝的概率仅取决于节点流量 [Zhou 2021, pp. 4-5]。
- 热传输中，裂缝中的纵向扩散可忽略；基质中热传导为一维 [Zhou 2021, pp. 4-5]。
- 正向模拟中，移除流速可忽略的裂缝段，死端段隐含在基质等效扩散特性中 [Zhou 2021, pp. 4-5]。
- 合成实验假设无测量误差；热突破曲线基于完全混合假设 [Zhou 2021, pp. 5-6, 8-9]。

## Key Variables / Parameters
- **DFN 参数**: \( C \) (裂缝密度), \( D \) (分形维数), 范围 \( C \in [2.5, 6.5] \), \( D \in [1.0, 1.3] \) [Zhou 2021, pp. 8-9]。
- **实验参数**: 水力梯度 \( J = 0.01 \), 热扩散系数 \( D_{\text{therm}} = 9.16 \times 10^{-7} \, \text{m}^2/\text{s} \), 裂缝孔径 \( 5 \times 10^{-4} \, \text{m} \) [Zhou 2021, pp. 3-4, 8-9]。
- **模拟参数**: 粒子数 \( N_{\text{part}} = 100 \), 矩阵传导截断概率 \( p_{\text{lim}} = 0.5 \) [Zhou 2021, pp. 8-9]。
- **反演参数**: 似然标准差 \( \sigma_d = 0.4 \), 先验权重 \( \gamma \in [0, 1] \) [Zhou 2021, pp. 6-7]。
- **神经网络参数**: 输入向量长度 \( N_m = 2 \), 输出 iCDF 长度 \( N_k = 50 \), 隐藏层数 6 [Zhou 2021, pp. 5-6, 9-11]。

## Reusable Claims
- 在合成热示踪实验中，裂缝密度 \( C \) 可通过贝叶斯反演从突破时间 CDF 中可靠估计，而分形维数 \( D \) 的估计不确定性较高；条件是参数范围限于 \( C \in [2.5, 6.5] \) 和 \( D \in [1.0, 1.3] \)，且使用均匀先验 [Zhou 2021, pp. 11]。
- 添加连接性先验（基于 DFN 随机实现中联通网络的比例）可显著锐化 \( C \) 和 \( D \) 的后验分布，并确保真实参数落入高概率区域；条件是需要 20 次以上随机实现和参数 \( \gamma = 0.5 \) 或 1.0 [Zhou 2021, pp. 12-14]。
- 神经网络替代正向模型可在训练后以极低成本执行大量前向运行，使网格搜索贝叶斯反演成为可能；但前提是训练数据充分且神经网络架构正确，且适用于低维参数空间 [Zhou 2021, pp. 6-8, 11-12]。
- WT 分形模型 \( N_r = C r^{-D} \) 可简化为 Davy et al. (1990) 模型，参数关系为 \( \alpha = CD/N_f \), \( L/D = D \), \( a = D+1 \)；这允许用最少参数代表自相似裂缝网络 [Zhou 2021, pp. 3-4]。

## Candidate Concepts
- [[discrete fracture network]]
- [[fractal dimension]]
- [[fracture density]]
- [[heat tracer]]
- [[cumulative distribution function]]
- [[inverse cumulative distribution function]]
- [[Hellinger distance]]
- [[Bayesian inversion]]
- [[particle-based heat transfer model]]
- [[Watanabe and Takahashi model]]

## Candidate Methods
- [[particle tracking for thermal transport in fractures]]
- [[deep neural network surrogate for iCDF prediction]]
- [[fully connected neural network with ReLU activation]]
- [[Latin hypercube sampling for parameter space exploration]]
- [[grid search Bayesian update with tunable prior weight]]
- [[connectivity-based prior PDF construction]]
- [[Adam optimizer for neural network training]]
- [[Hellinger loss function for quantile regression]]

## Connections To Other Work
- 基于 Watanabe 和 Takahashi (1995) 的裂缝网络分形模型，揭示了其与 Davy et al. (1990) 的自相似断裂模型等价 [Zhou 2021, pp. 3-4]。
- Gisladottir et al. (2016) 的粒子热传输方法是本正向模型的基础，展示了断裂密度和分形维数对突破曲线形状的影响 [Zhou 2021, pp. 4-5]。
- 现场数据来自 Bonnet et al. (2001) 的裂缝系统统计，用于构建先验 PDF [Zhou 2021, pp. 14-18]。
- 反演方法借鉴了多种加速马尔可夫链蒙特卡洛和异构卡尔曼滤波技术，如 Barajas-Solano et al. (2019) 和 Mo et al. (2019) [Zhou 2021, pp. 6-8, 16-17]。

## Open Questions
- 如何改进分形维数 \( D \) 的推断精度，例如通过额外的示踪数据或先验信息？[Zhou 2021, pp. 11-14]
- 方法能否有效扩展到三维 DFN 和更多统计参数（如断裂长度分布）？这不会显著增加计算成本，但未验证 [Zhou 2021, pp. 14]。
- 神经网络替代的 iCDF 近似精度和单调性保证需要系统分析；在实验设置变化时，迁移学习的可行性待探索 [Zhou 2021, pp. 14]。

## Source Coverage
All non-empty indexed fragments (15 blocks, 70,944 characters) were processed, yielding 15 compiled source blocks with 70,572 characters. Coverage ratio by blocks: 1.0; by characters: 0.994756. The fragments fully cover the original paper sections, including introduction, models, inversion, experiments, and conclusions [Zhou 2021, pp. 1-18].
