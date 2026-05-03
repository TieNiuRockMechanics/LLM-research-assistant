---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-wu-effect-of-flame-jet-induced-damage-on-physical-and-mechanical-properties-of-granite"
title: "Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite."
status: "draft"
source_pdf: "data/papers/2025 - Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wu, Yangchun, et al. \"Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 947-63. https://doi.org/10.1007/s00603-024-04155-3."
indexed_texts: "14"
indexed_chars: "68050"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "67475"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99155"
coverage_status: "full-index"
source_signature: "231410f7967172d0dd09ffb34c2c7994aae6e5e9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:17:08"
---

# Effect of Flame Jet-Induced Damage on Physical and Mechanical Properties of Granite.

## One-line Summary

火焰喷射在花岗岩表面产生剥落坑，并在其周围形成远大于剥落区的热损伤区，导致不同距离处试样的纵波波速、巴西劈裂抗拉强度、单轴抗压强度和弹性模量随距火焰路径距离减小而递减；基于波速和弹性模量的损伤因子可有效描述力学性能的弱化。

## Research Question

火焰喷射辅助机械破岩是实现硬岩矿山非爆破连续机械化开采的重要方法，但以往研究多集中于热剥落机理，忽视了剥落坑围岩力学性质的变化。因此，本文旨在研究火焰喷射后剥落坑围岩的物理力学性质，定量表征不同距离下花岗岩的损伤分布与强度弱化规律，并揭示其热损伤机制 [Wu 2025, pp. 1-3]。

## Study Area / Data

### 岩石材料与试样准备
- **花岗岩来源**：中国长沙，化学组成经XRF定量分析（SiO₂ 60.9%，Al₂O₃ 16.84%，K₂O 5.97%，Fe₂O₃ 5.30%，CaO 2.91%，Na₂O 2.83%，其他5.25%），完整性良好 [Wu 2025, pp. 3-4]。
- **原始物理力学参数**：未处理花岗岩的平均纵波波速3677.4 m/s，BTS 7.67 MPa，UCS 152.70 MPa，E 10.46 GPa（表1）[Wu 2025, pp. 4-6]。

### 热剥落试验系统与参数
- **火焰喷射系统**：丙烷-氧气切割枪、移动装置；丙烷流量5 NL/min，氧气流量30 NL/min，火焰功率13.6 kW；喷嘴与试样壁面距离25 mm，移动速度125 mm/min，处理时长约2分钟 [Wu 2025, pp. 3-4]。
- **热剥落结果**：花岗岩块表面形成宽约50 mm、长250 mm的剥落坑。从火焰路径两侧0、25、50、70 mm垂直距离处钻取圆柱（单轴压缩，Φ25×50 mm）和圆盘（巴西劈裂，Φ50×25 mm）试样，取样位置尽量靠近剥落坑上表面 [Wu 2025, pp. 3-4]。

## Methods

### 纵波波速测量
每块试样用纵波换能器和波速采集仪测量三次波速，涂抹凡士林保证耦合 [Wu 2025, pp. 4-6]。

### 巴西劈裂试验
- 加载速率0.001 mm/s，采用液压伺服试验机（最大荷载300 kN）。
- DIC（数字图像相关）系统记录表面应变场：试样表面制作散斑，通过相机采集照片并用MATLAB软件处理（算法见Blaber et al. 2015）。
- AE（声发射）系统监测试验过程，阈值45 dB [Wu 2025, pp. 4-6]。

### 单轴压缩试验
- 加载速率同上，仅采集AE特征，未分析DIC图像。
- 应力–应变曲线划分压实、弹性和屈服破坏阶段 [Wu 2025, pp. 6-8]。

### 数值模拟
- 采用COMSOL软件，基于Lyu et al. (2019)的20秒火焰喷射无围压花岗岩试验进行温度场模拟，验证后分析内部热应力分布。
- 模型参数：密度2620 kg/m³，比热容850 J/(kg·K)，导热系数2.647 W/(m·K)，热膨胀系数7×10⁻⁶ K⁻¹，弹性模量28 GPa，泊松比0.175等（表3）[Wu 2025, pp. 11-12]。

## Key Findings

1. **物理力学参数与距离的关系**：距火焰路径越远，试样的Vp、BTS、UCS和E越高。0 mm处平均Vp为3263.9 m/s，70 mm处升至3670.4 m/s（接近未处理值3677.4 m/s）；平均BTS从5.93 MPa增至7.53 MPa；平均UCS从98.14 MPa增至150.54 MPa；平均E从6.62 GPa升至10.28 GPa。70 mm处参数均略低于未处理试样，故该条件下火焰喷射对花岗岩的热损伤半径约为70 mm [Wu 2025, pp. 6-9]。

2. **巴西试验的DIC与AE特征**：高应变区从圆盘中心沿加载方向向两端扩展，最终形成贯穿裂纹。峰值强度时的累计AE计数随距离增加而增大（0 mm处为45.85×10⁴，70 mm处为55.45×10⁴），表明距火焰路径越近热损伤越严重 [Wu 2025, pp. 6-8]。

3. **单轴压缩的AE特征与破坏模式**：压实阶段，距火焰路径0或25 mm的试样AE计数更密集，累计AE计数增长显著，缘于近中心试样热损伤更重、微裂纹闭合更多。累计AE计数最大值随距离增大而升高（从45.73×10⁵增至59.18×10⁵）。破坏模式由远端的拉伸劈裂为主向近端的剪切破坏过渡，反映岩石从脆性向延性的转变 [Wu 2025, pp. 8-9]。

4. **热损伤因子**：基于Vp和E定义的损伤因子DVp(x)和DE(x)随距离增大而减小，与UCS和BTS的变化率趋势一致，能较好表征力学性能劣化 [Wu 2025, pp. 9-11]。

5. **热损伤机制模型**：数值模拟显示，火焰喷射期间试样表面存在高压缩应力区（导致热剥落），其下方为大范围的拉伸应力区（最大拉应力24.6 MPa）。拉应力区面积远大于压缩区，距火焰中心线越近拉应力越大，热损伤越严重。据此建立了火焰喷射下岩石热剥落与热损伤的分区模型：表面压缩应力超过UCS发生剥落，内部拉应力超过BTS产生损伤，且剥落区与损伤区之间存在未损伤区 [Wu 2025, pp. 11-14]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Vp随距离减小而降低：0 mm平均3263.9 m/s，70 mm平均3670.4 m/s | [Wu 2025, pp. 4-6, Table 1] | 火焰功率13.6 kW，丙烷5 NL/min，氧气30 NL/min，移动速度125 mm/min | 70 mm处Vp接近未处理值（3677.4 m/s） |
| BTS随距离减小而降低：0 mm平均5.93 MPa，70 mm平均7.53 MPa | [Wu 2025, pp. 6-8, Table 1, Fig. 8] | 同上，巴西圆盘Φ50×25 mm，加载速率0.001 mm/s | 70 mm处BTS与未处理（7.67 MPa）相差<2% |
| UCS随距离减小而降低：0 mm平均98.14 MPa，70 mm平均150.54 MPa | [Wu 2025, pp. 8-9, Table 1, Fig. 11] | 同上，圆柱Φ25×50 mm，加载速率0.001 mm/s | 70 mm处UCS略低于未处理（152.70 MPa） |
| E随距离减小而降低：0 mm平均6.62 GPa，70 mm平均10.28 GPa | [Wu 2025, pp. 8-9, Table 1, Fig. 11] | 同上 | 未处理E为10.46 GPa |
| 巴西试验中峰值累计AE计数随距离减小而下降：0 mm约45.85×10⁴，70 mm约55.45×10⁴ | [Wu 2025, pp. 6-8, Fig. 9] | 同上 | 距火焰近处热损伤更重 |
| 单轴压缩压实阶段近火焰路径试样AE计数更密集，累计AE计数显著增加 | [Wu 2025, pp. 8-9, Fig. 12] | 同上 | 近中心试样压实微裂纹更多 |
| 单轴压缩破坏模式：远距离为拉伸劈裂，近距离为剪切破坏 | [Wu 2025, pp. 8-9, Table 2] | 同上 | 表明热损伤导致脆性降低 |
| 损伤因子DVp和DE与UCS、BTS变化趋势一致，随距离增加而减小 | [Wu 2025, pp. 9-11, Fig. 13] | 基于Vp和E的定义 | 可用于描述力学性质劣化 |
| 数值模拟显示火焰喷射时表面为高压应力区，内部为大范围拉伸应力区（最大24.6 MPa） | [Wu 2025, pp. 11-12, Fig. 17] | 基于Lyu et al. (2019)试验验证的数值模型 | 解释损伤空间分布 |
| 热损伤区面积远大于剥落区，且二者之间存在未损伤区 | [Wu 2025, pp. 12-14, Fig. 19] | 依据压缩/UCS、拉伸/BTS准则划分 | 结合Rossi et al. (2018)的薄片观察 |

## Limitations

- 试验未考虑实际工况的三维应力状态，仅对无围压花岗岩进行火焰喷射 [Wu 2025, pp. 14-15]。
- 火焰喷射过程中未实时测量试样温度，温度场仅通过数值模拟间接获取 [Wu 2025, pp. 14-15]。
- 数值模拟的可靠性依赖已发表文献的温度验证（Lyu et al. 2019），尚未使用高精度接触或非接触传感器进行直接验证 [Wu 2025, pp. 14-15]。
- 未研究火焰喷射对剥落坑纵向方向力学性质的影响 [Wu 2025, pp. 3-4]。

## Assumptions / Conditions

- 火焰功率恒定为13.6 kW，丙烷与氧气流量固定（5 NL/min和30 NL/min），喷嘴移动速度125 mm/min [Wu 2025, pp. 3-4]。
- 热损伤评价基于距火焰路径的垂直距离（0, 25, 50, 70 mm），假设水平方向对称 [Wu 2025, pp. 3-4]。
- 数值模拟中岩石视为线弹性材料，满足准静态热弹性方程 [Wu 2025, pp. 11-12]。
- 忽略高温下岩石的化学变化，仅考虑热应力引起的损伤 [Wu 2025, pp. 9-11]。
- 实验室环境下的传热边界条件适用于模型（对流换热系数20 W/(m²·K)，辐射系数0.7）[Wu 2025, pp. 11-12]。

## Key Variables / Parameters

- 自变量：距火焰路径的垂直距离（0, 25, 50, 70 mm）
- 因变量：纵波波速Vp，巴西劈裂抗拉强度BTS，单轴抗压强度UCS，弹性模量E，AE计数及累计AE计数，DIC应变场，破坏模式
- 损伤因子：DVp(x) = 1 − [Vp(x)/Vp(x0)]²，DE(x) = 1 − E(x)/E(x0)
- 变化率：δ(σc(x)) = 1 − σc(x)/σc(x0)，δ(σt(x)) = 1 − σt(x)/σt(x0)
- 数值模拟参数：热物性（表3），热源为高斯分布q = αP/(πr₀²)·exp(−r²/r₀²)，α=0.25，r₀=2.5 cm [Wu 2025, pp. 9-12]

## Reusable Claims

1. **热损伤半径**：在火焰功率13.6 kW、移动速度125 mm/min的条件下，花岗岩的热损伤半径约70 mm（即距火焰路径70 mm处的力学参数与未处理试样相比差异可忽略）[Wu 2025, pp. 6-9]。  
2. **力学参数距离依赖性**：火焰喷射后，距火焰路径越近，花岗岩的Vp、BTS、UCS和E单调下降，且下降幅度逐渐增大 [Wu 2025, pp. 6-9]。  
3. **声发射压实特征**：单轴压缩的压实阶段，热损伤更严重的试样（距火焰近）产生更多AE计数，可作为微裂纹闭合的指标 [Wu 2025, pp. 8-9]。  
4. **损伤因子有效性**：基于Vp和E的损伤因子DVp和DE与UCS、BTS的变化率趋势一致，可用于量化火焰喷射引起的力学性能劣化 [Wu 2025, pp. 9-11]。  
5. **热损伤分布模式**：火焰喷射在岩石表面形成高压应力区导致剥落，在内部形成拉伸应力区产生损伤；拉应力区面积远大于压应力区，且两区间存在未损伤过渡区 [Wu 2025, pp. 12-14]。  
6. **破坏模式转变**：随着热损伤加重，单轴压缩破坏模式由拉伸劈裂转向剪切，脆性降低 [Wu 2025, pp. 8-9]。

## Candidate Concepts

- [[thermal spallation]]
- [[thermal damage]]
- [[flame jet-assisted mechanical rock breaking]]
- [[non-explosive continuous mechanized mining]]
- [[spalling pit surrounding rock]]
- [[damage factor]]
- [[P-wave velocity]]
- [[Brazilian tensile strength]]
- [[acoustic emission]]
- [[digital image correlation]]
- [[thermal stress distribution]]

## Candidate Methods

- [[thermal spalling test]]
- [[Brazilian test]]
- [[uniaxial compression test]]
- [[acoustic emission monitoring]]
- [[digital image correlation]]
- [[numerical simulation of thermal stress]]
- [[COMSOL multiphysics]]
- [[Vp-based damage factor]]
- [[elastic modulus-based damage factor]]

## Connections To Other Work

- 热剥落过程三阶段模型：引用Walsh et al. (2014)的起始、扩展、剥落阶段 [Wu 2025, pp. 2-3]。
- 临界表面温度与热通量条件：花岗岩热剥落需表面温度>500°C (Kant and Rudolf von Rohr 2016)，平均最低表面温度约518.3°C (Hu et al. 2019) [Wu 2025, pp. 2-3]。
- 热剥落数值模拟：Vogler et al. (2020)的模型表明钻进效率取决于火焰温度与矿物非均匀性；Meier et al. (2016)的准静态热弹性模型显示剥落速率随垂向应力线性增加 [Wu 2025, pp. 2-3]。
- 热力辅助钻进可行性：Rossi et al. (2018, 2020c)证实火焰射流弱化岩石可配合机械刀具高效破岩 [Wu 2025, pp. 2-3]。
- 高温岩石力学性质：Hu et al. (2016)、Hao et al. (2022)等报道高温后花岗岩破坏模式由拉伸劈裂向剪切转变 [Wu 2025, pp. 8-9]。
- 明火损伤距离效应：Sha et al. (2019)发现木炭加热花岗岩的Vp和BTS随距明火距离增大而升高 [Wu 2025, pp. 4-6]。
- 热损伤准则：引用Tang and Tang (2012)、Tang et al. (2015, 2016)提出的拉伸应力超过BTS即发生热损伤 [Wu 2025, pp. 12-14]。
- 非损伤区概念：Rossi et al. (2018)在经火焰处理的岩石薄片中观察到类似未损伤区 [Wu 2025, pp. 12-14]。

## Open Questions

- 不同火焰参数（功率、移动速度、距离）下热损伤区的定量演化规律尚未明确 [Wu 2025, pp. 14-15]。
- 火焰喷射辅助机械破岩中喷嘴间距、热损伤深度与刀具切削深度的合理匹配需进一步研究 [Wu 2025, pp. 14-15]。
- 在有围压的三维应力状态下，火焰喷射引起的热损伤分布与力学响应尚待试验验证 [Wu 2025, pp. 14-15]。
- 高温下不可剥落矿物的熔融对传热和损伤的影响机制及机械剥离熔渣的可行性仍需探讨 [Wu 2025, pp. 14-15]。  
- 集成火焰喷射系统的TBM等设备重新设计、安全储供燃料及工艺协调等工业应用问题尚未解决 [Wu 2025, pp. 14-15]。

## Source Coverage

本文依据14个经索引的非空文本片段编译而成，共处理67475字符，占索引总字符（68050字符）的99.16%，所有片段均已纳入，覆盖率（按字符计）为0.9916。索引签名：231410f7967172d0dd09ffb34c2c7994aae6e5e9。未使用片段的任何外部信息。
