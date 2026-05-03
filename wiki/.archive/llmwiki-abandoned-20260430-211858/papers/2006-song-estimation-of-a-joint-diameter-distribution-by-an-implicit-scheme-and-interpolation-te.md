---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2006-song-estimation-of-a-joint-diameter-distribution-by-an-implicit-scheme-and-interpolation-te"
title: "Estimation of a Joint Diameter Distribution by an Implicit Scheme and Interpolation Technique."
status: "draft"
source_pdf: "data/papers/2006 - Estimation of a joint diameter distribution by an implicit scheme and interpolation technique.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Song, Jae-Joon. \"Estimation of a Joint Diameter Distribution by an Implicit Scheme and Interpolation Technique.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 43, 2006, pp. 512-519. doi:10.1016/j.ijrmms.2005.09.009. Accessed 2026."
indexed_texts: "7"
indexed_chars: "32617"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:21:34"
---

# Estimation of a Joint Diameter Distribution by an Implicit Scheme and Interpolation Technique.

## One-line Summary
提出一种最小二乘隐式方案直接由窗口内包含迹长分布估计节理直径分布，并通过 B 样条插值改善小样本下的估计精度 [Song 2006, pp. 1-2]。

## Research Question
如何在不依赖无限窗口迹长分布的前提下，仅从采样窗口内的包含迹长样本直方图直接、准确地推断三维节理组的直径分布？ [Song 2006, pp. 2-3]

## Study Area / Data
研究基于蒙特卡洛模拟生成虚拟节理数据，未使用特定实际岩体现场数据。虚拟节理圆盘直径服从均值为 5 m、标准差为 2.5 m 的对数正态分布；采样窗口为水平矩形，宽 54 m、高 20 m；节理产状为 030/45°；体积频率在 0.01 m⁻³ 至 0.4 m⁻³ 之间调整以改变样本量。此外，对 Fisher 常数 K=15、25、35 的各向同性节理组方位进行了敏感性测试 [Song 2006, pp. 4-7]。

## Methods
1. **建模假设与几何关系**：将节理视为泊松圆盘，同一组内节理平行。给定矩形采样窗口尺寸和迹线与窗口边界的夹角，利用包含迹长中心点的存在区域面积 \(A_c^l\) 及圆盘中心点存在的平行六面体体积公式，建立迹线数量与直径分布之间的积分方程 [Song 2006, pp. 2-4]。
2. **隐式估计方案（最小二乘法）**：将直径分布视为离散函数，把积分方程转化为线性方程组 \( \mathbf{A} \mathbf{c} = \mathbf{N}_c \)，其中 \(\mathbf{A}\) 为系数矩阵，\(\mathbf{c}\) 为待求的各直径分级频率，\(\mathbf{N}_c\) 为各长度分级包含迹线的观测数量。采用最小二乘法直接求解直径分布 [Song 2006, pp. 3-4]。
3. **B 样条插值平滑**：在最小二乘估计前，用 B 样条（三阶、五阶、七阶混合函数）对样本包含迹长直方图进行插值，以减轻因局部样本不足导致的直方图突变，提高估计平滑性和精度 [Song 2006, pp. 5-8]。
4. **对比验证**：与 Song and Lee (2001) 的分布无关显式方法进行比较，通过蒙特卡洛模拟比较两种方法在不同样本量下的估计误差 [Song 2006, pp. 4-5]。

## Key Findings
- 提出的隐式方案（最小二乘法）在直径分布估计中比 Song and Lee (2001) 的显式方法更准确，尤其对小样本（例如包含迹线总数在数十至数百范围内）优势明显 [Song 2006, pp. 5-6]。
- 节理方位的聚集程度（用 Fisher 常数 K 衡量）对估计精度没有明显影响，表明该方法可直接应用于非严格平行的各向同性节理组 [Song 2006, pp. 5-7]。
- 对样本包含迹长分布应用 B 样条插值可以进一步降低估计误差，B 样条与最小二乘法组合的平均误差约为仅最小二乘法的 80%。误差降低在小样本时更为显著 [Song 2006, pp. 7-8]。
- 更高阶的 B 样条混合函数（五阶、七阶）相比三阶有更低误差：对于对数正态直径分布，五阶和七阶的平均误差分别为三阶的 82% 和 79%；对于正态和指数分布也呈类似趋势 [Song 2006, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---------|--------|------------|-------|
| 隐式方案（L.S.M.）的直径分布估计误差小于 Song and Lee (2001) 的显式方法，小样本时优势更突出 | [Song 2006, pp. 5-6, Fig. 4–5] | 对数正态直径分布（均值5m，标准差2.5m），矩形窗口54m×20m，平行节理组 | Monte Carlo 模拟；误差比较基于离散直径分级的相对误差 |
| 节理方位聚集程度（Fisher常数 K=15,25,35）对估计精度无明显影响 | [Song 2006, pp. 5-7, Fig. 6] | 各向同性节理组，其余条件同 Fig. 4 | 方法可直接用于非严格平行节理 |
| B 样条插值 + L.S.M. 的平均误差约为仅 L.S.M. 的 80%，小样本时误差降低更明显 | [Song 2006, pp. 7-8, Fig. 8] | 对数正态直径分布，三阶 B 样条 | 20 个直径分级上的平均相对误差 |
| 五阶、七阶 B 样条混合函数的误差低于三阶：对数正态时分别为 82% 和 79% | [Song 2006, pp. 7-8, Fig. 9] | 对数正态直径分布 | 20 个直径分级上的平均误差 |
| 对三种理论直径分布（对数正态、正态、指数）高阶 B 样条均一致降低误差 | [Song 2006, pp. 7-8, Fig. 10–11] | 正态分布、指数分布直径 | 误差降低比例见正文 |

## Limitations
- 研究假定采样窗口足够大可以忽略删截偏差（censoring bias）；删截偏差的解决方案被列为未来工作 [Song 2006, pp. 2-3]。
- 直径分布及其导数被假定连续，且直方图的平滑性依赖样本量，B 样条插值效果可能与实际分布的连续程度有关 [Song 2006, pp. 5-7]。
- 所有性能评估均基于蒙特卡洛模拟，未使用真实岩体节理数据验证 [Song 2006, pp. 4-8]。

## Assumptions / Conditions
- 节理为平行圆形薄盘，同一组内方向完全平行，圆盘中心点在三维空间内服从均匀泊松分布（泊松圆盘模型） [Song 2006, pp. 2-3]。
- 采样窗口为矩形且尺寸远大于节理尺寸，发育完全的包含迹线占主导，可暂时忽略窗口边界引起的尺寸删截和截断偏差 [Song 2006, pp. 2-3]。
- 直径分布函数及其一阶或更高阶导数是连续的，以保证 B 样条插值的合理性 [Song 2006, pp. 5- 7]。
- 仅处理单组平行节理，每组需单独分析 [Song 2006, pp. 2-3]。

## Key Variables / Parameters
- \( l \) : 包含迹线长度；\( s \) : 节理圆盘直径；\( \theta \) : 迹线与采样窗口边界的夹角；\( \phi \) : 节理面法向与窗口法向的夹角 [Song 2006, pp. 2-4]。
- \( W, H \) : 矩形窗的宽与高；\( A_c^l \) : 长度为 \( l \) 的包含迹线中心点可行区域的面积 [Song 2006, pp. 2-3]。
- \( dt \) : 对应不同直径圆盘产生给定迹长的圆盘中心点垂直厚度，是圆盘直径 \( s \) 的函数 [Song 2006, pp. 3-4]。
- \( \lambda_V \) : 节理中心点的体积频率；\( c(s) \) : 待估的节理直径概率分布 [Song 2006, pp. 3-4]。
- \( N_c^l \) : 窗口内长度为 \( l \) 的包含迹线数量；\( S_{\max} \) : 直径的上限 [Song 2006, pp. 3-4]。
- B 样条混合函数的阶数（三阶、五阶、七阶） [Song 2006, pp. 7-8]。

## Reusable Claims
- 对于只需包含迹长数据的直径分布估计，用最小二乘法求解关联方程组（公式 (11)）比基于无限窗口迹长分布的显式重建更准确，尤其当样本量较小时（如包含迹线总数 <500） [Song 2006, pp. 5-6]。
- 若采样窗口内包含迹线直方图存在局部锯齿，先使用 B 样条（三次或更高阶）进行平滑插值，再应用最小二乘法，可将直径分布估计的平均误差降低约 20%（B 样条与 L.S.M. 组合的误差约为仅 L.S.M. 的 80%），此改善在小样本中更突出 [Song 2006, pp. 7-8]。
- 节理方向分布的集中程度（Fisher 常数在 15~35 范围）不对该隐式方法估计精度造成可察觉的影响，意味着方法可适应中度分散到强烈集中的节理组，无需修改公式 [Song 2006, pp. 5-7]。
- 高阶 B 样条混合函数可提供更好的平滑性和更低的估计误差，七阶和五阶优于三阶，但改善幅度递减（例如对数正态分布下七阶误差为三阶的 79%） [Song 2006, pp. 7-8]。

## Candidate Concepts
- [[contained trace length]]
- [[joint diameter distribution]]
- [[Poisson disc model]]
- [[window sampling]]
- [[implicit estimation scheme]]
- [[least squares method in stereology]]
- [[B-spline interpolation]]
- [[Monte Carlo simulation for stereology]]
- [[fracture size estimation]]
- [[fracture reservoir]]

## Candidate Methods
- [[implicit least squares diameter estimation]]
- [[B-spline smoothing of trace length histograms]]
- [[Monte Carlo simulation of disc joint populations]]
- [[comparison of explicit vs implicit stereological methods]]

## Connections To Other Work
- 直接对比 Song and Lee (2001) 的基于无限窗口迹长分布的显式直径估计方法，证明新方法对小样本更优 [Song 2006, pp. 1-2, 4-5]。
- 提及 La Pointe et al. (1993) 利用包含与截断迹线比例解决删截偏差的思路，作为本方法未来消除删截偏差的潜在路径 [Song 2006, pp. 2-3]。
- 与一系列基于窗口或扫描线的节理尺寸估计工作（Baecher and Lanney 1978; Warburton 1980; Kulatilake and Wu 1986; Villaescusa and Brown 1992; Zhang and Einstein 等）共享 [[stereology]]、[[trace length bias correction]] 等理论与问题背景，但未直接对比这些方法 [Song 2006, pp. 8-8]。

## Open Questions
- 如何在当前隐式方案中系统纳入窗口尺寸限制引起的删截偏差（censoring bias），而非仅靠假设窗口足够大忽略之 [Song 2006, pp. 2-3]。
- B 样条插阶数、直方图分组数与估计误差之间的定量优化关系 [Song 2006, pp. 7-8]。
- 方法从模拟推广到真实、非平行、非纯圆盘节理数据时的鲁棒性 [Song 2006, pp. 4-8]。

## Source Coverage
本页基于提供的 7 个索引片段，覆盖论文的摘要、引言、方法详述（2.1‑2.3 节）、蒙特卡洛验证结果（2.3）、B 样条改进（第 3 节）以及文献列表部分。片段包含了核心公式（1）、（4）、（11）的说明和关键图形结果的文字描述，但缺失具体公式的完整形式和部分图表细节。论文所引其他文献的详细贡献超出本片段范围，因此仅依据片段中的提法进行连接。关于实际岩体案例的应用未在片段中出现，可能来源于论文未展示部分或本文确实只做了模拟分析。
