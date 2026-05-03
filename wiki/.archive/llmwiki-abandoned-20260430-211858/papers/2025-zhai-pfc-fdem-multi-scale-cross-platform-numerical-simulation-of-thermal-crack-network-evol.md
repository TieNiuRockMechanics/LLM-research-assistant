---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
title: "PFC-FDEM Multi-Scale Cross-Platform Numerical Simulation of Thermal Crack Network Evolution and SHTB Dynamic Mechanical Response of Rocks."
status: "draft"
source_pdf: "data/papers/2025 - PFC-FDEM multi-scale cross-platform numerical simulation of thermal crack network evolution and SHTB dynamic mechanical response of rocks.pdf"
collections:
  - "PFC热力耦合"
citation: "Zhai, Yue, et al. \"PFC-FDEM Multi-Scale Cross-Platform Numerical Simulation of Thermal Crack Network Evolution and SHTB Dynamic Mechanical Response of Rocks.\" *International Journal of Mining Science and Technology*, vol. 35, 2025, pp. 1555-89, doi:10.1016/j.ijmst.2025.08.013."
indexed_texts: "26"
indexed_chars: "127345"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:29:34"
---

# PFC-FDEM Multi-Scale Cross-Platform Numerical Simulation of Thermal Crack Network Evolution and SHTB Dynamic Mechanical Response of Rocks.

## One-line Summary

该研究提出了一种创新的多尺度跨平台 PFC-FDEM 耦合方法，用于桥接岩石在热‑动力耦合作用下的微观损伤机制与宏观动态断裂响应，揭示了热裂纹网络的三阶段演化规律及其对动态力学行为的定量影响。[Zhai 2025, pp. 1-1]

## Research Question

当前研究范式的核心认识论空白包括：  
- 多尺度耦合公式无法在尺度转换过程中保持裂缝网络几何不变量；  
- 缺乏将微观裂纹描述符与宏观本构参数关联起来的微观–宏观关联框架；  
- 对热损伤与动态加载相互作用机理的理解不充分；  
- 缺乏能够同时捕捉微观热致断裂机制与宏观动态响应的集成计算方法。[Zhai 2025, pp. 2-3]  

为此，本文需要回答：如何构建一个能够将粒子流代码（PFC）与有限‑离散元耦合方法（FDEM）协同起来的多尺度跨平台数值框架，在保持裂纹网络几何不变性前提下，从第一性原理解释热损伤对动态力学行为的影响机理。[Zhai 2025, pp. 2-3, 1-1]

## Study Area / Data

研究对象的热物性与力学参数依据实验标定，但研究区地理位置与岩石详细岩性未在索引片段中明确给出。标定所用材料为热处理后的红砂岩，相关 SHTB 实验数据被用于验证耦合‑解耦假设和动态强度增强规律。[Zhai 2025, pp. 7-8] PFC 模型的细观力学参数见表 1，包括有效弹性模量、平行粘结模量、刚度比、拉伸强度、粘聚力以及摩擦角等。[Zhai 2025, pp. 8-8] 此外，未从片段中确认是否包含原位或野外数据。

## Methods

### 整体耦合框架  
提出一种多尺度跨平台耦合方法论，包括：  
(1) 双向信息传输协议，实现 PFC 颗粒尺度热损伤表征与 FDEM 连续体尺度断裂扩展的无缝衔接；  
(2) 多物理场映射算法，在尺度转换时保持裂纹网络的几何不变量；  
(3) 跨平台内聚区实现，用于精确模拟 SHTB 动态加载。[Zhai 2025, pp. 1-1]

### PFC 热‑力模型  
- 采用颗粒间离散热传导模型，温度场通过隐式时间积分求解，并需满足三个收敛条件（导热系数等效、空间离散收敛、时间离散稳定性）以向连续体热传导模型过渡。[Zhai 2025, pp. 3-4]  
- 热膨胀按非均质组分考虑，径向增量 \(\Delta R_i\) 与参考温度 \(T_0\) 及温度增量 \(\Delta T_i\) 有关，线膨胀系数可表达为温度的二次多项式。[Zhai 2025, pp. 8-8]  
- 采用顺序热‑力耦合策略：先求解温度场，再计算热应力与裂纹演化，平衡方程采用隐式求解。[Zhai 2025, pp. 8-8]  
- 加热控制：边界颗粒以 5 °C/min 速率施加预设温度。[Zhai 2025, pp. 8-8]

### 裂纹几何特征提取与量化  
- 微裂纹几何参数通过变换矩阵定义，包括裂纹中点、长度和取向。[Zhai 2025, pp. 4-7]  
- 量化特征包括裂纹密度、长度分布（幂律或对数正态分布）、方向分布（Fisher 或 von Mises 分布）以及空间异质性（Ripley’s K 函数）。  
- 提出裂纹张量表示法以刻画网络各向异性。[Zhai 2025, pp. 8-11]

### FDEM 断裂力学与动态处理  
- 采用零厚度内聚元，基于双线性牵引‑分离本构，损伤变量 \(d\) 由等效分离位移 \(d_{eq}\) 控制。[Zhai 2025, pp. 4-7]  
- 动态分析采用解耦方法：率无关内聚律通过全局动态增加因子（DIF）修正，即 \(\pmb{\sigma}_{total} = \pmb{\sigma}_{static}(T,d) \cdot DIF(\dot{\varepsilon})\)；该解耦基于热软化与率硬化间的弱耦合假设，实验证据表明该耦合项对动态强度增强的贡献低于 8%。[Zhai 2025, pp. 7-8]  
- 裂纹动态扩展的分析精度可维持至裂纹速度为 0.4 倍 Rayleigh 波速，此时控制方程由能量平衡准则主导。[Zhai 2025, pp. 7-8]

### PFC‑FDEM 映射与能量一致性  
- 开发了从 PFC 提取裂纹几何信息的系统方法，通过统计分析实现裂纹长度、取向与空间分布向 FDEM 模型的传递，并采用基于热力学的一致性条件保证映射过程的能量守恒。[Zhai 2025, pp. 8-11]

## Key Findings

1. **三阶段裂纹演化与指数密度模型**：热裂纹网络演化呈现明显的三个阶段特征，且温度相关的裂纹密度服从指数模型。[Zhai 2025, pp. 1-1]  
2. **高温对动态强度的退化**：800 °C 高温暴露后岩石的动态强度比（?）降低至约 60%，表明热损伤显著削弱动态承载能力。[Zhai 2025, pp. 1-1]  
3. **弱耦合解耦的有效性**：在研究的应变率区间内，热软化与率硬化耦合项对总动态强度增强的贡献 < 8%，支持了解耦 DIF 方法的合理性。[Zhai 2025, pp. 7-8]  
4. **裂纹扩展速度限制**：在动态裂纹速度不超过 0.4 倍 Rayleigh 波速时，PFC‑FDEM 耦合能量平衡分析仍能保持准确。[Zhai 2025, pp. 7-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 800 °C 时动态强度比降至约 60% | [Zhai 2025, pp. 1-1] | 红砂岩经高温处理后进行 SHTB 动态加载，具体应变率未在片段中显式给出 | 强度比的定义未在片段中明确，推测为高温动态强度与常温动态强度之比 |
| 热‑率耦合项对动态强度增强的贡献 < 8 % | [Zhai 2025, pp. 7-8] | SHTB 试验处理热损伤红砂岩，特定应变率区间内 | 误差分析用于验证解耦方法的有效性 |
| 裂纹动态扩展分析适用于 \(v_{crack} \le 0.4 c_R\) | [Zhai 2025, pp. 7-8] | 准脆性材料，FDEM 结合动量平衡修正 | Rayleig 波速为上限参考 |
| 裂纹长度分布符合幂律或对数正态分布 | [Zhai 2025, pp. 8-11] | PFC 生成的热裂纹网络，统计拟合 | 用于映射到 FDEM 中作为离散裂缝网络 |
| PFC 细观校准参数（表 1）：有效模量 6 GPa，平行粘结模量 6 GPa，拉伸强度 10 MPa，粘聚力 28 MPa，摩擦系数 1 等 | [Zhai 2025, pp. 8-8] | 基于实验校准的红砂岩 PFC 模型 | 用于所有后续热‑力耦合模拟 |

## Limitations

- 动态增量采用解耦近似，仅适用于热软化与率硬化弱耦合的加载条件；当耦合效应显著时，DIF 直接修正方式可能失效。[Zhai 2025, pp. 7-8]  
- 裂纹动态传播分析精度受限于 \(v_{crack}/c_R \le 0.4\)，更高速度下能量平衡关系需要更复杂的动态断裂准则。[Zhai 2025, pp. 7-8]  
- 顺序热‑力耦合假设温度场与应力场之间无双向实时交互，忽略变形生热等高度耦合过程。[Zhai 2025, pp. 8-8]  
- PFC 与 FDEM 的双向信息传输与映射算法，其具体实现细节与普适性在片段中未完全呈现，可能存在计算成本与可扩展性问题。[未从索引片段中确认]

## Assumptions / Conditions

- **离散‑连续热等效条件**：PFC 离散热传导模型可与连续体热传导模型等效，需满足导热系数等效、空间离散收敛及时间离散稳定三个条件。[Zhai 2025, pp. 3-4]  
- **顺序热‑力耦合**：热分析与力学分析解耦，温度场先单独求解，再由热应力驱动裂纹，忽略力学变形对温度场的反馈。[Zhai 2025, pp. 8-8]  
- **应变率效应解耦**：认为总牵引可分解为温度依赖的准静态部分与动态增强因子的乘积，即热‑率耦合弱。[Zhai 2025, pp. 7-8]  
- **裂纹动态传播假设**：在 \(v_{crack} \le 0.4c_R\) 内，动态能量平衡成立，且无需引入额外的动态断裂韧度演化模型。[Zhai 2025, pp. 7-8]  
- **材料本构**：岩石基体连续体为线弹性，内聚元遵循双线性软化规律；PFC 颗粒间采用平行粘结模型。[Zhai 2025, pp. 4-7, 8-8]  
- **加热条件**：以 5 °C/min 的加热速率均匀施加温度边界，忽略实际升温过程中可能的热梯度与宏观破裂的非均匀性。[Zhai 2025, pp. 8-8]

## Key Variables / Parameters

- **PFC 细观参数**：有效弹性模量、平行粘结模量、刚度比、平行粘结拉伸强度、粘聚力、摩擦角、摩擦系数（见表 1）[Zhai 2025, pp. 8-8]  
- **裂纹几何参数**：裂纹长度分布（对数正态或幂律参数 \(l, b, a\)）、方向分布（Fisher 集中度 \(\kappa\)）、空间异质性（Ripley’s K 函数）[Zhai 2025, pp. 8-11]  
- **裂纹密度**：与损伤变量关系 \(D = 1 - \exp(-\beta \rho_{crack})\) [Zhai 2025, pp. 7-8]  
- **热物性参数**：热膨胀系数 \(\alpha_i(T)\)（包括参考系数 \(\alpha_{i,0}\) 及温度灵敏度 \(b_1, b_2\)）、热传导系数、热容等[Zhai 2025, pp. 8-8]  
- **动态强度指标**：动态增加因子 DIF = \(\sigma_d / \sigma_s\) 及其率相关参数 \(C, \dot{\varepsilon}_0, n\) [Zhai 2025, pp. 7-8]  
- **Rayleigh 波速 \(c_R\)**：用于限制裂纹速度的分析上限 [Zhai 2025, pp. 7-8]  
- **温度场**：从 PFC 计算得到的离散温度分布，经等效性验证后传入 FDEM。[Zhai 2025, pp. 3-4]

## Reusable Claims

1. 在弱耦合条件下，热‑动力响应的解耦方法（\(\pmb{\sigma}_{total} = \pmb{\sigma}_{static}(T,d) \cdot DIF(\dot{\varepsilon})\)）可有效近似总应力，条件是耦合项对总动态强度增强的贡献 < 8 %，且应变率范围与材料（热红砂岩）与本文的 SHTB 工况一致。[Zhai 2025, pp. 7-8]  
2. 若离散热传导模型满足三个等效条件（导热系数等效、空间离散收敛、时间离散稳定），则其在一定误差内（如一维稳态验证相对误差 < 5 %）可以将温度场准确传递给连续体 FDEM 模型。[Zhai 2025, pp. 3-4]  
3. 热致裂纹网络的长度分布可通过对数正态或幂律形式描述，取向可用 von Mises‑Fisher 分布拟合，空间不均匀性可采用 Ripley’s K 函数量化，这些统计描述可作为 PFC‑FDEM 信息传递的关键接口。[Zhai 2025, pp. 8-11]  
4. 对于花岗岩/红砂岩类岩石，高温（800 °C）可导致动态强度比降低约 40 %；该结论源自 SHTB 试验耦合 PFC‑FDEM 数值模拟，但适用范围受限于特定热处理历史与加载率。[Zhai 2025, pp. 1-1]

## Candidate Concepts

- [[Multi-scale coupling in geomechanics]]
- [[Thermally-induced crack network]]  
- [[Dynamic mechanical response of rocks]]
- [[Particle Flow Code (PFC) thermomechanics]]
- [[Combined finite-discrete element method (FDEM)]]
- [[Split Hopkinson Tensile Bar (SHTB)]]
- [[Discrete fracture network (DFN) statistics]]
- [[Dynamic increase factor (DIF)]]
- [[Cohesive zone model for dynamic fracture]]

## Candidate Methods

- [[PFC-FDEM cross-platform coupling]]
- [[Sequential thermal-mechanical coupling]]
- [[Discrete-to-continuum heat conduction equivalence]]
- [[Crack geometry tensor representation]]
- [[Ripley's K-function for fracture spatial heterogeneity]]
- [[Dynamic energy balance criterion for crack velocity]]
- [[Decoupled strain-rate enhancement in FDEM]]
- [[Thermodynamics-based crack mapping and energy consistency]]

## Connections To Other Work

- 该工作继承并发展了 Munjiza 等 [18] 的 FDEM 框架，通过引入热‑力耦合与跨平台映射，使其能处理热损伤岩石的动态响应。[Zhai 2025, pp. 1-2]  
- 在多尺度策略上，与 ABAQUS‑UDEC [21] 和 PFC‑FLAC [22] 的集成思路一脉相承，但本工作专注于 PFC‑FDEM 双向耦合与裂纹几何不变量保持。[Zhai 2025, pp. 1-2]  
- 在 SHTB 动态测试方面，借鉴 Hao 等 [35] 的界面约束改进、Khan & Iqbal [36] 的损伤‑率敏感性关系以及 Sun 等 [37] 的热损伤岩石破坏模式差异结论。[Zhai 2025, pp. 2-3]  
- 可与基于均匀化的多尺度方法（如 FE² [15]）互补，但本方法更适用于非连续、随机裂纹主导的损伤演化问题。[Zhai 2025, pp. 1-2]  
- 可从主题上连接到 [[Scale transition in heterogeneous media]]、[[Thermomechanical fracture in quasi-brittle materials]] 等宽泛方向。

## Open Questions

- 当动态裂纹速度接近或超过 0.4 c_R 时，PFC‑FDEM 耦合框架如何修正能量平衡以保持准确性？  
- 在更高加热速率或非均匀温度场条件下，顺序耦合是否仍足够精确，还是需要采用全热‑力双向耦合？  
- 所提 DFN 统计描述与动态各向异性程度（如 SHTB 冲击方向）之间的定量关系尚未揭示。[未从索引片段中确认]  
- 该方法从红砂岩标定，推广至其他岩性（如花岗岩、碳酸盐岩）时的普适性需进一步验证。[未从索引片段中确认]  
- 在真实工程尺度的深部岩体问题中，计算效率与界面映射误差的可控范围仍不明确。

## Source Coverage

本条目基于全部 26 条索引片段撰写，片段覆盖了论文摘要、引言、方法论（PFC 热‑力模型、FDEM 断裂力学、跨平台映射）、部分关键结果与讨论等主要内容。然而，以下信息在片段中缺失或仅部分覆盖：  
- 完整的实验‑数值对比验证数据集；  
- 详细的裂纹网络空间演化图像与阶段划分的定量依据；  
- 更多温度工况下的动态应力‑应变曲线；  
- 模型的计算效率、网格依赖性分析；  
- 讨论与结论部分的完整内容。  

因此，本页面在结果细节和实际应用验证方面可能存在覆盖不足，相关条目已标注“未从索引片段中确认”。
