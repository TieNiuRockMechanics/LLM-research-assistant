---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-meng-an-ifs-based-fractal-discrete-fracture-network-for-hydraulic-fracture-behavior-of-rock"
title: "An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass."
status: "draft"
source_pdf: "data/papers/2023 - An IFS-based fractal discrete fracture network for hydraulic fracture behavior of rock mass.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Meng, Qingxiang, et al. \"An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass.\" *Engineering Geology*, vol. 324, 2023, 107247. doi:10.1016/j.enggeo.2023.107247."
indexed_texts: "19"
indexed_chars: "90251"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "83999"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.930727"
coverage_status: "full-index"
source_signature: "297cfc4e4fa0dff92c627589ba6848fd7f8e7fdf"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:15:05"
---

# An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass.

## One-line Summary

基于迭代函数系统（IFS）的分形离散裂隙网络（DFN）生成方法用于模拟岩石水力压裂行为，揭示了注入压力三阶段特征及分形几何对压裂扩展的显著影响。

## Research Question

如何构建一种基于IFS分形插值的二维DFN模型，以准确描述原生裂隙的粗糙几何特征，并模拟其在水力压裂中的流体驱动断裂行为？

## Study Area / Data

研究以广州阳江抽水蓄能电站为背景[Meng 2023, pp. 1-2; pp. 13-14]，该工程最大水头差670 m，静水压力6.70 MPa，动水压力11.08 MPa[Meng 2023, pp. 1-2]。数值模型区域为20 m × 20 m，包含共轭断层型DFN[Meng 2023, pp. 13-14]。岩石基质采用弹性模型，物理力学参数见表3[Meng 2023, pp. 10; 13-14]。初始应力条件为σx=7.5 MPa, σy=9.7 MPa, σz=14.5 MPa，初始孔隙压力6.7 MPa[Meng 2023, pp. 13-14]。注入点为模型中心，注入速率为0.001 m³/s[Meng 2023, pp. 13-14]。

## Methods

### 分形DFN生成方法
- **IFS分形插值**：将初始多段线通过仿射变换生成具有自仿射特征的分形曲线[Meng 2023, pp. 2-4]。关键参数垂直缩放因子d_n控制波动程度；分形维数D与d_n关系由式(7)给出[Meng 2023, pp. 3-4]。三维IFS变换形式为式(8)[Meng 2023, pp. 3-4]。
- **曲线平滑**：采用Douglas–Peucker算法，通过设定垂距阈值T移除短边与冗余点，在保持基本几何形态前提下改善网格质量[Meng 2023, pp. 4-5]。
- **共轭断层转化**：提出分批次线段转化方法，先生成主组分形裂隙，再处理次组，以保证次组裂隙终止于主组的特征[Meng 2023, pp. 5-6]。
- **网格细化**：通过识别并合并短边和小间隙消除畸变单元风险，提升网格质量[Meng 2023, pp. 6-9]。

### 水力压裂模拟框架
- **粘聚区模型**：使用零厚度流动粘聚单元（COH2D4P），结合牵引分离定律（TSL）和损伤演化模拟断裂扩展[Meng 2023, pp. 5-6; pp. 6-9]。
- **流固耦合**：采用CPE4P单元模拟多孔介质变形与渗流，COH2D4P模拟裂隙内流体流动；依据质量守恒和立方定律计算裂隙流体压力[Meng 2023, pp. 5-6]。
- **粘聚单元生成**：通过单元分离、边提取、流动节点合并和网格重构四步，在所有实体单元相邻边插入零厚度粘聚单元[Meng 2023, pp. 9-10]。
- **裂隙属性区分**：将粘聚单元区分为原生裂隙和完整岩石两组，并利用Python脚本按高斯分布随机调整原生裂隙粘聚单元的构成厚度以模拟裂隙开度变化[Meng 2023, pp. 9-10]。
- **验证**：采用KGD问题解析解对数值方法进行验证，模拟的断裂长度、最大开度和注入压力与解析解吻合良好[Meng 2023, pp. 10-13]。

## Key Findings

1. **注入压力三阶段特征**：水力压裂过程中，注入节点孔隙压力依次经历突然上升（阶段A）、快速下降（阶段B）和长期稳定三个阶段[Meng 2023, pp. 14-15]。
2. **分形几何的影响**：相较于线性DFN，分形DFN表现出更低的起裂压力和更长的水力断裂总长度[Meng 2023, pp. 14-15]。当裂隙开度均匀时，分形DFN的断裂长度提升更为显著[Meng 2023, pp. 14-15]。
3. **裂隙开度变异性的影响**：高斯分布的裂隙开度导致更快的压力衰减（A至B点），并降低断裂延伸长度；开度均匀时断裂张口更大[Meng 2023, pp. 14-15]。
4. **网格敏感性**：当近似网格尺寸从0.08 m增至0.16 m，起裂压力差高达17.73 MPa，最终断裂长度差达10.81 m；随着网格细化，断裂路径趋于一致[Meng 2023, pp. 15-18]。
5. **流动路径迂曲度效应**：在相同面积裂隙密度下，分形天然裂隙较线性裂隙导致更长的水力断裂[Meng 2023, pp. 18-19]。IFS缩放因子d_n增大使裂隙面更凹凸，注入压力峰后下降更快，且可能改变断裂扩展方向[Meng 2023, pp. 19-20]。
6. **平滑算法阈值影响**：Douglas–Peucker算法的阈值T变化会改变注入压力曲线和断裂扩展（如T=0.0016 m时起裂压力较低、断裂较长）[Meng 2023, pp. 20-21]。
7. **裂隙开度尺寸影响**：开度尺寸越小，起裂压力越高，整个过程中的断裂总长度也越大[Meng 2023, pp. 20-21]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 注入压力呈现三阶段：突然增加、快速下降、稳定 | Meng 2023, pp. 14-15 | 二维共轭断层分形DFN，注入速率0.001 m³/s，均质弹性岩体，有效应力原理 | 所有模型均表现出此特征 |
| 分形DFN的起裂压力低于线性DFN | Meng 2023, pp. 14-15 | d_n=0.3，均匀或高斯裂隙开度，相同连通性 | 开度非均匀时差异更明显 |
| 均匀裂隙开度下分形DFN的水力断裂长度大于线性DFN | Meng 2023, pp. 14-15 | d_n=0.3，均匀开度0.0002 m | 高斯开度下此趋势减弱 |
| 高斯开度分布下压力从峰值快速下降 | Meng 2023, pp. 14-15 | μ=0.0002 m, σ=0.0002 m | 与均匀开度对比 |
| 随近似网格尺寸由0.08 m增至0.16 m，起裂压力差异达17.73 MPa，最终断裂长度差异10.81 m | Meng 2023, pp. 15-18 | d_n=0.3，均匀开度 | 网格细化后结果收敛 |
| 相同面积裂隙密度下，分形天然裂隙导致更长的水力断裂 | Meng 2023, pp. 18-19 | 模型包含1条、4条或多条连通裂隙，长度、角度和连通性严格一致 | 仅通过迂曲度改变形态 |
| d_n增大使裂隙面变得更凹凸，注入压力峰后下降更快 | Meng 2023, pp. 19-20 | d_n=0, 0.15, 0.30, 0.45, 均匀开度 | 面积裂隙密度也随之增大 |
| 平滑阈值T影响注入压力和断裂路径 | Meng 2023, pp. 20-21 | T=0.0016, 0.0020, 0.0024 m | T=0.0016 m时起裂压力最低 |
| 裂隙开度越小，起裂压力越高，断裂总长度越大 | Meng 2023, pp. 20-21 | 开度值：0.0002, 0.001, 0.002 m | 大尺寸开度改变扩展方向 |

## Limitations

- 本研究的数值模拟框架仅限于二维模型，三维模型因网格生成难度和计算成本尚未实现[Meng 2023, pp. 10-13]。
- 零厚度粘聚单元方法存在网格依赖性，网格尺寸对起裂压力和断裂长度有显著影响，不同网格划分结果需谨慎对比[Meng 2023, pp. 15-18]。
- 模型假设岩石基质为线弹性，未考虑塑性变形或各向异性[Meng 2023, pp. 13-14]。
- 分形DFN的生成过程中，不同d_n值的模型在连通性上存在微小的随机差异，尽管频率极低，可能对对比结果造成潜在干扰[Meng 2023, pp. 5-6]。

## Assumptions / Conditions

- 水力压裂过程基于有效应力原理和Terzaghi固结理论[Meng 2023, pp. 5-6; pp. 13-14]。
- 岩石基质视为弹性多孔介质，变形符合线弹性力学[Meng 2023, pp. 13-14]。
- 裂隙内流体流动遵循立方定律（Poisseuille定律）[Meng 2023, pp. 5-6]。
- 原岩应力场为均匀分布，且初始孔隙压力恒定[Meng 2023, pp. 13-14]。
- 天然裂隙被假设为零厚度，其力学性质通过粘聚单元的牵引分离法则表征[Meng 2023, pp. 6-9]。
- 本征裂隙开度变化服从高斯分布[Meng 2023, pp. 9-10]。

## Key Variables / Parameters

- **IFS缩放因子 d_n**：控制分形曲线的波动程度和分形维数[Meng 2023, pp. 3-4]。
- **分形维数 D**：与d_n满足隐式关系 ∑ |d_n| a_n^{D-1}=1；与节理粗糙度系数JRC的经验关系为 JRC=1000(D-1)[Meng 2023, pp. 3-4]。
- **平滑阈值 T**：决定道格拉斯-普克算法的简化程度[Meng 2023, pp. 4-5]。
- **最小线段阈值 d_min**：用于清理共轭断层交切后的极短线段[Meng 2023, pp. 5-6]。
- **裂隙开度（均匀或高斯分布的均值/方差）**：均匀开度尺寸固定，高斯分布由 μ 和 σ 描述[Meng 2023, pp. 14-15]。
- **网格近似尺寸**：影响计算精度和断裂形态，0.08 m至0.16 m范围测试[Meng 2023, pp. 15-18]。
- **注入速率**：0.001 m³/s[Meng 2023, pp. 13-14]。
- **原岩应力**：σ_x=7.5 MPa, σ_y=9.7 MPa, σ_z=14.5 MPa[Meng 2023, pp. 13-14]。
- **初始孔隙压力**：6.7 MPa（对应约670 m水头）[Meng 2023, pp. 13-14]。

## Reusable Claims

1. **IFS分形插值可生成具有自仿射特征的粗糙裂隙曲线**，其粗糙度由垂直缩放因子d_n唯一控制，且d_n与分形维数D通过式(7)关联，且与JRC存在JRC=1000(D-1)的经验关系。适用条件：二维插值，|d_n|<1。[Meng 2023, pp. 3-4]
2. **Douglas–Peucker算法可通过调整垂距阈值T在保留整体几何的前提下有效平滑分形裂隙**，减少点数以利于网格划分。适用条件：分形曲线由多段直线构成。[Meng 2023, pp. 4-5]
3. **基于IFS的共轭断层DFN生成流程能够保持主次裂隙组的交切关系**，通过分批次转化和端点移动确保次组终止于主组。适用条件：具有明确主次关系的两组裂隙。[Meng 2023, pp. 5-6]
4. **水力压裂过程中注入压力呈现三阶段模式**：应力累积导致突然上升，随后裂隙起裂致使压力快速下降，最后进入渗流平衡的稳定阶段。这是一个高概率的可重复行为，适用于均质弹性体且恒定注入速率的场景。[Meng 2023, pp. 14-15]
5. **在相同裂隙密度和连通性下，分形裂隙模型的最终水力断裂长度大于线性裂隙模型**，表明迂曲的流动路径促进了更远的断裂延伸。条件：裂隙开度均匀时此效应更显著。[Meng 2023, pp. 14-15; 18-19]
6. **零厚度流固耦合粘聚单元（COH2D4P）方法可以模拟二维复杂DFN的水力压裂，但其结果对网格尺寸敏感**。网格越细，断裂路径趋于收敛，因此分析中必须进行网格敏感性检验。适用条件：二维四边形网格，采用CPE4P和COH2D4P单元。[Meng 2023, pp. 9-10; 15-18]
7. **裂隙开度服从高斯分布的模型较均匀开度模型表现出更快的压力衰减和更小的最终断裂长度**，说明开度的非均质性对水力压裂有实质影响。适用条件：静水压力6.7 MPa，注入速率0.001 m³/s。[Meng 2023, pp. 14-15; 20-21]
8. **IFS缩放因子d_n增大不仅增加裂隙粗糙度和面积裂隙密度，还可能导致水力压裂的扩展主方向发生改变**。这意味着在实际工程中，天然裂隙的微细形态会影响宏观水力裂缝走向。适用条件：共轭断层背景，均匀开度。[Meng 2023, pp. 19-20]

## Candidate Concepts

- [[Fractal Discrete Fracture Network]]
- [[Iterated Function System (IFS)]]
- [[Fractal Interpolation]]
- [[Joint Roughness Coefficient (JRC)]]
- [[Fractal Dimension]]
- [[Cohesive Zone Model (CZM)]]
- [[Zero-thickness Cohesive Element]]
- [[Traction Separation Law (TSL)]]
- [[Hydraulic Fracture Propagation]]
- [[Tortuosity of Flow Path]]
- [[Fracture Aperture Variation]]
- [[Conjugate Fault]]
- [[Douglas-Peucker Algorithm]]
- [[Mesh Sensitivity]]

## Candidate Methods

- [[IFS-based Fractal Fracture Generation]]
- [[Douglas-Peucker Polyline Simplification]]
- [[Discrete Fracture Network (DFN) Modeling]]
- [[Cohesive Element Insertion for Hydraulic Fracture]]
- [[Fluid-solid Coupling with Zero-thickness Elements (COH2D4P)]]
- [[KGD Analytical Validation]]
- [[Gaussian Aperture Assignment]]
- [[Advancing Front Mesh Generation]]
- [[PartitionFaceBySketch for Fracture Embedding]]

## Connections To Other Work

- 水力压裂数值模拟框架与Nguyen et al. (2017) 提出的粘聚单元方法一脉相承，本文方法进一步扩展至分形DFN[Meng 2023, pp. 10-13]。
- IFS分形建模理论源于Hutchinson (1981) 和Barnsley (1986) 的工作，本研究将其应用于地质不连续面生成[Meng 2023, pp. 1-2]。
- 裂隙粗糙度与分形维数的关系引用自Turk et al. (1987) 和Carr & Warriner (1987) 提出的JRC-D经验公式[Meng 2023, pp. 2-4]。
- 与传统的光谱方法（如傅里叶变换、POCS）相比，IFS方法具有数学原理简单、易于编程实现和仅需单参数控制的优点[Meng 2023, pp. 1-2]。
- 研究延续了DFN随机生成的传统（Baecher, 1983; Dershowitz & Einstein, 1988），并提出用分形曲线取代直线或平面圆盘的新思路[Meng 2023, pp. 2-3]。

## Open Questions

- **三维推广**：文中明确限于二维模型，三维IFS分形裂隙的网格生成和流固耦合模拟是未来挑战[Meng 2023, pp. 10-13]。
- **连通性控制**：不同d_n值下如何保证分形DFN具有严格相同的裂隙连通性尚待解决[Meng 2023, pp. 5-6]。
- **网格依赖性降低**：当前方法存在明显的网格敏感性，如何减小或消除这一依赖性需要进一步研究[Meng 2023, pp. 15-18]。
- **更复杂的裂隙开度模型**：本研究中开度服从简单的高斯分布，而实际原位应力条件下的开度-应力耦合效应未被考虑[Meng 2023, pp. 9-10]。
- **多物理场耦合**：仅考虑了流-固耦合，未包含温度场或化学场对裂隙扩展的影响[Meng 2023, pp. 22-23]。

## Source Coverage

本文档基于提供的所有19个非空索引片段编写，片段索引覆盖率（按片段数）为100.0%，字符覆盖率为93.07%（共索引约90,251字符，汇编后使用约83,999字符）。所有片段均已处理，未遗漏任何来源内容。索引区块签名：297cfc4e4fa0dff92c627589ba6848fd7f8e7fdf。
