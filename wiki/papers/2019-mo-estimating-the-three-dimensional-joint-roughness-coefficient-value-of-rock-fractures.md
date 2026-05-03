---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-mo-estimating-the-three-dimensional-joint-roughness-coefficient-value-of-rock-fractures"
title: "Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures."
status: "draft"
source_pdf: "data/papers/2019 - Estimating the three-dimensional joint roughness coefficient value of rock fractures.pdf"
collections:
  - "zotero new"
citation: "Mo, Ping, and Yanrong Li. \"Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures.\" *Bulletin of Engineering Geology and the Environment*, vol. 78, 2019, pp. 857-66. doi:10.1007/s10064-017-1150-0."
indexed_texts: "8"
indexed_chars: "39905"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "39925"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.000501"
coverage_status: "full-index"
source_signature: "8e6168b983caea30b3362d8bd68d332a02697d3d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T23:03:50"
---

# Estimating the Three-Dimensional Joint Roughness Coefficient Value of Rock Fractures.

## One-line Summary
本文基于38组新鲜岩石节理的直接剪切试验，提出了利用九个三维粗糙度参数（θs、θg、θ2s、SsT、SsF、Van、Zsa、Zrms、Zrange）估算节理粗糙度系数（JRC）的经验方程，其中振幅参数计算简便，采样间隔影响较小，适合工程快速估算。[Mo 2019, pp. 1, 8,9]

## Research Question
如何利用从整个裂隙表面提取的三维粗糙度参数客观地估算岩石节理的节理粗糙度系数（JRC），并建立可靠的经验方程？[Mo 2019, pp. 1-3]

## Study Area / Data
- 38组新鲜岩石块体，中间含有结构面：9组石灰岩、12组花岗岩、17组砂岩，粗糙度从光滑到极粗糙形成序列。[Mo 2019, pp. 4]
- 试样尺寸：120 mm×120 mm，浇筑于150 mm×150 mm×223.5 mm混凝土块中，节理面尽可能水平对齐。[Mo 2019, pp. 4]
- 直剪试验法向应力500 kPa（模拟15–25 m深度），剪切速率0.3 mm/min，每个试样沿四个方向（D1–D4）依次剪切。[Mo 2019, pp. 5-6]
- 激光扫描（HAND SCAN™ 300，分辨率0.1 mm，精度0.04 mm）获取上下裂隙表面点云，空间分辨0.2 mm。[Mo 2019, pp. 6]
- 基本摩擦角（φb）通过锯切干燥节理面的倾斜试验测定，节理壁强度（JCS）用施密特回弹仪测定。[Mo 2019, pp. 5-6]

## Methods
- JRC值根据Barton的JRC-JCS模型由实测峰值剪应力（τ）、JCS和φb反算得出，采用四个方向剪切的平均值以考虑各向异性。[Mo 2019, pp. 7]
- 表面形态数字化后，以不同采样间隔（0.4, 0.8, 1.6, 3.2, 6.4 mm）构建网格数据，进而生成三角不规则网络（TIN）模型和三维线框模型。[Mo 2019, pp. 6]
- 振幅参数直接由点云计算；斜率参数由TIN模型计算；体积参数由三维线框模型计算；面积参数分别由TIN和三维线框模型计算。[Mo 2019, pp. 6-7]
- 提出方向无关的斜率参数θg（阈值角度的积分），以替代含拟合值的θci。[Mo 2019, pp. 7]
- 通过多元回归建立JRC与粗糙度参数及采样间隔的函数关系，并比较拟合优度（R²）。[Mo 2019, pp. 7-9]

## Key Findings
- 九个三维粗糙度参数（θs、θg、θ2s、SsT、SsF、Van、Zsa、Zrms、Zrange）与JRC具有密切相关性（R²>0.75），可用于估算JRC。[Mo 2019, pp. 9]
- 斜率参数（如θs）的拟合相关系数最高，振幅参数（Zsa、Zrms、Zrange）最低，但振幅参数计算最简单。[Mo 2019, pp. 9]
- 采样间隔对体积和振幅参数（Van、Zsa、Zrms、Zrange）的影响很小，而对斜率与面积参数（θs、θg、θ2s、SsT、SsF）影响较大。[Mo 2019, pp. 9]
- 其他参数（Zss、Zsk、Vsvi、Vsci、Sdr、Sts）与JRC无良好相关性。[Mo 2019, pp. 7-8]
- 反算JRC时采用四方向平均峰值强度，相对应地选用方向无关的粗糙度参数θs、θ2s和θg。[Mo 2019, pp. 7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 九个参数的JRC经验方程：JRC=2.9θs^0.7+SI^0.809−5.6 (R²=0.902)；JRC=3.9θg^0.6+SI^0.815−7.7 (R²=0.900)；JRC=36.5θ2s^0.5+SI^0.845−7.8 (R²=0.883)；JRC=47.7(SsT−1)^0.3+SI^0.836−6.7 (R²=0.889)；JRC=47.8(SsF−1)^0.3+SI^0.837−6.7 (R²=0.888)；JRC=43.9Van^0.1+SI^0.087−34.4 (R²=0.824)；JRC=58.5Zsa^0.1−SI^−0.071−48.9 (R²=0.804)；JRC=63.2Zrms^0.1+SI^−0.090−54.7 (R²=0.798)；JRC=15.5Zrange^0.2+SI^0.166−15.8 (R²=0.759) | [Mo 2019, Table 6, pp. 7-8] | 基于38组试样，法向应力500 kPa，采样间隔0.4–6.4 mm | 振幅参数计算简便，推荐用于工程快速估算 |
| 上下表面高度参数的最大变异（Vrms, Vsa, Vrange）约−4.68%，表明吻合良好；剪切前后高度参数差异<2.16%，表面无明显损伤 | [Mo 2019, Table 5, pp. 6] | 低应力水平（σn/JCS<0.03），D1–D3剪切位移约6 mm，D4剪切位移>30 mm | 支持用下表面代表耦合节理面进行参数提取 |
| 斜率参数θs、θ2s基于TIN模型计算比三维线框模型更准确，避免因四边形不共面而使用最小二乘平面替代带来的偏差 | [Mo 2019, pp. 7] | TIN三角面片均为平面 | 参数计算方法的建议 |
| θg为最大实际倾角αmax以下面积比率Aα的积分，替代θci避免拟合值C的影响 | [Mo 2019, pp. 7, Eq. 3] | 定义θg=∫₀^αmax Aα dα | 方向无关的新斜坡参数 |
| Zss、Zsk、Vsvi、Vsci与JRC的相关系数低于0.4，Sdr和Sts回归效果差 | [Mo 2019, pp. 7-8] | 38组试验数据 | 不推荐这些参数用于JRC估算 |

## Limitations
- 经验方程基于特定岩石类型（石灰岩、花岗岩、砂岩）和浅层条件（法向应力500 kPa，模拟15–25 m深度）得出，推广至其他岩性或深部高地应力情况需验证。[Mo 2019, pp. 9]
- 采样间隔的影响在斜率与面积参数上更显著，超出本研究使用的0.4–6.4 mm间隔时方程可能不适用。[Mo 2019, pp. 9]
- 剪切试验保持低应力比（σn/JCS<0.03）以防止表面损伤，对于高应力条件下节理面磨损的情况，方程可能高估JRC。[Mo 2019, pp. 6,9]
- 3D参数的提取依赖ArcGIS®、Surfer®、MATLAB®等专业软件，现场快速应用可能受限。[Mo 2019, pp. 6]

## Assumptions / Conditions
- 节理壁新鲜、上下表面完全接触、无明显张开度和充填物。[Mo 2019, pp. 4]
- 试样节理面在制样时通过参考线水平对齐，主倾向与剪切盒一致。[Mo 2019, pp. 4]
- 反算JRC采用四个方向剪切强度的平均值，粗糙度参数选用与剪切方向无关的指标以反映全表面特征。[Mo 2019, pp. 7]
- 上下表面变形匹配良好且剪切过程基本无损伤，可用下表面形态代表耦合节理面。[Mo 2019, pp. 6]
- 法向应力水平（500 kPa/JCS）均<0.03，保证了节理面在剪切中不发生显著破坏。[Mo 2019, pp. 6, Table 4]

## Key Variables / Parameters
- 独立变量：三维粗糙度参数（θs、θg、θ2s、SsT、SsF、Van、Zsa、Zrms、Zrange），采样间隔SI（mm）。[Mo 2019, pp. 7-8]
- 因变量：节理粗糙度系数JRC，由JRC-JCS模型反算获得。[Mo 2019, pp. 1,5]
- 机械参数：基本摩擦角φb、节理壁强度JCS、峰值剪应力τ、法向应力σn。[Mo 2019, Table 4]
- 表面形态参数：实际面积At、名义面积An、三角面片倾角αij、点云高度zij、正负体积Vpi/Vgi等。[Mo 2019, pp. 2-3,8]

## Reusable Claims
- 提出的九个参数的经验方程（见核心证据表）可直接用于估算浅层新鲜节理的JRC，并考虑采样间隔影响。[Mo 2019, Table 6]
- 对于要求快速估算的工程应用，推荐使用振幅参数（Zsa、Zrms、Zrange）的方程，因其仅需点云数据，计算简便。[Mo 2019, pp. 9]
- TIN模型比3D线框模型更适合计算斜面参数，因为其所有三角面片均为平面，避免了最小二乘平面拟合的误差。[Mo 2019, pp. 7]
- θg作为阈值倾角的积分，是方向无关替代θci的有效参数，计算简单且无需拟合参数C。[Mo 2019, pp. 7]
- 当采样间隔在0.4–6.4 mm范围内时，使用体积和振幅参数估算JRC对采样间隔不敏感，可放宽对点云密度一致性的要求。[Mo 2019, pp. 9]
- 上下节理面高度参数变异<5%，剪切前后高度参数差异<2.2%，表明在低应力条件下，裂隙表面在剪切中形态变化可忽略，可用剪切前形态替代。[Mo 2019, Table 5]

## Candidate Concepts
- [[三维关节粗糙度系数]]
- [[三角不规则网络 (TIN) 模型]]
- [[3D线框模型]]
- [[表观倾角]]
- [[阈值倾角 θg]]
- [[表面斜度参数 θs, θ2s]]
- [[面积比率参数 SsT, SsF]]
- [[净体积参数 Van]]
- [[振幅参数 Zsa, Zrms, Zrange]]
- [[采样间隔敏感性]]
- [[JRC-JCS模型]]
- [[剪切方向各向异性]]
- [[点云表面重构]]
- [[节理壁强度 JCS]]
- [[基本摩擦角 φb]]

## Candidate Methods
- [[直剪试验 (多方向剪切)]]
- [[反算法计算 JRC]]
- [[激光扫描获取表面点云]]
- [[多采样间隔网格化点云]]
- [[TIN模型构建与几何参数提取]]
- [[3D线框模型构建与几何参数提取]]
- [[基于最小二乘平面的净体积计算]]
- [[多元回归建立经验方程]]
- [[施密特回弹试验测定 JCS]]
- [[倾斜试验测定基本摩擦角]]
- [[阈值面积比率积分 θg 计算]]

## Connections To Other Work
- JRC的概念和JRC-JCS模型源于Barton (1973, 1976)；标准剖面目测对比法由Barton和Choubey (1977)提出并被ISRM采纳。[Mo 2019, pp. 1]
- 现有大量基于二维剖面的JRC估算参数（如Z2、σI、Rz、λ、Dh–L等）及其回归关系被引述（Tse and Cruden 1979; Yu and Vayssade 1991; Wakabayashi and Fukushige 1992; Li and Zhang 2015等）。[Mo 2019, pp. 1-2]
- 三维粗糙度表征方面，Grasselli (2001)提出基于TIN的表观倾角参数θ*max/C，后经Cottrell (2009)修正为θ*max/(1+C)；Belem等(2000)提出整体表面角度均值θs和均方根θ2s；Lee等(2011)考虑剪切方向将θs修订为θsi，Zhang等(2009)将θ2s修订为θ2si；El-Soudani (1978)定义面积比Ss，Belem等(2000,2009)进一步发展。[Mo 2019, pp. 2-3]
- 振幅和体积参数参照ISO 25178-2标准，Fan等(2013)也曾探讨耦合节理面的三维参数。[Mo 2019, pp. 3]
- 采样间隔对二维JRC估算影响的研究（Yang等2001; Li等2016; Zheng和Qi 2016; Liu等2017）支持本文对不同参数敏感性的区分。[Mo 2019, pp. 1-2,9]

## Open Questions
- 针对其他岩石类型（如页岩、变质岩）及深度更大、应力更高的条件，经验方程的适用性尚未检验。[Mo 2019, pp. 9]
- 对于剪切过程中节理面磨损较为严重的工况，本研究所假定的表面形态不变条件可能不成立，需要进一步验证。[Mo 2019, pp. 9]
- 采样间隔超出0.4–6.4 mm范围时，方程的可靠性未知，尤其对于斜率参数，微小间隔变化可能导致JRC估算偏差较大。[Mo 2019, pp. 9]
- 提出的θg参数虽然计算简便，但在实际工程中与标准方法（如目测对比）的对比尚缺乏广泛验证。[Mo 2019, pp. 7]
- 火山岩、裂隙充填或含断层泥的节理面不适用本研究方程。[Mo 2019, pp. 4]

## Source Coverage
所有非空索引片段均已处理。共处理8个片段，覆盖39925字符，片段覆盖率100%，字符覆盖率100.05%（因索引略微冗余）。
