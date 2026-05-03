---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-xu-influence-of-stress-and-high-temperature-treatment-on-the-permeability-evolution-behavio"
title: "Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone."
status: "draft"
source_pdf: "data/papers/2019 - Influence of stress and high-temperature treatment on the permeability evolution behavior of sandstone.pdf"
collections:
  - "zotero new"
citation: "Xu, Peng, and Sheng-Qi Yang. \"Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone.\" *Acta Mechanica Sinica*, vol. 35, no. 2, 2019, pp. 419-32. doi:10.1007/s10409-018-0824-6."
indexed_texts: "11"
indexed_chars: "52689"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52890"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003815"
coverage_status: "full-index"
source_signature: "fcb61e97a90b4727799905548ef329e947a68302"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T00:39:07"
---

# Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone.

## One-line Summary
红砂岩在三轴压缩条件下经历高温处理后渗透率的指数演化规律和一种简化双孔隙结构模型。

## Research Question
分析有效应力和高温处理对致密红砂岩渗透率演化的影响，尤其是在三轴压缩弹性阶段，不同温度处理后渗透率随静水压力和偏应力变化的定量规律 [Xu 2019, pp. 1-2, 2-2, 5-7]。

## Study Area / Data
- **材料**：山东产红砂岩，矿物成分为长石、石英、岩屑和胶结物 [Xu 2019, pp. 2-3]，试样为 φ50 mm × 100 mm 圆柱体，表面无明显裂纹 [Xu 2019, pp. 2-3]。
- **温度处理**：20 °C、200 °C、400 °C、500 °C、600 °C、700 °C、800 °C、900 °C，升温速率 5 °C/min，恒温 2 h 后冷却至室温 [Xu 2019, pp. 2-3]。
- **渗透试验**：冷却后采用稳态气体（纯氮）流动法，测试不同气体压力、静水应力、常围压、常轴压及偏应力条件下的气体质量流量 [Xu 2019, pp. 2-3, 3-5]。

## Methods
- **渗透率测量**：基于达西定律的稳态气体流动法，利用公式 \( K = \frac{2\mu L P_a Q}{A (P_1^2 - P_a^2)} \) 计算渗透系数（式中 \( \mu \) 为氮气动力粘度，\( L \)、\( A \) 为试样长度和截面积，\( P_1 \) 为上游压力，\( P_a \) 为大气压，\( Q \) 为下游气体质量流量）[Xu 2019, pp. 2-3]。气体压力系统提供 0–3 MPa 或 0–40 MPa 压力，三轴压力室最大 60 MPa [Xu 2019, pp. 2-3]。
- **加载方式**：三种路径——围压恒定增轴压、轴压恒定增围压、静水压缩（轴压和围压等速率增加），均在弹性压缩范围内 [Xu 2019, pp. 5-7]。
- **微观观测**：热处理前后采用光学显微镜、SEM 以及 CT 扫描技术观察微结构 [Xu 2019, pp. 3-5, 11-13]。
- **模型构建**：提出简化双孔隙结构模型，将岩石分为裂隙基质和微孔基质，裂隙渗透系数远大于微孔，裂隙视为主要渗流通道；模型基于 Louis 经验公式 [33] 修正三轴变形关系，推导出常规三轴压缩下的渗透率表达式（式 (12)）和静水压缩下的简化式（式 (13)）[Xu 2019, pp. 7-8]。

## Key Findings
1. 热处理后试样质量随温度升高而下降；400 °C 时侧面出现剥落损伤，500 °C 时出现拉伸裂缝，700 °C 时剥落与裂缝贯通 [Xu 2019, pp. 3-5]。
2. 渗透系数与温度呈指数关系：\( K = 3.40 \times 10^{-19} \exp(0.006T) \) （T 为 °C，静水应力约 30–40 MPa，R²=0.94）；温度从 20 °C 升至 800 °C，渗透系数增大两个数量级，约为初始值的 100 倍 [Xu 2019, pp. 3-5]。
3. 围压对渗透率的影响大于轴压（0–60 MPa 范围）；以 20 °C 为例，围压从 10.19 MPa 升至 49.95 MPa 时，渗透系数从 \(1.68\times10^{-18}\) m² 急剧降至 \(6.34\times10^{-19}\) m² [Xu 2019, pp. 5-7]。
4. 静水压缩下渗透系数随体积应力近似指数衰减，由式 (13) 拟合良好；初始渗透率（零外载）和极限渗透率（高压下不变化）均随温度指数增长，极限渗透率拟合为 \( K = 1.52 \times 10^{-19} \exp(0.0075T) \) [Xu 2019, pp. 8-10]。
5. 偏应力（σₐ‑σc）对渗透率影响显著：当轴压大于围压时，渗透率随偏应力增加而明显升高；当轴压小于围压时，渗透率先降后缓升，渗透率最低点并非发生在静水压缩点（σₐ=σc），而是当 σₐ‑σc ≈ −26 MPa 时 [Xu 2019, pp. 10-11]。
6. 参数 αₘ（反映裂隙体积变形特性）随温度先升后降，700 °C 时体模量达到最小，与 Wu 等 [35] 的体模量变化趋势一致 [Xu 2019, pp. 8-10]。
7. 双孔隙模型（式 (12)）在 800 °C 和 900 °C 条件下与实验数据吻合较好，可用于预测弹性三轴压缩下热处理砂岩的渗透率 [Xu 2019, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 质量随温度降低，200 °C 下降最快，700 °C 以上再次陡降；400 °C 出现表面剥落，500 °C 出现拉伸裂缝，700 °C 剥落与裂缝连接 | [Xu 2019, pp. 3-5] | 升温速率 5 °C/min，恒温 2 h，自然冷却后观测 | 水逸出和矿物变化是主要原因 |
| 渗透系数与温度的关系：\( K = 3.40\times10^{-19} \exp(0.006T) \) (m²)，T 单位 °C，R²=0.94 | [Xu 2019, pp. 3-5] | 静水应力约 30–40 MPa，气体压力变化 | 适用于 20–800 °C 处理后的红砂岩 |
| 20 °C 时，围压 10.19 MPa→49.95 MPa，渗透系数 \(1.68\times10^{-18} \rightarrow 6.34\times10^{-19}\) m² | [Xu 2019, pp. 5-7] | 轴压恒定 15 MPa | 围压影响大于轴压 |
| 静水压缩下渗透率-体积应力指数拟合参数示例：800 °C 时 \( K = [7.87\exp(-0.11\sigma_m)+1.10]\times10^{-17} \)，R²=0.99 | [Xu 2019, pp. 8-10] | Sᵢⱼ=0, σₘ 0–50 MPa | 其他温度类似拟合 |
| 初始渗透率 \( K = 5.56\times10^{-19}\exp(0.009T) \)；极限渗透率 \( K = 1.52\times10^{-19}\exp(0.0075T) \) (m²) | [Xu 2019, pp. 8-10] | 弹性压缩，静水应力从零增至高压 | 外推至零外载和无穷大体应力 |
| 参数 αₘ 变化：20 °C 至 700 °C 上升，700 °C 后急剧下降，表明体模量在 700 °C 最小 | [Xu 2019, pp. 8-10, 13-14] | 与 Wu 等 [35] 体模量数据对比，趋势一致，最低值温度略差（700 °C vs 800 °C） | 石英相变和长石熔融等可能机制 [Xu 2019, pp. 13-14] |
| 800 °C 下，σₐ‑σc = 0 并非渗透率最低点，最低点出现在 σₐ‑σc ≈ −26 MPa | [Xu 2019, pp. 10-11] | 体积应力∼25 MPa，气体压力恒定 | 900 °C 结果类似 |
| 800 °C SEM 观察：微孔隙和微裂纹数量与尺寸明显增加，矿物颗粒松散多孔 | [Xu 2019, pp. 11-13] | 对比 200 °C，颗粒间结构变得疏松 | 温度 200→800 °C 晶界明显，连通性增强 |

## Limitations
- 三轴试验设备最大轴压和围压 60 MPa，低于红砂岩单轴抗压强度，因此仅能在弹性压缩范围内进行试验，不涉及塑性或破坏阶段 [Xu 2019, pp. 2-2, 5-7]。
- 渗透率测量采用稳态气体法，适用于渗透率大于 \(10^{-25}\) m² 的岩石；若渗透率过低则测量时间过长导致误差 [Xu 2019, pp. 2-3]。
- 高温处理为事后冷却测试，非原位高温高压同步测量；冷却过程可能改变部分热开裂结构 [Xu 2019, pp. 2-2]。
- 双孔隙模型假设裂隙基质的渗透率远大于微孔基质，且微孔基质孔隙度在弹性压缩中不变，这与实际情况可能存在偏差 [Xu 2019, pp. 7-8]。
- 模型参数（α₁, α₃, αₘ）虽然由拟合获得，但物理意义未经过独立实验标定 [Xu 2019, pp. 8-10]。
- 试验仅针对一种红砂岩，结论向其他岩性的推广需谨慎。

## Assumptions / Conditions
- 气体渗流为层流，满足达西定律；渗透系数与流体压力关系不大 [Xu 2019, pp. 7-8]。
- 等温渗流条件；气体压缩因子 Z 和动力粘度 μ 在室温下近似恒定 [Xu 2019, pp. 7-8]。
- 岩石可简化为由裂隙基质和微孔基质组成的双孔隙结构；微孔基质孔隙度在弹性压缩阶段保持不变，变形主要由裂隙基质贡献 [Xu 2019, pp. 7-8]。
- 采用修正的 Louis 经验公式描述单裂隙法向变形，推广到三轴应力下裂隙体积变形 [Xu 2019, pp. 7-8]。
- 试验中所有压缩阶段岩石处于弹性状态，未产生新的损伤 [Xu 2019, pp. 5-7]。
- 渗透系数由下游稳定质量流量计算，当相邻两次记录差异小于 2% 时视为稳定 [Xu 2019, pp. 2-3]。

## Key Variables / Parameters
- **T**：热处理温度（°C），范围 20–900 °C。
- **K**：渗透系数（m²）。
- **σₐ**, **σc**：轴压、围压（MPa）。
- **σₘ**：体积应力，σₘ = (σₐ + 2σc)/3。
- **Sᵢⱼ**：偏应力张量；常规三轴下为 σₐ‑σc。
- **αₘ**：描述裂隙体积变形特性的模型参数（MPa⁻¹），与体模量负相关。
- **α₁, α₃**：偏应力变形模型参数（MPa⁻¹）。
- **Kₐ₀**, **Kb₀**：双孔隙模型中裂隙基质和微孔基质的初始渗透系数。
- **φₐ₀**, **φb₀**：裂隙基质和微孔基质的初始孔隙度。
- **δₘₐₓ**, **α**（Louis 公式）：裂隙最大法向变形和相关变形模量参数 [Xu 2019, pp. 7-8]。

## Reusable Claims
- 对于红砂岩，在弹性压缩和稳态气体流动条件下，热处理后渗透系数与温度呈指数关系：\( K = 3.40 \times 10^{-19} \exp(0.006T) \) m²，静水应力约 30–40 MPa [Xu 2019, pp. 3-5]。**条件**：适用于 20–800 °C 处理、冷却后测试，且试样未发生塑性破坏。
- 在弹性范围内，围压增加比轴压增加更能降低红砂岩的渗透系数 [Xu 2019, pp. 5-7]。**条件**：应力水平 0–60 MPa，温度范围 20–700 °C。
- 简化的双孔隙结构模型（式 (12)、式 (13)）能够描述弹性三轴压缩下热处理砂岩的渗透率演化 [Xu 2019, pp. 7-8, 8-10, 10-11]。**适用条件**：裂隙渗流主导，微孔基质孔隙度变化可忽略；模型参数可由静水压缩和常体积应力变偏应力试验拟合得到。
- 红砂岩体模量随热处理温度先降低后升高，在约 700 °C 达到最低值，与 αₘ 趋势一致，可能与石英相变和长石熔融有关 [Xu 2019, pp. 8-10, 13-14]。**条件**：温度范围 20–900 °C，升温速率 5 °C/min，恒温 2 h。
- 偏应力为零（静水压缩）并非渗透率最低状态；当围压大于轴压一定值（如 σₐ‑σc ≈ −26 MPa）时渗透率更低 [Xu 2019, pp. 10-11]。**条件**：热处理温度 800 °C 和 900 °C，体积应力约 25 MPa。

## Candidate Concepts
- [[permeability evolution of sandstone]]
- [[thermal treatment effect on rock]]
- [[double-pore texture model]]
- [[fracture reservoir]]
- [[gas seepage in sandstone]]
- [[effective stress and permeability]]
- [[bulk modulus temperature dependence]]
- [[thermal cracking]]
- [[red sandstone physical properties]]
- [[steady-state gas flow method]]
- [[triaxial compression permeability test]]

## Candidate Methods
- [[steady-state gas flow permeability test]]
- [[SEM and optical microscopy for thermal damage]]
- [[triaxial compression with varied stress paths]]
- [[simplified double-pore texture model for permeability prediction]]
- [[fitting exponential relationship from gas flow data]]
- [[Darcy’s law for compressible gas permeability calculation]]
- [[CT scanning for thermal cracks]]

## Connections To Other Work
- Jones and Owens [11] 关于低渗透岩石小孔隙度变化 [Xu 2019, pp. 1-2]。
- Ghabezloo and Sulem [12] 提出孔隙度-有效应力指数律 [Xu 2019, pp. 1-2]。
- Wang et al. [13] 在花岗岩和花岗片麻岩中给出应力-渗透率幂律关系 [Xu 2019, pp. 1-2]。
- Yang et al. [14] 将渗透率-轴向应变曲线划分为五个阶段 [Xu 2019, pp. 1-2]。
- Zheng et al. [15] 基于 TPHM 模型建立孔隙度-渗透率-有效应力关系 [Xu 2019, pp. 2-2]。
- Zhang et al. [16,17]、Wu et al. [18]、Zhao et al. [19] 研究了高温下岩石力学与渗透特性 [Xu 2019, pp. 2-2]。
- Wu et al. [35] 给出了砂岩体模量随温度变化数据，本文对比其趋势 [Xu 2019, pp. 10-11]。
- Yang et al. [20] 对热处理后砂岩三轴力学和渗透行为进行了系统试验 [Xu 2019, pp. 2-2]。
- Yang et al. [25] 提供红砂岩矿物成分和力学参数 [Xu 2019, pp. 2-3]。
- Sun et al. [36] 分析石英相转变对岩石物理力学性质的影响 [Xu 2019, pp. 13-14]。
- Yang et al. [37]、Yang and Hu [38] 进一步探讨了高温后颗粒流模拟和循环载荷下渗透率长期行为 [Xu 2019, pp. 13-14]。

## Open Questions
- 原位高温高压同时加载下的渗透率演化规律尚未明确 [Xu 2019, pp. 2-2]。
- 超过 900 °C 的热处理对红砂岩渗透率和双孔隙模型参数的影响有待研究。
- 在塑性屈服和破坏后阶段，双孔隙模型是否适用，以及如何扩展。
- 矿物相变（如石英 α→β，长石熔融）对渗透率贡献的定量分离尚未完成。
- 其他类型砂岩或碳酸盐岩的类似试验能否得到一致的指数关系和模型参数。
- 长期蠕变与循环载荷下热损伤砂岩的渗透率演化与本模型的关系 [联系 Yang and Hu [38]]。

## Source Coverage
所有非空索引片段均已处理。共 11 个非空源块，编译后 11 个块，覆盖率 100%（按块计），字符比为 1.003815（编译后 52,890 字符，来源 52,689 字符）。源签名：fcb61e97a90b4727799905548ef329e947a68302。文献来源：Xu, Peng, and Sheng-Qi Yang. “Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone.” Acta Mechanica Sinica, vol. 35, no. 2, 2019, pp. 419-32. doi:10.1007/s10409-018-0824-6。
