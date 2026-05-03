---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-li-effect-of-thermal-treatment-on-the-physical-and-mechanical-properties-of-sandstone-insig"
title: "Effect of Thermal Treatment on the Physical and Mechanical Properties of Sandstone: Insights from Experiments and Simulations."
status: "draft"
source_pdf: "data/papers/2022 - Effect of Thermal Treatment on the Physical and Mechanical Properties of Sandstone Insights from Experiments and Simulations.pdf"
collections:
  - "zotero new"
citation: "Li, Man, and Xianshan Liu. \"Effect of Thermal Treatment on the Physical and Mechanical Properties of Sandstone: Insights from Experiments and Simulations.\" *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 3171-94, doi:10.1007/s00603-022-02791-1."
indexed_texts: "12"
indexed_chars: "57423"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "56907"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991014"
coverage_status: "full-index"
source_signature: "dc2047831b21eeded42ef162ff8ad41391e93e4f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:14:30"
---

# Effect of Thermal Treatment on the Physical and Mechanical Properties of Sandstone: Insights from Experiments and Simulations.

## One-line Summary

通过实验和基于矿物组成随机模型的数值模拟，系统研究了25–800℃热处理对砂岩物理力学性质的影响，揭示了400℃为性质变化阈值，建立了完全耦合的热‑力‑损伤本构模型，成功再现了砂岩从脆性向延性转变的破坏过程 [Li 2022, pp. 1-2]。

## Research Question

高温热处理如何影响致密砂岩储层砂岩的物理和力学性质？热损伤的演化机制是什么？能否建立一个能够完整模拟“热损伤‑力学加载”两阶段过程的数值模型？ [Li 2022, pp. 1-2]

## Study Area / Data

- **采样地点**：中国重庆市九龙坡区致密砂岩储层 [Li 2022, pp. 2-3]。
- **岩性特征**：灰白色砂岩，平均体积密度2410 kg/m³ [Li 2022, pp. 2-3]。
- **矿物组成（XRD）**：石英40.14%，长石30.75%，角闪石15.16%，黏土矿物（高岭石、蒙脱石）13.95% [Li 2022, pp. 2-3]。
- **试样规格**：圆柱体，高100 mm，直径50 mm，按ISRM标准制备 [Li 2022, pp. 2-3]。
- **热处理温度组**：25℃（常温对照）、200℃、400℃、600℃、800℃ [Li 2022, pp. 3-5]。
- **力学试验**：单轴压缩（每组3个试样）和三轴压缩（围压5、10、30 MPa） [Li 2022, pp. 3-5]。

## Methods

- **热处理程序**：升温速率5℃/min，目标温度恒温2 h，炉内自然冷却至室温 [Li 2022, pp. 3-5]。
- **物理性质测试**：测量质量、体积、体密度、孔隙率；XRD分析矿物组成变化 [Li 2022, pp. 5-7]。
- **力学试验**：使用岩石伺服三轴试验机（Rock 600-50HT PLUS），位移控制加载速率0.05 mm/min，获取应力‑应变曲线、峰值应力、峰值应变、杨氏模量、泊松比、黏聚力和内摩擦角 [Li 2022, pp. 3-5, 7-8]。
- **数值模拟**：
  - 引入 **Knuth‑Durstenfeld 洗牌算法**，基于XRD矿物含量生成考虑矿物组成的随机非均质模型 [Li 2022, pp. 8-11]。
  - 控制方程：静力平衡方程、几何方程、线性热弹性本构（包含热膨胀项）和热传导方程 [Li 2022, pp. 11-12]。
  - 损伤准则：最大拉应力准则（拉伸损伤）和Mohr‑Coulomb准则（剪切损伤），损伤变量定义为最大拉/压应变的幂函数（指数n=2经参数校准） [Li 2022, pp. 11-12]。
  - 模拟流程：在COMSOL Multiphysics中实现两阶段损伤过程——先模拟热处理过程（升温‑恒温‑冷却）产生热损伤，再在此基础上进行单轴压缩模拟 [Li 2022, pp. 12-15]。
- **模型校准**：通过对比不同强度本构参数n下的单轴抗压强度模拟值与实验值，确定n=2时误差最小（0.53%） [Li 2022, pp. 12-15]。

## Key Findings

1. **物理性质阈值**：400℃是砂岩物理性质变化的阈值。低于400℃时，质量、体积、体密度变化轻微；超过400℃后，质量快速降低（800℃时减2.8%），体积膨胀加速（800℃时增1.75%），体密度急速下降 [Li 2022, pp. 5-7]。
2. **孔隙率演化**：孔隙率随温度升高而增加，400℃以下增加较缓，600℃和800℃时急剧增大，分别较室温增加37.41%和53.16%，主要由热致微裂纹引起 [Li 2022, pp. 5-7]。
3. **力学性质劣化**：峰值应力和杨氏模量随温度升高而降低，400℃为拐点。400℃以下降幅较小，超过400℃后降幅加剧，800℃时峰值应力较25℃下降24.91%，杨氏模量下降53.05% [Li 2022, pp. 7-8]。
4. **泊松比突变**：泊松比在400~600℃之间出现突变（先降后升），归因于573℃时石英α‑β相变导致的脆‑延转变 [Li 2022, pp. 7-8]。
5. **剪切强度参数**：黏聚力随温度升高而下降，400℃后加速降低（800℃较25℃下降20.87%）；内摩擦角随温度升高而增大，400℃后快速上升（800℃时增加11.11%） [Li 2022, pp. 7-8]。
6. **破坏模式转变**：400℃以下，砂岩呈脆性破坏，形成单一宏观破裂面；600℃和800℃时，转变为延性破坏，试样粉碎为细小碎片，形成扩展剪切带而非尖锐破裂面 [Li 2022, pp. 15-19]。
7. **数值模型有效性**：所建完全耦合热‑力‑损伤模型成功模拟了砂岩两阶段损伤过程，预测的最终破坏模式与实验结果吻合良好，验证了模型的可靠性 [Li 2022, pp. 15-23]。
8. **损伤类型统计**：热处理过程中，400℃和600℃以拉伸损伤为主，800℃时剪切损伤数量迅速超过拉伸损伤，与宏观延性增强和剪切强度降低一致 [Li 2022, pp. 15-19]。
9. **温度均匀性要求**：数值模拟表明，充分恒温加热能消除温度梯度引起的局部热应力，保证实验是针对材料热损伤而非梯度裂纹 [Li 2022, pp. 12-15]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 400℃为砂岩物理力学性质变化的阈值，低于400℃影响很小 | [Li 2022, pp. 5-7] | Jiulongpo砂岩，空气冷却热处理 | 质量、体积、体密度、孔隙率、峰值应力、弹性模量均在400℃左右趋势转折 |
| 800℃时质量损失2.8%，体积膨胀1.75%，体密度急剧下降 | [Li 2022, pp. 5-7] | 升温速率5℃/min，恒温2h，炉内自然冷却 | 黏土矿物分解（400‑700℃）和石英相变（573℃）是主因 |
| 800℃时孔隙率增加53.16% | [Li 2022, pp. 5-7] | SEM证实微裂纹增多 | 热裂纹导致孔隙连通性改善 |
| 800℃时峰值应力降24.91%，杨氏模量降53.05% | [Li 2022, pp. 7-8] | 单轴压缩，位移控制0.05mm/min | 热损伤显著分化力学性质 |
| 泊松比在400‑600℃间突变，归因于573℃石英α‑β相变 | [Li 2022, pp. 7-8] | XRD显示石英占比在高温后上升 | 标志脆‑延转变 |
| 黏聚力在800℃降20.87%，内摩擦角升11.11% | [Li 2022, pp. 7-8] | Mohr‑Coulomb准则拟合三轴试验 | 颗粒胶结弱化、摩擦增强 |
| Knuth‑Durstenfeld随机非均质模型能有效反映热损伤 | [Li 2022, pp. 8-11] | 模型与光学显微观测的晶界裂纹相符 | 优于传统Weibull分布假设 |
| n=2时单轴抗压强度模拟误差仅0.53% | [Li 2022, pp. 12-15] | 室温校准，不同n对比 | 作为损伤演化参数 |
| 模拟破坏模式与实验一致：400℃以下脆性剪切破坏，600℃以上延性粉碎 | [Li 2022, pp. 19-23] | 两阶段TMD耦合模型 | 验证了模型对破坏转变的预测能力 |

## Limitations

- 数值模拟中忽略了高温下矿物化学反应（如石英相变、黏土脱水）对力学性质的直接影响，导致峰值应变模拟趋势与实验不完全一致（模拟中峰值应变先减后增） [Li 2022, pp. 19-23]。
- 模型假设热处理过程中各矿物含量不变，且化学反应的力学效应可忽略 [Li 2022, pp. 12-15]。
- 有限元软件COMSOL无法表征岩石初始压密阶段，将压密和线弹性阶段合并处理 [Li 2022, pp. 15-19]。
- 试样数量每组仅3个，虽通过P波检测筛选但天然非均质性的影响仍可能存在 [Li 2022, pp. 2-3, 5-7]。

## Assumptions / Conditions

- 热处理过程中砂岩主要矿物含量不变 [Li 2022, pp. 12-15]。
- 矿物化学反应对砂岩力学性质的影响可忽略 [Li 2022, pp. 12-15]。
- 热处理造成的损伤为不可逆损伤 [Li 2022, pp. 12-15]。
- 数值模型将压缩应力（应变）定义为正，采用弹性损伤理论，损伤后弹性模量按\( E = (1-D)E_0 \)退化 [Li 2022, pp. 11-12]。
- 热传导模拟时，砂岩被视为均匀初始温度场，加热段采用温度边界条件模拟炉内升温 [Li 2022, pp. 12-15]。

## Key Variables / Parameters

- **温度 \( T \)**：25–800℃ [Li 2022, pp. 1-2]。
- **物理性质变化率 \( w = \frac{\delta(T) - \delta_0}{\delta_0} \)** [Li 2022, pp. 5-7]。
- **力学参数**：峰值应力、峰值应变、杨氏模量 \( E \)、泊松比 \( \nu \)、黏聚力 \( c \)、内摩擦角 \( \phi \) [Li 2022, pp. 7-8]。
- **热物理参数**：线热膨胀系数 \( \alpha_T \)、比热容 \( C_v \)、导热系数 \( k \)、体密度 \( \rho \) [Li 2022, pp. 11-12]。
- **损伤变量 \( D \)**：与最大弹性拉应变 \( \varepsilon_{t0} \)、最大弹性压应变 \( \varepsilon_{c0} \) 和本构参数 \( n \) 相关 [Li 2022, pp. 11-12]。
- **矿物组成含量**（石英40.14%、长石30.75%、角闪石15.16%、黏土矿物13.95%）及各矿物的力学/热学参数（见表5） [Li 2022, pp. 8-11]。

## Reusable Claims

- 对于Jiulongpo致密砂岩，400℃是热损伤显著加剧的温度阈值 [Li 2022, pp. 1-2, 5-7]。
- 573℃石英α‑β相变导致泊松比突变和脆‑延转变是此类砂岩的重要特征 [Li 2022, pp. 7-8]。
- 热处理砂岩的单轴压缩是一个两阶段损伤过程：不可逆热损伤 + 机械加载损伤 [Li 2022, pp. 2-3]。
- 基于矿物组成的Knuth‑Durstenfeld洗牌算法能够更准确地反映岩石热损伤的裂纹萌生位置（晶界） [Li 2022, pp. 8-11]。
- 采用拉伸和剪切双损伤准则（最大拉应力 + Mohr‑Coulomb）的弹性损伤模型，配合 \( n=2 \) 的应变软化关系，可有效预测温度‑力学耦合下砂岩的破坏行为 [Li 2022, pp. 11-12, 12-15]。

## Candidate Concepts

- [[thermal damage]]
- [[heterogeneity]]
- [[Knuth-Durstenfeld shuffle]]
- [[two-stage damage process]]
- [[brittle-ductile transition]]
- [[phase transition of quartz]]
- [[irreversible damage]]
- [[thermal-mechanical coupling]]
- [[mineral composition model]]

## Candidate Methods

- [[triaxial servo-controlled testing]]
- [[XRD mineral analysis]]
- [[SEM microstructure observation]]
- [[Knuth-Durstenfeld shuffle algorithm for random heterogeneous model]]
- [[COMSOL Multiphysics coupled thermal-mechanical simulation]]
- [[Mohr-Coulomb criterion with tension cutoff]]
- [[elastic damage model with strain-based damage variable]]
- [[parameter calibration by uniaxial compression simulation]]

## Connections To Other Work

- 与多种岩石（花岗岩、砂岩、碳酸盐岩等）的高温物理力学性质研究相呼应，汇总于Table 1 [Li 2022, pp. 2-3]。
- 热损伤数值模拟方面，与Zhao (2015)的PFC2D离散元模拟、Wang & Konietzky (2019)的FLAC3D模拟、Tang et al. (2016)的RFPA模拟等形成对比，本文采用有限元完全耦合方法并引入矿物组成，提高了真实性 [Li 2022, pp. 2-3]。
- 引用的矿物热反应数据（如黏土矿物分解、石英相变温度）与Tian et al. (2012)、Xiao et al. (2021)等一致 [Li 2022, pp. 5-7]。
- 力学参数计算方法（Mohr‑Coulomb拟合）与Kumari et al. (2017)、Wang & Konietzky (2019)等相同 [Li 2022, pp. 7-8]。

## Open Questions

- 如何将高温下矿物的物理化学反应（如石英相变引起的体积膨胀、黏土脱水收缩）定量耦合到力学本构模型中，以更准确地预测峰值应变等响应？ [Li 2022, pp. 19-23]
- 在更复杂的应力路径（如三轴、循环荷载）下，所提热‑力‑损伤模型的适用性如何？ [未在本研究中探讨，not confirmed]
- 热损伤的演变与渗透率提升之间的定量关系如何？尽管本文提及孔隙率变化，但未建立渗透率模型 [Li 2022, pp. 5-7]。

## Source Coverage

所有非空索引片段均已处理。  
- 索引文本块数：12  
- 索引字符数：57,423  
- 编译后源块数：12（全部使用）  
- 编译后字符数：56,907  
- 覆盖率（按块）：1.0  
- 覆盖率（按字符）：0.991
