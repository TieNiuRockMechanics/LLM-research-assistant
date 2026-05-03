---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-li-methodology-for-the-estimation-of-mining-face-stresses-using-rock-core-diametrical-defor"
title: "Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation."
status: "draft"
source_pdf: "data/papers/2023 - Methodology for the estimation of mining face stresses using rock core diametrical deformation.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 161, 2023, p. 105300. *ScienceDirect*, doi:10.1016/j.ijrmms.2022.105300. Accessed 2026."
indexed_texts: "6"
indexed_chars: "26475"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "24851"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.938659"
coverage_status: "full-index"
source_signature: "2ef0a8bd11fab150012b8a84a5d78e1022f8458d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:54:47"
---

# Methodology for the Estimation of Mining Face Stresses Using Rock Core Diametrical Deformation.

## One-line Summary

提出一种基于钻孔岩心直径变形估算采矿工作面近场双轴应力的分析方法，通过体积应变方程弥补原始岩心直径未知的缺陷，并在单轴实验数据上验证了模型的准确性。

## Research Question

如何利用从采矿工作面附近钻取的岩心直径变形，确定自由面附近与钻孔轴线垂直平面内的两个主应力大小？

## Study Area / Data

验证实验数据来自 Funato 和 Ito（2017）[12] 的实验室测试，包括在单轴压缩下从安山岩、花岗岩、砂岩和砂浆立方体中心取出的岩心。岩样力学参数见表 1，实测岩心直径数据见表 2。实验涵盖 5–15 MPa（安山岩）、5–10 MPa（花岗岩）、5–7.5 MPa（砂岩）及 2.5–7.5 MPa（砂浆）的施加应力。

## Methods

1. **基本假设**：钻孔轴线垂直于采矿工作面，且测量点靠近工作面，因此沿钻孔轴线方向的应力可忽略（σ_z ≈ 0）。  
2. **弹性解**：基于平面应力状态的胡克定律，建立主应力与岩心直径变化的关系（式 2a、2b），其中原始直径 d_o 未知。  
3. **体积应变方程**：利用岩心卸载后的体积应变 ε_v = (1-2ν)/E (σ_H + σ_h) 及椭圆截面面积积分（式 10、11），推导出 d_o 的表达式（式 13），与式 2a、2b 联立求解 σ_H、σ_h、d_o。  
4. **直径测量**：实验室采用高精度激光测微计，分辨率 ±0.0001 mm，测定最大直径 d_max 和最小直径 d_min。  
5. **岩石力学参数**：通过单轴抗压强度试验获取杨氏模量 E 和泊松比 ν。  

## Key Findings

1. 差分应力 σ_H – σ_h 对 d_o 的微小变化不敏感，因此岩心变形方法在估计主应力差时具有可靠性（式 5）。  
2. 通过引入体积应变约束，可确定未知原始直径 d_o，从而解出 σ_H 和 σ_h。  
3. 在 Funato 和 Ito 的单轴实验数据（12 组）上，本文方法估算的应力与实际施加应力高度吻合，决定系数 R² = 0.9313（图 7、表 3）。  
4. 与 Funato 和 Ito 的既有方法（只能给出差分应力或单轴应力）相比，本文方法能够估算双轴应力状态。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 差分应力公式 σ_H – σ_h = E/(1+ν) · (d_max – d_min)/d_o（式 5） | [Li 2023, pp. 2-3] | 忽略钻孔轴向应力 σ_z≈0 | Funato & Ito 12 首次提出，文中证明 d_o 微小变化对差分应力影响很小 |
| 控制方程（2a、2b）与体积应变导出的 d_o 公式（13）联立可解出 σ_H、σ_h、d_o | [Li 2023, pp. 2-3] | 需已知 E、ν，且 σ_z≈0 | 需高精度直径测量 |
| 单轴实验验证，12 组数据 R²=0.93（表 3、图 7） | [Li 2023, pp. 3-5] | 施加应力为已知，σ_h=0 | 包含安山岩、花岗岩、砂岩、砂浆 |
| 岩样力学参数（表1） | [Li 2023, pp. 4] | 实验室测定 | E 和 ν 为必要输入 |
| 高分辨率激光测微计（±0.0001 mm） | [Li 2023, pp. 1-2] | 测量 d_max、d_min | 精度影响应力估算敏感性 |
| 体积应变推导中，变形截面面积通过积分得到（式10） | [Li 2023, pp. 3] | 假设变形后截面为椭圆形式（式9） | 依赖 Funato 和 Ito 的截面表达式 |

## Limitations

1. 模型假设钻孔轴线垂直于工作面且 σ_z=0，这在距工作面较远或非垂直钻孔时可能不成立。  
2. 单孔岩心只能确定钻孔轴线垂直平面内的两个主应力，无法获得三维应力张量。  
3. 验证仅基于单轴压缩实验数据，尚未在双轴应力条件下进行实验校验（作者已计划后续工作）。  
4. 岩心直径的测量精度对应力估算结果高度敏感，需要极高分辨率的仪器。  
5. 推导中采用了各向同性线弹性假设，未考虑岩石的非均质性和非线性行为。

## Assumptions / Conditions

- 钻孔轴线垂直于自由采矿面，且测量点靠近该面，使得 σ_z ≈ 0。  
- 岩体为均质、各向同性线弹性材料。  
- 岩心卸载后的截面形状可用椭圆函数描述（式 9）。  
- 岩心在钻进过程中未发生塑性变形或损伤（除弹性卸载外）。  
- 岩石的 E 和 ν 可通过同一岩心的 UCS 试验准确确定。

## Key Variables / Parameters

- σ_H, σ_h：与自由面平行的平面内的最大、最小主应力（未知）  
- d_o：岩心在原始应力状态下的直径（未知）  
- d_max, d_min：卸载后岩心椭圆截面的最大、最小直径（实测）  
- E, ν：岩石的杨氏模量和泊松比（实验室测定）  
- ε_v：体积应变（由式 7 定义）  
- Δd = d_max - d_min  
- 应力差 Δσ = σ_H - σ_h

## Reusable Claims

1. 采矿工作面附近，垂直于工作面的应力可视为零时，可利用岩心弹性卸载引起的椭圆变形反算双轴主应力。  
2. 利用体积应变约束方程（式 13）可闭合由两个应力-应变方程（式 2a、2b）构成的欠定系统，从而得到 σ_H、σ_h 和 d_o。  
3. 该方法在单轴应力实验（σ_h=0）中的应力预测误差较小，R²=0.93，表明其对零侧压条件的双轴应力反演具有初步有效性。  
4. 对差分应力 σ_H – σ_h 的估计对 d_o 的选取不敏感，可在原始直径未知时可靠获得。

## Candidate Concepts

- [[diametrical core deformation analysis]]  
- [[strain relief method for stress measurement]]  
- [[volumetric strain closure for core analysis]]  
- [[near-field mining-induced stress]]  
- [[core-based stress estimation]]  
- [[biaxial stress from single borehole core]]  

## Candidate Methods

- [[laboratory core deformation measurement with laser micrometer]]  
- [[volumetric strain method for solving unknown core diameter]]  
- [[two-equation two-unknown stress inversion from core expansion]]  
- [[combination of core deformation and UCS test for stress determination]]  
- [[analytical model for biaxial stress at free face]]  

## Connections To Other Work

- 本文方法建立在 Funato 和 Ito（2017）[12] 的岩心直径变形分析基础之上，其原始方法仅能获得差分应力，本文通过体积应变闭合将其扩展至双轴应力量值估计。  
- 岩心变形测量的高精度要求与 Li 和 Mitri（2022）[11] 的装置开发工作相关。  
- 采矿工作面应力引起的表面破坏（剥落、岩爆等）与 Mitri 等[6-9]的岩体双轴强度研究相关联。  
- 传统应力测量如套芯法、水压致裂法通常测量远场应力[1-3]，本文方法聚焦于采矿活动诱导的近场应力。

## Open Questions

- 该模型在双轴应力（σ_h≠0）条件下的实验验证尚待完成。  
- 如何处理实际钻孔轴线与工作面不完全垂直的情况，需进一步研究。  
- 岩心从孔底到地面过程中的松弛是否仅为弹性，是否需要塑性修正。  
- 不同尺度（孔径、岩心直径）下该方法的适用性及其对仪器精度的最低要求。  
- 能否将单孔岩心数据扩展至三维应力估算，例如通过组合不同方向的岩心结果。

## Source Coverage

All 6 non-empty indexed fragments from the paper (including the corrigendum) were processed. The compiled source blocks total 6, with 24,851 characters extracted from an original 26,475 characters, yielding a block coverage ratio of 1.0 and a character coverage ratio of 0.939. No fragments were omitted.
