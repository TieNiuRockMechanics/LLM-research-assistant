---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-zhang-microbial-community-composition-in-deep-subsurface-reservoir-fluids-reveals-natural-i"
title: "Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity."
status: "draft"
source_pdf: "data/papers/2020 - Microbial Community Composition in Deep-Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.pdf"
collections:
  - "part4-1"
citation: "Zhang, Yuran, et al. \"Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.\" *Water Resources Research*, 2019, doi:10.1029/2019WR025916. Accessed 2026."
indexed_texts: "22"
indexed_chars: "109508"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "109989"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004392"
coverage_status: "full-index"
source_signature: "8a13c56b3a216e8913bbf468edbbde616acd78c2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:23:32"
---

# Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.

## One-line Summary

通过对桑福德地下研究设施（SURF）4850英尺（1478米）深处 EGS Collab 试验场流体样品进行16S rRNA 基因扩增子测序，发现相距约50米的 OT 和 PST 井产出流体具有高度相似的微生物群落组成，揭示了两井之间存在天然水力连通性，这一发现后被岩心记录和井下摄像所证实。[Zhang 2019, pp. 1-1]

## Research Question

该研究旨在回答六个根本性问题：
1. 深层地下微生物群落在空间上是否呈异质性分布？
2. 微生物群落数据如何为储层表征提供信息？
3. 从同一裂缝或储层单元中产出的流体样品应具有怎样的群落相似性？
4. 在多大程度上可以利用微生物群落数据区分地层水与注入的压裂水或钻井水？
5. 微生物群落组成数据在区分不同流体来源上是否比地球化学数据更具信息量？
6. 环境微生物学家常用的采样规范是否适用于深层地下环境？
[Zhang 2019, pp. 2-4]

## Study Area / Data

研究区位于美国南达科他州利德市（Lead, SD）的桑福德地下研究设施（SURF），原为霍姆斯特克金矿，深度达 4850英尺（1478米）。EGS Collab 项目在此建立了一个中尺度（10–100米）增强型地热系统试验场，钻设了8口新钻孔（I, P, PST, PSB, PDT, PDB, OT, OB），孔深达 161英尺至 56英尺不等。采样点包括自流井、裂隙滴水、矿井工业水等，采样时间为 2017 年 11 月至 2019 年 5 月。此外还整合了先前发表的两组SURF 4850 英尺水平的微生物数据。采样位置平面图及井配置见图 3。[Zhang 2019, pp. 4-6]

## Methods

- 流体样品用 0.2 μm Sterivex Duropore 过滤器现场过滤，部分滤液再用 0.02 μm Anotop 过滤器捕获超小细胞。过滤后滤芯立即干冰冷冻，运送至斯坦福大学存于 -80°C。[Zhang 2019, pp. 6-7]
- DNA 提取后，使用引物 515F‑Y/926R 对 16S rRNA 基因 V4‑V5 高变区进行 PCR 扩增，随后在 Illumina MiSeq PE250 平台上进行高通量测序。[Zhang 2019, pp. 7-8]
- 测序数据经质量过滤，生成 ASV（扩增子序列变体）丰度表并分配分类学（域、门、纲、目、科、属）。构建系统发育树，计算样品间的加权 UniFrac 距离，以量化群落相似性/相异性。加权 UniFrac 距离公式为 \( wUF_{A,B} = \sum_{i=1}^{n} b_i \left| \frac{A_i}{A_T} - \frac{B_i}{B_T} \right| \)。[Zhang 2019, pp. 7-8]
- 为与先前发表的数据（Momper et al., 2017; Osburn et al., 2014）进行对比，利用 515F‑C/806R 引物对本次研究的测序读长进行了体外截取再分析。[Zhang 2019, pp. 8-10]
- 水化学分析：阴离子用离子色谱，阳离子用 ICP‑MS 或 ICP‑OES 测定。[Zhang 2019, pp. 7-8]

## Key Findings

1. **钻井水与地层水的可区分性**：钻井水（地表泉水）与 OT/PST 流出的地层水在微生物群落组成上截然不同。OT/PST 中主导的蛋白菌科（如 Geobacteraceae、Magnetospirillaceae、Rhodocyclaceae 等）在钻井水中几乎不存在（总丰度 <0.5%），且 OT/PST 的群落多样性显著低于钻井水（~120 ASVs vs ~500 ASVs）。这证实了产出的流体确属地层水，而非回流的钻井水。[Zhang 2019, pp. 10-11]

2. **OT 和 PST 井间天然连通性的识别**：
   - OT 和 PST 两井虽相距约 50 米，但其微生物群落组成高度相似，超过 70% 的微生物科重叠，且许多重叠科在其他样品中几乎缺失。加权 UniFrac 距离仅为 0.37，而该样品集的“最小”距离（同源钻井水重复样品）为 0.17，“最大”距离（钻井水与深层流体）为 0.78。
   - 相比之下，其余空间上分散的样品（如 Fracture A vs PST、Borehole GC vs OT 等）加权 UniFrac 距离多在 0.6–0.84 之间，表现出显著的异质性，尽管它们之间的地理距离与 OT 和 PST 相近或更小。[Zhang 2019, pp. 10-12]
   - 序列变体（ASV）维恩图显示，OT 和 PST 共享 15.8% 的精确序列变体，而其它样品对共享率 ≤2.1%。[Zhang 2019, pp. 12-13]
   - 微生物组成相似性指向的 OT‑PST 连通性随后被岩心记录和下水道摄像证实：OT 孔深 49 m、P 孔深 37 m、PST 孔深 17 m 处的开启裂缝在空间上大致处于同一平面（走向 150.9°，倾角 87.5°），且具有水力联系。[Zhang 2019, pp. 15-16]

3. **微生物群落数据较地球化学数据具有更高分辨率**：例如，PST 和 Fracture A 同为高硫酸根水，离子组成非常相似，但微生物群落差异极大。Fracture A 与 Fracture B、Borehole 8 与 Port 17Ledge 等也存在类似现象。表明微生物群落结构能区分同一地质组内即使是地球化学上难以区分的局部水文单元。[Zhang 2019, pp. 17-18]

4. **过滤器孔径对微生物群落覆盖度的影响**：Fracture A 样品中，0.02–0.2 μm 级分的群落与 >0.2 μm 级分截然不同，被 0.2 μm 过滤器遗漏的组群中以古菌 Nanoarchaeota 为主导（78.8%），表明常用 0.2 μm 过滤器会遗漏纳米级微生物，影响对深层寡营养环境微生物群落的全面认识。[Zhang 2019, pp. 13-14]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| OT 和 PST 的微生物群落加权 UniFrac 距离为 0.37；钻井水与深层流体最大距离为 0.78；同源钻井水最小距离为 0.17 | [Zhang 2019, pp. 10-12] | SURF 4850 ft，采样时无工业扰动，数据经 515F‑C/806R 引物体外截取 | 近距离重复样品的最小距离为基线，OT‑PST 距离远小于其他异源样品对（0.6‑0.84） |
| OT 和 PST 共享超过 70% 的微生物科，且优势科 Rhodocyclaceae、Geobacteraceae 等在其余样品中几乎缺失 | [Zhang 2019, pp. 10-11] | 同上 | 家族水平相对丰度，Illumina MiSeq PE250 测序 |
| OT 和 PST 共享 15.8% 的精确 ASVs，其余样品对共享 ≤2.1% | [Zhang 2019, pp. 12-13] | SURF 4850 ft 土著样品 | 维恩图基于存在/缺失，不计丰度 |
| 钻井水与 OT/PST 的蛋白菌科组成：钻井水中主导的 Sphingomonadaceae (16.6%) 等在 OT/PST 中 <1%；OT/PST 中的 Geobacteraceae 等 (总计 49.1%/65.3%) 在钻井水中 <0.5% | [Zhang 2019, pp. 10-11, Table 1] | 钻井水采自地表泉水，OT/PST 为自流流体 | 同时还伴随多样性的显著差异 (~500 ASVs vs ~120 ASVs) |
| 岩心记录和下水道摄像在 OT‑49m、P‑37m、PST‑17m 发现开启流动裂缝，三者空间上拟合同一平面 | [Zhang 2019, pp. 15-16] | 2018 年 2 月摄像，裂缝定位来自 Dobson et al. (2018) 及 Fu et al. (2019) | 独立证据，与微生物群落推断一致 |
| Fracture A 和 PST 虽离子组成极相似，但微生物群落加权 UniFrac 距离为 0.77 | [Zhang 2019, pp. 17-18, Table B1] | 同属 Poorman 组，相距 ~50 m | 水化学数据不足以分辨局部水文区室 |

## Limitations

- 该研究的所有样品均在无进一步工业扰动（如压裂、化学处理）的条件下采集，且流体在天然水力条件下产出。因此，这一技术对已开发储层、经历过工业活动的储层适用性需谨慎评估。[Zhang 2019, pp. 14-15, 16‑17]
- 连通性的概念是相对的：在基质渗透率较高、水力单元连通性好的储层中，井间微生物群落差异可能整体偏小，导致解释困难；而在单一裂缝尺度极大时，裂缝内部可能产生环境梯度，导致群落差异超过不同裂缝之间的差异。这些情况需要未来研究。[Zhang 2019, pp. 16-17]
- 研究仅使用 0.2 μm 过滤器进行主要分析，纳米级微生物（0.02–0.2 μm）可能被遗漏，从而影响对群落真实组成的描绘。[Zhang 2019, pp. 13-14, 17]
- 样品数量有限，部分后续采集的样品（如 GC, Fracture A', B, C）测序深度较浅（~10,000 条质量过滤读数），可能影响比较的统计效力。[Zhang 2019, pp. 12, Table 2 注释]

## Assumptions / Conditions

- 深层地下储层中，同一天然裂缝或产层内的流体伴随微生物群落通过对流与扩散在局部被均匀混合，导致从同一裂缝产出的不同井流体具有相似的群落结构。[Zhang 2019, pp. 1-2]
- 钻井水或其他外来工作水的微生物群落与地层水群落可明确区分，因为两者起源环境迥异。[Zhang 2019, pp. 2-4]
- 采样时的新钻井（2天至3周龄）尚未受到钻井以外工业活动的显著影响，流体群落代表的是与当地环境长期平衡后的原位群落。[Zhang 2019, pp. 4, 16‑17]
- 加权 UniFrac 距离的解释依赖于样品集的自身“最小”与“最大”距离定标；且由于系统发育树的构建依赖于样品集大小，距离绝对值受样品数量影响。[Zhang 2019, pp. 7-8, 10‑11]

## Key Variables / Parameters

- **加权 UniFrac 距离**：量度两样品群落间的系统发生学 β 多样性，考虑分支长度及 ASV 逐分支相对丰度。[Zhang 2019, pp. 7-8]
- **ASV 数量与家族数**：OT/PST 的 ASV 数为 126/116，家族数 58/47；钻井水为 ~500 ASVs，180 家族；Fracture A 为 512 ASVs，188 家族。[Zhang 2019, pp. 12, Table 2]
- **主要差异微生物科**：Rhodocyclaceae (OT 21.5%, PST 36.4%)、Geobacteraceae (OT 13.2%, PST 10.4%)、Magnetospirillaceae (OT 7.4%, PST 2.1%) 等。这些科在钻井水中总丰度 <0.5%。[Zhang 2019, pp. 10-11, Table 1]
- **水化学离子**：PST 和 Fracture A 均为高 SO₄²⁻ (>2000 ppm)，离子组成相似；钻井水低矿化度。PST 的 Fe 含量（0.415 ppm）及 Mn、Ni 含量较高，与该井中检测到金属代谢菌（Geobacter, Magnetospirillum）一致。[Zhang 2019, pp. 17-18, Table B1]
- **滤波器孔径**：0.2 μm 与 0.02 μm 级分，用于评估纳米级微生物遗漏。[Zhang 2019, pp. 13-14]

## Reusable Claims

- 在未扰动的深层断裂储层中，通过对比产出流体的微生物群落组成（加权 UniFrac 距离、共享 ASV 比例、优势类群重叠度）可以识别天然井间连通性。前提是储层基质渗透率极低，水力单元之间隔离良好。[Zhang 2019, pp. 14-15, 17]
- 利用 16S rRNA 基因扩增子测序分析，能够可靠地区分外来工业水（钻井液、压裂液）与地层原生水，因它们的群落多样性、优势类群及生理代谢潜能（如厌氧铁/硫酸盐还原菌的存在）存在显著差异。[Zhang 2019, pp. 13-14]
- 微生物群落组成作为流体来源的“条形码”，其分辨率高于常规水化学分析，可在相同地质组内分辨局部不通连的水文区室。[Zhang 2019, pp. 17-18]
- 0.2 μm 过滤器可能无法捕获深层寡营养环境中的超小微生物（如 Nanoarchaeota），建议在深层地下采样中结合更小孔径的过滤器以获得更全面的群落信息。[Zhang 2019, pp. 13-14, 17]
- 该技术不需要井下传感器部署或长期流试验，只需对早期钻井阶段的自产流体进行采样和测序，即可获得井间连通性信息。[Zhang 2019, pp. 17]

## Candidate Concepts

- [[fracture reservoir]]
- [[indigenous microbial community]]
- [[enhanced geothermal system (EGS)]]
- [[interwell connectivity]]
- [[UniFrac distance]]
- [[weighted UniFrac]]
- [[16S rRNA gene amplicon sequencing]]
- [[subsurface microbiome]]
- [[beta diversity]]
- [[natural fracture]]
- [[reservoir diagnostic tool]]
- [[oligotrophic environment]]
- [[ultramicrobacteria]]
- [[Nanoarchaeota]]
- [[geomicrobiology]]

## Candidate Methods

- [[16S rRNA gene high-throughput sequencing]]
- [[DNA extraction from filters]]
- [[water chemistry analysis]]
- [[core logging]]
- [[sewer camera survey]]
- [[principal coordinate analysis (PCoA)]]
- [[Venn diagram analysis]]
- [[phylogenetic tree construction]]
- [[Illumina MiSeq amplicon sequencing]]
- [[ICP-MS/OES]]
- [[ion chromatography]]

## Connections To Other Work

- 先前研究已表明深层地下微生物具有高度多样性和广泛分布 (Fredrickson & Balkwill, 2007)。[Zhang 2019, pp. 1-2]
- 流动水可能起均质化作用，导致连通单元内微生物群落相似性增加 (Akasaka & Takamura, 2012; Oloo et al., 2016; Staley & Sadowsky, 2016)。[Zhang 2019, pp. 1-2]
- 其他研究也利用 16S rRNA 测序分析储层微生物，但多聚焦于生态学，或缺乏详细的储层表征方法 (Momper et al., 2017; Osburn et al., 2014; Daly et al., 2016; Vigneron et al., 2017)。[Zhang 2019, pp. 2-4, 7‑8]
- 微生物群落组成比水化学更敏感地反映环境变化，Mouser et al. (2010) 在地下水中发现微生物群落对污染更灵敏；Ino et al. (2016) 发现离子组成恒定时微生物群落随时间发生剧变。[Zhang 2019, pp. 17-18]
- 纳米级微生物在深层地下被遗漏的现象与 Luef et al. (2015) 等在其它含水层中的报道一致。[Zhang 2019, pp. 13]
- 该工作与利用 DNA 标记纳米颗粒示踪剂进行裂缝表征的思路 (Zhang et al., 2015; Zhang et al., 2017) 相互补充，但本方法利用天然微生物作为指纹。[Zhang 2019, pp. 1, 22‑23]

## Open Questions

- 实际已开发的油气或地热储层中，高压注入、化学添加剂等工业活动如何影响微生物群落动态？群落是否会在扰动后重新平衡？重新平衡后的群落是否仍能作为连通性指标？[Zhang 2019, pp. 14-15]
- 当裂缝规模极大或存在显著环境梯度（如温度、氧化还原梯度）时，单一裂缝内部的微生物群落差异是否会超过不同裂缝之间的差异？何种尺度下微生物数据的解释会失效？[Zhang 2019, pp. 16-17]
- 如何优化深层地下采样策略，特别是是否需要常规性地结合 0.2 μm 和更小孔径（0.02 μm）过滤器来更全面地捕获纳米级微生物，以提高对流体来源的辨识灵敏度？[Zhang 2019, pp. 17]
- 高通量测序成本虽已大幅下降，但其作为常规储层诊断工具的工业化应用流程（采样、保存、数据标准化解释）尚待建立。

## Source Coverage

所有 22 个非空索引片段均已处理。已编译源块字符总数为 109,989，原始索引字符总数为 109,508，覆盖比（按块数）为 1.0，（按字符数）为 1.004392。未添加片段外信息。源签名：8a13c56b3a216e8913bbf468edbbde616acd78c2。
