---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected"
title: "Experimental Investigation on Physical and Mechanical Properties of Granite Subjected to Cyclic Heating and Liquid Nitrogen Cooling."
status: "draft"
source_pdf: "data/papers/2021 - Experimental Investigation on Physical and Mechanical Properties of Granite Subjected to Cyclic Heating and Liquid Nitrogen Cooling.pdf"
collections:
  - "zotero new"
citation: "Rong, Guan, et al. \"Experimental Investigation on Physical and Mechanical Properties of Granite Subjected to Cyclic Heating and Liquid Nitrogen Cooling.\" *Rock Mechanics and Rock Engineering*, vol. 54, 2021, pp. 2383-2403. doi:10.1007/s00603-021-02390-6."
indexed_texts: "16"
indexed_chars: "77337"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "76567"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990044"
coverage_status: "full-index"
source_signature: "53681bd4cff11628a384cff4cc534c3f902b7bc6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:16:10"
---

# Experimental Investigation on Physical and Mechanical Properties of Granite Subjected to Cyclic Heating and Liquid Nitrogen Cooling.

## One-line Summary
以循环加热（300°C）与两种冷却方式（液氮骤冷、空气缓冷）处理花岗岩，系统对比其物理力学性质演化，发现液氮冷却使损伤集中在前约12次循环，随后趋于饱和，且损伤程度显著高于空气冷却。

## Research Question
循环液氮（LN₂）冷却对高温花岗岩的物理性质（质量、体积、密度、孔隙率、P波速度）和力学性质（抗压、抗拉强度、变形参数、应力阈值）的退化规律与损伤机理是什么？与空气冷却相比，差异如何？

## Study Area / Data
- **岩性**：花岗岩，取自湖北麻城矿山，主要矿物为微斜长石（39.56%）、钠长石（30.97%）、石英（20.45%）、白云母（7.23%）、绿泥石（1.79%）［Rong 2021, pp. 3-4］。
- **初始物理力学性质**（均值±标准差）［Rong 2021, pp. 3-4］：
  - 密度 ρ = 2.61 ± 0.02 g/cm³
  - 孔隙率 n = 0.82 ± 0.01%
  - P波速度 Vp = 4430 ± 26 m/s
  - 杨氏模量 E = 70.11 ± 3.47 GPa
  - 巴西抗拉强度 BTS = 5.42 ± 0.18 MPa
  - 单轴抗压强度 UCS = 160.37 ± 6.18 MPa
- **样品规格**：圆柱样 Φ50×100 mm，圆盘样 Φ50×25 mm，端面平整度 <0.02 mm，肉眼无可见缺陷［Rong 2021, pp. 3-4］。

## Methods
1. **循环加热–冷却处理**：箱式电阻炉以5°C/min缓慢加热至300°C（防止热冲击），恒温4 h后，分别进行液氮冷却（LG，浸入约‑196°C LN₂）和空气冷却（AG，环境大气中自然冷却）。循环次数：0（未处理）、1、3、6、12、18、24，每种条件3个重复样［Rong 2021, pp. 3-4］。
2. **物理性质测试**：每次循环前后测量质量M（0.01 g精度）、尺寸（三次取均值）计算体积V与密度ρ；真空饱和法（0.1 MPa抽真空24 h，烘干称重）按ISRM建议获取孔隙率n；基于超声脉冲传输技术（RSM-SY5(T)声波检测仪）测量P波速度Vp，每样重复5次取均值［Rong 2021, pp. 4-5］。
3. **力学试验**：
   - 巴西劈裂（200 N/s加载速率）得抗拉强度σt；单轴压缩（0.02 mm/min轴向变形控制）配置轴向/侧向LVDT和DS2全信息声发射（AE）仪（8传感器对称布置，增益40 dB，门槛50 dB）［Rong 2021, pp. 4-7］。
   - 应力阈值确定：裂纹闭合应力σcc用轴向应变响应法，裂纹起始应力σci用侧向应变响应法，裂纹损伤应力σcd用体积应变法［Rong 2021, pp. 9-10］。
4. **微观观察**：制备薄片（2.5 mm边长，~0.03 mm厚），Olympus BX53M偏光显微镜50×下识别粒间和粒内微裂纹，并测量裂纹宽度［Rong 2021, pp. 13-14］。
5. **损伤变量**：D(I)=1−Iₙ/I₀，I为UCS、BTS、E、Vp等参数［Rong 2021, pp. 14-17］。

## Key Findings
- **循环与冷却的协同效应**：无论冷却方式，循环次数增加均导致物理力学性质持续劣化（n↑，Vp↓，强度↓，E↓，εp↑），且可用指数函数良好拟合［Rong 2021, pp. 7-9, 14-17］。
- **液氮冷却加剧损伤**：液氮骤冷引起的冷冲击产生更高热应力，使LG样品的各指标降幅更大（如24次循环后UCS衰减24.8% vs AG的16.0%；BTS衰减53.5% vs 40.6%），微观上粒内裂纹出现更早（3次 vs 6次）且宽度更大（24次后~48 μm vs ~32 μm）［Rong 2021, pp. 9-10, 13-15］。
- **损伤阶段性发展**：损伤在前12次循环内迅速增长，随后趋于平稳。原因在于前期产生的微缺陷为矿物热膨胀提供空间，降低了后期循环的热应力水平［Rong 2021, pp. 14-17］。
- **AE特征**：随循环数增加，初始加载阶段AE计数率和累积事件增强，表明初始热裂纹密度增大；相同循环下LG样品的AE活动强于AG，证实液氮冷却加重了初始损伤［Rong 2021, pp. 11-13］。
- **变形行为改变**：循环使σcc/σp升高，弹性段缩短，不稳定裂纹扩展段延长，岩石从脆性向延性转变［Rong 2021, pp. 10-11］。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 24次循环后，LG的UCS降低24.8%（120.61 MPa），AG降低16.0%（134.73 MPa） | [Rong 2021, pp. 7-9, Table 3] | 300°C加热，5°C/min，0–24次循环 | 液氮冷却使抗压强度衰减更显著 |
| 24次循环后，BTS衰减LG为53.5%，AG为40.6% | [Rong 2021, pp. 7-9, Table 3] | 同上 | 抗拉强度对冷冲击更敏感 |
| 孔隙率n在12次循环后基本不变；0→12次，AG n增32.93%，LG增57.32% | [Rong 2021, pp. 7-9, Fig. 6a] | 同上 | 液氮冷却大幅增加孔隙 |
| P波速度Vp在12次循环后变化微弱；0→12次，AG Vp降35.20%，LG降42.56% | [Rong 2021, pp. 7-9, Fig. 6b] | 同上 | 声波速度反映微裂纹发育 |
| 损伤变量D随循环数呈指数增长（R²≥0.93），最大D值由BTS反映（AG 0.406，LG 0.585），其次为Vp、E、UCS | [Rong 2021, pp. 14-17, Fig. 19, Table 5] | 指数拟合 | BTS对热损伤最灵敏 |
| LG在3次循环即出现粒内微裂纹，AG在6次才出现；24次循环后LG微裂纹平均宽度48 μm，AG为32 μm | [Rong 2021, pp. 13-14, Fig. 17-18] | 偏光显微镜50×，薄片 | 液氮加速裂纹扩展并增大宽度 |
| 最终累积AE击中数随循环数增加而增多，且LG远高于AG | [Rong 2021, pp. 11-13, Fig. 16] | 单轴压缩全过程 | 液氮冷却导致更多微观破裂 |
| σcc/σp随循环增加而升高，弹性段比例缩小；LG的不稳定裂纹扩展阶段增长更明显 | [Rong 2021, pp. 10-11, Fig. 11] | 单轴压缩 | 力学行为由脆性向延性过渡 |

## Limitations
- 试验仅使用一种花岗岩（麻城）及单一目标温度（300°C），结果向其他岩性或温度区的推广需要验证［Rong 2021, pp. 3-4, 17-18］。
- 无围压条件，未模拟深部地应力；液氮浸泡冷却方式与现场井筒注入的热–流环境不同［Rong 2021, pp. 17-18］。
- 未直接测量渗透率，损伤程度仅通过孔隙率和P波速度间接表征［Rong 2021, pp. 7-9］。
- 现场应用中，液氮相变保温、管道低温强度、支撑剂携砂能力等工程问题尚未解决［Rong 2021, pp. 17-20］。

## Assumptions / Conditions
- 加热速率5°C/min足够缓慢，不会诱发热冲击微裂纹［Rong 2021, pp. 3-4］。
- 300°C是当前地热储层的典型开采温度上限［Rong 2021, pp. 3-4］。
- 恒温4 h保证样品内部温度均匀［Rong 2021, pp. 3-4］。
- 液氮温度约‑196°C（常压）［Rong 2021, pp. 2-3］。
- 所有样品天然状态下结构完整，无宏观缺陷；端面平整度<0.02 mm［Rong 2021, pp. 3-4］。
- 物理力学测试严格遵循ISRM建议方法，样品均经7天风干［Rong 2021, pp. 3-5］。

## Key Variables / Parameters
- **独立变量**：循环次数（0,1,3,6,12,18,24）、冷却方式（液氮骤冷 vs. 空气缓冷）。
- **物理响应变量**：M、V、ρ、n、Vp。
- **力学响应变量**：UCS、BTS、E、εp、σcc、σci、σcd及其归一化比值。
- **声发射变量**：AE计数率、累积AE击中数。
- **损伤量化**：D(UCS)、D(BTS)、D(E)、D(Vp)。
- **微观变量**：粒间/粒内微裂纹的出现时机、密度、宽度。

## Reusable Claims
1. **循环液氮冷却的饱和效应**：对于300°C高温花岗岩，在12次液氮冷却循环后，物理力学性质损伤趋于饱和，继续增加循环次数对改善渗透性的贡献微弱［Rong 2021, pp. 14-17］。**条件**：慢速加热至300°C、液氮浸泡冷却；**限制**：未在其他温度或岩石类型中验证。
2. **冷冲击的增强作用**：相比空气冷却，液氮冷却造成的热冲击损伤更严重，具体表现为：同等循环次数下，孔隙率增幅更大、P波速度降幅更大、强度衰减更多，且粒内裂纹更早出现并具有更大宽度［Rong 2021, pp. 7-9, 13-15］。**条件**：单轴加载，无围压；**限制**：基于单一花岗岩。
3. **损伤的指数衰减规律**：花岗岩在循环加热–冷却下的强度、模量、声速等损伤变量随循环次数呈指数变化，其中巴西抗拉强度对循环热损伤最为敏感，可作为监测指标［Rong 2021, pp. 14-17］。**条件**：0–24次循环，300°C；**限制**：相关性可能因岩性而异。
4. **力学行为脆–延转换**：循环次数增加导致裂纹闭合应力比σcc/σp升高，弹性变形阶段缩短，不稳定裂纹扩展阶段延长，岩石脆性减弱［Rong 2021, pp. 10-11］。**条件**：单轴压缩；**限制**：尚未考虑围压效应。
5. **AE作为热损伤指示**：初始加载阶段较强的AE活动反映循环冷热处理引入的初始微裂纹密度，液氮冷却下的AE活动更强，可作为定量评价初始损伤的间接手段［Rong 2021, pp. 11-13］。**条件**：门限50 dB，增益40 dB；**限制**：AE参数需针对不同岩石标定。

## Candidate Concepts
- [[循环液氮致裂]]
- [[冷冲击效应]]
- [[热应力疲劳]]
- [[花岗岩热损伤]]
- [[物理力学性质退化]]
- [[微裂纹（粒间/粒内）]]
- [[损伤变量]]
- [[P波速度与微缺陷]]
- [[声发射监测]]
- [[裂纹闭合应力]]
- [[裂纹起始应力]]
- [[裂纹损伤应力]]
- [[脆性–延性转变]]
- [[增强型地热系统（EGS）]]
- [[干热岩（HDR）]]
- [[无水压裂]]
- [[液氮辅助钻井]]

## Candidate Methods
- [[加热-冷却循环处理]]
- [[液氮浸泡冷却]]
- [[真空饱和法测孔隙率]]
- [[超声波P波速度测量]]
- [[巴西劈裂试验]]
- [[单轴压缩试验]]
- [[多通道声发射监测]]
- [[轴向应变响应法（ASR）求σcc]]
- [[侧向应变响应法（LSR）求σci]]
- [[体积应变法求σcd]]
- [[偏光显微镜岩相分析]]
- [[图像法测量微裂纹宽度]]
- [[指数函数拟合损伤演化]]

## Connections To Other Work
- 液氮致裂概念源于Shouldice (1964)，后用于煤和页岩压裂（McDaniel et al. 1997; Grundmann et al. 1998）［Rong 2021, pp. 2-3］。
- 室温下岩石液氮冷却效应已有较多研究（Finnie et al. 1979; Cai et al. 2014a,b, 2015; Qin et al. 2016, 2017；Han et al. 2018等），证实低温可提高孔隙连通性并降低强度［Rong 2021, pp. 2-3］。
- 循环液氮注入比单次注入更高效的观点在煤岩中由Qin et al. (2018a,b)证实，本研究将其推广到高温花岗岩［Rong 2021, pp. 2-3］。
- 冷却速率对热裂的影响在Kumari et al. (2017)和Kim et al. (2013)中讨论，本文通过对比液氮与空气冷却量化了速率效应。
- 声发射用于热损伤岩石破坏过程追踪，与Rong et al. (2018)、Peng et al. (2018)等方法一致［Rong 2021, pp. 5-7, 11-13］。
- 损伤变量的指数模型类似Hueckel et al. (1994)、Hu et al. (2018)等［Rong 2021, pp. 14-17］。

## Open Questions
- 如何在现场综合地质条件、施工成本与裂缝连通性，确定循环液氮致裂的最佳次数？［Rong 2021, pp. 17-18］
- 能否开发出适配液氮低粘度的新型支撑剂？［Rong 2021, pp. 18-20］
- 需要哪些有效措施保持液氮在注入过程中的低温状态，以最大化冷冲击效果？［Rong 2021, pp. 18-20］
- 高压液氮射流辅助钻井时，不同应力状态和射流压力下岩石的起裂应力与裂纹扩展特征如何？［Rong 2021, pp. 17-18］
- 本研究的12次循环饱和结论在其他岩性（砂岩、碳酸盐岩等）或更高温度（>300°C）下是否成立？［Rong 2021, pp. 17-18］
- 热–流–固多场耦合数值模拟能否可靠预测现场尺度循环液氮致裂效果？［Rong 2021, pp. 2-3, 17-18］

## Source Coverage
本页面由全部16个非空索引片段编译而成。源片段总字符数77337，编译后字符数76567，覆盖率：按片段数为100%，按字符数为99.0%。来源签名：53681bd4cff11628a384cff4cc534c3f902b7bc6，编译策略：单次直出Markdown。所有陈述均基于提供的索引证据，未添加额外推断。
