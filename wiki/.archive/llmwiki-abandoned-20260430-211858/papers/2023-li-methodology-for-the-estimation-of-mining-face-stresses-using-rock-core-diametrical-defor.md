---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-li-methodology-for-the-estimation-of-mining-face-stresses-using-rock-core-diametrical-defor"
title: "Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation."
status: "draft"
source_pdf: "data/papers/2023 - Methodology for the estimation of mining face stresses using rock core diametrical deformation.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 161, 2023, p. 105300. *ScienceDirect*, doi:10.1016/j.ijrmms.2022.105300. Accessed 2026."
indexed_texts: "6"
indexed_chars: "26475"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:57:15"
---

# Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation.

## One-line Summary
提出一种基于岩心直径变形的解析方法，用于估算地下矿山开采面附近的双轴主应力，并通过单轴压缩取芯实验进行了验证 [Li 2023, pp. 1-1][Li 2023, pp. 5-6]。

## Research Question
如何利用从开采面钻取的岩石岩心的直径变形数据，有效且实用地估算矿山开采面附近的采动诱导应力（包括大小主应力），以克服常规应力测量在近工作面区域不适用的局限 [Li 2023, pp. 1-1][Li 2023, pp. 1-2]。

## Study Area / Data
- 研究为方法学性质，未指定特定矿山研究区。
- 验证数据来自已发表文献（Funato and Ito）中的实验室试验：对安山岩、花岗岩、砂岩和砂浆立方体施加单轴压缩，在受压状态下从立方体中心钻取岩心，并测量其直径变形。共包含12组测试，所施加的单轴应力范围随岩石种类不同：安山岩5 – 15 MPa，花岗岩5 – 10 MPa，砂岩5 – 7.5 MPa，砂浆2.5 – 7.5 MPa [Li 2023, pp. 3-5]。
- 未从索引片段中确认有现场原位数据的使用。

## Methods
1. **基本原理**：将开采自由面前方岩体视为双轴应力状态，可转换为主应力σ_H和σ_h。当从该应力场中钻取岩心后，应力释放使岩心发生弹性膨胀，其直径与原始核心直径d_o及释放后测得的最大最小直径d_max、d_min相关 [Li 2023, pp. 1-2][Li 2023, pp. 2-3]。
2. **解析模型**：基于应力释放与岩心膨胀理论建立解析解，通过公式 (2a)、(2b) 关联主应力与弹性模量E、泊松比ν、直径测量值及原始直径d_o [Li 2023, pp. 2-3]。公式 (5) 给出了主应力差与直径差、E、ν、d_o的关系，并指出应力差对d_o的微小变化不敏感 [Li 2023, pp. 2-3]。
3. **原始直径确定**：考虑到d_o在现场难以直接测量，提出利用岩石可压缩性推导出d_o的估算式 (14)，该式表明d_o小于实测平均直径d_m [Li 2023, pp. 3-5]。
4. **实验室验证**：采用Funato和Ito的单轴压缩取芯实验数据，利用所提出的方程（式 (2a)、(2b)、(13)）反算施加应力，并与实际应力及Funato和Ito的差分应力法结果进行比较 [Li 2023, pp. 3-5]。
5. **材料参数获取**：方法还需要岩心的单轴抗压强度试验以获得弹性模量E和泊松比ν [Li 2023, pp. 1-2]。

## Key Findings
- 所提方法能较准确地估计开采面附近平面上的两个主应力，而Funato与Ito的原方法仅能提供主应力差 [Li 2023, pp. 5-6]。
- 基于12组单轴加载试验的验证结果显示，新解析模型估计应力与实际施加应力具有良好一致性，R²值达到93.13% [Li 2023, pp. 5-6]。
- 主应力差（σ_H − σ_h）的估计对原始核心直径d_o的小误差不敏感，但单个主应力的绝对值对d_o较为敏感；因此，高精度直径测量是实现可靠估计的必要条件 [Li 2023, pp. 2-3]。
- 当实测最小直径大、最小直径方向的应力释放程度不同时，可出现σ_h > νσ_H的情况，反映了应力释放的不对称性 [Li 2023, pp. 2-3]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 新解析模型对12组单轴压缩取芯试验的应力估计与实际应力高度吻合，R²=0.9313 | [Li 2023, pp. 5-6] | 单轴压缩（σ_h=0），岩类包括安山岩、花岗岩、砂岩、砂浆；弹性模量和泊松比由UCS试验提供；直径测量精度±0.0001 mm | 验证基于实验室控制条件，尚未包含双轴或现场试验。 |
| 主应力差（σ_H − σ_h）的估计对d_o的变化不敏感 | [Li 2023, pp. 2-3] | 理论推导，式 (5)，假设线弹性、各向同性；d_max与d_min测量不变 | 可靠性前提是高精度直径测量。 |
| 实测直径d_max与d_min在单轴试验中的具体数据可用于应力反算，Funato和Ito的方法高估了应力但本文方法改进明显 | [Li 2023, pp. 3-5, Table 3] | 数据对比在Table 3中给出（未在本索引片段中列出具体数值） | 具体数值未确认，仅表现为“agreed well”。 |
| 原始核心直径d_o可由式 (14) 估算，且恒有d_o < d_m | [Li 2023, pp. 3-5] | 基于岩石可压缩性推导 | 提供了一种避免直接测量d_o的实用途径。 |

## Limitations
- 方法假定垂直于开采自由面的正应力近似为零，因此仅适用于近自由面位置的双轴应力状态估计 [Li 2023, pp. 5-6]。
- 单个钻孔岩心只能确定垂直于钻孔轴线平面内的两个主应力，无法直接获得三维应力状态 [Li 2023, pp. 5-6]。
- 当前验证仅基于单轴压缩条件下的实验室试验，现场双轴或更复杂应力条件下的适用性尚未被证实。论文指出未来将进行双轴试验验证 [Li 2023, pp. 5-6]。
- 对测量设备的精度要求极高（文中实例采用±0.0001 mm分辨率的激光测微仪），现场测量条件可能难以达到同等精度 [Li 2023, pp. 1-2]。
- 论文有一份勘误（Corrigendum, 2023）提及原文中可能存在错误，但索引片段中未说明具体更正内容，可能影响原文部分公式或结论的准确性 [Li 2023, pp. 6-8]。

## Assumptions / Conditions
- **应力状态**：开采面前方岩体处于双轴应力场，且垂直于自由面的正应力近似为零（即σ_z ≈ 0，或表示为近零的次要应力） [Li 2023, pp. 5-6]。
- **材料行为**：岩石为连续、均质、各向同性的线弹性材料，应力释放引起的变形完全可恢复且服从胡克定律 [Li 2023, pp. 2-3]。
- **钻孔与岩心**：钻孔轴线垂直于所分析的主应力平面，岩心提取后变形为弹性释放，剖面保持圆形（无塑性或破坏） [Li 2023, pp. 1-2]。
- **测量**：岩心直径变形测量具备亚微米级精度；d_o可通过式（14）间接确定，前提是已获得弹性常数 [Li 2023, pp. 3-5]。

## Key Variables / Parameters
- **核心直径相关变量**：d_o（原始核心直径，即钻取瞬间的直径）、d_max（释放后最大直径）、d_min（释放后最小直径）、d_m（平均直径） [Li 2023, pp. 2-3]。
- **主应力**：σ_H（最大主应力）、σ_h（最小主应力），两者之差σ_H − σ_h [Li 2023, pp. 2-3]。
- **岩石力学参数**：E（杨氏弹性模量）、ν（泊松比），通过单轴抗压强度试验获得 [Li 2023, pp. 1-2]。
- **关键公式**：式(2a)、(2b)为应力-直径关系基本方程；式(5)为差分应力与直径差关系；式(14)为d_o估算式 [Li 2023, pp. 2-5]。
- **测量精度**：直径测量分辨率要求高，文中案例采用±0.0001 mm [Li 2023, pp. 1-2]。

## Reusable Claims
1. **基于线弹性的核心膨胀关系**：若已知岩石弹性模量E和泊松比ν，以及岩心释放后直径d_max、d_min，则主应力差可靠地表达为σ_H − σ_h = (E/(1+ν))·(d_max − d_min)/d_o，且该差值对d_o的微小变化不敏感。适用条件：岩心为各向同性线弹性，释放过程纯弹性，直径测量为高精度 [Li 2023, pp. 2-3]。
2. **原始直径的间接确定**：d_o可通过d_o = d_m / √( (1 − 2σ_mν/E) / (1 − 4σ_mν/E + 2σ_m/E) ) 进行估算，其中σ_m为平均应力（需迭代或同时满足应力方程）。此式源自材料的可压缩性，且表明d_o < d_m。适用条件：已知E、ν，并设定收敛准则求解 [Li 2023, pp. 3-5]。
3. **单岩心双轴应力反算方法**：利用测得的d_max、d_min、估算的d_o以及E、ν，通过联立方程可同时解出σ_H和σ_h，从而克服仅能获得应力差的不足。适用条件：自由面法向应力可忽略；材料性质已知；需满足高精度测量条件 [Li 2023, pp. 1-2]。
4. **验证结果的可重复性**：该方法在实验室条件下，对安山岩、花岗岩、砂岩和砂浆的单轴压缩取芯试验（应力5 – 15 MPa范围）给出了R²=0.9313的应力预测，可作为未来双轴或现场验证的基线。限制：当前仅限于单轴（σ_h=0）验证 [Li 2023, pp. 5-6]。

## Candidate Concepts
- [[diametrical core deformation analysis]] 岩心直径变形分析
- [[mining-induced stress estimation]] 采动应力估计
- [[stress relief method]] 应力解除法
- [[biaxial stress state]] 双轴应力状态
- [[rock core expansion after drilling]] 钻取岩心膨胀
- [[Young's modulus from UCS test]] 单轴抗压弹性模量
- [[pre-mining stress tensor]] 原岩应力张量
- [[near-field stress in sidewalls and back]] 井下近场应力

## Candidate Methods
- [[analytical model for core deformation]] 岩心变形解析模型
- [[uniaxial compression on rock cube with core extraction]] 取芯单轴压缩试验
- [[laser micrometer for core diameter measurement]] 激光测微仪岩心直径量测
- [[Funato and Ito’s differential stress approach]] Funato与Ito的差分应力法
- [[core-based stress measurement]] 基于岩心的应力测量
- [[diamond drilling for core extraction]] 金刚石钻进取芯

## Connections To Other Work
- 本文直接基于 **Funato和Ito (文献编号12)** 的岩心直径变形差分分析方法进行扩展，其原方法仅能获得主应力差，而本文进一步实现了两主应力的独立求解 [Li 2023, pp. 3-5][Li 2023, pp. 5-6]。
- 文中引用 **Ljunggren等 (2003)** 的岩石应力测量综述，作为现有应力测量方法分类的背景 [Li 2023, pp. 1-1, Ref 1]。
- 未从索引片段中确认与其他更广泛的原位应力测量方法（如套孔应力解除法、水力压裂法）有直接比较或连接。

## Open Questions
- 在双轴应力（σ_h ≠ 0）条件下该方法的准确性和可靠性如何？文中提到相关双轴试验工作正在进行，但未提供结果 [Li 2023, pp. 5-6]。
- 该方法对岩体各向异性、非线性及非连续面的敏感性未在片段中讨论。
- 现场应用中，如何确保获取未受扰动的开采面岩心，以及如何将实验室高精度测量移到现场环境，仍待解决。
- 勘误表中指出的原文错误具体涉及哪些内容，以及是否影响了已发表的公式或验证结论，未从片段中确认 [Li 2023, pp. 6-8]。

## Source Coverage
本页依据论文全部6条索引片段生成，覆盖了摘要、引言（部分）、方法（核心推导与d_o处理）、验证（实验设计与对比概述）以及讨论与结论的主要内容。由于片段未包含完整表格数据（如Table 1–3的具体数值）、所有公式细节、符号全部定义及图形内容，部分定量信息缺失。此外，勘误部分未给出具体更正条文，故无法评估对原文准确性的影响。总体而言，本文对解析方法推导和单轴验证的要点描述较为充分，但实验全貌和后续双轴验证细节不足。
