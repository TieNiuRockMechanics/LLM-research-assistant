---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-kim-stress-estimation-through-deep-rock-core-diametrical-deformation-and-joint-roughness-as"
title: "Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging."
status: "draft"
source_pdf: "data/papers/2020 - Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.pdf"
collections:
  - "zotero new"
citation: "Kim, Hanna, et al. \"Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.\" *Sensors*, vol. 20, no. 23, 2020, article 6802. doi:10.3390/s20236802."
indexed_texts: "11"
indexed_chars: "50552"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "50549"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.999941"
coverage_status: "full-index"
source_signature: "86074ccadbd352edf9941d7f7daa27d9d62b6212"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:40:08"
---

# Stress Estimation through Deep Rock Core Diametrical Deformation and Joint Roughness Assessment Using X-ray CT Imaging.

## One-line Summary
利用X射线CT成像对4.2 km深处花岗闪长岩岩心的直径变形和闭合节理粗糙度各向异性进行分析，通过直径岩心变形分析（DCDA）方法估算平均水平应力差约13.3 MPa，并发现最大水平主应力方向与最小节理粗糙度系数方向之间存在对齐关系，暗示节理粗糙度可能携带古应力方向信息。

## Research Question
能否通过深部岩心的直径弹性恢复变形，估算原位水平应力差？同时，岩心节理粗糙度各向异性的优势方向是否与最大水平主应力方向存在相关性，从而为应力方向追踪提供新指标？

## Study Area / Data
研究使用韩国浦项增强型地热系统（EGS）试验场PX-2井获取的岩心样品。岩心取自4219 m深处，直径100 mm，总取芯长度3.6 m，分11段（S‑I至S‑XI）。本研究选用S‑IX段的一段岩心（S‑IX‑3），其中包含一个闭合节理（CJ‑2），节理面倾角为80.8°。岩石为花岗闪长岩，矿物组成为钠长石43.1%、石英28.6%、微斜长石13.7%、白云母10.1%；弹性模量33.5 GPa，泊松比0.21，单轴抗压强度106.7 MPa，抗拉强度9.2 MPa ￼[Kim 2020, pp. 2-3]￼[Kim 2020, pp. 3-4]￼。该场地已有应力模型：勘探井EXP‑1报告应力比SHmax/Sv/Shmin=1.3/1.0/0.8，SHmax方向N130°E–N136°E ￼[Kim 2020, pp. 2-3]￼[Kim 2020, pp. 3-4]￼；韩国政府委员会评估的深部应力模型显示，在4.2 km深度逆断层应力状态下SHmax=243 MPa、Shmin=120 MPa、Sv=106 MPa，或走滑状态下SHmax=203 MPa、Shmin=93 MPa、Sv=106 MPa，SHmax方位角分别为77°和74° ￼[Kim 2020, pp. 4-4]￼。

## Methods
1. **直径岩心变形分析（DCDA）**  
   - 原理：当岩心从原位取出后，垂直于钻进方向的水平应力解除导致岩心发生各向异性弹性膨胀，最大膨胀方向与最大水平主应力方向一致，最小膨胀方向与最小水平主应力方向一致 ￼[Kim 2020, pp. 4-6]￼。  
   - 通过测量膨胀后岩心的最大直径dmax和最小直径dmin，结合弹性参数，用公式估算应力差：  
     S_max − S_min = (E/(1+ν)) × (d_max − d_min)/d_min ￼[Kim 2020, pp. 4-6]￼。  
   - 实际操作中，利用工业X射线CT扫描岩心S‑IX‑3，获取与钻进方向垂直的横截面图像。用ImageJ软件对CT切片进行二值化，提取岩心轮廓，拟合最佳椭圆，得到长、短轴长度及其方向 ￼[Kim 2020, pp. 6-7]￼。

2. **节理粗糙度各向异性评估**  
   - 以每10°间隔、每间隔内多条平行剖面，测量闭合节理CJ‑2的节理粗糙度系数（JRC）。各方向JRC取平均值后，拟合椭圆确定最大粗糙度（JRC_max）和最小粗糙度（JRC_min）方向 ￼[Kim 2020, pp. 7-8]￼。  
   - 将JRC_max、JRC_min方向从节理面（倾角80.8°）投影到水平面，以便与水平应力方向对比 ￼[Kim 2020, pp. 7-8]￼。

3. **应力方向与粗糙度方向对比**  
   - 将DCDA得到的dmax取向（代表SHmax方向）与水平投影后的JRC方向进行比较，探讨两者对齐关系 ￼[Kim 2020, pp. 7-8]￼。

## Key Findings
1. 岩心S‑IX‑3的CT测量显示，dmax在103.059~103.066 mm之间，dmin在103.022~103.027 mm之间。采用E=33.5 GPa、ν=0.21，算出的应力差范围为8.6~17.2 MPa，以平均值dmax=103.062 mm、dmin=103.0125 mm计算，得平均应力差**13.3 MPa** ￼[Kim 2020, pp. 6-7]￼。  
2. 该值与附近EXP‑1井水力压裂结果（SHmax=22.4 MPa，应力比1.7，得应力差9.22 MPa）处于同一量级，但略高；远低于韩国政府委员会模型给出的123 MPa或110 MPa ￼[Kim 2020, pp. 6-7]￼。  
3. CJ‑2节理的粗糙度各向异性：在节理面上，JRC_max方向为154.6°，JRC_min方向为64.6°（逆时针自水平参照线计），两者垂直 ￼[Kim 2020, pp. 7-8]￼。投影到水平面后，**JRC_min方向落入dmax方向范围（120.7°~136.2°）**，即最小粗糙度方向与最大水平主应力方向对齐 ￼[Kim 2020, pp. 7-8]￼。  
4. 这一对齐暗示：节理形成时，剪切方向受当时最大应力的控制，导致粗糙度最小方向平行于最大主应力方向；更高应力差可能形成更光滑的节理（低JRC），且应力方向可能通过节理粗糙度各向异性被记录 ￼[Kim 2020, pp. 7-8]￼。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 平均应力差13.3 MPa（范围8.6–17.2 MPa） | ￼[Kim 2020, pp. 6-7]￼ | 弹性模量33.5 GPa，泊松比0.21；岩心直径~100 mm，深度4.2 km；基于CT图像椭圆拟合 | DCDA方法计算，假设弹性变形 |
| EXP‑1井水力压裂应力差9.22 MPa | ￼[Kim 2020, pp. 6-7]￼ | 邻近勘探井，花岗岩地层 | 用于对比验证 |
| JRC_max方向154.6°，JRC_min方向64.6°（节理面） | ￼[Kim 2020, pp. 7-8]￼ | CJ‑2闭合节理，倾角80.8°；每10°剖面JRC拟合椭圆 | 相关系数0.98 |
| 水平投影后JRC_min与dmax方向对齐 | ￼[Kim 2020, pp. 7-8]￼ | dmax方向范围120.7°–136.2°；节理面投影考虑80.8°倾角 | 可能指示古应力方向 |
| DCDA方法实验室验证误差±0.87 MPa | ￼[Kim 2020, pp. 8-9]￼ | Funato & Ito (2017) 的砂浆及花岗岩试验 | 现场应用时真实误差未知 |

## Limitations
- DCDA方法要求岩心取出方向严格垂直于所研究的应力方向，钻进方向偏差会影响应力差估算精度 ￼[Kim 2020, pp. 8-9]￼。
- 仅使用垂直井的岩心，只能获得水平应力差，无法直接得到两个水平主应力的绝对值；需要至少三个不同方向的岩心才能求解完整应力张量 ￼[Kim 2020, pp. 8-9]￼。
- 本研究只分析了单块含闭合节理的岩心（S‑IX‑3），结果属于**初步结论**，样本量不足，统计代表性有限 ￼[Kim 2020, pp. 8-9]￼。
- 应力估算假设岩心服从线弹性各向同性行为，但花岗质岩石可能具有物理各向异性，该特性未被详细研究 ￼[Kim 2020, pp. 2-3]￼。
- 无法直接评估估算误差，因为真实原位应力未知；应力差结果与其他方法（如政府委员会模型）存在数量级差异，需更多交叉验证 ￼[Kim 2020, pp. 6-7]￼。

## Assumptions / Conditions
- 应力解除后岩心发生纯弹性恢复，无显著非弹性（如蠕变、微裂纹扩展）影响 ￼[Kim 2020, pp. 4-6]￼。
- 岩心材料为均质各向同性，弹性常数E、ν在应力解除前后不变 ￼[Kim 2020, pp. 4-6]￼。
- 岩心直径变化完全由水平应力差引起，忽略温度、湿度、孔隙压力变化等环境因素 ￼[Kim 2020, pp. 1-2]￼。
- 节理形成时，最大水平应力方向与剪切方向一致，且粗糙度各向异性记录了该方向 ￼[Kim 2020, pp. 7-8]￼。

## Key Variables / Parameters
- **dmax、dmin**：应力解除后岩心的最大和最小直径（mm） ￼[Kim 2020, pp. 4-6]￼。
- **E**（Young’s modulus）：33.5 GPa ￼[Kim 2020, pp. 2-3]￼。
- **ν**（Poisson’s ratio）：0.21 ￼[Kim 2020, pp. 2-3]￼。
- **ΔS**（水平应力差）：S_max − S_min，通过DCDA公式计算 ￼[Kim 2020, pp. 4-6]￼。
- **JRC_max、JRC_min方向**：节理粗糙度各向异性椭球的长轴和短轴方向（°） ￼[Kim 2020, pp. 7-8]￼。
- **dmax方向**：代表SHmax方向，CT测量值120.7°–136.2° ￼[Kim 2020, pp. 7-8]￼。

## Reusable Claims
1. 在弹性假设下，基于CT图像提取的dmax和dmin，结合岩石弹性常数，可估算水平应力差，适用于4.2 km深处的花岗闪长岩（σ_E=33.5 GPa，ν=0.21）￼[Kim 2020, pp. 4-6]￼[Kim 2020, pp. 6-7]￼。
2. DCDA方法所得应力差与邻近钻孔水力压裂结果（9.22 MPa）处于同一区间（8.6–17.2 MPa），表明该方法在特定地质条件下具有一定参考价值 ￼[Kim 2020, pp. 6-7]￼。
3. 闭合节理粗糙度各向异性的最小JRC方向可能与最大水平主应力方向对齐，前提是节理形成于该应力场下、且后期改造微弱 ￼[Kim 2020, pp. 7-8]￼。
4. 利用X射线CT与ImageJ椭圆拟合可高精度获取岩心直径变化，测量精度达到微米级，为DCDA实施提供了非接触式途径 ￼[Kim 2020, pp. 6-7]￼。
5. DCDA方法相比传统水压致裂等，经济成本低，尤其适合深部地热开发中的应力评估 ￼[Kim 2020, pp. 8-9]￼。

## Candidate Concepts
- [[diametrical core deformation analysis (DCDA)]]
- [[stress relief expansion anisotropy]]
- [[X-ray CT core metrology]]
- [[joint roughness anisotropy]]
- [[JRC (joint roughness coefficient) anisotropy ellipse]]
- [[maximum horizontal stress orientation from core expansion]]
- [[paleostress from joint roughness]]
- [[Pohang EGS stress model]]
- [[elastic stress recovery in granodiorite]]
- [[non‑contact core deformation measurement]]

## Candidate Methods
- [[DCDA using CT slices and ImageJ ellipse fitting]]
- [[JRC anisotropy estimation through multi‑angle profiles and ellipse fitting]]
- [[horizontal projection of joint morphology for stress comparison]]
- [[CT‑based diametrical deformation measurement at multiple heights]]

## Connections To Other Work
- Funato & Ito (2017) 首次提出DCDA方法并给出验证，其公式和弹性假设被本文直接采用 ￼[Kim 2020, pp. 4-6]￼。
- Kim et al. (2017) 在EXP‑1井的水力压裂与数值模拟提供了参照应力值，本文将其与DCDA结果对比 ￼[Kim 2020, pp. 6-7]￼。
- Diaz et al. (2017) 对同一批浦项岩心的节理粗糙度进行了系统测量，发现JRCmax方向在152.9°~166.8°间一致性，本文在此基础上对CJ‑2节理重新评估并投影 ￼[Kim 2020, pp. 4-6]￼[Kim 2020, pp. 7-8]￼。
- 韩国政府委员会（2019）的应力模型（逆断层与走滑断层方案）提供了深部应力差的另一种估计，但与DCDA结果差异显著，值得进一步探讨 ￼[Kim 2020, pp. 6-7]￼。
- Barton & Quadros (2015) 指出JRC随应力各向异性增大而减小，支持高应力差产生更光滑节理的观点 ￼[Kim 2020, pp. 8-8]￼。
- Huang & Doong (1990) 的剪切试验证明了节理剪切强度的方向依赖性，为粗糙度与应力方向关联提供了理论基础 ￼[Kim 2020, pp. 8-8]￼。

## Open Questions
- 单一样本的对齐现象是否具有统计显著性？需要更多含不同方向和倾角节理的岩心进行重复验证 ￼[Kim 2020, pp. 7-8]￼。
- DCDA估算的13.3 MPa与韩国政府委员会模型的123 MPa存在量级矛盾，原因可能涉及非弹性效应、应力结构复杂性或测量条件差异，需进一步研究 ￼[Kim 2020, pp. 6-7]￼。
- 节理粗糙度记录古应力的时间窗口和保存条件尚不明确——后期应力改变或矿物充填是否会掩盖原始信号？
- 如何将JRC方向转换为绝对地理方向，需结合岩心定向数据，而本文未提及岩心定向精度 ￼[Kim 2020, pp. 2-3]￼。
- DCDA方法在强各向异性、高应力或存在微裂纹的岩石中是否依然可靠？文中指出DSCA方法在类似条件下失效，DCDA亦可能受同样限制 ￼[Kim 2020, pp. 2-3]￼。

## Source Coverage
本文档完全基于提供的**11个非空索引片段**生成，未使用任何外部未标明信息。索引片段总字符数50,552，处理字符数50,549，覆盖率为：
- 按片段数：1.0（11/11）
- 按字符数：0.999941（50,549/50,552）
- 源签名：86074ccadbd352edf9941d7f7daa27d9d62b6212
- 编译策略：单次直通生成markdown，无额外检索。
