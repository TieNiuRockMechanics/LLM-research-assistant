---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-li-experimental-studies-on-the-effect-of-cyclic-thermal-shock-and-cooling-methods-on-the-me"
title: "Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone."
status: "draft"
source_pdf: "data/papers/2022 - Experimental studies on the effect of cyclic thermal shock and cooling methods on the mechanical properties and fracture behavior of prefabricated fissured sandstone.pdf"
collections:
citation: "Li, Man, et al. \"Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone.\" *Theoretical and Applied Fracture Mechanics*, vol. 122, 2022, art. 103576. doi:10.1016/j.tafmec.2022.103576. Accessed 2026."
indexed_texts: "15"
indexed_chars: "71404"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "66910"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.937062"
coverage_status: "full-index"
source_signature: "a4283547511e603ae2b572a8f82dbf02d89ae369"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:26:34"
---

# Experimental Studies on the Effect of Cyclic Thermal Shock and Cooling Methods on the Mechanical Properties and Fracture Behavior of Prefabricated Fissured Sandstone.

## One-line Summary
通过循环热冲击实验和数值模拟，研究了热冲击次数及冷却方式（空气/不同水温）对含预制裂隙砂岩力学性质与破裂行为的影响，提出损伤经验公式，揭示热冲击导致裂隙尖端温度梯度最大并引发拉伸破坏。

## Research Question
循环热冲击次数及冷却介质（空气、不同温度水）如何影响含单一预制裂隙砂岩的峰值应力、弹性模量、波速衰减、损伤积累及单轴压缩下裂纹起裂与最终破坏模式？能否建立考虑热冲击次数与冷却水温的损伤表征公式？[Li 2022, pp. 1-2]

## Study Area / Data
- 样品来源：重庆市九龙坡区储层砂岩，密度2450 kg/m³，矿物组成以石英（40.90%）、长石（24.92%）、方解石（10.82%）和黏土矿物（22.36%）为主。[Li 2022, pp. 2-3]
- 预制裂隙：倾角45°（最大剪应力方向），长度2a = 12 mm，宽度b = 1.5 mm，位于标准圆柱试样（直径50 mm，高100 mm）中部。[Li 2022, pp. 2-3]
- 热冲击目标温度：400 °C，加热速率5 °C/min，恒温2 h。[Li 2022, pp. 3-4]
- 冷却条件：空气冷却（20 °C）；水冷却，水温分别为20 °C、50 °C、80 °C。[Li 2022, pp. 3-4]
- 循环次数：N = 0（自然状态）、1、4、8。[Li 2022, pp. 4-5]

## Methods
1. **循环热冲击实验**：将试样在400 °C加热后，分别用空气冷却约3小时，或浸入不同温度水中冷却约10分钟，重复0、1、4、8次。每种条件3个试样，结果取均值。[Li 2022, pp. 3-5]
2. **物理与力学参数测量**：利用非金属超声波检测仪测量纵波波速；在WADJ-600伺服试验机上进行单轴压缩试验，加载速率0.1 mm/min，同时用CCD相机（1 Hz）捕获破裂过程。[Li 2022, pp. 3-4]
3. **微观结构观察**：对不同循环次数水冷试样切片进行SEM观测。[Li 2022, pp. 5-7]
4. **数值模拟**：在COMSOL Multiphysics中建立含预制裂隙砂岩模型，进行热-力耦合分析，计算温度场、应力场及损伤区域；取空气换热系数20 W/(m²·K)，水换热系数2000 W/(m²·K)，其他参数见表5。[Li 2022, pp. 9-11, 14-16]
5. **裂纹分类**：采用Wong和Einstein的7类裂纹模式（T1、T2、T3、S1、S2、S3、TS）划分起裂与扩展裂纹。[Li 2022, pp. 7-9]

## Key Findings
1. **纵波波速**：随热冲击次数增加而下降，8次冲击后，空气冷却、80 °C、50 °C和20 °C水冷下波速平均降幅分别为7.55%、15.99%、29.01%和33.71%。水冷换热系数大，冷却速率高，导致更多热裂纹。[Li 2022, pp. 4-5]
2. **峰值应力与弹性模量**：随热冲击次数指数衰减，拟合关系良好（R² > 0.96）。首次热冲击导致力学性质劣化最为严重，当次数超过4次后劣化减缓。峰值应力在首次热冲击时分别下降至8次冲击总降幅的63%（空冷）、56%（80 °C水冷）、74%（50 °C水冷）、62%（20 °C水冷）。[Li 2022, pp. 5-7]
3. **损伤变量**：以弹性模量定义的损伤变量D_E随次数累积，且随冷却水温降低而增大。提出经验公式：  
   \( D_{E1} = ( -0.001 T + 0.462 ) \exp(0.057 N) \), R² = 0.945，适用于储层损伤评估。[Li 2022, pp. 7-7]
4. **破坏模式**：单轴压缩下，裂纹起裂以拉伸翼裂纹（T1）为主。随热冲击次数增加和水温降低，初始裂纹模式由T1逐步转变为T2或更复杂模式。二阶段出现反翼裂纹（T3）和拉剪混合裂纹（TS），三阶段多出现剪切裂纹（S1）和贯穿裂纹，并伴有不同程度的表面剥落。[Li 2022, pp. 7-9, 11-14]
5. **热冲击机理**：数值模拟表明，水冷时试样外部监测点温度骤降，内部温度滞后，最大温差达370.3 °C（21 s）。最大主应力峰值出现在约13 s，滞后于冷却速率峰值，反映热-力耦合特性。预制裂隙尖端温度梯度最大（84 °C/mm），该处热应力最先超过抗拉强度，引发开裂。[Li 2022, pp. 10-14]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| P-wave velocity decreases by 7.55% (air), 15.99% (80°C water), 29.01% (50°C water), 33.71% (20°C water) after 8 shocks | [Li 2022, pp. 4-5] | N=8, target 400°C | Larger HT coefficient → more cracks |
| Peak stress-exponential fit: air σ_p = 49.45+15.28e^{-1.06N} (R²=0.993); water 20°C σ_p = 34.14+30.50e^{-1.03N} (R²=0.981) | [Li 2022, pp. 5-7, Table 3] | Uniaxial compression after thermal shocks | First shock accounts for 56–74% of total reduction at N=8 |
| Elastic modulus-exponential fit: air E=4.51+2.88e^{-1.73N} (R²=0.999); water 20°C E=2.65+4.72e^{-1.14N} (R²=0.979) | [Li 2022, pp. 5-7, Table 3] | Same as above | Similar deterioration pattern |
| Damage formula: D_E1 = (−0.001T+0.462)exp(0.057N) (R²=0.945) | [Li 2022, pp. 7-7, Eq. 3] | Water cooling, N=0–8, T=20–80°C | Based on damage variable from elastic modulus |
| Initial crack mode shifts from T1 to T2 or more complex with increasing N or decreasing water temperature | [Li 2022, pp. 11-14, Table 4] | Uniaxial loading after treatment | Spalling degree also increases |
| In 20°C water cooling, max temperature difference 370.3°C at 21 s; max temperature gradient 84°C/mm at fissure tip | [Li 2022, pp. 9-11] | COMSOL simulation, first shock | Damage area calculated where max principal stress > tensile strength (5.82 MPa) |
| Peak max principal stress at monitoring point No.1: 14.96 MPa (20°C), 13.75 MPa (50°C), 12.53 MPa (80°C) | [Li 2022, pp. 14-16, Table 6] | Simulation, first shock | Peak stress lags cooling rate peak, linear with water temperature (R²=1) |

## Limitations
- 试样表面热裂纹分布及剥落程度仅为定性分析，未采用数字化图像处理或CT扫描进行定量表征。[Li 2022, pp. 7-9]
- 数值模拟假设岩石为各向同性材料，忽略水温度对换热系数的影响，且仅模拟首次热冲击过程，未考虑多次循环的温度场叠加。[Li 2022, pp. 10-11, 14-16]
- 试验温度固定为400 °C，未探讨更高温度下矿物相变（如石英573 °C相变）对结果的影响。[Li 2022, pp. 3-4]
- 仅针对一种储层砂岩，结论的普适性需进一步验证。

## Assumptions / Conditions
- 加热温度400 °C以避免矿物热分解/相变对力学行为的干扰。[Li 2022, pp. 3-4]
- 水冷试样表面水分擦干后再烘干，消除残余水分影响。[Li 2022, pp. 3-4]
- 数值模型中，空气换热系数取20 W/(m²·K)，水取2000 W/(m²·K)，且水冷时认为换热系数不随水温变化。[Li 2022, pp. 9-11]
- 裂纹分类采用Wong与Einstein的七类模式。[Li 2022, pp. 7-9]
- 单轴压缩加载速率0.1 mm/min，位移控制。[Li 2022, pp. 3-4]

## Key Variables / Parameters
- **自变量**：热冲击次数N（0,1,4,8）、冷却方式（空气/水）、冷却水温T（20,50,80 °C）
- **因变量**：纵波波速V_p、峰值应力σ_p、弹性模量E、损伤变量D_E、裂纹模式（T1,T2,S1等）、最大主应力、温度梯度
- **材料参数**：砂岩密度2450 kg/m³，弹性模量7.39 GPa（自然状态），泊松比0.25，热膨胀系数5.4×10⁻⁶/K，导热系数3.0 W/(m·K)，比热880 J/(kg·K)，抗拉强度5.82 MPa [Li 2022, pp. 9-11, Table 5]
- **拟合系数**：指数衰减系数（如λ=0.057），线性温度系数p,q等 [Li 2022, pp. 7-7, Table 3]

## Reusable Claims
- 循环热冲击下，含预制裂隙砂岩的峰值应力和弹性模量随冲击次数呈指数衰减，首次冲击损伤最严重，超过4次后劣化减缓。[Li 2022, pp. 5-7]
- 水冷却较空气冷却造成的力学性质下降更显著，冷却水温越低损伤越大。[Li 2022, pp. 4-7]
- 损伤变量D_E1可由公式 \((-0.001T+0.462)\exp(0.057N)\) 较好地描述（R²=0.945），适用于地热开采条件下砂岩储层损伤评估。[Li 2022, pp. 7-7]
- 单轴压缩下，热冲击后裂隙砂岩的起裂模式以拉伸翼裂纹(T1)为主，随着N增大或水温降低，初始裂纹由T1向T2或更复杂模式转变，并伴随表面剥落。[Li 2022, pp. 11-14]
- 热冲击时预制裂隙尖端存在最大温度梯度（84 °C/mm），该处热应力最先超过抗拉强度，是热开裂的起始位置。[Li 2022, pp. 10-14]
- 冷却速率峰值、温度梯度峰值和最大主应力峰值均与冷却水温呈线性负相关，且应力峰值出现时间滞后于温度场变化，体现热-力耦合效应。[Li 2022, pp. 14-16]

## Candidate Concepts
- [[cyclic thermal shock]] / 循环热冲击
- [[prefabricated fissured sandstone]] / 预制裂隙砂岩
- [[thermal cracking]] / 热开裂
- [[damage variable D_E]] / 损伤变量D_E
- [[tensile wing crack]] / 拉伸翼裂纹（T1）
- [[heat transfer coefficient]] / 换热系数
- [[thermal-mechanical coupling]] / 热-力耦合
- [[temperature gradient]] / 温度梯度
- [[spalling]] / 剥落
- [[peak stress attenuation]] / 峰值应力衰减

## Candidate Methods
- [[cyclic thermal shock experiment]] / 循环热冲击试验
- [[uniaxial compression test on fissured rock]] / 含裂隙岩石单轴压缩试验
- [[P-wave velocity measurement]] / 纵波波速测试
- [[COMSOL Multiphysics thermal-mechanical simulation]] / COMSOL热-力耦合模拟
- [[crack mode classification (Wong & Einstein)]] / 裂纹模式分类（Wong & Einstein七类）
- [[SEM observation of thermal cracks]] / 扫描电镜热裂纹观测
- [[damage variable definition based on elastic modulus]] / 基于弹性模量的损伤变量定义

## Connections To Other Work
- 与前人研究一致：Brotons等（2013）报道水冷比空冷引起更大强度下降；Kim等（2013）发现热冲击在试样外层产生拉应力导致微裂纹；Pai等（2021）指出首次热冲击对花岗岩物理力学性质破坏最严重，且10次后减缓。本文将此规律推广至砂岩，并考虑裂隙影响。[Li 2022, pp. 2-2]
- 杨圣奇等（2022）研究了高温对含裂隙花岗岩的变形破坏影响，本文侧重循环热冲击与不同水温的叠加效应。[Li 2022, pp. 2-2, 16-16]
- 损伤公式的指数形式与文献[42,43]中热处理岩石的损伤规律类似，本文进一步引入冷却水温的线性项，得到适用于水温变化的经验公式。[Li 2022, pp. 7-7]

## Open Questions
- 多次循环热冲击下，温度场与应力场的累计损伤如何准确模拟？当前仅模拟首次冲击，未考虑裂纹扩展对应力集中的重新分布。[Li 2022, pp. 14-16]
- 换热系数随水温的实际变化是否显著？若考虑变换热系数，对温度梯度和热应力预测会如何修正？[Li 2022, pp. 14-16]
- 定量化表征表面热裂纹与剥落需要引入CT扫描或图像处理技术，以建立裂纹密度与力学参数的关系。[Li 2022, pp. 7-9]
- 是否存在阈值水温或循环次数，使得损伤模式发生突变？目前实验只设定了三档水温与三个循环次数，范围有限。
- 该砂岩储层在真实地热工况（高围压、高孔压、流体对流）下的循环热冲击行为尚待研究。

## Source Coverage
本页基于论文所有15个已索引片段（共计66,910字符）编译而成。片段涵盖引言、实验方法、结果、讨论与结论全内容。按数据块统计覆盖率100%，按字符数统计覆盖率93.7%。未使用任何片段外信息，所有陈述均附有来源标签。
