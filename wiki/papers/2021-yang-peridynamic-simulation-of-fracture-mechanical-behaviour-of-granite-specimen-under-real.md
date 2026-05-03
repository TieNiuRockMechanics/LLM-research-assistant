---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-yang-peridynamic-simulation-of-fracture-mechanical-behaviour-of-granite-specimen-under-real"
title: "Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments."
status: "draft"
source_pdf: "data/papers/2021 - Peridynamic simulation of fracture mechanical behaviour of granite specimen under real-time temperature and post-temperature treatments.pdf"
collections:
  - "zotero new"
citation: "Yang, Zhen, et al. \"Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 138, 2021, article 104573."
indexed_texts: "16"
indexed_chars: "75525"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "70122"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.928461"
coverage_status: "full-index"
source_signature: "32052e41f70d84635bfd2e3a497a85d5352cc1ba"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:35:15"
---

# Peridynamic Simulation of Fracture Mechanical Behaviour of Granite Specimen under Real-Time Temperature and Post-Temperature Treatments.

## One-line Summary
本研究在普通态基近场动力学框架下建立完全耦合的热力模型，分析实时温度（RT）与降温后温度（PT）条件下花岗岩的力学响应与破裂特征。

## Research Question
What are the differences in mechanical properties and fracture characteristics (stress-strain, cracking patterns, failure mode) of granite specimens subjected to real-time high temperature (RT) tests compared to post-temperature (PT) tests? Can PT test results be used to approximate RT conditions?

## Study Area / Data
- 花岗岩试样几何（数值标定阶段）：长 L=25 mm，高 H=50 mm；另一组验证实例：长 L=50 mm，高 H=100 mm。
- 温度工况：25 °C、200 °C、300 °C、400 °C、500 °C、600 °C、700 °C、800 °C。
- 矿物组分与热膨胀系数参考 Wang et al. (24) 和 Yin et al. (25)，见表5及图10。
- 实验对比数据：峰值强度、峰值轴向应变、破坏模式来自 Wang et al. (24) 和 Yin et al. (25)。

## Methods
- 理论框架：Fully coupled ordinary state-based peridynamics (OSB-PD) thermo-mechanics，基于 Oterkus et al. (39,40) 和 Gao and Oterkus (42)。
- 控制方程：运动方程（式1）、热扩散方程（式2），包含变形对温度影响的耦合项。
- 热边界：辐射加热采用 Stefan-Boltzmann 方程（式5），通过虚拟边界层施加，并在加热阶段采用逐步升温以避免热冲击（式6）。
- 非均质性实现：根据矿物类型与含量随机分配热膨胀系数（Yang et al. 43），用 shuffle 算法生成随机分布阵列。
- 改进的多层计算方法（Modified multi-layer computational method）：热力层尺寸大于力学层，热力层的额外区域承受热冲击；加载前将热力层损伤信息移植到力学层对应位置并裁剪掉额外区域数据（图9，表4），以消除温度梯度诱发的裂纹（热冲击裂纹）的效应。
- 时间积分：热过程采用多速率显式格式并施加稳定温度场条件|T^{n+1}_i - T^n_i|<ε；力学过程准静态采用自适应动态松弛（ADR），动态采用前向差分。
- 破坏准则：基于临界伸长量 s_0 的键断裂准则（式8），局部损伤 ϕ 定义为断裂键占比（式7）。
- 数值收敛性验证：方形板热传导模型进行 m-convergence 和 δ-convergence 测试（图5-6，表1）。
- 参数标定：室温单轴压缩实验标定泊松比 υ = 0.25 和断裂能释放率 G_0 = 70 J/m^2（图7-8，表2-3）。
- 模拟流程：PT 测试先加热至目标温度，自然冷却至室温后加载；RT 测试在目标温度下恒温加载（图4）。

## Key Findings
1. RT 试样的峰值强度低于 PT 试样，若用 PT 结果近似 RT 工况会高估岩石强度（第6节结论1）。
2. 高温处理产生不连续的热循环裂纹，单轴压缩使其扩展，导致宏观延性增强；总体而言 RT 试样延性高于 PT 试样（第6节结论2）。
3. 在 RT 试验中，热循环裂纹在持续高温下扩展为交错或分叉裂纹，并在外力下聚合；PT 试验中裂纹主要在热损伤严重区域沿最大剪应力方向扩展，裂纹表面较 RT 平滑（第6节结论3）。
4. 随着试验温度升高，破坏模式由拉剪混合向拉伸主导最后转变为拉伸破坏（第6节结论4）。
5. 数值模拟正确重现了热循环裂纹和热梯度诱发裂纹的区别，验证了改进多层计算方法的有效性（第4.3.1节，图12-15）。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| RT 试样峰值强度始终低于 PT 试样，且差异在500°C以上更明显 | Yang 2021, pp. 19-20; 图16(b) | 单轴压缩，温度25-700°C | 与 Wang et al. (24) 实验一致 |
| RT 试样表现出更高的延性，峰后应力下降较缓 | Yang 2021, pp. 15-16; 图16(a) | 单轴压缩，RT 与 PT 对比 | 归因于热循环裂纹的持续调整 |
| 破坏模式随温度升高从拉剪混合转为拉伸主导 | Yang 2021, pp. 19-20; 图20, 图21-24 | 温度200-800°C | 数值与实验破坏形态吻合 |
| 改进多层方法消除了热梯度裂纹影响，成功分离热循环裂纹与梯度裂纹 | Yang 2021, pp. 12-13; 图15 | 热力层尺寸大于力学层 | 验证了方法的可靠性 |
| 热循环裂纹在不均匀矿物热膨胀系数差下产生，与温度梯度无关 | Yang 2021, pp. 12-13; 图12-14 | 预加热阶段 | 符合 Simmons & Cooper (20) 两种裂纹分类 |
| 数值模型未能再现孔隙率效应导致峰值轴向应变小于实验值 | Yang 2021, pp. 15-16 | 所有温度 | 作者建议未来加入孔隙微结构 |

## Limitations
- 未考虑加热和加载过程中孔隙的产生与演化，导致模拟峰值轴向应变显著低于实验值。
- 材料参数假设与温度无关，未考虑高温下弹性模量、强度等参数的变化。
- 二维 PD 模型无法完全表征三维裂纹扩展和破坏形态，特别是碎块的分离过程。
- 热导率、比热等热物性参数取自文献恒定值，未随温度和损伤演化。
- 辐射加热通过虚拟边界层简化，未考虑真实试样与加热元件的几何及辐射视角因素。
- 数值时间步受限于临界时间步，无法采用实验中极低的升温速率，仍存在一定的热梯度效应。

## Assumptions / Conditions
- 材料均质化假设，通过随机赋值热膨胀系数体现矿物非均质性，但不考虑颗粒形状和界面弱化。
- 二维平面应力假设，试样厚度方向均匀。
- 准静态加载速率设定为 0.05 m/s（远高于实验速率），但通过 ADR 技术得到稳定解。
- 加热阶段采用大于设计温度的辐射源温度以建立温度势，并施加稳态温度场判断条件 |T^{n+1}_i - T^n_i|<ε。
- 临界伸长量 s_0 基于 OSB-PD 断裂能释放率 G_0 计算，且 G_0 经室温实验标定后适用于所有温度。
- 热力层和力学层共享损伤数组，热力层尺寸比力学层每边扩大 7.5 mm（x向）和 15 mm（y向）（4.2节）。
- 计算所用具体参数见表6：网格 80×160（热力层）、50×100（力学层），时间步 Δt_TH = 2×10^{-5} s，Δt_ME = 5×10^{-8} s 或 ADR Δt_ME = 1。

## Key Variables / Parameters
- 矿物热膨胀系数：长石 8.7×10^{-6} K^{-1}，石英 24.3×10^{-6} K^{-1}，黑云母 3.0×10^{-6} K^{-1}（表5）。
- 力学参数：E = 20 GPa, ν = 0.25, ρ = 2620 kg/m³, G_0 = 70 J/m²（标定值，3.2节）。
- 热参数：k_T = 3.5 W/(m·°C)，c_v = 900 J/(kg·°C)（表6）。
- 辐射温度 Θ_ss 和升温时间 t_0：升温速率 Θ_ss/t_0 = 0.01 °C/步，总加热时间 300 s（图11）。
- 非局部参数：m = δ/Δx = 3，Δx = 0.5 mm，δ = 1.5 mm（标定推荐，4.2节）。
- 试验温度：25, 300, 500, 700 °C（主要算例）；25, 200, 400, 600, 800 °C（第二算例）。
- 破坏指标：局部损伤 ϕ，临界伸长量 s_0（式7,8）。

## Reusable Claims
1. **[Fully coupled OSB-PD model with thermal cracking]** A fully coupled ordinary state-based peridynamic model can reproduce thermal cycling cracks and thermal gradient-induced cracks in granite under controlled heating conditions, provided mineral heterogeneity is represented via randomly assigned thermal expansion coefficients. Conditions: thermal and mechanical layers share damage field; failure governed by critical stretch; heating implemented via radiative boundary with gradual ramp-up.
2. **[Effect of test method on strength]** For granite subjected to high-temperature uniaxial compression, the real-time (RT) peak strength is consistently lower than the post-temperature (PT) peak strength across the range 25–700°C, implying that PT tests overestimate in-situ strength at elevated temperature. Conditions: same heating rate, cooling rate, and loading rate in both test types; material properties assumed temperature-independent.
3. **[Failure mode transition with temperature]** With increasing temperature from 25 to 800°C, the failure mode of both RT and PT granite samples shifts from mixed tensile-shear to tensile-dominated, and finally to pure tensile failure. Conditions: uniaxial compression; 2D OSB-PD simulation with the proposed multi-layer method; validated against experimental observations (Wang et al. 24; Yin et al. 25).
4. **[Modified multi-layer method to eliminate thermal shock cracks]** An extended thermal layer with a sacrificial boundary region effectively prevents thermal gradient-induced cracks from affecting the mechanical layer, allowing the mechanical response to be dominated solely by thermal cycling cracks. Conditions: thermal layer dimensions exceed mechanical layer by specified margins (Γ_x, Γ_y); damage array is shared and spatially cropped.
5. **[Ductility enhancement in RT tests]** RT specimens display greater macroscopic ductility (lower post-peak stress drop) than PT specimens, especially at 500°C, due to continuous propagation and adjustment of thermal cycling cracks during loading under sustained high temperature. Conditions: constant temperature during mechanical loading for RT; complete cooling before loading for PT.

## Candidate Concepts
- [[ordinary state-based peridynamics]]
- [[fully coupled thermo-mechanical model]]
- [[thermal cycling crack]]
- [[thermal gradient-induced crack]]
- [[modified multi-layer computational method]]
- [[radiation heating boundary]]
- [[critical stretch criterion]]
- [[rock heterogeneity representation]]
- [[non-local damage]]
- [[post-temperature treatment]]
- [[real-time temperature treatment]]

## Candidate Methods
- [[peridynamic heat conduction convergence test]]
- [[peridynamic uniaxial compression calibration]]
- [[adaptive dynamic relaxation (PD)]]
- [[multi-rate explicit time integration (thermo-mechanics)]]
- [[shuffle algorithm for mineral distribution]]
- [[thermal damage transplantation technique]]
- [[m- and δ-convergence tests in PD]]
- [[two-layer PD for thermal-mechanical coupling]]

## Connections To Other Work
- **Simmons & Cooper (20)**: Provided the conceptual distinction between thermal cycling cracks and thermal gradient-induced cracks that this study explicitly modeled.
- **Oterkus et al. (39,40) and Gao & Oterkus (42)**: Established the fully coupled OSB-PD thermo-mechanics framework adopted herein.
- **Wang et al. (24)** and **Yin et al. (25)**: Provided experimental data (AE characteristics, mechanical damage, stress–strain, failure modes) for granite under RT and PT conditions, used for model validation.
- **Yang et al. (43)**: Proposed the mineral heterogeneity assignment method used to model incompatible thermal expansion.
- **Wang, Zhou et al. (31,32,37,38)**: Earlier PD models for cracking in rocks and thermal failure, but did not differentiate RT and PT or eliminate thermal shock effects.
- **Tiskatine et al. (18)**: Highlighted quartz as a key mineral controlling thermal cracking, consistent with the heterogeneous thermal expansion approach.

## Open Questions
- How can porosity evolution during heating and loading be incorporated into the PD model to better capture the increase in axial strain with temperature?
- What is the influence of temperature-dependent material properties (E, ν, k_T, c_v) on the predicted failure behavior, and how can they be calibrated for a coupled thermo-mechanical model?
- Can this approach be extended to 3D without prohibitive computational cost to capture volumetric fragmentation and true triaxial stress states?
- How does the size of the sacrificial thermal layer (Γ_x, Γ_y) affect the residual thermal gradient effect and the resulting failure mechanisms, and what are the optimal dimensions for different rock types?
- What are the implications of the RT/PT strength and ductility differences for long-term storage or geothermal applications, where the rock is continuously heated under load?

## Source Coverage
所有非空索引片段（共 16 个，含 70122 字符）均被处理并用于编译本页面。索引片段覆盖论文全文，包括标题、摘要、引言、方法（2.1–2.4）、验证与标定（3.1–3.2）、数值模型准备（4.1–4.2）、结果（4.3）、讨论（5）、结论（6）及参考文献。覆盖比例（按字符）为 92.8%。
