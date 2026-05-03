---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-barton-advances-in-joint-roughness-coefficient-jrc-and-its-engineering-applications"
title: "Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications."
status: "draft"
source_pdf: "data/papers/2023 - Advances in joint roughness coefficient (JRC) and its engineering applications.pdf"
collections:
  - "zotero new"
citation: "Barton, Nick, et al. \"Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 15, 2023, pp. 3352-79, doi:10.1016/j.jrmge.2023.02.002. Accessed 2026."
indexed_texts: "32"
indexed_chars: "157612"
nonempty_source_blocks: "32"
compiled_source_blocks: "32"
compiled_source_chars: "158384"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004898"
coverage_status: "full-index"
source_signature: "b46ce356923c911f8d896a04cc96081a6997ea9b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:13:23"
---

# Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications.

## One-line Summary
本文综述了岩石节理粗糙度系数（JRC）自Barton (1973)提出以来的起源、含义、测量与估算方法、各向异性与尺度效应、基于JRC的节理力学性质描述及其在岩石工程中的应用，强调JRC是广泛采用的粗糙度参数，与JCS和φ_r共同构成Barton-Bandis非线性抗剪强度准则的核心。 [Barton 2023, pp. 1-1]

## Research Question
如何全面梳理JRC的发展脉络，阐明其概念内涵、测量与估算技术、方向性与尺度依赖性特征，以及基于JRC的节理与岩体力学行为描述和工程应用，从而揭示其作为岩石工程通用参数的优势与局限？ [Barton 2023, pp. 1-1]

## Study Area / Data
本文为综述性文章，不产生新的原始数据。其证据基础包括：
- Barton (1973)开展的130个天然节理试样的室内直剪及倾斜试验数据，获得390条粗糙度剖面。 [Barton 2023, pp. 2-4][Barton 2023, pp. 5-5]
- Bandis (1980)等通过大量节理及复制品直剪试验建立的尺度效应校正曲线与数据。 [Barton 2023, pp. 12-13]
- 小浪底水库区1157条节理剖面、后续19616条不同尺寸剖面的统计资料。 [Barton 2023, pp. 12-13][Barton 2023, pp. 13-14]
- 大量野外实测与室内3D激光扫描、摄影测量等数字化形貌数据。 [Barton 2023, pp. 4-5]
- 岩体分类Q系统、Q-slope法及UDEC-BB数值模拟在实践中积累的案例记录。 [Barton 2023, pp. 18-19][Barton 2023, pp. 19-20]

## Methods
本综述涵盖的JRC相关方法体系包括：
- **粗糙度测量**：轮廓梳（0.25 mm分辨率）、滚轮/探针式轮廓仪、直尺与卷尺测最大起伏度、非接触式（摄影测量、图像处理、结构光扫描、激光扫描）。 [Barton 2023, pp. 5-5]
- **JRC估算**：①视觉比较法（与Barton & Choubey的十条典型剖面比对）；②实验法（直剪试验反算、倾斜试验、推/拉试验）；③振幅/长度（a/L）法（直尺法、基础粗糙度尺），并给出从实验室尺度（100 mm）至10 m尺度的换算关系；⑤统计与分形方法（如SDi与JRC相关性）；⑥人工智能法（神经网络、支持向量机等）。 [Barton 2023, pp. 5-9][Barton 2023, pp. 9-10]
- **各向异性与尺度效应分析**：通过统计JRC方向分布、全局/局部各向异性指标、椭球函数拟合、中智函数导数确定平稳阈值（ST）等。 [Barton 2023, pp. 11-12][Barton 2023, pp. 13-14]
- **节理性质描述**：利用JRC-JCS模型描述剪切应力-位移、剪胀、法向闭合、水力传导（物理孔径E与水力孔径e的关系）等行为。 [Barton 2023, pp. 14-16][Barton 2023, pp. 16-18]
- **岩体性质评估**：Q系统中Jr与JRC的关联，Q-slope中Jr/Ja的加权，以及UDEC-BB/3DEC数值模拟中采用BB非线性准则。 [Barton 2023, pp. 18-19][Barton 2023, pp. 19-20]

## Key Findings
1. JRC由Barton (1973)提出，是一个从0到20（实际可超过20）的无量纲滑动尺度，约等于粗糙度振幅与试样长度的比值乘以400。其本质是描述具有潜在互锁性的节理壁相对粗糙度。 [Barton 2023, pp. 2-4]
2. 峰值抗剪强度准则τ/σ_n = tan[JRC·log₁₀(JCS/σ_n) + φ_r]（Barton-Bandis准则）考虑了JRC、JCS和残余摩擦角φ_r，并可通过倾斜试验、直剪试验等获取参数。该准则比线性莫尔-库仑准则更准确，已嵌入UDEC-BB等离散元程序。 [Barton 2023, pp. 2-4][Barton 2023, pp. 1-2]
3. JRC具有显著的尺度效应：随试样长度（或块体尺寸）增大，JRC降低，通常遵循JRC_n ≈ JRC_0 (L_n/L_0)^{-0.02 JRC_0}，JCS也有类似衰减律。相应地，剪切强度也随块体尺寸增大而减小。 [Barton 2023, pp. 12-13]
4. 岩石节理粗糙度表现出强烈的各向异性，不同方向的JRC统计值可用正态分布描述，并可通过全局/局部各向异性指标量化。方向性对节理的剪切行为有显著影响。 [Barton 2023, pp. 11-12]
5. 节理粗糙度的平稳阈值（ST）可通过JRC的中智函数导数确定，当试样尺寸超过ST后，粗糙度行为基本与尺度无关，全局各向异性趋于稳定。 [Barton 2023, pp. 13-14]
6. 基于JRC可定量描述节理的剪切应力-位移曲线（mobilized JRC与峰值位移d_peak关系）、剪胀角（d_n介于JRC log10(JCS/σ_n)/2与2JRC log10(JCS/σ_n)之间）、法向闭合行为（初始法向刚度K_ni = 0.02[JCS/a_j + 2JRC - 10]）以及水力传导（e = JRC^2.5 / (E/e)^2，即水力孔径与物理孔径之比随粗糙度增大而增大）。 [Barton 2023, pp. 14-16][Barton 2023, pp. 16-18]
7. 视觉比较法虽简单，但存在主观性；倾斜试验是较“科学”的确定JRC的方法，但多数研究忽略了该方法；直尺法（a/L法）在工程现场实用有效。 [Barton 2023, pp. 5-7][Barton 2023, pp. 9-10]
8. 岩体分类Q系统中，节理粗糙度系数Jr与JRC存在近似对应关系；Q-slope方法利用Jr/Ja加权计算安全无支护边坡角。 [Barton 2023, pp. 19-20]
9. 非连续介质方法（如UDEC-BB）比连续介质方法更适用于超过90%的岩体，因其能更真实地反映节理对变形和破坏的控制。 [Barton 2023, pp. 21-22]
10. 试样代表性与采样间隔对JRC估算精度影响显著：全局搜索法（GSM）能避免等分采样法的偏差；JRC测量所用采样间隔应随试样尺度增大而增大，且需根据粗糙度水平确定适宜阈值。 [Barton 2023, pp. 22-23][Barton 2023, pp. 25-26]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|-----------|-------|
| 峰值抗剪强度准则 τ/σ_n = tan[JRC log₁₀(JCS/σ_n) + φ_r] | Barton (1973); Barton & Choubey (1977) [Barton 2023, pp. 2-4] | 无充填、可风化的节理，φ_r由Schmidt锤回弹值估算 | 适用于法向应力范围很广，非线性包络取代了摩尔-库仑直线 |
| JRC与尺度关系 JRC_n ≈ JRC_0 (L_n/L_0)^{-0.02 JRC_0}，JCS_n ≈ JCS_0 (L_n/L_0)^{-0.03 JRC_0} | Barton & Bandis (1982) [Barton 2023, pp. 12-13] | L_0=100 mm，L_n为所需块体尺寸（交叉节理平均间距） | 解释剪切强度的负尺度效应 |
| 倾斜试验获得JRC公式 JRC = (α - φ_r) / log₁₀(JCS/σ_n0)，σ_n0 = γ·b·cos²α | Barton & Choubey (1977) [Barton 2023, pp. 8-9] | 实验室样品b≈20 mm，野外b≈200 mm，JCS≈100 MPa | 倾斜角α受限于避免倾覆，实验室尺度JRC上限约8~12 |
| 直尺法近似式 JRC ≈ 400a/L (L=0.1 m), 450a/L (L=1 m), 500a/L (L=10 m) | Barton (1981) [Barton 2023, pp. 9-10] | a为最大振幅，L为节理长度，直尺中间接触点须记录 | 基于“一级粗糙度”控制剪切强度的假设 |
| 峰值剪胀角与粗糙度成分关系 d_n ≈ JRC log₁₀(JCS/σ_n) (低损伤)，d_n ≈ JRC log₁₀(JCS/σ_n)/2 (高损伤) | Barton & Choubey (1977) [Barton 2023, pp. 15-16] | 损伤系数M=JRC/(d_n log₁₀(JCS/σ_n) )，低应力M≈1，高应力M≈2 | 剪胀起始于d/d_peak≈0.3 |
| 初始法向刚度 K_ni = 0.02[JCS/a_j + 2JRC - 10]，最大闭合V_m = A + B·JRC + C(JCS/a_j)^D | Bandis (1980); Barton (1982) [Barton 2023, pp. 16-16] | a_j为初始自重应力下的孔径，JRC=5~15, JCS=22~182 MPa, a_j=0.1~0.6 mm | 该双曲线模型优于Goodman的双函数模型 |
| 水力孔径与物理孔径关系 e = E² / JRC^{2.5} (E/e≥1) | Barton (1982); Barton & Quadros (1997) [Barton 2023, pp. 16-18] | 适用于轻微剪切位移、无显著碎屑生成的条件 | 立方律(E=e)仅对极光滑或极宽节理成立 |
| 岩体分类Q参数Jr与JRC的对应：Jr 1~4大致对应不同尺度的JRC | Barton (1987) [Barton 2023, pp. 19-20] | 需结合Jr/Ja评估节理抗剪能力，JRC_20和JRC_100为不同块体尺寸的JRC示例 | 实际工程中Q系统应用广泛 |
| 平稳阈值ST可通过|d(JRC)/dL| = 0.05确定 | Yong et al. (2020) [Barton 2023, pp. 13-14] | 基于中智函数导数分析JRC随样本长度的变化 | 超过ST后粗糙度各向异性基本不变 |
| 全局搜索法（GSM）获得的100 mm样本JRC均值与EPSM一致，但标准差显著不同 | Du et al. (2022a) [Barton 2023, pp. 23-25] | 以1000 mm长剖面为母体，GSM可提取1801个样本，EPSM仅得10个 | EPSM可能导致对粗糙度特征的错误估计 |

## Limitations
- 视觉比较法估计JRC具有较大主观性，不同评价者间变异显著，且对于非典型剖面（阶梯状、振幅不一致等）精度差。 [Barton 2023, pp. 5-7]
- 许多“改进JRC”的研究依赖二维剖面或三维激光扫描，但未通过倾斜试验进行校核，可能忽略了实际三维剪切行为中的其他参数（JCS、φ_r）。 [Barton 2023, pp. 9-10]
- 多数研究集中在实验室尺度（≤100 mm）的节理粗糙度，对工程尺度（数米至数十米）的JRC估计仍不够成熟，大于10 m的节理粗糙度与JRC关系尚待深入。 [Barton 2023, pp. 25-26]
- 试样代表性不足可能导致对尺度效应和抗剪强度统计特征的错误推断；等分采样法往往样本量过小，无法充分反映粗糙度非均质性。 [Barton 2023, pp. 22-23]
- 采样间隔的选择尚无统一标准，不恰当的SI可能平滑掉关键的不平整信息，从而导致JRC估计偏差。 [Barton 2023, pp. 25-26]
- 节理粗糙度中的“波状度”与“不平整度”对剪切强度的独立贡献尚未得到充分量化，现有方法多将二者合并处理。 [Barton 2023, pp. 9-10]

## Assumptions / Conditions
- Barton-Bandis准则假定节理壁粗糙度具有相关性，闭合时存在显著互锁，节理无充填（或充填不影响抗剪）且法向应力范围处于岩石的脆性行为域。 [Barton 2023, pp. 2-4]
- 利用a/L法估算JRC的前提是“一级粗糙度”（最大起伏角）主导抗剪强度；这一简化在多数情况下可接受，但未独立区分波状度与不平整度。 [Barton 2023, pp. 9-10]
- 倾斜试验推定JRC时，假定滑移瞬间的法向应力分布不均可由式σ_n0 = γ·b·cos²α近似修正，且试验自动限于不会发生倾覆的“较光滑”节理。 [Barton 2023, pp. 8-9]
- 尺度效应校正公式（JRC_n与JCS_n的衰减律）基于实验室尺度和模型材料试验数据外推，其实用性依赖于交叉节理间距作为等效块体尺寸的代表。 [Barton 2023, pp. 12-13]
- 水力传导模型中，物理孔径E与水力孔径e的关系仅适用于E/e≥1且无显著剪切破坏碎屑填充；其外推至工程尺度时假定闭合行为不具有尺寸依赖性。 [Barton 2023, pp. 16-18]
- 平稳阈值ST的确定依赖于JRC的中智函数导数绝对值降至0.05以下的假设，认为此时粗糙度的尺度敏感性可忽略。 [Barton 2023, pp. 13-14]

## Key Variables / Parameters
- **JRC**：节理粗糙度系数，0~20（可扩展至30），无量纲，表征节理相对粗糙度。 [Barton 2023, pp. 2-4]
- **JCS**：节理壁有效单轴抗压强度，随风化程度降低，可通过点荷载或Schmidt锤试验确定。 [Barton 2023, pp. 2-4]
- **φ_b**：基本摩擦角，反映材质矿物学性质，由光面岩片剪切试验获得。 [Barton 2023, pp. 4-5]
- **φ_r**：残余摩擦角，考虑风化时由φ_r = φ_b - 20° + 20(r/R)估算，r为风化节理面回弹值，R为未风化干岩面回弹值。 [Barton 2023, pp. 4-5]
- **尺度变量**：L_0（实验室标称长度，通常100 mm），L_n（目标块体尺寸，由交叉节理平均间距确定）。 [Barton 2023, pp. 12-13]
- **振幅a**：最大起伏幅度，用于a/L法。 [Barton 2023, pp. 5-5][Barton 2023, pp. 9-10]
- **孔径**：物理孔径E，水力孔径e，a_j（初始孔径），V_m（最大闭合量）。 [Barton 2023, pp. 16-18]
- **损伤系数M**：M = JRC / [d_n·log₁₀(JCS/σ_n)]，低应力M≈1，高应力M≈2。 [Barton 2023, pp. 15-16]
- **Q系统参数**：Jr（节理粗糙度系数），Ja（节理蚀变系数），与JRC存在关联。 [Barton 2023, pp. 19-20]
- **采样间隔SI与平稳阈值ST**：影响数字化剖面粗糙度表征，SI_max与样本尺度正相关，ST为粗糙度各向异性趋于平稳的临界尺寸。 [Barton 2023, pp. 13-14][Barton 2023, pp. 25-26]

## Reusable Claims
1. **Barton-Bandis峰值抗剪强度准则**：对于无充填、具有相关粗糙度的节理，在脆性行为范围内，峰值抗剪强度可由τ/σ_n = tan[JRC·log₁₀(JCS/σ_n) + φ_r]准确描述，该式通过130个天然节理试验统计得到，并可考虑尺度效应进行外推。 [Barton 2023, pp. 2-4]  
   *条件*：需已知JRC、JCS、φ_r，且节理面不存在厚层断层泥或充填物；法向应力不宜导致大面积节理壁凸起被剪断（即M≈1~2范围内适用）。  
   *局限*：JRC的获取存在主观性，且该准则为经验模型，未严格区分波状与不平整的贡献。

2. **倾斜试验测定JRC**：通过现场或实验室节理试样的自重重力滑移倾角α，按JRC = (α - φ_r) / log₁₀(JCS/σ_n0)反算得到JRC，是一种考虑三维方向性且避免试样反复损伤的方法。 [Barton 2023, pp. 8-9]  
   *条件*：适用于不发生倾覆破坏的相对光滑节理，实验室尺度上限JRC≈8~12（取决于φ_r与试样厚度），野外加风化可使上限提高至JRC=20；需已知φ_r、JCS和试样厚度。  
   *局限*：倾覆失效限制了粗糙度较大的节理应用，σ_n0的近似公式仅部分补偿应力不均匀。

3. **JRC的尺度效应衰减律**：对于工程尺度的岩体，可采用JRC_n ≈ JRC_0 · (L_n/L_0)^{-0.02·JRC_0}和JCS_n ≈ JCS_0 · (L_n/L_0)^{-0.03·JRC_0}将实验室100 mm尺度参数修正至目标块体尺寸。 [Barton 2023, pp. 12-13]  
   *条件*：块体尺寸L_n取交叉节理的平均间距；此关系基于模型材料张力裂缝和有限天然节理的直剪试验归纳，JRC_0值需由标准长度剖面或倾斜试验确定。  
   *局限*：对极宽大节理（>10 m）的校正效果尚缺少充分验证；环境风化与应力历史可能影响衰减指数。

4. **水力孔径与物理孔径关系**：对于粗糙节理，水力孔径e小于平均物理孔径E，可用关系 e = E² / JRC^{2.5}（E/e≥1）将现场水压试验测得的水力孔径换算为物理孔径，进而指导灌浆粒径选择等。 [Barton 2023, pp. 16-18]  
   *条件*：节理无显著剪切位移和碎屑生成；适用于E/e≥1的粗糙节理；假设法向闭合无尺度依赖性。  
   *局限*：该式为近似经验式，在极小孔径条件下偏差增大，且未考虑充填物和两壁局部接触的复杂影响。

5. **岩体分类中Jr与JRC的关联**：Q系统的节理粗糙度系数Jr可近似映射到不同尺度的JRC，从而将现场节理粗糙度的定性-半定量评价纳入岩体质量分级和支护设计。 [Barton 2023, pp. 19-20]  
   *条件*：Jr取值考虑节理壁粗糙度、平面性与充填情况；JRC与Jr的关系图（Fig. 23）基于经验，需注意到JRC可能因块体尺寸不同而变化。  
   *局限*：Jr仅反映“最弱节理组”的粗糙度，并不能完全代表各向异性；换算为JRC时须明确对应尺度。

6. **粗糙度平稳阈值ST的确定**：通过JRC的统计中智函数导数|d(JRC)/dL|降至0.05以下，可确定节理粗糙度的ST，超过该长度后粗糙度参数不再随尺度显著变化，各向异性亦趋于稳定。 [Barton 2023, pp. 13-14]  
   *条件*：需要获得不同长度剖面的大量JRC数据（如从100 mm到3000 mm），利用中智数表示其上、下界与均值，再求导。  
   *局限*：方法的普适性尚需更多岩石类型和节理形貌的验证；ST值可能受采样方向和形貌特征影响。

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[Barton-Bandis criterion]]
- [[scale effect of joint roughness]]
- [[roughness anisotropy]]
- [[stationarity threshold (ST)]]
- [[peak shear strength of rock joints]]
- [[residual friction angle]]
- [[basic friction angle]]
- [[joint wall compressive strength (JCS)]]
- [[joint damage coefficient (M)]]
- [[physical aperture and hydraulic aperture]]
- [[rock mass classification Q-system]]
- [[Q-slope method]]
- [[progressive failure components CcSs]]
- [[UDEC-BB distinct element model]]
- [[pseudo-continuum vs discontinuum approach]]
- [[representative elementary volume (REV) for fracture roughness]]
- [[neutrosophic functions for roughness representation]]

## Candidate Methods
- [[visual comparison method for JRC]]
- [[tilt test for JRC estimation]]
- [[direct shear test back-analysis for JRC]]
- [[push/pull test for JRC]]
- [[straight-edge method (a/L method)]]
- [[basal roughness ruler]]
- [[profile comb measurement]]
- [[roller-and-stylus profilometer]]
- [[sampling interval determination via Fourier series]]
- [[global search method (GSM) for representative joint samples]]
- [[equal-partition sampling method (EPSM)]]
- [[progressive coverage statistical sampling]]
- [[JRC scale correction curves]]
- [[hyperbolic normal closure model]]
- [[hydraulic aperture estimation from JRC]]
- [[Q-system rock mass classification]]
- [[UDEC-BB numerical modeling]]
- [[3DEC-BB calibration]]

## Connections To Other Work
- JRC的提出直接源于Patton (1966)的双线性抗剪强度理论及Newland & Allely (1957)的颗粒材料剪切抗力公式，Barton (1971)将其中的几何项i扩展为应力依赖的对数函数。 [Barton 2023, pp. 2-4]
- 粗糙度量化方面，众多学者（如Tse & Cruden (1979), Yu & Vayssade (1991), Tatone & Grasselli (2010)等）建立了JRC与统计参数（如倾斜角标准差SDi）或分形维数的关系；但分形方法中采用自相似法计算自仿射节理面时易出问题。 [Barton 2023, pp. 9-10]
- Grasselli (2001)等提出了基于三维形貌参数θ*_max/(C+1)的方向性粗糙度指标，其各向异性与JRC的各向极性图存在相似性。 [Barton 2023, pp. 11-12]
- Q系统（Barton et al., 1974）中的Jr与JRC近似关联，Q-slope （Barton & Bar, 2015）进一步将Jr/Ja加权用于边坡角估算。 [Barton 2023, pp. 19-20]
- 节理本构模型的扩展包括：Zhao (1997)引入节理吻合系数JMC；Bandis (1980)提出的法向闭合双曲线模型；Olsson & Barton (2001)完善了剪切过程中的水力-力学耦合；Xia et al. (2003)等尝试分离波状度与不平整度对闭合变形的影响。 [Barton 2023, pp. 14-15][Barton 2023, pp. 16-16]
- 与Mohr-Coulomb对比，UDEC-BB数值模拟展示出由于非线性剪胀导致的更高法向应力和更小位移，且块体旋转等机制更真实，许多工程验证（如Gjøvik冰球馆）证实了BB模型的准确性。 [Barton 2023, pp. 21-22]
- 在小浪底等工程中，Du等人的团队基于大量野外剖面发展了改进的直尺法、粗糙度尺、全局搜索采样方法和代表取样技术，为JRC的工程应用提供了重要补充。 [Barton 2023, pp. 9-10][Barton 2023, pp. 23-25]

## Open Questions
- 如何定量分离波状度（一级粗糙度）与不平整度（二级粗糙度）对节理抗剪强度及闭合行为的独立贡献？[Barton 2023, pp. 9-10]
- 对于实际工程中长达数米至数十米的节理，现有JRC尺度效应校正公式的可靠性和适用上限如何？如何进一步获取块体尺寸大于10 m的节理粗糙度与JRC的可靠关系？[Barton 2023, pp. 25-26]
- 在非连续介质三维数值模拟（如3DEC-BB）中，如何将JRC的方向性和尺度效应更系统地嵌入，以实现更真实的岩体力学响应预测？[Barton 2023, pp. 25-26]
- 如何建立统一的采样间隔选取原则，以兼顾实验室小尺度与现场大尺度粗糙度测量的精确性与经济性？[Barton 2023, pp. 25-26]
- 粗糙度表征的代表性样本量要求尚未形成规范：针对不同岩性、尺度及法向应力水平，最少试样数量（RMN）应如何确定才能保证抗剪强度统计推断的置信度？[Barton 2023, pp. 22-23]
- 热致超闭合与机械超闭合现象中，垂直于节理面的“JRC”效应是否需要单独定义，以解释地热储层中冷注水因光滑节理优先张开而导致的短路循环？[Barton 2023, pp. 16-16]

## Source Coverage
本页严格基于提供的全部32个非空索引片段进行编译，未添加片段外的信息。所有事实性陈述均追溯至原始片段标签。编译过程覆盖全部157,612字符（索引字符），输出字符158,384，区块覆盖率100%，字符覆盖率100.49%，具备完全索引（full-index）状态，无片段遗漏。 [Coverage audit: coverage_ratio_by_blocks=1.0, coverage_ratio_by_chars=1.004898]
