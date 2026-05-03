---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-meng-study-on-the-effect-of-sandstone-microscopic-damage-and-dynamic-compressive-properties"
title: "Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment."
status: "draft"
source_pdf: "data/papers/2022 - Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.pdf"
collections:
  - "论文"
citation: "Meng, Fandong, et al. “Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.” *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 1271-83. doi:10.1007/s00603-021-02733-3."
indexed_texts: "10"
indexed_chars: "46460"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46069"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991584"
coverage_status: "full-index"
source_signature: "3e70ea6eea8016d4fa07a9dc9b9966f794fac5c0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:00:29"
---

# Study on the Effect of Sandstone Microscopic Damage and Dynamic Compressive Properties After Heat Treatment.

## One-line Summary
研究不同高温处理后砂岩的微观损伤与动态压缩性能，揭示温度劣化与应变率强化的耦合效应，并建立考虑热损伤和冲击加载损伤的动态本构模型。

## Research Question
高温如何影响砂岩的物理化学特性（矿物组成、孔隙结构），以及温度劣化与冲击速度如何共同决定动态抗压强度、变形模量和本构关系？

## Study Area / Data
- **试样来源**：中国陕北石英砂岩，室温下石英含量93.1% [Meng 2022, pp. 2-3]。
- **尺寸**：直径98 mm，高50 mm的圆柱体 [Meng 2022, pp. 2-3]。
- **热处理**：6 个温度水平（20 °C、200 °C、400 °C、600 °C、800 °C、1000 °C），恒温2 h [Meng 2022, pp. 2-3]。
- **动态试验**：3 种平均冲击速度（8.6 m/s、14.6 m/s、18.8 m/s）下的SHPB单轴冲击压缩，每工况3个试件，共54个试件 [Meng 2022, pp. 2-3]。
- **微观测试**：XRD矿物分析、NMR孔隙度与T₂谱、MRI成像 [Meng 2022, pp. 2-3]。

## Methods
- **热处理**：AI‑518温控仪 + SX2‑10‑13马弗炉（最高1300 °C，精度1 °C），设定温度后恒温2 h [Meng 2022, pp. 2-3]。
- **矿物鉴定**：D/max 2500 X射线粉晶衍射仪（XRD） [Meng 2022, pp. 2-3]。
- **孔隙分析**：饱和水抽真空（4 h @ 0.1 MPa）+ 浸泡24 h，低场NMR系统MacroMR12‑150H‑I，T₂谱‑孔径转换系数C = 0.01 [Meng 2022, pp. 2-3, 3‑6]。
- **动态压缩**：Φ100 mm SHPB，45Cr合金钢（ρ=7850 kg/m³, E0=210 GPa），入射杆4.4 m，透射杆3.0 m，基于一维应力波理论计算应力‑应变 [Meng 2022, pp. 2-3, 6‑8]。
- **本构模型**：根据应变等效原理，定义总损伤 D = D0 + Di − D0Di，其中热损伤 D0 采用孔径面积权重法，冲击损伤 Di 基于 Weibull分布 [Meng 2022, pp. 9-10]。

## Key Findings
1. **矿物演变**：400 °C时赤铁矿全部还原为铁；温度升高导致粘土矿物分解（如高岭石500‑600 °C脱羟），石英含量增加 [Meng 2022, pp. 3-6]。
2. **孔隙变化**：孔隙度随温度呈S形增长，拐点311 °C，最大增长率0.95%；高温使大孔含量增加，孔径范围缩小 [Meng 2022, pp. 3-6]。
3. **温度‑应变率耦合**：动态抗压强度随温度升高而降低，低冲击速度下降更显著（8.6 m/s时1000 °C较20 °C下降45.53%，18.8 m/s时仅14.55%）。温度越高，应变率强化效应越强（1000 °C峰值强度增长率430.22%，20 °C为237.94%） [Meng 2022, pp. 6-9]。
4. **动态弹性模量**：E随温度呈“降低‑升高‑降低”三阶段，400‑600 °C回升反映冲击载荷增强效应；高冲击速度下E整体更高 [Meng 2022, pp. 8-9]。
5. **损伤本构模型**：耦合热损伤（孔径加权）与冲击损伤（Weibull分布）的模型曲线与1000 °C、8.6 m/s试验曲线几乎重合，模型合理 [Meng 2022, pp. 9-11]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 400 °C赤铁矿全还原，粘土矿物减少、石英增加 | [Meng 2022, pp. 3-6] | XRD，20‑1000 °C | Fig. 6, 7 |
| 孔隙度‑温度S形曲线，拐点311 °C，最大增长0.95% | [Meng 2022, pp. 3-6] | NMR饱和水，C=0.01 | Fig. 8 |
| 8.6 m/s时1000 °C峰值强度较20 °C下降45.53%，18.8 m/s仅14.55% | [Meng 2022, pp. 6-8] | SHPB三种冲击速度 | Fig. 14 |
| 峰值强度随应变率增长率：1000 °C为430.22%，20 °C为237.94% | [Meng 2022, pp. 8-9] | SHPB | Fig. 15 |
| 动态弹性模量在400‑600 °C出现回升 | [Meng 2022, pp. 8-9] | SHPB三种冲击速度 | Fig. 16 |
| 热‑载耦合本构模型验证曲线几乎重合 | [Meng 2022, pp. 10-11] | 1000 °C, 8.6 m/s | Fig. 17 |
| 应力平衡验证：σ_t = σ_i + σ_r 在18.8 m/s时成立 | [Meng 2022, pp. 6-8] | SHPB | Fig. 13 |

## Limitations
- 试验仅针对陕北石英砂岩，结论对其他岩性的普适性未验证（原文未提及）[推断]。
- 动态加载限于单轴冲击，没有围压条件（未在本文研究）[推断]。
- 假设岩石各向同性、满足一维应力波理论，实际可能有各向异性 [Meng 2022, pp. 6-8]。
- 未讨论不同冷却速率对损伤的影响（原文仅描述加热过程）[推断]。
- 孔隙分析中C=0.01为简化假设，实际可能变化 [Meng 2022, pp. 3-6]。

## Assumptions / Conditions
- SHPB试件和杆件各向同性，一维应力波理论适用 [Meng 2022, pp. 6-8]。
- 动态应力平衡 σ_t = σ_i + σ_r 成立（试验验证） [Meng 2022, pp. 6-8]。
- 孔径转换系数 C = 0.01 μm/ms（中国砂岩常用值） [Meng 2022, pp. 3-6]。
- 试件精度符合 GB/T50266‑2013 和 ISRM 标准 [Meng 2022, pp. 2-3]。
- 岩石强度服从 Weibull 统计分布 [Meng 2022, pp. 9-10]。
- 应变等效原理用于损伤耦合 [Meng 2022, pp. 9-10]。
- 热损伤因子采用变异系数加权的孔径面积比 [Meng 2022, pp. 9-10]。

## Key Variables / Parameters
- **温度**：20, 200, 400, 600, 800, 1000 °C
- **平均冲击速度**：8.6, 14.6, 18.8 m/s
- **动态峰值应力** σ_p，**峰值应变** ε_max，**动态弹性模量** E
- **孔隙度**，**微孔/中孔/大孔面积** (A_mic, A_mes, A_mac)
- **矿物含量**（石英、粘土矿物、赤铁矿）
- **损伤变量**：D0 (热损伤), Di (冲击损伤), D (总损伤)
- **本构参数**：c, φ, α, β, n, ε̇_s, F0, m (表1, 2) [Meng 2022, pp. 10-11]

## Reusable Claims
- 400 °C热处理后砂岩中赤铁矿完全还原，石英含量上升，粘土矿物减少 [Meng 2022, pp. 3-6]。
- 孔隙度随温度呈S形增长，拐点311 °C，最大增长率0.95% [Meng 2022, pp. 3-6]。
- 动态强度随温度升高而降低，但高冲击速度下温度劣化效应显著减弱 [Meng 2022, pp. 6-8]。
- 热处理砂岩的应变率敏感性随温度升高而增强，1000 °C时峰值强度应变率增长率约为20 °C时的两倍 [Meng 2022, pp. 8-9]。
- 动态弹性模量随温度变化呈现“温度弱化区‑冲击载荷增强区‑温度弱化区”三阶段特征 [Meng 2022, pp. 8-9]。
- 基于孔径权重的热损伤因子与Weibull分布冲击损伤因子耦合的本构模型能准确描述热处理砂岩的动态应力‑应变关系 [Meng 2022, pp. 9-11]。

## Candidate Concepts
- [[thermal damage]]
- [[dynamic compressive properties]]
- [[sandstone microscopic damage]]
- [[pore structure after heat treatment]]
- [[dynamic stress equilibrium]]
- [[strain rate effect]]
- [[temperature weakening and strain rate strengthening]]
- [[dynamic damage constitutive model]]
- [[S-shaped porosity-temperature curve]]
- [[quartz phase transition (α → β at 573 °C)]]

## Candidate Methods
- [[split Hopkinson pressure bar (SHPB) dynamic compression test]]
- [[low-field nuclear magnetic resonance (NMR) for pore characterization]]
- [[X-ray powder diffraction (XRD) for mineral identification]]
- [[magnetic resonance imaging (MRI) for pore distribution]]
- [[damage constitutive model coupling thermal and loading damage]]

## Connections To Other Work
- 与[[Meng et al., 2021]]研究冻融后砂岩的思路类似，采用孔径加权定义损伤因子。
- 引用[[Cao et al., 2017]]的非线性动态强度准则和[[Qi and Qian, 2003]]的微元强度公式建立加载损伤。
- 基础理论来自[[Lemaitre, 1984]]的应变等效原理。
- 温度对矿物和孔隙的影响与前人研究一致（如[[Hajpál and Török, 2004]]，[[Wong et al., 2020]]），但相较于仅单独考虑热损伤或加载损伤的模型，本文综合了两种损伤的耦合。

## Open Questions
- 这类砂岩的温度‑应变率耦合规律是否适用于其他沉积岩或火成岩？（原文未涉及）
- 围压条件下热‑载耦合本构模型如何修正？（原文仅单轴）
- 不同冷却方式（水冷、风冷）对动态损伤的影响？（原文未讨论）
- 微裂纹愈合现象在本文砂岩中未出现，在其他砂岩中是否存在？其原因是什么？[由温度劣化部分引申]
- 更高温度（>1000 °C）下动态力学特性与损伤演化规律？

## Source Coverage
所有非空索引片段均已处理（共10个片段）。按块数覆盖率为1.0，按字符数覆盖率为0.9916（索引字符总数46,460，编译使用46,069字符）。源签名为`3e70ea6eea8016d4fa07a9dc9b9966f794fac5c0`。本文完全基于提供的索引片段编译，未引入额外信息。
