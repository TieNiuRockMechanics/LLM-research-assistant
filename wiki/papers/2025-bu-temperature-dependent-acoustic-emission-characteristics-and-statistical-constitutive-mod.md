---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-bu-temperature-dependent-acoustic-emission-characteristics-and-statistical-constitutive-mod"
title: "Temperature-Dependent Acoustic Emission Characteristics and Statistical Constitutive Model of Granite under Uniaxial Compression."
status: "draft"
source_pdf: "data/papers/2025 - Temperature-dependent acoustic emission characteristics and statistical constitutive model of granite under uniaxial compression.pdf"
collections:
  - "zotero new"
citation: "Bu, Mohua, et al. \"Temperature-Dependent Acoustic Emission Characteristics and Statistical Constitutive Model of Granite under Uniaxial Compression.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2025, doi:10.1016/j.jrmge.2024.05.033."
indexed_texts: "17"
indexed_chars: "80694"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81032"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004189"
coverage_status: "full-index"
source_signature: "f4c8a7f7bfd36cb93ce184efd1a33a1237e8ef9a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:23:47"
---

# Temperature-Dependent Acoustic Emission Characteristics and Statistical Constitutive Model of Granite under Uniaxial Compression.

## One-line Summary

对二郎山花岗岩进行25–600 °C热处理和单轴压缩AE监测，发现物理性质持续劣化而力学性质在100–200 °C出现热强化，AE振铃计数、频率、b值强烈依赖于温度；提出引入AE参数的耦合热力损伤统计本构模型，能够拟合峰前非线性行为[Bu 2025, pp. 1-1]。

## Research Question

高温如何影响花岗岩的物理力学性质、热致裂纹演化及其声发射特征，以及如何构建能够反映温度效应和早期压实阶段的热力损伤统计本构模型[Bu 2025, pp. 1-1][Bu 2025, pp. 2-3]。

## Study Area / Data

- **样本来源**：四川二郎山隧道花岗岩，加工为直径50 mm、高100 mm的圆柱试样，共27块，取自同一岩块以保证均质性[Bu 2025, pp. 3-3]。
- **实验条件**：目标温度25、100、200、300、400、500、600 °C；加热速率0.1–2.4 °C/min，保温2 h，开炉门冷却[Bu 2025, pp. 3-4]。
- **测试数据**：热处理前后质量、体积、纵波速度；单轴压缩下应力–应变曲线、AE信号（振铃计数、振幅、频率、b值）；光学显微观察热致裂纹[Bu 2025, pp. 1-1][Bu 2025, pp. 3-4][Bu 2025, pp. 8-9]。

## Methods

- **温度曲线标定**：在试样端部钻3个垂直孔（深50 mm、直径5 mm）插入热电偶，用花岗岩粉末和耐火泥填充，实时监测加热和冷却过程中试样内部温度，获得标准热历史曲线[Bu 2025, pp. 3-3][Bu 2025, pp. 3-4]。
- **物理性质测量**：电子天平测质量，非金属超声波检测仪测纵波速度[Bu 2025, pp. 4-4]。
- **单轴压缩与AE监测**：加载速率0.025 mm/min，4个Nano30传感器采集AE信号，前置增益40 dB，门槛40 dB；AE信号分析包括振铃计数、振幅–频率特征、全局与动态b值（基于G-R关系，滑动窗口500事件、步长100事件）[Bu 2025, pp. 4-4][Bu 2025, pp. 4-6][Bu 2025, pp. 12-14]。
- **裂纹阈值确定**：采用累积AE计数与轴向应力–时间曲线方法，定义裂纹起裂应力σci和裂纹损伤应力σcd[Bu 2025, pp. 9-10]。
- **本构模型推导**：基于Weibull统计分布、Lemaitre等效应变原理，引入热损伤DT、力损伤DM和优化参数h、hTM、γ，结合温度相关的Mohr-Coulomb准则，建立耦合TM损伤本构方程；参数m和F0通过极值法求解[Bu 2025, pp. 14-20]。

## Key Findings

- **物理性质**：质量随温度单调降低（因水分蒸发和矿物颗粒脱落）；体积在600 °C急剧膨胀（膨胀率3.21%）；密度下降率逐渐增大；纵波速度非线性衰减，600 °C时下降81.75%，表明热损伤加剧[Bu 2025, pp. 4-6]。
- **力学行为**：峰值应力σp和弹性模量E在100–200 °C出现热强化（200 °C时σp增加13.21%），随后非线性下降；峰值应变εp在>200 °C后增大；600 °C时σp仅为25 °C时的56.98%；高温下应力–应变曲线非线性增强、脆性减弱、延性增加；破坏模式均为脆性拉伸劈裂，但高温下试样完整性降低、局部裂纹增多[Bu 2025, pp. 6-8]。
- **热致裂纹演化**：≤200 °C未观察到明显微裂纹；300–400 °C出现沿石英–石英、石英–长石边界的粒间裂纹；500 °C出现少量穿晶裂纹；600 °C因石英α/β相变（573 °C），石英和长石中穿晶裂纹显著增多[Bu 2025, pp. 8-9]。
- **AE振铃计数**：高温使裂纹闭合阶段AE活动增强，σci随温度升高而降低（从44.96降至17.91 MPa），归一化σci/σp减小；稳定裂纹扩展阶段（σci–σcd）延长；σcd/σp变化不明显[Bu 2025, pp. 9-10]。
- **AE振幅–频率**：主导频率先增后减（600 °C时算术平均频率降至255.43 kHz）；600 °C时低频信号占比显著增加，高频信号几乎消失至0%，表明剪切裂纹逐渐主导；不同应力水平下频率分布显示，热致裂纹与应力致裂纹相互作用导致低频成分增多[Bu 2025, pp. 10-12]。
- **b值**：全局b值在≤500 °C与25 °C相近，600 °C时显著增大（小尺度微裂纹相对比例上升）；动态b值在加载初期随温度升高信号增多、波动加剧，接近峰值应力时急剧下降，可作为破坏前兆[Bu 2025, pp. 12-14]。
- **本构模型**：提出的TM损伤统计本构模型（引入h、hTM、γ）能够良好拟合峰前压实、线弹性和裂纹扩展阶段，决定系数R²>0.98；模型参数m随温度降低（反映延性增强），F0先增后减（反映峰值强度变化）[Bu 2025, pp. 14-20]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 物理性质变化（质量损失率、体积膨胀率、密度下降率、纵波降低率定义及数值） | [Bu 2025, pp. 4-6] | 25–600 °C热处理，开炉门冷却 | 600 °C时体积膨胀率3.21%，纵波速度下降81.75% |
| 力学性质先强化后弱化（σp, E, εp归一化值） | [Bu 2025, pp. 6-8] | 加载速率0.025 mm/min | 200 °C时σp增加13.21%，600 °C时σp为56.98% |
| 热致裂纹显微观察（粒间、粒内、穿晶裂纹演化） | [Bu 2025, pp. 8-9] | 光学显微镜，25–600 °C | 573 °C石英相变导致大量穿晶裂纹 |
| AE振铃计数与应力阈值（σci, σcd值及归一化） | [Bu 2025, pp. 9-10] | 累计AE计数法 | σci从44.96降至17.91 MPa；σcd变化不显著 |
| AE振幅–频率分布（低频/中频/高频占比） | [Bu 2025, pp. 10-12] | Nano30传感器，0–10 V振幅 | 600 °C高频信号占比0%，低频显著增强 |
| 全局b值与动态b值 | [Bu 2025, pp. 12-14] | 滑动窗口500事件 | 600 °C全局b值显著增大，动态b值随应力下降 |
| 本构模型参数m和F0随温度变化 | [Bu 2025, pp. 14-20] | Weibull分布+Mohr-Coulomb | m下降，F0先增后减；峰前R²>0.98 |
| 模型验证（理论-试验曲线对比） | [Bu 2025, pp. 20-20] | 25–600 °C | 只拟合峰前，未考虑残余强度 |

## Limitations

- **本构模型范围有限**：模型仅能反映峰前应力–应变关系，未能涵盖峰后阶段和残余强度效应；未来计划考虑残余强度影响[Bu 2025, pp. 20-21]。
- **样品数量与均质性**：每组3个试样，力学性质差异可能由试样非均质性引起[Bu 2025, pp. 6-8]。
- **热处理条件未统一标准**：加热速率、恒温时间、冷却方式等因素对实验结果的影响尚未系统研究，且统计对比中前人实验条件各异[Bu 2025, pp. 8-9]。
- **AE阈值确定主观性**：裂纹阈值采用累积AE计数切线法，存在一定主观性[Bu 2025, pp. 9-10]。

## Assumptions / Conditions

- 试样均质性：所有试样取自同一花岗岩块，保证物理力学性质差异主要来源于温度处理[Bu 2025, pp. 3-3]。
- 温度均匀性：以中心钻孔（No.3）温度达到目标温度作为试样内外温度均匀的依据[Bu 2025, pp. 3-4]。
- 热损伤仅由热处理引起：假设加热过程中试样内部热应力与热反应是热致裂纹的唯一来源[Bu 2025, pp. 1-2]。
- 统计分布：假设岩石微元强度服从Weibull分布，且损伤变量由该分布积分定义[Bu 2025, pp. 14-14]。
- 等效应变原理：采用Lemaitre应变等价原理计算有效应力[Bu 2025, pp. 14-14]。

## Key Variables / Parameters

- **温度**：25, 100, 200, 300, 400, 500, 600 °C[Bu 2025, pp. 3-4]
- **物理量**：质量m, 体积V, 密度ρ, 纵波速度vp, 质量损失率ηm, 体积膨胀率ηV, 密度下降率ηρ, 纵波下降率ηvp[Bu 2025, pp. 4-6]
- **力学量**：峰值应力σp, 弹性模量E, 峰值应变εp[Bu 2025, pp. 6-8]
- **AE参数**：振铃计数RC, 累积振铃计数ARC, 振幅AdB, 主导频率（LF/IF/HF）, 全局b值, 动态b值[Bu 2025, pp. 9-14]
- **应力阈值**：裂纹起裂应力σci, 裂纹损伤应力σcd[Bu 2025, pp. 9-10]
- **本构模型参数**：Weibull形状参数m, 均值参数F0, 优化参数η, ηTM, γ, 热损伤DT, 力损伤DM, 总损伤D[Bu 2025, pp. 14-20]

## Reusable Claims

- 在100–200 °C温度区间，花岗岩因矿物颗粒膨胀、水分蒸发和裂纹闭合可出现峰值强度和弹性模量升高的热强化效应，但纵波速度仍单调下降[Bu 2025, pp. 6-8]。
- 纵波速度下降率在25–600 °C区间持续增大，600 °C时下降超过80%，可作为花岗岩热损伤程度的有效指标[Bu 2025, pp. 4-6]。
- AE累积振铃计数在裂纹闭合阶段随处理温度升高而增加，裂纹起裂应力σci及其归一化比值σci/σp随温度降低，表明热致裂纹使应力致裂纹提前萌生[Bu 2025, pp. 9-10]。
- 600 °C高温处理后，AE高频信号（>410 kHz）比例趋于零，低频信号比例显著升高，反映热致裂纹的波衰减和剪切破坏模式增强[Bu 2025, pp. 10-12]。
- 全局b值在600 °C显著增大，表明微裂纹事件相对大裂纹事件的比例上升；动态b值随加载应力增大而降低，接近峰值时急剧下降，可作为破坏前兆[Bu 2025, pp. 12-14]。
- 引入AE累积振铃计数优化的耦合TM损伤本构模型能有效描述峰前压实阶段，其中参数m表征岩石脆性，F0表征峰值强度[Bu 2025, pp. 14-20]。

## Candidate Concepts

- [[热损伤 (DT)]]
- [[热强化效应]]
- [[热致裂纹]]
- [[声发射 b 值]]
- [[动态 b 值]]
- [[裂纹起裂应力 (σci)]]
- [[裂纹损伤应力 (σcd)]]
- [[石英α/β相变]]
- [[Weibull统计分布]]
- [[Lemaitre等效应变原理]]
- [[Mohr-Coulomb准则 (温度相关)]]
- [[耦合TM损伤变量]]
- [[优化参数 η, ηTM, γ]]

## Candidate Methods

- [[标准热历史曲线标定法 (钻孔热电偶)]]
- [[纵波速度热损伤评估]]
- [[AE累积计数裂纹阈值判定法]]
- [[AE振幅-频率三频段划分 (LF/IF/HF)]]
- [[滑动窗口动态b值计算]]
- [[基于Weibull分布的统计损伤本构建模]]
- [[引入AE参数的损伤变量修正 (η = (N/Na)^(1/e))]]

## Connections To Other Work

- 多个前人研究对比了花岗岩高温后纵波速度和力学强度的归一化趋势，本研究的vp衰减和σp变化与文献统计一致[Bu 2025, pp. 6-8][Bu 2025, pp. 9-10]。
- 热强化机理参考了Yang et al. (2017), Sirdesai et al. (2017), Wong et al. (2020)等关于矿物膨胀、水分蒸发、热失配的解释[Bu 2025, pp. 8-9]。
- AE裂纹阈值确定方法继承自Ranjith et al. (2008)和Eberhardt et al. (1998)，并与其他热处理花岗岩研究比较[Bu 2025, pp. 9-10]。
- 耦合TM本构模型类似Xu and Karakus (2018)、Pathiranagei and Gratchev (2022)等基于Lemaitre原理的框架，但增加了AE参数优化压实阶段[Bu 2025, pp. 14-14]。

## Open Questions

- 热处理实验中加热速率、恒温时间、冷却方式等因素如何独立影响花岗岩的热强化/弱化效应？[Bu 2025, pp. 8-9]
- 如何在本构模型中考虑峰后残余强度，以完整描述全应力–应变曲线？[Bu 2025, pp. 20-21]
- 热致裂纹与应力致裂纹在加载过程中的相互作用机制（如抑制、促进）能否通过更精细的AE源定位或频谱特征量化？[Bu 2025, pp. 10-12]
- 动态b值作为破坏前兆的阈值和普适性是否需要在更大样本和不同岩石类型中验证？[Bu 2025, pp. 12-14]
- 600 °C以上至更高温度段，纵波速度下降速率减缓，但热损伤是否继续以新型裂纹形式累积？[Bu 2025, pp. 6-6]

## Source Coverage

所有非空索引片段（17个片段，共81032字符）均已处理并编译进本页面。覆盖比例：按片段数为1.0，按字符数为1.004189。未引入任何片段外信息。
