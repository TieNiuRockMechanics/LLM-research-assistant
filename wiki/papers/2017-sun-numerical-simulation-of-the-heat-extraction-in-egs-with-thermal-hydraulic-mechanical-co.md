---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co"
title: "Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model."
status: "draft"
source_pdf: "data/papers/2017 - Numerical simulation of the heat extraction in EGS with thermal-hydraulic-mechanical coupling method based on discrete fractures model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Sun, Zhi-xue, et al. \"Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model.\" *Energy*, vol. 120, 2017, pp. 20-33. doi:10.1016/j.energy.2016.10.046."
indexed_texts: "11"
indexed_chars: "53296"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53513"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004072"
coverage_status: "full-index"
source_signature: "84bb13c1cfeb84d54d4274b805772735dc20a70f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:20:14"
---

# Numerical Simulation of the Heat Extraction in EGS with Thermal-Hydraulic-Mechanical Coupling Method Based on Discrete Fractures Model.

## One-line Summary
本文提出一种基于离散裂隙模型与热‑水‑力（THM）全耦合的有限元数值方法，用于模拟增强型地热系统（EGS）在裂隙岩体中的热提取过程，并通过澳大利亚Cooper Basin案例分析了流动、传热和力学响应规律。

## Research Question
在考虑热‑水‑力耦合效应的条件下，如何利用离散裂隙网络模型准确模拟增强型地热系统的热提取性能，并揭示裂缝岩体中多物理场相互作用对出口温度的影响？

## Study Area / Data
- 研究案例：澳大利亚中部Cooper Basin Habanero增强型地热系统，目标储层为Big Lake Suite花岗岩，埋深约3600‑3800 m，温度超过244 °C[Sun 2017, pp. 5-6]。
- 计算模型：二维随机生成的裂隙网络，区域大小为300 m × 300 m；裂隙分为两组（倾角30°和110°），迹长服从正态分布（均值30 m，方差10 m）；裂隙开度0.0005 m，初始渗透率1.0 × 10⁻¹¹ m²[Sun 2017, pp. 6, Table 3]。
- 物性参数：见表3[Sun 2017, pp. 8]，包括岩石密度2700 kg/m³、比热1000 J/kg/K、导热系数3 W/m/K；水密度1000 kg/m³、比热4200 J/kg/K等。

## Methods
1. **数学模型**：基于局部热非平衡理论，建立包含岩石基质和离散裂隙的质量守恒、能量平衡和力学平衡方程组[Sun 2017, pp. 2-4]：
   - 渗流场：达西定律，裂隙质量守恒考虑法向交换项；
   - 温度场：岩石基质和裂隙水分别建立能量方程，换热项采用牛顿冷却定律（\[ q_f = h (T_s - T_f) \]）；
   - 力学场：线弹性有效应力原理，裂隙法向/切向刚度模型；
   - 耦合效应：裂隙渗透率随有效正应力指数变化（\[ k_f = k_0 \exp(-a\sigma'_n) \]），水密度和粘度随温压变化。
2. **数值实现**：使用COMSOL Multiphysics有限元软件进行全耦合求解，裂隙通过修改弱项添加到内部边界[Sun 2017, pp. 4-5]。
3. **模型验证**：
   - 单裂隙热‑水分析对比Barends解析解[Sun 2017, pp. 4-5, Fig.2]；
   - 一维热固结问题对比Bai解析解[Sun 2017, pp. 5-6, Figs.4‑6]。
4. **EGS案例模拟**：采用40年注采周期，时间步1天，施加固定压力边界（注入井80.4 MPa，生产井68.6 MPa），注入水温20 °C，初始储层200 °C[Sun 2017, pp. 6-7]。
5. **敏感性分析**：评估裂缝渗透率、岩石导热系数、注入温度、井距等对平均出口温度的影响[Sun 2017, pp. 9-13]。

## Key Findings
1. **THM耦合效应显著**：高压注水和温度变化引起岩体变形，裂缝有效正应力改变，导致渗透率上升或下降，反过来影响流体流动和热提取速率；数值结果显示了强烈耦合特征[Sun 2017, pp. 9, pp. 31-32]。
2. **裂隙网络为关键通道**：离散裂隙构成主要流动路径，热量主要在裂缝中传输，温度分布呈现强非均质性和各向异性；裂隙密集区温度下降更快[Sun 2017, pp. 8-9, Fig.12]。
3. **出口温度演化**：在基准参数下，前20年生产井温度稳定在约200 °C，随后低温区扩展到生产井，温度开始下降；40年时出口温度降至初始温度的75%‑85%[Sun 2017, pp. 9, pp. 31]。
4. **敏感性分析结果**[Sun 2017, pp. 9-13, Figs.18‑22]：
   - 裂缝渗透率对出口温度影响极大：低渗透率（0.5 × 10⁻¹¹ m²）时40年温度稳定，高渗透率则迅速降至40 °C；
   - 注入温度越低，出口温度下降越快；
   - 井距越小，热突破越早，稳定运行期缩短；
   - 岩石弹性模量通过变形影响裂隙开度，间接影响换热；
   - 岩石导热系数的影响相对有限。
5. **力学响应**：注水初期，高压和冷却引起位移场剧变；后期虽水压稳定，温度持续变化仍导致应力重分布，进一步影响裂缝渗透率[Sun 2017, pp. 9, Fig.13]。
6. **数值模型有效性**：与解析解对比验证了THM耦合模型的准确性；该模型能够描述EGS中裂缝控热、基质与流体换热的实际机制[Sun 2017, pp. 4-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 出口温度对裂缝渗透率、注入温度和井距高度敏感，岩石导热系数影响有限 | Sun 2017, p.31, p.13 | 2D随机裂隙网络，40年注采，基准参数见表3 | 敏感性分析使用方程(20)计算平均出口温度 |
| 注水后20年内生产井温度稳定在200 °C，之后逐渐下降 | Sun 2017, p.9 | 基准THM耦合工况 | 低温区扩展速度与裂缝分布相关 |
| 裂缝渗透率随有效正应力指数变化，注水过程中渗透率显著增大 | Sun 2017, p.9, Figs.15‑16 | 采用式(16)渗透率演化模型，a=‑0.2 × 10⁻⁶ Pa⁻¹ | 靠近生产井的裂缝渗透率增幅更大 |
| 数值结果与单裂隙热‑水解析解（Barends）吻合良好 | Sun 2017, p.5, Fig.2 | 单裂隙模型，有限域100 m × 100 m，恒温注入 | 微小偏差源于解析解半无限假设 |
| 耦合模型能反映THM相互作用：水压和温度变化引起变形，变形反作用于渗透率和热提取 | Sun 2017, p.9, p.31 | THM全耦合数值解 | 与Chen等[25]的离散裂隙研究结论一致 |
| 高裂缝渗透率导致出口温度在40年内急剧降至40 °C，低渗透率维持稳定 | Sun 2017, p.13, Fig.20 | 仅改变裂缝基线渗透率，其余参数同基准 | 说明裂缝导流能力主导热突破时间 |

## Limitations
1. 模型为二维，随机生成的裂隙网络可能代表性不足，未使用现场实际裂缝数据[Sun 2017, pp. 13]。
2. 计算域限制在300 m × 300 m，边界效应对长期预测的影响未讨论。
3. 渗透率演化模型中常数a的取值为假定值（‑0.2 × 10⁻⁶ Pa⁻¹），未根据具体岩性标定[Sun 2017, pp. 8]。
4. 忽略地应力初始场，仅关注注水和热提取引起的应力扰动[Sun 2017, pp. 8]。
5. 未考虑水的相变（沸腾），尽管文中论证储层条件下水不汽化[Sun 2017, pp. 2-3]。
6. 验证案例为一维热固结和无裂隙单裂缝，未涉及含复杂裂隙网络的解析解对比。

## Assumptions / Conditions
- 储层视为二维裂隙多孔介质，基质各向同性、渗透率远低于裂隙[Sun 2017, pp. 2]。
- 单相饱和液态水，不发生汽化（储层压力68.6‑80.4 MPa，最高温度473.15 K）[Sun 2017, pp. 2-3]。
- 流动遵循达西定律；传热采用局部热非平衡模型，裂隙面按牛顿冷却定律换热[Sun 2017, pp. 2-3]。
- 岩石基质为小变形线弹性，热应力以温度增量形式引入[Sun 2017, pp. 3]。
- 基质渗透率恒定，裂隙渗透率仅依赖于有效正应力（指数模型）[Sun 2017, pp. 4]。
- 水密度和粘度随温度和压力变化，采用经验公式（式17‑18）[Sun 2017, pp. 4]。
- 注入井压力80.4 MPa，生产井压力68.6 MPa，初始储层压力71.5 MPa，温度200 °C，注入水温20 °C[Sun 2017, pp. 6-8]。

## Key Variables / Parameters
| 变量/参数 | 取值 | 单位 | 说明 |
|------------|------|------|------|
| 裂隙基线渗透率 k₀ | 1.0 × 10⁻¹¹ | m² | 裂隙厚度0.0005 m |
| 岩石基质渗透率 k | 1.0 × 10⁻¹⁸ | m² | 远低于裂隙 |
| 岩石弹性模量 E | 30 | GPa | 热弹性参数 |
| 岩石泊松比 ν | 0.25 | － | |
| 热膨胀系数 αT | 5.0 × 10⁻⁶ | 1/K | |
| 对流换热系数 h | 3000 | W/m²/K | |
| 裂隙法向刚度 kn | 1200 | GPa/m | |
| 水动力粘度 η | 0.001 | Pa·s | 基准值（后续按温度修正） |
| 注入/生产压力差 | 11.8 | MPa | 80.4 ‑ 68.6 MPa |
| 井距 | 300 | m | 基准值（敏感性分析扩展至360 m、420 m） |
| 渗透率演化常数 a | ‑0.2 × 10⁻⁶ | Pa⁻¹ | 假定值 |

## Reusable Claims
- 在基于离散裂隙网络的THM耦合模型中，**裂隙渗透率随有效正应力的指数变化**（\[ k_f = k_0 \exp(-a\sigma'_n) \]）能够有效描述注采过程中岩石变形对流动能力的影响[Sun 2017, pp. 4]。此关系适用于以裂缝为主要流道的EGS储层，但常数a需针对具体裂缝特征标定。
- **EGS出口温度对裂缝渗透率、注入温度及井距高度敏感**，而对岩石本体导热系数不敏感[Sun 2017, pp. 31]。该结论基于二维随机裂隙网络的40年数值模拟，适用于类似花岗岩干热岩条件。
- 在恒定注入/生产压力边界下，**EGS系统可维持约20年的稳定出口温度（200 °C附近）**，之后低温区突破导致温度下降，20年出口温度降至初始值的75%‑85%[Sun 2017, pp. 9]。该结果可作为同类储层寿命评估的参考。
- 采用**局部热非平衡理论**分别建立岩石和流体的能量方程，能更真实地反映EGS裂隙换热中的温差传热过程[Sun 2017, pp. 3]。该方法适用于达西流速较高、换热未达瞬时平衡的裂隙流系统。
- 在模型验证中，单裂隙热‑水问题与Barends解析解的对比显示，数值方法能准确求解裂隙控热过程，误差主要源自有限计算域与半无限假设的差异[Sun 2017, pp. 5]。这一验证为后续复杂裂隙网络模拟提供了可信度基础。

## Candidate Concepts
- [[fractured porous media]]
- [[thermal non-equilibrium theory]]
- [[THM coupling]]
- [[discrete fracture network]]
- [[Darcy’s law]]
- [[Biot’s effective stress]]
- [[permeability evolution law]]
- [[Newton’s heat transfer law]]
- [[thermal consolidation]]
- [[poroelasticity]]
- [[EGS outlet temperature]]
- [[heat extraction efficiency]]
- [[fracture aperture-stress relation]]
- [[local thermal equilibrium vs. non-equilibrium]]

## Candidate Methods
- [[finite element method (FEM)]]
- [[COMSOL Multiphysics]]
- [[stochastic fracture network generation]]
- [[sensitivity analysis of geothermal parameters]]
- [[one-dimensional thermal consolidation validation]]
- [[single fracture analytical solution (Barends)]]
- [[THM full coupling solution strategy]]
- [[weak form implementation for fractures]]

## Connections To Other Work
- Jiang et al. (2013, 2014)：三维瞬态热水力模型，将储层等效为单孔隙连续介质，未考虑裂隙变形的影响[Sun 2017, pp. 2]。
- Xu et al. (2015)：基于等效管网模型的简化热水耦合模拟，同样忽略力学过程[Sun 2017, pp. 2]。
- Shaik et al. (2011)：天然裂缝地热系统的流‑热耦合数值研究，动态更新裂缝属性，但未耦合应力场[Sun 2017, pp. 2]。
- Bahrami et al. (2015)：利用孔弹性理论建立自支撑单裂缝THM模型，但难以扩展至密集裂缝网络[Sun 2017, pp. 2]。
- Zhao et al. (2015)：基于Goodman节理单元的三维THM耦合模型，针对深部单裂缝/少量裂缝，未系统考虑裂隙网络效应[Sun 2017, pp. 2]。
- Chen et al. (2014)：采用离散裂隙模型进行二维岩体流动与传热模拟，本文进一步引入力学耦合[Sun 2017, pp. 8]。
- Barends (2010) 和 Bai (2005)：分别提供单裂隙热输运和一维热固结解析解，用于本文模型验证[Sun 2017, pp. 5-6]。

## Open Questions
1. 如何将二维随机裂隙网络模型推广至三维实际裂缝系统，并利用现场微震监测数据约束裂缝几何参数？[Sun 2017, pp. 13]
2. 渗透率演化模型中常量a的确定方法及在不同岩性、裂缝粗糙度条件下的适用性仍需实验或现场标定。
3. 长期（>40年）THM耦合作用下，热‑化学效应（如矿物溶解沉淀）是否会影响裂缝开度和系统稳定性？
4. 更真实的初始地应力场和复杂边界条件（如多井系统）对EGS性能的预测影响如何？
5. 局部热非平衡模型中换热系数h的取值对结果敏感性的系统研究尚未开展。

## Source Coverage
All 11 non-empty indexed source blocks were processed.  
- Indexed text blocks: 11  
- Total indexed characters: 53,296  
- Compiled source blocks: 11  
- Compiled source characters: 53,513  
- Coverage by blocks: 1.0  
- Coverage by characters: 1.004  

The compiled page utilizes every provided fragment; no additional sources were used or fabricated.
