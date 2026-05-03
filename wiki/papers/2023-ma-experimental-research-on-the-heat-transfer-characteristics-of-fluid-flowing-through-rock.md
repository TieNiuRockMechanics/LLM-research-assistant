---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-ma-experimental-research-on-the-heat-transfer-characteristics-of-fluid-flowing-through-rock"
title: "Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures."
status: "draft"
source_pdf: "data/papers/2023 - Experimental research on the heat transfer characteristics of fluid flowing through rock with intersecting fractures.pdf"
collections:
citation: "Ma, Yueqiang, et al. \"Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures.\" *Geothermics*, vol. 107, 2023, 102587."
indexed_texts: "13"
indexed_chars: "64180"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "60540"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.943285"
coverage_status: "full-index"
source_signature: "0613844e84458f56e1723c2e4a374c5c8dc516ab"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:31:47"
---

# Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures.

## One-line Summary
基于室内试验，研究了单条、两条相交及三条相交裂缝中蒸馏水的对流换热特性，推导了适用于多裂缝通道的对流换热系数公式，并分析了加载与卸载过程中渗流及换热行为[Ma 2023, pp. 1-1, 1‑2, 13‑14]。

## Research Question
当流体流经含单裂缝与多裂缝（两条及三条相交裂缝）的岩石时，其渗流与换热特性的差异与机制是什么？[Ma 2023, pp. 1-1, 1‑2, 2‑3]

## Study Area / Data
- **岩样来源**：吉林省德惠市后山地区晚印支期花岗闪长岩（灰白色、致密、无显裂缝），加工为直径约50 mm、高约100 mm的圆柱形试件，通过线切割分别制成含一条裂缝、两条相交裂缝和三条相交裂缝的试样，裂缝面较平坦[Ma 2023, pp. 2-3]。
- **试验条件**：测试温度85 °C；围压分别为5、10、15、20、25 MPa；注入水温约21 °C；注入流量范围为1~25 ml/min（不同试件和围压设置多级流量）；总共154个试验工况，包含加载与卸载过程[Ma 2023, pp. 2-3, 3‑4, 4‑5]。
- **岩样基本参数**：试样I（单裂缝）：直径49.5 mm，高99 mm，质量508.24 g；试样II（两条相交裂缝）：直径49.1 mm，高100 mm，质量499.5 g；试样III（三条相交裂缝）：直径48.7 mm，高99.9 mm，质量493.75 g[Ma 2023, pp. 3-4]。

## Methods
- **试验装置**：自主研发的干热岩实验室模拟系统，包括渗透压力子系统、温度控制子系统、围压子系统、试样夹持器和数据采集记录子系统；注入泵为高精度柱塞泵（ISCO），可提供0~45 ml/min的流量，温控0~200 °C，围压0~40 MPa[Ma 2023, pp. 2-3]。
- **试验流程**：将加热至85 °C的岩样在目标围压下，以不同注入流量注入蒸馏水，监测进出口水温及注入压力，待出水温度稳定后记录；卸载过程按围压25→20→15→10→5 MPa逐步降压重复试验[Ma 2023, pp. 3-4, 8‑9]。
- **对流换热系数计算**：
  - 基于Zhao(2014)的裂缝内流体温度分布解析解（式2）导出平均流体温度（式5），并给出单裂缝整体换热系数公式（式6）[Ma 2023, pp. 3-4, 4‑5]。
  - 多裂缝情况按换热面积等效处理：两条相交裂缝时换热面积取 \(4LR\)，公式化为式(7)；三条相交裂缝时取 \(6LR\)，公式化为式(8)[Ma 2023, pp. 4-5]。
  - 与其他五种经典公式的对比验证采用Bai et al. (2017b)的数据[Ma 2023, pp. 4-5, 5‑6]。
- **渗流参数计算**：
  - 单裂缝等效水力隙宽用立方律（式9）[Ma 2023, pp. 4-5]。
  - 多裂缝等效水力隙宽用式(10)（各裂缝隙宽的立方和开立方）[Ma 2023, pp. P5‑6]。
  - 水力传导系数由达西定律（式11）并结合各试件的过水断面面积计算（式12‑14）[Ma 2023, pp. 5-6]。
  - 渗透率通过式(15)由水力传导系数换算[Ma 2023, pp. 5-6]。
  - 水的密度、比热容、动力粘度与温度的关系采用多项式拟合（式16‑18）[Ma 2023, pp. 5-6]。

## Key Findings
1. **多裂缝的渗流性能显著优于单裂缝**：与单裂缝相比，两条相交裂缝的等效水力隙宽增大2.14~2.22倍，三条相交裂缝增大3.60~4.59倍；水力传导系数和渗透率亦有数倍提升[Ma 2023, pp. 5-6, 13‑14]。
2. **围压对渗流的影响**：等效水力隙宽、水力传导系数和渗透率均随围压升高而降低，主因是围压导致裂缝面压缩、隙宽减小[Ma 2023, pp. 6-8]。
3. **加载‑卸载过程中的不可逆性**：在相同围压下，卸载过程中的注入压力高于加载过程（单裂缝高0.5~2.44 MPa，两条裂缝高0.05~0.66 MPa，三条裂缝高0~0.014 MPa），表明裂缝面发生了不可逆塑性变形，渗流能力无法完全恢复；水力传导系数在卸载后亦低于加载同围压水平[Ma 2023, pp. 8-10]。
4. **出口水温与换热量随注入流量的变化**：当注入流量小于15 ml/min时，出口水温差随流量增大而增大，流量进一步增大后温差反而下降；但单位时间换热量始终与注入流量正相关。高流量可提高瞬时取热功率，而低流量可维持出口水温长期稳定[Ma 2023, pp. 9-10]。
5. **多裂缝换热强度**：
   - 在相同注入流量下，单裂缝试件的对流换热系数最大，三条裂缝试件最小（因相同总流量下每条裂缝分得的流速降低）[Ma 2023, pp. 10-12]。
   - 若令各裂缝面获得相同流速，则换热系数排序为：三条裂缝 > 两条裂缝 > 单裂缝。与单裂缝相比，两条裂缝换热系数提升6.16%~20.93%，三条裂缝提升21.56%~31.27%。多裂缝通过增大换热面积和缩短热传递路径改善了整体换热强度[Ma 2023, pp. 12-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Equivalent hydraulic aperture of two-intersecting-fracture sample increased by 2.14~2.22 times compared to single fracture; three-intersecting-fracture increased by 3.60~4.59 times. | [Ma 2023, pp. 13-14] | Loading process, T=85°C, injection rate 5 ml/min under confining pressures 5~25 MPa | Calculated via Eqs. (9) & (10) |
| Under same confining pressure, injection pressure during unloading was higher than during loading: single fracture 0.5–2.44 MPa, two fractures 0.05–0.66 MPa, three fractures 0–0.014 MPa. | [Ma 2023, pp. 8-10] | Unloading process; injection rates varied | Indicates irreversible plastic deformation and/or minor particle clogging. |
| At injection rate 1 ml/min, heat extracted Q and outlet-inlet temperature difference T_out−T_in followed the order: Sample III > Sample II > Sample I. | [Ma 2023, pp. 10-10] | Confining pressure 15 MPa; T_c=85°C; Q values: 3.03, 3.16, 3.22 J/s for samples I, II, III respectively. | Increase attributed to larger heat transfer area and shorter path in multi-fracture samples. |
| Convective heat transfer coefficient h increased linearly with injection flow rate for all samples. | [Ma 2023, pp. 10-12] | Confining pressure 5 MPa, three-intersecting-fracture sample; flow rate 1→25 ml/min, h from 5.59 to 193.67 W/(m²·K). | Flow rate is a key controlling factor. |
| At same fluid velocity on each fracture surface, h of three-fracture sample was 21.56%~31.27% higher than single-fracture sample, and two-fracture sample was 6.16%~20.93% higher. | [Ma 2023, pp. 12-13] | Conditions: corresponding total injection rates to ensure equal per-fracture velocity. | Shows true advantage of multi-fracture network in heat transfer intensity. |

## Limitations
- 试验中机械隙宽未在施加围压后测量，因此等效水力隙宽均由流量‑压差反算，未能直接观察隙宽变化[Ma 2023, pp. 2-3]。
- 裂缝面为线切割获得的相对平坦表面，未涉及自然粗糙裂缝的空间形貌影响[Ma 2023, pp. 2-3]。
- 试验采用的最高围压为25 MPa，注入流量上限25 ml/min，与EGS实际储层高温高压、大流量工况仍有差距[Ma 2023, pp. 4-5]。
- 未考虑化学作用（如矿物溶解/沉淀）对长期渗流‑传热的耦合影响，文中仅提及THMC耦合的相关文献[Ma 2023, pp. 1-2]。
- 结论主要基于花岗闪长岩，对其它岩性的普适性未验证。

## Assumptions / Conditions
- 对流换热系数沿流动方向视为常数，并以此导出裂缝内流体温度分布（式2）[Ma 2023, pp. 3-4]。
- 出口水温近似为裂缝末端流体温度，忽略出口混合效应。
- 多裂缝换热计算将多裂缝视作一个“大裂缝”，按等效换热面积处理，每条裂缝贡献等同[Ma 2023, pp. 4-5]。
- 水物性参数仅考虑温度影响，采用多项式拟合（0‑100 °C范围内），未考虑压力影响[Ma 2023, pp. 5-6]。
- 立方律适用，假设裂缝内为层流，且流体充填整个裂缝通道。
- 卸载过程中围压逐步降低，相当于应力路径简化，未模拟复杂的多场耦合历史。

## Key Variables / Parameters
列出本研究中明确测量或计算的主要变量，尽量使用原文术语并保留源标签。

- **对流换热系数 \(h\)**（overall heat transfer coefficient）：基于式(6)、(7)、(8)计算[Ma 2023, pp. 4-5]。
- **注入流量 \(q_v\)**：1‑25 ml/min，多级设定[Ma 2023, pp. 4-5]。
- **等效水力隙宽 \(b\)**：单裂缝按式(9)、多裂缝按式(10)计算[Ma 2023, pp. P4‑5, P5‑6]。
- **水力传导系数 \(K\)**：式(11)，过水断面面积按式(12)‑(14)取不同[Ma 2023, pp. 5-6]。
- **渗透率 \(k\)**：由式(15)与K的换算关系获得[Ma 2023, pp. 5-6]。
- **进出口水温 \(T_{\text{in}}, T_{\text{out}}\)** 与岩石外壁温 \(T_c\)（85°C）[Ma 2023, pp. 3-4]。
- **围压 \(P_c\)**：5, 10, 15, 20, 25 MPa[Ma 2023, pp. 3-4]。
- **单位时间换热量 \(Q\)**（流体从岩石汲取的热量）[Ma 2023, pp. 9-10].
- **水流速度 \(v\)**（裂缝面上的平均流速）[Ma 2023, pp. 12-13].

## Reusable Claims
以下声明均基于本实验条件的结论，引用时需注明条件：
1. 对于光滑裂缝面，多裂缝试样的等效水力隙宽显著大于单裂缝，且隙宽增量随裂缝数目增加（两条裂缝增幅约2.1‑2.2倍，三条裂缝约3.6‑4.6倍），适用于无充填、裂缝面接触良好的情形[Ma 2023, pp. 13-14]。
2. 在加载‑卸载循环中，裂缝岩体的渗流能力发生不可逆降低，注入压力升高，水力传导系数下降，这一现象可能与裂缝面塑性变形及微粒堵塞有关[Ma 2023, pp. 8-10]。
3. 当总注入流量相同时，多裂缝试件的对流换热系数低于单裂缝，因为单条裂缝获得的流速更高；但若控制各裂缝面流速相同，则多裂缝的换热系数高于单裂缝（两条裂缝提升6‑21%，三条裂缝提升22‑31%），表明多裂缝网络在保证均匀流量分配时可强化换热[Ma 2023, pp. 12-13]。
4. 注入流量是控制换热强度的关键因素，对流换热系数与流量呈线性正相关（在所测流量范围内）[Ma 2023, pp. 10-12]。
5. 低流量下出口水温可长期稳定，高流量下瞬时取热功率增大但出水温度可能衰减，工程选择需在取热功率和系统寿命间权衡[Ma 2023, pp. 9-10]。
6. 围压对换热系数的影响不显著，在本文试验范围内换热系数随围压变化波动较小[Ma 2023, pp. 10-10]。

## Candidate Concepts
- [[intersecting fractures]]
- [[heat transfer coefficient]]
- [[equivalent hydraulic aperture]]
- [[hydraulic conductivity]]
- [[fracture network]]
- [[convective heat transfer]]
- [[unloading process]]
- [[irreversible deformation]]
- [[seepage characteristics]]
- [[hot dry rock (HDR) laboratory simulation]]
- [[cubic law]]
- [[geothermal reservoir]]

## Candidate Methods
- [[wire-cutting rock samples]]
- [[ISCO pump precision injection]]
- [[equations for heat transfer coefficient in multi-fracture channels]]
- [[Darcy’s law based hydraulic conductivity measurement]]
- [[polynomial fitting of water properties vs. temperature]]
- [[laboratory hot dry rock simulation system]]
- [[cyclic loading-unloading confining pressure test]]
- [[comparative analysis of single and multi-fracture heat transfer]]

## Connections To Other Work
- 本文在单裂缝换热系数公式推导上，沿用了Zhao (2014)的流体温度分布解析解，并与其公式I进行了对比[Ma 2023, pp. 3-4, 4‑5]。
- 整体换热系数公式的验证采用了Bai et al. (2017b)的试验数据，比较了五种现有公式（包括Bai et al. 2017b, He et al. 2021等），指出本公式(V)的适用性[Ma 2023, pp. 4-5]。
- 文中引述了多篇单裂缝换热试验（如Luo et al., 2017; Ma et al., 2018, 2019a; Jiang et al., 2017; Bai et al., 2017b等），并将本试验结果与Bai et al. (2017b)的结论进行了对照，均显示流量增大使出口温差先升后降[Ma 2023, pp. 9-10]。
- 关于过水断面面积计算和多裂缝隙宽的计算，引用了Huang et al. (2016a)和Sarkar et al. (2004)的方法[Ma 2023, pp. 5-6]。
- 文中提到Caulk et al. (2016), Kamali-Asl et al. (2018), Shu et al. (2020)等关于THMC耦合下渗透率变化的研究，作为背景但未在试验中涉及[Ma 2023, pp. 1-2]。

## Open Questions
- 本试验采用光滑切割裂缝，粗糙裂缝表面的流动与换热行为是否会导致截然不同的结论，尤其是多裂缝交会处的局部热传递机制尚不明确。
- 试验未考虑实际地热储层中的高温高压及化学作用，长期水岩反应对裂缝隙宽和换热系数的动态影响值得进一步研究。
- 多裂缝网络中各分支裂缝的流量分配不均匀性会如何影响整体的单位体积取热率，文中假设对称分配可能过于理想化。
- 在更高流速、超临界流体（如CO₂）条件下的多裂缝换热特性是否有类似的线性关系仍待验证。
- 卸载过程中的损伤和不可逆性是否可通过循环加载渐趋稳定，及其对长期热提取的经济性影响未讨论。

## Source Coverage
页面基于提供的全部13个非空索引片段编译而成，片段涵盖论文全文（从标题、摘要、引言、方法、结果到结论与参考文献）。索引字符数64,180，编译后使用字符数约60,540，覆盖率按字符计为94.33%，按片段数计为100%。所有片段均已纳入并保留源标签。未使用片段外的信息。
