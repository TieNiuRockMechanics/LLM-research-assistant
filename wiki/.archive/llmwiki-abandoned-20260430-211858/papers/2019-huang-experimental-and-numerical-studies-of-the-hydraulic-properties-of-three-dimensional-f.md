---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-huang-experimental-and-numerical-studies-of-the-hydraulic-properties-of-three-dimensional-f"
title: "Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures."
status: "draft"
source_pdf: "data/papers/2019 - Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.pdf"
collections:
citation: "Huang, Na, et al. \"Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.\" *Rock Mechanics and Rock Engineering*, vol. 52, 2019, pp. 4731-4746. doi:10.1007/s00603-019-01869-7."
indexed_texts: "13"
indexed_chars: "64881"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:06:31"
---

# Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.

## One-line Summary
本研究通过透明三维裂隙网络的流体流动实验与数值模拟，揭示了空间分布的非均质开度（aperture）对粗糙裂隙中水流渠道化（channeling flow）和渗透率的影响 [Huang 2019, pp. 1-2]。

## Research Question
如何定量评估由空间分布的非均质开度（服从正态分布与截断对数正态分布）引起的流动渠道化效应对三维裂隙网络水力特性的影响？ [Huang 2019, pp. 1-2]。

## Study Area / Data
- **物理实验样本**：一个尺寸为 200×100×100 mm 的三维透明树脂裂隙网络模型，包含 5 个裂隙分支（fracture segments 1–5），其开度场服从均值为 0.804 mm、偏差为 0.317 的正态分布，并包含若干零开度接触点 [Huang 2019, pp. 3-5]。
- **数值模拟拓展数据**：具有更大裂隙密度的复杂三维离散裂隙网络（DFN）模型，其开度场服从不同均值（em = 0.5, 1.0, 2.0 mm）和偏差（σ = 0.5, 1.0, 1.5, 2.0）的正态分布，以及服从截断与完整对数正态分布的模型 [Huang 2019, pp. 1-2, 9-10]。

## Methods
- **物理模型制备**：利用五轴加工技术（分辨率 0.05 mm，公差 0.006 mm）在透明树脂上精确制造具有空间分布开度的裂隙表面块体，并组装成三维裂隙网络模型 [Huang 2019, pp. 1-3, 3-5]。
- **流动可视化实验**：通过注射泵控制流量（0.39×10⁻⁵ 至 5.60×10⁻⁵ m³/s），使用高分辨率CCD相机直接观测并量化染色流体在透明裂隙网络内的流动行为，并记录了9种不同入口/出口组合下的水力压差 [Huang 2019, pp. 5-6]。
- **渗透率计算**：基于Forchheimer方程（综合考虑粘性项 A 和惯性项 B），在低雷诺数（Re）线性流阶段反算等效渗透率 K [Huang 2019, pp. 6-7]。
- **数值模拟代码**：使用 Huang et al. (2018) 开发的代码，对裂隙网络进行二维网格离散，用 Galerkin 方法求解稳态流方程，并处理裂隙交线处的连续性条件。模拟以恒定水头差作为边界条件 [Huang 2019, pp. 6-7]。
- **渠道化流定量评估**：定义优先流路径为局部流量与总流量之比大于 0.005 的单元，并计算主流动通道占裂隙平面的比例 [Huang 2019, pp. 1-2, 9-10]。

## Key Findings
- **制造与可视化**：五轴加工技术成功制造了具有空间分布开度的三维透明裂隙网络样本，实现了对裂隙内流动行为的直接可视化和量化 [Huang 2019, pp. 1-2]。
- **模型验证**：物理实验与数值模拟得到的等效渗透率 K 的相对误差 r1 小于 10%，验证了数值模拟方法的可靠性 [Huang 2019, pp. 7-9]。
- **流动非线性**：在高水力梯度下，由于裂隙空间变化和交叉点造成的摩擦损失，实测流量显著偏离基于立方定律的预测，表现出明显的非线性流动特征 [Huang 2019, pp. 7-9]。
- **开度分布对流动渠道化的影响**：开度均值减小或偏差增大，流动渠道化效应越显著。主流动通道（流量比>0.005 的单元）的面积占裂隙平面的大约 26–67% [Huang 2019, pp. 1-2]。
- **截断对数正态分布的影响**：当开度服从截断对数正态分布时，其渗透率与服从完整对数正态分布模型的渗透率之比，随截断阈值的增大先急剧增加，随后趋近于 1.0 [Huang 2019, pp. 1-2]。
- **临界截断阈值**：提出了一个预测临界截断阈值的数学表达式，该临界值定义为当标准化渗透率（normalized permeability）等于 0.9 时的截断阈值 [Huang 2019, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 数值模拟与物理实验的等效渗透率相对误差（r1）小于 10%。 | [Huang 2019, pp. 7-9, Table 1] | 对9种不同入口/出口组合进行了测试，使用透明裂隙网络物理模型。 | 验证了基于 Forchheimer 方程和连续性条件的数值代码的有效性。 |
| 实验测得的流量在高水力梯度下与立方定律预测值存在显著偏差。 | [Huang 2019, pp. 7-9, Fig. 4] | 需同时考虑粘性力和惯性力。 | 例如，在 case inlet 1&2、outlet 1 中，要达到 Q = 3×10⁻⁵ m³/s，非线性流所需的水力梯度（i=2.730）远大于线性流（i=0.774）。 |
| 随着开度均值减小或偏差增大，流动局部化现象愈发明显，主流动通道约占裂隙平面的 26–67%。 | [Huang 2019, pp. 1-2, 9-10] | 模型开度服从正态分布。主通道定义为局部与总流量比高于 0.005 的单元。 | 流动渠道化直接受控于开度场的统计参数。 |
| 截断对数正态分布模型的渗透率与完整对数正态分布模型的渗透率之比，随截断阈值增大先急剧增加后趋近于 1.0。 | [Huang 2019, pp. 1-2] | 用于评估开度分布尾部（大值开度）对整体渗透性的影响。 | 强调了必须合理选择截断阈值，以避免低估渗透率。 |

## Limitations
- 物理实验是在单个稀疏裂隙网络样本上进行的，其结论推广到更复杂的、高密度裂隙网络时需要依赖数值模拟的验证 [Huang 2019, pp. 2-3, 3-5]。
- 数值模拟中，裂隙交叉处的连续性条件的处理方式对结果精度至关重要，但文中未详细讨论其在不同几何复杂性下的适用性边界 [Huang 2019, pp. 6-7]。
- 关于开度分布影响的数值模拟结论，未从索引片段中确认是否涵盖了不同剪切位移或应力条件下的开度场。

## Assumptions / Conditions
- **物理模型**：裂隙网络模型被分割为数个块体，通过五轴加工并粘合而成；裂隙壁在接触点处被认为是光滑且平行的 [Huang 2019, pp. 3-5]。
- **流动方程**：在裂隙尺度采用 Forchheimer 方程描述流体流动，该方程同时考虑了粘性力（线性项 A）和惯性力（非线性项 B）。等效渗透率 K 是在忽略惯性效应的线性流阶段（低 Re 数下）反算得到的 [Huang 2019, pp. 6-7]。
- **数值模型**：数值模拟在每个裂隙面内使用二维网格，并在裂隙交线上施加流量和压力的连续性条件。边界条件为恒定水头差和无流量边界 [Huang 2019, pp. 6-7]。
- **开度分布**：数值模拟主要基于正态分布和（截断）对数正态分布生成开度场，所有负开度被设定为零以代表接触 [Huang 2019, pp. 3-3, 9-10]。

## Key Variables / Parameters
- `σ`：正态分布开度场的偏差 [Huang 2019, pp. 2-3]。
- `e_m`：正态分布开度场的均值 [Huang 2019, pp. 3-5]。
- `σ_f`：对数正态分布开度场的偏差 [Huang 2019, pp. 2-3]。
- `K`（等效渗透率）：基于 Forchheimer 方程在线性流阶段反算 [Huang 2019, pp. 6-7]。
- `A`、`B`：Forchheimer 方程中分别代表粘性和惯性效应的线性与非线性系数 [Huang 2019, pp. 6-7]。
- `r_1`（相对误差）：用于比较实验（KE）与数值模拟（KS）得到的等效渗透率 [Huang 2019, pp. 7-9]。
- `接触比`（Contact ratio）：接触面积与整个裂隙平面面积之比 [Huang 2019, pp. 9-10]。
- `主流动通道比例`：流量比高于 0.005 的单元面积占裂隙平面的百分比 [Huang 2019, pp. 1-2, 9-10]。
- `标准化渗透率`（Normalized permeability）：截断对数正态分布模型的渗透率与完整对数正态分布模型渗透率的比值。临界截断阈值定义为此值为 0.9 时的值 [Huang 2019, pp. 1-2]。

## Reusable Claims
- 五轴加工技术可被用于制造具有良好透明度和高精度、包含空间分布开度的三维裂隙网络物理模型，用于直接观察流动通道化 [Huang 2019, pp. 1-2]。
- 对于给定的三维裂隙网络，基于 Forchheimer 方程反算的等效渗透率 K 在 9 种不同流动方向下的物理实验与数值模拟结果之间的一致性（相对误差<10%），验证了所述的物理模型制备和数值计算方法的可靠性 [Huang 2019, pp. 7-9, Table 1]。
- 裂隙网络中开度场的统计属性（均值、偏差）直接控制着流动渠道化程度。在单一裂隙网络中，主流动通道的面积可低至总面积的 26% 左右，这一发现强调了在渗透率估算中考虑流动局部化的必要性 [Huang 2019, pp. 1-2]。
- 当使用截断对数正态分布描述开度时，存在一个临界截断阈值（基于标准化渗透率=0.9 定义），阈值以下的截断会显著低估渗透率；提出的数学表达式可用于预测该临界值 [Huang 2019, pp. 1-2]。

## Candidate Concepts
- [[fracture reservoir]]
- [[hydraulic properties]]
- [[discrete fracture network]]
- [[aperture distribution]]
- [[flow channeling]]
- [[equivalent permeability]]

## Candidate Methods
- [[five-axis machining]]
- [[flow visualization experiment]]
- [[Forchheimer equation]]
- [[cubic law]]
- [[Galerkin method]]
- [[numerical simulation of DFN]]

## Connections To Other Work
- 未从索引片段中确认该研究直接引用/对比了哪些具体论文的量化结论。可从主题上连接到以下候选概念与方法：
    - 裂缝性多孔介质流动：研究中引用了流体在裂缝性介质中沿优势通道流动的观点，如 Black et al. (2017) 和 Dessirier et al. (2018) 建议使用通道网络模型（channel network model）研究流动渠道化效应 [Huang 2019, pp. 2-3]。
    - 开度分布描述：研究直接建立在将开度场描述为正态分布（被 Brown et al. 1986 等认为符合天然裂缝）和对数正态分布（被 Keller 1998 等认为符合）的广泛工作之上 [Huang 2019, pp. 3-3]。
    - 离散裂隙网络建模：本研究是诸多利用 3D DFN 模型分析裂隙水力特性（如 de Dreuzy et al. 2012; Ishibashi et al. 2012）工作的延续和实验验证 [Huang 2019, pp. 2-3]。

## Open Questions
- 提出的临界截断阈值预测数学表达式的具体形式和普适性如何？未从索引片段中确认 [Huang 2019, pp. 1-2]。
- 如何处理具有相关长度（correlation length）和各向异性开度场（文中提及了 anisotropic aperture 的影响）对流动渠道化及尺度升级（upscaling）的定量影响？未从索引片段中确认 [Huang 2019, pp. 1-2]。
- 该方法应用于随应力变化的裂隙网络（如剪切导致的剪胀效应）时的适用性如何？未从索引片段中确认。

## Source Coverage
本页面依据索引中的 13 个片段编写，覆盖了论文的摘要、引言、方法（物理模型制备、实验设置、数值模拟框架）、部分结果（模型验证、开度分布影响）和关键结论。片段内容偏向方法和结论性描述，对具体公式推导、复杂 DFN 模型的数值模拟细节以及与其他研究的定量对比部分的覆盖可能不完整。论文后半部分关于“尺度升级”（upscaling）的讨论在摘要中被截断，未在片段中充分展开。
