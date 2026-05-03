---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-ye-experimental-study-of-real-time-temperature-dependent-nonlinear-deformation-of-sandstone"
title: "Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone."
status: "draft"
source_pdf: "data/papers/2023 - Experimental study of real-time temperature-dependent nonlinear deformation of sandstone.pdf"
collections:
  - "zotero new"
citation: "Ye, Zuyang, and Jianhang Yang. \"Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone.\" *Fuel*, vol. 354, 2023, article 129308. doi:10.1016/j.fuel.2023.129308. Accessed 2026."
indexed_texts: "13"
indexed_chars: "64403"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "60525"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.939785"
coverage_status: "full-index"
source_signature: "b66397b0b4efa0404f51e527b17215100e05aa18"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:38:06"
---

# Experimental Study of Real-Time Temperature-Dependent Nonlinear Deformation of Sandstone.

## One-line Summary

利用实时中温（25–200 ℃）单轴压缩实验与两段胡克模型（TPHM），揭示砂岩非线性变形存在125 ℃阈值温度：低于阈值热弱化使软部比例增大、硬部弹性模量降低，高于阈值热强化使软部缩小、硬部模量回升，软部弹性模量全程下降。

## Research Question

在实时中温（25–200 ℃）条件下，砂岩的非线性弹性变形行为如何受温度影响？特别地，两段胡克模型所定义的软部和硬部对温度的响应有何差异，以及是否存在临界温度导致热弱化向热强化的转变？[Ye 2023, pp. 2-3]

## Study Area / Data

- **试样来源**：中国临沂市砂岩（Linyi City sandstone）[Ye 2023, pp. 2]
- **试样规格**：圆柱形，直径50 mm，长100 mm；单轴抗压强度约45–49 MPa；密度平均值2.34 g/cm³ [Ye 2023, pp. 2-3]
- **数量与分组**：共40个试样，分8个温度组（25、50、75、100、125、150、175、200 ℃），每组5个 [Ye 2023, pp. 2-3]
- **预处理**：105 ℃干燥24 h后自然冷却，记录质量与尺寸 [Ye 2023, pp. 2]
- **数据**：实时单轴压缩应力–应变曲线（加载至60 kN终止），总计40组曲线的拟合参数及统计值 [Ye 2023, pp. 3-5]

## Methods

- **实验系统**：高低温试验箱（−30 ℃∼205 ℃，控温精度0.01 ℃）与微机控制岩石直剪仪（最大载荷300 kN，位移测量精度0.001）联用 [Ye 2023, pp. 2-3]
- **加热制度**：以3 ℃/min升温至目标温度后恒温2 h；实时温度由用户界面调控 [Ye 2023, pp. 2-3]
- **加载制度**：先以0.5 kN/s预加载至1 kN，清零位移后以1.5 kN/s轴向力控制加载至60 kN（约30 MPa）结束 [Ye 2023, pp. 2-3]
- **TPHM模型拟合**：利用高应力段直线斜率确定硬部弹性模量E_e和软部比例γ_t；通过直线与应变轴截距获取γ_t/3；再利用低应力点估计软部弹性模量E_t，以相关系数R²优选 [Ye 2023, pp. 4-5]
- **统计分析**：对每组参数计算平均值、标准差及95%置信区间（Student’s t分布，n<30时t=2.7764；同时给出切比雪夫不等式置信区间以包含所有数据点）[Ye 2023, pp. 5-7]

## Key Findings

1. **应力–应变非线性**：低应力区应变随应力非线性增长（微裂纹闭合主导），高应力区呈近似直线（硬部弹性主导）；同一温度下曲线趋势相似但个体存在离散 [Ye 2023, pp. 4-5]
2. **温度阈值125 ℃**：  
   - 25→125 ℃：曲线整体右移，压密阶段占比增大；软部比例γ_t从0.019060增至0.033233（+74.36%），硬部弹性模量E_e从4632 MPa降至4147 MPa（−10.47%）；热弱化由微裂纹生成与贯通驱动 [Ye 2023, pp. 8-9]  
   - 125→200 ℃：曲线逐渐平直，压密阶段几乎消失；γ_t降至0.006003（比室温低68.50%），E_e回升至5103 MPa（比室温高10.70%）；热强化源于硬部矿物颗粒热膨胀使结构更致密，压缩了软部空间 [Ye 2023, pp. 9-10]
3. **软部弹性模量E_t持续下降**：从室温5.329 MPa线性降至200 ℃的1.232 MPa（降幅76.88%），反映软部中杂质颗粒随温度升高更松散、易变形 [Ye 2023, pp. 10]
4. **经验关系**：归一化γ_t、E_e与温度分两段（≤125 ℃和≥125 ℃）分别拟合为指数或线性关系；E_t-nor在整个温区线性下降 [Ye 2023, pp. 10]
5. **影响因素排除**：预干燥去除了自由水影响，结合水未考虑（需>200 ℃蒸发）；热分解质量损失最大仅0.2581%，影响可忽略；γ_t比总孔隙度更能反映力学性质变化 [Ye 2023, pp. 7-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 40组应力–应变曲线与TPHM拟合良好，R²多≥0.99 | Fig.3(a)-(h), Table 2 [Ye 2023, pp. 5-6, 8-9] | 25–200 ℃, 0–30 MPa轴向应力 | 非线性压密阶段与线性弹性阶段区分清晰 |
| γ_t、E_e、E_t平均值随温度变化：γ_t在125 ℃最大，E_e在125 ℃最小，E_t全程下降 | Fig.5(a)-(c), Fig.7 [Ye 2023, pp. 7-10] | 5样本/温度，误差带显示离散 | 125 ℃为阈值，热弱化与热强化交替 |
| 质量损失率随温度升高但最大0.2581%，热分解可忽略 | Table 3, Fig.6 [Ye 2023, pp. 7-10] | 实时加热后称重 | 排除热分解对力学参数的主要干扰 |
| 其他研究者（Rathnaweera, Zha, Shao, Zhang等）的砂岩实时加热数据经TPHM拟合亦呈现类似γ_t、E_e、E_t趋势，阈值温度在100 ℃或200 ℃附近 | Table 4, Fig.8 [Ye 2023, pp. 10-12] | 不同砂岩类型，温度范围25–800 ℃ | 证实软硬部差异化响应的普遍性 |
| 归一化参数与温度的分段拟合方程：γ_t-nor=0.009759e^{0.034951T}+0.98, E_e-nor=−0.0012T+1.0243 (25–125 ℃)；γ_t-nor=33.036721e^{-0.023409T}−0.02037, E_e-nor=0.0033T+0.4618 (125–200 ℃)；E_t-nor=−0.0038T+1.1595 (25–200 ℃) | Eq.(12)-(14), Fig.7 [Ye 2023, pp. 10] | 室温归一化 | 可用于预测同类砂岩的实时温度非线性变形 |
| 软部比例γ_t与最大闭合应变概念（CCS）数值等效，比总孔隙度更准确表征缺陷结构对变形抗力的影响 | Fig.4(b)及说明 [Ye 2023, pp. 5-6] | TPHM原理 | γ_t增大对应压密阶段延长及抗变形能力下降 |

## Limitations

- 微尺度机制尚未探明：软部和硬部演化所对应的裂纹扩展和矿物颗粒接触变化需微观实时观测验证 [Ye 2023, pp. 12]
- 孔隙度无法在实时温度下测量，故未直接对比γ_t与孔隙度的动态关系；现有结论基于力学反演 [Ye 2023, pp. 7-8]
- 结合水的影响未考虑，因其蒸发需200 ℃以上，本研究温区上限200 ℃ [Ye 2023, pp. 7]
- 试样仅一种砂岩，地区单一（临沂），结论外推至其他岩类需谨慎；统计显示个体离散性，依靠均值分析 [Ye 2023, pp. 5-7]
- 温度范围限于25–200 ℃，超出200 ℃的行为（如热开裂加剧）仅作预测，未实验验证 [Ye 2023, pp. 12]

## Assumptions / Conditions

- 岩石可划分为软部（含微裂纹、微孔隙，服从真应变胡克定律）和硬部（含一般孔隙和基质，服从工程应变胡克定律）[Ye 2023, pp. 3-4]
- 水分影响已通过预干燥消除，自由水蒸发不影响结果；热分解在中温下可忽略 [Ye 2023, pp. 7-8]
- 矿物颗粒热膨胀不均匀，硬部（如石英颗粒紧密接触）与软部（含杂质颗粒）物理性质差异导致热响应不同 [Ye 2023, pp. 8]
- 热弱化主要由微裂纹生成与贯通引起，热强化由硬部热膨胀压缩软部空间所致 [Ye 2023, pp. 8-10]
- 单轴条件下忽略围压，假设侧向应力为零，TPHM简化为式(7) [Ye 2023, pp. 4]

## Key Variables / Parameters

- **γ_t**：软部体积比（V_{0,t}/V_0），表征微裂纹、微孔隙占比，与应力–应变压密幅度直接相关
- **E_e**：硬部弹性模量（MPa），主导线性弹性段斜率
- **E_t**：软部弹性模量（MPa），控制低应力非线性段的曲率
- **T**：实时温度（ ℃），25 ℃（室温）至200 ℃
- **σ_n, ε_n**：轴向应力（MPa）和轴向应变，由载荷和位移换算

## Reusable Claims

- 在25–200 ℃实时加热条件下，砂岩存在明显的非线性弹性变形，可用两段胡克模型（TPHM）精确描述（R²>0.99）[Ye 2023, pp. 4-5, 8-9]。
- 实时温度影响下，砂岩出现125 ℃的阈值温度：低于此温度表现为热弱化（γ_t升高、E_e下降），高于此温度表现为热强化（γ_t降低、E_e升高）[Ye 2023, pp. 9-10]。
- 软部弹性模量E_t随温度持续单调下降，不受阈值温度反转影响，表明软部中杂质颗粒的热膨胀效应与硬部不一致 [Ye 2023, pp. 10]。
- 软部比例γ_t作为裂纹闭合应变（CCS）的等效指标，比总孔隙度更灵敏地反映力学性能受温度诱导的微结构损伤 [Ye 2023, pp. 5-6, 8]。
- 提出的分段归一化经验关系（式12-14）可用于预测同类砂岩在实时中温条件下的非线性应力–应变行为，为地热工程安全评估提供依据 [Ye 2023, pp. 10]。
- 实时加热条件下的热强化现象比热处理（加热后冷却再加载）更显著，不可忽视 [Ye 2023, pp. 2]。

## Candidate Concepts

- [[Two-part Hooke's model (TPHM)]]
- [[非线性变形]]（Nonlinear deformation）
- [[热弱化]]（Thermal weakening）
- [[热强化]]（Thermal strengthening）
- [[阈值温度]]（Threshold temperature）
- [[软部]]（Soft part）与[[硬部]]（Hard part）
- [[实时加热]]（Real-time heating）
- [[中温]]（Moderate temperature）
- [[压密阶段]]（Compaction stage）
- [[微裂纹]]（Microcracks）
- [[热膨胀]]（Thermal expansion）
- [[裂纹闭合应变（CCS）]]
- [[弹性模量]]（Elastic modulus）
- [[软部比例（γ_t）]]

## Candidate Methods

- [[实时单轴压缩试验配合高低温试验箱]]（Real-time uniaxial compression with temperature-controlled chamber）
- [[TPHM参数确定法]]（高应力段直线拟合法与低应力点E_t优选）
- [[基于Student’s t分布的统计误差分析]]（均值、标准差、95%置信区间计算）
- [[切比雪夫不等式置信区间]]（Tchebyshev’s inequality for outlier inclusion）
- [[归一化参数分段拟合]]（Normalized parameter piecewise fitting）

## Connections To Other Work

- **与同类实时加热砂岩试验对比**：Rathnaweera et al. [36]、Zha et al. [37]、Shao et al. [38]、Zhang et al. [39] 的砂岩实时加热数据经TPHM重分析后，均呈现出类似的γ_t、E_e随温度先降后升（或趋势转折）的规律，阈值温度分别为200 ℃、100 ℃、低于100 ℃以及100 ℃，说明软硬部差异化响应是砂岩的普遍特征 [Ye 2023, pp. 10-12]。
- **孔隙度分类思想**：Shapiro 和 Kaselow [52] 将总孔隙度分为刚性孔与柔性孔（裂隙），柔性孔对压缩性影响更大，与TPHM软部概念一致 [Ye 2023, pp. 8]。
- **热强化的微观解释**：Aversa 和 Evangelista [60] 认为岩石基质受热膨胀导致颗粒压实，Wong et al. [58] 在大理岩中发现25–200 ℃存在热弱化和热强化的竞争，本研究在砂岩中同样证实此现象并与软硬部响应关联 [Ye 2023, pp. 8-10]。
- **孔隙在水-力-热耦合中的作用**：Li et al. [55] 发现25–200 ℃时砂岩微孔（10–300 nm）增加最大，Jin et al. [51] 也指出小孔隙在该温区增量最大，与本研究中γ_t的变化趋势相容，但γ_t更直接关联力学响应 [Ye 2023, pp. 8]。
- **数据可靠性设计依据**：参考 Gill et al. [40] 的小样本理论和ISRM建议，每组5个试样合理；实验设计借鉴了Ranjith et al. [10]、Yang et al. [28] 等的加热和加载参数 [Ye 2023, pp. 2-3]。

## Open Questions

- 软部比例下降和硬部弹性模量回升的微观过程（裂纹愈合？颗粒重排？）尚缺乏实时显微镜或CT观察证据 [Ye 2023, pp. 12]。
- 200 ℃以上至300 ℃区间是否会出现第二次热弱化（新裂纹大量生成）？文中仅预测而未实验验证 [Ye 2023, pp. 12]。
- 结合水在中高温下的逸出对阈值温度和软硬部参数的影响未量化 [Ye 2023, pp. 7]。
- 不同围压条件下TPHM参数的温度响应规律是否与单轴一致？多轴条件下的普适关系需进一步研究。
- 其他沉积岩（如页岩、石灰岩）是否具有相似的阈值温度？尚需更多岩类实验数据。
- 如何将本实验的宏观TPHM参数与数值模拟中的微观损伤模型联系起来，实现多尺度预测？

## Source Coverage

本文档使用了全部13个已索引的非空源块，覆盖了[Ye 2023, pp. 1-13]的完整长文实验。源块字符总规模64403，编译后使用60525字符，以块计覆盖率为1.0，以字符计覆盖率约0.9398，索引完整性标记为full-index，编译策略为单次直通（single-pass-markdown）。所有事实性陈述均来自这些片段，无额外虚构。
