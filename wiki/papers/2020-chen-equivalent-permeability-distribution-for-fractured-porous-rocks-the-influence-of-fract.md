---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks The Influence of Fracture Network Properties.pdf"
collections:
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.\" *Geofluids*, vol. 2020, 2020, pp. 1-12, doi:10.1155/2020/6751349."
indexed_texts: "12"
indexed_chars: "56247"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "56488"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004285"
coverage_status: "full-index"
source_signature: "0d74ab30477922bca7f61d2ee55db625336fe9a2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:26:36"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.

## One-line Summary
统计分布研究显示，裂缝多孔岩石的等效渗透率分布形状与裂缝网络几何（长度、数量）强烈相关，对角线分量由幂律分布转为对数正态分布，且均值随裂缝密度线性增加，为随机等效渗透率模型提供了定量依据。[Chen 2020, pp. 1-2; 9-10]

## Research Question
裂缝网络几何性质（裂缝长度和数量）如何影响等效渗透率的统计分布？具体包括：对角线分量和非对角线分量的直方图形状如何随裂缝几何变化？等效渗透率均值与裂缝密度之间存在怎样的定量关系？[Chen 2020, pp. 2-2; 9-10]

## Study Area / Data
研究基于合成二维离散裂缝模型，区域大小为20 m × 20 m。裂缝长度服从幂律分布（下界lmin从4 m增加至6 m、8 m、10 m；上界lmax固定为40 m），裂缝数量N从50增加至75、100、125，共生成16组离散裂缝模型，每组取10次实现。裂缝位置和方位随机生成。裂缝孔径假定为常数1.2×10⁻⁴ m，裂缝渗透率依据立方定律为1.2×10⁻⁹ m²；基质渗透率设为9.87×10⁻¹⁶ m²（1 md）。[Chen 2020, pp. 2-3; 3-4; 8-9]

## Methods
采用**多重边界法（multiple boundary method）** 将离散裂缝模型的等效渗透率升尺度至等效裂缝模型。步骤包括：1）将裂缝网络划分为2 m × 2 m的网格块；2）对每个网格块内的离散裂缝模型进行非结构化网格剖分，施加线性边界条件（沿x轴和y轴）并求解稳态流动问题；3）利用Darcy定律的矩阵形式反算等效渗透率张量kxx、kyy和kxy（假设kxy = kyx）。流动模拟通过MATLAB Reservoir Simulation Toolbox (MRST)完成。等效渗透率的统计分布通过直方图分析，并采用最小二乘法对直方图进行拟合；同时定义了无量纲等效渗透率k′ = k/km和无量纲裂缝密度ρ = (1/A)∑(li/2)²，用于分析等效渗透率与裂缝几何的关系。[Chen 2020, pp. 2-3; 3-4; 4-6; 6-8]

## Key Findings
1. **直方图形状演化**：当lmin较小且N较少时（如lmin=4 m, N=50），对角线分量kxx和kyy的直方图呈幂律状分布；随着裂缝长度和数量增加，直方图形状转变为对数正态状分布。非对角线分量kxy的直方图呈正态状分布，且随裂缝几何改变，其分布范围对称扩展。[Chen 2020, pp. 4-6; 9-10]
2. **对角线分量的线性关系**：无量纲对角线等效渗透率k′xx和k′yy的均值随无量纲裂缝密度ρ线性增加，拟合关系为k′diag = a·ρ + b，其中斜率a约20，截距b约30。其标准差也随ρ增加。[Chen 2020, pp. 6-8]
3. **非对角线分量行为**：kxy的均值在零附近小幅波动，但其标准差和分布范围随ρ增大而增加。[Chen 2020, pp. 6-8]
4. **张量各向异性**：kxx、kyy和kxy的空间分布差异由裂缝方位主导，体现了裂缝岩石的强各向异性，强调需使用全张量形式描述等效渗透率。[Chen 2020, pp. 4-6; 9-10]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 对角线等效渗透率直方图由幂律状变为对数正态状 | [Chen 2020, pp. 4-6] | lmin从4 m增至10 m，N从50增至125；10次实现 | 形状变化与裂缝连通性增强一致 |
| 非对角线分量kxy直方图始终保持正态状，对称分布于0附近 | [Chen 2020, pp. 4-6] | 同上述参数变化 | 范围随lmin和N增加而展宽 |
| 对角线分量均值与裂缝密度呈线性关系，斜率约20 | [Chen 2020, pp. 6-8] | ρ范围2–14，k′diag范围50–350 | 与单网格块研究结果可比（Leung & Zimmerman, 2012） |
| kxy均值不随ρ变化，但其标准差增加 | [Chen 2020, pp. 6-8] | 同上 | 由倾斜裂缝的转换公式解释 |
| 恒定裂缝孔径假设下，裂缝网络连通性（长度和数量）是控制等效渗透率分布的主要因素 | [Chen 2020, pp. 2-2; 8-9] | 裂缝孔径1.2×10⁻⁴ m，基质渗透率1 md | 变孔径情况会影响分布，需进一步研究 |

## Limitations
- 研究仅考虑二维离散裂缝模型，假设裂缝垂向延伸，而实际裂缝倾角随机时，二维结果与三维存在差异，且从二维外推到三维需结合具体地质背景和裂缝几何。[Chen 2020, pp. 9-10]
- 裂缝孔径设为常数，忽略了天然裂缝中孔径的非均质性及其与长度、应力状态的关联，可能导致等效渗透率高估（与孔径非均质情况相比可达6倍）或低估大裂缝的控制作用。[Chen 2020, pp. 8-9]
- 固定域尺寸（20 m×20 m）和每组参数仅10次实现虽已满足当前稳定性要求，但引入更多因素时需考虑多尺度域尺寸和更多实现以获得更稳健的统计结果。[Chen 2020, pp. 8-9]
- 三维升尺度在数据可用性、采样偏差校正、基准模型和高效计算平台方面仍有限制。[Chen 2020, pp. 9-10]

## Assumptions / Conditions
- 裂缝长度服从幂律分布，指数介于1.3–3.5之间，且研究采用下界lmin和上界lmax截断的分布。[Chen 2020, pp. 2-3]
- 所有裂缝具有恒定孔径1.2×10⁻⁴ m，且每条裂缝对流动贡献相同。[Chen 2020, pp. 3-4; 8-9]
- 等效渗透率张量假设对称，即kxy = kyx。[Chen 2020, pp. 3-4; 4-6]
- 升尺度网格块采用2 m×2 m尺寸，线性边界条件施加压力梯度1 Pa/m。[Chen 2020, pp. 3-4]
- 传感器效应（censoring effect）对幂律分布裂缝网络在本研究中不是严重问题。[Chen 2020, pp. 2-3]
- 岩石基质具有孔隙度和渗透率，允许未连通裂缝间发生流动。[Chen 2020, pp. 2-2]

## Key Variables / Parameters
- 等效渗透率张量分量：kxx, kyy, kxy（单位m²）[Chen 2020, pp. 3-4]
- 无量纲等效渗透率：k′ = k/km，km = 9.87×10⁻¹⁶ m² [Chen 2020, pp. 6-8]
- 裂缝长度下界 lmin（4, 6, 8, 10 m）[Chen 2020, pp. 2-3]
- 裂缝数量 N（50, 75, 100, 125）[Chen 2020, pp. 2-3]
- 无量纲裂缝密度 ρ = (1/A)∑(li/2)² [Chen 2020, pp. 6-8]
- 裂缝孔径（常数1.2×10⁻⁴ m）[Chen 2020, pp. 3-4]
- 幂律长度分布指数 a（未指定具体值，工作范围内为1.3–3.5）[Chen 2020, pp. 2-3]
- 域尺寸 20 m × 20 m [Chen 2020, pp. 2-3]

## Reusable Claims
- 基于多重边界法的二维升尺度结果表明，当裂缝长度和数量增加时，对角线等效渗透率的直方图从幂律状迁移至对数正态状，而非对角线分量保持正态状。[Chen 2020, pp. 4-6]
- 对角线等效渗透率的均值与裂缝密度呈线性正相关，斜率约20，这一关系可用于从裂缝密度推断均值渗透率。[Chen 2020, pp. 6-8]
- 等效渗透率张量的各分量空间分布各不相同，主要受裂缝方位控制，表明在裂缝性多孔岩石流动模拟中必须采用全张量形式。[Chen 2020, pp. 4-6; 9-10]
- 恒定裂缝孔径假设下，裂缝连通性（由长度和数量表征）是等效渗透率分布形状转变的主要驱动力。[Chen 2020, pp. 2-2; 8-9]
- kxy的标准差随裂缝密度增大而增大，均值维持在零附近，该行为可由倾斜裂缝的坐标转换公式解释。[Chen 2020, pp. 6-8]
- 多重边界法利用网格块多个边界的流量信息计算等效渗透率，相较于单边界法能更好地匹配解析解，避免低估渗透率。[Chen 2020, pp. 3-4]

## Candidate Concepts
- [[multiple boundary method]]
- [[equivalent permeability distribution]]
- [[power law fracture length distribution]]
- [[lognormal-like distribution of permeability]]
- [[fracture connectivity]]
- [[dimensionless fracture density]]
- [[fracture aperture heterogeneity]]
- [[anisotropy of fractured porous rocks]]
- [[stress-dependent aperture]]
- [[censoring effect in fracture sampling]]
- [[discrete fracture model]]
- [[equivalent fracture model]]

## Candidate Methods
- [[multiple boundary upscaling method]]
- [[linear boundary condition for upscaling]]
- [[ADFNE code for stochastic fracture generation]]
- [[MRST for flow simulation in fractured models]]
- [[least square histogram fitting]]
- [[Darcy's law inversion for equivalent permeability tensor]]
- [[dimensionless permeability and fracture density analysis]]
- [[power law distribution sampling]]

## Connections To Other Work
- 与Leung & Zimmerman (2012)的成果一致：单网格块等效渗透率随裂缝密度线性增加，本研究推广至网格块均值的线性关系。[Chen 2020, pp. 6-8; 11-12]
- 等效渗透率的幂律状直方图与Chen et al. (2018)对三维弱连通离散裂缝模型的升尺度结果相似。[Chen 2020, pp. 4-6]
- 升尺度方法沿用Chen et al. (2015)提出的多重边界法，该方法被证明在复杂裂缝网络中比单边界法更准确。[Chen 2020, pp. 2-2; 3-4]
- 孔径-长度相关性影响的讨论与Baghbanan & Jing (2007, 2008)的结论一致：变孔径下大裂缝控制渗透率。[Chen 2020, pp. 8-9]
- 对幂律长度分布、裂缝密度和连通性的处理建立在Bonnet et al. (2001)、de Dreuzy et al. (2001)等基础研究之上。[Chen 2020, pp. 2-3; 8-9]

## Open Questions
- 当裂缝孔径非均质且与长度和应力状态相关时，等效渗透率分布将会如何变化？[Chen 2020, pp. 8-9]
- 三维天然裂缝岩石的等效渗透率分布能否由二维结果经适当校正后预测？[Chen 2020, pp. 9-10]
- 不同功率律指数a和域尺寸对渗透率分布形状转变点有何影响？[Chen 2020, pp. 2-3; 8-9]
- 将升尺度的分布模型纳入随机渗透率场生成时，如何保证各向异性张量的内在一致性？[Chen 2020, pp. 4-6]

## Source Coverage
所有12个非空索引片段均已处理并纳入本页面。覆盖度统计：基于原始片段文本，按字符数计算的覆盖比为1.004，按索引块数计算的覆盖比为1.0（片段索引完全处理）。编译后的源块数为12，字符总数56488，与原始索引区段签名0d74ab3匹配，覆盖状态为“full-index”。本次采用单pass markdown编译策略。
