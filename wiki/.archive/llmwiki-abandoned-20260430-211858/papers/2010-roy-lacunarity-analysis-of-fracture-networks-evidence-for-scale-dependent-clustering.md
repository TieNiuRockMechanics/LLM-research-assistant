---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering"
title: "Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering."
status: "draft"
source_pdf: "data/papers/2010 - Lacunarity analysis of fracture networks Evidence for scale-dependent clustering.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Roy, Ankur, et al. “Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering.” *Journal of Structural Geology*, 2010."
indexed_texts: "7"
indexed_chars: "31389"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:00:26"
---

# Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering.

## One-line Summary
本文提出一种归一化空隙度（lacunarity）方法，去除裂缝丰度影响以纯粹量化二维裂缝网络的聚集程度，并应用于威尔士 Telpyn Point 和挪威 Hornelen 盆地，揭示裂缝聚集随观测尺度减小而增强的尺度依赖性，该趋势被归因于从沉积旋回尺度的“层控”系统向层理尺度的“非层控”系统的转变 [Roy 2010, pp. 1-1].

## Research Question
- 如何通过归一化空隙度消除裂缝丰度（fraction of occupied sites, f）对空隙度曲线的影响，从而获得对裂缝网络聚集程度的纯粹度量？[Roy 2010, pp. 1-1, 2-4]
- 天然裂缝网络的聚集特征是否具有空间尺度依赖性？若有，何处产生可从“层控”到“非层控”的行为转变？[Roy 2010, pp. 1-1, 4-5]

## Study Area / Data
- **Telpyn Point, Wales (UK)**：发育于石炭纪砂岩中的两组近似正交的充填节理（走向 200° NS 组与 290° EW 组）。数据取自 247.6 m² 的露头范围。NS 组节理主要呈聚集状分布，EW 组相对稀疏且规则 [Roy 2010, pp. 2-4].
- **Hornelen Basin, Norway**：采用 Odling (1997) 的四张嵌套航拍裂缝图（地图 4～7），覆盖面积从 90 m × 90 m 至 720 m × 720 m，比例尺依次为 1:511、1:1023、1:2045、1:4091。图像采集时通过改变直升机高度改变空间分辨率，构成独特的跨尺度数据集 [Roy 2010, pp. 4-4].
  - 表 1（片段引用）给出了各图的面积、比例尺、盒计数分形维数 D_b、裂缝占据比例 f 及非归一化空隙度 L(10) 和 L(500) [Roy 2010, pp. 4-5].

## Methods
- **滑动盒算法（gliding‑box algorithm）**：对于二值化的裂缝分布图，以边长 r 的盒子滑动扫描全部区域，统计每个盒子内裂缝占据的格点数 s(r)。定义一阶矩 Z₁(r)=s(r)、二阶矩 Z₂(r)=s²_s(r)+[s(r)]²，空隙度 L(r)=Z₂(r)/[Z₁(r)]² [Roy 2010, pp. 2-4]. 该定义源自 Allain & Cloitre (1991) 及 Plotnick et al. (1996)。
- **归一化空隙度**：本文提出新归一化方法，使归一化空隙度 L*(r) 的值域变为 r=1 时为 1，r=r_t（整幅图大小）时为 0，从而剔除裂缝占据比例 f 的影响，使曲线仅反映聚集特性 [Roy 2010, pp. 4-4]. 归一化后的曲线不再需要对数变换。
  - 具体归一化公式未从索引片段中确认。
- 对 Telpyn Point 的三幅图（NS 组、EW 组、两组组合）和 Hornelen 盆地的四张嵌套图分别计算 L*(r)，并绘制其随盒子大小 r 的变化曲线 [Roy 2010, pp. 4-4, 4-5].

## Key Findings
1. **同一尺度不同裂缝组的聚集差异**：Telpyn Point 数据表明，归一化空隙度曲线对裂缝组的聚集程度高度敏感。聚集更强的 NS 组的 L*(r) 明显高于稀疏分布的 EW 组；当 NS 与 EW 组合时，整体 L*(r) 曲线几乎完全由 NS 组主导，因 NS 组紧紧聚集 [Roy 2010, pp. 4-4].
2. **聚集程度的尺度依赖性**：Hornelen 盆地的归一化空隙度曲线随地图尺度减小（从 720 m→90 m）而系统抬升，即空间尺度越小（细观尺度），裂缝网络越趋向于“非层控”型聚集；尺度越大，聚集程度越低 [Roy 2010, pp. 4-5, 5-6].
3. **层控与非层控行为的转变**：在航摄像片尺度下观察到贯穿沉积旋回（100 – 200 m 厚）的裂缝呈 50 – 100 m 的规则间距，表现为“层控”系统；而在数十米厚的层理尺度内，裂缝常穿过层理面，形成“非层控”聚集系统。聚集程度的尺度依赖性正源于这一从沉积旋回（独立力学单元）向层理（弱力学界面）的过渡 [Roy 2010, pp. 4-5, 5-6].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| Telpyn Point NS 组归一化空隙度显著高于 EW 组；综合网络的空隙度曲线由更聚集的 NS 组主导 | [Roy 2010, pp. 4-4] | 二值化裂缝图，滑动盒法计算，归一化去除 f 的影响 | 表明归一化空隙度可分离不同组的聚类贡献 |
| Hornelen 地图 4（90 m）至地图 7（720 m）的归一化空隙度曲线依次降低 | [Roy 2010, pp. 4-5] | 嵌套航拍数据，分辨率随比例尺变化；裂缝组多世代复杂 | 证实聚集程度随空间尺度减小而增强 |
| 大尺度航拍显示沉积旋回（100 – 200 m）中的裂缝呈 50 – 100 m 规则间距 | [Roy 2010, pp. 5-6] | Hornelen 盆地，航摄像片尺度 | 支撑大尺度下趋向“层控”系统的解释 |
| 表中 Hornelen 各图的 D_b 均在 1.81–1.84，f 在 7.93–10.09%，未归一化 L(10) 和 L(500) 随面积增大而减小 | [Roy 2010, pp. 4-5] | 指源自 Roy et al. (2007) 的分形维数 | 非归一化值也显示尺度趋势，但受到 f 变化干扰 |

## Limitations
- 索引片段未明确列出该研究的局限性。
- 可推断但未从索引片段确认的潜在局限：分析仅针对二维露头或航拍图像，未考虑裂缝开度、充填状态或三维网络连通性；Hornelen 盆地的尺度效应可能受限于航拍分辨率，未能涵盖更微细或更宏观的尺度；两处地质背景均为特定沉积地层，结论向其他力学地层环境的推广性待验证。

## Assumptions / Conditions
- 裂缝图可被合理二值化，每个格点仅记录裂缝存在与否 [Roy 2010, pp. 2-4].
- 归一化空隙度计算时，整个研究区视为均匀的占据概率 f，归一化后可消除 f 对空隙度曲线的干扰，使结果仅反映聚集差异 [Roy 2010, pp. 4-4].
- 区分“层控”与“非层控”的物理依据：层控系统受控于明显力学界面（如高刚性对比的层理），裂缝多终止于界面；非层控系统发育于力学差异不足的岩层，裂缝可贯穿层理 [Roy 2010, pp. 1-1, 4-5].
- Hornelen 盆地沉积旋回（100 – 200 m）具有高刚性对比，可作为独立力学单元；而内部层理（数十米）未构成强界面 [Roy 2010, pp. 4-5].

## Key Variables / Parameters
- **L(r)**：非归一化空隙度，L(r) = Z₂(r)/[Z₁(r)]²，其中 Z₁(r)=s(r)，Z₂(r)=σ_s²(r)+[s(r)]² [Roy 2010, pp. 2-4].
- **L*(r)**：归一化空隙度，取值范围 0 – 1，消除了 f 的影响 [Roy 2010, pp. 4-4].
- **r**：滑动盒边长（箱尺 size）[Roy 2010, pp. 2-4].
- **f**：裂缝占据格点的比例，影响未归一化 L(r) 的上界 L_max=1/f [Roy 2010, pp. 2-4].
- **s(r)**, σ_s²(r)：单个盒子内占据格点数的均值和方差 [Roy 2010, pp. 2-4].
- **D_b**：盒计数分形维数，表中用于描述各图的裂缝空间填充特征 [Roy 2010, pp. 4-5].
- **地图面积/比例尺**：用于分析尺度依赖性 [Roy 2010, pp. 4-5].

## Reusable Claims
1. **归一化空隙度可纯粹表征裂缝聚集**  
   “通过将空隙度归一化至 [0,1] 并消除裂缝丰度 f 的影响，L*(r) 的值完全反映聚集强度，聚集越强，L*(r) 越高。”  
   - 适用条件：二维二值化裂缝分布图，采用滑动盒算法计算。  
   - 证据：Telpyn Point 的 NS 组 L*(r) 高于 EW 组，且归一化后不再受 f 差异干扰 [Roy 2010, pp. 4-4].  
   - 限制：仅在正交节理组上验证，其他复杂断裂样式的表现未从索引片段确认。

2. **裂缝聚集的尺度依赖性可反映力学单元边界**  
   “在 Hornelen 盆地，从小尺度到大尺度，归一化空隙度系统降低，表明聚集减弱；这对应于从‘非层控’（层理尺度）向‘层控’（沉积旋回尺度）系统的演化。当观测尺度跨过力学单元的特征厚度时，聚集行为发生转变。”  
   - 适用条件：具有明确力学分层的沉积地层，裂缝尺度范围跨越层理与旋回厚度。  
   - 证据：Hornelen 地图 4–7 的 L*(r) 曲线趋势，以及航拍图上沉积旋回裂缝的规则间距 [Roy 2010, pp. 4-5, 5-6].  
   - 限制：仅基于一个盆地的航拍数据，未从索引片段确认是否在其他盆地重现。

3. **强聚集组主导组合网络的空隙度响应**  
   “当多种裂缝组共存时，归一化空隙度曲线将由聚集最强的组主导，表明空隙度分析可识别控制网络聚集特性的关键组系。”  
   - 条件：各组裂缝可被区分且其二值图可分别计算；聚集程度差异足够大。  
   - 证据：Telpyn Point NS+EW 组合的 L*(r) 曲线与 NS 组几乎重合 [Roy 2010, pp. 4-4].  
   - 限制：仅针对两组正交节理的情况，多组非正交裂缝的情况未从索引片段确认。

## Candidate Concepts
- [[lacunarity]]
- [[normalized lacunarity]]
- [[fracture clustering]]
- [[stratabound fractures]]
- [[non-stratabound fractures]]
- [[scale-dependent clustering]]
- [[fractal dimension]]
- [[box-counting]]
- [[mechanical stratigraphy]]
- [[joint spacing]]
- [[gliding-box algorithm]]
- [[fracture network heterogeneity]]

## Candidate Methods
- [[gliding-box lacunarity analysis]]
- [[normalized lacunarity curve analysis]]
- [[box-counting fractal analysis]]
- [[2D fracture map digitalization]]
- [[scanline spacing analysis]]
- [[semivariogram analysis of fractures]]

## Connections To Other Work
- 本研究的归一化空隙度方法建立在 Plotnick et al. (1996) 和 Allain & Cloitre (1991) 的空隙度框架之上，但通过新归一化消除了 f 效应 [Roy 2010, pp. 2-4, 4-4].
- 所用 Hornelen 盆地裂缝图源自 Odling (1997)，同时利用了 Roy et al. (2007) 的分形盒计数结果 [Roy 2010, pp. 4-4, 4-5].
- 文中提及的裂缝间距量化方法还包括基于扫描线的半变异函数（La Pointe & Hudson, 1985; Chiles, 1988）以及间距标准偏差/均值比（Gillespie et al., 1999），以此引出二维空隙度分析的必要性 [Roy 2010, pp. 1-2].

## Open Questions
- “空隙度与裂缝连通性之间的关系”尚需在未来研究中阐明，因为聚集的尺度依赖性对岩体强度和流体流动具有潜在重要影响 [Roy 2010, pp. 5-6].
- 归一化空隙度方法在三维裂缝网络、多相流体运移建模中的应用能力未从索引片段中确认。
- 不同构造体制或岩性组合下，尺度依赖的层控‑非层控转变阈值是否具有普适性，亦未在片段中讨论。

## Source Coverage
本页面基于 7 条索引片段编译，覆盖论文的摘要、引言（研究背景）、方法说明、Telpyn Point 案例分析、Hornelen 盆地多尺度结果及部分讨论与结论。片段提供了完整的作者信息、核心公式、归一化优势、关键图表趋势及地质解释。  
**可能的缺失信息**：归一化空隙度的具体计算表达式未出现在片段中；对方法局限性的自述缺失；部分参数（如格点分辨率、盒子滑动步长）未详述；对结果不确定性的定量讨论（例如误差棒含义）无从确认；讨论中引用 Bai & Pollard (2000) 等的具体上下文未完整呈现。
