---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-ziegler-evaluation-of-the-diametrical-core-deformation-and-discing-analyses-for-in-situ-str"
title: "Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge"
status: "draft"
source_pdf: "data/papers/2021 - Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge.pdf"
collections:
  - "zotero new"
citation: "Ziegler, Martin, and Benoît Valley. “Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Geothermal Borehole, Switzerland.” *Rock Mechanics and Rock Engineering*, vol. 54, 2021, pp. 6511–32. doi:10.1007/s00603-021-02631-8. Accessed 2026."
indexed_texts: "18"
indexed_chars: "89770"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:29:16"
---

# Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge

## One-line Summary
本研究评估了基于直径岩心变形分析（DCDA）和岩心饼化分析在深部地应力估计中的应用，利用瑞士巴塞尔地热井 4.9 km 深处的二长岩-二长花岗岩岩心，发现摄影测量扫描可提取可靠数据，但岩心直径差异的高变异性和岩石弹性各向异性显著影响差应力估计[Ziegler 2021, pp. 1-2]。

## Research Question
- 摄影测量岩心扫描能否可靠地用于执行直径岩心变形分析（DCDA）？[Ziegler 2021, pp. 1-2]
- DCDA 估计的最大水平主应力方向（S~Hmax~）和水平差应力（ΔS）与钻孔崩落及应力诱导岩心饼化裂缝（CDF）数据集是否一致？[Ziegler 2021, pp. 1-2]
- 岩石弹性各向异性如何影响 DCDA 的 ΔS 估计？[Ziegler 2021, pp. 1-2]

## Study Area / Data
- **地点**：瑞士 Upper Rhine Graben 东南角 Basel‑1 地热钻孔，孔深约 5 km，岩心段 4909–4918 m 钻深[Ziegler 2021, pp. 3-4]。
- **岩性**：主要岩性为二长岩（monzonite，约 5.76 m）和二长花岗岩（monzogranite，约 3.03 m），少量镁铁质包体；结晶基底之上为约 2504 m 沉积盖层[Ziegler 2021, pp. 3-5][Ziegler 2021, pp. 6-7]。
- **岩心**：连续取心长度 9.09 m，岩心直径 101 mm；实际分析可用 68 块岩心片，多呈应力诱导饼化，饼厚多为 2–4 cm[Ziegler 2021, pp. 6-7]。
- **区域应力背景**：沿整个花岗岩段 S~Hmax~ 平均方位 N144°（最可靠的应力分量）；4.9 km 深度 S~Hmax~ 大小估计约 115 MPa（来自崩落分析），应力体系处于正断与走滑的交界[Ziegler 2021, pp. 5-7]。岩石抗拉强度估计在 4–11 MPa 之间[Ziegler 2021, pp. 4-6]。

## Methods
1. **直径岩心变形分析（DCDA）**  
   - 基于 Funato et al. (2012) 的弹性解法，利用岩心直径差异 Δd = d~max~ − d~min~ 估计水平差应力 ΔS = S~Hmax~ − S~hmin~，假设线弹性、各向同性，垂直井取心[Ziegler 2021, pp. 10-10]。  
   - 取 E = 65 GPa，ν = 0.22，以 d~min~ 近似初始直径 d~0~[Ziegler 2021, pp. 10-10]。  
   - 进行简单的参数敏感性分析，并利用数值模拟探究岩石各向异性对岩心直径的影响[Ziegler 2021, pp. 10-10]。
2. **岩心几何数据获取**  
   - **坐标测量机（CMM）**：对部分岩心切片以 36 点/周测量，椭圆拟合得到 d~max~、d~min~ 及其方向，作为参考[Ziegler 2021, pp. 7-9]。  
   - **摄影测量扫描（GOM ATOS 300 Core©）**：对 32 块岩心进行 3D 扫描，精度 10–20 μm；通过手动或 RANSAC 圆柱拟合对齐，取 1 mm 厚切片拟合椭圆获取直径和方向[Ziegler 2021, pp. 9-10]。  
   - 两种方法对齐误差通过合成圆柱测试评估，以保证提取的 Δd 远低于预期的岩心径向变形[Ziegler 2021, pp. 9-10]。
3. **岩心饼化分析（Core Discing）**  
   - 利用岩心饼状裂缝的鞍形槽轴（凹轴）方向推断 S~Hmax~ 方向；使用 360°展开岩心照片和阴影摄影测量模型进行识别[Ziegler 2021, pp. 10-10]。
4. **比较与验证**  
   - DCDA 方向与应力诱导岩心饼化裂缝（CDF）及已有钻孔崩落结果进行对比[Ziegler 2021, pp. 1-2]。

## Key Findings
- 摄影测量扫描可有效提取可靠的岩心直径数据和 CDF 迹线[Ziegler 2021, pp. 1-2]。
- 局部对齐的岩心片显示的 S~Hmax~ 方向与钻孔崩落结果一致，但 Basel‑1 岩心片的直径差异（Δd）变异极大，导致 ΔS 估计值散布很宽[Ziegler 2021, pp. 1-2]。
- 必须考虑岩心弹性各向异性才能获得有意义的应力信息，这要求对岩石弹性模量进行稳健估计[Ziegler 2021, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Photogrammetric scanning can extract reliable core diametrical data and core discing fracture traces. | [Ziegler 2021, pp. 1-2] | 32 monzogranitic to monzonitic core pieces from 4.9 km depth; GOM ATOS 300 Core© scanner | Accuracy 10–20 μm; verified against CMM data & synthetic cylinders. |
| Locally aligned core pieces exhibit S~Hmax~ orientations similar to borehole breakouts. | [Ziegler 2021, pp. 1-2] | Vertical Basel‑1 borehole, crystalline section; photogrammetry‑based DCDA | Alignment based on reference line and toothpick markers. |
| Core diametrical variability is large, causing a wide spread in ΔS estimates. | [Ziegler 2021, pp. 1-2] | Basel‑1 core pieces; DCDA using Eq. 1, E=65 GPa, ν=0.22 | Not attributed to measurement noise alone; possible material heterogeneity/anisotropy. |
| Core elastic anisotropy must be considered; robust moduli estimates are required. | [Ziegler 2021, pp. 1-2] | Numerical simulations and sensitivity analysis on Eq. 1 | Implies isotropic assumptions in standard DCDA are insufficient. |

## Limitations
- DCDA 解析解假定线弹性、各向同性，实际岩石表现出弹性各向异性，尤其片麻状或定向结构岩石[Ziegler 2021, pp. 10-10][Ziegler 2021, pp. 1-2]。
- ΔS 估计对弹性模量（E）和泊松比（ν）敏感，未提供完整的模量各向异性表征方法[Ziegler 2021, pp. 10-10]。
- 仅基于单一深度的短岩心段（约 9 m），通用性受限；岩心饼化强烈，部分岩心因历史取样/测试而缺失[Ziegler 2021, pp. 6-7]。
- 摄影测量对齐方法的选择可能引入系统误差，尤其是短岩心片；但通过合成圆柱测试控制了该误差[Ziegler 2021, pp. 9-10]。

## Assumptions / Conditions
- 垂直井取心，钻孔轴线与主应力之一（垂直应力）平行，从而 d~max~ 方向指示 S~Hmax~[Ziegler 2021, pp. 2-3][Ziegler 2021, pp. 10-10]。
- 卸载线弹性行为，忽略非弹性和各向异性变形[Ziegler 2021, pp. 10-10]。
- 初始岩心横截面为圆形，且 d~min~ 可作为 d~0~ 的近似，由此引起的误差可忽略[Ziegler 2021, pp. 10-10]。
- 岩心饼化裂缝的鞍形槽轴代表 S~Hmax~ 方向（基于弹性理论）[Ziegler 2021, pp. 2-3][Ziegler 2021, pp. 10-10]。
- 采用弹性模量 E=65 GPa、ν=0.22 作为参考值，未区分岩性变化[Ziegler 2021, pp. 10-10]。

## Key Variables / Parameters
- ΔS：水平差应力，S~Hmax~ − S~hmin~[Ziegler 2021, pp. 1-2]
- d~max~, d~min~：最大和最小岩心直径[Ziegler 2021, pp. 7-9]
- Δd = d~max~ − d~min~[Ziegler 2021, pp. 10-10]
- d~0~：初始岩心直径（近似取 d~min~）[Ziegler 2021, pp. 10-10]
- E, ν：岩石杨氏模量和泊松比[Ziegler 2021, pp. 10-10]
- 弹性各向异性程度（未从索引片段中确认具体指标或参数）
- 岩心饼化几何：鞍形槽轴方向[Ziegler 2021, pp. 10-10]

## Reusable Claims
1. **摄影测量扫描用于 DCDA 的有效性**：对于直径约 100 mm 的深部结晶岩取心，使用精度达 ~20 μm 的摄影测量扫描并以 1 mm 切片拟合椭圆，可提取可靠的岩心直径差异和饼化裂缝迹线；前提是岩心对齐足够精确且表面反光处理得当[Ziegler 2021, pp. 1-2][Ziegler 2021, pp. 9-10]。
2. **DCDA 应力方向与钻孔崩落的一致性**：在垂直井中，局部对齐的岩心片通过 DCDA 得到的 S~Hmax~ 方向与钻孔崩落结果吻合，可作为方向约束，即使岩心直径差异绝对值波动大[Ziegler 2021, pp. 1-2]。
3. **差应力估计的变异性**：由于岩心直径差异（Δd）的原始变异性大，直接使用平均值和均一弹性参数计算的 ΔS 具有较大散布，不宜不加甄别地作为点估计；需要结合岩性、损伤、各向异性信息进行校正[Ziegler 2021, pp. 1-2]。
4. **弹性各向异性对差应力估计的必要性**：忽略弹性各向异性会导致 ΔS 估计偏差，在具备岩石定向弹性模量的情况下，应使用各向异性解或修正因子[Ziegler 2021, pp. 1-2]。该声明基于本研究中的参数敏感性分析和数值模拟，但具体各向异性修正公式未在片段中详述。

## Candidate Concepts
- [[Diametrical Core Deformation Analysis (DCDA)]]
- [[Core Discing Fracture (CDF)]]
- [[Borehole Breakout]]
- [[Photogrammetric Core Scanning]]
- [[In-Situ Stress Estimation]]
- [[Elastic Anisotropy]]
- [[Stress Regime (Normal, Strike-Slip)]]
- [[Rock Core Relaxation]]
- [[Saddle Trough Axis]]

## Candidate Methods
- [[Coordinate Measuring Machine (CMM) core profiling]]
- [[Photogrammetric 3D scanning (GOM ATOS)]]
- [[RANSAC cylinder fitting for core alignment]]
- [[Ellipse fitting to core cross-sections]]
- [[DCDA elastic solution (Funato et al. 2012)]]
- [[Core discing fracture mapping]]
- [[Borehole breakout width analysis]]
- [[Numerical simulation of anisotropic core deformation]]
- [[Ultrasonic velocity anisotropy (RACOS)]]

## Connections To Other Work
- **DCDA 方法基础**：采用 Funato et al. (2012) 的弹性公式、Funato and Ito (2017) 的拓展工作[Ziegler 2021, pp. 2-3][Ziegler 2021, pp. 10-10]。
- **岩心饼化机制**：依据 Corthésy and Leite (2008) 的弹塑性模型（裂缝起裂于岩心中心）以及 Wu et al. (2018) 关于应力体制对起裂位置的影响[Ziegler 2021, pp. 2-3]。
- **现场应力基准**：以 Valley and Evans (2019) 的崩落宽度分析给出的 S~Hmax~ 值和应力体制，以及 Häring et al. (2008) 的注入压力分析、Braun (2007) 的 RACOS 岩心测量为基础[Ziegler 2021, pp. 4-6]。
- **岩石强度参数**：抗拉强度估计参考了 Perras and Diederichs (2014) 的 Hoek‑Brown 方法，以及 Valley and Evans (2019) 的解释[Ziegler 2021, pp. 4-6]。
- **摄影测量对齐**：使用了 Schnabel et al. (2007) 的 RANSAC 形状检测算法[Ziegler 2021, pp. 9-10]。

## Open Questions
- 如何定量分离岩性非均质性、岩石损伤和弹性各向异性对 Δd 变异性的贡献，未从索引片段中确认。
- 缺乏系统性的各向异性修正方案或校正因子，以及如何仅利用岩心获得现场弹性模量各向异性的实用流程，未在片段中详述。
- DCDA 的 ΔS 估计值散布宽的情况下，是否可以通过批统计方法（如概率分布）获得更可信的差应力范围，未从索引片段中确认。
- 此类方法在更长井段、不同岩性及不同应力体制下的适用性有待进一步验证。

## Source Coverage
本页依据给定 18 条索引片段中可用的信息撰写，片段主要覆盖论文的摘要、引言（背景与目标）、研究区概况、部分方法描述（DCDA 原理、摄影测量扫描流程、CMM 参考测量）以及关键发现摘要。缺少详细的结果数据、完整讨论和结论部分的内容：如 DCDA 与 CDF/崩落的定量方向对比统计、ΔS 的具体数值范围、敏感性分析细节、各向异性数值模拟的具体情形与结果均未在片段中出现，因此本 Wiki 仅基于摘要中的定性结论。后续若补充完整论文，可大幅充实证据表和定量可复用声明。
