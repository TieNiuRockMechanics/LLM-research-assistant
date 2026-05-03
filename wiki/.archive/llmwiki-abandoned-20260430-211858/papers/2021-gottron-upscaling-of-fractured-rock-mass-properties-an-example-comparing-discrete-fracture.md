---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-gottron-upscaling-of-fractured-rock-mass-properties-an-example-comparing-discrete-fracture"
title: "Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications."
status: "draft"
source_pdf: "data/papers/2021 - Upscaling of fractured rock mass properties – An example comparing Discrete Fracture Network (DFN) modeling and empirical relations based on engineering rock ma.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Gottron, D., and A. Henk. \"Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications.\" *Engineering Geology*, vol. 294, 2021, 106382, doi:10.1016/j.enggeo.2021.106382."
indexed_texts: "19"
indexed_chars: "91396"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:33:26"
---

# Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications.

## One-line Summary

本研究基于两个砂岩露头，比较了离散裂隙网络（DFN）建模与基于工程岩体分类的经验关系在岩体弹性属性升级中的表现，并评估了各方法的不确定性 [Gottron 2021, pp. 1-2]。

## Research Question

如何可靠地估算裂隙岩体的弹性属性（如变形模量和泊松比），并在离散裂隙网络建模方法与基于传统工程岩体分类的经验关系之间进行系统性比较？研究同时旨在量化由于裂隙几何和输入参数不确定性导致的估算结果变异性 [Gottron 2021, pp. 1-2]。

## Study Area / Data

研究应用于德国南部的 Remlingen 和北部的 Flechtingen 两个砂岩采石场。数据来源于：
- **露头扫描**：使用地面激光扫描仪获取点云数据（Remlingen 点云含27,196,466个点，Flechtingen 含18,057,301个点），并据此提取裂隙产状、尺寸和强度 [Gottron 2021, pp. 6-7]。
- **实验室测试**：对完整岩石进行单轴和三轴试验，获取单轴抗压强度（UCS）、弹性模量和泊松比；对裂隙表面进行直剪试验获取剪切强度。三轴围压范围 5–30 MPa，直剪正应力范围 1.5–6.5 MPa [Gottron 2021, pp. 7-8]。
- 对于 Remlingen 采石场未能取样的水平层状弱面（R3），其力学参数引用自 Ernst et al. (2016) [Gottron 2021, pp. 7-8]。

## Methods

研究流程包含以下步骤：
1. **裂隙几何建模**：基于点云数据确定裂隙组（产状、等效半径和强度 P10, P32 的概率密度函数）[Gottron 2021, pp. 5-6]。使用 Pij 系统，通过 P10 和 C31 系数解析转换为 P32 [Gottron 2021, pp. 3-4]。
2. **DFN 建模**：使用统计方法生成随机裂隙网络，可结合确定性大型裂隙/断层。通过比较现场数据验证模型几何。为裂隙组和岩块赋值实验室测得的力学参数（黏聚力、摩擦角、法向刚度和剪切刚度）[Gottron 2021, pp. 8-9]。
3. **升级方法**：采用 **Oda 岩土力学方法**，基于裂隙柔度张量及岩块柔度张量，计算岩体弹性属性。假设岩体为各向同性或垂直横向各向同性（VTI）[Gottron 2021, pp. 8-9]。
4. **经验关系**：基于工程岩体分类（RQD, RMR, GSI）的经验公式计算变形模量 [Gottron 2021, pp. 4-5]。
5. **不确定性处理**：通过蒙特卡洛仿真技术处理分类方案中输入参数（如评分）的不确定性 [Gottron 2021, pp. 2-3]。开展包含18个额外模型的参数敏感性分析，以探究岩块弹性模量、剪切/法向刚度和裂隙强度的影响 [Gottron 2021, pp. 8-9]。

## Key Findings

1. 不同经验方法估算的岩体属性存在**显著离散性**。只有那些在分类评分外**同时包含完整岩石属性**的经验公式能得到合理的结果（即因裂隙导致强度显著降低），并与 DFN 方法的估算结果一致 [Gottron 2021, pp. 1-2]。
2. DFN 方法能提供各向异性的水力-力学属性张量，而基于分类的经验关系则无法直接提供空间变异和各向异性属性 [Gottron 2021, pp. 2-3]。
3. 参数敏感性分析揭示了如岩块弹性模量、刚度和裂隙强度等输入参数对升级结果的具体影响 [Gottron 2021, pp. 8-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 仅整合了完整岩石属性的经验公式，其结果与 DFN 模型估算结果一致，并显示出因裂隙导致的显著弱化。 | [Gottron 2021, pp. 1-2] | 应用于两个砂岩露头。 | 强调了在分类评分外考虑完整岩石属性的重要性。 |
| Remlingen 采石场裂隙组 R1 的等效半径为 7.63 ± 0.56 m (lognormal)，P32 为 0.28 m⁻¹。 Flechtingen 采石场裂隙组 F3 的等效半径为 3.54 ± 1.51 m (lognormal)，P32 为 0.38 m⁻¹。 | [Gottron 2021, pp. 5-6] | 基于 TLS 点云数据提取。 | 具体数据见表1，展示了裂隙几何参数及其概率分布。 |
| Oda 岩土力学法用于升级，可通过结合裂隙柔度张量和岩块柔度张量，计算各向同性或 VTI 假设下的岩体弹性特性。 | [Gottron 2021, pp. 8-9] | 应用于 DFN 模型网格（50×50×50 m³ 单网格，或 10×10×10 网格）。 | 升级结果与经验公式对比。 |
| RQD 值受钻孔或测线方向与裂隙方向关系影响高度敏感，尤其在裂隙中等发育的岩体中，且存在钻探材料和岩芯回收率等误差源。 | [Gottron 2021, pp. 4-5] | 参考 Priest and Hudson (1976) 的负指数关系。 | 强调 RQD 的不确定性。 |

## Limitations

- 对 Remlingen 采石场的水平层状弱面（R3）**未能直接取样测试**，其力学参数从其他文献引用，引入不确定性 [Gottron 2021, pp. 7-8]。
- RMR 等分类评分依赖于个人经验，**存在主观性** [Gottron 2021, pp. 4-5]。
- 研究结果基于两个特定地点的砂岩岩体，其**普适性**未从索引片段中确认。
- 未从索引片段中确认 DFN 模型对裂隙尺寸（等效半径）取值的截断或上限效应是否被充分讨论。

## Assumptions / Conditions

- 研究假设岩体的力学行为可用弹性模型描述，重点关注变形模量和泊松比 [Gottron 2021, pp. 1-2]。
- DFN 升级计算中假设岩体为**各向同性或垂直横向各向同性** [Gottron 2021, pp. 8-9]。
- 裂隙被视为具有特定力学属性（黏聚力、摩擦角、刚度）的离散平面 [Gottron 2021, pp. 8-9]。
- 蒙特卡洛仿真用于处理分类指标的随机性，假设各输入参数的统计分布是可靠的 [Gottron 2021, pp. 2-3]。
- 升级过程中采用的 Oda 方法假设裂隙对岩体总体柔度的贡献可叠加 [Gottron 2021, pp. 8-9]。

## Key Variables / Parameters

- **几何参数**：裂隙组产状（倾向/倾角），等效半径，裂隙强度（P10，P32），C31 系数 [Gottron 2021, pp. 3-6]。
- **岩块力学参数**：弹性模量，泊松比，单轴抗压强度（UCS） [Gottron 2021, pp. 7-8]。
- **裂隙力学参数**：黏聚力，摩擦角，法向刚度，剪切刚度 [Gottron 2021, pp. 8-9]。
- **经验分类指标**：岩石质量指标（RQD），岩体评分（RMR），地质强度指标（GSI） [Gottron 2021, pp. 4-5]。
- **升级后属性**：岩体变形模量，泊松比 [Gottron 2021, pp. 1-2]。

## Reusable Claims

1. 采用经验关系评估裂隙岩体变形模量时，仅依靠分类评分（如 RMR）会引入显著不确定性；为获得与数值模型（如 DFN）一致的结果，经验公式必须显式地纳入完整岩石的力学属性 [Gottron 2021, pp. 1-2]。
2. 裂隙强度指标 P32（裂隙面积/体积）是 DFN 建模中刻画裂隙网络密度的非方向性关键参数，可从定向性指标 P10 通过 C31 系数解析转换求得 [Gottron 2021, pp. 3-4]。
3. RQD 值对采样方向敏感，在用其作为岩体分类的输入指标时，应结合可能的范围或概率分布处理其不确定性 [Gottron 2021, pp. 4-5]。

## Candidate Concepts

- [[Discrete Fracture Network (DFN)]]
- [[rock mass classification]]
- [[Upscaling in fractured media]]
- [[Oda Geomechanics Method]]
- [[Pij system]]
- [[Rock Quality Designation (RQD)]]
- [[Rock Mass Rating (RMR)]]
- [[Geological Strength Index (GSI)]]
- [[Terrestrial Laser Scanning (TLS) for geomechanics]]

## Candidate Methods

- [[Monte Carlo Simulation for rock mass property estimation]]
- [[DFN-based Oda upscaling]]
- [[P10 to P32 conversion]]
- [[Empirical estimation of deformation modulus from RMR]]
- [[Vertical Transverse Isotropy (VTI) assumption in rock masses]]

## Connections To Other Work

- 索引片段中提及了升级和 DFN 相关的先前工作，如 Oda et al.（1984）开发的岩土力学方法 [Gottron 2021, pp. 2-3, 8-9]，Priest and Hudson（1976）的 RQD 关系 [Gottron 2021, pp. 4-5]，以及 Bieniawski（1973, 1989）的 RMR 系统 [Gottron 2021, pp. 4-5]。
- 研究流程可连接到 [[fracture reservoir]] 的水力-力学特性耦合研究，以及任何涉及从裂隙几何统计到等效连续体属性转换的主题。候选方法如 [[Representative Elementary Volume (REV) analysis]] 和 [[Stochastic fracture modeling]]。

## Open Questions

- 未从索引片段中确认 DFN 模型升级结果对裂隙尺寸分布的敏感性，特别是大尺度裂隙（“桥接”效应）对弹性属性的影响。
- 研究采用的垂直横向各向同性假设对含倾斜优势裂隙组的岩体的适用性未被评估。
- 未从索引片段中确认不同网格分辨率（50 m 单网格 vs. 5 m 多网格）对升级结果离散性的影响被详细讨论。

## Source Coverage

本页依据论文索引的 **19个片段** 生成。覆盖了论文的 **摘要、引言、方法（数据采集、DFN建模、升级、经验关系）、部分研究区域描述、部分实验结果和主要建模步骤**。内容主要集中在研究框架、数据来源和处理方法上。**缺失部分** 包括：
- 详细的模型验证结果数据。
- DFN 与经验关系比较的具体定量结果（如变形模量的对比图、表）。
- 参数敏感性分析（18个模型）的详细结果。
- 讨论部分和最终结论的完整细节。
因此，本页对**方法和条件**的覆盖较好，但对**具体结果和数值证据**的覆盖存在缺失。
