---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks"
title: "Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Péclet-Number-Dependent Longitudinal Dispersion in Discrete Fracture Networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yin, Tingchang, et al. \"Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks.\" *Water Resources Research*, 2024, doi:10.1029/2024WR038437. Accessed 2026."
indexed_texts: "25"
indexed_chars: "124689"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:20:58"
---

# Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks.

## One-line Summary
通过大量三维随机离散裂隙网络(DFN)模拟，本文发现纵向弥散系数依赖于基于大裂隙影响重新定义的Péclet数，并提出了一个普适的有限尺度标度函数 [Yin 2024, pp. 1-1, 3-4]。

## Research Question
在离散裂隙网络中，纵向弥散系数如何受Péclet数和裂隙网络结构（如密度、尺寸分布）影响？渐近弥散状态在何种条件下出现？能否找到一个普适关系来描述弥散行为？[Yin 2024, pp. 1-1, 1-2]

## Study Area / Data
### 模拟场景设置
研究基于大量三维随机离散裂隙网络(DFN)。裂隙的等效开度(b)和导水系数遵循幂律关系，并采用立方定律关联开度与导水系数 [Yin 2024, pp. 4-6]。模拟设计了四组场景，改变裂隙密度、尺寸分布和Péclet数，密度范围从约ρ'<sub>c</sub>到4×ρ'<sub>c</sub>（其中ρ'<sub>c</sub> ≈ 2.31为逾渗阈值）[Yin 2024, pp. 7-9]。每个模拟注入粒子数N<sub>P</sub> = 300,000 [Yin 2024, pp. 6-7]。

## Methods
### DFN生成与流动模拟
生成了三维随机DFN，其中裂隙中心位置、取向和尺寸可以变化。裂隙尺寸分布考虑了单一尺寸、幂律、对数正态和均匀分布四种类型 [Yin 2024, pp. 4-6]。裂隙等效开度b与尺寸R遵循幂律关系b = γR<sup>β</sup>，并引入立方定律k<sub>f</sub> = b³/12计算单裂隙导水系数 [Yin 2024, pp. 4-6]。

### 溶质运移模拟
采用离散时间随机游走方法进行粒子追踪，模拟裂隙内平流-扩散过程 [Yin 2024, pp. 6-7]。根据Péclet数的大小，采用不同的粒子注入条件和分配规则：在高Péclet数限下，粒子在交点处按出流流量权重分配；在低Péclet数限下，采用不同的分配方式 [Yin 2024, pp. 6-7]。通过计算粒子位移方差的线性时间演化来评估是否达到渐近弥散状态 [Yin 2024, pp. 1-1, 1-2]。

### 新Péclet数定义
提出了一个新的Péclet数(Pe<sub>c</sub>)，其中特征长度尺度考虑了大裂隙的影响，通过裂隙尺寸的一阶矩和平均裂隙速度来定义 [Yin 2024, pp. 1-1, 3-4]。

### 无量纲密度与连接性
采用无量纲密度ρ′来量化裂隙网络的局域连通性，该参数考虑了裂隙密度、尺寸和取向的期望值对连通性的影响，公式为 ρ′ = ρ × E[V<sub>a</sub><sup>ex</sup>]，其中 E[V<sub>a</sub><sup>ex</sup>] 与裂隙面积和周长期望值及取向相关 [Yin 2024, pp. 7-8]。

## Key Findings
### 渐近弥散状态的出现条件
渐近弥散状态在足够密的DFN中出现 [Yin 2024, pp. 1-1, 1-2]。随着裂隙密度的增加，迂曲度减小，首次通过时间(FPT)分布近似为钟形曲线，表明溶质粒子穿越更多裂隙、宏观裂隙间混合更均匀，但并未完全保证渐近状态的出现 [Yin 2024, pp. 1-1]。

### Péclet数的影响与幂律关系
重新定义后的Pe<sub>c</sub>对弥散的影响远超其他裂隙参数 [Yin 2024, pp. 3-4]。无量纲纵向弥散系数D′<sub>L</sub>与高Pe<sub>c</sub>值呈现唯一的幂律关系 [Yin 2024, pp. 1-1]。当平流占主导(Pe ≫ 1)时，D′<sub>L</sub>随Pe增加呈幂律增大，且随裂隙密度增加而减小；当扩散占主导(Pe ≪ 1)时，Pe对D′<sub>L</sub>影响可忽略，但D′<sub>L</sub>随裂隙密度增加而增大 [Yin 2024, pp. 2-3]。

### 有限尺度标度(FSS)函数
当平流占主导时，无量纲D<sub>L</sub>可由一个与裂隙密度和域尺寸相关的普适有限尺度标度函数描述，该函数对于不同裂隙参数和域尺寸是普适的 [Yin 2024, pp. 1-1, 3-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|:---|:---|:---|:---|
| 渐近状态在足够密的DFN中出现 | [Yin 2024, pp. 1-1, 1-2] | 三维随机DFN，裂隙开度与尺寸幂律相关 | FPT分布趋于钟形，粒子位移方差线性演化 |
| D′<sub>L</sub>与高Pe<sub>c</sub>值呈唯一幂律关系 | [Yin 2024, pp. 1-1] | 使用新定义的Pe<sub>c</sub>，特征长度考虑大裂隙影响 | 无量纲化后普适成立 |
| Pe的影响远强于裂隙密度 | [Yin 2024, pp. 1-1, 3-4] | 对比不同密度和Pe条件的模拟 | 新Pe<sub>c</sub>定义下更显著 |
| 平流主导时D′<sub>L</sub>随Pe幂律增大且随密度增大而减小 | [Yin 2024, pp. 2-3] | Pe ≫ 1场景 | 一前人在多孔介质中有相似发现 |
| 扩散主导时D′<sub>L</sub>受Pe影响小但随密度增大而增大 | [Yin 2024, pp. 2-3] | Pe ≪ 1场景 | 与多孔介质行为相似 |
| 有限尺度标度函数在平流主导时普适成立 | [Yin 2024, pp. 1-1, 3-4] | 不同裂隙参数和域尺寸条件 | 函数取决于裂隙密度和域尺寸 |

## Limitations
- 渐近状态的推定基于FPT分布近似钟形，但作者指出“并不完全保证”渐近弥散状态的出现 [Yin 2024, pp. 1-1]。
- 三维DFN模拟在特定参数范围内进行，密度从接近ρ′<sub>c</sub>到4×ρ′<sub>c</sub> [Yin 2024, pp. 8-9]。未从索引片段中确认参数范围是否覆盖所有实际场景。
- 裂隙开度与尺寸的幂律关系和立方定律假设仅适用于特定条件，可能不适用于所有真实裂隙 [Yin 2024, pp. 4-6]。
- 粒子追踪方法对于多组分混合可能不够准确 [Yin 2024, pp. 6-7]。

## Assumptions / Conditions
- 断裂网络为三维随机离散裂隙网络(DFN)，裂隙中心、取向和尺寸遵循特定分布 [Yin 2024, pp. 4-6]。
- 裂隙等效开度b与尺寸R遵循幂律关系 b = γR<sup>β</sup>，并采用立方定律 k<sub>f</sub> = b³/12 [Yin 2024, pp. 4-6]。
- 溶质运移由平流-扩散方程描述，采用离散时间随机游走方法求解 [Yin 2024, pp. 6-7]。
- 粒子在裂隙交点处采用完全混合规则；高Pe时限下按出流流量权重分配，低Pe时限下采用不同规则 [Yin 2024, pp. 6-7]。
- 水饱和条件，粒子为被动示踪剂 [Yin 2024, pp. 6-7]。
- 渐近状态定义基于粒子位移方差的线性时间演化（即弥散系数时间无关） [Yin 2024, pp. 1-2]。

## Key Variables / Parameters
| Variable / Parameter | Definition | Unit / Form | Source |
|:---|:---|:---|:---|
| Pe | 传统Péclet数，平流与扩散速率的比值 | 无量纲 | [Yin 2024, pp. 2-3] |
| Pe<sub>c</sub> | 新定义的Péclet数，特征长度考虑大裂隙影响 | 无量纲 | [Yin 2024, pp. 1-1, 3-4] |
| D<sub>L</sub> | 纵向弥散系数 | L²T⁻¹ | [Yin 2024, pp. 1-1] |
| D′<sub>L</sub> | 无量纲纵向弥散系数 (D<sub>L</sub>/D<sub>m</sub>) | 无量纲 | [Yin 2024, pp. 2-3] |
| D<sub>m</sub> | 分子扩散系数 | L²T⁻¹ | [Yin 2024, pp. 2-3] |
| ρ′ | 无量纲密度，局域连通性指标 | 无量纲 | [Yin 2024, pp. 7-8] |
| ρ′<sub>c</sub> | 逾渗阈值 | 约2.31 | [Yin 2024, pp. 7-8] |
| b | 裂隙等效开度 | L | [Yin 2024, pp. 4-6] |
| R | 裂隙尺寸（半径） | L | [Yin 2024, pp. 4-6] |
| γ, β | 开度-尺寸幂律关系常数与指数 | β无量纲 | [Yin 2024, pp. 4-6] |
| k<sub>f</sub> | 单裂隙导水系数 | L³ | [Yin 2024, pp. 4-6] |
| κ | 裂隙取向分布的浓度参数 | 无量纲 | [Yin 2024, pp. 8-9] |

## Reusable Claims
### Claim 1
在三维DFN中，当裂隙密度足够高时，溶质运移可达到渐近弥散状态，表现为粒子位移方差随时间的线性演化 [Yin 2024, pp. 1-1, 1-2]。条件：裂隙开度与尺寸幂律相关，溶质为被动示踪剂。限制：作者指出FPT钟形曲线“并不完全保证”渐近状态的出现 [Yin 2024, pp. 1-1]。

### Claim 2
重新定义的Péclet数Pe<sub>c</sub>（特征长度考虑大裂隙影响）比裂隙密度对纵向弥散的影响更强，且无量纲D<sub>L</sub>与高Pe<sub>c</sub>值呈唯一幂律关系 [Yin 2024, pp. 1-1, 3-4]。条件：新Pe<sub>c</sub>定义，高Pe<sub>c</sub>范围。限制：具体幂律指数未从索引片段中确认。

### Claim 3
平流主导(Pe ≫ 1)时，无量纲纵向弥散系数D′<sub>L</sub>随Pe幂律增大，随裂隙密度增加而减小；扩散主导(Pe ≪ 1)时，Pe影响可忽略但D′<sub>L</sub>随密度增加而增大 [Yin 2024, pp. 2-3]。条件：三维DFN，裂隙开度-尺寸幂律关系。限制：具体参数范围和幂律指数未从片段中确认。

### Claim 4
在平流主导条件下，无量纲D<sub>L</sub>可通过一个与裂隙密度和域尺寸相关的普适有限尺度标度(FSS)函数来描述，该函数对不同裂隙参数和域尺寸是普适的 [Yin 2024, pp. 1-1, 3-4]。条件：平流主导，三维DFN。限制：函数的具体形式未从索引片段中确认；扩散主导时是否成立未确认。

## Candidate Concepts
- [[fracture network]] (离散裂隙网络)
- [[asymptotic dispersion]] (渐近弥散)
- [[Péclet number]] (Péclet数)
- [[longitudinal dispersion coefficient]] (纵向弥散系数)
- [[finite-size scaling]] (有限尺度标度)
- [[percolation threshold]] (逾渗阈值)
- [[tortuosity in fractured media]] (裂隙介质迂曲度)
- [[Fickian dispersion]] (Fickian弥散)
- [[random walk particle tracking]] (随机游走粒子追踪)
- [[cubic law]] (立方定律)

## Candidate Methods
- [[discrete fracture network (DFN) generation]] (离散裂隙网络生成)
- [[particle tracking method]] (粒子追踪法)
- [[finite element method for DFN flow]] (DFN流动有限元法)
- [[discrete time random walk]] (离散时间随机游走)
- [[Monte Carlo simulation for DFN]] (DFN蒙特卡洛模拟)
- [[first passage time distribution analysis]] (首次通过时间分布分析)
- [[percolation analysis]] (逾渗分析)

## Connections To Other Work
### Previously Confirmed Relations
- Huseby et al. (2001) 发现在三维单分散DFN中，对于 Pe ≫ 1，D<sub>L</sub> 随 Pe 幂律增加并随裂隙密度增加而减小；Pe ≪ 1 时 Pe 影响可忽略但 D<sub>L</sub> 随密度增加而增大 [Yin 2024, pp. 2-3]。
- Zhao et al. (2010) 在二维DFN中发现当纵向运移距离足够长时D<sub>L</sub>值稳定，且流动方向与裂隙平均取向平行时流速更大、D<sub>L</sub>更小 [Yin 2024, pp. 2-3]。
- 多孔介质中也观察到类似的Pe依赖关系：Pe ≫ 1时弥散随Pe幂律增大，Pe ≪ 1时弥散与Pe弱相关但随结构变化 [Yin 2024, pp. 2-3]。

### Candidate Connections
- [[permeability estimation in fracture networks]]：通过局域连通性ρ′将弥散行为与水力特性（连通性、渗透率）关联 [Yin 2024, pp. 7-8]。
- [[solute transport in porous media]]：Pe依赖规律与多孔介质中观测相似，暗示可能的跨介质类比关系 [Yin 2024, pp. 2-3]。

## Open Questions
- 新定义的Pe<sub>c</sub>在低Péclet数条件下是否仍具有主导影响，以及其与弥散的普适关系是否仍然成立？[未从索引片段中确认]
- 有限尺度标度函数的具体数学形式及其适用范围（如扩散主导时）？[未从索引片段中确认]
- 渐近状态出现的确切条件（如最低密度阈值）以及如何定量判定的更严格准则？[Yin 2024 指出FPT钟形曲线不构成充分条件，pp. 1-1]
- 在实际野外尺度的裂隙网络中，这些普适关系的适用性和验证情况如何？[未从索引片段中确认]

## Source Coverage
本页基于论文索引的25个片段（覆盖第1-9页主要涉及摘要、引言、方法与部分结果）。覆盖内容包括：研究动机与背景 [Yin 2024, pp. 1-4]、DFN生成与数值方法 [Yin 2024, pp. 4-7]、部分结果（渐近状态判定、Pe<sub>c</sub> 定义与影响、FSS假设）[Yin 2024, pp. 1-1, 3-4, 7-9]。**未覆盖的重要信息可能包括**：完整的模拟参数表、FPT分布的具体形状分析、FSS函数的具体表达式和拟合参数、低Pe条件下Pe<sub>c</sub>的表现、Pe<sub>c</sub>的定义公式细节、迂曲度的具体计算结果、第四组模拟场景的详细结果、以及讨论与结论部分的完整论述。片段主要集中在论文前半部分，对验证部分和最终结论的覆盖有限。
