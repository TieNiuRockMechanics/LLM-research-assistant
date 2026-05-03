---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-tong-meg3d-an-open-source-software-for-dfn-model-and-3d-numerical-manifold-elements-generat"
title: "MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation."
status: "draft"
source_pdf: "data/papers/2024 - MEG3D——An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Tong, Defu, et al. \"MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.\" *Computers and Geotechnics*, vol. 172, 2024, 106383, doi:10.1016/j.compgeo.2024.106383."
indexed_texts: "16"
indexed_chars: "75916"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "69703"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.91816"
coverage_status: "full-index"
source_signature: "24f3191a89d8f3a02a2dfeb61b5b076c7fac6b38"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:34:16"
---

# MEG3D —— An Open-Source Software for DFN Model and 3D Numerical Manifold Elements Generation.

## One-line Summary
MEG3D是一款面向三维数值流形法(3D-NMM)及其他基于块体数值方法的开源C++预处理软件，可生成离散裂缝网络(DFN)模型和三维数值流形单元，具备高模块化、实时可视化和用户交互界面。

## Research Question
如何为三维NMM开发一个快速、鲁棒、用户友好的预处理工具，以解决现有工具无法处理复杂几何、节理网络和流形单元自动生成的难题？本文旨在通过开发MEG3D填补这一空白。

## Study Area / Data
本文未指定具体工程场地，而是使用多个典型算例验证软件功能：包含曲面和平面裂缝的地下硐室、带弯曲隧道的边坡、含马蹄形隧道的立方体DFN模型、复杂边坡、土石混合体边坡、龙形几何体、复杂形状机器人、某大型水电工程V形边坡等。几何模型通过Rhino软件生成并导入OBJ/STL文件；利用数字摄影测量技术（Zhao et al., 2020）获取真实岩石骨料三维形状；随机节理参数采用均匀分布和正态分布（表1）；验证算例使用简支梁模型（尺寸6×0.6×0.8 m，弹性模量1 GPa，泊松比0.3，集中力10 kN）。

## Methods
软件采用面向对象的C++编程，分为三个模块：计算几何模块（纯C++，无系统API，可移植）、可视化模块（OpenGL库）、控制器模块（基于Qt框架）。关键算法包括：
- 基于B-rep和哈希表的块体识别（五级拓扑结构：顶点→有向边→有向环→有向面→有向体）；
- 小尺度裂缝用多边形模拟并通过蒙特卡洛法随机生成（六参数：倾角、倾向、半径、间距、迹长、中心坐标），大尺度曲面用三角形网格逼近（利用钻孔数据、Kriging插值或激光扫描等）；
- 裂缝网络相交检查算法（方向叉积求交线、交点排序、确定有效线段）；
- 自适应结构化六面体数学网格生成，仅在数学网格与物理界面（节理、边界等）相交时执行切割操作，否则直接转换为流形块体（MB），提高效率；
- 覆盖系统编码采用改进的并查集算法（Union-Find）将同一数学覆盖内的MB聚类为物理片（PP），不引入额外编号系统；
- 利用OpenMP库实现CPU并行加速，因块体切割和覆盖编码任务独立、无数据依赖。
生成流形单元的核心流程：构建块体系统→生成数学网格→块体切割形成MB→覆盖系统编码→OpenGL实时显示ME。

## Key Findings
MEG3D表现出高鲁棒性与效率。能够处理曲面/平面裂缝切割、随机DFN模型生成、土石混合体建模等复杂场景。在网格密度从2m到0.2m的测试中，串行生成2,033,709个流形单元耗时41.527秒，并行仅需8.508秒，加速比约4.744–5.152倍（14核CPU）。龙形几何体生成69,079个ME仅用9.139秒。软件可识别的最小块体体积为0.0000265 m³，V形边坡算例中最小流形单元体积为2.58×10⁻⁸ m³，表明几何处理的高数值稳定性。DFN模型成功生成双组随机节理网络。利用数字摄影测量重建的土石混合体边坡模型实现了真实骨料投放与离散。梁的验证算例显示，随着网格加密（120→1920个ME），3D-NMM计算的竖向位移逐渐逼近解析解，1920个ME时几乎一致，验证了所生成数值模型的准确性。软件还可为离散元(DEM)、非连续变形分析(DDA)等方法生成模型。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 并行加速比4.744-5.152倍（14核CPU, i9-12900H） | 第4.3节，表2 | 网格密度2m至0.2m，ME数3,401至2,033,709 | 使用OpenMP并行，任务独立 |
| 龙形几何体生成69,079个ME耗时9.139s | 第4.5节，图29 | 数学网格尺寸0.2m，复杂边界采用BVH包围盒算法 | 验证复杂形状处理效率 |
| 最小ME体积2.58×10⁻⁸ m³ | 第4.6节 | V形边坡模型，2,893个ME，容差10⁻¹⁰ | 显示数值稳定性 |
| 梁位移收敛至解析解（1,920个ME） | 第5节，图33 | E=1 GPa, μ=0.3, P=10 kN, 网格尺寸0.3m→0.1m | 验证生成模型的3D-NMM计算精度 |
| 块体切割后识别最小块体体积0.0000265 m³ | 第4.1节，图22 | 含曲面隧道的边坡，123个子块体 | 体积近似正态分布，76块<50 m³ |
| DFN模型成功生成双组随机节理网络 | 第4.2节，图23、表1 | 60×30×45m立方体模型，一组均匀分布，一组正态分布 | 蒙特卡洛法，多边形表征裂缝 |

## Limitations
MEG3D尚处于初步版本，可能存在未被作者发现的缺陷，未来需进一步完善和升级（Conclusion）。当前仅提供预处理功能，未集成三维接触算法和力学求解器。仅对有限规模算例进行了测试，未涉及超大规模（如千万级单元以上）模型。

## Assumptions / Conditions
采用数值流形法的双重覆盖系统（数学覆盖MC与物理覆盖PC），数学覆盖由结构化六面体有限元网格定义，且必须完全覆盖物理域。块体采用B-rep定向拓扑表示，小尺度裂缝简化为平面多边形，大尺度裂缝由三角形网格逼近。块体切割仅在数学网格与物理面相交时进行；若网格与物理域无交且中心在域内，则自动转换为MB。部分算例中几何容差设为10⁻¹⁰。梁算例假设线弹性小变形且不计重力。软件基于Qt和OpenGL开发，具有跨平台特性。并行化假设切割与编码任务之间无依赖关系。

## Key Variables / Parameters
- 随机裂缝参数：倾角、倾向、半径、间距、迹长、中心坐标（表征多边形裂缝）；
- 数学网格尺寸（控制ME数量和计算精度）；
- 几何容差；
- 梁算例：弹性模量E=1 GPa，泊松比μ=0.3，集中荷载10 kN，梁尺寸6×0.6×0.8 m。

## Reusable Claims
- MEG3D采用纯C++面向对象编程，计算几何模块无系统API，具有良好的可移植性，可嵌入其他C++兼容框架（如Python）[Tong 2024, 第3.1节]。
- 软件通过改进的Union-Find并查集算法高效地将流形块体聚类为物理片，避免了额外的编号系统，提升编码效率[第3.3.3节]。
- 在数学网格与物理域不相交且网格中心在物理域内部时，可直接转换为流形块体，省去切割操作，大幅提高生成效率[第3.3.2节]。
- OpenMP并行化使ME生成效率提高约5倍，对于大规模模型具有实用价值[第4.3节，表2]。
- 数字摄影测量技术可用于重建真实岩块几何，并融入土石混合体边坡的NMM离散化模型[第4.4节]。
- 软件可识别极小体积的块体（~10⁻⁵ m³）和流形单元（~10⁻⁸ m³），表明几何处理具有高鲁棒性[第4.1、4.6节]。

## Candidate Concepts
- [[3D数值流形法 (3D-NMM)]]
- [[流形单元 (ME)]]
- [[双重覆盖系统]]
- [[数学覆盖 (MC)]]
- [[物理覆盖 (PC)]]
- [[流形块体 (MB)]]
- [[块体切割]]
- [[边界表示 (B-rep)]]
- [[离散裂缝网络 (DFN)]]
- [[土石混合体 (SRM)]]
- [[并查集算法 (Union-Find)]]
- [[自适应数学网格]]
- [[数字摄影测量]]
- [[面向对象编程 (OOP)]]

## Candidate Methods
- [[蒙特卡洛法生成随机DFN]]
- [[多边形裂缝表征]]
- [[三角形网格逼近曲面裂缝]]
- [[哈希表辅助的块体识别]]
- [[改进的Union-Find覆盖系统编码]]
- [[OpenMP并行预处理]]
- [[基于数字摄影测量的骨料重建]]
- [[自适应六面体网格生成]]
- [[B-rep块体五级拓扑结构]]
- [[BVH包围盒加速块体切割]]

## Connections To Other Work
本文建立在先前3D-NMM预处理研究基础上，包括Li和Zhang (2014)的有限元网格生成ME、Yang等 (2016)的布尔交运算方法、Wu等 (2017)的含节理断层的ME生成算法、Ke和Wang (2020)的四/六面体数学覆盖以及Yang和Li (2022)的并行预处理策略。软件可输出用于DDA (Shi 1992b)和DEM (Cundall 1988)的模型。数字摄影测量技术参考Zhao等 (2020)。NMM基础理论源自Shi (1992a)。背景中亦提及连续介质方法常用软件FLAC、Abaqus等。

## Open Questions
MEG3D目前为初始版本，可能存在未发现的程序缺陷，未来需进一步改进升级。尚未集成3D-NMM的接触算法和求解器，无法直接进行力学计算。对于超大规模模型（数千万级单元）的处理能力和稳定性有待验证。如何更高效地整合CT扫描等先进勘测技术以自动构建几何模型，仍是开放方向。

## Source Coverage
所有16个非空索引片段均已处理。源字符总数75,916，汇编后源字符69,703，字符覆盖率91.8%；块覆盖率100%。
