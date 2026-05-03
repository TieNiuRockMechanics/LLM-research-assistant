---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-li-practical-methodology-for-evaluating-mining-front-stability-based-on-the-diametrical-cor"
title: "Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique."
status: "draft"
source_pdf: "data/papers/2024 - Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.\" *Minerals*, vol. 14, no. 385, 2024, https://doi.org/10.3390/min14040385. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42461"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42358"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.997574"
coverage_status: "full-index"
source_signature: "178641c41dcc9a433bcb3d9c72be339a97f88f53"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:49:26"
---

# Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.

## One-line Summary
本文提出了一种将岩芯直径变形技术（DCDT）与三维数值模拟相结合的实用方法，用于评估采矿工作面的稳定性，并以魁北克北部Eleonore金矿的案例研究进行了演示和验证[Li 2024, pp. 1-2][Li 2024, pp. 12-13]。

## Research Question
如何利用从采矿工作面钻取的岩芯直径变形测量，结合三维数值模拟迭代调整局部应力场，进而评估采矿工作面的应力分布与稳定性？[Li 2024, pp. 1-2][Li 2024, pp. 7-8]

## Study Area / Data
- **地点**：加拿大魁北克北部Eleonore金矿，位于Opinaca水库下方，Roberto区出露地表，走向延伸1.9 km，深度至少1400 m[Li 2024, pp. 2-3]。
- **案例工作面**：530 m水平的存取巷道0530-AMN-509，巷道断面5 m × 5 m，位于wacke岩层中[Li 2024, pp. 2-3][Li 2024, pp. 3-5]。
- **岩芯数据**：从巷道工作面垂直钻取NQ规格（内径47.6 mm）岩芯，总长3 m；前2.5 m因爆破损伤严重碎裂，2.5–3 m段为完整岩芯，用于DCDT测量[Li 2024, pp. 3-5]。
- **力学参数**：wacke岩石完整岩块及岩体力学参数见表1（UCS=162 MPa, σt=15 MPa, Ei=39.05 GPa, Erm=28.62 GPa, ν=0.14, mi=11, RMR=70–84）[Li 2024, pp. 2-3]。
- **原位应力**：矿区最大水平主应力σ₁⁰=19+γz，最小水平应力σ₂⁰=γz，垂直应力σ₃⁰=γz，γ=0.0275 MN/m³[Li 2024, pp. 2-3]。
- **岩芯直径测量**：使用分辨率为0.0001 mm的激光测微仪，测量完整回转360°，重复三次，平均值dmax=47.1950 mm，dmin=47.1604 mm[Li 2024, pp. 3-5]。
- **应力方向标志**：岩芯上标记了重力方向，用于实验室确定应力方向[Li 2024, pp. 3-5]。

## Methods
1. **DCDT分析模型**：采用作者前期发展的基于线弹性岩芯应变释放的解析模型（式2a–2c），利用完整岩石弹性常数（E, ν）及实测直径dmax、dmin计算与钻孔轴线垂直平面内的局部主应力σL、σl[Li 2024, pp. 5-7]。
2. **高精度岩芯直径测量**：使用定制化激光测微系统，对岩芯360°轮廓进行测量，并通过正弦曲线拟合确定最大、最小直径方向，该方向即为局部主应力方向[Li 2024, pp. 3-5]。
3. **三维线弹性数值模型**：建立50 m × 50 m × 50 m的FLAC3D模型，包含25 m长的5 m × 5 m巷道，边界为滚轴约束，模型顶部为505水平，巷道位于530水平。采用wacke岩体参数及原位应力公式（1）初始化模型，并根据DCDT结果旋转σ₃⁰方向（顺时针10°）[Li 2024, pp. 7-8]。网格尺寸在矿面前缘加密至0.075 m，总单元数929,042[Li 2024, pp. 7-8]。
4. **损伤区建模**：因岩芯前2.5 m碎裂，采用前人提出的卸压爆破本构模型，引入岩石破碎因子α和应力消散因子β，损伤区弹性模量Edestress = Eα，泊松比νdestress = ν(2−α)，残余应力张量{σr} = (1−β){σ}，取α=0.4, β=0.6[Li 2024, pp. 8-9]。损伤区深度按岩芯损伤长度近似为2.5 m[Li 2024, pp. 8-9]。
5. **迭代应力调整**：以FLAC3D在岩芯位置（2.5 m深处）的计算主应力σC_L、σC_l与DCDT结果进行比对，迭代调整初始应力σ₂⁰、σ₃⁰的大小和方向，直至差异控制在约5%以内[Li 2024, pp. 9-12]。
6. **稳定性评估**：采用Hoek–Brown破坏准则，以水静压力线（σ₁=σ₃）为基准计算安全系数（FS = (强度)/(外加应力)），分析全工作面稳定性[Li 2024, pp. 9-12][Li 2024, pp. 12-13]。

## Key Findings
- 在岩芯2.5 m处，当孔轴应力σx取12 MPa时，DCDT估算的局部主应力σL=33.6 MPa，σl=6.0 MPa[Li 2024, pp. 9-12]。
- 经五次迭代调整后，局部应力状态调整为σL=26.3 MPa，σl=9.5 MPa，σx=12 MPa，与FLAC3D计算值的差异为σL 2.1%，σl 5%，认为该误差对采矿前缘应力结果无显著影响，可接受[Li 2024, pp. 9-12]。
- 初始DCDT在σx=0下估算的σL=25.0 MPa，σl=3.5 MPa，它们随σx的引入而更新[Li 2024, pp. 5-7]。
- 应变释放方向显示局部最小主应力σl方向为顺时针偏离重力方向10°，即近垂直[Li 2024, pp. 5-7]。
- 损伤区采用α=0.4, β=0.6可合理模拟爆破引起的岩芯碎裂，损伤区深度取2.5 m[Li 2024, pp. 8-9]。
- 全工作面安全系数分布表明，该采矿工作面总体稳定，但局部区域FS较低，且因应力方向倾斜，FS分布不对称[Li 2024, pp. 9-12]。
- DCDT与数值模拟结合的方法能有效评估采矿工作面稳定性，建议未来钻取多根岩芯以提高应力估算及模型预测的可靠性[Li 2024, pp. 12-13]。

## Core Evidence Table
| 证据 | 来源 | 条件 / 背景 | 备注 |
|------|------|-------------|------|
| 实测平均最大直径 dmax=47.1950 mm，最小直径 dmin=47.1604 mm | [Li 2024, pp. 3-5] | NQ钻头，wacke岩芯，2.5 m深处完整岩芯段 | 三次测量平均，激光测微仪分辨率0.0001 mm |
| σL=25.0 MPa, σl=3.5 MPa (σx=0时) | [Li 2024, pp. 5-7] | 采用wacke完整岩石E、ν及DCDT解析模型 | 平面应力假设，σx=0 |
| 局部小主应力方向为顺时针偏离重力10° | [Li 2024, pp. 5-7] | 岩芯标记重力方向，实验室测量对比 | 图7 |
| FLAC3D模型在2.5 m处初始计算应力：σC_L=15.6 MPa, σC_l=13.8 MPa | [Li 2024, pp. 9-12] | 旋转σ₃⁰方向+10°，原位应力公式(1)初始化 | 表2 |
| DCDT更新后 (σx=12 MPa) σL=33.6 MPa, σl=6.0 MPa | [Li 2024, pp. 9-12] | σx取自FLAC3D在2.5 m处的结果 | 式2a–2c，E=39.05 GPa, ν=0.14 |
| 迭代调整后局部应力：σL=26.3 MPa, σl=9.5 MPa, σx=12 MPa | [Li 2024, pp. 9-12] | 调整σ₂⁰和σ₃⁰的大小、方向，共5次迭代 | 表3，最终差异<5% |
| 损伤区参数 α=0.4, β=0.6，深度2.5 m | [Li 2024, pp. 8-9] | 依据岩芯碎裂观察以及前人卸压模型 | 式3–5，参考[13] |
| 安全系数分布显示工作面总体稳定，局部FS较低且不对称 | [Li 2024, pp. 9-12] | Hoek–Brown准则，水静压力线基准FS计算 | 图12 |
| FLAC3D与DCDT结果差异：σL 2.1%, σl 5% | [Li 2024, pp. 9-12] | 五次迭代后，2.5 m深度 | 表4 |

## Limitations
- 本案例仅基于一根岩芯进行DCDT测量，缺乏复测验证，代表了单一的局部应力点[Li 2024, pp. 5-7]。
- 损伤区深度直接根据岩芯碎裂长度近似为2.5 m，未进行更精细的钻孔摄像或物探确认[Li 2024, pp. 8-9]。
- 安全系数的阈值并未给出，仅提出由分析者自行决定[Li 2024, pp. 9-12][Li 2024, pp. 12-13]。
- 损伤区建模中使用的α、β值取自前人卸压爆破研究，未针对该特定岩体进行标定[Li 2024, pp. 8-9]。
- 数值模型为线弹性，未考虑岩体屈服后行为或渐进破坏[Li 2024, pp. 7-8]。
- 将岩芯损伤主要归因于爆破振动，可能忽略了其他原因（如应力集中造成的开裂）[Li 2024, pp. 3-5]。

## Assumptions / Conditions
- 岩石在卸载过程中行为遵循线弹性，DCDT解析模型基于此假设[Li 2024, pp. 3-5][Li 2024, pp. 5-7]。
- 在自由面上，孔轴方向应力σx=0，属于平面应力状态；而在面板后方，σx>0，应力状态为三维，必须由数值模型提供σx[Li 2024, pp. 5-7][Li 2024, pp. 12-13]。
- DCDT测得的直径最大/最小方向直接对应局部大/小主应力方向[Li 2024, pp. 5-7]。
- 损伤区是由于前一轮爆破引起的，可采用基于破碎因子和应力消散因子的卸压本构模型进行模拟[Li 2024, pp. 8-9]。
- 模型中岩体力学参数取自Eleonore矿区2008年地质力学调查报告，适用于wacke岩体[Li 2024, pp. 2-3]。
- 原位应力场基于矿区应力测量公式(1)，其中最大水平主应力平行于巷道轴向，且在自由面上该应力自然为零[Li 2024, pp. 5-7]。
- 安全系数计算以Hoek–Brown准则中从水静压力线（σ₁=σ₃）量测强度和应力之比为基础[Li 2024, pp. 9-12]。
- 迭代调整仅改变σ₂⁰和σ₃⁰的大小与方向，σ₁⁰保持与公式（1）一致[Li 2024, pp. 9-12]。

## Key Variables / Parameters
- 岩芯直径：dmax, dmin, do（原始直径）[Li 2024, pp. 3-5][Li 2024, pp. 5-7]
- 局部主应力：σL, σl (YZ平面内大/小主应力)[Li 2024, pp. 5-7]
- 孔轴应力：σx[Li 2024, pp. 5-7]
- 完整岩石弹性常数：E=39.05 GPa, ν=0.14[Li 2024, pp. 2-3][Li 2024, pp. 5-7]
- 损伤区参数：α=0.4 (破碎因子), β=0.6 (应力消散因子)[Li 2024, pp. 8-9]
- 岩体力学参数：UCS=162 MPa, σt=15 MPa, Erm=28.62 GPa, ν=0.14, mi=11, RMR=70–84[Li 2024, pp. 2-3]
- 原位应力分量：σ₁⁰=19+γz, σ₂⁰=γz, σ₃⁰=γz, γ=0.0275 MN/m³[Li 2024, pp. 2-3]
- 方向参数：θ₀ (初始大主应力方向，旋转10°), θC (FLAC3D计算大主应力方向)[Li 2024, pp. 5-7][Li 2024, pp. 9-12]
- Hoek–Brown参数：m, s（由mi和RMR导出）[Li 2024, pp. 9-12]

## Reusable Claims
- 当岩芯来自垂直于采矿工作面的钻孔时，DCDT可估算工作面平面内的诱导主应力大小与方向，若σx由数值模型提供，可用于面板后方位置的应力推算[Li 2024, pp. 5-7][Li 2024, pp. 12-13]。
- 通过DCDT结果迭代调整局部三维数值模型的原位应力分量（σ₂⁰、σ₃⁰的大小和方向），可使模型计算应力与DCDT估算值吻合，差异控制在5%以内被认为是可接受的工程误差[Li 2024, pp. 9-12]。
- 若岩芯存在爆破损伤区，可将其视为卸压带，采用岩石破碎因子α和应力消散因子β的简化本构模型进行模拟，损伤区范围可按岩芯碎裂长度近似确定[Li 2024, pp. 8-9]。
- 基于Hoek–Brown准则，从水静压力线量测强度与施加应力之比，可计算采矿工作面的安全系数，用于稳定性评估，但判别破坏的FS阈值需由分析者确定[Li 2024, pp. 9-12][Li 2024, pp. 12-13]。
- 该方法适用于有或无可见损伤区的采矿工作面稳定性评估，流程包括现场取芯、室内直径测量、DCDT解析计算、数值模型迭代调整及破坏准则判定[Li 2024, pp. 1-2][Li 2024, pp. 12-13]。

## Candidate Concepts
- [[Diametrical Core Deformation Technique (DCDT)]]
- [[mining front stability]]
- [[stress relief by core drilling]]
- [[linear elastic rock behavior]]
- [[Hoek-Brown failure criterion]]
- [[factor of safety from hydrostatic line]]
- [[damage zone in rock core]]
- [[destress blasting model]]
- [[local stress field around excavation]]
- [[blast-induced rock damage]]
- [[in situ stress rotation]]
- [[finite difference method (FLAC3D)]]

## Candidate Methods
- [[DCDT analytical model (Li & Mitri 2023)]]
- [[high-precision laser micrometer core diameter measurement]]
- [[3D linear-elastic numerical modeling with FLAC3D]]
- [[iterative in-situ stress adjustment using DCDT feedback]]
- [[damage zone simulation using fragmentation factor α and dissipation factor β]]
- [[Hoek-Brown FS calculation based on hydrostatic line]]
- [[mesh sensitivity analysis for convergence]]

## Connections To Other Work
- 本文DCDT理论基于作者先前研究：Li & Mitri (2023)《Methodology for the estimation of mining face stresses using rock core diametrical deformation》[Li 2024, pp. 5-7][Li 2024, pp. 13-13]，以及2022年的技术介绍[Li 2024, pp. 13-13]。
- 损伤区建模沿用了Vennes等(2020)提出的卸压爆破本构模型，其中引入α、β因子[Li 2024, pp. 8-9][Li 2024, pp. 13-13]；泊松比修正方法参考Tang & Mitri (2001)[Li 2024, pp. 8-9][Li 2024, pp. 13-13]。
- 原位应力场方向依据Hauta等(2020)在Eleonore矿区的反分析结果，确认最大水平主应力平行于巷道轴向[Li 2024, pp. 5-7][Li 2024, pp. 13-13]。
- 采矿诱导应力相关研究（Singh et al. 2011; Shabanimashcool & Li 2012, 2013; Li et al. 2018等）构成本文问题的背景[Li 2024, pp. 1-2][Li 2024, pp. 13-13]。
- 破坏准则选择Hoek & Brown (1980, 1997)[Li 2024, pp. 9-12][Li 2024, pp. 13-13]；安全系数计算思路参考Shoerey et al. (1989)、Yudhbir et al. (1983)、Bieniawski (1974)等[Li 2024, pp. 12-13][Li 2024, pp. 13-13]。
- 岩芯变形分析方法参照Funato & Ito (2017)的思路[Li 2024, pp. 3-5][Li 2024, pp. 13-13]。

## Open Questions
- 若钻取多根岩芯（如4根），能否显著提高应力场估计的精度和稳定性评估的可靠性？[Li 2024, pp. 12-13]
- 在其他类型岩体（非wacke）或不同深度条件下，该方法是否依然适用且具有相似的误差水平？[未确认]
- 安全系数的阈值如何根据具体工程要求合理确定，才能准确指示局部破坏？[Li 2024, pp. 12-13]
- 损伤区参数α和β可否通过现场实测（如声波测试）进行更准确的标定？[Li 2024, pp. 8-9]
- 随着采矿推进，应力场动态变化，该方法如何实现快速周期性的稳定性评估？[Li 2024, pp. 12-13]
- 线弹性假设能否扩展至考虑压剪屈服或应变软化，以更真实地预测破坏形态？[未确认]

## Source Coverage
本页面已处理所有9个非空索引片段，覆盖范围：区块覆盖率100%，字符覆盖率99.76%。索引片段包括[Li 2024, pp. 1-2]至[Li 2024, pp. 13-13]，总计42,361字，其中42,358字被编译，编译策略为single-pass-markdown。所有引用均来自提供的源标签，未添加外部虚构内容。
