---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-li-effect-of-mechanical-damage-on-the-thermal-conductivity-of-granite"
title: "Effect of Mechanical Damage on the Thermal Conductivity of Granite."
status: "draft"
source_pdf: "data/papers/2020 - Effect of Mechanical Damage on the Thermal Conductivity of Granite.pdf"
collections:
  - "zotero new"
citation: "Li, Zheng-Wei, et al. \"Effect of Mechanical Damage on the Thermal Conductivity of Granite.\" *Rock Mechanics and Rock Engineering*, vol. 53, 2020, pp. 1039-1051. doi:10.1007/s00603-019-01956-9."
indexed_texts: "10"
indexed_chars: "48000"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "47532"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99025"
coverage_status: "full-index"
source_signature: "79eeefe025f27540045a02e45382e9079114e18b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:15:28"
---

# Effect of Mechanical Damage on the Thermal Conductivity of Granite.

## One-line Summary
本研究在干燥与饱水条件下，通过循环加卸载诱导花岗岩产生机械损伤，并利用光学扫描法测量热导率，揭示机械损伤导致热导率总体下降、热非均质性增强，且损伤使不同方向的热导率差异增大，饱水可缩小该差异。

## Research Question
机械损伤（微裂纹萌生与扩展）如何改变花岗岩的热导率、热非均质性以及空间分布特征？饱水条件对损伤前后的热导率演变有何影响？

## Study Area / Data
- **岩样来源**：中国东部辽东省采集的花岗岩露头，所有试样取自同一岩块以保证均一性[Li 2020, pp. 2-4]。
- **基本物理性质**：密度范围 2.62–2.66 g/cm³（均值 2.64 g/cm³）；P 波速度范围 5393–5867 m/s（均值 5582 m/s）[Li 2020, pp. 2-4]。
- **矿物组成**（X 射线衍射）：石英 33.6%，钾长石 21.9%，斜长石 28.8%，云母 15.1%，黄铁矿 0.6%[Li 2020, pp. 2-4]。
- **样品几何**：圆柱样 φ50 mm × 100 mm；热导率测试时将圆柱样切割成厚 33 mm 的圆盘，在圆盘两端面的六条扫描线上进行测量[Li 2020, pp. 6-7]。

## Methods
### 机械损伤处理[Li 2020, pp. 2-6]
1. **基础参数确定**：通过单轴压缩试验获取完整应力‑应变曲线及声发射（AE）活动，确定裂纹初始应力（σci ≈ 60 MPa）、裂纹损伤应力（σcd ≈ 90 MPa）和峰值强度。循环加载的上限和下限应力分别设定为 100 MPa 和 70 MPa（略大于 σcd 和 σci）。
2. **循环加卸载方案**：采用余弦波加载，频率 0.1 Hz，初始加载速率 500 N/s。以横向应变为损伤程度指标，设置四个损伤水平：‑0.5 mε、‑0.55 mε、‑0.6 mε、‑0.65 mε。试验过程中同步监测 AE 活动。
3. **损伤评价**：测量损伤前后圆柱样及切割后圆盘的 P 波速度，验证损伤效果。

### 热导率测量[Li 2020, pp. 6-10]
- **方法**：采用光学扫描法（Popov 2016，ISRM 建议方法），在圆盘两端的六个扫描方向上测量热导率（每条扫描线获得 λ_max、λ_min、λ_ave）。
- **干燥/饱水处理**：干燥条件为 110℃ 烘 24 小时；饱水条件为真空饱和 48 小时。
- **热非均质性因子**：β = (λ_max − λ_min)/λ_ave。
- **方向差异量化**：每个端面六次测量的变异系数 COV_thermal = λ_std/λ_ave。
- **孔隙度计算**：n = (m_sat − m_dry)/(m_sat − m_sat in water) × 100%。

## Key Findings
1. **损伤验证**：循环加卸载后 P 波速度下降，四个损伤水平的平均下降率分别为 5.5%、5.9%、9.9%、14.3%；切割后的圆盘平均 P 波速度较未损伤圆柱样降低 9.14%[Li 2020, pp. 6-7]。
2. **热导率整体降低**：干燥条件下，未损伤花岗岩热导率范围 2.49–3.12 W/(m·K)（均值 2.77）；损伤后热导率范围 2.36–3.02 W/(m·K)（均值 2.61）。损伤使低热导率（<2.55）样本比例由 5.4% 增至 21.5%[Li 2020, pp. 6-7]。
3. **热非均质性增强**：未损伤样品 β 均值 0.11（97% 样品 <0.15）；损伤样品 β 均值 0.22，最大值 0.38，46.5% 的损伤样品 β > 0.25[Li 2020, pp. 7-9]。
4. **饱水效应**：饱水后两种样品热导率均提高；损伤样品的平均增加率（4.18%）大于未损伤样品（2.73%）。此因损伤使孔隙/微裂纹增多，饱水时吸水量更大[Li 2020, pp. 9-10]。
5. **方向差异**：干燥条件下，损伤样品的 COV_thermal 均值（0.026）大于未损伤样品（0.015）。饱水后方向差异减小。损伤处理导致微裂纹定向排列，增大了不同方向热导率的离散度。花岗岩热导率各向异性因子可观测（如 K=1.06 或 1.16），但各向异性程度较小[Li 2020, pp. 10-12]。
6. **孔隙度‑热导率关系**：获得线性反演式 λ = −0.0953n + 2.8217 (R=0.385)，损伤使孔隙度增大，热导率相应减小[Li 2020, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 未损伤花岗岩热导率 2.49–3.12 W/(m·K)，均值 2.77；损伤后 2.36–3.02 W/(m·K)，均值 2.61 | Li 2020, pp. 6-7 | 干燥，室温常压，光学扫描法测量圆盘端面 | 损伤使低 λ 比例上升 |
| 热非均质性因子 β：未损伤均值 0.11，损伤均值 0.22，最大 0.38 | Li 2020, pp. 7-9 | 干燥条件 | 损伤后非均质性显著增加 |
| P 波速度下降：损伤圆盘平均下降 9.14%；四水平下降率 5.5%–14.3% | Li 2020, pp. 6-7 | 循环加卸载后立即测量 | 验证损伤引入 |
| 饱水热导率增加率：未损伤均值 2.73%，损伤均值 4.18% | Li 2020, pp. 9-10 | 真空饱水，室温 | 饱水使水替代空气充填微裂纹 |
| 方向差异 COV_thermal：未损伤均值 0.015，损伤均值 0.026 | Li 2020, pp. 10-12 | 干燥条件，六扫描方向 | 饱水后 COV_thermal 下降 |
| 热导率‑孔隙度关系：λ = −0.0953n + 2.8217，R=0.385 | Li 2020, pp. 9-10 | 未损伤与损伤混合数据 | 负相关，但相关系数不高 |
| λ 与 P 波速度相关系数 0.114，无显著相关（α=0.01 临界值 0.285） | Li 2020, pp. 7-9 | 损伤圆盘样，扫描线平均值 | 表明 P 波速度不宜直接预测热导率 |

## Limitations
- 损伤程度仅以横向应变为控制指标，未能直接量化微裂纹密度或损伤变量[Li 2020, pp. 4-6]。
- 样品取自单一岩块花岗岩，结果可能不适用于其他岩性或区域[Li 2020, pp. 2-4]。
- 光学扫描法测得的为扫描线平均热导率，不能完全反映三维裂纹网络的空间异质性[Li 2020, pp. 6-7]。
- 试验在大气压力、室温下进行，未考虑原位应力与温度对热导率的耦合影响[Li 2020, pp. 2-3]。
- 损伤后热导率的方向差异虽有所增加，但各向异性因子较小，文中未探讨裂纹优势取向对方向差异的定量贡献[Li 2020, pp. 10-12]。

## Assumptions / Conditions
- 机械损伤主要由微裂纹萌生与扩展导致，且循环加卸载过程中裂纹持续发展[Li 2020, pp. 4-6]。
- 横向应变增量是损伤的可靠宏观指标，残余横向应变反映不可逆损伤[Li 2020, pp. 4-6]。
- 热导率测量基于光学扫描法，假设沿扫描线的温度变化能反映材料局部热物性[Li 2020, pp. 7-9]。
- 干燥（110°C/24 h）和真空饱水（48 h）处理能够完全排空/填充孔隙与微裂纹[Li 2020, pp. 7]。
- 试验温度处于室温，未考虑温度对矿物和流体热导率的影响[Li 2020, pp. 2]。

## Key Variables / Parameters
- 热导率 λ (W/(m·K))，干燥与饱水状态
- P 波速度 V_p (m/s)
- 横向应变 (mε) 及残余横向应变
- 循环加卸载上限/下限应力 (100/70 MPa)，频率 0.1 Hz
- 裂纹初始应力 σci，裂纹损伤应力 σcd
- 热非均质性因子 β
- 方向变异系数 COV_thermal
- 孔隙度 n (%)
- 热导率各向异性因子 K = λ_par/λ_per
- 声发射撞击计数

## Reusable Claims
- 在干燥条件下，单轴循环加卸载造成的机械损伤使花岗岩平均热导率由 2.77 W/(m·K) 降低至 2.61 W/(m·K)[Li 2020, pp. 6-7]。
- 机械损伤处理后，花岗岩的热非均质性因子 β 均值从 0.11 升至 0.22，表明扫描线上热导率离散度显著增大[Li 2020, pp. 7-9]。
- 饱水条件下，花岗岩的热导率增加，且损伤样品的增加率（均值 4.18%）大于未损伤样品（均值 2.73%），因为水充填损伤引起的微裂纹，水的导热性远优于空气[Li 2020, pp. 9-10]。
- 损伤导致不同测试方向的热导率差异增大（COV_thermal 均值从 0.015 增至 0.026），但饱水后该差异缩小[Li 2020, pp. 10-12]。
- 花岗岩损伤后孔隙度增大，热导率与孔隙度呈负线性关系 λ = −0.0953n + 2.8217（相关系数 0.385）[Li 2020, pp. 9-10]。
- P 波速度与热导率在损伤样品中无显著线性相关（r=0.114），说明 P 波速度不能简单替代热导率用于损伤评估[Li 2020, pp. 7-9]。
- 循环加卸载过程中声发射活动表明，首次加载至上界应力时裂纹已大量萌生，后续循环中 AE 仍缓慢增加，证实损伤持续累积[Li 2020, pp. 4-6]。

## Candidate Concepts
- [[Mechanical damage]]
- [[Thermal conductivity]]
- [[Optical scanning method]]
- [[P-wave velocity]]
- [[Thermal inhomogeneity factor]]
- [[Cyclic loading and unloading]]
- [[Acoustic emission]]
- [[Water saturation]]
- [[Crack initiation stress]]
- [[Crack damage stress]]
- [[Porosity]]
- [[Anisotropy factor]]
- [[Lateral strain damage indicator]]
- [[Microcrack initiation and propagation]]

## Candidate Methods
- [[Uniaxial cyclic loading and unloading test for artificial rock damage]]
- [[Optical scanning method for rock thermal conductivity (ISRM suggested)]]
- [[P-wave velocity measurement for damage evaluation]]
- [[Acoustic emission monitoring during rock failure]]
- [[Porosity calculation from saturated and dry mass]]
- [[Lateral strain-based damage level classification]]
- [[Complete stress-strain curve analysis for crack initiation/damage stress]]
- [[Thermal conductivity scanning line analysis with COV_thermal and β factor]]

## Connections To Other Work
- 前人研究指出孔隙度与热导率呈反比关系（Robertson & Peck 1974; Sayed 2011），本研究在损伤花岗岩中亦观察到该趋势，且给出线性关系，但相关性中等[Li 2020, pp. 1-2, 9‑10]。
- Popov et al. (2003b) 发现热导率与声速、孔隙度等物性存在关联，但本研究在损伤样品中未发现显著的 λ‑V_p 相关，说明损伤机制可能使此类关系复杂化[Li 2020, pp. 7-9]。
- Zimmerman (1989) 理论分析认为脆性岩石热导率与微裂纹发育、分布及流体饱和状态密切相关，本试验结果为该观点提供了实验支持[Li 2020, pp. 2]。
- Chen et al. (2011) 建立了考虑微结构演化、裂纹形状及饱和度的有效热导率微力学模型；Zhu et al. (2009) 和 Li et al. (2013) 在数值模型中假设损伤与热导率呈指数或突变关系，本研究为验证这些定量关系提供了实验数据[Li 2020, pp. 2]。
- 在试验方法上，Demırcı et al. (2004) 和 Görgülu et al. (2008) 测量了应力状态对热导率的影响，而本研究采用光学扫描法在无应力条件下聚焦损伤效应，两种路线互补[Li 2020, pp. 2]。

## Open Questions
- 文中未明确列出开放问题；研究目标是为工程岩体热导率演化机制提供知识，但以下问题尚待探索：  
  - 损伤变量（如裂纹密度、损伤因子）与热导率降低量之间的定量函数关系；  
  - 不同岩性（沉积岩、变质岩）中机械损伤对热导率的影响是否遵循相同规律；  
  - 温度‑应力‑损伤耦合条件下热导率的实时演化；  
  - 微裂纹优势取向对热导率各向异性的定量描述及模型化。  
  （上述问题基于论文研究范围和结果推演，未直接在原文中声明。）

## Source Coverage
已处理所有非空索引片段（共 10 段），索引字符数 48,000，编译策略为单次覆盖。片段覆盖率 1.0（按块），字符覆盖率 0.99025。所有引用均来自提供的片段，未使用外部知识。
