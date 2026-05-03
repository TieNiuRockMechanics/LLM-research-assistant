---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1967-haimson-initiation-and-extension-of-hydraulic-fractures-in-rocks"
title: "Initiation and Extension of Hydraulic Fractures in Rocks."
status: "draft"
source_pdf: "data/papers/1967 - Initiation and Extension of Hydraulic Fractures in Rocks.pdf"
collections:
  - "part4-2"
citation: "Haimson, Bezalel, and Charles Fairhurst. \"Initiation and Extension of Hydraulic Fractures in Rocks.\" *Society of Petroleum Engineers Journal*, vol. 7, no. 3, 1967, pp. 310-, onepetro.org/spejournal/article-pdf/7/03/310/2153162/spe-1710-pa.pdf. Accessed 2026."
indexed_texts: "7"
indexed_chars: "30873"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31038"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005344"
coverage_status: "full-index"
source_signature: "c5e721913e8f9c0833ce0e88cc0fdea85fe998a0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:24:36"
---

# Initiation and Extension of Hydraulic Fractures in Rocks.

## One-line Summary
本文提出了考虑井周多孔弹性效应的垂直水力压裂起裂与扩展理论，推导了起裂压力和裂缝宽度的解析表达式，并将其用于从压裂数据反演深部水平主应力。

## Research Question
如何将注入流体向多孔地层的渗透效应纳入水力压裂起裂和扩展准则，以更准确地预测破裂压力、确定裂缝几何尺寸，并由此推求原位区域应力？

## Study Area / Data
未指明具体研究区域；理论推导及数值示例均为一般性。数值示例采用假定参数：例1中 E = 5×10⁶ psi，ν = 0.2，α = 0.8，σ₂₂ = -1400 psi，pf = 1800 psi；例2中 E = 10×10⁶ psi，ν = 0.25，α = 0.9，pc = 2200 psi，σt（未明确写出但参与计算）等。来源：[Haimson 1967, pp. 7-8] 数值示例段。

## Methods
- **应力场叠加**：将井眼周围应力分解为三个场的叠加——（1）非静水区域水平应力（S₁₁, S₂₂）引起的应力集中；（2）井眼与地层压差引起的应力；（3）压差驱动的达西径向渗流引起的应力（类比热弹性）。来源：[Haimson 1967, pp. 2-4] “State of stress around the wellbore”。
- **起裂准则**：采用 Hubbert 的准则，即当井壁某点的有效切向应力达到岩石抗拉强度 σt 时起裂；仅考虑 θ = 0, π 处最大拉应力点，推导起裂所需压差（式10）。来源：[Haimson 1967, pp. 4-5] “Initiation of vertical fracture”。
- **裂缝扩展与宽度计算**：假设恒定注入速率下裂缝达到稳态（∇²p = 0），将裂缝简化为薄裂纹，使用 Muskhelishvili 复变函数方法和保形映射（2ω(ζ) = L(ζ + 1/(4ζ))），分别求解边界荷载（裂缝内压力与远场应力）和向地层渗流引起的裂缝面位移，叠加得到总裂缝宽度（式43、44）。来源：[Haimson 1967, pp. 5-8] “Extension of vertical fracture”和“Effect of regional stresses …”。
- **确定区域应力**：利用起裂压力方程（式10）和裂缝宽度方程（式44）联立，结合可测的 Wmax/L 或裂缝长度，反算 σ₂₂ 和 σ₁₁。来源：[Haimson 1967, pp. 7-8] “Numerical examples” 及结论。

## Key Findings
- **渗透性流体起裂压力**：包含流体渗透效应的起裂准则（式10）表明，破裂压力依赖于岩石多孔弹性参数 (ν, α)、抗拉强度 σt、水平有效主应力 σ₁₁ 和 σ₂₂ 以及地层孔隙压力 P₀。非渗透流体时，该准则简化为 Hubbert 准则（式13）。来源：[Haimson 1967, pp. 4-5]。
- **裂缝宽度与区域应力的关系**：稳态扩展垂直裂缝的总宽度 W（井眼处为 Wmax）由裂缝半长 L、垂直于裂缝面的有效区域应力 σ₂₂、注入压力 pf 及 E, ν, α 共同决定（式43、44）。井眼流体压力 pf 与最小水平有效主应力 σ₁₁ 无关。来源：[Haimson 1967, pp. 7-8] 式31、43、44。
- **反演区域应力**：若测知 Wmax/L 并结合起裂压力数据，可由式45、46 计算出 σ₂₂ 和 σ₁₁。数值示例给出 σ₁₁ = -2120 psi，σ₂₂ = -1700 psi（假定的岩石参数下）。来源：[Haimson 1967, pp. 8] 数值示例及结论。
- **线性关系**：当区域应力场固定时，Wmax/L 与井眼压力 pf 呈线性关系（式45），可用于现场推断。来源：[Haimson 1967, pp. 8] 及图7说明。
- **必须已知弹性参数**：与当时的部分认识不同，多孔弹性参数 (E, ν, α) 对获得现实结果是必需的。来源：[Haimson 1967, pp. 9] “contrary to what was previously believed…”。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 起裂压差公式 (式10)：\( p_c = \frac{3\sigma_{22} - \sigma_{11} + \sigma_t - \frac{1-2\nu}{1-\nu}\alpha p_c}{2 - \frac{1-2\nu}{1-\nu}\alpha} \) | pp. 4-5 推导至式10 | 弹性、多孔、各向同性、光滑井壁；渗透性流体；区域应力 S₁₁ = σ₁₁ - P₀, S₂₂ = σ₂₂ - P₀ | 若已知 σ₁₁、σ₂₂ 可预测破裂压力 Pc；否则与扩展方程联立求解 |
| 非渗透流体起裂准则 (式13)：\( p_c = 3\sigma_{22} - \sigma_{11} + \sigma_t \) | p. 5 式13及说明 | 非渗透流体，孔隙压力 P₀ 处处均匀 | 与 Hubbert (1957) 一致 |
| 裂缝总宽度方程 (式44)：\( W_{\max} = \frac{2(1-\nu^2)L}{E} [ - \sigma_{22} + p_f ] \cdot [ 2(1-\nu) - \alpha(1-2\nu) ] \) （原文式44经整理） | pp. 7-8 式43、44 | 稳态扩展、平面应变、平衡裂纹（尖端应力有限）；恒定注入速率 | 可由 Wmax, L, pf 中两个量求第三个量 |
| Wmax/L 与 pf 线性关系 (式45)：\( \frac{W_{\max}}{L} = \frac{2(1-\nu^2)}{E} [ - \sigma_{22} + p_f ] \cdot [ 2(1-\nu) - \alpha(1-2\nu) ] \) | p. 8 式45 | 给定的区域应力场 (σ₁₁, σ₂₂ 恒定) | 可用于从 Wmax/L 推算 σ₂₂ |
| 数值示例1：E=5×10⁶ psi, ν=0.2, α=0.8, σ₂₂=-1400 psi, pf=1800 psi → Wmax/L = 1.4×10⁻⁴，L=2000 in → Wmax≈0.28 in | p. 7 | 参数假定 | 示意裂缝宽度量级 |
| 数值示例2：Wmax/L=0.5×10⁻⁴, E=10×10⁶ psi, ν=0.25, α=0.9, pc=2200 psi → σ₂₂=-1700 psi, σ₁₁=-2120 psi | p. 8 | 参数假定 | 展示区域应力反演流程 |

## Limitations
- 结果并非完整解：必须预先知晓缝长或缝宽中的一个尺寸，才能准确确定另一个（结论语）[Haimson 1967, pp. 8]。
- 多孔弹性参数 (E, ν, α) 必须已知，否则得不到实际结果[Haimson 1967, pp. 9]。
- 所有推导基于弹性、均质、各向同性假设，且井壁光滑、圆形，未涉及岩石非线性、各向异性或粗糙度影响。
- 裂缝扩展分析仅针对垂直缝，且假定沿最大水平应力方向对称扩展；未考虑裂缝弯曲或非对称性。
- 渗流引起的位移计算中，假设 Re（外部半径）很大且取一阶近似（式41），可能损失精度。
- 未给出破裂时间或非稳态过程的定量描述。

## Assumptions / Conditions
- 岩石为弹性、多孔、各向同性、均质（Assumptions）[Haimson 1967, pp. 1]。
- 区域应力为非静水，且一个主应力垂直（上覆岩压 S₃₃ = -ρD）；地表平坦，地层不陡倾[Haimson 1967, pp. 1]。
- 井壁光滑、截面圆形[Haimson 1967, pp. 1]。
- 注入流体与地层原生流体性质相似[Haimson 1967, pp. 3]。
- 流体流动遵循达西定律；渗透率均匀，径向轴对称[Haimson 1967, pp. 3]。
- 问题简化为无限长圆柱体，水平横截面应力分布沿深度不变，满足平面应变[Haimson 1967, pp. 1, 6]。
- 裂缝起裂后对称扩展，裂缝尖端应力有限（平衡裂纹），压力沿缝长缓慢变化，可用多项式近似[Haimson 1967, pp. 5-6]。
- 稳态扩展阶段满足 ∇²p = 0（稳态渗流），且远处压力回归地层压力 P₀[Haimson 1967, pp. 6]。
- 热弹性类比适用于多孔弹性介质中流体流动引起的应力与位移[Haimson 1967, pp. 3, 6]。

## Key Variables / Parameters
- **应力和压力**：S₁₁, S₂₂, S₃₃（总主应力，拉为正）；σ₁₁, σ₂₂, σ₃₃（有效主应力）；P₀（原始地层孔隙压力）；Pw, Pc（井眼压力、起裂压力）；pf = Pf - P₀（稳态扩展时井眼压力差）；p(x)（裂缝内压力分布）；σt（岩石抗拉强度）。
- **岩石力学参数**：E（杨氏模量）、ν（泊松比）、α = 1 - C_r/C_b（孔隙弹性常数，C_r 基质压缩系数，C_b 体积压缩系数）。
- **几何参数**：rw（井眼半径）、re（外部边界半径）、L（裂缝半长）、Wmax（井眼处裂缝最大宽度）。
- **中间变量**：R, Re（映射平面中的半径）、ζ（映射平面复坐标）、ω(ζ)（映射函数）、φ, ψ（Muskhelishvili 应力函数）。
- **物理常数**：ρ（上覆岩石平均密度）、D（深度）。

## Reusable Claims
- 考虑流体渗入地层的垂直水力压裂起裂压力是岩石抗拉强度、两个水平有效主应力、地层孔隙压力以及岩石泊松比与孔隙弹性常数 α 的函数，表达式为式10。该准则在非渗透流体时退化为 Hubbert 准则（式13）。来源：[Haimson 1967, pp. 4-5]。
- 当注入速率恒定时，垂直裂缝进入稳态；裂缝宽度（尤其井眼处）由缝长、垂直于缝面的区域有效应力、注入压力差以及 E, ν, α 确定，且与最小水平有效应力无关。来源：[Haimson 1967, pp. 7-8] 式31、44。
- 在相同区域应力场下，最大缝宽与缝长之比与井眼压力呈线性关系，可用于从可测几何比反推 σ₂₂。来源：[Haimson 1967, pp. 8] 式45。
- 结合起裂压力数据和裂缝几何宽度数据，可唯一确定两个水平有效主应力（式10 与 式44 联立），但前提是多孔弹性参数必须已知。来源：[Haimson 1967, pp. 7-8] 数值示例及 p. 9 结论。
- 裂纹尖端应力有限的条件（式24‑25）给出了边界荷载函数的约束关系，是求解裂缝位移和宽度的关键中间结果。来源：[Haimson 1967, pp. 6] 推导。

## Candidate Concepts
- [[多孔弹性效应与水力压裂]]
- [[水力压裂起裂准则]]
- [[有效应力与区域应力解译]]
- [[Muskhelishvili 复变函数方法]]
- [[水力裂缝宽度方程]]
- [[达西渗流引起的附加应力场]]
- [[热弹性-多孔弹性类比]]
- [[保形映射与裂纹问题]]
- [[稳态裂缝扩展与平衡条件]]
- [[破裂压力与注入压力区分]]

## Candidate Methods
- [[三场应力叠加法求解井周应力]]
- [[复变函数保形映射求解裂缝位移]]
- [[利用压力-时间曲线区分破裂起裂与扩展]]
- [[基于裂缝宽度与长度反演区域应力]]
- [[多项式近似裂缝内压力分布]]
- [[弹性参数 (E, ν, α) 实验室测定]]
- [[印象封隔器判定裂缝方向并配合变注入速率控制缝长/缝宽]]

## Connections To Other Work
- **Hubbert & Willis (1957)**：本文起裂准则在非渗透极限下与之一致；并扩展至渗透情况（式13）[Haimson 1967, pp. 4-5]。
- **Biot (1941, 1956)**：多孔弹性理论与热弹性类比是处理渗流应力的基础（引用5, 6; 引用8）[Haimson 1967, pp. 3, 6]。
- **Geertsma (1957)**：流体压力下降对多孔岩石体积变化的影响与之相关（引用7）[Haimson 1967, pp. 9]。
- **Fairhurst (1964)**：水力压裂用于原地应力测量，本文为后续应力确定方法提供理论基础（引用1）[Haimson 1967, pp. 9]。
- **Muskhelishvili (1963)**：复变方法直接应用于裂纹应力与位移计算（多处引用）[Haimson 1967, pp. 5-6]。
- **Bowie (1956)**：圆形孔放射状裂纹分析为裂缝扩展简化提供支撑（引用10）[Haimson 1967, pp. 9]。
- **Nowacki (1962)**：热弹性解用于渗流应力场简化（引用9, 10）[Haimson 1967, pp. 3]。

## Open Questions
- 如何在不预知裂缝长度或宽度的条件下，仅利用井口压力数据同时确定两者的量值？“结果不构成完全解，因为需要预先知道裂缝的一个尺寸才能准确确定另一个”（结论）[Haimson 1967, pp. 8]。
- 对于非均质、各向异性或多层岩石，渗透效应和裂缝扩展规律如何修正？当前工作均假设均质各向同性。
- 裂缝起裂后的早期非稳态阶段（压力变化、渗透区发展）对总裂缝尺寸的影响未予考虑。
- 可控注入速率下裂缝长度与宽度的动态演化关系仍需实验或现场验证（提及可用印象封隔器验证裂缝方向，但未报道实验）[Haimson 1967, pp. 8]。
- 文中仅给出稳态的一阶近似，当 Re 不很大或压力分布与二次多项式偏差较大时，式44的精度有待评估。

## Source Coverage
所有非空索引片段均已处理，共 7 个片段，总计约 30873 索引字符，编译后字符数约 31038，覆盖比 1.0。未遗漏任何提供内容。
