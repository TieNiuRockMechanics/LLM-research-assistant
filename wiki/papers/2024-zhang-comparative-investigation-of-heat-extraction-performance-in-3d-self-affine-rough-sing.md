---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-zhang-comparative-investigation-of-heat-extraction-performance-in-3d-self-affine-rough-sing"
title: "Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid."
status: "draft"
source_pdf: "data/papers/2024 - Comparative investigation of heat extraction performance in 3D self-affine rough single fractures using CO2,N2O and H2O as heat transfer fluid3D.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhang, Jiansong, et al. \"Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid.\" *Renewable Energy*, vol. 235, 2024, p. 121309. doi:10.1016/j.renene.2024.121309."
indexed_texts: "12"
indexed_chars: "59008"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59259"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004254"
coverage_status: "full-index"
source_signature: "25a77161d52374042b1c90c864653e3c3609828d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:18:55"
---

# Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid.

## One-line Summary
本文针对岩心尺度（φ50×100 mm）三维自仿射粗糙单裂隙，利用数值模型对比了CO₂、N₂O和H₂O作为传热流体在不同入口流速（0.005–0.025 m/s）和入口温度（37–57 °C）下出口平均温度和提取热率（HER）的变化规律，发现H₂O的取热性能最优，CO₂与N₂O性能相近且均低于H₂O；流速是影响对流换热的主导因素，温度是影响传导换热的主导因素[Zhang 2024, pp. 15-16]。

## Research Question
在岩心尺度的干热岩（HDR）粗糙单裂隙中，CO₂、N₂O和H₂O三种传热流体的热提取性能有何差异？入口流速和入口温度如何影响出口平均温度和热提取率？[Zhang 2024, pp. 1-1]

## Study Area / Data
- **物理对象**：岩心尺度（φ50×100 mm）的花岗岩单裂隙，裂隙宽度1 mm，围岩温度200 °C，压力30 MPa，代表深层干热岩（HDR）增强型地热系统（EGS）的裂隙特征[Zhang 2024, pp. 3-4, 8-11]。  
- **裂隙几何**：采用具备分形自仿射特性的Weierstrass-Mandelbrot（W‑M）函数生成，分形维数D=2.5，标度常数G=1.5，频率密度γ=1.5，叠加隆起数M=10，最大频率n_max=10；计算得到裂隙表面峰值粗糙度ξ=2.78 mm，均方根粗糙度RMS=0.42 mm，平均粗糙度Rm=0.33 mm，节理粗糙度系数JRC=12.38[Zhang 2024, pp. 4-7]。  
- **流体热物性数据**：来自NIST REFPROP v9.1，温度范围37–300 °C，压力30 MPa，三种流体均处于超临界（CO₂、N₂O）或液态（H₂O），密度、比热容、导热系数、动力粘度通过实测数据拟合为分段解析式（式9–20）[Zhang 2024, pp. 7-8]。

## Methods
- **几何建模**：使用W‑M函数（式1‑3）生成具有自仿射特征的粗糙裂隙表面，并依据剖分线的高度分布验证其正态性（x=10,20,30,40 mm；y=20,40,60,80 mm）[Zhang 2024, pp. 4-7]。  
- **多物理场耦合**：建立热‑水力（TH）耦合数学模型，控制方程包括质量守恒（式21）、动量守恒（式22）、流体能量守恒（式23）和固相能量守恒（式24），忽略岩石基质的渗透、流体的汽化及化学作用[Zhang 2024, pp. 7-8]。  
- **数值求解**：采用COMSOL Multiphysics有限元软件，直接求解器，瞬态时间步长1 s，总时长800 s，收敛判据相对容差1e‑3；网格数约10万，经独立性验证出口平均温度变化可忽略[Zhang 2024, pp. 9-10]。  
- **模型验证**：利用已有的水在粗糙单裂隙中的实验结果与光滑裂隙解析解，出口温度误差≤3.8%；利用CO₂在光滑裂隙中的实验结果，出口温度误差≤2.4%[Zhang 2024, pp. 8-8]。  
- **评价参数**：出口平均温度T_out(t)采用面积加权积分（式29），热提取率P采用温度差、比热、密度和速度的面积积分（式30）[Zhang 2024, pp. 11-12]。

## Key Findings
1. **流体间性能排序**：在相同入口流速和温度下，CO₂与N₂O的出口平均温度和HER基本一致，均显著低于H₂O；其根本原因是CO₂与N₂O的四项基本热物性（密度、比热、粘度、导热系数）相近，而H₂O与之差异明显[Zhang 2024, pp. 15-15]。  
2. **流速主导机制**：当入口流速从0.005 m/s增至0.025 m/s时，裂隙内岩石基质向流体的热对流效应起主导作用，流速是影响流体与岩石传热的主要因素；随流速增大，稳态出口平均温度下降，低 温区由入口向深部扩展[Zhang 2024, pp. 14-14]。  
3. **温度主导机制**：当入口温度从37 °C升至57 °C时，岩石基质向流体的热传导效应起主导作用，温度是影响传热过程的主要因素；稳态下低 温区范围变窄[Zhang 2024, pp. 14-14]。  
4. **出口温度变化量**：恒温下流速由0.005→0.025 m/s，CO₂出口平均温度最大降幅64.94 °C，N₂O降62.61 °C，H₂O降75.69 °C[Zhang 2024, pp. 14-14]；恒速下温度由37→57 °C，CO₂出口平均温度最大升幅8.3 °C，N₂O升7.73 °C，H₂O升11.14 °C[Zhang 2024, pp. 14-15]。  
5. **热提取率增幅**：恒温下流速增加，CO₂的HER最大增加118.85 W，N₂O增加117.05 W，H₂O增加266.4 W[Zhang 2024, pp. 14-14]；恒速下温度增加，CO₂的HER最大增加15.34 W，N₂O增加13.9 W，H₂O增加45.45 W[Zhang 2024, pp. 15-15]。  
6. **动态粘度影响**：N₂O在较高流速下出口平均温度略高于CO₂和H₂O，主要因其粘度较低（见式12、16、20及图8），表明在四项热物性中动态粘度对出口平均温度影响最大[Zhang 2024, pp. 11-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| CO₂与N₂O的出口平均温度和HER基本相同，均低于H₂O | [Zhang 2024, pp. 15-15] | 入口流速0.005–0.025 m/s，入口温度37–57 °C，压力30 MPa，JRC=12.38 | 结论(1)，与Okoroafor等人（2022）和Liu等人（2022）结果一致 |
| 流速由0.005→0.025 m/s（恒温），CO₂出口温度降64.94 °C，N₂O降62.61 °C，H₂O降75.69 °C | [Zhang 2024, pp. 14-14] | 入口温度37 °C（选取），压力30 MPa | 图19数据，流速是热对流主导因素 |
| 温度由37→57 °C（恒速），CO₂出口温度升8.3 °C，N₂O升7.73 °C，H₂O升11.14 °C | [Zhang 2024, pp. 14-15] | 入口流速0.025 m/s（选取），压力30 MPa | 图22数据，温度是热传导主导因素 |
| 恒温条件下流速增加，CO₂的HER最大增幅118.85 W，N₂O 117.05 W，H₂O 266.4 W | [Zhang 2024, pp. 14-14] | 入口温度37 °C，压力30 MPa | 图20数据 |
| 恒速条件下温度增加，CO₂的HER最大增幅15.34 W，N₂O 13.9 W，H₂O 45.45 W | [Zhang 2024, pp. 15-15] | 入口流速0.025 m/s，压力30 MPa | 图23数据 |
| 动态粘度是影响出口平均温度最重要的热物性参数 | [Zhang 2024, pp. 11-12] | 对比N₂O与CO₂、H₂O温度曲线，结合粘度随温度变化（式12、16、20） | 源于图14分析 |
| JRC=12.38的裂隙由W‑M函数生成，分形维数D=2.5 | [Zhang 2024, pp. 4-6] | L=100，γ=1.5，G=1.5，M=10，n_max=10 | 方法基础 |
| 模型验证：水出口温度误差≤3.8%，CO₂误差≤2.4% | [Zhang 2024, pp. 8-8] | 与实验（Zhao & Tso，1993；Jiang等人，2017）及解析解（Zhao，2014）对比 | 保证数值可靠性 |

## Limitations
- 仅考虑单一粗糙裂隙，未涉及裂隙网络或多裂隙相互作用[Zhang 2024, pp. 1-3]。  
- 耦合物理场限于热‑水力（TH），未包括力学变形（THM）或化学作用（THMC）[Zhang 2024, pp. 15-16]。  
- 岩石基质假设为零渗透率，流体无汽化，无岩石‑流体化学反应[Zhang 2024, pp. 7-8]。  
- 边界条件设定为岩体外围温度恒定为200 °C，未考虑实际地温梯度及远场热补给变化[Zhang 2024, pp. 8-11]。  
- 流体热物性拟合基于30 MPa定压，未讨论压力变化对物性及取热性能的影响[Zhang 2024, pp. 7-8]。  
- 研究尺度为岩心级（mesoscopic），直接应用于现场EGS需谨慎尺度升级[Zhang 2024, pp. 3-4]。

## Assumptions / Conditions
- 岩石基质无渗透性，流体仅在裂隙内流动[Zhang 2024, pp. 7-8]。  
- 流体在裂隙内不发生相变（无汽化）[Zhang 2024, pp. 7-8]。  
- 岩石与流体之间无化学反应[Zhang 2024, pp. 7-8]。  
- 热储层温度和压力范围为37–200 °C和20–40 MPa，但流体物性拟合扩展至37–300 °C以涵盖局部高温可能[Zhang 2024, pp. 7-8]。  
- 裂隙入口和出口端面（岩石部分）设为绝热，岩石外表面恒温200 °C[Zhang 2024, pp. 8-11]。  
- 裂隙宽度固定为1 mm，不考虑应力导致的孔径变化[Zhang 2024, pp. 9-9]。  
- 三种流体在给定条件下CO₂和N₂O为超临界态，H₂O为液态，保证可比性[Zhang 2024, pp. 8-8]。

## Key Variables / Parameters
| Parameter | Value/Description | Source |
|-----------|-------------------|--------|
| 裂隙宽度 | 1 mm | [Zhang 2024, pp. 9-9] |
| 岩石直径 | 50 mm | [Zhang 2024, pp. 9-9] |
| 岩石长度 | 100 mm | [Zhang 2024, pp. 9-9] |
| 入口流速范围 | 0.005, 0.015, 0.025 m/s | [Zhang 2024, pp. 9-9] |
| 入口温度范围 | 37, 47, 57 °C | [Zhang 2024, pp. 9-9] |
| 岩石外壁温度 | 200 °C | [Zhang 2024, pp. 9-9] |
| 出口压力 | 30 MPa | [Zhang 2024, pp. 8-8] |
| 花岗岩密度 | 2700 kg/m³ | [Zhang 2024, pp. 9-9] |
| 花岗岩比热容 | 1000 J/(kg·°C) | [Zhang 2024, pp. 9-9] |
| 花岗岩导热系数 | 2.4 W/(m·°C) | [Zhang 2024, pp. 9-9] |
| JRC | 12.38 | [Zhang 2024, pp. 4-6] |
| 流体热物性 | 根据NIST REFPROP拟合的密度、比热、导热系数、动力粘度随温度的变化式（Eq.9‑20） | [Zhang 2024, pp. 7-8] |

## Reusable Claims
- 对于JRC=12.38的岩心尺度假定粗糙单裂隙，在30 MPa、背景岩温200 °C的条件下，H₂O的热提取率始终高于CO₂和N₂O，且后两者性能相当；当入口流速从0.005 m/s增至0.025 m/s时，H₂O的HER增幅（266.4 W）约为CO₂（118.85 W）和N₂O（117.05 W）的2.25倍[Zhang 2024, pp. 14-14, 15-15]。  
- 在恒定入口温度下增大流速，出口平均温度下降，低流速下CO₂与N₂O温降曲线几乎重合，高流速下N₂O出口温度略高于CO₂和H₂O，归因于N₂O相对较低的动态粘度[Zhang 2024, pp. 11-12]。  
- 流速是控制对流换热的主动因素；温度是控制热传导的主动因素。当温度固定、流速变化时，传热由对流主导；流速固定、温度变化时，传热由传导主导[Zhang 2024, pp. 14-14]。  
- 裂隙表面的温度分布沿剖分线呈波状起伏，主要受裂隙几何曲折度影响，入口流速增大使波动加剧，而入口温度变化对波动形态影响较小[Zhang 2024, pp. 12-13]。  
- 采用W‑M函数可以生成符合正态高度分布的自仿射粗糙裂隙，通过调节分形维数D和标度常数G可控制粗糙度，本案例中JRC=12.38、RMS=0.42 mm、Rm=0.33 mm，为类似岩心尺度研究提供了可控的几何参考[Zhang 2024, pp. 4-6]。

## Candidate Concepts
- [[自仿射粗糙裂隙 (self-affine rough fracture)]]
- [[热提取率 (heat extraction rate, HER)]]
- [[出口平均温度 (outlet mean temperature)]]
- [[节理粗糙度系数 JRC]]
- [[Weierstrass-Mandelbrot函数]]
- [[热-水力耦合 (TH coupling)]]
- [[超临界CO₂传热流体]]
- [[超临界N₂O传热流体]]
- [[增强型地热系统 EGS]]
- [[干热岩 HDR]]
- [[动态粘度主导传热]]
- [[热对流主导区与热传导主导区]]
- [[岩心尺度模型 (core-scale model)]]

## Candidate Methods
- [[W-M函数生成三维粗糙裂隙几何]]
- [[NIST REFPROP数据库热物性拟合（密度、比热、导热系数、粘度）]]
- [[COMSOL多物理场瞬态有限元求解]]
- [[出口平均温度面积加权积分（式29）]]
- [[热提取率P的积分定义（式30）]]
- [[网格独立性验证]]
- [[基于剖分线的高度正态分布检验]]
- [[裂隙表面温度轮廓图分析]]
- [[实验数据与解析解双重模型验证（水、CO₂出口温度）]]

## Connections To Other Work
- 研究结果与Okoroafor等人[17]关于高注入速率下水的取热率高于CO₂的结论一致，但未涉及裂隙非均匀孔径的影响[Zhang 2024, pp. 15-15]。  
- 与Huang等人[18]的单裂隙双井EGS研究相比，本文使用了具有粗糙度的三维裂隙，而Huang等人采用光滑垂直裂隙；本文发现N₂O与CO₂性能相近，而Huang等人报道N₂O热提取功率更高，差异可能源于裂隙几何与边界条件[Zhang 2024, pp. 3-4, 15-15]。  
- 与Liu等人[19]的二维随机裂隙网络研究一致，均得出N₂O和CO₂的热提取功率基本相同的结论[Zhang 2024, pp. 15-15]。  
- 模型验证引用了Zhao & Tso（1993）的水-裂隙传热实验、Jiang等人（2017）的CO₂-光滑裂隙实验以及Zhao（2014）的光滑裂隙解析解，证实TH耦合模型在岩心尺度具有良好精度[Zhang 2024, pp. 8-8]。

## Open Questions
- 在热-水力-力学（THM）和热-水力-力学-化学（THMC）多场耦合下，不同传热流体的热提取性能将如何变化？这是论文明确的未来工作方向[Zhang 2024, pp. 15-16]。  
- 裂隙粗糙度（JRC）取单一数值（12.38），不同粗糙度水平对三种流体取热性能差异的影响程度尚未量化。  
- 本文仅考虑恒定压力30 MPa，实际EGS中裂隙压力随注入、生产动态变化，压力变动对超临界流体密度和粘度的耦合效应有待探索。  
- 岩心尺度结果如何扩展到米级或场级裂隙网络仍存在尺度效应问题，需结合裂隙网络随机模拟进一步验证。

## Source Coverage
本次编译使用论文《Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid》（Renewable Energy, 2024）的全部12个非空索引碎片（来源块），共覆盖59,259字符，索引覆盖率为1.0（按字符计）。未插入任何外部信息，所有事实性陈述均附原文页号标注。
