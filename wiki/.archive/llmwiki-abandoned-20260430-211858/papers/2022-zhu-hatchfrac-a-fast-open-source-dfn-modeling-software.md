---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-zhu-hatchfrac-a-fast-open-source-dfn-modeling-software"
title: "HatchFrac: A Fast Open-Source DFN Modeling Software."
status: "draft"
source_pdf: "data/papers/2022 - HatchFrac A fast open-source DFN modeling software.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhu, Weiwei, et al. \"HatchFrac: A Fast Open-Source DFN Modeling Software.\" *Computers and Geotechnics*, vol. 150, 19 July 2022, p. 104917. Accessed 2026."
indexed_texts: "14"
indexed_chars: "67935"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:49:09"
---

# HatchFrac: A Fast Open-Source DFN Modeling Software.

## One-line Summary
HatchFrac 是一个开源 C++ 软件包，支持二维和三维离散裂缝网络（DFN）的随机建模，集成了机器学习生成任意分布变量、扩展 Newman–Ziff 集群算法以及裂缝生长模拟以生成 T 型交切，并应用于渗流、强度与流动连通性分析 [Zhu 2022, pp. 1-1]。

## Research Question
论文未明确提出单一研究问题，其核心目标是开发一个兼具高计算效率与全面模拟功能的开源 DFN 平台，以解决现有高层语言工具（如 Matlab）在处理百万级三维裂缝网络时的性能瓶颈，并提升对天然裂缝系统中分形聚集、T 型交切等复杂现象的建模能力 [Zhu 2022, pp. 1-1, 1-2]。

## Study Area / Data
HatchFrac 是通用模拟器，文中应用示例基于合成裂缝网络（类型 1、2、3），并引用 18 个露头裂缝图作为对比数据。露头裂缝的长度服从幂律分布，指数范围为 2.0–3.0，且呈分形聚集特征 [Zhu 2022, pp. 7-8]。未从索引片段中确认其他现场数据集。

## Methods
- **随机变量生成**：采用逆累积分布函数和接受–拒绝法处理常用随机分布；利用多层感知机（MLP）结合逆 CDF 从任意有限频率直方图生成随机变量，避免预设连续分布 [Zhu 2022, pp. 1-1, 2-3]。
- **裂缝形状与空间分布**：2D 使用线段，3D 使用凸多边形（可表示圆盘、椭圆等）；裂缝中心位置支持均匀密度和分形密度分布，分形分布通过乘性级联过程实现 [Zhu 2022, pp. 1-2, 2-3]。
- **交集检查**：2D 两线交点判定两步完成；3D 分解为多组线–面相交检测，算法复杂度均为 O(1) [Zhu 2022, pp. 3-4]。
- **高效集群分析**：扩展 Newman–Ziff 算法，采用 PTR 数组和 FindRoot 过程标记连通组；结合空间分块方法预筛潜在相交裂缝，大幅减少不必要的交集调用 [Zhu 2022, pp. 4-5]。
- **裂缝生长与 T 型交切**：基于规则模拟成核、生长和停滞过程，3D 下通过坐标缩放实现生长，并设定两种停滞模式（最长对角线两顶点停止或任意三顶点停止），从而在最终网络中形成 T 型交切 [Zhu 2022, pp. 5-7]。
- **C++ 实现**：全部算法用 C++ 编写，利用块方法等策略提升效率，比 Matlab 更适用于大规模 3D 模拟 [Zhu 2022, pp. 1-2, 4-5]。

## Key Findings
- **计算性能**：3D 网络构建比 2D 更消耗内存，但计算时间增加有限；2D 和 3D 集群检查算法标度相似，且 3D 中因块内裂缝更少，块方法加速效果更显著 [Zhu 2022, pp. 5-6]。
- **渗流参数敏感性**：对于长度服从幂律分布、方位服从 von Mises–Fisher 分布、位置均匀或分形的合成网络，仅当幂律指数大于 3.5 时，三个常用统计量（长度、密度等）才能作为渗流参数；分形分布网络中没有一个量是渗流参数。实际露头裂缝大多类似于分形分布网络 [Zhu 2022, pp. 7-8]。
- **强度分析功能**：软件可生成 3D 网络并完成 1D/2D/3D 强度测量（如 \(P_{10}\), \(P_{21}\), \(P_{30}\), \(I_{2D}\), \(I_{3D}\)），以研究不同维度强度参数间的标度关系 [Zhu 2022, pp. 7-8]。
- **多功能验证**：成功应用于渗流分析、强度分析和流动连通性分析，证明软件通用性 [Zhu 2022, pp. 1-1, 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 扩展 Newman–Ziff 与块方法结合加速集群分析，2D 和 3D 计算时间标度相似 | [Zhu 2022, pp. 5-6] | 2D 线段、3D 多边形裂缝网络，块大小固定 | 3D 加速效果更强 |
| 幂律指数 >3.5 时，三个几何量可作渗流参数；分形分布网络中均无效 | [Zhu 2022, pp. 7-8] | 合成网络长度幂律分布、方位 von Mises–Fisher、位置均匀/分形 | 与 18 个露头图对比 |
| MLP 结合逆 CDF 可从任意频率直方图生成随机变量 | [Zhu 2022, pp. 2-3] | MLP 作为回归器，输入有限样本 | 灵活替代多项式插值 |
| 3D 裂缝交集检查复杂度 O(1)，通过线-面相交实现 | [Zhu 2022, pp. 3-4] | 适用于任意多边形裂缝 | 伪代码 Algorithm 1 |
| 裂缝生长模型可产生 T 型交切，提供两种 3D 停滞模式 | [Zhu 2022, pp. 6-7] | 基于规则成核-生长-停滞；缩放因子由速度模型决定 | 2D 和 3D 均实现 |

## Limitations
- 3D 裂缝形状假设为简单凸多边形，忽略天然裂缝的粗糙度和不规则边界；虽尺度增大时形状影响减弱，但局部表现受限 [Zhu 2022, pp. 1-2]。
- 裂缝生长模型的规则需由现场观测或实验标定，通用性取决于所选规则的合理性 [Zhu 2022, pp. 6-6]。
- 流动与连通性分析的具体验证结果未在索引片段中提供，无法评估其在真实地下问题中的准确性。
- 未全面测试软件在极端参数组合或接近内存极限时的表现。

## Assumptions / Conditions
- 裂缝独立生成（除生长模型外），各裂缝的位置和方向独立随机取样 [隐含于随机生成流程]。
- 裂缝几何为平面多边形（2D 线段、3D 多边形），忽略厚度和粗糙度 [Zhu 2022, pp. 1-2]。
- 分形空间密度分布通过乘性级联生成，分形维数 \(D\) 在 2D 中位于 1–2，3D 中 1–3；\(D\) 等于空间维数时退化为均匀分布 [Zhu 2022, pp. 2-3]。
- 生长模型中成核位置随机，扩展速度由固定模型确定，已存在裂缝在生长过程中保持固定 [Zhu 2022, pp. 5-7]。
- 集群分析需要将域划分为固定大小的块，且块内裂缝索引表实时维护 [Zhu 2022, pp. 4-5]。
- MLP 变量生成假设训练数据已充分覆盖目标分布，网络结构合适 [Zhu 2022, pp. 2-3]。

## Key Variables / Parameters
- 裂缝尺寸：幂律长度分布指数 \(a\) [Zhu 2022, pp. 7-8]
- 方位：von Mises–Fisher 分布集中参数 \(\kappa\) 和均值方向 \(\mu\) [Zhu 2022, pp. 7-8]
- 空间分布：分形维数 \(D\)（2D: \(D=2\) 均匀, \(D<2\) 聚集；3D 类似）[Zhu 2022, pp. 2-3]
- 集群标识：PTR 数组（记录根索引或集群大小）[Zhu 2022, pp. 4-5]
- 块方法：分块边长 \(Bs\)，决定筛选效率 [Zhu 2022, pp. 5-5]
- 强度指标：\(P_{10}\), \(P_{21}\), \(P_{30}\), \(I_{2D}\), \(I_{3D}\) [Zhu 2022, pp. 7-8]
- 生长模型：成核数 \(N\)，停滞模式（Mode 1/2）[Zhu 2022, pp. 6-7]
- MLP 参数：网络层数和神经元数（未具体给定）[Zhu 2022, pp. 2-3]

## Reusable Claims
1. **Claim**: 组合 Newman–Ziff 算法与空间分块方法可以在 2D 和 3D  DFN 中以近似线性时间完成连通集群识别；3D 场景下块内裂缝更少，加速效果更为明显。**Evidence**: Algorithm 2 和计算时间标度图 [Zhu 2022, pp. 4-6]。**Conditions**: 需要预先划分空间块并维护裂缝-块索引。**Limitations**: 最佳块大小依赖于裂缝密度与尺寸分布，文中未给出自动选取方法。
2. **Claim**: 利用 MLP 结合逆 CDF 能从有限频率直方图生成随机变量，无需预设分布函数，增强了模拟数据驱动性。**Evidence**: 文中描述并引用 Zurada (1992) 佐证 MLP 的回归能力 [Zhu 2022, pp. 2-3]。**Conditions**: 需要足够训练样本，并合理选择 MLP 架构。**Limitations**: 生成质量依赖于训练数据，未报告量化误差。
3. **Claim**: 裂缝生长模型通过引入成核、扩展和停滞规则，可以生成具有 T 型交切的网络，降低死端比例并提高连通性。**Evidence**: Algorithm 4 和 2D/3D 生长示意图 [Zhu 2022, pp. 5-7]。**Conditions**: 需定义成核密度、生长速度函数和停滞判据；3D 需选择停滞模式。**Limitations**: 计算成本随裂缝数增加而上升，规则合理性需外部数据约束。
4. **Claim**: 当裂缝长度幂律指数 \(a > 3.5\) 时，常用几何统计量可作为有效渗流参数；分形空间分布网络（\(D <\) 空间维数）中此类参数均失效。**Evidence**: 合成网络分析与露头验证 [Zhu 2022, pp. 7-8]。**Conditions**: 长度幂律分布、方位 von Mises–Fisher、位置均匀或分形。**Limitations**: 结论基于特定参数范围，未考虑方位集中度等因素的交互影响。

## Candidate Concepts
- [[discrete fracture network]]
- [[fracture clustering]]
- [[power-law distribution]]
- [[fractal spatial density]]
- [[percolation threshold]]
- [[fracture intensity]]
- [[T-type intersection]]
- [[connected fracture cluster]]
- [[Newman–Ziff algorithm]]
- [[machine learning]]
- [[multilayer perceptron]]
- [[block method]]

## Candidate Methods
- [[inverse CDF method]]
- [[acceptance–rejection method]]
- [[MLP for random variable generation]]
- [[multicascade process for fractal distribution]]
- [[Newman–Ziff cluster identification]]
- [[block-based spatial indexing]]
- [[3D fracture intersection detection]]
- [[rule-based fracture growth]]
- [[percolation analysis]]
- [[fracture intensity measurement (P10, P21, P30, etc.)]]
- [[flow and connectivity analysis in DFN]]

## Connections To Other Work
- 渗流分析结果直接沿用 [[Zhu et al. 2018]] 的研究，详细讨论了不同裂缝网络类型的渗流行为 [Zhu 2022, pp. 7-8]。
- 裂缝形状参照 [[Baecher et al. 1977]] 的随机圆盘模型，并参考 [[Jing and Stephansson 2007]] 对形状影响的评述 [Zhu 2022, pp. 1-2]。
- 分形空间分布借鉴了 [[Darcel et al. 2003]] 的连通性分析和 [[Bour and Davy 1997]] 的均匀分布假设 [Zhu 2022, pp. 2-3]。
- 裂缝生长模型基于 [[Davy et al. 2013]] 的 2D 三步生长框架并扩展至 3D [Zhu 2022, pp. 5-6]。
- 集群算法源自 [[Hoshen and Kopelman 1976]]，并参考了 [[Al-Futaisi and Patzek 2003]] 的改进 [Zhu 2022, pp. 4-4]。
- 未从索引片段中确认与其他 DFN 软件（如 FracMan、dfnWorks）的直接性能对比。

## Open Questions
- 两种 3D 停滞模式（Mode 1 和 Mode 2）对连通性和强度参数的量化影响如何？片段未提供比较数据。
- MLP 生成随机变量时尾部分布的保真度是否有理论保障？与传统核密度估计方法的比较结果未显示。
- 软件是否支持力学反馈或非均匀应力场引导的生长过程？当前规则可能仅适用于简单动力学约束。
- 流动与连通性分析的具体实现细节（如边界条件、求解器）以及在真实网络中的验证结果均未在片段中给出。

## Source Coverage
本页依据 14 个索引片段，主要覆盖论文摘要、引言、方法描述（第 2–3 节）及应用示例的开头部分（第 3 节），页码范围 pp. 1-8。片段缺失完整的计算结果对比、性能基准测试数据、MLP 具体训练参数、强度分析回归公式以及附录内容。因此，性能的量化细节、部分方法的有效性验证以及软件极限等重要信息未能包含。现有信息足以概述软件架构和创新点，但深入评估需查阅全文。
