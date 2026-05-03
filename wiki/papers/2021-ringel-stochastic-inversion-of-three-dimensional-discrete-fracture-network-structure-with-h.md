---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h"
title: "Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2021 - Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.pdf"
collections:
citation: "Ringel, Lisa Maria, et al. \"Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.\" 2021."
indexed_texts: "16"
indexed_chars: "77553"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "77358"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.997486"
coverage_status: "full-index"
source_signature: "ecd42da975c25b922e501564db61b78cb98815b0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:46:46"
---

# Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.

## One-line Summary
基于贝叶斯框架与可逆跳马尔可夫链蒙特卡洛方法，利用水力层析成像数据对三维离散裂隙网络的几何与水力参数进行随机反演，以概率图形式评估不确定性，并在瑞士 Grimsel 试验场合成案例中验证了主要流动路径的识别能力 [Ringel 2021, pp. 1-1][Ringel 2021, pp. 1-2][Ringel 2021, pp. 4-5]。

## Research Question
如何基于水力层析成像实验的瞬态压力响应，在三维空间中灵活且随机地反演离散裂隙网络的几何结构（裂隙数量、位置、产状、延伸长度）及水力开度，并量化其不确定性？[Ringel 2021, pp. 1-2][Ringel 2021, pp. 2-3]

## Study Area / Data
- 研究所用的合成数据及概念模型参照 **瑞士 Grimsel 试验场（Grimsel test site）** 的原位水力与地质信息构建，尤其借鉴了 ISC（in situ stimulation and circulation）实验中的光学钻孔电视、裂隙连接矩阵等资料 [Ringel 2021, pp. 5-6][Ringel 2021, pp. 6-8]。
- 实际用于反演的“测量数据”为 **四个合成测试案例** 中通过正演模拟生成的井间水力层析压力信号，并加入约 3% 均值的正态分布噪声 [Ringel 2021, pp. 5-6]。
- 基础案例（测试案例 1）包含两个裂隙组、5 个源/接收点，钻孔布置与裂隙特征取自 Grimsel 现场数据 [Ringel 2021, pp. 5-6][Ringel 2021, pp. 6-8]。

## Methods
- **正演模型**：采用基于有限元法（FEM）的离散裂隙网络（DFN）流动模型，裂隙简化为平面椭圆、均匀开度的二维壳单元，流动遵循立方定律，使用 Gmsh 生成网格并处理裂隙交线 [Ringel 2021, pp. 2-3][Ringel 2021, pp. 3-4]。
- **反演框架**：基于贝叶斯原理，通过可逆跳马尔可夫链蒙特卡洛（rjMCMC）进行跨维度采样，同时推断裂隙数量与各裂隙的几何、水力参数。似然函数采用独立正态误差假设，先验分布由野外裂隙组统计信息限定 [Ringel 2021, pp. 3-4][Ringel 2021, pp. 4-5]。
- **参数更新策略**：包含两种更新类型：模型间移动（插入或删除裂隙）和模型内移动（修改裂隙位置、长度、开度）。插入裂隙可在域内任意位置进行，不强制与主网络连接 [Ringel 2021, pp. 4-5][Ringel 2021, pp. 5-6]。
- **结果评估**：将后验样本生成裂隙概率图（fracture probability maps, FPM），剔除未连通的无效裂隙后，通过栅格化计算每个体积单元属于裂隙的样本均值；当开度也被反演时，进一步获得平均水力开度分布 [Ringel 2021, pp. 8-9][Ringel 2021, pp. 9-9]。

## Key Findings
- **主要流动路径可高确定性识别**：水力层析反演能够很好地约束对压力信号影响最大的源/接收点间连接裂隙的位置和延伸长度，这些裂隙的 FPM 分辨率高，不确定性小 [Ringel 2021, pp. 9-9][Ringel 2021, pp. 11-13]。
- **水力开度可联合反演但增加歧义**：在测试案例 2 中，同时反演几何参数与开度时，解的多样性显著增加，FPM 分辨率降低，表明仅有水力层析数据可能不足以唯一确定开度分布 [Ringel 2021, pp. 9-11][Ringel 2021, pp. 13-14]。
- **增加约束改善反演精度**：测试案例 3 中增加一个源/接收点后，FPM 分辨率明显提升，且 y 坐标（背面方向）的不确定性减小，说明二维简化会丢失信息 [Ringel 2021, pp. 11-13]。
- **多裂隙组导致更高不确定性**：测试案例 4 引入第三裂隙组，由于可能的流动路径增多，单一裂隙对信号的贡献降低，反演结果的精度和确定性均下降 [Ringel 2021, pp. 12-13]。
- **后验样本可区分可靠与不可靠裂隙**：低概率区域（<10%）的裂隙表征不充分，提示这些裂隙未被水力数据有效约束，需补充其他地质或地球物理信息 [Ringel 2021, pp. 9-9][Ringel 2021, pp. 11-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| rjMCMC 反演成功重构了 Grimsel 基础案例中连接注入孔 2 的裂隙，位置与长度偏差小，FPM 显示高概率；注入孔 2 的裂隙长度因更多信号组合约束而优于孔 1。 | [Ringel 2021, pp. 9-9] | 测试案例 1：已知裂隙组方向，固定开度，5 个 S/R 点，噪声 3%。 | 主要流路对应高可靠度；y 坐标约束弱，可在 x-z 面自由移动。 |
| 同时反演开度与几何参数时，FPM 分辨率下降，低概率区域增多，开度均值接近预设值但存在多种补偿可能（如平行裂隙增多）。 | [Ringel 2021, pp. 9-11] | 测试案例 2：开度范围设定为真值的 ±80% 先验界限。 | 仅靠水力层析难以唯一确定几何与开度，需额外数据约束概念模型。 |
| 增加 S/R 6 点后，下部裂隙的 FPM 更集中，y 坐标不确定性降低，表明三维反演不可简化为二维。 | [Ringel 2021, pp. 11-13] | 测试案例 3：在基础案例上增加一个与井相交的裂隙及新的源/接收点。 | 可用于指导未来补充测点的位置选择。 |
| 引入第三裂隙组后，上部可定位但下部难以确定，表明多裂隙组下的反演结果不确定性增大，需更多先验信息或额外数据。 | [Ringel 2021, pp. 12-13] | 测试案例 4：第三裂隙组绕 x 轴旋转 75°，额外 S/R 6，但流动路径增多。 | 分辨率可通过更多先验或补充测量改善。 |

## Limitations
- 合成案例中概念模型与真实场地的偏差未充分检验；示例假定裂隙为平面椭圆且开度均匀，未考虑非均匀开度或沟道化流动 [Ringel 2021, pp. 8-9]。
- 反演精度高度依赖可用的水力信号数量及源/接收点布设；对于多组裂隙或开度同时反演的情况，不确定性显著增加，需要额外的地质或地球物理先验信息 [Ringel 2021, pp. 9-11][Ringel 2021, pp. 13-14]。
- rjMCMC 计算成本较高，尽管文中采用了保守的烧入和稀疏策略，但对于真实三维问题可能仍需要进一步改善效率 [Ringel 2021, pp. 12-13]。
- 未考虑井内流动细节和封隔器泄漏等实际影响 [Ringel 2021, pp. 8-9]。

## Assumptions / Conditions
- 裂隙可简化为平面椭圆，长度等比固定（短轴为长轴一半），且开度在单裂隙内均匀 [Ringel 2021, pp. 8-9]。
- 流动满足立方定律，压力梯度沿裂隙平面恒定 [Ringel 2021, pp. 2-3]。
- 测量误差为独立同正态分布，且噪声水平约为压力均值的 3% [Ringel 2021, pp. 5-6]。
- 先验信息来自钻孔裂隙编录和露头，可限定裂隙组方位、开度变化范围及最大可能裂隙数 [Ringel 2021, pp. 8-9]。
- 注入点可通过封隔器完全隔离，无井筒存储效应 [Ringel 2021, pp. 8-9]。

## Key Variables / Parameters
- **待反演的几何参数**：各裂隙中心坐标、长轴长度；裂隙数量（通过 rjMCMC 跨维度确定） [Ringel 2021, pp. 8-9]。
- **可选反演的水力参数**：水力开度（测试案例 2 中作为未知数，其余案例固定） [Ringel 2021, pp. 9-11]。
- **固定参数**：裂隙组倾斜角、倾角、绕 x 轴旋转角；比储水系数；短轴与长轴比例；流体属性等 [Ringel 2021, pp. 8-9]。
- **输出诊断量**：裂隙概率图（FPM）、平均开度分布、后验样本的模拟压力均值与实测对比 [Ringel 2021, pp. 9-9][Ringel 2021, pp. 9-11]。

## Reusable Claims
- **Claim 1**：基于贝叶斯 rjMCMC 的三维 DFN 反演方法可在无需预设裂隙数量的情况下，同时推断裂隙几何与水力开度，并生成概率图表征不确定性 [Ringel 2021, pp. 1-2][Ringel 2021, pp. 4-5]。
  - *条件与限制*：要求有可靠的先验裂隙组信息（方位、长度范围、开度上下界）且水力层析信号包含充足的压力瞬态数据；当裂隙组增多或开度灵活变化时，反演结果的不确定性增大，需要额外数据约束。
- **Claim 2**：水力层析对主要流动路径的约束力强，而对次要裂隙的定位和几何参数不确定性高，可通过 FPM 辨别 [Ringel 2021, pp. 9-9]。
  - *条件与限制*：适用于层析信号主要受主干通道控制的裂隙介质；若流动路径增多且各裂隙贡献相近，单一裂隙的辨识度下降。
- **Claim 3**：在贝叶斯框架下引入先验信息（如裂隙组方位、开度范围）可有效缩小解空间，且该框架允许融合其它来源的数据作为附加先验 [Ringel 2021, pp. 13-14]。
  - *条件与限制*：先验分布需基于可靠的野外调查，否则可能引入偏差；该框架的可扩展性尚未在实测数据中验证。

## Candidate Concepts
- [[离散裂隙网络 (Discrete Fracture Network, DFN)]]
- [[水力层析成像 (Hydraulic Tomography)]]
- [[可逆跳马尔可夫链蒙特卡洛 (Reversible Jump MCMC)]]
- [[贝叶斯反演 (Bayesian Inversion)]]
- [[裂隙概率图 (Fracture Probability Map)]]
- [[立方定律 (Cubic Law)]]
- [[壳单元 (Shell Elements)]]
- [[跨维度反演 (Transdimensional Inversion)]]
- [[先验分布 (Prior Distribution)]]
- [[似然函数 (Likelihood Function)]]

## Candidate Methods
- [[有限元法 (FEM) 流动模拟]]
- [[Gmsh 网格生成与布尔操作]]
- [[rjMCMC 采样策略]]
- [[先验约束下的参数更新]]
- [[裂隙概率图 (FPM) 后处理]]
- [[水力开度联合反演]]

## Connections To Other Work
- 二维 DFN 跨维度反演的前期研究 (Ringel et al., 2019; Somogyvári et al., 2017) 为本工作提供了算法基础；本研究将其推广至三维并加入开度反演 [Ringel 2021, pp. 1-2][Ringel 2021, pp. 3-4]。
- 与传统连续介质水力层析不同，本研究采用显式 DFN 表示，能够捕捉优先流通道及结构非均质性，与 Hadgu et al. (2017) 的对比结论和 Klepikova et al. (2020) 的简化路径反演思路相呼应 [Ringel 2021, pp. 1-1][Ringel 2021, pp. 2-3]。
- 与 Dorn et al. (2013) 通过地球物理和水文数据约束随机 3D 裂隙网络的方法类似，但本文采用完全基于水力的跨维度反演，并强调不确定性量化 [Ringel 2021, pp. 1-2]。
- 正演模型可选择其他 DFN 模拟工具（如 Hyman et al., 2015; Keilegavlen et al., 2021）替换，以考虑更复杂的物理过程或不同测量数据 [Ringel 2021, pp. 13-14]。

## Open Questions
- 如何有效分离并评估水力开度与裂隙位置、数量之间的参数相关性，尤其在多组裂隙反演中？[Ringel 2021, pp. 13-14]
- 为提高反演效率，是否可引入邻近合并或分裂裂隙的更新类型？[Ringel 2021, pp. 13-14]
- 在真实野外数据中，概念模型误差（如非椭圆裂隙、非均质开度）会如何影响反演结果？可通过估计误差方差进行量化吗？[Ringel 2021, pp. 8-9]
- 如何系统性地融合连续反演结果、地球物理信号或示踪层析数据作为贝叶斯先验，以进一步降低不确定性？[Ringel 2021, pp. 13-14]
- 文中采用的“任意位置插入裂隙”策略虽改善了收敛性，但产生的未连通裂隙是否会导致后验样本的冗余，如何更高效地处理？[Ringel 2021, pp. 5-6]

## Source Coverage
所有提供的非空索引片段均已处理并纳入本页面。片段总数为 16，非空源文本区块数为 16，已编译源区块数为 16，区块覆盖率 1.0。源文本字符总数 77,553，已编译字符数 77,358，字符覆盖率 0.997486。索引策略为 single-pass-markdown。任何未被直接引用的片段信息均已通过整合与提炼融入相应章节，无额外信息添加。
