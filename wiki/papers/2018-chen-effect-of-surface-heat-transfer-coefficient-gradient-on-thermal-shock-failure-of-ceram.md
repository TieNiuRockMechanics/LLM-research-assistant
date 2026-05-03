---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-chen-effect-of-surface-heat-transfer-coefficient-gradient-on-thermal-shock-failure-of-ceram"
title: "Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition."
status: "draft"
source_pdf: "data/papers/2018 - Effect of surface heat transfer coefficient gradient on thermal shock failure of ceramic materials under rapid cooling condition.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Chen, Limin, et al. \"Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition.\" *Ceramics International*, 2018, doi:10.1016/j.ceramint.2018.02.100."
indexed_texts: "9"
indexed_chars: "40291"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "40477"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004616"
coverage_status: "full-index"
source_signature: "acf267e1d2acafeb0c888e34ccf5627a76a385e0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:27:32"
---

# Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition.

## One-line Summary
本研究通过快速热处理（RTP）装置与水淬、沸腾水淬及聚合物水溶液淬冷对比，系统揭示了表面换热系数（h）梯度在 ZrB₂–SiC–石墨（ZSG）陶瓷热震失效中的关键作用，证明热震损伤由体温度梯度与表面 h 梯度联合产生，并给出了各淬冷介质对应的临界瞬时冷却速率 V(max)₍c₍（水淬约 270 °C s⁻¹，聚合物淬冷约 500 °C s⁻¹，沸腾水淬 >600 °C s⁻¹）。

## Research Question
在快速冷却条件下，表面换热系数梯度如何影响陶瓷材料的热震失效？其与体温度梯度共同导致热震损伤的机制是什么？

## Study Area / Data
- 材料：热压烧结 ZrB₂ + 20 vol% SiC + 15 vol% 石墨（ZSG）复合材料，切割为 3 mm × 4 mm × 36 mm 矩形条。试样表面抛光至 1 µm，棱边倒角。  
- 冷却介质与装置：  
  - 水浴（20 °C）直接淬冷；沸腾水浴（100 °C）直接淬冷；聚合物水溶液淬冷参考前期工作 [Chen 2018, pp. 1-2]。  
  - 快速热处理（RTP，Annealsys AS‑One 100）装置，采用辐射加热与快速冷却套件，实现间接接触冷却（试样与不锈钢水冷床板接触，无表面 h 梯度）。  
- 热震温度范围：水淬 300~450 °C [Chen 2018, pp. 2-2]；沸腾水淬 400~750 °C [Chen 2018, pp. 2-2]；RTP 条件 ΔT 可达 1000 °C [Chen 2018, pp. 4-4]。  

## Methods
- **残余强度测试**：淬冷后三点弯曲，跨距 30 mm，加载速率 0.5 mm min⁻¹，至少三根试样取均值，以室温强度的 70% 定义临界值 (ΔT₍c₍, V(max)₍c₍) [Chen 2018, pp. 2-2]。  
- **实时温度采集**：试样 3 mm × 4 mm 面中心加工小坑，匹配 K 型热电偶并用细铜丝绑紧，淬入介质时实时记录温度，获得瞬时冷却速率 V 及其最大值 V(max) [Chen 2018, pp. 2-3]。  
- **微观表征**：SEM 观察表面和断口形貌；XRD 分析淬冷前后物相演变 [Chen 2018, pp. 4-4]。  
- **有限元模拟**：ANSYS16.0 三维瞬态对流模型，假设无限平板，采用轴对称四分之一模型，赋予弹性模量 450 GPa、泊松比 0.12，设定不同介质的热热系数（水 130 kW m⁻² K⁻¹，蒸汽泡膜 50 W m⁻² K⁻¹，聚合物膜 10 kW m⁻² K⁻¹，沸腾水 20 kW m⁻² K⁻¹），计算温度场和热应力场 [Chen 2018, pp. 6-7]。

## Key Findings
1. **表面 h 梯度决定热震损伤的严重程度**：  
   - 间接接触 RTP 冷却无表面 h 梯度，即使 ΔT = 1000 °C 试样强度无明显下降；而直接水淬引入巨大表面 h 梯度，导致强度急剧退化 [Chen 2018, pp. 4-4]。  
   - 水淬时随机成核气泡造成表面 h 梯度极大，V(max)₍c₍ ≈ 276 °C s⁻¹；通过改变水量验证得到 V(max)₍c₍ ≈ 271 °C s⁻¹，两者一致 [Chen 2018, pp. 4-5]。  
   - 聚合物淬冷剂中高分子链降低气泡随机性，界面聚合物膜提供相对均匀的换热，V(max)₍c₍ 提高至 ≈ 500 °C s⁻¹ [Chen 2018, pp. 5-5]。  
   - 沸腾水淬冷无气相膜形成，不存在表面 h 梯度，即使 V(max) 约 600 °C s⁻¹ 强度仍不下降，即 V(max)₍c₍ > 600 °C s⁻¹ [Chen 2018, pp. 5-5]。  

2. **失效机制为体温度梯度与表面温度梯度的联合作用**：  
   - 热震损伤源于体温度梯度产生的热应力 (f₂) 与表面 h 梯度产生的热应力 (f₁) 的叠加，当合成热应力超过材料固有强度时发生失效 [Chen 2018, pp. 5-5, 6-6]。  
   - FEA 结果显示三种淬冷条件下均存在两种温度梯度和对应的两类热应力 [Chen 2018, pp. 6-7]。  

3. **实际服役相关性**：  
   - 沸腾水淬代表单相传热环境（如晴朗天气），UHTCs 可能仅承受体温度梯度，性能保持良好；聚合物淬冷代表多相传热环境（如雨、雪、沙尘、盐雾），会同时承受两类热应力，性能可能严重退化 [Chen 2018, pp. 7-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水淬临界温度差 ΔT₍c₍ = 306 °C，对应 V(max)₍c₍ ≈ 276 °C s⁻¹ | [Chen 2018, pp. 4-4, 5-5] | 水浴 20 °C，试样从 300‑450 °C 淬入；水体积充足，标准 ASTM C1525 准则 | 传统水淬方法，获得 70% 残余强度的临界值 |
| 固定水温、改变水量，400 °C 恒温条件下 V(max)₍c₍ ≈ 271 °C s⁻¹ | [Chen 2018, pp. 4-5] | 试样加热至 400 °C，淬入不同体积水 | 与传统水淬实验吻合，确认水淬临界冷却速率常数 |
| RTP 间接接触冷却，ΔT 达 1000 °C 残余强度基本不变 | [Chen 2018, pp. 4-4] | 辐射加热，样品与冷水床板接触冷却；空气气氛 | 无表面 h 梯度，强度保持 |
| 聚合物水溶液淬冷 V(max)₍c₍ ≈ 500 °C s⁻¹ (前期工作) | [Chen 2018, pp. 5-5] | 淬冷剂中加入聚合物 | 较水淬 V(max)₍c₍ 显著提高 |
| 沸腾水淬 V(max) 约 600 °C s⁻¹ 时残余强度无下降，V(max)₍c₍ > 600 °C s⁻¹ | [Chen 2018, pp. 5-5] | 淬入 100 °C 沸腾水 | 无气相膜，无表面 h 梯度 |
| 水淬试样表面因气泡随机成核形成巨大的表面 h 梯度；聚合物界面膜减小该梯度 | [Chen 2018, pp. 5-5] | 示意图 Fig. 8，基于传热机制分析 | h₁ < h₃ < h₂，对应蒸汽膜、聚合物膜、水 |
| FEA 模拟揭示水淬、聚合物淬、沸腾水淬中均存在体温度梯度和表面温度梯度及对应的两类热应力 | [Chen 2018, pp. 6-7] | 弹性模量 450 GPa，泊松比 0.12，设定热热系数，热震时间 0.01 s | 模拟结果与实验结果定性一致 |

## Limitations
- 试验条件不能完全复现实际高超音速飞行中的极端气动加热/冷却，所得结论仅为热震行为提供补充性认识 [Chen 2018, pp. 2-2]。  
- FEA 模拟采用无限平板假设和各向同性线弹性本构，未考虑微裂纹萌生、扩展等真实损伤过程；热热系数为定常假定，气泡分布随机设定，与实际动态过程有差异 [Chen 2018, pp. 6-7]。  
- 仅研究单一 ZSG 复合材料体系，未涵盖其他 UHTCs 或不同组分；试样尺寸固定，尺寸效应未探讨。  

## Assumptions / Conditions
- 淬冷前试样在炉中保温至少 3 min，确保无温度梯度；淬冷后 100 °C 烘干 1 h 后冷却再测强度 [Chen 2018, pp. 2-2]。  
- V(max) 定义为淬冷瞬间温度-时间微分的绝对值最大值，V(max)₍c₍ 为残余强度降至室温强度 70% 时对应的 V(max) [Chen 2018, pp. 3-4, 4-4]。  
- FEA 假设：仅考虑对流换热边界，忽略辐射；热震时间 0.01 s；材料弹性模量 450 GPa、泊松比 0.12；热热系数分别为：水 130 kW m⁻² K⁻¹、蒸汽泡膜 50 W m⁻² K⁻¹、聚合物膜 10 kW m⁻² K⁻¹、沸腾水 20 kW m⁻² K⁻¹ [Chen 2018, pp. 6-7]。  
- RTP 实验在常压空气下进行，因腔体密封有限氧气，高温下氧化极轻微，试样表面状态几乎不变 [Chen 2018, pp. 4-4]。  

## Key Variables / Parameters
- `V(max)` — 最大瞬时冷却速率，即温度‑时间曲线在淬冷瞬间的斜率绝对值最大值（°C s⁻¹）  
- `V(max)₍c₍` — 临界瞬时冷却速率，残余弯曲强度降至初始强度 70% 时对应的 V(max)  
- `ΔT` — 加热温度与淬冷介质温度之差  
- `ΔT₍c₍` — 临界温度差，70% 强度保留时的 ΔT  
- `h` (表面换热系数) — 单位温差、单位时间、单位面积传递的热量（W m⁻² K⁻¹）  
- `表面 h 梯度` — 热热系数的空间分布不均匀性，主要由淬冷介质相变（气泡、聚合物膜）引起  
- `体温度梯度` — 试样内部的温度不均匀性，由瞬时冷却速率 V 决定  

## Reusable Claims
1. **对于 ZrB₂–SiC–石墨复合材料，水淬（20 °C）条件下的临界表面冷却速率约为 270 °C s⁻¹**。该值由两种实验方案（变加热温度和变淬冷水量）交叉验证，在水体积足够、试样尺寸 3 × 4 × 36 mm 的条件下成立 [Chen 2018, pp. 4-5]。  
2. **消除表面 h 梯度可大幅提高材料的抗热震能力**。在 RTP 间接接触冷却或无相变的沸腾水淬中，试样仅承受体温度梯度，即使冷却速率超过 600 °C s⁻¹ 或温差达 1000 °C，仍能保持原始强度 [Chen 2018, pp. 4-4, 5-5]。  
3. **通过在水基淬冷剂中引入聚合物链，可降低气泡成核的随机性，形成界面聚合物膜，使表面 h 梯度减小，从而将临界冷却速率提高至 ~500 °C s⁻¹**。这一结论基于与纯水淬的直接对比 [Chen 2018, pp. 5-5]。  
4. **热震损伤是体温度梯度引起的热应力与表面 h 梯度引起的热应力耦合作用的结果**，当两者叠加产生的瞬态热应力超过材料强度时即发生强度退化。该机制同时得到实验与有限元模拟的支撑 [Chen 2018, pp. 5-5, 6-7]。  
5. **在评估 UHTCs 的实际服役性能时，水淬试验因引入过大的表面 h 梯度而过分严重，其结论的工程参考价值有限；沸腾水淬（单相传热）和聚合物淬冷（多相传热）分别模拟晴朗与雨/雪/沙尘等天气，能更合理地反映实际热震行为** [Chen 2018, pp. 7-7]。  

## Candidate Concepts
- [[表面换热系数梯度 (surface h gradient)]]  
- [[体温度梯度 (body temperature gradient)]]  
- [[临界冷却速率 (V(max)c)]]  
- [[热震抗力 (thermal shock resistance)]]  
- [[快速热处理装置 (RTP) 间接接触冷却]]  
- [[沸腾传热与气泡成核]]  
- [[蒸汽泡膜 (steam bubble film)]]  
- [[聚合物淬冷介质]]  
- [[多相传热与单相传热]]  
- [[组合热应力 (combined thermal stress)]]  
- [[ZrB2‑SiC‑石墨复合材料]]  
- [[残余强度保留率]]  
- [[微裂纹主导的热震失效]]  

## Candidate Methods
- [[水淬试验 (water quenching)]]  
- [[沸腾水淬试验 (boiling water quenching)]]  
- [[聚合物溶液淬冷法]]  
- [[RTP 间接接触冷却技术]]  
- [[实时温度采集 (thermocouple) 获得冷却曲线]]  
- [[三点弯曲残余强度测试]]  
- [[热震损伤的有限元瞬态热‑力耦合分析]]  
- [[X 射线衍射 (XRD) 表面物相鉴定]]  
- [[扫描电镜 (SEM) 观察表面与断口微裂纹]]  
- [[基于 ASTM C1525 标准的热震评价程序]]  

## Connections To Other Work
- **Hasselman 的热应力损伤理论** [30]：该研究观察到残余强度在临界条件附近急剧下降，符合 Hasselman 关于脆性陶瓷热震的典型特征 [Chen 2018, pp. 4-4]。  
- **团队前期的聚合物淬冷剂工作** [27]：本文的 V(max)₍c₍ ≈ 500 °C s⁻¹ 即引自该前期研究，并进一步比较了水、聚合物、沸腾水的热震行为 [Chen 2018, pp. 5-5]。  
- **其他淬冷介质的对比** [24]：文献报道 ZrB₂‑SiC 在沸水、空气、甲基硅油中强度几乎不变，本文通过 RTP 实验再次证明无表面 h 梯度时强度可保持 [Chen 2018, pp. 4-4, 8-8]。  
- **SiC 晶须增强硼化物陶瓷的热震行为** [23]：其中采用沸水淬冷以避免气相膜，本文借鉴其思路并定量关联 V(max)₍c₍ [Chen 2018, pp. 8-8]。  
- **淬冷过程中热传递变量的影响** [31-33]：本文承认表面 h 随试样温度和表面状态变化，但指出平均效应仍然导致恒定的临界冷却速率 [Chen 2018, pp. 5-5]。  
- **ASTM C1525 标准** [25]：本研究依据该标准确定临界温差和临界冷却速率 [Chen 2018, pp. 2-2]。

## Open Questions
- 实验室水淬或聚合物淬冷产生的不均匀气/液相分布与真实高速飞行中激波、边界层转捩等导致的热梯度之间有何定量映射关系？ [Chen 2018, pp. 7-7]  
- 材料固有的微观结构（如石墨片层取向、SiC 分布、气孔等）如何影响表面 h 梯度的形成及其诱发的微裂纹扩展路径？文中仅强调表面微裂纹主导失效，但未深入讨论微观结构参数 [Chen 2018, pp. 4-4]。  
- 是否存在一个统一的、考虑表面 h 梯度与体温度梯度耦合的无量纲热震损伤准则？目前的有限元模拟仅提供了现象学解释，未给出可推广的理论判据 [Chen 2018, pp. 6-7]。  
- 在实际多相传热环境下（雨滴、沙粒撞击），瞬态热应力和机械冲蚀的耦合效应如何？文中虽将聚合物淬冷比作多相天气，但尚未对同时存在的机械效应进行评价。  

## Source Coverage
所有 9 个非空索引片段均已被处理，覆盖全文第 1 至 8 页。片段索引字符数：40,291；编译后的源字符数：40,477。区块覆盖率 1.0，字符覆盖率 1.004616。所有引用均基于已提供片段，未添加任何外部信息。
