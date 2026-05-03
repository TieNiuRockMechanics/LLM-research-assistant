---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-meng-an-ifs-based-fractal-discrete-fracture-network-for-hydraulic-fracture-behavior-of-rock"
title: "An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass."
status: "draft"
source_pdf: "data/papers/2023 - An IFS-based fractal discrete fracture network for hydraulic fracture behavior of rock mass.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Meng, Qingxiang, et al. \"An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass.\" *Engineering Geology*, vol. 324, 2023, 107247. doi:10.1016/j.enggeo.2023.107247."
indexed_texts: "19"
indexed_chars: "90251"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:53:27"
---

# An IFS-Based Fractal Discrete Fracture Network for Hydraulic Fracture Behavior of Rock Mass.

## One-line Summary
本文提出一种基于迭代函数系统（IFS）的二维分形离散裂隙网络（DFN）生成方法，并将其与零厚度流体内聚单元结合，用于模拟岩体水力压裂行为，结果表明与传统线性DFN相比，分形DFN显著改变注入压力演化和裂缝扩展模式 [Meng 2023, pp. 1-2]。

## Research Question
如何构建具有分形粗糙形态的离散裂隙网络模型，以更真实地刻画岩体水力压裂过程中裂缝的扩展规律，并定量评估分形特征对注入压力、裂缝开度及扩展路径的影响？

## Study Area / Data
未从索引片段中确认具体工程场地或原位数据。论文以共轭断层作为抽象地质模型，设定两组裂隙优势方向夹角约为60°，一组为主裂隙（长度较长），另一组为次裂隙（长度较短且多终止于主裂隙） [Meng 2023, pp. 4-5]。模型生成基于统计规律和分形插值，未引用特定区域野外测量数据。

## Methods
1. **分形DFN生成**：  
   - 通过四个控制点生成初始折线，再用IFS分形插值将其转换为粗糙裂缝曲线，插值式中垂直缩放因子 \(d_n\) 控制起伏程度 [Meng 2023, pp. 3-4]。  
   - 使用基于垂直距离阈值的平滑技术去除过密短线，保留基本几何形态 [Meng 2023, pp. 4-5]。  
   - 按共轭断层模式在计算域内随机生成两组初始线性裂缝，将线性段替换为分形曲线，并剔除短边和狭小间隙，最终形成二维分形DFN [Meng 2023, pp. 5-6]。

2. **水力压裂模拟**：  
   - 岩体视为多孔弹性介质，基于Terzaghi有效应力原理和孔隙压力扩散连续性方程，耦合裂缝内流动与基质渗流，考虑滤失 [Meng 2023, pp. 5-6]。  
   - 裂缝内流体流动采用立方定律（cubic law），损伤与扩展利用零厚度内聚区模型（CZM）描述，以牵引‑分离法则控制起裂、脱粘和扩展 [Meng 2023, pp. 5-6]。  
   - 为解决复杂分形几何的网格划分困难，提出一套网格细化流程：提取原有网格交界面，合并流体节点，重构零厚度流体内聚单元，保证流体在交叉路径上的连续分配 [Meng 2023, pp. 9-10]。  
   - 使用经典KGD水力压裂解析模型验证数值解，材料参数取自表2（\(E=17\) GPa，\(\nu=0.2\)，断裂能100 Pa·m，流体粘度0.1 Pa·s，注入速率0.001 m³/s等） [Meng 2023, pp. 9-10]。

## Key Findings
1. 分形DFN水力压裂的注入压力呈现三个阶段：突然上升、快速下降、趋于稳定 [Meng 2023, pp. 1-2]。  
2. 与常规线性DFN相比，基于IFS的分形DFN显著改变了注入压力演化过程和裂缝扩展形态 [Meng 2023, pp. 1-2]。  
3. 裂缝开度的变化是影响水力压裂行为的重要因素 [Meng 2023, pp. 1-2]。  
4. 在KGD验证算例中，采用零厚度CZM耦合有限元模型获得的裂缝长度、最大缝宽和注入压力与解析解吻合良好 [Meng 2023, pp. 9-10]。  
5. 分形曲线的起伏程度随垂直缩放因子 \(d_n\) 增大而增强；当 \(\sum |d_n|>1\) 且插值点不共线时，分形维数 \(D\) 由 \(\sum |d_n| a_n^{D-1}=1\) 确定，否则 \(D=1\) [Meng 2023, pp. 3-4]。

## Core Evidence Table
| Evidence | Source | Conditions / Assumptions | Notes |
|----------|--------|--------------------------|-------|
| 注入压力表现为突然增加、迅速下降和稳定三个阶段 | [Meng 2023, pp. 1-2] | 二维分形DFN，共轭断层分布，CZM，立方定律 | 仅基于数值模拟，未提供实测对比 |
| 分形DFN与传统线性DFN在注入压力演化和裂缝扩展上存在明显差异 | [Meng 2023, pp. 1-2] | 相同几何参数框架下比较，具体量化差异未在片段中给出 | 强调分形粗糙度的影响 |
| 数值解与KGD解析解在裂缝长度、最大缝宽、注入压力上吻合 | [Meng 2023, pp. 9-10] | 材料参数见表2，平面应变，均质线弹性，牛顿流体，恒定注入速率 | 验证了CZM耦合模型的准确性 |
| 平滑算法可在保持基本几何的前提下减少短线数量（如从137条减至24条） | [Meng 2023, pp. 4-5] | 初始曲线长0.2 m，\(d_n=0.4\)，不同阈值 \(T\) | 未给出定量误差分析 |

## Limitations
- 不同 \(d_n\) 取值下分形DFN的连通性与初始线性DFN完全一致是尚未解决的挑战 [Meng 2023, pp. 5-6]。  
- 零厚度CZM本身具有网格依赖性和对凝聚参数的敏感性，文中虽提出网格细化方法，但参数敏感性影响未深入讨论 [Meng 2023, pp. 6-7]。  
- 分析仅限于二维情形，未涉及三维分形裂隙网络的生成和水力耦合行为。  
- 未结合具体工程实例进行校准或验证，仅以共轭断层概念模型和KGD经典问题作为算例。  
- 索引片段未提供不同 \(d_n\)、裂隙密度或方向对水力压裂响应的系统性参数分析结果。

## Assumptions / Conditions
- **几何与分形**：初始裂缝由四点折线经IFS插值生成，\(N=3\)；垂直缩放因子满足 \(|d_n|<1\) 以保证收敛；共轭断层中主裂隙较长、次裂隙较短，且次裂隙终止于主裂隙 [Meng 2023, pp. 3-5]。  
- **岩体与力学**：岩体为连续、均质、各向同性多孔介质，服从线弹性本构和Terzaghi有效应力原理；裂缝内流体为不可压缩牛顿流体，流动遵循立方定律；基质渗流符合Darcy定律并考虑滤失 [Meng 2023, pp. 5-6]。  
- **断裂与损伤**：采用牵引‑分离型内聚区模型，损伤起始由应变能释放率达到断裂能控制，拉伸强度取2 MPa，断裂能100 Pa·m [Meng 2023, pp. 6-7, 9-10]。  
- **边界与加载**：KGD算例为平面应变问题，通过预设孔压节点和恒定注入速率驱替，忽略温度效应和缝内支撑剂 [Meng 2023, pp. 9-10]。

## Key Variables / Parameters
- **分形控制参数**：垂直缩放因子 \(d_n\)，分形维数 \(D\)（当 \(\sum |d_n|>1\) 时由公式(7)给出），仿射变换常数 \(a_n\) [Meng 2023, pp. 3-4]。  
- **几何参数**：初始裂缝长度、共轭断层夹角（~60°）、平滑阈值 \(T\)、最小裂缝长度 \(d_{\min}\) [Meng 2023, pp. 4-5]。  
- **材料参数**：杨氏模量 \(E=17\) GPa，泊松比 \(\nu=0.2\)，孔隙率0.1，基质与裂缝抗拉强度2 MPa，断裂能100 Pa·m [Meng 2023, pp. 9-10]。  
- **流体与注入参数**：流体粘度0.1 Pa·s，注入速率0.001 m³/s [Meng 2023, pp. 9-10]。  
- **水力响应变量**：注入压力、裂缝开度（aperture）、裂缝长度、裂缝扩展路径 [Meng 2023, pp. 1-2, 9-10]。

## Reusable Claims
1. **IFS分形插值可生成具有可控粗糙度的裂隙曲线**  
   给定初始折线后，通过调节垂直缩放因子 \(d_n\)（满足 \(|d_n|<1\)）能系统改变曲线的波动幅度；当 \(\sum |d_n|>1\) 且插值点不共线时，分形维数 \(D\) 由公式 \(\sum |d_n| a_n^{D-1}=1\) 确定，否则 \(D=1\) [Meng 2023, pp. 3-4]。  
   *适用条件*：二维插值，\(N=3\) 的四个初始点生成折线；证据来自图2的形态对比和公式(7)；*限制*：曲线形态还受初始点位置影响，且 \(d_n\) 绝对值须小于1以避免迭代发散。

2. **注入压力响应呈现三阶段特征**  
   基于分形DFN的水力压裂模拟显示，注入压力先急剧上升，随后快速下降，最后趋于平稳；这一特征与线性DFN存在差别 [Meng 2023, pp. 1-2]。  
   *适用条件*：共轭断层型2D分形DFN，采用零厚度CZM和立方定律；证据来自摘要结论；*限制*：未给出具体的压力‑时间曲线，仅定性描述，且未验证其普适性。

3. **网格细化与零厚度内聚元插入法适用于复杂分形DFN**  
   通过提取原网格交界面边并重构零厚度内聚单元、合并重复流体节点，可在不破坏原有网格拓扑的前提下嵌入流动与断裂耦合路径，使流体在任意交叉点得以分配 [Meng 2023, pp. 9-10]。  
   *适用条件*：二维三角形/四边形网格，配合CAD或脚本处理；证据来自方法描述及KGD验证；*限制*：对极度密集或高度扭曲的网格可能仍需预处理，且参数敏感性未排除。

4. **分形粗糙度不影响基本连通性时，仍可大幅改变水力压裂响应**  
   在分形插值不改变主次裂隙交切关系的情况下，仅引入粗糙起伏即可使注入压力演变和裂缝扩展行为与光滑DFN显著不同 [Meng 2023, pp. 1-2]。  
   *证据*：文章明确指出在与传统线性DFN对比时，分形DFN表现出明显差异；*限制*：片段未展示不同 \(d_n\) 下的具体量化结果，连接性是否完全一致仍是待解决问题。

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]  
- [[Iterative Function System (IFS)]]  
- [[Fractal Fracture]]  
- [[Hydraulic Fracturing]]  
- [[Cohesive Zone Model (CZM)]]  
- [[Cubic Law]]  
- [[Fractal Dimension]]  
- [[KGD Model]]  
- [[Tortuosity of Fracture Networks]]  
- [[Conjugate Fault System]]  
- [[Zero-thickness Cohesive Element]]  
- [[Terzaghi's Effective Stress]]  
- [[Porous Media Flow]]

## Candidate Methods
- [[IFS Fractal Interpolation]]  
- [[Random DFN Generation]]  
- [[Mesh Refinement for Cohesive Elements]]  
- [[Zero-thickness Flow Cohesive Element Insertion]]  
- [[Hydromechanical Coupling in Porous Media]]  
- [[Numerical Solution of KGD Problem]]  
- [[Ramer–Douglas–Peucker Smoothing]] (used conceptually for curve smoothing)

## Connections To Other Work
- **分形插值理论基础**：Barnsley (1986) 提出分形插值的概念；Hutchinson (1981) 揭示了自然中普遍存在的自相似分形结构；Long et al. (1992) 已将基于IFS的反演方法用于建立非均质裂缝性储层模型 [Meng 2023, pp. 2-2]。  
- **裂隙分形特征**：大量研究表明岩体裂隙具有分形结构（Heping and Zhida, 1988; Miller et al., 1990），且节理面粗糙度可用分形维数描述（Turk et al., 1987） [Meng 2023, pp. 2-2]。  
- **曲折度与流动**：流体在裂隙网络中的输运特性与流动路径曲折度密切相关（Tsang, 1984; Bo‑Ming and Jian‑Hua, 2004），分形曲线能够反映局部波动，因此本方法有潜力捕捉迂曲流径 [Meng 2023, pp. 2-2]。  
- **水力压裂数值方法**：线性弹性断裂力学（LEFM）、扩展有限元（XFEM）、离散元（DEM）等方法已被广泛用于DFN水力压裂，文中采用CZM作为平衡精度与效率的替代方案 [Meng 2023, pp. 2-3, 6-9]。  
- **现有DFN生成方法**：Wang et al. (2022) 基于傅里叶变换方法构建粗糙DFN，发现节理网络几何会极大改变岩体强度和破坏模式 [Meng 2023, pp. 2-3]。

## Open Questions
- 如何在保持分形插值改变粗糙度的同时，确保不同 \(d_n\) 下裂隙网络拓扑连通性完全相同？[Meng 2023, pp. 5-6]  
- 三维IFS分形插值在裂隙网络建模中如何实现并有效耦合水力压裂求解？当前片段仅给出了三维变换形式，未给出数值案例 [Meng 2023, pp. 3-4]。  
- 分形维数 \(D\) 与水力压裂关键响应（如起裂压力、缝网复杂度）之间是否存在定量的关联公式？  
- 如何基于实际岩体露头或钻孔数据标定 \(d_n\) 和平滑阈值 \(T\) 等参数，使分形DFN反映特定场地的裂隙粗糙度？  
- CZM的参数（如断裂能、牵引–分离曲线形状）对分形裂缝交叉和分支的敏感性如何？文中仅为验证目的采用单一组参数 [Meng 2023, pp. 9-10]。

## Source Coverage
本知识页依据19个索引片段整理，片段覆盖了摘要、引言（分形与IFS背景）、分形DFN生成方法（2.1节）、水力压裂建模及零厚度内聚元插入技术（2.2节）、以及KGD验证算例的部分内容。**已覆盖信息**：核心算法原理、建模流程、注入压力定性结论和模型验证。**明显缺失**：缺少不同 \(d_n\) 或不同几何参数下的参数敏感性结果，未提供分形DFN与线性DFN对比的具体压力‑时间曲线或裂缝扩展图，也未讨论现场尺度验证或工程应用案例。因此，关于方法适用范围和定量预测能力的证据尚不完整。
