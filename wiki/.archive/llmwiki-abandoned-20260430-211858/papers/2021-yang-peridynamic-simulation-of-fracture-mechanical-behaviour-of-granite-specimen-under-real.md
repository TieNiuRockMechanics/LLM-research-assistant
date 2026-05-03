---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-yang-peridynamic-simulation-of-fracture-mechanical-behaviour-of-granite-specimen-under-real"
title: "Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments."
status: "draft"
source_pdf: "data/papers/2021 - Peridynamic simulation of fracture mechanical behaviour of granite specimen under real-time temperature and post-temperature treatments.pdf"
collections:
  - "zotero new"
citation: "Yang, Zhen, et al. \"Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 138, 2021, article 104573."
indexed_texts: "16"
indexed_chars: "75525"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:03:27"
---

# Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments.

## One-line Summary
本研究发展了基于常规态型近场动力学（OSB-PD）的全耦合热力学模型，并提出改进的多层计算方法，用以模拟花岗岩在实时温度（RT）和温度后（PT）处理下的断裂力学行为。[Yang 2021, pp. 1-1]

## Research Question
- 实时温度（RT）与温度后（PT）测试下，岩石材料的力学与断裂行为差异是什么？[Yang 2021, pp. 1-2]
- PT测试的结果能否用于逼近RT条件？[Yang 2021, pp. 1-2]

## Study Area / Data
未从索引片段中确认具体的研究区/野外数据。本文为数值模拟研究，其参数校准依据的是Wang等对花岗岩试样的单轴压缩实验结果。[Yang 2021, pp. 1-2, 11-12] 模拟试样尺寸为长25mm、高50mm。[Yang 2021, pp. 11-12]

## Methods
- **总体框架**：发展了常规态型近场动力学（OSB-PD）框架下的全耦合热力学模型，以研究花岗岩材料的热力学特性和断裂特征。[Yang 2021, pp. 1-1]
- **关键技术创新**：提出了一种**改进的多层计算方法**（modified multi-layer computational method），该方法令热学层尺寸大于测试试样，利用附加区域承受热冲击，从而在加载前切除该区域数据，以消除温度梯度诱发的裂纹影响。[Yang 2021, pp. 1-1]
- **数值验证与校准流程**：
    - 进行了方板热传导的基准测试，以考察**运动方程**和**热扩散方程**的数值收敛性。[Yang 2021, pp. 1-1, 9-11]
    - 通过模拟室温下花岗岩单轴压缩试验，校准了模型的关键力学参数——**泊松比（υ）**和**断裂能释放率（G0）**。[Yang 2021, pp. 1-1, 11-12]
- **关键离散化参数**：在m-收敛和δ-收敛测试中，使用的非局部比率m（δ/Δx）为2-4，材料点间距Δx为0.075-0.15 mm，邻域尺寸δ为0.225-0.45 mm。[Yang 2021, pp. 5-6]
- **失效准则**：采用了基于**临界伸长准则**（critical stretch criterion）的态型PD失效判断，其中临界伸长s₀由断裂能相等原理导出。[Yang 2021, pp. 6-7]

## Key Findings
- **裂纹区分的验证**：所提出的方法被验证能够建模并区分**热循环裂纹**（thermal cycling cracks）和**温度梯度诱发的裂纹**（thermal gradient-induced cracks）。[Yang 2021, pp. 1-1]
- **模拟能力**：该方法能恰当地模拟RT和PT两类试样的应力-应变行为及开裂模式。[Yang 2021, pp. 1-1]
- **高温度问题模拟的挑战**：在模拟超过600 °C的高温岩石材料问题时，岩石的低导热系数会导致热能在边界层积累，形成非均匀温度场，进而诱发不期望的温度梯度裂纹，切断核心区域的热流路径，使其难以加热至目标温度。[Yang 2021, pp. 7-9]
- **数值收敛性验证**：通过m-收敛和δ-收敛测试，验证了运动方程和热扩散方程的数值收敛性。在弹性变形阶段，不同收敛测试得到的模拟应力-应变曲线几乎重合。[Yang 2021, pp. 11-12]
- **参数校准结果**：通过与室温下单轴压缩实验结果的反复试算，最终确定泊松比υ为**0.25**，断裂能释放率G0为**70 J/m²**。[Yang 2021, pp. 11-12] 这两个数值与实验实测峰值强度**107.21 MPa**和峰值轴向应变**0.00674**的模拟结果较为匹配（强度差异约1-13%）。[Yang 2021, pp. 6-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 所提出方法能区分热循环裂纹和温度梯度裂纹 | [Yang 2021, pp. 1-1] | 基于OSB-PD和改进多层方法 | 方法验证的核心结论之一 |
| 室温下校准得到的参数：υ = 0.25, G₀ = 70 J/m² | [Yang 2021, pp. 11-12] | 试样尺寸25mm×50mm, ρ=2620 kg/m³, E=20 GPa，加载速率0.05 m/s | 通过反复试错确定的 |
| 校准参数下，峰值强度（107-112 MPa）与实验值（107.21 MPa）接近 | [Yang 2021, pp. 6-7] | δ和m取不同值时（如δ=1.5, m=2），强度变化范围为93.7-127.46 MPa | 模拟与实验强度误差在1-13% |
| 超过600°C时，低导热系数导致热能在表层积累，诱发梯度裂纹并阻碍核心升温 | [Yang 2021, pp. 7-9] | 热时间步须小于临界热时间步 | 这是提出改进多层方法的直接原因 |
| ρ(x) ∂²u(x,t)/∂t² = ∫ { ... } dV' + b(x,t) | [Yang 2021, pp. 2-3] | OSB-PD运动方程（式1），积分域为邻域Hx | 带热力耦合项B[x,t]力态 |

## Limitations
- 未从索引片段中确认该模拟方法对非花岗岩类岩石材料的适用性。
- 改进的多层方法旨在消除温度梯度诱发裂纹，但文中指出该类裂纹“仍然存在”，其可能未被完全消除。[Yang 2021, pp. 7-9]
- 所有模拟基于2D平面假设，而真实试样为3D，泊松比取值也因此与3D试验模型不同。[Yang 2021, pp. 11-12]
- 未从索引片段中确认模型在高围压（如三轴压缩）或更高温度（如>800°C）下的验证情况。
- 机械场的准静态模拟采用了0.05 m/s的加载速率，显著高于真实实验室的准静态速率，采用了ADR技术处理。[Yang 2021, pp. 11-12]

## Assumptions / Conditions
- **热力耦合框架**：模型基于常规态型近场动力学（OSB-PD）框架，所有离散和积分均在其非局部理论下进行。[Yang 2021, pp. 2-3]
- **热源模拟**：辐射加热通过电磁能量施加，由Stefan–Boltzmann定律描述，假设理想热源的发射率ε=1。[Yang 2021, pp. 3-6]
- **裂纹类型假设**：建模关注由矿物热膨胀失配导致的**热循环裂纹**和由温度场不均匀导致的**温度梯度诱发的裂纹**。[Yang 2021, pp. 1-1, 2-3]
- **加载方式**：采用自适应动力松弛法（ADR）模拟准静态加载过程。[Yang 2021, pp. 9-11]
- **模型维度**：所有模拟为2D平面应力或平面应变下的数值算例。[Yang 2021, pp. 11-12]
- **失效准则**：假设裂纹萌生和扩展遵循**临界伸长准则**，一旦键的伸长超过s₀则不可逆断裂。[Yang 2021, pp. 6-7]

## Key Variables / Parameters
- **力学参数**：材料密度（ρ），泊松比（υ），弹性模量（E），断裂能释放率（G₀） [Yang 2021, pp. 11-12]
- **热学参数**：导热系数（k_T），比热容（c_v） [Yang 2021, pp. 9-11]
- **热边界参数**：辐射表面温度（Θss），目标加热时间（t₀），Stefan–Boltzmann常数（σ），发射率（ε） [Yang 2021, pp. 3-6]
- **离散化参数**：材料点间距（Δx），近场范围（horizon, δ），非局部比率（m=δ/Δx） [Yang 2021, pp. 5-6]
- **时间步**：机械时间步（Δt_ME），热学时间步（Δt_TH） [Yang 2021, pp. 7-11]
- **力学量**：材料点位移（u），温度变化（T），力态（T），形变态（Y），热力态（B） [Yang 2021, pp. 2-3]
- **失效参数**：临界伸长（s₀），键断裂因子（χ） [Yang 2021, pp. 6-7]

## Reusable Claims
- **Claim1**：在PD热力耦合模拟中，通过将热学计算域（thermal layer）设置得比力学试样（mechanical layer）大，可令超出部分承受热冲击损伤。在机械加载前切除超出部分的数据，能有效消除或缓解温度梯度诱发的裂纹对后续力学测试的干扰。[Yang 2021, pp. 1-1, 7-9] (条件：用于模拟升温过程中因非均匀温度场产生的热冲击裂纹问题；限制：未完全消除该影响)
- **Claim2**：对于花岗岩（室温下ρ=2620 kg/m³，E=20 GPa），使用带键失效的OSB-PD 2D模型模拟其单轴压缩断裂行为时，一组有效的力学参数组合为：泊松比υ=0.25，断裂能释放率G₀=70 J/m²。[Yang 2021, pp. 11-12] (证据：模拟峰值强度接近实验值107.21 MPa；限制：该组参数为针对特定2D模型的试错结果，应区分于3D真实材料参数)
- **Claim3**：在模拟岩石高温（>600°C）热-力学行为时，由于岩石的导热系数低，直接应用热辐射传导模型会导致热能在表面边界层累积，形成稳定温度梯度，进而产生温度梯度诱发的裂纹，阻断向核心传热，使核心区难以达到目标温度。这种效应使模拟失真。[Yang 2021, pp. 7-9]

## Candidate Concepts
- [[Peridynamics (PD)]]
- [[Ordinary State-Based Peridynamics (OSB-PD)]]
- [[Fully coupled thermo-mechanics]]
- [[Real-time temperature (RT) test]]
- [[Post-temperature (PT) test]]
- [[Thermal gradient-induced cracks]]
- [[Thermal cycling cracks]]
- [[Granite specimen]]
- [[Critical stretch criterion]]
- [[Multi-layer computational method]]
- [[Non-local continuum mechanics]]

## Candidate Methods
- [[Modified multi-layer computational method]]
- [[Adaptive dynamic relaxation (ADR) technique]]
- [[m-convergence]]
- [[δ-convergence]]
- [[Forward difference time integration]]
- [[Calibration via uniaxial compression experiment]]
- [[Heat conduction benchmark]]
- [[Stefan–Boltzmann law for radiation boundary]]

## Connections To Other Work
- 本研究的实验对比基线来自 Wang et al. 24 和 Yin et al. 25，他们开展了花岗岩的RT和PT测试并对比了声发射特征和力学损伤。[Yang 2021, pp. 1-2]
- 本文的运动方程和热扩散方程基于 Madenci and Oterkus 44 的OSB-PD热力学理论。[Yang 2021, pp. 7-9]
- 失效准则中的临界伸长公式参考了 Zhang and Qiao 51 提出的态型PD临界伸长准则。[Yang 2021, pp. 6-7]
- 本文将PD应用于岩石材料断裂模拟，可以与 [[Three-point bending beam]] 或 [[Brazillian disk test]] 等标准断裂力学测试的PD模拟进行方法连接。[Yang 2021, pp. 1-2]
- 主题上，本文与 [[Modeling of crack propagation in rock]] 和 [[Thermal-mechanical coupling in geomaterials]] 等研究领域高度相关。

## Open Questions
- 完全消除而非仅缓解温度梯度诱发裂纹的方法是否可行？ [Yang 2021, pp. 7-9]
- 文中提出的改进多层方法及其标定的参数（如G₀=70 J/m²）对于更大尺度或三维问题是否具有良好的可扩展性和鲁棒性？未从索引片段中确认。
- PT测试的结果在多大程度上、在哪种温度范围内可以可靠地用于逼近RT条件？[Yang 2021, pp. 1-2]
- 模拟所得的开裂模式与实验的定量对比结果如何？未从索引片段中确认具体差异指标。

## Source Coverage
本知识页内容基于提供的16个索引片段生成。这些片段覆盖了论文的**摘要 (pp. 1-1)**、引言与研究空白 (pp. 1-2)、**方法论核心 (pp. 2-3, 3-6, 6-7)**、**数值实现细节 (pp. 7-9, 9-11)** 以及**参数校准与验证 (pp. 11-12)**。因此，本文对页面的覆盖偏向**方法与模型建立**及**初步结果验证**。

可能缺失的重要信息包括：对RT和PT全数值算例的详细描述与讨论、所有模拟与实验结果（如AE特征）的系统性对比、讨论部分对深层机理的分析以及具体结论。索引片段中缺少关于三轴压缩或更高温度下模拟表现的直接证据。
