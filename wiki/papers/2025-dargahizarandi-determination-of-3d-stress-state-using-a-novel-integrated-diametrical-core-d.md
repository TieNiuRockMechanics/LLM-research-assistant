---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-dargahizarandi-determination-of-3d-stress-state-using-a-novel-integrated-diametrical-core-d"
title: "Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis."
status: "draft"
source_pdf: "data/papers/2025 - Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.pdf"
collections:
  - "zotero new"
citation: "Dargahizarandi, Atefeh, et al. \"Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 4377-4401, doi:10.1007/s00603-025-04427-6. Accessed 2026."
indexed_texts: "14"
indexed_chars: "69367"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "68861"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.992705"
coverage_status: "full-index"
source_signature: "7f5142100526608f2131fcb5c856616516ab2930"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:00:16"
---

# Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.

## One-line Summary
提出了一种融合直径岩心变形分析（DCDA）与超声波速度映射的实验室新方法，可依据岩心样本测定完整三维应力张量（含方位角、倾角与大小），并在澳大利亚地下金属矿中经套芯应力测量验证有效 [Dargahizarandi 2025, pp. 1-2; 4-6; 17-19]。

## Research Question
现有基于岩心的应力测量方法（如ASR、DSCA、DRA、AE）往往仅限于二维应力状态且存在较大不确定性，而DCDA虽提升了可靠性但同样仅适用于二维情形；如何从岩心确定完整的三维应力状态（三个主应力的大小、方位角与倾角）仍然缺乏整合的方案 [Dargahizarandi 2025, pp. 2-4]。

## Study Area / Data
– **位置**：澳大利亚昆士兰Dugald River锌-铅-银矿床，距Cloncurry西北约65 km。  
– **钻孔与岩心**：两个近垂直钻孔（Borehole 1 深度490～665 m，Borehole 2 深度590～715 m），共采集8个均质、无明显缺陷的岩心（直径约50 mm，长径比≈2） [Dargahizarandi 2025, pp. 8-9]。  
– **对比数据**：5个现场套芯应力测量点（其中一处与Borehole 1位置重叠），应力大小、方位角与倾角均已知；同时引用Mount Isa区域的线性应力曲线作为区域参考 [Dargahizarandi 2025, pp. 17-19]。

## Methods
1. **直径分析 (DCDA)**：利用自行搭建的高分辨率激光扫描装置（分辨率0.1 μm）对岩心进行360°周向扫描，每隔8°记录直径，拟合正弦函数，峰值和谷值方向分别对应最大和最小（或中间）主应力的方位角 [Dargahizarandi 2025, pp. 10-12]。  
2. **弹性参数测定**：在同一样品上开展单轴压缩试验（仅弹性阶段），由轴向应变计与环向引伸计获得杨氏模量和泊松比 [Dargahizarandi 2025, pp. 9-10]。  
3. **倾角测定 (超声波映射)**：从大岩心上沿两个已识别的方位方向，以0°、25°、50°、75°、90°钻取直径12 mm的小岩心；采用1 MHz压电换能器进行透射波速测量，利用维纳滤波与AIC算法拾取P波初至，得到不同倾角下的归一化波速；最小波速方向指向最大主应力倾角，最大波速方向指向最小或中间主应力倾角 [Dargahizarandi 2025, pp. 12-16]。  
4. **应力大小估算**：基于Li & Mitri (2023a)的解析模型（式2–4），利用最大/最小直径计算平面上双轴应力；考虑到所研究矿山垂直应力近似与钻孔轴一致，故直接采用该模型；最终将水平面应力转换至由倾角确定的实际主平面，获得S1, S2, S3 [Dargahizarandi 2025, pp. 6-8; 16-17]。  
5. **验证**：对比同一位置套芯测量结果，并利用归一化应力 ($\sigma_{NL} = \frac{E_N}{E_M} (\sigma_{ML} - \frac{\sigma_v \nu}{1-\nu}) + \frac{\sigma_v \nu}{1-\nu}$) 与Mount Isa区域曲线进行比较 [Dargahizarandi 2025, pp. 19-20]。

## Key Findings
- 8个岩心的直径扫描均呈现良好的正弦变化，最大/最小直径方向明确指示了主应力方位角 [Dargahizarandi 2025, pp. 13-14]。  
- 超声波速度随倾角变化与理论预期一致：最大主应力倾角处波速最低（多接近0°），另一主应力倾角处波速最高；其结果与同一样品不同角度单轴压缩测得的杨氏模量趋势相符 [Dargahizarandi 2025, pp. 14-16]。  
- 推算的三维应力状态（表1）与邻近套芯测量结果高度吻合：例如在Borehole 1深度约533 m处，核心法测得S1=20 MPa (方位121°, 倾角0°), S2=13.2 MPa (149°, 12°), S3=10 MPa (206°, 78°)，而同一位置（深度478 m）的套芯结果为S1=18.1 MPa，S2=16.7 MPa，S3=9.9 MPa，倾角分别为3°、4°、85° [Dargahizarandi 2025, pp. 17-18]。  
- 归一化应力随深度分布与Mount Isa地区线性应力曲线吻合良好，表明方法具有区域一致性 [Dargahizarandi 2025, pp. 19-20]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 直径正弦变化可指示主应力方位 | [Dargahizarandi 2025, pp. 13-14, Fig. 11-12] | 均质、各向同性岩心；核心释放后弹性膨胀；主应力与孔轴垂直或斜交 | 方位角从激光扫描的拟合正弦波的峰/谷角读取 |
| 最小P波速度方向对应最大主应力倾角 | [Dargahizarandi 2025, pp. 15-16, Fig. 15] | 微裂隙发育由应力释放控制；其它各向异性因素可排除 | 需多角度取样(0°,25°,50°,75°,90°) |
| 解析模型可估计双轴应力大小 | [Dargahizarandi 2025, pp. 6-8] | 弹性小变形；垂直应力近似为另一主应力；忽略剪切变形对直径的影响 | 使用最大/最小直径及弹性常数计算 |
| 归一化应力与Mount Isa线性曲线一致 | [Dargahizarandi 2025, pp. 19-20, Fig. 20] | 考虑杨氏模量变化的影响 | 公式 $\sigma_{NL} = \frac{E_N}{E_M} (\sigma_{ML} - \frac{\sigma_v \nu}{1-\nu}) + \frac{\sigma_v \nu}{1-\nu}$ |
| 倾角结果与同角度单轴压缩模量趋势一致 | [Dargahizarandi 2025, pp. 14-16, Fig. 14] | 仅针对样品4进行了验证 | 最小模量对应最大主应力倾角，最大模量对应最小主应力倾角 |

## Limitations
- 高度非均质岩心会影响周向直径扫描的精度与可重复性 [Dargahizarandi 2025, pp. 19-20]。  
- 超声波测量需从主岩心上钻取多角度子样，步骤较繁琐；可通过宽频换能器与多通道系统改善，但原文尚未实现 [Dargahizarandi 2025, pp. 19-20]。  
- 对未在矿山模型中识别的潜在构造（如Borehole 1深度632 m处方位角偏差），难以溯源解释 [Dargahizarandi 2025, pp. 17-18]。  
- 目前仅在一个地下金属矿进行了验证，普适性有待进一步检验。

## Assumptions / Conditions
- 岩石为均质、各向同性，并处于线弹性小变形状态 [Dargahizarandi 2025, pp. 6-8]。  
- 剪切应变对岩心长度和直径的影响可忽略，即应力释放导致的变形以正应变为主 [Dargahizarandi 2025, pp. 5-6]。  
- 垂直应力近似与钻孔轴平行，因此可直接使用Li & Mitri (2023a)的二维解析解计算水平面应力，再转换至实际主平面 [Dargahizarandi 2025, pp. 7-8]。  
- 超声波速度的各向异性主要来源于应力释放诱发的微裂隙，而非岩石原生结构 [Dargahizarandi 2025, pp. 12-13]。  
- 岩心膨胀引起的直径变化足够被0.1 μm分辨率的激光传感器检测到 [Dargahizarandi 2025, pp. 10-11]。

## Key Variables / Parameters
- **测量变量**：周向直径 d(θ)；P波走时及其归一化速度；杨氏模量 E；泊松比 ν。  
- **导出参数**：最大直径 dmax、最小直径 dmin；原始直径 d0（由式(4)或(8)反算）；双轴应力 σH, σh；主应力 S1, S2, S3 的大小、方位角、倾角。  
- **辅助指标**：归一化应力 σNL；归一化杨氏模量（单角度/平均）；归一化波速（单角度/平均）。

## Reusable Claims
1. **方位角判定**：“DCDA 周向扫描得到的最大直径方向与最大水平主应力方向一致，最小直径方向与最小水平主应力方向一致” [Dargahizarandi 2025, pp. 4-6]，前提是岩石均质且各向同性。  
2. **倾角判定**：“超声波P波速度在最大主应力倾角方向最低，在最小主应力倾角方向最高” [Dargahizarandi 2025, pp. 6-8, 15-16]，适用条件为应力释放产生的微裂隙主导速度各向异性。  
3. **应力大小算式**：“利用式 (2)–(4) 可由 dmax, dmin, d0 及 E, ν 估算与孔轴垂直平面内的双轴应力” [Dargahizarandi 2025, pp. 7-8]。  
4. **垂直应力省略**：“当垂直应力远小于水平应力或可忽略时，式 (4) 足以计算双轴应力” [Dargahizarandi 2025, pp. 8-9]。  
5. **验证一致性**：“归一化应力与区域线性应力曲线的吻合可作为方法可靠性的间接佐证” [Dargahizarandi 2025, pp. 19-20]。

## Candidate Concepts
- [[diametrical core deformation analysis (DCDA)]]
- [[ultrasonic mapping for stress dip angle]]
- [[3D in-situ stress tensor estimation]]
- [[core expansion after stress release]]
- [[sinusoidal diameter variation]]
- [[P-wave velocity anisotropy]]
- [[normalised stress magnitude]]
- [[overcoring validation]]

## Candidate Methods
- [[laser circumferential scanning (0.1 μm resolution)]]
- [[Wiener filter denoising for ultrasonic signals]]
- [[AIC arrival picking for P-wave]]
- [[analytical biaxial stress solution (Li & Mitri 2023a)]]
- [[normalisation of stress magnitude using Young’s modulus]]
- [[multi-angle small-core drilling for ultrasonic dip measurement]]
- [[uniaxial compression testing for elastic constants]]

## Connections To Other Work
- 引用 Funato & Ito (2017) 提出的基本 DCDA 方法，本文在其基础上扩展至三维 [Dargahizarandi 2025, pp. 4-5]。  
- 引用 Li & Mitri (2023a) 的解析解，并修改以纳入垂直应力影响 [Dargahizarandi 2025, pp. 7-8]。  
- 比较了现有实验室应力方法：ASR (Voight 1968; Teufel 1983)、DSCA (Strickland & Ren 1980)、DRA (Yamamoto et al. 1990)、AE/Kaiser效应 (Kanagawa et al. 1977)，指出它们的局限（如温度影响、微裂隙过多、需高应力等） [Dargahizarandi 2025, pp. 2-4]。  
- 提及 Ziegler & Valley (2021) 用摄影测量评估 DCDA 并考虑各向异性，以及现场方法如水力致裂、套芯、钻孔崩落 [Dargahizarandi 2025, pp. 2-3]。

## Open Questions
- 未探明的小尺度构造或节理如何影响直径扫描和超声波响应？Borehole 1 在 632 m 处的方位角偏差是否由隐伏断层引起？[Dargahizarandi 2025, pp. 17-18]  
- 在更不均质或层状岩石（如页岩、片麻岩）中，该方法的假设（各向同性、剪切应变可忽略）是否依然成立？  
- 能否通过宽频换能器和多通道采集实现无子样钻取的超声波倾角测量，从而简化流程并减少样品损坏？[Dargahizarandi 2025, pp. 19-20]  
- 该方法在不同构造环境（如逆冲、走滑）下的适用性及通用校准策略？目前仅在一个矿区进行了验证。

## Source Coverage
全部 **14 个非空索引片段**（共 68,861 字符）均已被处理。  
- 源块数量：14  
- 字符总数：68,861  
- 覆盖率（按块）：1.0  
- 覆盖率（按字符）：0.9927  
- 源签名：7f5142100526608f2131fcb5c856616516ab2930  
所有片段均用于构建本页面，未引入任何未索引的外部事实。
