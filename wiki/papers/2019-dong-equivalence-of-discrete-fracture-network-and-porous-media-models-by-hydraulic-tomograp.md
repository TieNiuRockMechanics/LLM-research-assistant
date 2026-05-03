---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp"
title: "Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2019 - Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.pdf"
collections:
citation: "Dong, Yanhui, et al. \"Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.\" *Water Resources Research*, 2019. doi:10.1029/2018WR024290."
indexed_texts: "14"
indexed_chars: "65786"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "66072"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004347"
coverage_status: "full-index"
source_signature: "87a4f4f3b895e93013fa82d64de0e6c0c16656a6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T23:01:39"
---

# Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.

## One-line Summary
水力层析成像（HT）配合等效多孔介质（EPM）模型可以表征离散裂隙网络（DFN）的导水率和储水率分布，其等效性取决于是否存在裂隙连通概率的空间代表性单元体（spatial REV）：稠密裂隙网络存在空间REV时EPM预测可靠；稀疏裂隙网络无空间REV时只能识别主导裂隙，且需要密集观测井。

## Research Question
在不考虑岩石基质的DFN模型中，采用EPM‑hetero模型的瞬时水力层析成像（HT）能够在多大程度上表征裂隙网络的导水率和储水率分布？并通过定义裂隙连通概率的空间REV建立DFN与EPM的等效判据。[Dong 2019, pp. 1-2]

## Study Area / Data
合成算例：使用FracMan软件随机生成三个二维DFN模型（A、B、C），域尺寸1000 m × 1000 m × 1 m，包含两组小裂隙（Set1、Set2）和两条大断层（F1、F2），总裂隙数分别为200、500、1000条。裂隙几何参数及水力参数见表1（方位角、半径、开度、渗透率、压缩系数）。13口井用于反演，其中9口进行顺序注水试验（单井注水速率0.00001 m³/s，持续150 h），另设25口验证井（V1–V25）独立于反演，通过3口中心验证井的注水试验获取验证水头数据。注水响应序列各取11个时间点。数值模拟采用MAFIC程序，只模拟裂隙内二维非承压渗流，忽略基质。[Dong 2019, pp. 3-4]

## Methods
- 裂隙生成：Enhanced Baecher模型，泊松过程定位裂隙中心，正方形垂直平面。
- 正演模拟：MAFIC求解二维裂隙渗流方程，层流假设，无基质，无通量边界，初始均匀水头100 m。
- 水力层析成像反演：采用SimSLE（Simultaneous Successive Linear Estimator）算法，通过VSAFT2代码执行。VSAFT2为二维有限元连续介质模型（EPM），域离散为50 × 50个20 m×20 m的方形单元。每个注水响应序列选取4个数据点（早、中、晚期）用于反演。计算在国家超算广州中心天河二号上进行。[Dong 2019, pp. 4-5]
- 验证：利用未参与反演的验证井注水数据，比较DFN观测水头与基于估计的K和Ss的EPM预测水头。分析不同裂隙密度下的预测误差。
- 空间REV分析：以不同控制体积（50~500 m）遍历域内，计算裂隙强度P₃₂（单位体积裂隙总面积）的变异系数（COV），回归COV与CV尺寸的关系，确定空间REV尺寸（COV≈0.1–0.2）。并用文献[Farichah et al., 2017]提出的方程(3)计算REV尺寸。[Dong 2019, pp. 10-11]

## Key Findings
- 稀疏DFN（模型A）无空间REV：HT‑EPM仅能识别沿大断层的高K带和两个独立裂隙簇之间的低K分隔，但预测水头大量虚高（20口不连通井被误判有响应）；验证误差很大（绝对平均偏差967.21，标准差2234.23）。
- 中密度DFN（模型B）存在空间REV（约250 m）：HT‑EPM得到的K、Ss分布与连通裂隙基本一致，验证散点较多集中在1:1线附近，偏差较小（绝对平均偏差83.66，标准差78.81），但对部分不连通井仍有高估。
- 高密度DFN（模型C）存在空间REV（约200 m）：K、Ss层析图能捕捉高连通区和低K边界，大部分验证点（19个连通井）沿1:1线分布，偏差最低（绝对平均偏差38.68，标准差38.70），且成功识别了一处不连通井（V12）的低K特征。
- 空间REV分析表明：P₃₂的COV在模型A中最低为0.71，不满足均匀性；模型B和C的COV随CV增大降至0.14和0.16，说明裂隙连通概率在整个域内具有空间不变性，此时DFN可视为等效连续介质（EPM）。方程(3)计算的REV尺寸与手动统计吻合（表3）。
- 综上，裂隙连通概率的空间REV概念定义了DFN与多孔介质模型的等效性。若存在空间REV，有限监测井的HT能以合理的K、Ss分布预测全域渗流；若无空间REV，则只能刻画主导裂隙，准确成像需极密监测网络。[Dong 2019, pp. 5-8, 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 稀疏DFN（模型A）无空间REV，验证误差绝对均值967.21，标准差2234.23；20口不连通井被EPM高估水头 | [Dong 2019, pp. 5-6] [Table 2] | DFN总数200条裂隙+2条断层；监测井13口，验证井25口；注水速率0.00001 m³/s，持续150 h | EPM低估了非连通性 |
| 中密度DFN（模型B）空间REV约250 m，验证误差绝对均值83.66，标准差78.81；8口不连通井高估，但连通井响应偏差较小 | [Dong 2019, pp. 6-7] [Table 2] | 裂隙500条+2断层 | 整体连续性改善 |
| 高密度DFN（模型C）空间REV约200 m，验证误差绝对均值38.68，标准差38.70；仅5口不连通井高估，且一不连通验证井（V12）被成功识别为低K区 | [Dong 2019, pp. 7-8] [Table 2] | 裂隙1000条+2断层 | EPM预测能力接近DFN |
| 模型A P₃₂变异系数最低0.71，不收敛；模型B变异系数随CV增大从0.5降至0.14（约250 m）；模型C从～降至0.16（约200 m） | [Dong 2019, pp. 10-11] [Fig.6] | CV尺寸50~500 m，移动采样避免边界 | 手动统计确定REV |
| 方程(3)计算REV大小：模型A 1058 m（超出计算域），模型B 231 m，模型C 206 m | [Dong 2019, pp. 11] [Table 3] | P₃₂取全局均值，D为等效直径 | 与手动结果吻合，方程可辅助估算REV |
| HT‑EPM估计的K和Ss是“条件有效参数”，可再现所有注水试验下的观测水头，但非DFN裂隙的固有参数，尤其在基质缺失时Ss异常偏大 | [Dong 2019, pp. 8-9] | 使用VSAFT2作为EPM反演模型 | 验证有效性已单独检验 |

## Limitations
- 二维DFN模型完全忽略岩石基质，可能夸大了实际岩体中断裂的不连续性，使得EPM的适用性偏于保守。[Dong 2019, pp. 12]
- 监测井网和注水井数量固定；稀疏DFN所需的极高密度井网在本文未量化探讨。[Dong 2019, pp. 12]
- 空间REV基于几何参数P₃₂定义，未直接检验水力传导系数的REV。且实际中获取足够裂隙测量数据以计算P₃₂和等效直径D仍很困难。[Dong 2019, pp. 12]
- 验证仅使用了三个中心验证井的注水数据，可能未覆盖全部流场特征。

## Assumptions / Conditions
- 裂隙内为层流，服从达西定律及立方定律。[Dong 2019, pp. 2, 4]
- 裂隙为垂直正方形平面，裂隙参数在每组内恒定，未考虑变异性。[Dong 2019, pp. 3-4]
- EPM模型（VSAFT2）采用连续介质假设，单元内参数均值化，空间离散为20 m×20 m的正方形网格。[Dong 2019, pp. 4-5]
- 无通量边界，初始水头100 m均一分布。
- 注水试验为瞬时过程，不考虑井储效应。
- 验证井处若5 m半径内存在裂隙则移至该裂隙，否则保持未连接；这简化了裂隙与井筒的水力联系。[Dong 2019, pp. 4]

## Key Variables / Parameters
- 裂隙强度（密度）：总裂隙数200、500、1000（模型A、B、C）
- 裂隙几何：走向、倾角、等效半径、开度
- 裂隙水力参数：渗透率（Set1: 9.87E‑12 m², Set2: 2.96E‑12 m², F1: 9.87E‑11 m², F2: 3.95E‑11 m²），压缩系数均为1.00E‑07 1/kPa
- 注水速率：0.00001 m³/s
- 注水历时：150 h
- 反演选取时间点：每个响应序列4个点
- 控制体积尺寸系列：50×50~500×500 m²
- P₃₂：单位体积裂隙总面积（L⁻¹）
- COV(P₃₂)阈值0.1~0.2定义空间REV
- 验证误差指标：绝对平均误差、标准差

## Reusable Claims
- 当裂隙网络存在裂隙连通概率的空间REV时，基于EPM的水力层析成像能够有效估计等效K和Ss分布，并用有限监测井预测独立注水引起的流场。[Dong 2019, pp. 11-12]
- 对于稀疏裂隙网络（无空间REV），HT‑EPM只能识别由大断层和连通簇组成的主导高渗透带，而无法刻画孤立的局部裂隙，验证中大量不连通点被误判为有响应。[Dong 2019, pp. 11-12]
- 空间REV可根据P₃₂的COV‑CV尺寸曲线确定，也可粗略用方程COV＝0.84·V⁻⁰·⁵·P₃₂⁻⁰·⁵·D估算。[Dong 2019, pp. 10-11]
- HT反演得到的EPM参数场是条件有效参数，严格反映注入/抽水试验中的水头响应，并非裂隙本身的固有属性，但在存在空间REV时具有较好的预测能力。[Dong 2019, pp. 8-9]
- 增加裂隙密度（降低裂隙稀疏度）可显著减小验证误差，改善EPM模型的适用性。[Dong 2019, pp. 10]

## Candidate Concepts
- [[spatial REV]] (裂隙连通概率的空间代表性单元体)
- [[equivalent porous media (EPM) model]] (等效多孔介质模型)
- [[discrete fracture network (DFN)]] (离散裂隙网络)
- [[hydraulic tomography (HT)]] (水力层析成像)
- [[fracture connectivity probability]]
- [[conditional effective parameters]] (条件有效参数)
- [[P32 fracture intensity]] (裂隙强度P₃₂)
- [[coefficient of variation of P32]] (P₃₂的变异系数)
- [[ensemble REV]] (集合REV)
- [[fracture zone]] (裂隙带)
- [[SimSLE]] (同时逐次线性估计器)

## Candidate Methods
- [[FracMan fracture generation]]
- [[MAFIC fracture flow simulation]]
- [[VSAFT2 heterogeneous porous media model]]
- [[Simultaneous Successive Linear Estimator (SimSLE)]]
- [[sequential injection hydraulic tomography]]
- [[validation with independent wells]]
- [[spatial REV analysis by P32 COV]]
- [[geometric REV estimation equation (Farichah et al. 2017)]]

## Connections To Other Work
- Yeh, Mao, et al. (2015) 对空间REV和集合REV的区分被用于解释稀疏DFN仍可视为集合REV，但预测不确定性高。[Dong 2019, pp. 11]
- Farichah et al. (2017) 提出的几何REV计算公式(3)在本文中用于验证手动确定的REV尺寸，发现结果吻合。[Dong 2019, pp. 11, 13]
- 多篇HT研究（如Zha et al., 2014, 2016; Illman et al., 2009; Castagna et al., 2011; Fischer et al., 2017, 2018）为HT在裂隙介质中的应用提供了背景，但多数使用EPM生成合成数据，本文首次以DFN生成数据验证EPM‑HT的可行性。[Dong 2019, pp. 1-2]
- Yeh et al. (1996) 提出的条件有效参数概念解释了估计场能拟合观测但非真实参数的原因。[Dong 2019, pp. 8]

## Open Questions
- 实际三维裂隙‑基质系统中，基质存在是否会缩小无空间REV的范围，使EPM更方便应用？[Dong 2019, pp. 12]
- 能否将空间REV的概念从P₃₂推广到水力传导系数的空间REV，以直接判定等效性？
- 在稀疏DFN情况下，需要多高密度的观测井网（数量和空间布局）才能实现局部裂隙的精确定位？[Dong 2019, pp. 12]
- 方程(3)在实际中如何通过有限的裂隙测量（如钻孔图像）实用化？
- HT中增加通量测量是否能改善稀疏网络的成像能力（如Tso et al., 2016; Zha et al., 2014所建议）？[Dong 2019, pp. 8]

## Source Coverage
本文档完全基于提供的14个非空索引片段编译，覆盖论文全文（页1–14）。所有片段均已处理，不包含片段外的信息。索引文本总字符数65,786，编译后总字符数66,072，覆盖率按片段计100%，按字符计100.4%。
