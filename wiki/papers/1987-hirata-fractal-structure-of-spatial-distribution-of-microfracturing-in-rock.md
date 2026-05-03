---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1987-hirata-fractal-structure-of-spatial-distribution-of-microfracturing-in-rock"
title: "Fractal Structure of Spatial Distribution of Microfracturing in Rock."
status: "draft"
source_pdf: "data/papers/1987 - Fractal structure of spatial distribution of microfracturing in rock.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Hirata, Takayuki, et al. \"Fractal Structure of Spatial Distribution of Microfracturing in Rock.\" *Geophys. J. R. astr. SOC.*, vol. 90, 1987, pp. 369-374."
indexed_texts: "4"
indexed_chars: "15854"
nonempty_source_blocks: "4"
compiled_source_blocks: "4"
compiled_source_chars: "15696"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990034"
coverage_status: "full-index"
source_signature: "4a850e3bc28adf93e4f578a803ea87bd680c7874"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:59:28"
---

# Fractal Structure of Spatial Distribution of Microfracturing in Rock.

## One-line Summary
在恒定应力蠕变实验中，Oshima花岗岩的声发射震源空间分布具有分形结构，其分形维数随岩石破裂演化而降低，暗示可能通过分形维数的减小预测大地震的发生。

## Research Question
微破裂的空间分布是否也表现出与地震空间分布类似的分形行为？[Hirata 1987, pp. 1-3]

## Study Area / Data
- **实验样品**：Oshima花岗岩圆柱体试样，直径50 mm，长100 mm，端面平行度在±0.005 mm以内；真空干燥后在室内环境放置超过2个月。[Hirata 1987, pp. 3-5]
- **实验条件**：围压40 MPa，差应力恒定在547 MPa（约为恒定应力速率试验所得破裂强度的85%），蠕变过程中轴压波动小于±0.1%，围压波动小于±0.2%。[Hirata 1987, pp. 1-3]
- **声发射数据**：用20个PZT换能器（谐振频率2 MHz）检测声发射，共定位2064个事件。根据蠕变应变曲线划分为三个阶段：
  - 初始蠕变（0–4410 s）：353个事件
  - 稳态蠕变（4410–15210 s）：273个事件
  - 加速蠕变（15210–22410 s）：1438个事件[Hirata 1987, pp. 3-5]
- **定位精度**：震源定位误差在±2 mm以内。P波速度测量同时考虑了平行和垂直于加载轴方向的各向异性。[Hirata 1987, pp. 3-5]

## Methods
- **关联积分（correlation integral）**：计算三维震源分布的关联积分 C(r) = (2 / N(N-1)) * Nr(R < r)，其中Nr是距离小于r的点对数。若分布具有分形结构，则 C(r) ∝ r^D，D为关联维数。该方法相比盒计数法对少量数据更稳定。[Hirata 1987, pp. 3-5]
- **震源对方向分析**：将震源对 (pi, pj) 构成的向量投影到上半球等面积投影上，分析方向分布的聚类变化。[Hirata 1987, pp. 3-5]

## Key Findings
1. **空间分形结构**：三个蠕变阶段的关联积分在对数坐标上均为直线，表明声发射震源的空间分布具有分形结构。分形维数分别为：初始蠕变 2.75，稳态蠕变 2.66，加速蠕变 2.25。[Hirata 1987, pp. 3-5]
2. **维数降低与聚类趋势**：分形维数从3（随机分布）降低，表明震源在空间中趋向形成自相似聚类结构。[Hirata 1987, pp. 5-6]
3. **与地震分形维数的可比性**：三维分形集在平面截口上的维数一般为 D-1，因此声发射震源平面截口的分形维数在 1.75 至 1.25 之间，与板内地震震中的分形维数（1.0–1.6）大致吻合，暗示微破裂与地震的尺度不变性。[Hirata 1987, pp. 5-6]
4. **方向聚类**：随蠕变进展，震源对的方向分布也趋于聚类，聚类形式为体积型（具有若干聚类中心）而非平面型。[Hirata 1987, pp. 3-5]
5. **与b值的关系**：未观察到分形维数D与震级-频度关系中的b值存在相关性，尽管b值在破坏前也有下降趋势，但 D 在实验室尺度上对预测主破裂似乎比b值更敏感。[Hirata 1987, pp. 5-6]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 声发射震源空间分布在蠕变各阶段均遵循 C(r) ∝ r^D | [Hirata 1987, pp. 3-5, Fig. 3] | 围压40 MPa，恒定差应力547 MPa，Oshima花岗岩 | 分形维数从2.75→2.66→2.25 |
| 分形维数降为2.25时对应加速蠕变阶段 | [Hirata 1987, pp. 3-5] | 同上 | 聚类增强，预示宏观破裂 |
| 平面截口维数（D-1）与板内地震震中维数一致 | [Hirata 1987, pp. 5-6] | 假设三维分形集平面截口维数为D-1 | 支持尺度不变性 |
| 震源对方向分布趋向体积型聚类 | [Hirata 1987, pp. 3-5, Fig. 4] | 同一实验 | 与单轴蠕变试验结果一致（Yanagidani et al., 1985） |
| D与b值无显著相关，D对主破裂更敏感 | [Hirata 1987, pp. 5-6] | 实验室声发射幅值得出b值 | 实验室局限可能导致此现象 |

## Limitations
- 数据点数在个别阶段较少（如稳态蠕变仅273个事件），可能影响关联积分估计的稳定性，但关联积分方法本身对少量数据较为鲁棒。[Hirata 1987, pp. 3-5]
- 实验室试样尺寸有限，震源定位精度为±2 mm，可能对短距离关联积分的影响较大。
- 作者指出 D 比 b 值对预测更敏感“可能源自实验室实验的不足”，具体不足未被详细说明。[Hirata 1987, pp. 5-6]

## Assumptions / Conditions
- 假设微破裂过程与大地震的破裂过程具有尺度不变性，可将实验室结果外推到天然地震。[Hirata 1987, pp. 5-6]
- 分形分析基于关联积分方法，其维数（关联维数）是Hausdorff维数的下限。[Hirata 1987, pp. 3-5]
- 震源定位时考虑了应力下P波速度各向异性，假设定位算法与地震定位算法原理相同。[Hirata 1987, pp. 3-5]
- 平面截口维数取 D−1，基于Mandelbrot (1983) 的一般性结论。[Hirata 1987, pp. 5-6]

## Key Variables / Parameters
- 分形维数 D（关联维数）
- 蠕变阶段（时间间隔）
- 差应力（547 MPa，恒定）与围压（40 MPa）
- 声发射事件数（N）
- 关联积分中的距离尺度 r（mm）
- 震源对方向分布（矢量方向聚类程度）
- b值（震级-频度关系的斜率）

## Reusable Claims
1. **在恒定应力蠕变条件下，岩石声发射震源的空间分布可用关联积分揭示出分形结构，且分形维数随破裂演化单调下降。** 具体地，Oshima花岗岩在围压40 MPa、差应力547 MPa时，维数从初始蠕变的2.75降至加速蠕变的2.25。该声明的条件为：三轴蠕变，差应力恒定，使用20个换能器进行声发射定位，定位精度±2 mm以内；局限性在于实验仅针对一种岩石类型和一种应力条件。[Hirata 1987, pp. 3-5]
2. **分形维数 D 的下降可视为岩石加速破裂、形成宏观破坏面的前兆指标，在实验室尺度下其对主破裂的敏感性可能优于b值。** 条件是：在蠕变实验中，主破裂前 D 的降低伴随震源的体积型聚类；但实验室实验可能存在未指明的不足，导致 D 与 b 不相关，且 D 更敏感。[Hirata 1987, pp. 5-6]
3. **微破裂空间分布的分形维数（三维）平面截口值为 1.25–1.75，与板内地震震中分形维数 1.0–1.6 大致相当，支持从厘米级微破裂到千米级地震的尺度不变破裂模式。** 条件是取平面截口维数近似为 D−1，且地震震中数据来自其他研究（Kagan & Knopoff 1980; Sadovskiy et al. 1984）。[Hirata 1987, pp. 5-6]

## Candidate Concepts
- [[fractal]]
- [[fractal dimension]]
- [[correlation integral]]
- [[acoustic emission]]
- [[creep]]
- [[primary creep]]
- [[secondary creep]]
- [[tertiary creep]]
- [[stochastic self-similarity]]
- [[hypocenter distribution]]
- [[earthquake prediction]]
- [[scale invariance]]
- [[b-value]]
- [[Gutenberg-Richter relationship]]

## Candidate Methods
- [[correlation integral method]]
- [[hypocenter location]]
- [[box-counting algorithm]]
- [[acoustic emission monitoring]]
- [[constant stress creep experiment]]

## Connections To Other Work
- **Mandelbrot (1967, 1983)**：提出分形概念，指出海岸线、岩石表面等具分形特征。本研究基于其关于分形为岩石破裂过程的假设。[Hirata 1987, pp. 1-3]
- **Brown & Scholz (1985)**：证明岩石节理、断层表面的几何形态为分形，揭示了破裂表面的分形特征。[Hirata 1987, pp. 1-3]
- **Kagan & Knopoff (1978, 1980, 1981)**：证明地震时间序列和空间分布具有随机自相似性，震中分形维数在1～1.5之间。本研究获得的平面截口维数与此一致。[Hirata 1987, pp. 1-3, 5-6]
- **Sadovskiy et al. (1984)**：用盒计数法得出世界范围地震分形维数1.6，Nurek地区地震1.4。本研究声发射的平面维数与之吻合。[Hirata 1987, pp. 1-3, 5-6]
- **Ouchi & Uekawa (1986)**：发现大地震前地震聚类程度增加，本研究从微破裂尺度提供了支持。[Hirata 1987, pp. 5-6]
- **Yanagidani et al. (1985)**：Oshima花岗岩单轴蠕变试验中，膨胀局部化呈体积型聚类，本研究方向分析结果与之吻合。[Hirata 1987, pp. 3-5]

## Open Questions
- 分形维数D与b值之间的确切关系如何？在本文实验中未能观察到两者的相关性，但b值亦呈现破坏前下降趋势，其物理机制和不同条件下的表现尚需进一步研究。[Hirata 1987, pp. 5-6]
- 实验室条件下，分形维数D对主破裂预测的敏感性高于b值，这一现象是否源自实验室实验的局限性（例如试样尺寸、加载方式）？若将方法外推至天然地震目录，D能否保持类似敏感度？[Hirata 1987, pp. 5-6]
- 声发射震源分形结构的形成机制：为何裂缝会自组织成具有特定分形维数的空间格局？其与岩石内部非均质性、应力场演化的定量关系尚不明确。

## Source Coverage
所有非空索引片段均已处理。共4个源块，涵盖原文 15696 个字符（覆盖率 0.99）。片段覆盖论文的摘要、引言、实验描述、方法、结果分析及讨论部分，确保了关键证据的完整提取。
