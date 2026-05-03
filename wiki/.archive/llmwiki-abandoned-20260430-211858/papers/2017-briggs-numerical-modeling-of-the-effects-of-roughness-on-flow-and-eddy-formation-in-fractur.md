---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur"
title: "Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures."
status: "draft"
source_pdf: "data/papers/2017 - Numerical modeling of the effects of roughness on flow and eddy formation in fractures.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Briggs, Scott, et al. \"Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 9, 2017, pp. 105–15. doi:10.1016/j.jrmge.2016.08.004. Accessed 10 Oct. 2026."
indexed_texts: "13"
indexed_chars: "62044"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:47:25"
---

# Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures.

## One-line Summary
采用格子玻尔兹曼方法模拟人工裂隙与天然白云岩裂隙中的流动，揭示粗糙度引起的涡流生长与有效水力孔径下降，并提出一个与雷诺数相关的三区非线性有效水力传导率模型 [Briggs 2017, pp. 1-1, 5-8]。

## Research Question
裂隙表面粗糙度如何影响流体流动与涡流（eddies）的形成？这些效应如何随雷诺数（Re = 0.01–500）变化并导致有效水力传导率的非线性行为？ [Briggs 2017, pp. 1-1, 1-2, 3-3]。

## Study Area / Data
- **人工裂隙**：采用 SynFrac 软件生成统计自仿射裂隙，分形维数从 2 至 2.35（对应的 Hurst 指数 H = 1～0.65），失配长度设为 15 mm。每个合成裂隙长 100 mm，平均孔径 1.7 mm [Briggs 2017, pp. 5-5]。
- **天然裂隙**：一块含缝合线的白云岩样本，原始尺寸约 350 mm × 250 mm × 70 mm，沿缝合线预开切口后用单轴压缩加载形成裂隙，修剪后尺寸为 280 mm × 210 mm × 70 mm。用 ATOS II 立体地形测量系统获取裂隙表面形貌，所得裂隙孔径分布长约 16 mm，平均孔径约 0.1 mm [Briggs 2017, pp. 3-5]。

## Methods
- **数值方法**：二维格子玻尔兹曼方法（LBM），在 GPU 上使用 CUDA 编程 [Briggs 2017, pp. 3-3]。
- **边界与驱动力**：左右边界采用周期边界条件以模拟无限域，消除入口/出口效应；流体仅受重力驱动，重力加速度以局部速度增量形式加入 [Briggs 2017, pp. 3-3]。
- **有效水力孔径**：由 LBM 模拟的流量与重力驱动立方定律反算有效水力孔径 [Briggs 2017, pp. 3-3]。
- **非线性分析**：计算 Forchheimer 方程（\(i = a_1 q + b q^2\)）与 Izbash 方程（\(i = c q^\beta\)）的拟合参数，以表征非线性流动 [Briggs 2017, pp. 3-5]。
- **涡流识别**：通过流速场分析涡流区域及其体积随 Re 的变化，定义涡流体积分数以量化二次流 [Briggs 2017, pp. 5-6, 6-8]。

## Key Findings
- **有效水力孔径与 Re 的关系**：在 Re < 1 时，所有裂隙的有效水力孔径几乎不变，流动近似遵循立方定律；Re > 1 时，有效孔径开始降低，且降低速率随粗糙度增大而加快 [Briggs 2017, pp. 5-6]。
- **三区非线性模型**：随 Re 增加，裂隙流呈现三个区域：I 区（Re 很低）线性达西流；II 区涡流快速增长，与非线性偏差的开始重合；III 区涡流增长速率因几何约束而减缓。这一模型在合成裂隙和天然白云岩裂隙中均得到证实 [Briggs 2017, pp. 1-1, 1-2, 6-8]。
- **涡流与粗糙度**：粗糙度越大，相同 Re 下涡流体积越大，有效水力传导率越低。涡流使流动脱离主流，减小了有效过流断面 [Briggs 2017, pp. 1-1, 5-6]。
- **Forchheimer 与 Izbash 拟合**：在高 Re 的 III 区，水力梯度与流量之间可用 Forchheimer 方程描述；Izbash 方程中的幂律关系在 I、II 区为线性，在 III 区变为非线性 [Briggs 2017, pp. 6-8]。
- **天然裂隙的适用性**：白云岩裂隙在较高 Re 下也表现出三区非线性有效孔径关系，但涡流增长在 Re ≈ 50 处出现反弹，这仍受几何限制，三区模型仍合理 [Briggs 2017, pp. 6-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 有效水力孔径比（有效孔径/平均孔径）在 Re < 1 时几乎恒定，Re > 1 时开始下降 | [Briggs 2017, pp. 5-6] | 2D LBM，重力驱动，周期边界，Re=0.01-500 | 所有粗糙度裂隙均表现出此趋势，粗糙度越大下降越快 |
| 涡流体积分数随 Re 增长，在 Re≈1 以下接近零，随后快速增长，再后增长趋缓，表现出三区特征 | [Briggs 2017, pp. 6-8] | 合成裂隙（H=0.65），白云岩裂隙 | 白云岩裂隙在 Re≈50 处出现反弹，但总体趋势符合三区模型 |
| Forchheimer 拟合参数 \(a_1\) 和 \(b\) 受粗糙度影响，粗糙度越大，非线性系数越大 | [Briggs 2017, pp. 6-8, Table 2] | 最光滑与最粗糙合成裂隙对比 | 仅部分结果展示于片段，完整数据见原文表2 |
| 相同平均孔径下，粗糙裂隙的有效水力孔径小于光滑裂隙，表明二次流占比更大 | [Briggs 2017, pp. 5-6] | 合成裂隙，Hurst 指数 1 到 0.65 | 支持“涡流占据体积导致有效孔径减小”的机制 |

## Limitations
- 模拟均为二维，未考虑三维迁曲度或横向粗糙度效应 [Briggs 2017, pp. 3-3, 6-8]。
- 周期边界条件虽可代表无限域，但可能不能准确再现现场裂隙的流入/流出条件 [Briggs 2017, pp. 3-3]。
- 雷诺数最高只到 500，未覆盖向完全湍流转捩的更高 Re 范围 [Briggs 2017, pp. 3-3, 6-8]。
- 人工裂隙与天然白云岩裂隙的尺度、平均孔径均不同（合成裂隙长 100 mm、孔径 1.7 mm；天然裂隙长 16 mm、孔径 0.1 mm），表面特性并未专门匹配 [Briggs 2017, pp. 6-8]。
- 天然裂隙仅包含一块白云岩样本，无法推广至其他岩性或裂隙类型。

## Assumptions / Conditions
- 流动为二维不可压缩等温流动，满足 LBM 的 D2Q9 模型 [Briggs 2017, pp. 3-3]。
- 周期边界条件使模型代表裂隙网络中的一段单元，忽略宏观压差与端部效应 [Briggs 2017, pp. 3-3]。
- 重力是唯一的驱动力，无其他体积力或压力边界 [Briggs 2017, pp. 3-3]。
- 有效水力孔径通过重力驱动下的立方定律反算，假定平行板流动关系在局部适用 [Briggs 2017, pp. 3-5]。
- SynFrac 人工裂隙的分形特性由 Hurst 指数（或分形维数）和失配长度控制，且失配长度基于 Brown et al. (1995) 方法设为 15 mm [Briggs 2017, pp. 5-5]。

## Key Variables / Parameters
- **雷诺数 (Re)**：0.01–500，基于平均孔径与平均流速 [Briggs 2017, pp. 1-1]。
- **有效水力孔径**：由立方定律从 LBM 流量反推 [Briggs 2017, pp. 3-5]。
- **Hurst 指数 H / 分形维数**：控制合成裂隙粗糙度，H 从 1 到 0.65，对应分形维数 2 到 2.35 [Briggs 2017, pp. 5-5]。
- **角阈值 (Angular threshold)**：SynFrac 生成的表面粗糙度度量，H=0.65 时为 27.29°，H=1 时为 9.62° [Briggs 2017, pp. 5-6, Table 1]。
- **涡流体积分数**：量化二次流区域占总孔隙体积的比例 [Briggs 2017, pp. 6-8]。
- **Forchheimer 系数 \(a_1\) (线性项)、\(b\) (非线性项)** [Briggs 2017, pp. 3-5, 6-8]。
- **Izbash 系数 \(c\) 与指数 \(\beta\)** [Briggs 2017, pp. 3-5, 6-8]。
- **LBM 弛豫参数 \(s\)** 或晶格粘度 \(\nu_L\)：控制流体粘度 [Briggs 2017, pp. 3-3]。

## Reusable Claims
- **粗糙度-涡流-传导率关联**：在粗糙裂隙中，增大粗糙度会增大相同 Re 下的涡流体积，从而降低有效水力孔径和有效水力传导率。此关系在 Re > 1 的层流非线性区间成立，且适用于人工自仿射裂隙和白云岩裂隙 [Briggs 2017, pp. 1-1, 5-6]。
- **三区非线性有效孔径模型**：裂隙流动的有效水力孔径（或破坏线性关系的偏差）可划分为三个 Re 区间：I 区（Re 很低）有效孔径恒定；II 区有效孔径随涡流快速增长而下降；III 区涡流增长受限，有效孔径下降速率减缓。该模型可用于表征从线性到惯性效应主导的流动转折，且已在统计生成裂隙与天然裂隙中得到验证 [Briggs 2017, pp. 1-1, 6-8]。
- **Forchheimer 方程适用条件**：在 III 区（合成裂隙中约 Re > 30），水力梯度与比流量之间的非线性关系可用 Forchheimer 方程稳定描述，粗糙度对系数 \(a_1\) 和 \(b\) 均有影响 [Briggs 2017, pp. 6-8]。
- **Izbash 方程适用条件**：Izbash 幂律关系可区分线性区（I、II 区，指数接近 1）和非线性 III 区（指数偏离 1），粗糙度越大非线性偏离越早 [Briggs 2017, pp. 6-8]。
- **周期边界条件下的 LBM 应用**：对粗糙裂隙的单段，采用周期边界与重力驱动 LBM，可避免进口段效应并有效逼近无限裂隙网络中的流场，适用于研究局部二次流与宏观压降关系，但需注意对真实裂隙入口/出口条件的代表性有限 [Briggs 2017, pp. 3-3]。
- **粗糙度对临界 Re 的影响**：在粗糙裂隙中，线性流动偏离的临界 Re 大约为 1；这与 Brush and Thomson (2003) 关于局部立方定律在 Re < 1 时偏差最小的结论一致 [Briggs 2017, pp. 1-2]。

## Candidate Concepts
- [[fracture flow]]
- [[fracture roughness]]
- [[eddy formation]]
- [[effective hydraulic aperture]]
- [[nonlinear flow]]
- [[Forchheimer equation]]
- [[Izbash equation]]
- [[three-zone model]]
- [[Hurst exponent]]
- [[fractal dimension]]
- [[local cubic law]]
- [[rough fracture hydrogeology]]

## Candidate Methods
- [[lattice Boltzmann method (LBM)]]
- [[CUDA GPU computing]]
- [[periodic boundary conditions]]
- [[SynFrac fracture generation]]
- [[Forchheimer analysis]]
- [[Izbash analysis]]
- [[cubic law effective aperture calculation]]
- [[gravity-driven flow simulation]]

## Connections To Other Work
- 与 Brush and Thomson (2003) 的研究关联：两者均检验了粗糙裂隙中局部立方定律的有效性，均发现 Re < 1 时偏差很小。Briggs 等的结果进一步扩展到更高 Re 并建立了三区模型 [Briggs 2017, pp. 1-2]。
- 与 Skjetne et al. (1999) 的关联：Skjetne 等首次提出了基于 Darcy、弱惯性、强惯性的三流态划分。本研究继承并明确了涡流增长是流态转换的直接原因，且将其与有效水力孔径变化定量关联 [Briggs 2017, pp. 1-2]。
- 与 Chaudhary et al. (2011, 2013) 的关联：Chaudhary 等在孔隙介质中提出水力传导率随 Re 变化的三区模型。本研究将其应用于粗糙裂隙，并证实涡流生长速率的变化是该模型的基础 [Briggs 2017, pp. 1-2]。
- 与 Zou et al. (2015) 的关联：Zou 等发现小尺度粗糙度增加涡流复杂性。本研究确认，包含完整粗糙度谱的裂隙比仅考虑大尺度特征的模型具有更强烈的二次流发展 [Briggs 2017, pp. 5-6]。
- 与 Bouquain et al. (2012) 的关联：其理想正弦型孔隙中的涡流体积分数较相同 Re 下的粗糙裂隙更小，说明裂隙的突变通道几何更易诱发大范围二次流 [Briggs 2017, pp. 5-6]。

## Open Questions
- 本研究中三区模型和涡流动力学是否在三维裂隙中仍然保持？二维结果可能高估或低估了流动通道化与涡流体积 [Briggs 2017, pp. 3-3]。
- Re > 500 后，涡流发展与湍流转捩对三区模型的适用性有何影响？未从索引片段中确认。
- 不同应力条件下（如法向加载改变孔径）粗糙度-涡流-传导率的关系如何变化？未从索引片段中确认。
- 天然裂隙表面的化学非均匀性和充填物如何耦合粗糙度效应？本研究仅考虑几何粗糙度。

## Source Coverage
本页面基于论文的 13 个索引片段，覆盖了摘要、引言（文献回顾）、方法（LBM 设置、裂隙生成）、结果（涡流可视化、三区分析、Forchheimer/Izbash 拟合）和部分讨论。片段提供了主要发现、关键定量结果及模型参数表（表1和部分表2、3），但可能存在以下遗漏：完整结果表格（如 Forchheimer 参数的完整对比）、更多天然裂隙细节（如白云岩的完整表面测量数据）、对数值收敛性和网格分辨率的讨论、以及对非达西现象更深入的理论分析。文中未涉及的潜在重要信息标注为“未从索引片段中确认”。
