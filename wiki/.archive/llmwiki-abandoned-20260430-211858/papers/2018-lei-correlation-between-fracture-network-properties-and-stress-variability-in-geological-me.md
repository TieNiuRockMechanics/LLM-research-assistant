---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-lei-correlation-between-fracture-network-properties-and-stress-variability-in-geological-me"
title: "Correlation Between Fracture Network Properties and Stress Variability in Geological Media."
status: "draft"
source_pdf: "data/papers/2018 - Correlation Between Fracture Network Properties and Stress Variability in Geological Media.pdf"
collections:
citation: "Lei, Qinghua, and Ke Gao. “Correlation Between Fracture Network Properties and Stress Variability in Geological Media.” *Geophysical Research Letters*, 2018, doi:10.1002/2018GL077548."
indexed_texts: "10"
indexed_chars: "46811"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:38:54"
---

# Correlation Between Fracture Network Properties and Stress Variability in Geological Media.

## One-line Summary
在二维含裂隙地质介质中，局部应力扰动（由局部应力张量至平均应力张量的欧几里得距离度量）与局部裂隙强度（单位面积上的裂隙总长度）呈正线性相关，且在连通性好且处于临界摩擦滑动状态的裂隙系统中出现强烈的整体应力离散 [Lei 2018, pp. 1-1; pp. 11-11].

## Research Question
断裂网络属性（如强度、连通性）与受到构造应力作用的地质介质中应力场变异性之间是否存在相关性？若存在，这种相关性如何量化？[Lei 2018, pp. 1-1; pp. 1-2].

## Study Area / Data
研究数据包括两类二维裂隙网络模式：
- **合成裂隙网络**：遵循幂律长度分布，幂律长度指数$ a $遍历1.5、2.0、2.5、3.0和3.5，平均裂隙强度$ \gamma $设定为2.5 m⁻¹和5.0 m⁻˝两个场景，每种参数组合生成10个实现 [Lei 2018, pp. 2-4].
- **天然裂隙网络**：基于Hornelen盆地真实露头图的描摹，通过旋转采样窗口提取不同角度（θ）下的网络几何和局部裂隙强度 [Lei 2018, pp. 2-4; Lei 2018, pp. 11-12].

所有网络均被限定在边长为10 m的方形域内 [Lei 2018, pp. 2-4].

## Methods

### 裂隙网络生成与表征
- **合成网络**采用幂律模型$ n(l, L) = \alpha L^D l^{-a} $生成，其中$ D $为分形维数，$ a $为幂律长度指数，$ l \in [l_{min}, l_{max}] $ [Lei 2018, pp. 1-2].
- **裂隙强度**定义为局部采样窗口内单位面积上的裂隙总长度（$ \gamma $），同时计算网络连通性的逾渗参数$ p $和裂隙强度的方差$ \sigma^2 $ [Lei 2018, pp. 2-4].

### 力学模拟
- 采用**有限-离散元模型**计算二维应力张量场。在10 m × 10 m的域内，不同构造应力条件（远场主应力比$ S^\infty_{xx}/S^\infty_{yy} $）和裂隙面摩擦系数（$ \mu $）下求解应力场，所有单元节点处的二阶柯西应力张量分量均被确定 [Lei 2018, pp. 4-5; Lei 2018, pp. 1-1].

### 应力变异性张量分析
- **平均应力张量**：采用Fréchet均值函数推导，证明等于远场构造应力张量 [Lei 2018, pp. 4-5].
- **局部应力扰动**：使用局部应力张量$ S_i $与平均应力张量$ \bar{S} $间的**欧几里得距离**（Frobenius范数）度量：$ d(S_i, \bar{S}) = \| S_i - \bar{S} \|_F $ [Lei 2018, pp. 4-5].
- **整体应力变异性**：使用应力张量场的**有效方差**$ V_e(\mathbf{S}) $作为标量度量 [Lei 2018, pp. 10-11].

## Key Findings
- **局部应力扰动与裂隙强度正线性相关**：度量指标$ d(S_i, \bar{S}) $与局部裂隙强度$ \gamma $之间存在正的线性关系，该关系在不同裂隙网络、不同摩擦系数及不同构造应力条件下均能保持 [Lei 2018, pp. 10-11; Lei 2018, pp. 1-1].
- **应力扰动散布随裂隙强度线性增长**：每个$ \gamma $分格内$ d(S_i, \bar{S}) $的散布范围$ h $亦随$ \gamma $线性变化，进一步确认了系统性关联的存在 [Lei 2018, pp. 10-11].
- **连通性控制应变与应力分布**：当断裂网络由不连通状态（$ p < p_c $）过渡到连通状态（$ p > p_c $）时，摩擦滑动引起的总应变$ \varepsilon $急剧增大，应力有效方差$ V_e $亦显著上升，该现象在高差应力（$ S^\infty_{xx}/S^\infty_{yy} = 3.0 $）和低摩擦系数（$ \mu = 0.6 $）下尤为突出 [Lei 2018, pp. 10-11].
- **连通性与应力离散**：在不连通区域（$ p < p_c $）内，$ V_e $几乎不依赖于摩擦系数；而在连通区域（$ p > p_c $），$ V_e $随$ \mu $增大而显著降低 [Lei 2018, pp. 10-11].
- **应力扰动空间集中**：局部应力扰动集中出现在控制摩擦滑动的大裂隙（择向优取）尖端和交会处附近，这些区域伴随强烈的力学相互作用和脆性破坏 [Lei 2018, pp. 5-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 局部应力扰动$ d(S_i, \bar{S}) $与局部裂隙强度$ \gamma $存在正的线性相关 | [Lei 2018, pp. 10-11; pp. 1-1] | 二维合成及天然裂隙网络，多种$ a $、$ \gamma $、$ \mu $值及不同远场应力比$ S^\infty_{xx}/S^\infty_{yy} $下均成立 | 应力扰动散布范围$ h $亦与$ \gamma $线性相关 |
| 连通网络（$ p > p_c $）中总应变和应力有效方差随逾渗参数接近并超过临界值而急剧上升 | [Lei 2018, pp. 10-11] | 特别在$ S^\infty_{xx}/S^\infty_{yy} = 3.0 $且$ \mu = 0.6 $时最为显著 | 高差应力和临界应力状态下效应放大 |
| 连通区域内有效方差$ V_e $随摩擦系数$ \mu $增大而减小 | [Lei 2018, pp. 10-11] | 仅在连通状态（$ p > p_c $）下明显 | 不连通时$ V_e $几乎不依赖于$ \mu $ |
| 局部应力扰动集中分布于择优取向的大尺度滑动裂隙的尖端和交会处 | [Lei 2018, pp. 5-10] | 二维裂隙网络，摩擦系数$ \mu = 0.6 $及多种构造应力条件下 | 高剪切位移区域与高应力扰动区域空间一致 |

## Limitations
- **二维限制**：分析仅针对二维情景，仅适用于纵向特征尺度远大于横向尺度的地质体，未涉及三维裂隙网络 [Lei 2018, pp. 1-2].
- **无尺度效应分析**：研究固定在10 m × 10 m的单一尺度，明确未分析尺度效应 [Lei 2018, pp. 1-2].
- **模型假设限制**：假设裂隙模式与现今构造应力场相关性很小，且应力扰动完全由现今构造应力发育，不考虑复杂残余应力效应；并忽略了应力阴影效应等对裂隙组织的控制 [Lei 2018, pp. 1-2; pp. 2-4].
- **应力状态推论的局限性**：未从索引片段中确认关于模型的更多力学细节限制（如弹性参数选择、边界条件的具体实现方式，或有限-离散元接触算法的细节）。

## Assumptions / Conditions
- 二维平面应变或平面应力假设，地质体纵向远大于横向 [Lei 2018, pp. 1-2].
- 裂隙几何模式由古应力演化形成，与施加的现今构造应力场统计独立 [Lei 2018, pp. 1-2].
- 应力扰动完全源于当代构造应力，忽略残余应力 [Lei 2018, pp. 1-2].
- 岩石基质视为线弹性，裂隙之间以及裂隙内部接触遵循库仑摩擦定律（以摩擦系数$ \mu $表征） [Lei 2018, pp. 5-10].
- 固定的研究尺度，不讨论尺度依赖性 [Lei 2018, pp. 1-2].
- 裂隙遵循幂律长度分布（合成网络部分） [Lei 2018, pp. 1-2].
- 边界载荷由远场均匀双轴应力状态$ S^\infty_{xx}/S^\infty_{yy} $定义 [Lei 2018, pp. 10-11].

## Key Variables / Parameters
- **局部裂隙强度** $ \gamma $：单位面积上的裂隙总长度（指标） [Lei 2018, pp. 1-1].
- **局部应力扰动** $ d(S_i, \bar{S}) $：局部应力张量至平均应力张量的欧几里得距离（Frobenius范数） [Lei 2018, pp. 4-5].
- **平均应力张量** $ \bar{S} $：Fréchet均值，等价于远场应力张量 [Lei 2018, pp. 4-5].
- **应力场有效方差** $ V_e(\mathbf{S}) $：整体应力变异性的标量度量 [Lei 2018, pp. 10-11].
- **远场主应力比** $ S^\infty_{xx}/S^\infty_{yy} $：构造应力条件控制参数 [Lei 2018, pp. 10-11].
- **裂隙摩擦系数** $ \mu $：控制裂隙面摩擦滑动行为 [Lei 2018, pp. 5-10; pp. 10-11].
- **幂律长度指数** $ a $：控制合成网络裂隙尺度分布形态 [Lei 2018, pp. 1-2; pp. 2-4].
- **平均裂隙强度** $ \bar{\gamma} $：全局裂隙强度的均值 [Lei 2018, pp. 2-4].
- **逾渗参数** $ p $：表征裂隙网络的几何连通性 [Lei 2018, pp. 2-4；pp. 10-11].
- **总摩擦滑动应变** $ \varepsilon $：所有裂隙几何矩（平均剪切位移与长度的乘积）之和除以域面积 [Lei 2018, pp. 10-11].

## Reusable Claims
- **Claim 1**：在二维含裂隙介质中，采用Fréchet均值定义的应力张量平均值被证明等于远场构造应力张量，因而局部应力扰动可以通过局部应力与远场应力间欧几里得距离（Frobenius范数）量化。该公式与距离度量是对构造成因应力变异性进行张量一致性解析的基础。[Lei 2018, pp. 4-5]  *(适用条件：单相、弹性基质，远场应力为均匀均值边界条件；证据：与Gao 2017的解析结果一致且在本模拟数据中得证；限制：仅对二阶柯西应力成立，未验证三维和非均质加载。)*
- **Claim 2**：局部应力扰动的强度与局部裂隙强度呈正的线性关联，且该关系在幂律指数、均强、摩擦系数及构造应力比等参数的大范围变化下保持稳健。散布指标亦与裂隙强度线性相关。这为利用裂隙强度分布（来自露头或测井）直接估测局部应力扰动水平提供了定量依据。[Lei 2018, pp. 10-11] *(适用条件：二维裂隙网络，裂隙模式与远场应力不相关，线性弹性基质，库仑摩擦接触；证据：合成及天然裂隙网络的多个实现下的散点图及误差棒分析；限制：结论来自2-D模拟，三维及非弹性的普适性待验证。)*
- **Claim 3**：断裂网络的逾渗连通性是控制整体应力离散度和总应变的关键开关。当系统由不连通过渡到连通后，应变$ \varepsilon $和有效方差$ V_e $出现阶跃式增大；在连通区域，$ V_e $随裂隙摩擦系数增大而显著减小。这意味着构造应力场评价与地震或工程活动评估中必须考虑断裂逾渗状态。[Lei 2018, pp. 10-11] *(适用条件：裂隙系统接近或超过逾渗阈值时，特别在构造差应力高的情况下；证据：$ \varepsilon $-$ p $和$ V_e $-$ p $曲线在$ p_c $附近的突变；限制：边界效应（大小10 m域）、限定2-D、受限于所测试的$ \mu $和应力比取值。)*

## Candidate Concepts
- [[Fracture network connectivity]]
- [[Local fracture intensity]]
- [[Stress perturbation]]
- [[Effective variance of stress tensor]]
- [[Percolation parameter]]
- [[Fréchet mean stress tensor]]
- [[Critically stressed fracture]]
- [[Power law length scaling]]
- [[Finite-discrete element model (FDEM)]]
- [[Tectonic stress variability]]
- [[Coulomb frictional sliding]]

## Candidate Methods
- [[Power-law fracture network generation]]
- [[Discrete element method for fractured rock]]
- [[Tensor-based stress data analysis]]
- [[Euclidean distance for stress tensors]]
- [[Fréchet mean for symmetric positive-definite matrices]]
- [[Percolation analysis]]
- [[Local sampling window method for intensity]]
- [[Strain geometric moment method]]

## Connections To Other Work
- 本文采用张量向量化距离（Frobenius范数）和Fréchet均值的基础方法学直接继承自 **Gao (2017)**、**Gao & Harrison (2016, 2018)** 的应力变异性表征工作 [Lei 2018, pp. 4-5; pp. 11-12].
- 使用的平均应力张量等价于远场应力的解析证明，可在 **Gao et al. (2017)** 中找到 [Lei 2018, pp. 4-5].
- 合成裂隙网络的幂律长度模型是基于 **Bonnet et al. (2001)** 和 **Bour & Davy (1999)** 的自然裂隙观测，以及 **Lei & Wang (2016)** 的前期工作 [Lei 2018, pp. 1-2].
- 尽管应力阴影效应在许多自然裂隙组织中被认为重要 (e.g., Ackermann & Schlische, 1997; Davy et al., 2010)，本文明确指出未考虑此效应，属于对以上工作的简化假设 [Lei 2018, pp. 2-4].
- 天然裂隙数据获取自 **Odling (1997)** 对Hornelen盆地的测绘 [Lei 2018, pp. 2-4].
- 应变计算采用的几何矩方法引用了 **Marrett & Allmendinger (1991)** [Lei 2018, pp. 10-11].
- 可从主题上连接到：[[fracture reservoir]]中的地应力扰动分析，[[induced seismicity]]预测中的临界应力裂隙网络，[[DFN (discrete fracture network)]]方法在岩石力学中的应用，以及[[damage zone]]和[[fault interaction]]等相关研究。

## Open Questions
- 未从索引片段中确认本研究在三维裂隙网络中的适用性以及尺度效应的详细表征，该问题有待解决 [Lei 2018, pp. 1-2].
- 未从索引片段中确认残余应力或古应力对现今应力变异性的潜在贡献及与构造应力的耦合影响。
- 未从索引片段中确认该线性相关性是否可通过解析微力学模型推导，或是否有其他形态（如非线性）存在。
- 未从索引片段中确认在更广泛的构造体制（例如，剪扭、拉张）和层状各向异性介质中的普适性。
- 未从索引片段中确认如何基于该成果开发实际可操作的地应力估算和预测工具。

## Source Coverage
本 Wiki 页面依据 **10个**索引片段编制，覆盖了论文的摘要、引言、方法学、关键图表说明及主要结论部分。来源提供了对研究主旨、数据生成方案（合成和天然网络参数）、核心数学公式（欧几里得距离和Fréchet均值定义）、主要结果（局部线性相关和整体逾渗效应）以及固有假设的连贯描述。但是，可能缺失以下信息：文献综述全景、更详尽的模型参数设置（如弹性常数、网格精度、边界载荷施加细节）、各参数组合下更完备的定量统计表格、以及全部支持信息中的补充分析图件。部分参考文献的讨论受限于仅能在片段尾部的参考文献列表中提取。
