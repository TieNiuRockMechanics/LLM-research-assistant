---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-song-active-crustal-deformation-model-of-the-fen-wei-rift-zone-north-china-integration-of-g"
title: "Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets."
status: "draft"
source_pdf: "data/papers/2022 - Active crustal deformation model of the Fen–Wei rift zone, North China Integration of geologic, geodetic, and stress direction datasets.pdf"
collections:
  - "山西断裂地质构造"
citation: "Song, Shangwu, et al. \"Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets.\" *Frontiers in Earth Science*, vol. 10, 2022, doi:10.3389/feart.2022.964800."
indexed_texts: "16"
indexed_chars: "78787"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "79134"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004404"
coverage_status: "full-index"
source_signature: "808c9d7fdcc593b69574bb8d4cff3c3ade25766e"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:00:15"
---

# Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets.

## One-line Summary
本研究通过联合拟合更新的地质断层滑动速率、大地测量GPS速度场和主压应力方向数据集，利用NeoKinema运动学有限元模型，构建了汾渭裂谷（FWRZ）的长期活动地壳变形模型，揭示了该区低应变背景、有限的秦岭横向挤出和中部山西裂谷的右旋剪切，并识别出大同、韩城和运城盆地的地震空区[Song 2022, pp. 1-2, 16-17]。

## Research Question
- 汾渭裂谷长期断层活动的总体特征是什么？[Song 2022, pp. 3-4]
- 沿东西向秦岭山脉是否存在显著的构造挤出？[Song 2022, pp. 3-4]
- 山西裂谷的剪切和伸展应变如何分布？[Song 2022, pp. 3-4]
- 汾渭裂谷中哪些区域具有强震潜力？[Song 2022, pp. 3-4]

## Study Area / Data
研究区为华北的汾渭裂谷（FWRZ），长约1200公里，由渭河裂谷和山西裂谷组成，位于秦岭与燕山之间[Song 2022, pp. 1-3]。输入数据包括：
- 80条活断层迹线，其中32条具有晚第四纪地质滑动速率及标准差[Song 2022, pp. 5-6]；
- 468站GPS水平速度场（源自Hao et al., 2021），已排除同震和震后影响，并对弹性锁定效应进行负位错校正[Song 2022, pp. 6-7]；
- 541个主压应力方向数据（来自WSM，包括震源机制解和钻孔崩落数据），经插值后用于约束连续体单元的主应变率方向[Song 2022, pp. 7]。

## Methods
采用运动学有限元程序NeoKinema（Bird and Liu, 2007），以加权最小二乘法联合拟合多源约束，目标函数包含三项：GPS速度、沿断层迹线的地质滑动速率、以及连续体单元中的应变率最小化和各向同性约束[Song 2022, pp. 4-5]。模型通过调整三个调谐参数（μ、L0、A0）实现多约束间的优化：首先固定μ=3.2×10⁻¹⁷ s⁻¹，再在参数空间搜索，最终选定L0=1.65×10⁴ m和A0=2.2×10⁹ m²为最优组合[Song 2022, pp. 7-9]。断层滑动速率先验约束中，对缺少资料的断层赋予零目标速率和较大标准差（5 mm/a），以降低权重[Song 2022, pp. 5-6]。

## Key Findings
- 汾渭裂谷多数活动断层预测长期滑动速率小于1 mm/a，反映低应变构造背景[Song 2022, pp. 9, 16]。
- 渭河裂谷正断层滑动速率向东增强：西秦岭北缘断层0.29±0.06 mm/a，东秦岭北缘断层0.61±0.28 mm/a，华山断裂达1.20±0.59 mm/a[Song 2022, pp. 9-10]。
- 秦岭构造挤出有限：铁炉子断层左旋走滑速率仅0.13±0.11 mm/a，从鄂尔多斯地块南部到秦岭的总左旋剪切率约1 mm/a[Song 2022, pp. 9-11, 16]。
- 山西裂谷中部N-S向断层存在~0.5 mm/a的右旋剪切，向南北两端递减；大同和运城盆地跨盆地水平伸展率分别为1.0–1.2 mm/a和~0.8 mm/a，不能完全归因于中部的右旋剪切终端效应[Song 2022, pp. 10-12, 16]。
- 基于SHIFT模型的地震危险性预测显示，大同、韩城和运城盆地存在显著的地震空区（计算地震率高于历史记录，如大同盆地计算3.96/522年、实际2/522年），表明这些地区具有较高的强震潜力[Song 2022, pp. 13-16]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 西秦岭北缘断层正断速率0.29±0.06 mm/a | 模型预测 vs. 地质0.11–0.45 mm/a (Table 2) | μ=3.2e-17, L0=1.65e4 m, A0=2.2e9 m² | 与地质约束一致 |
| 东秦岭北缘断层正断速率0.61±0.28 mm/a | 模型预测 vs. 地质0.5–0.8 mm/a (Table 2) | 同上 | 一致性良好 |
| 铁炉子断层左旋走滑速率0.13±0.11 mm/a | 模型预测 vs. 地质0.5–1.25 mm/a (Fig. 5, Table 2) | 无先验走滑约束 | 明显低于地质估计，可能受GPS误差或定年不确定性影响 |
| 山西裂谷中部右旋剪切速率~0.5 mm/a | 模型预测的霍山断裂0.23±0.12 R, 北西岣山断裂0.43±0.21 R (Table 2) | 无先验走滑约束，仅由GPS和应力方向约束 | 与近期地质研究（Xu et al., 2013）吻合 |
| 大同盆地伸展率1.0–1.2 mm/a | 速度剖面A (Fig. 7) 及参考模型 (Fig. 10A) | 与GPS远场速率一致 | 与Middleton et al. (2017) 地质估计兼容 |
| 运城盆地伸展率~0.8 mm/a | 速度剖面C (Fig. 7) 及参考模型 (Fig. 10E) | 参考模型与GPS远场一致 | |
| 地震空区：大同盆地计算M≥6地震3.96次/522年，实际2次 | SHIFT模型与历史目录 (Fig. 12, Supplementary Table S1) | 阈值M6，目录1500-2022年 | 地震缺失指示较高潜在地震风险 |

## Limitations
- 铁炉子断层的模型走滑速率（0.13±0.11 mm/a）远低于晚第四纪地质估计（0.5–1.25 mm/a），原因可能是GPS观测误差或地质定年不确定性，尚需进一步研究[Song 2022, pp. 9, 16]。
- 对于滑动速率低于1 mm/a的断层，GPS本身难以精确约束，需依赖地质数据补偿[Song 2022, pp. 3, 12]。
- 太原盆地等处仅凭GPS无法识别明显的伸展信号，必须依靠联合反演恢复长期变形场[Song 2022, pp. 12-13]。
- 部分断层（如交城断裂、北西岣山断裂）的模型滑动速率与地质约束存在较大偏差，可能反映地质速率的高估或GPS站点分布的影响[Song 2022, pp. 8-9]。

## Assumptions / Conditions
- 假设长期（10⁴年尺度）地壳变形可由GPS（数十年尺度）速度场近似，且通过弹性锁定校正（锁定深度1–15 km）后可代表稳态变形[Song 2022, pp. 3, 7, 12]。
- 连续体单元内应变率目标值为零，但存在未发现活断层的可能性，因此赋予非零的不确定性μ[Song 2022, pp. 4-5]。
- 连续体单元的主应变率方向应与主应力方向一致，应力方向数据作为松弛约束[Song 2022, pp. 4, 7]。
- 无地质滑动速率资料的断层，先验目标为零，并赋予5 mm/a的大标准差[Song 2022, pp. 5-6]。
- GPS站点距离断层迹线2 km以内且滑动速率>1 mm/a的站点在预处理中被剔除[Song 2022, pp. 6-7]。

## Key Variables / Parameters
- μ (应变率不确定性) = 3.2×10⁻¹⁷ s⁻¹（固定值）[Song 2022, pp. 7-9]
- L0 (参考长度) = 1.65×10⁴ m[Song 2022, pp. 7-9]
- A0 (参考面积) = 2.2×10⁹ m²[Song 2022, pp. 7-9]
- 断层地质滑动速率及其标准差（Table 1, 32条断层）[Song 2022, pp. 5-6]
- 地震危险性预测参数：震源层厚度 (cz)、角震级 (m_c)、渐近谱斜率 (β)[Song 2022, pp. 13-15]

## Reusable Claims
- 汾渭裂谷是一个典型的低应变构造背景，大多数活断层的长期滑动速率小于1 mm/a[Song 2022, pp. 9, 16]。
- 渭河裂谷的正断层活动自西向东增强，南、北缘断层滑动速率均呈现东高西低的趋势[Song 2022, pp. 9-10, 16]。
- 沿东西向秦岭山脉的构造挤出非常有限，鄂尔多斯地块南部至秦岭的总左旋剪切率仅约1 mm/a[Song 2022, pp. 11, 16-17]。
- 山西裂谷中部存在明显的右旋剪切（~0.5 mm/a），向南北两端递减，伴随着南北端盆地的强烈地壳伸展（1.1–1.2 mm/a），且该伸展不能仅由中部剪切终端效应解释[Song 2022, pp. 10-12, 16-17]。
- 大同、韩城和运城盆地为地震空区，预测的地震活动率高于历史记录，具有较高的强震危险性[Song 2022, pp. 15-16]。
- 在低应变区，联合反演地质和大地测量数据可有效恢复长期地壳变形场，弥补各自方法局限[Song 2022, pp. 3, 12-13]。

## Candidate Concepts
- [[Fen-Wei rift zone]]
- [[low-strain kinematic setting]]
- [[transtensional tectonics]]
- [[active crustal deformation model]]
- [[NeoKinema]]
- [[SHIFT model]]
- [[fault slip rate]]
- [[strain partitioning]]
- [[seismicity forecast]]
- [[seismic gap]]
- [[Ordos block]]
- [[Qinling Mountains]]
- [[Shanxi rift]]
- [[Weihe rift]]
- [[extrusion tectonics]]

## Candidate Methods
- [[joint inversion of geodetic and geologic data]]
- [[kinematic finite-element modeling]]
- [[multi-parameter grid search optimization]]
- [[integration of stress direction constraints]]
- [[elastic dislocation correction for interseismic locking]]
- [[strain-rate field estimation from continuum elements]]

## Connections To Other Work
- 直接引用并拟合了前人的活断层数据库（Deng et al., 2002; Xu et al., 2016）以及大量地质滑动速率研究（Table 1）[Song 2022, pp. 2, 5-6]。
- GPS速度场来自Hao et al. (2021)，并经过同震/震后校正和弹性锁定校正，与长期地壳变形建立联系[Song 2022, pp. 6-7]。
- 主压应力方向数据取自世界应力图项目（WSM 2016）（Heidbach et al., 2009）[Song 2022, pp. 7]。
- 参考了活动块体理论（Deng et al., 2003; Zhang et al., 2003）和“挤出构造”假说（Tapponnier et al., 2001），并指出秦岭挤出有限[Song 2022, pp. 1-2, 16-17]。
- 山西裂谷的伸展率结果与Middleton et al. (2017)的地质估计相容，太原盆地仪表现代GPS难以识别伸展，但地质模型可互补[Song 2022, pp. 3, 12-13]。
- 地震危险性评估使用SHIFT模型（Bird and Kagan, 2004），并与历史地震目录（1500-2022年，M≥6）对比[Song 2022, pp. 13-16]。

## Open Questions
- 铁炉子断层模型左旋滑动速率（~0.13 mm/a）与晚第四纪地质估计（0.5–1.25 mm/a）之间显著差异的原因，是由于走滑运动的时变性还是观测/定年误差？[Song 2022, pp. 9, 16-17]
- 山西裂谷中部有限的右旋剪切（~0.5 mm/a）如何驱动南北端盆地高达1.1–1.2 mm/a的伸展？深部物质垂向交换或太平洋俯冲远场效应是否叠加？[Song 2022, pp. 16-17]
- 交城断裂、北西岣山断裂等与地质约束不符的模型结果，是否表明地质滑动速率存在高估？[Song 2022, pp. 8-9]
- 太原盆地现代GPS观测中伸展信号不明显，其长期变形特征和地震危险性如何准确评估？[Song 2022, pp. 12-13]

## Source Coverage
本页面处理了全部16个非空索引片段，所有片段均已编译。编译源块数为16，源字符数为78,134；覆盖率按块数为1.0，按字符数为1.004404（因少量格式字符使编译后字符数略高于源索引字符数）。片段的原始源签名为808c9d7fdcc593b69574bb8d4cff3c3ade25766e。未遗漏任何索引文本。
