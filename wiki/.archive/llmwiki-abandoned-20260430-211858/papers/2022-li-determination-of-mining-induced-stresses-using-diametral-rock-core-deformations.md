---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-li-determination-of-mining-induced-stresses-using-diametral-rock-core-deformations"
title: "Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations."
status: "draft"
source_pdf: "data/papers/2022 - Determination of mining-induced stresses using diametral rock core deformations.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations.\" *International Journal of Coal Science & Technology*, vol. 9, article 80, 2022. doi:10.1007/s40789-022-00549-2. Accessed 25 Mar. 2026."
indexed_texts: "7"
indexed_chars: "31884"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:03:09"
---

# Determination of Mining-Induced Stresses Using Diametral Rock Core Deformations.

## One-line Summary
该研究提出并验证了一种通过测量实验室中勘探岩芯的直径变形来分析采矿诱发局部主应力差及脆性剪切比（Brittle Shear Ratio, BSR）的实用方法 [Li 2022, pp. 1-2]。

## Research Question
如何利用从地下矿山钻取的勘探岩芯，发展一种简单且实用的方法来确定由于采矿活动引起的局部地应力（尤其是垂直于岩芯轴平面上的主应力差）？ [Li 2022, pp. 1-2]

## Study Area / Data
- **案例研究1：Fraser矿山**：岩芯样本来自三个不同的钻孔，位于地表以下约1340米（4400英尺）。覆岩压力估算为37.5 MPa。样本钻孔使用了AQTK和NQ钻头尺寸，涉及岩石类型包括花岗岩（Granite）、长英片麻岩（Felsic Gneiss）、萨德伯里角砾岩（Sudbury Breccia）和马塔切万辉绿岩（Matachewan Diabase） [Li 2022, pp. 5, 7]。
- **案例研究2：Hoyle Pond矿山**：岩芯样本来自两个钻孔（编号25947和25986），提取深度在1357米至1840米之间，均使用NQ钻头。覆岩压力分别估算为36.6 MPa和49.7 MPa。共测量了19个样本 [Li 2022, pp. 7-8]。
- **样本深度范围**：研究中使用的岩石样本从地表以下1.3至1.8公里处获取 [Li 2022, pp. 2-3]。

## Methods
1. **岩芯直径变形测量**：使用定制的高精度测量设备，测量由于应力解除引起的岩芯最大直径（d_max）和最小直径（d_min）及其方向 [Li 2022, pp. 1-2]。
    - 基于敏感性分析，要求测量设备的分辨率不低于 ± 0.0001 mm，以确保主应力计算误差在 ±3% 以内 [Li 2022, pp. 4-5]。
    - 测量装置包含间隙可调的滚轮对，以适应不同的岩芯尺寸（AQTK， BQ / NQ， HQ / PQ） [Li 2022, pp. 5-7]。
2. **岩石力学性质测试**：依据ASTM D7012标准，进行单轴抗压强度（UCS）测试，采用液压伺服控制单轴压力机和数据采集系统，以确定岩石的杨氏模量（E）和泊松比（ν） [Li 2022, pp. 5-6]。
3. **应力分析模型**：采用Funato and Ito (2017) 提出的基于线弹性、各向同性、均质、连续体假设的解析模型，该模型关联了岩芯直径变化与局部主应力场。由于只有一个方程，该方法只能确定平面内的主应力差 `σ_H - σ_h` 及主方向，无法确定单个主应力的绝对值 [Li 2022, pp. 2-3]。
4. **脆性剪切比（BSR）分析**：利用计算得到的主应力差结合完整岩石的单轴抗压强度（UCS_intact）来评估岩体损伤和岩爆风险。BSR等级标准参考了 Castro et al. (2012) 的划分表 [Li 2022, pp. 10-12]。

## Key Findings
- **差应力计算**：Fraser矿山案例中，一个萨德伯里角砾岩样本（441034-SDBX-84）的差应力计算结果为31.3 MPa [Li 2022, pp. 7]。
- **差应力与深度关系**：在Hoyle Pond矿山案例中，通过分析10个样本的差应力与深度（43-50 m）数据，发现差应力往往随深度增加而增加 [Li 2022, pp. 10-11]。
- **案例对比**：Hoyle Pond矿山案例（案例2）中岩芯直径差（d_max - d_min）的平均范围（0.013–0.058 mm）高于Fraser矿山案例（案例1），表明案例2中的主应力差异更大 [Li 2022, pp. 8, 10]。
- **测量精度影响**：敏感性分析表明，计算出的最小主应力值对测量分辨率比最大主应力更敏感。0.0001 mm的分辨率比0.00025 mm的分辨率能显著减小差应力计算的最大误差（从大于5%降至小于2.3%） [Li 2022, pp. 4-5]。
- **BSR应用条件**：在加拿大矿山，基于加拿大盾构应力数据库，垂直应力通常小于两个水平应力。当岩芯取自远离开挖面区域时（即`σ_z > σ_y`），由岩芯直径变形获得的`σ_H`和`σ_h`即可视为主应力`σ_1`和`σ_3`，可直接用于计算差应力与BSR [Li 2022, pp. 11-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 对于测量分辨率0.00025 mm，差应力计算的最大误差超过5%；对于0.0001 mm分辨率，最大误差小于2.3%。 | [Li 2022, pp. 4-5] | 基于对d_max和d_min设定±0.00025 mm和±0.0001 mm公差的敏感性分析案例。 | 结论建议采用不低于±0.0001 mm的测微仪器分辨率。 |
| 案例研究1中，样本441034-SDBX-84的差应力为31.3 MPa。 | [Li 2022, pp. 7] | 样本为萨德伯里角砾岩，NQ钻头尺寸，d_max=47.6139 mm, d_min=47.5921 mm。岩石弹性模量和泊松比由UCS测试获得。 | 方法可以得到具体的差应力数值。 |
| 案例研究2中，差应力在43米深处为33.82 MPa，在50米深处为58.69 MPa，显示出随深度增加的趋势。 | [Li 2022, pp. 10] | 来自Hoyle Pond矿山钻孔ID: 24986的10个样本数据。 | 差应力数值在33.82 MPa到90.81 MPa之间波动，但整体趋势上升。 |
| BSR > 0.7 时，对应“Major”级别的岩体损伤和“Major”的应变型岩爆（strain bursting）可能性。 | [Li 2022, pp. 11] | 证据来自引用的Castro et al. (2012) 的BSR分级表。 | 该表用于根据计算的BSR值评估现场风险。 |

## Limitations
- **测量需求苛刻**：该方法要求极高的直径测量精度（±0.0001 mm），在现场或简易实验室条件下可能难以达到 [Li 2022, pp. 4-5]。
- **信息不完整**：该方法基于线弹性解析模型，仅能确定平面内的主应力差和主方向，无法获得单个主应力的绝对值或远场应力状态 [Li 2022, pp. 2-3]。
- **岩芯条件假设**：分析模型基于线弹性、各向同性、均质和连续岩石的假设，这些假设在实际非均质、各向异性或破碎岩体中可能不成立 [Li 2022, pp. 2-3]。
- **物理因素干扰**：测量到的NQ岩芯直径明显小于其标准尺寸（47.6 mm），这可能是钻探过程中的材料损失造成的，可能影响结果的准确性 [Li 2022, pp. 10]。
- **特定应力假设**：直接利用差应力计算BSR来评估岩体风险，依赖于岩芯轴平行于一个现场主应力（如在远离巷道自由面的钻探）且垂直应力小于水平应力的特殊工况 [Li 2022, pp. 11-12]。

## Assumptions / Conditions
- **岩石本构模型**：应用Funato and Ito (2017) 的解析模型，假设岩石为线弹性、各向同性、均质且连续 [Li 2022, pp. 2-3]。
- **测量条件**：能够准确测量岩芯从钻孔取出后的最大和最小直径（d_max, d_min）及其对应的方向 [Li 2022, pp. 2-3]。
- **应力条件**：在计算BSR并用于岩体稳定性分析时，设定了一个特殊情况：岩芯轴平行于一个现场主应力，从而使岩芯横截面上的应力即为其余两个主应力 [Li 2022, pp. 2, 11-12]。
- **岩芯芯轴方向**：分析的应力所在的平面垂直于提取的岩芯轴 [Li 2022, pp. 1-2]。

## Key Variables / Parameters
- 岩芯最大和最小直径 (`d_max`, `d_min`) [Li 2022, pp. 2-3]
- 杨氏模量 (`E`) 和 泊松比 (`ν`) [Li 2022, pp. 2-3]
- 局部主应力差 (`σ_H − σ_h`) [Li 2022, pp. 2-3]
- 单轴抗压强度 (`UCS_intact`) [Li 2022, pp. 10-11]
- 脆性剪切比 (`BSR`) [Li 2022, pp. 10-11]
- 测量仪器分辨率（关键要求：不低于±0.0001 mm） [Li 2022, pp. 4-5]
- 深度（用于分析差应力与深度的关系） [Li 2022, pp. 2-3, 10]

## Reusable Claims
- **精度要求**：利用岩芯直径变形进行应力分析时，为保证差应力计算误差在3%以内，直径测量设备的分辨率必须不低于±0.0001 mm [Li 2022, pp. 4-5]。
- **方法局限性**：基于岩芯直径变形解析模型的方法只能恢复垂直于钻孔轴平面上的差应力（`σ_H - σ_h`）及其主方向，不能确定单个主应力的大小 [Li 2022, pp. 2-3]。
- **应用场景**：该方法可应用于地下矿山勘探过程中获取的岩芯，计算出差应力，进而结合UCS计算BSR，作为硬岩矿山岩体脆性破坏风险的评估指标 [Li 2022, pp. 1, 10-11]。
- **应力与深度关系**：在特定矿山案例中（Hoyle Pond Mine），由该方法测得的采矿诱发差应力表现出随深度增加而增大的趋势 [Li 2022, pp. 10]。
- **BSR风险评估**：基于Castro et al. (2012) 标准，当BSR大于0.7时，预示着存在“Major”级别的岩体损伤和高应变型岩爆可能性 [Li 2022, pp. 10-11]。

## Candidate Concepts
- [[Mining-induced stresses]]
- [[In-situ stress measurement]]
- [[Strain relief]]
- [[Diametral core deformation analysis]]
- [[Brittle shear ratio (BSR)]]
- [[Strainburst prediction]]
- [[Core disking]]

## Candidate Methods
- [[Diametral rock core deformation method]]
- [[Uniaxial Compressive Strength test (UCS)]]
- [[Core-based stress measurement]]
- [[Overcoring stress measurement]]
- [[ASTM D7012]]

## Connections To Other Work
- 本研究的应力分析解析模型直接基于 **Funato and Ito (2017)** [Li 2022, pp. 2-3]。
- 岩体损伤与应变型岩爆的可能性分级标准引用了 **Castro et al. (2012)** 的BSR分级表 [Li 2022, pp. 11]。
- 该方法可与[[Overcoring]]、[[Hydraulic fracturing]]等其他地应力测量方法在适用条件和能力（如获取完整应力张量 vs. 仅获取差应力）上进行比较。未从索引片段中确认与其他方法的具体对比关系。

## Open Questions
- 如何量化和校正钻探过程中的材料损失及其他因素对岩芯直径测量结果的影响？ [Li 2022, pp. 10]
- 该方法是否适用于高度各向异性、非均质或裂隙发育的岩体？当前模型假设基于线弹性、各向同性、均质和连续岩石 [Li 2022, pp. 2-3]。
- 如何将这种仅能提供二维差应力的测量结果更广泛地应用到不满足“岩芯轴平行于一个主应力”这一特殊条件的普遍工况中？ [Li 2022, pp. 11-12]

## Source Coverage
本页面基于该论文的7个索引片段生成。片段覆盖了论文的引言、方法原理、实验装置设计、敏感性分析、两个案例研究的描述与结果、以及讨论与结论部分。覆盖度相对全面，但缺少对方法论更深层的数学推导细节、完整的数据表以及文中未提供的参考文献内容。摘要部分对核心结论有较好总结。
