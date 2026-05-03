---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-marji-the-explosive-fracturing-technique-analysis-for-highly-low-permeable-reservoirs-using"
title: "The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method."
status: "draft"
source_pdf: "data/papers/2023 - The explosive fracturing technique analysis for highly low permeable reservoirs using analytical, displacement discontinuity and finite difference coupled method.pdf"
collections:
  - "论文"
citation: "Marji, Mohammad Fatehi, et al. “The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method.” *Journal of Petroleum Geomechanics*, vol. 6, no. 3, autumn 2023, p. 44. DOI: 10.22107/JPG.2023.412506.1208."
indexed_texts: "12"
indexed_chars: "58727"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "57433"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.977966"
coverage_status: "full-index"
source_signature: "cb94e133df95fdc3acceffe7f5789c57967a6a7d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:14:52"
---

# The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method.

## One-line Summary
本研究提出了一种分析‑数值耦合方法（格林函数解析解、显式有限差分法 FDM 与高阶位移不连续法 DDM），模拟爆炸冲击波和气体压力联合作用下低渗透储层井周径向裂缝的起裂与扩展过程，并评估其在页岩/致密油水平井增产中的适用性。[Marji 2023, pp. 1-2] [Marji 2023, pp. 12-13]

## Research Question
如何通过耦合解析与数值方法，完整模拟爆炸压裂中“冲击波致裂”和“气体压力驱动裂缝扩展”两个阶段，以评价其对高致密低渗透储层（非常规储层）增产的有效性？[Marji 2023, pp. 1-2] [Marji 2023, pp. 3-4]

## Study Area / Data
研究案例取自一伊朗油田，具体井深 4014.5 m。模拟中采用均质、各向同性、连续线弹性岩石假设，二维问题。岩石与爆炸参数见表 1。爆炸源用双指数衰减压力脉冲表示。数值模型尺寸 10 m × 10 m，井眼直径 0.2 m（半径 0.1 m），远场应力 σ Hmax = 92.5 MPa，σ hmin = 82.2 MPa。[Marji 2023, pp. 4-6] [Marji 2023, pp. 8-9]

**表 1 研究区特征（部分）**[Marji 2023, pp. 8-9]
| 参数 | 数值 |
|------|------|
| 深度 (m) | 4014.5 |
| 岩石密度 (gr/cm³) | 2.5 |
| 泊松比 | 0.2 |
| 弹性模量 (GPa) | 20 |
| 单轴抗压强度 (MPa) | 20 |
| 粘聚力 (MPa) | 14.3 |
| 摩擦角 (°) | 46 |
| 最大水平应力 σHmax (MPa) | 92.5 |
| 最小水平应力 σhmin (MPa) | 82.2 |
| 炸药密度 (gr/cm³) | 1.2 |
| 爆轰速度 VOD (m/s) | 4500 |

## Methods
- **解析解**：基于弹性动力学的 Lame‑Navier 方程，采用格林函数法求解爆炸冲击波引起的位移、应变和应力场，用于裂纹起裂验证。[Marji 2023, pp. 3-6]
- **有限差分法**：使用 FLAC2D 对冲击波传播阶段进行显式动力模拟。模型设置粘性吸收边界以模拟无限介质，输入远场地应力和爆炸压力脉冲（双指数形式）；评估井周塑性/破裂区及初生径向裂纹图案（6‑12 条）。[Marji 2023, pp. 3-4] [Marji 2023, pp. 6-9]
- **位移不连续法**：在准静态气体膨胀阶段，采用高阶二次位移不连续单元（含裂尖特殊单元）的间接边界元方法。将 FLAC2D 得到的初始裂纹图案输入 TDDQCR 代码，施加爆炸气体压力（通常为爆轰压力的 50%–60%）驱动裂纹扩展。[Marji 2023, pp. 9-10]
- **水平井延伸**：以水平井筒对称水力裂缝为例，基于线弹性断裂力学（模式 I、II 应力强度因子和最大拉应力准则）分析不同 β 值下的裂纹扩展模式。[Marji 2023, pp. 10-12]

## Key Findings
- **冲击波主导起裂**：仅考虑冲击波传播时，FLAC2D 模拟显示井周产生约 8 条主要径向裂纹（忽略微裂纹和不成熟裂纹）。[Marji 2023, pp. 9-10]
- **气体压力驱动扩展**：准静态 DDM 模拟表明，爆生高压气体在已起裂的径向裂缝内流动并加压，是使裂缝进一步扩展的主要驱动力。[Marji 2023, pp. 10-12]
- **裂缝长度受应力方向控制**：在非静水应力场中，沿最大水平主应力方向的径向裂缝（1 型）长度约 141.44 cm，长于沿最小水平主应力方向的裂缝（2 型，约 136.4 cm）。若为静水应力，两者长度近似相等且对称。[Marji 2023, pp. 10-12]
- **水平井适用性**：爆炸气体压力可数值模拟为水平井的水力压裂过程；裂缝扩展模式受几何参数 β 影响，β 较小时内裂纹扩展受外裂纹抑制。[Marji 2023, pp. 10-13]

## Core Evidence Table
| 证据 | 来源 | 条件/假设 | 备注 |
|------|------|-----------|------|
| 爆炸产生冲击波和高压气体两阶段致裂机制可提高非常规储层渗透率 | [Marji 2023, pp. 1-2] | 低渗储层；无水力裂缝连接的储层可能更适用 | 文中明确对比了水力压裂的局限 |
| 已有无水压裂技术中，爆炸压裂最经济且环保 | [Marji 2023, pp. 1-3] 引用 Rogala et al. (2013) | 无水压裂技术评估 | 来自文献综述 |
| 解析解与 FDM 数值解的位移和应力对比验证了模型的可靠性（图 4） | [Marji 2023, pp. 4-6] | 均质、各向同性、连续弹性介质；二维问题 | 解析解基于格林函数和 Navier 方程 |
| FDM 模拟仅考虑冲击波时，井周生成约 8 条主要径向裂纹 | [Marji 2023, pp. 9-10] | 忽略微裂纹和未成热裂纹 | 图 10a、10b |
| 准静态 DDM 模拟气体压力驱动后，径向裂纹长度约 136‑141 cm | [Marji 2023, pp. 10-12] | 气体压力约 50%‑60% 爆轰压力；案例参数 | 图 11 |
| 裂纹沿最大水平主应力方向更长 | [Marji 2023, pp. 10-12] | 非静水应力场 | 各向异性假设被排除在外 |
| 水平井数值模型中，β 值影响裂纹扩展模式；β=0.5 时内裂纹未完全扩展 | [Marji 2023, pp. 10-12] | 基于 LEFM 和最大拉应力准则 | 图 13 |
| 采用 FLAC2D‑TDDQCR 耦合可模拟完整的两阶段爆炸致裂 | [Marji 2023, pp. 10-12] | 动力 FDM 起裂 + 准静态 DDM 扩展 | 本研究核心方法 |

## Limitations
- 本研究仅考虑主要径向裂纹的扩展阶段，未纳入不成熟或更小的动力起裂裂纹，这些裂纹可能增强动态破裂效果。[Marji 2023, pp. 12-13]
- 未考虑围岩非均质性、各向异性和已有裂隙对爆炸致裂模式和裂纹长度的影响。[Marji 2023, pp. 10-12]
- 二维模型假设，无法描述三维裂纹扩展和应力重新分布。（来源未提供三维验证信息）
- 缺乏现场实验或生产数据验证，仅依赖数值与分析相互校验。（来源未提供现场数据）

## Assumptions / Conditions
- 岩石为均质、各向同性、连续弹性介质（二维问题）。[Marji 2023, pp. 4-6]
- 爆炸过程分为动态冲击波传播和准静态气体膨胀两个独立阶段。[Marji 2023, pp. 3-4]
- 动力模拟使用粘性吸收边界模拟无限域。[Marji 2023, pp. 8-9]
- 爆炸源压力由双指数衰减函数表示。[Marji 2023, pp. 9-10]
- 使用线性弹性断裂力学（LEFM）描述裂纹扩展，采用模式 I 和模式 II 应力强度因子与最大拉应力准则。[Marji 2023, pp. 10-12]
- 气体压力约为爆轰压力的 50%‑60%。[Marji 2023, pp. 10-12]

## Key Variables / Parameters
- 岩石力学参数：密度 2.5 gr/cm³，泊松比 0.2，弹性模量 20 GPa，单轴抗压强度 20 MPa，粘聚力 14.3 MPa，摩擦角 46°。[Marji 2023, pp. 8-9]
- 地应力：σHmax = 92.5 MPa，σhmin = 82.2 MPa。[Marji 2023, pp. 8-9]
- 爆炸参数：炸药密度 1.2 gr/cm³，爆轰速度 4500 m/s。[Marji 2023, pp. 8-9]
- 爆炸压力脉冲：双指数形式 P(t)=P0 (e^(-αt)-e^(-βt))，归一化因子 N≈4；α, β 根据岩体弹性参数和炮孔半径估算。[Marji 2023, pp. 9-10]
- 爆轰压力公式：P_d = (ρ_e × V_d² × 10⁻⁶) / (1+0.8ρ_e) （Jimeno et al., 1995）。[Marji 2023, pp. 8-9]
- 水平井模拟参数：无量纲参数 β，用于调节裂纹几何。[Marji 2023, pp. 10-12]

## Reusable Claims
- 在高致密低渗透储层中，“爆炸冲击波起裂 + 爆炸气体压力扩展”的两阶段机制是有效的无水压裂增产替代方案。（条件：储层缺乏连通裂缝；该结论基于均质连续介质数值模型）[Marji 2023, pp. 1-2] [Marji 2023, pp. 12-13]
- 基于格林函数的 Lame‑Navier 方程解析解可用于验证爆炸应力波引起的近场和远场位移与应力分布。（条件：均质、各向同性、弹性、二维、无限域）[Marji 2023, pp. 4-6]
- 使用 FLAC2D 进行动力模拟可生成可靠的井周径向裂纹起裂图案（约 6‑12 条主要裂纹）。（条件：需采用粘性吸收边界和合适的爆炸压力函数）[Marji 2023, pp. 9-10]
- 在非静水应力场中，径向裂纹沿最大水平主应力方向扩展更远，可作为裂缝延伸方向预测的依据。（条件：各向异性、天然裂隙等未考虑）[Marji 2023, pp. 10-12]
- FLAC2D‑TDDQCR 的耦合方法为模拟“两阶段爆炸致裂”提供了可行的数值流程。（条件：动力 FDM 负责起裂，准静态 DDM 负责气体压力扩展；尚未推广至三维）[Marji 2023, pp. 10-12]
- 爆炸气体压力可数值等效为水平井的水力压裂驱动力，通过调整裂纹几何参数 β 可控制扩展模式。（条件：基于 LEFM 的平面模型）[Marji 2023, pp. 10-12]

## Candidate Concepts
- [[爆炸压裂]]
- [[低渗透储层]]
- [[位移不连续法]]
- [[有限差分法]]
- [[弹性动力学格林函数]]
- [[径向裂纹]]
- [[冲击波致裂]]
- [[气体压力驱动裂缝]]
- [[水平井压裂]]
- [[线弹性断裂力学]]

## Candidate Methods
- [[显式有限差分法]]
- [[位移不连续法]]
- [[FLAC2D]]
- [[TDDQCR]]
- [[弹性动力学解析解]]
- [[格林函数法]]
- [[最大拉应力破裂准则]]
- [[应力强度因子]]

## Connections To Other Work
- 本文对比并引用了多种无水压裂技术（液体 CO₂、氮气泡沫、LPG 压裂、甲烷爆燃压裂等），并指出爆炸压裂可能是最经济、环保的方案。[Marji 2023, pp. 1-3]
- 引用 Rogala et al. (2013) 比较无水压裂技术；引用 Zhu et al. (2023) 的电脉冲冲击波研究；引用 Jiang et al. (2023)、Wang et al. (2023) 的甲烷爆燃压裂研究。[Marji 2023, pp. 1-3] [Marji 2023, pp. 12-13]
- 数值框架继承自作者团队此前开发的 DDM 工作（Abdollahipour et al., 2016; Marji, 2014; Haeri et al., 2015；FDM 背景详见 Lak et al., 2018, 2019）。[Marji 2023, pp. 6-8] [Marji 2023, pp. 13-15]
- 爆炸压力脉冲模型参考 Brady & Brown (2005)、Duvall (1953) 等经典文献。[Marji 2023, pp. 9-10]

## Open Questions
- 文中明确指出，未来的研究应纳入起裂阶段产生的“微裂纹和不成熟动力裂纹”，以评估它们对整体动态破裂效果的贡献。[Marji 2023, pp. 12-13]
- 非均匀性、各向异性以及已有裂隙/弱面对爆炸致裂模式和裂缝长度的影响尚未涉及。（来源未确认）
- 三维效应（如更真实的爆炸载荷分布和裂纹面扩展）是否需要耦合其他数值方法尚未讨论。（来源未确认）
- 缺少从数值模拟到实际储量产能提升的定量转换研究。（来源未确认）

## Source Coverage
All non-empty indexed fragments from the paper (12 source blocks, 58,727 indexed characters, 57,433 compiled characters) have been processed in a single-pass markdown compile with a compile ratio of 1.0 by blocks and 0.978 by characters. No text from outside the supplied fragments was used. Source signature: cb94e133df95fdc3acceffe7f5789c57967a6a7d. Full-index coverage status confirmed. Any unconfirmed or missing details are explicitly noted as not confirmed in the relevant sections.
