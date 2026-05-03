---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2000-collin-analysis-and-prediction-of-thermal-shock-in-brittle-materials"
title: "Analysis and Prediction of Thermal Shock in Brittle Materials."
status: "draft"
source_pdf: "data/papers/2000 - Analysis and prediction of thermal shock in brittle materials.pdf"
collections:
  - "part2"
  - "zotero new"
citation: "Collin, M., and D. Rowcliffe. “Analysis and Prediction of Thermal Shock in Brittle Materials.” *Acta Materialia*, vol. 48, no. 7, 2000, pp. 1655–1665, doi:10.1016/S1359-6454(00)00011-2."
indexed_texts: "10"
indexed_chars: "47048"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T11:22:39"
---

# Analysis and Prediction of Thermal Shock in Brittle Materials.

## One-line Summary
通过实验与建模，本文研究了压痕淬火法，揭示了残余应力与热应力组合如何控制脆性材料的裂纹扩展，并推导出一个基于断裂韧性的抗热震性能预测公式。

## Research Question
如何使用压痕淬火法分析和预测脆性材料中的热震行为，尤其是裂纹在不同温差下的稳定与失稳扩展机制，并定义抗热震性能的量化指标？[Collin 2000, pp. 1-2]

## Study Area / Data
研究测试了四种材料（细晶氧化铝、碳化硅晶须增韧氧化铝、钛基金属陶瓷、高合金高速钢）制成的板状试样，通过对它们进行Vickers压痕后在不同温差下淬火，测量了约20条裂纹的生长情况，并观察了亚表面裂纹形貌 [Collin 2000, pp. 2-3] [Collin 2000, pp. 3-4]。

## Methods
采用**压痕淬火法**对四种含预制Vickers压痕裂纹的脆性材料试样进行热震实验。通过测量不同温差下的裂纹扩展量，获得裂纹扩展曲线，并划分出三个扩展区域。结合有限差分法计算瞬态热应力，并建立了考虑热应力与残余应力强度叠加的**总应力强度模型**来分析裂纹扩展驱动力 [Collin 2000, pp. 1-2] [Collin 2000, pp. 3-5]。同时，通过假设热冲击断裂应力与压痕板的机械强度等同，利用失稳扩展临界温差估算**表面换热系数** [Collin 2000, pp. 6-7]。

## Key Findings
1.  **裂纹扩展三区域**: 压痕淬火后的裂纹扩展量随温差变化曲线显示出三个区域：在极低温差下无裂纹扩展（区域A），中等温差下稳定扩展（区域B），高于临界温差时不稳定扩展（区域C） [Collin 2000, pp. 1-2]。
2.  **扩展机理**: 裂纹的稳定与失稳扩展由**残余应力和热应力的组合**控制。残余应力的存在使压痕淬火法比其它方法更敏感，也使得定义特定应用的临界温差成为可能 [Collin 2000, pp. 1-2] [Collin 2000, pp. 8-9]。
3.  **抗热震性能预测公式**: 推导出一个基于断裂韧性、热学和力学性能参数的抗热震性能预测公式（失稳扩展临界温差）。该公式强调了**断裂韧性**在定义抗热失效能力中的重要性，其形式为独立的材料本征性能参数，而非常用的工程强度值 [Collin 2000, pp. 1-2] [Collin 2000, pp. 7-8]。
4.  **材料适用性**: 该方法不仅适用于明显脆性的陶瓷，也适用于以开裂形式失效的金属陶瓷和钢材，前提是可以引入压痕预裂纹 [Collin 2000, pp. 1-2] [Collin 2000, pp. 9-10]。
5.  **R曲线行为**: 氧化铝和晶须增韧氧化铝表现出R曲线行为，这可以解释其裂纹的逐步扩展现象，并导致在失稳扩展开始时估算的断裂韧性值高于初始值。金属陶瓷和高速钢未表现出类似行为 [Collin 2000, pp. 8-9] [Collin 2000, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 压痕淬火法裂纹扩展-温差曲线呈现无扩展、稳定扩展、不稳定扩展三个区域 | [Collin 2000, pp. 1-2] [Collin 2000, pp. 3-4] | 试样为含Vickers压痕预裂纹的板片，淬入30°C水中。 | 区域A、B、C的划分是该分析方法的核心。 |
| 失稳扩展临界温差可用于估算表面换热系数 | [Collin 2000, pp. 6-7] | 假设热震断裂时的热应力等同于压痕板的机械强度。 | 该假设是估算表面换热系数的基础。 |
| 总应力强度是热应力强度与残余应力强度之和 | [Collin 2000, pp. 3-5] [Collin 2000, pp. 5-6] | 应用应力强度因子叠加原理。 | 即`K_tot = K_thermal + K_residual`。 |
| 失稳扩展临界温差的预测公式为 `DT_U = A * K_Ic(c_U) * (1 - ν) / (E * a * f_0(b) * sqrt(π*a_U))` | [Collin 2000, pp. 7-8] | 推导时忽略了R曲线对导数的影响，并简化了热应力强度表达式。 | 该公式以断裂韧性`K_Ic`为核心参数，优于以强度`σ_f`为核心的参数。 |
| 氧化铝表现出R曲线行为，其失稳扩展时的估算断裂韧性高于初始值 | [Collin 2000, pp. 8-9] | 未经索引片段确认R曲线的直接测量由本工作完成。 | 初始`K_Ic`为2.93 MPa√m，失稳时估算`K_Ic`为3.96 MPa√m。 |

## Limitations
1.  分析模型**未能解释**在极低温差下裂纹完全不扩展的现象（区域A） [Collin 2000, pp. 8-9]。
2.  预测公式的推导过程中**忽略了R曲线行为的影响**（假设`d(K_Ic(c))/dc = 0`），这可能不适用于所有材料 [Collin 2000, pp. 7-8]。
3.  表面换热系数的估算依赖于“热应力等同于机械强度”的等价假设，这仍未经验证实 [Collin 2000, pp. 6-7]。
4.  `f_0(b)`函数在Bi数极低或极高时的物理行为尚未完全明晰 [Collin 2000, pp. 6-7]。
5.  金属陶瓷的热导率值（6 W/(mK)）远低于文献报道的类似成分材料（12 W/(mK)），其原因未从索引片段中确认 [Collin 2000, pp. 7-8]。

## Assumptions / Conditions
*   **应力强度叠加**: 裂纹尖端的应力强度由热应力和残余应力产生的强度因子线性叠加而成 [Collin 2000, pp. 3-5] [Collin 2000, pp. 5-6]。
*   **热机载荷等价**: 热震导致的裂纹失稳扩展与机械双轴弯曲载荷导致的断裂等价，即热震断裂应力等同于压痕板的弯曲强度 [Collin 2000, pp. 6-7]。
*   **裂纹几何假设**: 在应力强度计算中将裂纹近似为半椭圆形几何，并假设裂纹扩展过程中的形状因子（a/c）为常数（0.8）[Collin 2000, pp. 3-5] [Collin 2000, pp. 7-8]。
*   **材料常数**: 进行预测计算时，假设材料的弹性模量、泊松比、热膨胀系数等为常数，未考虑其随温度的变化，这被认为是区域A无扩展的可能原因之一 [Collin 2000, pp. 8-9]。
*   **残余应力因子**: 假设材料中残余应力因子`χ_surf`和`χ_deep`的关系与玻璃中的类似 [Collin 2000, pp. 5-6]。

## Key Variables / Parameters
*   `ΔT`：淬火温差
*   `ΔT_U`：裂纹失稳扩展临界温差
*   `K_tot`, `K_thermal`, `K_residual`：总应力强度、热应力强度、残余应力强度
*   `K_Ic(c)`：随裂纹长度变化的断裂韧性
*   `c`, `a`：表面裂纹长度和裂纹深度
*   `σ_biax`：含压痕板的双轴弯曲强度
*   `f_0(b)`：与总温差相关的表面最大热应力参数
*   `β`：毕渥数，表征表面传热与内部导热之比
*   `h`：表面换热系数

## Reusable Claims
1.  运用压痕淬火法评估脆性材料抗热震性能时，观察到裂纹扩展曲线的三个分区（无扩展、稳定扩展、失稳扩展），此现象可通过**残余应力与热应力**的叠加效应来解释 [Collin 2000, pp. 1-2]。**限制**: 该模型仅适用于可引入压痕裂纹的材料。
2.  抗热震性能的预测应以材料的**断裂韧性**为依据，而非常用的**工程强度值**。因为强度是评估值而非材料本征参数，且在公式中忽略了初始裂纹尺寸的影响，不适用于机械疲劳研究 [Collin 2000, pp. 7-8]。**证据**: 从热应力与残余应力强度叠加机制推导出以`K_Ic(c_U)`为核心的预测公式。
3.  即使在裂纹扩展受R曲线行为影响的材料中，通过测量失稳扩展临界温差，可以反推出该阶段的有效断裂韧性值 [Collin 2000, pp. 8-9]。**条件**: 该应用建立在热载荷与机械载荷对裂纹驱动力等价的假设之上。

## Candidate Concepts
*   [[thermal shock resistance]]
*   [[indentation fracture mechanics]]
*   [[residual stress intensity factor]]
*   [[R-curve behavior / T-curve behavior]]
*   [[Biot number]]
*   [[surface heat transfer coefficient in quenching]]

## Candidate Methods
*   [[indentation-quench method]]
*   [[Vickers indentation precracking]]
*   [[finite difference method for thermal stress]]
*   [[stress intensity superposition]]
*   [[biaxial bending test for strength evaluation]]
*   [[fractographic analysis of subsurface cracks]]

## Connections To Other Work
*   本文方法是对传统**淬火-强度法**的替代和改进，传统方法通过测量淬火后剩余弯曲强度来确定临界温差 [Collin 2000, pp. 1-2]。
*   文中引入了文献[36]中提出的基于强度的抗热震参数`ΔT_C`，并用基于断裂韧性的新参数替换了它 [Collin 2000, pp. 7-8]。
*   未从索引片段中确认与本工作有具体对比或继承关系的其它特定论文。

## Open Questions
1.  如何解释压痕淬火后在极低温差下（区域A）裂纹完全不扩展的现象？[Collin 2000, pp. 8-9]
2.  金属陶瓷的实际热导率为何远低于文献报道的同类材料值？[Collin 2000, pp. 7-8]
3.  如何通过系统实验（改变材料、压痕载荷、板厚和淬火介质）获得可推广的表面换热系数经验知识？[Collin 2000, pp. 8-9]
4.  有没有替代Vickers压痕的方法在不形成径向裂纹的材料（如大多数高速钢）中引入预裂纹？[Collin 2000, pp. 2-3]

## Source Coverage
本页基于10个索引片段生成，片段覆盖了摘要、引言、材料与方法、部分结果、详细分析、讨论和结论的完整主体章节。覆盖较为全面，包含了核心公式推导、机理模型、关键假设和实验验证的主要论点。尽管覆盖了讨论部分，但可能缺失详细的图表数据和完整的微观结构表征信息。
