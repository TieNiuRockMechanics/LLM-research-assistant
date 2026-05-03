---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-chen-study-on-the-stability-and-seepage-characteristics-of-underwater-shield-tunnels-under"
title: "Study on the Stability and Seepage Characteristics of Underwater Shield Tunnels under High Water Pressure Seepage."
status: "draft"
source_pdf: "data/papers/2023 - Study on the Stability and Seepage Characteristics of Underwater Shield Tunnels under High Water Pressure Seepage.pdf"
collections:
  - "郤"
citation: "Chen, Luhai, et al. \"Study on the Stability and Seepage Characteristics of Underwater Shield Tunnels under High Water Pressure Seepage.\" *Sustainability*, vol. 15, no. 21, 2023, p. 15581. doi:10.3390/su152115581."
indexed_texts: "17"
indexed_chars: "83560"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:21:25"
---

# Study on the Stability and Seepage Characteristics of Underwater Shield Tunnels under High Water Pressure Seepage.

## One-line Summary
基于流固耦合数值模拟，研究高水压渗流条件下双线盾构隧道的围岩稳定性与渗流特征，揭示地表沉降叠加效应及渗透各向异性的影响 [Chen 2023, pp. 1-2]。

## Research Question
高水压渗流作用如何影响水下双线盾构隧道施工过程中围岩的稳定性与渗流特征？具体关注：（1）地表沉降的叠加效应；（2）衬砌弱透水性对渗流场及管片变形的影响；（3）各向异性渗流条件下的孔压分布与地层变形规律 [Chen 2023, pp. 1-2, 8-9]。

## Study Area / Data
工程背景为中国太原地铁2号线的迎泽湖水下段。该段为双线盾构隧道，采用土压平衡（EPB）盾构施工。左线和右线隧道间距14.2 m，拱顶距湖底约13.5~18.2 m，湖底段隧道长度约156 m。迎泽湖深约1.5~5.0 m，湖宽约40~300 m。地下水为第四系松散层孔隙潜水，水位埋深2~7.5 m，受季节性影响年变幅约1.0 m；含水层厚、渗透系数大，且受湖水渗漏补给影响显著。隧道主要穿越2–4细砂质黏土和2–5中砂质黏土层 [Chen 2023, pp. 5-6]。

## Methods
研究方法包括理论推导与三维流固耦合数值模拟：
- 建立了各向异性渗流条件下双线盾构隧道施工强度分析的解析模型 [Chen 2023, pp. 1-2]。
- 数值模型尺寸为156 m (长) × 77 m (宽) × 46 m (高)，单元数237,640个，节点数244,332个。土体采用摩尔–库仑弹塑性模型，衬砌管片采用壳单元模拟 [Chen 2023, pp. 6-7]。
- 模拟采用异步开挖方式：左线先开挖（共130步），右线后开挖（131~260步），每步进尺2.4 m。盾构机外壳、盾尾间隙、注浆压力（环向均布）及硬化注浆材料均被逐步模拟 [Chen 2023, pp. 7-8]。
- 流固耦合分析基于以下控制方程：应力平衡方程（考虑有效应力原理、等效孔压系数 α），以及满足达西定律的渗流连续性方程。同时进行了各向异性渗透系数表达式的理论推导，以反映应力–渗流耦合过程中渗透系数的变化 [Chen 2023, pp. 3-6]。
- 边界条件：模型上表面施加5 × 10^4 Pa的均布压力以等效5 m水深；初始应力按自重应力计算。瞬态变形阶段，模型四周及底部边界设为不透水；长期固结沉降阶段，远场边界设为透水并保持初始静水压力。盾构开挖过程中，管片内边界孔压固定为0 [Chen 2023, pp. 7-8]。

## Key Findings
- **地表沉降叠加效应**：左线贯通后至双线贯通期间，左线隧道中心线上方地表沉降值增加了5.56 mm（增幅82%）。后行隧道开挖对先行隧道上方地表沉降有持续叠加影响 [Chen 2023, pp. 8-9]。
- **最大地表沉降值**：双线贯通后，最大地表沉降为-13.0 mm，位于双线隧道中心偏左位置 [Chen 2023, pp. 9]。
- **沉降发展过程**：左线隧道开挖面穿越监测断面过程中，地表沉降增量先增后减；开挖面距监测断面4.8 m时沉降开始，至开挖面过后9.6 m时最大沉降达7.6 mm [Chen 2023, pp. 8-9]。
- **渗流对变形模式的影响**：地下水渗流会显著增大地表沉降的范围与量值，并使地层变形模式呈漏斗状 [Chen 2023, pp. 2-3，引用 Lü et al.]。
- **衬砌透水性的影响**：在衬砌弱透水性的影响下，渗流场将受到改变，进而影响管片变形；监测需予以加强 [Chen 2023, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 左线开挖过程中，开挖面过监测断面后最大沉降达7.6 mm | [Chen 2023, pp. 8-9] | Y=78 m监测断面；左线开挖至9.6 m过断面后 | 增量先增后减 |
| 双线贯通后左线中心线上方地表沉降增幅达82%（+5.56 mm） | [Chen 2023, pp. 9] | 异步开挖，后行右线隧道施工后 | 沉降叠加效应 |
| 双线贯通后地表最大沉降值为-13.0 mm | [Chen 2023, pp. 9] | 位于双线隧道中心偏左位置 | |
| 数值模型尺寸156m×77m×46m，237,640单元 | [Chen 2023, pp. 6-7] | 范围取3–5D；密网格靠近隧道 | D为隧道直径 |
| 瞬态阶段模型四周及底部设为不透水边界 | [Chen 2023, pp. 7-8] | 软黏土渗透系数小，外部边界远不如排水 | 长期阶段边界透水且保持静水压力 |
| 管片密度2500 kg/m³，弹模34.5 GPa，泊松比0.3，刚度折减系数0.8 | [Chen 2023, pp. 7] | 取自文献[34–36] | 壳单元模拟 |
| 渗流连续性方程基于达西定律，考虑各项异性渗透系数 | [Chen 2023, pp. 3-5] | 假设地下水不可压缩，土壤变形为线性弹性 | 见公式(4) |
| 等效孔压系数 α 表达式(3)含实验常数a1, a2, a3 | [Chen 2023, pp. 3-4] | 0 < α < 1 | 未给出常数具体值 |

## Limitations
- 衬砌的弱透水性对渗流场及长期固结沉降影响的定量研究结果未从片段中确认具体数值。
- 各向异性渗透系数表达式推导的最终形式及其在数值模型中的具体实现未在片段中给出。
- 模型验证方面，未从片段中确认是否与现场监测数据进行了充分比对。
- 实验研究、离心模型试验和透明土试验等替代方法在本研究中未采用，故缺乏真实物理实验的验证 [Chen 2023, pp. 2-3]。

## Assumptions / Conditions
- 土体为饱和多孔连续介质，由土颗粒骨架和孔隙水组成，且土颗粒和水均假设为不可压缩 [Chen 2023, pp. 3]。
- 地下水渗流满足达西定律 [Chen 2023, pp. 3]。
- 土体变形为线性弹性或变形不显著 [Chen 2023, pp. 3]。
- 盾构外壳和衬砌管片单元均视为完全弹性且不透水 [Chen 2023, pp. 5]。
- 瞬态变形阶段，模型外部边界（除上表面）不透水；长期固结阶段，远场边界透水且保持初始静水压力 [Chen 2023, pp. 7-8]。
- 5 m 水深等效为上表面5×10⁴ Pa 均布压力和孔压边界 [Chen 2023, pp. 7-8]。

## Key Variables / Parameters
- σ′ᵢⱼ，σᵢⱼ，p，α, δᵢⱼ—有效应力张量、总应力张量、孔压、等效孔压系数（0<α<1）、克罗内克符号 [Chen 2023, pp. 3-4]；α的表达式含实验常数 a1, a2, a3，及体积应力 Θ [Chen 2023, pp. 4]。
- kₓ, kᵧ, k𝓏—x, y, z 方向的渗透系数 [Chen 2023, pp. 4]。
- γ_w, β_w, ε_V—水的容重、水的体积压缩系数、体积应变 [Chen 2023, pp. 4]。
- 隧道间距14.2 m，拱顶覆土深度13.5~18.2 m，隧道直径 D 未明确给出，但用作模型范围尺度 [Chen 2023, pp. 5-6]。
- 每步开挖进尺2.4 m，管片宽度1.2 m，总计260个开挖步 [Chen 2023, pp. 7]。
- 管片参数：密度2500 kg/m³, 弹模34.5 GPa, 泊松比0.3, 刚度折减系数0.8 [Chen 2023, pp. 7]。

## Reusable Claims
- 在高水压水下双线盾构隧道中，后行隧道开挖会导致先行隧道上方地表沉降产生叠加效应（本例中左线中心上方沉降增加82%，+5.56 mm），设计中应考虑该附加变形 [Chen 2023, pp. 9]。
- 基于有效应力原理和等效孔压系数 α 的流固耦合模型（公式1-3），可用于分析饱和土体中盾构隧道施工的应力场 [Chen 2023, pp. 3-4]。
- 渗流–应力耦合模拟中，需考虑渗透系数的各向异性，并建立其与主应变的演化关系，以反映应力场变化对渗流场的反馈 [Chen 2023, pp. 5-6]。
- 地下水渗流会显著改变无水条件下的地表沉降模式，增大沉降量和影响范围，使其呈漏斗状分布，该结论与 Lü et al. 的模拟结果一致 [Chen 2023, pp. 2-3]。

## Candidate Concepts
- [[anisotropic seepage]]  
- [[fluid-solid coupling]]  
- [[underwater shield tunnel]]  
- [[superposition effect of ground settlement]]  
- [[effective stress principle]]  
- [[Darcy’s law]]  
- [[Moore-Cullen elastic-plastic model]]

## Candidate Methods
- [[three-dimensional numerical simulation]]  
- [[asynchronous excavation simulation of dual-lane shield tunnel]]  
- [[conformal mapping in seepage analysis]]  
- [[shell element for lining segments]]  
- [[EPB shield machine step-by-step modeling]]  
- [[seepage continuity equation with anisotropic permeability]]

## Connections To Other Work
- 本文引用了 Chen et al. [20] 的离心模型试验，该实验研究了稳态渗流条件下隧道开挖面的稳定性，得出了有效支撑压力与水土压力差的关系 [Chen 2023, pp. 2]。
- 本文引用了 Feng and Chen [21] 的透明土可视化试验，该实验研究了饱和砂性地层盾构隧道施工中的突涌砂灾害 [Chen 2023, pp. 2]。
- 本文引用了 Lü et al. [24] 的有限元模拟，其结论为地下水渗流会显著增大地表沉降量及范围，并使变形呈漏斗状，与本文发现一致 [Chen 2023, pp. 2-3]。
- 本文的理论框架基于连续介质力学和有效应力原理 [31] [32]，渗流参数的解析研究参考了考虑各向异性的水下圆形隧道渗流场解析解 [19] [Chen 2023, pp. 2-4]。

## Open Questions
- 弱透水性衬砌对长期固结沉降和管片受力的定量影响规律如何？[Chen 2023, pp. 1-2]
- 各向异性渗透系数的具体演化方程及其在数值模型中的标定结果如何？
- 数值模拟结果与现场实测数据的对比验证情况未从索引片段中确认。
- 不同水深、不同土层组合条件下，沉降叠加效应的普适性规律如何？

## Source Coverage
本页依据论文《Study on the Stability and Seepage Characteristics of Underwater Shield Tunnels under High Water Pressure Seepage》的17条索引片段编写。片段覆盖了论文摘要、引言部分文献综述、方法与原理（含控制方程和工程背景）、模型建立与参数、边界条件、以及部分结果讨论（位移场分析）。覆盖深度偏向方法细节与沉降规律的定性—定量描述。重要信息如全部结果（特别是渗流场、应力场、塑性区分布的完整分析）、讨论中的参数敏感性分析、以及结论部分未在片段中体现。若需完整评估，需阅读全文。
