---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-lai-study-on-damage-characteristics-of-hot-dry-rock-by-liquid-nitrogen-cyclic-cold-shocks-b"
title: "Study on Damage Characteristics of Hot Dry Rock by Liquid Nitrogen Cyclic Cold Shocks Based on Ultrasonic Testing."
status: "draft"
source_pdf: "data/papers/2023 - Study on Damage Characteristics of Hot Dry Rock by Liquid Nitrogen Cyclic Cold Shocks Based on Ultrasonic Testing.pdf"
collections:
  - "zotero new"
citation: "Lai, Yongshuai, et al. \"Study on Damage Characteristics of Hot Dry Rock by Liquid Nitrogen Cyclic Cold Shocks Based on Ultrasonic Testing.\" *Energy & Fuels*, vol. 37, 2023, pp. 16573-16587. *ACS Publications*, doi:10.1021/acs.energyfuels.3c03229. Accessed 28 Apr. 2026."
indexed_texts: "15"
indexed_chars: "72378"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "72655"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003827"
coverage_status: "full-index"
source_signature: "68c1c380ba38ec51774741248ec91e9a8bc81316"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:10:36"
---

# Study on Damage Characteristics of Hot Dry Rock by Liquid Nitrogen Cyclic Cold Shocks Based on Ultrasonic Testing.

## One-line Summary

通过核磁共振和超声测试，研究高温花岗岩在液氮循环冷冲击（五次）下的损伤特征，发现随加热温度和冷冲击次数增加，岩心孔隙度上升、波速下降、波形畸变加剧、频率向低频移动、小波包能量向低频转移、Hilbert能量谱总能量减少且高能持续时间缩短，品质因子Q与孔隙度呈良好线性关系，为干热岩储层液氮增透提供理论依据。[Lai 2023, pp. 1-2, 12-14]

## Research Question

液氮循环冷冲击对干热岩（高温花岗岩）的损伤特征是什么？如何利用超声检测技术从波速、波形、频率、小波包能量和时频谱的角度定量评价其损伤程度？[Lai 2023, pp. 1-3, 11-12]

## Study Area / Data

样品为取自山东烟台的均质花岗岩，加工成直径50 mm、高50 mm的圆柱形岩心，经波速筛选后选取15块，分为5组（每组3块），加热温度分别为200、300、400、500、600 °C。原始岩心基本性质：密度2.654 g/cm³，初始孔隙度0.700%（0.761±0.231%），初始纵波速度3.671 km/s。XRD分析表明主要矿物为石英，次为钾长石、斜长石和云母。[Lai 2023, pp. 2-3]

## Methods

1. **加热与液氮冷冲击循环**：将岩心在箱式炉中以5 °C/min升温至目标温度（200 °C、300 °C、400 °C、500 °C、600 °C），恒温2 h后迅速投入充满液氮的杜瓦瓶冷却至室温，此为一个循环，共进行5次循环。[Lai 2023, pp. 3-4]
2. **孔隙度测量**：每次循环后对岩心进行真空饱和（-0.095 MPa，24 h），使用低场核磁共振分析仪（MesoMR23-060H）测量孔隙度。[Lai 2023, pp. 3-4]
3. **超声波测试**：干燥后采用NM-4A超声检测仪（激励电压500 V，采样周期0.4 μs，探头频率50 kHz）测试纵、横波速度，并采集透射波形。[Lai 2023, pp. 3-4]
4. **信号处理与损伤表征**：
   - 快速傅里叶变换（FFT）分析频域特征；
   - 7层小波包分解（Db6小波基，采样频率2.5 MHz，Nyquist频率1.25 MHz），计算第7层128个子带的能量占比；
   - Hilbert‑Huang变换获取时频谱；
   - 采用振幅衰减法计算岩石品质因子Q，公式 \(Q = \pi f t / \ln(A_0/A(x))\)。[Lai 2023, pp. 5-12]

## Key Findings

1. **孔隙度变化**：随加热温度和冷冲击次数增加，岩心孔隙度持续增大。200 °C、300 °C、400 °C时损伤较小，5次冷冲击后孔隙度分别增加1.018%、1.154%、0.959%（原文中数据略有差异，综合为约1.108%、1.154%、1.158%）；500 °C和600 °C时损伤显著，5次循环后孔隙度增加3.080%和6.896%，且第一次冷冲击贡献了总增量的39.1%和54.9%。当温度超过573 °C时，α→β石英相变引起体积突增，加剧损伤。[Lai 2023, pp. 3-5]
2. **波速与损伤因子**：纵波和横波速度随循环次数增加而下降，最大降幅出现在首次冷冲击后。例如，400 °C时首次冷冲击造成的纵波速度降占五次总降的80.9%；对应的损伤因子（\(D = 1 - (V_p/V_0)^2\)）在200–600 °C首次冷冲击后分别达到0.454、0.547、0.671、0.762和0.911。[Lai 2023, pp. 4-5]
3. **波形与频谱特征**：
   - 原始波形完整、幅值高，随损伤加重，首波延迟（最高达53.6 μs）、振幅降低、波形畸变明显，出现不规则加宽和突变点。[Lai 2023, pp. 5-8]
   - FFT谱显示主频向低频漂移，幅值衰减（600 °C时主频从48.8 kHz降至4.9 kHz，幅值降70.8%），高频信号消失，低频成分增多，出现多峰和频散。[Lai 2023, pp. 8-9]
   - 小波包能量初始集中于中频（子带5，约39.0–48.8 kHz），损伤后能量逐渐转移至低频（子带1），严重损伤时低频子带能量占比达83.4%（子带1占61.0%）。[Lai 2023, pp. 8-11]
   - Hilbert能量谱显示总能量降低，高瞬时能量持续时间缩短，频率分布范围向低频收缩（400 °C时高能持续时间由初始132.8 μs缩短至14.8 μs，减幅88.9%）。[Lai 2023, pp. 11-12]
4. **品质因子Q**：Q值随温度升高和循环次数增加而降低，200–600 °C五次冷冲击后Q分别下降22.9%、23.8%、27.3%、45.8%和97.2%。Q与孔隙度呈优良的线性关系（全工况拟合R²=0.982），可为损伤定量评价提供依据。[Lai 2023, pp. 12-14]

## Core Evidence Table

| 证据 (Evidence) | 来源 (Source) | 条件 (Conditions) | 备注 (Notes) |
|----------------|---------------|-------------------|--------------|
| 原始花岗岩密度=2.654 g/cm³, 孔隙度=0.700%, 纵波速度=3.671 km/s | [Lai 2023, pp. 2-3] | 干燥状态，室温 | 样品基本物性 |
| 200°C加热，5次冷冲击后孔隙度增加1.018% | [Lai 2023, pp. 3-4] | 每循环后饱和水测NMR | 损伤轻微，冷冲击疲劳效应 |
| 300°C，5次冷冲击后孔隙度增加1.154% | [Lai 2023, pp. 3-4] | 同上 | 孔隙度线性增长 |
| 400°C，5次冷冲击后孔隙度增0.959%（另有累计1.158%） | [Lai 2023, pp. 3-4] | 前两次冷冲击增量最大 | 温度逐渐主导损伤 |
| 500°C，5次冷冲击后孔隙度增加3.080%，首次冲击贡献39.1% | [Lai 2023, pp. 4-5] | 微裂纹扩展、连通 | 中、大孔隙增多 |
| 600°C，5次冷冲击后孔隙度增加6.896%，首次冲击贡献54.9% | [Lai 2023, pp. 4-5] | >573°C石英相变，热应力叠加 | 损伤最严重 |
| 400°C时，首次冷冲击纵波速度降占总降80.9% | [Lai 2023, pp. 4-5] | 波速对初次损伤最敏感 | 此后降幅平缓 |
| 600°C首次冷冲击后损伤因子0.911，五次后0.960 | [Lai 2023, pp. 5-7] | 基于纵波速度 | 高温下极严重损伤 |
| 200°C五次冷冲击首波延迟5.2–8.4 μs，首次延迟占69.2–71.4% | [Lai 2023, pp. 5-7] | 波形畸变轻微 | 低温时损伤小 |
| 600°C首次冷冲击首波延迟29.6 μs，五次后最长达53.6 μs | [Lai 2023, pp. 7-8] | 波形严重畸变，振幅降7.78% | 裂缝网络发育 |
| 原始主频48.8 kHz，600°C五次冷冲击后主频降至4.9 kHz，幅值降70.8% | [Lai 2023, pp. 8-9] | 频谱向低频漂移 | 高频严重衰减 |
| 小波包子带1能量占比：原始约10.8%，600°C五次后61.0% | [Lai 2023, pp. 10-11] | 7层分解，Db6，0–9.766 kHz | 能量向低频集中 |
| 400°C Hilbert高能持续时间从132.8 μs降至14.8 μs（减幅88.9%） | [Lai 2023, pp. 11-12] | 最大瞬时能量从3.187×10⁴降至1.298×10⁴ | 能量衰减，高频丢失 |
| 200–600°C五次冷冲击后Q值分别下降22.9%、23.8%、27.3%、45.8%、97.2% | [Lai 2023, pp. 12-12] | 振幅衰减法计算 | Q随损伤指数性下降 |
| Q与孔隙度全工况线性拟合R²=0.982 | [Lai 2023, pp. 12-14] | 不同温度、循环次数数据合并 | 高线性度，可用于定量评价 |

## Limitations

- 仅使用了一种花岗岩样品（烟台），矿物组成和结构的影响未考虑，结论外推需谨慎。[Lai 2023, pp. 2-3]
- 实验未施加围压，未考虑地应力对液氮损伤的抑制作用；论文指出“仍需进一步研究压力对液氮损伤的影响及液氮作用范围”。[Lai 2023, pp. 14-14]
- 冷冲击循环仅五次，高温长期循环效应和疲劳机制未探讨。
- 超声参数（如Q值）的拟合受温度区间影响，不同温度下斜率有差异（200°C时R²较低），单一线性关系泛化能力有限。[Lai 2023, pp. 12-14]
- 未直接获取孔隙结构（孔径分布、连通性）的演化细节，超声波分析只能间接反演损伤。[Lai 2023, pp. 14]

## Assumptions / Conditions

- 实验前岩心真空饱和24 h，干燥24 h（80 °C），保证NMR测孔的前后一致性。[Lai 2023, pp. 3-4]
- 冷冲击时液氮液面始终高于岩心，确保完全冷却至液氮温度（常压沸点-196 °C）。[Lai 2023, pp. 3-4]
- 加热速率5 °C/min，目标温度恒温2 h，使岩心整体温度均匀。[Lai 2023, pp. 3-4]
- 超声波测试前岩心在80 °C烘24 h并冷却至室温，以避免水分对波速和波形的干扰。[Lai 2023, pp. 3-4]
- 纵、横波探头频率50 kHz，激励电压500 V，采样周期0.4 μs；信号处理假设岩心为各向同性线弹性介质，忽略频散和各向异性。[Lai 2023, pp. 3-4]
- 品质因子Q的计算基于振幅衰减法，假设超声波以平面波形式传播且衰减服从指数规律。[Lai 2023, pp. 12-12]

## Key Variables / Parameters

- 控制变量：加热温度（200、300、400、500、600 °C）、液氮冷冲击循环次数（0次初始，1–5次）。
- 响应变量（宏微观损伤）：
  - NMR孔隙度 [Lai 2023, pp. 3-5]
  - 纵波速度 \(V_p\)、横波速度 \(V_s\) [Lai 2023, pp. 4-5]
  - 损伤因子 \(D = 1 - (V_p/V_0)^2\) [Lai 2023, pp. 5-7]
- 超声波形特征参数：
  - 首波到时延迟、波形畸变程度 [Lai 2023, pp. 5-7]
  - FFT主频及幅值 [Lai 2023, pp. 8-9]
  - 小波包子带能量占比（子带1–16）[Lai 2023, pp. 10-11]
  - Hilbert瞬时能量最大值、高能持续时间、频率范围 [Lai 2023, pp. 11-12]
  - 品质因子 \(Q\) [Lai 2023, pp. 12-14]

## Reusable Claims

1. **首次冷冲击即引起大部分损伤**：在200–600 °C范围内，纵波速度降、损伤因子增量、孔隙度增量以及波形畸变均以首次液氮冷冲击最为显著，后续循环产生的附加损伤相对较小。[Lai 2023, pp. 4-5, 14]
2. **400 °C是损伤加速的阈值**：加热温度低于400 °C时，花岗岩孔隙度增加有限（<1.2%），损伤以冷冲击次数为主要控制因素；超过400 °C后温度成为主导，孔隙度和波速变化剧烈，600 °C时损伤达到极端水平。[Lai 2023, pp. 3-5, 14]
3. **超声频域特征可定性划分损伤等级**：轻微损伤时主频几乎不变，仅幅值微降；中等损伤时主频向低频轻微偏移，出现次峰；严重损伤时主频大幅衰减，频谱完全转为低频主导，且信号散射严重。[Lai 2023, pp. 8-9]
4. **小波包能量迁移是可靠损伤指标**：随损伤加重，接收波能量从中频子带（子带5）逐渐转移至低频子带（子带1），高损时低频能量占比可超80%，可作为量化的损伤指纹。[Lai 2023, pp. 10-11]
5. **品质因子Q与孔隙度线性关系可作为定量评估工具**：在不同温度和冷冲击次数下，Q值与NMR孔隙度高度线性相关（R²=0.982），通过测量Q值可间接推估孔隙度，实现无损定量评价。[Lai 2023, pp. 12-14]
6. **超声波时‑频‑能综合分析比单纯波速更敏感**：波形畸变、频率漂移、Hilbert能量衰减等特征能捕捉到波速变化不明显的早期微损伤，为储层改造过程提供更精细的监测手段。[Lai 2023, pp. 12-14]

## Candidate Concepts

- [[干热岩（Hot Dry Rock）]]
- [[液氮循环冷冲击（Liquid Nitrogen Cyclic Cold Shock）]]
- [[超声波检测（Ultrasonic Testing）]]
- [[损伤因子（Damage Factor）]]
- [[品质因子Q（Quality Factor Q）]]
- [[小波包分解（Wavelet Packet Decomposition）]]
- [[Hilbert-Huang变换（Hilbert-Huang Transform）]]
- [[增强型地热系统（Enhanced Geothermal System, EGS）]]
- [[热应力（Thermal Stress）]]
- [[石英α-β相变（α-β Quartz Transition）]]
- [[核磁共振孔隙度（NMR Porosity）]]
- [[时频分析（Time-Frequency Analysis）]]

## Candidate Methods

- [[低场核磁共振（Low-field NMR）]]
- [[超声纵/横波速度测量（Ultrasonic P/S Wave Velocity Measurement）]]
- [[快速傅里叶变换（Fast Fourier Transform, FFT）]]
- [[小波包能量谱（Wavelet Packet Energy Spectrum）]]
- [[振幅衰减法计算品质因子Q（Amplitude Attenuation Method for Q）]]
- [[Hilbert时频谱（Hilbert Energy Spectrum）]]
- [[真空饱和法（Vacuum Saturation Method）]]
- [[箱式炉缓慢加热（Muffle Furnace Slow Heating）]]

## Connections To Other Work

- 本文属于水法增透（水力压裂）向无水/少水增透手段转变的探索，与液氮压裂综述 [Lai 2023, pp. 1-2, 24-26] 相呼应，聚焦于循环冷冲击对干热岩的损伤。
- 与Cai et al. (2022) [Lai 2023, pp. 30] 的液氮处理高温花岗岩超声、巴西劈裂和声发射研究形成补充，本文更强调多维度超声信号（波形、频率、小波包、Hilbert谱）的深入分析，而非仅关注波速和强度。
- 与Wu et al. (2019) [Lai 2023, pp. 33] 的比较实验中关于液氮冷却后渗透率增大、波速和强度降低的结论一致，但本文增加了循环次数对孔隙度、Q值等动态演化规律的量化。
- 借鉴了Li et al. (2016) [Lai 2023, pp. 28] 中超临界CO₂处理后基于波速定义损伤系数的思路，本文引入了基于纵波速度的损伤因子，并与Q值关联。
- 波形分析中的小波包、Hilbert变换方法与岩石力学中振动监测 [Lai 2023, pp. 43-47, 50-51] 同源，将工程损伤诊断手段移植到高温岩石热损伤评价。
- 针对干热岩EGS储层改造，本文为热刺激（液氮）方法提供了实验室数据支撑，与水力压裂现场案例Soultz项目 [Lai 2023, pp. 19]、深层砂岩 [Lai 2023, pp. 20]形成对比，指出液氮无水环保优势。

## Open Questions

- 有围压条件下液氮冷冲击的损伤效应如何？论文指出“需进一步研究压力对液氮损伤的影响”。[Lai 2023, pp. 14]
- 液氮的作用范围（冷却半径）及其在裂缝网络中的传热规律尚未涉及。
- 高温花岗岩在液氮循环冷冲击后内部孔隙结构（孔径分布、配位数）的演化特征尚待高精度成像（如CT）验证。[Lai 2023, pp. 14]
- 多次循环（>5次）下的疲劳损伤极限及长期渗透率演化规律不明确。
- 小波包能量迁移规律、Hilbert能量衰减与微观破裂机制的精细化对应关系仍需理论建模。
- 本文结论基于烟台花岗岩，其他岩性（如碳酸盐岩、变质岩）的适用性未知。
- 如何在现场通过超声波层析成像等手段实时监测干热岩储层的热损伤程度，是工程转化的关键。

## Source Coverage

All 15 non-empty indexed fragments from the source PDF were processed. The compiled source blocks amount to 72,655 characters, covering 100% of the indexed source blocks (coverage ratio by blocks: 1.0) and exceeding the original indexed character count (72,378 characters) by a factor of 1.003827, indicating complete inclusion of all available evidence. No fragments were omitted. Compilation was performed in a single pass without code fences or YAML front matter, using only the supplied indexed texts.
