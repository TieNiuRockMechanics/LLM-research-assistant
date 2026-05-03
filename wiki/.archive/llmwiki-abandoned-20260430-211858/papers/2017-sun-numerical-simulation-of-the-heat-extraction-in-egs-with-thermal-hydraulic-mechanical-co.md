---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co"
title: "Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model."
status: "draft"
source_pdf: "data/papers/2017 - Numerical simulation of the heat extraction in EGS with thermal-hydraulic-mechanical coupling method based on discrete fractures model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Sun, Zhi-xue, et al. \"Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model.\" *Energy*, vol. 120, 2017, pp. 20-33. doi:10.1016/j.energy.2016.10.046."
indexed_texts: "11"
indexed_chars: "53296"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:49:47"
---

# Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model.

## One-line Summary
基于离散裂缝模型与热-水-力（THM）全耦合方法，通过二维随机裂缝网络数值模拟了增强型地热系统（EGS）的热量提取过程，并以澳大利亚库珀盆地Habanero地热田为例验证了模型，强调了THM耦合对系统性能评估的重要性 [Sun 2017, pp. 1-2]。

## Research Question
如何准确模拟增强型地热系统（EGS）中密集裂缝网络的复杂THM耦合过程，并辨识影响生产井出口温度的主要控制参数？ [Sun 2017, pp. 1-2, 8-9]

## Study Area / Data
案例研究基于澳大利亚中部库珀盆地Habanero增强型地热系统（Habanero Engineered Geothermal System）。该区高放射性花岗岩（Big Lake Suite）位于3600–3800 m深度，上覆厚沉积层，井底初始温度在5 km以内可达244°C以上。模拟设定初始温度200°C，注水压力80.4 MPa，生产压力68.6 MPa，注入水温20°C，周期40年，时间步长1天。裂缝网络为二维随机生成模型。 [Sun 2017, pp. 5-6, 6-8]

## Methods
- **物理模型**：将储层视为由岩石基质和离散裂缝网络组成的裂缝性多孔介质，采用热非平衡理论描述热量交换 [Sun 2017, pp. 1-2, 3-4]。
- **控制方程**：推导了质量守恒、能量平衡、动量平衡（含热弹性变形）的全耦合THM方程，包括 Darcy 定律、Biot 固结理论及热应力项 [Sun 2017, pp. 2-4]。
- **渗透率演化**：基于HM耦合，裂缝渗透率随有效应力/应变演化（式16），以此反映受力变形对渗流的影响 [Sun 2017, pp. 4-5]。
- **数值实现**：采用COMSOL Multiphysics进行全耦合求解，通过修改内部边界的弱形式嵌入裂缝刚度矩阵 [Sun 2017, pp. 4-5]。
- **模型验证**：与单裂缝热-水分析解析解（Barends [32]）以及一维热固结解析解（Bai [33]）对比，结果吻合良好 [Sun 2017, pp. 5-6]。

## Key Findings
- 温度下降在裂缝密集区更为迅速，连接裂缝形成主流通道，热对流显著；热分布呈现强非均质性与各向异性 [Sun 2017, pp. 8-9]。
- 注水高压和低温引起的热应力导致储层变形，应力场的改变反过来影响渗透率，进而影响热提取效率。有效正应力变化导致裂缝渗透率动态演变 [Sun 2017, pp. 8-9]。
- 考虑THM耦合效应对评估EGS的效率与性能至关重要；忽略力学变形将高估或低估热提取能力 [Sun 2017, pp. 1-2, 8-9]。
- 通过敏感性分析研究了控制出口温度的主要参数（具体参数列表未从索引片段中确认） [Sun 2017, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 数值模型与 Barends 解析解（单裂缝热-水问题）及 Bai 热固结解析解吻合良好，验证了 THM 耦合实施的准确性。 | [Sun 2017, pp. 5-6] | 二维单裂缝模型及一维热固结问题；采用表1、表2所列参数。 | 解析解作为基准，验证了耦合方程及 COMSOL 实现的正确性。 |
| THM 耦合效应显著影响 EGS 效率和性能，忽略力学-水力交互将导致对热提取评估的偏差。 | [Sun 2017, pp. 1-2] | 基于二维随机裂缝网络的 Habanero 案例；考虑热弹性变形。 | 文中的核心主张之一。 |
| 裂缝网络是决定 EGS 技术与经济可行性的基本组成部分。 | [Sun 2017, pp. 2-2] | 适用于密集裂缝网络的 EGS。 | 引用自引言部分，对模拟必要性进行支撑。 |
| 出口温度下降在裂缝集中区域更快，连接裂缝形成高流速主通道，呈现局部加速降温。 | [Sun 2017, pp. 8-9] | Habanero 案例，40 年模拟期，注入 20°C 水。 | 展示了裂缝网络对热传递的控制作用。 |
| 注入初期大幅位移变化由高压和急剧温差引起；后期虽压力稳定，但温度持续变化导致热应力驱动位移演变。 | [Sun 2017, pp. 8-9] | Habanero 案例，时间步长 1 天，模拟 40 年。 | 说明了力学响应与热、流过程的长期耦合。 |
| 渗透率随有效正应力变化而演化，直接受应力状态控制。 | [Sun 2017, pp. 8-9] | 基于裂缝特征点 #1–#4 的模拟结果。 | 支持 HM 耦合对渗透率演化的量化影响。 |

## Limitations
- 数值模拟局限于二维随机裂缝网络，未能体现真实三维裂缝连通性与流动几何 [Sun 2017, pp. 1-2, 6-8]。
- 岩石基质采用热弹性小应变假设，未考虑塑性或断裂扩展 [Sun 2017, pp. 2-3]。
- 模拟未包含水蒸气相变，假定储层内水始终为液态 [Sun 2017, pp. 2-3]。
- 敏感性分析的具体参数列表及其影响程度未从索引片段中确认。
- 模型虽经解析解验证，但未报告与现场实测温度、压力或位移数据的对比。

## Assumptions / Conditions
- 储层为裂缝性多孔介质，由不透水的岩石基质和离散裂缝网络构成 [Sun 2017, pp. 1-2]。
- 基于热非平衡理论，分别建立岩石和流体的能量方程，以描述实际热量交换过程 [Sun 2017, pp. 3-4]。
- 储层内水不汽化，始终以液态存在（储层最大温度 473.15 K，远低于饱和压力对应的沸点） [Sun 2017, pp. 2-3]。
- 对流和传导是主要的换热机制 [Sun 2017, pp. 2-3]。
- 岩石基质为热弹性材料，基于小应变假定 [Sun 2017, pp. 2-3]。
- 裂缝变形遵循局部弹性关系，正应力和剪应力分别由法向和切向刚度控制 [Sun 2017, pp. 3-4]。
- 模拟不考虑初始地应力，仅研究注水和采热引起的应力扰动 [Sun 2017, pp. 6-8]。

## Key Variables / Parameters
- **场变量**：压力 \( p \)、位移 \( u \)、温度 \( T \) 等。
- **材料参数**：弹性模量 \( E \)、泊松比 \( \nu \)、Biot 系数 \( a_B \)、线性热膨胀系数 \( a_T \)、体积模量 \( K' \) 等 [Sun 2017, pp. 3-4, 6-8]。
- **水力参数**：固有渗透率 \( k \)、裂缝渗透率 \( k_f \)、流体动力粘度 \( \eta \)、流体密度 \( \rho_f \)、限定存储系数 \( S \)、裂缝存储系数 \( S_f \) [Sun 2017, pp. 2-3]。
- **裂缝几何与刚度**：裂缝厚度 \( d_f \)、法向/切向刚度 \( k_n \)、\( k_s \) [Sun 2017, pp. 3-4]。
- **热力学参数**：岩石和流体的比热容、热导率等 [Sun 2017, pp. 5-8]。
- **耦合演化项**：有效应力/应变驱动的渗透率变化关系式（式 16）[Sun 2017, pp. 4-5]。
- **控制参数**：出口温度的主要控制参数通过敏感性分析研究，具体参数名称未从索引片段中确认 [Sun 2017, pp. 1-2]。

## Reusable Claims
1. 在 EGS 数值模拟中，若不考虑 THM 耦合效应，可能导致对热提取性能评估产生明显偏差。该结论基于二维离散裂缝模型与 Habanero 案例，限于文中假设的小应变与无相变条件 [Sun 2017, pp. 1-2, 8-9]。
2. 采用热非平衡模型可以更真实地捕捉裂缝内流体与岩石基质之间的非瞬时热交换特征，适用于密集裂缝网络的模拟场景 [Sun 2017, pp. 3-4]。
3. 裂缝网络的几何连通性与密度是决定 EGS 热提取效率的核心结构因素，高流速通道往往产生局部加速降温 [Sun 2017, pp. 8-9]。
4. 裂缝渗透率对应力状态高度敏感；通过引入依赖有效应力的渗透率演化模型，可以实现 HM 双向耦合，从而更准确地预测 EGS 长期性能 [Sun 2017, pp. 4-5, 8-9]。
5. 利用 COMSOL Multiphysics 修改内部边界弱形式可灵活实现离散裂缝的力学与渗流耦合，该方法在单裂缝和热固结问题中通过解析解验证 [Sun 2017, pp. 4-6]。

## Candidate Concepts
[[Enhanced Geothermal System (EGS)]], [[Hot Dry Rock (HDR)]], [[Thermal-Hydraulic-Mechanical (THM) coupling]], [[Discrete Fracture Network]], [[Fractured porous media]], [[Thermal non-equilibrium]], [[Darcy’s law]], [[Biot’s constant]], [[Habanero EGS]], [[Cooper Basin]], [[Permeability evolution]], [[Effective stress]], [[Heat extraction efficiency]]

## Candidate Methods
[[Numerical simulation]], [[COMSOL Multiphysics]], [[Discrete fracture model]], [[THM coupling model]], [[Finite element method]], [[2D stochastic fracture model]], [[Sensitivity analysis]], [[Analytical solution validation (Barends, Bai)]], [[Equations of mass conservation]], [[Energy balance equation (thermal non-equilibrium)]], [[Linear elastic constitutive law]]

## Connections To Other Work
- 本工作区别于 Jiang et al. [16,17] 的等效多孔介质模型和 Xu et al. [18] 的等效管道网络模型，将其扩展到考虑固体变形对 THM 过程的反馈作用 [Sun 2017, pp. 2-2]。
- 与 Zhao et al. [21] 的 3D 裂缝单元模型相比，本文聚焦于二维随机密集裂缝网络中的 THM 全耦合，弥补了以往研究在复杂裂缝系统中对力学效应考虑的不足 [Sun 2017, pp. 2-2]。
- 在方法验证上延续了单裂缝热-水分析的传统（如 Barends 解析解），并加入了热固结的对比，确保了模型在无裂缝情况下的可靠性 [Sun 2017, pp. 5-6]。

## Open Questions
- 如何在三维离散裂缝网络（尤其是包含剪切膨胀、裂缝滑移）中实现高效的 THM 全耦合模拟？ [Sun 2017, pp. 2-2]
- 长期运行过程中，渗透率演化是否会出现自调节或裂缝闭合现象，其对储层寿命的影响如何？
- 更精确的现场数据（如测井、示踪测试）能否进一步验证模型预测，尤其是应力变化部分？
- 控制出口温度的关键参数（如裂缝间距、初始渗透率、注入温度等）的定量敏感性结论未从索引片段中确认 [Sun 2017, pp. 1-2]。

## Source Coverage
本知识页基于提供的 11 个索引片段撰写，这些片段涵盖论文摘要、引言、方法（控制方程与耦合效应）、数值验证以及部分案例设置与初步结果。主要集中于论文前半部分，可能缺失完整的结果与讨论章节（例如详细的敏感性分析、参数敏感性排序、更深层的力学与热效率分析）以及结论部分。全篇的完整数据表和更多数值对比图未能通过索引片段获取。
