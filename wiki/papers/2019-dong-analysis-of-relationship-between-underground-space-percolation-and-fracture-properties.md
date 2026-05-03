---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-dong-analysis-of-relationship-between-underground-space-percolation-and-fracture-properties"
title: "Analysis of Relationship between Underground Space Percolation and Fracture Properties."
status: "draft"
source_pdf: "data/papers/2019 - 地下空间逾渗与裂缝属性的关系分析.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Dong, Shaoqun, et al. \"Analysis of Relationship between Underground Space Percolation and Fracture Properties.\" *Earth Science Frontiers*, vol. 26, no. 3, 2019, pp. 140-146, doi:10.13745/j.esf.sf.2019.4.22."
indexed_texts: "6"
indexed_chars: "26931"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "25764"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.956667"
coverage_status: "full-index"
source_signature: "6d267badc20296e810968dfe08408073b6cacb52"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:42:07"
---

# Analysis of Relationship between Underground Space Percolation and Fracture Properties.

## One-line Summary
本文通过二维离散裂缝网络数值模拟，直接使用裂缝长度和数量等直接表征参数，建立了适用于不同尺度的逾渗临界值预测方程及裂缝网络连通性四级评价标准。[Dong 2019, pp. 1-1, 7-7]

## Research Question
裂缝网络连通性评价是地下空间研究的重要内容，传统方法多采用分形维数、无量纲密度等间接表征参数确定逾渗阈值，但不同连通性的裂缝网络可能具有相同的间接参数，导致预测可靠性下降。为避免此类多解性问题并更准确快速地表征连通性，能否摒弃间接参数简化方式，直接利用裂缝数量、长度等属性参数构建逾渗临界条件方程？方程在不同尺度研究区是否有效？[Dong 2019, pp. 1-1, 1-3]

## Study Area / Data
- 模拟研究区：正二维方形域，基准尺为100 m×100 m；尺度验证时选用边长为w = 50, 500, 5 000 m等，校正实验覆盖1～10 000 m。[Dong 2019, pp. 3-5, 5-7]
- 裂缝网络类型：
  - 等长裂缝网络：裂缝长度L = 2, 4, …, 98 m；裂缝数量n = 10, 20, …, 300。[Dong 2019, pp. 3-5]
  - 指数分布裂缝网络：裂缝长度均值 1/λ = 10^i m (i = 0.1, 0.124, …, 1.99)；裂缝数量n = 40, 50, …, 280。[Dong 2019, pp. 5-7]
- 裂缝走向均为完全随机分布。[Dong 2019, pp. 3-5]
- 每组参数生成N = 100个离散裂缝网络实现，计算逾渗概率P = Np/N。[Dong 2019, pp. 3-5]

## Methods
1. **二维离散裂缝网络（DFN）建模**：基于示性点过程，采用稳态泊松过程生成裂缝中心（均匀分布），示性过程生成裂缝走向（von Mises分布）和长度（等长或指数分布）。[Dong 2019, pp. 3-5]
2. **逾渗检测**：使用基于包围盒和扫描线（BBSL）的方法进行滤波与粗精炼，快速识别相交裂缝簇，判断是否存在连通域内相对两边（A、B边）的裂缝簇。[Dong 2019, pp. 3-5]
3. **临界条件提取**：分别提取P≈0（低概率）、P≈0.5（中概率）、P≈1（高概率）逾渗边界散点，采用指数函数进行非线性拟合，得到裂缝长度（或平均长度）与裂缝数量之间的临界方程。[Dong 2019, pp. 3-7]
4. **尺度校正**：
   - 等长网络：校正系数rV = w/100。[Dong 2019, pp. 5-7]
   - 指数分布网络：通过数值模拟确定校正系数与w呈线性关系rV ≈ 0.01w（综合低、中、高概率），可近似为rV = w/100。[Dong 2019, pp. 5-7]
   - 校正后临界长度U = L̄ × rV，用于不同尺度预测。[Dong 2019, pp. 5-7]
5. **连通性评价标准建立**：利用f1、f2、f3三条临界曲线将连通性分为较差、差、好、较好四级。[Dong 2019, pp. 7]

## Key Findings
- 等长裂缝网络与指数分布裂缝网络的三条逾渗临界边界均可由指数函数很好地拟合（相关指数普遍高于0.99），表现为L_t或L̄_t = a × n^{-b}的形式（式3～8）。[Dong 2019, pp. 3-7]
- 裂缝数量较少时，指数分布网络因随机抽样可能产生长裂缝，使其在低概率下更容易逾渗；当裂缝数量较多时，等长网络所需裂缝长度更大。[Dong 2019, pp. 5-7]
- 结合尺度校正rV = w/100后，建立的临界方程对不同尺度研究区（w = 50, 500, 5 000 m）的预测值与模拟值高度一致，相关系数均在0.998及以上。[Dong 2019, pp. 5-7]
- 基于校正临界值U与f1(n)、f2(n)、f3(n)的比较，可对地下裂缝网络连通性进行分级评价（表2）。[Dong 2019, pp. 7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 等长DFN逾渗低/中/高临界边界散点可用指数函数拟合，相关指数R² = 0.983/0.996/0.991 | [Dong 2019, pp. 3-5] | 2D 100 m×100 m区域，走向随机，n=10–300，L=2–98 m | 方程见式(3)–(5)，L_t = a·n^{–b} |
| 指数长度分布DFN三条临界边界同样可用指数函数拟合，R² = 0.942/0.993/0.992，低概率边界相关性稍差 | [Dong 2019, pp. 5-7] | 同上区域，n=40–280，L̄ = 10^i m，i=0.1–1.99 | 方程见式(6)–(8)，L̄_t = a·n^{–b} |
| 两种网络对比：低概率下指数分布所需L̄更小；中高概率下，n少时指数分布所需L̄更大，n多时等长网络需求更大 | [Dong 2019, pp. 5-7] | 图6对比 | 源于指数分布随机产生长/短裂缝的特性 |
| 等长网络尺度校正系数rV = w/100；指数网络校正系数rV与w亦呈线性，近似为rV = w/100 | [Dong 2019, pp. 5-7] | 高概率临界条件下模拟证实，低/中概率结果类似 | 校正后U = L̄ × rV |
| 验证结果：不同尺度和n值的预测值与模拟值相关性R² = 0.993~1.000 | [Dong 2019, pp. 5-7] | w=50,500,5000 m；n=80,200,2000 | 图8交会图 |
| 连通性评价标准：U < f1（较差），f1 ≤ U < f2（差），f2 ≤ U < f3（好），U ≥ f3（较好） | [Dong 2019, pp. 7] | 适用于裂缝长度均值经过尺度校正的情况 | 表2 |

## Limitations
- 仅研究了2D离散裂缝网络，且裂缝走向假设为完全随机，尚未涉及具有优势方位的情况。[Dong 2019, pp. 7]
- 裂缝网络模型采用稳态泊松点过程，未考虑裂缝位置的空间相关性或聚类分布。[Dong 2019, pp. 3-5]
- 校正系数对于非随机走向的推广有待验证，直接使用尺度比例系数可能导致误差。[Dong 2019, pp. 5-7]
- 指数长度分布网络低概率边界（limt1）的拟合相关性相对较低（R²=0.942），在裂缝数量较少时不确定性较大。[Dong 2019, pp. 5-7]

## Assumptions / Conditions
- 裂缝网络均为二维离散裂缝网络，裂缝简化为线线段，中心位置服从均匀分布（稳态泊松过程）。[Dong 2019, pp. 3-5]
- 裂缝走向使用von Mises分布，长度或为等长，或服从指数分布且均值等于1/λ。[Dong 2019, pp. 3-5]
- 逾渗定义为存在一簇相交裂缝连通域内两条对边（A边和B边），研究区为正方形。[Dong 2019, pp. 3-5]
- 逾渗概率通过100次等参数随机实现统计，逾渗阈值广义上对应P=0.5，但本文同时给出P≈0和P≈1的边界。[Dong 2019, pp. 3-5]
- 尺度校正公式适用于随机走向情形，且对于指数长度网络，校正系数基于特定参数范围内的模拟结果外推。[Dong 2019, pp. 5-7]

## Key Variables / Parameters
- n：裂缝数量 [Dong 2019, pp. 3-7]
- L：等长裂缝的裂缝长度 [Dong 2019, pp. 3-5]
- λ：指数分布裂缝长度参数，平均长度L̄ = 1/λ [Dong 2019, pp. 3-5]
- w：研究区正方形边长 [Dong 2019, pp. 5-7]
- P = Np/N：逾渗概率，N为总实现数，Np为逾渗实现数 [Dong 2019, pp. 3-5]
- f1(n), f2(n), f3(n)：分别对应低、中、高概率逾渗临界长度（或平均长度）函数 [Dong 2019, pp. 3-7]
- rV：尺度校正系数 [Dong 2019, pp. 5-7]
- U = L̄ × rV：校正后的临界长度均值，用于连通性评价 [Dong 2019, pp. 5-7]

## Reusable Claims
- 对于裂缝中心均匀随机的2D离散裂缝网络，无论裂缝等长还是指数长度分布，逾渗临界长度（或平均长度）与裂缝数量均可用指数函数L_t = a·n^{-b}精确拟合，系数a、b因长度分布类型和概率水平而异。[Dong 2019, pp. 3-7], 式3–8
- 等长裂缝网络的尺度依存关系可通过线性缩放因子rV = w/100直接处理，即裂缝临界长度与域边长呈正比。[Dong 2019, pp. 5-7]
- 指数长度分布网络的尺度校正系数在低、中、高逾渗概率下均可近似为rV = w/100（w为研究区边长，单位为m），该关系通过数值模拟验证有效。[Dong 2019, pp. 5-7]
- 基于f1、f2、f3三条函数曲线可将地下裂缝网络连通性分为四等，为快速评定地下空间岩体质量提供定量参照。[Dong 2019, pp. 7], 表2
- 直接使用裂缝长度和数量等属性参数构建逾渗阈值方程，可避免间接表征参数（如分形维数、无量纲密度）带来的多解性问题，提高连通性预测的可靠性。[Dong 2019, pp. 1-1, 1-3]

## Candidate Concepts
- [[underground space evaluation]]
- [[fracture connectivity]]
- [[discrete fracture network]]
- [[percolation threshold]]
- [[direct characterization parameters]]
- [[indirect characterization parameters]]
- [[scale correction]]

## Candidate Methods
- [[2D DFN modeling]]
- [[marked point process]]
- [[BBSL fracture intersection detection]]
- [[nonlinear exponential fitting]]
- [[Monte Carlo percolation simulation]]
- [[connectivity classification criteria]]

## Connections To Other Work
- 传统的裂缝网络逾渗研究多依赖间接参数，如：基于分形维数D、裂缝数量初值N₀和孔隙率构建的逾渗阈值表达式（冯增朝等，2006）[Dong 2019, pp. 1-3]；基于连续区逾渗理论和分形特征的连通度方法（李乐等，2015）[Dong 2019, pp. 1-3]；基于无量纲密度的阈值公式在二维（Robinson, 1983）、三维（Khamforoush et al., 2008）及走向优势方位、空间相关等网络中的推广（Manzocchi, 2002; Khamforoush & Shams, 2007等）[Dong 2019, pp. 1-3]。
- 本文采用的BBSL裂缝相交检测法源自Dong et al. (2018) [Dong 2019, pp. 3-5]；DFN建模的理论基础参考Xu & Dowd (2010)和董少群等 (2018) [Dong 2019, pp. 3-7]。
- 与以上工作相比，本研究的关键区别在于放弃间接参数，直接以裂缝数量、长度为变量拟合逾渗方程，并提供了系统化的尺度校正方法。

## Open Questions
- 当裂缝具有优势方位时，本文建立的预测方程及校正系数如何调整仍是未来研究的难点与重点。[Dong 2019, pp. 7]
- 三维离散裂缝网络的逾渗临界方程及尺度校正规律尚未给出，需进一步工作。[Dong 2019, pp. 7]
- 裂缝位置的空间相关性（如聚类或分形点过程）对直接参数逾渗阈值的影响未被覆盖。[Dong 2019, pp. 3-5]
- 现场裂缝数据（如采自照片或露头统计）能否直接换算为本文所需直接参数，以及预测的不确定性如何量化，也需要后续探索。

## Source Coverage
本页面基于全部6个非空索引片段编译，覆盖论文摘要、引言、离散裂缝网络模型、逾渗检测方法、两种裂缝网络的逾渗临界条件拟合、尺度校正与验证、连通性评价标准及结论。所有非空片段均被处理，源代码块覆盖率1.0，字符覆盖率0.956667。原文索引签名：6d267badc20296e810968dfe08408073b6cacb52。数据来源：[Dong 2019, pp. 1-1; 1-3; 3-5; 5-7; 7-7]。
