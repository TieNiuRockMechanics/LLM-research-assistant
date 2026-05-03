---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-ziegler-evaluation-of-the-diametrical-core-deformation-and-discing-analyses-for-in-situ-str"
title: "Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge"
status: "draft"
source_pdf: "data/papers/2021 - Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge.pdf"
collections:
  - "zotero new"
citation: "Ziegler, Martin, and Benoît Valley. “Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Geothermal Borehole, Switzerland.” *Rock Mechanics and Rock Engineering*, vol. 54, 2021, pp. 6511-32. doi:10.1007/s00603-021-02631-8. Accessed 2026."
indexed_texts: "18"
indexed_chars: "89770"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "88945"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99081"
coverage_status: "full-index"
source_signature: "ab0db5e327ef2efb0908abb4f2c4a5da069929b0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:09:26"
---

# Evaluation of the Diametrical Core Deformation and Discing Analyses for In-Situ Stress Estimation and Application to the 4.9 km Deep Rock Core from the Basel Ge

## One-line Summary
该研究评估了摄影测量岩心扫描在进行直径岩心变形分析（DCDA）中的适用性，并将DCDA结果与井壁崩落和应力诱发的岩心饼化裂缝数据进行了对比，同时研究了岩石弹性各向异性对从DCDA估算差应力（ΔS）的影响，使用来自瑞士巴塞尔地热井4.9 km深处的岩心。

## Research Question
- 摄影测量岩心扫描能否可靠地获取DCDA所需的高分辨率直径数据？ [Ziegler 2021, pp. 1-2]
- 从DCDA得到的最大水平主应力（SHmax）方向与井壁崩落和岩心饼化裂缝（CDF）推断的方向是否一致？ [Ziegler 2021, pp. 2]
- 岩石弹性各向异性（横向各向同性）如何影响基于DCDA的差应力估算？ [Ziegler 2021, pp. 2]

## Study Area / Data
- **地点**：瑞士巴塞尔市内的巴塞尔-1（BS-1）地热井，坐标（瑞士CH1903）611,810.054, 270,535.874。 [Ziegler 2021, pp. 2-3]
- **岩心深度区间**：钻探深度4909.0–4917.7 m（累积岩心长度9.09 m，直径101 mm，100%取心率）。 [Ziegler 2021, pp. 3,6]
- **岩石类型**：二长花岗岩至二长岩，含少量煌斑岩和细晶岩脉，未见天然裂隙。部分岩心含圆形的镁铁质捕虏体。 [Ziegler 2021, pp. 3-4,6]
- **力学参数**：杨氏模量E = 65 GPa，泊松比ν = 0.22，单轴抗压强度117.7 MPa，抗拉强度估计范围4–11 MPa。 [Ziegler 2021, pp. 4]
- **应力背景估计**（在岩心深度处）：
  - SHmax方向：平均N144°，岩心深度处由井壁崩落得到的方位为N142°。 [Ziegler 2021, pp. 5-6]
  - 垂向应力Sv：122 MPa（梯度24.9 MPa/km）。 [Ziegler 2021, pp. 5]
  - 最小水平主应力Shmin：76–79 MPa（基于套管鞋压力测试和崩落宽度变化推断）。 [Ziegler 2021, pp. 5-6]
  - SHmax大小：不确定，不同方法给出的范围在106–160 MPa之间。 [Ziegler 2021, pp. 6]
- **数据来源**：68块岩心碎片（部分为锯切割端面），用于摄影测量扫描（32块）、坐标测量机（CMM，4块）、超声速度测量（22块）和饼化裂缝分析（16块）。 [Ziegler 2021, pp. 6-7, Table 3]

## Methods
- **摄影测量岩心变形分析**：使用GOM ATOS 300 Core©扫描仪获取岩心表面的高密度点云（每毫米切片约4000–5000点），通过视觉对齐定义参考线，拟合椭圆得到各1 mm切片的最大/最小直径（dmax, dmin）和dmax方向，据此计算差直径Δd。采用滤波去除Δd > 500 μm的异常值。 [Ziegler 2021, pp. 7-9]
- **坐标测量机（CMM）验证**：用Mitutoyo Strato Apex 9106 CMM以约0.2 N的接触力、10°间隔测量4块岩心的径向形状，精度约1 μm，以评估摄影测量方法的可靠性。 [Ziegler 2021, pp. 7]
- **差应力计算**：基于线弹性各向同性假设，使用Funato et al. (2012)公式ΔS = (Δd/dmin) * E/(1+ν)，其中d0近似为dmin，E = 65 GPa，ν = 0.22。 [Ziegler 2021, pp. 10]
- **岩心饼化裂缝分析**：利用360°展开照片和摄影测量阴影模型，绘制鞍形饼化裂缝轨迹，由低点连线方向确定SHmax方向，高点方向确定Shmin方向。共绘制106条裂缝轨迹，按质量分为高、低两级。 [Ziegler 2021, pp. 10]
- **径向超声波速度测量**：在22块岩心径向以15°间隔测量P波速度（54 kHz传感器），计算每块岩心vpmax和vpmin的大小和方向，以表征径向各向异性。 [Ziegler 2021, pp. 10-11]
- **数值模拟**：利用三维有限元程序RS3模拟横向各向同性对岩心变形的影响。模型尺寸2×2×5 m，含212.7 mm钻孔和101 mm岩心，施加Sv=122 MPa，SHmax=115 MPa，Shmin=76 MPa。分两阶段模拟：先施加初始应力，然后一次性移除钻孔环空，允许岩心自由卸荷。通过拟合椭圆计算岩心直径差。 [Ziegler 2021, pp. 11]
- **参数敏感性分析**：对ΔS公式中的参数（E, ν, d0, Δd）进行不确定性传播分析。 [Ziegler 2021, pp. 11]

## Key Findings
- **摄影测量与CMM一致性**：两种方法得出的Δd差值在2–11 μm之间，dmax平均方位角差值2–9°，当Δd > 200 μm时方位角差值小于4°。摄影测量精度（10–20 μm）虽比CMM低约一个数量级，但仍足以分辨预期的岩心变形（50–150 μm）。 [Ziegler 2021, pp. 11-12, 18]
- **DCDA数据变异性**：30个摄影测量岩心块的Δd中位数为101 μm（第一四分位数79 μm，第三四分位数125 μm），1σ方向变异性中位数27°，个别岩块Δd值极大（如1-1, 1-3等，可能因严重饼化导致损伤）。 [Ziegler 2021, pp. 11, Table 4]
- **应力方向一致性**：对于能够拼接的岩心组，DCDA得出的SHmax方向与饼化裂缝低点轴方向具有一致性；总体而言，两种方法的SHmax方向角差平均为15.5°，且DCDA的不确定性范围大得多，与饼化裂缝的不确定性范围重叠。饼化裂缝给出的方向变异性（1σ）平均仅为4°，与同深度段井壁崩落数据相当。 [Ziegler 2021, pp. 15, 18-19]
- **差应力估算**：基于各向同性假设和Δd中值101 μm，得出ΔS中值为53 MPa（E=65 GPa, ν=0.22），但Δd的高变异性导致ΔS范围极宽。敏感性分析显示，参数不确定性可使ΔS从低值36.8 MPa到高值73.3 MPa，杨氏模量误差贡献最大。 [Ziegler 2021, pp. 11-13]
- **岩石各向异性影响显著**：P波速度径向测量显示vp max/vp min比值为1.13±0.04，表明存在明确的各向异性。数值模拟表明，各向同性面方位和各向异性指数λ对Δd的影响很大：当各向同性面近垂直于SHmax时，变形增强；近垂直于Shmin时，变形减弱。在合理参数范围内（λ 0.59–0.99，各向同性面倾角73–84°，走向与vp max一致，SHmax方向由饼化低点确定），模拟的Δd范围（30–150 μm）与实测值的分布基本一致，但个别受损伤岩块（如1-1, 1-3, 3-2）偏离较大。 [Ziegler 2021, pp. 15, 17-18]
- **饼化裂缝厚度指标**：观测到的平均饼厚/直径比约0.27，按Lim & Martin (2010)的准则对应最大主应力/抗拉强度比6–8，结合抗拉强度4–11 MPa，推算的Smax仅24–88 MPa，低于其他方法估计值，可能表明该经验关系在更大直径岩心和不同应力条件（中主应力、孔隙压力等）下不适用。 [Ziegler 2021, pp. 13, 19-20]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 摄影测量Δd与CMM Δd偏差2–11 μm | [Ziegler 2021, pp. 11-12, Fig. 7, Fig. 8] | 四块岩心（4-1,5-2,6-4,7-1），恒温±1°C | 摄影测量精度~10–20 μm，CMM精度~1 μm |
| DCDA方位角（dmax方向）与CMM偏差2–9° | [Ziegler 2021, pp. 11-12, Fig. 8] | 同上，当Δd > 200 μm时偏差<4° | 各向异性可能产生系统误差 |
| Δd中位数101 μm（n=30） | [Ziegler 2021, pp. 11, Table 4] | 排除箱线图识别的异常高Δd岩块 | 变异性大，部分岩块因饼化损伤Δd异常大 |
| 饼化裂缝低点方向1σ变异性~4° | [Ziegler 2021, pp. 13, Table 5] | 16块岩心，106条裂缝轨迹，仅鞍形裂缝 | 与同深度井壁崩落方向变异性一致 |
| DCDA与饼化裂缝的SHmax方向角差平均15.5°，不确定性范围重叠 | [Ziegler 2021, pp. 15, Fig. 11] | 逐块比较 | DCDA不确定度约±27°远大于饼化的±4° |
| 径向P波速度各向异性vpmax/vpmin=1.13±0.04 | [Ziegler 2021, pp. 15, Fig. 10] | 22块岩心，径向15°间隔测量 | 速度最大值方向与岩石组构走向偏角平均2±16° |
| 数值模拟中横向各向同性对Δd的放大/抑制作用可达数倍 | [Ziegler 2021, pp. 17 Fig. 12] | λ≥0.7时影响显著，各向同性面垂直于SHmax时Δd最大 | 基于Basel-1条件（Sv=122, SHmax=115, Shmin=76 MPa） |
| 考虑各向异性后模拟Δd范围30–150 μm，与多数实测Δd重叠 | [Ziegler 2021, pp. 18, Fig. 13] | 参数范围：λ 0.59–0.99，各向同性面倾角73–84°，走向方位026–068° | 异常高Δd的岩块可能与损伤有关，不满足弹性假设 |
| 饼厚/直径比推算Smax仅为24–88 MPa，远低于其他估计值 | [Ziegler 2021, pp. 13, 19] | 依据Lim & Martin (2010)准则，假定抗拉强度4–11 MPa | 可能因岩心直径差异、中主应力影响等使经验准则不适用 |

## Limitations
- 巴塞尔-1岩心未定向，导致只能在局部拼接块内比较相对方向，无法获得绝对地理方位。 [Ziegler 2021, pp. 6-7, 18]
- 摄影测量精度（10–20 μm）低于CMM（~1 μm）或光学微米计，但足以分辨平均变形量级。 [Ziegler 2021, pp. 18]
- 弹性模量和各向异性参数未在本研究中进行直接测量（仅限于非破坏性方法），导致ΔS估算不确定度大。 [Ziegler 2021, pp. 19]
- Δd测量结果变异性大（部分岩块标准差达数十微米），尤其在饼化严重或有钻井诱导损伤的岩块中，纯弹性假设可能不成立。 [Ziegler 2021, pp. 18, 19]
- 各向异性模拟仅限于横向各向同性，且未考虑泊松比各向异性，可能过于简化。 [Ziegler 2021, pp. 16-17]

## Assumptions / Conditions
- DCDA的基本假设：旋转钻井产生初始正圆形岩心截面；岩心卸荷后的径向变形为纯弹性，无塑性或非弹性恢复。 [Ziegler 2021, pp. 2, 10]
- 各向同性分析中假设材料为线弹性各向同性，使用单一杨氏模量65 GPa和泊松比0.22。 [Ziegler 2021, pp. 10]
- 数值模拟中采用横向各向同性简化：Saint-Venant近似计算Gxz，所有泊松比均取0.22，Ez = λEx。各向同性面倾角78°（根据矿物定向），方位基于vpmax与饼化低点的关系估算。 [Ziegler 2021, pp. 16-17]
- 饼化裂缝分析假定裂缝为张性（基于羽状痕和模型），鞍形低点连线方向对应SHmax。 [Ziegler 2021, pp. 2, 10]
- 计算ΔS时初始直径d0近似取dmin，产生的误差可忽略（Δd远小于d0）。 [Ziegler 2021, pp. 10]

## Key Variables / Parameters
- Δd：岩心最大与最小直径差（μm），中位值101 μm。 [Ziegler 2021, pp. 11, Table 4]
- dmax方位角：相对于岩心参考线的方向（°），变异性1σ中位数27°。 [Ziegler 2021, pp. Table 4]
- E：杨氏模量，基准值65 GPa。 [Ziegler 2021, pp. 10]
- ν：泊松比，0.22。 [Ziegler 2021, pp. 10]
- vpmax/vpmin：P波速度各向异性比，平均1.13。 [Ziegler 2021, pp. 15]
- λ：各向异性指数（Ez/Ex），取值范围0.59–0.99，平均0.77。 [Ziegler 2021, pp. 17]
- 各向同性面产状：倾角73–84°，走向相对SHmax的方位角范围026–068°。 [Ziegler 2021, pp. 17]
- 饼化裂缝低点方向1σ变异性：平均3.8°。 [Ziegler 2021, pp. 13]
- ΔS（差应力）：各向同性解中位53 MPa，考虑参数不确定性范围36.8–73.3 MPa。 [Ziegler 2021, pp. 11-13]

## Reusable Claims
- 摄影测量扫描可以提供足够精度的岩心直径数据用于DCDA，其与CMM的Δd差异在2–11 μm，方位角差2–9°。 [Ziegler 2021, pp. 11-12, 18] *条件：岩心表面预先做好防反射处理，环境温度恒定，且岩心无明显宏观损伤。*
- DCDA得出的SHmax方向与鞍形岩心饼化裂缝低点轴方向在不确定性范围内一致，但DCDA的方向变异性（~27°）比饼化方向变异性（~4°）大一个数量级。 [Ziegler 2021, pp. 15, 18-19] *条件：适用于深度4.9 km的致密花岗岩类岩心。*
- 忽略岩石弹性各向异性会显著高估或低估差应力ΔS，其影响可达数十兆帕。 [Ziegler 2021, pp. 17-18] *条件：各向异性指数λ < 0.8且各向同性面倾角较陡时影响最为突出。*
- 当岩心存在密集饼化或钻井诱导损伤时，Δd测量值可能异常偏高（可达数百微米），偏离弹性卸荷假设，因此在DCDA中应剔除或谨慎使用。 [Ziegler 2021, pp. 11, 18, Table 4]
- 在巴塞尔4.9 km深处，考虑横向各向同性后的模拟Δd范围（30–150 μm）与多数实测值吻合，支持该深度应力状态处于走滑与正断层的过渡边界。 [Ziegler 2021, pp. 18, 20]
- 基于饼厚/直径比的经验应力估计方法（Lim & Martin 2010）在岩心直径101 mm的条件下给出的Smax值（24–88 MPa）低于其他独立估计，表明该经验关系在此特定条件下可能不适用。 [Ziegler 2021, pp. 19-20]

## Candidate Concepts
- [[diametrical core deformation analysis (DCDA)]]
- [[core discing fracture (CDF)]]
- [[photogrammetric core scanning]]
- [[transverse isotropy in core deformation]]
- [[borehole breakout]]
- [[anisotropy index (λ)]]
- [[saddle-shaped disc fractures]]
- [[differential stress (ΔS)]]
- [[elastic unloading in drill cores]]
- [[in-situ stress estimation from cores]]

## Candidate Methods
- [[photogrammetric 3D core scanning with ellipse fitting]]
- [[coordinate measuring machine (CMM) for core diameter]]
- [[least-squares ellipse fitting (Halíř & Flusser 1998)]]
- [[ultrasonic radial velocity anisotropy measurement]]
- [[3D finite-element simulation of core relaxation (RS3)]]
- [[RANSAC cylinder fitting for core alignment]]
- [[core disc thickness-to-diameter ratio stress estimation]]

## Connections To Other Work
- **DCDA方法**：基于Funato et al. (2012)和Funato & Ito (2017)提出的各向同性弹性解，本研究首次用摄影测量替代光学微米计进行连续测量。 [Ziegler 2021, pp. 2, 18]
- **巴塞尔应力状态**：与Valley & Evans (2009, 2019)的井壁崩落方向及应力大小估计进行对比，证实SHmax方向一致性；同时与Terakawa et al. (2012)的震源机制解以及Kraft & Deichmann (2014)的震源机制混合解进行了比较。 [Ziegler 2021, pp. 5-6, 19]
- **岩心饼化机制**：参考了Lim & Martin (2010)的饼化程度-应力比经验关系，以及Corthésy & Leite (2008)的弹塑性模型和Wu et al. (2018)的离散元模拟，但本研究表明该经验关系在本例中可能不成立。 [Ziegler 2021, pp. 2, 19-20]
- **岩石弹性各向异性影响**：与一般认识一致，即忽略各向异性可能导致应力估计错误；本研究通过数值模拟定量展示了横向各向同性对DCDA的具体影响。 [Ziegler 2021, pp. 15-18]
- **非弹性效应**：与Lim et al. (2012)的微裂纹观察一致，即巴塞尔岩心中微裂纹主要在垂直于轴线的平面内发育，对径向应变影响较小，支持DCDA的弹性假设在低损伤段有效。 [Ziegler 2021, pp. 19]

## Open Questions
- 巴塞尔岩心中观察到的二次诱导裂缝（不完全环绕痕迹，常位于饼化裂缝低点之间）的成因是什么？它们在应力估计中是否可被利用？ [Ziegler 2021, pp. 13, 19]
- 为什么基于饼厚/直径比的经验方法（Lim & Martin 2010）给出的Smax估算值远低于其他方法？是因为岩心直径差异、中主应力影响、温度效应，还是抗拉强度标定问题？ [Ziegler 2021, pp. 19-20]
- 本研究提出的考虑横向各向同性的DCDA校正方法，能否通过实验室双轴加载试验获得更多岩心材料的各向异性参数后得到进一步验证？ [Ziegler 2021, pp. 19]
- 在更广泛的岩性和应力条件下，摄影测量DCDA方法能否实现自动化处理，从而提供连续的随深度差应力剖面？ [Ziegler 2021, pp. 19]
- 岩心卸荷过程中是否存在时间依赖的径向应变（如蠕变）？长期存放（>10年）后的岩心是否仍可视为弹性恢复完毕？ [Ziegler 2021, pp. 18-19]

## Source Coverage
所有18个非空索引片段（覆盖从标题页到参考文献的全部正文与引用内容）均已处理并纳入本页。源块编译字符数为88,945，原片段总字符数为89,770，覆盖率（按字符数）为99.08%，按块数计为100%。未使用的仅包括出版社编号行与个别极短的致谢参考文献无关行。源签名：ab0db5e327ef2efb0908abb4f2c4a5da069929b0。
