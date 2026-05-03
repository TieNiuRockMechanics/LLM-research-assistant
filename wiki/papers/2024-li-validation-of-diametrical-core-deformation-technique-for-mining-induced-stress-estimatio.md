---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-li-validation-of-diametrical-core-deformation-technique-for-mining-induced-stress-estimatio"
title: "Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study."
status: "draft"
source_pdf: "data/papers/2024 - Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation A Case Study.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, et al. “Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study.” *Rock Mechanics and Rock Engineering*, vol. 57, 2024, pp. 7643-52, doi:10.1007/s00603-024-03866-x."
indexed_texts: "7"
indexed_chars: "32195"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31909"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991117"
coverage_status: "full-index"
source_signature: "4aefeda1288c3f94bfbc172440e6c8e85d344767"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:03:58"
---

# Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study.

## One-line Summary

通过对加拿大某地下矿山底板岩芯实施直径变形技术（DCDT）并与经校准的FLAC3D全矿山数值模型对比，验证了DCDT在估算采矿诱发应力量级和方向方面的现场适用性，结果显示二者吻合良好。

## Research Question

在采矿工程中，能否将实验室已验证的直径变形技术（DCDT）成功地应用于野外条件，以经济快速地估算采动应力，并通过与独立的、基于地质力学数据库和历史采矿活动的数值模型进行对比，证实其作为实用地压管理工具的可靠性。

## Study Area / Data

案例矿山为加拿大安大略省的Young‑Davidson（YD）金矿，矿体处于Kirkland‑Larder Lake金矿带，受区域Larder Lake‑Cadillac断裂带切割[Li 2024, pp. 2-3]。测试位置在9130中段（埋深1170 m）的一条脉外运输巷底板，使用NQ金刚石钻头钻取两个垂直岩芯，取样深度分别为底板以下3 m和1.5 m[Li 2024, pp. 5-7]。地质力学参数来自Golder Associates公司2013年完成的岩体表征，岩石类型包括Timiskaming沉积岩（TSED）、正长岩（SYN）和镁铁质火山岩（MAFIC），因互层高度发育而平均为“YDave”材料，其单轴抗压强度132.1 MPa、弹性模量69.4 GPa、泊松比0.26[Li 2024, pp. 2-3]。原位应力数据由Geomechanics Research Centre于2012年采用套芯应变解除法在四个中段取得，并由McKinnon and Labrie (2006)的区域应力数据库补充，主应力方向调整为正交，回归得到的应力方程（式1）用于模型初始化[Li 2024, pp. 3-5]。

## Methods

DCDT操作：在实验室用高精度激光测微仪测量岩芯转动时的直径变化，拟合正弦曲线获得最大和最小直径（d_max, d_min），据此确定平面内主应力方向与差应力；再利用Li and Mitri (2023)的分析模型，假定钻孔轴向应力近似为零，推求底板主应力量值[Li 2024, pp. 5-7]。

为验证DCDT结果，基于Khalil (2023)的全矿山FLAC3D模型建立简化版本。模型范围3000 m×1800 m×2100 m，包含86个采场、两条主要岩脉群及目标巷道，使用线性弹性本构，以滚轴边界约束侧面和底部位移，顶部为自由地表。初始应力场通过三维应力张量变换（式2–5）由原位应力方程生成，并在地表施加23 MPa附加应力以匹配应力趋势，模拟采掘‑充填序列至岩芯提取时刻[Li 2024, pp. 7-9]。从模型提取岩芯位置（A、B两点）的应力分量，经坐标变换得到平面主应力，与DCDT估算值进行对比[Li 2024, pp. 9-10]。

## Key Findings

- DCDT分析的两个岩芯（YD‑9130L‑NQ‑V1和V2）给出的最大主应力方向分别为N45°E和N90°E，平均为N67°E，与区域数据库给出的N35°E以及数值模型的平均方向N20°E均位于东北象限，方向判断吻合[Li 2024, pp. 5-7][Li 2024, pp. 9-10]。
- 应力大小对比：在3 m深处（A点），DCDT与模型的大主应力相差17.1%，小主应力差33%，差应力仅差8.7%；在1.5 m深处（B点），大主应力差14.2%，小主应力差0.3%，差应力差20.3%[Li 2024, pp. 9-10]。尽管存在偏差，工程实用上完全可接受。
- FLAC3D模型计算得到的原位应力随深度变化与实测回归方程吻合良好，说明应力初始化方式可靠[Li 2024, pp. 7-9]。
- 研究认为，DCDT可作为有效的应力风险快速诊断工具，辅助采准、预切顶及矿柱等场合的地压管理[Li 2024, pp. 9-10]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| DCDT测得位置A（3 m）大主应力66.4 MPa，小主应力17.9 MPa，差应力48.5 MPa；位置B（1.5 m）大主应力107.6 MPa，小主应力29.1 MPa，差应力78.5 MPa。 | [Li 2024, pp. 5-7] 表3 | TSED岩石；E=68.8 GPa, ν=0.25；垂直岩芯取自底板；假设σ_z=0。 | 直径数据来自三次旋转测量拟合。 |
| 数值模型对应位置应力：A点σ_L1=80.1 MPa, σ_L2=26.9 MPa, 差53.1 MPa, 方向20.14°；B点σ_L1=94.2 MPa, σ_L2=29.0 MPa, 差65.2 MPa, 方向19.14°（自Y轴逆时针方向）。 | [Li 2024, pp. 9-10] 表5、表6 | 线性弹性FLAC3D模型；应力初始化基于原位方程和调整后的正交主方向；模拟了实际采矿步骤。 | 方向转换后与DCDT比较。 |
| 原位主应力梯度方程：σ₁=−0.065x+677.84; σ₂=0.0028x+6.39; σ₃=0.0072x‑47.72（x为矿山标高，单位米）。 | [Li 2024, pp. 3-5] 式1 | 基于四个中段的套芯测量；应力值经方向正交化调整；假设随深度线性变化。 | 用于FLAC3D应力场生成。 |
| YDave平均材料参数：UCS=132.1 MPa, E=69.4 GPa, ν=0.26, 密度2.76 t/m³, GSI=63。 | [Li 2024, pp. 2-3] 表1 | TSED、SYN、MAFIC三种岩石由于强烈互层而均化处理。 | 实际岩体为互层状。 |
| 区域主应力方向N35°E（McKinnon and Labrie 2006）；YD矿实测平均方向019/28；数值模型得出的大主应力方向在东北象限。 | [Li 2024, pp. 2-3][Li 2024, pp. 3-5][Li 2024, pp. 9-10] | 考虑了区域构造和Y D矿实际测量。 | DCDT结果与这些区域及模型方向一致。 |

## Limitations

- DCDT的应用前提是钻孔轴向应力可忽略，本案例中底板轴向应力较小（17.7 MPa和13.6 MPa）故条件满足，但在远离自由面的位置可能不成立[Li 2024, pp. 5-7][Li 2024, pp. 9-10]。
- 验证仅基于两个岩芯，样本数偏少，且两者给出的方向差异较大（N45°E vs N90°E），方法的稳定性需要更多样本检验[Li 2024, pp. 5-7]。
- 数值模型为线性弹性，未考虑岩体屈服或破坏，且将复杂的采掘顺序简化为每500 m深度成组开挖，可能影响局部应力计算精度[Li 2024, pp. 7-9]。
- 岩芯北向标记可能存在人为操作误差，文中指出此因素可解释部分方向差异[Li 2024, pp. 9-10]。

## Assumptions / Conditions

- DCDT分析假设岩石为线弹性各向同性，解除套芯后直径变形仅由平面双轴应力释放引起，且钻孔轴向应力因靠近自由面而可忽略[Li 2024, pp. 5-7]。
- FLAC3D模型采用线性弹性本构，边界约束为垂直面法向位移约束，模型初始应力由实测回归方程通过三维张量变换施加，且主应力方向已人工调整至正交[Li 2024, pp. 7-9]。
- 原位应力场假定随深度线性变化，此线性关系外推至目标中段[Li 2024, pp. 3-5]。
- 底板围岩按平均属性处理，将互层的TSED、SYN、MAFIC合并为均质材料YDave[Li 2024, pp. 2-3]。

## Key Variables / Parameters

- 岩芯直径变形量 d_max, d_min
- 岩石弹性模量 E 与泊松比 ν（TSED案例中 E=68.8 GPa, ν=0.25）
- 原位主应力回归方程系数（σ₁、σ₂、σ₃随标高变化的梯度）
- 应力张量变换中的方向余弦矩阵 [L]
- FLAC3D模型输出的应力分量（σ_x, σ_y, σ_z, τ_xy）
- 平面主应力 σ_L1, σ_L2 及其方向 θ
- 岩芯取样深度（相对于底板）

## Reusable Claims

- [Li 2024] 证明了DCDT技术可有效估算采动应力，在底板自由面附近，其给出的主应力方向与区域构造场及数值模型一致，量级差异在20%左右，可用于工程实践。条件：线弹性岩石，轴向应力小，北向标记需准确。
- [Li 2024] 在拥有可靠地质力学数据和采掘历史的矿山，线性弹性FLAC3D模型能提供可用于校准新应力测量方法的参考应力场，即使模型经过简化仍可获得合理的对比基准。
- [Li 2024] DCDT作为一种快速、低成本的应力评估方法，可以部署在采场预生产、矿柱等地点，辅助识别应力集中风险；但需注意其精度受取样位置和方向标记的影响。

## Candidate Concepts

- [[diametrical core deformation technique (DCDT)]]
- [[mining-induced stress]]
- [[principal stress orientation]]
- [[core-based stress measurement]]
- [[linear elastic rock assumption]]
- [[mine-wide numerical model]]
- [[FLAC3D]]
- [[geomechanical database]]
- [[overcoring strain-relief method]]
- [[stress initialization in numerical models]]
- [[Young-Davidson mine]]

## Candidate Methods

- [[高精度激光测微仪测量岩芯直径变形]]
- [[岩芯旋转正弦曲线拟合法确定应力方向]]
- [[三维应力张量变换初始应力方法]]
- [[现场实测应力回归线性方程外推法]]
- [[基于微震事件校准的矿山数值模拟]]

## Connections To Other Work

- 直接延续Li and Mitri (2023)建立的DCDT分析模型及实验室验证，将其推广至现场验证[Li 2024, pp. 2-3][Li 2024, pp. 5-7]。
- 引用McKinnon and Labrie (2006)对Cadillac断裂带附近应力场的解释，获得区域主应力方向N35°E[Li 2024, pp. 2-3][Li 2024, pp. 3-5]。
- 数值模型框架源自Khalil (2023)的完整矿山模型，该模型通过Hoek‑Brown、Burst Potential Index、Brittle Shear Ratio等判据与九次主要微震事件进行了校准[Li 2024, pp. 7-9]。
- 在应力测量方法综述中，提及声发射（AE）、非弹性应变恢复（ASR）、差应变曲线分析（DSCA）、发展率分析（DRA）等岩芯法，以及钻孔变形、井壁崩落法等，并指出现有方法的局限性（如不能提供方向，或需专门设备）[Li 2024, pp. 1-2]。

## Open Questions

- 本次验证仅有两个样本，DCDT的应力方向离散性较大（N45°E至N90°E），欲评估其总体精度，需在更多地点和岩性条件下进行重复试验。
- 如果钻孔轴向应力不能忽略（如深孔测量），DCDT是否仍能通过校正模型获得可靠的差应力，尚待研究。
- 现场岩芯北向标记的人为误差如何通过标准化流程或改进的定向工具来消除，值得探讨。
- 简化采矿序列对模型局部应力计算结果的影响幅度，需要进一步量化分析。
- DCDT在采准巷道以外的采矿结构（如间柱、顶底柱、充填体附近）的适用性，尚未得到直接验证。

## Source Coverage

本页面完全根据提供的7个索引片段生成。所有非空片段均被处理，索引片段总字符数32195，编译使用字符数31909，按字符覆盖率0.991117，按块覆盖率1.0。来源签名：4aefeda1288c3f94bfbc172440e6c8e85d344767。未添加任何索引片段之外的信息。
