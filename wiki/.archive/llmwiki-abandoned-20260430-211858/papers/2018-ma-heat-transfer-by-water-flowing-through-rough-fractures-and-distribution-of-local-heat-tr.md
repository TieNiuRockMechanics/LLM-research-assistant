---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-ma-heat-transfer-by-water-flowing-through-rough-fractures-and-distribution-of-local-heat-tr"
title: "Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction."
status: "draft"
source_pdf: "data/papers/2018 - Heat transfer by water flowing through rough fractures and distribution of local heat transfer coefficient along the flow direction.pdf"
collections:
citation: "Ma, Yueqiang, et al. \"Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction.\" *International Journal of Heat and Mass Transfer*, vol. 119, 2018, pp. 139-147. doi:10.1016/j.ijheatmasstransfer.2017.11.102."
indexed_texts: "8"
indexed_chars: "37344"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:55:59"
---

# Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction.

## One-line Summary
通过数值模拟与3D打印粗糙裂缝试样的实验，研究了水流过粗糙裂缝时的换热特性，发现局部换热系数沿流向先急升后趋于定值，且受裂缝面曲折度影响 [Ma 2018, pp. 1-1]。

## Research Question
研究核心问题是：水流经具有不同粗糙度的裂隙时，总换热系数与局部换热系数的分布规律如何，以及裂缝面粗糙度（曲折度）如何影响换热特性 [Ma 2018, pp. 1-1]。

## Study Area / Data
本研究的物理对象为包含粗糙裂缝的圆柱体试样，裂缝形态基于3D打印技术制造。试样粗糙度通过节理粗糙度系数（JRC）进行量化，具体研究了 JRC 为 0–2、10–12 和 18–20 的三种表面形态 [Ma 2018, pp. 4-6]。实验条件为：围压维持 1 MPa，以防止水从试样与夹具间隙流过；试样被加热至 90 °C 后注入水 [Ma 2018, pp. 2-4]。水流体为水，数值模拟与实验设定的体积流量为 5, 10, 15, 20 ml/min [Ma 2018, pp. 4-6]。

## Methods
研究采用了数值模拟与实验相结合的方法。
1.  **试样制备**：利用3D打印技术制造了具有不同粗糙度（JRC=0-2, 10-12, 18-20）的混凝土裂缝试样 [Ma 2018, pp. 1-1, 4-6]。
2.  **实验系统**：使用ISCO泵精确控制水流注入。实验系统包含围压控制子系统（最高40MPa）和温度控制子系统（可加热至200°C）。实验时围压保持 1 MPa，试样加热至 90 °C [Ma 2018, pp. 2-4]。
3.  **数值模拟**：基于3DEC（三维离散元程序）建立数值模型，模拟了水流和热传递过程 [Ma 2018, pp. 4-6, 6-7]。模拟中假设裂隙内流体流动为层流，忽略岩石基块内的流体流动 [Ma 2018, pp. 4-6]。
4.  **数据计算**：
    *   **局部换热系数** `h'`：通过将试样沿水流方向离散为微小单元，结合牛顿冷却定律和流体吸收热量公式推导得出 [Ma 2018, pp. 6-7]。
    *   **总换热系数** `h_total`：基于Bai提出、假设温度沿试样半径线性分布的公式计算 [Ma 2018, pp. 7-8]。
    *   **努塞尔数（Nusselt number）** 关联式：采用 `Nu = C Re^n Pr^m` 的形式对不同实验条件下的数据进行拟合 [Ma 2018, pp. 7-8]。

## Key Findings
1.  裂隙面粗糙度显著影响水流经岩石的换热特性。总换热系数在JRC值恒定时与体积流量呈正相关，在体积流量恒定时随JRC值增大而增大 [Ma 2018, pp. 8-9]。
2.  水温沿流动方向的分布并非线性增长。因此，使用进、出口水温算数平均值代替裂隙内水的平均温度，可能会低估总换热系数值 [Ma 2018, pp. 7-8, 8-9]。
3.  局部换热系数沿流向的分布规律为：在入口处增加到最大值，然后沿程下降至一个相对稳定的定值 [Ma 2018, pp. 1-1, 8-9]。
4.  裂隙面的曲折度（tortuosity）会影响局部换热系数的波动，但体积流量不影响局部换热系数的分布规律 [Ma 2018, pp. 1-1, 8-9]。
5.  数值模拟的出口水温与实验值吻合良好，最大误差为0.82%，验证了数值模型的正确性 [Ma 2018, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 裂隙面粗糙度显著影响换热特性 | [Ma 2018, pp. 8-9] | 比较了不同JRC值下的总换热系数 | 结论与Zhao的 viewpoint 一致 |
| 总换热系数与体积流量呈正相关，与JRC值呈正相关 | [Ma 2018, pp. 8-9] | 固定JRC改变流量，或固定流量改变JRC | |
| 水温沿流向非线性增长 | [Ma 2018, pp. 7-8, 8-9] | 通过数值模拟温度分布云图（Fig. 13）得出 | 结论与Zhao的 viewpoint 一致 |
| 局部换热系数在入口最大，后下降至稳定值 | [Ma 2018, pp. 1-1, 8-9] | 所有模拟和实验工况 | |
| 数值模型出口水温最大误差0.82% | [Ma 2018, pp. 7-8] | 体积流量为20 ml/min时 | 用于验证模型可靠性 |

## Limitations
未从索引片段中确认对本研究局限性的明确说明。论文可能在其他未提供章节讨论了3D打印与天然裂隙表面差异、模型放大效应或温度范围限制。

## Assumptions / Conditions
1.  **实验条件**：围压恒定在 1 MPa，该值高于流体压力，以确保水流仅发生在试样裂隙内 [Ma 2018, pp. 2-4]。
2.  **数值模型（3DEC）**：裂隙中的流体流动为层流；岩石基块不透水，流体仅在裂隙中流动和发生热对流；热传输包括流体中的对流、流体内部的热传导以及岩石中的热传导 [Ma 2018, pp. 4-6]。
3.  **总换热系数计算**：假设试样沿半径方向的温度分布为线性函数 [Ma 2018, pp. 7-8]。
4.  **数据范围**：主要结论基于对三个JRC等级（0-2, 10-12, 18-20）和四种体积流量（5, 10, 15, 20 ml/min）的实验与模拟结果 [Ma 2018, pp. 4-6, 7-8]。

## Key Variables / Parameters
*   流体参数：流体温度 `Tf`、进水温度 `Tin`、出水温度 `Tout`、水密度 `ρw`、水比热 `cp,w`、普朗特数 `Pr` [Ma 2018, pp. 2-4, 6-7]。
*   岩石/裂隙参数：节理粗糙度系数 `JRC`、裂隙内表面算数平均温度 `Tr`、圆柱试样直径 `d`、长度 `L`、岩石热导率 `k_T_rock` [Ma 2018, pp. 1-1, 2-4, 6-7]。
*   流动参数：体积流量 `qv`、雷诺数 `Re`、流速 [Ma 2018, pp. 2-4, 6-7]。
*   换热性能指标：局部换热系数 `h'`、总换热系数 `h_total`、努塞尔数 `Nu`、对流换热面积 `A` [Ma 2018, pp. 6-7]。

## Reusable Claims
*   **Claim 1**：在水流经粗糙裂隙的换热模拟与实验中，采用3D打印技术可以制备具有特定、可控JRC值的试样，以系统研究粗糙度对换热的影响 [Ma 2018, pp. 1-1]。证据：研究采用3D打印制作了JRC为0-2, 10-12, 18-20的试样。条件：用于实验规模的裂隙换热研究。
*   **Claim 2**：对于层流状态下的单裂隙换热，局部换热系数沿流向衰减并趋于常数的分布特征 —— 入口效应显著，入口处换热系数最高，随后沿程下降 [Ma 2018, pp. 1-1]。证据：模拟和实验结果均显示此规律。限制：此规律仅在本文体积流量（5-20 ml/min）和JRC范围（0-20）内得到验证。
*   **Claim 3**：在计算粗糙裂隙对流传热的平均温度时，若简单地使用进、出口水温算数平均代替裂隙内流体平均温度，会导致对总换热系数的低估 [Ma 2018, pp. 8-9]。证据：数值模拟显示水温沿程非线性分布。条件：该低估现象的根本原因是水温沿程的非线性分布。

## Candidate Concepts
*   [[rough fracture]] / [[rock fracture]]
*   [[heat transfer coefficient]]
*   [[local heat transfer coefficient]]
*   [[joint roughness coefficient (JRC)]]
*   [[tortuosity]]
*   [[enhanced geothermal system (EGS)]]
*   [[convective heat transfer]]
*   [[3D printing in rock mechanics]]

## Candidate Methods
*   [[3DEC (3-Dimensional Distinct Element Code)]]
*   [[experimental heat transfer measurement]]
*   [[numerical simulation of flow in fractures]]
*   [[Nusselt number correlation (Nu = C Re^n Pr^m)]]
*   [[3D printing of rock specimens]]

## Connections To Other Work
索引片段中引用的工作与本研究的连接点：
*   与 Zhao [3] 和 Zhao [5] 的观点一致：确认了裂隙粗糙度对换热的影响，以及温度沿程非线性分布 [Ma 2018, pp. 8-9]。
*   与 Bai [6] 的公式相关：总换热系数计算采用了Bai提出的公式 [Ma 2018, pp. 7-8]。
*   与 Shaik et al. [9] 等研究相关：均关注岩体裂隙中流体流动与换热过程对地热系统经济性的影响 [Ma 2018, pp. 1-2]。
*   引申主题连接：本研究方法可连接到使用[[3D printing]]技术研究[[rock mechanics]]问题的其他工作；其结论可连接到所有涉及[[fracture reservoir]]内[[fluid flow]]和[[heat transfer]]的研究。

## Open Questions
1.  本研究发现的局部换热系数分布规律对于更高流速（湍流）或更高粗糙度（JRC>20）的裂隙是否仍然适用？[未从索引片段中确认]
2.  实际地热储层中，裂隙处于高温高压及化学作用环境中，本文的实验和模拟结果如何有效地向上扩展到野外尺度？ [未从索引片段中确认]
3.  论文关于“体积流量不影响局部换热系数分布”的结论，其物理机制和普遍性如何？ [未从索引片段中确认]

## Source Coverage
本知识页主要依据索引片段中的8个片段生成，覆盖了论文的摘要、引言、实验系统与方法、数据推导、部分结果与结论。片段提供了大部分关键信息，但对以下部分覆盖不足或缺失：实验准备的完整步骤、所有工况的详细数值模拟结果图表、所有拟合得到的努塞尔数关联式系数、以及论文的局限性分析。参考文献信息仅部分提供。
