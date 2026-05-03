---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-tom-s-how-do-high-temperatures-affect-rock-properties-a-comprehensive-review-of-experimenta"
title: "How Do High Temperatures Affect Rock Properties? A Comprehensive Review of Experimental Thermal Effects and Underlying Mechanisms."
status: "draft"
source_pdf: "data/papers/2025 - How do high temperatures affect rock properties A comprehensive review of experimental thermal effects and underlying mechanisms.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Tomás, Roberto, et al. \"How Do High Temperatures Affect Rock Properties? A Comprehensive Review of Experimental Thermal Effects and Underlying Mechanisms.\" *Engineering Geology*, vol. 357, 2025, article 108323. doi:10.1016/j.enggeo.2025.108323."
indexed_texts: "36"
indexed_chars: "178174"
nonempty_source_blocks: "36"
compiled_source_blocks: "36"
compiled_source_chars: "170302"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.955818"
coverage_status: "full-index"
source_signature: "8e67691de0249f462f758482e45466bae7546ae2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:29:54"
---

# How Do High Temperatures Affect Rock Properties? A Comprehensive Review of Experimental Thermal Effects and Underlying Mechanisms.

## One-line Summary
系统综述岩石高温行为的实验方法、物性变化、热过程及控制因素，基于187篇文献构建超过10 000组温度‑属性数据对、1360条演化曲线与22种地质力学性质的综合数据库。

## Research Question
高温如何改变岩石的物理、力学、热学与水力学性质？其核心物化机制、控制因子和不同岩石类型的响应规律是什么？

## Study Area / Data
研究资料源自Web of Science检索并筛选的187篇以实验室高温岩石测试为主的原创论文（初始检索449篇），并补充至2025年1月的特定文献。最终数据库包含>10 000组温度‑属性数据对、1360条温度‑属性演化曲线，覆盖22种地质力学性质。岩石类型覆盖碎屑沉积岩（砂岩、灰岩、页岩等）、火成岩（花岗岩、玄武岩、辉长岩等）及变质岩（大理岩、矽卡岩），并以花岗岩、砂岩、灰岩和大理岩最为集中。

## Methods
- **数据获取**：Web of Science高级检索（关键词组合包括‘high temperature’、‘rock properties’、‘effect’、‘test’），通过题录筛选与人工排除，再以WebPlotDigitizer数字化图表数据。
- **热处理方法**：加热设备以辐射式电阻马弗炉（可达1600 °C）为主，兼有微波、流体包围加热、火焰射流、激光等；冷却方式包括空气缓慢冷却、水浸冷却和液氮（LN₂）急速冷却。升温模式分为恒温速率法和变温速率法。
- **目标温度范围**：预制加热（先加热再冷却后测试）最高至1200 °C，模态温度800 °C；实时加热测试模态温度100 °C，特殊三轴设备可至>1000 °C。
- **表征技术**：视觉（ICOMOS-ISCS劣化图案描述）；微结构（XRD，TG‑DTA，SEM‑EDX，偏光显微镜，荧光浸渗法，CT，MIP，NMR）；物理性质（色度，质量/体积，密度，孔隙率，吸水率，超声波P/S波速，声发射，硬度）；力学性质（单轴压缩UCS、弹性模量、泊松比、动态弹性参数，间接拉伸强度，点荷载指数，抗弯强度，剪切强度参数c/φ，断裂韧度I～III型，DIC全场应变）；热学性质（导热系数，比热容，热膨胀系数）；渗透率等。
- **模型技术**：综述了数值方法（FEM、DEM、连续损伤模型等）和人工智能预测方法。

## Key Findings
- **热转变温度阈值**：多数岩石和大部分性质的明显劣化起始于300～400 °C，但临界温度因岩类和性质而异（TTT或TTTR范围）。
- **主导机制**：矿物热膨胀差异、石英α‑β相变（~573 °C）、方解石/白云石热分解（700～900 °C）及黏土矿物脱羟基是微结构损伤和性质突变的主因；脱水、氧化/燃烧、固相反应等伴随质量损失与孔裂隙增生。
- **升温与保温影响较小**：常用实验室加热速率（5 °C/min）对岩石性质的影响远小于目标温度；保温时间（多数2 h）在高温下影响亦有限。
- **冷却方式冲击显著**：急速冷却（水冷、LN₂）导致表面拉应力急剧升高，诱发更多更宽的微裂纹甚至宏观裂纹，显著劣化力学与渗透特性。LN₂平均冷却速率达307.32 °C/min，远超空气冷却（0.49 °C/min）和水冷（7.02 °C/min）。
- **岩石类型响应差异**：
  - 火成岩（主要为花岗岩）：UCS、杨氏模量、拉伸强度常见先升后降（Type IV），强化幅度可达60 %以下，随后在>500 °C快速下降。密度、波速、导热系数等持续下降。
  - 沉积岩（砂岩、灰岩等）：行为变异度大。孔隙率可增至初始的47.8倍；波速降幅显著（可达原值10～70 %）；灰岩因方解石分解在700 °C以上质量损失>30 %，强度急剧损耗。黏土质胶结的岩石在≥400 °C可能因烧结出现强度回升。
  - 变质岩（大理岩为主）：数据稀少，大致呈Type I或III‑1型劣化，方解石分解温度附近强度突降。
- **孔隙‑渗透率耦合**：渗透率一般随温度呈缓慢—急剧两阶段上升，尤其在石英相变或有机质热解阶段；高围压部分抵消热开裂。
- **微结构控制**：矿物组成、粒径分布、原生微裂隙和粒间孔隙比矿物学本身更主导热敏感性。粗粒、高初始孔隙度在一定温度下可容纳膨胀，但也是裂纹萌生点。
- **强化与弱化机制**：低温强化是微裂隙闭合、有效应力增加、应力分散及烧结共同作用的结果；高温弱化受微裂隙萌生‑扩展、矿物分解与相变控制。
- **标准化与多场耦合空白**：缺乏统一实验规程；鲜有温度‑流体‑力学耦合研究；标度律缺失；模型不确定性与微观‑宏观定量联系仍为薄弱环节。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 沉积岩在600 °C后质量损失可达30 %以上，火成岩即使在1000 °C亦<5 %。 | [Tom 2025, pp. 16-16] | 预加热，空气中冷却后称重 | 图8a，数据汇总 |
| 孔隙率升高：沉积岩个别可达初始值的47.8倍，火成岩一般缓慢增加，在500 °C后加速。 | [Tom 2025, pp. 16-16] | 常规重‑体积法与MIP综合 | 图8d；Type IVi行为见于部分岩石（先降后升） |
| P波速度在800 °C时降至原值的10 %–70 %；花岗岩在400–700 °C间下降显著。 | [Tom 2025, pp. 16-17] | 预加热，超声波测试 | 图9a；行为类型III‑1、II等 |
| UCS强化：花岗岩在500 °C以下可升高60 %（多数<20 %），之后急剧下降。灰岩以Type I或III‑1为主，800 °C时降至原值20 %。 | [Tom 2025, pp. 19-19] | 单轴压缩 | 图10a；强化归因于裂隙闭合、烧结 |
| 冷却速率：空气~0.49 °C/min，水~7.02 °C/min，液氮~307.32 °C/min (Wu et al., 2019)。 | [Tom 2025, pp. 8-8] | 间接测量 | Wu et al. (2019) 数据 |
| 方解石分解反应CaCO₃→CaO+CO₂在700–900 °C发生，可导致质量损失>40 %且试样失去完整性。 | [Tom 2025, pp. 9-10] | 热重分析与差热分析 | 反应(2)；堆积气体可致爆炸 |
| 石英α‑β相变在~573 °C，伴随约1 %体积膨胀，是石英质岩石微裂隙剧增的关键转折。 | [Tom 2025, pp. 10-11] | 物理过程描述 | 相变可逆，冷却时恢复但残余损伤 |
| 常温常压实验室马弗炉常用升温速率5 °C/min，与标准火灾曲线（237–1640 °C/min）相差数个数量级。 | [Tom 2025, pp. 5-5, 8-8] | 实验室加热 | 图2a；低速率是为避免热冲击 |
| 渗透率呈缓慢—快速两阶段增长，石英相变或有机质热解后突增。 | [Tom 2025, pp. 22-22] | 预加热后渗透率测试 | 图13；类型IIi和III‑1i |
| 导热系数随温度非线性下降，初始导热系数高的岩石降幅更大。 | [Tom 2025, pp. 22-22] | 预加热试验 | 图12a；Vosteen & Schellschmidt (2003) |

## Limitations
- 缺乏统一的实验规程（升温速率、保温时间、冷却方式、试样尺寸等），致不同研究难以直接对比。
- 多数研究集中于花岗岩、砂岩、灰岩和大理岩，变质岩及非常规岩类研究不足。
- 破坏‑冷却循环未被纳入（该综述明确排除）。
- 大量结论基于模型，且部分结果相互矛盾（如粒径影响）。
- 微结构损伤与宏观性质的定量联系多停留在定性或半定量水平。
- 实验多在岩心尺度常压下进行，实时高温‑压‑流体耦合数据稀缺。
- 岩样天然变异性、制样与测试标准差异引入的不确定性难以量化。
- 急速升温（如火灾曲线）尚未在多数研究中被真实再现，冷却梯度的实验监测信息也很有限。

## Assumptions / Conditions
- 实验均在实验室大气压力下完成，除少数三轴围压测试外。
- 热处理方式以预加热（加热后冷却）为主，部分实时测试需特制三轴室。
- 大部分数据来自恒速升温（常见5 °C/min），保温时间多为2 h，随后以空气、水或LN₂冷却。
- 性质演化曲线采用归一化值P_norm(T)=P(T)/P₀，并依据形状划分为四类趋势（Type I～IV，及其倒置型）。
- 数据库仅收录同行评审的英文期刊文章；排除地热系统、低温影响、纯地质学等不直接相关的文献。
- 综述未涉及加热‑冷却循环的影响，仅关注单次热暴露。

## Key Variables / Parameters
- 独立变量：目标温度T、升温速率、保温时间、冷却方式与冷却速率；岩石类型、矿物组成、粒径、原生微裂隙密度、粒间孔隙度。
- 响应变量（22种性质）：质量损失、体积变化、密度、孔隙率、表观密度（真实密度）、吸水率、P/S波速、声发射特征参数、表面硬度；单轴抗压强度UCS、杨氏模量、泊松比、动态弹性模量、间接拉伸强度、点荷载指数、抗弯强度、黏聚力c、内摩擦角φ、I/II/III型断裂韧度、全场应变；导热系数、比热容、热膨胀系数；渗透率；电阻率、可钻性指数、崩解耐久性、基本摩擦角等。
- 中间变量（微结构损伤指标）：裂纹密度、宽度、长度、孔隙尺寸分布、微裂纹取向、T₂谱面积等。

## Reusable Claims
- **热转变温度**：多数岩石性质的显著劣化始于300–400 °C，但具体温度因岩类和性质而异，可定义为TTT property或TTTR[Tom 2025, pp. 12-12]。
- **冷却伤害**：液氮冷却对岩石微结构的破坏远大于水冷和空气冷却，表现为微裂纹数量与宽度剧增[Tom 2025, pp. 25-25]。
- **石英相变效应**：α↔β石英转变（约573 °C）导致含石英岩石的物理、力学性质出现台阶式突变[Tom 2025, pp. 10-11]。
- **碳酸盐分解阈值**：方解石在700–900 °C分解为CaO+CO₂，引起质量损失>40 %并丧失结构完整性[Tom 2025, pp. 9-10]。
- **强度强化规律**：低温（<500 °C）下，因裂隙闭合、有效应力增加、矿物烧结等机制，UCS和弹性模量可能增强，多见于花岗岩和部分砂岩[Tom 2025, pp. 23-25]。
- **孔隙演化双模式**：部分岩石升温初期因矿物膨胀导致孔隙暂时减小，随后显著增大（Type IVi），而多数岩石呈持续增加（Type Ii、IIi）[Tom 2025, pp. 16-16]。
- **导热系数始终下降**：随温度升高，岩石导热系数非线性下降，初始导热系数高的岩石降幅更大[Tom 2025, pp. 22-22]。
- **渗透率两阶段增长**：先在低温下缓慢增加（蒸发与微开裂），超过TTT后因密集裂纹网络而急剧增大[Tom 2025, pp. 22-22]。
- **微裂纹双重作用**：原生微裂隙和孔隙既可吸收低温膨胀（延缓开裂），也可作为应力集中点加速热致开裂[Tom 2025, pp. 11-12]。
- **升温速率影响微弱**：在5～300 °C/min范围内，升温速率对变形性质的影响远小于目标温度本身[Tom 2025, pp. 8-8]。
- **微结构表征互补性**：SEM、MIP、NMR、CT在孔裂隙结构与矿物信息上各具优势和局限，联合使用可提升解释可靠性[Tom 2025, pp. 14-14]。

## Candidate Concepts
- [[thermal transition temperature]]
- [[α-β quartz transition]]
- [[calcination]]
- [[thermal shock]]
- [[microcracking threshold]]
- [[differential thermal expansion]]
- [[anisotropic thermal expansion]]
- [[preheating procedure]]
- [[real-time heating test]]
- [[cooling gradient]]
- [[thermal conductivity reduction]]
- [[permeability enhancement]]
- [[strengthening by thermal treatment]]
- [[pore network evolution]]
- [[acoustic emission b-value]]
- [[digital image correlation (DIC)]]
- [[numerical modelling of thermal cracking]]
- [[AI-based prediction of rock properties]]
- [[microstructural thermal damage]]
- [[thermally induced ductility]]
- [[sintering effect in clay-rich rocks]]
- [[fire curve replication]]

## Candidate Methods
- [[X-ray diffraction (XRD)]]
- [[thermogravimetric analysis (TGA)]]
- [[differential thermal analysis (DTA)]]
- [[scanning electron microscopy (SEM) with EDS]]
- [[optical polarized microscopy]]
- [[fluorescence microscopy of microcracks]]
- [[computer tomography (CT) for pore network]]
- [[mercury intrusion porosimetry (MIP)]]
- [[nuclear magnetic resonance (NMR) relaxometry]]
- [[CIE Lab* colour measurement]]
- [[ultrasonic P-wave and S-wave velocity]]
- [[acoustic emission (AE) monitoring]]
- [[uniaxial compressive strength (UCS) test]]
- [[indirect tensile (Brazilian) test]]
- [[point load index test]]
- [[three-point bending (flexural strength)]]
- [[direct shear or triaxial shear for c and φ]]
- [[fracture toughness testing (Mode I, II, III)]]
- [[thermal conductivity measurement]]
- [[specific heat capacity measurement]]
- [[thermal expansion coefficient measurement]]
- [[permeability measurement under high temperature]]
- [[digital image correlation (DIC) for strain fields]]
- [[finite element method (FEM) for thermomechanics]]
- [[discrete element method (DEM) for crack growth]]
- [[artificial intelligence (AI) modelling for property prediction]]

## Connections To Other Work
- 加热曲线与ISO、Eurocode、RABT等标准火灾曲线的对比，指出现有实验室升温速率远低于真实火灾[Tom 2025, pp. 4-5]。
- 引用Heuze (1983) 对花岗岩热物性早期综述，Tian (2013) 的行为分类框架被扩展为Type I–IV四类[Tom 2025, pp. 12-12]。
- Rossi et al. (2018) 的火焰射流高速加热实验证实了局部热应力集中对晶界开裂的促进作用[Tom 2025, pp. 5-6]。
- Wu et al. (2019) 提供了冷却速率的定量数据，支撑了液氮急速冷却造成严重热冲击的结论[Tom 2025, pp. 8-8]。
- 微结构控制因素的讨论与Homand‑Etienne and Houpert (1989)、Siegesmund et al. (2000) 等经典微裂隙研究衔接[Tom 2025, pp. 11-12]。
- 多场耦合数值模型方面，回顾了Timoshenko and Goodier (1951) 的解析解以及后续FEM、DEM、PD等离散‑连续方法的发展[Tom 2025, pp. 25-25]。
- 人工智能应用引用了Gao et al. (2023) 基于SEM图像的损伤识别、Ma et al. (2025) 弹性模量预测等成果[Tom 2025, pp. 25-25]。
- 工程应用中的温度范围参考了地热（≤200 °C）、火灾（500–1350 °C）、核废料（可达800 °C）、煤地下气化（>1000 °C）等文献[Tom 2025, pp. 3-4]。

## Open Questions
- 如何建立统一的热处理实验标准，使不同研究的升温程序、冷却方式、试样尺寸和测试时机可以横向对比？
- 缺少温度‑流体（水、CO₂）‑力学多场耦合的原位试验数据，尤其是高温高压条件下渗透率‑裂隙动态演化。
- 微结构损伤参量（裂纹密度、开度、连通性）与宏观力学响应的定量本构关系仍需深化。
- 变质岩及其他非常规岩类（如蒸发岩、火山碎屑岩）的高温行为研究极少，代表性不足。
- 粒径影响仍存争议：粗晶似乎产生更大的热膨胀系数，但亦有实验得出相反趋势；需要结合颗粒形态、结晶取向等更多文本进行分析。
- 快速升温（如秒级升至1000 °C）对性质的影响与慢速升温是否存在本质差异？目前高于50 °C/min的数据极少。
- 在长期高温‑泄压循环条件下，岩石时效损伤（如蠕变‑松弛‑愈合）规律几乎完全空白。
- 从岩心尺度到工程尺度（隧道、储层）的宏观标度律仍然缺失，数值模型亟需多尺度的实验室与现场验证。

## Source Coverage
本次编辑使用了全部36个非空索引片段，源字符数178 174，编译后字符数170 302，片段覆盖率（按块计）1.0，字符覆盖率约0.956。未增添任何超出所供片段的信息。所有事实性声明均源自已编入的片段，如需进一步确认可追溯至原出处。
