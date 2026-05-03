---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-he-effect-of-cooling-rate-on-the-mechanical-properties-of-amorphous-alloy-from-the-perspect"
title: "Effect of Cooling Rate on the Mechanical Properties of Amorphous Alloy: From the Perspective of Heterogeneity."
status: "draft"
source_pdf: "data/papers/2025 - Effect of cooling rate on the mechanical properties of amorphous alloy From the perspective of heterogeneity.pdf"
collections:
  - "zotero new"
citation: "He, Yezeng, et al. \"Effect of Cooling Rate on the Mechanical Properties of Amorphous Alloy: From the Perspective of Heterogeneity.\" *Materials Letters*, vol. 387, 2025, 138239. doi:10.1016/j.matlet.2025.138239."
indexed_texts: "4"
indexed_chars: "16287"
nonempty_source_blocks: "4"
compiled_source_blocks: "4"
compiled_source_chars: "15520"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.952907"
coverage_status: "full-index"
source_signature: "f8cd2c588c4ffb28bcfd67c127bf4de14fbf3819"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:02:55"
---

# Effect of Cooling Rate on the Mechanical Properties of Amorphous Alloy: From the Perspective of Heterogeneity.

## One-line Summary
通过分子动力学模拟，该研究发现提高冷却速率会减少Cu<sub>50</sub>Zr<sub>50</sub>金属玻璃中五次对称结构（如二十面体），增加“类液体区”，从而降低剪切带形成所需的应变，同时增强结构和力学异质性。

## Research Question
冷却速率如何影响Cu<sub>50</sub>Zr<sub>50</sub>非晶合金的结构和力学异质性，以及剪切带的形成机制？

## Study Area / Data
研究体系为Cu<sub>50</sub>Zr<sub>50</sub>非晶合金。模拟包含20,480个原子，初始随机置于立方盒子中。冷却速率范围为1×10<sup>11</sup>至5×10<sup>13</sup> K/s。结构分析基于Voronoi镶嵌，力学性能通过纳米压痕模拟评估。

## Methods
- **分子动力学模拟**：使用LAMMPS软件包，原子间相互作用采用半经验多体势（EAM/FS）。系统在2000 K弛豫2 ns后，以不同冷却速率淬火至1 K。模拟在NPT系综下进行，使用Nosé-Hoover恒温器和恒压器控制温度和压力，压力在淬火和弛豫阶段保持为零，采用周期性边界条件。
- **结构表征**：采用Voronoi镶嵌法分析原子堆垛和配位数。
- **纳米压痕模拟**：沿Z轴方向使用球形虚拟压头，加载速率0.2 Å/ps，温度维持1 K以消除热效应。排斥力由F(r) = –K(R – r)<sup>2</sup>计算（K=20 eV/Å<sup>3</sup>）。局域相对弹性模量由Hertz公式拟合获得。
- **异质性分析**：计算Voronoi多面体含量及相对弹性模量的分布，并定义异质性参数δ<sub>polyhedron</sub>和δ<sub>E\*</sub>。采用Spearman秩相关系数量化<0,0,12,0>等结构与缩减弹性模量的相关性，阈值设为0.8。

## Key Findings
1. 提高冷却速率导致剪切带形成所需的应变降低：在测试的冷却速率下，剪切带形成应变分别为3.33%、3.90%和5.41%（对应冷却速率依次升高）。
2. 剪切带的萌生区域通常具有较低的相对弹性模量，这些区域对应“类液体区”，原子堆砌疏松，易发生应力集中和局域变形。
3. Spearman秩相关分析表明，<0,0,12,0>二十面体结构与缩减弹性模量在所有冷却速率下均呈强正相关（系数>0.8），表明该稳定结构有助于抵抗变形。其他短程序团簇如<0,3,6,3>在10<sup>13</sup> K/s时也表现出显著相关性。
4. 随冷却速率增加，<0,0,12,0>中心原子的空间分布差异增大，且该类多面体含量下降，导致整体结构异质性增强。
5. 冷却速率升高同时提高了多面体结构异质性（δ<sub>polyhedron</sub>）和弹性模量异质性（δ<sub>E\*</sub>），这种异质性的增加与塑性的改善相关联。

## Core Evidence Table
| 证据 | 来源 | 条件 | 注释 |
|------|------|------|------|
| 剪切带形成应变随冷却速率升高而降低（3.33%， 3.90%， 5.41%） | [He 2025, pp. 1-2], Fig. 1(a-c) | Cu<sub>50</sub>Zr<sub>50</sub>，MD模拟，压痕速率0.2 Å/ps | 应变值对应该文所述“progressively higher cooling rates”；原文明确指出高冷却速率降低应变 |
| 剪切带萌生区具有较低的相对弹性模量（“类液体区”） | [He 2025, pp. 1-2], Fig. 1(d-f) | 同上，Hertz公式拟合 | 低模量区原子松散堆积，易于应力集中 |
| <0,0,12,0>二十面体与缩减弹性模量呈强正相关（Spearman系数） | [He 2025, pp. 2-3], Fig. 2 | 五种冷却速率（10¹¹ K/s至5×10¹³ K/s） | 相关系数均高于0.8的阈值（绿色虚线） |
| <0,0,12,0>中心原子分布随冷却速率升高而更加不均匀 | [He 2025, pp. 3-4], Fig. 3 | 比较10¹¹, 10¹², 10¹³ K/s三个条件 | 直观显示结构异质性增大 |
| 冷却速率升高引起多面体异质性（δ<sub>polyhedron</sub>）和弹性模量异质性（δ<sub>E\*</sub>）同时增加 | [He 2025, pp. 3-4], Fig. 4(b) | 冷却速率范围1×10¹¹−5×10¹³ K/s | 文中将异质性增强与塑性改善关联（引自Refs [18]等） |

## Limitations
- 文中指出缺乏精确表征方法，阻碍建立经典的结构–性能关系（Introduction）。
- 模拟仅针对Cu<sub>50</sub>Zr<sub>50</sub>一种成分，其他体系的通用性未经检验。
- 使用EAM/FS经验势，其精度可能影响微观结构预测的细节。
- 模拟盒子尺寸有限（20,480原子），周期边界条件可能引入尺寸效应。
- 仅通过纳米压痕模拟获得力学响应，未进行宏观拉伸或压缩等模拟。
- 未直接与实验数据进行比较验证。

## Assumptions / Conditions
- 原子间相互作用由EAM/FS势准确描述。
- 淬火和弛豫过程中压力保持为零（NPT系综）。
- 纳米压痕在1 K极低温度下进行，忽略热激活效应。
- 虚拟压头为球形，排斥力简化为F(r) = –K(R – r)<sup>2</sup>，K=20 eV/Å<sup>3</sup>。
- 相对弹性模量通过Hertz公式拟合得到，假定拟合中的微小变化来源于原子尺度效应。
- 周期性边界条件适用于所有方向。

## Key Variables / Parameters
- 冷却速率：1×10¹¹， 5×10¹¹， 10¹²， 5×10¹²， 10¹³ K/s
- 剪切带形成应变：3.33% – 5.41%
- 缩减弹性模量（E\*）及其分布
- Voronoi多面体类型与含量，尤其是<0,0,12,0>二十面体
- Spearman秩相关系数
- 结构异质性参数（δ<sub>polyhedron</sub>）和力学异质性参数（δ<sub>E\*</sub>）
- 压头加载速率：0.2 Å/ps
- 系统原子数：20,480

## Reusable Claims
- 在Cu<sub>50</sub>Zr<sub>50</sub>非晶合金的分子动力学模拟中，将冷却速率从1×10¹¹ K/s提高到5×10¹³ K/s，可使剪切带形成应变从约5.41%降低至约3.33%。[条件：NPT系综，EAM/FS势，压痕加载速率0.2 Å/ps，温度1 K。限制：仅针对该成分，且为模拟结果，未与实验对比。]
- <0,0,12,0>二十面体结构的含量与缩减弹性模量在所有考察的冷却速率下均呈强正Spearman相关（r > 0.8）。[条件：基于Voronoi镶嵌分析。限制：相关性仅针对Cu–Zr金属玻璃的模拟体系。]
- 升高冷却速率导致<0,0,12,0>多面体含量下降，同时使多面体结构异质性和弹性模量异质性增加，这被认为有助于提高塑性。[条件：冷却速率范围1×10¹¹−5×10¹³ K/s。限制：异质性与塑性的直接因果验证缺失。]
- 剪切带萌生倾向于发生在相对弹性模量较低的“类液体”区域，这些区域原子堆积松散。[条件：MD纳米压痕模拟，局域模量由Hertz公式拟合。限制：纳米尺度机制外推到块体材料需谨慎。]
- 冷却速率可通过调制五次对称结构的含量和“类液体区”的比例来调控非晶合金的力学性能。[条件：Cu<sub>50</sub>Zr<sub>50</sub>，快速凝固模拟。限制：其他合金体系需进一步验证。]

## Candidate Concepts
- [[冷却速率]]
- [[结构异质性]]
- [[力学异质性]]
- [[剪切带]]
- [[非晶合金]]
- [[金属玻璃]]
- [[类液体区]]
- [[二十面体结构]]
- [[Voronoi镶嵌]]
- [[Spearman秩相关]]
- [[缩减弹性模量]]
- [[分子动力学模拟]]
- [[纳米压痕]]

## Candidate Methods
- [[分子动力学模拟 (MD)]]
- [[LAMMPS]]
- [[EAM/FS势]]
- [[NPT系综]]
- [[Nosé-Hoover恒温器与恒压器]]
- [[Voronoi多面体分析]]
- [[纳米压痕模拟]]
- [[Hertz公式]]
- [[Spearman秩相关系数]]

## Connections To Other Work
- 研究结果与先前冷却速率影响结构有序度的发现一致（Refs [1–4]），并进一步揭示了与力学异质性的内在联系（Ref [6]）。
- 通过调节异质性改善塑性的思路与回春块体金属玻璃中抑制剪切带的研究（Ref [10]）相呼应。
- 文中指出其他短程序（如<0,3,6,3>）在10¹³ K/s下亦显著相关，与多组元金属玻璃的原位应力分析（Ref [16]）形成补充。
- 过冷液体中的结构差异对异质性的贡献（Ref [17]）在本研究中通过Voronoi分析得以具体化。

## Open Questions
- 高冷却速率导致的结构与力学异质性增强如何定量转化为宏观塑性提高？模拟中缺乏直接的塑性应变数据验证。
- 能否发展精确的实验表征手段（如原位纳米力学测试）来验证模拟预测的局域弹性模量和剪切带萌生位置的关系？
- 冷却速率对其他非晶合金体系（如Fe基、Zr基多组元）的结构和性能是否具有相似的调控规律？
- 如何建立从冷却速率-微观结构统计特征-宏观力学性能的预测模型，以指导实际制备工艺优化？

## Source Coverage
所有非空索引片段均已编译。覆盖情况：索引文本块数 4，索引字符数 16287，非空源块数 4，编译源块数 4，编译字符数 15520，块覆盖率 1.0，字符覆盖率 0.9529，源签名 f8cd2c588c4ffb28bcfd67c127bf4de14fbf3819。
