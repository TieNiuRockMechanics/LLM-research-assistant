---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-frank-transient-heat-transfer-processes-in-a-single-rock-fracture-at-high-flow-rates"
title: "Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates."
status: "draft"
source_pdf: "data/papers/2021 - Transient heat transfer processes in a single rock fracture at high flow rates.pdf"
collections:
citation: "Frank, Sascha, et al. \"Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates.\" *Geothermics*, vol. 89, 2021, p. 101989. Accessed 2026."
indexed_texts: "20"
indexed_chars: "95356"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "90820"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.952431"
coverage_status: "full-index"
source_signature: "a4383a83d79f7d1924becbbdf4750995f02d0afe"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:53:44"
---

# Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates.

## One-line Summary

在高流速（80–350 mm/s）条件下，通过劈裂砂岩单裂隙的瞬态传热实验，研究了表面粗糙度、流速对局部热非平衡（LTNE）状态下传热系数和热突破行为的影响，发现高流速下出口温度降低可能导致传热量上限，且瞬态热突破时间受岩石热容和导热能力控制。<a id="ref-1"></a>[Frank 2021, pp. 1-1]

## Research Question

- 在单裂隙系统中，高流速瞬态传热过程及达到稳态时的行为如何？<a id="ref-2"></a>[Frank 2021, pp. 1-1]
- 裂隙宽度、表面粗糙度、渗透率和传输参数（如弥散系数）对传热过程有何影响？<a id="ref-3"></a>[Frank 2021, pp. 1-2]
- 在高于以往实验的流速下（最高350 mm/s），是否存在传热上限？<a id="ref-4"></a>[Frank 2021, pp. 2-3]

## Study Area / Data

- 样本：Flechtinger砂岩（Permian），取自德国Saxony-Anhalt的Bebertal采石场，岩心垂直于层理钻取，尺寸为直径100 mm、长度150 mm。<a id="ref-5"></a>[Frank 2021, pp. 2-3]
- 孔隙度：6–11%，基质渗透率约10⁻¹⁷ m²。<a id="ref-6"></a>[Frank 2021, pp. 2-3]
- 裂隙通过巴西劈裂试验生成，用Teflon热缩管固定两半，未施加额外围压。<a id="ref-7"></a>[Frank 2021, pp. 2-3]
- 裂隙水力开度121 μm，渗透率1.2×10⁻⁹ m²（由Darcy和示踪试验得到）。<a id="ref-8"></a>[Frank 2021, pp. 3-3]
- 粗糙度：沿流动方向JRC=14（Barton & Choubey分类的第7至第8级，“rough, undulating”），垂直流动方向稍高；真实表面积比平滑面大10%，但接触面积约占31%，故有效换热面积比光滑面总面积小约21%。<a id="ref-9"></a>[Frank 2021, pp. 6-7]
- 实验流体为自来水，系统压力3 bar。<a id="ref-10"></a>[Frank 2021, pp. 4-5]

## Methods

### 实验装置
- 核心部件：高压釜（austenitic stainless steel 1.4571）放置岩心，5 L水箱，活塞隔膜泵，氦气瓶加压，双管式换热器（HEX）用于冷却。<a id="ref-11"></a>[Frank 2021, pp. 3-3]
- 温度控制：两个浴槽恒温器分别加热高压釜和水箱，电伴热带维持管路恒温。<a id="ref-12"></a>[Frank 2021, pp. 3-3]
- 测量：4个K型热电偶（精度±0.5 °C）和2个压力传感器（Wika IS‑10，精度0.25% FS，即1 bar），距离岩心5 mm测量进出口温度；科里奥利质量流量计测量泵流量（1.1~4.2 g/s）。<a id="ref-13"></a>[Frank 2021, pp. 3-3, 3-5]
- 岩心装入高压釜，两端用铝块定位，密封圈防止旁流。<a id="ref-14"></a>[Frank 2021, pp. 3-3]

### 实验流程
- 系统加热至约55 °C并维持热平衡；实验开始时切换流路通过换热器进行冷却，随后关闭换热器进行再加热；每个流速和冷却速率组合共进行了8组实验。<a id="ref-15"></a>[Frank 2021, pp. 4-5]
- 流速设定：1.1 g/s (92 mm/s)、2.0 g/s (168 mm/s)、3.0 g/s (252 mm/s)、4.2 g/s (352 mm/s)；冷却水流量为>20 g/s（高冷却度）和4.5 g/s（低冷却度）。<a id="ref-16"></a>[Frank 2021, pp. 4-5]
- 实验在出口温度达到稳态后停止，再加热阶段同样记录数据。<a id="ref-17"></a>[Frank 2021, pp. 4-5]

### 数据分析与理论背景
- 流速换算：由质量流量和密度计算体积流量，并结合裂隙体积得到流动速度；用立方定律（Cubic law）从压差算出参考流速。<a id="ref-18"></a>[Frank 2021, pp. 5-5]
- 雷诺数计算：Re = 2·q_V·ρ_w/(μ·L_W)，初始约55 °C时Re介于39~164，降温后（≈26 °C）降至23~96，文中假设全程以层流为主。<a id="ref-19"></a>[Frank 2021, pp. 10-11]
- 局部热非平衡（LTNE）热方程：固相仅导热，流体相包含对流、热弥散和源汇项Q_rw（代表相间传热）。<a id="ref-20"></a>[Frank 2021, pp. 5-5]
- 传热系数计算：
  - 式 (9)：h = ρ_w C_w q_v (T₂−T₁) / [A (T_c − (T₁+T₂)/2)]（Bai et al., 2017）。<a id="ref-21"></a>[Frank 2021, pp. 5-5]
  - 式 (11)：h = −0.5 ρ_w C_w q_v / A · ln[(T₂−T_c)/(T₁−T_c)]（基于Heinze et al., 2017; Zhao, 2014），作为传热系数下限。<a id="ref-22"></a>[Frank 2021, pp. 5-6]
- 稳态传热量：Q = C_w ρ_w q_v (T₂−T₁)。<a id="ref-23"></a>[Frank 2021, pp. 6-6]
- 瞬态突破曲线拟合：使用含恒定源项的解析ADE（van Genuchten & Alves, 1982），拟合参数v、D_w、γ。<a id="ref-24"></a>[Frank 2021, pp. 5-5, 11-11]
- 弥散系数对比：用NaCl示踪试验的ADE拟合结果与热弥散系数比较。<a id="ref-25"></a>[Frank 2021, pp. 13-14]

## Key Findings

1. **稳态出口温度与传热量**：出口温度随流速增加而降低，高冷却度下从11.6 °C温差（92 mm/s）降至7.5 °C（352 mm/s）；低冷却度下从9.3 °C降至6.3 °C。<a id="ref-26"></a>[Frank 2021, pp. 7-7]
2. **传热量上限趋势**：总传热量随流速增加而增加，但增速减缓，在约250 mm/s后更明显；最高流速352 mm/s时未出现绝对最大值，但线性外推预示极高流速下可能触及极限。<a id="ref-27"></a>[Frank 2021, pp. 7-8]
3. **整体传热系数**：式(9)的结果为230–420 W/(m²·°C)，式(11)为110–270 W/(m²·°C)，两种模型均随流速增加而略有下降；但实际下降原因与入口绝对温度随流速下降有关，并非流速本身直接导致。<a id="ref-28"></a>[Frank 2021, pp. 8-8]
4. **瞬态热突破**：
   - 突破时间（入口温度开始下降至出口温度首次可测下降）为5.5~39.0秒，远长于流体实际穿越时间（0.5~1.6秒），表明岩石可短时维持出口最高温度。<a id="ref-29"></a>[Frank 2021, pp. 8-9]
   - 冷却和加热过程的突破时间相近，加热过程略长；突破时间与流速呈非线性关系。<a id="ref-30"></a>[Frank 2021, pp. 9-9]
   - 瞬态持续期1000~1600 s，无明显趋势。<a id="ref-31"></a>[Frank 2021, pp. 9-9]
5. **热传递方向反转**：在最高流速4.2 g/s的再加热阶段，约1600 s时出现约10秒的入口温度高于出口温度现象，即热量由流体传向岩石，随即恢复为岩石向流体传热，未观察到滞后效应。<a id="ref-32"></a>[Frank 2021, pp. 9-10]
6. **压力‑温度耦合**：系统压力随温度变化快速响应，冷却时压力降低，加热时升高；压差幅度可达0.5×10⁵ Pa，主要由流体热胀冷缩引起，非机械效应。<a id="ref-33"></a>[Frank 2021, pp. 10-10]
7. **粗糙度对传热系数的影响**：计入真实表面积和接触面积后，有效换热面积减小21%，导致传热系数估算值相应提高（模型反比于面积）；但总传热量不受影响。<a id="ref-34"></a>[Frank 2021, pp. 11-12]
8. **ADE拟合局限性**：
   - 拟合得到的流速极低（0.2~0.7 mm/s），比实际流速小3个数量级。<a id="ref-35"></a>[Frank 2021, pp. 11-12]
   - 热弥散系数（8.5×10⁻⁶~9.0×10⁻⁵ m²/s）与溶质弥散系数（2.0×10⁻⁵~2.9×10⁻⁵ m²/s）量级相当，表明热与溶质弥散机制相似。<a id="ref-36"></a>[Frank 2021, pp. 13-14]
   - 恒定源项（~2.2×10⁻¹⁴ °C/s）无法捕捉动态传热，导致拟合总传热量远低于实测值。<a id="ref-37"></a>[Frank 2021, pp. 11-12]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| JRC在流动方向为14，垂直方向稍高；接触面积占31%，真实表面积比几何面大10%，有效换热面积比几何面小21%。 | [Frank 2021, pp. 6-7] | 劈裂Flechtinger砂岩，无围压 | 粗糙度单项使估算的h提高约20%。 |
| 稳态出口温差：高冷却下11.6 °C (92 mm/s) → 7.5 °C (352 mm/s)；低冷却下9.3 °C → 6.3 °C。 | [Frank 2021, pp. 7-7] | 入口温度范围26.9–44.5 °C | 差值几乎线性下降。 |
| 传热量：最高流速352 mm/s时高冷却度132.5 W，低冷却度110.0 W；增速变缓。 | [Frank 2021, pp. 7-8] | 泵流量4.2 g/s | 认为未达到绝对上限。 |
| h (式9)：高冷却度451.6→346.8 W/(m²·°C)；低冷却度463.8→411.4 W/(m²·°C)。 | [Frank 2021, pp. 8-8] | 计算用T_c取高压釜两温度均值 | 对入口绝对温度敏感。 |
| h (式11)：高冷却度289.1→174.7 W/(m²·°C)；低冷却度302.9→207.8 W/(m²·°C)。 | [Frank 2021, pp. 8-8] | 代表下限值 | 与式(9)趋势一致，值低1/2至2/3。 |
| 热突破延迟：5.5 s (352 mm/s) 至 39.0 s (92 mm/s)；流体穿越时间0.5~1.6 s。 | [Frank 2021, pp. 8-9] | 55 °C初始，瞬态初期 | 表明岩石热容维持出口高温。 |
| 热传方向反转：4.2 g/s再加热期约10 s内T_in > T_out。 | [Frank 2021, pp. 9-10] | 冷却停止后约1600 s时出现 | 无滞后，传热系数方向无关。 |
| ADE拟合流速0.2~0.7 mm/s，实际92~352 mm/s。 | [Frank 2021, pp. 11-12] | 含恒定源项的解析解 | 低估约千倍。 |
| 热弥散系数与溶质弥散系数可比：热8.5e-6~9.0e-5 m²/s，质2.0e-5~2.9e-5 m²/s。 | [Frank 2021, pp. 13-14] | NaCl示踪试验 | 基础机制相似。 |
| 压力随温度变化幅度可达0.5×10⁵ Pa，响应迅速。 | [Frank 2021, pp. 10-10] | 闭路系统，3 bar初始压力 | 热膨胀/收缩主导。 |

## Limitations

- 实验最高流速接近泵能力上限，且入口非均匀冷却导致水箱温度轻微下降，可能影响稳态入口恒定性。<a id="ref-38"></a>[Frank 2021, pp. 9-9, 12-12]
- 高压釜加热方式导致岩心外表面存在约1 °C的轴向温差，尽管认为可忽略。<a id="ref-39"></a>[Frank 2021, pp. 8-8]
- 利用立方定律估算的流速比泵流量推算值高一个数量级，压差数据可能受裂隙粗糙度及系统热效应干扰，不能直接用于流速验证。<a id="ref-40"></a>[Frank 2021, pp. 13-13]
- ADE拟合使用了恒定源项，无法反映相间温差随时间的变化，不适合定量分析LTNE瞬态。<a id="ref-41"></a>[Frank 2021, pp. 13-14]
- 对真实换热面积的评估基于静态表面扫描，未考虑裂隙面间的热传导及局部流动路径的影响。<a id="ref-42"></a>[Frank 2021, pp. 11-12]
- 雷诺数处于层流‑湍流过渡边界，尤其在实验初期温度较高时可能局部出现非层流状态，但未进行详细流态区分。<a id="ref-43"></a>[Frank 2021, pp. 10-11]

## Assumptions / Conditions

- 假设流经裂隙的水全部通过断裂，无基质渗流（因基质渗透率远低于裂隙渗透率）。<a id="ref-44"></a>[Frank 2021, pp. 3-3]
- 假设实验全程以层流为主，尽管雷诺数覆盖过渡区。<a id="ref-45"></a>[Frank 2021, pp. 5-5]
- 计算整体传热系数时，假设最大岩石温度T_c为高压釜上、下测温点的均值，并沿轴向线性分布。<a id="ref-46"></a>[Frank 2021, pp. 8-8]
- ADE解析解中将热交换处理为线性恒定源项。<a id="ref-47"></a>[Frank 2021, pp. 5-5]
- 采用饱和砂岩，孔隙水与固体骨架处于局部热平衡，对基质热容产生影响，但不参与裂隙流动传热。<a id="ref-48"></a>[Frank 2021, pp. 13-13]
- 实验中未考虑化学作用或矿物溶解‑沉淀的影响。<a id="ref-49"></a>[Frank 2021, pp. 12-13]

## Key Variables / Parameters

- 质量流量 q_P：1.1, 2.0, 3.0, 4.2 g/s
- 体积流量 q_V：1.11, 2.03, 3.04, 4.26 ×10⁻⁶ m³/s
- 流速 v：92, 168, 252, 352 mm/s
- 初始系统温度 ~55 °C
- 入口温度 T_in 范围：26.9–44.5 °C
- 出口温度 T_out 范围：34.4–53.8 °C
- 最大岩石温度 T_c 范围：54.3–56.8 °C（高压釜上下均值）
- 整体传热系数 h (式9)：230~464 W/(m²·°C)； h (式11)：110~303 W/(m²·°C)
- 热弥散系数 D_w：8.5×10⁻⁶ 至 9.0×10⁻⁵ m²/s
- 溶质弥散系数（示踪）：2.0×10⁻⁵ 至 2.9×10⁻⁵ m²/s
- 热突破延迟：5.5~39.0 s
- 瞬态持续时间：1000~1600 s
- 裂隙水力开度：121 μm；渗透率：1.2×10⁻⁹ m²
- 表面接触面积比：31%；有效换热面积系数：0.79（相对光滑面积） <a id="ref-50"></a>[Frank 2021, pp. 7-13]

## Reusable Claims

- 在高流速单裂隙实验中，稳态出口温差随流速线性下降，但总传热量仍上升，斜率递减；极高流速下可能存在传热量上限。（条件：Flechtinger砂岩，开度~120 μm，Re约30~160，水温26–55°C）<a id="ref-51"></a>[Frank 2021, pp. 7-8]
- 真实表面粗糙度和接触面积使有效换热面积约减少21%，导致式(9)和式(11)估算的h值对应提高。（限制：完全基于表面扫描，未考虑裂隙两半间的热传导）<a id="ref-52"></a>[Frank 2021, pp. 6-7, 11-12]
- 含恒定源项的ADE解析解无法正确再现LTNE条件下的热突破曲线，拟合的流速偏低3个数量级；该方法不适用于定量反演裂隙传热参数。<a id="ref-53"></a>[Frank 2021, pp. 13-14]
- 瞬态热突破延迟远大于流体穿越时间，且与流速呈非线性关系，表明岩石的有效热容和导热能力是控制瞬态行为的关键参数。<a id="ref-54"></a>[Frank 2021, pp. 8-9]
- 实验捕获到短暂（约10 s）的传热方向反转，期间未见传热系数的方向依赖性，暗示整体h可能适用于冷却与加热两种工况。（条件：单一流速4.2 g/s，加热相位）<a id="ref-55"></a>[Frank 2021, pp. 13-13, 9-10]
- 闭路系统中流体热胀冷缩引起压力与温度同步变化，幅度可达0.5×10⁵ Pa，数值模拟需包含温度依赖的流体物性以复现该现象。<a id="ref-56"></a>[Frank 2021, pp. 10-10, 14-14]
- 热弥散系数与溶质弥散系数处于同一量级，表明裂隙中热与物质弥散的物理机制相似，但热弥散额外受基质导热影响。<a id="ref-57"></a>[Frank 2021, pp. 13-14]

## Candidate Concepts

- [[local thermal non-equilibrium (LTNE)]]
- [[fracture roughness]]
- [[joint roughness coefficient (JRC)]]
- [[overall heat transfer coefficient]]
- [[thermal breakthrough curve]]
- [[advection-dispersion equation (ADE)]]
- [[thermal dispersivity]]
- [[cubic law]]
- [[heat transfer area]]
- [[thermal equilibrium / non-equilibrium]]
- [[Flechtinger sandstone]]
- [[dual porosity]]
- [[effective heat capacity]] of saturated rock

## Candidate Methods

- [[transient heat transfer experiment in single fracture]]
- [[Brazilian test for fracture generation]]
- [[3D laser scanning for roughness characterization]]
- [[Darcy and tracer tests for hydraulic parameters]]
- [[analytical solution of ADE with constant source term]]
- [[least-squares fitting of thermal breakthrough curves]]
- [[steady-state heat transfer coefficient calculation]]
- [[Cubic law flow velocity estimation]]
- [[comparison of thermal and solute dispersion coefficients]]

## Connections To Other Work

- 整体传热系数的定义和模型对比了 Zhao(2014)、Heinze et al.(2017)、Bai et al.(2016, 2017) 的成果；指出 Zhao(2014) 的方程在更高流速下产生负值，而 Bai et al.(2017) 和本文推导的式(11)可给出合理结果。<a id="ref-58"></a>[Frank 2021, pp. 1-2, 7-8]
- 实验流速范围较以往研究（多数为几mm/s）高出两个数量级，扩展了对传热系数速度依赖性的认识。<a id="ref-59"></a>[Frank 2021, pp. 1-2]
- 瞬态热突破分析在单裂隙LTNE中研究较少；Gossler et al.(2019) 在多孔介质中研究了类似问题。<a id="ref-60"></a>[Frank 2021, pp. 13-14]
- Heinze & Hamidi (2017) 的双重孔隙LTNE模型表明孔隙水可影响瞬态热容，与本文推断一致。<a id="ref-61"></a>[Frank 2021, pp. 13-13]
- 热弥散与溶质弥散的对比借鉴了 Rau et al.(2012, 2017) 把热作为示踪剂的理解框架。<a id="ref-62"></a>[Frank 2021, pp. 11-12, 13-14]

## Open Questions

- 极高流速下传热量是否达到上限，上限由什么机制控制？<a id="ref-63"></a>[Frank 2021, pp. 7-8, 12-12]
- 裂隙表面的接触区域对两半岩体间的热传导有何影响？<a id="ref-64"></a>[Frank 2021, pp. 11-12]
- 如何建立适用于单裂隙LTNE瞬态突破曲线的反演方法，取代不准确的ADE恒定源项拟合？<a id="ref-65"></a>[Frank 2021, pp. 13-14]
- 在更大的流速范围内，传热系数的速度依赖性是否发生质变？<a id="ref-66"></a>[Frank 2021, pp. 12-12]
- 真实裂隙中局部流动异质性（如宏观孔洞）如何影响整体传热？<a id="ref-67"></a>[Frank 2021, pp. 12-12]
- 饱和与非饱和砂岩的瞬态热行为差异有多大？<a id="ref-68"></a>[Frank 2021, pp. 13-13]
- 是否存在通用、可预测的局部传热系数模型，能涵盖岩石类型和粗糙度效应？<a id="ref-69"></a>[Frank 2021, pp. 12-13]

## Source Coverage

所有20个非空索引片段均已处理。索引文本总字符数95,356，编译后使用源文本90,820字符，覆盖比率按字符计95.24%，按块计100%。源签名为 a4383a83d79f7d1924becbbdf4750995f02d0afe。编译策略为单次Markdown生成。<a id="ref-70"></a>[Coverage audit metadata]
