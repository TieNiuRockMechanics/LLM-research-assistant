---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-feng-fractal-discrete-fracture-network-model-for-the-analysis-of-radon-migration-in-fractur"
title: "Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media."
status: "draft"
source_pdf: "data/papers/2020 - Fractal discrete fracture network model for the analysis of radon migration in fractured media.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Shengyang, et al. \"Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media.\" *Computers and Geotechnics*, vol. 128, 2020, 103810. *ScienceDirect*, doi:10.1016/j.compgeo.2020.103810. Accessed 12 Feb. 2026."
indexed_texts: "10"
indexed_chars: "46766"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:48:35"
---

# Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media.

## One-line Summary
本研究提出一种结合分形理论与离散裂缝网络（DFN）的模型，用于模拟裂缝介质中氡的迁移，并开发了可计算氡扩散系数和析出率的软件 [Feng 2020, pp. 1-1]。

## Research Question
如何利用分形 DFN 模型有效地描述复杂裂缝几何特征，并据此预测裂缝介质中的氡迁移行为？此前尚无研究将分形理论与 DFN 模型结合用于氡迁移分析 [Feng 2020, pp. 1-2]。

## Study Area / Data
- **天然露头验证**：使用一个自然露头的裂缝图，提取裂缝中心分布、长度和方向参数（拟合得到长度指数 *a* = 2.39，密度常数 α = 1.49，平均方向 *μ*₀ = 86.4°，Fisher 常数 *κ* = 5.24），生成区域为 100 m × 100 m、含 2163 条裂缝的 DFN。边界条件：下部 100 m 处铀矿床氡浓度 *C*₁ = 3.7 × 10⁵ Bq/m³，地表空气氡浓度 *C*₂ = 180 Bq/m³，岩石氡生成率 *q* = 0.43 Bq/m³/s [Feng 2020, pp. 5-7]。
- **实验验证数据**：使用铀尾矿、水泥和水制成的固化材料（尺寸 0.5 m × 0.5 m），内嵌 1 mm 厚塑料片构造特定裂缝网络（参数 *D*_f = 1.5，*a* = 3.5，α = 1.85，*μ*₀ = 45°，*κ* = 1），测定氡浓度（高、低浓度分别为 139102 Bq/m³ 和 8096 Bq/m³）及材料的氡生成率（0.12 Bq/m³/s），用以验证模型预测的氡析出率 [Feng 2020, pp. 4-5]。

## Methods
1. **裂缝网络生成**：
   - **中心与长度**：采用一阶模型 [Davy et al., 1990]：裂缝数分布 *n(l, L)dl = α L^{D_f} l^{-a} dl*，其中 *D*_f 为裂缝中心分布的分形维数（1 < *D*_f < 2），*a* 为长度指数（*a* > 1），α 为密度归一化常数。二维情形采用迭代细分（每步一分为四，尺度比 *l*_ratio = 2），三维每步分为八份，随后生成概率图并分配裂缝长度 [Feng 2020, pp. 1-2]。
   - **方向**：二维方向采用 von Mises-Fisher 分布 *f(θ|μ₀, κ) = e^{κ cos(θ‑μ₀)} / [2π I₀(κ)]*，其中 *μ₀* 为平均方向，*κ* 为 Fisher 常数（*κ* = *N_t* / (2|**r_n**|)）；*κ* 较小时趋于均匀分布，*κ* > 5 时集中于平均方向。三维方向按 Villaescusa（1993）方法生成倾角和倾向 [Feng 2020, pp. 2-3]。
   - **开度与形状**：裂缝开度 *d* 由开度‑长度相关模型给出：*d = γ_f l^{0.5}*，其中 *γ_f = (K_IC (1 − ν²)/E) √(8/π)*，*K_IC* 为断裂韧性，*E* 为杨氏模量 [Feng 2020, pp. 2-3]。

2. **氡迁移计算**：
   - 单裂缝内氡通量包含扩散与对流项，末端通量 *J(L) = η c₀ + β c_L + γ q*，具体参数由裂缝几何与流速决定（流速依立方定律 *v = 9.8 d² ΔH / (12 μ L)* 估算） [Feng 2020, pp. 3-4]。
   - 网络中仅连通裂缝参与迁移，孤立和“死端”裂缝忽略。节点处通量平衡构建稀疏线性方程组 **A x = b**，采用稀疏矩阵求逆解出节点氡浓度，再反算各裂缝通量 [Feng 2020, pp. 3-4]。
   - 开发了可计算氡扩散系数和析出率的二维/三维软件 [Feng 2020, pp. 1-1]。
   - 实验测定氡析出率公式为 *J = (c₂ − c₁) · ?*（片段中记为 *J = c₂ c₁ A Δt V*，准确形式未从索引片段中确认） [Feng 2020, pp. 4-5]。

## Key Findings
1. **模型有效性与鲁棒性**：与自然露头的裂缝网络对比，模型能刻画裂缝中心、长度分布和方向等关键统计信息（尽管在描述所有细节上存在局限）；与 Darcel 和 Sa（2006）的裂缝中心对关联函数结果一致 [Feng 2020, pp. 4-5]。
2. **REV 存在性与尺度规律**：在分析裂缝网络中氡迁移时，REV 确实存在，且 REV 尺寸随长度指数 *a* 的增大而减小，遵循指数衰减规律；当 *a* 由 2.0 增至 2.8 时，REV 尺寸从 60 m 降至 5 m（以 5% 变异系数为基准） [Feng 2020, pp. 7-9]。
3. **参数影响**：长度指数 *a* 增大意味着模型中含有更多短裂缝，由于氡在空气中的扩散长度有限（约 2.18 m），短裂缝占优的网络更快达到 REV [Feng 2020, pp. 8-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 生成的 DFN 与露头裂缝在中心对关联函数上一致 | [Feng 2020, pp. 4-5] | 二维；使用一阶模型和 von Mises-Fisher 分布；与 Darcel 和 Sa (2006) 对比 | 验证了模型描述裂缝空间结构的能力 |
| 实验测定氡析出率， DFN 材料含铀尾矿，给定裂缝参数 (*D*_f=1.5, *a*=3.5, *μ*₀=45°, *κ*=1) | [Feng 2020, pp. 4-5] | 0.5 m × 0.5 m 人工裂缝网络；高、低氡浓度 139102 Bq/m³ 和 8096 Bq/m³ | 验证模型计算氡析出率的有效性，但具体对照结果未在片段中给出数值 |
| REV 尺寸随 *a* 增加而指数下降，*a*=2.0 时 REV=60 m，*a*=2.8 时 REV=5 m | [Feng 2020, pp. 7-9] | 5% 变异系数阈值；二维 DFN 模型；平均有效氡扩散系数为指标 | 表明裂缝长度分布对等效参数有显著影响 |
| 露头案例中，生成 2163 条裂缝的 DFN，预测氡浓度分布（连通裂缝） | [Feng 2020, pp. 5-7] | 参数从露头获取；边界条件：*C*₁=3.7×10⁵ Bq/m³, *C*₂=180 Bq/m³, *q*=0.43 Bq/m³/s | 展示了模型的实际应用能力 |

## Limitations
- 一阶模型仅能捕获裂缝长度的统计分布趋势，无法精确再现自然裂缝的所有细节 [Feng 2020, pp. 4-5]。
- 模型仅考虑连通裂缝中的氡迁移，忽略基质中的扩散和滞留，可能低估总析出量 [Feng 2020, pp. 3-4]。
- 实验验证所用 DFN 为人工固化材料和规则的塑料片诱导裂缝，与天然裂缝的粗糙度和分叉特性有差异，但片段未量化这种差异的影响。三维验证的细节未在索引片段中充分说明。

## Assumptions / Conditions
- **裂缝网络假设**：裂缝中心分布符合分形特征（*D*_f 介于 1 和 2 之间），裂缝长度遵循幂律分布（*a* > 1），裂缝方向可用 von Mises-Fisher 分布描述，开度与长度的平方根成正比（弹性断裂力学假设） [Feng 2020, pp. 1-3]。
- **氡迁移假设**：氡在裂缝中的运移仅由扩散和压力驱动的对流传质控制，忽略放射性衰变链以外的反应；裂缝中的气体流动遵循立方定律；裂缝交叉点处通量守恒，忽略局部能量损失 [Feng 2020, pp. 3-4]。
- **边界与源项**：所考虑的模型入口处氡浓度恒定，岩石基体均匀产生氡（体源项 *q*），且无其他外部源 [Feng 2020, pp. 5-7]。
- **REV 判据**：以平均有效氡扩散系数的变异系数低于 5% 作为 REV 准则 [Feng 2020, pp. 8-9]。
- **实验条件**：人工 DFN 样品的裂缝完全由塑料片的位置决定，忽略基质渗透性对迁移的贡献；测定采用 RAD7 探测器，短时间间隔内浓度变化呈线性近似（用于计算析出率） [Feng 2020, pp. 4-5]。

## Key Variables / Parameters
- 裂缝网络参数：*D*_f （中心分布分形维数），*a* （长度指数），α （密度归一化常数），*μ*₀ （平均方向角），*κ* （Fisher 常数） [Feng 2020, pp. 1-3]。
- 几何参数：*d* （裂缝开度），*γ*_f （开度‑长度比例系数），*l*_ratio （生成过程的尺度比，固定为 2） [Feng 2020, pp. 2-3]。
- 力学参数：*K*_IC （断裂韧性），*E* （杨氏模量），*ν* （泊松比，出现在 *γ*_f 中但未单独列出） [Feng 2020, pp. 2-3]。
- 流体与迁移参数：空气密度 ρ，动力粘度 μ，压力头差 *ΔH*，扩散系数 *D*，氡生成率 *q*，氡浓度 *c*，氡析出率 *J* [Feng 2020, pp. 3-5]。
- 尺度指标：REV 尺寸（随 *a* 变化），变异系数 [Feng 2020, pp. 8-9]。

## Reusable Claims
- 以分形 DFN 方法生成裂缝网络时，若采用一阶模型且长度指数 *a* > 1，裂缝数量与长度满足幂律关系；该模型可推广至二维和三维，但三维生成需引入倾向和倾角分布 [Feng 2020, pp. 1-2]。
- 在仅考虑连通裂缝且气体流动遵循立方定律的条件下，氡迁移的节点守恒方程可化为大型稀疏线性系统 **A x = b**，利用稀疏矩阵求逆可高效求解 [Feng 2020, pp. 3-4]。
- 当裂缝网络长度指数 *a* 较大（即短裂缝占优）时，REV 尺寸以指数规律减小；对于氡扩散长度约 2.18 m 的空气，短裂缝网络在更小尺度上即达到等效性质 [Feng 2020, pp. 8-9]。
- 采用 von Mises-Fisher 分布描述裂缝方向时，若 *κ* > 5 则方向高度集中，*κ* 极小时趋于均匀分布；该分布可直接用于生成二维网络，三维需结合 Villaescusa 方法 [Feng 2020, pp. 2-3]。

## Candidate Concepts
- [[fractal discrete fracture network]]
- [[radon migration in fractured media]]
- [[fracture aperture-length relationship]]
- [[von Mises-Fisher distribution]]
- [[representative elementary volume (REV)]]
- [[radon exhalation rate]]
- [[fracture toughness]]

## Candidate Methods
- [[first-order fracture model (Davy et al.)]]
- [[von Mises-Fisher distribution modeling]]
- [[pair correlation function analysis]]
- [[sparse matrix algorithm for fracture flow]]
- [[cubic law for fracture flow]]
- [[outcrop fracture mapping and parameter fitting]]

## Connections To Other Work
- 与 Darcel 和 Sa（2006）的裂缝中心对相关函数结果进行对比，验证了所生成模型的空间分布合理性 [Feng 2020, pp. 4-5]。
- 引用了 Zhang 等（2019）的二维分形 DFN 模型用于渗透率预测，本研究将其扩展至氡迁移 [Feng 2020, pp. 1-2]。
- 与 Kim 和 Schechter（2009）的分形 DFN 孔隙度研究相关联，均利用分形描述裂缝多尺度特征 [Feng 2020, pp. 1-2]。
- 在力学开度方面，模型采用 Olson（2003）提出的开度‑长度相关方法，可连接到 [[dynamic fracture propagation]] [Feng 2020, pp. 2-3]。

## Open Questions
- 模型是否可推广至非饱和或水‑气两相条件下的氡迁移？未从索引片段中确认。
- 基质扩散和吸附对氡总析出率的贡献未被考虑，其影响程度和参数化方式待明确。
- 三维 DFN 模型的验证细节（除方向生成外）在索引片段中未充分展开，其与实验或露头三维数据的对比尚不明确。
- 模型对不同裂缝密度 α 和分形维数 *D*_f 的敏感度未在片段中系统展示。

## Source Coverage
本页依据论文的 10 个索引片段撰写，覆盖了标题、摘要、引言、核心方法（裂缝生成、氡迁移方程）、实验验证装置描述及部分参数、露头案例研究参数和结果、REV 分析的主要结论。片段主要来自方法部分和案例验证部分，结论部分较完整。但以下信息可能缺失：
- 实验验证部分的完整数据对比（例如氡浓度随时间变化的具体曲线）。
- 三维 DFN 生成的详细算法和三维氡迁移计算的具体推导。
- 软件界面、计算效率及参数敏感性分析的更多细节。
- 对模型局限性的深入讨论（仅在部分文字中暗示）。
- 所有引用文献的完整上下文。
