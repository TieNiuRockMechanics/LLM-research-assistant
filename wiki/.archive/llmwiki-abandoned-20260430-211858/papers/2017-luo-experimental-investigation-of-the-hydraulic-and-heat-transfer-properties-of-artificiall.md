---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-luo-experimental-investigation-of-the-hydraulic-and-heat-transfer-properties-of-artificiall"
title: "Experimental Investigation of the Hydraulic and Heat-Transfer Properties of Artificially Fractured Granite."
status: "draft"
source_pdf: "data/papers/2017 - Experimental investigation of the hydraulic and heat-transfer properties of artificially fractured granite.pdf"
collections:
  - "part2"
citation: "Luo, Jin, et al. \"Experimental Investigation of the Hydraulic and Heat-Transfer Properties of Artificially Fractured Granite.\" *Scientific Reports*, vol. 7, 39882, 5 Jan. 2017. DOI:10.1038/srep39882."
indexed_texts: "9"
indexed_chars: "42715"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:36:40"
---

# Experimental Investigation of the Hydraulic and Heat-Transfer Properties of Artificially Fractured Granite.

## One-line Summary
本实验研究通过三维形态学分析和“热-水-力”（THM）耦合测试，揭示了人造裂缝花岗岩的粗糙度（以面积比表征）对水力开度、导水系数及传热效率的控制作用，以及围压和温度对水力特性的竞争性影响 [Jan 2017, pp. 1-2, 8-9]。

## Research Question
裂缝形态（特别是粗糙度）、围压和温度如何共同影响人造裂缝花岗岩的水力开度、导水系数及其传热效率？ [Jan 2017, pp. 1-2]。

## Study Area / Data
样本采自两个不同地点，得到两组岩心（组一：#1、#2、#3；组二：#4、#5、#6），基本热物性（密度、导热系数、比热、热扩散率）列于表 1。所有样品均为圆柱形（直径约25 mm，长度约31–58 mm），实际测试高度加工为40 mm。研究区域的确切地理位置未从索引片段中确认。 [Jan 2017, pp. 2-4] 表1：六块岩样的基本热物性 [Jan 2017, pp. 2-4]。

## Methods
- **人造裂缝制备**：采用改进的巴西劈裂法，利用岩石力学测试系统以3 × 10⁻³ mm/s的位移速度对圆柱试样施加压缩荷载，产生贯通轴向的单条粗糙裂缝 [Jan 2017, pp. 2-4]。
- **三维形态学建模**：对裂缝表面进行拍照，提取约130万个点的点云，剔除异常点后生成三维数字模型，并计算“面积比”（真实表面积与投影面积之比）以量化粗糙度 [Jan 2017, pp. 2-4]。
- **水力测试程序**：试验在能控制围压、温度和液压的渗透仪中进行。对于组一，固定温度和液压，围压由4 MPa逐步升至24 MPa（级差2 MPa），每级稳定30 分钟后进行60分钟流动测试；对于组二，固定围压和液压，岩石温度从25 °C以5 °C步长升至100 °C，入口流体温度恒定20 °C [Jan 2017, pp. 4-5]。
- **数据处理**：基于平板裂缝立方定律（式1）计算水力开度 e，由水力开度与流体运动粘度系数进一步计算导水系数 K（式2）。对于单裂缝岩样，导水系数直接与水力开度的平方及重力加速度/运动粘度的比值关联 [Jan 2017, pp. 4-5]。
- **传热效率分析**：在耦合水-热-力条件下记录出口流体温度与岩石温度，计算换热速率[Jan 2017, pp. 8-9]。

## Key Findings
1. **裂缝形态对水力特性的控制**：面积比（反映粗糙度）越大，水力开度和导水系数越高。例如，#3样品面积比最大（4.048），开度最大（425 μm），导水系数最高（16 cm/s）；#1面积比最小（2.045），开度最小（180 μm），导水系数最低（3 cm/s） [Jan 2017, pp. 5-7]。
2. **围压效应**：水力开度和导水系数均随围压增加而减小，衰减趋势在围压达到约14.0 MPa后变缓 [Jan 2017, pp. 7-8, 8-9]。
3. **温度对水力性质的竞争影响**：随着岩石温度从25 °C升至100 °C，水力开度因花岗岩热膨胀（热膨胀系数约3.0×10⁻⁶ m/°C）而呈指数衰减（例如，某一条件下从190 μm降至130 μm，降幅46.15%）。然而，导水系数却随温度升高而增大，因为水的粘度从20 °C的100.5×10⁻⁵ Pa·s降至100 °C的28.38×10⁻⁵ Pa·s，其降幅（平方根约降21.16%）部分抵消了开度减小的影响，使得总体导水系数上升 [Jan 2017, pp. 7-8]。
4. **温度与传热的关系**：出口流体温度与岩石温度之间存在线性关系；换热速率受液压和围压影响，当液压从0.1 MPa升至0.9 MPa（围压固定8 MPa）时，换热速率提高 [Jan 2017, pp. 8-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 面积比与水力开度正相关：面积比4.048 → 开度425 μm；面积比2.045 → 开度180 μm | [Jan 2017, pp. 5-7] | 组一和三样品，围压与液压未明确列出，但基于形态学分析 | 粗糙度通过抑制裂缝闭合而保留更多流动通道 |
| 导水系数与面积比正相关：#3 16 cm/s，#2 7 cm/s，#1 3 cm/s | [Jan 2017, pp. 5-7] | 同上，计算基于立方定律 | 导水系数与水力开度的平方成正比 |
| 围压增加导致水力开度和导水系数降低，当围压>14 MPa后衰减趋势减缓 | [Jan 2017, pp. 7-8, 8-9] | 组一样品，温度固定，围压4–24 MPa，每级稳定30 min | 不同样品衰减曲线略有差异 |
| 水力开度随岩石温度升高呈指数衰减：y = 204.4796e⁻⁰·⁰⁰⁴ˣ（#4, 液压0.1 MPa），R²=0.978 | [Jan 2017, pp. 8-9] 表5 | 组二，#4，围压8 MPa，液压0.1 MPa，温度25–100 °C | 不同样品和液压下的指数关系类似，详见表5 |
| 导水系数随岩石温度升高而增加，在液压0.1 MPa和0.9 MPa下均观测到 | [Jan 2017, pp. 8-9] 图7b | 组二，#4–#6，围压8 MPa，温度25–100 °C | 粘度降低对导水系数的促进作用超过了开度减小的抑制作用 |
| 出口流体温度与岩石温度呈线性关系 | [Jan 2017, pp. 8-9] 图7c | 组二，液压0.1 MPa，围压8 MPa | 未在片段中给出回归参数详情 |

## Limitations
- 试验采用小尺寸人造裂缝（直径25 mm，高度40 mm），可能无法完全代表现场尺度裂缝网络的力学与水力学行为 [Jan 2017, pp. 2-4]。
- 组一样品在长期高围压测试后发生损坏，无法再用于温度效应实验，导致温度分析仅基于组二样品（#4–#6），样本量有限 [Jan 2017, pp. 7-8]。
- 水力计算基于立方定律，其假设为不可压缩、等温、层流、光滑平行板，而实际裂缝为粗糙面；该方法在低流速下的适用性未进一步验证 [Jan 2017, pp. 4-5]。
- 传热分析仅报告了出口温度与换热速率的定性趋势，未给出完整的热突破曲线、局部传热系数或热-水-力全耦合模型参数 [Jan 2017, pp. 8-10]。
- 未从索引片段中确认实验误差分析、化学作用（如溶解、沉淀）对裂缝长期演化的影响，以及试验中是否发生矿物反应。

## Assumptions / Conditions
- **立方定律适用条件**：流体为不可压缩牛顿流体，流动处于层流状态，裂缝为光滑平行板，流速足够低以至惯性效应可忽略 [Jan 2017, pp. 4-5]。
- **水力开度计算**：将粗糙裂缝等效为平行板开度，未直接考虑裂缝迂曲度或粗糙度对流速分布的局部影响 [Jan 2017, pp. 4-5]。
- **围压效应试验条件**：围压以准静态方式加载，每级稳定30 分钟后进行流动测试，假设孔隙压力变化可瞬时传递且裂缝达到力学平衡 [Jan 2017, pp. 4-5]。
- **温度效应试验条件**：入口流体温度恒定20 °C，仅改变岩石温度；假定岩样内部温度均匀，且流体与岩石间瞬时热平衡 [Jan 2017, pp. 7-8]。
- **物理性质**：花岗岩热膨胀系数取常数≈3.0×10⁻⁶ m/°C [Jan 2017, pp. 7-8]。
- **样品代表性**：人工裂缝由巴西劈裂产生，所有样品均视为各向同性均质花岗岩，未讨论原位应力或天然裂隙的影响 [Jan 2017, pp. 2-4]。

## Key Variables / Parameters
- **面积比**（−）：裂缝真实表面积与投影面积之比，表征粗糙度 [Jan 2017, pp. 5-7]。
- **水力开度 e**（μm或m）：基于立方定律反算的等效裂缝宽度，公式 e = (12 ν q / g J )^{1/3} [Jan 2017, pp. 4-5]。
- **导水系数 K**（cm/s或m/s）：基于水力开度和运动粘度的函数， K = (g e²)/(12 ν) [Jan 2017, pp. 4-5]。
- **围压**（MPa）：实验中4–24 MPa范围内的各级压力 [Jan 2017, pp. 4-5]。
- **岩石温度**（°C）：25–100 °C，用于研究温度影响 [Jan 2017, pp. 4-5]。
- **流体运动粘度 ν**（m²/s）或动力粘度（Pa·s），影响开度与导水系数的温度依赖性 [Jan 2017, pp. 7-8]。
- **水力梯度 J **（−）：驱动流动的压力梯度 [Jan 2017, pp. 4-5]。
- **单位宽度流量 q**（m²/s）：用于立方定律输入 [Jan 2017, pp. 4-5]。
- **换热速率**（W或单位未明确）：通过流体吸取的热量速率 [Jan 2017, pp. 8-9]。

## Reusable Claims
1. **裂缝粗糙度（面积比）可作为水力开度的有效预测指标**：在室温、低围压条件下，面积比越高，水力开度越大，因为粗糙表面的微凸体被压碎后留下更多微裂隙供流体通过 [Jan 2017, pp. 5-9]。  
   *条件*：单条轴向拉张裂缝，围压作用使两壁压紧，岩石为花岗岩。  
   *限制*：该关系基于6个样本，尚未在更高围压或原位应力下验证；当压碎效应有限时，粗糙度与开度的关系可能反转。

2. **围压超过约14 MPa后，裂缝水力开度的应力敏感性显著降低**，表明大部分可闭合的微裂隙已压实 [Jan 2017, pp. 7-9]。  
   *条件*：实验用花岗岩人造裂缝，温度恒定（组一），围压加载历史为逐步递增。  
   *限制*：该阈值可能依赖于岩石类型、裂缝初始粗糙度及加载路径，且未考虑循环加载或长期蠕变。

3. **温度升高通过降低流体粘度而提升导水系数，即使热膨胀使裂缝机械闭合**，因此在中焓地热储层（90–150 °C）中，流体粘度变化是热增产的关键机制 [Jan 2017, pp. 7-8]。  
   *条件*：花岗岩围压8 MPa，温度25–100 °C，单裂缝，流体为水。  
   *限制*：该竞争关系未包含裂隙表面的热-化学溶蚀或沉淀影响，且假设岩石热膨胀各向同性；在更高温度或不同流体下需另评估。

4. **增大液压（从0.1 MPa至0.9 MPa）可提高换热速率**，在固定围压8 MPa条件下，流量增加促进了热提取 [Jan 2017, pp. 8-9]。  
   *条件*：裂缝单一，岩石与流体温度差约5–80 °C，流动时间短（无热突破细节）。  
   *限制*：未给出换热速率的具体数值和效率系数，也未讨论高流速下可能的热非均衡或压力损失。

## Candidate Concepts
- [[fractureroughness]]
- [[hydraulic conductivity]]
- [[cubic law]]
- [[enhanced geothermal systems (EGS)]]
- [[area ratio (morphology)]]
- [[confining pressure]]
- [[thermal expansion of rock]]
- [[fluid viscosity temperature dependence]]
- [[coupled thermo-hydro-mechanical (THM) processes]]
- [[heat transfer efficiency in fractured media]]
- [[single fracture flow]]
- [[fracture aperture]]

## Candidate Methods
- [[improved Brazilian test for artificial fracture creation]]
- [[3D point cloud reconstruction for fracture surface morphology]]
- [[hydraulic test under controlled confining pressure and temperature]]
- [[cubic law for equivalent hydraulic aperture]]
- [[exponential fitting of aperture-temperature relation]]
- [[steady-state heat transfer test with constant inlet temperature]]

## Connections To Other Work
- 本文引用[[DECOVALEX project]]，表明其研究属于国际耦合模型验证框架的一部分，关注THM过程 [Jan 2017, pp. 2-2]。  
- 前人用离散元法研究节理岩体中的热对流 [[Abdallah et al. 1995]]，指出裂缝开度、循环速度和流体粘度是敏感参数，与本文发现的温度-粘度竞争机制一致 [Jan 2017, pp. 2-2]。  
- Morrow等人（2001）观测到花岗岩在水热条件下渗透率降低，Caulk等人（2016）在EGS系统中发现机械效应主导开度变化，本文的围压试验从力学角度补充了裂缝闭合对水力特性的影响，但未涉及长期化学演化 [Jan 2017, pp. 2-2, 9-10]。  
- 可进一步连接的概念包括：[[stress-dependent fracture permeability]]、[[thermo-hydro-mechanical-chemical (THMC) coupling]]、[[local cubic law modifications for roughness]]、[[viscosity-driven permeability enhancement in geothermal systems]]。

## Open Questions
- 未从索引片段中确认作者是否提出了长期渗透率演化的预测模型，以及如何将面积比参数集成至现场尺度的裂隙网络模拟中。  
- 实验中未监测化学溶解或沉淀，热-水-化学（THC）耦合对开度和传热的影响有待研究 [Jan 2017, pp. 2-2, 9-10]。  
- 立方定律在粗糙裂缝、高流速下的适用性边界，以及热非平衡效应对换热速率的影响未进一步探讨。  
- 对于循环加载或不同应力路径下的面积比–水力特性关系，数据尚缺。

## Source Coverage
本页基于该论文的9个索引片段（页码范围约pp. 1-10），覆盖了摘要、引言、部分方法、核心结果和初步讨论。碎片包含了研究目的、人造裂缝制备、3D形态学流程、水力测试程序、围压与温度效应的关键图表描述，以及明确的数量关系（如面积比与开度、开度与温度的指数拟合）。然而，下列重要信息缺失或未详述：实验装置的完整示意图、数据的原始流量和压力记录、传热测试的完整时间序列、误差棒或不确定性分析、结论与展望部分的剩余内容，以及作者提出的关于热-水-力耦合的数值模型或预测关系。研究区地理位置、样品采集的具体层位以及岩石学特征也未在片段中确认。因此，本知识页侧重于已确认的实验观测和相关参数关系，对于机理的深入解释和普适性需要参考全文。
