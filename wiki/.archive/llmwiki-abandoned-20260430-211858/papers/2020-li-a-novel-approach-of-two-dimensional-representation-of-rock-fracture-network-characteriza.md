---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-li-a-novel-approach-of-two-dimensional-representation-of-rock-fracture-network-characteriza"
title: "A Novel Approach of Two-Dimensional Representation of Rock Fracture Network Characterization and Connectivity Analysis."
status: "draft"
source_pdf: "data/papers/2020 - A novel approach of two-dimensional representation of rock fracture network characterization and connectivity analysis.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Li, Wei, et al. \"A Novel Approach of Two-Dimensional Representation of Rock Fracture Network Characterization and Connectivity Analysis.\" *Journal of Petroleum Science and Engineering*, vol. 184, 2020, 106507, doi:10.1016/j.petrol.2019.106507."
indexed_texts: "11"
indexed_chars: "50955"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:03:42"
---

# A Novel Approach of Two-Dimensional Representation of Rock Fracture Network Characterization and Connectivity Analysis.

## One-line Summary
本文提出一种基于分形与拓扑几何的二维裂缝网络连通性数值表征方法，并分析分形维数、裂缝组数与组间夹角对连通性的影响 [Li 2020, pp. 1-1]。

## Research Question
如何有效表征天然裂缝网络的连通性，并系统量化裂缝组分形维数、裂缝组数量及组间夹角对二维裂缝网络连通性的影响？ [Li 2020, pp. 1-1]

## Study Area / Data
- **方法验证与展示**：通过生成具有一定随机几何特性的裂缝网络进行数值模拟分析 [Li 2020, pp. 5-8]。
- **案例应用**：以四川南部龙马溪组页岩露头为实例，应用所提方法分析天然裂缝分布与连通性。该露头主要发育水平、垂直及倾斜三组节理面，裂缝长度多分布在1m至1.5m范围，呈具有一定偏度的正态分布 [Li 2020, pp. 11-11]。
- **模拟参数**：案例模拟中设置了三组裂缝：水平缝65条，最大长度50，分形维数1.7；垂直缝34条，最大长度50，分形维数1.6；倾斜缝15条，最大长度50，分形维数1.6，倾角30° [Li 2020, pp. 10-11]。总共进行了22组系统数值模拟以全面分析连通性特征 [Li 2020, pp. 8-10]。

## Methods
1. **分形描述模型**：基于分形几何理论，建立了裂缝尺寸与裂缝数量的分形描述模型，用于生成符合特定分形维数的裂缝分布 [Li 2020, pp. 1-1, 2-3]。文中给出了裂缝累计长度与数量随尺寸分布的分形关系式：N(r)α(r_max/r)^(DR/2) [Li 2020, pp. 2-3]。
2. **裂缝方位模拟**：采用 **Fisher分布**（Fisher, 1953）生成裂缝组的方位，该分布已被广泛验证可用于表征裂缝组的优势方向 [Li 2020, pp. 2-3]。
3. **拓扑分析**：将二维裂缝相交产生的节点分类为O、V、Y、X、OV、OX、LW七种类型，通过统计各类节点数量计算网络拓扑参数，如总节点数、连通节点数和分支数，以此表征连通性。其中，O型节点代表不连通节点，其余为连通节点 [Li 2020, pp. 3-5]。
4. **连通性指标**：定义了多个拓扑参数，包括总节点数（Ns = No + Nv + Ny + Nx + Nov + Nox + Nlw）、连通节点数（Nc = Nv + Ny + Nx）以及裂缝分支总数。同时，引入分支平均连通性（Cb）作为量化指标 [Li 2020, pp. 3-8]。
5. **数值模拟流程（MCS）**：通过MATLAB编译了蒙特卡洛模拟程序，基于未指明的PDF模型生成随机裂缝几何，并在假设裂缝不重合、无交叉点的前提下，识别节点、统计分支与节点信息来分析连通性。每组算例模拟50次以求取稳定的平均值 [Li 2020, pp. 5-10]。

## Key Findings
1. **裂缝网络连通性的三大敏感因素**：裂缝连通性对分形维数、裂缝组数和裂缝组间的夹角都非常敏感 [Li 2020, pp. 1-1]。
2. **分形维数与连通性呈负相关**：随着分形维数的增大，裂缝网络连通性变差 [Li 2020, pp. 1-1, 8-10]。节点数量与分形维数的关系遵循幂律函数 [Li 2020, pp. 8-10]。
3. **裂缝组数与组间夹角与连通性呈正相关**：随着裂缝组数和组间夹角的增加，网络连通性变好 [Li 2020, pp. 1-1]。
4. **最优裂缝组间夹角**：当两组裂缝夹角为90°时，裂缝节点的平均总数达到最大值，而裂缝分支平均数达到最小值 [Li 2020, pp. 10-11]。当夹角为0°（平行）时，网络无连通节点，所有节点均为O型 [Li 2020, pp. 10-11]。
5. **连通性由关键节点主导**：裂缝网络的连通性主要由V型、Y型和X型等连通节点控制，其中X型节点的占比通常高于V型和Y型节点 [Li 2020, pp. 8-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 裂缝连通性对分形维数、裂缝组数和组间夹角高度敏感 | Li 2020, pp. 1-1 | 二维裂缝网络数值模拟 | 三大核心结论之首 |
| 分形维数增大，裂缝连通性变差 | Li 2020, pp. 1-1, 8-10 | 基于MCS算法的22组模拟 | 节点数与分形维数呈幂律关系 |
| 裂缝组数和组间夹角增加，连通性变好 | Li 2020, pp. 1-1 | 二维裂缝网络数值模拟 | 三大核心结论之三 |
| 两组裂缝夹角为90°时，总节点平均数最大，分支平均数最小 | Li 2020, pp. 10-11 | 夹角从0°到180°变化模拟 | 存在最优连通角度 |
| 裂缝网络连通性主要由V、Y、X型连通节点控制 | Li 2020, pp. 8-10 | 两组和三组裂缝网络模拟 | X型节点占比通常最高 |

## Limitations
- 本研究聚焦于二维裂缝网络表征，未从索引片段中确认三维裂缝网络特性。
- 数值模拟基于蒙特卡洛算法，每次生成随机结果，需多次模拟（50次）求平均值以确保稳定性 [Li 2020, pp. 8-10]。
- 模型假设所有裂缝不重合且没有交叉点 [Li 2020, pp. 5-8]。
- 文中提及Fisher分布仅用于计算裂缝平均倾角，但未说明生成特定Fisher分布方向的具体方法 [Li 2020, pp. 2-3]。
- 实例分析仅针对一个特定页岩露头（川南龙马溪组），其普适性未从索引片段中确认 [Li 2020, pp. 11-11]。

## Assumptions / Conditions
- **模型假设**：模拟生成的裂缝网络中，裂缝互不重合，且不存在交叉点 [Li 2020, pp. 5-8]。
- **稳定结果条件**：为保证节点数据计算的稳定性，每组数值算例被模拟50次并取平均值 [Li 2020, pp. 8-10]。
- **方位分布**：裂缝组的方位遵循Fisher分布 [Li 2020, pp. 2-3]。
- **尺寸-数量关系**：裂缝尺寸与数量之间被假定遵从特定的分形分布规律 [Li 2020, pp. 2-3]。
- **拓扑不变性**：裂缝节点的类型不随样本空间和尺度的变换而改变，是拓扑分析的基础 [Li 2020, pp. 3-5]。

## Key Variables / Parameters
- **输入/控制参数**：分形维数（`DRi`）、裂缝组数（`m`）、裂缝组间夹角、裂缝尺寸（`rmin`, `rmax`）、裂缝数量（`Ni`）、裂缝组方位（倾角）[Li 2020, pp. 1-2, 2-3, 5-8]。
- **拓扑输出参数**：各类节点数（`No`, `Nv`, `Ny`, `Nx`, `Nov`, `Nox`, `Nlw`）、总节点数（`Ns`）、连通节点数（`Nc`）、裂缝分支总数、分支平均连通性（`Cb`）[Li 2020, pp. 3-5]。
- **节点类型**：O型、V型、Y型、X型、OV型、OX型、LW型 [Li 2020, pp. 3-5]。

## Reusable Claims
1. **Claim**：在二维裂缝网络中，裂缝连通性随分形维数的增大而变差，节点数与分形维数之间服从幂律函数关系。**Condition**：该关系在基于分形理论的MCS数值模拟下成立，用于生成裂缝网络时已知其分形维数。**Evidence**: [Li 2020, pp. 8-10]。**Limitation**: 关系在二维模型及文中设定的参数范围内得出。
2. **Claim**：增加裂缝组数和组间夹角可以有效改善裂缝网络的连通性。**Condition**：适用于基于分形分布生成的二维多组裂缝网络。**Evidence**: [Li 2020, pp. 1-1]。**Limitation**: 只研究了二组和三组裂缝，更多组数的影响未确认。
3. **Claim**：对于两组相交裂缝，其最优连通角度为90°，此时连通节点总数最大。当夹角为0°时，网络完全由不连通的O型节点组成。**Condition**：此结论在裂缝网络二维模拟中得出，裂缝组遵循Fisher分布。**Evidence**: [Li 2020, pp. 10-11]。**Limitation**: 仅讨论了两组裂缝夹角变化的情况。
4. **Claim**：裂缝网络的连通性主要由X型、Y型和V型等连通节点控制，其中X型节点的比例通常最大。**Condition**：在排除了OV、OX、LW型复合节点的简化网络中成立。**Evidence**: [Li 2020, pp. 3-5, 8-10]。**Limitation**: 节点类型的分布可能受裂缝生成算法和参数影响。

## Candidate Concepts
- [[Fracture network connectivity]]
- [[Fractal dimension]]
- [[Topological geometry in fractures]]
- [[Fracture node types (O, V, Y, X)]]
- [[Stimulated reservoir volume (SRV)]]
- [[Fractured reservoir characterization]]
- [[Discrete Fracture Network (DFN)]]
- [[Fisher distribution]]

## Candidate Methods
- [[Fractal geometry-based fracture modeling]]
- [[Monte Carlo Simulation (MCS) for fracture networks]]
- [[Topological analysis of fracture networks]]
- [[Fracture node counting and classification]]
- [[Fisher distribution for orientation generation]]

## Connections To Other Work
- 本研究继承了前人关于裂缝网络分形特征的研究，引用了分形维数与储层渗透阈值、流动及传导特性敏感性的相关研究（Zhang et al., 1994; Doughty and Karasaki, 2002）[Li 2020, pp. 1-2]。
- 研究动机基于仅约20%的裂缝对总流动有贡献、孤立裂缝导致流动非均匀性的认识（Bear et al., 1993a; Li et al., 2018b）[Li 2020, pp. 1-2]。
- 裂缝方位模拟采用已被广泛使用的Fisher分布 (Cacas et al., 1990; Lee et al., 1995) [Li 2020, pp. 2-3]。
- 可从主题上与[[Discrete Fracture Network (DFN) Modeling]]、[[Percolation theory in fractured media]]等概念和方法进行连接。

## Open Questions
- 本方法在三维裂缝网络中的适用性和表现如何？未从索引片段中确认。
- 研究中生成的裂缝网络是否考虑了裂缝的空间相关性或成簇现象？未从索引片段中确认。
- 龙马溪组露头实例分析的定量连通性结果与模拟参数的对应关系细节未从索引片段中确认。
- 除了分形维数、组数和夹角，其他潜在影响连通性的因素（如基质孔隙度、裂缝开度、填充状态）是否被纳入模拟？未从索引片段中确认。

## Source Coverage
本页依据了标注为[Li 2020, pp. 1-1]至[Li 2020, pp. 11-11]的共11个索引片段。片段覆盖了论文的标题、作者信息、摘要、引言、方法模型、拓扑参数定义、数值模拟流程、主要结果分析及案例应用研究等大部分章节。覆盖面较广，但部分公式推导、图表数据细节和讨论的完整性可能受限。文章结论部分的完整论述未完全包含在片段中。
