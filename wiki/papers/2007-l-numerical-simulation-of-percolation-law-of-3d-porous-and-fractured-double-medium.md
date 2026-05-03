---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2007-l-numerical-simulation-of-percolation-law-of-3d-porous-and-fractured-double-medium"
title: "Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium."
status: "draft"
source_pdf: "data/papers/2007 - Numerical simulation of percolation law of 3D porous and fractured double-medium.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Lü, Zhao-xing, et al. \"Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium.\" *Rock and Soil Mechanics*, vol. 28, Suppl., Oct. 2007, pp. 291-294. DOI:10.16285/j.rsm.2007.s1.003."
indexed_texts: "2"
indexed_chars: "7152"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "6418"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.897371"
coverage_status: "full-index"
source_signature: "33847b4afdde1f9ae47d33c494c9f9f1c41ad89b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:07:48"
---

# Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium.

## One-line Summary
本文建立了三维多孔与裂隙双重介质逾渗模型，利用VC++6.0软件模拟了双重介质的逾渗规律，结果表明裂隙显著提高逾渗概率，逾渗转变随孔隙度、裂隙分形维数及裂隙数量分布初始值的增大而必然发生。

## Research Question
裂隙的存在如何影响三维多孔−裂隙双重介质的逾渗行为？双重介质的逾渗阈值如何确定？

## Study Area / Data
本研究为数值模拟，无现场数据。使用合成三维立方网格，尺寸为50×50×50 = 125,000个单元，概念上适用于煤层、岩体等多孔−裂隙介质。

## Methods
- **双重介质模型**：将三维多孔介质（基质）与裂隙网络叠加。
  - 多孔基质：采用三维立方格子位点逾渗模型，格子边长L=50，孔隙度为φ，随机占据格点。
  - 裂隙网络：依据分形分布律生成：\( N(\delta) = N_0 (\delta/\delta_0)^{-D} \)，其中δ为裂隙尺度，N₀为裂隙数量分布初始值，D为裂隙分形维数（取值范围2~3）。
- **逾渗定义**：逾渗概率P∞定义为系统出现无限大团簇（跨越整个系统）的概率；有限系统模拟中以团簇是否贯穿样本作为判定依据。
- **软件开发**：基于VC++6.0开发三维模拟软件，实现双重介质生成、团簇识别及逾渗判断。
- **参数设置**：格点总数125,000；孔隙度φ、分形维数D、初始值N₀可调；D以步长0.025从2增至3。

## Key Findings
1. 纯多孔介质逾渗阈值位于0.3~0.38之间，逾渗概率在该区间内由0陡升至1（图3）。
2. 当孔隙度φ=0时，仅靠裂隙网络即可发生逾渗：存在临界分形维数Dc，当D＜Dc时逾渗概率为0，D＝Dc时发生跃变，D＞Dc时概率随D增大而上升；Dc随N₀增大而减小（图4）。
3. 双重介质中，低孔隙度（φ=0.1、0.2）时逾渗概率随D出现两次门槛式变化；当φ≥0.3时，曲线与纯多孔介质情形相近。例如φ=0.1、N₀=2.71828时，由裂隙导致的逾渗阈值D≈2.23（图5）。
4. 裂隙可显著提高系统的逾渗概率，双重介质的逾渗规律与纯多孔介质明显不同。
5. 随着孔隙度、裂隙分形维数以及裂隙数量分布初始值的增大，逾渗转变现象必然发生。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 纯三维多孔介质逾渗概率-孔隙度曲线，阈值在0.3~0.38之间 | [Zhao 2007, pp. 1-4] 图3 | L=50，无裂隙 | 文中提及经典三维位点逾渗阈值0.3116，但本文模拟结果略高 |
| 孔隙度为零时，不同N₀下逾渗概率-分形维数曲线，Dc存在 | [Zhao 2007, pp. 1-4] 图4 | N₀={1, 2, 2.71828, 7.38901} | Dc随N₀增大而左移 |
| 双重介质逾渗概率-分形维数曲线，φ=0.1时D≈2.23为有效阈值 | [Zhao 2007, pp. 1-4] 图5 | φ=0.1，N₀=2.71828 | 文中指出φ=0.1和0.2时呈双门槛现象 |
| 孔隙度≥0.3时裂隙贡献减弱，曲线趋近纯多孔介质 | [Zhao 2007, pp. 1-4] 图5 | N₀=2.71828 | |

## Limitations
- 模型为简化三维规则格子，裂隙几何仅采用简单分形律，未针对实际岩体裂隙特征进行标定。
- 仅采用单一格子尺寸（50³），未做有限尺寸标度分析，所给阈值仅为近似值。
- 裂隙网络仅考虑随机分布，未涉及方向性、各向异性及力学作用。
- 模拟基于VC++6.0自主开发，缺乏与实验的直接对比验证。

## Assumptions / Conditions
- 立方网格尺寸50×50×50，总格点数125,000。
- 多孔基质：位点随机占据，孔隙度φ。
- 裂隙网络服从幂律分布 \( N(\delta)=N_0 \delta^{-D} \)，D∈[2,3]。
- 逾渗定义为存在至少在一个方向上贯穿整个样品的团簇（文中未明确方向数）。
- 逾渗概率通过大量有限系统实现的频率来近似无限大系统概率。

## Key Variables / Parameters
- 孔隙度 φ
- 裂隙分形维数 D
- 裂隙数量分布初始值 N₀（取值包括1, 2, 2.71828, 7.38901）
- 格子尺寸 L=50
- 总单元数 125,000

## Reusable Claims
- 在三维位点逾渗中，孔隙度阈值约为0.3–0.38，逾渗概率在该区间内由0到1发生突然转变（需注意这对有限尺寸敏感，经典值为0.3116）。[来源：图3]
- 仅由服从 \( N(\delta)=N_0 \delta^{-D} \) 的裂隙网络，当D超过某一临界Dc时，即使基质无孔隙度也能发生逾渗，Dc与N₀负相关。[来源：图4]
- 双重介质中，当基质孔隙度较低（≤0.2）时，裂隙主导逾渗；例如φ=0.1、N₀=2.71828时，裂隙逾渗阈值D≈2.23；当φ≥0.3时基质主导，裂隙效应可忽略。[来源：图5]
- 裂隙的存在使双重介质逾渗概率明显高于纯多孔介质。[来源：摘要]

## Candidate Concepts
- [[percolation threshold]]
- [[3D porous medium]]
- [[fracture network]]
- [[fractal dimension]]
- [[double-medium percolation]]
- [[cluster spanning]]
- [[finite-size scaling]]

## Candidate Methods
- [[Monte Carlo simulation of percolation]]
- [[fractal fracture generation (power-law)]]
- [[VC++6.0 percolation software]]
- [[cluster identification algorithm]]

## Connections To Other Work
- 本文参考文献涉及逾渗理论经典文献（Stauffer等）、梯度逾渗[1]、方格上差分逾渗[2]、二维预分形多孔介质逾渗阈值[3]、材料科学中的逾渗模型[4]、多孔介质随机模拟[5]、Nature与Science上的逾渗应用[6,7]、无限三角形格子张力损失逾渗[9]、多尺度结构描述多孔介质[10]、煤体裂隙尺度分布的分形研究[11]及岩体表面数量的三维分形分布[12]。

## Open Questions
- 本文给出的纯多孔介质逾渗阈值（0.3–0.38）与经典值0.3116的差异是否由有限尺寸效应引起？需要系统增大L进行标度分析。
- 裂隙的取向、连通规则以及与基质的力学耦合如何影响双重介质逾渗？
- 如何将该模型与煤层、岩体的真实裂隙测量数据相标定？
- 若采用连续孔隙度或不同类型格子，双重介质逾渗规律是否一致？

## Source Coverage
All non-empty indexed source blocks were processed: 2 blocks [Zhao 2007, pp. 1-4] and [Zhao 2007, pp. 4-4], total indexed chars 7,152, compiled chars 6,418, coverage ratio by chars 0.897. No source blocks were omitted.
