---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1998-shen-jin-三峡永久船闸高边坡岩体裂隙分布的分形研究-fractal-distribution-for-rock-mass-in-fractures-for-rock-mass"
title: "三峡永久船闸高边坡岩体裂隙分布的分形研究 [Fractal distribution for rock mass in fractures for rock mass in high slopes and its application to the lock of Three Gorges]."
status: "draft"
source_pdf: "data/papers/三峡永久船闸高边坡岩体裂隙分布的分形研究_申晋.pdf"
collections:
citation: "Shen Jin, Zhu Weishen, and Zhao Yangsheng. \"三峡永久船闸高边坡岩体裂隙分布的分形研究 [Fractal distribution for rock mass in fractures for rock mass in high slopes and its application to the lock of Three Gorges].\" 岩土工程学报, vol. 20, no. 5, 1998, pp. 97-98."
indexed_texts: "2"
indexed_chars: "6991"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "6961"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.995709"
coverage_status: "full-index"
source_signature: "5269576801d7fe3cf7f17801c232cdf7336ce925"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:07:01"
---

# 三峡永久船闸高边坡岩体裂隙分布的分形研究 [Fractal distribution for rock mass in fractures for rock mass in high slopes and its application to the lock of Three Gorges].

## One-line Summary
本文运用分形几何学研究了三峡永久船闸高边坡岩体裂隙的分布规律，发现其满足分形分布，并建立了可用于预测不同尺度下裂隙数量的关系式。

## Research Question
岩体结构面（裂隙）的几何参数随尺度变化的规律未知，阻碍了对岩体力学问题的深入认识。研究旨在定量描述三峡永久船闸高边坡岩体裂隙在不同尺度下的分布规律 [Shen 1998, pp. 1-3]。

## Study Area / Data
研究区域为三峡永久船闸北坡内的#11勘探平硐断面（2m×2m，硐口高程167m，长400m）[Shen 1998, pp. 1-3]。数据包括：
1.  在该平硐内选取的24个2.0m×2.0m研究区段。
2.  在平硐外侧开挖暴露岩体表面，按2.0m×2.0m、3.0m×3.0m和12.0m×12.0m三种尺寸范围进行的裂隙统计。
3.  在研究区段钻取的不同长度岩芯（∅92mm）共23段，用于细观分形研究和实验室测试 [Shen 1998, pp. 1-3]。

## Methods
采用分形统计方法：在岩体表面划定边长为L0的正方形区域，统计穿过该区域的裂隙条数N(L0)；然后将区域划分为边长为L1=L0/r（r为分形比，取r=2）的网格，统计并累加所有小网格内的裂隙条数作为N(L1)；依此类推得到不同尺度Li下的裂隙条数N(Li)。在双对数坐标系中，若ln Li与ln N(Li)呈线性关系，则满足分形分布关系式：N(Li) ∝ Li^{-D} [Shen 1998, pp. 1-3]。

## Key Findings
1.  三峡永久船闸高边坡岩体裂隙迹线长度与条数之间的分布满足分形关系式 N(L) = n0 L^{-D}，具有很强的统计自相似性 [Shen 1998, pp. 1-3]。
2.  在跨越10^2数量级的四种尺度（0.066m, 2.0m, 3.0m, 12.0m）下，分形维数D值变化很小，平均值约为1.195，表明存在无标度区域，裂隙分布具有随尺度不变性 [Shen 1998, pp. 1-3]。
3.  建立了从已知尺度预测未知尺度裂隙数量的公式：N(L) = 1.01 L_E^2 L^{-1.195}，其中L_E为工程区域边长 [Shen 1998, pp. 1-3]。
4.  由小尺度（如0.066m）预测较大尺度（如2.0m, 3.0m）的裂隙条数与实际统计结果吻合较好，但预测12.0m尺度时误差较大，主要原因是大尺度下裂隙（特别是小裂隙）统计误差较大 [Shen 1998, pp. 3-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 不同尺度下裂隙分布满足分形关系式 N(Li) ∝ Li^{-D}。 | [Shen 1998, pp. 1-3] | 对三峡永久船闸高边坡花岗岩体裂隙进行统计。 | 线性回归可信度均达90%以上。 |
| 四种尺度（L0=0.066m, 2.0m, 3.0m, 12.0m）下的平均分形维数D约为1.195。 | [Shen 1998, pp. 1-3] | 统计数据通过t检验，可信度≥90%。 | 无标度区域跨越10^2数量级。 |
| 提出预测公式 N(L) = 1.01 L_E^2 L^{-1.195}。 | [Shen 1998, pp. 1-3] | 假设在无标度区域内，分形维数D取平均值。 | 用于从已知尺度外推预测。 |
| 由L0=0.066m预测L0=2.0m和3.0m的裂隙条数与实际观测吻合较好。 | [Shen 1998, pp. 3-4] | 使用公式（7）进行预测。 | 预测值与统计值对比见图3。 |
| 由L0=0.066m或2.0m预测L0=12.0m的裂隙条数误差较大。 | [Shen 1998, pp. 3-4] | 使用公式（7）、（8）、（9）进行预测。 | 主要原因是12.0m范围内裂隙统计本身误差大，尤其对小裂隙易遗漏。 |

## Limitations
1.  在推测12.0m×12.0m大范围区域的裂隙条数时，预测值与实际统计值误差较大 [Shen 1998, pp. 3-4]。
2.  误差主要来源于大尺度下（特别是受开挖扰动后）岩体表面原生裂隙辨别困难，以及较短裂隙的统计不准确和遗漏 [Shen 1998, pp. 3-4]。

## Assumptions / Conditions
1.  岩体裂隙的分布满足分形几何的自相似性假设 [Shen 1998, pp. 1-3]。
2.  研究在特定的无标度区域（跨越10^2数量级）内进行，在此区域内分形维数D可视为常数 [Shen 1998, pp. 1-3]。
3.  预测公式的推导基于“在相同的地质生成条件下”这一前提 [Shen 1998, pp. 1-3]。

## Key Variables / Parameters
- **分形维数 (D)**: 表征裂隙分布复杂性的关键参数，本研究中平均值约为1.195 [Shen 1998, pp. 1-3]。
- **比例系数 (n0)**: 分形关系式 N(L) = n0 L^{-D} 中的系数，随初始观测尺度L0变化 [Shen 1998, pp. 1-3]。
- **网格尺度 (Li)**: 分形统计中使用的正方形网格边长，Li = L0 / r^i [Shen 1998, pp. 1-3]。
- **工程区域边长 (LE)**: 预测公式中目标工程区域的边长 [Shen 1998, pp. 1-3]。

## Reusable Claims
1.  **条件**: 对于三峡永久船闸高边坡花岗岩体，在跨越约0.066m至12.0m（10^2数量级）的尺度范围内。**主张**: 其裂隙迹线长度与条数的分布满足分形规律，分形维数D稳定在约1.195，表明该尺度范围内裂隙分布具有尺度不变性 [Shen 1998, pp. 1-3]。
2.  **条件**: 在相同的地质生成条件和无标度区域内。**主张**: 可以利用小尺度（如岩芯尺度）的裂隙分形统计结果，通过公式 N(L) = 1.01 L_E^2 L^{-1.195} 来预测工程尺度（如数米至十余米）岩体表面的裂隙数量分布 [Shen 1998, pp. 1-3]。
3.  **条件**: 当进行大范围（如12m×12m）岩体裂隙现场统计时。**主张**: 需要特别注意提高统计精度，尤其是对小裂隙的识别和统计，以减少预测误差 [Shen 1998, pp. 3-4]。

## Candidate Concepts
- [[分形几何]]
- [[岩体结构面]]
- [[裂隙分布]]
- [[尺寸效应]]
- [[无标度区域]]
- [[统计自相似性]]

## Candidate Methods
- [[分形统计方法]]
- [[网格覆盖法]]
- [[线性回归分析]]
- [[t检验]]

## Connections To Other Work
本文引用了B. B. Mandelbrot创立的分形几何学理论 [Shen 1998, pp. 1-3]。研究背景中提及，已有国内外学者对岩体结构面几何特征及网络系统进行了不同的分形研究 [Shen 1998, pp. 1-3]。具体参考文献包括Barton & Larsen (1985), La Pointe (1988), Sakellariou (1991), 谢和平等 (1988, 1990), 康天合等 (1995) 的工作 [Shen 1998, pp. 1-3]。

## Open Questions
1.  如何改进大尺度（如12m以上）岩体裂隙的现场统计方法，以减小统计误差，提高分形预测的准确性？
2.  所得的分形维数D≈1.195及预测公式是否适用于其他地质条件下的花岗岩体或其他岩性？
3.  裂隙分布的分形特征如何与岩体的力学性质（如强度、渗透性）建立定量联系？

## Source Coverage
所有非空索引片段均已处理。共处理2个索引片段，总字符数6991，编译后字符数6961，覆盖率（按字符）为99.57%。
