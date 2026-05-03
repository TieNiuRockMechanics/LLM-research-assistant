---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-gao-numerical-simulation-of-diametrical-core-deformation-and-fracture-induced-by-core-drill"
title: "Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling."
status: "draft"
source_pdf: "data/papers/2021 - Numerical simulation of diametrical core deformation and fracture induced by core drilling.pdf"
collections:
  - "zotero new"
citation: "Gao, Guiyun, et al. \"Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling.\" *Arabian Journal of Geosciences*, vol. 15, no. 1, 2021, article 59. doi:10.1007/s12517-021-09378-0. Accessed 2026."
indexed_texts: "9"
indexed_chars: "40291"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:01:50"
---

# Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling.

## One-line Summary
本研究通过ABAQUS数值模拟，分析了岩芯钻取过程中矿物非均质性、微裂纹及断裂对岩芯直径变形的影响，并评估了其对基于岩芯的DCDA地应力测量方法的适用性限制。

## Research Question
矿物组分引起的弹性非均质性如何影响岩芯钻取过程中的直径变形与断裂行为？这些影响如何制约基于弹性均质假设的DCDA地应力测量方法的准确性？

## Study Area / Data
未从索引片段中确认。

## Methods
- **弹性非均质性模拟：** 采用两种方法纳入矿物组分——球状夹杂物法和基于ABAQUS二次开发的随机单元属性法 [Gao 2021, pp. 3-4]。
- **脆性断裂模拟：** 使用ABAQUS/Explicit中的脆性开裂模型（Brittle cracking model），该模型在拉伸应力下允许更详细的裂后响应建模 [Gao 2021, pp. 3-4]。
- **内聚断裂模拟：** 使用牵引-分离内聚力模型（Traction–separation cohesive material law），采用二次名义应力起裂准则预测损伤起始 [Gao 2021, pp. 4-6]。
- **岩芯钻取过程模拟：** 通过移除周围岩体来模拟应力释放，模型施加对称边界条件及水平X与Y方向的应力（如20 MPa和10 MPa）以模拟原位应力场 [Gao 2021, pp. 6-9]。

## Key Findings
- 在弹性均质模型中，数值模拟的岩芯变形结果与DCDA理论公式（公式4）的计算值完全吻合 [Gao 2021, pp. 11-12]。
- 岩芯变形受应力比（S_Hmax/S_hmin）影响，但在均质情况下，模拟得到的直径差（dmax-dmin）与理论值一致；而在非均质岩石中可能不适用 [Gao 2021, pp. 11-12]。
- 矿物组分显著影响应力释放引起的岩芯变形和断裂行为；由于岩石的非均质性，应力释放后会产生残余应力，导致DCDA的均质弹性理论可能不再适用 [Gao 2021, pp. 9-11]。
- 岩芯钻取可引发脆性开裂，微裂纹首先在黑云母矿物周围形成并扩展，且在最小水平主应力方向上延伸 [Gao 2021, pp. 11-12]。
- 局部残余应力可能极高，甚至接近外加应力水平 [Gao 2021, pp. 9-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 弹性均质模拟结果与DCDA理论值完全吻合 | [Gao 2021, pp. 11-12] | 不同应力比（1.0， 1.5， 2.0， 2.5, 3.0）的均质模型 | 验证了DCDA理论在均质材料中的适用性 |
| 岩芯变形U1随石英比率增加而增加，随斜长石比率增加而减小；而U2变形则相反 | [Gao 2021, pp. 9-11] | 非均质模型，考虑了矿物组分的体积比变化 | 表明矿物组分对直径变形有直接影响 |
| 黑云母矿物周围形成微裂纹，裂纹沿最小水平主应力方向扩展 | [Gao 2021, pp. 11-12] | 使用脆性开裂模型，采用随机单元属性法 | 揭示了非均质性引起的应力差异是导致开裂的关键 |

## Limitations
- 索引片段未明确说明模型的尺寸、网格依赖性分析以及计算成本。
- 研究主要基于数值模拟，未从索引片段中确认是否包含实验室物理实验的直接对比验证。

## Assumptions / Conditions
- **本构假设：** 对于脆性开裂模型，假设材料在压缩下为线弹性；对于内聚力模型，使用二次名义应力准则判断损伤起始 [Gao 2021, pp. 4-6]。
- **加载与边界条件：** 模型假设几何形状和载荷关于X和Y轴对称，仅建立四分之一模型进行分析 [Gao 2021, pp. 6-9]。
- **DCDA理论基础：** 基于弹性、均质岩石变形假设 [Gao 2021, pp. 3-4]。
- **理想化缺陷：** 弹性非均质性通过理想化的球状夹杂物或随机单元集合来表征 [Gao 2021, pp. 3-4]。

## Key Variables / Parameters
- **几何/位移变量：** dmax， dmin, d0 （最大、最小、初始直径）, U1 (X方向变形), U2 (Y方向变形) [Gao 2021, pp. 3-4]
- **应力/应变变量：** εmax, εmin （与dmax、dmin对应的应变）, SHmax, Shmin (原位最大、最小水平主应力), 残余应力（S11, S22, Mises应力）[Gao 2021, pp. 3-4] [Gao 2021, pp. 6-9]
- **材料参数：** 弹性模量 (E), 泊松比 (ν), 矿物组分体积比, 破坏应力 (Ts), I型断裂能 (GIC), 直接开裂破坏应变/位移 [Gao 2021, pp. 4-6]
- **模型参数：** 损伤变量 (D), 单元刚度退化变量 (SDEG), 内聚强度 (tno, tso, tto), 临界分离位移 (δn), 断裂能 (Gc) [Gao 2021, pp. 4-6] [Gao 2021, pp. 11-12]

## Reusable Claims
- 在弹性均质条件下，由应力释放导致的岩芯直径差理论值可通过公式 dmax - dmin = d0 * (1+ν)/E * (SHmax - Shmin) 计算，且该理论值与基于移除围岩的数值模拟结果完全一致 [Gao 2021, pp. 3-4] [Gao 2021, pp. 11-12]。
- 岩石中较软弱的矿物（如黑云母，其弹性模量为19.9 GPa）相对于较硬的矿物（如石英，其弹性模量为86.1 GPa），在应力释放过程中会诱发更高的局部拉伸应力，从而成为裂纹萌生的优先位置 [Gao 2021, pp. 6-9] [Gao 2021, pp. 11-12]。
- 岩石的非均质性会在岩芯内部引起不均匀的变形，导致DCDA方法基于均质理论的假设失效，并产生显著的残余应力，影响地应力测量的准确性 [Gao 2021, pp. 9-11]。
- 采用ABAQUS二次开发的随机单元属性法可以精确设计各矿物组分的体积比，但无法控制颗粒尺寸，该方法适用于模拟岩石的弹性非均质特征 [Gao 2021, pp. 3-4]。

## Candidate Concepts
- [[Diametrical Core Deformation Analysis]]
- [[in-situ stress measurement]]
- [[stress release]]
- [[microcracks]]
- [[elastic heterogeneity]]
- [[brittle cracking]]
- [[cohesive fracture model]]
- [[core drilling]]

## Candidate Methods
- [[ABAQUS numerical simulation]]
- [[brittle cracking model]]
- [[cohesive element method]]
- [[random elemental properties method]]
- [[spherical inclusion method]]

## Connections To Other Work
该研究是DCDA方法发展的一部分，其理论基础与数值模拟工作可关联至该领域内其他用于验证和改进DCDA实验与理论的研究 [Gao 2021, pp. 12-13]。具体而言，文中引用了Funato和Ito等人的工作，这些工作包括DCDA方法的新发展、实验室验证，以及适用于深部高温环境的双钻头取芯应力测量方法的实验验证 [Gao 2021, pp. 12-13]。同时，文中的数值模拟方法（如内聚力单元、脆性开裂）可与非均质岩石力学中关于矿物微力学和混合模式断裂的研究相联系 [Gao 2021, pp. 12-13]。

## Open Questions
- 如何修正DCDA方法以消除弹性非均质性、微裂纹和残余应力对地应力测量结果的影响？ [Gao 2021, pp. 12-13]
- 不同生成方法（球状夹杂物 vs. 随机单元属性法）对模拟结果的具体差异和适用性是否得到了充分对比与量化？

## Source Coverage
本页内容基于提供的9个索引片段，覆盖了论文的摘要、引言、方法、主要结果和讨论部分。信息足以概述核心研究内容、数值模拟方法及关键发现。然而，索引片段中未包含研究区域的具体信息、详细的模型构建参数（如几何尺寸、所有加载条件）以及结论部分的完整陈述。部分图表数据（如图2、9、11的具体细节）和所有参考文献列表仅能从片段中部分获取。
