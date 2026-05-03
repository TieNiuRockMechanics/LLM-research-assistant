---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-pai-an-investigation-on-the-deterioration-of-physical-and-mechanical-properties-of-granite"
title: "An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock."
status: "draft"
source_pdf: "data/papers/2021 - An investigation on the deterioration of physical and mechanical properties of granite after cyclic thermal shock.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Pai, Ning, et al. “An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock.” *Geothermics*, vol. 97, 2021, 102252."
indexed_texts: "13"
indexed_chars: "62842"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "59651"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.949222"
coverage_status: "full-index"
source_signature: "56da6d829f1bf5a471c3dc9fb9c250cb5dc1771f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:54:16"
---

# An Investigation on the Deterioration of Physical and Mechanical Properties of Granite after Cyclic Thermal Shock.

## One-line Summary

针对干热岩地热开采中储层花岗岩频繁遭受热冲击的工程背景，本文通过0~20次循环热冲击后花岗岩的物理力学性质试验和ANSYS数值模拟，揭示了循环热冲击导致花岗岩物理力学性质劣化的规律及其热应力–热裂纹机制。

## Research Question

循环热冲击如何影响花岗岩的纵波波速、导热系数、孔隙度、强度、变形及声发射特征？其内部劣化机理与热应力分布规律是什么？对增强型地热系统（EGS）的储层改造与长期可靠性有何启示？

## Study Area / Data

- **样品来源**：山东省济宁市花岗岩，密度2.56–2.67 g/cm³，天然纵波波速3509–3636 m/s，矿物成分为石英、钠长石、斜长石、黑云母。
- **样品制备**：同一岩体沿同一钻进方向取芯，按ISRM建议加工为直径50 mm、高100 mm的标准圆柱样，每试验组至少3个样品。
- **试验条件**：热冲击循环次数0（天然状态）、1、5、10、20次；以5°C/min升温至450°C恒温2 h，立即置于冷水（室温）中急冷；循环后测量纵波波速、导热系数、孔隙度，并进行单轴压缩及声发射试验。
- **数值模型参数**：直径0.05 m，高0.10 m，弹性模量16.62 GPa，泊松比0.25，导热系数3.28 W·m⁻¹·K⁻¹，比热容1058 J/kg·K⁻¹，线热膨胀系数3.57e-6，对流换热系数300 W·m⁻²·K⁻¹，密度2692 kg/m³，环境温度298 K，初始岩石温度723 K。

## Methods

- **循环热冲击试验**：箱式气氛炉以5°C/min升温至450°C，保温2 h后取出并浸入冷水中冷却；用高精度热电偶监测表面温度降至室温（约12 min），继续浸泡1 h后擦拭干燥；重复至设定次数。
- **物理参数测量**：HC-U81超声波监测仪测量纵波波速（精度0.1 μs）；HotDisk TPS 500热常数分析仪（瞬态平板热源法）测量导热系数；真空饱和容器（φ200mm×400 mm，负压1 MPa）结合烘干称重法间接测量孔隙度（水饱和质量m_s、干质量m_d及体积V）。
- **力学与声发射试验**：MTS816电液伺服岩石试验系统（最大轴压1459 kN）进行单轴压缩，加载速率0.002 mm/s；PCI-2声发射系统采集信号，门槛值35 dB，前置放大器增益40 dB，采样频率2 MHz；记录轴向载荷、位移、AE计数与时间。
- **数值模拟**：ANSYS建立轴对称模型，所有边界设为对流换热边界，分析热冲击过程中瞬时温度场及热应力σ_x、σ_y的演化。

## Key Findings

1. **物理性质劣化**：随循环次数增加，纵波波速从3572 m/s降至1469 m/s（−58.9%），导热系数从3.283 W·m⁻¹·K⁻¹降至1.840 W·m⁻¹·K⁻¹（−43.9%），孔隙度从0.321%升至2.491%（+676.0%）；前10次循环导致的劣化占总变化幅度的85%以上。
2. **力学性质劣化**：峰值强度从157.6 MPa降至60.7 MPa（−61.5%），峰值应变先非线性增加（首次循环增25.2%）后减少；弹性模量从16.65 GPa降至8.94 GPa（−46.3%），变形模量从11.93 GPa降至3.28 GPa（−72.5%）；首次热冲击对变形模量影响显著（降幅占59.7%），前10次对弹性模量影响占91.1%。
3. **应力–应变特征**：循环后曲线呈现初始压密段凹形明显、线弹性段斜率降低、裂纹扩展段延长、破坏段阶梯状下降；花岗岩由脆性逐渐转向延性。
4. **声发射特征**：循环后初期压密段AE计数显著升高；裂纹扩展起始及整个扩展阶段的最大AE计数均低于天然状态，系因已有热裂纹提供了额外的能量释放路径。
5. **热应力机制**：热冲击初期模型内部形成巨大瞬时温差，最大温差出现在60 s（中心413°C，表面141°C）；热应力快速增大后缓慢消散。花岗岩外部主要受竖向拉应力（最大9.18 MPa），内部主要受竖向压应力（最大7.59 MPa）。拉应力导致表面萌生与扩展二次热裂纹，压应力使内部有利方位的先存微裂纹扩展。

## Core Evidence Table

| 证据 | 出处 | 条件 | 备注 |
|------|------|------|------|
| 纵波波速从3572 m/s降至1469 m/s（−58.9%） | Pai 2021, p.4-5, Table 1 | 0~20次循环热冲击，450°C水冷 | 前10次降幅占93.2% |
| 导热系数从3.283降至1.840 W·m⁻¹·K⁻¹（−43.9%） | Pai 2021, p.4-5, Table 1 | 同上 | 热阻增大所致 |
| 孔隙度从0.321%升至2.491%（+676.0%） | Pai 2021, p.4-5, Table 1 | 同上 | 前10次增幅占85.6% |
| 峰值强度从157.6 MPa降至60.7 MPa（−61.5%） | Pai 2021, p.5-6, Table 2 | 同上 | 首次循环后132.0 MPa |
| 峰值应变首次循环后增25.2%，后下降 | Pai 2021, p.5-6, Table 2 | 同上 | 1次:1.390%→10次:1.425%→20次:1.360% |
| 弹性模量从16.65 GPa降至8.94 GPa（−46.3%） | Pai 2021, p.6-7, Table 3 | 同上 | 前10次降幅占91.1% |
| 变形模量从11.93 GPa降至3.28 GPa（−72.5%） | Pai 2021, p.6-7, Table 3 | 同上 | 首次循环降幅占59.7% |
| 天然花岗岩裂纹扩展起始最大AE计数24.57×10³，扩展阶段26.76×10³；20次后分别降至7.78×10³、22.70×10³ | Pai 2021, p.7-8, Table 5 | 同上 | 多能量释放路径 |
| 模型表面竖向拉应力最大9.18 MPa，内部竖向压应力最大7.59 MPa | Pai 2021, p.9-10, Fig.17–18 | 450°C→室温水冷瞬态模拟 | 最大应力出现在高度方向 |
| 循环热冲击后花岗岩表面出现环向与轴向宏观裂纹，SEM显示裂纹长度和开度显著增加而数量增长不明显 | Pai 2021, p.6 Fig.9, p.10 Fig.19 | 20次热冲击后 | 表面图及微观图像 |

## Limitations

- 每组样品数量为至少3个，样本量较小。
- 仅针对济宁花岗岩一种岩性、450°C单一目标温度和自来水急冷方式，结论的普适性受限。
- 数值模型中部分热力学参数（泊松比、比热容等）引用文献，对流换热系数通过表面冷却曲线标定，与实际工程条件存在偏差。
- 未考虑循环过程中水流与岩石的化学相互作用及地应力耦合效应。

## Assumptions / Conditions

- 5°C/min升温速率视为不引起花岗岩热损伤的临界速率（参照文献）。
- 孔隙度通过水饱和–烘干称重法间接计算，假设水完全充填连通孔隙。
- 数值模拟采用轴对称二维模型，边界均为对流换热条件，忽略辐射换热。
- 热冲击过程中室温水温恒定，样品表面水分擦拭后测温，不计蒸发影响。

## Key Variables / Parameters

- **自变量**：热冲击循环次数（0,1,5,10,20）。
- **因变量（物理）**：纵波波速V_p、导热系数λ、孔隙度φ。
- **因变量（力学）**：峰值强度σ_c、峰值应变ε_c、弹性模量E、变形模量E_50、全程应力–应变曲线。
- **因变量（声发射）**：各阶段AE计数与累计计数。
- **数值模拟变量**：瞬时温度场、水平热应力σ_x、竖向热应力σ_y。
- **模型输入参数**：导热系数、比热容、线热膨胀系数、对流换热系数、密度、初始温度等。

## Reusable Claims

1. 首次热冲击对花岗岩物理力学性质的劣化最为严重，当循环次数超过10次后劣化趋势减缓。 *[Pai 2021, pp. 1 abstract; 结论1]*
2. 循环热冲击后矿物颗粒间接触热阻增大是花岗岩导热系数降低的主要原因。 *[Pai 2021, pp. 4-5; 结论2]*
3. 局部应力集中效应增强和局部承载能力差异增大导致花岗岩峰值强度持续下降和延性特征增强。 *[Pai 2021, pp. 5-6; 结论2]*
4. 热裂纹的存在使加载过程中能量释放路径增多，因此循环热冲击后花岗岩在裂纹扩展起始及整个扩展阶段的最大声发射计数均小于天然花岗岩。 *[Pai 2021, pp. 7-8; 结论3]*
5. 热冲击过程中花岗岩外部主要承受竖向拉应力（最大9.18 MPa），内部主要承受竖向压应力（最大7.59 MPa）；竖向应力占主导。 *[Pai 2021, pp. 9-10; 结论4]*
6. 劣化的两个本质原因：内部压应力导致有利取向先存微裂纹扩展；表面拉应力导致二次热裂纹的萌生与扩展。 *[Pai 2021, pp. 11; 结论5]*

## Candidate Concepts

- [[hot dry rock geothermal resources]]
- [[enhanced geothermal system (EGS)]]
- [[cyclic thermal shock]]
- [[physical and mechanical properties deterioration]]
- [[thermal stress]]
- [[contact thermal resistance]]
- [[thermal cracks]]
- [[microcrack network]]
- [[acoustic emission characteristics]]
- [[ductility enhancement]]
- [[local stress concentration]]
- [[temperature gradient]]
- [[numerical simulation of thermal stress]]

## Candidate Methods

- [[cyclic thermal shock test with box furnace and water cooling]]
- [[P-wave velocity measurement (ultrasonic monitor)]]
- [[thermal conductivity measurement (HotDisk TPS 500)]]
- [[porosity measurement by water saturation method]]
- [[uniaxial compression test (MTS816)]]
- [[acoustic emission monitoring (PCI-2)]]
- [[ANSYS numerical simulation for temperature and thermal stress]]
- [[scanning electron microscope (SEM) for microstructure]]

## Connections To Other Work

- 与前人关于高温后快速冷却（水冷、液氮冷却）导致花岗岩力学性质劣化的研究（如Zhu et al. 2018; Wu et al. 2019a; Deng et al. 2020）一致，进一步证实冷却速率较自然冷却加剧损伤。
- 与Rong et al. (2018)、Jin (2019)、Zhang et al. (2021b)关于循环热处理（加热–急冷）下岩石性质存在阈值的结论相呼应，并补充了声发射及热应力数值分析的机理解释。
- 在导热系数劣化机制上，深化了Cheng et al. (2017)关于岩石热物理性质影响因素的认识，明确了接触热阻增大的贡献。
- 采用的5°C/min临界升温速率参考了Yin Q et al. (2019)、Ranjith et al. (2012)等人的工作，保证单一热冲击效应可剥离。

## Open Questions

- 超过20次循环后的长期劣化规律及热裂纹网络连通性演化尚不明确。
- 不同温度水平（如>450°C）及不同冷却介质（如液氮）对热冲击劣化机理的差异需进一步对比。
- 热冲击导致的微观结构变化与储层渗透率、水流换热效率的定量关系有待研究。
- 现场条件下地应力和水-岩化学作用对热裂纹开闭与力学行为的耦合效应尚需验证。
- 数值模型中未考虑岩石非均质性及矿物各向异性，更精细的多尺度模拟是未来方向。

## Source Coverage

所有13个非空索引片段均已处理。源覆盖度：按片段数100%（13/13），按字符数94.9%（59651/62842）。
