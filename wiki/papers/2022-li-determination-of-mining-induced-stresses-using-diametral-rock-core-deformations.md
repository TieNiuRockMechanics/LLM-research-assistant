---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-li-determination-of-mining-induced-stresses-using-diametral-rock-core-deformations"
title: "Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations."
status: "draft"
source_pdf: "data/papers/2022 - Determination of mining-induced stresses using diametral rock core deformations.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations.\" *International Journal of Coal Science & Technology*, vol. 9, article 80, 2022. doi:10.1007/s40789-022-00549-2. Accessed 25 Mar. 2026."
indexed_texts: "7"
indexed_chars: "31884"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31525"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.98874"
coverage_status: "full-index"
source_signature: "d459a98dd0cf954759fd2c18069d3b823a1814c4"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:13:29"
---

# Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations.

## One-line Summary
提出并验证一种利用岩心直径变形测量估算采矿诱发的差应力及脆性剪切比（BSR）的非破坏性方法，通过两个地下矿山案例展示其可行性。

## Research Question
如何利用勘探岩心钻取后因应力释放产生的直径变化，在实验室条件下确定采动诱发的差应力及其方向，从而为硬岩矿山岩体稳定性评价和应变岩爆风险分析提供一种简便实用的方法？

## Study Area / Data
- **案例1**：加拿大Fraser矿，三个钻孔（ST46745, ST46745A, 441034），深度约1340 m。岩样包括花岗岩、长英质片麻岩、Sudbury角砾岩、Matachewan辉绿岩，钻头尺寸AQTK (30.5 mm) 和 NQ (47.6 mm)。[Li 2022, pp. 7-10]
- **案例2**：加拿大Hoyle Pond矿，两个钻孔（25947, 25986），深度1357 m 和 1840 m，共19个NQ (47.6 mm) 岩样，岩性为高铁玄武岩和玄武质科马提岩。[Li 2022, pp. 10-12]

## Methods
- **岩心直径测量**：采用分辨率±0.0001 mm的激光测微系统，在实验室中对旋转360°的岩心进行连续测量，获取最大直径 \( d_{max} \) 和最小直径 \( d_{min} \)。该装置由高精度滚轮支撑，可适应AQTK到PQ多种尺寸。[Li 2022, pp. 3-5]
- **弹性参数试验**：直径测量后，按ASTM D7012标准进行单轴抗压强度（UCS）试验，试件粘贴水平和垂直120 Ω应变片，以测定杨氏模量 \( E \) 和泊松比 \( \nu \)。[Li 2022, pp. 5-7]
- **应力计算**：基于Funato和Ito (2017)的线弹性各向同性模型，采用公式 \( \sigma_H - \sigma_h = \frac{E}{1+\nu} \cdot \frac{d_{max} - d_{min}}{d_{min}} \) 计算垂直于岩心轴平面上的差应力。[Li 2022, pp. 2-3]
- **灵敏度分析**：针对0.00025 mm和0.0001 mm两种分辨率，评估直径测量误差对差应力计算结果的影响，以确定仪器精度要求。[Li 2022, pp. 3-5]

## Key Findings
- 为保证差应力计算误差控制在±3%以内，测微仪分辨率不应低于±0.0001 mm；分辨率由0.00025 mm提升至0.0001 mm时，差应力最大误差从>5%降至<2.3%。[Li 2022, pp. 3-5]
- NQ (47.6 mm) 岩心直径变形测量的重复性明显优于AQTK (30.5 mm)，小直径岩心难以确定主应力方向。[Li 2022, pp. 7-10, 12]
- Fraser矿案例：441034钻孔NQ Sudbury角砾岩 (\( d_{max}=47.61393 \) mm, \( d_{min}=47.59205 \) mm, \( E=80.0 \) GPa, \( \nu=0.174 \)) 的差应力为31.3 MPa。[Li 2022, pp. 7-10]
- Hoyle Pond矿案例：钻孔25986的NQ玄武质科马提岩 (\( E=83.3 \) GPa, \( \nu=0.13 \)) 差应力范围为33.82–90.81 MPa，随深度呈整体上升趋势，但波动可能由附近采矿活动引起。[Li 2022, pp. 10-12]
- 差应力可进一步转化为最大剪应力 \( (\sigma_1-\sigma_3)/2 \) 和脆性剪切比 \( BSR = (\sigma_1-\sigma_3)/UCS_{intact} \)，用于硬岩应变岩爆潜能分级（BSR>0.7 对应严重损伤）。[Li 2022, pp. 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 分辨率0.0001 mm下最大应力误差: σH ±0.52%, σh ±2.67%，差应力误差<2.3% | [Li 2022, pp. 3-5] | 基准参数: dmax=47.61393 mm, dmin=47.59205 mm, E=76.4 GPa, ν=0.174 | 0.00025 mm分辨率差应力误差>5% |
| Fraser矿441034-SDBX-84 (NQ Sudbury角砾岩) dmax=47.61393 mm, dmin=47.59205 mm, E=80.0 GPa, ν=0.174 | [Li 2022, pp. 7-10] | 深度1340 m, 钻孔倾角-38.15° | 计算差应力=31.3 MPa |
| Hoyle Pond矿NQ玄武质科马提岩E=83.3 GPa, ν=0.13 | [Li 2022, pp. 10-12] | 钻孔25986, 深度43–50 m | 差应力33.82–90.81 MPa, 随深度增加 |
| BSR分级: ≤0.35 无/微损伤; 0.45–0.6 中等; >0.7 重度应变岩爆潜能 | [Li 2022, pp. 10-12] | 依据Castro et al. (2012) | 适用于硬岩矿山脆性破坏评估 |

## Limitations
1. 理论模型假设岩石为完美线弹性、各向同性、连续介质，实际岩体常偏离此假设。[Li 2022, pp. 12]
2. 岩心应力释放引起的变形和破裂可能受矿物成分影响（Gao et al. 2021）；若变形受裂隙主导，则无法用本法确定主应力（Funato and Ito 2017）。[Li 2022, pp. 12]
3. 该方法仅能获得垂直于岩心轴平面上的差应力与主方向，当岩心未标记重力方向或未记录钻孔方位时，无法还原绝对应力方向。[Li 2022, pp. 7-8, 12]

## Assumptions / Conditions
- 岩体为均质、各向同性、线弹性连续体。[Li 2022, pp. 2-3, 12]
- 岩心直径变化完全由应力释放引起，且dmax和dmin可精确测量。[Li 2022, pp. 1-2]
- 实验室可获取可靠的E和ν值。[Li 2022, pp. 5-7]
- 当岩心轴与某一原位主应力方向平行时，计算出的σH与σh即为该平面上的两个主应力。[Li 2022, pp. 2-3]

## Key Variables / Parameters
- 岩心最大/最小直径 \( d_{max} \), \( d_{min} \) (mm)
- 杨氏模量 \( E \) (GPa)，泊松比 \( \nu \)
- 差应力 \( \Delta\sigma = \sigma_H - \sigma_h \) (MPa)
- 脆性剪切比 \( BSR = \Delta\sigma / UCS_{intact} \)
- 仪器分辨率 (mm)
- 岩心尺寸 (AQTK: 30.5 mm; NQ: 47.6 mm)

## Reusable Claims
- 采用分辨率≥0.0001 mm的激光测微仪进行岩心直径变形测量，可确保差应力计算误差在±3%以内。[Li 2022, pp. 3-5]
- 大直径岩心（如NQ）的变形测量重复性优于小直径岩心（AQTK），应优先选用大尺寸岩心以提高应力估计精度。[Li 2022, pp. 7-10, 12]
- 在已知E和ν的情况下，差应力可由简化的线弹性公式 \( \Delta\sigma = \frac{E}{1+\nu} \cdot \frac{d_{max} - d_{min}}{d_{min}} \) 直接估算。[Li 2022, pp. 2-3]
- BSR可作为硬岩矿山脆性破坏和应变岩爆潜能的实用判据，当BSR>0.7时预示严重风险。[Li 2022, pp. 10-12]

## Candidate Concepts
- [[diametral core deformation]]
- [[mining-induced stress]]
- [[brittle shear ratio (BSR)]]
- [[stress relief method]]
- [[strainburst potential]]
- [[exploration core-based stress measurement]]

## Candidate Methods
- [[laser micrometer core diameter measurement]]
- [[UCS test with strain gauges]]
- [[Funato and Ito (2017) diametral deformation analysis]]
- [[sensitivity analysis for measurement resolution]]
- [[differential stress calculation from core expansion]]

## Connections To Other Work
- Funato和Ito (2017) 提出的岩心直径变形分析模型是本研究应力计算的基础。[Li 2022, pp. 2-3]
- Castro et al. (2012) 建立的BSR-岩体损伤关系表被直接引用，将差应力成果转化为脆性破坏评估依据。[Li 2022, pp. 10-12]
- Gao et al. (2021) 对岩心钻取过程中变形与破裂的数值模拟提醒了矿物组分和裂隙可能干扰测量信号。[Li 2022, pp. 12]
- Ziegler和Valley (2021) 的研究验证了利用岩心直径变形确定主应力方向的可靠性。[Li 2022, pp. 7-8]

## Open Questions
- 当岩心未标记重力方向时，如何有效恢复原位主应力方向？[Li 2022, pp. 7-8]
- 对于裂隙发育或显著各向异性岩体，该方法是否仍然适用？[Li 2022, pp. 12]
- 能否结合多方向钻孔的测量结果反演场地的三维应力状态？
- 差应力深部变化与采矿活动间的定量因果关系尚不清楚，需进一步结合开挖时序验证。[Li 2022, pp. 10-12]

## Source Coverage
All non-empty indexed fragments were processed. Coverage ratios: by blocks = 1.0, by characters = 0.98874. The source signature is d459a98dd0cf954759fd2c18069d3b823a1814c4, compiled from 7 source blocks encompassing 31525 characters (out of 31884 indexed characters). The full content from pages 1–12, including abstract, methodology, case studies, discussion, and references, was incorporated.
