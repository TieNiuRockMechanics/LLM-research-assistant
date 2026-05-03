---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-feng-three-dimensional-simulation-for-radon-migration-in-fractured-rock-masses-a-computatio"
title: "Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach."
status: "draft"
source_pdf: "data/papers/2024 - Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses A Computational Modeling Approach.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Shengyang, et al. “Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach.” *Rock Mechanics and Rock Engineering*, vol. 57, 2024, pp. 3751–65. doi:10.1007/s00603-024-03766-0."
indexed_texts: "12"
indexed_chars: "59406"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:35:19"
---

# Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach.

## One-line Summary
本文提出了一种基于分形离散裂缝网络（DFN）的三维氡气迁移计算模型，开发了开源软件DFNRn，并利用有限元法模拟，揭示裂缝中流体对流主导氡迁移，分析了裂缝密度等参数对逾渗阈值和氡析出速率的影响。

## Research Question
传统模型将裂隙岩体视为均质各向同性介质，忽视了裂缝作为主要迁移通道的实质影响，导致氡迁移被低估[Feng 2024, pp.2-3]。如何构建能够在三维裂隙岩体中准确模拟氡迁移的计算模型，并系统量化裂缝网络非均质性、流体对流及裂缝几何参数的作用，是核心研究问题。

## Study Area / Data
研究区为一处位于地下约100 m的废弃铀矿[Feng 2024, pp.7-9]。模型底部边界氡浓度设为极限浓度 \(C_\infty = 3.7 \times 10^5 \, \text{Bq/m}^3\)，顶部为流出边界[Feng 2024, pp.8]。基岩假设渗透率为 \(8.7 \times 10^{-13} \, \text{m}^2\)，孔隙度0.2，氡扩散系数 \(1.1 \times 10^{-8} \, \text{m}^2/\text{s}\)[Feng 2024, pp.8]。模型所用DFN参数来自露头测量，包括分形维度、长度指数、归一化常数、平均方向角、Fisher常数、裂缝孔径分布等，具体数值见表1[Feng 2024, pp.7-8]。模型域尺寸为100 m[Feng 2024, pp.1]。实测氡析出速率为 \((4.53\pm 0.62)\times 10^{-3} \, \text{Bq/m}^2/\text{s}\)，用于验证模型[Feng 2024, pp.8]。

## Methods
- **DFN生成**：裂缝位置采用**分形乘性级联（multiplicative cascade）方法**（第一阶模型），以生成接近真实裂缝的聚簇分布[Feng 2024, pp.3-4]。裂缝长度和空间分布由**双幂律模型**描述（Davy et al. 1990）[Feng 2024, pp.3]。裂缝孔径采用**对数正态分布**确定，参数由露头或测井资料获取[Feng 2024, pp.4]。裂缝几何用**椭圆面**表示，未简化为等效管网络[Feng 2024, pp.4]。
- **数学模型**：分别建立裂缝内和基岩内氡迁移的控制方程，包含对流、扩散、衰变及源项，并在裂缝-基岩界面施加氡通量守恒条件[Feng 2024, pp.5-7]。
- **数值求解与软件**：利用**有限元法（FEM）**对含椭圆裂缝的三维几何进行离散和求解。开发了开源软件**DFNRn**（Discrete Fracture Network model for Radon migration），该软件集成**MATLAB**与**COMSOL Multiphysics**，通过LiveLink自动将生成的DFN导入COMSOL建立几何模型并求解[Feng 2024, pp.5-7]。软件已公开发布于GitHub[Feng 2024, pp.1]。
- **验证与参数分析**：对比不考虑流体对流（仅扩散）和考虑压力驱动对流两种情况，使用实测数据验证模型。进一步利用DFNRn子程序分析裂缝体积密度 \(P_{32}\) 对氡析出速率的影响，并研究了逾渗阈值 \(P'_{32}\) 与DFN关键参数的关系[Feng 2024, pp.1-2,10-11]。

## Key Findings
- **对流主导氡迁移**：无流体对流时，模型计算的平均氡析出速率仅 \(3.66 \times 10^{-5} \, \text{Bq/m}^2/\text{s}\)，远小于实测值；引入气体压力差并考虑对流后，模拟结果与实测一致，验证了模型准确性[Feng 2024, pp.8-9]。裂缝中最大氡析出速率是基质的15.4倍，表明氡迁移主要受裂缝内气体对流控制，且与Richon et al. (2010) 的结论一致[Feng 2024, pp.9]。
- **逾渗阈值效应**：裂缝体积密度 \(P_{32}\) 存在逾渗阈值 \(P'_{32} = 0.25 \, \text{m}^{-1}\)。低于此值，无裂缝从模型底部连接到顶部；超过后，连通裂缝提供快速对流通道，使氡析出速率显著增大（例如 \(P_{32}=0.36 \, \text{m}^{-1}\) 时的析出速率是 \(0.25 \, \text{m}^{-1}\) 时的2.8倍）[Feng 2024, pp.10-11]。
- **逾渗阈值与分形参数的关系**：
  - \(P'_{32}\) 随分形维数 \(D_f\) （\(1.4 \le D_f \le 1.9\)）和归一化常数 \(\alpha\)（\(1.4 \le \alpha \le 1.8\)）增大而减小；
  - \(P'_{32}\) 与长度指数 \(a\)（\(1.2 \le a \le 2.8\)）无相关关系；
  - \(P'_{32}\) 随平均方向角增大而减小，与Fisher常数无相关关系[Feng 2024, pp.1-2]。
- **时间演化特征**：裂缝出口最大氡浓度在对流开始后（约1.1天）显著上升，最大对流速度约90.9 m/d；基岩出口最大浓度稳定时间约5.5天，裂缝出口需7.2天，裂缝最大浓度为基质的6.86倍[Feng 2024, pp.9-10]。
- **源项影响**：基岩的氡源项对氡迁移影响最大[Feng 2024, pp.1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 无对流时模拟氡析出速率3.66×10⁻⁵ Bq/m²/s，远小于实测值(4.53±0.62)×10⁻³ Bq/m²/s；考虑气体对流后模拟结果与实测一致 | [Feng 2024, pp.8-9] | 底部边界浓度3.7×10⁵ Bq/m³，顶部流出；基岩渗透率8.7×10⁻¹³ m²，孔隙度0.2，扩散系数1.1×10⁻⁸ m²/s；气体压力差按约22.4 Pa估计 | 验证了对流在氡迁移中的主导地位 |
| 裂缝出口最大氡浓度在对流开始1.1天后快速上升，最大对流速度90.9 m/d；裂缝出口浓度稳定值为基质的6.86倍 | [Feng 2024, pp.9-10] | 域尺寸100 m；基质渗流速度4.5×10⁻⁷ m/s | 说明对流导致的快速运移通道 |
| 逾渗阈值 \(P'_{32}=0.25 \, \text{m}^{-1}\)，低于此值无贯通裂缝；\(P_{32}=0.36 \, \text{m}^{-1}\)时析出速率较0.25 m⁻¹增大2.8倍 | [Feng 2024, pp.10-11] | 采用与前文相同的模型参数；\(P_{32}\) 变化通过子程序控制，每个点模拟8次取平均 | 逾渗阈值以下连接性的缺失限制了氡运移 |
| \(P'_{32}\) 随 \(D_f\) (1.4–1.9) 和 \(\alpha\) (1.4–1.8) 增大而减小；与长度指数 \(a\) (1.2–2.8) 和Fisher常数无相关性；随平均方向角增大而减小 | [Feng 2024, pp.1-2] | 参数范围基于DFN建模时所采用的取值范围 | 揭示了控制逾渗的结构性因子 |
| 基岩氡源项对氡迁移影响最大 | [Feng 2024, pp.1-2] | 来自模型分析结论，详细灵敏度结果未在片段中提供 | 强调了源项在后续研究中的重要性 |

## Limitations
- 模拟中的气体压力差采用简化估算，方法有一定任意性，其准确性依赖于对气体密度等参数的假设[Feng 2024, pp.9]。
- DFN模型基于露头统计数据生成，实际三维裂缝网络的完整识别仍有困难，未从索引片段中确认更多讨论。
- 模型未明确考虑机械弥散和两相流效应，未从索引片段中确认其假设影响。
- 网格依赖性和计算成本未在片段中深入分析。

## Assumptions / Conditions
- 裂缝位置通过乘性级联过程生成，具有聚簇分布特征，基于一阶模型[Feng 2024, pp.3-4]。
- 裂缝长度分布服从双幂律模型[Feng 2024, pp.3]。
- 裂缝孔径服从对数正态分布，参数来自露头测量[Feng 2024, pp.4]。
- 裂缝形状为无厚度椭圆盘，未简化为等效管网络[Feng 2024, pp.4]。
- 基岩视为多孔介质，满足达西定律；流体为不可压缩气体；氡在基岩中满足以扩散为主、兼顾衰变和源项的对流-扩散方程[Feng 2024, pp.5-7]。
- 模型底部氡浓度恒定，顶部为流出边界；忽略地表大气氡背景影响[Feng 2024, pp.8]。
- 数值模拟中不考虑温度变化和化学反应。

## Key Variables / Parameters
- 裂缝网络参数：体密度 \(P_{32}\)、面密度 \(P_{21}\)；分形维数 \(D_f\)、归一化常数 \(\alpha\)、长度指数 \(a\)；Fisher常数 \(\kappa\)、平均方向角；裂缝孔径平均值 \(d\)、最小值 \(d_a\)、最大值 \(d_b\)、偏差 \(h\)。
- 逾渗阈值 \(P'_{32}\) （裂缝开始贯通时的临界体密度）。
- 基岩物性：渗透率 \(8.7 \times 10^{-13} \, \text{m}^2\)、孔隙度 \(\phi = 0.2\)、氡扩散系数 \(D = 1.1 \times 10^{-8} \, \text{m}^2/\text{s}\)。
- 源项与边界：底部恒定氡浓度 \(C_\infty = 3.7 \times 10^5 \, \text{Bq/m}^3\)；气体压力差（估算值约22.4 Pa）。
- 概化公式：\(P_{32} = C_{32} P_{21}\) 中校正因子 \(C_{32}\) 与Fisher常数和平均采样校正角有关[Feng 2024, pp.7-8]。
- 输出指标：氡析出速率（Bq/m²/s）、裂缝/基质氡浓度、对流速度、稳定时间。

## Reusable Claims
- 在连通裂缝网络存在足够气体压力差时，裂缝内流体对流是氡迁移的主要驱动力，其对氡析出速率的贡献可比纯扩散高数个量级；因此任何忽略对流的模型将严重低估氡的输出。适用条件：存在一定的压力梯度且裂缝连通路径已形成，否则扩散仍占主导。[Feng 2024, pp.8-10]
- 三维 DFN中裂缝体密度存在逾渗阈值 \(P'_{32}\)，低于该值时模型顶部无贯通裂缝，氡难以通过裂缝通道快速逃逸；超过阈值后，进一步增大 \(P_{32}\) 对析出速率的增量效应减弱。适用条件：在给定的DFN建模框架和分形参数范围内。[Feng 2024, pp.10-11]
- 逾渗阈值 \(P'_{32}\) 随分形维数 \(D_f\) 和归一化常数 \(\alpha\) 的增大而减小，但与长度指数 \(a\) 和Fisher常数无关。这意味着提高裂缝的空间填充程度（通过增大 \(D_f\) 或 \(\alpha\)）使贯通更容易发生。适用条件：参数范围 \(1.4 \le D_f \le 1.9\)、\(1.4 \le \alpha \le 1.8\)、\(1.2 \le a \le 2.8\)。[Feng 2024, pp.1-2]
- 使用对数正态分布与乘性级联相结合的方法能够生成具有真实聚类特征的裂缝网络，结合椭圆几何和有限元求解，是模拟裂缝岩体氡迁移的有效计算策略。该策略可延伸至其他溶质运移问题。限制：对复杂几何的计算成本较高，当前实现通过COMSOL完成。[Feng 2024, pp.3-7]

## Candidate Concepts
- [[fractured rock mass]]
- [[discrete fracture network]]
- [[radon migration]]
- [[multiplicative cascade process]]
- [[percolation threshold]]
- [[fractal dimension]]
- [[fluid convection]]
- [[ellipse fracture]]
- [[lognormal aperture distribution]]
- [[uranium mine radon]]
- [[coal-uranium co-exploitation]]
- [[radon exhalation rate]]

## Candidate Methods
- [[finite element method]]
- [[multiplicative cascade method]]
- [[dual-power-law model]]
- [[COMSOL Multiphysics]]
- [[DFNRn software]]
- [[lognormal distribution]] for aperture
- [[Darcy’s law]] for seepage velocity

## Connections To Other Work
- 模型引用了Davy et al. (1990) 的双幂律模型来描述裂缝长度与空间分布[Feng 2024, pp.3]；采用Baghbanan and Jing (2007) 的对数正态分布确定裂缝孔径[Feng 2024, pp.4]；裂缝位置生成基于Darcel et al. (2003b) 的乘性级联概念[Feng 2024, pp.3-4]。
- 模拟所得“对流主导氡迁移”的结论与Richon et al. (2010) 的现场观测一致[Feng 2024, pp.9]。
- 传统氡迁移模型（如Rogers and Nielson 1991）假设岩体均质各向同性，本文工作可视为对该类模型的替代和深化[Feng 2024, pp.2]。
- 与本研究相关的候选联系方向包括：[[radon tracing for earthquake prediction]]、[[coal-uranium deposit]]、[[fracture network modeling in geothermal reservoirs]]、[[gas transport in DFN]]。

## Open Questions
- 气体压力差的精确确定方法尚属简化估算，实际压力场在多相流条件下的分布如何影响氡迁移，未从索引片段中确认。
- 片段指出“基岩的氡源项对氡迁移影响最大”，但未进一步探究源项的空间非均质性或衰减特性对出口浓度的敏感性，有待后续研究。
- 机械弥散、吸附、两相流等次级机制的影响在片段中未讨论，是否在特定条件下需要加入模型，未从索引片段中确认。
- 模型所采用的分形和统计参数基于特定露头，推广至其他地质背景（如深部结晶岩）的适应性有待验证。

## Source Coverage
本页基于提供的12个索引片段编写，覆盖了论文的摘要、引言（问题与方法动机）、DFN生成与裂缝参数方法、数值求解与软件开发、验证案例及逾渗阈值分析等关键部分。片段较完整地呈现了核心方法、关键验证结果和参数敏感性结论，但对模型全部控制方程、源项处理的具体形式、详细的敏感性分析（如源项、扩散系数等）以及软件使用的完整操作流程覆盖有限。部分重要公式和参数取值范围已在片段内给出，但深层理论推导和模型限制的更细致讨论未在片段中展开。
