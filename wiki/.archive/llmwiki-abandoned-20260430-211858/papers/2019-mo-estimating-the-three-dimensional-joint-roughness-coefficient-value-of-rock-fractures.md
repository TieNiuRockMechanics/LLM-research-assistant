---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-mo-estimating-the-three-dimensional-joint-roughness-coefficient-value-of-rock-fractures"
title: "Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures."
status: "draft"
source_pdf: "data/papers/2019 - Estimating the three-dimensional joint roughness coefficient value of rock fractures.pdf"
collections:
  - "zotero new"
citation: "Mo, Ping, and Yanrong Li. \"Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures.\" *Bulletin of Engineering Geology and the Environment*, vol. 78, 2019, pp. 857–66. doi:10.1007/s10064-017-1150-0."
indexed_texts: "8"
indexed_chars: "39905"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:03:05"
---

# Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures.

## One-line Summary
Mo & Li (2019) 通过直接剪切试验和三维形貌扫描，建立了基于九种全表面三维粗糙度参数的节理粗糙度系数（JRC）经验估算方程，并评估了采样间隔的影响。

## Research Question
如何利用反映整个裂隙面的三维粗糙度参数来可靠地估算岩石节理的 JRC 值？不同类别的三维参数估算效果如何？采样间隔对这些参数的估算能力有何影响？

## Study Area / Data
- **样本**：38 组新鲜岩石块体，包括 9 组石灰岩、12 组花岗岩和 17 组砂岩；节理面从光滑到极粗糙，形成系列 [Mo 2019, pp. 4-6]。
- **试件尺寸**：长度和宽度限制在 120 mm × 120 mm [Mo 2019, pp. 4-6]。
- **数据采集**：利用激光扫描（HAND SCAN™ 300，分辨率 0.1 mm，精度 0.04 mm）以 0.2 mm 空间分辨率对剪切前后的上、下裂隙面进行数字化，获得点云数据 [Mo 2019, pp. 6-7]。
- **力学参数**：通过锯切干燥节理面的倾斜试验获取基本摩擦角 (φb)；38 组试件的 JCS 范围为 15.02–71.19 MPa，法向应力与 JCS 之比 (σn/JCS) 均小于 0.03 [Mo 2019, pp. 4-6]。

## Methods
- **三维粗糙度参数分类与综述**：将描述整个裂隙面的参数按物理意义分为四类：坡度、面积、体积和幅度参数，并综述其可计算性 [Mo 2019, pp. 2-3]。
- **表面重构模型**：采用不规则三角网（TIN）和三维线框（3D wireframe）模型从点云重建裂隙面形貌 [Mo 2019, pp. 2-3][Mo 2019, pp. 6-7]。
- **粗糙度参数计算**：
  - 幅度参数（如 Zsa, Zrms, Zrange）由点云直接通过 Excel 计算；
  - 坡度参数（θs, θ2s）由 TIN 模型计算；
  - 体积参数（Van）由三维线框模型计算；
  - 面积参数（SsT 和 SsF）由 TIN 和三维线框模型计算 [Mo 2019, pp. 6-7]。
- **JRC 反算**：对每组试样沿四个方向进行直剪试验，取四个方向峰值强度的平均值，利用 Barton 的 JRC‑JCS 模型反算 JRC [Mo 2019, pp. 7-8]。
- **经验方程建立**：对样本进行回归分析，建立不同三维粗糙度参数与反算 JRC 的经验方程，并考虑采样间隔（0.4, 0.8, 1.6, 3.2, 6.4 mm）的影响 [Mo 2019, pp. 8-10]。

## Key Findings
- 九种参数 (θs, θg, θ2s, SsT, SsF, Van, Zsa, Zrms, Zrange) 与 JRC 具有高度相关性（相关系数 > 0.75），可用于估算岩石裂隙面的 JRC [Mo 2019, pp. 1-2][Mo 2019, pp. 8-10]。
- 六种参数 (Zss, Zsk, Vsvi, Vsci, Sdr, Sts) 与 JRC 无良好相关性 [Mo 2019, pp. 1-2]。
- 体积和幅度参数 (Van, Zsa, Zrms, Zrange) 对采样间隔不敏感；坡度参数 (θs, θg, θ2s) 和面积参数 (SsT, SsF) 的估算受采样间隔影响较大 [Mo 2019, pp. 1-2][Mo 2019, pp. 8-10]。
- 在工程实践中，推荐使用计算简便的幅度参数方程来实现 JRC 的快速估算 [Mo 2019, pp. 1-2][Mo 2019, pp. 8-10]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 九参数 (θs, θg, θ2s, SsT, SsF, Van, Zsa, Zrms, Zrange) 与 JRC 经验方程的相关系数均大于 0.75 | [Mo 2019, pp. 1-2, 8-10] | 基于 38 组新鲜岩石裂隙直剪试验数据，法向应力/JCS < 0.03 | 坡度参数表现最优，幅度参数表现最差 |
| 幅度参数 (Zsa, Zrms, Zrange) 对采样间隔（0.4–6.4 mm）不敏感 | [Mo 2019, pp. 1-2, 8-10] | 点云按 0.4, 0.8, 1.6, 3.2, 6.4 mm 间隔重采样 | 因此推荐幅值参数用于工程快速估算 |
| 剖面斜率参数 (θs, θg, θ2s) 和面积参数 (SsT, SsF) 受采样间隔影响明显 | [Mo 2019, pp. 1-2, 8-10] | 同条件下，采样间隔变化导致回归系数改变 | 与坡度型 2D 参数的高灵敏度一致 |
| 上下裂隙面的幅度参数（Zrms, Zsa, Zrange）差异最大约 −4.68%，表明表面匹配良好 | [Mo 2019, pp. 6-7] | 新鲜裂隙，上下表面无宏观间隙和充填 | 支持用下表面代表耦合节理面 |
| 所提新参数 θg（全表面实际倾角积分）避免了拟合值 C，计算更简便 | [Mo 2019, pp. 7-8] | 基于 TIN 模型和实际倾角分布 Aα | 替代考虑了剪切方向的 θci 参数 |
| Zsk 和 Zss 与 JRC 无相关性 | [Mo 2019, pp. 8-10] | 基于 38 组样本的回归分析 | 两者属于形貌高度分布的偏度和峰度参数 |

## Limitations
- 经验方程仅基于 38 组新鲜、匹配良好的岩石节理，未考虑风化、充填或错动节理表面 [Mo 2019, pp. 4-6]。
- 试验在低法向应力（σn/JCS < 0.03）下进行，以避免剪切过程中表面破坏，但限制了对高应力条件的推广 [Mo 2019, pp. 7-8]。
- 所推荐的幅度参数尽管计算简便，但与 JRC 的相关性在所有四类参数中最弱 [Mo 2019, pp. 8-10]。
- 原始论文中可能涉及的其他限制因素（如尺寸效应、岩性多样性）未从索引片段中确认。

## Assumptions / Conditions
- 上下裂隙面为新劈裂且 100% 接触，无空隙和填充物，形貌匹配良好 [Mo 2019, pp. 4-6]。
- 用平均峰值强度（四个方向的均值）反算 JRC，假定了表面粗糙度参数具有方向无关性 [Mo 2019, pp. 7-8]。
- 下表面可代表耦合节理面，且其原始形貌用于生成三维粗糙度参数 [Mo 2019, pp. 7-8]。
- 试验中 σn/JCS 维持极低水平，防止了表面在剪切中严重损伤，从而保证 JRC 反算可靠 [Mo 2019, pp. 7-8]。

## Key Variables / Parameters
- **JRC**：节理粗糙度系数，由平均峰值强度通过 Barton 模型反算。
- **三维粗糙度参数（有显著相关性的九种）**：θs （全表面角系数）、θg （实际倾角积分）、θ2s （表面角系数平方）、SsT 和 SsF （表面积比）、Van （净体积/投影面积比）、Zsa （绝对高度平均值）、Zrms （均方根高度）、Zrange （高度范围） [Mo 2019, pp. 1-2, 7-10]。
- **三维粗糙度参数（无显著相关性的六种）**：Zss （偏度）、Zsk （峰度）、Vsvi （谷部流体滞留指数）、Vsci （核心流体滞留指数）、Sdr （相对表面粗糙度）、Sts （表面曲折系数） [Mo 2019, pp. 1-4]。
- **采样间隔（SI）**：点云重采样间隔 0.4, 0.8, 1.6, 3.2, 6.4 mm [Mo 2019, pp. 6-7]。
- **基本摩擦角 (φb) 和 JCS**：由倾斜试验和施密特锤测定，用于反算和剪切强度计算 [Mo 2019, pp. 1-6]。

## Reusable Claims
1. 对于低法向应力下的新鲜匹配岩石节理，可使用与方向无关的全表面三维粗糙度参数来估算 JRC；其中坡度参数（θs, θg, θ2s）的相关性最高，但计算需借助 TIN 模型和专用软件 [Mo 2019, pp. 7-10]。
2. 当工程中需要快速、简便的 JRC 估算时，推荐采用幅度参数（Zsa, Zrms, Zrange），因其可直接从点云通过 Excel 计算，且对采样间隔不敏感，尽管回归相关系数略低于坡度参数 [Mo 2019, pp. 8-10]。
3. 若采用坡度或面积参数（如 θs, SsT）估算 JRC，必须注意采样间隔会明显影响估算系数，应在实践中固定采样间隔或建立间隔相关的多元回归方程 [Mo 2019, pp. 8-10]。
4. 参数 θg（全表面实际倾角的积分）可作为对剪切方向敏感参数（如 θci）的有效替代，它避免了拟合常数 C 的引入，同时计算更为简便 [Mo 2019, pp. 7-8]。

## Candidate Concepts
- [[joint roughness coefficient]]
- [[three-dimensional roughness parameter]]
- [[direct shear test]]
- [[point cloud]]
- [[rock fracture surface morphology]]
- [[peak shear strength]]
- [[JRC-JCS model]]

## Candidate Methods
- [[Triangulated Irregular Network (TIN) model]]
- [[3D wireframe model]]
- [[laser scanning digitization]]
- [[back-calculation of JRC from shear tests]]
- [[multiple regression with sampling interval]]

## Connections To Other Work
- 本研究的根基是 Barton (1973) 提出的 JRC‑JCS 模型，用于节理峰值剪切强度估算 [Mo 2019, pp. 1-2]。
- 三维表面形貌表征方法借鉴了 Grasselli (2001) 和 Belem et al. (2000) 的 TIN 与 3D 线框模型，以及他们提出的坡度与面积参数 [Mo 2019, pp. 2-3]。
- 部分幅度参数（如 Zsa, Zrms, Zrange）和体积参数参照了 ISO 25178‑2:2012 表面形貌标准 [Mo 2019, pp. 3-4]。
- 本研究提出的振幅参数选择和对采样间隔敏感性的讨论与 Li et al. (2016) 和 Liu et al. (2017) 在二维 JRC 估算中的发现一致：振幅类 2D 参数对采样间隔的敏感性低于坡度类参数 [Mo 2019, pp. 8-10]。

## Open Questions
- 所建方程对风化、含充填物或在较高法向应力下未匹配节理的适用性未从索引片段中确认。
- 对不同岩性（石灰岩、花岗岩、砂岩）的混合使用是否引入额外不确定性，是否需要分岩性建立方程，未从索引片段中确认。
- 三维参数估算 JRC 的尺寸效应和大规模原位节理的适用性未从索引片段中确认。

## Source Coverage
本知识页依据论文的 8 个索引片段编写，覆盖了摘要、文献综述、样本制备与试验方法、部分结果（经验方程和讨论）。由于片段均为摘录，完整的方法细节（如所有三维参数的具体计算公式表）、全部 38 组试样的详细力学与形貌数据表以及结论部分可能缺失。所引页码为索引片段中标注的范围，非原论文精确页码，建议引用时参考正式出版物。任何超出片段范围的推论已被标注为“未从索引片段中确认”。
