---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i"
title: "A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale."
status: "draft"
source_pdf: "data/papers/2017 - A new global database to improve predictions of permeability distribution in crystalline rocks at site scale.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Achtziger-Zupan, P., et al. “A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale.” *Journal of Geophysical Research: Solid Earth*, 2017, doi:10.1002/2017JB014106. Accessed 2026."
indexed_texts: "27"
indexed_chars: "133770"
nonempty_source_blocks: "27"
compiled_source_blocks: "27"
compiled_source_chars: "134472"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005248"
coverage_status: "full-index"
source_signature: "7d291397d69c701ee122c6e6f67d871cda4ce42c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:31:57"
---

# A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale.

## One-line Summary
建立了一个包含约29,000个现场渗透率数据的全球结晶岩渗透率数据库，揭示了渗透率随深度、地震构造活动和长期构造地质历史变化的定量关系，提出了预测场地尺度渗透率分布的新回归模型。

## Research Question
如何更准确地预测场地尺度结晶岩中渗透率的空间分布？技术因素（测量方法、尺度效应、优先采样、水力各向异性）和地质因素（岩性、当前应力状态、地震构造活动、长期构造地质历史）如何影响渗透率随深度的变化？能否建立一个基于全球数据的、可考虑关键地质因素的渗透率预测方法？

## Study Area / Data
- 数据来自全球30个国家的221篇文献和报告，共约29,000个现场渗透率测量值（最终合并后使用19,062个），深度范围为0–2000米地下（mbgs）[Achtziger 2017, pp. 1-1] [Achtziger 2017, pp. 1-3] [Achtziger 2017, pp. 14-15]。
- 主要数据来源：欧洲（83%）、北美（7%）、日本、韩国、中国（共7%），其余地区（3%）[Achtziger 2017, pp. 3-4]。
- 测量方法包括：裸孔测试、单/双栓塞测试、压水/吕荣测试、钻杆测试、差分流测井、隧道离散入流测量、地震活动反演、地下水模型校准等，最终使用数据限制为每种方法至少100次观测，且剔除超过100 m测量段和低于测量极限的数值[Achtziger 2017, pp. 3-4] [Achtziger 2017, pp. 4-5]。
- 同时汇编了32组跨孔试验得出的单位出水量/储水系数数据，深度可达1700 mbgs [Achtziger 2017, pp. 4-5]。

## Methods
- **数据均一化**：将所有渗透系数、导水系数转换为SI单位的渗透率k (m²)，假设水静压饱和条件，考虑温度、总溶解固体（TDS）带来的误差（浅层可忽略，深层<25%）。温度由现场或标准地温梯度3 K/km推算[Achtziger 2017, pp. 3-4]。
- **计算测试体积**：对恒定水和定流量试验，采用Jacob和Lohman（1952）公式估算影响半径；对微水试验采用Cooper等（1967）公式；对脉冲试验采用Bredehoeft和Papadopulos（1980）公式，进而按圆柱体计算测试岩石体积[Achtziger 2017, pp. 4-5]。
- **子数据集划分**：按深度区间（50 m、100 m、250 m等）、测量方法、测段长度对数级、测试体积对数级、岩性（11类）、地质省（6类）、峰值地面加速度（PGA，4类）、局部应力体制（5类）分类[Achtziger 2017, pp. 7-8]。
- **统计与聚类分析**：对每个子数据集计算对数平均、方差、偏度；使用k-means聚类（基于对数均值、方差、偏度），用轮廓图确定4个聚类；对全数据集及子数据集进行对数-对数线性回归 log(k) = A × log(z) + B，计算R²和RMSE[Achtziger 2017, pp. 7-8] [Achtziger 2017, pp. 8-9]。
- **检验与预测算法**：采用留一交叉验证检验回归模型，并用奥地利和圭亚那两个独立数据集进行预测验证[Achtziger 2017, pp. 21-22] [Achtziger 2017, pp. 22-23]。

## Key Findings
1. **全局渗透率-深度关系**：全数据集对数-对数回归为 log(k) = -1.5 × log(z) - 16.3，其中k为渗透率(m²)，z为深度(km)。在2000 mbgs深度范围内渗透率下降约3.5个数量级。预测能力R²=0.2，RMSE约1.5个数量级。[Achtziger 2017, pp. 14-15]
2. **方差与偏度**：渗透率对数方差在不同深度大致恒定约2个数量级（90%置信区间约5个数量级），偏度随深度持续增加（不显著）。[Achtziger 2017, pp. 14-15] [Achtziger 2017, pp. 15-16]
3. **储水特性**：单位出水量/储水系数随深度变化的回归为 log(Sy/S) = -1.0 × log(z) - 6.0，与渗透率趋势相似。在约600 mbgs以下仅观测到承压裂隙和基质流，而浅部200 mbgs内存在非承压-承压混合。[Achtziger 2017, pp. 4-5] [Achtziger 2017, pp. 19-20]
4. **技术因素影响**：
   - 不同测量方法获得的渗透率范围有差异，但多栓塞测试覆盖了其他方法的范围。差分流测井的斜率最高（-0.5），裸孔测试、吕荣测试、单栓塞测试斜率依次变陡（-1.36到-1.31）。[Achtziger 2017, pp. 10-11] [Achtziger 2017, pp. 15-16]
   - 优先采样与水力各向异性影响可忽略：水平、倾斜、垂直三个方向的回归斜率和截距非常接近。[Achtziger 2017, pp. 11-12] [Achtziger 2017, pp. 15-16]
   - 尺度效应明显：测试段长度增加，斜率变陡（-0.8到-2.08），截距降低；计算测试体积每变化一个数量级，渗透率变化约0.6个数量级。[Achtziger 2017, pp. 15-16] [Achtziger 2017, pp. 19-20]
5. **地质因素主控**：地质省（长期构造历史）和地震构造活动（PGA）是控制渗透率分布的最主要地质因素。岩性影响较小。
   - PGA：高PGA区斜率最高（-1.23）、截距最高（-15.28），随PGA降低斜率和截距均下降；极低PGA区斜率-1.48、截距-16.26。[Achtziger 2017, pp. 17-18]
   - 地质省：俯冲带活动造山带渗透率最高（截距-15.60），被动古造山带最低（截距-17.07，斜率-2.34），稳定地盾居于中间。[Achtziger 2017, pp. 17-18]
   - 岩性：大理岩斜率最陡（-2.41）、截距最低（-16.78）；接触变质岩斜率也较陡；石英岩截距较高（-15.58）。花岗岩等酸性侵入岩斜率-1.43、截距-16.17。[Achtziger 2017, pp. 13-14] [Achtziger 2017, pp. 16-17]
6. **三层水力结构模型**：k-means聚类揭示：近地表（~100 m）高渗透率（~10⁻¹⁴ m²）、高方差（~2个数量级）；中层（100–500 m）渗透率降至10⁻¹⁶–10⁻¹⁵ m²，方差2–4个数量级；深层（>500 m）渗透率进一步降至3×10⁻¹⁷ m²，方差约1.7个数量级。[Achtziger 2017, pp. 15-16]
7. **预测模型验证**：基于地质因素回归系数的平均预测在两个独立场地（奥地利Klasgarten滑坡、圭亚那Aurora金矿）均正确预测了深度趋势，RMSE略低估0.2个数量级。[Achtziger 2017, pp. 21-23]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 全数据集回归：log(k) = -1.5 × log(z) - 16.3，R²=0.2，RMSE=1.54 | [Achtziger 2017, pp. 14-15], Table 3 | 深度0–2000 mbgs，剔除异常数据后的19,062个值 | 平均渗透率在1000 m深度约为-16.3 log(m²) |
| 单位出水量/储水系数随深度：log(Sy/S) = -1.0 × log(z) - 6.0 | [Achtziger 2017, pp. 4-5] | 32个独立数据点 | 在1000 m深度典型值为10⁻⁶ m⁻¹ |
| 测试体积与渗透率关系：每增加1个数量级测试体积，渗透率变化约0.6个数量级 | [Achtziger 2017, pp. 19-20] | 基于钻孔和隧道测试体积分类 | 与Illman和Tartakovsky（2006）的0.55因子接近 |
| 多栓塞测试回归：斜率-1.59，截距-16.37，RMSE=1.71 | Table 3 [Achtziger 2017, pp. 8-9] | 11,182个测量值，深度至1973 mbgs | 使用最广泛的测试方法 |
| 高PGA区回归：斜率-1.23，截距-15.28，RMSE=1.78 | Table 3 [Achtziger 2017, pp. 9-10] | 531个测量值，PGA>2.4 m/s² | 主要为板块边界活跃带 |
| 被动古造山带回归：斜率-2.34，截距-17.07，RMSE=1.35 | Table 3 [Achtziger 2017, pp. 9-10] | 3072个测量值 | 代表长期稳定但曾有构造活动的地区 |
| 接触变质岩回归：斜率-2.22，截距-16.34，RMSE=1.70 | Table 3 [Achtziger 2017, pp. 8-9] | 1433个测量值 | 高温低压变质导致高脆性 |
| 留一交叉验证RMSE与模型RMSE吻合 | [Achtziger 2017, pp. 22-23] | 全数据集 | 表明回归方程具有预测能力 |
| 预测与独立数据对比：奥地利Klasgarten预测 log(k) = -1.4 × log(z) - 16.0，测量值相符 | [Achtziger 2017, pp. 22-23] | 高品位变质岩+石英岩，碰撞造山带，中等PGA | 稳定基岩的渗透率在预测误差带内 |
| 预测与独立数据对比：圭亚那Aurora预测 log(k) = -1.6 × log(z) - 16.3，多数数据符合 | [Achtziger 2017, pp. 22-23] | 绿片岩相变沉积/变火山岩，低PGA地盾 | 浅部预测偏低，可能因当地水文连通性 |

## Limitations
- 数据来源偏重欧洲（83%），北美（7%）和亚洲（7%），其他地区仅3%，可能造成地理偏差 [Achtziger 2017, pp. 3-4]。
- 深层数据（>1000 m）来自少数几个场地（瑞士阿尔卑斯、德国厄尔士山脉），样本代表性有限 [Achtziger 2017, pp. 14-15]。
- 抽水试验时间、影响半径等关键参数常缺失，测试体积仅约半数数据可计算 [Achtziger 2017, pp. 5-7]。
- 由于数据源于多种目的，存在采样偏差（例如废物处置场地偏向低渗介质）[Achtziger 2017, pp. 18-19]。
- 渗透率转换假设了饱和静水压力，忽略了温度、矿化度的空间变化，深层误差可达20–25% [Achtziger 2017, pp. 3-4]。
- 回归模型R²普遍较低（0.01–0.55），单个回归方程的预测能力有限 [Achtziger 2017, pp. 15-16] [Achtziger 2017, pp. 18-19]。
- 地质因素分类较粗，岩性常按整个钻孔/场地归纳，可能掩盖岩性控制作用 [Achtziger 2017, pp. 21-22]。
- 未考虑热-水-力-化学耦合对渗透率的动态影响 [Achtziger 2017, pp. 19-20]。

## Assumptions / Conditions
- 所有测量均假设为饱和、静水压力条件下的达西流 [Achtziger 2017, pp. 3-4]。
- 渗透率与储水系数在计算测试体积时视为不相关 [Achtziger 2017, pp. 19-20]。
- 缺失温度数据采用标准地温梯度3 K/km和地表温度估算 [Achtziger 2017, pp. 3-4]。
- 地质省划分基于USGS（1997）分类并局部修改 [Achtziger 2017, pp. 14-15]。
- 峰值地面加速度（PGA）使用全球地震危险图GSHAP，10%超越概率/50年 [Achtziger 2017, pp. 13-14]。
- 局部应力体制取自世界应力图数据库，水平距离≤10 km、垂直距离≤0.5 km [Achtziger 2017, pp. 13-14]。
- 测量段长度>100 m或低于方法检测限的数据被剔除，可能截断了低渗端 [Achtziger 2017, pp. 3-4] [Achtziger 2017, pp. 18-19]。

## Key Variables / Parameters
- **渗透率k (m²)**：通过公式 k = K·μ/(ρg) 转换自渗透系数K [Achtziger 2017, pp. 3-4]。
- **深度z (km, 正数)**：从地表到测段中点的垂直深度 [Achtziger 2017, pp. 14-15]。
- **回归斜率A**：反映渗透率随深度衰减的陡峭程度，例如-1.53 [Achtziger 2017, pp. 8-9]。
- **回归截距B**：1000 m深度处的对数渗透率，例如-16.26 [Achtziger 2017, pp. 8-9]。
- **RMSE**：预测的标准误差，通常1–2个数量级 [Achtziger 2017, pp. 9-10]。
- **测试岩石体积V (m³)**：由影响半径和测试段长度估计 [Achtziger 2017, pp. 4-5]。
- **单位出水量/储水系数Sy/s (m⁻¹)**：跨孔试验获得的水力参数 [Achtziger 2017, pp. 4-5]。
- **峰值地面加速度PGA**：分四类：极低（0–0.2 m/s²）、低（0.2–0.8）、中等（0.8–2.4）、高（>2.4） [Achtziger 2017, pp. 13-14]。
- **地质省类别**：稳定省、活动碰撞造山带、俯冲相关造山带、被动古造山带、盆地、伸展省（数据不足） [Achtziger 2017, pp. 14-15]。
- **岩性类别**：酸性侵入岩、中性侵入岩、基性/超基性岩、大理岩、石英岩、接触变质岩、中级变质岩、高级变质岩、超高等级变质岩、变侵入岩、变火山岩 [Achtziger 2017, pp. 7-8] [Achtziger 2017, pp. 13-14]。

## Reusable Claims
- 全球结晶岩0–2000 m深度范围内，渗透率对数均值服从 log(k) = -1.5 × log(z) - 16.3，但R²仅0.2，表明深度只能解释一小部分方差；适用于区域性趋势估计，不可用于单点精确预测。[Achtziger 2017, pp. 14-15]
- 在场地尺度，渗透率分布主要受当前地震构造活动（用PGA表征）和长期构造地质历史（用地省表征）控制，其影响超过局部岩性差异；基于多元回归的预测模型可将预测误差控制在1–2个数量级内。[Achtziger 2017, pp. 17-18] [Achtziger 2017, pp. 21-22]
- 水力测试的尺度效应可用测试体积变化解释：测试体积每增加1个数量级，渗透率增加约0.6个数量级。该结论基于钻孔和隧道两类测试的比较，但测试体积计算依赖于渗透率本身，需独立验证。[Achtziger 2017, pp. 19-20]
- 渗透率的方向各向异性在区域尺度上不明显，优先采样对深度-渗透率关系影响可忽略，因此可在预测时忽略测量方向因素。[Achtziger 2017, pp. 15-16]
- 单位出水量/储水系数与渗透率的深度衰减趋势相似，在1000 m深度储水系数约为10⁻⁶ m⁻¹，该值可用于缺乏数据的深部地下水流模型。[Achtziger 2017, pp. 4-5]
- 当已知场地所属地质省和PGA等级时，可利用表3中的对应回归参数（斜率和截距）估算深度-渗透率趋势，误差约为1.5个数量级。[Achtziger 2017, pp. 9-10] [Achtziger 2017, pp. 22-23]

## Candidate Concepts
- [[crystal rock permeability prediction]]
- [[permeability-depth relation]]
- [[scale effect in fractured rock]]
- [[geological province control on permeability]]
- [[seismotectonic activity and permeability]]
- [[hydraulic test volume scaling]]
- [[fracture flow vs matrix flow depth transition]]
- [[global crustal permeability database]]
- [[k-means clustering hydraulic stratification]]
- [[specific storage depth trend]]
- [[preferential sampling bias in hydrogeology]]

## Candidate Methods
- [[global permeability compilation and homogenization]]
- [[log-log regression of permeability vs depth]]
- [[Jacob-Lohman radius of influence estimation]]
- [[Cooper slug test interpretation]]
- [[Bredehoeft-Papadopulos pulse test radius]]
- [[multivariate statistical analysis of permeability factors]]
- [[k-means clustering for permeability-depth distribution]]
- [[leave-one-out cross validation for regression]]
- [[prediction of site-scale permeability using geological factors]]

## Connections To Other Work
- 本研究对比了Stober和Bucher（2007）的渗透率-深度方程，发现本数据的斜率稍缓（-1.5 vs -1.7），截距相近；亦与Manning和Ingebritsen（1999）的标准曲线不同，浅部更陡且截距更低。[Achtziger 2017, pp. 19-20]
- 与Ranjram等人（2015）关于深度、岩性和构造环境的研究一致，认为构造环境对浅层渗透率有控制作用，但在深度>400 m时影响减弱。[Achtziger 2017, pp. 14-15]
- 储水系数与渗透率趋势的平行性呼应了Masset和Loew（2010）的工作，但未给出物理解释。[Achtziger 2017, pp. 19-20]
- 尺度效应结果与Illman和Tartakovsky（2006）在Grimsel试验场获得的0.55指数吻合，验证了跨孔试验推导的规律。[Achtziger 2017, pp. 19-20]
- 地质省和PGA作为控制因素的观点与Faulkner和Armitage（2013）关于构造环境对渗透率发育影响的实验室观测一致。[Achtziger 2017, pp. 13-14]

## Open Questions
- 为何渗透率方差在不同深度保持约2个数量级？这是否意味着脆性断裂带始终存在高渗透率通道？[Achtziger 2017, pp. 14-15] [Achtziger 2017, pp. 19-20]
- 隧道入流测试与钻孔测试在相近测试体积下渗透率系统偏低3–4个数量级的机制尚不清楚，可能与开挖周边应力变化或非达西流有关。[Achtziger 2017, pp. 19-20]
- 岩性在局部场地可显著控制渗透率（如片理、矿物成分影响），但全局尺度被地质省掩盖，如何整合多尺度信息？[Achtziger 2017, pp. 21-22]
- 极低地震活动区（如地盾）的渗透率仍较高，是否与冰后期回弹诱发的非地震断层蠕动有关？[Achtziger 2017, pp. 20-21]
- 深部（>1000 m）渗透率数据稀缺，如何获取更多深层数据以验证趋势？[Achtziger 2017, pp. 14-15]
- 是否可能建立动态的渗透率模型，纳入地震周期、流体矿化沉淀/溶解等时间相关过程？[Achtziger 2017, pp. 20-21]

## Source Coverage
本次编译处理了所有27个非空索引片段，共133,770个字符。编译后获得了27个源块，总字符数为134,472。源块覆盖率为1.0（按块数），字符覆盖率为1.005248。所有索引片段均被纳入本页面，无遗漏。源签名：7d291397d69c701ee122c6e6f67d871cda4ce42c。
