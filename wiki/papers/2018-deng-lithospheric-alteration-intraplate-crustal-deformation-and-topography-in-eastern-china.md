---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-deng-lithospheric-alteration-intraplate-crustal-deformation-and-topography-in-eastern-china"
title: "Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China."
status: "draft"
source_pdf: "data/papers/2018 - Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.pdf"
collections:
  - "山西断裂地质构造"
citation: "Deng, Yangfan, and Will Levandowski. \"Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.\" *Tectonics*, vol. 37, 2018, pp. 4120-4134. doi:10.1029/2018TC005079. Accessed 2026."
indexed_texts: "13"
indexed_chars: "61475"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61743"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004359"
coverage_status: "full-index"
source_signature: "00c7d33937d591a758ae9ce6b032822adf710d3c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:52:19"
---

# Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.

## One-line Summary
基于重力与地形的联合反演及挠曲均衡分析，定量揭示了中国东部沿地形梯度带（TGB）地壳浮力过度补偿高程差异、东部岩石圈普遍减薄至约90 km，并提出地幔再富化可能加剧这一差异。

## Research Question
中国东部板内构造域中横贯4000 km的显著地形梯度带（TGB）为何能持续存在？该梯度是否反映了岩石圈热化学结构的东西向突变？地壳、地幔岩石圈温度/成分、及软流圈流动各自对地表高程贡献如何？[Deng 2018, pp. 1-1]

## Study Area / Data
- **研究区**：中国东部（华北克拉通、华南板块及周边），重点对比TGB东、西两侧。[Deng 2018, pp. 1-1]
- **数据来源**：
  - 地形：ETOPO1（1弧分全球模型）[Deng 2018, pp. 1-4]
  - 布格重力：EGM2008 [Deng 2018, pp. 1-4]
  - 壳幔S波速度：Shen等 (2016) 的三维模型 [Deng 2018, pp. 4-5]
  - 莫霍面深度：来自接收函数（Y. Li等, 2014）[Deng 2018, pp. 4-5]
  - 莫霍面温度：来自稳态热传导模拟与地震波速约束（Sun等, 2013）[Deng 2018, pp. 7-9]
  - 地表热流：Jiang等 (2016) 汇编数据 [Deng 2018, pp. 1-4]
  - 弹性厚度：基于多窗谱法（Pérez-Gussinyé等, 2004）自算的二维模型 [Deng 2018, pp. 7-9]

## Methods
1. 利用S波速-密度经验关系构造初始三维密度模型，然后以地形和重力为观测进行联合反演，迭代优化获得精细地壳－上地幔密度结构（0–150 km）。[Deng 2018, pp. 4-5]
2. 从观测地形中扣除地壳均衡贡献 \(H_c\)（通过对密度模型垂向积分），得到剩余地形，将其归因于地幔岩石圈（ML）。[Deng 2018, pp. 4-5]
3. 考虑挠曲均衡（而非局部均衡），采用新计算的弹性厚度模型进行空间滤波，以反映岩石圈强度对短波长地形的支撑。[Deng 2018, pp. 4-5, 7-9]
4. 假设线性地温梯度（莫霍面温度至软流圈温度1350 °C），用热膨胀系数将地幔岩石圈温度场转换为密度，再根据剩余地形解算地幔岩石圈厚度。[Deng 2018, pp. 4-5]
5. 定性讨论动态地形、成分异常和水化作用对厚度估算的潜在影响。[Deng 2018, pp. 10-12]

## Key Findings
- **地壳浮力超补偿**：TGB西侧地壳贡献高程 \(H_c\) 普遍 >4.2 km，东侧约3.6 km，地壳浮力的东西跃变幅度超过实际地形差，即若无地幔岩石圈补偿，地形梯度将更大。[Deng 2018, pp. 7-9]
- **岩石圈厚度系统性差异**：TGB大致对应岩石圈厚度110 km的等值线（东北和秦岭—大别除外），西侧（鄂尔多斯、四川盆地）岩石圈 >120 km，东侧（华北克拉通东部、华夏地块）约90 km。[Deng 2018, pp. 9-10]
- **东部岩石圈普遍减薄**：不仅华北克拉通东部，华南东部及整个中国东部沿海均显示出薄岩石圈，暗示大范围的岩石圈拆沉或改造。[Deng 2018, pp. 1-1, 9-10]
- **地幔再富化的潜在影响**：若东部ML因再富化而密度偏高（如Mg#降低2%），等厚条件下所需岩石圈厚度将更薄（~70 km），从而加剧东西差异。[Deng 2018, pp. 10-11]
- **动态地形影响有限**：东部下方若存在大规模软流圈上涌，需更厚的岩石圈来解释地形，但这与地震学观测（60–70 km）矛盾，因此推断动态地形对地表高程贡献较小。[Deng 2018, pp. 10-11]
- **水化作用可能缩小差异**：若东部ML因俯冲板片脱水而水化（1%蛇纹石化），密度降低会使所需的岩石圈厚度增加（从90 km→~100 km），从而部分抵消东西不均一。[Deng 2018, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| TGB以西地壳对地形的贡献 \(H_c\) 普遍超4.2 km，以东约3.6 km，地壳浮力东弱西强。 | [Deng 2018, pp. 7-9] | 基于联合反演后的三维密度模型，考虑挠曲均衡滤波。 | 地壳厚度和密度共同导致该差异，与莫霍面深度正相关。 |
| 东侧岩石圈总厚度（地壳+ML）普遍约90 km，西侧超过120 km，TGB为110 km厚度等值线（东北和秦岭—大别除外）。 | [Deng 2018, pp. 9-10] | 采用线性地温梯度假设、软流圈温度1350 °C、热膨胀系数4.0×10⁻⁵/°C。 | 未考虑成分和水化偏差时，厚度差异主因温度控制。 |
| 华北克拉通东部（ENCC）及华南东南部岩石圈厚度与地震学结果（60–70 km）趋势一致，但等厚结果偏厚（~90 km）。 | [Deng 2018, pp. 12-13] | 与Chen(2010)、Zheng等(2014)的地震学模型对比。 | 差异可能源于地幔成分密度偏高（再富化），使实际热厚度更薄。 |
| 假设东侧软流圈上涌造成动态地形，则岩石圈需更厚，与地震学薄岩石圈相悖，故动态地形贡献不大。 | [Deng 2018, pp. 10-11] | 对比东部板内火山下方实际地震模型。 | 上涌可能为火山提供物质，但对地表高程影响微弱。 |
| 1%蛇纹石化使ML密度降低约8 kg/m³，东部若存在水化则等厚岩石圈厚度从~90 km增至~100 km。 | [Deng 2018, pp. 11-12] | 引用Christensen(2004)的岩石密度数据。 | 水化可能来源于俯冲太平洋板片的脱水作用。 |

## Limitations
- 莫霍面深度不确定性（<4 km）可导致岩石圈厚度约8 km的误差，在东部占比~9%，西部<7%。[Deng 2018, pp. 9-10]
- 莫霍面温度不确定性<100 °C，引起ML密度误差±6.4 kg/m³，造成岩石圈厚度不确定性西侧~20 km、东侧<15 km。[Deng 2018, pp. 9-10]
- 弹性厚度估计本身存在较大不确定性；局部均衡与挠曲均衡结果差异主要出现在高弹性厚度区（鄂尔多斯、四川盆地），但整体趋势一致。[Deng 2018, pp. 10-11]
- 所有剩余地形被归因为ML温度，未同时反演成分、水化及动态地形，仅进行了定性敏感性讨论。[Deng 2018, pp. 10-12]
- 热结构采用稳态方程，构造活动区（如火山附近、板块边界）可能存在非稳态偏差。[Deng 2018, pp. 11-12]

## Assumptions / Conditions
- 岩石圈处于挠曲均衡状态，强度由弹性厚度参数化，短波长载荷由岩石圈强度支撑。[Deng 2018, pp. 4-5]
- 地幔岩石圈密度仅由温度线性决定，热膨胀系数、软流圈温度及地温梯度均为均匀给定值（δ=4.0×10⁻⁵/°C, θa=1350 °C）。[Deng 2018, pp. 4-5]
- 初始密度模型基于S波速－密度经验关系，并假定重力与地形残差可通过修改地壳规模密度分布来同时拟合。[Deng 2018, pp. 4-5]
- 停滞的太平洋板片对重力和地形的贡献极小（近中性浮力），故忽略过渡带密度异常。[Deng 2018, pp. 4-5]
- 软流圈参考密度为3200 kg/m³，大洋中脊均衡校正项 \(H_0\) = 2.4 km。[Deng 2018, pp. 4-5]

## Key Variables / Parameters
- \(H_c\)：地壳对地形的均衡贡献（km）
- \(H_{ml}\)：地幔岩石圈对地形的均衡贡献（km）
- \(T_{ml}\)：地幔岩石圈厚度（km）
- \(\rho_c, \rho_{ml}, \rho_a\)：地壳、地幔岩石圈、软流圈密度（kg/m³）
- \(\theta_c, \theta_a\)：莫霍面温度与软流圈温度（°C）
- \(\delta\)：热膨胀系数（4.0×10⁻⁵/°C）
- 弹性厚度 \(T_e\)：控制挠曲滤波的岩石圈有效弹性厚度（km）
- 莫霍面深度：取自接收函数（km）
- 地表热流：用于温度场约束（mW/m²）

## Reusable Claims
- 中国东部地形梯度带（TGB）对应的地表高程跃变（~900 m）主要受地壳厚度和密度控制，东、西两侧地壳均衡贡献差约1 km，地壳浮力过度补偿真实地形。[Deng 2018, pp. 7-9]
  - 条件：三维密度与莫霍面深度约束下，采用挠曲均衡扣除地壳影响后，剩余地形揭示地幔岩石圈贡献。东侧地壳偏薄（30–35 km）且下地壳密度高，西侧厚（>35 km）且下地壳密度相对低。
- 中国东部沿海地区（华北克拉通东部、华南东部）的岩石圈厚度在均衡框架下约为90 km，显著小于中央克拉通（>120 km），指示大规模岩石圈减薄事件可能波及整个东部大陆。[Deng 2018, pp. 9-10, 12-13]
  - 条件：基于热密度假设，若考虑再富化导致成分密度增加，实际热岩石圈可能更薄；若水化则略厚，但薄岩石圈的空间趋势不变。
- 中国东部的板内火山活动区若存在较强的动态地形，则需要异常厚的岩石圈，与地震学观测相矛盾，因此软流圈上涌对地表高程的直接贡献很小。[Deng 2018, pp. 10-11]
  - 条件：仅探讨了垂向流动的地形效应，俯冲过程可能通过水化等间接途径影响岩石圈。
- 地幔岩石圈成分差异（如Mg#变化2%）可引起约10–20 km的等厚岩石圈厚度偏差，可在无额外温度异常时解释地震学与均衡厚度之间的差异。[Deng 2018, pp. 10-11]
  - 条件：适用区为经历显生宙改造的克拉通边缘，需要独立的地球化学约束。

## Candidate Concepts
- [[topographic gradient belt (TGB)]]
- [[lithospheric dismemberment]]
- [[refertilization of mantle lithosphere]]
- [[dynamic topography]]
- [[flexural isostasy]]
- [[North-South Gravity Lineament (NSGL)]]
- [[craton destruction]]
- [[mantle hydration by subduction]]
- [[elastic thickness]]
- [[Moho temperature]]

## Candidate Methods
- [[joint inversion of gravity and topography for 3‑D density]]
- [[flexural isostatic stripping of crustal contribution]]
- [[thermal lithosphere thickness from linear geotherm]]
- [[multitaper spectral estimation of elastic thickness]]
- [[3‑D steady-state thermal modeling with seismic constraints]]

## Connections To Other Work
- 与华北克拉通东部岩石圈减薄研究一致：[[North China Craton destruction]] (Chen等, 2009；Zheng等, 2007)；薄岩石圈与软流圈上涌的争论，本研究通过地形约束补充说明减薄空间范围可能逾越华北克拉通，涵盖华南东部。[Deng 2018, pp. 12-13]
- 与太平洋俯冲相关模型关联：停滞的太平洋板片可能通过脱水引发上覆地幔交代与水化 (Huang & Zhao, 2006)；本文从地形角度探讨了水化密度效应，认为可部分解释均衡厚度与地震厚度的偏差。[Deng 2018, pp. 11-12]
- 与壳幔弹性厚度研究对比：Chen等 (2013) 提出NSGL为继承性薄弱带，本文新计算的弹性厚度图显示TGB附近普遍低弹性厚度，支持该论点。[Deng 2018, pp. 7-9]
- 与青藏高原周边应变传递相关：文章仅少量引用，但莫霍面温度高处与印度—亚洲碰撞剪切生热 (Deng & Tesauro, 2016) 呼应。[Deng 2018, pp. 7-9]

## Open Questions
- 东部岩石圈减薄的机制：拆沉、热侵蚀还是熔体—岩石反应主导？地形均衡分析仅提供厚度约束，需结合岩石学与地球化学数据区分。[Deng 2018, pp. 1-1, 12-13]
- 松辽盆地下方岩石圈厚度在均衡结果中偏厚（>130 km），与S波接收函数和大地电磁显示的浅埋藏高导层（~60–85 km）矛盾：是由于莫霍面温度过高估计还是该处存在显著的成分密度异常（富化）？[Deng 2018, pp. 12-13]
- 华南克拉通是否同样经历了部分根去除？均衡厚度显示东南沿海薄但向西逐渐增厚，该过渡与地震间断面的关系有待多学科约束。[Deng 2018, pp. 12-13]
- 地幔水化对密度的定量影响尚存较大不确定性，俯冲板片脱水范围与程度如何系统性地改变东部岩石圈浮力？[Deng 2018, pp. 11-12]
- 软流圈上涌的动态地形效应在地表几乎不可见，但火山链的成因是否意味着存在小尺度对流或边缘对流？如何通过联合地震—重力—地形反演分辨？[Deng 2018, pp. 10-11]

## Source Coverage
本页面使用了全部13个非空索引文本片段（共61,475字符），所有片段均已处理，覆盖率达100%（按片段数计1.0，按字符数计1.004359）。来源文件：`data/papers/2018 - Lithospheric Alteration, Intraplate Crustal Deformation, and Topography in Eastern China.pdf`，DOI: 10.1029/2018TC005079。数据获取于2026年。
