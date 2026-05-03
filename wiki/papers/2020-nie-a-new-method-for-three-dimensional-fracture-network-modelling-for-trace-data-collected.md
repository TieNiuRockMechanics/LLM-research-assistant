---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-nie-a-new-method-for-three-dimensional-fracture-network-modelling-for-trace-data-collected"
title: "A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window."
status: "draft"
source_pdf: "data/papers/2020 - A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Nie, Zhenbang, et al. \"A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.\" *Rock Mechanics and Rock Engineering*, vol. 53, 2020, pp. 1145-1161, doi:10.1007/s00603-019-01969-4."
indexed_texts: "13"
indexed_chars: "63131"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62548"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990765"
coverage_status: "full-index"
source_signature: "29145b4308130c10741353efba2643ee225087fa"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:44:54"
---

# A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.

## One-line Summary

本文提出一种针对大采样窗口（裂隙两端均可见）采集的迹长数据的三维裂隙网络建模新方法，重点通过随机数学推导确定裂隙圆盘直径，并结合大藤峡水电站工程实例验证了方法的合理性与精度。

## Research Question

如何利用大采样窗口（绝大多数裂隙两端可见）获取的迹长数据，简单快速地建立三维裂隙网络模型？核心在于如何避免传统小窗口方法中的删截校正等繁琐步骤，直接确定裂隙圆盘直径分布。

## Study Area / Data

研究区位于中国广西桂平市黔江流域大藤峡水电站枢纽泄水闸下游。选取#28坝段下游D₁y1-2和D₁y1-3地层的岩体裂隙。该处岩层为下泥盆统那高岭组（D₁n）和郁江组（D₁y），软层发育，裂隙多陡倾。现场采用大采样窗口法：D₁y1-3采集面积693.5 m²，共277条裂隙；D₁y1-2采集面积807.3 m²，共390条裂隙。采集时裂隙两端均可见，迹长大于0.5m。记录内容包括端点坐标、倾向、倾角、开度、充填物等。采用Shanley和Mahtab方法分组，得到两组主要裂隙（Set 1和Set 2），两组均用于建模。

## Methods

1. **裂隙圆盘直径确定**
   - 假设裂隙为圆形薄盘，盘中心至迹线中点的距离u在[0, r]上均匀分布，即 u/r ~ U(0,1)。由此导出 E(ch²/r²) = 2/3，进而得 E(r²) = 1.5 E(ch²)（r为圆盘半径，ch为半迹长）。
   - 设定r²的可能分布类型（正态、对数正态、Gamma、负指数），通过试错法调整 D(r²) 使生成的随机数ch²的方差D(ch²)与现场数据一致。
   - 利用卡方检验比较模拟ch与现场ch，选定r²的最优分布类型。
   - 对揭露面上的半径r进行三维校正：裂隙与揭露面夹角θ，采集概率 f = (2r sinθ)/L，通过将r的随机数等分为X个区间（X=100），由 nab 转换得到三维空间中 n′ab，生成三维半径r′，再用卡方检验确定r′的分布。

2. **裂隙方位和密度**
   - 方位校正：采用等面积施密特投影图，将投影网分为47个等面积区，利用 P₁ = Nα/∑Nα 与 N′α = Nα / sinα 校正各区间频率，最终得到三维方位频率 P₂ = N′α / ∑N′α。
   - 密度确定：试错法。预设三维网络裂隙数n，生成网络后用同方位虚拟平面切割，得到虚拟迹线数N′。当 N′ = (A′/A) N 时（A′为虚拟面面积，A为现场采集面积，N为现场裂隙数），对应的n即为密度。

3. **三维网络生成**
   - 基于蒙特卡洛模拟，随机合成裂隙中心坐标（Poisson分布）、圆盘直径（r′分布）和方位（校正后分布），生成完整三维裂隙网络。

## Key Findings

- 通过理论推导与多种r分布模拟证实 E(r²)/E(ch²) ≈ 1.5（见原文表1）。
- D₁y1-3和D₁y1-2两组裂隙的r²分布均优选对数正态分布（表3）；校正后的三维半径r′也符合对数正态分布（表4）。
- 模拟迹线统计参数（Fisher常数、迹线条数、P20、P21、迹长均值与标准差）与现场数据比较，相对误差均小于10%（表6）。
- 模拟迹长概率密度曲线与现场曲线高度吻合，相关系数R均大于0.99（图12）。
- 忽略ch<0.25m的小裂隙，E(ch²)和D(ch²)变化在10%以内，对建模影响可忽略（表7）。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| E(r²)=1.5 E(ch²) 由随机切割假设推导并数值验证 | [Nie 2020, pp. 3-4] | 裂隙中心随机，u/r~U(0,1) | 表1中各种r分布模拟结果均接近1.5 |
| 模拟迹长统计量与现场数据误差<10% | [Nie 2020, pp. 13-14, Table 6] | 大采样窗口，两端可见 | 包括Fisher常数、P20、P21、均值、标准差 |
| 忽略ch<0.25m裂隙对E(ch²)和D(ch²)影响<10% | [Nie 2020, pp. 15-16, Table 7] | 截断数据 | 工程上可接受 |
| 校正后三维半径r′符合对数正态分布 | [Nie 2020, pp. 10-11, Table 4] | 卡方检验选定 | 例如D₁y1-3 Set1: μ=-0.41, σ=0.61 |
| 方位校正采用等面积投影和N′α = Nα/sinα | [Nie 2020, pp. 5-6, 11-13] | 与揭露面夹角影响采集概率 | 校正后小夹角区间频率增加 |
| 密度试错法满足N′=(A′/A)·N | [Nie 2020, pp. 6-8] | 虚拟切割平面与揭露面同方位 | 表5给出各层裂隙最终密度n |

## Limitations

- 该方法严格要求大采样窗口且裂隙两端可见，不适用于小窗口或测线法采集的数据。
- 忽略了迹长<0.5 m（ch<0.25 m）的小裂隙，虽经论证影响小，但仍可能遗漏细小裂隙的结构效应。
- 裂隙形状假设为理想圆盘，实际可能为多边形或不规则面。
- 裂隙中心假设为泊松分布（随机均匀分布），未考虑成簇等非均匀空间分布。
- 在D₁n和D₁y1-1地层中，因软层间距小，未进行网络建模，假设裂隙贯通可能偏于保守。
- 概率密度曲线与直方图顶部不完全吻合，可能因现场样本量有限或真实分布过于复杂。

## Assumptions / Conditions

- 每条裂隙在三维空间中视为圆形薄盘（基于Kulatilake and Wu, 1986）。
- 研究窗口大，采集的裂隙两端均可见，无删截偏差。
- u/r ~ U(0,1)，即裂隙盘中心相对迹线位置均匀随机。
- 推导r²时假定ch²与r²相互独立（大样本量下相关性可忽略）。
- 仅考虑ch ≥ 0.25 m的裂隙，截断影响可忽略。
- D₁y1-2和D₁y1-3软层间距较大，裂隙被假定为非贯通，建模时不考虑软层截断。
- 方位校正时，各角度区间内以平均夹角α代替实际变化，且裂隙密度均匀。

## Key Variables / Parameters

- A (m²): 现场裂隙采集面积
- A′ (m²): 三维网络与虚拟面交切面积
- α (°): 裂隙盘与揭露面平均夹角
- ch (m): 半迹长
- E(ch²), D(ch²): 半迹长平方的均值与方差
- r (m): 揭露面裂隙盘半径
- r′ (m): 三维空间裂隙盘半径
- θ (°): 裂隙盘与揭露面夹角
- f: 裂隙可采集概率，f=2r sinθ/L
- L (m): 三维空间高度
- n: 三维网络裂隙总数（密度）
- N, N′: 现场采集裂隙数、虚拟迹线数
- P20 (m⁻²): 单位面积迹线条数
- P21 (m/m²): 单位面积迹线总长
- X: r等分区间数（文中取100）
- 分布参数：μ, σ (对数正态); k, γ (Gamma); λ (负指数)

## Reusable Claims

- 大采样窗口下，裂隙圆盘半径平方的均值 E(r²) = 1.5 E(ch²)。[Nie 2020, pp. 3-4]
- 通过比较模拟ch与现场ch的卡方检验可确定r²的最优分布类型。[Nie 2020, pp. 4-5]
- 三维空间中裂隙半径分布r′需利用采集概率 f=2r sinθ/L 从揭露面半径r校准得到。[Nie 2020, pp. 5-6]
- 裂隙方位频率校正原则：小夹角区间在三维模型中的频率应高于现场，大夹角区间应降低。[Nie 2020, pp. 5-6, Eqs.6-8]
- 裂隙密度通过试错法确定：虚拟迹线数 N′ = (A′/A)·N 时的n即为所求密度。[Nie 2020, pp. 6-8]
- 忽略ch<0.25 m的短裂隙，对E(ch²)和D(ch²)的相对影响可控制在10%以内，工程上可接受。[Nie 2020, pp. 15-16]

## Candidate Concepts

- [[大采样窗口]]
- [[三维裂隙网络建模]]
- [[裂隙圆盘直径]]
- [[迹长数据]]
- [[采样偏差校正]]
- [[卡方检验]]
- [[蒙特卡洛模拟]]
- [[裂隙密度]]
- [[裂隙方位校正]]
- [[泊松分布模型]]

## Candidate Methods

- [[随机数生成]]
- [[试错法]]
- [[等面积施密特投影方位校正]]
- [[虚拟揭露面切割验证]]
- [[对数正态分布拟合]]
- [[Gamma分布拟合]]
- [[卡方检验分布选择]]
- [[蒙特卡洛网络合成]]

## Connections To Other Work

- 裂隙圆盘假设可追溯到 Kulatilake and Wu (1986)。
- 迹长与直径关系的立体学基础见 Warburton (1980)，Zhang and Einstein (2000) 等。
- 裂隙分组方法采用 Shanley and Mahtab (1976)。
- 采样偏差校正沿袭 Terzaghi (1965)、Priest (1985) 的思路。
- 三维裂隙网络在 Cheng et al. (2004)、Vazaios et al. (2017) 等研究中已应用于实际工程。
- 与传统小窗口数据方法（如 Han et al. 2016）相比，本方法利用大窗口数据避免了迹长校正等复杂操作。

## Open Questions

- 当现场迹长分布复杂时，理想化概率密度曲线与直方图顶部的不完全吻合如何进一步改善直径估计？
- 如何以恰当方式将ch<0.25 m的大量小裂隙纳入模型而不使建模过程过度复杂？
- 本方法在非层状岩体或构造强烈区（如断层密集带）的适用性？
- 裂隙圆盘假设对非等轴状裂隙的偏差影响有多大？
- 三维裂隙网络的空间相关性（如成簇）如何影响后续的力学分析？

## Source Coverage

所有非空索引片段均被处理。共索引文本13块，总字符数63131，编译后使用62548字符，覆盖率（按块）1.0，（按字符）0.9908。本页面完全依据提供的证据片段编纂，未引入片段外内容。
