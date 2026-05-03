---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-walsh-simulating-electropulse-fracture-of-granitic-rock"
title: "Simulating Electropulse Fracture of Granitic Rock."
status: "draft"
source_pdf: "data/papers/2020 - Simulating electropulse fracture of granitic rock.pdf"
collections:
  - "part3-2"
citation: "Walsh, Stuart D.C., and Daniel Vogler. \"Simulating Electropulse Fracture of Granitic Rock.\" *International Journal of Rock Mechanics and Mining Sciences*, preprint, 18 Nov. 2019, eartharxiv.org. Accessed 2026."
indexed_texts: "9"
indexed_chars: "44037"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "44241"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004632"
coverage_status: "full-index"
source_signature: "b630f509bd446dd5fbbb5078d4f685598f0d33d8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:35:08"
---

# Simulating Electropulse Fracture of Granitic Rock.

## One-line Summary
本文提出了一种新的多物理场数值模拟方法，用于研究花岗岩中的电脉冲致裂，该方法在颗粒尺度上耦合了放电、电阻加热、热击穿以及热力学损伤过程，并考虑了矿物组成与微孔隙的影响。

## Research Question
如何构建一个能够描述电脉冲作用下硬岩（如花岗岩）断裂过程的耦合电‑力学模型，以理解材料组成（矿物与微孔隙分布）及操作参数（电压、脉宽）对岩石损伤行为的影响，从而辅助电脉冲工具的设计与优化。

## Study Area / Data
研究以典型花岗岩（取自Lac du Bonnet岩体[53]）为对象，其矿物组成与颗粒尺寸如下：
- 钾长石：体积含量45%，粒径3.7 mm；
- 斜长石：20%，3.1 mm；
- 石英：30%，1.8 mm；
- 黑云母：5%，0.9 mm [53]。
微孔隙分布参照Montgomery和Brace的实测数据[34]：石英0.9％，斜长石1.8％，钾长石0.9％，黑云母0.9％（Table 2）。模拟设定的电脉冲参数为600 kV、2 μs，样品厚度2 cm、宽度10 cm，这些条件落在已有实验报道的范围[13,14,19,15]。

## Methods
模拟基于多物理场有限元求解器MOOSE[21]。计算分为两个阶段：
1. **放电与电阻加热阶段**：采用准静态假设，依据欧姆定律描述电流（Eq. 1），电阻耗散产热由Eq. 2给出，并通过温度‑电导率反馈（Eq. 3‑5，Table 1，Fig. 2）实现热击穿[22‑24]。液体介质的电导率使用Sinmyo & Keppler模型[27]和Arps定律[28]计算；固体与孔隙流体的混合电导率采用Glover对Archie定律的扩展式[31,32]（Eq. 9），其中Archie指数取m=1.5[33]。流体与固体的分相加热由Eq. 10‑13描述，混合温度初值由Eq. 14给出。
2. **热‑力学响应阶段**：热扩散（Eq. 15）和线热应变（Eq. 16）引起热应力（Eq. 17）。破坏准则采用Diederichs等[42,43]提出的五模式损伤模型，区分Hoek‑Brown破坏、剥落破坏（spalling）和拉伸破坏，具体参数：σc=122 MPa，m=25，σt=10 MPa，剥落强度比σ1/σ3=8[42,44,50‑52]。
岩石微观结构通过Voronoi镶嵌生成，经迭代松弛使各矿物满足设定的体积分数与粒径分布[59‑61]。

## Key Findings
- 在初始阶段，由于斜长石具有较高的体积微孔隙率，孔隙流体的电导率使该矿物区域的整体电导率更高，电流优先沿斜长石分布[Walsh 2019, pp. 14-15]。
- 施加单个600 kV、2 μs的脉冲后，电极附近区域产生了超过200 K的温升，足以形成局部导通路径，并引发岩石断裂[Walsh 2019, pp. 14-15]。
- 破坏主要集中于电极周围，破坏模式包括拉伸破坏（模式1）、受拉和受压条件下的剥落破坏（模式2、3）以及超过实验室长期强度的拉伸破坏（模式4）[Walsh 2019, pp. 14-15]。
- 上下电极下方损伤区域的差异源于接触矿物不同（顶部为斜长石，底部为钾长石），说明矿物组成直接通过电导率影响能量耗散和破坏范围[Walsh 2019, pp. 14-15]。
- 模拟得到的击穿和损伤区与实验条件下观察到的岩石破碎现象相符，验证了该方法的有效性[Walsh 2019, pp. 15-19]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 电脉冲钻进比能耗约为100‑200 J/m³，而回转钻进为600‑950 J/m³ | [2]，引自[Walsh 2019, pp. 3-6] | 硬岩钻进 | 电脉冲以拉伸破坏为主，能量利用更高效 |
| 花岗岩中的微孔隙分布（斜长石1.8%，石英0.9%，钾长石0.9%，黑云母0.9%） | [34]，引自[Walsh 2019, pp. 6-8] | 基于实测的Lac du Bonnet花岗岩 | 用于设定各矿物的初始孔隙度，影响初始电导率 |
| 采用Glover混合模型且取Archie指数m=1.5时能有效模拟花岗岩双导电特性 | [31‑33]，引自[Walsh 2019, pp. 6-8] | 花岗岩，假定两条平行导电通路 | 该混合律将流体与固体作为独立导电通道处理 |
| 单次600 kV、2 μs脉冲在电极附近引起拉伸和剥落破坏，且损伤集中于电极周围 | [Walsh 2019, pp. 14-15] | 2 cm厚花岗岩试样，两端夹持，单脉冲 | 破坏模式与实验破碎现象一致 |
| 损伤模型参数σc=122 MPa, m=25, σt=10 MPa, 剥落极限σ1/σ3=8可预测硬岩近表面破坏 | [42,44,50‑52]，引自[Walsh 2019, pp. 11-14] | 硬岩隧道与实验室条件 | 参数源于Diederichs等的研究 |
| 各矿物的导电率‑温度模型参数见Table 1 | [25,26]，引自[Walsh 2019, pp. 6-8] | 石英、斜长石、钾长石、黑云母 | 公式形式为Λ=A exp(‑B/kbθ) 或 Λθ=A exp(‑B/kbθ) |

## Limitations
- 模型仅模拟损伤起始，未涉及裂纹扩展与交互作用，无法直接预测碎块脱离和钻进效率[Walsh 2019, pp. 14-15]。
- 为简化计算，假设脉冲作用期间电压降恒定，未考虑实际电脉冲装置的放电动态响应[Walsh 2019, pp. 11-14脚注]。
- 热击穿过程采用经验模型，未区分原子尺度的纯电击穿或其他机制，因此不能精确再现击穿的微观物理本质[Walsh 2019, pp. 8-11]。
- 微孔隙在矿物颗粒内的分布被假定为均匀，未考虑颗粒内部的非均质性。
- 损伤准则只适用于损伤开端，模拟未考虑多次脉冲或长时间作用下的损伤累积。

## Assumptions / Conditions
- 所有电阻耗散能量均转化为热能，忽略声、光等其他形式的能量损失[Walsh 2019, pp. 6-8]。
- 电脉冲过程按准静电场处理。
- 岩石被视为由固体和孔隙流体组成的双组分混合物，采用平行导电通路假设（Glover混合律）。
- 孔隙流体的初始含盐度等效为3 wt% NaCl[36]。
- 固体矿物的电导率随温度按指数或类似经验关系变化，参数取自文献（Table 1, Fig. 2）。
- 热击穿是建立放电通路的主导过程，这一假设与航空复合材料雷击建模中的做法一致[40,41]。
- 岩石由四种矿物构成，其组成与粒径固定为Lac du Bonnet花岗岩的典型值，不考虑实际岩体的空间变异。

## Key Variables / Parameters
- **电学变量**：电势φ、电场强度Ei、电流密度Ji、电导率Λ、电阻耗散生热qD。
- **热学变量**：温度θ（或T）、热容量cp、密度ρ、热导率κ、热膨胀系数α。
- **力学变量**：应力、应变、损伤状态。
- **关键参数**：脉冲电压600 kV，持续时间2 μs；样品厚度2 cm、宽度10 cm；矿物电导率模型参数（A, B, Table 1）；Archie指数m=1.5；流体与固体的热物性；强度参数σc=122 MPa，m=25，σt=10 MPa，剥落极限σ1/σ3=8；各矿物的微孔隙体积分数（Table 2）。

## Reusable Claims
- 在花岗岩电脉冲处理中，初始电流通道沿微孔隙含量较高的矿物（如斜长石）形成，原因是孔隙流体的导电性主导了整体的初始电导率[Walsh 2019, pp. 14-15]。
- 单次600 kV、2 μs脉冲足以在电极附近产生局部温升并引发拉伸和剥落破坏，从而启动岩石碎裂[Walsh 2019, pp. 14-15]。
- 采用基于Diederichs模型的剥落准则（σ1/σ3=8）可有效预测硬岩自由面附近的损伤萌生[Walsh 2019, pp. 11-14]。
- Glover扩展的Archie混合律能够捕捉电脉冲模拟中孔隙流体与固体两相共同承载电流的行为[Walsh 2019, pp. 6-8]。
- “放电‑电阻加热”与后续“热‑力学”两阶段计算策略能够复现实验中的击穿和损伤条件，为电脉冲破岩工具的设计提供数值支撑[Walsh 2019, pp. 15-19]。

## Candidate Concepts
- [[electropulse fracture]]
- [[thermal breakdown in rock]]
- [[dielectric breakdown of solids]]
- [[microporosity in plagioclase]]
- [[spalling failure]]
- [[Hoek-Brown failure criterion]]
- [[dual-conductivity material]]
- [[resistive heating]]
- [[Voronoi tessellation for rock microstructure]]
- [[Archie’s law]]
- [[Glover’s mixture model]]
- [[pulse voltage ramp rise time]]

## Candidate Methods
- [[two-stage multiphysics simulation (electrical discharge → thermomechanical)]]
- [[finite element solver MOOSE]]
- [[quasi-static electric field model]]
- [[Glover’s extension to Archie’s law]]
- [[empirical conductivity-temperature models for minerals]]
- [[Diederichs damage model]]
- [[Voronoi cell relaxation for material composition]]

## Connections To Other Work
- 引用电脉冲破碎岩石的实验与机理研究，如Andres[2,4,5,19]、Inoue等[13,14]、Voigt等[16]。
- 将雷击复合材料建模中的热击穿思路[40,41]移植到岩石放电过程。
- 与热剥落钻进（thermal spallation drilling）模型共享类似的岩石破坏模式与损伤准则[47,48,49,54‑58]。
- 岩石微观结构生成方法延续了颗粒尺度力学建模中的Voronoi松弛技术[59‑61]。

## Open Questions
- 在初始破坏萌生后，裂纹如何扩展并最终导致岩屑剥离和钻进进尺？
- 多次脉冲及不同脉冲参数（如电压波形、重复频率）对岩石损伤累积的影响如何？
- 在高围压和原位应力条件下（如深井），电脉冲的击穿和破岩效果会发生哪些变化？
- 孔隙流体的盐度、饱和度以及表面导电效应对电导率和断裂模式的定量作用有待更系统的参数分析。
- 是否存在纯电气性质（而非热）的击穿机制，其对模型中热击穿假设的影响程度如何？

## Source Coverage
本页面严格基于全部9个非空索引片段编制。片段总字符数44 241，编译后总字符数44 241，源段覆盖率（按块）为1.0，字符覆盖率约为1.005（微小差异源于文本拼接）。所有片段均已被处理并纳入，未引入来自片段之外的作者、页码、数据或结论。
