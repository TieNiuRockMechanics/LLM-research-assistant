---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-huang-mechanism-of-drilling-rate-improvement-using-high-pressure-liquid-nitrogen-jet"
title: "Mechanism of Drilling Rate Improvement Using High-Pressure Liquid Nitrogen Jet."
status: "draft"
source_pdf: "data/papers/2019 - Mechanism of drilling rate improvement using high-pressure liquid nitrogen jet.pdf"
collections:
citation: "Huang, Zhongwei, et al. \"Mechanism of Drilling Rate Improvement Using High-Pressure Liquid Nitrogen Jet.\" *Petroleum Exploration and Development*, vol. 46, no. 4, Aug. 2019, pp. 810-18, doi:10.1016/S1876-3804(19)60239-9."
indexed_texts: "9"
indexed_chars: "40492"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:26:09"
---

# Mechanism of Drilling Rate Improvement Using High-Pressure Liquid Nitrogen Jet.

## One-line Summary
通过液氮（LN₂）热冲击显著降低岩石单轴抗压强度和弹性模量，并联合高压射流冲击作用，实现高效率、低压阈值的破岩，从而提出了一种高压液氮射流辅助钻井新方法 [Huang 2019, pp. 1-1]。

## Research Question
能否利用高压液氮射流的热冲击与射流冲击耦合作用，突破深部高温硬岩钻井中岩石强度高、钻速低的瓶颈？其破岩机理与效果如何？[Huang 2019, pp. 1-1]

## Study Area / Data
研究基于室内实验，并非野外实际地层。实验对象为三种代表性的岩石：花岗岩、页岩和砂岩。制备了两种尺寸的试样：直径 25 mm、长 50 mm 的圆柱体（用于力学性质测试）与边长 13 cm 的立方体（用于射流破岩实验）。岩石初始温度范围覆盖 25 °C 到 480 °C。数据包括声波波速、应力-应变曲线、单轴抗压强度（UCS）、弹性模量（E）、破岩深度和表面温度-时间曲线等 [Huang 2019, pp. 1-2, 3-4, 4-6]。

## Methods
- **力学性质对比实验**：将三种岩石的圆柱试样分别经加热后采用空气自然冷却与液氮冷却，测量 P 波速度（Vp）变化，并进行单轴压缩试验，记录应力-应变曲线，计算 UCS 和弹性模量的劣化因子 \( D_I = 1 - I_{LN2} / I_{air} \) [Huang 2019, pp. 1-2, 2-3, 7-8]。
- **高压液氮射流破岩实验**：利用最大排量 4000 L/h、耐压 35 MPa 的低温流体泵和液氮罐等组成的射流系统，对预先加热至不同目标温度的立方体岩石进行射流冲击，射流压力固定为 25 MPa，观察宏观破岩形态、深度及体积破碎阈值 [Huang 2019, pp. 3-4, 4-6]。
- **微观结构观察**：对射流冲击后的岩石取样，使用扫描电子显微镜（SEM）观察微裂纹类型 [Huang 2019, pp. 6-6]。
- **传热与热应力分析**：测量岩石表面温度变化，结合热应力计算公式，分析液氮冷却过程中的沸腾模式转变（膜沸腾→过渡沸腾→核沸腾）及其对热应力的影响 [Huang 2019, pp. 6-7]。

## Key Findings
- **波速降低与热损伤**：液氮冷却引起 P 波速度降幅明显大于空气冷却，且降幅随岩石初始温度升高而增大。例如，25–260 °C 下花岗岩液氮冷却后 Vp 降低 4.1%–18.4%，比空气冷却高出 4.1%–7.7%。表明液氮热冲击造成了显著的岩石损伤 [Huang 2019, pp. 2-3]。
- **力学性质劣化**：液氮冷却后 UCS 和弹性模量均下降，温度越高劣化越明显。花岗岩和页岩对热冲击更敏感，而砂岩劣化程度弱。260 °C 时花岗岩 UCS 劣化因子达 29.00%，弹性模量劣化因子为 13.11% [Huang 2019, pp. 3-4, 7-8]。
- **射流破岩表现**：在 25 MPa 射流压力下，花岗岩大体积破碎的阈值温度在 150–260 °C 之间，破岩深度随温度升高而增加。页岩和砂岩在更高温度下才出现宏观裂纹，花岗岩的破岩效率最高 [Huang 2019, pp. 4-6]。
- **微裂纹模式**：SEM 观察发现，液氮冲击区形成大量晶间裂纹和晶内裂纹，主要源于不同矿物热膨胀系数差异引起的热应力 [Huang 2019, pp. 6-6]。
- **热应力演化**：岩石表面温度降至 Leidenfrost 点后，膜沸腾解体，换热急剧增强，热应力曲线出现陡增 [Huang 2019, pp. 6-7]。
- **敏感性差异**：花岗岩热应力显著高于砂岩和页岩，其力学性质劣化最突出，是决定破岩性能优越的关键因素 [Huang 2019, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 花岗岩 LN₂ 冷却后 Vp 降幅 4.1%–18.4%，比空气冷却高 4.1%–7.7% | [Huang 2019, pp. 2-3] | 初始温度 25–260 °C；圆柱试样 | 证实热冲击损伤 |
| 页岩 LN₂ 冷却后 Vp 降幅 −0.12%–0.81%，砂岩 3.2%–3.3% | [Huang 2019, pp. 2-3] | 同上 | 页岩和砂岩的 Vp 变化较小 |
| 花岗岩 UCS 劣化因子：25 °C 为 1.09%，150 °C 为 18.90%，260 °C 为 29.00% | [Huang 2019, pp. 7-8] | LN₂ 冷却后单轴压缩 | 随温度升高劣化加剧 |
| 页岩 UCS 劣化因子：25 °C 0.69%，150 °C 11.41%，260 °C 27.94% | [Huang 2019, pp. 7-8] | 同上 | 劣化幅度逊于花岗岩 |
| 花岗岩在 25 MPa 射流下，大体积破碎阈值温度 150–260 °C | [Huang 2019, pp. 4-6] | 边长 13 cm 立方体试样 | 破岩表现最好 |
| 砂岩在 480 °C 下才出现宏观网状裂纹 | [Huang 2019, pp. 4-6] | 射流压力 25 MPa | 砂岩最难破碎 |
| 热应力曲线在约 200 s 时剧增，对应 Leidenfrost 点转变 | [Huang 2019, pp. 6-7] | 岩石初始温度约 20 °C | 沸腾模式转变导致换热突变 |

## Limitations
未从索引片段中确认明确的研究局限性。可推断的潜在限制包括：实验采用小尺寸岩样，未考虑地应力和真实井底约束；射流压力固定为 25 MPa，未探索更宽参数范围；未涉及深层钻井中的循环温度、井壁稳定性及经济性评估。

## Assumptions / Conditions
- 圆柱试样基于相近的 P 波速度筛选，以降低初始损伤非均质性的影响 [Huang 2019, pp. 1-2]。
- 通过比较空气冷却与 LN₂ 冷却，消除了加热过程中水分丢失等因素的干扰，认为 Vp 的额外降低仅由热冲击引起 [Huang 2019, pp. 2-3]。
- 热应力计算假设岩石为线弹性材料，且表面热交换边界条件符合膜沸腾向核沸腾转变的经典淬火曲线 [Huang 2019, pp. 6-7]。
- 破岩实验假定液氮射流在冲击区域均匀覆盖，岩石初始温度分布均匀。

## Key Variables / Parameters
- P 波速度 \( V_p \) (m/s)、P 波速度变化量 \( \Delta V_p \)
- 单轴抗压强度 (UCS)、弹性模量 \( E \) (GPa)、劣化因子 \( D_I \) (%)
- 岩石初始温度 (°C)、表面温度 (°C)、温度降 \( \Delta T \) (K)
- 热应力 \( \sigma_T \) (MPa)、线性热膨胀系数 \( \alpha \) (K⁻¹)
- 射流压力 (固定 25 MPa)
- 破岩深度、体积破碎阈值温度、膜沸腾持续时间

## Reusable Claims
- **条件**：花岗岩，初始温度 ≥ 150 °C，液氮射流压力 25 MPa，无地应力。**主张**：液氮射流可实现大体积破碎，破岩深度随温度升高显著增加 [Huang 2019, pp. 4-6]。
- **条件**：任何硬岩，经受 LN₂ 冷却，无围压。**主张**：单轴抗压强度和弹性模量随初始温度升高而加剧劣化，花岗岩的劣化因子最高，砂岩最低 [Huang 2019, pp. 7-8]。
- **条件**：岩石经历快速温度变化 (>200 °C 温差)。**主张**：因矿物热膨胀系数失配，产生晶间与晶内微裂纹，导致力学性质弱化和破岩压力阈值降低 [Huang 2019, pp. 6-6]。
- **条件**：低温液体与大温差表面接触。**主张**：膜沸腾向核沸腾的转变发生在 Leidenfrost 点，伴随热流密度和热应力的骤增，可大幅提高破岩效率 [Huang 2019, pp. 6-7]。

## Candidate Concepts
- [[liquid nitrogen jet]]
- [[thermal shock]]
- [[rock mechanics]]
- [[uniaxial compressive strength]]
- [[Leidenfrost effect]]
- [[deep drilling]]
- [[hot dry rock (HDR) geothermal]]
- [[high-pressure jet assisted drilling]]

## Candidate Methods
- [[cryogenic fluid pumping]]
- [[SEM analysis]]
- [[acoustic wave velocity test]]
- [[uniaxial compression test]]
- [[thermal stress calculation]]
- [[rock-breaking experiment with jet]]
- [[heat transfer analysis]]

## Connections To Other Work
索引片段提及该方法结合了前人关于“射流是一种高效强化传热方式” [10–11] 以及“LN₂ 冷却可弱化硬岩力学性质” [12–13] 的认识 [Huang 2019, pp. 1-2]。传热分析中引用了沸腾模式转变的经典淬火实验 [18] [Huang 2019, pp. 6-7]。这些工作分别属于 [[enhanced heat transfer]]、[[cryogenic rock weakening]] 和 [[quenching heat transfer]] 领域，但具体文献未在片段中列出。本页可从主题上连接到 [[cryogenic drilling fluids]]、[[thermal spallation drilling]] 等候选概念。

## Open Questions
- 高压 LN₂ 射流在实际深部钻井循环中的保温技术、管柱耐久性和经济性如何？[Huang 2019, pp. 7-8] 仅提及双壁隔热钻杆的潜在方案，未给出技术细节。
- 有地应力、孔隙压力及多场耦合条件下，该方法的破岩阈值和效率如何变化？未从索引片段中确认。
- 长时间射流冲击对岩石热传导和裂纹扩展的累积效应是否会导致井壁失稳？未从索引片段中确认。

## Source Coverage
本页依据论文索引的 9 个片段进行整理，这些片段覆盖了摘要、引言、实验方法、主要结果（力学性质测试、射流破岩特征、SEM 分析、传热与热应力）以及结论与部分展望。**重要缺失**包括：详尽的传热模型数学描述、热应力计算公式的推导、实验数据的统计误差分析、现场施工流程的详细设计（如图 13 的具体说明）以及对经济性或局限性的系统讨论。因此，本页对核心机理论述已较充分，但技术实现细节和工程适用性尚存信息缺口。
