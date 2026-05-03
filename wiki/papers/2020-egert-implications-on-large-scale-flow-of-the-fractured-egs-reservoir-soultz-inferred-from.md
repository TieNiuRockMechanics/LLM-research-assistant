---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-egert-implications-on-large-scale-flow-of-the-fractured-egs-reservoir-soultz-inferred-from"
title: "Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments."
status: "draft"
source_pdf: "data/papers/2020 - Implications on large-scale flow of the fractured EGS reservoir Soultz inferred from hydraulic data and tracer experiments.pdf"
collections:
  - "part4-1"
citation: "Egert, Robert, et al. \"Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments.\""
indexed_texts: "15"
indexed_chars: "74042"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "73389"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991181"
coverage_status: "full-index"
source_signature: "46a65eabf5c145caaaeffcf7b284cc71328d12f1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:55:30"
---

# Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments.

## One-line Summary
基于十三断裂带离散裂隙网络、瞬态全耦合水‑溶质（HS）迁移模拟，成功同时再现了2005年示踪实验中GPK2与GPK4两井的穿透曲线，量化了井间流道、扫掠孔隙体积及最小换热面积，并识别出分隔南北储层的WNW‑ESE向“分离断层”的关键水力角色[Egert unknown-year, pp. 1-3][Egert unknown-year, pp. 20-22]。

## Research Question
如何利用水力学数据与示踪实验，在保留Soultz EGS储层复杂断层‑裂隙网络真实几何的瞬态三维离散裂隙‑基质（DFM）模型中，同时定量评定GPK3–GPK2与GPK3–GPK4之间的井间连接及大规模流动路径，并揭示影响储层流动分区与示踪剂回收的关键地质构造[Egert unknown-year, pp. 4-6][Egert unknown-year, pp. 20-22]？

## Study Area / Data
*   **研究区**：Soultz‑sous‑Forêts增强型地热系统，位于法国上莱茵地堑（URG）中部，属于“欧洲新生代裂谷系”。Soultz储层为一地垒构造，夹于Hermerswiller和Kutzenhausen断层之间，新生界‑中生界盖层厚约1400 m，下伏低渗透天然裂隙结晶基底，储层深度可达5000 m，温度高达200 °C[Egert unknown-year, pp. 4-6]。
*   **主要数据来源**：
    *   2005年7‑12月历时145天的井间示踪实验：荧光素（fluorescein）于GPK3注入（浓度146 mg·l⁻¹持续24 h），自GPK2（平均产率11.9 l·s⁻¹）与GPK4（3.1 l·s⁻¹）采出，注入流体再回注入GPK3。流量预循环8天以建立稳定流场[Egert unknown-year, pp. 12-14]。
    *   2009年GPK4单井循环试验与2011年GPK1‑GPK3三井循环试验：用于率定裂隙导水系数与基质渗透率，期间记录了井口压力变化[Egert unknown-year, pp. 10-12]。
    *   地质与地球物理模型：基于Sausse et al. (2010)和Place et al. (2011)的结构模型，包括井轨迹、裸眼段、套管泄漏点、裂隙产状与识别[Egert unknown-year, pp. 6-8]。
*   **储层特征**：主要裂隙走向160 ±15°（平行现今最大水平主应力170 ±10°），其他组为Rhenish（20 ±10°）和Hercynian（130 ±10°）走向，陡倾西（>60°）；平均隙宽0.1 mm到250 mm。平行主应力方向的裂隙保持张开且渗透率较高，正交方向的裂隙趋于封闭。结晶基岩基质渗透率极低（10⁻²⁰ m²到10⁻¹⁹ m²）。GPK2存在3880 m深度套管泄漏，连接GPK3‑FZ4770断裂带[Egert unknown-year, pp. 4-6]。

## Methods
1.  **三维离散裂隙‑基质（DFM）模型**：域范围13 km（E‑W）×11 km（N‑S）×5 km（垂向，1000 m–6000 m深度），包含13条主要导水断层和裂隙（含新增“Separation”断裂和GPK1‑FZ2856），以及GPK1‑GPK4裸眼段和泄漏点。使用有限元（FE），裂隙为二维面元，井筒为一维线元，与三维基质共享节点[Egert unknown-year, pp. 6-10]。
2.  **模拟器**：TIGER (THC sImulator for GEoscience Research)，基于MOOSE框架开发的全耦合热‑水‑溶质（HS）迁移代码[Egert unknown-year, pp. 6-8]。
3.  **控制方程**：基于达西定律的孔隙压力方程（考虑裂隙隙宽与井截面尺度因子）；溶质运移采用对流‑弥散方程。采用二阶半隐式Crank‑Nicolson时间积分和Streamline Upwind方法以提高精度并抑制数值弥散[Egert unknown-year, pp. 6-8]。
4.  **水力参数率定**：利用2009年GPK4单井循环与2011年GPK1‑GPK2‑GPK3循环试验的压力响应数据，率定各裂隙的导水系数和基质的正交各向异性渗透率（N‑S方向取较高值以反映区域应力场和小尺度裂隙）[Egert unknown-year, pp. 10-12]。
5.  **示踪实验模拟与拟合**：在率定的水力模型基础上，以定时变化的浓度狄利克雷边界条件注入示踪剂，拟合GPK2和GPK4的穿透曲线，调整裂隙渗透率以匹配运移时间和流体速度，并通过调整纵/横向弥散度及隙宽变化实现峰顶周围的混合[Egert unknown-year, pp. 12-14]。
6.  **辅助因素分析**：考虑示踪剂回注（同一产出的富示踪剂盐水回注至GPK3）和天然背景通量对长期浓度的影响，并进行了敏感性分析[Egert unknown-year, pp. 14-17]。

## Key Findings
1.  **GPK3‑GPK2存在三条独立水力通道**：
    *   第一通道：沿裂隙GPK3‑FZ4770直接连接GPK3裸眼段与GPK2套管泄漏，是主要捷径，峰值到达13天（峰速2.6 m·h⁻¹），示踪剂回收率14.5%，扫掠孔隙体积4000 m³，最小换热面积约2.1×10⁶ m²（基于流线分析，为平行板假设计算面积的2倍）[Egert unknown-year, pp. 12-14][Egert unknown-year, pp. 17-20]。
    *   第二通道：沿GPK3‑FZ4770和MS‑GPK2‑2000a，峰值出现于90天（峰速0.5 m·h⁻¹），回收率10.1%，扫掠体积10300 m³[Egert unknown-year, pp. 12-14][Egert unknown-year, pp. 17-19]。
    *   第三通道：沿GPK3‑FZ5020和MS‑GPK2‑2000a，示踪剂被储层流体强烈稀释，未检测到峰值[Egert unknown-year, pp. 12-14]。
2.  **GPK3‑GPK4连接极弱**：
    *   初次到达23天，但整个实验期内无明确峰，最大浓度仅31 µg·l⁻¹（约为GPK2峰浓度的1/23）。长时预测显示1.5年后出现峰浓度48 µg·l⁻¹。低流速（0.06 m·h⁻¹）、极低示踪剂回收率（0.4%）和扫掠体积（133 m³，比GPK2主通道小两数量级），表明二者之间水力连通差。主要归因于WNW‑ESE向的“分离（Separation）”断层构成优先流动路径，将储层分为北（GPK1‑3）和南（GPK4）两部分，并连接北储层至区域断层系统[Egert unknown-year, pp. 12-14][Egert unknown-year, pp. 17-20]。
3.  **水流场与示踪剂路径特征**：
    *   主要缝网GPK3‑FZ4770上的流场呈不对称分布：GPK2采出的流体大部分来自两孔之间较小区域，而大量注入溶质滞留于储层深处未进入GPK2影响区[Egert unknown-year, pp. 17-20]。
    *   根据Shook (2003)的概念，GPK3‑FZ4770可视为内部不均一的集群通道组合，实验产出的一半流体仅流经27%的孔隙体积，暗示实际换热面积大于平行板计算值[Egert unknown-year, pp. 19-20]。
4.  **过程影响因素的量化**：
    *   示踪剂回注：若忽略，GPK2末时刻浓度降低约20%，GPK4降低约6%[Egert unknown-year, pp. 14-17]。
    *   天然背景对流：影响甚微，忽略后GPK2浓度仅增加约2%，而GPK4因背景流向与水力梯度反向，浓度下降约5%[Egert unknown-year, pp. 14-17]。
5.  **总回收率与储层分区**：全模型实验期间总示踪剂回收率25.0%（GPK2贡献24.6%，GPK4贡献0.4%），与实验外推值（23.5‑25.3%）吻合良好。分离断层兼具高导水性与屏障效应，其对区域流场的控制与微震反演和VSP探测的异常带吻合[Egert unknown-year, pp. 17-20]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 13断裂带DFM模型包含“Separation”断层和GPK1‑FZ2856，域尺寸13×11×5 km | [Egert unknown-year, pp. 6-10] | 结构模型基于Sausse et al. (2010)和Place et al. (2011) | 新增两条断裂以改善GPK3‑GPK4和GPK1附近的参数调整 |
| 2011年GPK1‑GPK3循环试验压力匹配 | [Egert unknown-year, pp. 10-12] | 利用平均稳态段拟合；GPK2套管泄漏影响后期压力 | 拟合忽略井内系统泄漏，但指出了其影响 |
| 2009年GPK4单井循环试验压力匹配 | [Egert unknown-year, pp. 10-12] | 拟合天30‑110的稳态段 | 实验后期扰动忽略 |
| 裂隙及基质率定结果：GPK3‑FZ4770导水系数4.80×10⁻⁵ m²·s⁻¹，基质渗透率x=1.34×10⁻¹⁶ m²等 | [Egert unknown-year, pp. 10-12] | 基于循环试验反演 | 井旁断裂率定精度高，远断断裂仅为粗略估计 |
| GPK2示踪剂穿透曲线拟合 | [Egert unknown-year, pp. 12-14] | 主峰13天，尾长明显，存在多峰叠加；模型可区分三条路径贡献 | 强尾可能与不同裂隙组连接有关 |
| GPK4示踪剂穿透曲线及5年预测 | [Egert unknown-year, pp. 12-14] | 实验期内无明显峰，最高浓度31 µg·l⁻¹；预测1.5年后峰浓度48 µg·l⁻¹ | 浓度极低，不确定性高 |
| 各通道回收率和扫掠体积 | [Egert unknown-year, pp. 17-19] | 基于模拟浓度和产率计算；假设稳态流场、保守示踪剂 | 第二通道回收偏高与晚期高估有关 |
| 最小换热面积估算：流线分析2.1×10⁶ m²，基于扫掠体积的平行板计算1.1×10⁶ m² | [Egert unknown-year, pp. 19-20] | 条件：GPK3‑FZ4770主通道，仅考虑实验时段 | 实际面积因内部复杂结构可能更大 |
| 回注敏感性：忽略回注使GPK2浓度降低约20%，GPK4降低约6% | [Egert unknown-year, pp. 14-17] | 基于模型比较 | 强调长期评估中需考虑回注 |
| 背景对流敏感性：忽略使GPK2浓度增约2%，GPK4降约5% | [Egert unknown-year, pp. 14-17] | 背景通量按约11 cm·yr⁻¹转化为裂隙流量 | 被迫对流速度远超背景速度 |

## Limitations
*   模型未考虑裂隙内部粗糙度、断层泥和内部混合等细观结构，这些效应被概括在水动力弥散中。不过当运移尺度远大于裂隙内通道间距时，采用统计均匀系统是合适的[Egert unknown-year, pp. 6-10]。
*   示踪剂扩散进入基质及荧光素的热降解效应被忽略，理由是该系统强对流主导，运移时间远短于基质扩散时间尺度，且无基质扩散证据，但在极长时间下可能导致偏差[Egert unknown-year, pp. 8-10][Egert unknown-year, pp. 17-19]。
*   距井较远的断层和裂隙的导水系数仅能粗略估计，率定主要约束在井附近区域[Egert unknown-year, pp. 10-12]。
*   2011年循环试验后期GPK2的套管泄漏未纳入模拟，导致部分压力拟合偏差[Egert unknown-year, pp. 10-12]。
*   GPK4浓度预测存在高度不确定性，因为实测数据分散且未捕获峰顶[Egert unknown-year, pp. 12-14]。
*   第二水通道的轻微高估可能因未包含与之相连的未知裂隙或裂隙交汇处的复杂混合所致，但此类裂隙未被钻遇且几何形态未知[Egert unknown-year, pp. 17-19]。

## Assumptions / Conditions
*   基质和裂隙适用代表性单元体积（REV）假设，耦合过程可交互[Egert unknown-year, pp. 6-8]。
*   全储层初始及边界孔隙压力设为静水压力[Egert unknown-year, pp. 8-10]。
*   基质渗透率正交各向异性，N‑S方向渗透率较高以反映区域应力和小尺度裂隙[Egert unknown-year, pp. 8-10]。
*   裂隙和基质中采用达西流；示踪剂为保守的（无反应、无吸附），忽略放射性及热降解[Egert unknown-year, pp. 8-10]。
*   各裂隙裂隙隙宽均匀，出平面混合效应由纵/横向弥散度代替[Egert unknown-year, pp. 6-10]。
*   天然背景流设定为沿主要断层与裂隙的S‑N向地堑平行通量1 m³·h⁻¹，按各裂隙隙宽分配[Egert unknown-year, pp. 8-10]。
*   溶质注入模拟为时间依赖的狄利克雷边界条件，基于GPK3井口实测浓度[Egert unknown-year, pp. 8-10]。
*   示踪剂实验期间流速稳定，流体性质（ρ=1065 kg·m⁻³, μ=2.3×10⁻⁴ Pa·s等）基于150 °C、35 MPa、1.5 mol·kg⁻¹盐度的储层条件[Egert unknown-year, pp. 8-10]。

## Key Variables / Parameters
*   **裂隙导水系数**：GPK3‑FZ4770总导水系数4.80×10⁻⁵ m²·s⁻¹；分段：GPK3‑FZ4770‑GPK2段5.65×10⁻⁵，GPK3‑FZ4770‑GPK3段2.95×10⁻⁵；GPK1‑FZ2856导水系数5.00×10⁻⁵；分离断层（Separation）6.80×10⁻⁵等[Egert unknown-year, pp. 10-12]。
*   **基质渗透率**：x=1.34×10⁻¹⁶ m²（N‑S），y=3.30×10⁻¹⁶ m²，z=1.65×10⁻¹⁶ m²[Egert unknown-year, pp. 10-12]。
*   **孔隙率**：裂隙1.0，基质0.01[Egert unknown-year, pp. 8-10]。
*   **溶质扩散系数**：4×10⁻¹⁰ m²·s⁻¹[Egert unknown-year, pp. 8-10]。
*   **流体性质**：密度1065 kg·m⁻³，动力黏度2.3×10⁻⁴ Pa·s，流体压缩系数2×10⁻⁹ Pa⁻¹，基质压缩系数5×10⁻¹³ Pa⁻¹[Egert unknown-year, pp. 8-10]。
*   **示踪剂注入**：浓度146 mg·l⁻¹持续24 h，注入流量15 l·s⁻¹（GPK3）[Egert unknown-year, pp. 12-14]。
*   **产率**：GPK2平均11.9 l·s⁻¹，GPK4平均3.1 l·s⁻¹[Egert unknown-year, pp. 12-14]。
*   **流道特征速度**：主通道2.6 m·h⁻¹，第二通道0.5 m·h⁻¹，GPK4通道0.06 m·h⁻¹[Egert unknown-year, pp. 12-14]。
*   **示踪剂回收率与扫掠体积**：见核心证据表[Egert unknown-year, pp. 17-19]。

## Reusable Claims
*   在利用井间示踪剂资料对Soultz EGS进行评价时，单条断裂或多条平行板假设不足以描述井间复杂流动；必须采用包含多个离散断裂的三维DFM模型，才能同时匹配多口生产井的穿透曲线[Egert unknown-year, pp. 3-4][Egert unknown-year, pp. 20-22]。
*   GPK3‑GPK2之间由GPK3‑FZ4770主断裂提供的直接通道是主要的示踪剂回收来源（回收率约14.5%），但第二条路径（经由MS‑GPK2‑2000a）贡献了可观的回收量（约10.1%），并显著影响长期尾迹[Egert unknown-year, pp. 12-14][Egert unknown-year, pp. 17-19]。
*   WNW‑ESE向的“分离（Separation）”断裂充当将GPK4与其余井隔开的水力屏障兼优先通道，这解释了GPK3‑GPK4之间极其微弱的示踪响应。这一认识得到微震活动和VSP异常区的独立支持[Egert unknown-year, pp. 17-20]。
*   在强断裂对流系统中，示踪剂回注对长期浓度尾部有显著影响（GPK2末端降低约20%），而天然背景对流的影响可忽略不计（<5%）[Egert unknown-year, pp. 14-17]。
*   基于平行板假设解析计算得到的最小换热面积可能被严重低估，本研究基于流线分析得到的面积是解析值的两倍，且实际因裂隙内部群集通道结构面积可能更大[Egert unknown-year, pp. 17-20]。
*   储层北部（GPK1‑GPK2区域）存在快速流道，可能增加热突破风险，但目前运营方案（GPK2生产，GPK3，GPK4回注）可降低短路风险；分离断层连接区域断层系统的发现也为未来扩建提供了潜在目标[Egert unknown-year, pp. 19-22]。

## Candidate Concepts
*   [[离散裂隙‑基质（DFM）模型]]
*   [[分离断层（Separation Fault）]]
*   [[水力屏障与优先通道]]
*   [[井间示踪剂多重路径]]
*   [[扫掠孔隙体积（swept pore volume）]]
*   [[最小换热面积估算]]
*   [[增强型地热系统（EGS）]]
*   [[Soultz‑sous‑Forêts地热储层]]
*   [[示踪剂回注效应]]
*   [[天然背景对流]]
*   [[裂隙导水系数率定]]
*   [[二维离散裂隙作为特征单元]]
*   [[保守示踪剂假设]]
*   [[热突破风险评估]]
*   [[重力驱动区域流]]

## Candidate Methods
*   [[TIGER有限元模拟器（THC）]]
*   [[二阶半隐式Crank‑Nicolson时间积分]]
*   [[Streamline Upwind稳定化方法]]
*   [[多示踪剂途径通道分解]]
*   [[REV达西流耦合溶质运移]]
*   [[裂隙‑井筒多维度离散化（2D‑1D‑3D）]]
*   [[基于井口压力响应的裂隙导水系数反演]]
*   [[利用稳态循环试验约束水力参数]]
*   [[穿透曲线多参量拟合（峰速、弥散度、隙宽）]]
*   [[示踪剂回收率与扫掠体积的Levenspiel公式]]
*   [[流线分析估算换热面积]]

## Connections To Other Work
*   本研究是Held et al. (2014) 模型的扩展，新增两条关键断裂，并首次实现瞬态示踪剂突破曲线的多井同时匹配[Egert unknown-year, pp. 4-6][Egert unknown-year, pp. 6-8]。
*   多井同时拟合不同路径的方法克服了以往独立模拟各井的局限，如Blumenthal et al. (2007)、Gessner et al. (2009) 的简化模型以及Radilla et al. (2012)的等效层状介质方法[Egert unknown-year, pp. 3-4]。
*   “分离断层”的识别与微震反演（Kohl et al., 2006）识别出的E‑W向及地震不活动面，以及VSP层析成像（Calò et al., 2016）发现的井间地震异常带一致[Egert unknown-year, pp. 17-20]。
*   示踪剂回收率和扫掠体积与Sanjuan et al. (2006) 和Sanjuan et al. (2015) 的实验分析结果吻合，但第三通道等的量化提供了新的细节[Egert unknown-year, pp. 17-19]。
*   裂隙内流动的非均匀性分析借用了Shook (2003, 2005) 关于断裂通道组流动‑存储容量关系的概念[Egert unknown-year, pp. 19-20]。
*   该研究关于基质扩散可忽略的结论与Radilla et al. (2012) 等先前研究中缺乏基质扩散证据的说法相符[Egert unknown-year, pp. 17-19]。

## Open Questions
*   “分离”断层是否总是表现为水力屏障，还是在特定应力扰动下可能转变为导水通道？其局部渗透率结构如何？[Egert unknown-year, pp. 17-20]
*   模型未捕获的未知裂隙（特别是与第二通道相通者）的几何形态和水力影响是什么？这些裂隙对长期回收率和热突破预测有何潜在影响？[Egert unknown-year, pp. 17-19]
*   忽略基质扩散和热衰减在数十年寿命尺度上是否仍合理？这些过程对长时间尺度浓度和换热面积的低估或高估程度？[Egert unknown-year, pp. 17-19]
*   储层北端的扩大导水区（北至GPK2以北）以及分离断层与区域断层系统的确切连接如何？能否作为未来钻探和增产的目标？[Egert unknown-year, pp. 19-22]
*   在当前商业运营方案（GPK2生产，GPK3、GPK4回注）下，不同流道间的动态分配和扫掠效率将如何演化？[Egert unknown-year, pp. 19-22]

## Source Coverage
本文档完全基于论文 `2020-egert-implications-on-large-scale-flow-of-the-fractured-egs-reservoir-soultz-inferred-from` 的所有索引片段。共处理 **15** 个非空源块，总计 **74042** 字符被索引，实际编译利用 **73389** 字符，覆盖率达 **99.1%**（按字符数）。所有非空源块均被纳入并用于提取信息，来源签名为 `46a65eabf5c145caaaeffcf7b284cc71328d12f1`。无额外文献或外部数据。
