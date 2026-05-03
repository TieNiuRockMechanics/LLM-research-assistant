---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-li-characterization-of-a-jointed-rock-mass-based-on-fractal-geometry-theory"
title: "Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory."
status: "draft"
source_pdf: "data/papers/2019 - Characterization of a jointed rock mass based on fractal geometry theory.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Li, Lichen, et al. \"Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory.\" *Bulletin of Engineering Geology and the Environment*, vol. 78, 2019, pp. 6101–6110. https://doi.org/10.1007/s10064-019-01526-x."
indexed_texts: "8"
indexed_chars: "38776"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:48:27"
---

# Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory.

## One-line Summary
该研究利用分形几何理论描述节理岩体的产状、间距与迹长，并基于三维离散裂隙网络（DFN）重建了某露天矿的岩体结构，发现分形维数比Fisher参数能更全面地反映节理产状信息，分形分布模型比负指数模型更能表征节理间距特征 [Li 2019, pp. 1-2, 8-9]。

## Research Question
如何利用分形几何理论更合理地描述节理岩体的非连续、非均质各向异性特征，并构建能够反映现场节理分布的离散裂隙网络模型？[Li 2019, pp. 1-3]

## Study Area / Data
研究区为某 **露天石灰岩矿**，现场采用测线法进行节理测绘，获取了节理产状、间距和迹长数据。具体的矿区地理位置、采样规模和节理组数量未从索引片段中确认 [Li 2019, pp. 1, 3-4]。

## Methods
- **产状分形维数计算**：利用简化的等面积施密特投影网格法（基于陈等 2007 的方法），通过VBA代码实现自动网格划分，计算盒计数维数；在“自相似性范围”内通过 ln(*d*)−ln(*N*(*d*)) 斜率的绝对值求得分形维数 *D* [Li 2019, pp. 3-4]。
- **间距与迹长分形描述**：将节理间距数据分段，建立累计数量与间距的 ln−ln 曲线以判断分形特征，据此推导出包含最小间距/迹长值和分形维数的分形概率密度函数 [Li 2019, pp. 4-6]。
- **离散裂隙网络（DFN）建模**：利用 **3DEC 5.0** 内置DFN模块，产状采用 **Fisher 分布**，间距和迹长采用基于分形分布的 FISH 分布（通过 Monte Carlo 方法生成随机数），构建 30 m × 30 m × 30 m 的DFN模型 [Li 2019, pp. 7-8]。
- **模型验证**：通过比较模拟露头与现场数据的节理间距和迹长平均值来评估适用性 [Li 2019, pp. 8-9]。

## Key Findings
- **产状分形维数的优越性**：与 Fisher 参数相比，分形维数能同时反映节理数量和离散程度，是更好的产状分布描述指标，尤其当现场数据不服从 Fisher 分布时 [Li 2019, pp. 8-9]。
- **间距数据的分形特征**：所有节理组的间距均表现出分形模式，通过引入分形维数和最小间距值推导出的分形概率密度函数，能更全面地刻画间距分布，克服了负指数模型忽略不同间距值组成比例的问题 [Li 2019, pp. 4-6]。
- **DFN 建模的适用性**：基于分形理论的DFN模型能够统计性地重现节理分布，模拟数据（如间距、迹长平均值）与现场数据吻合良好 [Li 2019, pp. 8-9]。
- **分形分布函数**：推出了节理间距的分形概率密度函数 *f*(*s*) = *D*<sub>s</sub> *s*<sub>min</sub><sup>*D*<sub>s</sub></sup> *s*<sup>-(*D*<sub>s</sub>+1)</sup>，该函数不受测线长度影响，能更全面地覆盖间距分布信息 [Li 2019, pp. 5-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 分形维数较 Fisher 参数包含更多产状信息（节理数量与离散度） | [Li 2019, pp. 8-9] | 现场产状数据可能不服从 Fisher 分布 | 基于施密特投影的盒计数维数计算 |
| 所有节理组的间距 ln(*N*(*s*))−ln(*s*) 呈线性关系，表明间距具有分形特征 | [Li 2019, pp. 4-5] | 间距数据限制在最小与最大值之间，无需确定自相似范围 | 为分形概率密度函数的推导提供依据 |
| 分形分布模型比负指数分布模型更能表征节理间距，因引入了分形维数和最小间距，能识别不同间距范围的组成比例 | [Li 2019, pp. 5-6] | 比较对象为 Set 1 的间距数据 | 指数模型忽略不同间距值的差异，而分形维数可分辨 |
| 利用分形分布生成的 DFN 模型中，模拟露头的平均节理间距（0.46 m）和迹长（3.73 m）与现场数据（0.35 m 和 3.32 m）一致 | [Li 2019, pp. 8-9] | 模型尺寸 30 m × 30 m × 30 m，模拟域扩大至 ±20 以减小边界效应 | 验证了 DFN 模型的适用性 |

## Limitations
- 产状仅计算了分形维数，未构建适用于 Monte Carlo 模拟的完整分形分布形式，因此 DFN 中产状仍采用 Fisher 分布，未实现基于纯分形参数的产状模拟 [Li 2019, pp. 8-9]。
- 文中提及需进一步研究平均产状与分形维数相结合的描述方法，当前方法的通用性尚未在多种地质条件下验证 [Li 2019, pp. 8-9]。
- 索引片段未提及模型在力学或水力特性模拟中的应用效果。

## Assumptions / Conditions
- **自相似性范围**：产状分形维数计算仅在特定的自相似性/自仿射性范围内有效，该范围通过 ln−ln 图的线性段确定 [Li 2019, pp. 3-4]。
- **间距与迹长上限**：推导分形概率密度函数时，假定最小间距/迹长和分形维数可充分描述分布，且数据本身在统计上具有分形特征 [Li 2019, pp. 4-6]。
- **DFN 模型边界**：模拟域设置为实际模型尺寸的扩大区域，以减少有限尺寸效应 [Li 2019, pp. 7-8]。
- **数据代表性**：现场测绘采用测线法，假设该采样方式能代表岩体的整体节理特征 [Li 2019, pp. 3]。
- **节理形状假设**：DFN 中节理被设为圆形或多边形（具体形状未从索引片段中确认），其大小由迹长推断。

## Key Variables / Parameters
- **产状分形维数 *D***：由 ln(*d*)−ln(*N*(*d*)) 斜率绝对值求得 [Li 2019, pp. 3-4]。
- **间距分形维数 *D*<sub>s</sub>** 和 **迹长分形维数**（未具体命名）：从 ln(*N*(*s*))−ln(*s*) 或 ln(*N*(*l*))−ln(*l*) 曲线拟合得到 [Li 2019, pp. 4-7]。
- **最小间距 *s*<sub>min</sub>**（及最小迹长）：分形概率密度函数的关键参数 [Li 2019, pp. 4-5]。
- **分形概率密度函数**：*f*(*s*) = *D*<sub>s</sub> *s*<sub>min</sub><sup>*D*<sub>s</sub></sup> *s*<sup>-(*D*<sub>s</sub>+1)</sup> [Li 2019, pp. 5]。
- **三维节理密度 *λ*<sub>v</sub>**：由迹长和产状转换得到，用于确定模拟域内的节理数量 [Li 2019, pp. 7]。
- **Fisher 参数**：作为产状分形维数的对比指标 [Li 2019, pp. 1]。

## Reusable Claims
1.  **产状分形维数替代 Fisher 参数**：当现场节理产状不符合 Fisher 分布或需要同时反映节理数量和离散度时，应优先采用等面积施密特投影法计算分形维数，其在信息容量上优于 Fisher 参数 [Li 2019, pp. 1, 8-9]。
2.  **间距分形概率密度函数**：对于具有分形特征的节理间距，可使用 *f*(*s*) = *D*<sub>s</sub> *s*<sub>min</sub><sup>*D*<sub>s</sub></sup> *s*<sup>-(*D*<sub>s</sub>+1)</sup> 进行描述，该函数不受测线长度影响，且能区分不同间距值贡献的差异。适用条件为间距数据在双对数坐标下呈现线性关系（即满足分形律），并需预先确定最小间距和分形维数 [Li 2019, pp. 5-6]。
3.  **DFN 的分形参数输入**：在 3DEC 等平台的 DFN 生成中，利用 FISH 函数实现基于分形累计概率函数的 Monte Carlo 随机数发生器，可生成符合分形分布的节理间距和迹长，比直接使用负指数分布更能反映原始数据的统计结构 [Li 2019, pp. 7-8]。

## Candidate Concepts
- [[fractal geometry]]
- [[jointed rock mass]]
- [[discrete fracture network]]
- [[fractal dimension]]
- [[joint spacing distribution]]
- [[rock mass characterization]]
- [[Schmidt projection]]

## Candidate Methods
- [[equal-area meshing method for orientation fractal dimension]]
- [[Cantor's dust method]]
- [[power-law distribution]]
- [[FISH distribution in 3DEC]]
- [[Monte Carlo simulation for fractal distributions]]
- [[scanline sampling]]

## Connections To Other Work
- 引用了 **Mandelbrot (1983)** 奠定分形几何理论基础 [Li 2019, pp. 2-3]。
- 产状分形维数计算方法基于 **Chen et al. (2007)** 的等面积网格法简化 [Li 2019, pp. 3-4]。
- 间距分形描述与 **Cantor’s dust 方法 (Velde et al., 1991)** 以及 **Liu et al. (2015)** 的二维分形渗透率模型有关联 [Li 2019, pp. 2-3]。
- 主题上可进一步与 [[rock mass rating (RMR)]]、[[rock mass quality (RMQ)]] 的分形评价以及节理粗糙度系数（[[joint roughness coefficient]]) 的分形量化相连接 [Li 2019, pp. 2-3]。
- 可与其他 DFN 建模工作结合，例如 **Lei et al. (2017)** 的耦合行为模拟或 **Oda (1988)** 的代表性单元体方法 [Li 2019, pp. 2, 9-10]。

## Open Questions
- 如何将产状的分形维数与平均产状结合，构建能够直接用于 Monte Carlo 生成的完整分布形式？[Li 2019, pp. 8-9]
- 目前的分形表征方法在更多岩性（非石灰岩）或更大尺度的岩体中的适用性如何？未从索引片段中确认。
- 基于分形DFN的模型在岩体力学、水力学特性模拟中的具体表现及与真实工程响应的对比尚待研究。

## Source Coverage
本页面依据 **8 个索引片段** 编译，覆盖了论文的摘要、引言、方法（产状分形维数、间距/迹长分形描述）、DFN 建模实现及主要结论。片段对研究区细节、具体节理组划分、部分图表数据以及 DFN 验证的详细统计量披露有限。结论部分的远景展望和参考文献列表未完全包含，但不影响核心主张的提取。
