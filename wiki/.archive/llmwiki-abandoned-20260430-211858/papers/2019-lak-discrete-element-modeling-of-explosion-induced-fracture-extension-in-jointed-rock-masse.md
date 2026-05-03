---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-lak-discrete-element-modeling-of-explosion-induced-fracture-extension-in-jointed-rock-masse"
title: "Discrete Element Modeling of Explosion-Induced Fracture Extension in Jointed Rock Masses."
status: "draft"
source_pdf: "data/papers/2019 - Discrete element modeling of explosion-induced fracture extension in jointed rock masses.pdf"
collections:
citation: "Lak, M., et al. \"Discrete Element Modeling of Explosion-Induced Fracture Extension in Jointed Rock Masses.\" *Journal of Mining and Environment*, vol. 10, no. 1, 2019, pp. 125-38. DOI: 10.22044/jme.2018.7291.1579."
indexed_texts: "8"
indexed_chars: "39189"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:56:43"
---

# Discrete Element Modeling of Explosion-Induced Fracture Extension in Jointed Rock Masses.

## One-line Summary
该研究提出一种双重裂隙介质方法，结合离散元法（DEM）与Voronoi镶嵌技术，模拟节理岩体中爆炸诱发的既有裂隙活化与新裂纹起裂、扩展过程，并应用于预裂爆破效果的评估 [Lak 2019, pp. 1-2]。

## Research Question
如何在离散元框架下同时考虑岩体节理（固有裂隙）和爆炸新生的完整岩块破裂，以模拟爆炸诱发的动态裂隙扩展？该问题衍生自爆破工程中节理岩体对冲击载荷的空间非连续响应 [Lak 2019, pp. 2-3]。

## Study Area / Data
模型中的节理几何参数来源于伊朗亚兹德省 Choghart 铁矿北坡的实地调查数据，物理力学性质由该矿区的实验室测试提供 [Lak 2019, pp. 3-5]。

## Methods
- **离散元方法 (DEM)** ：采用基于显式有限差分的程序（如 UDEC）求解全动态运动方程，将岩块视为可变形体，内部由有限差分区域组成 [Lak 2019, pp. 5-6, 6-10]。
- **双重裂隙介质模拟**：
    - 用**离散裂隙网络 (DFN)** 随机生成岩体中的固有节理，遵循统计分布 [Lak 2019, pp. 2-5]。
    - 用**Voronoi 镶嵌技术**将完整岩块分割为次生块体，并在其接触面上设置接近完整岩的力学性质，从而允许新裂纹在“完整”岩体中萌生和扩展 [Lak 2019, pp. 2-5]。
- **动态分析设置**：
    - **输入脉冲**：铵油炸药（ANFO）爆轰产生的压力脉冲，密度 0.8 g/cm³，爆速 2400 m/s，压力由材料密度和爆速的经验公式计算 [Lak 2019, pp. 5-6]。
    - **边界条件**：模型外边界施加粘性非反射条件以消除应力波反射 [Lak 2019, pp. 6-10]。
    - **阻尼**：采用 Rayleigh 阻尼（质量比例+刚度比例），自然阻尼比落在 2–5% 临界阻尼范围 [Lak 2019, pp. 6-10]。
    - **单元尺寸**：为保证波形保真，单元尺寸小于约 1/10–1/8 波长，通过无阻尼自振获得模型自然频率（270 Hz），并对输入波加速度做 FFT 得到卓越频率（2213 Hz）来控制 [Lak 2019, pp. 5-6]。
- **模型几何**：考虑爆孔的径向截面（5×5 m）和纵向截面（5×10 m），爆孔半径 0.05 m [Lak 2019, pp. 3-5]。
- **预裂爆破模拟**：在爆破孔后方预设 0.03 m 宽的空隙，对比有无预裂情况下裂隙扩展模式 [Lak 2019, pp. 10-13]。

## Key Findings
- 双重裂隙介质方法（DFN+Voronoi）能够模拟节理岩体中爆炸冲击波导致的裂隙延伸，包括沿既有节理面的滑动/张开以及完整岩桥的断裂 [Lak 2019, pp. 13-14]。
- 径向和纵向截面中的质点速度图展现了不同时刻的冲击阵面和能量传播特征 [Lak 2019, pp. 6-10]。
- 预裂间隙能有效阻挡爆炸裂隙向爆孔后方（保留岩体）扩展，与无预裂情况相比，后方节理的延伸和新裂纹形成明显受限 [Lak 2019, pp. 10-13]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 模型自然频率 270 Hz，输入波卓越频率 2213 Hz（FFT 结果） | [Lak 2019, pp. 5-6] | 模型无阻尼自振；输入波为 ANFO 爆轰脉冲 | 用于确定单元尺寸上限 |
| 爆轰压力 Pd 依赖于炸药密度和爆速，由公式 (6) 计算 | [Lak 2019, pp. 5-6] | ANFO 炸药，ρe=0.8 g/cm³, Vd=2400 m/s | 公式见原文 (6)，考虑成分差异 |
| 采用 Rayleigh 阻尼（质量+刚度比例），自然阻尼建议 2–5% 临界阻尼 | [Lak 2019, pp. 6-10] | 动力时程分析 | 引用 Itasca(2000) & Cundall(1990) |
| 无预裂模型爆后 1 ms 内裂隙由孔壁向四周岩体延伸 | [Lak 2019, pp. 10-13] | 二维径向模型，节理岩体 | 裂隙模式见图 13 |
| 预裂模型（0.03 m 间隙）中，爆炸区后方裂隙延伸被显著抑制 | [Lak 2019, pp. 10-13] | 相同岩体几何和输入载荷 | 裂隙模式见图 14 |

## Limitations
- 未从索引片段中确认模型是否经过实际爆破试验验证，可能仅停留在数值算例阶段。
- 爆炸模拟仅考虑了冲击波阶段，未包含爆炸气体压力驱动的二次裂隙扩展（文中指出爆炸包含冲击波和气体膨胀两阶段，而本研究以冲击波作为动态输入） [Lak 2019, pp. 13-14]。
- 节理网络参数仅源自单一矿山（Choghart），其普遍适用性未从片段中确认。
- 未从索引片段中确认是否讨论了三维效应、非均质应力场以及高应变率下岩石动态强度增强等因素。
- Voronoi 次生块体接触的力学参数是为逼近完整岩行为而人为标定的，与真实新裂隙萌生准则的吻合程度未在片段中讨论 [Lak 2019, pp. 3-5]。

## Assumptions / Conditions
- **双重裂隙介质假设**：DFN 生成的裂隙代表岩体中的真实节理，而 Voronoi 边缘代表潜在的完整岩破裂路径，其接触性质经过校准以模拟完整岩强度 [Lak 2019, pp. 2-5]。
- **动态载荷简化**：爆炸载荷简化为一个压力脉冲，忽略后续爆生气体的准静态加压作用 [Lak 2019, pp. 13-14]。
- **材料行为**：岩块自身为弹性或弹塑性可变形体，采用有限差分区域计算应力/应变；节理和 Voronoi 接触可能遵循库仑滑移等本构（具体本构未在片段中给出）。
- **边界条件**：模型周边设置粘性（非反射）边界，以模拟无限岩体中的波传播 [Lak 2019, pp. 6-10]。
- **阻尼模型**：采用 Rayleigh 阻尼，并假定阻尼比在 2–5% 范围内，该假设常用于岩土类材料 [Lak 2019, pp. 6-10]。
- **单元尺寸准则**：为保证应力波数值传递的准确性，单元尺寸小于波长的 1/10–1/8，波长由卓越频率和波速决定 [Lak 2019, pp. 5-6]。
- **炸药参数**：爆炸源采用 ANFO 典型工业炸药参数 [Lak 2019, pp. 5-6]。

## Key Variables / Parameters
- **几何**：爆孔半径 0.05 m；径向模型 5×5 m，纵向模型 5×10 m；预裂间隙 0.03 m [Lak 2019, pp. 3-5, 10-13]。
- **动态输入**：爆轰压力 Pd（由公式 (6) 关联的 ρe 和 Vd 计算）；冲击波形状与持续时长 [Lak 2019, pp. 5-6]。
- **频率与阻尼**：模型自然频率 270 Hz；输入波卓越频率 2213 Hz；Rayleigh 阻尼系数 γ、δ [Lak 2019, pp. 5-6, 6-10]。
- **节理参数**：DFN 的几何参数（如迹长、间距、方位分布等，具体值见于原文 Table 1，片段未列出） [Lak 2019, pp. 3-5]。
- **接触力学性质**：Voronoi 次生块体之间的接触强度、刚度等，其特定数值未从片段中确认。

## Reusable Claims
1. “在离散元模型中，采用 DFN 表征既有节理，同时用 Voronoi 镶嵌网格分割完整岩块并赋予较高接触强度，可以模拟爆炸载荷下既有裂隙的剪切/张开与完整岩桥的次生裂纹萌生。”  
   *适用条件*：岩体具有统计可描述的节理网络，且爆炸载荷主要体现为应力波传播。  
   *证据与限制*：计算实例表明该方法能再现裂隙延伸模式 [Lak 2019, pp. 2-5, 13-14]，但未验证次生裂纹的起裂强度是否与实际动态断裂韧性一致。

2. “为确保离散元动态计算中应力波的数值精度，局部单元尺寸应不大于波长的 1/10 至 1/8，且可通过模型无阻尼自振得出自然频率、通过输入波 FFT 得到卓越频率，从而估算最小波长。”  
   *适用条件*：显式有限差分或离散元动力分析，输入为脉冲型动态载荷。  
   *证据与限制*：本研究据此采用 270 Hz 自然频率与 2213 Hz 卓越频率确定网格尺寸 [Lak 2019, pp. 5-6]；该准则普遍适用于波动问题，但需根据实际波速和频谱灵活调整。

3. “在节理岩体中采用预裂爆破（形成连续空腔或裂隙面）可有效阻挡主体爆破裂隙向预留岩体的扩展，这可由离散元模拟中预裂间隙附近节理与新裂纹的阻断效应直观显现。”  
   *适用条件*：节理发育的岩质边坡或矿岩，且预裂缝形成时间先于主爆区起爆。  
   *证据与限制*：数值算例对比了有无 0.03 m 预裂间隙的裂隙模式，显示裂隙被抑制 [Lak 2019, pp. 10-13]；该现象依赖于预裂缝的隔离效果，未考虑实际中预裂缝闭合、偏斜的可能性。

## Candidate Concepts
- [[Discrete Element Method]]
- [[Discrete Fracture Network]]
- [[Voronoi tessellation]]
- [[explosion-induced fracturing]]
- [[jointed rock mass]]
- [[pre-splitting (controlled blasting)]]
- [[dynamic wave propagation]]
- [[Rayleigh damping]]
- [[non-reflecting boundary]]
- [[shock wave pulsation]]
- [[fracture extension]]

## Candidate Methods
- [[Dual fracture media approach]]
- [[Distinct Element Method (UDEC)]]
- [[Fast Fourier Transform (FFT) for frequency analysis]]
- [[DFN stochastic generation]]
- [[Voronoi sub-block fracturing]]
- [[controlled blasting simulation]]
- [[dynamic viscous boundary condition]]

## Connections To Other Work
- 片段中提及，此前爆破模拟多将岩体视为连续介质，或仅考虑单条预存裂纹/断层的影响，而本工作引入 DFN+Voronoi 双重裂隙方法，实现了节理群体与新生破裂的耦合 [Lak 2019, pp. 2-3]。
- 概念上，本研究继承了早期 DEM 爆破模拟（如 Saharan & Mitri 2008; Zhu et al. 2007）和双重介质流体模型（如 [32],[33]）的思想，可连接到 [[fracture reservoir]] 的离散裂隙网络建模、[[dynamic fracture mechanics]] 以及 [[wave propagation in jointed rock]] 等领域。

## Open Questions
- 实际的爆炸气体压力如何进一步驱动裂隙扩展，并且如何与冲击波引发的初始破裂网络相互作用，未从索引片段中确认。
- 模型参数（尤其是 Voronoi 接触强度）的标定是否基于真实动态断裂实验，片段未提供细节。
- 数值结果是否与现场实测的爆后裂隙分布或块度进行过对比验证，未提及。
- 三维情况、高地应力或含水节理对爆炸裂隙扩展的调控作用尚未在本文中探讨。

## Source Coverage
本页面依据 8 个索引片段撰写，覆盖了论文的摘要、引文/理论背景、模型几何与参数设定、动态分析方法、部分结果（粒子速度图、裂隙扩展模式）以及结论，并包含了预裂爆破的应用示例。片段中未提供节理网络的具体统计参数（Table 1）、完整的岩体力学输入参数、网格敏感性分析或模型验证结果。部分方法细节（如节理和 Voronoi 接触本构的具体形式）仅能根据有限差分/DEM 常规知识推断，原始文献的完整限制条件和参数列表仍属缺失。
