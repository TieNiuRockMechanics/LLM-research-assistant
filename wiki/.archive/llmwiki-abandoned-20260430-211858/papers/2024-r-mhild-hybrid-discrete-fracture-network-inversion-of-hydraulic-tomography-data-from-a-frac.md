---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-r-mhild-hybrid-discrete-fracture-network-inversion-of-hydraulic-tomography-data-from-a-frac"
title: "Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site."
status: "draft"
source_pdf: "data/papers/2024 - Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site.pdf"
collections:
citation: "Römhild, Lukas, et al. “Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site.” *Water Resources Research*, vol. 60, no. 7, 2024."
indexed_texts: "18"
indexed_chars: "87979"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:04:22"
---

# Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site.

## One-line Summary
提出了一种基于混合离散裂缝网络（DFN）的水力层析成像（HT）数据反演方法，能够同时考虑裂缝流和多孔基质流，并在德国哥廷根（Göttingen）的裂隙–多孔野外场地数据上成功应用并验证 [Lukas 2024, pp. 1-1].

## Research Question
现有的离散裂缝网络（DFN）反演方法未考虑基质中的流动，而连续介质模型则忽视了单个裂缝的作用。裂隙岩体与多孔基质共同存在时，单独使用任一模型都不足。本研究旨在扩展 DFN 反演方法，通过引入非零基质渗透率的混合模型，实现更准确的水力特征刻画 [Lukas 2024, pp. 2-3].

## Study Area / Data
- **实验场地**：德国哥廷根大学北校区，位于德国下萨克森州南部 **Leinetalgraben** 沉陷带东缘 [Lukas 2024, pp. 3-5].
- **地质概况**：地质结构因多期构造活动复杂，岩性属于中、下 Keuper 层，主要由黏土序列和粉砂–砂岩层组成。表层 14 m 为含石英、长石、方解石矿化的第四纪灰岩与黏土岩 [Lukas 2024, pp. 3-5].
- **实验配置**：
  - 两口井（泵送井 O、观测井 M），目标深度为 45 m 以上的井间区域，配置 4 个泵送段（O2-O5）与 4 个观测段（M2-M5），呈现层析成像式配置 [Lukas 2024, pp. 3-5].
  - 采用多段抽水试验，抽水速率约 30 L min⁻¹ [Lukas 2024, pp. 3-5].
  - 观测段 M5 因噪声极高被排除 [Lukas 2024, pp. 3-5].
  - 泵送井中的压力数据（受三维扩散影响显著）未在二维正演模型中使用 [Lukas 2024, pp. 3-5].
- **验证数据**：独立的热示踪试验温度剖面 [Lukas 2024, pp. 1-1].

## Methods
### 1. 水力走时反演（Hydraulic Travel Time Inversion）
- 基于压力信号前几秒的水力走时，利用 **Dijkstra 算法** 和 **广义高斯-牛顿法** 进行射线追踪反演，推求水力扩散系数（hydraulic diffusivity *D*） [Lukas 2024, pp. 5-6].
- 通过乘以假设均匀的比储量 *S*ₛ (5 · 10⁻⁵ m⁻¹) 转换为导水系数 *K* [Lukas 2024, pp. 5-6].
- 使用 0.5 m 垂直/1 m 水平分辨率的矩形网格，以适应沉积环境层状结构并匹配较低的数据密度（仅 12 个走时，150 个网格单元） [Lukas 2024, pp. 5-6].
- 源/接收点设置在间隔顶部或底部，以最小化信号最短路径距离 [Lukas 2024, pp. 5-6].

### 2. 混合 DFN 随机反演
- **正演模型**：建立包含二维离散裂缝与多孔基质的混合模型。基质导水系数 *K*_matrix = 10⁻⁶ m s⁻¹，比储量 *S*ₛ = 5 · 10⁻⁵ m⁻¹（基于现场单井多段抽水试验与配线分析法结果） [Lukas 2024, pp. 7-7].
- **裂缝参数**：由光学钻孔电视数据确定三组裂缝方位（倾角 −0.94°, −26.31°, 49.64°），裂缝方位在整个反演中固定 [Lukas 2024, pp. 7-7].
- **反演算法**：
  - 采用贝叶斯框架，将 DFN 参数（位置、尺寸、导水系数 *K*）视为随机变量，通过 **马尔可夫链蒙特卡洛（MCMC）** 采样生成后验 DFN 集合 [Lukas 2024, pp. 6-7].
  - 使用 **可逆跳 MCMC（Reversible Jump MCMC）** 实现裂缝插入/删除（跨维度更新），并调整裂缝位置、长度与 *K* [Lukas 2024, pp. 6-7].
  - 利用 Gibbs 采样估计数据方差 σ² [Lukas 2024, pp. 6-7].
  - 不同初始 DFN 的平行反演最终收敛至相似的后验集合，初始裂缝在反演中均被更新 [Lukas 2024, pp. 7-9].

## Key Findings
- 混合 DFN 反演结果可以成功预测独立的热示踪试验温度分布，验证了反演模型的可靠性 [Lukas 2024, pp. 1-1].
- 反演得到的一个示例后验 DFN 包含 23 条裂缝（第一组 3 条，第二组 11 条，第三组 9 条），裂缝导水系数集中在 0.25–0.99 m s⁻¹（接近先验上限），比基质高约 5 个数量级 [Lukas 2024, pp. 7-9].
- 裂缝网络主要通过间接连接（多裂缝组合或通过基质间隙）实现不同井段间的水力连通，其中仅发现一处直接对面间隔的连接（裂缝 B），且该位置与走时反演结果中的高扩散区吻合 [Lukas 2024, pp. 7-9].
- 基质流在维持裂缝间隙（裂缝末端与间隔之间的小间隙）的水力连通中起关键作用，体现了混合方法的必要性 [Lukas 2024, pp. 7-9].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 仅靠连续介质模型或纯 DFN 模型不足以刻画出裂隙–多孔介质的流动 | [Lukas 2024, pp. 2-3] | 裂隙岩体与具显著渗透性的多孔基并存 | 需要混合模型考虑两种流态 |
| 走时反演揭示的高扩散区与混合 DFN 反演结果中唯一一条直接连接间隔的裂缝位置吻合 | [Lukas 2024, pp. 7-9] | 示例 DFN 集合 | 两种独立反演方法具有一致性 |
| 后验 DFN 中大部分井间连接为间接形式，通过裂缝组合或基质间隙连通 | [Lukas 2024, pp. 7-9] | 示例后验 DFN，23 条裂缝 | 强调基质流和网络效应的关键角色 |
| 裂缝导水系数集中于 0.25–0.99 m s⁻¹，高于基质约 5 个数量级 | [Lukas 2024, pp. 7-9] | 示例后验 DFN，裂缝 *K* 的先验上限为 1 m s⁻¹ | 表明主要导水通道仍为裂缝 |
| 不同初始 DFN 的平行反演均收敛至相似后验集合 | [Lukas 2024, pp. 7-9] | 反演算法收敛性检验 | 说明反演结果的稳定性，不依赖于初始猜测 |
| 混合 DFN 反演结果能成功预测独立的热示踪试验温度数据 | [Lukas 2024, pp. 1-1] | 独立验证实验 | 定量验证了反演所得参数场的预测能力 |

## Limitations
- 观测段 M5 数据因高噪声被弃用，减少了数据密度 [Lukas 2024, pp. 3-5].
- 二维模型无法考虑泵送井中记录的三维压力扩散效应 [Lukas 2024, pp. 3-5].
- 数据空间仅包含 12 个走时，分辨率较粗 (垂直 0.5 m，水平 1 m)，更精细的网格并不被数据所支持 [Lukas 2024, pp. 5-6].
- 基质导水系数和比储量基于早期研究设定为固定值，未在反演中与裂缝参数同时推断；具体的参数不确定性讨论程度未从索引片段中确认 [Lukas 2024, pp. 7-7].

## Assumptions / Conditions
- **流场维度**：二维（共面）流场，忽略三维效应（如泵送井中数据未被使用） [Lukas 2024, pp. 3-5].
- **裂缝属性**：裂缝的方位角在反演过程中固定，基于光学电视数据预先识别为三个主要方向 [Lukas 2024, pp. 7-7].
- **介质属性**：多孔基质为均质，具有恒定的导水系数 (10⁻⁶ m s⁻¹) 和比储量 (5·10⁻⁵ m⁻¹) [Lukas 2024, pp. 7-7].
- **走时反演**：比储量为均匀分布，使用常数 5·10⁻⁵ m⁻¹；矩形单元有助于识别层状沉积特征，无需施加各向异性约束 [Lukas 2024, pp. 5-6].
- **反演算法**：噪声等级（数据方差）通过 Gibbs 采样估计 [Lukas 2024, pp. 6-7].

## Key Variables / Parameters
- **裂缝参数**：位置、长度、导水系数 *K*_frac [Lukas 2024, pp. 6-7].
- **裂缝几何**：固定倾角 −0.94°、−26.31°、49.64° [Lukas 2024, pp. 7-7].
- **基质参数**：基质导水系数 *K*_matrix = 10⁻⁶ m s⁻¹，比储量 *S*_s = 5·10⁻⁵ m⁻¹ [Lukas 2024, pp. 7-7].
- **裂缝水力学**：后验裂缝 *K* 范围 0.25–0.99 m s⁻¹ [Lukas 2024, pp. 7-9].
- **扩散系数**：*D* (走时反演中得到) [Lukas 2024, pp. 5-6].
- **目标函数**：似然函数与数据方差 σ² [Lukas 2024, pp. 6-7].

## Reusable Claims
### Claim 1
当反演水力层析成像数据时，若目标场地同时存在高渗透性离散裂缝与具显著渗透率的基质，采用混合 DFN-连续介质模型比单独使用任一模型更能准确刻画流动行为。该主张基于德国哥廷根裂隙–多孔场地的成功应用，并以独立热示踪数据进行了验证 [Lukas 2024, pp. 1-1, pp. 2-3].

### Claim 2
在数据稀疏（例如仅有 12 个走时）时，将水力走时反演的网格分辨率限制在较低水平（如 0.5 m × 1 m），并使用矩形网格单元，可以避免因数据不足而虚构精度，并适应沉积地层的水平层状特性 [Lukas 2024, pp. 5-6].

### Claim 3
基于贝叶斯框架和可逆跳 MCMC 的 DFN 反演算法，在基质渗透率非零的混合模型下，其反演结果对初始猜测具有鲁棒性：平行运行的不同初始 DFN 可收敛至相似的后验集合，表明后验分布主要由数据决定 [Lukas 2024, pp. 7-9].

## Candidate Concepts
- [[Hydraulic Tomography (水力层析成像)]]
- [[Discrete Fracture Network (离散裂缝网络)]]
- [[Hybrid Fractured-Porous Model (混合裂隙-多孔模型)]]
- [[Bayesian Inversion (贝叶斯反演)]]
- [[Markov chain Monte Carlo (MCMC) (马尔可夫链蒙特卡洛)]]
- [[Hydraulic Travel Time Inversion (水力走时反演)]]
- [[Fracture Network Connectivity (裂缝网络连通性)]]
- [[Heat Tracer Test Validation (热示踪试验验证)]]

## Candidate Methods
- [[Hydraulic Travel Time Inversion (水力走时反演)]]：基于 Dijkstra 算法反演水力扩散系数 [Lukas 2024, pp. 5-6].
- [[Reversible Jump MCMC (可逆跳 MCMC)]]：用于跨维度更新裂缝数量 [Lukas 2024, pp. 6-7].
- [[Gibbs Sampling (Gibbs 采样)]]：用于估计数据方差 [Lukas 2024, pp. 6-7].
- [[Ray Tracing with Dijkstra's Algorithm (基于 Dijkstra 算法的射线追踪)]]：计算水力走时 [Lukas 2024, pp. 5-6].
- [[Optical Televiewer Data Analysis (光学钻孔电视数据分析)]]：识别并固定裂缝方位 [Lukas 2024, pp. 7-7].

## Connections To Other Work
- **水力走时反演**：该方法承袭自 [[Brauchler et al., 2011]] 和 [[Song et al., 2023]] 的水力衰减反演，并类似于地震走时层析成像。本研究使用常数 *S*_s 进行 *D* 到 *K* 的转换 [Lukas 2024, pp. 5-6].
- **DFN 反演方法**：反演框架沿用 [[Ringel et al., 2022]] 的 DFN 随机反演方法，并将其扩展为考虑非零基质渗透率的混合模型 [Lukas 2024, pp. 2-3, pp. 6-7].
- **理论基础**：本研究与 [[Yeh & Liu, 2000]] 的水力层析成像概念、[[Fischer et al., 2020]] 对混合模型必要性的论述直接相关 [Lukas 2024, pp. 1-1, pp. 2-3].
- **概念上可能的连接**：可连接到其他裂隙–多孔介质表征、多尺度渗流模拟、以及地球物理与水文联合反演领域.

## Open Questions
- 该混合 DFN 反演方法在不同地质条件或更大尺度场地的可迁移性未从索引片段中确认。
- 基质参数 (*K*_matrix, *S*_s) 的不确定性对 DFN 反演结果的影响程度，以及将这些参数纳入联合反演的可行性未从索引片段中确认。
- 该方法在三维条件下的扩展及计算效率问题未从索引片段中确认。

## Source Coverage
本页基于作者提供的 18 个索引片段编写，片段覆盖了论文的标题、摘要、引言、站点与数据、方法（走时反演与混合 DFN 反演）和部分结果（DFN 示例、模型对比）。关于验证（第4章）、详细讨论（第5章）和结论（第6章）的碎片化信息有限，因此可能缺失以下内容：走时反演与混合方法更详尽的定量比较、热示踪验证的具体步骤和统计指标、以及论文的全部结论性陈述。
