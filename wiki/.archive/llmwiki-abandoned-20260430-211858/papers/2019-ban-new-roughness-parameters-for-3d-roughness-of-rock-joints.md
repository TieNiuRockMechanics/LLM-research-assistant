---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-ban-new-roughness-parameters-for-3d-roughness-of-rock-joints"
title: "New Roughness Parameters for 3D Roughness of Rock Joints."
status: "draft"
source_pdf: "data/papers/2019 - New roughness parameters for 3D roughness of rock joints.pdf"
collections:
  - "zotero new"
citation: "Ban, Liren, et al. \"New Roughness Parameters for 3D Roughness of Rock Joints.\" *Bulletin of Engineering Geology and the Environment*, vol. 78, 2019, pp. 4505–17. doi:10.1007/s10064-018-1394-3."
indexed_texts: "9"
indexed_chars: "43038"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:29:10"
---

# New Roughness Parameters for 3D Roughness of Rock Joints.

## One-line Summary
本研究提出等效高度差系统及两个三维粗糙度参数 AHD 与 D\AHD，以联系节理面形态与剪切强度并反映各向异性 [Ban 2019, pp. 1-2]。

## Research Question
如何提出能够反映三维表面形态各向异性并与剪切强度有明确物理联系的岩石节理粗糙度参数系统 [Ban 2019, pp. 1-2]。

## Study Area / Data
研究使用五组尺寸为 200 × 100 mm 的节理面样本，利用三维激光扫描仪以 0.25 mm 扫描间隔获取表面离散点坐标，并由此生成三维表面图 [Ban 2019, pp. 2-4]。五组节理的最大高度从 27.5 mm 到 33.4 mm 不等，各自具有不同的几何分布特征 [Ban 2019, pp. 2-4]。用于验证的标准 JRC 剖面数据来源未从索引片段中确认。

## Methods
- **等效高度差概念**：将节理面形态等效为连续矩形凸起网格。考虑凸起的剪胀与非剪胀两种失效模式，提出等价高度差以区分不同几何参数对剪切强度的贡献 [Ban 2019, pp. 4-6]。
- **AHD 粗糙度参数**：沿剪切方向对等价高度差取平均得到平均等价高度差 (AHD)，计算公式涉及对行-列数据的处理及临界纵横比 m\c [Ban 2019, pp. 6-9]。
- **分形维数 D\AHD**：基于 AHD(δ) 与测量尺度 δ 之间呈现幂律关系，通过线性拟合 ln[AHD(δ)]-ln(δ) 获得具有向量特性的分形维数 D\AHD [Ban 2019, pp. 9-10]。
- **与 JRC 的关联**：将二维化后的 AHD0 与 D\AHD 参数与标准 JRC 剖面进行回归分析，得到关系式 JRC = 0.285(AHD0/D\AHD) + 1.047，R² = 0.98 [Ban 2019, pp. 10-12]。

## Key Findings
- **参数方向依赖性**：同一节理面在不同剪切方向得到的 AHD 值不同，可客观描述粗糙度的各向异性 [Ban 2019, pp. 6-9]。
- **分形特性与尺度稳定性**：AHD(δ) 与 δ 满足幂律关系，ln[AHD(δ)]-ln(δ) 呈高度线性相关；节理面在 0.25–3 mm 测量尺度范围内具有稳定的分形维数 [Ban 2019, pp. 9-10][Ban 2019, pp. 12-13]。
- **JRC 高匹配度**：提取的标准 JRC 数据与已有文献（Tse and Cruden 1979; Yu and Vayssade 1991; Yang et al. 2001）一致，且本系统得到的 AHD0 与 D\AHD 组合能高精度拟合 JRC 值 [Ban 2019, pp. 10-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 五个节理面在四个方向上 AHD 值不同（如节理面 1: 8.60/6.15/5.78/10.23） | [Ban 2019, pp. 6-9] Table 1 | 1 mm 采样间隔 | 证明 AHD 具有方向依赖性 |
| 五组节理面 ln[AHD(δ)]-ln(δ) 均呈高度线性分布，分形维数 D\AHD 在 2.031–2.152 之间 | [Ban 2019, pp. 9-10] Fig. 7, Table 2 | 0.25–3 mm 测量尺度范围 | 支持分形特性与尺度效应描述 |
| JRC = 0.285(AHD0/D\AHD) + 1.047 (R² = 0.98) | [Ban 2019, pp. 10-12] Fig. 9 | 二维退化至标准 JRC 剖面 | 新参数系统对二维 JRC 的定量拟合优度 |
| 参数 AHD 与临界纵横比 m\c 相关，而 m\c 与完整岩石材料性质有关 | [Ban 2019, pp. 10-12] | 提及但未深入分析 | 粗糙度参数可能受材料力学参数影响 |

## Limitations
- 等效高度差系统中涉及的临界纵横比 m\c 与完整岩石材料属性相关，这导致粗糙度参数可能不是纯粹的几何量，未从索引片段中确认对此有进一步系统分析 [Ban 2019, pp. 10-12]。
- 虽提及宽分级尺度范围内可能不严格满足幂律，但仅给出了推荐应用范围（0.25–3 mm），未从索引片段中确认是否评估了该尺度范围外或在非自仿射条件下的误差。
- 将三维参数退化至二维与 JRC 进行回归，未从索引片段中确认系统地进行了由新参数直接预测三维剪切强度的物理实验或现场验证。

## Assumptions / Conditions
- 节理凸起可被矩形网格等效，且凸起剪切时遵循剪胀失效和非剪胀失效两种模式 [Ban 2019, pp. 4-6]。
- 等效高度差计算依赖凸起临界纵横比 m\c 的判定，而 m\c 由完整岩石材料性质确定 [Ban 2019, pp. 10-12]。
- 分形维数 D\AHD 的提取基于形态在 0.25–3 mm 尺度范围内表现出分形特性，并采用最小二乘线性拟合 [Ban 2019, pp. 12-13]。

## Key Variables / Parameters
- **AHD** (平均等价高度差)：沿剪切方向定义的粗糙度参数 [Ban 2019, pp. 6-9]。
- **D\AHD** (分形维数)：基于 AHD(δ) 与测量尺度 δ 幂律关系的具有向量特性的分形参数 [Ban 2019, pp. 9-10]。
- **AHD0**：用于二维退化情况的截距参数 [Ban 2019, pp. 10-12]。
- **δ**：测量尺度 (采样间隔) [Ban 2019, pp. 9-10]。
- **m\c**：凸起临界纵横比，区分剪胀与非剪胀失效 [Ban 2019, pp. 4-6]。
- **h**, **l**: 凸起的高度与长度 [Ban 2019, pp. 4-6]。

## Reusable Claims
1. **岩石节理粗糙度参数 AHD 能反映剪切强度的各向异性**：参数 AHD 被定义为沿某一剪切方向的等价高度差的平均值，当剪切方向改变时数值不同。这一特性可望用于构建方向依赖的剪切强度方程。前提条件是节理表面被离散为矩形网格且已知临界纵横比 m\c [Ban 2019, pp. 6-9]。
2. **AHD(δ) 与测量尺度 δ 之间服从幂律，其分形维数 D\AHD 可在 0.25–3 mm 范围内描述多尺度粗糙度特性**：根据五个节理面的实验数据，ln[AHD(δ)]-ln(δ) 呈高度线性相关。D\AHD 能综合反映尺度效应且具有方向性，在该尺度范围内稳定 [Ban 2019, pp. 9-10][Ban 2019, pp. 12-13]。
3. **新粗糙度参数系统（AHD0 与 D\AHD）与 JRC 可建立高精度的定量关系**：将参数退化至二维标准 JRC1–10 剖面的条件下，回归得到 JRC = 0.285(AHD0/D\AHD) + 1.047 (R² = 0.98) [Ban 2019, pp. 10-12]。
4. **AHD 与岩石材料力学性质存在潜在联系**：因 AHD 中使用了与完整岩石材料性质相关的临界纵横比 m\c，故该粗糙度参数可能受到材料强度等因素的影响，但具体的定量关系未从索引片段中确认 [Ban 2019, pp. 10-12]。

## Candidate Concepts
- [[rock joint shear strength]]
- [[three-dimensional surface morphology]]
- [[joint roughness coefficient JRC]]
- [[fractal dimension]]
- [[equivalent height difference]]

## Candidate Methods
- [[equivalent height difference system]]
- [[rectangular asperity idealization]]
- [[AHD roughness parameter calculation]]
- [[power law and fractal analysis for roughness]]
- [[3D laser scanning for joint surfaces]]

## Connections To Other Work
- 本研究基于 JRC 方法（Barton and Choubry 1997; Barton and Quadros 1997）本身的局限（主观性、无法描述三维与方向依赖性），以及二维统计参数-分形维-JRC 方法（Tse and Cruden 1979; Lee et al. 1990; Maerz et al. 1990）等前期工作提出新参数系统 [Ban 2019, pp. 2-2]。
- 将退化至二维的结果与 Tse and Cruden (1979)、Yu and Vayssade (1991)、Yang et al. (2001) 所报道的标准 JRC 剖面数据进行一致性比较 [Ban 2019, pp. 10-12]。

## Open Questions
- AHD 粗糙度参数系统是否能够直接应用于预测三维岩石节理的剪切强度，并经过剪切实验验证，未从索引片段中确认。
- 临界纵横比 m\c 的选取如何影响不同完整岩石条件下 AHD 计算及后续剪切强度预测的灵敏性，未从索引片段中确认。
- 在 0.25–3 mm 推荐尺度范围外，该参数系统是否仍然稳定或可修正，未从索引片段中确认。

## Source Coverage
本页依据了 9 个索引片段，覆盖了摘要、方法设计、实验数据示例、主要公式和结果分析。部分重要基础信息（如第五部分讨论中可能涉及的更系统性的因素分析或实际验证）可能未被完整收录；有关标准 JRC 剖面具体来源的细节也未在片段中提供。
