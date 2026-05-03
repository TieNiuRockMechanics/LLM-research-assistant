---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-xu-influence-of-stress-and-high-temperature-treatment-on-the-permeability-evolution-behavio"
title: "Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone."
status: "draft"
source_pdf: "data/papers/2019 - Influence of stress and high-temperature treatment on the permeability evolution behavior of sandstone.pdf"
collections:
  - "zotero new"
citation: "Xu, Peng, and Sheng-Qi Yang. \"Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone.\" *Acta Mechanica Sinica*, vol. 35, no. 2, 2019, pp. 419-32. doi:10.1007/s10409-018-0824-6."
indexed_texts: "11"
indexed_chars: "52689"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:20:13"
---

# Influence of Stress and High-Temperature Treatment on the Permeability Evolution Behavior of Sandstone.

## One-line Summary
通过热处理后红砂岩的三轴渗流实验，发现渗透率随温度升高呈指数增长（800°C时可增大100倍），并建立一个双孔纹构模型来描述弹性压缩下渗透率随静水应力和偏应力的演化 [Xu 2019, pp. 1-2]。

## Research Question
本文旨在分析有效应力和热处理温度对致密红砂岩渗透率的影响，特别是在三轴压缩条件下渗透率的演化规律 [Xu 2019, pp. 2-2]。

## Study Area / Data
实验选用中国山东省的红砂岩，矿物成分为长石、石英、岩屑和胶结物。试样制备成直径50 mm、高100 mm的圆柱体，表面无明显裂纹，内部结构致密，微孔隙和微裂纹较少 [Xu 2019, pp. 2-3]。热处理温度范围为20°C至900°C（20, 200, 400, 500, 600, 700, 800, 900 °C），升温速率5 °C/min，冷却后开展气体渗流测试 [Xu 2019, pp. 2-3]。

## Methods
利用可施加三轴压力的气体渗流系统，测量不同热处理温度后砂岩在多样应力路径（静水压缩、恒围压轴向加载、恒轴压围压加载）下的渗透率。系统最高围压为60 MPa，适用于渗透系数大于10⁻²⁵ m²的岩石，测试介质为气体 [Xu 2019, pp. 2-3]。基于双孔纹构概念，将岩石分为微孔基质（孔隙度变化可忽略）和裂缝基质（压缩变形主导孔隙度变化），结合Darcy渗流定律推导渗透率与应力的理论关系，并通过实验曲线拟合确定模型参数 [Xu 2019, pp. 7-8]。

## Key Findings
1. 热处理导致试样质量下降，200°C时因弱结合水逸出下降最快，400°C出现剥落，500°C出现平行于未来围压方向的拉伸裂纹 [Xu 2019, pp. 3-5]。
2. 渗透率系数与温度呈指数关系，温度从20°C升至800°C时，渗透率增大约100倍（量级从10⁻¹⁹ m²升至10⁻¹⁷ m²）[Xu 2019, pp. 5-7]。
3. 静水应力下渗透率随应力增加呈指数衰减，先快后缓并趋于极限值；初始渗透率和极限渗透率均随温度指数上升，模型与实验吻合良好 [Xu 2019, pp. 8-10]。
4. 偏应力对渗透率影响显著：当轴压高于围压时，渗透率随偏应力明显增加；当轴压低于围压时，渗透率先降后升，最小值出现在偏应力约-26 MPa处，而非静水条件 [Xu 2019, pp. 10-11]。
5. 体积模量随温度先降后升，在800°C附近达到最小值（数据来自文献[35]）[Xu 2019, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 热处理后质量随温度递减，200°C下降最剧烈，400°C表面剥落，500°C出现拉伸裂纹 | [Xu 2019, pp. 3-5] | 红砂岩，升温5°C/min，炉冷 | 质量损失归因于不同形态水分逃逸 |
| 渗透率系数与温度呈指数关系，800°C渗透率为20°C的100倍 | [Xu 2019, pp. 5-7] | 红砂岩，不同温度热处理，不同气体压力测试 | 基于气体渗流试验的实测值 |
| 静水应力下渗透率指数式下降，并有趋于稳定极限值，模型预测与实验相符 | [Xu 2019, pp. 8-10] | 弹性压缩阶段，零偏应力，多种温度 | 双孔模型假设微孔基质孔隙度不变 |
| 偏应力为-26 MPa时渗透率达最小，而非静水压缩状态 | [Xu 2019, pp. 10-11] | 800°C、900°C试样，恒定体积应力和孔隙压力 | 偏应力定义σₐ-σₖ |
| 渗透率与孔隙度成正比（K/K₀=φ/φ₀），裂缝变形主导孔隙度变化 | [Xu 2019, pp. 7-8] | 等温达西流，微孔基质孔隙度恒定假设 | 用于推导应力-渗透率关系 |

## Limitations
- 仪器最大围压60 MPa低于红砂岩单轴抗压强度，因此试验主要处于弹性阶段；对于渗透系数低于10⁻²⁵ m²的岩石不适用 [Xu 2019, pp. 2-3]。
- 未能进行500°C以上的实时高温三轴测试，采用热处理后冷却试样的替代方法，可能与真实高温原位行为有差异 [Xu 2019, pp. 2-3]。
- 双孔模型假设气体流动为层流、等温且微孔基质不变形，不适用于非弹性及破坏后阶段 [Xu 2019, pp. 7-8]。
- 偏应力测试的温度和应力范围有限，其他温度下的响应未从索引片段中确认。
- 未提供渗透率测试的重复性和误差分析。

## Assumptions / Conditions
- 岩石可简化为由高刚度微孔基质和低刚度裂缝基质组成的双孔结构，压缩下裂隙闭合主导孔隙度变化，微孔基质孔隙度假定为常数 [Xu 2019, pp. 7-8]。
- 气体渗流满足达西定律，渗透系数与流体压力基本无关 [Xu 2019, pp. 7-8]。
- 渗透率与孔隙度存在线性关系 K/K₀ = φ/φ₀ [Xu 2019, pp. 7]。
- 裂缝基质变形可采用Louis经验公式 δₙ = δₘₐₓ · …（未从片段中完整给出）[Xu 2019, pp. 8]。
- 热处理过程中弱结合水在~150°C完全逸出，强结合水在200-300°C逸出 [Xu 2019, pp. 3-4]。
- 试验均保持在试样弹性压缩范围内，应力小于强度 [Xu 2019, pp. 10]。

## Key Variables / Parameters
- 温度 T (°C)
- 渗透系数 K (m²)，初始渗透系数 K₀，极限渗透系数（静水压缩下的稳定值）
- 孔隙度 φ，初始孔隙度 φ₀
- 裂缝基质初始孔隙度 φₐ₀
- 微孔基质单元长 a，裂缝基质单元宽 b
- 裂缝变形量 Δₓ, Δᵧ, Δ₂
- 静水应力 S (或体积应力)，偏应力 σₐ – σₖ
- 参数 αₘ (与体积压缩性相关，随温度变化)
- 气体压力 p，偏差因子 Z，动力粘度 μ，压缩系数 c₉（理论公式中涉及，未给出具体值）
- 裂隙最大闭合量 δₘₐₓ（经验参数）
- 体积模量（参考图14，数据源自文献[35]）

## Reusable Claims
- **热‑渗指数律**：对于致密红砂岩，热处理温度20‑800°C范围内，渗透率系数随温度呈指数增长，提高幅度可达两个数量级。该关系在冷却后测试条件下成立，可用于评估热损伤砂岩的渗透性变化，但须考虑岩石类型和升温速率等限制 [Xu 2019, pp. 5-7]。
- **静水压缩‑渗透率衰减模型**：在弹性三轴压缩下，渗透率随静水应力增加呈指数衰减并趋近极限值。此行为可由双孔纹构模型描述，其中裂缝闭合控制渗透率下降。模型要求微孔基质刚度远大于裂缝基质，且变形在弹性范围 [Xu 2019, pp. 7-10]。
- **非对称偏应力响应**：偏应力对渗透率的影响非单调；当围压大于轴压时渗透率可能先下降再上升，最小值偏离静水条件（约‑26 MPa）。该效应需在非静水原位应力状态的渗流分析中考虑 [Xu 2019, pp. 10-11]。
- **水分逃逸与质量损失分阶段特征**：200°C质量锐减对应弱结合水，200‑300°C强结合水逃逸，400°C以上出现宏观热裂纹和剥落，这些机制共同导致渗透率升高 [Xu 2019, pp. 3-5]。
- **热裂纹方向性**：无围压加热时产生的拉伸裂纹平行于未来加载的围压方向，表明存在各向异性热损伤 [Xu 2019, pp. 4-5]。

## Candidate Concepts
- [[high-temperature rock permeability]]
- [[thermal cracking in sandstone]]
- [[double-porosity model]]
- [[Darcy flow in porous rock]]
- [[elastic triaxial compression]]
- [[permeability-stress relationship]]
- [[bound water in rock]]
- [[effective stress law for permeability]]
- [[thermal damage in reservoir rocks]]
- [[gas permeability measurement]]

## Candidate Methods
- [[gas seepage test under triaxial compression]]
- [[post-thermal-treatment permeability measurement]]
- [[double-pore texture model for permeability]]
- [[empirical fracture closure law (Louis)]]
- [[SEM observation of microstructure]]
- [[CT scanning for thermal cracks]]
- [[steady-state gas flow method]]
- [[porosity-permeability exponential fitting]]

## Connections To Other Work
- Yang 等 [14] 提出的渗透率‑轴向应变五阶段划分和气体压力影响，为本研究提供了现象学基础 [Xu 2019, pp. 2-2]。
- Zheng 等 [15] 基于两部分胡克模型（TPHM）建立了低渗沉积岩的孔隙度‑渗透率‑有效应力关系，形成理论背景 [Xu 2019, pp. 2-2]。
- Zhang 等 [16,17]、Wu 等 [18]、Zhao 等 [19] 开展了高温下花岗岩和砂岩的渗透率与声发射等测试，但未提出温度与渗透率的定量规律，本工作是对该不足的补充 [Xu 2019, pp. 2-2]。
- Yang 等 [20] 的热处理砂岩三轴试验讨论了密度、孔隙度、渗透率及变形模量与温度的关系，是本研究的直接前驱 [Xu 2019, pp. 2-2]。
- 裂隙变形模拟引用了 Louis [33] 的经验公式 [Xu 2019, pp. 8]。
- 体积模量数据参考了文献 [35]（具体出处未从片段中确认）[Xu 2019, pp. 10-11]。

## Open Questions
- 模型在岩石屈服、破坏及峰后阶段的适用性未检验。
- 高温实时渗透率测试技术若突破，是否会导致渗透率演化规律与冷却后测试结果不同？
- 该双孔模型和指数关系是否适用于其他岩石类型（如花岗岩、碳酸盐岩）及低渗岩石？
- 偏应力导致最小渗透率偏移的物理机制尚需深入探讨，特别是与裂隙各向异性闭合和张开的关系。
- 体积模量随温度非线性变化的矿物学与微观机制未从索引片段中确认。
- 气体滑脱效应（Klinkenberg效应）在低压时是否影响结果未讨论。

## Source Coverage
本知识页基于11条索引片段汇编，覆盖了论文的摘要、引言、材料与实验方法、部分实验结果（质量变化、渗透率‑温度、静水应力渗透率、偏应力渗透率）以及理论模型的建立与验证。缺失内容包括完整的实验数据表、不同温度下偏应力测试的详细工况、参数识别过程、讨论部分（如温度对力学性质影响的深入分析）及结论。同时，对其他相关工作的对比讨论亦不够充分。因此，本页呈现了核心发现与方法，但在实验细节和机理讨论上存在局限。
