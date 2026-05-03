---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-wang-ling-ling-seismic-prediction-method-of-multiscale-fractured-reservoir"
title: "Seismic Prediction Method of Multiscale Fractured Reservoir."
status: "draft"
source_pdf: "data/papers/2018 - Seismic prediction method of multiscale fractured reservoir.pdf"
collections:
  - "part1"
citation: "Wang Ling-Ling, et al. \"Seismic Prediction Method of Multiscale Fractured Reservoir.\" *Applied Geophysics*, vol. 15, no. 2, June 2018, pp. 240-52. DOI:10.1007/s11770-018-0667-8."
indexed_texts: "10"
indexed_chars: "47095"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46355"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.984287"
coverage_status: "full-index"
source_signature: "644c634562e68b07f4c59bb2ec69bec12759456d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:15:11"
---

# Seismic Prediction Method of Multiscale Fractured Reservoir.

## One-line Summary
[Wang 2018, pp. 1-2] 提出一种基于裂缝密度分布的叠后‑叠前联合多尺度裂缝预测方法：利用曲波变换多方向相干技术提取宏观裂缝（大于1/4波长）密度，利用叠前衰减属性方位各向异性反演提取介观裂缝（1/4–1/100波长）密度，将两者融合以区分裂缝尺度并改善密度连续性。

## Research Question
[Wang 2018, pp. 1-2] 常规叠前裂缝预测方法难以清晰区分不同尺度的裂缝；宏观与介观裂缝的预测结果常通过分离或叠合对比，且宏观裂缝预测仅给出方位和属性值，缺少裂缝密度。因此，如何基于裂缝密度实现宏观‑介观裂缝的一体化预测，避免介观方法造成的密度不连续问题，是该文的科学问题。

## Study Area / Data
[Wang 2018, pp. 4-5] 采用中国西部某裂缝性储层的三维地震物理模型。模型尺寸100 cm × 100 cm × 20 cm（对应实际10000 m × 10000 m × 2000 m），速度相似比1:2，频率相似比5000:1。模型共6层，目标层为大安寨层（Da’anzhai layer），厚约190 m，分为上、下两部分。模型中心简化区含8组裂缝带（宏观裂缝为主，含部分介观‑微观裂缝），南部复杂区含9组裂缝带、7组交叉裂缝、7个裂缝簇及随机裂缝带（多为大角度介观裂缝）。裂缝密度0.95条/米（第三组可变密度，范围0.319–1.336条/米）。数据采集采用宽方位长偏移距三维观测系统，方位纵横比0.84，采样间隔1 ms，主频0.23 MHz（对应实际46 Hz）。处理流程包括球面扩散补偿、高速滤波、反褶积、速度分析、Radon滤波、分方位角叠加及叠后时间偏移等。

## Methods
[Wang 2018, pp. 2-3] **宏观裂缝预测——基于曲波变换的多方向相干技术**  
1. 用第二代离散曲波变换将叠后振幅数据分解为多尺度多方向数据体（方向数 L=8，方位间隔约22.5°）；  
2. 计算各方向数据的相干属性，识别最小相干系数 `(Cl)min` 及对应方向；  
3. 裂缝密度 FI = 1.0 − `(Cl)min`，裂缝方位 FR = 90/L × (l−1) + 180/L（l 为最小相干对应方向序号），若工区有倾角需校正。  

[Wang 2018, pp. 3-4] **介观裂缝预测——叠前衰减属性方位各向异性反演**  
1. 基于 Chichinina et al. (2006) 的 P 波衰减随偏移距和方位变化的表达式（QVOA），将叠前道集按方位角（6个扇区，中心角11.5°~168.5°）划分；  
2. 从方位数据反演频率衰减梯度、吸收品质因子等衰减属性；  
3. 对各属性在 6 个方位的值进行椭圆拟合，椭圆率表示裂缝密度，椭圆长/短轴方向给出裂缝方位；特别选用频率衰减梯度属性，因其对介观裂缝更敏感、信噪比更高。  

[Wang 2018, pp. 4, 11‑12] **裂缝密度融合**  
因两种方法给出的密度范围均为0–1，可直接融合。采用加权平均法和装配法：加权平均法强调宏观裂缝带边界，装配法突出介观裂缝的小尺度密度分布。

## Key Findings
[Wang 2018, pp. 7, 9‑11]  
- 曲波变换多方向相干技术可有效识别断层和宏观裂缝，裂缝密度在裂缝带边界呈环状分布，但对介观裂缝不敏感。  
- 频率衰减梯度属性对介观裂缝高度敏感，能识别出模型中的7个裂缝簇（与实际一致），且其反演的裂缝方位（60.7°）与模型（60°）吻合最佳；但将该属性用于宏观裂缝时，密度分布不连续，呈多个小尺度密度团，易被误解释为介‑微观裂缝。  
- 融合后的裂缝密度图（加权平均或装配）增强了断层的连续性，清晰区分了宏观与介观裂缝，解决了叠前方位各向异性方法预测宏观裂缝时密度不连续的问题。  

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 曲波变换多方向相干预测出的宏观裂缝密度在简化区呈环状，低速度基质材料环带更宽（阻抗差大）。 | [Wang 2018, pp. 5-7] | 叠后振幅数据，8个方向分解，C3相干算法 | 方位受裂缝带边界能量主导，内部裂缝方位未能揭示。 |
| 频率衰减梯度属性可识别7个裂缝簇，预测密度范围0.31–0.56。 | [Wang 2018, pp. 9-11] | 偏移距800–4781.25 m，方位角等分6扇区，覆盖率27次 | 吸收品质因子结果存在与模型不符的假象，频率衰减梯度无此假象。 |
| 在CDP(InLine 408, XLine 781)处，频率衰减梯度反演的裂缝密度为0.518，方位60.7°，与模型（密度0.95条/米，方位60°）接近；振幅属性密度仅0.332。 | [Wang 2018, pp. 9-11] | 介观裂缝带，模型方位60° | 衰减属性对介观裂缝敏感度优于振幅。 |
| 融合方法（加权平均）使宏观裂缝带边界更清晰，装配法使介观小尺度密度分布更明显。 | [Wang 2018, pp. 11-12] | 密度值均归一化至0–1 | 融合后有效密度宏观区0–0.35，介观区0.31–0.56。 |
| 宏观裂缝预测不能给出裂缝产状的一一对应关系，远离断层的裂缝带密度与位置对应差。 | [Wang 2018, pp. 7] | 简化和复杂区均适用 | 高密度出现在断层边缘，而非裂缝带内部。 |

## Limitations
[Wang 2018, pp. 1-2, 7, 11]  
- 方法仅针对宏观（>λ/4）和介观（λ/4‑λ/100）裂缝，无法预测微观裂缝；微观裂缝仅能通过岩心电镜观察。  
- 曲波变换多方向相干技术对介观裂缝不敏感，而叠前衰减属性用于宏观裂缝时密度不连续，容易产生解释偏差。  
- 宏观裂缝预测的方位受裂缝带边界能量干扰，可能反映边界走向而非裂缝真实走向。  
- 衰减属性反演依赖等效参数 ∆N、∆I N、∆T，这些参数在物理模型中通过拟合估计，实际资料中难以精确获取。  
- 物理模型的裂缝采用等效介质模拟，未考虑真实裂缝形态和复杂填充流体，适用性需实际资料验证。

## Assumptions / Conditions
[Wang 2018, pp. 3-5, 7‑9]  
- 除变倾角裂缝带外，裂缝带被视为具有水平横向各向同性（HTI）的等效介质。  
- 宏观裂缝预测使用叠后振幅数据，并假设反射波振幅的空间变化主要由断层和裂缝带引起；方向分解时仅考虑方向变化，尺度固定。  
- 介观裂缝预测基于 Chichinina et al.（2006）的 QVOA 近似，入射角范围0–40°，且裂缝为垂直排列、液态充填。  
- 方位角分选保证各扇区覆盖次数相等（中心次数27次），保留远偏移距以增强各向异性。  
- 频率衰减梯度被选为最优预测属性，其信噪比高于吸收品质因子，且对宏观裂缝不敏感。  
- 融合时两种密度均未归一化，直接加权或装配。

## Key Variables / Parameters
[Wang 2018, pp. 2-4, 5, 9‑11]  
- 裂缝密度 FI（宏观，由最小相干系数计算）；介观裂缝密度（椭圆率）。  
- 裂缝方位 FR（度）。  
- 相干系数 `(Cl)min`；方向序号 l（1≤l≤L，L=8）。  
- 衰减属性：最大能量、频率衰减梯度、吸收品质因子 Q。  
- 衰减各向异性因子 εQ、截距 C 和斜率 G。  
- 等效复弱度 ∆N、∆I N、∆T（物理模型中拟合为 0.43、0.06、0.50 用于宏观，0.35、0.17、0.53 用于介观）。  
- 入射角 θ、方位角 φ、裂缝对称轴方位 φs。  
- 频率 40 Hz（模型目标频率）；裂缝密度（条/米），如简化区 0.95 条/米，第三组可变密度 0.319‑1.336。

## Reusable Claims
[Wang 2018, pp. 1-3]  
- 基于曲波变换的多方向相干技术可以从叠后数据提取宏观裂缝的密度和方位，但对介观裂缝不敏感。  
- Chichinina et al.（2006）的 QVOA 公式是叠前衰减属性预测垂直裂缝参数的理论基础，入射角0–40°时有效。  
- 频率衰减梯度属性对介观裂缝的敏感度显著高于振幅属性和最大能量属性，适合介观裂缝密度反演。  
- 将宏观与介观裂缝预测结果按裂缝密度融合可以区分裂缝尺度，并克服单独使用介观方法时宏观裂缝密度不连续的问题。  
- 裂缝密度范围0–1时无需归一化可直接融合，加权平均法利于突出宏观边界，装配法利于突出小尺度裂缝。  
- 球面扩散补偿是使用衰减属性的必要处理步骤，可恢复深层和远偏移距振幅（证据来自物理模型单炮记录对比）。  
- 方位角分选需保证覆盖次数一致，中心角范围对称分布，以提供可靠各向异性数据。  
- 介观裂缝带的衰减大于宏观裂缝带，且衰减随方位角变化更显著，表明衰减各向异性对裂缝尺寸敏感。

## Candidate Concepts
[[multiscale fracture]], [[fracture density]], [[fracture orientation]], [[curvelet transform]], [[multidirectional coherence]], [[poststack seismic attribute]], [[azimuthal anisotropy]], [[attenuation anisotropy]], [[QVOA]], [[frequency attenuation gradient]], [[absorption quality factor]], [[HTI medium]], [[seismic physical model]], [[equivalent fracture zone]], [[spherical diffusion compensation]], [[fracture cluster]], [[macro-fracture]], [[meso-fracture]], [[micro-fracture]]

## Candidate Methods
[[Multidirectional coherence technique based on curvelet transform]], [[Prestack azimuthal attenuation inversion]], [[Frequency attenuation gradient attribute inversion]], [[Azimuthal ellipse fitting for fracture parameters]], [[Fracture density integration (weighted average and assembly)]], [[Spherical diffusion compensation for attenuation preservation]], [[Azimuth sectoring of prestack gathers]], [[C3 coherence algorithm on directional data]]

## Connections To Other Work
[Wang 2018, pp. 1-2, 12‑13]  
- 介观裂缝预测的理论基础来自 Chichinina et al. (2006) 的 QVOA 表达式和 Rüger (1997) 的 PP 波反射系数近似。  
- 裂缝尺度划分引用 MacBeth and Li (1999) 的宏观/介观/微观分类。  
- 曲波变换的多尺度相干由 Zheng et al. (2009)、Zhang et al. (2011) 发展为多方向相干技术。  
- 叠前方位各向异性预测裂缝已有诸多应用（如 Qu et al., 2001; Yin et al., 2012; Wang et al., 2014; An, 2015），但均未基于密度进行多尺度融合。  
- Chen et al. (2016) 提出了地质‑测井‑地震多尺度综合预测方法，但未将宏观与介观地震预测以密度方式融合。

## Open Questions
[Wang 2018, pp. 11-12]  
- 如何将微观裂缝（岩心电镜尺度）纳入地震预测综合框架，实现真‑三‑尺度统一？  
- 文中融合方法的选择（加权平均 vs. 装配）尚缺乏定量准则，实际应用中如何根据储层特征自动优选？  
- 频率衰减梯度属性在含不同流体（油、气、水）的裂缝储层中的敏感性差异尚未探讨。  
- 物理模型中裂缝取向与边界效应强相关，实际地震数据中如何减弱地层倾角或岩性边界对密度‑方位的影响？  
- 所述方法在野外实际三维宽方位地震资料中的适用性和反演精度需进一步验证。  
- 文中采用的 QVOA 近似假设裂缝垂直、液态充填，对于倾斜裂缝或干裂缝的拓展形式有待研究。

## Source Coverage
本次汇编使用了全部10个非空索引片段片段来源 [Wang 2018, pp. 1-13]，总计已索引字符数47095，汇编后字符数46355，覆盖比率按区块计为1.0，按字符计为0.984。所有非空索引片段均已处理，无缺失。
