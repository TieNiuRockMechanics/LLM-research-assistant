---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-pai-an-investigation-on-the-deterioration-of-physical-and-mechanical-properties-of-granite"
title: "An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock."
status: "draft"
source_pdf: "data/papers/2021 - An investigation on the deterioration of physical and mechanical properties of granite after cyclic thermal shock.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Pai, Ning, et al. “An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock.” *Geothermics*, vol. 97, 2021, 102252."
indexed_texts: "13"
indexed_chars: "62842"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:00:49"
---

# An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock.

## One-line Summary
通过对花岗岩进行0–20次循环热冲击实验并结合数值模拟，研究发现第一次热冲击造成的物理力学性能劣化最为严重，当热冲击次数超过10次后劣化趋势减缓 [Pai 2021, pp. 1-2]。

## Research Question
频繁的冷热循环会如何改变花岗岩（EGS干热岩储层的主要介质）的物理与力学性质？其内部劣化机制是什么？[Pai 2021, pp. 1-2]

## Study Area / Data
- **研究对象**：花岗岩样品，作为地热储层中经常遇到的代表性岩石 [Pai 2021, pp. 2-3]。
- **样本**：花岗岩样品的天然状态作为对照组（0次热冲击），实验组分别进行1、5、10、20次循环热冲击 [Pai 2021, pp. 3-4]。
- **测试属性**：纵波（P波）速度、热导率、孔隙度、单轴压缩下的全应力-应变曲线、峰值强度、峰值应变、弹性模量、变形模量、声发射（AE）特征以及XRD矿物成分分析 [Pai 2021, pp. 4-8]。

## Methods
- **循环热冲击实验**：将花岗岩样品以5°C/min的速率（临界加热速率，不引起损伤）加热至450°C，恒温2小时，随后立即放入冷水中快速冷却。待样品表面温度降至室温后，继续浸泡1小时，此为一次循环。循环次数设定为0、1、5、10、20次 [Pai 2021, pp. 3-4]。
- **物理力学性质测试**：
  - **孔隙度**：通过测量饱和吸水样品质量、干燥质量和体积间接计算 [Pai 2021, pp. 4-5]。
  - **力学测试**：进行单轴压缩与声发射联合测试，获取全应力-应变曲线、强度、弹性模量等参数 [Pai 2021, pp. 3-4]。
  - **矿物成分分析**：对循环热冲击后的花岗岩进行XRD衍射分析 [Pai 2021, pp. 5-6]。
- **数值模拟**：结合ANSYS软件，对花岗岩在热冲击过程中的内部温度场和热应力场的演化特征进行可视化分析 [Pai 2021, pp. 1-2]。

## Key Findings
- **第1次热冲击导致最为严重的劣化**：花岗岩的物理和力学性能在第1次热冲击后表现出最剧烈的退化。当热冲击次数超过10次后，劣化速度减缓 [Pai 2021, pp. 1-2]。
- **物理性质变化显著**：经历20次热冲击后，与天然状态相比，P波速度下降58.9%（从3572 m/s降至1469 m/s），热导率下降43.9%（从3.283 W·m⁻¹·K⁻¹降至1.840 W·m⁻¹·K⁻¹），孔隙度增加676.0%（从0.321%增至2.491%）。这些变化在0–10次热冲击阶段最为敏感，占0–20次总变化幅度的85.6%–93.2% [Pai 2021, pp. 4-5]。
- **热导率下降机理**：矿物成分未观察到显著变化，因此热导率的下降主要归因于循环热冲击导致的矿物颗粒间接触热阻的增加 [Pai 2021, pp. 5-6]。
- **力学性质劣化与延性增强**：
  - **全应力-应变曲线**：热冲击后的花岗岩曲线呈现出初始压密阶段凹形更明显、线弹性阶段斜率降低、裂纹扩展阶段显著延长、破坏阶段由瞬时跌落变为阶梯式跌落等特性 [Pai 2021, pp. 6-7]。
  - **强度与变形**：峰值强度和弹性模量随热冲击次数增加而降低。延性特征增强，这是由于局部应力集中效应增强和局部承载能力差异增大所致 [Pai 2021, pp. 1-2]，[Pai 2021, pp. 6-7]。
  - **峰值应变非线性变化**：峰值应变先增后减，增加是因为压缩热裂纹需要更大的轴向位移；超过10次后下降是因为承载能力降低限制了大规模变形的产生 [Pai 2021, pp. 6-7]。
- **声发射（AE）特征改变**：
  - 初始压密阶段AE计数显著增多，声发射活动更活跃。
  - 线弹性阶段AE计数变化有限。
  - 裂纹扩展阶段的最大AE计数降低。
  - 机理在于：热裂纹的存在为能量释放提供了更多路径，包括已有热裂纹的扩展、汇合以及新的力学裂纹的萌生、扩展与汇合，这削弱了平均能量释放强度，体现为AE计数的下降 [Pai 2021, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| P波速度在20次热冲击后下降58.9% | [Pai 2021, pp. 4-5] | 加热至450°C后水冷，0–20次循环 | 0–10次循环的降幅占0–20次总降幅的93.2% |
| 热导率在20次热冲击后下降43.9% | [Pai 2021, pp. 4-5] | 加热至450°C后水冷，0–20次循环 | 劣化主因非矿物成分变化，而是颗粒间接触热阻增加 [Pai 2021, pp. 5-6] |
| 孔隙度在20次热冲击后增加676.0% | [Pai 2021, pp. 4-5] | 加热至450°C后水冷，0–20次循环 | 从天然状态的0.321%增至2.491% |
| 力学性能劣化在首次热冲击时最严重，超过10次后减缓 | [Pai 2021, pp. 1-2] | 加热至450°C后水冷，0–20次循环 | 体现于峰值强度、弹性模量等指标 |
| 全应力-应变曲线破坏阶段由瞬时跌落转为阶梯式跌落 | [Pai 2021, pp. 6-7] | 单轴压缩实验 | 表明延性特征增强与局部承载差异有关 |
| 裂纹扩展阶段AE最大计数降低 | [Pai 2021, pp. 7-8] | 单轴压缩与声发射联合测试 | 归因于能量释放路径增多，单次释放强度减弱 |

## Limitations
- **温度上限单一**：实验最高加热温度固定为450°C，未从索引片段中确认不同温度水平下的对比数据。
- **冷却方式单一**：仅采用了冷水冷却一种热冲击方式，未探讨其他冷却速率的影响。
- **循环次数有限**：实验最大循环次数为20次，更高循环次数的长期效应未从索引片段中确认。
- **机理分析定性**：对局部应力集中和能量释放路径的分析主要基于现象推断和定性描述，缺乏定量的微观裂纹观测数据（如CT扫描）的直接支持 [Pai 2021, pp. 2-3]。

## Assumptions / Conditions
- **临界加热速率假设**：5°C/min被视为不引起花岗岩损伤的临界加热速率 [Pai 2021, pp. 3-4]。
- **非热致矿物相变假设**：在450°C峰值温度下，XRD结果显示花岗岩的主要矿物（石英、钠长石等）未发生显著的相变或分解，故物理力学性质劣化主要归因于热应力产生的微裂纹，而非矿物成分改变 [Pai 2021, pp. 5-6]。
- **热阻模型**：热导率的下降被解释为矿物颗粒间接触热阻增加的结果 [Pai 2021, pp. 5-6]。
- **能量释放多路径模型**：声发射特征的改变被归因于热裂纹的存在为能量释放提供了额外路径 [Pai 2021, pp. 7-8]。

## Key Variables / Parameters
- **自变量**：循环热冲击次数（0, 1, 5, 10, 20）。
- **物理因变量**：P波速度 (`Vp`)、热导率 (`λ`)、孔隙度。
- **力学因变量**：峰值强度、峰值应变、弹性模量、变形模量。
- **声学因变量**：声发射计数（AE counts），包括各阶段的计数和最大计数。
- **分析与机制参数**：矿物颗粒间接触热阻、局部应力集中、局部承载能力差异、能量释放路径。

## Reusable Claims
- **Claim 1**：对于此花岗岩，在从室温加热到450°C并水冷的循环热冲击条件下，首次冲击是造成其物理力学性质（如P波速度、热导率、强度）劣化的最剧烈阶段。当循环次数超过10次后，劣化速率显著减缓。[Pai 2021, pp. 1-2]。
  - **适用条件/限制**：峰值温度450°C，水冷冷却方式。未在其他温度或冷却方式下验证。
- **Claim 2**：循环热冲击导致岩石热导率下降，其主要机制并非矿物成分变化（当温度低于相变阈值时），而是微裂纹增生导致的矿物颗粒间接触热阻增加。[Pai 2021, pp. 5-6]。
  - **适用条件/限制**：基于XRD结果，在450°C处理下未检测到主要矿物相变。
- **Claim 3**：循环热冲击通过增加岩石内部微裂纹数量，导致其在单轴压缩下表现出延性增强特征。具体表现为全应力-应变曲线中，裂纹扩展阶段延长，破坏阶段由瞬时脆性跌落转变为阶梯式延性破坏。其机理是热裂纹加剧了局部承载能力的差异，并增强了局部应力集中效应。[Pai 2021, pp. 6-7]。
  - **适用条件/限制**：观察基于单轴压缩实验，直接原因与热裂纹有关。
- **Claim 4**：经历热冲击后的花岗岩，其声发射活动在裂纹扩展阶段的最大计数值降低。这是因为预存的微裂纹为能量释放提供了额外路径，分散了单次破裂释放的能量，削弱了平均释放强度。[Pai 2021, pp. 7-8]。
  - **适用条件/限制**：结论基于单轴压缩过程中的声发射监测数据。

## Candidate Concepts
- [[cyclic thermal shock]]
- [[enhanced geothermal system (EGS)]]
- [[hot dry rock]]
- [[thermal damage]]
- [[thermal conductivity degradation]]
- [[contact thermal resistance]]
- [[ductility enhancement in brittle rock]]
- [[acoustic emission (AE) for damage characterization]]
- [[thermal stress cracking]]

## Candidate Methods
- [[cyclic heating and rapid cooling test]]
- [[uniaxial compression test]]
- [[acoustic emission monitoring]]
- [[P-wave velocity measurement]]
- [[thermal conductivity measurement]]
- [[porosity measurement by water saturation]]
- [[X-ray diffraction (XRD) for mineralogy]]
- [[ANSYS numerical simulation for thermal-mechanical coupling]]

## Connections To Other Work
- 文献综述表明，前人研究更多集中于高温后自然冷却条件下的岩石热损伤，或单次快速冷却的影响。关于循环热处理特别是循环热冲击的研究相对不足 [Pai 2021, pp. 2-3]。
- 部分研究者已发现热循环对岩石物理力学性质的影响存在一个阈值，在阈值之前影响更剧烈，本研究结果与前人定性认知相符 [Pai 2021, pp. 2-3]。
- 前人研究多基于对热应力的定性理解来解释损伤机制，而本研究通过ANSYS数值模拟，试图更直观地展示温度场和热应力的动态演化 [Pai 2021, pp. 2-3]。
- 可从主题上连接到以下候选概念与方法：
  - 微裂纹演化与定量表征技术：可连接 [[micro-CT scanning]] 和 [[crack network morphology]]。
  - 岩石本构模型：研究中的全应力-应变曲线变化可连接 [[damage constitutive model for rock]]。
  - 地热工程应用：研究发现可为 [[thermal stimulation]] 和 [[reservoir fracturing]] 提供实验依据，可连接 [[reservoir permeability enhancement]] 和 [[long-term stability of EGS]]。

## Open Questions
- 不同的加热上限温度（如低于或高于450°C）对循环热冲击劣化趋势有何定量影响？未从索引片段中确认。
- 不同的冷却速率（如空气冷却、液氮冷却）造成的热冲击损伤机理与差异？未从索引片段中确认。
- 超过20次热冲击后，物理力学性能劣化是否会达到一个稳定残余值？长期效应未从索引片段中确认。
- 文中定性描述的热裂纹、局部应力集中等现象，能否通过微观成像技术（如SEM、CT）进行定量关联和验证？未从索引片段中确认。
- 如何将本实验得到的劣化规律用于修正或建立可预测EGS储层服役性能的数值模型？未从索引片段中确认。

## Source Coverage
本页依据原论文索引的13个片段编写，内容覆盖了摘要、引言、实验方法、主要结果（物理与力学性质）和部分讨论。覆盖较为全面，但仍有重要信息缺失：数值模拟（ANSYS）的具体模型设置、边界条件、温度场/应力场演化的可视化结果等在提供的片段中描述不足；对实验结果深层机理的讨论（如“更多能量释放路径”的具体形式）可能在后文中有更详细阐述，但未包含在索引片段中。结论和对地热工程的启示部分（`3.5` 节）在片段结尾处被截断，不完整。
