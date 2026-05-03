---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-ye-experimental-study-of-real-time-temperature-dependent-nonlinear-deformation-of-sandstone"
title: "Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone."
status: "draft"
source_pdf: "data/papers/2023 - Experimental study of real-time temperature-dependent nonlinear deformation of sandstone.pdf"
collections:
  - "zotero new"
citation: "Ye, Zuyang, and Jianhang Yang. \"Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone.\" *Fuel*, vol. 354, 2023, article 129308. doi:10.1016/j.fuel.2023.129308. Accessed 2026."
indexed_texts: "13"
indexed_chars: "64403"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:30:30"
---

# Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone.

## One-line Summary
在实时加热条件下（25–200 °C），砂岩的非线性弹性变形存在阈值温度125 °C：低于该温度，热致微裂纹（热弱化）导致软部分比例增加、硬部分模量降低；高于该温度，热膨胀（热强化）使结构更致密化，变形转而由硬部分主导 [Ye 2023, pp. 8‑10]。

## Research Question
- 实时（非热后处理）中等温度（25–200 °C）如何影响砂岩在弹性阶段的非线性应力‑应变行为？
- 能否用两段胡克模型（TPHM）描述这种与温度相关的非线性变形？是否存在特征阈值温度？ [Ye 2023, pp. 1‑2]

## Study Area / Data
- **试样**：40个砂岩圆柱试样（具体来源/产地在索引片段中未提及）。
- **温度组**：8个温度等级（25, 50, 75, 100, 125, 150, 175, 200 °C），每组5个试样 [Ye 2023, pp. 2‑3]。
- **测试**：每个试样进行实时恒温条件下的单轴压缩，记录轴向应力‑应变曲线，加载终止于约60 kN（约30 MPa），重点关注压实阶段和线弹性阶段 [Ye 2023, pp. 2‑3]。

## Methods
1. **实验系统**：高低温试验箱与微机控制岩石直剪仪联用，实现实时温度控制和轴向加载 [Ye 2023, pp. 2‑3]。
2. **升温与保温**：以3 °C/min的速率加热至目标温度（25–200 °C），恒温2小时后开始加载 [Ye 2023, pp. 2‑3]。
3. **加载方式**：预加载采用力控0.5 kN/s至1 kN，之后以1.5 kN/s轴力控制加载至试样破坏，计算机自动记录轴向力和位移；本文仅分析压实和弹性阶段，故在约60 kN（约30 MPa）时停止 [Ye 2023, pp. 2‑3]。
4. **试样预处理**：为防止水分对强度的干扰，试样事先干燥；200 °C以下结合水蒸发微弱，未予考虑 [Ye 2023, pp. 7‑8]。
5. **本构模型**：采用两段胡克模型（TPHM）。将岩石分为软部分（含微裂纹）和硬部分（致密基质）。软部分遵循真应变胡克定律，硬部分遵循工程应变胡克定律，其一维应力‑应变关系为 \( \frac{dV}{V_0} = \gamma_e \frac{d\sigma}{K_e} + \gamma_t \exp\left(-\frac{\sigma}{K_t}\right)\frac{d\sigma}{K_t} \)，其中 \(\gamma_t = V_{0,t}/V_0\) 为软部分体积比，\(\gamma_e = 1-\gamma_t\) 为硬部分体积比，\(K_e\)、\(K_t\) 分别为硬部分、软部分体积模量 [Ye 2023, pp. 3‑4]。
6. **参数拟合**：对实测应力‑应变曲线的高应力线性段拟合直线，其斜率作为硬部分弹性模量 \(E_e\)，截距a对应于裂纹闭合应变（CCS），进而确定 \(\gamma_t\)；软部分弹性模量 \(E_t\) 亦通过拟合获得 [Ye 2023, pp. 5‑7]。

## Key Findings
- 25–125 °C：随温度升高，应力‑应变曲线右移，同等应力下变形增大；压实阶段占比增加，表明热裂纹增多，且 \(\gamma_t\) 上升、\(E_e\) 下降，呈现热弱化特征 [Ye 2023, pp. 4‑5]。
- 125 °C是一个阈值温度：此时 \(\gamma_t\) 达到最大值（约0.033），\(E_e\) 降到最低（约4147 MPa）[Ye 2023, pp. 8‑9]。
- 125–200 °C：曲线反趋平坦，175 °C和200 °C时近乎过原点的直线，硬部分主导，软部分影响可忽略；\(\gamma_t\) 下降、\(E_e\) 上升，表现为热强化 [Ye 2023, pp. 4‑5, 8‑10]。
- \(E_t\) 在整个25–200 °C范围内持续减小，表明软部分的热膨胀效应与硬部分不一致（软部分含杂质颗粒） [Ye 2023, pp. 8‑10]。
- 热分解效应在中等温度下可忽略，最大质量损失仅为0.2581% [Ye 2023, pp. 7‑8]。
- TPHM模型对各个温度下非线性应力‑应变曲线的拟合效果良好（\(R^2\) 普遍高于0.99），证明了模型的有效性 [Ye 2023, pp. 8‑9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 25 °C组平均：\(\gamma_t = 0.01906\)，\(E_e = 4632\ \mathrm{MPa}\)，\(E_t = 5.329\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 砂岩，实时加热，单轴压缩至~30 MPa | 弹性模量单位缺省，原文如此 |
| 50 °C组平均：\(\gamma_t = 0.01998\)，\(E_e = 4468\ \mathrm{MPa}\)，\(E_t = 4.682\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | 热弱化开始显现 |
| 75 °C组平均：\(\gamma_t = 0.02058\)，\(E_e = 4270\ \mathrm{MPa}\)，\(E_t = 4.655\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | |
| 100 °C组平均：\(\gamma_t = 0.02505\)，\(E_e = 4243\ \mathrm{MPa}\)，\(E_t = 4.767\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | |
| 125 °C组平均：\(\gamma_t = 0.03323\)（最大值），\(E_e = 4147\ \mathrm{MPa}\)（最小值），\(E_t = 4.044\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | 阈值温度，\(\gamma_t\) 和 \(E_e\) 达到极值 |
| 150 °C组平均：\(\gamma_t = 0.01919\)，\(E_e = 4532\ \mathrm{MPa}\)，\(E_t = 3.181\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | 热强化开始，\(\gamma_t\) 回升，\(E_e\) 下降 |
| 175 °C组平均：\(\gamma_t = 0.00901\)，\(E_e = 5011\ \mathrm{MPa}\)，\(E_t = 2.836\ \mathrm{MPa}\) | [Ye 2023, pp. 8‑9] | 同上 | 曲线接近直线，软部分影响微弱 |
| 所有温度组的 \(R^2\) 普遍大于0.99 | [Ye 2023, pp. 8‑9] | 砂岩，实时加热 | TPHM拟合优度高 |
| 试样质量随温度升高而减少，但最大降幅仅0.2581% | [Ye 2023, pp. 7‑8] | 中等温度（25–200 °C） | 热分解可忽略 |
| 样品预先干燥以避免自由水影响；结合水在200 °C以下蒸发不强 | [Ye 2023, pp. 7‑8] | 实验预处理 | 未评估结合水效应 |

## Limitations
- 本实验只加载至约30 MPa，未涵盖峰后破坏阶段，仅反映压实和弹性阶段的变形特征 [Ye 2023, pp. 2‑3]。
- 试样数量每组5个，虽可接受，但离散性依然存在，参数统计结果以平均值给出 [Ye 2023, pp. 7‑8]。
- 砂岩产地未在索引片段中明确，结果的代表性局限于类似砂岩。
- 实验中未测量实时孔隙率，仅用 \(\gamma_t\) 间接表征内部缺陷的发展 [Ye 2023, pp. 7‑8]。
- 未考虑结合水的可能影响，仅排除自由水干扰 [Ye 2023, pp. 7‑8]。
- 模型假设软部分直接遵循真应变胡克定律，硬部分遵循工程应变胡克定律，未涉及塑性或损伤演化。

## Assumptions / Conditions
- **模型假设**：岩石可划分为软部分（含微裂纹）和硬部分（无裂纹基质）；软部分服从真应变胡克定律，硬部分服从工程应变胡克定律 [Ye 2023, pp. 3‑4]。
- **实验假设**：试样干燥后，自由水对力学性能的影响可忽略；200 °C以下结合水不显著蒸发，热分解可忽略 [Ye 2023, pp. 7‑8]。
- **温升路径**：3 °C/min 的升温速率和2 h 恒温足以使试样内部温度均匀 [Ye 2023, pp. 2‑3]。
- **加载控制**：采用力控方式，避免初始接触干扰，且只观察压实和线性弹性段，确保试样未进入显著破坏阶段 [Ye 2023, pp. 2‑3]。
- **温度范围**：仅针对“中等温度”25–200 °C，适用于深部矿床、核废料围岩等工程背景 [Ye 2023, pp. 2‑2]。

## Key Variables / Parameters
- **变形参数**：
  - \(\gamma_t\)：软部分体积比（或面积比），反映了微裂纹等缺陷的等效含量。
  - \(E_e\)：硬部分的弹性模量（MPa）。
  - \(E_t\)：软部分的弹性模量（MPa）。
- **应力与应变**：轴向应力 \(\sigma\)，轴向应变 \(\varepsilon\)；裂纹闭合应变 CCS（由线性段截距 a 定义），可用以直接估计 \(\gamma_t\) [Ye 2023, pp. 5‑7]。
- **温度变量**：实时温度 \(T\)（25–200 °C），升温速率 3 °C/min。
- **阈值**：阈值温度 \(T_{\text{th}} \approx 125\ \mathrm{°C}\)，在该温度 \(\gamma_t\) 最大、\(E_e\) 最小 [Ye 2023, pp. 8‑10]。
- **实验控制**：加载速率（1.5 kN/s），预加载（0.5 kN/s），目标终点载荷60 kN（约30 MPa）。

## Reusable Claims
1. 对于经受实时加热的砂岩，存在一个中等温度阈值（~125 °C）：温度低于该阈值时，热弱化占主导，表现为 \(\gamma_t\) 增大、\(E_e\) 减小；高于该阈值时，热强化占主导，\(\gamma_t\) 减小、\(E_e\) 回升 [Ye 2023, pp. 8‑10]。
2. 两段胡克模型（TPHM）能够准确描述砂岩在实时温度下的非线性弹性变形，拟合优度 \(R^2\) 普遍超过0.99，且参数具有清晰的物理意义（软、硬部分） [Ye 2023, pp. 1‑2, 8‑9]。
3. 软部分的弹性模量 \(E_t\) 在整个25–200 °C范围内持续下降，表明软部分（通常含杂质或微裂纹）与硬部分的温度响应机制不同 [Ye 2023, pp. 8‑10]。
4. 采用裂纹闭合应变（CCS）或软部分比 \(\gamma_t\) 比孔隙率更适合表征实时温度下砂岩抵抗变形的能力 [Ye 2023, pp. 5‑7]。
5. 在实时加热、中等温度条件下（≤200 °C），热分解造成的质量损失极小（不足0.3%），对力学性质的影响可忽略不计 [Ye 2023, pp. 7‑8]。
6. 实时加热实验能揭示出与热处理（先升温冷却再加载）不同的温度效应，表现为更显著的热强化现象 [Ye 2023, pp. 2‑2]。

## Candidate Concepts
- [[two-part Hooke’s model]]
- [[nonlinear elastic deformation]]
- [[real-time heating]]
- [[thermal weakening]]
- [[thermal strengthening]]
- [[threshold temperature]]
- [[soft part]]
- [[hard part]]
- [[crack closure strain]]
- [[moderate temperature geomechanics]]

## Candidate Methods
- [[uniaxial compression test under real-time temperature]]
- [[TPHM parameter fitting]]
- [[true-strain Hooke’s law]]
- [[engineering-strain Hooke’s law]]
- [[high-low temperature chamber + direct shear instrument setup]]

## Connections To Other Work
- 本研究所用的TPHM框架直接继承自 Liu 等 [29] 和 Zhao & Liu [30] 的工作，他们将岩石划分为软硬两部分以处理含裂纹介质的非线性弹性行为 [Ye 2023, pp. 3‑4]。
- 实时加热实验的设计思路与 Ranjith 等 [10] 及 Yang 等 [28] 的研究相似，但本工作限定了中等温度范围（≤200 °C），并聚焦于压实和弹性阶段的非线性变形 [Ye 2023, pp. 3‑4]。
- 此前有研究指出实时加热下热强化现象比传统热处理更明显，但未能用线性模型解释；本文验证了TPHM能够捕捉这一差异 [Ye 2023, pp. 2‑2]。
- 与测量冷却后孔隙率的常规方法不同，本文提出以 \(\gamma_t\) （软部分比）作为实时状态下表征内部缺陷的替代指标，这与 Shapiro & Kaselow [52] 将孔隙分为刚性与柔性部分的思想相呼应 [Ye 2023, pp. 7‑8]。
- 论文提及但未在片段中展开的比较对象还包括：深部地热系统（Fenton Hill）、核废料处置（围岩温度165–200 °C）等工程场景，可从中等温度地热储层、高放废物地质处置等领域寻找联系 [Ye 2023, pp. 2‑2]。

## Open Questions
- 该阈值温度（125 °C）是否适用于其他类型的砂岩或更广泛的地质材料？ [未从索引片段中确认]
- 在高围压或三轴条件下，实时温度引起的非线性变形规律与TPHM的适用性如何？ [未从索引片段中确认]
- 软部分 \(E_t\) 持续减小的微观机理（如矿物颗粒边界滑移、杂质相变等）仍需深入揭示 [未从索引片段中确认]
- 当温度超过200 °C后，热分解和结合水释放是否会改变软/硬部分的响应模式？ [未从索引片段中确认]
- 如何在实时温度下直接测量孔隙率或微裂纹密度，以进一步验证TPHM的物理基础？ [Ye 2023, pp. 7‑8] 提到该困难，但未提出解决方案。

## Source Coverage
本知识页完全基于论文“Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone”的13个索引片段。片段覆盖了摘要与引言、实验系统与步骤、TPHM模型推导与参数拟合方法、主要实验结果（应力‑应变曲线、参数趋势、阈值温度）以及部分讨论（热弱化/热强化机理、热分解与含水量影响）。然而，可能缺失的信息包括：完整的结论部分、详细的微观证据（如SEM照片）、200 °C组的完整拟合参数、与其他模型（如孔隙弹性）的定量对比、以及对工程应用的直接讨论。因此，本文的解读仅限于这些片段所提供的信息。
