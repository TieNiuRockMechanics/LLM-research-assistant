---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
title: "Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2023 - Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.pdf"
collections:
citation: "Yoon, Seonkyoo, et al. \"Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.\" 2023."
indexed_texts: "17"
indexed_chars: "83282"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "82565"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991391"
coverage_status: "full-index"
source_signature: "875e19e3816fc82a38d77350bdedea8971fb1628"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:24:33"
---

# Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.

## One-line Summary
本研究通过大规模三维离散裂隙网络模拟，证明死端裂隙的占比在逾渗阈值处达到最大，并由此引起最强的非菲克溶质拖尾，提出了一种基于图论的死端裂隙识别方法，并建立了死端裂隙密度与溶质运移非菲克行为之间的定量关系。

## Research Question
主要有两个问题：[Yoon 2023, pp. 2-3]
1. 裂隙密度如何控制死端裂隙的形成？
2. 死端裂隙在非菲克运移行为（尤其是溶质拖尾）中扮演什么角色？

## Study Area / Data
研究不针对特定场地，而是基于系统生成的三维离散裂隙网络（DFN）集合。计算域为边长15 m的立方体；裂隙为随机Poisson过程生成的圆盘状多边形（8顶点），半径服从截断幂律分布，下限1 m，上限5 m，衰减指数α取2.0、2.2、2.4；裂隙水力开度与半径通过正相关幂律关系关联；密度以逾渗阈值归一化，取ρ = [0.5, 1, 2, 4, 8]；每种α‑ρ组合生成15个实现，共225个裂隙网络。[Yoon 2023, pp. 2-4]

## Methods
- 裂隙网络生成：基于截断幂律长度分布和随机取向的泊松过程，并考虑边界缓冲区。开度与半径相关但不考虑面内开度非均质。[Yoon 2023, pp. 2-4]
- 逾渗阈值确定：对每种α，在10至500递增步长下生成50个实现，计算经验逾渗概率，并用误差函数拟合以获得临界数pc，进而定义归一化密度ρ = p/pc。[Yoon 2023, pp. 3-4]
- 死端裂隙识别：提出新的图论方法。将裂隙表示为节点，交切表示为边，引入源节点和目标节点。通过深度优先搜索将全图分解为双连通分量，其中移除后不割裂源‑目标节点的分量对应的节点集合即为死端裂隙。该方法全面优于传统的2‑核子图定义。[Yoon 2023, pp. 4-7, table 1]
- 流体与溶质运移模拟：使用dfnWorks，求解雷诺方程（∇·(b³∇P)=0），采用1 MPa压差边界，其余为无流边界；用PFLOTRAN有限体积法求解。仅考虑平流，在交叉点依据体积流量分配出流概率；注入10⁵个示踪粒子，通量加权初始位置。记录首达时间，并计算首次通过时间分布（FPTD），以孔隙体积（PV）无量纲化；在95%~99.99%分位数间线性回归获取尾部斜率。[Yoon 2023, pp. 7-8]

## Key Findings
1. 死端裂隙的相对面积（S_d）和数量在逾渗阈值（ρ = 1）处达到最大，之后随密度增加因连通性改善而下降。对应的溶质拖尾尾部斜率在此处最小（即尾最长），表现为最强的非菲克行为。[Yoon 2023, pp. 8-11]
2. 对比完整网络FPTD与去除死端裂隙后的骨架RTD，死端裂隙对溶质滞留时间的贡献在逾渗阈值处最大；随着密度增大，骨架RTD与FPTD几乎重合，表明死端裂隙的拖尾效应减弱。[Yoon 2023, pp. 11-12]
3. 死端裂隙面积与尾部斜率呈显著正相关（回归斜率2.37），且死端裂隙面积也与粒子轨迹平均迂曲度高度相关，说明死端裂隙不仅直接延迟运移，还能指示主运移路径的迂曲程度。[Yoon 2023, pp. 10-13]
4. 提出的基于双连通分量的死端裂隙定义较之2‑核子图定义更能捕捉死端裂隙的滞留效应：后者得到的骨架RTD与实际FPTD几乎无差异，而前者能显著减弱尾部。[Yoon 2023, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 死端裂隙总面积占比（S_d）在ρ=1时最大，随后下降 | [Yoon 2023, pp. 9-10, Fig.6a] | α=2.0,2.2,2.4；仅考虑连通裂隙；各组合15个实现 | 趋势不依赖于长度分布指数 |
| FPTD尾部斜率在ρ=1时最小（约0.5-1），非菲克，之后随ρ增大斜率增大，ρ≥4时接近菲克（斜率>3） | [Yoon 2023, pp. 8-9, Fig.5a] | 同上网络条件；平流；无扩散和基质 | 尾部斜率在95%~99.99%分位数间拟合 |
| 逾渗阈值处示踪粒子进入死端裂隙的比例最高 | [Yoon 2023, pp. 10-11, Fig.6b] | 粒子路径完整，死端裂隙由拓扑定义 | 比例曲线形状与死端面积一致 |
| 去除死端裂隙的骨架RTD尾部明显低于完整FPTD，尤其在ρ=1时差异最大 | [Yoon 2023, pp. 11-12, Fig.4, Fig.8] | 基于新定义死端裂隙；α=2.4示例 | 2‑核定义骨架RTD与FPTD几乎无差异 |
| 死端面积与尾部斜率正相关，回归斜率2.37 | [Yoon 2023, pp. 10-11, Fig.7] | 所有α和ρ组合数据点 | 说明死端面积可作为拖尾指标 |
| 粒子轨迹平均迂曲度在ρ=1时最大，且变化范围最宽 | [Yoon 2023, pp. 12-13, Fig.11] | 完整网络粒子轨迹 | 迂曲度趋势与死端面积趋势相似 |

## Limitations
- 未考虑裂隙面内开度非均质性，因此结论仅适用于面内变异性可忽略的情形。[Yoon 2023, pp. 3-4, 13-14]
- 仅模拟平流过程，未显式考虑分子扩散、基质扩散或吸附等迟滞机制。[Yoon 2023, pp. 7-8, 13-14]
- 基质假定为完全不渗透，忽略裂隙‑基质相互作用。尽管对于花岗岩等硬岩适用，但一般情形下可能重要。[Yoon 2023, pp. 7-8]
- 裂隙网络生成采用泊松过程和幂律分布，未涉及地质力学成因的裂隙演化，结论推广需验证。[Yoon 2023, pp. 2-3, 13-14]
- 扩散仅通过交叉点完全混合等效体现，未单独模拟扩散进入低流速区的过程。[Yoon 2023, pp. 13-14]

## Assumptions / Conditions
- 裂隙长度服从截断幂律分布，α∈{2.0,2.2,2.4}，下截半径1 m，上截半径5 m。[Yoon 2023, pp. 2-3]
- 裂隙开度b与半径r满足b = γ r^β，γ=5.0e-4，β=0.5，且面内均匀。[Yoon 2023, pp. 3-4]
- 裂隙方位均匀随机。[Yoon 2023, pp. 3]
- 流动为层流，用雷诺方程描述，基质不透水。[Yoon 2023, pp. 7-8]
- 溶质运移仅考虑平流；在交叉点按出流流量比例分配粒子。[Yoon 2023, pp. 7-8]
- 粒子注入方式为通量加权。[Yoon 2023, pp. 7]
- 死端裂隙定义为双连通分量中移除后不切断源‑目标路径的节点对应的裂隙。[Yoon 2023, pp. 5-7]
- 归一化密度ρ = p/pc，pc由逾渗概率拟合得到（∏_L(pc)=1/2）。[Yoon 2023, pp. 3-4]

## Key Variables / Parameters
- 归一化裂隙密度 ρ ∈{0.5,1,2,4,8}
- 长度分布衰减指数 α ∈{2.0,2.2,2.4}
- 死端裂隙总面积占比 S_d = S_d / S_i （死端裂隙表面积与全部裂隙表面积之比）
- FPTD尾部斜率（95%~99.99%分位数线性回归系数）
- FPTD方差
- 死端裂隙中示踪粒子经历比例
- 骨架网络（去除死端裂隙）滞留时间分布（RTD）
- 粒子轨迹平均迂曲度 τ = (1/L) ∫|v| dt
- 逾渗临界数 pc （随α变化：α=2.0时pc≈90，α=2.2时pc≈82，α=2.4时pc≈72，见[Yoon 2023, Fig.1]）

## Reusable Claims
1. 在三维离散裂隙网络中，死端裂隙的归一化表面积在逾渗阈值附近达到最大值，此后随裂隙密度增加而单调下降。[Yoon 2023, pp. 9-10] 条件：裂隙长度幂律分布，开度与半径相关，无面内开度变异性，仅考虑平流；适用密度范围覆盖亚临界至超逾渗。
2. 溶质首次通过时间分布的尾部斜率在逾渗阈值处最小（非菲克特征最强），死端裂隙的滞留作用是主要成因。[Yoon 2023, pp. 8-12] 条件同前，尾部斜率量化使用95%~99.99%分位数线性回归。
3. 基于双连通分量的图论死端定义能更有效地捕捉死端裂隙对拖尾的影响，较之2‑核子图定义更能剔除对主运移路径贡献小的裂隙。[Yoon 2023, pp. 5-7, 11-12] 适用任意三维裂隙网络拓扑，无需流动信息。
4. 死端裂隙的占比与溶质尾部斜率和粒子轨迹迂曲度均呈正相关，因此死端密度可作为非菲克运移的预测指标。[Yoon 2023, pp. 10-13] 条件：网络连接性中等至稀疏，平流主导。
5. 在逾渗阈值附近，示踪粒子进入死端裂隙的比例最高，表明最大程度的低速区域接触，从而产生强拖尾。[Yoon 2023, pp. 10-11] 结合图6b，粒子百分比规律与S_d一致。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[dead-end fracture]]
- [[percolation threshold]]
- [[non-Fickian transport]]
- [[solute tailing]]
- [[first passage time distribution (FPTD)]]
- [[biconnected component]]
- [[graph-based fracture network representation]]
- [[flow channelization]]
- [[backbone network]]
- [[truncated power-law distribution]]
- [[tortuosity]]
- [[normalized fracture density]]

## Candidate Methods
- [[graph-based dead-end fracture identification via biconnected components]]
- [[dfnWorks]]
- [[Reynolds equation solver (PFLOTRAN)]]
- [[flux-weighted particle injection]]
- [[particle tracking (advection-only)]]
- [[linear regression on tail slopes (95–99.99% quantiles)]]
- [[percolation threshold estimation via error function fitting]]
- [[parsimonious DFN generation using Poisson process]]

## Connections To Other Work
- 非菲克运移在裂隙网络中的普遍性已由Becker & Shapiro (2000)、Berkowitz & Scher (1997)、Hyman, Rajaram, et al. (2019) 等多篇文献证实。[Yoon 2023, pp. 1]
- Hyman (2020) 和 Sherman et al. (2020) 指出低密度时流动通道化显著，密度增加后通道化减弱，与本研究观察的拖尾趋势一致。[Yoon 2023, pp. 1-2, 8]
- Hyman et al. (2017) 提出的子网络模型能捕捉平均行为，但需要标定才能预测晚期拖尾，暗示次要裂隙（如死端）可能控制晚期行为。[Yoon 2023, pp. 2]
- 2‑核子图曾被用作识别参与主流动的裂隙（Hyman et al., 2017; Doolaeghe et al., 2020），本研究提出的双连通分量定义更精确地隔离了死端。[Yoon 2023, pp. 6-7]
- Maillot et al. (2016) 基于流动信息识别低流速死端裂隙，而本研究仅依赖拓扑，效率更高且标准一致。[Yoon 2023, pp. 7]

## Open Questions
- 当显式包含分子扩散时，死端裂隙的低流速区会更易被粒子进入，拖尾效应将如何增强？[Yoon 2023, pp. 13-14]
- 如果考虑裂隙面内开度非均质性，其对死端裂隙相关拖尾的影响是否可忽略？[Yoon 2023, pp. 13-14]
- 该结果对地质力学成因的裂隙网络（存在分簇和分形特征）是否依然成立？[Yoon 2023, pp. 3, 14]
- 死端裂隙的拓扑定义与其他流量或几何定义在不同网络结构下的定量比较尚需系统研究。
- 能否利用死端裂隙密度直接预测非菲克参数（如CTRW的参数），而不仅仅是相关关系？

## Source Coverage
本页面处理了所有17个非空索引片段（索引文本17项，总字符数83282），已编译片段总字符数82565，按片段数量覆盖率100%，按字符覆盖率约99.14%，来源签名875e19e3816fc82a38d77350bdedea8971fb1628，达到全索引覆盖，采用单次直出Markdown合成。
