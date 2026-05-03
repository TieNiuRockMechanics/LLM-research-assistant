---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture"
title: "Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Relationship between box-counting fractal dimension and properties of fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Shaoqun Dong, et al. \"Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.\" *Unconventional Resources*, vol. 4, 2024, p. 100068. Accessed 2026."
indexed_texts: "12"
indexed_chars: "57552"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:24:29"
---

# Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.

## One-line Summary
该研究采用多元分析方法，针对三类二维离散裂缝网络，建立了用裂缝属性（数量、长度、方向）预测盒计数分形维数(D)的有理函数公式，并验证了其高拟合精度 [Shaoqun 2024, pp. 1-1, 5-11]。

## Research Question
如何量化裂缝网络的多种属性（裂缝长度、数量、方向）对盒计数分形维数(D)的综合影响，并建立一个能够预测D的多元关系式？ [Shaoqun 2024, pp. 1-1, 2-3]。

## Study Area / Data
- **模拟区域**：二维正方形区域，尺寸为100 m × 100 m [Shaoqun 2024, pp. 3-5]。
- **裂缝网络模型**：通过离散裂缝网络（DFN）建模生成合成裂缝网络，共分为三种类型：
    1. 恒定裂缝长度、随机（各向同性）方向 [Shaoqun 2024, pp. 1-1, 5-7]。
    2. 指数分布裂缝长度、随机方向 [Shaoqun 2024, pp. 1-1, 7-9]。
    3. 指数分布裂缝长度、von-Mises分布（各向异性）方向 [Shaoqun 2024, pp. 1-1, 10-11]。
- **重复实现**：部分分析中使用了多次（如20次）随机实现以计算平均值和标准差 [Shaoqun 2024, pp. 7-9]。

## Methods
- **离散裂缝网络 (DFN) 建模**：使用基于标记点过程 (MPP) 的随机模拟方法生成二维裂缝网络 [Shaoqun 2024, pp. 2-3]。裂缝位置由点过程（如泊松过程）确定，裂缝属性（长度服从给定分布，方向服从给定函数）由标记过程确定 [Shaoqun 2024, pp. 2-3]。
- **盒计数分形维数 (D) 计算**：通过对覆盖裂缝网络的网格进行层次化缩放和计数，计算被裂缝占据的盒子数，然后对 `log(N)` 与 `log(1/r)` 进行线性拟合，其斜率即为分形维数 D [Shaoqun 2024, pp. 3-5]。
- **多元分析**：首先进行单变量分析，分别探究D与单个属性（如裂缝数量n、恒定长度L）的关系，观察到它们可用有理函数（`y = (ax + b)/(x + c)`）拟合 [Shaoqun 2024, pp. 5-7]。基于此，提出D与多个属性之间的关系可由包含交叉项的有理函数表示，并利用模拟数据进行曲面拟合以验证假设 [Shaoqun 2024, pp. 2-3, 7-9, 9-10]。

## Key Findings
- **单变量关系**：对于恒定裂缝长度和随机方向的网络，D与裂缝数量(n)和裂缝长度(L)的关系均可由有理函数 `D = (a1*x + a2) / (x + a3)` 很好地表达。D随n或L的增加而增加，但在n或L值较低时增速快，值较高时增速放缓 [Shaoqun 2024, pp. 5-7]。
- **多元预测公式-情况1**：对于恒定长度(L)和随机方向的网络，D与(n, L)的关系可以准确地由形如 `D = (c1 n + c2 L + c3 nL + c4) / (n + c5 L + c6 nL + c7)` 的有理函数拟合，拟合的相关系数大于0.999，均方根误差为0.0152 [Shaoqun 2024, pp. 7-9]。
- **多元预测公式-情况2**：对于指数分布长度和随机方向的网络，D与裂缝数量(n)和平均长度的倒数(1/λ)的关系同样可由类似的有理函数（公式9）高精度拟合，相关系数大于0.999，均方根误差为0.0141 [Shaoqun 2024, pp. 9-10]。
- **方向影响**：对于指数分布长度和von-Mises方向的网络，用一个集中度参数(κ)量化方向各向异性。D与κ的关系可由有理函数（公式10）描述。当κ较小时（方向更集中），对于相同(n, 1/λ)的裂缝网络，其D值通常更大 [Shaoqun 2024, pp. 10-11]。
- **拟合残差模式**：当裂缝数量少或长度短时，D的预测残差相对较大。这是因为在精细网格尺度下，稀疏的裂缝结构占据的网格单元较少，随网格尺度增大其结构会快速扭曲或消失 [Shaoqun 2024, pp. 7-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| D与裂缝数量(n)和恒定长度(L)的单变量关系可用有理函数 `y = (ax+b)/(x+c)` 拟合。 | [Shaoqun 2024, pp. 5-7] | 二维DFN，恒定裂缝长度，随机方向。 | 当n或L较低时D增加快，高时增加慢。 |
| D = f(n, L)的多元关系式（公式6）拟合效果极佳，相关系数>0.999，均方根误差0.0152。 | [Shaoqun 2024, pp. 7-9] | 二维DFN，恒定裂缝长度，随机方向，100m×100m区域。 | 残差在n小或L短时较大。 |
| D = f(n, 1/λ)的多元关系式（公式9）拟合效果极佳，相关系数>0.999，均方根误差0.0141。 | [Shaoqun 2024, pp. 9-10] | 二维DFN，指数分布裂缝长度，随机方向。 | |
| D与方向集中度参数(κ)的平均关系可用有理函数（公式10）描述，相关系数0.9953。 | [Shaoqun 2024, pp. 10-11] | 二维DFN，指数分布裂缝长度，von-Mises方向，多次实现后取平均。 | 关系在小实现次数时不明显，随实现次数增加而明晰。 |
| 当方向集中度参数(κ)较小时，在相同(n, 1/λ)下，D值通常更大。 | [Shaoqun 2024, pp. 10-11] | 二维DFN，指数分布裂缝长度，von-Mises方向。 | |

## Limitations
- 该研究仅基于二维合成裂缝网络模型，其结果向三维真实裂缝网络的适用性未从索引片段中确认。
- 研究区域为固定的100m × 100m正方形，区域尺寸对结论的影响未从索引片段中确认。
- 部分关键关系的推导依赖于特定的概率分布假设（如指数长度分布、von-Mises方向分布），对其它分布的普适性未从索引片段中确认。

## Assumptions / Conditions
- **模型**：二维离散裂缝网络，裂缝被简化为线段 [Shaoqun 2024, pp. 2-3]。
- **生成过程**：裂缝中心位置由点过程（如泊松过程）模拟，属性（长度、方向）由其各自的概率分布函数独立生成 [Shaoqun 2024, pp. 2-3]。
- **实验设置**：
    - 模拟区域：100m × 100m方形区域 [Shaoqun 2024, pp. 3-5]。
    - 裂缝密度P20与裂缝数量n成正比：`P20 = n / 10^4` [Shaoqun 2024, pp. 5-7]。
- **三种分析场景**：
    1. 恒定裂缝长度，随机（均匀）方向 [Shaoqun 2024, pp. 5-7]。
    2. 指数分布裂缝长度，随机（各向同性）方向 [Shaoqun 2024, pp. 7-9]。
    3. 指数分布裂缝长度，von-Mises分布（各向异性）方向 [Shaoqun 2024, pp. 10-11]。
- **公式假设**：多元关系可用包含交叉项的有理函数（公式6、9、11）有效拟合，该假设基于单变量有理函数关系的观察 [Shaoqun 2024, pp. 2-3]。

## Key Variables / Parameters
- **D**：盒计数分形维数（目标变量） [Shaoqun 2024, pp. 1-1]。
- **n**：裂缝数量 [Shaoqun 2024, pp. 5-7]。
- **L**：恒定裂缝长度 [Shaoqun 2024, pp. 5-7]。
- **1/λ**：指数分布裂缝长度的平均值 [Shaoqun 2024, pp. 7-9]。
- **κ**：von-Mises方向分布的集中度参数，值越小表示方向越集中 [Shaoqun 2024, pp. 10-11]。
- **P20**：裂缝密度 (`P20 = n/10^4`) [Shaoqun 2024, pp. 5-7]。

## Reusable Claims
- **Claim 1**：在二维DFN中，若裂缝长度恒定且方向随机，则盒计数分形维数D与裂缝数量n和长度L的单变量关系均可用有理函数 `y = (ax+b)/(x+c)` 精确描述。**适用条件**：二维DFN模型，n∈[130, 970] 步长40， L∈[7, 95] 步长2的离散取值范围。**证据**：[Shaoqun 2024, pp. 5-7] 图6展示并拟合了D vs. n 和 D vs. L 的曲线。**限制**：外推到该参数范围之外需谨慎；对三维网络不一定成立。
- **Claim 2**：盒计数分形维数D与裂缝数量n和恒定长度L的综合关系可由公式 `D = (c1 n + c2 L + c3 nL + c4) / (n + c5 L + c6 nL + c7)` 高精度拟合（R^2>0.999, RMSE=0.0152）。**适用条件**：二维DFN，恒定裂缝长度，随机方向。**证据**：[Shaoqun 2024, pp. 7-9] 图8a-c展示了拟合曲面、残差图和交叉图。**限制**：在低裂缝数量或较短裂缝长度时残差较大。
- **Claim 3**：当裂缝长度服从指数分布且方向随机时，D可由以n和1/λ为变量的有理函数（公式9）高精度拟合（R^2>0.999, RMSE=0.0141）。**适用条件**：二维DFN，裂缝长度服从指数分布，方向随机。**证据**：[Shaoqun 2024, pp. 9-10] 图12a-c展示了拟合曲面、残差和交叉图。**限制**：在n或1/λ值较小时残差较大。
- **Claim 4**：对于具有各向异性方向（von-Mises分布）的DFN，在相同裂缝数量和平均长度下，方向越集中（κ值越小），其盒计数分形维数D通常越大。**适用条件**：二维DFN，采用指数长度和von-Mises方向分布。**证据**：[Shaoqun 2024, pp. 10-11] 比较κ=5和κ=41.9时的D轮廓。**限制**：结论从特定参数κ的对比得出。

## Candidate Concepts
- [[fracture network]]
- [[box-counting fractal dimension]]
- [[discrete fracture network (DFN)]]
- [[marked point process]]
- [[fracture connectivity]]
- [[permeability of fractured rock mass]]
- [[percolation threshold]]
- [[synthetic fracture network]]

## Candidate Methods
- [[discrete fracture network modeling]]
- [[box-counting method]]
- [[Monte Carlo simulation]]
- [[multivariate analysis]]
- [[rational function fitting]]

## Connections To Other Work
- 索引片段提到，已有大量研究探究了分形维数与单个裂缝网络属性（如连通性、渗透率）之间的关系 [Shaoqun 2024, pp. 1-1]。
- 片段指出，二维和三维裂缝网络的数值模拟显示，逾渗阈值的确定依赖于分形维数和另外两个参数 [Shaoqun 2024, pp. 1-2]。
- 片段引用了先前研究，指出裂缝交点和裂缝线的盒计数分形维数与无因次密度之间存在非线性直接关系 [Shaoqun 2024, pp. 1-2]。
- 该研究与使用分形维数预测裂缝网络渗透率的研究主题相关 [Shaoqun 2024, pp. 1-2]。

## Open Questions
- 本研究提出的多元有理函数预测公式，对于三维裂缝网络是否依然有效？
- 能否将预测公式从合成裂缝网络推广到复杂的真实裂缝网络？
- 对于其他未测试的概率分布（如正态分布、幂律分布）的裂缝长度和方向，该方法的拟合优度如何？
- 除了长度、数量和方向，其他裂缝属性（如开度、空间相关性）如何融入此预测框架？
- 当研究区域尺寸（len）发生变化时，预测公式是否需要修正？

## Source Coverage
本页基于论文提供的12条索引片段写作。片段覆盖了文章标题、摘要、方法原理（DFN建模、盒计数维数计算）、实验设置以及第3节中的全部三种分析场景的关键结果、图表及公式（公式3-11）。覆盖内容详细，主要集中在方法论和核心实验结果。引言的完整文献综述、第4节（讨论）和第5节（结论）的具体细节、以及所有图表和公式的完整参数表未能从片段中全部确认。
