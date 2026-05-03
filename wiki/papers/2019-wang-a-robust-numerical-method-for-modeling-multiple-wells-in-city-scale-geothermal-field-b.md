---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-wang-a-robust-numerical-method-for-modeling-multiple-wells-in-city-scale-geothermal-field-b"
title: "A Robust Numerical Method for Modeling Multiple Wells in City-Scale Geothermal Field Based on Simplified One-Dimensional Well Model."
status: "draft"
source_pdf: "data/papers/2019 - A robust numerical method for modeling multiple wells in city-scale geothermal field based on simplified one-dimensional well model基于简化一维井模型的城市尺度地热田多井建模的稳健数值方法。.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Wang, Guiling, et al. \"A Robust Numerical Method for Modeling Multiple Wells in City-Scale Geothermal Field Based on Simplified One-Dimensional Well Model.\" *Renewable Energy*, vol. 139, 2019, pp. 873-94. doi:10.1016/j.renene.2019.02.131."
indexed_texts: "12"
indexed_chars: "56786"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "57046"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004579"
coverage_status: "full-index"
source_signature: "94bdfe79ae2c249077843f082e6d0f40a2b67c0f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:33:35"
---

# A Robust Numerical Method for Modeling Multiple Wells in City-Scale Geothermal Field Based on Simplified One-Dimensional Well Model.

## One-line Summary
提出一种基于简化一维井模型的城市尺度地热田多井建模方法，通过等效传热系数考虑井筒套管与水泥环热阻，将三维井筒降维为线单元，大幅降低计算成本，并在北京城区地热田（39口井）的案例中揭示了多井效应、储层间相互作用及断层控制规律。

## Research Question
如何高效模拟包含数十口井的城市尺度地热田中的耦合流动与传热过程？传统模型因井筒（直径 ~dm）与储层（尺度 ~km）的尺度差异而需极细网格，且多数模型仅考虑单对井，难以反映多井长期运营下的真实热-水耦合行为。[Wang 2019, pp. 1-2; pp. 2-3]

## Study Area / Data
- **场地**：北京城区地热田，位于北京地堑东南边界与大兴隆起西北之间，为典型凹陷盆地。  
- **地质**：中-新元古界沉积盖层，下伏蓟县系白云岩，发育两组主要热储：浅部铁岭组（埋深578–1200 m）和深部雾迷山组（埋深517–2456 m），二者被洪水庄页岩隔开，浅部热储上覆下马岭页岩。地温梯度：铁岭组4.4–7.8 °C/100 m，雾迷山组2.8–3.0 °C/100 m。[Wang 2019, pp. 8-9]  
- **井系统**：共39口井，其中采水井31口，回灌井9口（表5）。[Wang 2019, pp. 9-10]  
- **历史动态**：自1970年代开采，1980年代后水位下降速率0.83–2.36 m/a；2000年代起实施回灌。[Wang 2019, pp. 8-9]  
- **模型范围**：水平面积11.6×8.5 km²，垂向从地表至深度2 km，包括9个地层、4条主要断层（水力开启）及全部井。[Wang 2019, pp. 9-10]  
- **参数来源**：储层和盖层参数来自文献 [33–35]，流体物性按温度依赖性公式（10）-（13）给定。[Wang 2019, pp. 10-12]

## Methods
1. **简化一维井模型**：将套管和水泥环的径向传热集总为一个等效传热系数 \((hZ)_{\rm eq}\)，该系数由井径、套管/水泥导热系数、流体物性及流速决定（式24–27），井内仅考虑轴向对流-导热及摩擦热，忽略径向温度变化。[Wang 2019, pp. 3-6]  
2. **储层模型**：全饱和刚性多孔介质，单相达西流（式1–3）和宏观能量守恒（式4–6）；断层采用切向达西律（式7–9）；流体密度、粘度、导热系数和比热容作为温度的函数（式10–13）。[Wang 2019, pp. 3-4; pp. 4-6]  
3. **井-储层耦合**：通过开孔段长度将质量通量分配给储层内部边界（式32），热通量由注入井底温度或采出井井底平均温度确定（式33–34）；初始条件为静水压力和稳态地温梯度（式29）；侧边界按1971–1979年动态资料试差校准。[Wang 2019, pp. 8-9; pp. 10-12]  
4. **数值实现**：基于有限元平台COMSOL，储层和盖层用四面体单元离散，井用一维线单元；时间积分采用向后欧拉格式，求解器为并行直接稀疏求解器。[Wang 2019, pp. 8-9]  
5. **基准验证**：设计单井系统对比全三维参考模型（储层573445单元、井141309单元，计算耗时3.83 h）和简化模型（精细网格0.67 h，节省83%计算时间），监测点温度曲线吻合良好。[Wang 2019, pp. 6-8; Table 3]  
6. **北京案例**：按图6计算流程，采用不同注采比方案（0.26和1.0）模拟50年运行，评估温度突破时间。[Wang 2019, pp. 10-16]

## Key Findings
- **计算效率提升**：基准算例中，简化模型在维持精度的前提下，将单井计算时间从3.83 h降至0.67 h，节省约83%。[Wang 2019, pp. 6-8]  
- **多井效应显著**：高注采比（1.0）和长期运行下，同一回灌井周边的多口采水井均可能受到冷却前锋的影响，传统井对模型不足以描述此类多井相互作用。[Wang 2019, pp. 12-16]  
- **热突破时间**：  
  - 注采比0.26时，雾迷山组29号井（8.8 a）、35号井（22.5 a）发生热突破；铁岭组31号井（23.3 a）。  
  - 注采比1.0时，雾迷山组29号井（2.1 a）、35号井（8.0 a）、5号井（14.8 a）；铁岭组除27号井外全部突破。[Wang 2019, pp. 12-16]  
- **储层间相互作用**：当厚层盖岩非渗透时，深部回灌井（R1）在50年内未影响浅部采水井（30号井）的温度，亦未维持浅部储层压力。[Wang 2019, pp. 16-21]  
- **断层作用**：断层为快速水流通道，跨断层回灌井（T4）附近温度下降明显，跨断层采水井（22号井）温度因热水补给而缓升。[Wang 2019, pp. 16-21]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 简化一维井模型与全三维参考模型温度曲线一致，计算时间减少83% | [Wang 2019, pp. 6-8] | 单井系统，层流，忽略粗糙度； i7-4790K, 16 GB | 网格敏感性分析表明精细网格方案即可满足精度 |
| 注采比0.26时，雾迷山组29、35号井热突破时间分别为8.8 a、22.5 a；铁岭组31号井23.3 a | [Wang 2019, pp. 12-16] | 恒定注入水温20 °C，回灌量192.6 m³/h（部分井） | 回灌井G周边的多口采水井未突破 |
| 注采比1.0时，29号井2.1 a、35号井8.0 a、5号井14.8 a热突破；铁岭组除27号井外全部突破 | [Wang 2019, pp. 12-16] | 回灌率提升2.875倍 | 多井效应更突出 |
| 回灌井R1（雾迷山组）与采水井30（铁岭组）在50年内无温度干扰 | [Wang 2019, pp. 16-21] | 盖层非渗透，仅热传导 | 压力也未受影响 |
| 跨断层回灌井T4导致断层附近温度快速下降，跨断层采水井22温度随时间缓升 | [Wang 2019, pp. 16-21] | 断层渗透率4.93×10⁻⁷ m²，厚度10 cm | 断层为快通道 |

## Limitations
- 模型仅考虑单相流和完全饱和条件，未包含气-液两相或非饱和效应。[Wang 2019, pp. 3-4]  
- 机械（M）和化学（C）过程未耦合，不能反映注入诱导的应力变化或结垢/溶蚀。[Wang 2019, pp. 16-21 (Discussion)]  
- 基准算例假设层流及光滑壁面，未涵盖紊流高粗糙度情形。[Wang 2019, pp. 6-8]  
- 北京案例中部分储盖参数取自文献，初始和边界条件为简化设定，且未考虑深部热水通过断层的上涌。[Wang 2019, pp. 10-12]  
- 未涉及长期运营中岩石变形或孔渗演化。[Wang 2019, pp. 16-21 (Comparison with other models)]

## Assumptions / Conditions
- 储层岩石刚性、全饱和，达西流动有效；流体密度、粘度等随温度变化的经验公式（10–13）适用。[Wang 2019, pp. 3-4]  
- 井内温度仅沿轴向变化，周向均匀，套管-水泥环各界面温度连续且相同。[Wang 2019, pp. 4-6]  
- 等效传热系数基于热稳态假设推导，膜传热系数用Nusselt数关联式（层流3.66，紊流用Gnielinski式27）。[Wang 2019, pp. 4-6]  
- 初始地温场符合测井地温梯度，侧向边界水头通过1971–1979年动态试差校准后被恒定。[Wang 2019, pp. 10-12]  
- 断层用切向达西律描述，忽略法向渗透性变化。[Wang 2019, pp. 3-4]

## Key Variables / Parameters
| Variable | Description | Source |
|----------|-------------|--------|
| \(q\) | 单井注/采量（m³/h） | [Wang 2019, Table 6] |
| \(T_{\rm in}\) | 回灌水温（°C） | [Wang 2019, Table 4,6] |
| \(k, \phi\) | 储层渗透率、孔隙度 | [Wang 2019, Table 6] |
| \((hZ)_{\rm eq}\) | 等效传热系数，含井径、套管/水泥导热系数及膜系数 | [Wang 2019, Eq. 25] |
| \(k_f, C_{p,f}, \rho_f, \mu\) | 流体物性（温度函数） | [Wang 2019, Eqs. 10–13] |
| \(d_h, e/d_h\) | 水力直径和相对粗糙度 | [Wang 2019, Eq. 16–17] |
| \(l_{\rm open}\) | 井筒裸眼段长度 | [Wang 2019, Eq. 32, Table 5] |
| 地温梯度 | 铁岭组4.4–7.8 °C/100 m，雾迷山组2.8–3.0 °C/100 m | [Wang 2019, pp. 8-9] |
| 注采比 | 方案Ⅰ 0.26，方案Ⅱ 1.0 | [Wang 2019, pp. 12] |

## Reusable Claims
- 基于等效传热系数的简化一维井模型可在不损失精度的前提下，将城市尺度地热田的多井模拟计算时间降低约一个数量级。[Wang 2019, pp. 6-8]  
- 多井系统在长期高回灌量运行下，回灌井周围的采水井群可能同时受到热突破影响，单井对模型无法捕捉此类多井效应。[Wang 2019, pp. 12-16]  
- 储层间若被厚层非渗透盖岩分隔，深部回灌对浅部采水温度与压力几乎无影响；断层则成为加速热量传递的优势通道。[Wang 2019, pp. 16-21]  
- 热突破时间受井位、井深和注采比的显著控制，合理优化井网参数可延缓热突破。[Wang 2019, pp. 16-21 (Conclusions)]

## Candidate Concepts
- [[simplified one-dimensional well model]]  
- [[equivalent heat transfer coefficient]]  
- [[scale disparity]]  
- [[thermal breakthrough]]  
- [[injection-production ratio]]  
- [[multiple wells effects]]  
- [[fracture reservoir]]  
- [[Darcy’s law]]  
- [[fault-controlled heat transfer]]  
- [[cap rock insulation]]

## Candidate Methods
- [[finite element method (COMSOL)]]  
- [[Darcy flow simulation]]  
- [[convection-conduction equation]]  
- [[Haaland friction factor]]  
- [[Nusselt number correlation (Gnielinski)]]  
- [[backward Euler time integration]]  
- [[parallel direct sparse solver]]  
- [[coupled well-reservoir mass and heat transfer]]  
- [[steady-state initialization with trial-and-error calibration]]

## Connections To Other Work
- 与传统耦合THM过程的数值模型（如TOUGH2、OpenGeoSys、COMSOL）相比，本方法的优势在于可高效处理数十口井的大尺度系统，而以往模型通常不超过10口井，且多限于双井系统 [Wang 2019, pp. 2-3, Table 1]。  
- 井筒模型继承了Al-Khoury等人（2005, 2006）的伪三维到一维的降维思想，并进一步通过等效传热系数计入套管和水泥环的热阻 [Wang 2019, pp. 4-6]。  
- 基准模型与Saeid等（2013）的单个双井系统相似，但本文验证的是单一井筒简化，且扩展到39井的实际场地 [Wang 2019, pp. 6-8]。  
- 北京地热田的先前研究（如Yang et al., 1986; Kearey & Wei, 1993）提供了地质概况和初期动态，本文在此基础上建立了更精细的数值模型 [Wang 2019, pp. 8-9]。

## Open Questions
- 若在模型中耦合岩石变形和化学过程，多井系统的长期响应（如渗透率演化、热突破加速）将如何变化？[Wang 2019, pp. 16-21 (Comparison with other models)]  
- 在更复杂的流动状态（紊流、高气水比）下，等效传热系数的适用性是否需要修正？[Wang 2019, pp. 6-8]  
- 如何利用本模型反演实际地热田的注采方案以达到“零热突破”或“延迟热突破”的目标？  
- 当断层兼具流体输移和应力传递双重作用时，多井系统与断层的相互作用机制尚未明确。  
- 模型中未被考虑的深部热水通过断层上涌的效应是否会在更长的时间尺度上显著改变储层温度场？[Wang 2019, pp. 10-12 (Assumptions)]

## Source Coverage
本文档基于 Wang 等 (2019) 论文的全部 12 个非空索引片段编译而成。源文本块覆盖率（coverage_ratio_by_blocks）为 1.0，字符覆盖率（coverage_ratio_by_chars）为 1.004579（因少量格式转换导致的字符略多）。编译策略为单次通过 Markdown 组装，所有事实性陈述均附有对应的源标签，未编造作者、页码、数据或结论。
