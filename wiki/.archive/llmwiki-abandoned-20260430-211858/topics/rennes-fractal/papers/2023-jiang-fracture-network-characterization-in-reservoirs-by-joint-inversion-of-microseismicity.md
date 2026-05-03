---
type: "paper"
paper_id: "2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity"
title: "Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification."
status: "draft"
source_pdf: "data/papers/2023 - Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data Method Development and Verification.pdf"
citation: "Jiang, Zhenjiao, et al. \"Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.\" American Geophysical Union, 2023."
indexed_texts: "22"
indexed_chars: "106616"
compiled_at: "2026-04-27T19:46:27"
---

# Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.

## One-line Summary
本研究开发了一种基于贝叶斯原理的联合反演程序，利用微地震(MS)事件和热突破数据，以推断裂缝网络的裂缝数量、几何形状和开度。

## Research Question
在深部储层中，裂缝网络的表征是一项具有挑战性的任务，因为可用于进行井下测井和井间水力及示踪剂测试的钻孔数量有限 [Jiang 2023, pp. 1-1]。本研究旨在开发一种联合反演程序，以更可靠地表征裂缝网络，其具体目标是推断裂缝数量、几何形状（走向、长度、位置）和开度 [Jiang 2023, pp. 1-1]。

## Study Area / Data
本研究的验证使用了两个二维测试案例 [Jiang 2023, pp. 8-9]：
1.  **简单案例**：一个由4条裂缝组成的简单储层模型，模拟深度范围为1500米至1600米，用于直接评估反演模型在表征裂缝数量、走向、位置、长度和开度方面的准确性 [Jiang 2023, pp. 9-9]。
2.  **复杂案例**：一个由从真实野外露头数据中提取的17条裂缝组成的复杂案例，用于评估反演模型捕捉裂缝骨架和预测在不同注入与开采情景下流出温度的能力 [Jiang 2023, pp. 9-9]。

数据方面，该方法利用微地震(MS)事件云和热突破数据（开采井的流出温度）进行反演 [Jiang 2023, pp. 1-1]。具体的MS事件和热突破数据来源于上述两个合成测试案例，而非真实场地数据，此点未从索引片段中完全确认。

## Methods
该研究提出了一种联合反演程序，该程序基于贝叶斯原理，并利用可逆跳转马尔可夫链蒙特卡罗 ([[reversible jump Markov chain Monte Carlo (rjMCMC)]]) 算法 [Jiang 2023, pp. 1-1, 3-4]。主要包括以下步骤：
1.  **生成初始裂缝几何形状**：通过最小化裂缝与MS事件之间的距离，从MS事件云中生成一个基础的离散裂缝网络(DFN)几何形状，包括走向、长度和位置 [Jiang 2023, pp. 4-6]。
2.  **正演模拟**：利用开源代码THERMAID求解流动和热传输方程（式4-8），以计算热突破曲线（流出温度）[Jiang 2023, pp. 6-7]。
3.  **贝叶斯反演与更新**：根据计算和观测的热突破数据之间的拟合差，利用rjMCMC算法对裂缝几何形状（通过“添加”或“删除”步骤）和开度（通过“更新”步骤）进行迭代调整，以更好地表征后验分布 [Jiang 2023, pp. 4-6, 7-8]。
4.  **收敛判断**：当拟合差波动稳定，且低于测量误差时，认为反演收敛，并提供可行的DFN实现作为反演结果 [Jiang 2023, pp. 8-9]。

## Key Findings
- 对于包含4条裂缝的简单案例，反演能够准确地估计裂缝数量，以及裂缝开度的分布范围，并有效识别出贯穿钻孔的裂缝 [Jiang 2023, pp. 9-9]。
- 对于包含17条裂缝的复杂案例，反演能够捕捉到裂缝网络的主要骨架，并成功预测了在其原始数据条件下观测到的流出温度 [Jiang 2023, pp. 9-9]。
- 即使在没有完整温度曲线可用于校准的情况下（例如仅有一次温度测量），该方法也能通过反演获得改善的裂缝网络模型，其预测精度优于仅使用MS事件构建的网络 [Jiang 2023, pp. 9-9]。
- 总体上，该联合反演方法被证明能够有效降低裂缝网络表征中的不确定性 [Jiang 2023, pp. 1-1]。

## Limitations
- 论文目前仅关注基于二维裂缝网络的模型开发和验证，以提高计算效率 [Jiang 2023, pp. 6-7]。
- 模型开发旨在表征储层刺激后裂缝网络的最终状态，因此未考虑力学耦合效应的影响 [Jiang 2023, pp. 6-7]。
- 模型中忽略了温度和压力对流体密度和粘度的影响，其影响有待进一步讨论 [Jiang 2023, pp. 6-7]。
- 该方法要求MS事件与水力活动的裂缝共面，但微地震与裂缝几何形状之间的关系仍在争论中 [Jiang 2023, pp. 2-3]。
- 计算成本方面，需要足够多的迭代次数以确保rjMCMC算法的收敛，这可能在应用时构成限制 [Jiang 2023, pp. 8-9]。

## Reusable Claims
- 微地震事件提供了重建裂缝网络几何形状的三维信息，但其对裂缝网络水力连通性的洞察有限 [Jiang 2023, pp. 2-3]。
- 从钻孔成像中获取的钻孔诱导裂缝与原地裂缝的走向信息，可为压力诱导的水力裂缝走向提供关键指示 [Jiang 2023, pp. 3-4]。
- “湿”微地震事件可用于定位水力活跃裂缝的几何形状，而“干”事件则可能导致高估裂缝几何尺寸，应予以排除 [Jiang 2023, pp. 2-3]。
- 反演计算中，钻孔揭示的原始（非诱导）裂缝数量可作为裂缝数量估计的最小值 [Jiang 2023, pp. 3-4]。

## Candidate Concepts
- [[fracture reservoir]]
- [[discrete fracture network (DFN)]]
- [[microseismicity (MS) event]]
- [[heat transport]]
- [[thermal breakthrough curve]]

## Candidate Methods
- [[joint inversion]]
- [[transdimensional inversion]]
- [[reversible jump Markov chain Monte Carlo (rjMCMC)]]
- [[Bayesian inference]]
- [[THERMAID code]]

## Open Questions
- 如何更可靠地区分与裂缝活动相关的“湿”事件和由应力变化引起的“干”事件，以精确构建水力裂缝几何形状？[Jiang 2023, pp. 2-3]
- 在三维模型中应用该方法时，其计算效率和表征能力如何？[Jiang 2023, pp. 6-7]
- 温度和压力对流体性质的影响如何影响反演结果，其影响程度有多大？[Jiang 2023, pp. 6-7]
- 该方法的有效性是否依赖于MS事件与裂缝几何形状之间存在何种确定性关系？[Jiang 2023, pp. 2-3]

## Source Coverage
索引片段主要涵盖了论文的引言、方法描述以及两个验证测试案例的设置与结果（1-9页）。片段提供了对研究问题、方法学（包括[[rjMCMC]]的应用细节和正演模型）及主要发现的完整描述。关于方法中具体参数的设置（如下限值）、代码细节以及与其他方法的详细比较等内容未在片段中完全确认。
