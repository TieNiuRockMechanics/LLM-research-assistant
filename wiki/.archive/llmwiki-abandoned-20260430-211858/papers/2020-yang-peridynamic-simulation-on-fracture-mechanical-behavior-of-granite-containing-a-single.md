---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-yang-peridynamic-simulation-on-fracture-mechanical-behavior-of-granite-containing-a-single"
title: "Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment."
status: "draft"
source_pdf: "data/papers/2020 - Peridynamic simulation on fracture mechanical behavior of granite containing a single fissure after thermal cycling treatment.pdf"
collections:
  - "zotero new"
citation: "Yang, Zhen, et al. \"Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment.\" *Computers and Geotechnics*, vol. 120, 2020, 103414. doi:10.1016/j.compgeo.2019.103414."
indexed_texts: "16"
indexed_chars: "75676"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:18:45"
---

# Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment.

## One-line Summary
该论文基于全耦合常规状态近场动力学方法，提出了一种反映花岗岩非均质性的新方法，并模拟了热循环处理后含单裂隙花岗岩在单轴压缩下的热-力耦合断裂行为 [Yang 2020, pp. 1-2]。

## Research Question
热循环处理引起的矿物非兼容性膨胀如何导致微裂纹萌生，以及热循环处理后裂隙倾角如何组合影响花岗岩的应力-应变响应、峰值强度和裂纹演化过程？ [Yang 2020, pp. 1-3]

## Study Area / Data
**研究材料与数据来源**:
- **材料**: 含单条预制裂隙的花岗岩，裂隙角度（与水平方向夹角）为30°，用于校准模型；后用不同裂隙倾角进行参数化研究 [Yang 2020, pp. 7-10]。
- **数据**: 单轴压缩下的宏观力学行为（应力-应变曲线）实验数据引用自文献 [2] [Yang 2020, pp. 7-8]。具体包括室温下的峰值强度、峰值应变、裂纹路径等 [Yang 2020, pp. 8-10]。
- **热循环处理模拟**: 基于红外辐射加热、恒温与自然冷却阶段的描述，模拟热循环处理（对应于大多数实验室的炉膛加热试验） [Yang 2020, pp. 2-3] [Yang 2020, pp. 5-6]。

## Methods
1. **数值框架**: 采用全耦合常规状态近场动力学 (Fully Coupled Ordinary State-Based Peridynamic, OSB-PD) 方法，实现变形场与温度场的双向耦合 [Yang 2020, pp. 2-5]。
2. **岩石非均质性建模**: 提出了一种新方法，通过“Shuffle algorithm”对材料点进行重排序并赋予不同矿物参数，以准确反映矿物的组成和相应的热力学特性 [Yang 2020, pp. 8-10]。
3. **热循环处理模拟**: 基于辐射热交换边界条件（Stefan-Boltzmann方程）模拟热循环处理过程中的热-力耦合行为 [Yang 2020, pp. 5-6]。
4. **断裂准则**: 采用临界能量密度准则（Critical Energy Density Criterion），当储存在材料点对之间的能量密度超过临界值 `ξ_c` 时，键断裂，裂纹萌生并自发扩展 [Yang 2020, pp. 5-6]。
5. **参数校准**: 通过两个基准算例（瞬态热传导和裂纹扩展）进行模型确认与数值收敛性测试 (m-收敛 和 δ-收敛)，并通过将模拟结果与文献 [2] 中的实验数据进行对比，校准了泊松比、断裂能等核心力学参数 [Yang 2020, pp. 7-8]。

## Key Findings
1. **模型验证与收敛性**: 所提出的全耦合OSB-PD模型能够准确地模拟瞬态热传导问题。在m-收敛性测试中，非局部参数m=3时可以获得计算精度与效率的平衡；而m=2时会出现非真实的微裂纹。最终确定的离散化参数为非局部比率`m=3`，近场范围`δ=2.4 mm` [Yang 2020, pp. 6-10]。
2. **参数校准结果**: 通过与实验结果的比较，校准得到的花岗岩泊松比 (`υ`) 为 0.3，断裂能 (`G₀`) 为 50 J/m²。模拟得到的轴向应力-应变曲线和宏观力学参数（如峰值强度、峰值应变）与实验结果吻合良好 [Yang 2020, pp. 7-10]。
3. **裂纹路径模拟的局限性**: 虽然在室温下单裂隙花岗岩的宏观力学行为得到了很好的再现，但模型中未能适当地模拟出实验观察到的反剪切裂纹（anti-shear cracks），导致在峰值强度之后呈现出不真实的延性特征 [Yang 2020, pp. 8-10]。
4. **非均质性模拟**: 提出的Shuffle算法能够有效模拟岩石材料的非均质性，为研究不同矿物颗粒间的非兼容性热膨胀导致的微裂纹萌生奠定了基础 [Yang 2020, pp. 1-2] [Yang 2020, pp. 8-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 最优离散化参数为 `δ=2.4 mm`, `m=3`，可平衡计算精度和效率。 | [Yang 2020, pp. 8-10] | 模型校准阶段，针对含30°裂隙的花岗岩单轴压缩试验。 | 当 `m=2` 时出现非真实微裂纹，`m=4` 时结果变化不大但计算耗时增加。 |
| 校准后的力学参数 `υ = 0.3` 和 `G₀=50 J/m²` 能很好地再现实验应力-应变曲线。 | [Yang 2020, pp. 7-8] | 材料密度 `ρ = 2790 kg/m³`，弹性模量 `E=36 GPa`。 | 与文献[2]中常温实验数据对比验证。 |
| 模拟与实验的峰值强度和峰值应变高度接近，但未能捕捉到反剪切裂纹和峰后延性。 | [Yang 2020, pp. 8-10] | 参数 `δ=2.4 mm`, `m=3`，室温条件。 | 这表明模型在捕捉特定裂纹模式 (crack modes) 上存在局限性。 |
| 采用 `Critical Energy Density Criterion` 作为键的断裂准则。 | [Yang 2020, pp. 5-6] | 线弹性脆性材料，2D/3D 条件下的临界能量密度计算公式不同。 | 裂纹萌生与扩展是模型的内禀属性，无需外部准则。 |

## Limitations
1. **裂纹模式捕捉不足**: 模型未能成功模拟室温实验中观察到的反剪切裂纹，并导致了不真实的峰后延性行为 [Yang 2020, pp. 8-10]。
2. **摩擦接触行为缺失**: 基于连续体假设的PD模型不允许物理上的滑移行为，因此模型中没有包含有限元方法（FEM）中考虑的宏观摩擦-接触行为 [Yang 2020, pp. 5-6]。
3. 由于索引片段有限，尚不清楚模型在模拟多裂隙、三维复杂裂隙或更高温度循环次数下的表现和局限性。

## Assumptions / Conditions
1. **物理模型**: 材料本构为线弹性热弹性体；采用小变形假设；在运动方程和热扩散方程中考虑了全场双向耦合 [Yang 2020, pp. 2-5]。
2. **PD模型假设**: 基于连续体假设，每个材料点的邻域成员在变形过程中保持不变；损伤是材料响应的一部分，裂纹萌生和扩展自发进行；断裂准则为临界能量密度准则 [Yang 2020, pp. 5-6]。
3. **热边界**: 模拟辐射热处理对应于实验室的炉膛加热，其中热交换主要由辐射主导，并使用Stefan-Boltzmann方程描述 [Yang 2020, pp. 5-6]。
4. **加载条件**: 单轴压缩模拟采用0.1 m/s的加载速率进行准静态加载 [Yang 2020, pp. 7-8]。

## Key Variables / Parameters
- **离散化参数**: 材料点间距 `Δx`，近场范围 (horizon) `δ`，非局部比率 `m` (= `δ/Δx`) [Yang 2020, pp. 6-7] [Yang 2020, pp. 8-10]。
- **力学参数**: 材料密度 `ρ`, 弹性模量 `E`, 泊松比 `υ`, 断裂能 `G₀` [Yang 2020, pp. 7-8]。
- **热学参数**: 未从索引片段中确认。
- **断裂参数**: 能量密度 `ξ`，临界能量密度 `ξ_c` [Yang 2020, pp. 5-6]。
- **响应指标**: 峰值强度 `σ_c`，峰值应变 `ε_1c`，损伤度 `φ` [Yang 2020, pp. 8-10]
- **结构变量**: 预制裂隙的倾角 [Yang 2020, pp. 1-2]。

## Reusable Claims
- **Claim 1**: 在利用常规状态近场动力学（OSB-PD）模拟脆性岩石断裂时，为了获得准确的裂纹路径并避免非物理的微裂纹，非局部比率`m`不应小于3。例如，当采用`m=3`、`δ=2.4 mm`的离散化参数时，可以准确再现花岗岩中预制裂隙尖端的裂纹扩展路径，而`m=2`则会在应力-应变曲线中引入振荡并产生虚假微裂纹 [Yang 2020, pp. 8-10]。该结论基于对含30°裂隙花岗岩的单轴压缩模拟校准。
- **Claim 2**: 对于二维线弹性脆性岩石的OSB-PD断裂模拟，采用临界能量密度准则（`ξ_c = 3G₀ / h³`）可以准确地再现宏观力学行为（如峰值强度、峰值应变）。作者通过将校准后的断裂能 `G₀=50 J/m²` 的模拟结果与实验数据进行对比，验证了该准则的有效性 [Yang 2020, pp. 5-8]。该论断适用于所测试的花岗岩材料。
- **Claim 3**: 基于连续体假设的近场动力学模型无法捕捉到需要物理材料分离和滑动摩擦的裂纹行为。具体体现为，模型无法模拟出实验观察到的反剪切裂纹，进而导致模拟的峰后响应表现出不真实的延性特征。因此，在需要精确复现依赖于摩擦的裂纹模式时，该模型存在根本性限制 [Yang 2020, pp. 5-6] [Yang 2020, pp. 8-10]。

## Candidate Concepts
- [[Peridynamics]]
- [[Thermal cycling treatment]]
- [[Granite fracture]]
- [[Heterogeneity]]
- [[Critical energy density criterion]]
- [[Uniaxial compression]]
- [[Crack propagation]]

## Candidate Methods
- [[Fully coupled ordinary state-based peridynamics]]
- [[m-convergence and δ-convergence tests]]
- [[Shuffle algorithm for heterogeneity]]
- [[Radiation boundary condition (Stefan-Boltzmann law)]]
- [[Uniaxial compression simulation]]
- [[Parameter calibration through experimental comparison]]

## Connections To Other Work
- **数值方法比较**: 文中在引言部分提到了多种处理断裂问题的方法，包括用于模拟动态裂纹的扩展有限元法 ([[extended finite element method]] / XFEM) [Wei and Chen, ref. 13]、损伤粒子法 ([[damage particle method]]) [Wei and Chen, ref. 14]、以及研究热震断裂的相场法 ([[phase field fracture method]]) [refs. 17-19]。近场动力学方法的提出，旨在解决这些基于传统连续介质力学的方法在处理裂纹萌生、扩展和分叉问题时仍需外部准则或技术（如重划网格）的缺点 [Yang 2020, pp. 2-2]。
- **热力学耦合框架**: 文中提及了基于连续损伤力学的热力学框架 [Zhu and Arson, ref. 16]，用于耦合温度与应力对岩石裂纹开闭的影响。本文采用的PD全耦合方法与这些基于经典连续介质的方法（[[continuum damage mechanics]] / CDM）在理论上形成补充，其核心区别在于PD的非局部积分方程形式和损伤的自然萌生特性 [Yang 2020, pp. 2-2]。
- **从主题上连接**: 该研究可以从主题上连接到 [[fracture reservoir]]、[[enhanced geothermal system]] 和 [[disposal of high-level radioactive waste]] 等应用领域，因为其核心问题“热-力耦合作用下的裂隙岩体力学响应”是这些地下工程项目的关键科学问题。

## Open Questions
- 如何改进或修正现有的PD断裂模型，以准确捕捉花岗岩等脆性材料在压缩载荷下的反剪切裂纹 (anti-shear cracks) 以及更真实的峰后脆性破坏行为？ [Yang 2020, pp. 8-10]
- 索引片段中未确认模型在不同热循环次数、不同冷却方式或更高温度条件下的模拟表现如何。
- 未从索引片段中确认将提出的非均质性建模方法应用于多矿物相互作用导致的微裂纹网络演化时，其定量化精度如何。

## Source Coverage
本页面基于提供的16个索引片段，覆盖范围集中在论文的摘要、引言（方法背景）、方法论核心部分（全耦合PD方程、损伤与失效准则、数值实现）、模型验证与参数校准以及部分数值算例。由于是索引片段，缺失了论文中“第5节 单裂隙花岗岩热循环处理后压缩模拟”的详细结果与讨论、以及“第6节 结论”的全部内容。这导致对核心研究问题——“热循环与裂隙倾角的组合效应”——的直接证据和具体发现缺失，本页面的相关结论仅能基于引言中的概括性陈述和校准部分的观察。关于热循环引起的微裂纹萌生过程的具体模拟结果也未能从片段中直接获得。
