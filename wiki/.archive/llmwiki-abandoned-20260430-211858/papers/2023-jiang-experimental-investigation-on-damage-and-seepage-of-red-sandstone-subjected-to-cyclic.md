---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-jiang-experimental-investigation-on-damage-and-seepage-of-red-sandstone-subjected-to-cyclic"
title: "Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment."
status: "draft"
source_pdf: "data/papers/2023 - Experimental investigation on damage and seepage of red sandstone subjected to cyclic thermal and cold treatment.pdf"
collections:
  - "zotero new"
citation: "Jiang, Haopeng, et al. \"Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment.\" *Geoenergy Science and Engineering*, vol. 222, 2023, 211461."
indexed_texts: "11"
indexed_chars: "52029"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:22:32"
---

# Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment.

## One-line Summary
通过三轴渗流试验与统计损伤理论，研究了红砂岩在热‑冷循环冲击下的损伤演化和渗透率变化规律，并构建了考虑耦合损伤的渗透率模型。

## Research Question
在寒冷地区地热工程中，热‑冷循环冲击对围岩造成的损伤及渗透特性如何变化？能否建立一个考虑损伤的渗透率模型来描述其水力耦合行为？

## Study Area / Data
- 研究对象：红砂岩（Red sandstone），未指定具体产地，但从片段看为均质岩样，制备成标准试件用于实验室三轴渗流测试。
- 实验分组：对照组（20°C，无循环）、四个热处理温度组（200°C、400°C、800°C、1000°C），每组分别进行10次和20次热‑冷冲击循环，每个循环条件使用3个试件 [Jiang 2023, pp. 2-5]。
- 冷处理温度固定为 -30°C，模拟寒冷地区环境 [Jiang 2023, pp. 2-5]。
- 热处理的最高温度达1000°C，对应深部地热开采可能温度 [Jiang 2023, pp. 2-5]。

## Methods
- **热‑冷循环处理**：试件先干燥（20°C, 48 h），加热至目标温度（升温速率5°C/min），保温4小时后立即置入 -30°C 冻融箱中保持8小时，此为一个循环 [Jiang 2023, pp. 2-5]。
- **三轴渗流试验**：采用流变仪在恒定围压20 MPa下施加5 MPa孔隙水压，以0.01 mm/min轴向位移速率加载，实时监测应力‑应变与渗透率变化，获得全应力‑应变过程中的渗流特性 [Jiang 2023, pp. 2-5]。
- **损伤本构与渗透率模型**：基于统计损伤理论，定义热‑冷循环造成的初始损伤 \( D(T,n) = 1 - \frac{E(T,n)}{E(20°C,0)} \)，结合加载引起的统计损伤，建立耦合损伤变量 \( D_{tol} \)。采用有效应力原理，定义裂隙压缩系数 \( C_f = \gamma D_{tol} \)，导出渗透率模型 \( k = k_0 \exp\left[ -3\gamma D_{tol} \left( 3(\sigma_3 - p_w) + \Delta\sigma - \sigma_{e0} \right) \right] \) [Jiang 2023, pp. 7-9]。
- 模型参数（\( m \), \( K \), \( k_0 \), \( \gamma \) 等）通过拟合应力‑应变试验数据确定，并由实验验证 [Jiang 2023, pp. 9-10]。

## Key Findings
- 峰值应力 \( \sigma_c \) 和弹性模量 \( E \) 均随温度和循环次数增加而下降：以200°C为基准，10次循环后1000°C时 \( \sigma_c \) 下降68.15%，20次循环后下降76.56%；弹性模量相应下降37.72%和31.62%。热损伤是力学参数劣化的主因，循环加剧了矿物颗粒胶结强度的削弱 [Jiang 2023, pp. 6-7]。
- 破坏模式随温度与循环次数由单一主控张拉裂纹转变为多裂纹堆叠的树枝状损伤，表明热‑冷循环改变了岩石内部裂纹扩展与贯通方式 [Jiang 2023, pp. 7-8]。
- 初始渗透率和最大渗透率均随温度和循环次数增加而增大（详见Fig. 5），在渐进破裂过程中渗透率随裂纹扩展而上升 [Jiang 2023, pp. 7-8]。
- 建立的渗透率模型理论曲线与实验曲线吻合良好，能有效表征渗透率与耦合损伤的关系，耦合损伤 \( D_{tol} \) 随应变呈“S”形单调增加，且其增长加速段与渗透率快速上升段对应 [Jiang 2023, pp. 9-11]。
- 不同温度‑循环条件下的耦合损伤演化可用指数型经验公式描述（如：200°C‑10cycles下 \( D_{tol} = 1 - 0.841 \exp(-(\varepsilon/0.0160)^{3.925}) \)）[Jiang 2023, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 峰值应力 \( \sigma_c \) 随温度和循环数下降，1000°C‑10cycles 下降68.15%，20cycles 下降76.56% | [Jiang 2023, pp. 6-7] | 围压20 MPa，孔隙水压5 MPa，200°C为参考 | 热‑冷循环劣化效应显著 |
| 弹性模量 \( E \) 随温度和循环数下降，1000°C‑10cycles 下降37.72%，20cycles 下降31.62% | [Jiang 2023, pp. 6-7] | 同上 | 弹性模量劣化与循环次数及温度正相关 |
| 初始渗透率与最大渗透率均随温度与循环数增加而增大 | [Jiang 2023, pp. 7-8] | 基于Fig. 5趋势描述，具体数值未给出 | 渗透率增大与微裂纹发育有关 |
| 渗透率模型 \( k = k_0 \exp[-3\gamma D_{tol}(3(\sigma_3-p_w)+\Delta\sigma-\sigma_{e0})] \) 与实验数据吻合 | [Jiang 2023, pp. 9-10] | 不同温度与循环条件的14组试验（见表2） | 模型参数 \( m,K,k_0,\gamma \) 由拟合确定 |
| 耦合损伤 \( D_{tol} \) 随应变呈“S”形增长，初始损伤随温度增大，加载后加速趋于1 | [Jiang 2023, pp. 10-11] | 基于Fig.8和各条件经验公式 | 损伤与应变的关系由统计损伤理论导出 |

## Limitations
- 未从索引片段中确认试验是否控制了天然岩石的非均质性，所有结论基于红砂岩这一种岩性。
- 围压恒定在20 MPa，未探讨其他围压条件下模型的适用性。
- 渗流测试仅关注轴向加载过程，未体现卸载或循环荷载下水力耦合的响应。
- 模型参数（\( m, K, \gamma \) 等）依赖特定温度‑循环条件下的试验拟合，未从片段中获得参数物理意义的普适性验证。
- 片段仅描述了宏观力学与渗透率关系，微观结构演化的直接证据（如SEM）未在片段中体现，分析原因多基于推断。

## Assumptions / Conditions
- 岩石被视为各向同性连续体，损伤演化可采用统计损伤理论（Weibull分布）描述 [Jiang 2023, pp. 7-9]。
- 有效应力原理适用，渗透率变化主要受有效应力与损伤引起的裂隙体积变化控制。
- 热‑冷循环造成的初始损伤由弹性模量比定义，且与后续荷载损伤耦合为标量损伤变量 \( D_{tol} \)。
- 所有试验在固定围压20 MPa、孔隙水压5 MPa、室温（未说明具体温度）下进行，未考虑孔隙压变化对有效应力的动态影响。
- 裂隙压缩系数 \( C_f \) 与耦合损伤 \( D_{tol} \) 呈线性关系（\( C_f = \gamma D_{tol} \)），其中 \( \gamma \) 为修正因子。
- 试验采用单一升温速率（5°C/min）和固定的保温/冷却时间，未讨论热惯性或温度梯度的影响。

## Key Variables / Parameters
- \( T \)：加热温度（200, 400, 800, 1000°C）
- \( n \)：热‑冷循环次数（10, 20）
- \( \sigma_c \)：峰值应力
- \( E \)：弹性模量
- \( k_0 \)：初始渗透率
- \( k_{max} \)：最大渗透率
- \( D(T,n) \)：热‑冷循环初始损伤变量
- \( D_{tol} \)：耦合损伤变量
- \( \sigma_3 \)：围压（20 MPa）
- \( p_w \)：孔隙水压（5 MPa）
- \( \Delta\sigma \)：偏应力（\( \sigma_1 - \sigma_3 \)）
- \( \sigma_{e0} \)：峰值有效应力（实验确定）
- \( \gamma \)：裂隙压缩修正因子
- \( m, K \)：统计损伤模型中的Weibull分布参数
- \( C_f \)：裂隙压缩系数

## Reusable Claims
- **热‑冷循环对强度的影响**：在恒定围压20 MPa、孔隙水压5 MPa条件下，红砂岩的峰值应力 \( \sigma_c \) 随处理温度和循环次数增加而单调降低。1000°C时10次循环后强度较200°C降低68.15%，20次循环后降低76.56% [Jiang 2023, pp. 6-7]。该结论适用于快速热‑冷交替且冷端为-30°C的工况。
- **热‑冷循环对弹性模量的影响**：相同温压条件下，弹性模量 \( E \) 同样随温度和循环数递减，1000°C‑10cycles 时较200°C下降37.72%，20cycles下降31.62% [Jiang 2023, pp. 6-7]。可作为热‑冷冲击下刚度劣化的定量参考。
- **渗透率增强规律**：红砂岩的初始渗透率和最大渗透率均随热‑冷循环的温度和次数增加而上升，在加载破坏过程中渗透率与微裂纹扩展正相关 [Jiang 2023, pp. 7-8]。具体数值依赖于条件但整体趋势明确。
- **渗透率‑损伤耦合模型**：表达式 \( k = k_0 \exp[-3\gamma D_{tol} (3(\sigma_3-p_w)+\Delta\sigma-\sigma_{e0})] \) 可较好预测红砂岩在不同热‑冷循环历史和应力状态下的渗透率变化，参数需通过目标温度‑循环组试验拟合获取 [Jiang 2023, pp. 9-10]。
- **耦合损伤演化规律**：耦合损伤 \( D_{tol} \) 随轴向应变呈“S”形增长，且可表示为 \( D_{tol} = 1 - a \exp(-(\varepsilon/b)^c) \) 形式，参数 \( a, b, c \) 随温度和循环条件变化 [Jiang 2023, pp. 10-11]。该经验关系可直接用于类似岩石的损伤评价。

## Candidate Concepts
- [[thermal-cold cycle shock]]
- [[damage variable]]
- [[hydro-mechanical coupling]]
- [[statistical damage theory]]
- [[permeability model]]
- [[red sandstone]]
- [[cyclic thermal treatment]]
- [[fracture compressibility]]
- [[effective stress principle]]
- [[geothermal reservoir damage]]
- [[progressive fracture]]

## Candidate Methods
- [[triaxial seepage test with controlled pore pressure]]
- [[cyclic thermal-cold shock treatment]]
- [[permeability measurement during complete stress-strain curve]]
- [[elastic modulus-based damage definition]]
- [[Weibull distribution-based statistical damage model]]
- [[coupling damage variable construction]]
- [[parameter fitting for permeability-damage relation]]

## Connections To Other Work
- 文中指出 Wang et al. (2021) 的水力耦合试验证实渗透率在弹性阶段变化不大，在峰值应力处急剧上升，本研究观察到了类似阶段特征 [Jiang 2023, pp. 2]。
- Liu et al. (2020) 开展了砂岩的热‑水‑力耦合渗透试验并获取了渗透率‑温度‑损伤关系，本研究在此基础上进一步引入冷循环效应 [Jiang 2023, pp. 2]。
- 对于热循环后花岗岩的渗透率与力学特性，Gautam et al. (2020) 研究了250°C循环的影响，本研究则覆盖了更高温度和红砂岩 [Jiang 2023, pp. 2]。
- Guo et al. (2020) 提出了热‑水‑力‑损伤耦合模型并试验验证，本研究提出的模型同样采用损伤‑渗透率耦合思路，但损伤定义和方程形式不同 [Jiang 2023, pp. 2]。
- 从主题上，本研究可与 [[fracture reservoir]]、[[cold region geothermal engineering]]、[[thermal shock on rocks]] 等领域建立联系，但其具体对比未在片段中细化。

## Open Questions
- 该渗透率模型在其他岩石类型（如花岗岩、石灰岩）或更复杂应力路径下的适用性如何？未从索引片段中确认。
- 热‑冷循环中冷却速率（此处为炉冷至-30°C）和冻融持续时间的变化对损伤和渗透率的影响未在片段中探讨。
- 片段仅给出模型验证的部分数据，模型对渗透率恢复或卸载过程的描述能力未提及。
- 微观机制（如矿物颗粒热膨胀系数差异、微裂纹密度量化）与宏观损伤的定量联系尚未在片段中揭示。
- 长期多次循环（>20次）的损伤累积规律是否仍符合现有模型？未从索引片段中确认。

## Source Coverage
本页依据提供论文索引的**11个片段**编写，覆盖了摘要、引言部分、实验设计（2.2节）和主要结果（3.2、3.3、4节）的主要内容。片段包含了实验流程、部分力学数据对比、渗透率变化趋势以及模型构建与验证的公式和参数表。然而，以下信息明显缺失：完整的应力‑应变曲线数值、不同循环下的具体渗透率数值（仅提供变化趋势和少量点）、微观分析的直接证据（如CT或SEM）、讨论部分对工程应用的深入阐述、结论段落的完整表述。因此，本页对机理的解释多基于片段中的推理，未包含论文的全部细节。
