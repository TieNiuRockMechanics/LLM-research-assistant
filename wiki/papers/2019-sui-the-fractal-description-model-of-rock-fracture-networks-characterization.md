---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-sui-the-fractal-description-model-of-rock-fracture-networks-characterization"
title: "The Fractal Description Model of Rock Fracture Networks Characterization."
status: "draft"
source_pdf: "data/papers/2019 - The fractal description model of rock fracture networks characterization.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Sui, Lili, et al. \"The Fractal Description Model of Rock Fracture Networks Characterization.\" *Chaos, Solitons and Fractals*, vol. 129, 2019, pp. 71-76."
indexed_texts: "8"
indexed_chars: "37813"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "37359"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.987994"
coverage_status: "full-index"
source_signature: "788e0875a12bf8a111847889461e125b1c3ca067"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:34:14"
---

# The Fractal Description Model of Rock Fracture Networks Characterization.

## One-line Summary
针对传统分形维数在岩石断裂网络量化中不稳定、依赖回归等问题，提出一种基于分形自相似性和头/尾分割法的简单分形指数（SFI），并在两个二维煤断裂样本上验证其有效性、简便性和稳定性。

## Research Question
如何克服现有传统几何与分形方法（如盒计数维数、立体学法）在量化岩石断裂网络时的缺陷——包括分形维数计算不稳定、最小二乘回归偏差大、2D–3D关系不确定——以建立一种更准确、更稳定且便于工程实践的断裂网络描述方法？

## Study Area / Data
使用来自 Jafari 和 Babadagli（2012）文献中的两幅二维岩石断裂网络图像（图3），分别记为 (a) 和 (b)，图像尺寸分别为 364×217 像素和 408×324 像素[Sui 2019, pp. 4-5]。图像经过对比度调整和二值化处理，转换为矢量图，并在 ArcGIS 10.0 中利用 Axwoman 扩展模块按预定规则进行断裂识别与长度分级。

## Methods
1. **断裂识别规则**：从任意点开始追踪，若连接断裂间夹角不超过45°，则较长者视为一条断裂；若超过45°，则“长直”断裂被计入（直断裂定义为整条断裂转弯角度不超过45°）。该规则保证断裂分级的一致性[Sui 2019, pp. 4-5]。
2. **头/尾分割（ht break）原理**：基于分形集合中“小碎片远多于大碎片”的重尾分布特征，将数据按均值分割为“头”（少量大值）和“尾”（大量小值），保留尾部而非头部（因尾部微小断裂对岩石可压裂性关键），递归分割至不再出现该模式，得到层级结构[Sui 2019, pp. 3-4]。
3. **简单分形指数（SFI）计算**：对最后两步尾部分：
   - 计算均值 `mean1`、`mean2` 及累积量 `sum1`、`sum2`，令 `r = mean1 / mean2`。
   - 计算数量比 `N = (N_t / mean1) / N_2`，其中 `N_t` 为倒数第二步尾部分的总断裂数，`N_2` 为最后一步尾部分的断裂数。
   - 则 `SFI = ln N / ln r`[Sui 2019, pp. 4]。
4. **与传统分形维数对比**：该方法无需极限回归，避免最小二乘法引起的取值区间不稳定问题，且因保留了尾部而更能表征整体复杂性。

## Key Findings
- 对图 (a) 和 (b) 计算得到的 SFI 分别为 1.59 和 1.60，表明 (b) 的断裂网络更复杂，符合视觉判断和分形特征[Sui 2019, pp. 4-5]。
- SFI 计算过程直接、稳定，无传统分形维数的回归区间选择问题，且能捕捉分形集合的层级动态[Sui 2019, pp. 5]。
- 头/尾分割法应用于断裂识别后的层级结构分离，有效实现了“以小见大”的描述，并降低计算步骤[Sui 2019, pp. 4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SFI₁ = 1.59，SFI₂ = 1.60，对应两幅2D断裂网络 | Sui 2019, pp. 4-5 | 断裂图像来自 Jafari & Babadagli (2012)；识别规则：夹角≤45°；图像已二值化 | SFI 值越大网络越复杂，与分形本质一致；验证方法有效 |
| 3次迭代 Koch 曲线的 ht 指数 = 3 | Sui 2019, pp. 3-4 | 84个线段（长度1/3、1/9、1/27） | 展示头/尾分割程序 |
| 断裂取向常服从 Fisher 或 Bingham 分布，优于指数/正态分布 | Sui 2019, p. 2 | 基于现场测量统计，Deshowitz (1988) 对比结果 | 引用 [17, 20, 18, 19, 22] |
| 盒计数分形维数随回归时段而异，导致不稳定 | Sui 2019, pp. 1-2 | 不同分形维数计算方法比较 | 赵等 (2011)；乔等 (2015) |
| 立体学关系：a_3D = a_1D + 2，但分形维数关系 D_{d-1} 不稳定（有时 = D_d - 1，有时 = d - 1） | Sui 2019, p. 3 | 基于幂律长度分布；由 Davy 等 (1990) 提出 | 不稳定性阻碍工程应用 |
| 渗透率预测方程：Ln(K) = A exp(B X₁) + C Ln(X₂) + D Ln(X₃) + E，X₁连接性指数，X₂水力传导率，X₃断裂线盒计数维数 | Sui 2019, p. 3 | 非线性多元回归；出自 Jafari & Babadagli (2012) | 相关系数最高；神经网络进一步提升估算精度 |

## Limitations
- 文中所提 SFI 方法仅涉及断裂分形量化，并未建立 SFI 与岩石渗透率、可压裂性等工程参数间的具体关系；SFI 仍是一个单纯的数值指标，后续应用需开展相关性分析[Sui 2019, pp. 5]。
- 分形维数定义过于严格，导致其普遍性不足；实践中使用的近似值会放大断裂网络重构的误差[Sui 2019, pp. 3]。
- 立体学方法给出的 2D–3D 分形维数关系随长度分布指数 `a` 变化而不稳定，难以直接用于工程预测[Sui 2019, pp. 3]。
- 断裂识别规则依赖 45° 阈值，不同阈值可能影响分级结果，其敏感性未讨论。

## Assumptions / Conditions
- 岩石断裂网络具有统计自相似性和重尾分布，即“小碎片远多于大碎片”，这是头/尾分割法适用的前提[Sui 2019, pp. 3-4]。
- 断裂识别假定相连断裂夹角 ≤ 45° 时属于同一断裂，且全程转弯 ≤ 45° 视为直断裂，较长断裂优先识别[Sui 2019, pp. 4-5]。
- 图像预先经过二值化处理并转换为矢量图，以减少噪声干扰。
- SFI 计算中尾部分割保留代表整体特征的微小断裂，而舍弃头部少量大断裂，这一处理基于微小断裂对工程性质影响更大的认识。

## Key Variables / Parameters
- **SFI（Simple Fractal Index）**：`SFI = ln N / ln r`，综合反映断裂规模与数量的层级比。
- **N**：数量比，`N = (N_t / mean1) / N_2`，其中 `N_t` 为倒数第二步尾部分总断裂数，`mean1` 为其均值，`N_2` 为最后一步尾部分断裂数。
- **r**：均值比，`r = mean1 / mean2`，`mean1`、`mean2` 分别为倒数第二步和最后一步尾部分的平均长度。
- **头/尾分割迭代次数**：等于 `ht 指数 - 1`，反映层级深度。
- **断裂长度**：通过 ArcGIS 识别并分级的线段长度（像素单位）。
- **角度阈值 45°**：用于判断断裂连续性的经验值。

## Reusable Claims
- 基于头/尾分割的简单分形指数（SFI）可以避免最小二乘回归引起的偏差，提供比传统盒计数分形维数更稳定的岩石断裂网络量化结果[Sui 2019, pp. 4-5]。适用条件：断裂网络需呈现自相似重尾分布；需先行识别与分级。
- 传统盒计数分形维数因回归时间段选择不同，其数值和变化趋势均可能改变，故在工程实践中计算结果不稳定，容易引入误差[Sui 2019, pp. 1-2]。此结论基于赵等（2011）及乔等（2015）的研究。
- 断裂取向的统计分布以 Fisher 分布和 Bingham 分布拟合效果更佳，优于指数或正态分布；这一结果为岩体结构面图生成与预测提供依据[Sui 2019, pp. 2]。
- 以 45° 为转角阈值并结合“长直优先”规则，能够有效从二值化断面图像中提取断裂层级结构，为头/尾分割提供可靠输入[Sui 2019, pp. 4-5]。该规则来源于 Jafari & Babadagli (2012) 图像数据。

## Candidate Concepts
[[fracture network]], [[fractal dimension]], [[self-similarity]], [[head/tail break]], [[heavy-tailed distribution]], [[simple fractal index]], [[fracture orientation distribution]], [[Fisher distribution]], [[Bingham distribution]], [[box-counting dimension]], [[stereological analysis]], [[fracture density]], [[permeability estimation]], [[connectivity index]], [[power-law length distribution]]

## Candidate Methods
[[head/tail break method]], [[simple fractal index calculation]], [[box counting]], [[scanline method]], [[yardstick method]], [[spectrum method]], [[least squares regression in fractal dimension]], [[ArcGIS-based fracture extraction]], [[Axwoman extension]], [[stereological 2D-3D conversion]], [[binary image vectorization]]

## Connections To Other Work
- 在 Barton (1985) 首次发表二维天然断裂迹长分形测量之后发展而来，其量化思想与 Barton 的工作一脉相承，但通过引入头/尾分割改进了计算的稳定性和准确性[Sui 2019, pp. 1, 3]。
- 对 Darcel 等 (2003) 提出的立体学关系（`a_3D = a_1D + 2`）进行了评述，指出其分形维关系的非唯一性（有时 `D_{d-1} = D_d - 1`，有时 `D_{d-1} = d - 1`），强调了 2D 信息升维至 3D 的困难[Sui 2019, pp. 3]。
- 直接使用了 Jafari & Babadagli (2012) 中的断裂网络图像作为验证样本，同时评述了其基于多参数的渗透率回归方程和神经网络改进估算[Sui 2019, pp. 3, 4-5]。
- 继承了 Jiang (2013, 2014) 提出的 ht 指数和头/尾分割的概念，但创新地将保留对象从“头”改为“尾”，以适应岩石断裂中微小裂隙的重要性[Sui 2019, pp. 3-4]。

## Open Questions
- SFI 与岩石渗透率、可压裂性、孔隙率等工程特性之间的定量映射关系尚待建立[Sui 2019, pp. 5]。
- 如何利用二维 SFI 可靠地推断三维断裂网络的分形特征，目前立体学关系仍不稳定，需进一步辨识[Sui 2019, pp. 3, 5]。
- 断裂识别规则（如角度阈值、图像处理参数）对 SFI 的敏感性及其影响规律有待研究。
- 该方法在更大规模、多类型岩石（如火成岩、变质岩）中的适用性未经验证。

## Source Coverage
所有 8 个非空索引片段均已处理。来源字符覆盖率约 98.8%，片段覆盖率 100%。具体审核数据：indexed_texts=8, compiled_source_blocks=8, coverage_ratio_by_chars=0.987994, coverage_ratio_by_blocks=1.0。
