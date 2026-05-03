---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-tong-meg3d-an-open-source-software-for-dfn-model-and-3d-numerical-manifold-elements-generat"
title: "MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation."
status: "draft"
source_pdf: "data/papers/2024 - MEG3D——An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Tong, Defu, et al. \"MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.\" *Computers and Geotechnics*, vol. 172, 2024, 106383, doi:10.1016/j.compgeo.2024.106383."
indexed_texts: "16"
indexed_chars: "75916"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:12:07"
---

# MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.

## One-line Summary
MEG3D 是一个基于 C++ 开发的开源、快速、轻量且用户友好的交互式前处理软件，用于为三维数值流形方法（3D-NMM）及其他块体类数值方法生成离散块体系统和数值模型 [Tong 2024, pp. 1-2]。

## Research Question
由于几何描述复杂且缺乏可靠的三维接触算法，三维数值流形方法（3D-NMM）的发展长期面临挑战。本研究试图解决其前处理难题，开发一个能够集成几何识别、裂隙网络生成、结构化有限数学网格划分、块体切割及数值流形单元生成的高效工具 [Tong 2024, pp. 1-2] [Tong 2024, pp. 3-4]。

## Study Area / Data
未从索引片段中确认具体的工程场地或地理区域。论文通过多个典型算例来验证软件鲁棒性、效率和精度，包括曲线块切割、离散裂隙网络（DFN）模型、土石混合体边坡、隧道表面以及不同截面梁在点载荷下的响应 [Tong 2024, pp. 3-4]。

## Methods
MEG3D 的开发与实现方法如下：

- **核心算法**：
  - **块体系统构建**：采用块体分区方法，并基于边界表示法（B-rep）描述子块。使用顶点、有向边、有向环、有向面和有向体五级结构表征块体，并通过拓扑检查和体积检查（Eq. (1) ~ (3)）确保块体准确性 [Tong 2024, pp. 4-5]。
  - **离散裂隙网络（DFN）建模**：使用多边形表征不连续面（将圆盘形裂隙等价于增加顶点数的多边形）。表征参数包括倾角、倾向、半径、间距、迹长和中心坐标（x0, y0, z0）。通过局部和全局坐标系转换（Eq. (4)）实现裂隙生成 [Tong 2024, pp. 5-7]。通过找两面交线的有效线段（Eq. (6) & (7)）及最大角度原理搜索面和块体环，构建含裂隙网络的块体系统 [Tong 2024, pp. 7-8]。
  - **数值流形单元（MEs）生成**：首先根据物理域范围自适应生成结构化的正交六面体数学网格（图 17）。然后，仅对与物理面（如节理、边界、材料界面）相交的数学网格执行块切割操作以生成流形块；如果一个数学网格不与任何物理面相交且其中心在物理域内，则自动转换为流形块，以提高效率 [Tong 2024, pp. 9-11]。

- **软件架构与实现**：
  - **编程策略**：采用高度模块化、可移植性强的 C++ 新策略 [Tong 2024, pp. 1-2]。
  - **软件架构**：包含三个独立模块：`C++ Core`（计算核心）、`Visualization`（基于 OpenGL 开发实现跨平台可视化）和 `Controller`（基于跨平台 Qt 框架开发，用于控制人机交互和模型操作）（图 13 & 14）[Tong 2024, pp. 8-9]。
  - **数据结构**：基于面向对象编程（OOP）策略，所有数据和操作封装为类。顶层类包括 `CGeometryFileIO`、`CGeometry3D` 和 `CManifoldElement`（图 15a）[Tong 2024, pp. 9-11]。

## Key Findings
- MEG3D 成功生成了曲线块切割、DFN 模型、土石混合体边坡和复杂形状几何体等验证算例，表明该软件鲁棒、高效且用户友好 [Tong 2024, pp. 1-2]。
- MEG3D 不仅可为 3D-NMM 生成模型，还能为离散元法（DEM）、非连续变形分析（DDA）等基于块体的数值方法生成模型，可作为一个通用前处理程序 [Tong 2024, pp. 1-2]。
- 采用了一种新的块切割优化算法，仅需对与物理面相交的数学网格执行块切割操作，位于物理域内部且未与任何物理面相交的数学网格将自动转换为流形块，从而显著提升了生成效率 [Tong 2024, pp. 9-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| MEG3D 是一个快速、轻量且用户友好的交互式软件，用于生成 3D-NMM 数值模型。 | [Tong 2024, pp. 1-2] | 基于 OpenGL 和 Qt 开发。 | 作为前处理工具。 |
| 软件能处理曲线块切割、DFN 模型、土石混合体边坡等，证明其鲁棒、高效、用户友好。 | [Tong 2024, pp. 1-2] | 包含多个验证算例。 | 还可用作 DEM, DDA 预处理器。 |
| 块体系统构建采用 B-rep 方法，通过拓扑检查和体积检查（Eq. 1-3）保证块体正确性。 | [Tong 2024, pp. 4-5] | 基于有向定理。 | 五级结构：顶点，有向边，有向环，有向面，有向体。 |
| 裂隙相交算法通过计算有效线段（Eq. 6, 7）来确定有效交线。 | [Tong 2024, pp. 7-8] | 应用于 3D 裂隙网络。 | 使用最大角度原理搜索环和块体。 |
| 软件架构包含 C++ Core, Visualization (OpenGL), Controller (Qt) 三个独立模块，具有高兼容性和可移植性。 | [Tong 2024, pp. 8-9] | 用于保障跨平台兼容性。 | Controller 依赖跨平台 Qt 框架。 |

## Limitations
- 索引片段未明确提及软件在处理特大尺度或极高复杂度裂隙网络时的性能瓶颈。
- 索引片段未提及该软件在接触算法处理方面的能力，但论文背景指出了“缺乏可靠的 3D 接触算法是 3D-NMM 发展的长期挑战” [Tong 2024, pp. 1-2]。
- 软件中使用的 B-rep 方法在构建具有复杂相交关系的块体系统时，可能存在拓扑搜索效率问题，但具体限制未从索引片段中确认。

## Assumptions / Conditions
- **数学模型**：3D-NMM 采用双覆盖系统（数学模型覆盖和物理覆盖），并要求数学覆盖始终大于或等于计算区域 [Tong 2024, pp. 3-4]。
- **裂隙表征**：在小尺度（IV～V级）不连续面建模时，假设其可通过统计数据和概率函数（如蒙特卡洛方法）随机生成，且使用多边形等效圆盘模型 [Tong 2024, pp. 5-7]。
- **块体分区**：块体系统构建基于块体分区方法，假设一个完整块体被不连续面（裂隙）切割成多个子块，所有子块的集合构成块体系统 [Tong 2024, pp. 4-5]。

## Key Variables / Parameters
- **裂隙几何参数**：倾角（α）、倾向（β）、半径（r）、间距（d）、迹长（L）和中心坐标（x0, y0, z0）[Tong 2024, pp. 5-7]。
- **坐标系转换关系**：Eq. (4)，用于局部坐标系与全局坐标系之间的变换 [Tong 2024, pp. 5-7]。
- **裂隙交线方向向量**：由两裂隙法向量的叉积计算，Eq. (6) [Tong 2024, pp. 7-8]。
- **裂隙交线上点排序依据**：基于点间向量在交线方向上的投影长度，Eq. (7) [Tong 2024, pp. 7-8]。

## Reusable Claims
- **Claim 1**: 在 NMM 前处理中，为了提高数值流形单元生成效率，可仅对与物理面（边界、节理、材料界面）相交的数学网格执行块切割操作，而将中心位于物理域内部且不与任何物理面相交的数学网格直接转换为流形块。该方法依据 [Tong 2024, pp. 9-11]，其有效性已在 MEG3D 软件中得到验证。
- **Claim 2**: 构建三维离散裂隙网络时，可以使用多边形（尤其是凸多边形）来表征不连续面，因为其在分析相交关系时比椭圆更简便。圆盘形裂隙可通过增加顶点数来等价，这种设定下的模型参数包括倾角、倾向、半径等六个 [Tong 2024, pp. 5-7]。
- **Claim 3**: MEG3D 采用的 C++ 软件架构，将计算核心、基于 OpenGL 的可视化模块和基于 Qt 的控制器模块独立开来，可以作为一种实现数值模拟软件跨平台兼容性和高模块化的 C++ 编程策略 [Tong 2024, pp. 8-9]。

## Candidate Concepts
- [[Numerical Manifold Method (NMM)]]
- [[Dual Cover System]]
- [[Block System (Rock Mechanics)]]
- [[Discrete Fracture Network (DFN)]]
- [[Boundary Representation (B-rep)]]
- [[Mathematical Cover (MC)]]
- [[Physical Cover (PC)]]
- [[Manifold Element (ME)]]
- [[Block Cutting Analysis]]

## Candidate Methods
- [[OpenGL-based Visualization]]
- [[Qt Framework for GUI]]
- [[Object-Oriented Programming (OOP) Strategy]]
- [[Adaptive Mesh Generation]]
- [[Monte-Carlo Method]]
- [[Block Partition Method]]
- [[Constructive Solid Geometry (CSG)]]

## Connections To Other Work
- **非连续变形分析 (DDA) 和 离散元法 (DEM)**：MEG3D 不仅为 3D-NMM 生成模型，还可以作为 DDA 和 DEM 等块体类数值方法的通用前处理器 [Tong 2024, pp. 1-2]。这两种方法与 NMM 同属于解决不连续介质问题的数值方法。
- **有限元-离散元法 (FDEM)**：论文在引言中对比了 FDEM 和 NMM，指出 FDEM 使用零厚度节理单元和显式解法，而 NMM 使用双覆盖系统和隐式解法，具有更高精度并能在统一框架下自然处理连续-非连续问题 [Tong 2024, pp. 2-3]。
- **裂隙网络生成：Baecher 模型与 Zhu 的方法**：MEG3D 中使用了多边形而非传统的圆盘模型（Baecher et al., 1977）来表征裂隙，理由是凸多边形在分析相交时更简便 [Zhu et al., 2022, as cited in Tong 2024, pp. 5-7]。软件中的块体识别与系统构建算法，可参考 [Zhang et al., 2020, as cited in Tong 2024, pp. 7-8]。

## Open Questions
- MEG3D 生成的三维数值模型在不同加载和接触条件下的计算精度验证，除了一个梁的算例外，其他更复杂工况的验证情况未从索引片段中确认。
- MEG3D 与其他主流 NMM 或 DEM 前处理软件（如 Neper, Gmsh）在性能和功能上的量化对比，未从索引片段中确认。
- 软件如何处理和优化特大型（例如，包含数十万条裂隙）的 DFN 模型，其算法效率和内存管理策略，未从索引片段中确认。

## Source Coverage
本页依据 16 个索引片段中的 10 个片段编写，覆盖了论文的摘要、引言、方法论（双覆盖与块系统、软件架构、算法实现）和部分验证章节。信息主要集中于方法描述和软件功能声明。具体实验结果数据、与其它软件的详细对比分析、以及结论章节的完整内容可能缺失，因为这些部分未在提供的索引片段中体现。
