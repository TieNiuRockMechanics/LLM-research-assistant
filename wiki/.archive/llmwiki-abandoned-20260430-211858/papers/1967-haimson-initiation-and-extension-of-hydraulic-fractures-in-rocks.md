---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "1967-haimson-initiation-and-extension-of-hydraulic-fractures-in-rocks"
title: "Initiation and Extension of Hydraulic Fractures in Rocks."
status: "draft"
source_pdf: "data/papers/1967 - Initiation and Extension of Hydraulic Fractures in Rocks.pdf"
collections:
  - "part4-2"
citation: "Haimson, Bezalel, and Charles Fairhurst. \"Initiation and Extension of Hydraulic Fractures in Rocks.\" *Society of Petroleum Engineers Journal*, vol. 7, no. 3, 1967, pp. 310-, onepetro.org/spejournal/article-pdf/7/03/310/2153162/spe-1710-pa.pdf. Accessed 2026."
indexed_texts: "7"
indexed_chars: "30873"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T10:26:58"
---

# Initiation and Extension of Hydraulic Fractures in Rocks.

## One-line Summary
该论文建立了考虑井筒周围三个应力场的垂直水力压裂起裂准则，并导出了裂缝扩展的压力-几何关系，从而可利用压裂数据反演岩层中的原位水平主应力。

## Research Question
如何基于多孔弹性理论描述垂直水力压裂的起裂与扩展过程？能否利用压裂过程中的井筒压力数据确定岩石中两个水平区域主应力？[Haimson 1967, pp. 1-2]

## Study Area / Data
未从索引片段中确认具体的现场研究区或实测数据。文中仅提供了一个理论数值算例，其中输入了假定的区域有效应力、弹性模量、泊松比和 Biot 系数等参数以展示计算流程，无实际压裂施工数据佐证 [Haimson 1967, pp. 7-9]。

## Methods
1. **井筒周围应力建模**：将无限大平板中圆孔受两向不等压的弹性解与注入流体引起的孔压扩散效应叠加，得到井周有效应力分布，其中假定注入流体与地层孔隙流体性质相似 [Haimson 1967, pp. 2-4]。
2. **起裂准则**：基于临界拉应力判据，分别导出了流体渗透井壁与非渗透井壁下的起裂压力表达式（Eq. 10、Eq. 13），并将后者与 Hubbert 的经典结果对比 [Haimson 1967, pp. 4-5]。
3. **裂缝扩展解析解**：将长度大于井径的垂直裂缝简化为平面内受内压和远场地应力的 Griffith 裂纹，采用 Muskhelishvili 复变函数方法和保角映射（\(z_D = \frac{1}{2}(\zeta + 1/\zeta)\)）求解应力场，在裂纹尖端应力有限的假设下导出裂缝宽度与压力、尺寸及材料参数的关系 [Haimson 1967, pp. 5-8]。

## Key Findings
- 井筒起裂所需的流体压力是岩石多孔弹性常数、两个不等水平主应力、抗拉强度和地层孔隙压力的函数；渗透与非渗透井壁的起裂公式不同 [Haimson 1967, pp. 1-5]。
- 恒速注入下，裂缝延伸至平衡后，维持裂缝张开的压力取决于岩石多孔弹性参数、垂直于缝面的区域应力分量、地层孔隙压力及裂缝尺寸 [Haimson 1967, pp. 1-2]。
- 裂缝最大宽度 \(W_{\text{max}}\) 与裂缝半长 \(L\)、垂直于裂缝的有效区域应力及注入压力之间存在闭合关系（Eq. 44），由此可由已知的任意两个变量估算第三个 [Haimson 1967, pp. 7-8]。
- 结合起裂压力方程和裂缝宽度/长度关系，可求解两个水平区域有效主应力；但不同于以往认知，要获得符合现实的应力估算必须知晓岩石的多孔弹性参数 \(E, \nu, \alpha\) [Haimson 1967, pp. 8-9]。
- 当注入流体不渗透井壁时，起裂准则退化为 Hubbert 所给出的形式，即仅与最小有效周向应力和抗拉强度相关 [Haimson 1967, pp. 4-5]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 起裂压力 \(P_{\text{breakdown}}\) 由（Eq.10）给出，它与抗拉强度、多孔弹性常数以及两个有效主应力等参数有关 | [Haimson 1967, pp. 4-5] | 线弹性多孔岩石，裸眼井壁光滑，注入流体可渗透井壁 | 方程显式包含 Biot 系数 \(\alpha\)、泊松比 \(\nu\) 等 |
| 非渗透井壁起裂准则（Eq.13）与 Hubbert 的公式一致 | [Haimson 1967, pp. 4-5] | 井壁被滤饼或低渗透材料堵塞，孔压不随注入改变 | 此时井壁处孔压等于远场地层压力 |
| 平衡状态下裂缝最大宽度公式（Eq.44）：\(W_{\text{max}} = \frac{4(1-\nu)L}{\mu}\left[...\right]\)（部分表达式） | [Haimson 1967, pp. 7-8] | 裂缝半长 \(L\)>>井径 \(r_w\)，裂纹尖端应力有限，远场应力与内压静态平衡 | 由 Muskhelishvili 法导出，\(W_{\text{max}}\) 与 \(L\), \(E,\nu,\alpha\) 及有效应力 \(\sigma_{22}\) 相关 |
| 数值算例：给定 \(\sigma_{22}=-1400\) psi, \(E=5×10^6\) psi, \(\nu=0.2\), \(\alpha=0.8\) 后可由 \(W_{\text{max}}/L\) 推算应力 | [Haimson 1967, pp. 7-9] | 同上参数条件，并知晓注入压力 \(p_i\) | 仅为演示范例，无实测对比 |

## Limitations
未从索引片段中确认实验验证、现场应用或误差分析；文中解析解仅适用于线弹性、均质、各向同性的多孔岩石，且要求裂缝为垂直、平面应变条件；扩展模型忽略了井筒对长裂缝应力场的扰动，仅在 \(L >> r_w\) 时成立；流体压力分布仅定性地指出因滤失而沿缝长递减，未给出具体的流-固耦合方程。

## Assumptions / Conditions
- 岩石为线弹性、均质、各向同性的多孔介质，满足 Biot 孔弹性理论框架 [Haimson 1967, pp. 1-4]。
- 总应力以张为正；垂直总应力 \(S_{33}\) 等于上覆岩层压力，且为中间主应力 [Haimson 1967, pp. 2-4]。
- 水力裂缝为垂直裂缝，在垂直于最大有效水平主应力 \(\sigma_{22}\) 的平面内向两侧对称延伸 [Haimson 1967, pp. 4-5]。
- 注入流体与地层原生孔隙流体物性相同，使渗流问题简化 [Haimson 1967, pp. 2-4]。
- 对于裂缝扩展分析，假设裂缝长度远大于井筒半径后，井筒应力集中影响可忽略，裂缝可视为无限大平板中的中心裂纹 [Haimson 1967, pp. 4-6]。
- 裂纹处于平衡状态，且尖端应力不是奇异的（即采用非奇异的应力边界条件）[Haimson 1967, pp. 5-7]。
- 裂缝内流体压力沿其长度分布，因向地层漏失而递减，但未假定具体的压力分布函数 [Haimson 1967, pp. 4-5]。

## Key Variables / Parameters
- **应力**：\(S_{11}, S_{22}\) 分别为最小与最大水平总主应力；\(\sigma_{11}, \sigma_{22}\) 为对应有效主应力；\(P_0\) 为原始地层孔隙压力；\(P_w\) 为井筒流体压力；\(p_m = P_w - P_0\)；\(p_i\) 为井筒内用于扩展裂缝的压力 [Haimson 1967, pp. 1-4, 7-8]。
- **岩石力学参数**：\(E\)（杨氏模量）、\(\nu\)（泊松比）、\(\alpha\)（Biot 有效应力系数）[Haimson 1967, pp. 7-9]；抗拉强度（符号未从片段中确认，摘要提及“tensile strength”）[Haimson 1967, pp. 1-2]。
- **几何参数**：\(r_w\)（井筒半径），\(L\)（裂缝半长），\(W\)（裂缝宽度），\(W_{\text{max}}\)/\(W_0\)（最大/井壁处裂缝宽度）[Haimson 1967, pp. 2-8]。
- **其他**：\(C_b, C_r\)（岩石体积与基质压缩系数，命名表中出现）[Haimson 1967, pp. 8-9]。

## Reusable Claims
- 当井壁被注入流体渗透时，垂直水力裂缝的起裂不能仅用经典有效应力准则判定，而必须考虑由井筒与地层孔压差引起的径向渗流附加应力场，因此起裂压力方程会显式包含 Biot 系数 \(\alpha\) 等孔弹性常数 [Haimson 1967, pp. 1-5]。
- 在非渗透井壁条件下，仅需最小有效周向应力达到岩石抗拉强度即可起裂，此时准则与 Hubbert（1953）的结论完全相同；这暗示了井壁存在滤饼或岩石渗透性极低时，可使用简化判据 [Haimson 1967, pp. 4-5]。
- 利用平衡状态下裂缝最大宽度与半长之比 \(W_{\text{max}}/L\) 结合井筒扩展压力，可通过闭合关系反算垂直于裂缝方向的有效区域应力 \(\sigma_{22}\)，前提是已知岩石的 \(E, \nu, \alpha\)；若进一步获得起裂压力，可求解两个水平有效主应力，实现地应力测定 [Haimson 1967, pp. 7-9]。
- 忽略多孔弹性常数的传统应力解释方法会导致不切实际的结果，因为孔弹性耦合显著影响裂缝宽度和压力响应 [Haimson 1967, pp. 8-9]。

## Candidate Concepts
[[hydraulic fracture initiation]], [[breakdown pressure]], [[poroelastic effect]], [[horizontal principal stress estimation]], [[Muskhelishvili method]], [[fracture width prediction]], [[effective stress law]], [[non-penetrating fracture criterion]], [[wellbore stress concentration]], [[plane strain crack]]

## Candidate Methods
[[elastic superposition]], [[conformal mapping]], [[complex variable method for cracks]], [[poroelasticity]], [[Biot coefficient]], [[stress intensity factor]]

## Connections To Other Work
- 文中将非渗透井壁下的起裂公式直接追溯至 Hubbert (1953) 的经典水力压裂准则，并证明两者在物理上等价 [Haimson 1967, pp. 4-5]。
- 多孔岩体的应力-孔压耦合是建立在 Biot 孔弹性理论基础上的，文中引用了 Biot (1956)、Geertsma (1957) 等关于多孔介质体积变化与热弹性比拟的工作 [Haimson 1967, pp. 9-9]。
- 裂缝扩展分析采用了 Muskhelishvili (1963) 的复势函数解法和 Bowie (1956) 的裂纹映射思路，属于平面弹性断裂力学的经典解析框架 [Haimson 1967, pp. 5-7, 9-9]。
- 概念上，本项研究可关联至利用压力-时间曲线解释地应力的 [[mini-frac stress testing]] 和 [[fracture pressure decline analysis]] 等现场方法。

## Open Questions
- 未从索引片段中确认该理论在真实地层（含天然裂缝、各向异性）中的适用性或修正方案。
- 没有证据显示文中有相应的室内实验或现场数据验证，因此模型预测的绝对精度和不确定性仍为开放问题。
- 裂缝延伸过程中流体压力分布与多孔介质滤失的详细耦合方程未给出，这限制了将该解析解直接用于更复杂的注入工况。
- 文中假设裂纹尖端应力有限，但未明确讨论起裂后扩展的动态效应或非弹性区，这与现代水压致裂断裂力学模型（如基于断裂韧性的扩展判据）如何衔接仍有待确认。

## Source Coverage
本知识页基于全部 **7**个索引片段编写，这些片段涵盖了论文的摘要、井筒周围弹性应力解、起裂准则推导与对比、裂缝扩展的复变函数解析过程以及最终应用公式和数值示例。覆盖的重点为理论推导与方法结果，偏重于核心方程和结论性陈述，但对引言背景、前人工作回顾、完整的参数敏感性分析以及任何可能的实验/现场验证部分**未能确认**，因为片段中未包含此类信息。此外，由于片段跳跃，部分公式推导的中间步骤（如式14-29的细节）以及完整的符号定义表未完全呈现。
