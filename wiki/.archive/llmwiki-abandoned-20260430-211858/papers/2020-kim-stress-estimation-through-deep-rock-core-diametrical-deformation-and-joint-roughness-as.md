---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-kim-stress-estimation-through-deep-rock-core-diametrical-deformation-and-joint-roughness-as"
title: "Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging."
status: "draft"
source_pdf: "data/papers/2020 - Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.pdf"
collections:
  - "zotero new"
citation: "Kim, Hanna, et al. \"Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.\" *Sensors*, vol. 20, no. 23, 2020, article 6802. doi:10.3390/s20236802."
indexed_texts: "11"
indexed_chars: "50552"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:36:52"
---

# Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.

## One-line Summary
利用X射线CT成像分析4.2km深部花岗闪长岩岩心的直径变形，估算水平差应力约为13.3MPa，并发现节理最小粗糙度方向与最大水平主应力方向之间存在关联 [Kim 2020, pp. 1-2, pp. 7-8]。

## Research Question
- 能否通过深部岩心直径变形分析（DCDA）方法可靠地估算地应力 [Kim 2020, pp. 2-3]？
- 节理粗糙度的各向异性是否与地应力方向存在相关性，从而可作为应力方向的潜在指标 [Kim 2020, pp. 1-2, pp. 7-8]？

## Study Area / Data
- **地点**：韩国浦项增强型地热系统（EGS）项目场地，PX-2井 [Kim 2020, pp. 3-4]。
- **样本**：取自地下4219m深处，直径100mm的花岗闪长岩岩心样本 S-IX-3，内含一条倾角80.8°的闭合节理(CJ-2) [Kim 2020, pp. 1-2, pp. 3-4]。
- **参考数据**：附近4km外的EXP-1勘探井有水力压裂等地应力数据 [Kim 2020, pp. 4-4]。韩国政府委员会关于2017年浦项地震与EGS项目的报告提供了该深度的应力模型 [Kim 2020, pp. 4-4]。

## Methods
1. **直径变形测量**：使用工业X射线CT扫描岩心样本S-IX-3，生成垂直于取心方向的横截面切片。利用ImageJ软件对CT切片进行二值化和椭圆拟合处理，测量岩心扩张后的最大直径(dmax)和最小直径(dmin) [Kim 2020, pp. 4-6, pp. 6-7]。
2. **差应力估算 (DCDA方法)**：基于Funato和Ito [9]提出的方法，假设应力解除引起的直径变形为弹性变形，使用公式 `S_max - S_min = (E / (1 + ν)) * (d_max - d_min) / d_min` 计算水平差应力，其中E为杨氏模量，ν为泊松比 [Kim 2020, pp. 4-6]。
3. **节理粗糙度评估**：根据Diaz等人[18]的方法，对闭合节理CJ-2在相对平面上每隔10°进行多平行截面测量，计算各方向的节理粗糙度系数(JRC)均值，并通过椭圆拟合确定最大(JRC_max)和最小(JRC_min)粗糙度方向 [Kim 2020, pp. 7-8]。
4. **方向对比**：将JRC_max和JRC_min方向投影至水平面，与DCDA得到的d_max（即最大水平应力S_Hmax）和d_min方向进行对比 [Kim 2020, pp. 7-8]。

## Key Findings
- **差应力估算**：基于直径变形测量，水平差应力(S_max - S_min)估算范围在8.6 MPa至17.2 MPa之间，基于平均直径的差应力结果为**13.3 MPa**。此结果与附近EXP-1勘探井的报告值相似 [Kim 2020, pp. 1-2, pp. 6-7]。
- **粗糙度各向异性与应力方向的关联**：观测到JRC_min（最小节理粗糙度系数）方向与d_max（最大直径变形，代表S_Hmax）方向存在对齐（alignment）现象 [Kim 2020, pp. 7-8]。这表明最大水平主应力方向可能与节理面上最低粗糙度的方向相关 [Kim 2020, pp. 1-2, pp. 7-8]。
- **粗糙度方向结果**：闭合节理CJ-2的JRC_max和JRC_min方向在节理相对平面上互为垂直，分别为154.6°和64.6°（从水平参考线逆时针测量）[Kim 2020, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 水平差应力估算为13.3 MPa（范围8.6-17.2 MPa） | [Kim 2020, pp. 6-7] | 使用样本S-IX-3，弹性模量33.5 GPa，泊松比0.21。假设弹性变形。 | 结果与附近EXP-1勘探井的值相似 |
| JRC_min方向与d_max方向存在对齐 | [Kim 2020, pp. 7-8] | 针对倾角80.8°的闭合节理CJ-2进行JRC测量。 | 提出节理粗糙度各向异性可能追踪应力方向 |
| 样本中闭合节理CJ-2的倾角为80.8° | [Kim 2020, pp. 1-2] | 样本S-IX-3 | 节理方向与垂直取心方向的夹角 |
| 岩心取自4.2km深度的花岗闪长岩 | [Kim 2020, pp. 3-4] | 浦项EGS场地，PX-2井 | 力学性质由Kwon等人[17]测定 |
| 差应力计算公式为 `S_max - S_min = (E / (1 + ν)) * (d_max - d_min) / d_min` | [Kim 2020, pp. 4-6] | 由Funato和Ito [9]提出，假设小变形，用d_min替代原始直径d0。 | DCDA方法的核心公式 |
| JRC_max和JRC_min方向在节理相对平面上互相垂直 | [Kim 2020, pp. 7-8] | 样本S-IX-3，节理CJ-2 | 椭圆拟合相关系数为0.98 |

## Limitations
- 本研究基于单一样本（S-IX-3），其通用性未从索引片段中确认 [Kim 2020, pp. 3-4]。
- DCDA方法假设岩心为均质、各向同性且发生弹性变形，但文中指出花岗岩类通常存在物理各向异性，且此特性未在本批岩心中进行研究 [Kim 2020, pp. 3-4, pp. 4-6]。
- 差应力估算值范围较大（8.6-17.2 MPa），反映了直径测量的不确定性 [Kim 2020, pp. 6-7]。
- 关于粗糙度与应力方向关联的讨论，是基于观测到的“对齐”现象，但未从索引片段中确认其因果机制的直接证据，且引用的Barton等人[28]的研究显示高差应力下形成更光滑的节理（低JRC），并未直接估计差应力对粗糙度各向异性的影响 [Kim 2020, pp. 7-8]。
- 文中未将估算应力与更直接的本地应力测量数据（如PX-2井自身的水力压裂数据）进行对比验证，只与4km外的EXP-1井数据和政府报告模型进行了比较 [Kim 2020, pp. 4-4, pp. 6-7]。

## Assumptions / Conditions
- **核心假设**：岩石在应力解除后发生的直径变形是线弹性的，且各向同性 [Kim 2020, pp. 1-2, pp. 4-6]。
- **实验条件**：
    - 岩心垂直提取，取心方向与水平主应力方向垂直 [Kim 2020, pp. 4-6]。
    - 直径测量在无荷载条件下进行，用CT扫描图像分析 [Kim 2020, pp. 4-6]。
    - CT扫描时，样本垂直对齐以保证每个横截面都垂直于取心方向 [Kim 2020, pp. 4-6]。
- **方法前提**：由于应力接触导致的变形较小，在公式中可用d_min代替原始直径d0 [Kim 2020, pp. 4-6]。

## Key Variables / Parameters
- **关键参数**：
    - `d_max`（扩张后最大直径）[Kim 2020, pp. 6-7]
    - `d_min`（扩张后最小直径）[Kim 2020, pp. 6-7]
    - `E`（杨氏模量，33.5 GPa）[Kim 2020, pp. 3-4, pp. 6-7]
    - `ν`（泊松比，0.21）[Kim 2020, pp. 3-4, pp. 6-7]
- **关键变量**：
    - `S_max - S_min`（水平差应力）[Kim 2020, pp. 4-6]
    - `JRC_max` / `JRC_min`（节理粗糙度系数最大值/最小值）方向 [Kim 2020, pp. 7-8]
- **控制因素**：未从索引片段中确认。

## Reusable Claims
- **Claim 1**：对于深部（~4.2km）花岗闪长岩岩心，直径岩心变形分析（DCDA）结合X射线CT扫描，可以为水平差应力提供一个数值范围（本例中为8.6 MPa至17.2 MPa，均值13.3 MPa）。[来源：Kim 2020, pp. 6-7] **条件**：此估算基于弹性变形假设，并使用该区域岩石的特定弹性模量（33.5 GPa）和泊松比（0.21）。**限制**：该值未与同井的直接应力测量数据对比验证，且花岗岩的各向异性未被考虑。
- **Claim 2**：在某些节理面上，最小节理粗糙度系数（`JRC_min`）的方向可能与最大水平主应力（`S_Hmax`）的方向存在对齐关系。[来源：Kim 2020, pp. 7-8] **证据**：在分析的单一闭合节理样本中观测到该现象。**条件**：该关系是在一个倾角为80.8°的闭合节理上发现的。**限制**：此观测基于孤例，其形成机制的因果关系（应力如何塑造各向异性）尚未被证明。

## Candidate Concepts
- [[in-situ stress estimation]]
- [[Deep Rock Core]]
- [[Diametrical Core Deformation Analysis (DCDA)]]
- [[Joint Roughness Coefficient (JRC)]]
- [[anisotropy]]
- [[stress relief]]
- [[Enhanced Geothermal System (EGS)]]
- [[X-ray computed tomography (CT)]]

## Candidate Methods
- [[Diametrical Core Deformation Analysis (DCDA)]]
- [[X-ray CT Imaging for Deformation Measurement]]
- [[Joint Roughness Assessment using Parallel Cross Sections]]
- [[Ellipse Fitting for Anisotropy Analysis]]

## Connections To Other Work
- **Funato and Ito [9]**：首创了基于岩心直径弹性变形估算差应力的DCDA方法。本研究是对该方法的直接应用和探索性扩展，尝试用CT影像替代激光扫描进行测量 [Kim 2020, pp. 2-3, pp. 4-6]。
- **Kwon et al. [17]**：为浦项岩心提供了关键的力学参数（弹性模量和泊松比），本研究的差应力计算直接依赖这些参数 [Kim 2020, pp. 3-4, pp. 6-7]。
- **Diaz et al. [18]**：本研究中JRC测量和多截面取平均值的评估方法遵循了其提出的流程 [Kim 2020, pp. 7-8]。
- **Huang et al. [26]**：指出了节理剪切强度的各向异性及其对剪切方向的依赖性，为粗糙度与应力方向的关系提供了背景 [Kim 2020, pp. 7-8]。
- **Barton et al. [28]**：研究表明JRC随差应力增加而降低，即高差应力下倾向形成更光滑的节理。这与本研究发现低JRC方向可能与最大主应力方向对齐的现象存在概念上的联系 [Kim 2020, pp. 7-8]。
- **主题连接 (Candidate Connections)**：本研究主题可连接到其他应力测量方法，如 [[Hydraulic Fracturing]]、[[Kaiser Effect (Acoustic Emission)]]、[[Deformation Rate Analysis (DRA)]] 以及 [[Differential Strain Curve Analysis (DSCA)]]，这些在论文引言中均有提及并比较 [Kim 2020, pp. 2-3]。

## Open Questions
- 本研究仅在一个岩心样本上开展，在更多不同深度、不同岩性、不同节理类型的样本上进行类似观测，是否能确认节理粗糙度各向异性与应力方向之间的普遍关联？[推断自 Kim 2020, pp. 1-2, pp. 6-7 的单一样本限制]
- 最大水平主应力导致最小粗糙度方向的物理机制是什么？[推断自 Kim 2020, pp. 7-8 关于“应力引导剪切方向”的讨论]
- 能否利用此关联，在没有差应力绝对值的情况下，通过测量节理粗糙度各向异性来单独推断古应力或现今应力的方向？[推断自 Kim 2020, pp. 1-2 的研究目标]

## Source Coverage
本页面基于提供的11个片段中的信息创建，覆盖了论文的标题、摘要、引言、研究区域/数据、方法、结果和部分讨论（涵盖了约第1页至第8页）。由于未包含第8页之后及参考文献列表的片段，关于更详细的方法讨论、潜在的验证步骤、完整的结论以及未来工作展望等信息**缺失**。总体覆盖偏重于方法描述和主要结果，但对完整的讨论和结论部分覆盖不足。
