---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-miyazaki-application-of-laboratory-based-rate-of-penetration-model-for-polycrystalline-diam"
title: "Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling."
status: "draft"
source_pdf: "data/papers/2023 - Application of laboratory-based rate of penetration model for polycrystalline diamond compact bit to geothermal well drilling.pdf"
collections:
  - "part3-2"
citation: "Miyazaki, Kuniyuki, et al. \"Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling.\" *Geomechanics and Geophysics for Geo-Energy and Geo-Resources*, vol. 9, no. 103, 2023, https://doi.org/10.1007/s40948-023-00644-x."
indexed_texts: "7"
indexed_chars: "32002"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31526"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.985126"
coverage_status: "full-index"
source_signature: "cfe6d25b6198935f075357a4b2e02941d2f1fc78"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:16:08"
---

# Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling.

## One-line Summary
本研究基于室内试验建立的聚晶金刚石复合片（PDC）钻头机械钻速（ROP）模型被评价并验证可适用于地热井钻进现场数据，尤其是当岩屑有效携带时，钻头性能参数p随钻进长度呈指数衰减的特性与模型一致。

## Research Question
Miyazaki等（2022）提出的考虑钻头磨损的实验室PDC钻头ROP模型能否应用于地热区域实际钻井数据？特别是用于表征钻头性能的参数p（结合钻进参数与岩石强度）在现场条件下的适用性如何？[Miyazaki 2023, pp. 1-2]

## Study Area / Data
本研究使用了四个地热区构造钻孔的现场钻井试验数据，分别编号为Field test No.1至No.4。每套试验对应的地质层位及钻进参数记录如下：[Miyazaki 2023, pp. 4-5]

- **Field test No.1**：晚中新世英安质凝灰角砾岩与熔结凝灰岩，钻头Bit A，钻进井段1756 – 1917 m（测深），钻进31.0小时，IADC钝化等级：内排2，外排3。
- **Field test No.2**：凝灰质砂岩、火山砾凝灰岩及火山砾岩，钻头Bit B，井段797 – 1106 m，钻进93.4小时，IADC钝化等级：内排0，外排1。
- **Field test No.3**：新近系安山岩熔岩、角闪英安质火山碎屑岩（含玄武岩侵入体），钻头Bit C分两趟使用，第一趟井段1210 – 1249 m，第二趟1414 – 1484 m，总钻进56.0小时，IADC第一趟内排0/外排1，第二趟内排1/外排3。
- **Field test No.4**：富含石英的安山岩、英安岩和玄武岩，钻头Bit D，井段1372 – 1392 m，钻进9.0小时，IADC内排1，外排3。

现场数据包括钻压（W）、转速（N）、机械钻速（u）随井深（MD）的变化曲线，以及钻头使用前后的室内钻进性能测试（pretest/posttest）。岩石单轴抗压强度（Sc）由回收的岩心实验室测得，其中Field test No.1使用紧邻钻头钻进段上部的1753–1757 m岩心；其余试验使用邻近区域岩心估算。[Miyazaki 2023, pp. 5-8]

## Methods
**核心模型**：Miyazaki等（2022）通过全尺寸PDC钻头（直径216 mm，58个切削齿）在五种岩石中累计98 m的室内钻进试验建立了以下力学钻速模型：

\[
u = p_0 \cdot N \cdot \left(\frac{W}{S_c}\right)^2 \cdot \exp(-\gamma \cdot V_{wd})   \tag{1}
\]

其中，u为机械钻速，N为转速，W为钻压，Sc为岩石单轴抗压强度，V_{wd}为钻头鼻部和肩部16个切削齿上聚晶金刚石层的平均磨损体积，p_0和γ分别为磨损起始时的钻头性能参数及磨损对钻速的影响系数。[Miyazaki 2023, pp. 2-3]

定义钻头性能指标p：

\[
p = \frac{u/N}{(W/S_c)^2} = p_0 \cdot \exp(-\gamma \cdot V_{wd}) \tag{2}
\]

当钻进均质岩层且磨损体积与钻进长度L_d成正比时，式(2)可改写为：

\[
p = p_0 \cdot \exp(-\gamma' \cdot L_d) \tag{3}
\]

γ'代表钻头在该岩层中的耐久性参数。[Miyazaki 2023, pp. 3-4]

**现场应用方法**：对每个现场试验，利用实测N、W、u以及岩心Sc，按式(2)计算钻头在现场的p值，并以p随钻进长度Ld（或井深MD）的变化趋势与实验室预试（p_{pre}）及后试（p_{post}）结果对比。实验室预/后试采用相同或同规格钻头在标准岩样上测定u/N – W关系，验证Bingham’s b值接近2，满足模型对(N, W/Sc)平方关系的依赖。[Miyazaki 2023, pp. 4-6]

**钻头磨损评估**：现场测试仅收集到IADC钝化等级作为磨损半定量指标，缺少V_{wd}直接测量值，因此依赖p值的变化间接反映磨损程度。[Miyazaki 2023, pp. 8-9]

## Key Findings
1. **Field test No.1和No.4**：p随钻进长度呈指数下降（半对数坐标下近似线性），起始和末尾的p值分别与实验室p_{pre}和p_{post}吻合。这验证了式(3)描述的磨损导致ROP衰减规律在现场硬岩钻进中的适用性。[Miyazaki 2023, pp. 6-9, Fig.9, Fig.13]

2. **Field test No.2**：由于岩性软塑，出现钻头泥包（bit balling），岩屑粘附于钻体，p显著低于实验室性能值，模型无法直接解释。该异常表明模型应用前提之一为岩屑高效输送。[Miyazaki 2023, pp. 7-8, Fig.10, Fig.11]

3. **Field test No.3**：在侵入玄武岩段p的下降斜率更陡，暗示玄武岩的磨蚀性更强；在初次使用结束时出现p瞬时骤降，推测为钻柱推力传递不足所致（如键槽、岩屑床）。忽略异常点后，p整体仍呈随L_d衰减趋势，最终接近p_{post}。[Miyazaki 2023, pp. 8-9, Fig.12]

4. **整体结论**：实验室建立的ROP模型能够合理解释在岩屑正常携带条件下PDC钻头钻进硬地层的现场数据，表征钻头性能的参数p可被视为钻头磨损的实时监测指标。[Miyazaki 2023, pp. 9-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| u/N ≈ (W/S_c)^2在PDC钻头磨损前、后均近似成立，Bingham’s b≈2 | Miyazaki 2023, pp. 4-6; Table 1 | 室内预试/后试，直径216mm PDC钻头，钻进多种硬岩 | 模型本质假设得到实验和现场数据支持 |
| Field test No.1中log(p)随L_d线性下降，p_{pre}↔p_{post}衔接 | Miyazaki 2023, pp. 6-7; Fig.9 | 均质英安质凝灰角砾岩，钻压基本恒定，岩屑清除正常 | 现场p与室内p可比较，无需校正 |
| Field test No.2中p远低于p_{pre}和p_{post}，泥包导致钻头性能未充分发挥 | Miyazaki 2023, pp. 7-8; Fig.10, Fig.11 | 软岩、钻头泥包；增大泥浆流量后p短暂恢复 | 模型不适用于岩屑输送严重恶化的情况 |
| Field test No.3中p在硬玄武岩段衰减更快，存在推力传递失效造成的瞬时下跌 | Miyazaki 2023, pp. 8-9; Fig.12 | 两次使用的Bit C，岩性非均质，局部含玄武岩侵入体 | γ'受岩石磨蚀性影响，且p对井下故障敏感 |
| Field test No.4中p指数衰减，首尾值与室内测试一致 | Miyazaki 2023, pp. 9; Fig.13 | 石英安山岩、英安岩、玄武岩，钻进20 m | 短井段数据也能体现模型趋势 |

## Limitations
- 模型目前仅适用于u/N与(W/S_c)平方近似成正比的PDC钻头；若应用前须通过实验室测试确认该指数关系。[Miyazaki 2023, pp. 9]
- 仅在相对较硬的岩层中进行了验证，对磨蚀性沉积岩等其他类型地层的适用性尚需检验。[Miyazaki 2023, pp. 9-10]
- 岩屑携带不良（如钻头泥包）会显著降低p值，使模型失效；实际应用需结合水力学设计。[Miyazaki 2023, pp. 7-8]
- 现场仅获得IADC钝化等级，缺乏精确的切削齿磨损体积数据，限制了模型的精细标定。[Miyazaki 2023, pp. 8-9]
- 参数γ'（反映钻头耐久性和岩石磨蚀性）在钻进前难以准确估计，缺少定量预测方法。[Miyazaki 2023, pp. 10]

## Assumptions / Conditions
- 钻进过程中岩石类型均匀，Sc为常数，使V_{wd}与L_d成正比，从而p可简化为式(3)的指数衰减形式。[Miyazaki 2023, pp. 3-4]
- 循环系统能够有效清除岩屑，避免钻头重复破碎和泥包，钻头处于“完全清岩”状态（基于Maurer的完美清岩假设）。[Miyazaki 2023, pp. 2-3]
- 钻头切削齿的磨损体积从可观测磨损点开始与钻进长度呈线性关系，且微观磨损已导致p从p_i突降至p_0。[Miyazaki 2023, pp. 3]
- 钻压和转速在评估区间内保持较稳定，或N和W的变化已按模型关系归一化处理。[Miyazaki 2023, pp. 5-6]
- p值可通过钻井仪表实时计算，从而间接监测钻头磨损状态。[Miyazaki 2023, pp. 9]

## Key Variables / Parameters
- **u** – 机械钻速（ROP）
- **N** – 钻头转速
- **W** – 钻压
- **S_c** – 岩石单轴抗压强度 (UCS)
- **V_{wd}** – PDC切削齿聚晶金刚石层平均磨损体积
- **p_0** – 磨损起始点对应的钻头性能基准值
- **γ** – 磨损体积影响系数（控制p随V_{wd}下降的速率）
- **γ'** – 钻头在特定岩层中的耐久性衰减系数（与岩石磨蚀性有关）
- **p_{pre}, p_{post}** – 实验室测试得到的钻头使用前、后性能参数
- **b** – Bingham幂指数（p值计算隐含b=2的假设，即u/N∝(W/S_c)^2）
- **L_d** – 累计钻进长度
- **IADC Dull Grade** – 钻头钝化等级（现场磨损的半定量指标）

## Reusable Claims
- **Claim 1**：在硬地热岩层中正常钻进时，PDC钻头的性能参数p（定义见式(2)）随钻进长度呈指数衰减，即log(p)≈常数-γ'·L_d，可用于估计钻头磨损程度和剩余寿命。[Miyazaki 2023, pp. 6-9]
- **Claim 2**：实验室预试和后试获得的p_{pre}和p_{post}值与现场计算的p值在首尾端能较好吻合，说明即使没有现场V_{wd}测量，p值也可作为对比实验室与现场钻头性能的统一尺度。[Miyazaki 2023, pp. 7, 9]
- **Claim 3**：当出现钻头泥包导致岩屑清除效率大幅下降时，p值远低于模型预测值，模型适用条件被破坏；此时增大泥浆流量可暂时恢复p值，表明井下清洗状态直接关联模型的可解释性。[Miyazaki 2023, pp. 7-8]
- **Claim 4**：在非均质地层中，p对岩性变化敏感，如在硬玄武岩段γ'增大；此外，因钻柱推力传递问题（如键槽、岩屑床）引起的瞬时ROP和p骤降可能与磨损无关，数据分析时需结合工况甄别。[Miyazaki 2023, pp. 8-9]
- **Claim 5**：该ROP模型形式极其简单，仅需N, W, Sc三个主参数并结合经验系数p0, γ'即可工程应用，相较于Hareland模型和Motahhari模型更易在现场标定。[Miyazaki 2023, pp. 3-4]

## Candidate Concepts
- [[PDC drill bit]]
- [[Rate of penetration (ROP) model]]
- [[Bit wear]]
- [[Rock abrasivity]]
- [[Polycrystalline diamond compact (PDC)]]
- [[IADC dull grading]]
- [[Bingham’s drilling exponent]]
- [[Bit balling]]
- [[Schimazek’s F-abrasivity]]
- [[Perfect-cleaning theory (Maurer)]]
- [[Drill string friction]]
- [[Cuttings transport]]
- [[Geothermal well drilling]]

## Candidate Methods
- [[Laboratory full-scale PDC bit drilling test under controlled conditions]]
- [[Field drilling test for geothermal structural wells]]
- [[p-parameter real-time wear monitoring]]
- [[Exponential decay model for ROP degradation due to bit wear]]
- [[Pre-test and post-test laboratory drilling performance assessment]]
- [[Least-squares power approximation for u/N–W relationship]]
- [[Torque measurement for qualitative bit wear detection]]

## Connections To Other Work
- 该模型基于Maurer (1962) 的完美清岩理论，保留u/N与(W/S_c)^2的正比关系，并引入指数磨损项。[Miyazaki 2023, pp. 2-3]
- 与其他含磨损的PDC钻头ROP模型（Hareland & Rampersad 1994; Motahhari et al. 2010; Soares et al. 2016; Mazen et al. 2021）相比，本模型形式最简洁，且是全尺寸钻头室内试验结果，区别显著。[Miyazaki 2023, pp. 3-4]
- Karasawa et al. (2016) 提出了通过扭矩定性判断钻头磨损的方法，Mazen et al. (2021) 引入了磨损指数W_i。本模型则通过p值的连续变化提供一种无需直接测量扭矩的磨损监测手段。[Miyazaki 2023, pp. 4]
- 在试验中，V_{wd}与Schimazek’s F-磨蚀因子、Plinninger磨蚀指数等岩石磨蚀性指标相关性好，暗示γ'可间接关联这些工程常用指标。[Miyazaki 2023, pp. 3]

## Open Questions
- 该ROP模型是否适用于其他类型的PDC钻头（不同尺寸、切削齿布局、后倾角）以及磨蚀性沉积岩，尚未验证。[Miyazaki 2023, pp. 9-10]
- 钻头性能衰减参数γ'如何在钻前根据岩石磨蚀性和钻头设计进行定性或定量预测，目前仍是难点。[Miyazaki 2023, pp. 10]
- 当钻头泥包或推力传递失效时，模型失效的临界条件和补偿方法需要进一步界定。[Miyazaki 2023, pp. 7-8]
- 如何利用比IADC钝化等级更精细的磨损测量数据，提升p值的绝对精度和诊断能力。[Miyazaki 2023, pp. 8-9]
- 该指数衰减规律是否可扩展至其他类型钻头（如牙轮钻头）尚不清楚。[Miyazaki 2023, pp. 8]

## Source Coverage
所有非空索引碎片已全部处理和整合。共处理索引文本块7个，源字符总数32,002，编译后字符数31,526；区块覆盖率100%，字符覆盖率98.51%（基于一次编译策略）。[Coverage audit: indexed_texts=7, compiled_source_blocks=7, coverage_ratio_by_blocks=1.0, coverage_ratio_by_chars=0.985126]
