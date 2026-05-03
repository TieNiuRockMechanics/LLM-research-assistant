---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v"
title: "Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization."
status: "draft"
source_pdf: "data/papers/2021 - Scale-Bridging in Three-Dimensional Fracture Networks Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.pdf"
collections:
citation: "Hyman, Jeffrey D., et al. \"Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.\" *Geophysical Research Letters*, vol. 48, no. 14, 2021."
indexed_texts: "15"
indexed_chars: "71807"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "71527"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.996101"
coverage_status: "full-index"
source_signature: "e8a98e1a6f58a5a11f9775e6afa53758dc00aa33"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:40:26"
---

# Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.

## One-line Summary
首次将原位应力条件下获取的Marcellus页岩真实裂缝孔径分布融入三维离散裂缝网络（DFN）模拟，证明微观孔径变异性可引发尺度桥接效应，显著重组网络尺度的流场，使流动通道化程度平均提升170%，活性表面积大幅下降。

## Research Question
微观尺度的裂缝孔径变异性（内部孔径分布）如何影响网络宏观尺度的流动与溶质运移特性？核心在于厘清不同尺度非均质性的影响层级——网络结构通常被认为是主导因素，但孔径变异性是否能跨越尺度、重组整个网络的流场结构，此前尚未通过真实孔径观测加以证实。[Hyman 2021, pp. 1-1] [Hyman 2021, pp. 1-2]

## Study Area / Data
- **岩石类型**：Marcellus页岩（Bedford, Pennsylvania outcrop），矿物组成为66%碳酸盐、19%石英和长石、13%黏土、2%其他，呈硬脆特性。[Hyman 2021, pp. 2-3]
- **实验条件**：三轴直剪装置配合实时X射线成像，在有效围压4.4 MPa、平均孔隙压力0.6±0.4 MPa的条件下对完整圆柱试样（长25.4 mm，直径25.2 mm）进行剪切断裂，剪切位移0.60 mm。[Hyman 2021, pp. 2-3]
- **孔径场数据**：通过直接阈值分割3D X射线灰度数据得到，体素尺寸46.6±0.4 μm。孔径场统计量：算术平均值2.38×10⁻⁴ m，几何平均值1.85×10⁻⁴ m，对数方差1.21×10⁻¹² m²，变异系数0.59，相关长度≈3×10⁻⁴ m。低于体素尺寸的孔径被设为体素尺寸，约占样品表面积的22%。[Hyman 2021, pp. 2-3]
- **数据获取**：数据可在数字岩石门户获取（Frash & Carey, 2018）。[Hyman 2021, pp. 9-10]

## Methods
- **离散裂缝网络（DFN）构建**：使用dfnWorks生成10个独立同分布的厘米级立方体3D DFN样本。网络由三个裂缝组组成，平均方向与笛卡尔坐标轴对齐（Fisher分布参数κ=100），裂缝为边长2×10⁻³ m的正方形，位置均匀随机分布。每网络随机放置400条裂缝，移除孤立裂缝后约240条形成连通系统，存在多条从入口到出口的路径。选取均匀裂缝尺寸以分离孔径变异性与其他几何因素的影响。[Hyman 2021, pp. 3-5] [Hyman 2021, pp. 5-6]
- **孔径场映射**：对每个网络中的每条裂缝，从实验一维孔径场（图1c）随机选择不同区域进行投影，并随机旋转与镜像，使每条裂缝具有独特的变孔径分布。孔径场在裂缝间独立，交叉处不相关。此方法保证不产生低于CT分辨率的特征，也不因粗化网格而平滑特征。[Hyman 2021, pp. 5-6]
- **网格划分与流动模拟**：使用共形Delaunay三角剖分，均匀边长为50 μm（与CT分辨率相当）。采用pflotran以两点通量有限体积法求解稳态不可压缩等温流场，施加Dirichlet边界条件。机械孔径直接作为水力孔径。经Brush & Thomson (2003)准则确认，当雷诺数小于1时，局部立方律可接受。[Hyman 2021, pp. 5-6]
- **溶质运移模拟**：采用无分子扩散的纯对流粒子追踪方法，100000个被动粒子以通量加权方式注入，在裂缝交叉处采用完全混合规则。粒子追踪用于生成突破曲线（BTC）、粒子弯曲度、流动拓扑图（FTG）等。[Hyman 2021, pp. 6-7]
- **对比方案**：为每条网络生成恒定孔径版本（孔径2.2×10⁻⁴ m，介于几何与算术平均值之间）作为参考。每条网络生成10个独立孔径场实现，总计110次模拟（10网络×10变孔径+100额外恒定孔径样本用于活性表面积对比）。[Hyman 2021, pp. 5-6] [Hyman 2021, pp. 8-9]

## Key Findings
1. **网络尺度流场重组**：变孔径导致FTG结构发生显著变化，主流通道的位置与数量改变，有时形成新的优势子网络，甚至出现单主导通道。[Hyman 2021, pp. 6-7]
2. **突破曲线特征变化**：与恒定孔径相比，变孔径网络的首次到达时间更早，BTC峰值降低，幂律尾部衰减更慢（衰减指数−2.3 vs −2.6），表明整体弥散性增强。这两类网络的置信区间不重叠，差异不能归因于网络间变异。[Hyman 2021, pp. 7-8]
3. **粒子弯曲度增加**：变孔径网络的粒子平均弯曲度普遍高于恒定孔径网络，部分样本平均弯曲度增加超过50%，这不仅源于裂隙平面内的局部弯曲，更源于网络尺度流场重组。[Hyman 2021, pp. 8-9]
4. **活性表面积大幅下降**：变孔径网络的活性表面积分布更集中，数值普遍低于恒定孔径网络，多数情况下活性表面积降幅超过50%，反映了大规模子网络在变孔径条件下完全失去显著流动。[Hyman 2021, pp. 8-9]
5. **流动通道化程度激增**：以Hyman (2020)方法度量，变孔径网络前20条主通道传输的总质量均大于对应恒定孔径网络，平均增加170%，最大增加311%。这是尺度桥接的直接证据。[Hyman 2021, pp. 8-9]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 变孔径网络FTG显示流场结构重组，主通道位置改变或形成单主导通道 | [Hyman 2021, pp. 6-7] | 10个DFN样本，每个样本10个独立孔径场实现 | 代表110个样本的典型现象 |
| BTC尾部衰减指数：变孔径网络−2.3，恒定网络−2.6 | [Hyman 2021, pp. 7-8] | 粒子数10万，纯对流 | 置信区间不重叠 |
| 变孔径网络平均粒子弯曲度普遍增加，部分增幅>50% | [Hyman 2021, pp. 8-9] | 100个变孔径样本与10个恒定孔径对照 | 增加源于网络尺度重组而非仅局部弯曲 |
| 变孔径网络活性表面积多数降幅>50% | [Hyman 2021, pp. 8-9] | 190个网络统计（100变孔径+90恒定） | 变孔径网络分布更集中 |
| 主通道输运质量增幅：平均170%，最大311% | [Hyman 2021, pp. 8-9] | Hyman (2020)通道化度量，前20主通道 | 所有变孔径样本均高于恒定对照 |

## Limitations
- 模拟在厘米尺度进行，虽然预期场尺度也会出现类似模式，但未经验证。[Hyman 2021, pp. 9-10]
- 仅考虑稳态层流和纯对流输送，未包含分子扩散、惯性效应（较高雷诺数）、基质扩散或流体-岩石化学反应。这些过程可能受到流动变化的影响，但本研究未予量化。[Hyman 2021, pp. 5-6] [Hyman 2021, pp. 9-10]
- 网络参数虽基于Marcellus页岩观测，但非特定场地再现；裂缝尺寸均一，裂缝密度较高，未考虑裂缝长度、孔径均值等变异性的交互作用。[Hyman 2021, pp. 3-5]
- 机械孔径直接用作水力孔径，未单独校准二者关系。[Hyman 2021, pp. 5-6]
- 实验孔径场基于单个样本的一次剪切事件，变异性范围可能有限。[Hyman 2021, pp. 2-3]

## Assumptions / Conditions
- 流动为不可压缩、等温、稳态层流，且雷诺数<1，局部立方律可接受。[Hyman 2021, pp. 5-6]
- 每条裂缝的孔径场独立从实验场随机投影获得，裂缝间孔径不相关，交叉处无孔径相关性建模。[Hyman 2021, pp. 5-6]
- 机械孔径等价于水力孔径。[Hyman 2021, pp. 5-6]
- 粒子为无扩散的被动示踪剂，以通量加权注入，裂缝交叉口采用完全混合规则。[Hyman 2021, pp. 6-7]
- 裂缝形状为平面正方形，尺寸固定，方向分布集中，以隔离孔径变异性的影响。[Hyman 2021, pp. 3-5]

## Key Variables / Parameters
- **孔径场统计量**：算术均值2.38×10⁻⁴ m，几何均值1.85×10⁻⁴ m，对数方差1.21×10⁻¹² m²，变异系数0.59，相关长度≈3×10⁻⁴ m。[Hyman 2021, pp. 2-3]
- **DFN参数**：域尺寸1 cm³；裂缝形状正方形边长2×10⁻³ m；裂缝组3个，方向Fisher κ=100；放置裂缝数400（连通常约240）；网格分辨率50 μm。[Hyman 2021, pp. 3-5]
- **流动条件**：恒定孔径参考值2.2×10⁻⁴ m；压力梯度保证Re<1；边界条件为Dirichlet压差。[Hyman 2021, pp. 5-6]
- **运移参数**：粒子数100,000；注入方式为通量加权；交叉口混合规则为完全混合。[Hyman 2021, pp. 6-7]
- **分析指标**：首次到达时间分布、BTC衰减指数、粒子弯曲度（总路径/直线距离）、活性表面积比例、Hyman (2020)流动通道化度量（前20通道质量占比）。[Hyman 2021, pp. 8-9]

## Reusable Claims
- 当三维裂缝网络中每条裂缝采用真实、独立的空间变孔径分布时，微观孔径变异性可导致网络尺度流动场的显著重组，这种效应被称为“尺度桥接”。条件：裂缝密度高，网络具有多连通路径，孔径变异性基于实验室观测，且流动为层流。来源：[Hyman 2021, pp. 1-1] [Hyman 2021, pp. 8-9]。
- 变孔径网络的首达时间提前、BTC峰值降低、尾部衰减幂律指数绝对值减小（例：由−2.6变为−2.3），显示出相对于恒定孔径网络更强的整体弥散性。条件：DFN厘米级模型，不锈钢场为纯对流，雷诺数<1。来源：[Hyman 2021, pp. 7-8]。
- 活性表面积（有显著流动的区域占比）在变孔径网络中可下降超过50%，且分布更为集中，表明大量裂隙原本的流动区域在孔径变异下丧失传输功能。条件：网络密度高，孔径变异系数0.59。来源：[Hyman 2021, pp. 8-9]。
- 流动通道化程度（前20主通道传输的质量分数）在变孔径条件下相对于相同网络几何的恒定孔径情形平均增加170%，最大可达311%。该度量可用于表征尺度桥接的强度。条件：使用Hyman (2020)的方法，网络大小和裂缝数量与本研究相似。来源：[Hyman 2021, pp. 8-9]。

## Candidate Concepts
- [[scale-bridging | 尺度桥接]]
- [[flow channelization | 流动通道化]]
- [[aperture variability | 孔径变异性]]
- [[discrete fracture network | 离散裂缝网络]]
- [[network-scale flow field | 网络尺度流场]]
- [[active surface area | 活性表面积]]
- [[breakthrough curve | 突破曲线]]
- [[tortuosity | 弯曲度]]
- [[flow topology graph | 流动拓扑图]]
- [[local cubic law | 局部立方律]]
- [[particle tracking | 粒子追踪]]

## Candidate Methods
- [[triaxial direct-shear | 三轴直剪实验]]
- [[X-ray microtomography | X射线微米CT]]
- [[dfnWorks | dfnWorks模拟套件]]
- [[conforming Delaunay triangulation | 共形Delaunay三角剖分]]
- [[pflotran | pflotran有限体积法流动模拟]]
- [[flux-weighted particle injection | 通量加权粒子注入]]
- [[complete mixing rule | 完全混合规则]]
- [[flow channelization metric (Hyman 2020) | 流动通道化度量]]

## Connections To Other Work
- 单裂隙中孔径变异性导致流动通道化和弥散已被广泛研究（Brown, 1987a; Boutt et al., 2006; Detwiler et al., 2000; Kang et al., 2016等）。本研究将此认知扩展至网络尺度。[Hyman 2021, pp. 1-1] [Hyman 2021, pp. 1-2]
- 以往网络模拟多采用统计表征的孔径场（de Dreuzy et al., 2012; Frampton et al., 2019; Huang et al., 2019; Karra et al., 2015; Makedonska et al., 2016; Zou & Cvetkovic, 2020），本研究首次使用实验原位应力孔径场，验证了真实复杂性的影响。[Hyman 2021, pp. 1-2]
- 局部立方律适用性参考Brush & Thomson (2003)的论证。[Hyman 2021, pp. 5-6]
- 流动通道化度量采用Hyman (2020)的方法。[Hyman 2021, pp. 8-9]
- 研究受多项地下工程应用的驱动，如增强型地热系统、页岩油气开采、CO₂封存、核废料处置，这些领域均需理解裂隙网络中的非均质流。[Hyman 2021, pp. 1-2]

## Open Questions
- 这些观察到的流动变化是否及如何影响其他地球物理过程，如基质扩散和吸附导致的滞留、流体-流体和流体-固体的反应性传输？[Hyman 2021, pp. 9-10]
- 在场尺度条件下，类似的尺度桥接效应是否仍然存在，且变异性是否有比例放大？[Hyman 2021, pp. 2-3]
- 当网络包含多种裂缝尺寸、方向变异性和不同孔径均值时，孔径变异性的影响层级如何变化？[Hyman 2021, pp. 3-5]
- 雷诺数较高时惯性效应与孔径变异性耦合对网络流场的相对重要性？[Hyman 2021, pp. 5-6]

## Source Coverage
所有非空索引片段均已处理，共计15个源块。编译后的源字符数为71,527，覆盖率（按字符计）为99.6%（覆盖率按块计为100%）。源签名：e8a98e1a6f58a5a11f9775e6afa53758dc00aa33。所有证据均来自索引片段，未引用片段外信息。
