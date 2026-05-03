---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-meng-study-on-the-effect-of-sandstone-microscopic-damage-and-dynamic-compressive-properties"
title: "Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment."
status: "draft"
source_pdf: "data/papers/2022 - Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.pdf"
collections:
  - "论文"
citation: "Meng, Fandong, et al. “Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.” *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 1271–83. doi:10.1007/s00603-021-02733-3."
indexed_texts: "10"
indexed_chars: "46460"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:23:05"
---

# Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.

## One-line Summary
本文通过 NMR、MRI、XRD 和 SHPB 测试，研究了热处理后砂岩的微观损伤特征和动态压缩力学性质，并建立了一个同时考虑温度初始损伤和冲击加载损伤的动态损伤本构模型 [Meng 2022, pp. 1-2; pp. 10-11]。

## Research Question
高温如何改变砂岩的矿物组成与孔隙结构，以及这种微观损伤如何影响其在不同冲击速度下的动态抗压强度、弹性模量和破坏特征？能否建立一个考虑温度与冲击耦合效应的损伤本构模型？[Meng 2022, pp. 1-3]。

## Study Area / Data
砂岩试样取自中国陕北，该地区以岩溶地貌为主、矿产资源丰富 [Meng 2022, pp. 2-3]。试样加工为直径 98 mm、高 50 mm 的圆柱体，符合《工程岩体试验方法标准》[Meng 2022, pp. 2-3]。试验设置六种温度处理（20 °C、200 °C、400 °C、600 °C、800 °C、1000 °C）和三种平均冲击速度（8.6 m/s、14.6 m/s、18.8 m/s），每种工况 3 个试样，共 54 个砂岩试样 [Meng 2022, pp. 3-6]。

## Methods
- **热处理**：对砂岩试样进行 20–1000 °C 不同温度的热处理 [Meng 2022, pp. 3-6]。
- **微观表征**：利用 X 射线衍射（XRD）分析矿物组成与含量变化；利用核磁共振（NMR）和磁共振成像（MRI）技术分析孔隙结构变化，并通过 T₂ 谱和公式 \(r = C \cdot T_2\)（取 C=0.01 μm/ms）将弛豫时间转换为孔隙半径，将孔隙分为大孔（≥1 μm）、中孔（0.1–1 μm）和微孔（<0.1 μm）[Meng 2022, pp. 3-6; pp. 6-8]。
- **动态压缩试验**：采用直径 100 mm 的分离式霍普金森压杆（SHPB）进行单轴冲击压缩试验，设定三种冲击气压（0.2 MPa、0.35 MPa、0.5 MPa），对应平均冲击速度为 8.6 m/s、14.6 m/s、18.8 m/s，并假设杆件和试样满足各向同性及一维应力波理论 [Meng 2022, pp. 3-6; pp. 6-8]。
- **本构模型**：采用应变等效原理，将温热损伤变量 \(D_0\)（基于孔径加权）与冲击载荷损伤变量 \(D_i\)（基于 Weibull 分布和动态微元强度准则）结合，建立总损伤变量 \(D = D_0 + D_i - D_0 D_i\)，并采用非线性动态强度准则 \(\sigma_p = k + \alpha \ln(\dot{\varepsilon}/\dot{\varepsilon}_0) + \beta (\dot{\varepsilon}/\dot{\varepsilon}_s)^n / [(\dot{\varepsilon}/\dot{\varepsilon}_s)^n + 1]\) 进行验证 [Meng 2022, pp. 9-11]。

## Key Findings
1. **矿物组成变化**：砂岩室温下含 93.1% 石英，属石英砂岩。热处理后黏土矿物（如高岭石）含量下降，石英含量增加；在 400 °C 时内部赤铁矿全部被还原，导致试样表面呈暗红色 [Meng 2022, pp. 3-6]。
2. **孔隙结构演化**：随温度升高，试样内大孔含量逐渐增加，孔径分布范围缩小；孔隙率与温度的关系呈 S 形曲线，孔隙率增长率在 311 °C 达到最大值 0.95% [Meng 2022, pp. 6-8; pp. 11]。
3. **动态强度劣化**：同一冲击速度下，单轴动态抗压强度随温度升高而降低；温度劣化效应在低冲击速度（8.6 m/s）下更显著 [Meng 2022, pp. 8-9; pp. 11]。
4. **温度和应变率耦合效应**：冲击速度减弱了温度对砂岩的劣化效应，而温度则增强了应变率的强化效应；动态弹性模量随温度与冲击载荷呈三阶段变化：温度弱化阶段、冲击荷载增强阶段、再次温度弱化阶段 [Meng 2022, pp. 9-10; pp. 11]。
5. **动态强度准则**：峰值应力与应变率对数呈非线性关系，文中给出了不同温度下的动态强度参数 \(\alpha, \beta, n, \dot{\varepsilon}_s\) 和 \(R^2\)（见表2）[Meng 2022, pp. 10-11]。
6. **损伤本构模型验证**：利用实验数据与模型理论曲线进行对比（以 1000 °C、8.6 m/s 的应力‑应变曲线为例），两条曲线几乎重合，证明模型合理 [Meng 2022, pp. 10-11]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 400 °C 时赤铁矿全部被还原，黏土矿物分解，石英含量增加，试样表面变暗红 | [Meng 2022, pp. 3-6] | 石英砂岩，陕北试样 | XRD 测试结果；高岭石在 500–600 °C 脱羟基 |
| 孔隙率‑温度曲线呈 S 形，最大增长率 0.95% 出现在 311 °C | [Meng 2022, pp. 6-8; pp. 11] | C=0.01 μm/ms，孔径分为微孔、中孔、大孔 | 基于 NMR T₂ 谱和孔隙半径关系 |
| 随温度升高，大孔含量增加，孔径分布范围缩小 | [Meng 2022, pp. 6-8] | 同上 | T₂ 谱右峰增大、左峰减小 |
| 相同冲击速度下，动态抗压强度随温度升高而降低 | [Meng 2022, pp. 8-9] | 冲击速度 8.6、14.6、18.8 m/s | 温度劣化效应 |
| 冲击速度减弱温度劣化效应，温度增强应变率强化效应 | [Meng 2022, pp. 9-10; pp. 11] | 同上 | 温度与应变率耦合 |
| 动态弹性模量 E (峰前 50% 峰值应力处切线模量) 随温度和冲击速度变化呈三阶段 | [Meng 2022, pp. 9-10] | 基于 SHPB 数据 | 弹性模量随温度先降后升再降 |
| 热损伤变量 D₀ 基于大、中、微孔面积变化加权 (权重 0.525, 0.243, 0.232) | [Meng 2022, pp. 9-10] | NMR T₂ 谱面积，室温与热处理后对比 | 变异系数加权法 |
| 冲击损伤变量 Dᵢ 基于 Weibull 分布，动态微元强度采用非线性准则 | [Meng 2022, pp. 9-11] | 参数 m, F₀ 由实验数据拟合 | 考虑黏聚力和内摩擦角(表1) |
| 1000 °C、8.6 m/s 应力‑应变理论曲线与实验曲线几乎重合 | [Meng 2022, pp. 10-11] | 模型验证 | 证明本构模型合理 |

## Limitations
- 动态试验基于 SHPB 一维应力波假设和试样各向同性假设，实际岩石可能存在各向异性和非均匀性 [Meng 2022, pp. 6-8]。
- NMR 孔隙尺寸转换中取横向表面弛豫率 C 为常数 0.01 μm/ms，未考虑温度可能对 C 值的影响 [Meng 2022, pp. 6-8]。
- 热损伤变量仅考虑孔隙面积变化，未纳入矿物分解、相变等化学损伤的独立量化 [Meng 2022, pp. 9-10]。
- 使用的黏聚力和内摩擦角数据（表1）引自分层明等人的研究，而非本文独立测定，且只列出了截至 1000 °C 的数值 [Meng 2022, pp. 10-11]。
- 本构模型验证仅展示了 1000 °C、8.6 m/s 一条曲线，其余工况的验证情况未在索引片段中体现 [Meng 2022, pp. 10-11]。

## Assumptions / Conditions
- SHPB 试验中杆件与试样均为各向同性材料，满足一维应力波传播理论 [Meng 2022, pp. 6-8]。
- 核磁共振 T₂ 谱转换为孔隙半径时采用固定 C 值 (0.01 μm/ms)，且孔隙分类阈值 (微孔<0.1 μm, 中孔 0.1–1 μm, 大孔≥1 μm) 沿用前人经验 [Meng 2022, pp. 6-8]。
- 热损伤变量 D₀ 基于室温与热处理后 T₂ 谱面积的加权差异，假设不同尺度孔隙对强度的权重可通过变异系数分配 [Meng 2022, pp. 9-10]。
- 冲击载荷损伤 Dᵢ 服从 Weibull 统计分布，且动态微元强度采用非线性强度准则，其中参数 k 由黏聚力和内摩擦角计算 [Meng 2022, pp. 9-10]。
- 模型采用应变等效原理，且总损伤为热损伤与冲击损伤的复合，忽略两者之间可能的非线性叠加细节 [Meng 2022, pp. 9-10]。

## Key Variables / Parameters
- **温度 (T)**: 热处理水平，20–1000 °C [Meng 2022, pp. 3-6]。
- **平均冲击速度 (v)**: SHPB 试验加载速率指标，8.6, 14.6, 18.8 m/s [Meng 2022, pp. 3-6]。
- **动态抗压强度 (\(\sigma_d\))**: 单轴动态压缩下的峰值应力 [Meng 2022, pp. 8-9]。
- **动态弹性模量 (E)**: 峰前 50% 峰值应力处切线模量 [Meng 2022, pp. 9-10]。
- **孔隙率、孔径分布**: 大孔、中孔、微孔面积/含量，由 NMR T₂ 谱导出 [Meng 2022, pp. 6-8]。
- **矿物含量**: 石英、黏土矿物、赤铁矿相对含量 [Meng 2022, pp. 3-6]。
- **热损伤变量 (D₀)**: 根据孔径权重和面积比表征 [Meng 2022, pp. 9-10]。
- **冲击损伤变量 (Dᵢ)**: Weibull 分布参数 m 和 F₀，动态微元强度 F_d [Meng 2022, pp. 9-10]。
- **动态强度参数**: 非线性准则中 \(\alpha, \beta, n, \dot{\varepsilon}_s\)，随温度变化（见表2）[Meng 2022, pp. 10-11]。
- **黏聚力 (c)、内摩擦角 (\(\varphi\))**: 用于计算动态强度中的 k 值，随温度变化（见表1）[Meng 2022, pp. 10-11]。
- **应变率 (\(\dot{\varepsilon}\))**: 由 SHPB 数据处理得到，与冲击速度相关 [Meng 2022, pp. 6-8]。
- **横向表面弛豫率 (C)**: 取值 0.01 μm/ms [Meng 2022, pp. 6-8]。
- **孔隙权重 (w₁, w₂, w₃)**: 微、中、大孔变异系数权重，分别为 0.232, 0.243, 0.525 [Meng 2022, pp. 9-10]。

## Reusable Claims
- **高温对砂岩矿物组分的影响**：在石英砂岩中，加热至 400 °C 可使赤铁矿全部还原，表面变暗红；黏土矿物随温度分解，石英含量相对增加 [Meng 2022, pp. 3-6]。适用条件：富含粘土矿物与赤铁矿的石英砂岩；证据：XRD 矿物衍射图谱与组分含量变化；限制：其他类型砂岩（如长石砂岩）的矿物演化路径可能不同。
- **孔隙率‑温度的 S 形曲线与转折点**：砂岩孔隙率随温度呈 S 形增长，最大增长速率出现在约 311 °C，可作为热损伤快速发展的标志点 [Meng 2022, pp. 6-8; pp. 11]。适用条件：本文所用石英砂岩及类似的致密砂岩；证据：NMR 孔隙率数据拟合；限制：该转折温度可能受升温速率、初始孔隙率等因素影响。
- **温度与应变率对动态强度的耦合效应**：低冲击速度下温度劣化效应更明显；冲击速度的提高可部分抵消温度的弱化作用，同时温度的存在使得强度的应变率敏感性增强 [Meng 2022, pp. 9-10; pp. 11]。适用条件：单轴动态压缩，应变率范围对应于 8.6–18.8 m/s 冲击速度；证据：不同温度‑速度组合下的峰值应力与弹性模量变化；限制：未从索引片段中确认高围压、水等其他环境因素下的耦合效应。
- **考虑双重损伤的唯象本构模型**：将基于孔径权重的初始热损伤与基于 Weibull 分布的冲击损伤通过应变等效耦合，配合非线性动态强度准则，可以较好地复现热处理砂岩的动态应力‑应变行为 [Meng 2022, pp. 9-11]。适用条件：已知不同温度下的孔隙分布、黏聚力和内摩擦角数据；证据：1000 °C、8.6 m/s 下的模型与实验曲线对比验证；限制：模型参数 m, F₀ 需通过实验拟合，且仅验证了一条曲线。
- **热损伤变量的孔径权重分配方法**：利用 T₂ 谱微孔、中孔、大孔面积的变异系数计算权重，突出大孔对强度损失的主导作用（权重 0.525）[Meng 2022, pp. 9-10]。适用条件：可获取 NMR T₂ 谱的砂岩；证据：文中给出的具体权重值和 D₀ 计算式；限制：未考虑孔形状、连通性等因素。

## Candidate Concepts
- [[thermal damage]]
- [[dynamic compressive strength]]
- [[split Hopkinson pressure bar]]
- [[NMR pore structure]]
- [[XRD mineral analysis]]
- [[Weibull distribution]]
- [[strain rate effect]]
- [[constitutive model]]
- [[phase transition of quartz]]
- [[clay mineral decomposition]]

## Candidate Methods
- [[heat treatment]]
- [[uniaxial impact compression test]]
- [[NMR T2 spectrum analysis]]
- [[MRI imaging]]
- [[X-ray diffraction]]
- [[strain equivalence principle]]
- [[nonlinear dynamic strength criterion]]
- [[pore size weighting]]
- [[least squares fitting for Weibull parameters]]

## Connections To Other Work
- 本文引用了大量关于高温岩石力学性质的前人研究，如 Fan et al. (2020)、Xu et al. (2021) 指出的热处理后岩石抗张强度降低，Gong et al. (2019) 的 SHPB 试验方法，以及 Lemaitre (1984) 对应变等效原理的提出 [Meng 2022, pp. 2-3; pp. 9-10]。
- 热损伤变量的建立参考了 Meng et al. (2021) 的孔径权重方法，冲击损伤部分基于 Wang et al. (2007) 提出的岩石微元强度 Weibull 分布假设，动态微元强度准则借鉴了 Cao et al. (2017) 和 Qi and Qian (2003) 的工作 [Meng 2022, pp. 9-10]。
- 论文的方法和结论可与 [[thermal effect on rock strength]]、[[dynamic behavior of sandstone]]、[[damage mechanics of brittle materials]] 等主题建立连接，但在本索引片段内未确认与具体后序或平行研究的直接比较。
- 可进一步与 [[high temperature rock mechanics]]、[[SHPB testing standards]] 中的概念和方法建立联系。

## Open Questions
- 本文仅进行了单轴动态压缩试验，热处理砂岩在多轴动态加载和围压条件下的强度演化规律如何？[未从索引片段中确认]。
- 冷却方式（自然冷却？急冷？）是否对砂岩的损伤特征有显著影响？片段未提及冷却路径 [Meng 2022, pp. 3-6]。
- 文中针对 1000 °C 高温处理后的岩石强度参数 (c, φ) 引用了外部数据，其适用性和变异性如何？[未从索引片段中确认]。
- 耦合损伤本构模型在其他温度、冲击速度组合下的普遍验证结果未完全展示，模型的泛化能力有待进一步确认 [Meng 2022, pp. 10-11]。

## Source Coverage
本页内容基于论文的 10 个索引片段，覆盖了摘要、引言（文献综述与目的）、实验方法（试样制备、设备、参数）、微观分析结果（XRD、NMR）、SHPB 动态力学结果、动态损伤本构模型建立与验证以及主要结论。索引片段包含关键数据表格（表1、表2）和模型验证实例，因此信息相对完整。可能缺失的部分包括：详细的应力‑应变曲线全图、所有温度‑速度组合下的破坏模式描述、MRI 图像的直接分析结果、热损伤以外的低温处理影响、以及更多关于孔隙连通性的讨论。此外，部分引用的参数（如 c, φ）来源于其他文献，文中仅直接引用而未独立重测，其细节在片段中未完全展开。
