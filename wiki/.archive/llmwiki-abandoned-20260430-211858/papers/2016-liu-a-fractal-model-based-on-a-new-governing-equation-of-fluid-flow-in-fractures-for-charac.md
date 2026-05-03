---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac"
title: "A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks."
status: "draft"
source_pdf: "data/papers/2016 - A fractal model based on a new governing equation of fluid flow in fractures for characterizing hydraulic properties of rock fracture networks.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Liu, Richeng, et al. \"A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks.\" *Computers and Geotechnics*, vol. 75, 2016, pp. 57–68. doi:10.1016/j.compgeo.2016.01.025. Accessed 2026."
indexed_texts: "12"
indexed_chars: "59438"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:40:24"
---

# A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks.

## One-line Summary
本研究提出了一种整合裂缝长度分形分布（Df）与单裂缝表面粗糙度迂曲度（DT）的新控制方程，并通过 1290 个离散裂缝网络数值模拟验证了其对岩体等效渗透率的表征能力，发现流量与水力开度的 6/DT 次方成正比，优于经典立方律。

## Research Question
如何基于新的流量控制方程和分形描述方法，更准确地表征岩石裂缝网络在水力载荷下的渗透特性？具体而言，如何将裂缝网络几何分布的分形维数（Df）与单裂缝面外粗糙度引起的迂曲度（DT）统一纳入一个修正的立方律中，并评估其对等效渗透率的预测能力。

## Study Area / Data
本研究未基于某一特定地理区域的现场数据，而是使用文献中报道的原位测量关系（如 Olson、Klimczak 等关于张开型裂缝开度与长度的经验关系）作为参数基础，并通过蒙特卡洛方法生成大量二维离散裂缝网络（DFN）作为模拟对象。共生成 1290 个 DFN，模型边长从 0.5 m 到 43 m 不等，裂缝长度分布由分形维数 Df（范围 1.3–1.8）控制。未从索引片段中确认具体现场验证的岩石类型或地点。

## Methods
- **分形长度分布模型**：假设裂缝迹长 l 服从幂律分布，其数量‑长度关系由分形维数 Df 表征；通过 Df 与裂缝质量密度 dm 的经验关系确定模型尺寸对应的裂缝总数 [Liu 2016, pp. 4-5]。
- **单裂缝控制方程**：将基于立方律的流量公式修改为考虑迂曲度 DT 的形式，使流量 Q 与 e^{6/DT} 成正比，其中 e 为水力开度，DT 为描述三维表面粗糙度及流体流动迂曲长度的分形维数 [Liu 2016, pp. 4-5]。
- **裂缝开度‑长度关系**：针对“硬币形”张开模式裂缝，采用 emax ∝ a0 L^{0.5} 及 eavg = (π/4) emax 计算平均开度；系数 a0 由材料断裂韧性、杨氏模量和泊松比决定 [Liu 2016, pp. 3-4]。
- **DFN 生成与提取**：利用三组独立随机数分别控制裂缝的中心位置、方向和长度，按式（1）和式（11）生成裂缝，并删除不连通的孤立段；从大模型中提取不同尺寸的子网络进行流动模拟 [Liu 2016, pp. 5-7]。
- **流动模拟**：对每个 DFN 施加恒定水力梯度（水平方向 10 kPa/m），求解等效渗透率；共采用 10 组不同随机数种子生成 1290 个 DFN 以考察随机数影响 [Liu 2016, pp. 7-8]。

## Key Findings
- 裂缝长度‑数量幂律分布的指数 α 与分形维数 Df 呈高度线性负相关（α = -2.22 Df + 5.61, R²=0.994）[Liu 2016, pp. 8-9]。
- 由本模型计算得到的 α 值范围（1.17–3.39）与之前现场或数值研究报道的范围（如 Bour & Davy 1997: 1.0–3.0）基本一致 [Liu 2016, pp. 8-9]。
- 引入迂曲度分形维数 DT 后，DFN 的总流量与水力开度 e 的 6/DT 次方成正比，较经典立方律（e³）更符合文献中原位测量结果 [Liu 2016, pp. 1-2]。
- 等效渗透率对生成裂缝长度所用的随机数的敏感性高于对生成裂缝位置和方向的随机数 [Liu 2016, pp. 1, 8-9]。
- DT 能有效量化三维表面粗糙度对渗流的影响：DT=1.04 的裂缝比 JRC=20 的二维粗糙度参数对应的裂缝更粗糙，因其计入了面外几何效应 [Liu 2016, pp. 8-9]。
- DFN 的等效渗透率受 Df 和模型尺寸共同制约，裂缝数量随 Df 增大和模型尺寸增加而非线性变化，该关系可通过 Df 与 dm 的经验方程加以预测 [Liu 2016, pp. 4-5]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 裂缝数量‑长度幂律指数 α 与 Df 存在线性关系 α = -2.22 Df + 5.61（R²=0.994） | [Liu 2016, pp. 8-9, Fig.6] | 裂缝长度分布由分形模型生成，位置和方向均匀随机；Df=1.3–1.8 | 基于数值生成的 DFN，现场适用性需进一步验证 |
| 本模型所得 α 范围 1.17–3.39 与 Bour & Davy (1997) 的 1.0–3.0 相近 | [Liu 2016, pp. 8-9, Table 3] | 适用本研究 DFN 生成条件 | 与其他研究的 α 比较，支持分形长度分布的合理性 |
| DFN 流量 Q 与 e^{6/DT} 成正比 | [Liu 2016, pp. 1-2] | 修正立方律，考虑 DT 的三维迂曲效应 | 经典立方律对应 DT=1，Q∝e³；未给出详细推导图表 |
| DT=1.04 对应的面外粗糙度大于 JRC=20 | [Liu 2016, pp. 8-9] | 对比 Kulatilake et al. 的 DT‑JRC 关系（JRC=20 时 DT≈1.02） | DT 囊括 x‑y 平面及面外几何的影响 |
| 等效渗透率对裂缝长度随机数更敏感 | [Liu 2016, pp. 1, 8-9] | 基于 10 组随机数的 DFN 模拟 | 结论未量化敏感度差异的具体比值 |
| Df 与裂缝质量密度 dm 的经验关系 Df = a'' + b'' ln(dm + c'')，其中 a''=0.4594，b''=0.2797，c''=8.4968 | [Liu 2016, pp. 4-5] | DFN 必须满足裂缝长度分布遵循式（1）且位置、方向均匀随机 | 参数可能不适用于其他分布假设，且来自前驱研究 [33] |
| 模型尺寸‑裂缝数量公式 N0_t = Nt (L_n²/L_T²) … [部分公式未完整给出] | [Liu 2016, pp. 4-5] | 依托上述 Df‑dm 关系 | 未从片段中确认完整的公式及推导过程 |

## Limitations
- 模型仅考虑张开模式（penny-shaped）裂缝，且假设 L=W，不适用于剪切或撕裂模式占主导的裂缝系统 [Liu 2016, pp. 3-4]。
- DT 与裂缝粗糙度的对应主要通过与文献中 JRC 数值的类比间接论证，缺乏直接的原位粗糙度测量校准。
- 流动模拟在二维 DFN 中进行，未考虑基质渗流以及三维裂缝网络中的复杂拓扑结构；面外粗糙度仅通过 DT 参数化引入，而非直接几何建模。
- 对随机数敏感性的分析基于 10 组种子，统计稳定性未从索引片段中确认。
- Df‑dm 经验关系中的回归参数 a''、b''、c'' 仅限于裂缝长度分布遵循式（1）且位置方向均匀随机的 DFN，推广至其他分布形式的适用性未验证。
- 未从索引片段中确认对新控制方程的直接实验验证，其优越性仅通过与文献中间接的原位测量对比得出。

## Assumptions / Conditions
- 所有裂缝都属于“硬币形”张开模式，裂缝宽度 W 等于其长度 L；裂缝开度与长度满足 emax = a0 L^{0.5} 及 e = eavg = (π/4) emax [Liu 2016, pp. 3-4]。
- 单裂缝内流体流动可由修正立方律描述，且表面粗糙度引起的迂曲效应完全由分形维数 DT 表征，当不考虑面外粗糙度时 DT = 1，恢复经典立方律 [Liu 2016, pp. 4-5]。
- 裂缝网络的长度分布遵循幂律，可由分形维数 Df 描述；裂缝中心位置和方向在模型域内服从均匀随机分布 [Liu 2016, pp. 5-7]。
- 流体为恒定黏度的不可压缩牛顿流体，忽略基质渗透性，流动仅发生在裂缝网络中 [Liu 2016, pp. 5-7]。
- 水力模拟采用统一水平梯度（10 kPa/m），模型边界条件为两侧定压差、其余边界不透水 [Liu 2016, pp. 5-7]。
- 用于计算模型尺寸‑裂缝数量的式（11）及 Df‑dm 关系适用于裂缝长度分布由式（1）生成的 DFN，位置和方向均匀随机 [Liu 2016, pp. 4-5]。

## Key Variables / Parameters
- Df：表征裂缝网络长度分布几何特征的分形维数（取值 1.3–1.8）
- DT：表征单裂缝表面粗糙度引起流体迂曲效应的分形维数（DT ≥ 1）
- α：裂缝长度‑数量分布的幂律指数（由 Df 线性确定）
- a：幂律函数的比例系数
- e：水力开度（等同平均开度 eavg）
- emax：裂缝最大张开位移
- L：裂缝直长（用于 “硬币形” 裂缝亦等于宽度 W）
- Lt：裂缝迂曲长度
- Nt：某基准模型边长 LT 对应的裂缝总数
- N0_t：任意边长 Ln 模型中的裂缝数
- dm：裂缝质量密度
- a''、b''、c''：Df‑dm 经验关系中的回归参数（a''=0.4594, b''=0.2797, c''=8.4968）
- a0：控制张开模式裂缝开度‑长度关系的系数（与 K1c、ν、E 有关）
- K1c：材料固有断裂韧性
- ν：泊松比
- E：杨氏模量
- K：裂缝网络等效渗透率
- Q：流量
- μ：流体动力黏度
- R：生成裂缝位置、方向或长度所用的随机数
- JRC：节理粗糙度系数（仅用于与 DT 的比较）

## Reusable Claims
1. **裂缝长度‑数量的幂律指数 α 通过 α = -2.22 Df + 5.61 与分形维数 Df 关联**。该关系适用于 Df 在 1.3–1.8 范围内且裂缝位置和方向均匀随机分布的 DFN，基于大量数值模拟获得（R²=0.994）。限制在于其来源于数值生成的理想化网络，在真实岩体中的应用需通过现场裂缝编录进行校准 [Liu 2016, pp. 8-9]。
2. **对于考虑三维面外粗糙度的裂缝，修正立方律指出流量 Q 与 e^{6/DT} 成正比**。当 DT>1 时，该关系可捕捉粗糙度对渗流的额外抑制作用，预测结果优于经典 e³ 比例。该声明的局限在于 DT 的标定仍依赖于与 JRC 等二维指标的间接联系，需要更直接的粗糙度测量方法 [Liu 2016, pp. 1, 8-9]。
3. **Df 可通过裂缝质量密度 dm 按 Df = 0.4594 + 0.2797 ln(dm + 8.4968) 预测**，前提是裂缝网络的长度分布遵循给定的分形生成函数且位置、方向均匀随机。该关系仅适用于满足前述生成条件的二维 DFN，推广至其他裂缝分布模式时的误差大小尚未评估 [Liu 2016, pp. 4-5]。
4. **在蒙特卡洛生成的 DFN 中，等效渗透率对控制裂缝长度的随机数比对控制位置和方向的随机数更敏感**。这意味着在实际建模中应重点检验长度随机性对结果稳定性的影响。限制在于该结论基于 10 组随机数试验，且未量化不同 Df 和模型尺寸下的敏感度变化 [Liu 2016, pp. 1, 8-9]。
5. **分形维数 DT 可将裂缝三维粗糙度统一纳入一个指数形式的水力模型，当 DT=1.04 时对应的粗糙度已超过 JRC=20 的案例**。该声明可用于论证在 DFN 渗流计算中忽略面外粗糙度会大幅高估渗透性。限制是 DT 与 JRC 的对照基于文献中 Kulatilake 等人的工作，未提供本研究的独立验证实验 [Liu 2016, pp. 8-9]。

## Candidate Concepts
- [[fractal dimension Df]]
- [[tortuosity DT]]
- [[discrete fracture network]]
- [[cubic law]]
- [[penny-shaped fracture]]
- [[equivalent permeability]]
- [[fracture surface roughness]]
- [[power-law length distribution]]
- [[opening-mode fracture]]
- [[fracture aperture]]
- [[fracture length]]
- [[JRC]]
- [[Monte Carlo simulation]]
- [[fracture density]]
- [[representative elementary volume]]

## Candidate Methods
- [[fractal length distribution model]]
- [[modified cubic law with tortuosity]]
- [[DFN generation with random number sets]]
- [[Monte Carlo method for fracture networks]]
- [[fracture aperture-length correlation]]
- [[flow simulation in discrete fracture networks]]
- [[statistical analysis of fracture length distribution]]
- [[extraction of DFN sub‑models from large parent networks]]

## Connections To Other Work
- **与幂律指数 α 的比较**：本研究计算的 α 范围（1.17–3.39）与 Dverstop & Anderson (1989)、Bour & Davy (1997)、De Dreuzy (2001) 等现场观察或数值研究大多吻合，验证了分形长度分布模型的普遍性 [Liu 2016, pp. 8-9, Table 3]。
- **与粗糙度表征的对比**：借助 Kulatilake et al. 建立的 DT‑JRC 对应关系，将本文的 DT 值与已有的 JRC 量级进行对比，指出仅靠二维粗糙度描述会低估实际迂曲度，说明在 DFN 渗流中考虑三维粗糙度的必要性 [Liu 2016, pp. 8-9]。
- **裂缝开度‑长度经验规律的来源**：本文采用的张开模式裂缝开度公式直接引用 Olson (2003) 和 Klimczak et al. (2010) 的现场及理论工作，将材料力学参数（K1c，E，ν）与裂缝几何属性联结起来 [Liu 2016, pp. 3-4]。
- **与前期分形模型的延续**：作者在 [33] 中已建立了 Df 与等效渗透率的关系，但该研究所用模型边长固定为 5 m。本文扩展了模型尺寸的适用范围，并加入了 DT 修正的控制方程，从而提升了模型对多尺度特征的描述能力 [Liu 2016, pp. 2-3, 4-5]。

## Open Questions
- 如何将模型推广到包含剪切和撕裂模式裂缝的非均质网络，并使 DT 在不同破裂机制下保持物理一致性？未从索引片段中确认。
- DT 的无损直接测量方法以及与 JRC 等传统工程指标之间的定量校准关系仍需建立，目前仅基于类比和前人文献。
- 模型在真实三维岩体裂缝网络中的预测精度如何？需要补充基于现场渗透率测试的独立验证，这一点在本片段中并未涉及。
- Df‑dm 经验关系中的参数 a''、b''、c'' 对于非均匀分布（如成组定向裂缝）的适用性尚未讨论，其泛化能力有待检验。
- 随机数对不同分形维数 Df 和不同模型尺寸下等效渗透率变异性影响的定量程度未完整展示，这可能关系到 REV 判定的稳定性。
- 在哪些条件下基质的渗透性不能再被忽略，应考虑双重介质或多尺度渗透模型？本工作假设所有流动仅限于裂缝，此假设的适用范围未明确界定。

## Source Coverage
本 Markdown 页面基于 12 个索引片段构建，片段主要覆盖了摘要、引言（前人文脉络）、方法（控制方程、裂缝开度‑长度关系、Df‑dm 关系、DFN 生成与边界条件）、部分结果（α‑Df 线性关系、与前人 α 的比较、DT 与 JRC 的对比、随机数敏感性）等内容。由于片段并未涵盖论文的所有章节，以下信息可能缺失或不足：完整修正立方律的推导细节（特别是 Eq. 9 的形式）、流量‑开度关系 e^{6/DT} 的数据图表、不同 Df 和尺寸下等效渗透率的系统变化曲线、对随机数影响的详细统计分析、以及讨论与结论部分的完整论述。因此，本页面的某些声明可能未能呈现原文的全部论据和限制条件。
