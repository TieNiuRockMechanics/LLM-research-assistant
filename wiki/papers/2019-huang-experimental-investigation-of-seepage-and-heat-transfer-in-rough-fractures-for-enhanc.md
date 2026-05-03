---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc"
title: "Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2019 - Experimental investigation of seepage and heat transfer in rough fractures for enhanced geothermal systems.pdf"
collections:
  - "part2"
  - "雷恩学派分形研究"
citation: "Huang, Yibin, et al. \"Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems.\" *Renewable Energy*, vol. 135, 2019, pp. 846-855. 10.1016/j.renene.2018.12.063. Accessed 2026."
indexed_texts: "10"
indexed_chars: "47042"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "47262"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004677"
coverage_status: "full-index"
source_signature: "ab788fd4d51d1cd58aab5b5ceb56cbb83628e876"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T00:28:44"
---

# Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems.

## One-line Summary
本研究利用3D打印技术与Barton节理粗糙度系数（JRC）剖面，在人工水泥砂浆岩样中开展蒸馏水渗流及对流换热实验，揭示了粗糙度方向性对裂隙渗流能力和热传递性能的相反影响，为增强型地热系统（EGS）储层裂隙优化提供了可重复的实验依据。

## Research Question
粗糙裂隙形貌（特别是粗糙度的方向性）与围压条件如何影响单裂隙中的渗流特性及对流换热效率？明确在EGS环境下，垂直于流动方向和平行于流动方向的大粗糙度分别对等效水力开度、流动稳定性、岩石温度演化和对流换热系数的作用机制。

## Study Area / Data
本研究在实验室条件下进行，不涉及野外现场区域。实验数据来自两个以水泥砂浆浇铸、内嵌JRC模板的人工圆柱形岩样（尺寸约φ50 mm × 100 mm）。岩样粗糙度组合分别为：① 10–12 (轴向) & 18–20 (径向)；② 18–20 (轴向) & 10–12 (径向)。工质为蒸馏水，实验温度设定为60、70、80、90 °C，流速为5、10、15、20 ml/min，对流换热测试时围压固定为1 MPa；渗流特性测试时围压分别为5、10、15 MPa，入口压力多级变化。

## Methods
1. **试样制备**：通过Barton典型JRC剖面（10–12和18–20）建立数字模型，采用高精度（层厚0.1 mm）3D打印制作模板，将模板置入圆柱形模具后浇铸水泥砂浆（水泥:砂:水=1:1:0.4，普通硅酸盐水泥325R，砂细度模数2.4），水中养护28天得到可重复的人工裂隙岩样。
2. **实验系统**：自研热干岩实验及模拟系统，包括ISCO双泵注水系统、岩心夹持器、电动水泵（最高围压40 MPa）、环状加热（最高200 °C）、PT1000铂电阻温度测量（岩壁6个，出口流体1个）及数据采集记录系统。
3. **实验步骤**：对流换热实验中，先将岩样加热至设定温度（60、70、80、90 °C），然后以不同流量注入22 °C蒸馏水，实时记录岩壁与出口温度。渗流特性实验在常温及80 °C下进行，改变围压与入口压力，监测流量变化。
4. **数据处理**：
   - 对流换热系数由牛顿冷却公式结合温度分布推导\[Eq. (7)\]：  
     \(h = \frac{c_i \rho_i q (T_{out} - T_{in})}{2RL\left(T_w - \frac{T_{out}+T_{in}}{2}\right)}\)，  
     其中\(T_w\)为岩壁温度，\(T_{in}\)、\(T_{out}\)为进、出口水温，\(R\)、\(L\)为岩样半径与长度。
   - 等效水力开度由立方定律反演\[Eq. (11)\]：  
     \(b = \sqrt[3]{\frac{12 \nu \rho L q}{D \Delta p_0}}\)，  
     \(D\)为裂隙宽度，\(\Delta p_0\)为进出口压差。
5. **不确定性分析**：温差测量不确定度最高0.28%，岩壁与流体温差不确定度0.41%，长度和直径的测量误差分别为±2%和±4%，流量误差±0.3%，最终对流换热系数h的最大不确定度为±4.51%。

## Key Findings
1. **渗流特性**  
   - 在相同围压下，流量随入口压力呈指数式增加；围压越高，相同入口压力对应的流量越低。  
   - 粗糙度方向显著影响渗流能力：当轴向JRC=18–20（垂直流向的大粗糙度）时，等效水力开度小于轴向JRC=10–12的情况（例如5 MPa围压下，前者b=1.4–1.8 mm，后者b=1.45–1.87 mm），导致流量降低。  
   - 高围压下裂隙闭合增强，由入口压力变化引起的开度增量减小（15 MPa时变化仅约0.2 mm），且流动达到稳定的时间更短（15 MPa约150 s，5 MPa约350 s）。

2. **岩石温度响应**  
   - 注入流体后0~约10 min内，岩壁温度快速下降，之后趋于平缓；高流速加速热传导，温度下降更快且最终温度更低（60 °C时，5 ml/min比20 ml/min温度高约2.0 °C；80 °C时高约3.0 °C）。  
   - 出口流体温度与初始岩温几乎呈线性关系；高初始岩温与高流速均可提升出口水温。

3. **粗糙度方向对传热的影响**  
   - 岩壁温度在裂隙凸起和凹槽处出现波动，与裂隙几何形态密切相关。  
   - 垂直流向的大粗糙度（如18–20）造成流体扰动，产生涡流，增大有效换热面积，对流换热系数较高；平行流向的大粗糙度（如18–20）则易形成渗流优势通道，降低有效换热面积，换热系数较低。  
   - 对流换热系数随流速和温度升高近似线性增加，与边界层厚度减小有关。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 同围压下流量随入口压力指数增加；垂直流向的大粗糙度使流量降低 | Huang 2019, pp. 6-7 | 围压5、10、15 MPa，室温，蒸馏水，人工裂隙 | 基于JRC 10–12 & 18–20 与 18–20 & 10–12 两组试样的对比 |
| 等效水力开度：18–20 & 10–12试样在围压5 MPa时为1.4–1.8 mm，10 MPa为0.88–1.04 mm，15 MPa为0.69–0.87 mm | Huang 2019, pp. 6-7 | 由立方律反算，围压5、10、15 MPa | 入口压力变化时开度变动范围约0.4 mm (5 MPa) 至0.2 mm (15 MPa) |
| 高围压下流量稳定时间更短：15 MPa→约150 s，10 MPa→约250 s，5 MPa→约350 s | Huang 2019, pp. 7 | 入口压力2 MPa，岩温80 °C，试样18–20 & 10–12 | 高围压使裂隙接触更紧密，凹槽导流作用减弱 |
| 岩温在0~约10 min内快速下降，后趋于稳定；5 ml/min比20 ml/min最终壁温高2.0 °C（60 °C）和3.0 °C（80 °C） | Huang 2019, pp. 7-8 | 试样18–20 & 10–12，初始岩温60、80 °C | 高流速提取热量更多，热传导加速 |
| 出口温度与初始岩温呈近似线性关系；高流速可提升出口温度 | Huang 2019, pp. 8-9 | t=10 min，试样18–20 & 10–12与10–12 & 18–20 | 10 ml/min和20 ml/min条件下均呈线性趋势 |
| 垂直流向的大粗糙度（18–20）导致岩壁温度在凸起/凹槽处出现明显下降（NO.2、NO.5），换热系数较大；平行流向的大粗糙度（18–20）则波动较小，换热系数较小 | Huang 2019, pp. 8-10 | 初始岩温60、90 °C，t=10 min | 对流换热系数具体数值见原文图16，此处保留定性结论 |
| 对流换热系数随流速和温度升高而近似线性增加 | Huang 2019, pp. 9-10 | 岩温60~90 °C，流速5~20 ml/min | 与运动粘度降低、边界层减薄有关 |

## Limitations
- 实验仅采用两种JRC组合（10–12 & 18–20 和 18–20 & 10–12），未涵盖更多粗糙度级别及方向组合。
- 岩样为水泥砂浆人工材料而非真实花岗岩，热物理性质与力学响应可能存在差异。
- 仅使用蒸馏水作为工质，且限于单相层流条件，未考虑多相流或超临界态流体。
- 对流换热测试中围压固定为1 MPa，未系统考察高围压（如>5 MPa）下传热特性。
- 模型简化为二维流动，忽略热辐射，且假设裂隙内流体温度可由进出口平均温度表征，可能引入误差。
- 岩样尺寸为φ50×100 mm，尺度较小，可能未完全反映实际储层裂隙网络的非线性行为。
- 3D打印模板精度为0.1 mm，虽可忽略，但手工浇铸导致岩样表面不光滑，直径测量误差达±4%。

## Assumptions / Conditions
- 流体为单相不可压缩，流动为稳定层流。
- 裂隙面的渗透率远大于岩体基质，流体在裂隙中为二维流动。
- 热传递过程中忽略热辐射。
- 裂隙内流体温度\(T_f\)由进出口平均温度\((T_{in}+T_{out})/2\)近似替代；岩样中心点温度\(T_0\)同样由此平均温度代替（引自Bai et al., 2016）。
- 对流换热测试中围压施加1 MPa，确保两半圆柱岩样紧密接触，使流体主要受JRC剖面影响而不致沿平面流过。
- 蒸馏水的物性（比热容、密度、运动粘度）随温度变化，采用已知函数关系（图6）。

## Key Variables / Parameters
- 节理粗糙度系数：轴向JRC和径向JRC；两种组合：10–12 & 18–20 和 18–20 & 10–12
- 等效水力开度 \(b\) (mm)
- 流量 \(q\) (ml/min)
- 入口/出口压力，围压 (MPa)
- 岩壁温度 \(T_w\) (°C)，进出口温度 \(T_{in}\)=22 °C, \(T_{out}\)
- 初始岩石温度：60, 70, 80, 90 °C
- 对流换热系数 \(h\) (W/(m²·K))
- 时间 (s/min)
- 热物理性质：比热容 \(c_i\)，密度 \(\rho_i\)，运动粘度 \(\nu\)

## Reusable Claims
- **渗透方向性效应**：在相同水力梯度下，垂直于流动方向的粗糙度越大，等效水力开度越小，渗流能力越低。此结论适用于单相层流条件，且裂隙开度受围压控制明显。［Huang 2019, pp. 6-7］
- **流动稳定性**：围压越高，裂隙闭合越充分，流动达到稳定所需的时间越短；入口压力对开度的增量影响随围压增加而减弱，提示深层EGS中注入压力对裂隙开度的贡献有限。［Huang 2019, pp. 6-7］
- **热提取速率**：高注水流量加速岩体降温并提取更多热量；相同的初始岩温下，低流量可维持较高岩温但整体采热率低。［Huang 2019, pp. 7-8］
- **出口温度线性关系**：在定流量条件下，出口流体温度与初始岩温近似呈线性正相关，高初始岩温可获得更高出口温度，对EGS产能评估有参考意义。［Huang 2019, pp. 8-9］
- **粗糙度方向对传热的相反影响**：垂直流向的大粗糙度（如JRC=18–20）通过诱发涡流增大有效换热面积，从而提高对流换热系数；平行流向的大粗糙度（如JRC=18–20）则因形成渗流优势通道而减小有效换热面积，降低换热效率。此结论揭示了裂隙形貌方向性在EGS设计中的双刃剑效应。［Huang 2019, pp. 8-10］
- **传热增强条件**：对流换热系数随流体流速和岩石温度的升高而近似线性增加，其机理为高流速和高温均导致边界层厚度减小。该趋势适用于蒸馏水在60–90 °C、5–20 ml/min的试验范围。［Huang 2019, pp. 9-10］

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[enhanced geothermal system (EGS)]]
- [[convective heat transfer coefficient]]
- [[equivalent hydraulic aperture]]
- [[fracture roughness directionality]]
- [[seepage dominant path]]
- [[cubic law]]
- [[Barton’s standard profiles]]
- [[channeling flow in fractures]]
- [[boundary layer theory in fractures]]
- [[effective heat transfer area]]
- [[3D printed rock fractures]]

## Candidate Methods
- [[Barton JRC profile replication via 3D printing]]
- [[artificial rock sample with cement mortar casting]]
- [[two-equation thermal model for fracture convection]]
- [[uncertainty analysis of convective heat transfer coefficient]]
- [[cubic law inversion for hydraulic aperture]]
- [[transient temperature monitoring by multiple PT1000 sensors]]
- [[radial conduction model for cylindrical specimen]]
- [[repeatable fracture manufacturing using digital templates]]

## Connections To Other Work
- **立方定律与粗糙度**：Lomize (1951) 提出粗糙度概念并建立平行板裂隙的立方定律，本研究通过等效水力开度将立方律应用于粗糙裂隙，验证其适用性。［Huang 2019, pp. 2］
- **岩体节理粗糙度表征**：Barton & Choubey (1977) 系统提出10条标准JRC剖面，ISRM推广应用；本研究直接采用JRC=10–12和18–20两种剖面，并与Mandelbrot (1983)的分形维度及Xie et al. (1993, 1994)的分形表征相关联。［Huang 2019, pp. 2］
- **粗糙裂隙对流换热实验**：与Bai et al. (2016, 2017) 在天然花岗岩裂隙中开展的对流换热试验一致，均采用中心点温度替代裂隙表面温度进行数据处理；与Zhang et al. (2017) 使用超临界CO₂的研究形成对比，后者也观察到了粗糙度引发的渗流优势通道。［Huang 2019, pp. 2, 5］
- **流动槽道效应**：Fox et al. (2015, 2016) 指出裂隙开度空间变异会减少有效换热面积并形成流动沟道，本研究发现平行流向的大粗糙度同样产生渗流优势路径，与其实质一致。［Huang 2019, pp. 2, 9–10］
- **应力-渗透关系**：Co et al. (2017) 基于DDM模型分析了不同应力条件下粗糙裂隙渗透率的演化，本研究实验结果显示围压与水力开度的相关性，支持其数值模拟结论。［Huang 2019, pp. 2］
- **裂隙网络模拟**：Watanabe et al. (2012, 2013) 发展GeoFlow模型预测三维裂隙网络流动，Ishibashi et al. (2012) 利用X射线CT开展裂隙流动可视化，均表明沟道流的重要性，本研究从粗糙度方向角度提供了单裂隙实验佐证。［Huang 2019, pp. 2］

## Open Questions
- 本实验仅测试两种JRC组合，粗糙度方向效应在其他级别（如JRC 4–6, 14–16）或分形裂隙中是否仍然成立？需要系统的参数化研究。
- 实验限于低围压（1 MPa）的对流换热测试，高围压（>15 MPa）下裂隙闭合如何影响对流换热系数的方向依赖性？目前仅靠渗流数据推测，缺乏直接测量。
- 工质仅为蒸馏水，未涉及超临界CO₂或含溶解质流体，多相流与相变条件下的方向性效应尚不明确。
- 人工水泥砂浆与真实花岗岩的热扩散系数、表面粗糙度微观特征不同，结论外推到实际HDR场址需更多验证。
- 单裂隙模型未考虑裂隙网络交叉流及热干扰，如何将此方向性机理扩展到裂隙网络尺度？
- 长时间循环下的矿物溶解/沉淀对粗糙度及优势通道的演化有何影响？文中未涉及。

## Source Coverage
本页面严格基于所提供的全部10个非空索引片段编译而成，未添加任何片段外的事实、作者或数据。索引片段覆盖比率为：按块数覆盖1.0，按字符数覆盖1.004677（源片段签名：ab788fd4d51d1cd58aab5b5ceb56cbb83628e876，编译源字符数47262，索引字符数47042）。所有证据均标注来源，符合full-index单次编译策略。
