---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml"
title: "A Fractal Model for Characterizing Fluid Flow in Fractured Rock Masses Based on Randomly Distributed Rock Fracture Networks."
status: "draft"
source_pdf: "data/papers/2015 - A fractal model for characterizing fluid flow in fractured rock masses based on randomly distributed rock fracture networks.pdf"
collections:
  - "分形"
citation: "Liu, Richeng, et al. \"A Fractal Model for Characterizing Fluid Flow in Fractured Rock Masses Based on Randomly Distributed Rock Fracture Networks.\""
indexed_texts: "12"
indexed_chars: "58537"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:11:28"
---

# A Fractal Model for Characterizing Fluid Flow in Fractured Rock Masses Based on Randomly Distributed Rock Fracture Networks.

## One-line Summary
本文提出了一个分形模型，将随机分布裂隙网络的几何特征（分形维数）与其等效渗透率关联起来，并表明流体流动的迂曲度、裂隙开度及随机数对渗透率有显著影响 [Liu unknown-year, pp. 1-5]。

## Research Question
如何利用分形理论建立一个数学模型，以表征随机分布岩石裂隙网络的几何特征，并揭示这些特征对流体流动等效渗透率的影响？[Liu unknown-year, pp. 1-5]。

## Study Area / Data
本研究基于随机生成的二维离散裂隙网络模型，并非特定实地研究区域。裂隙的几何参数设定为：迹长遵循幂律分布；最小开度1 μm，最大开度100 μm；裂隙方向和中心点位置假设为均匀分布 [Liu unknown-year, pp. 12-15]。模型尺寸依据裂隙质量密度与分形维数的回归关系确定 [Liu unknown-year, pp. 12-15]。

## Methods
- **裂隙网络生成**：采用蒙特卡洛方法生成二维随机离散裂隙网络。裂隙迹长遵循基于分形理论推导的概率密度函数分布 [Liu unknown-year, pp. 5-7]。
- **裂隙参数关联**：裂隙水力开度与迹长通过包含误差函数的公式(14)关联，该公式假设开度服从对数正态分布 [Liu unknown-year, pp. 7-10]。
- **流体流动模拟**：采用稳态流体流动假设，基于质量守恒方程（式18）在通用离散元程序中进行，边界条件为水平方向的恒定水力梯度 [Liu unknown-year, pp. 10-12]。
- **分形维数计算**：采用改进的盒计数法计算离散裂隙网络模型的分形维数Df [Liu unknown-year, pp. 15-17]。
- **参数引入**：模型引入两个分形维数：Df代表裂隙的宏观几何分布；DT代表流体在粗糙裂隙中流动的微观迂曲度 [Liu unknown-year, pp. 20-22]。

## Key Findings
- **模型验证**：提出的分形长度分布方法得到的裂隙数量-长度相关性与前人研究结果吻合良好。通过盒计数法计算的分形维数Df与其理论值一致，验证了模型的可靠性 [Liu unknown-year, pp. 1-5]。
- **长度分布规律**：裂隙长度遵循幂律分布，其幂律指数a与分形维数Df呈线性负相关（a = -0.49Df + 3），理论范围从1.49到2.49，与文献报道的现场测量和理论分析值相符 [Liu unknown-year, pp. 15-17]。
- **流动路径识别**：当Df较小时（如1.5），流体主要在少数与水流方向近平行的长裂隙中流动。当Df超过某值（如1.5），流率分布变得均匀，较短的、非贯通的裂隙主导优势流动路径 [Liu unknown-year, pp. 20-22]。
- **渗透率影响因素**：等效渗透率显著受流体流动迂曲度（DT）和裂隙开度影响。随DT增加，渗透率降低。随Df增加，等效渗透率的变化遵循指数规律 [Liu unknown-year, pp. 20-22] [Liu unknown-year, pp. 1-5]。
- **随机性影响**：当Df较小时（如1.3），由于随机数导致的迹长、位置和方向的随机性，等效渗透率的变异性可达约5个数量级。当Df较大时（如1.7-1.8），变异性降至2个数量级以内，模型变得更加稳定和均质 [Liu unknown-year, pp. 17-20]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 计算的分形维数Df与理论值一致；裂隙长度-数量相关性与前人研究吻合 | [Liu unknown-year, pp. 1-5] | 使用本研究提出的分形长度分布方法生成的离散裂隙网络模型 | 验证了模型和长度分布方法的可靠性 |
| 等效渗透率K随分形维数Df的变化遵循指数规律 | [Liu unknown-year, pp. 20-22] | 模型具有较大Df值时 | 该数学表达式可用于大Df值的模型 |
| 裂隙长度幂律指数a与分形维数Df线性相关（a = -0.49Df + 3） | [Liu unknown-year, pp. 15-17] | 二维裂隙网络(Df∈[1, 2]) | 幂律指数a的理论范围（1.49-2.49）与文献一致 |
| 渗透率变异性随Df增大而减小：Df=1.3时约5个数量级，Df=1.7-1.8时小于2个数量级 | [Liu unknown-year, pp. 17-20] | 使用不同随机种子生成的同Df值模型 | 说明模型在小Df值时不稳定性高 |
| 随DT增加，等效渗透率减小 | [Liu unknown-year, pp. 20-22] | 迹长比（lmin/lmax）保持恒定 | DT代表微观迂曲度，增加流动阻力 |

## Limitations
- 模型验证是基于理论值的自洽性验证和与前人研究结果的对比，未从索引片段中确认是否有独立的物理实验或现场数据验证 [Liu unknown-year, pp. 1-5]。
- 裂隙方向和中心点分布被假设为均匀分布，这表明研究主要关注分形模型的有效性，而未涉及复杂的方向性分布对渗透率的影响 [Liu unknown-year, pp. 12-15]。
- 提出的渗透率与Df的数学表达式（指数关系）被指出主要适用于具有较大Df值的模型，对于小Df值模型，需引入如连通性等其他参数，但索引片段未提供这些参数的进一步分析 [Liu unknown-year, pp. 20-22]。

## Assumptions / Conditions
- **二维假设**：模型仅限于二维裂隙网络，Df的取值范围为[1, 2] [Liu unknown-year, pp. 5-7]。
- **裂隙尺寸分布**：裂隙迹长遵循基于分形理论推导的幂律分布 [Liu unknown-year, pp. 5-7]。
- **开度-长度关系**：假设长裂隙具有更大的水力开度，两者通过包含误差函数的公式相关，该公式基于开度对数正态分布的假设，并设定其第一、第二矩为log e=0, b=1 [Liu unknown-year, pp. 7-10]。
- **流动条件**：流体流动模拟采用稳态流，并施加恒定水力梯度的水平方向边界条件 [Liu unknown-year, pp. 10-12]。
- **裂隙方向与位置**：裂隙的取向和中心点在模型内均匀分布 [Liu unknown-year, pp. 12-15]。

## Key Variables / Parameters
- **Df**: 代表裂隙网络宏观几何分布的分形维数 [Liu unknown-year, pp. 1-5]。
- **DT**: 代表流体在粗糙裂隙内微观流动迂曲度的分形维数 [Liu unknown-year, pp. 1-5]。
- **K**: 裂隙网络的等效渗透率 [Liu unknown-year, pp. 1-5]。
- **lmin, lmax**: 裂隙的最小和最大迹长 [Liu unknown-year, pp. 5-7]。
- **a**: 裂隙长度幂律分布指数 [Liu unknown-year, pp. 15-17]。
- **Nt**: 裂隙总数量 [Liu unknown-year, pp. 7-10]。
- **R**: 用于生成长度分布的随机数 [Liu unknown-year, pp. 7-10]。
- **ei**: 第i条裂隙的水力开度 [Liu unknown-year, pp. 7-10]。
- **dm**: 裂隙的质量密度（每平方米的迹长总和） [Liu unknown-year, pp. 12-15]。

## Reusable Claims
- **Claim 1**: 对于二维离散裂隙网络模型，裂隙长度分布可采用分形方法描述，其幂律指数a与分形维数Df存在线性关系a = -0.49Df + 3。该模型生成的裂隙长度-数量相关性符合理论预期 [Liu unknown-year, pp. 15-17]。适用条件：裂隙为二维分布，Df在[1, 2]之间。
- **Claim 2**: 基于分形维数Df与渗透率K的指数关系建立的数学表达式，其主要适用范围是Df值较大的裂隙网络。对于Df值较小的网络，渗透率受随机性影响过大，该关系不再稳健 [Liu unknown-year, pp. 20-22]。局限性是未给出该表达式的具体形式以及Df的阈值。
- **Claim 3**: 裂隙网络模型的等效渗透率变异性与分形维数Df相关。Df越小，变异性越大；Df越大，模型越均质，变异性越小。这表明在高密度裂隙网络中，等效渗透率对局部几何细节的敏感性降低 [Liu unknown-year, pp. 17-20]。
- **Claim 4**: 在二维裂隙网络中，流体流动优势路径受分形维数Df控制。低Df时，流动受控于少数与宏观流向一致的长裂隙；高Df时，流动路径变得均匀，由众多较短的非贯通裂隙构成 [Liu unknown-year, pp. 20-22]。

## Candidate Concepts
- [[fractured rock mass]]
- [[fractal geometry]]
- [[discrete fracture network (DFN)]]
- [[equivalent permeability]]
- [[tortuosity]]
- [[power law distribution]]
- [[Monte Carlo method]]
- [[box-counting method]]

## Candidate Methods
- [[Monte Carlo simulation for fracture networks]]
- [[discrete fracture network (DFN) modeling]]
- [[fluid flow simulation in DFNs]]
- [[fractal dimension calculation (box-counting)]]
- [[fracture aperture-trace length correlation]]

## Connections To Other Work
- 本研究验证了Majumdar和Bhushan提出的面积/长度分布方程（公式2）可被用于描述裂隙长度分布 [Liu unknown-year, pp. 5-7]。
- 研究所采用的裂隙迹长-开度关联方法引用了Bagde等人和Liu等人的工作 [Liu unknown-year, pp. 7-10]。
- 生成的裂隙网络幂律长度分布与文献[17-18]中的二维随机裂隙网络类似 [Liu unknown-year, pp. 10-12]。
- 得出的幂律指数a的理论范围（1.49-2.49）与文献[17-18, 43-45]中的现场测量和理论分析结果吻合 [Liu unknown-year, pp. 15-17]。

## Open Questions
- 对于分形维数Df较小的裂隙网络模型，由于渗透率的巨大变异性，除连通性之外，还有哪些控制参数可以用来建立可靠等效渗透率预测模型？[Liu unknown-year, pp. 20-22]
- 本研究提出的分形模型如何从二维扩展至三维真实裂隙网络，三维条件下的指数关系和参数特性会是怎样？未从索引片段中确认。
- 模型假设裂隙方向和位置均匀分布，若考虑更符合地质实际的定向分布（如Fisher分布），分形维数与渗透率的关系将如何变化？未从索引片段中确认。

## Source Coverage
本知识页依据论文的12个索引片段（涵盖pp. 1-22）整理而成。片段覆盖了摘要、引言、方法论（分形特征、流动控制方程）、结果与分析（模型尺寸确定、长度分布验证、渗透率影响因素）以及结论等主要章节。索引片段提供了模型构建逻辑、关键参数关系、主要验证过程和核心发现，但缺少完整的公式推导细节、详尽的参数敏感性分析、与实验数据的直接对比验证，以及对小Df值模型局限性的深入讨论。
