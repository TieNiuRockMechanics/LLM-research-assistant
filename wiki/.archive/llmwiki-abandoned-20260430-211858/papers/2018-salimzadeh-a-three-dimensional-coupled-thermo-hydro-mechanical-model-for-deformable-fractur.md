---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur"
title: "A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2018 - A three-dimensional coupled thermo-hydro-mechanical model for deformable fractured geothermal systems.pdf"
collections:
  - "part3-3"
citation: "Salimzadeh, Saeed, et al. “A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems.” *Geothermics*, vol. 71, 2018, pp. 212–24. doi:10.1016/j.geothermics.2017.09.012."
indexed_texts: "13"
indexed_chars: "64271"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:30:56"
---

# A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems.

## One-line Summary
该论文提出并验证了一个针对可变形裂隙地热系统的三维完全耦合热-水-力（THM）有限元模型，该模型能精细刻画裂隙开度变化对流动和传热的影响 [Salimzadeh 2018, pp. 1-4]。

## Research Question
如何构建一个能够同时考虑裂隙变形、接触应力、热-水-力多物理场相互作用的三维数值模型，以准确评估增强型地热系统（EGS）及天然裂隙储层中裂隙开度改变对冷流体流动和热量提取的影响？[Salimzadeh 2018, pp. 3-4, 9-10]

## Study Area / Data
本研究的模拟对象为理想化的地热系统，未关联具体的地点或现场数据。验证与示例基于特定的边界条件和材料参数，部分参数（如注入温度、初始应力）在示例中给出，但完整的数据集未从索引片段中确认。模拟设置了三种算例：一个用于验证热传递模块，另外两个分别展示在EGS单个裂隙和裂隙性储层中由热孔弹性变形引起的接触应力和裂隙开度变化对流动的影响 [Salimzadeh 2018, pp. 9-10]。

## Methods
### 整体框架
模型通过有限元方法求解，由五个交互的子模型构成：热弹性变形模型、基质渗流模型、裂隙渗流模型、基质传热模型和裂隙传热模型。基质采用三维四面体离散，裂隙被处理为二维表面不连续，两侧位移独立计算。裂隙面接触应力通过独立的接触模型迭代求解，并与THM模型耦合 [Salimzadeh 2018, pp. 3-5, 9-10]。

### 力学模型
热弹性本构采用公式 \(\boldsymbol{\sigma}' = \mathbf{D}\boldsymbol{\varepsilon} - \beta K (T - T_0) \mathbf{I}\)，其中 \(\mathbf{D}\) 为排水刚度矩阵，\(\beta\) 为热膨胀系数，\(K\) 为体积模量。考虑小变形，由位移梯度计算应变。裂隙面施加流体压力和接触应力 [Salimzadeh 2018, pp. 4-5]。

### 渗流模型
- **基质渗流**：采用达西定律，耦合Biot系数 \(\alpha\)，控制方程包含流体可压缩性和热膨胀项 [Salimzadeh 2018, pp. 5]。
- **裂隙渗流**：基于立方定律，平均流速 \(\mathbf{v}_f = -\frac{a_f^2}{12\mu_f}\nabla p_f\)，其中 \(a_f\) 为裂隙开度（两侧法向位移差），\(a_{fc}\) 为接触时的残余开度。考虑裂隙渗流与基质渗流之间的泄漏质量交换，该交换是压差和基质渗透率的函数 [Salimzadeh 2018, pp. 4-5]。
- **单相流假设**：裂隙和基质内均为单相流体 [Salimzadeh 2018, pp. 3]。

### 传热模型
- **基质传热**：假设流体流速足够慢，固体颗粒与基质流体始终处于局部热平衡。热通量包含传导项和热对流项，有效热导率为固体和流体的体积平均 [Salimzadeh 2018, pp. 5-6]。
- **裂隙传热**：允许基质与裂隙间通过裂隙壁传导和泄漏流平流进行热量交换，局部热非平衡状况下裂隙流体与基质流体存在温差 [Salimzadeh 2018, pp. 3-4]。

### 接触模型
裂隙接触开度 \(a_{fc}\) 的变化与法向接触应力 \(\Delta\sigma_n\) 呈线性关系，\(\Delta a_{fc} = \Delta\sigma_n / K_n\)。热力与水力载荷作为体力项施加于接触模型，接触应力作为边界牵引力应用于THM模型。二者在每个时间步内迭代更新，直至收敛 [Salimzadeh 2018, pp. 9-10]。

### 数值求解
控制方程采用加权残量法积分，得到以位移、压力和温度为未知量的耦合刚度矩阵形式 \(\mathbf{SX} = \mathbf{F}\)。时间离散采用隐式有限差分，每个时间步内使用加权平均法迭代求解，收敛容差为0.01。程序基于帝国理工学院地质力学工具包（Imperial College Geomechanics toolkit）和CSMP++平台，使用二次非结构单元（四面体和三角形）进行空间离散 [Salimzadeh 2018, pp. 6-9]。

## Key Findings
- 模型通过与 Ghassemi 等（2008）的解析解对比得到验证，在刚性裂隙且考虑基质渗透率各向异性的条件下，裂隙内流体温度的空间分布与解析解吻合良好 [Salimzadeh 2018, pp. 7-9]。
- 模拟显示，在初温80 °C、初始围压60 MPa的低注入温度场景下，裂隙内的温度、开度和接触应力随时间（10年、20年、30年）呈现明显空间非均匀分布，裂隙尖端附近的接触应力和开度变化显著 [Salimzadeh 2018, pp. 9-10]。
- 模型证明，考虑热孔弹性变形以及由此引起的裂隙开度和接触应力演化，对于准确预测地热系统的流动和热提取性能至关重要 [Salimzadeh 2018, pp. 4, 9-10]。
- （更多详细的定量结果，如产流温度、开度变化量等，未从索引片段中确认。）

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 裂隙内流体温度空间分布曲线与 Ghassemi 等（2008）的解析解一致，验证了不同基质渗透率和泄漏比下的传热计算 | [Salimzadeh 2018, pp. 7-9] | 刚性裂隙、忽略变形，考虑基质渗透率及各向异性情况 | 图3显示对比，模型的渗透率假设仅为法向，除非标注为[2D] |
| 在低注入温度（Tini=80°C）、高初始围压（σini=60 MPa）条件下，模拟展示了10、20、30年后裂隙温度、开度和接触应力的空间分布图 | [Salimzadeh 2018, pp. 9-10] | 可变形裂隙，考虑热孔弹性变形，基于迭代接触模型 | 图8显示，没有给出具体数值，仅定性趋势 |
| 模型框架与公式的详细推导（包括刚度矩阵各子块的表达式） | [Salimzadeh 2018, pp. 6-9] | 小变形、高纵横比裂隙、单相流等假设 | 公式(31)-(57)给出具体矩阵形式 |

## Limitations
- 模型假设为单相流，不适用于有相变（如沸腾）或两相流体的地热系统 [Salimzadeh 2018, pp. 3-4]。
- 裂隙接触模型采用线性关系，虽然片段提到可扩展为非线性模型，但未给出非线性算例 [Salimzadeh 2018, pp. 9-10]。
- 基质传热模型建立在局部热平衡假设上，当达西流速较高时该假设可能失效 [Salimzadeh 2018, pp. 5-6]。
- 本研究中的示例均为理想化几何和边界条件，未与实际工程监测数据对比验证。模型对复杂裂隙网络的适用性未从索引片段中确认。

## Assumptions / Conditions
- **力学**：小变形、各向同性线性热弹性本构；裂隙面上的流体剪切力忽略不计；Biot系数α在力学与基质渗流中耦合，在裂隙流模型中不显式出现 [Salimzadeh 2018, pp. 4-5]。
- **渗流**：基质为饱和多孔介质，遵循达西定律；裂隙为高纵横比表面，满足立方定律适用范围；单相流体，正压流体；泄漏量是基质-裂隙压差和基质渗透率的线性函数 [Salimzadeh 2018, pp. 3-5]。
- **传热**：基质内固-液局部热平衡；裂隙与基质间允许局部热非平衡，通过传导和泄漏对流传热；有效热导率按固体和流体的体积分数线性插值 [Salimzadeh 2018, pp. 5-6]。
- **接触**：接触开度与法向接触应力线性相关，刚度系数 \(K_n\) 为常数 [Salimzadeh 2018, pp. 9-10]。
- **模拟场景**：三维域内包含单个或少量离散裂隙，忽略重力影响 [Salimzadeh 2018, pp. 9-10]。

## Key Variables / Parameters
- \(a_f\)：动态裂隙开度（定义为单位法向位移差）；\(a_{fc}\)：接触状态下的残余开度 [Salimzadeh 2018, pp. 4-5]。
- \(p_f\), \(p_m\)：裂隙和基质中的流体压力 [Salimzadeh 2018, pp. 4-5]。
- \(T\), \(T_0\)：温度和参考温度 [Salimzadeh 2018, pp. 4-6]。
- \(\alpha\)：Biot系数，控制基质变形-渗流耦合强度（\(\alpha=0\)时解耦）[Salimzadeh 2018, pp. 5]。
- \(K\)：体积模量；\(\beta\)：热膨胀系数 [Salimzadeh 2018, pp. 4]。
- \(\mu_f\)：流体粘度；\(c_f\)：流体压缩系数；\(\beta_f\)：流体体积膨胀系数 [Salimzadeh 2018, pp. 4-5]。
- \(k\)：基质固有渗透率 [Salimzadeh 2018, pp. 5]。
- \(\lambda_m\)：基质有效热导率，由 \(\lambda_s\) 和 \(\lambda_f\) 按孔隙度线性插值得到 [Salimzadeh 2018, pp. 5-6]。
- \(C_f\)：流体比热容；\(\rho_f\)：流体密度 [Salimzadeh 2018, pp. 5-6]。
- \(\sigma_n\)：裂隙面法向接触应力（压为正）；\(K_n\)：裂隙法向接触刚度 [Salimzadeh 2018, pp. 9-10]。
- 泄漏流量系数 \(m\)（与基质渗透率和基质-裂隙压差相关）[Salimzadeh 2018, pp. 7-9]。

## Reusable Claims
1. 在高纵横比裂隙中，平均流体流速可按立方定律表达为 \(\mathbf{v}_f = -\frac{a_f^2}{12\mu_f} \nabla p_f\)，开度 \(a_f\) 定义为两侧壁面的法向位移差。当裂隙闭合到接触状态时，存在最小残余开度 \(a_{fc}\) [Salimzadeh 2018, pp. 4-5]。
2. 将裂隙显式建模为二维表面不连续，并独立求解其内部压力和温度，相比等效连续介质模型能够更精确地表征裂隙内流场、温度场及应力场的局部非均匀性，这是由立方定律高度非线性和接触约束造成的 [Salimzadeh 2018, pp. 3-4]。
3. 基质渗流与裂隙渗流可通过泄漏质量交换进行耦合，该交换量是基质与裂隙流体压差以及基质渗透率的函数，同时泄漏流也携带热量，构成裂隙与基质间的热平流项 [Salimzadeh 2018, pp. 3-4, 5]。
4. 对于可变形裂隙，接触应力直接影响裂隙开度，而接触应力本身会因热载荷（冷却收缩）和孔弹性压力变化而变化，因此需要将接触模型与THM方程在每个时间步进行迭代耦合以正确描述这一机械反馈 [Salimzadeh 2018, pp. 9-10]。
5. 在增强地热系统的长期运行中（例如30年），裂隙尖端的开度和接触应力变化最大，可能形成流动通道集中区域，影响热提取效率和系统的长期稳定性 [Salimzadeh 2018, pp. 9-10]。
6. 当基质渗透率较小时，忽略基质-裂隙热交换会导致对裂隙内流体冷却速度的预测偏差，特别是当考虑多维度泄漏流时，误差更为明显 [Salimzadeh 2018, pp. 7-9]。

## Candidate Concepts
- [[fractured geothermal reservoir]]
- [[cubic law]]
- [[local thermal non-equilibrium]]
- [[contact mechanics]]
- [[thermo-hydro-mechanical coupling]]
- [[enhanced geothermal systems (EGS)]]
- [[leakoff mass exchange]]
- [[finite element method]]
- [[thermoporoelasticity]]
- [[fracture aperture]]
- [[rock matrix permeability]]

## Candidate Methods
- [[finite element method for THM]]
- [[iterative coupling of contact and THM]]
- [[cubic law flow in fractures]]
- [[Darcy flow in porous matrix]]
- [[leakoff boundary condition]]
- [[advection-conduction heat transfer in fractures]]
- [[contact model with thermal and hydraulic loading]]
- [[octree meshing for fractures]]
- [[weighted average iterative solver]]

## Connections To Other Work
- 模型的传热模块通过与 Ghassemi 等（2008）针对刚性裂隙提出的半解析解进行对比验证 [Salimzadeh 2018, pp. 7-9]。
- 模型对裂隙流动的处理基于 Zimmerman 和 Bodvarsson（1996）推导的立方定律 [Salimzadeh 2018, pp. 4]。
- 热弹性本构参考了 Khalili 和 Selvadurai（2003）的工作 [Salimzadeh 2018, pp. 4]。
- 文献指出在 EGS 中，热致裂隙、水力压裂及剪切刺激共同作用，引用 McClure 和 Horne（2014）等 [Salimzadeh 2018, pp. 2-3]。
- 模型中基质有效热导率的简单体积平均近似，并指出更精确模型参考 Zimmerman（1989）[Salimzadeh 2018, pp. 5-6]。
- 模型使用的有限元框架基于 Paluszny 和 Zimmerman（2011）的地质力学工具包以及 CSMP++ 平台 [Salimzadeh 2018, pp. 7-9]。
- （由于片段限制，与其他有关裂隙性介质THM模拟的对比，如 Rutqvist 等（2005）的具体差异未在片段中展开论述。）

## Open Questions
未从索引片段中确认。论文可能讨论了模型的拓展方向（如非线性接触、裂隙网络扩展、两相流等），但当前片段未提供相关信息。

## Source Coverage
本页面依据所提供论文的 **13** 个索引片段编写。片段覆盖了论文的版权页、摘要、引言、计算模型的核心公式及其推导、数值实现细节、部分验证（与 Ghassemi 等对比）以及模拟示例的简要结果。覆盖内容明显偏向**方法和实现**章节（第2节），包含了刚度矩阵、耦合策略和接触迭代流程的详细描述；结果部分仅提供了两个定性图示的描述，缺少产流温度、开度变化量等定量数据；讨论和结论章节的内容完全缺失。因此，该页面对模型的数学框架和耦合机制描述较为完整，但对于模型的应用效果、参数敏感性、以及与现场数据的对比等关键信息可能不充分，无法确认模型的预测能力和工程适用性。
