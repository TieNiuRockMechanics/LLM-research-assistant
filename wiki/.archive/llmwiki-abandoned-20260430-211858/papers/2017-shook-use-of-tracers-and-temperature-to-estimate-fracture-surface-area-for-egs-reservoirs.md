---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-shook-use-of-tracers-and-temperature-to-estimate-fracture-surface-area-for-egs-reservoirs"
title: "Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs."
status: "draft"
source_pdf: "data/papers/2017 - Use of tracers and temperature to estimate fracture surface area for EGS reservoirs.pdf"
collections:
citation: "Shook, G. Michael, and Anna Suzuki. “Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs.” *Geothermics*, vol. 67, 2017, pp. 40–47. *ScienceDirect*, doi:10.1016/j.geothermics.2016.12.006."
indexed_texts: "8"
indexed_chars: "39939"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:14:47"
---

# Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs.

## One-line Summary
本文提出了一套利用示踪剂和温度数据估算增强型地热系统（EGS）裂隙表面积的工作流程，并通过数值模拟验证了该方法在不同非均质性条件下的稳健性 [Shook 2017, pp. 1-2]。

## Research Question
EGS 设计与管理中的关键不确定性在于控制热量从围岩到循环注入水传热速率的裂隙表面积 [Shook 2017, pp. 1-2]。如何利用示踪测试与产出温度历史来估计这一表面积，并评估其对长期可持续性与发电能力的影响？

## Study Area / Data
本研究采用了一个单井对模型，该井对完井于单一垂向裂隙组中，围岩为非裂隙原生岩石。裂隙半长为 99 m，高度 75 m，开度 0.02 m，基质宽度 642.66 m。初始温度 200 °C，注入质量流量 2 kg/s，注入温度 25 °C [Shook 2017, pp. 4-5]。设置了两个算例：Example 1 假定裂隙均匀并包含两个损伤区；Example 2 假定损伤区具有不同的渗透率和孔隙度 [Shook 2017, pp. 4-4]。模型网格设置为 33 × 15 × 3，DX=3 m，DY 为 0.01, 0.02, 0.04,…，DZ=25 m [Shook 2017, pp. 4-5]。

## Methods
提出的工作流程分两步 [Shook 2017, pp. 4-4]：  
1. 先进行一次示踪剂测试，利用式 (8) 估算总扫掠孔隙体积，并通过 F-Φ 曲线（流动能力-储存能力图）判别流动几何形态，识别多条裂隙或主力裂隙周围的损伤区，从而分配各条裂隙的孔隙体积和流量 [Shook 2017, pp. 3-4, 4-4]。  
2. 根据裂隙数量，将产液温度表示为每条裂隙对应温度解析解的叠加，定义目标函数 OF = Σ(T_F − T_M)^2，利用非线性求解器通过迭代调整各裂隙的表面积最小化 OF [Shook 2017, pp. 4-4]。  
温度解析解基于 Gringarten 与 Sauty (1975) 的方程，该方程描述流体在裂隙中运移而围岩中进行热传导的过程 [Shook 2017, pp. 2-3]。具体地，对于单一裂隙，产出温度随时间的演化由式 (7) 给出；多裂隙情形采用叠加原理，以各裂隙的流量 q_i 与孔隙体积 V_pi 加权求和 [Shook 2017, pp. 5-6]。示踪测试数据处理时，若尾迹未完全回收，可采用指数外推法补充 [Shook 2017, pp. 3-4]。

## Key Findings
1. 利用示踪测试估计的总扫掠孔隙体积与真实值的相对误差很小（Example 1 为 2.2%，Example 2 为 2.66%），证明该方法准确 [Shook 2017, pp. 4-5, 5-6]。  
2. 基于示踪反演的孔隙体积，通过温度历史拟合估算的裂隙表面积与真实值吻合良好，即使在存在多条不同渗透率流动路径的非均质条件下仍表现出色 [Shook 2017, pp. 5-6]。  
3. F-Φ 曲线能够有效识别并分割不同流动路径的流量与孔隙体积，即使示踪曲线出现多峰也能较准确地分配 [Shook 2017, pp. 5-6]。  
4. 利用估测的裂隙性质，可进行不同注入流量下的长期温度预测与累积发电量评估，发现较高的注入速率虽可在短时间内获得较高功率，但长期产热衰减更快 [Shook 2017, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 示踪剂扫掠孔隙体积估算误差小于 3% | [Shook 2017, pp. 4-5, 5-6] | 数值模型，单井对，单一裂隙带两个损伤区 | 使用式 (8) 计算，Example 1 误差 2.2%，Example 2 误差 2.66% |
| 表面积估算与“真实”值误差小，即使在非均质条件下 | [Shook 2017, pp. 5-6] | Example 2 包含三个不同渗透率的流径 | 通过温度叠加拟合三个流径的表面积，精度“outstanding” |
| F-Φ 曲线斜率突变点对应不同流径 | [Shook 2017, pp. 5-6] | Example 2 示踪数据 | 利用切线斜率分割流动单元，分配流量和孔隙体积 |
| 不同注入流量下的累积发电量对比 | [Shook 2017, pp. 6-7] | 使用 Example 2 的性质和表面积估计，模拟不同注入速率 | 高注入速率早期产电高但后期衰减快 |

## Limitations
1. 方法假定基质渗透率为零，即无流体滤失；该假设的放宽需要进一步研究 [Shook 2017, pp. 7-8]。  
2. 示踪测试若提前终止导致尾迹未完全回收，会低估扫掠体积，需采用指数外推等校正手段，但其适用性未在本文验证 [Shook 2017, pp. 3-4]。  
3. 所用的温度解析解基于 Gringarten & Sauty (1975) 方程，该方程假设裂隙中热对流与围岩中一维热传导，忽略了可能的三维效应、基质内对流等 [Shook 2017, pp. 2-3]。  
4. 文中仅用数值模型验证，未提供实际现场数据验证。  
5. 对于“增强型”EGS（位于水热储层边缘，可能存在原有裂隙），方法是否仍然有效尚需研究 [Shook 2017, pp. 7-8]。

## Assumptions / Conditions
- 储层为干热岩，基质渗透率为零，无流体漏失 [Shook 2017, pp. 7-8]。  
- 裂隙中流体流动为一维，温度在裂隙垂直方向无变化（可通过局部热平衡假设描述） [Shook 2017, pp. 2-3]。  
- 围岩中的热传导为垂直于裂隙方向的一维过程，且岩石热物性均匀 [Shook 2017, pp. 2-3]。  
- 示踪测试时注入流体温度恒定，且示踪剂为惰性、不发生吸附或反应。  
- 裂缝几何形态在测试期间不发生显著变化。  
- 注入与生产井之间通过增产措施确保良好连通 [Shook 2017, pp. 4-4]。

## Key Variables / Parameters
- 裂隙表面积 S (m²)  
- 扫掠孔隙体积 Vs 或 Vp (m³)  
- 示踪剂平均停留时间 t* (s)  
- 体积流量 q (m³/s)，各裂隙流量 qi  
- 裂隙宽度 b (m)  
- 岩石密度 ρR、比热 CpR、导热系数 KR  
- 水的密度 ρw、比热 Cpw  
- 注入温度 TJ、初始温度 TI、产出温度 Tw  
- 流动能力-储存能力图 (F-Φ curve) 的斜率与突变点  
- 目标函数 OF = Σ(TF − TM)²  
- 热电转换效率 η，文中使用 η = 6.9681 ln(T) − 29.713 (基于二元循环电厂平均效率) [Shook 2017, pp. 6-7]

## Reusable Claims
1. 利用一次示踪测试计算的扫掠孔隙体积结合 F-Φ 曲线，可分离出多条裂隙的孔隙体积与流量份额，即使示踪曲线表现出多峰特征；条件是示踪数据可用，且注入/产出速率稳定 [Shook 2017, pp. 5-6]。  
2. 温度解析解 (Gringarten & Sauty, 1975) 可通过叠加原理处理多个并行流动路径，只需已知各流径的孔隙体积与流量；使用非线性回归匹配产出温度历史即可反演各流径的表面积 [Shook 2017, pp. 4-4]。  
3. 估算的裂隙表面积可支撑长期产能预测与运营优化，例如：在确定表面积后，可预测不同注入速率下的温度衰减曲线和累积发电量，从而进行可持续性评估 [Shook 2017, pp. 6-7]。  
4. 示踪测试曲线尾迹的外推方法（如指数衰减外推）可用于减轻因测试提前终止造成的体积低估，但需谨慎验证尾迹下降趋势 [Shook 2017, pp. 3-4]。

## Candidate Concepts
- [[Enhanced Geothermal System]]  
- [[fracture surface area]]  
- [[tracer test]]  
- [[flow geometry]]  
- [[F-Φ curve]]  
- [[heat transfer in fractured rock]]  
- [[Gringarten and Sauty solution]]  
- [[superposition of temperature solutions]]  
- [[geothermal power potential]]  
- [[damage zone]]

## Candidate Methods
- [[moment analysis of tracer data]]  
- [[flow capacity-storage capacity diagram]]  
- [[nonlinear regression for thermal history matching]]  
- [[exponential tail extrapolation]]  
- [[binary cycle power conversion efficiency model]]

## Connections To Other Work
- 本研究的温度解析基础来自 Gringarten & Sauty (1975)、Lauwerier (1955) 以及 Carslaw & Jaeger (1959) 等经典热传导与裂隙流动解 [Shook 2017, pp. 2-3]。  
- 示踪测试的流动几何分析思想源于石油工程中的流动单元划分方法，如 Stiles (1949)、Schmalz & Rahme 以及 Shook (2003) 等 [Shook 2017, pp. 3-4]。  
- 文末提及 Dean et al. (2015) 的实验室阳离子交换示踪实验用于裂隙表面积估计，但本方法未采用此类化学反应性示踪 [Shook 2017, pp. 7-8]。  
- 热电转换效率公式取自 Moon & Zarrouk (2012) 对二元循环电厂的经验回归 [Shook 2017, pp. 6-7]。  
- 从主题上可连接到 [[solute transport in fractures]]、[[heat extraction from HDR]]、[[reservoir characterization with conservative tracers]] 等领域的概念与方法。

## Open Questions
- 当基质渗透率不可忽略（存在流体漏失）时，本工作流程是否仍能准确估计表面积？文中提到需进一步研究 [Shook 2017, pp. 7-8]。  
- 对于 Enhanced EGS（处于水热储层边缘、存在预存裂隙），F-Φ 方法是否可有效识别并分组裂隙尚未证明 [Shook 2017, pp. 7-8]。  
- 示踪测试尾迹外推在实际复杂条件下的适用性与不确定性未得到量化。  
- 现场实际数据对该方法的验证仍为空白。  
- 该方法在更多注入-生产井构型（如多井多裂隙系统）的推广效果有待更系统的评估，文中仅做了初步的对称双生产井示例。

## Source Coverage
本页内容全部基于 8 个索引片段，这些片段覆盖了论文的摘要、引言（部分）、符号表、方法描述、验证算例（Example 1 和 2）、讨论与结论等部分，主要偏向方法、验证结果和部分应用示例。对原文的实验设计、网格细节、引用的其他具体文献列表等细节在片段中有提及但未完全展开，可能缺少更细致的公式推导、与其它方法的对比分析等。因此，本页对方法的核心步骤与关键发现能较准确呈现，但无法确认原文是否有更多关于现场实施建议或与其他手段的讨论。
