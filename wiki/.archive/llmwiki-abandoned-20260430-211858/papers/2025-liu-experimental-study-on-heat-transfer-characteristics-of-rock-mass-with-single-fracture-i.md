---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-liu-experimental-study-on-heat-transfer-characteristics-of-rock-mass-with-single-fracture-i"
title: "Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir."
status: "draft"
source_pdf: "data/papers/2025 - Experimental study on heat transfer characteristics of rock mass with single fracture in geothermal reservoir.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Liu, Keliu, et al. \"Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir.\" *Thermal Science and Engineering Progress*."
indexed_texts: "20"
indexed_chars: "96895"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:13:42"
---

# Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir.

## One-line Summary

通过室内加热与注水实验，本文研究了含单裂隙花岗岩在地热储层条件下的温度场演化、热传导与热对流特征，并分析了热源温度和注水流量对稳定温度的影响 [Liu unknown-year, pp. 1-1]。

## Research Question

地热储层裂隙岩体的传热特性是什么，单裂隙如何影响岩体内的热传导与热对流过程？ [Liu unknown-year, pp. 1-1]

## Study Area / Data

- 实验对象：含单一45°倾角贯通裂隙的花岗岩试件，尺寸为200 × 100 × 200 mm [Liu unknown-year, pp. 3-4]。
- 实验材料物理化学属性：花岗岩含有石英、斜长石、正长石、黑云母等矿物，化学组分含64.6% SiO₂、12.3% Al₂O₃等 [Liu unknown-year, pp. 3-4]。
- 数据采集：58个布置在基质内的温度测点及2个位于裂隙上下端的温度测点，使用多通道数据记录仪进行实时监测 [Liu unknown-year, pp. 1-1] [Liu unknown-year, pp. 4-6]。
- 加热源温度（ T₀ ）变量：60, 70, 80, 90 °C [Liu unknown-year, pp. 4-6]。
- 注水流量（ q_w ）变量：0.5, 1.0, 1.5, 2.0, 2.5 L/min [Liu unknown-year, pp. 4-6]。

## Methods

- 实验系统：构建了含恒定温度加热容器、可调速循环泵、多通道数据记录仪与自动补水系统的裂隙花岗岩对流换热实验系统 [Liu unknown-year, pp. 4-6]。
- 实验步骤：
    1. 设置目标热源温度，启动循环泵使容器内水温均匀。
    2. 向水箱注入5 kg、25 °C的水并连接模拟注采井。
    3. 当加热容器水温稳定于目标温度后，将试件底部30 mm浸入加热容器并启动数据记录。
    4. 加热9小时后，调节注水流量并开始向裂隙注水。
    5. 注水持续9小时后停止记录，自然冷却后准备下一组实验 [Liu unknown-year, pp. 4-6]。
- 温度梯度计算方法：采用相邻等温面温度差与垂直距离比值的极限定义温度梯度 ∇Tr，结合傅里叶导热定律计算热通量 [Liu unknown-year, pp. 6-8]。
- 加热与冷却阶段划分标准：
    - 缓慢升温（I₁）：连续秒间温差 ≤ 0.1 °C 的最后时刻为过渡点 τ_sh。
    - 快速升温（I₂）与第二次缓慢升温（I₃）的分界为升温速率开始衰减的时刻 τ_rh。
    - 温度稳定（I₄）通过后续测点与参考时刻的温度波动处于 ±0.1 °C 以内来判定 [Liu unknown-year, pp. 10-11]。
- 不确定性分析：利用函数独立变量不确定性传播公式评估系统内循环泵、流量计、热源等组件对循环水温度的不确定性 [Liu unknown-year, pp. 4-6]。

## Key Findings

- 裂隙花岗岩加热过程中温度分布具区域性特征，整体经历四个阶段：第一次缓慢升温（I₁, ≤ 24 min）、快速升温（I₂, ≤ 84 min, 0.54 °C/min）、第二次缓慢升温（I₃, ≤ 84 min, 0.04 °C/min）、温度稳态（I₄） [Liu unknown-year, pp. 1-1]。
- 随热源温度 T₀ 升高，稳态加热温度 T_h 逐渐增加；随距离热源垂直距离 d_v 增加，裂隙左侧 T_h 非线性下降，右侧 T_h 线性下降 [Liu unknown-year, pp. 1-1]。
- 注水后花岗岩经历快速冷却（II₁, ≤ 15 min）、缓慢冷却（II₂, ≤ 25 min）、缓慢升温（II₃, ≤ 358 min）、温度稳态（II₄, ≤ 142 min）四个阶段 [Liu unknown-year, pp. 1-1]。
- 稳态循环水温度 T_w 与注水流量 q_w 呈线性增长关系，与热源温度 T₀ 呈指数增长关系 [Liu unknown-year, pp. 1-1]。
- 裂隙的存在显著改变热传递路径，导致岩体内温度呈同心圆状分布，裂隙上方区域温度始终低于下方区域 [Liu unknown-year, pp. 6-8]。
- 裂隙与热源夹角越大，裂隙对热传递的阻碍效应越小；裂隙岩体内的传热机制主要为热传导与热对流 [Liu unknown-year, pp. 1-1] [Liu unknown-year, pp. 1-2]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 加热过程岩体温度分布呈区域性特征，经历 I₁–I₄ 四个阶段 | [Liu unknown-year, pp. 1-1] | T₀ = 60–90 °C，试件底部30 mm浸入加热 | I₁ ≤ 24 min, I₂ ≤ 84 min (0.54 °C/min), I₃ ≤ 84 min (0.04 °C/min) |
| 随 d_v 增加，裂隙左侧 T_h 非线性下降，右侧 T_h 线性下降 | [Liu unknown-year, pp. 1-1] | 加热达到稳态 | 左右侧由裂隙分隔 |
| 注水后花岗岩经历 II₁–II₄ 四个阶段 | [Liu unknown-year, pp. 1-1] | 注水流量 0.5 L/min 等，连续注水9 h | II₁ ≤ 15 min, II₂ ≤ 25 min, II₃ ≤ 358 min, II₄ ≤ 142 min |
| 稳定 T_w 与 q_w 呈线性增长关系，与 T₀ 呈指数增长关系 | [Liu unknown-year, pp. 1-1] | 注水流量范围 0.5–2.5 L/min；T₀ 范围 60–90 °C | 未从索引片段中确认具体拟合参数 |
| 裂隙上方测点（#38）与下方测点（#21）在加热5 h后温差达 11.9 °C | [Liu unknown-year, pp. 8-10] | T₀ = 70 °C，监测线AA | #38: 43.2 °C, #21: 55.0 °C |
| I₁ 阶段持续时间最短3 min（#15），最长24 min（#54），峰值温度28.1 °C（#43） | [Liu unknown-year, pp. 10-11] | 全部测点在加热初期 | 测点位置见图3 |

## Limitations

- 实验仅针对含单一45°倾角贯通裂隙的花岗岩试件，未考虑多裂隙、裂隙网络或不同角度的影响 [Liu unknown-year, pp. 1-1] [Liu unknown-year, pp. 3-4]。
- 未从索引片段中确认实验是否考虑围压或原位地应力条件。
- 热源仅从试件底部单一方向加热，与真实地热储层多场耦合环境（如THM耦合）可能存在差异 [Liu unknown-year, pp. 1-2]。
- 实验流体仅为25 °C初始温度的纯水，未考虑流体化学成分或相变影响。

## Assumptions / Conditions

- 岩体传热遵循傅里叶导热定律，温度梯度与热通量关系成立 [Liu unknown-year, pp. 6-8]。
- 实验系统处于常压室内环境，热源恒定，循环水温度均匀 [Liu unknown-year, pp. 4-6]。
- 裂隙用高温防水胶密封前后端面，视为仅通过两模拟井筒进行流体交换 [Liu unknown-year, pp. 3-4]。
- 试件被视为各向同性连续介质，除裂隙外无其他内部缺陷 [Liu unknown-year, pp. 3-4]。

## Key Variables / Parameters

- T₀ ：热源温度 (°C) [Liu unknown-year, pp. 2-3]。
- T_h ：稳态加热温度 (°C) [Liu unknown-year, pp. 2-3]。
- T_w ：循环水温度 (°C) [Liu unknown-year, pp. 2-3]。
- d_v ：距离热源的垂直距离 (mm) [Liu unknown-year, pp. 2-3]。
- q_w ：注水流量 (L/min) [Liu unknown-year, pp. 2-3]。
- τ ：时间 (min)；τ_sh, τ_rh, τ_h 为各阶段特征时间 [Liu unknown-year, pp. 2-3] [Liu unknown-year, pp. 10-11]。
- 温度梯度 ∇Tr (°C/m) [Liu unknown-year, pp. 6-8]。
- 热通量 Q(x, τ) (W/m²) [Liu unknown-year, pp. 6-8]。
- θ ：裂隙倾角 (45°) [Liu unknown-year, pp. 2-3]。
- λ ：热导率 (W/m·K) [Liu unknown-year, pp. 2-3]。

## Reusable Claims

- Claim 1：对于含单裂隙的岩体加热过程，温度演变可划分为四次缓慢升温、快速升温、二次缓慢升温和稳态四个阶段。实验给出快速升温阶段最大速率为0.54 °C/min，二次缓慢升温阶段为0.04 °C/min（热源60–90 °C，底部加热条件下） [Liu unknown-year, pp. 1-1]。
- Claim 2：裂隙的存在导致岩体温度场呈区域性非对称分布，裂隙上方与下方测点在相同加热时间下温差可达11.9 °C（加热5 h，T₀ = 70 °C，d_v 约60–80 mm量级，依据监测线AA，#38与#21） [Liu unknown-year, pp. 8-10]。
- Claim 3：注水诱发的冷却—加热过程分为四阶段：快速冷却（≤15 min）、缓慢冷却（≤25 min）、缓慢升温（≤358 min）、温度稳态（≤142 min）。实验基于花岗岩试件，注水流量≥0.5 L/min，初始水温25 °C [Liu unknown-year, pp. 1-1]。
- Claim 4：稳态循环水温度 T_w 随注水流量 q_w 线性增加，随热源温度 T₀ 指数增加。该关系适用于 T₀ = 60–90 °C、q_w = 0.5–2.5 L/min 的条件 [Liu unknown-year, pp. 1-1]。
- Claim 5：裂隙与热源夹角越大，对热传递的阻碍效应越小。该结论基于实验获得的温度分布与传热路径分析，具体角度效应量化未从索引片段中确认 [Liu unknown-year, pp. 1-1]。

## Candidate Concepts

- [[fracture reservoir]]
- [[heat conduction in rock mass]]
- [[heat convection in fracture]]
- [[temperature field of fractured media]]
- [[single fracture geothermal]]
- [[fracture connectivity and heat transfer]]
- [[non-Darcy flow in fractures]]
- [[rough discrete fracture network]]
- [[enhanced geothermal systems (EGS)]]

## Candidate Methods

- [[multichannel temperature monitoring]]
- [[steady-state heat transfer experiment]]
- [[uncertainty analysis for thermal experiments]]
- [[water jet cutting for artificial fracture preparation]]
- [[temperature gradient estimation from discrete isothermal surfaces]]
- [[stage division of transient temperature curves]]

## Connections To Other Work

- 文中提及 Liu et al. [19] 提出利用裂隙表面积表征换热系数的经验函数，并比较了二维与三维单裂隙数值模型的流体流动与换热行为差异 [Liu unknown-year, pp. 1-2]。该工作可与本研究实验数据进行对比验证。
- 提及 Xue et al. [20] 采用复合单元法将三维对流-传导方程转化为等效变分原理以处理裂隙岩体渗流-传热，提示本研究裂隙传热的数值分析可连接该方法 [Liu unknown-year, pp. 1-2]。
- 提及 Chen et al. [21] 对三维交叉裂隙模型进行对流换热模拟并分析了死端裂隙（DEF）几何效应，本研究的单裂隙实验可与其结果做几何效应比较 [Liu unknown-year, pp. 1-2]。
- 提及 Xie et al. [22] 探索了裂隙倾角对岩体热导率的量化影响，结果指出热导率随裂隙角度偏离热流方向增大而降低，与本研究中“夹角越大阻碍效应越小”的定性结论在主题上可相互关联 [Liu unknown-year, pp. 2-3]。
- 本研究可从主题上连接到以下文献所发展的数值或解析方法：[[composite element method for fractured rock]]、[[non-Darcy rough discrete fracture network (NR-DFN) model]]、[[three-dimensional intersecting fracture heat transfer model]]、[[two-dimensional vs three-dimensional fracture flow and heat transfer comparison]]。

## Open Questions

- 未从索引片段中确认不同裂隙倾角、裂隙粗糙度或裂隙宽度（ξ）对传热阶段与稳定温度的具体影响。
- 多裂隙或裂隙网络条件下温度场演化与单裂隙情况的差异未从现有片段中讨论。
- 实验条件未包含地应力，裂隙渗透率随应力变化对热对流的影响尚不清楚。
- T_w 与 T₀ 的指数关系、与 q_w 的线性关系的经验公式或定量回归参数未从索引片段中提取到。
- 裂隙阻碍效应的定量表征模型，如等效热阻 R 与裂隙角度 θ 之关系，未在片段中展开。

## Source Coverage

本页面基于论文索引片段中的20个片段生成，主要覆盖了摘要、引言、实验系统与样本制备、不确定性分析、温度场分布、加热与冷却阶段划分等结果部分。片段提供了较详细的实验条件、温度场定性描述与阶段划分证据。但全文关于定量回归模型、具体数据拟合方程、不同热源温度与流量组合下的完整温度数据表、与数值模拟结果的对比验证等可能存在于论文其他部分的内容未在给定片段中，因此本页面无法提供这些方面的精确细节。
