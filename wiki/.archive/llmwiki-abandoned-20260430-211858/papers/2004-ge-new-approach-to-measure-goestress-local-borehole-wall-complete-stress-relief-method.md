---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2004-ge-new-approach-to-measure-goestress-local-borehole-wall-complete-stress-relief-method"
title: "New Approach to Measure Goestress——Local Borehole-Wall Complete Stress Relief Method."
status: "draft"
source_pdf: "data/papers/2004 - 一种测定深部岩体地应力的新方法——钻孔局部壁面应力全解除法.pdf"
collections:
  - "part4-2"
citation: "Ge, Xiurun, and Mingxun Hou. \"New Approach to Measure Goestress——Local Borehole-Wall Complete Stress Relief Method.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 23, no. 23, Dec. 2004, pp. 3923-3927."
indexed_texts: "2"
indexed_chars: "6584"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:01:28"
---

# New Approach to Measure Goestress——Local Borehole-Wall Complete Stress Relief Method.

## One-line Summary
本文提出一种无需套钻、无需额外假定的深部地应力测量方法——钻孔局部壁面应力全解除法（LBWCSRM），理论上可适用于任意深度的钻孔 [Ge 2004, pp. 1-4]。

## Research Question
如何突破传统钻孔应力测量方法（如套钻法）在深度和地应力状态假设上的限制，实现深部岩体地应力张量的有效测定？[Ge 2004, pp. 1-4]

## Study Area / Data
未从索引片段中确认。

## Methods
- 基于线弹性力学理论建立钻孔周边应力分布模型，导出远场应力分量作用下孔壁附近径向、切向与剪应力的解析表达式（公式1–4）[Ge 2004, pp. 1-4]。
- 在钻孔局部壁面按特定方位布置应变花（120°配置），实施应力解除并记录孔壁的弹性恢复应变 [Ge 2004, pp. 4-5]。
- 通过方向余弦矩阵建立大地坐标系与钻孔坐标系之间的转换关系，将局部测量的应变反算至全局应力张量；仅需6个独立应变测量即可唯一确定应力张量的全部6个分量 [Ge 2004, pp. 4-5]。
- 方法的核心特点是 **不采用套钻取心（overcoring）**，也无需对主应力方向或应力状态做任何先验假设 [Ge 2004, pp. 1-4]。

## Key Findings
- 提出的钻孔局部壁面应力全解除法（LBWCSRM）在计算地壳应力张量时，无需套钻作业，亦无其他假设条件 [Ge 2004, pp. 1-4]。
- 理论推导显示该方法不受钻孔深度限制，能够为任意深度钻孔的应力测量提供统一技术路线 [Ge 2004, pp. 1-4]。
- 通过孔壁局部区域的应变花测量，结合坐标转换和弹性力学反演，可以完全确定原地应力张量的六个独立分量 [Ge 2004, pp. 4-5]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| LBWCSRM 无需套钻、无额外假设即可求得应力张量 | [Ge 2004, pp. 1-4] | 基于线弹性岩石模型 | 摘要明确指出方法优势 |
| 方法理论上不受钻孔深度限制，适用于任意深钻 | [Ge 2004, pp. 1-4] | 未给出深度验证实例 | 摘要声明“free from the limitation of borehole depth” |
| 钻孔周围应力场可由基于弹性理论的公式（1-4）描述 | [Ge 2004, pp. 1-4] | 均匀远场应力，各向同性线弹性体 | 给出了包含 a、r、θ 的完整表达式 |
| 通过坐标转换，可利用孔壁应变获取全局应力张量的6个分量 | [Ge 2004, pp. 4-5] | 需已知钻孔方位和倾角 | 提供了方向余弦矩阵和应变花布置示意图 |

## Limitations
- 片段未包含该方法的现场测试或试验验证信息，理论推导的实用性有待工程实例支撑。
- 未提供方法在非弹性、各向异性、破碎岩体或高应力下钻孔稳定情况下的适用性讨论。
- 未给出与已有应力测量方法的定量对比数据，精度与误差分析缺失。

## Assumptions / Conditions
- 钻孔围岩为均匀、各向同性、线弹性介质，适用线弹性力学理论 [Ge 2004, pp. 1-4]。
- 远场地应力在钻孔影响范围内均匀分布，钻孔视为无限长圆形直孔 [Ge 2004, pp. 1-4]。
- 应力解除过程引起的扰动可忽略或可建模，且测量得到的应变完全来自弹性恢复 [Ge 2004, pp. 4-5]。
- 钻孔的空间方位（倾角、方位角）已测定，并可用方向余弦进行坐标系转换 [Ge 2004, pp. 4-5]。

## Key Variables / Parameters
- 远场地应力分量：σ_x^∞, σ_y^∞, σ_z^∞, τ_xy^∞, τ_yz^∞, τ_zx^∞ [Ge 2004, pp. 1-4]
- 钻孔半径 a，径向距离 r，极角 θ [Ge 2004, pp. 1-4]
- 钻孔坐标系方向余弦：l_i, m_i, n_i (i=1,2,3) [Ge 2004, pp. 4-5]
- 应变花布置角度及测得的孔壁应变分量 [Ge 2004, pp. 4-5]

## Reusable Claims
1. **LBWCSRM 无需套钻即可实施应力解除**：该方法仅在钻孔局部壁面触发应力解除，不依赖取心操作，规避了传统套钻法的工艺约束与扰动问题 [Ge 2004, pp. 1-4]。（条件：需能进行孔壁应变测量的完整钻孔段）
2. **计算地应力张量时无额外假设**：反演过程不对主应力方向或应力状态做任何先验假定，仅依赖6个独立应变测量即可求解 [Ge 2004, pp. 1-4]。（限制：反演基于线弹性模型）
3. **理论深度无限制**：应力模型不显含钻孔深度变量，因而方法原则上可用于任意深孔 [Ge 2004, pp. 1-4]。（实际限制：测量系统耐压、耐温等未予讨论）
4. **应变花配位与坐标变换**：通过已知钻孔方位的方向余弦矩阵，可将孔壁局部应变场准确地转换为全局应力张量，并解决方程完备性问题 [Ge 2004, pp. 4-5]。（条件：需要钻孔定向参数）

## Candidate Concepts
- [[地应力测量]]
- [[应力解除法]]
- [[钻孔局部壁面应力全解除法 (LBWCSRM)]]
- [[深部地应力]]
- [[KTB 科学钻孔]]
- [[线弹性岩石力学]]

## Candidate Methods
- [[钻孔应变解除法]]
- [[套钻法 (overcoring)]]
- [[孔壁应变测量]]
- [[应力张量坐标转换]]

## Connections To Other Work
- 文中提及 KTB 科学钻孔已利用相关方法在 6000 m 深度估计完整应力张量（Brudy et al. 1997），LBWCSRM 可作为进一步拓展深部应力测量的候选方案 [Ge 2004, pp. 1-4]。
- 传统应力解除法通常被限制在约 30 m 深度，该方法意图消除这一深度瓶颈 [Ge 2004, pp. 1-4]。
- 主题上可与 [[水力压裂法]]、[[非弹性应变恢复法 (ASR)]] 等深孔应力测量方法建立概念连接，但片段未提供直接比较。

## Open Questions
- LBWCSRM 在真实深钻孔（如 >1000 m）中的验证案例和测量精度未在片段中报告。
- 在高偏应力或钻孔损伤区，线弹性假设的适用性及偏倚程度不详。
- 片段未讨论应力解除过程中裂隙、孔隙压力或温度变化的影响。

## Source Coverage
本页依据论文索引的两个片段 [Ge 2004, pp. 1-4] 与 [Ge 2004, pp. 4-5]，覆盖了摘要、引言、钻孔力学模型的建立、坐标变换框架以及主要结论。缺失的内容包括具体的实验或数值验证细节、实地应用案例、与其它方法的定量对比以及深入的误差与局限性分析。因此，本页对方法实际表现和工程适用性的反映并不完整。
