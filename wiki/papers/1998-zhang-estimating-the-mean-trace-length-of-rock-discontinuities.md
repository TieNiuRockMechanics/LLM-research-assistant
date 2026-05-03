---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1998-zhang-estimating-the-mean-trace-length-of-rock-discontinuities"
title: "Estimating the Mean Trace Length of Rock Discontinuities."
status: "draft"
source_pdf: "data/papers/1998 - Estimating the Mean Trace Length of Rock Discontinuities.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhang, L., and H. H. Einstein. \"Estimating the Mean Trace Length of Rock Discontinuities.\" *Rock Mechanics and Rock Engineering*, vol. 31, no. 4, 1998, pp. 217-235. Accessed 2026."
indexed_texts: "8"
indexed_chars: "35338"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "35424"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.002434"
coverage_status: "full-index"
source_signature: "667ae0b7b8c860a6d4c4a506f381e8d08a8a01d9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:35:43"
---

# Estimating the Mean Trace Length of Rock Discontinuities.

## One-line Summary
提出一种无需迹长实测数据与方位信息的圆形采样窗口法，仅凭迹端截断、单端可见、双端可见的计数即可校正尺寸偏差与审查偏差，从而估计无限大面上不连续面平均迹长 \[Zhang 1998, pp. 1-3][pp. 8-10][pp. 17-19]。

## Research Question
如何在考虑尺寸偏差与审查偏差的情况下，利用有限尺寸圆形采样窗口内的迹线出现方式（双端截断、单端可见、双端可见）估计不连续面的总体平均迹长，且不依赖迹长测量与方位分布信息？\[Zhang 1998, pp. 1-3][pp. 5-8]。

## Study Area / Data
数据为FracMan离散裂隙网络代码生成的模拟迹线。两个模拟案例：各包含4000个圆形不连续面，放置于20 m×20 m×8 m的箱体中；在z=4 m水平面上设置半径c分别为1, 2, 3, 5, 9 m的圆形采样窗口。两个案例的极点方向均为30°/30°，但直径分布不同：模拟1为对数正态分布（均值2.0 m，标准差1.0 m），模拟2为负指数分布（均值2.0 m）。每个案例有10次实现；同时使用了不同位置多窗口（每次实现5个窗口）的采样方案以降低非均匀性影响。\[Zhang 1998, pp. 10-14][pp. 14-17]。

## Methods
1. **采样逻辑与计数**：在圆形窗口内将迹线分为三类：两端截断（N₀）、一端截断一端可见（N₁）、两端可见（N₂）。仅需计数，不测量长度。\[Zhang 1998, pp. 1-3][pp. 3-5]。
2. **数学模型推导**：基于三点假设（迹线中点均匀分布；迹长与方位独立；不连续面为平面且与窗口交为直线）推导出总体平均迹长m的估计式：
   \[
   m = \frac{\pi (N + N_0 - N_2)}{2(N - N_0 + N_2)} c
   \]
   样本估计式 \(\hat{m}\) 同理，用 \(\hat{N}, \hat{N}_0, \hat{N}_2\) 替代。\[Zhang 1998, pp. 5-8][pp. 8-10]。
3. **验证方法**：用FracMan模拟迹线，分别用估计式获得预测值\(\hat{m}\)；同时基于Warburton (1980) 体视学关系推导理论解（对数正态 \(\mu_l = \frac{\pi}{4}[1+(\sigma_D/\mu_D)^2]\mu_D\)；负指数 \(\mu_l = \frac{\pi}{2}\mu_D\)），比较相对误差。\[Zhang 1998, pp. 10-14][pp. 17-19]。

## Key Findings
- 所提方法可有效校正长度偏差（2b）与审查偏差（4），且无需迹长实测数据与方位分布信息；适用于任意方位分布的迹线，亦可处理多组不连续面。\[Zhang 1998, pp. 8-10][pp. 17-19]。
- 两个模拟案例中，预测平均迹长与理论解的相对误差范围分别为−8.3%～13.3%（对数正态）和−12.6%～6.9%（负指数），且误差与窗口尺寸无系统关系。\[Zhang 1998, pp. 14-17]。
- 直接采用观测迹长平均值会明显低估真实均值，且窗口越小偏差越大，表明审查偏差占主导，但随窗口增大而减小。\[Zhang 1998, pp. 10-14]。
- 使用多个相同尺寸、不同位置的窗口取平均，可降低迹线分布非均匀性带来的估计波动，提高结果稳定性。\[Zhang 1998, pp. 14-17]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 估计式 \(\hat{m} = \frac{\pi(\hat{N}+\hat{N}_0-\hat{N}_2)}{2(\hat{N}-\hat{N}_0+\hat{N}_2)}c\) | \[Zhang 1998, pp. 8-10] | 迹线中点均匀分布；迹长与方位独立；圆形窗口半径c已知 | 仅需计数三类迹线，不测量迹长 |
| 对数正态直径下理论均值关系 \(\mu_l = \frac{\pi}{4}[1+(\sigma_D/\mu_D)^2]\mu_D\) | \[Zhang 1998, pp. 17-19] | 直径服从对数正态分布，圆形不连续面 | 用于验证模拟案例 |
| 负指数直径下理论均值关系 \(\mu_l = \frac{\pi}{2}\mu_D\) | \[Zhang 1998, pp. 14-17][pp. 17-19] | 直径服从负指数分布，圆形不连续面 | 用于验证模拟案例 |
| 模拟1（对数正态，μD=2.0 m）预测均值平均2.052 m，误差−8.3%～13.3% | \[Zhang 1998, pp. 14] | 5个窗口尺寸，10次实现；无截断偏差 | 理论解μl=1.963 m |
| 模拟2（负指数，μD=2.0 m）预测均值平均3.195 m，误差−12.6%～6.9% | \[Zhang 1998, pp. 14] | 同上 | 理论解μl=3.142 m |
| 观测迹长均值均小于预测均值，且随窗口减小差距增大 | \[Zhang 1998, pp. 10-14] | 审查偏差相对于尺寸偏差占主导 | 强调偏差校正必要性 |
| 多窗口（5个）取平均后预测结果波动减小 | \[Zhang 1998, pp. 14-17] | 窗口半径2 m，不同位置 | 推荐实际采样采用多个窗口 |

## Limitations
- 方法假设迹线中点均匀分布；当所有迹线两端均可见（\(\hat{N}_2 = \hat{N}\)）时，该假设被违背，估计量失效（\(\hat{m}=0\)），此时需改用最大似然法。\[Zhang 1998, pp. 8-10]。
- 当窗口过小以致所有迹线两端截断（\(\hat{N}_0 = \hat{N}\)）时，估计趋向无穷，需增大窗口尺寸。\[Zhang 1998, pp. 8-10]。
- 推导忽略了截断偏差，并假设已采取足够小的截断长度（如10 mm）以使其影响可忽略。若实际截断阈值较大，校正不完整。\[Zhang 1998, pp. 3-5]。
- 验证仅基于模拟数据；未在文中提供实际岩体露头数据的应用案例。\[Zhang 1998, pp. 10-17]。
- 估计量\(\hat{m}\)的标准差特性文中未给出，仅提及其无偏性，方差研究待后续发表。\[Zhang 1998, pp. 8-10]。

## Assumptions / Conditions
1. 所有不连续面为平面，与窗口的交线为直线迹线。\[Zhang 1998, pp. 3-5]。
2. 迹线中点在二维采样面内均匀分布。\[Zhang 1998, pp. 3-5]。
3. 迹长与迹线方位统计独立。\[Zhang 1998, pp. 3-5]。
4. 窗口为有限半径c的圆形，且采样时仅记录窗口内的迹线段，未考虑伸出的部分。\[Zhang 1998, pp. 1-3]。
5. 截断偏差已通过采用足够小的截断长度降至可忽略水平。\[Zhang 1998, pp. 3-5]。
6. 计数时明确区分三类端点状况，且不要求测量实际迹长。\[Zhang 1998, pp. 5-10]。

## Key Variables / Parameters
- \(c\)：圆形采样窗口半径
- \(N\)：窗口内迹线总数
- \(N_0\)：两端截断迹线数
- \(N_2\)：两端可见迹线数
- \(m\) 或 \(\mu_l\)：平均迹长（总体）
- \(\hat{m}\)：平均迹长样本估计
- \(m_D, \mu_D\)：不连续面直径均值
- \(\sigma_D\)：直径标准差
- \(f(\theta,\phi)\) 和 \(f(l)\)：方位与迹长概率密度函数（推导中未直接需要）

## Reusable Claims
- 可在不测量迹长、不获取方位数据的情况下，仅根据圆形窗口内三类端部条件的计数估计平均迹长（\(\hat{m} = \frac{\pi(\hat{N}+\hat{N}_0-\hat{N}_2)}{2(\hat{N}-\hat{N}_0+\hat{N}_2)}c\)），条件是迹线中点均匀且迹长与方位独立。\[Zhang 1998, pp. 8-10]。
- 当迹线中点均匀假设有效时，该估计量无偏。\[Zhang 1998, pp. 8-10]。
- 忽略截断偏差并校正尺寸偏差与审查偏差后，预测平均迹长与理论解吻合良好（误差约±13%以内）。\[Zhang 1998, pp. 14-17]。
- 直接使用观测迹长的算术均值会明显低估平均迹长，且这种低估随采样窗口减小而加剧。\[Zhang 1998, pp. 10-14]。
- 采用多个相同尺寸、不同位置的圆形窗口并对估计值取平均，可有效降低迹线空间非均匀性的影响。\[Zhang 1998, pp. 14-17]。

## Candidate Concepts
- [[mean trace length]]
- [[circular sampling window]]
- [[censoring bias]]
- [[size bias]]
- [[truncation bias]]
- [[orientation bias]]
- [[trace midpoint uniformity]]
- [[trace length orientation independence]]
- [[stereological relationship (trace length vs. discontinuity diameter)]]
- [[FracMan discrete fracture network]]

## Candidate Methods
- [[circular window sampling for trace length estimation]] (Zhang & Einstein 1998)
- [[non-measurement trace length estimation from end-condition counts]]
- [[correction of length and censoring biases without orientation data]]
- [[multi-window averaging to reduce spatial heterogeneity]]
- [[theoretical relation for mean trace length from diameter distribution (lognormal and exponential)]]

## Connections To Other Work
- 继承了Pahl (1981) 和Kulatilake & Wu (1984) 的矩形窗口估算框架（需方位分布），但将其拓展至圆形窗口，从而消去对方位分布的依赖。\[Zhang 1998, pp. 3-5][pp. 17-19]。
- 对截断偏差的忽略基于Warburton (1980) 的截断校正方法与Priest & Hudson (1981) 关于低截断水平的建议。\[Zhang 1998, pp. 3-5]。
- 理论解推导直接使用了Warburton (1980) 的体视学关系式 (A1)。\[Zhang 1998, pp. 17-19]。
- 当迹线中点均匀假设不成立时，引用了Baecher (1980)、Laslett (1982) 等的最大似然法作为替代。\[Zhang 1998, pp. 8-10][pp. 19]。
- 模拟工具采用了FracMan (Dershowitz et al., 1993)。\[Zhang 1998, pp. 10][pp. 19]。

## Open Questions
- 估计量\(\hat{m}\)的标准差（方差）特性尚未给出，文中指出正在研究并将另行发表。\[Zhang 1998, pp. 8-10]。
- 方法在实际野外露头上的适用性，尤其当迹线中点均匀性假设受强烈非均匀分布挑战时的表现，未经验证。\[Zhang 1998, pp. 10-17]。
- 对于非常小的窗口（导致大多数迹线两端截断）或所有迹线两端可见的极端情况，如何系统性调整或选择合适的窗口尺寸准则，未深入讨论。\[Zhang 1998, pp. 8-10]。

## Source Coverage
本文所有8个非空索引片段均已处理，覆盖整篇论文。编译后字符数比原始索引字符数多约0.24%，原因是章节标题与标点格式化。覆盖率按块计为100%，按字符计为100.24%，来源签名为 `667ae0b7b8c860a6d4c4a506f381e8d08a8a01d9`，判定状态为完整索引。
