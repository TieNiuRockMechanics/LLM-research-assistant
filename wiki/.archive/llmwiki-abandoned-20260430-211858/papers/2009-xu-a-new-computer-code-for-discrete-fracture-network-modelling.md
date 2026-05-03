---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2009-xu-a-new-computer-code-for-discrete-fracture-network-modelling"
title: "A New Computer Code for Discrete Fracture Network Modelling."
status: "draft"
source_pdf: "data/papers/2010 - A new computer code for discrete fracture network modelling.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Xu, Chaoshui, and Peter Dowd. \"A New Computer Code for Discrete Fracture Network Modelling.\" *Computers & Geosciences*, 2009, doi:10.1016/j.cageo.2009.05.012. Accessed 2026."
indexed_texts: "10"
indexed_chars: "45862"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T17:49:32"
---

# A New Computer Code for Discrete Fracture Network Modelling.

## One-line Summary
Xu 和 Dowd 开发了 FracSim3D，一款使用标记点过程（MPP）进行二维与三维随机岩石裂隙模拟的综合软件包，并提供平面、窗口、扫描线等多种虚拟采样与统计分析工具 [Xu 2009, pp. 1-1].

## Research Question
如何开发一个综合性的计算机代码，以整合多种点过程模型和虚拟采样工具，实现对二维和三维离散裂隙网络（DFN）的随机模拟与验证？ [Xu 2009, pp. 1-1]

## Study Area / Data
未从索引片段中确认。

## Methods
该软件 FracSim3D 的核心方法基于标记点过程（MPP），其中裂隙位置由一个点过程建模，裂隙属性被视为与点相关的“标记” [Xu 2009, pp. 2-3]. 其方法主要包括：

-   **模拟裂隙位置**：提供了四种点过程模型 [Xu 2009, pp. 2-3]：
    -   **齐次泊松模型**：生成具有完全空间随机性（CSR）的点模式，其点位在给定区域内独立且均匀分布，区域内点数遵循泊松分布 [Xu 2009, pp. 2-3].
    -   **非齐次模型**：通过一个与位置相关的强度函数 λ(X) 控制点位密度。软件支持以网格文件导入的非参数模型和通过文本编辑器输入函数表达式的参数模型 [Xu 2009, pp. 3-4].
    -   **集群点过程模型**：又称父代-子代模型，首先生成父代点，然后围绕每个父代点，根据特定概率分布生成子代点（裂隙） [Xu 2009, pp. 4-5]. 软件通过使用周期性边界条件来处理模拟区域边缘问题 [Xu 2009, pp. 5-6].
    -   **Cox 过程模型**：被视为前三种模型的泛化，其强度函数 L(X) 既是位置依赖的，又是随机的，即引入了随机元素来驱动非齐次泊松过程 [Xu 2009, pp. 5-6].
-   **生成裂隙**：将模拟点作为裂隙中心点，通过蒙特卡洛模拟从预设的概率密度函数（PDF）中抽取裂隙的几何参数（尺寸和方向）。在3D模拟中，裂隙形状假设为椭圆形；在2D中则假设为直线 [Xu 2009, pp. 6-7].
-   **模拟额外裂隙属性**：在生成几何形态后，可通过蒙特卡洛采样，为裂隙赋予额外的物理属性（如渗透率或粗糙度），软件支持的分布类型包括均匀、正态、指数、对数正态和非参数分布。最多可添加五种不同属性 [Xu 2009, pp. 7-8].
-   **虚拟采样**：模拟真实数据采集过程，提供了三种采样工具 [Xu 2009, pp. 7-8]：
    -   平面采样：利用虚拟平面与3D裂隙网络相交，提取迹线。
    -   窗口采样：在生成的2D迹线图上设定窗口，分析窗口内迹线的长度和方位。
    -   扫描线采样：在模拟迹线上进行采样，分析迹线间距。
-   **统计与可视化工具**：软件提供直方图分析、概率图、玫瑰花图和半球投影等统计工具，用于分析生成裂隙和采样数据的属性与方向 [Xu 2009, pp. 1-2].

## Key Findings
-   该软件综合集成了多种随机模型和采样工具，为裂隙网络的模拟提供了一个统一的平台 [Xu 2009, pp. 1-1].
-   通过案例研究验证，FracSim3D 的模拟结果能够与理论预测模型相吻合。在一个假设裂隙为平行圆形且采样平面与之垂直的案例中，利用该软件模拟的迹长分布与 Warburton (1980) 提出的理论模型一致，并且模拟平均值紧密遵循理论预测模型 [Xu 2009, pp. 9-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| FracSim3D 的模拟迹长分布与理论预测模型吻合。 | [Xu 2009, pp. 9-10] | 裂隙为均匀分布的平行圆形盘，采样平面垂直于裂隙面，分别采用负指数和对数正态分布作为裂隙尺寸分布 g(s)。 | 验证了软件在特定条件下模拟结果的准确性。 |

## Limitations
-   该版本的软件（FracSim3D）未包含裂隙属性之间的相关性模型，例如尺寸与厚度 [Xu 2009, pp. 7-8].
-   3D裂隙的形状被固定假设为椭圆形（在特定验证案例中被简化为圆盘），2D裂隙被假设为直线，这可能无法完全代表自然界中复杂多变的裂隙几何形态 [Xu 2009, pp. 1-2, 7-8].
-   点过程模型和属性分布的选取需要用户根据实际地质知识预先定义，软件本身不提供自动推断或选择最优模型的功能。未从索引片段中确认。
-   未从索引片段中确认软件在处理大规模网络时的计算效率或潜在的性能瓶颈。
-   生成的裂隙网络依赖于对真实三维数据的统计推断，而实际数据常常是有限的、有偏的二维样本，推断过程本身存在不确定性 [Xu 2009, pp. 1-2].

## Assumptions / Conditions
-   **模型假设**：岩石裂隙的形成过程可以由标记点过程（MPP）来描述，即裂隙中心的空间位置与裂隙的几何和物理属性是独立或可分解的 [Xu 2009, pp. 2-3].
-   **几何假设**：在3D模拟中，裂隙被假定为椭圆形平面；在2D模拟中，裂隙被假定为直线段 [Xu 2009, pp. 1-2, 7-8].
-   **地质分类**：通常假设由同一地质活动形成的裂隙具有相似的属性和优势方位，因此在实际应用中，应先对裂隙进行分组再分别建模 [Xu 2009, pp. 1-2].
-   **属性模拟**：额外的裂隙属性（如渗透率）被假定相互独立，且可由用户指定的概率分布（均匀、正态、指数、对数正态或非参数）来描述 [Xu 2009, pp. 7-8].
-   **周期性边界**：在处理集群过程模型时，为保留所有生成的子代点，假设模拟区域（矩形）具有周期性边界，即被视为一个无边缘的环面 [Xu 2009, pp. 5-6].

## Key Variables / Parameters
-   **λ (lambda)**: 点过程的强度参数，在齐次泊松模型中为常数，在非齐次模型中为位置函数 λ(X) [Xu 2009, pp. 2-4].
-   **g(s)**: 裂隙尺寸（2D迹长或3D椭圆轴半径）的概率密度函数 [Xu 2009, pp. 9-10].
-   **f(l)**: 由采样平面揭露的裂隙迹长的概率密度函数 [Xu 2009, pp. 9-10].
-   **PDF for orientation**: 裂隙方向（2D方位角或3D产状）的概率密度函数 [Xu 2009, pp. 6-7].
-   **采样平面参数**：用于定义虚拟采样平面的倾角和倾向 [Xu 2009, pp. 7-8].
-   **裂隙属性分布**：可用于描述额外属性的分布类型及其参数，如正态分布的均值与方差 [Xu 2009, pp. 7-8].

## Reusable Claims
-   **Claim 1**：FracSim3D软件中，齐次泊松点过程的模拟严格遵循完全空间随机性（CSR）的三个性质：区域内点数服从泊松分布、给定点数时点位服从均匀分布，以及在不重叠区域内点数相互独立 [Xu 2009, pp. 2-3]. 适用条件：用户选择“homogeneous Poisson model”作为裂隙位置的生成模型。
-   **Claim 2**：在 FracSim3D 中使用集群点过程模型时，通过应用三维周期性边界条件，可以避免因区域截断导致的边缘数据丢失问题，其具体实现是将超出某一边界的点坐标映射到相对边界 [Xu 2009, pp. 5-6]. 适用条件：模拟区域为矩形/长方体，且用户启用了该边界处理方式。
-   **Claim 3**：Cox 过程模型通过引入一个随机强度函数 L(X) 来驱动非齐次泊松过程，使其不仅能捕捉点密度的空间变化，还能反映其随机性，形式上可以涵盖齐次、非齐次和集群过程等特例 [Xu 2009, pp. 5-6]. 适用条件：需要生成比简单泊松过程更复杂的、具有空间相关性和随机强度变化特征的点模式。
-   **Claim 4**：给定裂隙尺寸分布 g(s) 为负指数或对数正态分布时，FracSim3D对平行圆盘裂隙网络进行垂直平面采样所得的迹长分布 f(l) 的模拟结果，与 Warburton (1980) 的理论推导一致，且多次模拟的平均值紧密追随理论曲线 [Xu 2009, pp. 9-10]. 适用条件：裂隙网络为空间均匀分布的平行圆形裂隙，采样平面严格垂直于裂隙面，且裂隙尺寸足够大。
-   **Claim 5**：FracSim3D 允许对同一裂隙网络进行至多五种额外属性的模拟，这些属性通过蒙特卡洛方法从用户指定的概率分布中独立取样 [Xu 2009, pp. 7-8]. 适用条件：面向需要导出裂隙属性以进行流體流动或力学分析的后续模拟，且暂未考虑属性间的相关性。

## Candidate Concepts
-   [[Discrete Fracture Network (DFN)]]
-   [[Marked Point Process (MPP)]]
-   [[Stochastic Simulation]]
-   [[Spatial Point Process]]
-   [[Monte Carlo Simulation]]
-   [[Fracture Reservoir]]
-   [[Geostatistics]]
-   [[Fracture Geometry]]
-   [[Spatial Correlation]]

## Candidate Methods
-   [[Poisson Process Simulation]]
-   [[Cox Process Simulation]]
-   [[Cluster Point Process Simulation]]
-   [[Virtual Sampling (Scanline, Window, Plane)]]
-   [[Probability Distribution Fitting]]
-   [[Monte Carlo Sampling]]
-   [[Stereographic Projection]]
-   [[Bias Correction in Rock Fracture Surveys]]

## Connections To Other Work
-   **与[[Warburton 1980]]的关系**：本文直接引用了Warburton (1980) 关于裂隙尺寸与迹长分布关系的理论模型，并以此作为验证FracSim3D软件模拟结果的标准 [Xu 2009, pp. 9-10].
-   **与[[Dershowitz and Einstein 1988]]的关系**：本文在引言中提到，使用无限大平面（泊松平面）模拟三维裂隙是一种常见方法，并引用了此文献。
-   **与其他裂隙建模工作的主题连接**：本文的主题是离散裂隙网络的随机建模，可从概念上连接到更广泛的裂隙网络生成、水力学性质模拟、以及裂隙尺寸-迹长曲线反演方法的研究。其他可能的候选概念包括：
    -   [[Enhanced Geothermal Systems (EGS)]]
    -   [[Underground Waste Disposal]]
    -   [[Fracture Size-Trace Length Relationship]]
    -   [[Joint Set Identification]]

## Open Questions
-   该软件如何处理和消除从二维露头数据推断三维裂隙网络时固有的采样偏差（如截断、删失和边缘效应），文中仅提及该问题的重要性，但未详述软件内置的具体校正方法 [Xu 2009, pp. 1-2].
-   对于更复杂的裂隙形状（如多边形），软件的未来版本是否计划增加支持？未从索引片段中确认。
-   软件的计算效率如何？在处理包含数百万条裂隙的大型模型时，其性能是否可接受？未从索引片段中确认。
-   除了文中展示的迹长验证案例，是否有关于裂隙连通性、渗透性等其他关键网络属性模拟精度的验证？未从索引片段中确认。

## Source Coverage
本页依据论文《A New Computer Code for Discrete Fracture Network Modelling》的10个索引片段 [Xu 2009, pp. 1-10] 整理而成。这些片段覆盖了摘要、引言（部分）、核心方法论（四种点过程、裂隙生成、属性模拟、虚拟采样）以及一个验证性案例研究。覆盖较为全面，尤其侧重于方法部分的描述。然而，索引片段中缺少“离散裂隙网络建模的应用背景”的完整讨论，关于软件架构、用户界面、输入输出数据格式、更详细的案例研究结果以及对局限性的更深入讨论等信息可能未能完全覆盖。
