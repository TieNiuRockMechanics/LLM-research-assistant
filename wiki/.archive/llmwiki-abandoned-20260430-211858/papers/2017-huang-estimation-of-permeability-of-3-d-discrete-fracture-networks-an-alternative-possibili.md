---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-huang-estimation-of-permeability-of-3-d-discrete-fracture-networks-an-alternative-possibili"
title: "Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis."
status: "draft"
source_pdf: "data/papers/2017 - Estimation of permeability of 3-D discrete fracture networks An alternative possibility based on trace map analysis.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Huang, Na, et al. \"Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis.\" *Engineering Geology*, vol. 226, 2017, pp. 12-19. doi:10.1016/j.enggeo.2017.05.005."
indexed_texts: "9"
indexed_chars: "43334"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:32:18"
---

# Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis.

## One-line Summary
本研究基于对84个三维和672个二维离散裂隙网络（DFN）模型的分析，提出了一种利用二维切面（trace maps）的渗透率并结合三维几何参数来预测三维裂隙网络渗透率的多元回归函数 [Huang 2017, pp. 1-2].

## Research Question
如何利用更容易获取的二维裂隙网络（如露头 trace maps）的信息，结合关键的三维几何参数，来准确预测三维离散裂隙网络（DFN）的渗透率？因为直接使用二维渗透率近似三维渗透率会在量级和方向上产生显著误差，而三维表征和计算成本又很高 [Huang 2017, pp. 2-2].

## Study Area / Data
本研究为数值模拟研究，未涉及具体实地场地。数据来源于程序生成的离散裂隙网络（DFN）模型，总计包含84个3-D DFN模型和从这些模型中提取的672个2-D DFN模型。模型考虑了不同的裂隙密度和裂隙长度指数，详细参数列表见原文附录A [Huang 2017, pp. 1-2].

## Methods
- **3-D DFN生成**：裂隙被假定为圆盘状，中心位置和方向随机均匀分布，开度统一设为1mm，忽视非均质性。裂隙长度遵循幂律分布 $n(l) = \alpha \cdot l^{-a}$，其中 $a$ 为裂隙长度指数 [Huang 2017, pp. 2-4]。
- **2-D DFN提取**：通过在与水力梯度变化方向（x-z平面）平行的平面上切割3-D DFN模型，得到其trace map作为2-D DFN模型 [Huang 2017, pp. 4-4]。
- **3-D流动模拟**：使用作者基于3DEC和Matlab开发的代码进行稳态流模拟，代码包含裂隙网络生成、网格划分和基于Galerkin方法求解流动方程三个模块。等效渗透率 $K$ 由达西定律反算 $Q = \frac{AK}{\mu} \frac{\Delta P}{L}$ [Huang 2017, pp. 4-4]。
- **2-D流动模拟**：在2-D切面模型中，单个裂隙的流动遵循立方定律。边界条件与3-D模型保持一致 [Huang 2017, pp. 4-4]。
- **回归模型构建**：通过分析建立了多元回归函数 $K'_{3D} = -2.34 \ln(\rho) + 1.54 a + 0.48 K'_{2D} + 1.48$ 来预测 $K'_{3D}$，其中 $K'_{2D}$ 是从每个3-D模型提取的8个2-D切面渗透率的平均值 [Huang 2017, pp. 5-6].

## Key Findings
- **2-D与3-D渗透率差异**：2-D DFN模型的渗透率会低估对应3-D DFN模型的渗透率，低估幅度约为10.45%至80.92% [Huang 2017, pp. 1-2]。
- **渗透率与裂隙密度关系**：3-D裂隙网络的无量纲等效渗透率 ($K'_{3D}$) 随裂隙密度 $\rho$ 增加而增加，并遵循线性关系 [Huang 2017, pp. 1-2]。
- **渗透率与裂隙长度指数关系**：$K'_{3D}$ 随着裂隙长度指数 $a$ 的增加而线性递减。当 $a=2.0$ 时，网络主要由若干长裂隙构成并导流；当 $a=4.5$ 时，网络连通性由大量相对小的裂隙主导。随着 $\rho$ 从 0.0100 增至 0.0175 m⁻³，$K'_{3D}$ 在 $a=2.0$ 时从 3.63 增至 8.74，在 $a=4.5$ 时从 1.56 增至 2.98。$a=2.0$ 时的 $K'_{3D}$ 增量（5.11）约为 $a=4.5$ 时增量（1.42）的3.6倍，表明 $K'_{3D}$ 的变化对较小的 $a$ 更敏感 [Huang 2017, pp. 4-5]。
- **预测模型效果**：提出的多元回归函数对模拟结果拟合良好，相关系数 $R^2 = 0.845$。该函数对更高密度 (\rho = 0.025 - 0.125 m⁻³) 的裂隙网络也表现出良好的适用性 [Huang 2017, pp. 5-6].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 2-D DFN model permeability underestimates 3-D DFN permeability by approximately 10.45 – 80.92%. | [Huang 2017, pp. 1-2] | Analysis based on 84 3-D models and 672 2-D cut planes. | 具体低估程度取决于几何参数。 |
| $K'_{3D}$ increases with increasing $\rho$ following linear relationship. | [Huang 2017, pp. 1-2] | 3-D DFN with circular fractures, power-law length distribution, $a$ varying. | 未从索引片段中确认所有 $a$ 值下的具体 $R^2$ 数值。 |
| For a=2.0, flow is mainly in several long fractures; for a=4.5, connectivity is dominated by many small fractures. | [Huang 2017, pp. 1-2] | DFN with variable fracture length exponent $a$. | 这是基于网络结构观察得出的结论。 |
| The variation of $K'_{3D}$ is more sensitive to a smaller $a$. The increment of $K'_{3D}$ for a=2.0 (5.11) is ~3.6 times larger than that for a=4.5 (1.42) when $\rho$ increases from 0.0100 to 0.0175 m⁻³. | [Huang 2017, pp. 4-5] | 3-D DFN model, $\rho$ increases from 0.0100 to 0.0175 m⁻³. | 证据来源于对图2的分析。 |
| A multi-variable regression function (Eq. 7) gives good predictions ($R^2=0.845$) to the simulation results of the 3-D DFNs. | [Huang 2017, pp. 5-6] | Fractures with uniformly and randomly distributed center location and orientation; power-law length distribution. | 回归函数将 $K'_{3D}$ 与 $\rho$, $a$, $K'_{2D}$ 联系起来。 |

## Limitations
- 本研究的DFN模型中，所有裂隙的开度被统一设定为1mm，忽略了开度非均质性对渗透率的影响 [Huang 2017, pp. 2-4]。
- 未考虑孔隙基质的影响。对于裂隙嵌入在多孔固体基质中的介质，裂隙和基质相互作用，两者的渗透率都可能随空间变化 [Huang 2017, pp. 6-7]。
- 未计算3-D裂隙网络的表征单元体。模型域为20m×20m×20m的立方体，流动计算主要集中在较低裂隙密度（0.01至0.0175 m⁻³）。对于低密度模型，其尺寸可能未达到REV，会影响渗透率的量级 [Huang 2017, pp. 6-7]。

## Assumptions / Conditions
- **裂隙形状**：所有裂隙被假定为具有不同半径的圆盘 [Huang 2017, pp. 2-4]。
- **裂隙空间分布**：裂隙中心位置和方向随机且均匀分布 [Huang 2017, pp. 2-4]。
- **裂隙开度**：所有裂隙开度恒定，均为1 mm，不考虑开度非均质性 [Huang 2017, pp. 2-4]。
- **裂隙长度分布**：裂隙长度（直径）遵循幂律分布函数 $n(l) = \alpha \cdot l^{-a}$，其中指数 $a$ 介于2.0至4.5之间，长度有上下限 $l_{min}$ 和 $l_{max}$ [Huang 2017, pp. 2-4]。
- **流动规律**：3-D模型中的流动假设为稳态流；2-D切面中的单个裂隙流动遵循立方定律 [Huang 2017, pp. 4-4]。
- **边界条件**：2-D切面与原始3-D模型的水力边界条件一致 [Huang 2017, pp. 4-4]。

## Key Variables / Parameters
- **$\rho$ (Fracture Density)**：3-D裂隙网络密度，定义为单位体积内的裂隙中心数量 [Huang 2017, pp. 2-4]。
- **$a$ (Fracture Length Exponent)**：幂律长度分布的指数，控制网络中长短裂隙的比例 [Huang 2017, pp. 2-4]。
- **$l$ (Fracture Length)**：由直径表示的裂隙长度，遵循幂律分布 [Huang 2017, pp. 2-4]。
- **$K'_{3D}$ (Dimensionless Equivalent Permeability)**：3-D DFN的无量纲等效渗透率 [Huang 2017, pp. 4-5]。
- **$K'_{2D}$ (Dimensionless Equivalent Permeability of 2-D Model)**：2-D切面模型的无量纲等效渗透率 [Huang 2017, pp. 5-6]。
- **$P_{32}$**：单位体积内裂隙表面的总面积 [Huang 2017, pp. 4-5]。
- **$K$ (Equivalent Permeability)**：根据达西定律反算的等效渗透率 [Huang 2017, pp. 4-4]。

## Reusable Claims
1.  对于三维离散裂隙网络，若所有裂隙开度相同，其无量纲等效渗透率（$K'_{3D}$）随裂隙密度（$\rho$）增加而线性增加 [Huang 2017, pp. 1-2]。
    - **Conditions**: 裂隙开度均匀，裂隙长度遵循幂律分布。
2.  在开度均匀的三维离散裂隙网络中，无量纲等效渗透率（$K'_{3D}$）随裂隙长度指数（$a$）的增加（即网络中较小裂隙比例增加）而线性递减，且其对较小的 $a$ 值（即由长裂隙主导的网络）的变化更为敏感 [Huang 2017, pp. 4-5]。
    - **Evidence**: 当 $a$ 从 2.0 增至 4.5，$K'_{3D}$ 下降；且当 $\rho$ 增加相同幅度时，$a=2.0$ 情况下的 $K'_{3D}$ 增量约是 $a=4.5$ 情况下的3.6倍 [Huang 2017, pp. 4-5]。
    - **Limitation**: 此结论基于 $\rho$ 在 0.0100 到 0.0175 m⁻³ 范围内的数据。
3.  直接使用从三维模型切割出的二维切面（平行于水力梯度方向）的渗透率来估算原三维模型的渗透率，会产生显著低估，低估范围约为10.45%至80.92% [Huang 2017, pp. 1-2]。
    - **Conditions**: 三维模型由随机分布的圆盘状裂隙构成，遵循幂律长度分布。二维切面提取方向平行于宏观水力梯度。

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Equivalent Permeability]]
- [[Trace Map Analysis]]
- [[Power-law Length Distribution]]
- [[Fracture Connectivity]]
- [[Percolation Theory]]
- [[Cubic Law]]
- [[Representative Elementary Volume (REV)]]
- [[Fracture Density]]
- [[P32]]

## Candidate Methods
- [[Discrete Fracture Network Generation and Meshing]]
- [[Steady-State Flow Simulation in DFN]]
- [[Galerkin Method for DFN]]
- [[Multi-variable Regression]]
- [[Stereological Analysis of Fracture Networks]]
- [[Comparison of 2D and 3D Permeability]]

## Connections To Other Work
- **2-D与3-D关系研究**: 文章提及前人工作主要集中于导出2-D和3-D裂隙网络的几何关系，如Balberg et al. (1984)的平均排除面积/体积，Darcel et al. (2003b)的分形裂隙网络体视学规则，Zhao et al. (2015)的裂隙面3-D分形维数和2-D轨迹参数关联，但指出这些研究未涉及流体流动计算。本研究填补了这一空白 [Huang 2017, pp. 2-2]。
- **流动模拟代码**: 本研究使用的3-D流动模拟代码由同一作者团队开发（Huang et al., 2016），并已被使用 [Huang 2017, pp. 4-4]。
- **连通性与隧穿理论**: 文章引用了Bour & Davy (1997, 1998)的工作来讨论不同裂隙长度指数($a$)对网络连通性的控制作用，例如当 $a>4$ 时小裂隙主导连通性，当 $1<a<3$ 时流动可能强烈局域化在少数几个大裂隙中 [Huang 2017, pp. 4-5]。

## Open Questions
- 如何在预测模型中纳入裂隙开度的非均质性，而非假设所有开度统一为1mm？[Huang 2017, pp. 2-4]
- 当裂隙嵌入在多孔基质中时，裂隙网络与基质的相互作用如何影响整体的渗透率预测模型？[Huang 2017, pp. 6-7]
- 如何确定并考虑3-D DFN的表征单元体，以评估并消除模型尺寸对渗透率计算结果的影响？[Huang 2017, pp. 6-7]

## Source Coverage
本页依据 Huang et al. (2017) 的9个索引片段整理而成。片段覆盖了论文的**摘要**、**引言**（部分）、**方法**（3-D/2-D DFN生成、流动模拟）、**结果**（裂隙长度指数和密度的影响、回归函数建立）和**结论**。由于索引片段覆盖了论文主体部分，信息量较为充足。但**讨论**（Discussion）部分的详细分析（除“Limitations”外）和**附录A**的完整参数表未在片段中详细体现，因此对这些部分的描述可能存在缺失。
