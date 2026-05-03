---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var"
title: "Heat extraction performance of fractured geothermal reservoirs considering aperture variability."
status: "draft"
source_pdf: "data/papers/2023 - Heat extraction performance of fractured geothermal reservoirs considering aperture variability.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Gao, Xuefeng, et al. \"Heat extraction performance of fractured geothermal reservoirs considering aperture variability.\" *Energy*, vol. 269, 2023, p. 126806. Accessed 2026."
indexed_texts: "14"
indexed_chars: "66924"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "63225"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.944728"
coverage_status: "full-index"
source_signature: "c2eef8f2993afa68b8bfe46bc935348fad213c03"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:39:41"
---

# Heat extraction performance of fractured geothermal reservoirs considering aperture variability.

## One-line Summary
通过将含有接触障碍体的异质孔径场植入不同连接路径与密度的离散裂隙网络（DFN），该研究发现裂缝系统中的流动通道化使有效流动面积不足40%，且生产温度与累积产热量均与孔径场的相关长度呈线性关系，表明孔径变异引起的流动通道化是控制裂隙地热储层产能的核心因素。

## Research Question
裂缝性热储中，孔径变异性（异质性）如何通过流动通道化影响网络尺度的流体运移与采热性能？传统平行板模型忽略孔径变异，其产能预测误差如何受相关长度、裂隙密度等因素影响？

## Study Area / Data
研究未针对特定地热场地，而是使用一套由随机生成的三维DFN模型构成的数值算例。模型域为20 m × 20 m × 15 m，包含三组相互正交的方形裂隙子集，每组6条，裂隙面为边长8.86 m的四边形面片。构建了五种不同连接路径与密度的DFN方案：短路径（L_sp）、中路径（L_mp）、长路径（L_lp），以及它们叠加形成的L_smp和L_smlp。裂隙密度P32范围为0.0916 m²/m³至0.2486 m²/m³。每条裂隙均赋予由序贯高斯模拟（SGSIM）生成的异质孔径场，均值0.2 mm，方差0.04 mm²，相关长度φ取0.5、1.0、1.5、2.0 m四个水平，各实现20次；局部孔径＜0.2 μm被视为接触障碍并将其替换为0.2 μm。同时设置等均值（0.2 mm）的平行板模型作为对照。上述所有碎片均来自[Gao 2023, pp. 1-2, 2-3, 3-4]。

## Methods
1. **DFN模型构建**：随机生成三组正交裂隙网络，通过叠加形成不同连接路径长度和密度的方案（L_sp、L_mp、L_lp、L_smp、L_smlp），并使用水平压裂裂缝沟通注采双井以减小注入方式的不确定性 [Gao 2023, pp. 2-3]。
2. **多尺度孔径场生成**：基于序贯高斯模拟（SGSIM）和球形变异函数模型（式(2)）生成孔径场，控制参数为均值d_f=0.2 mm，方差σ²=0.04 mm²和相关长度φ=0.5–2 m。将孔径小于0.2 μm的节点替换为0.2 μm以模拟接触障碍体 [Gao 2023, pp. 2-4]。
3. **流动与传热模拟**：采用达西定律描述裂隙与基质中的流体流动（式(3)-(4)），利用立方定律（式(5)）由孔径计算裂隙渗透率，粗糙度因子取1.4。能量守恒方程（式(6)-(9)）通过COMSOL Multiphysics求解器实现流‑热耦合。模拟采用稳态压力初始化后进行瞬态热‑水力耦合计算。注水压力5.5 MPa，生产压力5 MPa，注入水温30 °C，储层初始温度200 °C [Gao 2023, pp. 4-5]。
4. **模型验证**：将数值解与Lauwerier解析解进行对比，在裂隙长度20 m、50 m、70 m、100 m处吻合良好，验证了数值方法的可靠性 [Gao 2023, pp. 5-6]。
5. **后期分析**：提取生产温度T_pro、流量分布，使用有效流动面积A_eff（取截止流量q_c=5×10⁻⁶ m²/s）、有效流动强度EFI（A_eff/A_f）、累积产热量E_pro等指标量化流动通道化对采热的影响 [Gao 2023, pp. 8-10]。

## Key Findings
1. 在变孔径裂隙系统中出现显著的流动通道化，有效流动面积占比（EFI）不足40%；接触障碍体和相关长度增加使流动通道数量减少、宽度增大，但总有效流动面积下降[Gao 2023, pp. 1-1, 8-9]。
2. 生产温度T_pro与孔径场的相关长度φ呈线性正相关（T_pro = a + α φ）；平行板模型低估T_pro，且低估程度随φ增大而加剧。T_pro的变异系数（CV）随φ增大而升高，表明预测不确定性增加[Gao 2023, pp. 5-7]。
3. 裂隙网络中的优势流动通道会因孔径场变异而发生迁移和重选（流动拓扑网络图8），这不同于平行板模型的固定流径，是生产观测不确定性的重要来源[Gao 2023, pp. 8-9]。
4. 累积产热量E_pro随φ增大而减小，主要因流量Q_pro减少导致；E_pro与φ呈线性负相关。平行板模型对E_pro的预测先低估后高估[Gao 2023, pp. 9-10]。
5. 有效流动强度EFI与裂隙密度P32和连接路径长度无关，但与φ呈负相关[Gao 2023, pp. 8-9]。
6. 有效流动面积A_eff与累积产热量E_pro之间存在强对数或线性关系（R²均高），说明流动通道是裂隙网络中换热和流体输运的主要场所。裂隙开孔面积A_o也可作为E_pro的预测工具，但其适用范围限于小相关长度（φ较小）的场景[Gao 2023, pp. 10-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 变孔径DFN中有效流动面积占比低于40%（EFI≈40%），约一半的裂隙区域无显著流动 | [Gao 2023, pp. 1-1, 8-9] | φ=0.5–2 m，d_f=0.2 mm，σ²=0.04 mm²，q_c=5×10⁻⁶ m²/s | 平行板模型假设100%参与流动 |
| T_pro与φ呈线性关系：T_pro = a + α φ；随φ增大，T_pro升高 | [Gao 2023, pp. 6-7] | 五组DFN模型，操作条件如表2～3 | a为与运行参数相关的基准常数 |
| 平行板模型对T_pro的平均低估率AUR随φ增大而增大，且AUR_sp > AUR_mp > AUR_lp | [Gao 2023, pp. 7-8] | 同上述孔径与操作条件 | 延伸连接路径长度可降低AUR |
| 有效流动强度EFI与裂隙密度P32无关，与φ呈负相关 | [Gao 2023, pp. 8-9] | φ=0.5–2 m，DFN的P32=0.0916–0.2486 m²/m³ | 封闭面积A_cl仅占1–9% |
| 累积产热量E_pro随φ增大而减小（因Q_pro降低），E_pro与φ可用线性模型描述 | [Gao 2023, pp. 9-10] | 同操作条件 | E_pro的主要贡献来自ΔT和Q_pro，Q_pro下降主导 |
| A_eff与E_pro呈强对数/线性相关；EFI与E_pro呈对数相关 | [Gao 2023, pp. 10-11] | φ=0.5–2 m，所有DFN方案 | 亦可用开孔面积A_o预测E_pro，但小φ时适用 |
| 随φ增大，流动拓扑中优势通道发生迁移，通道位置不固定 | [Gao 2023, pp. 8-9] | L_smlp案例，第5、20实现对比 | 该重选现象是平行板模型不具备的 |
| T_pro的变异系数CV随φ增大而升高，裂隙密度增加会放大CV增量 | [Gao 2023, pp. 6-7] | 第200天统计，所有实现 | 长连接路径可减弱观测离散度 |

## Limitations
- 未考虑原位应力对孔径场的影响：实际中正应力通过压缩或拉伸改变孔径均值，剪应力通过剪胀效应影响接触障碍体比例和孔径场结构。本模型采用正交裂隙弱化了剪胀效应[Gao 2023, pp. 12-12]。
- 数值模拟未与现场生产数据直接对比，仅通过解析解验证，因此产能预测的绝对误差范围需在实际场地中进一步检验[Gao 2023, pp. 5-6, 12-12]。
- 孔径场基于SGSIM生成的合成场，其统计特征（正态分布、球形变异函数）虽在实验室观测中有依据，但真实储层孔径分布可能更复杂[Gao 2023, pp. 1-1, 2-3]。
- 模型未考虑化学沉淀/溶解对孔径的时变影响，仅考虑静态非均质孔径场[Gao 2023, pp. 1-1]。

## Assumptions / Conditions
- 流体在裂隙和基质中为层流，符合达西定律；裂隙渗透率满足局部立方定律，粗糙度因子δ固定为1.4[Gao 2023, pp. 4-4]。
- 储层基质为低渗透（k=2×10⁻¹⁶ m²），裂隙为主要导流通道；热物性参数（比热容、密度、导热系数）不随温度变化（表2），但水的物性参数（ρ_w, C_p,w, λ_w）随温度演化，依赖温度[Gao 2023, pp. 4-5]。
- 模型边界为绝热、不渗透，模拟域50×50×40 m³，DFN模型置于中心；注采井水平段以恒定压力（5.5 MPa注入，5 MPa产出）驱动，压差0.5 MPa维持层流[Gao 2023, pp. 4-5]。
- 孔径场各向同性（主值在各方向相同），忽略裂隙面内各向异性；接触障碍体定义为局部孔径<0.2 µm并被替换为0.2 µm[Gao 2023, pp. 3-4]。
- 裂隙全部连通，孤立裂隙因对流体输送贡献可忽略而未包含[Gao 2023, pp. 2-3]。

## Key Variables / Parameters
- **相关长度 φ**：0.5、1.0、1.5、2.0 m，表征孔径场的空间连续性，是控制异质性的核心参数[Gao 2023, pp. 3-4]。
- **裂隙密度 P32**：0.0916 m²/m³（L_sp/L_mp/L_lp）、0.1701 m²/m³（L_smp）、0.2486 m²/m³（L_smlp），衡量网络尺度裂隙发育程度[Gao 2023, pp. 3-3]。
- **有效流动面积 A_eff**：基于截止流量 q_c=5×10⁻⁶ m²/s 划分，量化实际参与流动的裂隙面积[Gao 2023, pp. 8-9]。
- **有效流动强度 EFI** = A_eff / A_f ×100%，衡量流动通道化程度[Gao 2023, pp. 8-9]。
- **生产温度 T_pro** 和 **累积产热量 E_pro**：主要生产观测指标。
- **平均低估率 AUR**：量化平行板模型对非均质模型生产温度的预测偏差[Gao 2023, pp. 6-7]。
- **变异系数 CV**：评估因孔径变异性引起的生产数据的离散度。
- **开孔面积 A_o**：直接由孔径场统计的连通区域，与A_eff对比。
- **孔径统计参数**：均值 d_f=0.2 mm，方差 σ²=0.04 mm²。

## Reusable Claims
- 在裂隙型地热储层中，即使裂隙密度较高，流动通道化仍会使有效流动面积占比低于40%，因此基于全区域利用假设的模型会显著高估产能 [Gao 2023, pp. 1-1, 8-9]。
- 当孔径场呈各向同性异质且服从正态分布时，生产温度与相关长度之间呈线性增加关系，该关系可作为利用生产数据反演相关长度的理论依据 [Gao 2023, pp. 6-7]。
- 平行板模型（均匀孔径）会系统性低估生产温度，且低估程度随相关长度增大而增大，而随连接路径长度增加而减小，提示在评价长路径储层时该模型的误差可能相对较小 [Gao 2023, pp. 7-8]。
- 裂隙密度虽能增加有效流动面积，但无法提升有效流动强度（相对占比），即新增裂隙对缓解通道化的作用有限 [Gao 2023, pp. 8-9]。
- 累积产热量与有效流动面积之间存在强线性/对数关系，因此可通过简易的流动面积估算来快速预测储层的产热能力，但这种方法仅在已知孔径统计特征（均值、方差、相关长度）的前提下可靠 [Gao 2023, pp. 10-11]。
- 当相关长度较小时，裂隙开孔面积可近似代替有效流动面积用于产能预测；而当相关长度较大时，两者差异增大，开孔面积的预测能力下降 [Gao 2023, pp. 10-11]。
- 优势流动通道在DFN中会随孔径场的不同实现而迁移（重选），这一特性是生产观测离散度的重要来源，并在流动拓扑网络中可被清晰识别 [Gao 2023, pp. 8-9]。

## Candidate Concepts
- [[flow channelization]]
- [[aperture variability/heterogeneity]]
- [[effective flow area]]
- [[effective flow intensity (EFI)]]
- [[contact obstacles]]
- [[correlation length]]
- [[discrete fracture network (DFN)]]
- [[preferential flow channel]]
- [[flow topology network]]
- [[local cubic law]]
- [[sequential Gaussian simulation (SGSIM)]]
- [[parallel plate model]]
- [[average underestimation rate (AUR)]]
- [[coefficient of variation (CV)]]
- [[scaling of production temperature]]
- [[cumulative heat energy production]]

## Candidate Methods
- [[discrete fracture network (DFN) modeling]]
- [[sequential Gaussian simulation (SGSIM) for aperture field]]
- [[Darcy’s law + local cubic law for fracture flow]]
- [[thermo-hydraulic coupling with COMSOL]]
- [[flow channelization quantification via cutoff flow rate]]
- [[effective flow area partitioning]]
- [[flow topology network graph]]
- [[Lauwerier analytical solution validation]]
- [[correlation analysis: linear/logarithmic fit between A_eff and E_pro]]
- [[machine learning inversion framework for correlation length]]

## Connections To Other Work
- 本文工作与EGS Collab现场的流动通道化观测（Fu et al., 2021; Wu et al., 2021）相呼应，后者在中尺度现场测试中证实了孔径变异引发的显著通道化 [Gao 2023, pp. 1-1]。
- 早期单裂隙通道化实验（Brown et al., 1998; Abelin et al., 1988）和网络尺度非均匀流动模拟（Hyman et al., 2021; Kang et al., 2020）为本研究的认识基础 [Gao 2023, pp. 1-2, 13-13]。
- 关于裂隙密度、粗糙度对网络换热的影响，Yao et al. (2020)、Chen et al. (2018) 等研究指出粗糙度会延长热突破时间并提升等效换热系数，本文进一步量化了孔径相关长度对生产观测的线性影响 [Gao 2023, pp. 2-2, 10-10]。
- Pandey & Chaudhuri (2017)、Guo et al. (2016) 等开展了单裂隙尺度的变孔径采热模拟，本文将其扩展至网络尺度，并强调了流动通道重选现象 [Gao 2023, pp. 2-2]。
- 方法论上，SGSIM孔径场生成、局部立方定律应用参考了Okoroafor et al. (2022) 与Brush & Thomson (2003) 等 [Gao 2023, pp. 3-4, 13-13]。

## Open Questions
- 原位应力（特别是剪应力）如何改变孔径场的接触率与结构，进而影响网络尺度的流动通道化及生产观测？[Gao 2023, pp. 12-12]
- 能否利用生产井的温度、流量数据和机器学习框架（如Wu et al., 2021）反演难以直接测量的相关长度参数？[Gao 2023, pp. 12-12]
- 在非正交、更符合天然裂隙分布的DFN中，连接路径长度的定义与观测不确定性之间的关系是否仍成立？
- 考虑长期运行中矿物溶解/沉淀导致的孔径动态演化后，有效流动面积与累积产热量的关系将如何变化？
- 现场规模的裂隙网络（远超20 m尺度）中，相关长度的尺度依赖性是否依然保持线性？生产温度与相关长度的线性关系是否存在尺度上限？

## Source Coverage
本页面基于全部14个非空索引片段编译。所有索引源块均被处理（覆盖率100%），编译后总字符数为63,225，占索引总字符数66,924的94.47%（因格式转换和摘要省略造成少量字符未直接复用）。阶段数为1，采用单次整合策略。覆盖审计确认全文核心论点、方法、数据、结果及讨论均被纳入。
