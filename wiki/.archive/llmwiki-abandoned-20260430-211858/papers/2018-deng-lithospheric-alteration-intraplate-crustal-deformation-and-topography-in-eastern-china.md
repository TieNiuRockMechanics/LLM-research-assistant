---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-deng-lithospheric-alteration-intraplate-crustal-deformation-and-topography-in-eastern-china"
title: "Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China."
status: "draft"
source_pdf: "data/papers/2018 - Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.pdf"
collections:
  - "山西断裂地质构造"
citation: "Deng, Yangfan, and Will Levandowski. \"Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.\" *Tectonics*, vol. 37, 2018, pp. 4120–4134. doi:10.1029/2018TC005079. Accessed 2026."
indexed_texts: "13"
indexed_chars: "61475"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:06:50"
---

# Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.

## One-line Summary
联合地震速度、重力和地形数据，发现中国东部地形梯度带(TGB)两侧地壳浮力过度补偿、岩石圈厚度差异显著，并探讨了水化与动态地形对岩石圈改造的影响 [Deng 2018, pp. 1-1]。

## Research Question
中国东部显著的沿走向地形梯度带(TGB)是如何被岩石圈结构所控制的？如何定量区分地壳、地幔岩石圈温度/成分以及软流圈流动对板内地形和变形的贡献？[Deng 2018, pp. 1-1, 1-4]

## Study Area / Data
**研究区**：中国东部，涵盖华北克拉通（西块WNCC、中部造山带TNCO、东块ENCC）、华南（扬子与华夏地块）、秦岭-大别、东北地区等。  
**主要数据与来源**：
- S波速度模型 (Shen et al., 2016) 用以构建初始密度 [Deng 2018, pp. 1-4]。
- 接收函数莫霍深度 (Y. Li et al., 2014) [Deng 2018, pp. 1-4]。
- 地壳温度模型（由地表热流、P波速度和3-D稳态热传导方程联合约束）(Sun et al., 2013) [Deng 2018, pp. 1-4]。
- 地形与布格重力异常 [Deng 2018, pp. 1-1]。
- 弹性厚度通过多窗口谱估计法 (Pérez-Gussinyé et al., 2004) 计算，窗口尺寸600×600 km [Deng 2018, pp. 7-9]。

## Methods
1. **构建初始密度模型**：利用S波速度转换为密度 [Deng 2018, pp. 1-4]。
2. **联合反演**：将初始密度模型同时拟合观测地形和重力残差，精化地壳密度结构（容许残差分别≤0.05 km和≤5 mGal）[Deng 2018, pp. 5-7]。
3. **计算地壳对地形的贡献（Hc）**：使用精化密度模型与接收函数给出的莫霍深度，按公式 \( H_c = \int_{Moho}^{topo} \frac{1}{\rho_a}(\rho_a - \rho_c(z))\,dz \) 计算，其中 \( \rho_a = 3200\,\text{kg/m}^3 \) [Deng 2018, pp. 4-5, 7-9]。
4. **估算地幔岩石圈厚度（Tml）**：假设挠曲均衡，由剩余地形（\( E - H_c - H_0 \)，\( H_0=2.4\,\text{km} \) 为洋中脊参考项）反推，并采用线性地热梯度（莫霍温度 \( \theta_c \) 至岩石圈-软流圈边界温度 \( \theta_a=1350^\circ\text{C} \)，热膨胀系数 \( \delta=4.0\times10^{-5}/^\circ\text{C} \)）计算地幔岩石圈平均密度，最终解出Tml [Deng 2018, pp. 4-5]。
5. **不确定性评估**：分别从莫霍深度不确定性和温度不确定性传导至岩石圈厚度 [Deng 2018, pp. 9-10]。

## Key Findings
- **密度残差的区域格局**：初始密度模型预测的残差重力可达80 mGal，残差地形达0.6 km，且呈显著的东-西差异 [Deng 2018, pp. 5-7]。
- **地壳贡献的过度补偿**：TGB以东的Hc典型值约3.6 km，而以西多超过4.2 km，最高达6.0 km；Hc的横向差异（~1 km/200 km）过度补偿了实际地表高程的变化 [Deng 2018, pp. 7-9]。
- **岩石圈厚度与TGB的对应**：TGB大致相当于110 km岩石圈厚度等值线（东北地区和秦岭-大别除外）[Deng 2018, pp. 9-10]。
- **东部岩石圈显著减薄**：TGB以东（如ENCC与华南东南部）岩石圈厚度仅~90 km，而西部的四川盆地和鄂尔多斯盆地岩石圈最厚 [Deng 2018, pp. 9-10]。
- **弹性厚度分异**：扬子、华夏地块弹性厚度~15 km，而四川盆地东部和WNCC弹性厚度>60 km [Deng 2018, pp. 7-9]。
- **水化效应**：若TGB以东地幔岩石圈含1%蛇纹石化，密度相对软流圈的正差会从+50 kg/m³降至+42 kg/m³，所匹配的岩石圈厚度由90 km增至~100 km，削弱厚度东西差异 [Deng 2018, pp. 11-12]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 初始密度模型产生高达80 mGal的残差重力与0.6 km的残差地形，且呈东-西差异 | [Deng 2018, pp. 5-7] | 基于S波速度转换，未精化 | 东部残差平均值与西部差异不显著，显示区域尺度偏差 |
| Hc在TGB以东约3.6 km，以西>4.2 km，最高6.0 km | [Deng 2018, pp. 7-9] | 精化密度模型与接收函数莫霍深度 | Hc与莫霍深度呈线性正相关 |
| TGB与110 km岩石圈厚度等值线大致一致，不包括东北和秦岭-大别 | [Deng 2018, pp. 9-10] | 挠曲均衡、线性地热、给定θa、δ等 | 东部最薄~90 km，四川、鄂尔多斯最厚 |
| 莫霍深度不确定性<4 km导致Hc不确定性~0.13 km，进而引起岩石圈厚度不确定性~8 km | [Deng 2018, pp. 9-10] | 假设最下地壳密度3000 kg/m³ | 不确定性占东部岩石圈厚度的~9%，西部的<7% |
| 莫霍温度不确定性<100°C，造成地幔岩石圈密度变化±6.4 kg/m³ | [Deng 2018, pp. 9-10] | 基于三维稳态热传导方程与地震速度约束 (Sun et al., 2013) | 温度不确定性对厚度的影响见图9 |
| 扬子、华夏弹性厚度~15 km，四川盆地东部、WNCC弹性厚度>60 km | [Deng 2018, pp. 7-9] | 多窗口谱估计，600×600 km窗口 | NSGL整体呈低弹性厚度 |
| 1%蛇纹石化使地幔岩石圈密度降低~8 kg/m³，可把模型所需的东部岩石圈厚度从90 km提高至~100 km | [Deng 2018, pp. 11-12] | 根据Christensen (2004) 和Hacker & Abers (2004) 的数据类推 | 仅为示意性计算，非反演约束 |

## Limitations
- 莫霍深度和温度输入的不确定性虽然量化，但仍可能低估真实变化，尤其温度在构造活跃区不满足稳态假设 [Deng 2018, pp. 9-10, 11-12]。
- 挠曲均衡计算未充分纳入动态地形；若存在软流圈上涌/下涌，会系统性地改变反演的岩石圈厚度 [Deng 2018, pp. 10-11]。
- 水化与成分影响仅通过示例性计算讨论，未进行联合约束 [Deng 2018, pp. 11-12]。
- 东北和秦岭-大别地区未能用简单岩石圈厚度等值线解释，机制有待厘清 [Deng 2018, pp. 9-10]。
- 数据空间覆盖与分辨率有限，对缺乏地震测线的区域仅提供间接指导 [Deng 2018, pp. 1-1]。

## Assumptions / Conditions
- 地壳与地幔岩石圈满足挠曲均衡（计入弹性厚度）[Deng 2018, pp. 4-5]。
- 地幔岩石圈内温度按线性地热梯度分布，从莫霍温度θc到θa=1350°C [Deng 2018, pp. 4-5]。
- 软流圈密度ρa=3200 kg/m³，热膨胀系数δ=4.0×10⁻⁵/°C [Deng 2018, pp. 4-5]。
- 地壳温度模型基于三维稳态热传导方程 [Deng 2018, pp. 1-4, 9-10]。
- 初始密度与S波速关系的适用性 [Deng 2018, pp. 1-4]。

## Key Variables / Parameters
- \( H_c \)：地壳对地形的均衡贡献；\( H_{ml} \)：地幔岩石圈均衡贡献；\( T_{ml} \)：地幔岩石圈厚度 [Deng 2018, pp. 4-5]。
- \( \rho_a = 3200\ \text{kg/m}^3 \)；\( \theta_a = 1350^\circ\text{C} \)；\( \delta = 4.0\times10^{-5}/^\circ\text{C} \) [Deng 2018, pp. 4-5]。
- 莫霍面温度 \( \theta_c \)（由Sun et al., 2013的地壳温度模型提供）[Deng 2018, pp. 1-4]。
- 参考项 \( H_0 = 2.4\ \text{km} \) [Deng 2018, pp. 4-5]。
- 弹性厚度 \( T_e \)（由Pérez-Gussinyé et al., 2004方法计算）[Deng 2018, pp. 7-9]。
- 残差重力（目标≤5 mGal）和残差地形（目标≤0.05 km）作为反演收敛判据 [Deng 2018, pp. 5-7]。

## Reusable Claims
- 中国东部地形梯度带(TGB)以东，地壳均衡贡献Hc约为3.6 km，以西则超过4.2 km，这种差异过度补偿了地表高程的变化 [Deng 2018, pp. 7-9]。
- 采用S波速度-密度转换并联合地形和重力（允许残差≤0.05 km和≤5 mGal）精化，可以显著改善岩石圈密度模型的匹配度 [Deng 2018, pp. 5-7]。
- 在挠曲均衡、线性地热和给定软流圈参数的前提下，TGB大致与110 km岩石圈厚度等值线一致，但东北和秦岭-大别不符合该规律 [Deng 2018, pp. 9-10]。
- 若莫霍深度有4 km不确定性，当最下地壳密度为3000 kg/m³时，会导致Hc的变化约0.13 km，最终引起岩石圈厚度估算偏差约8 km [Deng 2018, pp. 9-10]。
- 仅1%的蛇纹石化可使地幔岩石圈密度降低~8 kg/m³，足够使东部所需的岩石圈厚度从90 km增至~100 km，说明水化可以部分解释东西岩石圈厚度差异 [Deng 2018, pp. 11-12]。
- 扬子与华夏地块的弹性厚度仅~15 km，远低于四川盆地东部和西华北克拉通的>60 km，指示显著横向强度差异 [Deng 2018, pp. 7-9]。

## Candidate Concepts
- [[topographic gradient belt (TGB)]]
- [[flexural isostasy]]
- [[intraplate crustal deformation]]
- [[lithospheric thinning]]
- [[hydration-induced density reduction]]
- [[dynamic topography]]
- [[receiver function Moho depth]]
- [[elastic thickness (Te)]]
- [[cratonic nucleus rigidity]]
- [[mantle refertilization]]
- [[asthenospheric upwelling]]

## Candidate Methods
- [[joint inversion of topography and gravity]]
- [[S-wave velocity to density conversion]]
- [[receiver function analysis]]
- [[multitaper spectral estimation of elastic thickness]]
- [[3-D steady-state heat conduction equation]]
- [[flexural isostasy modeling with linear geotherm]]

## Connections To Other Work
- 核心输入数据来自已发表的地震与热模型：S波速度模型 (Shen et al., 2016)、接收函数莫霍 (Y. Li et al., 2014)、地壳温度模型 (Sun et al., 2013)，表明本工作是多种地球物理数据的集成 [Deng 2018, pp. 1-4, 5-7]。
- 弹性厚度计算采用 Pérez-Gussinyé et al. (2004) 的多窗口谱估计法，并与 Chen et al. (2013) 关于华南克拉通继承弱带的讨论保持一致 [Deng 2018, pp. 7-9]。
- 地幔楔的低速异常与俯冲板片脱水水化关系引用 Huang & Zhao (2006)、Zhao et al. (2011) 等地震层析结果 [Deng 2018, pp. 11-12]。
- 水化密度效应的估算参考 Christensen (2004) 和 Hacker & Abers (2004) 的实验数据 [Deng 2018, pp. 11-12]。
- 动态地形机制与 Flament et al. (2013)、Liu (2015) 等研究相关联 [Deng 2018, pp. 10-11]。
- 未从索引片段中确认与其他特定研究（如水化定量模拟或岩石圈热-化学演化模型）的直接比较。

## Open Questions
- 软流圈上涌对板内火山区地表高程的真实贡献有多大？是否主要被化学浮力而非热浮力驱动？[Deng 2018, pp. 10-11]
- 东北和秦岭-大别地区违背TGB与岩石圈厚度等值线关系的原因是什么？[Deng 2018, pp. 9-10]
- 地幔岩石圈的再富化(#Mg变化)对东西密度差异的定量贡献是多少？[Deng 2018, pp. 11-12, 未详细展开]
- 在构造活跃区域，偏离稳态的热结构如何系统性地影响岩石圈厚度估算？[Deng 2018, pp. 11-12]
- 能否将水化程度、成分改变与热状态进行真正联合反演，而非仅示例性测算？[Deng 2018, pp. 11-12]

## Source Coverage
本知识页基于13个索引片段编写，覆盖了摘要 [pp. 1-1]、引言与研究背景 [pp. 1-4]、方法公式 [pp. 4-5]、初始模型残差与精化 [pp. 5-7]、弹性厚度与地壳贡献结果 [pp. 7-9]、岩石圈厚度及不确定性 [pp. 9-10]、动态地形讨论 [pp. 10-11]、水化效应讨论 [pp. 11-12]。  
片段重点反映了方法框架、主要发现和部分物理机制讨论；**缺失或未详细索引的内容**可能包括：完整的数据处理流程、详细的弹性厚度空间分布图、再富化定量讨论的进一步细节、动态地形模型的具体预测、与全球其他克拉通比较的讨论以及论文末尾的结论段落。若需完整评估，应回溯原文全文。
