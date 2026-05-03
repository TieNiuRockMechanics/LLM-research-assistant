---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-miao-a-fractal-analysis-of-permeability-for-fractured-rocks"
title: "A Fractal Analysis of Permeability for Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2015 - A fractal analysis of permeability for fractured rocks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Miao, Tongjun, et al. “A Fractal Analysis of Permeability for Fractured Rocks.” *International Journal of Heat and Mass Transfer*, 2014. doi:10.1016/j.ijheatmasstransfer.2014.10.010."
indexed_texts: "7"
indexed_chars: "34262"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "34403"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004115"
coverage_status: "full-index"
source_signature: "a7fe4a0688fc76043ddc7f15291c19892179223b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:39:00"
---

# A Fractal Analysis of Permeability for Fractured Rocks.

## One-line Summary
基于分形几何理论与立方定律，推导了裂缝性岩石渗透率的解析模型，并通过数值模拟验证了模型的有效性。 [Miao 2014, pp. 1-1] [Miao 2014, pp. 4-5]

## Research Question
如何建立裂缝性岩石/介质的渗透率与分形维数、孔隙度、裂缝密度及微观结构参数（如裂缝长度、孔径、方位角、倾角）之间的定量关系？ [Miao 2014, pp. 1-1] [Miao 2014, pp. 1-2]

## Study Area / Data
- 模型验证使用了文献中四组随机裂缝网络的数值模拟数据（Zhang and Sanderson, 1996）[Miao 2014, pp. 3-4]。
- 与Jafari and Babadagli（2011）的22个天然裂缝网络2D图及相应3D等效渗透率模拟结果进行对比 [Miao 2014, pp. 4-5]。
- 相关参数取自文献报道：最大裂缝长度 $l_{\max}=1.5\ \text{m}$，最小长度 $l_{\min}=0.0005\ \text{m}$，平均分形维数 $D_f=1.3$，平均孔隙度 $\varphi=0.018$ [Miao 2014, pp. 3-4]；另一组对比中 $l_{\max}=2\ \text{m}$，倾角 $\theta=0$ [Miao 2014, pp. 4-5]。

## Methods
1. **裂缝长度分布的分形标度律**  
   将裂缝面积分布类比岛面积分布，结合孔径与长度的线性关系 $a=bl\ (n=1)$，导出裂缝长度的累积数分布：
   $$ N(L \ge l) = \left( \frac{l_{\max}}{l} \right)^{D_f} $$  
   式中 $D_f$ 为裂缝长度分布的分形维数，0 < $D_f$ < 2（二维） [Miao 2014, pp. 2-3]。

2. **分形维数与孔隙度的关系**  
   将多孔介质中孔隙的分形关系推广至裂缝：
   $$ D_f = d_E + \frac{\ln \varphi}{\ln (l_{\max}/l_{\min})} $$  
   二维时 $d_E=2$，$\varphi$ 为裂缝面积孔隙度 [Miao 2014, pp. 2-3]。

3. **裂缝密度表达式**  
   基于裂缝总长度定义裂缝密度 $D = l_{\text{total}}/A$，结合分形标度得到：
   $$ D = \frac{(2-D_f)\,\varphi\left[ 1-\left( l_{\min}/l_{\max} \right)^{1-D_f} \right]}{(1-D_f)\,b\,l_{\max}\left[ 1-\left( l_{\min}/l_{\max} \right)^{2-D_f} \right]} $$  
   简化后亦可写为 $D = \frac{(2-D_f)(1-\varphi)^{\frac{1-D_f}{2-D_f}}}{(1-D_f) b l_{\max}} \varphi$ [Miao 2014, pp. 3-4]。

4. **渗透率模型**  
   考虑裂缝方位角 $\alpha$ 与倾角 $\theta$ 对流动的影响，由立方定律 $q(l) = \frac{a^3 l}{12\mu}\frac{\Delta P}{L_0}(1-\cos^2\alpha \sin^2\theta)$，积分所有裂缝得总流量，与达西定律对比导出渗透率：
   $$ K = \frac{b^3}{128A} \frac{D_f (1-\cos^2\alpha \sin^2\theta)}{4-D_f} l_{\max}^4 $$  
   或代入裂缝密度 $D$：
   $$ K = \frac{b^3 D}{128} \frac{1-D_f}{4-D_f} l_{\max}^3 (1-\cos^2\alpha \sin^2\theta) \frac{(1-\varphi)^{\frac{1-D_f}{2-D_f}}}{\varphi} $$ [Miao 2014, pp. 4-5]

5. **参数确定步骤**：给定 $l_{\max}, \varphi, \alpha, \theta, b$ → 由盒计数法或式(7)求 $D_f$ → 由式(13b)求 $D$ → 由式(21)计算 $K$ [Miao 2014, pp. 4-5]。

## Key Findings
1. 裂缝性岩石的渗透率是分形维数 $D_f$、最大裂缝长度 $l_{\max}$、裂缝密度 $D$、面积孔隙度 $\varphi$、裂缝方位角 $\alpha$ 和倾角 $\theta$ 的函数 [Miao 2014, pp. 4-5]。
2. 渗透率随孔隙度和裂缝密度的增加而增大；裂缝倾角增大时渗透率降低（流动阻力增加） [Miao 2014, pp. 5-6]。
3. 模型预测与Zhang and Sanderson (1998)的四组随机裂缝网络密度数据吻合良好（Fig. 2） [Miao 2014, pp. 3-4]。
4. 模型预测的渗透率与Jafari and Babadagli (2011)的22个天然裂缝网络等效渗透率模拟结果一致（Fig. 4） [Miao 2014, pp. 4-5]。
5. 裂缝密度 $D$ 随分形维数 $D_f$ 和孔隙度 $\varphi$ 的增加而增加（Fig. 2, Fig. 3） [Miao 2014, pp. 3-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 裂缝长度累积数分布 $N(L \ge l) = (l_{\max}/l)^{D_f}$ | [Miao 2014, pp. 2-3] Eq. (4) | 裂缝面积分布满足分形，孔径与长度线性相关 $a=bl$ | $D_f$ 通过盒计数法或式(7)确定 |
| $D_f = 2 + \ln \varphi / \ln(l_{\max}/l_{\min})$ | [Miao 2014, pp. 2-3] Eq. (7) | 二维分形裂缝系统 | 类比孔隙介质分形关系导出 |
| 裂缝密度 $D = \frac{(2-D_f)\varphi[1-(l_{\min}/l_{\max})^{1-D_f}]}{(1-D_f)bl_{\max}[1-(l_{\min}/l_{\max})^{2-D_f}]}$ | [Miao 2014, pp. 3-4] Eq. (13a) | 裂缝总长度由分形积分求得 | 可简化得式(13b) |
| 渗透率 $K = \frac{b^3}{128A} \frac{D_f(1-\cos^2\alpha\sin^2\theta)}{4-D_f} l_{\max}^4$ | [Miao 2014, pp. 4-5] Eq. (20) | 层流，所有裂缝连通，平均方位角/倾角 | 对比达西定律导出 |
| Fig. 2：模型预测的裂缝密度与四组模拟数据吻合 | [Miao 2014, pp. 3-4] | $l_{\max}=1.5\ \text{m}$, $l_{\min}=0.0005\ \text{m}$, $D_f=1.3$, $\varphi=0.018$ | 验证了$D$-$D_f$关系 |
| Fig. 4：渗透率模型预测与22个天然裂缝网络模拟结果一致 | [Miao 2014, pp. 4-5] | $l_{\max}=2\ \text{m}$, $\theta=0$, $b=0.002$ | 采用盒计数$D_f$，由式(13b)求$D$，式(21)求$K$ |

## Limitations
- 模型假设所有裂缝均连通并形成网络，未考虑裂缝间的相互作用和连接性 [Miao 2014, pp. 5-6]。
- 未涉及逾渗理论和临界行为 [Miao 2014, pp. 5-6]。
- 采用平均裂缝方位角和平均倾角，未考虑取向分布的非均匀性 [Miao 2014, pp. 3-4]。
- 依赖于孔径与长度的线性标度律 $n=1$，该线性关系在某些尺度下可能不成立 [Miao 2014, pp. 1-2]。

## Assumptions / Conditions
1. 裂缝长度分布符合分形标度律，具有统计自相似性 [Miao 2014, pp. 1-2]。
2. 裂缝有效孔径 $a$ 与长度 $l$ 满足线性关系 $a = bl$（$n=1$），保证网络自相似性 [Miao 2014, pp. 1-2]。
3. 裂缝中流体流动为层流，可用立方定律描述 [Miao 2014, pp. 3-4]。
4. 所有裂缝在代表性单元体内连通，贡献整体渗透率，基质孔隙可忽略 [Miao 2014, pp. 1-1] [Miao 2014, pp. 5-6]。
5. 裂缝取向简化为平均方位角 $\alpha$ 与平均倾角 $\theta$ [Miao 2014, pp. 3-4]。
6. 最大裂缝长度 $l_{\max}$ 远大于最小长度 $l_{\min}$，且单位面积内仅有一条最大裂缝 [Miao 2014, pp. 2-3]。
7. 面积孔隙度 $\varphi$ 由裂缝总面积定义，适用二维分形关系 $D_f = 2 + \ln\varphi / \ln(l_{\max}/l_{\min})$ [Miao 2014, pp. 2-3]。

## Key Variables / Parameters
| 符号 | 名称 | 单位/范围 | 描述 |
|------|------|-----------|------|
| $D_f$ | 裂缝长度分布分形维数 | 0–2（2D） | 表征裂缝长度分布的幂律指数 |
| $\varphi$ | 裂缝面积孔隙度 | - | 裂缝总面积与单元面积之比 |
| $l_{\max}$ | 最大裂缝长度 | m | 系统中唯一一条最长裂缝的长度 |
| $l_{\min}$ | 最小裂缝长度 | m | 自相似范围的下限 |
| $b$ | 孔径-长度比例系数 | - | $a = bl$ 中的系数 |
| $n$ | 孔径-长度标度指数 | 1（本文） | 取1对应自相似分形 |
| $D$ | 裂缝密度 | m/m² | 单位面积内所有裂缝的总长度 |
| $\alpha$ | 平均裂缝方位角 | rad | 裂缝走向与Y轴夹角 |
| $\theta$ | 平均裂缝倾角 | rad | 裂缝面与水平面的夹角 |
| $A$ | 代表单元面积 | m² | 计算渗透率时的截面面积 |
| $\mu$ | 流体动力粘度 | Pa·s | 立方定律中参数 |

## Reusable Claims
1. **裂缝长度分布标度律**  
   对于自相似分形裂缝网络，裂缝累积数 $N(L \ge l)$ 满足 $N \propto l^{-D_f}$，其中 $D_f$ 在二维中介于0–2 [Miao 2014, pp. 2-3]。该关系可用盒计数法验证，适用范围为 $l_{\min} \le l \le l_{\max}$。

2. **分形维数与孔隙度的关系**  
   二维裂缝网络的孔隙度 $\varphi$ 与 $D_f$ 及 $l_{\max}/l_{\min}$ 的关系为 $D_f = 2 + \frac{\ln \varphi}{\ln (l_{\max}/l_{\min})}$ [Miao 2014, pp. 2-3]。此式仅当裂缝面积分布满足严格或统计自相似时成立。

3. **裂缝密度预测公式**  
   裂缝密度 $D = \frac{(2-D_f)\varphi}{(1-D_f)bl_{\max}} \cdot \frac{1-(l_{\min}/l_{\max})^{1-D_f}}{1-(l_{\min}/l_{\max})^{2-D_f}}$ [Miao 2014, pp. 3-4]。在 $l_{\min} \ll l_{\max}$ 时可简化为 $D \approx \frac{(2-D_f)\varphi}{(1-D_f)bl_{\max}}$。该式与随机网络数值模拟吻合（Fig. 2）。

4. **裂缝性岩石渗透率解析模型**  
   渗透率可由微结构参数显式表达：
   $$ K = \frac{b^3 D}{128} \frac{1-D_f}{4-D_f} l_{\max}^3 (1-\cos^2\alpha \sin^2\theta) \frac{(1-\varphi)^{\frac{1-D_f}{2-D_f}}}{\varphi} $$  
   或等效形式 $K = \frac{b^3}{128A} \frac{D_f(1-\cos^2\alpha \sin^2\theta)}{4-D_f} l_{\max}^4$ [Miao 2014, pp. 4-5]。条件：层流、裂缝完全连通、平均方位角/倾角、$n=1$。

5. **渗透率随孔隙度和密度的正相关性**  
   在分形裂缝网络中，渗透率随 $\varphi$ 和 $D$ 的增大而增大；倾角 $\theta$ 增大则渗透率减小 [Miao 2014, pp. 5-6]。该趋势与数值模拟结果一致 [Miao 2014, pp. 5-6]。

6. **最大裂缝长度的主导作用**  
   $K \propto l_{\max}^4$ 或 $l_{\max}^3$，表明渗透率对最大裂缝长度极为敏感，长裂缝因其宽孔径主导了流动 [Miao 2014, pp. 4-5]。

## Candidate Concepts
- [[fracture reservoir]]
- [[fracture network]]
- [[fractal dimension]]
- [[cubic law]]
- [[parallel plate model]]
- [[self-similarity]]
- [[power-law length distribution]]
- [[fracture density]]
- [[area porosity]]
- [[box-counting method]]
- [[Darcy's law]]
- [[permeability]]
- [[aperture-length scaling]]
- [[fracture orientation]]
- [[fractal porous media]]
- [[percolation threshold]]
- [[dual porosity media]]

## Candidate Methods
- [[Box-counting method]] for fracture length fractal dimension
- [[Cubic law]] for laminar flow in a fracture
- [[Parallel plate model]]
- [[Fractal scaling law for fracture length distribution]]
- [[Fractal geometry theory]]
- [[Monte Carlo simulation]] (referenced in other works)
- [[Numerical simulation of random fracture networks]]
- [[Self-avoiding random generation of fractures]]

## Connections To Other Work
- **Snow (1965)** [4]：早期平行板模型估算裂缝网络渗透率，本文在此基础上引入分形结构 [Miao 2014, pp. 1-1]。
- **Koudina et al. (1998)** [6]：三维多边形裂缝网络数值模拟，假设裂缝内满足达西律，本文对比并强调了分形参数的显式表达 [Miao 2014, pp. 1-1]。
- **Dreuzy et al. (2001)** [7]：二维幂律长度分布随机裂缝网络的渗透率研究，验证了理论模型，本文的标度律(4)与之类似 [Miao 2014, pp. 1-1]。
- **Klimczak et al. (2010)** [8]：基于孔径-长度幂律相关的平行板模型，本文采用 $n=1$ 的线性关系并推广至网络尺度 [Miao 2014, pp. 1-1] [Miao 2014, pp. 1-2]。
- **Jafari & Babadagli (2011, 2012)** [14, 49]：利用分形维数和统计特性估算等效裂缝网络渗透率，但表达式包含经验常数，本文提供了纯解析形式 [Miao 2014, pp. 1-1, 4-5]。
- **Zhang & Sanderson (1998)** [36]：随机自回避裂缝网络生成方法，本文用其模拟数据验证了裂缝密度公式 [Miao 2014, pp. 3-4]。
- **Hatton et al. (1994)** [28]、**Schultz et al. (2008)** [29]：支持裂缝孔径与长度的线性标度律（$n=1$），为本文假设提供了依据 [Miao 2014, pp. 1-2]。
- **Yu & Li (2001)** [35]：多孔介质分形维数与孔隙度的关系（式6），本文推广至裂缝体系 [Miao 2014, pp. 2-3]。

## Open Questions
- 如何将裂缝间的相互作用与连接性（如逾渗临界行为）纳入本模型？ [Miao 2014, pp. 5-6]
- 当孔径-长度标度指数 $n \ne 1$ 时，分形标度律和渗透率模型如何修正？ [Miao 2014, pp. 1-2]
- 对于非均匀裂缝取向分布，是否需要引入取向分布函数以替代平均方位角/倾角？ [Miao 2014, pp. 3-4]
- 基质孔隙对整体渗透率的贡献在何种条件下不可忽略？ [Miao 2014, pp. 1-1]

## Source Coverage
所有非空索引片段均已处理，共7个片段，总字符数34,403个。按代码块计算覆盖率为100%（覆盖比1.0）；按字符数计算覆盖率约为1.004。使用的片段标识：`2014-miao-a-fractal-analysis-of-permeability-for-fractured-rocks`。
