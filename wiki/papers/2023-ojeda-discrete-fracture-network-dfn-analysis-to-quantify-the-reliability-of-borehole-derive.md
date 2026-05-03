---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-ojeda-discrete-fracture-network-dfn-analysis-to-quantify-the-reliability-of-borehole-derive"
title: "Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity."
status: "draft"
source_pdf: "data/papers/2023 - Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Ojeda, Pedro, et al. \"Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.\" *Geosciences*, vol. 13, no. 6, 2023, article 187. doi:10.3390/geosciences13060187."
indexed_texts: "20"
indexed_chars: "98121"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "97893"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.997676"
coverage_status: "full-index"
source_signature: "6b0fb9392b616768bf2ff5505a474c025ce7ba4f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:20:40"
---

# Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.

## One-line Summary

本文利用离散裂隙网络（DFN）模型探讨了基于钻孔 1D 裂隙数据估计体积裂隙强度（P32）的可靠性，提出了考虑裂隙与钻孔夹角的可变区间长度计算 P32 的方法，并给出了减轻 DFN 模型中边界效应的校正步骤。

## Research Question

钻孔数据（1D）被广泛用于估算不可直接测量的体积裂隙强度 P32；实践中常采用 Terzaghi 加权并限制最小夹角（如 15°）以及使用钻程长度作为计算区间。本文拟回答：这种限制最小夹角和固定短区间长度是否会导致 P32 的系统性低估和高变异性？能否通过可变区间长度方法既捕捉空间变异性又避免人为改变强度？同时，DFN 模型中的边界效应如何影响目标强度，以及如何有效减轻这一效应？[Ojeda 2023, pp. 1-2][Ojeda 2023, pp. 19-20]

## Study Area / Data

本研究为纯数值模拟，无实际现场研究区。数据来自基于确定参数生成的 DFN 模型，包括不同的裂隙尺寸、强度和方位。模型使用 FracMan 8.0 软件生成，裂隙形状为等维度六边形，空间分布采用 Enhanced Baecher 模型。主分析中，生成了 48 个 DFN 模型，体积兴趣区为 100 m × 100 m × 100 m，并使用 10 口不同方向的合成钻孔进行采样。 [Ojeda 2023, pp. 3-5][Ojeda 2023, pp. 10-11]

## Methods

1. **边界效应分析**：在 150 m 边长的生成箱中生成裂隙，并用逐渐缩小的采样箱计算 P32，揭示边界效应对强度的影响。通过定义校正因子（目标 P32 / 采样平均 P32 的渐近值）重新调整输入强度，并采用“体积兴趣区边长 + 3 倍平均裂隙半径”的生成箱尺寸来减轻边界效应。  
2. **P10‑P32 关系研究**：生成一系列具有已知 P32 的 DFN 模型，用合成钻孔采样得到线性强度 P10，分析二者在不同裂隙尺寸下的关系。  
3. **钻孔推导 P32 的方法**：基于 Chilès 等人的方法（公式 4），对比不同最小偏差角（α）和采样区间长度对计算 P32 的影响。  
4. **可变区间长度方法**：提出根据裂隙与钻孔的锐角 α 选择不同区间长度（α≥15° 时用 10–20 m；2°≤α<15° 时用 20–50 m；1°≤α<2° 时用 >50 m 至全孔段）来计算 P32，然后叠加各区间结果，避免重复计数。  
5. **验证**：将计算得到的钻孔 P32 与按 10 m 网格直接计算的“实际”P32 进行对比，通过 100 次实现的累积频率曲线评估方法优劣。 [Ojeda 2023, pp. 3-8][Ojeda 2023, pp. 10-18]

## Key Findings

- DFN 模型存在不可忽视的边界效应，输入 P32 与目标体积内实际 P32 的差异可达 30%；当以裂隙中心为参考点生成裂隙时，收敛更快。 [Ojeda 2023, pp. 5-6]  
- 通过定义校正因子并使生成箱尺寸依赖于平均裂隙半径（如体积兴趣区边长 + 3 倍平均半径），可以有效将边界效应降低至可接受范围；校正因子在保持其他参数不变时与强度值无关。 [Ojeda 2023, pp. 6-8]  
- 当边界效应得到减轻后，P10 与 P32 呈线性关系，且该关系与裂隙尺寸无关；但裂隙尺寸仍是生成 DFN 的必要输入。 [Ojeda 2023, pp. 10-11]  
- 实践中限制最小偏差角为 15° 并使用钻程长度（如 3 m）计算 P32，会导致系统性低估和极高的变异性；而当最小角取 1° 时，平均 P32 与输入值吻合良好，但标准差增大。 [Ojeda 2023, pp. 12-13]  
- 采用可变区间长度法计算 P32，既能捕捉空间变异，又能避免人为增大或减小强度值。该方法在 10 口合成井中得到的 P32 中位数与输入 P32 偏差多在 1～5% 以内，线性拟合斜率接近 1，R² > 0.85。 [Ojeda 2023, pp. 16-18]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 边界效应导致输入 P32 与采样 P32 相差高达 30% | [Ojeda 2023, pp. 5-6] | 生成箱 150 m 侧长，裂隙平均半径 20 m，输入 P32 = 2 m⁻¹，中心点生成 | 采用表面点生成时偏差类似，但收敛更慢 |
| 校正因子 0.84（即 2.00/2.38）可使 100 m 兴趣体积内目标 P32 为 2 m⁻¹ | [Ojeda 2023, pp. 6-7] | 平均半径 20 m，兴趣区 100 m 立方体，生成箱取兴趣区 + 3 倍平均半径 | 曲线在距边界约 50 m 处稳定，略小于 3 倍平均半径 |
| 生成边界效应减轻后，P10 与 P32 呈线性关系且与裂隙尺寸无关 | [Ojeda 2023, pp. 10-11] | 多组尺寸（半径 2–25 m）和强度（1–8 m⁻¹），十口井采样 | 表明可从钻孔 P10 估计 P32，但先需裂隙尺寸生成 DFN |
| 最小 α = 15° 时，计算 P32 被低估，平行于钻孔的井（Well 5）低估达 24% | [Ojeda 2023, pp. 12-13] | 全井段计算，输入 P32 多水平，10 口井平均 | 随最小 α 减小，比率趋近 1，但离散度增大 |
| 可变区间法所得 P32 中位数与输入 P32 偏差 ≤5%，R² ≥ 0.85 | [Ojeda 2023, pp. 16-18] | 基于 10 口合成井，区间按 α 分类，100 次实现 | 优于固定 15° 和 3 m 区间的方法 |

## Limitations

- 研究完全基于合成 DFN 模型，尚未在实际数据中应用；由于无法直接测量原位 P32，计算结果无法通过野外实测验证。 [Ojeda 2023, pp. 19-20]  
- 所有裂隙被假设为极薄、平面、六边形且等维度（纵横比 1），与实际弯曲、非等维的天然裂隙存在差异。 [Ojeda 2023, pp. 20-21]  
- 空间分布采用随机独立模型（Enhanced Baecher），未考虑地质构造（如距断层距离）对强度的控制。 [Ojeda 2023, pp. 20-21]  
- 假定合成钻孔能识别所有被交切的裂隙，而实际钻孔记录中存在遗漏天然裂隙或误将机械破碎计为天然裂隙的偏差。 [Ojeda 2023, pp. 20-21]  
- 当裂隙尺寸极大时，所提出的边界效应减轻方法可能需要极大生成箱，导致计算时间不可接受。 [Ojeda 2023, pp. 20-21]

## Assumptions / Conditions

- 所有裂隙为平面、零厚度、六边形且形状恒定。 [Ojeda 2023, pp. 20-21]  
- 裂隙方位服从经自助法产生的 Fisher 分布，浓度参数 80。 [Ojeda 2023, pp. 4-5]  
- 空间模型采用 Enhanced Baecher，裂隙位置随机且独立。 [Ojeda 2023, pp. 4-5]  
- 裂隙尺寸服从对数正态分布，标准差为平均半径的 40%。 [Ojeda 2023, pp. 4-5]  
- 在可变区间法中，体积兴趣区内 P32 目标值的容许误差设定为 ±1%。 [Ojeda 2023, pp. 8-9]

## Key Variables / Parameters

- **P32**：单位体积内裂隙面面积总和（m⁻¹），不可直接测量，为 DFN 建模首选强度指标。 [Ojeda 2023, pp. 1-2]  
- **P10**：单位长度内裂隙数量（m⁻¹），即线性裂隙强度。  
- **α**（偏差角）：裂隙与扫描线之间的锐角；Terzaghi 加权中的 sinα 因子。 [Ojeda 2023, pp. 2-3]  
- **裂隙尺寸**：对数正态分布，平均半径从 2 至 25 m。  
- **生成箱/采样箱尺寸**：影响边界效应的关键尺寸，如 150 m 生成箱 vs. 100 m 兴趣区。  
- **校正因子**：输入 P32 与兴趣体积内平均采样 P32 的比值，用于抵消边界效应。  
- **区间长度**：用于计算 P32 的钻孔分段，推荐与 α 角相关。  
- **实现次数**：越大裂隙所需实现次数越多，如平均半径 25 m 需 30–50 次，2 m 仅需约 10 次。 [Ojeda 2023, pp. 7-8]

## Reusable Claims

- 在未减轻边界效应的 DFN 模型中，目标体积内的 P32 可能比输入值高出最多 30%，且使用裂隙中心生成方式收敛更快。 [Ojeda 2023, pp. 5-6]  
- 边界效应可通过“兴趣区边长 + 3 倍平均裂隙半径”的生成箱以及强度校正因子得到有效控制，校正因子在保持几何和方位不变时与强度值无关。 [Ojeda 2023, pp. 6-8]  
- 在边界效应受控条件下，P10 与 P32 呈线性关系，且该关系对裂隙尺寸不敏感，因此可用线性回归通过钻孔 P10 推断 P32 的均值与标准差。 [Ojeda 2023, pp. 10-11]  
- 将 Terzaghi/Chilès 公式中的最小偏差角设为 15° 并配合短区间（如 3 m 钻程）会系统性地低估 P32 且引入高变异性；应使用 1° 最小角和可变区间长度。 [Ojeda 2023, pp. 12-13][Ojeda 2023, pp. 16-17]  
- 可变区间法（α≥15° 用 10–20 m，2°≤α<15° 用 20–50 m，1°≤α<2° 用 >50 m）可在保持空间变异性的同时获得与网格“真实”P32 吻合良好的结果，线性拟合因子 ≈ 1，R² > 0.85。 [Ojeda 2023, pp. 16-18]  
- 若仅需平均 P32，建议使用钻孔全段长度且最小 α 限定为 1°，以避免极高加权因子或除零错误。 [Ojeda 2023, pp. 16-17]

## Candidate Concepts

- [[volumetric fracture intensity (P32)]]  
- [[linear fracture intensity (P10)]]  
- [[Terzaghi Weighting]]  
- [[Chilès’ methodology]]  
- [[Discrete Fracture Network (DFN)]]  
- [[boundary effects in DFN]]  
- [[orientation bias in fracture sampling]]  
- [[blind zone]]  
- [[Baecher spatial model]]  
- [[enhanced Baecher model]]  
- [[fracture size distribution]]  
- [[hexagonal fracture shape]]  
- [[P10-P32 linear relationship]]  
- [[cumulative average convergence plot]]

## Candidate Methods

- [[DFN modeling with FracMan]]  
- [[boundary effect correction via oversized generation volume and correction factor]]  
- [[variable interval length method for P32 estimation from boreholes]]  
- [[synthetic borehole sampling in DFN]]  
- [[cumulative average plot for realization convergence assessment]]  
- [[grid-based P32 validation against wellbore-derived P32]]

## Connections To Other Work

- 边界效应问题曾被 Priest (1993) 及 Samaniego & Priest (1984) 讨论，建议使用位于生成体中心的小体积兴趣区；Junkin et al. (2019) 提出在 DFN 边界添加裂隙轨迹以减轻边界效应。 [Ojeda 2023, pp. 3-4]  
- P10 与 P32 的线性关系曾由 Dershowitz & Herda (1992) 通过 DFN 模拟证明。 [Ojeda 2023, pp. 10-11]  
- Zhang & Einstein (2000) 提出结合钻孔和裸露面估计体积强度；Wang (2005) 提出了基于 Fisher 分布的 P10‑P32 数值近似；Chilès et al. (2008) 发展了基于 Terzaghi 加权的直接估计法，并建议不丢弃低角度数据。 [Ojeda 2023, pp. 2-2, 13]  
- 本研究中关于短区间（钻程）导致高变异性的结论与 Elmo & Stead (2021) 及 Yang et al. (2022) 对 RQD 计算中钻程长度问题的批评一致。 [Ojeda 2023, pp. 17-18]  
- 钻孔强度插值时的变异性问题与 Hekmatnejad et al. (2017) 的发现呼应，即在复合尺度上 P32 波动可能较大但有向均值回归的趋势。 [Ojeda 2023, pp. 14]

## Open Questions

- 可变区间方法在真实钻孔数据（含缺失、误判裂隙）中的表现如何？能否通过对实测数据的反算间接验证？  
- 若裂隙非等维度、弯曲或具有厚度，P10‑P32 线性关系是否仍成立？  
- 当裂隙密度受构造控制而非随机分布时，提出的边界校正和区间选择方法是否需要调整？  
- 对于极大裂隙（如数十米尺度），如何在实际应用中平衡生成箱尺寸和计算资源？

## Source Coverage

所有非空的索引片段（共 20 个片段，包含约 97,893 个字符）均已处理。覆盖比率（按片段计）：1.0；按字符计：0.997676。单次通篇编译完成，无二次加工。证据仅来自上述索引片段，未添加外部知识。
