---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-xi-experimental-comparison-of-mechanical-properties-and-fractal-characteristics-of-geotherm"
title: "Experimental Comparison of Mechanical Properties and Fractal Characteristics of Geothermal Reservoir Rocks after Different Cooling Treatments."
status: "draft"
source_pdf: "data/papers/2022 - Experimental comparison of mechanical properties and fractal characteristics of geothermal reservoir rocks after different cooling treatments.pdf"
collections:
  - "part2"
  - "zotero new"
  - "论文"
citation: "Xi, Yan, et al. \"Experimental Comparison of Mechanical Properties and Fractal Characteristics of Geothermal Reservoir Rocks after Different Cooling Treatments.\" *Energy Reports*, vol. 8, 2022, pp. 5158-76. *ScienceDirect*, doi:10.1016/j.egyr.2022.03.207. Accessed 2026."
indexed_texts: "14"
indexed_chars: "68652"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:25:36"
---

# Experimental Comparison of Mechanical Properties and Fractal Characteristics of Geothermal Reservoir Rocks after Different Cooling Treatments.

## One-line Summary
通过对砂岩和花岗岩进行400–800°C加热后采用自然冷却、水冷、液氮(LN₂)冷却，结合SHPB动态冲击、超声波检测、SEM和分形分析，揭示了冷却方式和温度对地热储层岩石动力学特性与破碎特征的差异化影响规律。

## Research Question
地热钻井中，高温储层岩石与冷却介质（如钻井液）热交换引起的热冲击如何改变岩石动态力学性质？不同冷却方式（自然冷却、水冷、液氮冷却）在不同加热温度下对砂岩和花岗岩的力学劣化、微裂纹扩展及碎片分布有何差别？能否通过分形方法量化这种热‑力耦合损伤？[Xi 2022, pp. 1-1]

## Study Area / Data
研究对象为地热井主要储层基质的**砂岩**和**花岗岩**，加工成标准试样。通过CT扫描测得砂岩孔隙度为5.83%，花岗岩为0.14%，砂岩孔隙分布特征显著且均匀，花岗岩组分结合紧密、微孔隙极少且不均[Xi 2022, pp. 3-4]。实验数据覆盖：
- 加热温度：25°C（对照）、400°C、600°C、800°C。
- 冷却方式：自然冷却（空气中12 h）、水冷（浸没1 h）、液氮(LN₂)冷却（浸没1 h）。
- 冲击条件：SHPB冲击速度控制在10.35 m/s–10.48 m/s。
- 测试项目：超声波P波速度、动态应力‑应变曲线、弹性模量、SEM微裂纹形貌、碎片分形分布。具体地理来源未从索引片段中确认。

## Methods
- **加热与冷却处理**：马弗炉加热，升温速率2.5°C/min以避免剧烈温度梯度，达到目标温度后恒温2 h使试样内外温度均匀；然后分别采用自然冷却、水冷和LN₂冷却[Xi 2022, pp. 4-6]。
- **超声波波速测试**：利用超声波检测仪测量P波速度，以间接表征力学性质变化和微裂纹发育[Xi 2022, pp. 6-8]。
- **SHPB动态实验**：采用分离式Hopkinson压杆进行冲击，基于一维波传播理论计算动态应力‑应变，并通过入射、反射和透射波验证应力平衡，公式(1)用于参数计算[Xi 2022, pp. 4-6]。  
  \[
  \begin{aligned}
  \sigma(t) &= \frac{A}{2A_S}E(\varepsilon_I + \varepsilon_R + \varepsilon_T)\\
  \varepsilon(t) &= \frac{C}{L_s}\int_0^t(\varepsilon_I - \varepsilon_R - \varepsilon_T)dt\\
  \dot{\varepsilon}(t) &= \frac{C}{L_s}(\varepsilon_I - \varepsilon_R - \varepsilon_T)
  \end{aligned}
  \]
- **SEM观察**：SHPB实验后从每个试样取4块碎片，用Hitachi SU8010冷场发射扫描电镜观察裂纹形貌，平均以减少不均匀性误差[Xi 2022, pp. 4-6]。
- **分形分析**：对碎片分布进行分形量化，建立分形维数与温度和冷却方式的对应关系[Xi 2022, pp. 1-1]。

## Key Findings
1. **P波速度与弹性模量劣化**  
   - 同一冷却方式下，砂岩和花岗岩的P波速度随加热温度升高而降低；600°C时三种冷却方式下花岗岩波速下降约60%，砂岩约40%，花岗岩对热处理更敏感[Xi 2022, pp. 6-8]。  
   - 水冷使砂岩波速下降幅度大于自然冷却；LN₂对花岗岩波速劣化最显著，例如800°C时LN₂冷却导致的花岗岩波速衰减率高于水冷和自然冷却[Xi 2022, pp. 6-8]。  
   - 弹性模量（基于P波模量公式(2)）随温度升高而降低；砂岩在400°C时水冷影响最大；花岗岩在600°C时液氮影响最大，800°C时三种冷却方式差异极小[Xi 2022, pp. 8-10]。

2. **动态应力‑应变响应**  
   - 加热温度升高导致动态峰值应力下降、峰值应变增大[Xi 2022, pp. 8-10]。  
   - 砂岩在800°C时，自然冷却、LN₂、水冷后的峰值强度分别为96.1 MPa、85.2 MPa、73.3 MPa，水冷劣化作用最强[Xi 2022, pp. 8-10]。  
   - 花岗岩在800°C时，液氮和水冷造成的强度衰减基本相同（均为155.1 MPa），均显著大于自然冷却的132.2 MPa[Xi 2022, pp. 10-10]。

3. **温度与冷却方法敏感性差异**  
   - 低于400°C时砂岩对温度的敏感性高于花岗岩；高于400°C时花岗岩的温度敏感性急剧增加[Xi 2022, pp. 10-10]。  
   - 砂岩对冷却方式的敏感性整体强于花岗岩，且随温度升高差异增大[Xi 2022, pp. 10-10]。  
   - 砂岩的动态抗压强度随加热温度呈近似线性下降，而花岗岩的下降趋势不同[Xi 2022, pp. 10-10]。

4. **微观裂纹特征**  
   - SEM显示：800°C处理后，花岗岩中液氮冷却产生的微裂纹最显著，而砂岩中水冷却导致的裂纹最明显，表明热损伤受岩石基质和冷却介质特性共同影响[Xi 2022, pp. 6-8]。

5. **分形与碎片分布**  
   - 采用分形方法分析碎片得到分形维数与热处理温度和冷却方式的对应关系，可反映热‑力耦合破碎程度；具体分形维数的数值和变化曲线未从索引片段中确认[Xi 2022, pp. 1-1]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 600°C时花岗岩P波速度降低约60%，砂岩降低约40%（三种冷却方式下） | Xi 2022, pp. 6-8 | 加热至600°C，自然、水、LN₂冷却，室温对照25°C | 表明花岗岩内部结构损伤更严重 |
| 800°C砂岩水冷后动态峰值强度73.3 MPa，明显低于自然冷却的96.1 MPa和LN₂的85.2 MPa | Xi 2022, pp. 8-10 | 冲击速度~10.4 m/s | 水冷对砂岩强度劣化最显著 |
| 花岗岩800°C下液氮和水冷的抗压强度均为155.1 MPa，自然冷却为132.2 MPa | Xi 2022, pp. 10-10 | 同上冲击条件 | 快速冷却对花岗岩影响大于慢速 |
| 加热温度超过400°C后花岗岩温度敏感性显著增加 | Xi 2022, pp. 10-10 | 实验室热-力条件 | 用于解释强度突降 |
| 砂岩冷却方式敏感性高于花岗岩，且差异随温度增大 | Xi 2022, pp. 10-10 | 多组实验比较 | 指导钻井冷却策略的选择 |
| LN₂冷却在花岗岩中产生最显著裂纹，水冷在砂岩中裂纹最明显（800°C处理后） | Xi 2022, pp. 6-8 | SEM观察，取四块碎片平均 | 微观裂纹与冷却介质及岩石类型直接相关 |
| 分形方法可量化碎片分布与处理条件的关系 | Xi 2022, pp. 1-1 | 碎片分形分析 | 具体分形维数缺失 |

## Limitations
- 研究基于小尺寸实验室试样，未考虑原岩应力和钻井液循环的真实多场耦合环境，结论向工程尺度的外推需要谨慎。
- 仅对比了三种冷却方式，未涉及其他常见冷却介质（如不同组分的钻井液）。
- 分形分析的详细结果（分形维数具体数值及变化规律）在索引片段中未给出，无法评估其可量化性和灵敏度。
- 冲击速度未做系统的参数变化研究，动态破裂的速率效应未被充分揭示。
- 实验加热过程采用恒定升温速率，与井下非稳态温度场存在差异。

## Assumptions / Conditions
- 2.5°C/min升温速率及保温2 h足够保证试样内外温度均匀，热梯度引起的附加损伤可忽略 [Xi 2022, pp. 4-6]。
- SHPB测试满足一维波传播条件，且通过入射-反射-透射波对比验证了动态应力平衡 [Xi 2022, pp. 4-6]。
- 同一批次冲击速度控制在10.35–10.48 m/s，近似认为加载速率恒定。
- SEM观察时从每个工况取4块碎片并平均，以消除岩石非均质性的影响 [Xi 2022, pp. 4-6]。
- 自然冷却12小时、水冷和LN₂浸没1小时被视作充分的冷却过程，试样终态温度假定与环境一致。
- 岩石在加热过程中未发生明显化学相变（如石英相变温度573°C可能的影响在讨论中隐含，但索引片段未深入分析）。

## Key Variables / Parameters
- **自变量（控制因素）**：加热温度(25, 400, 600, 800°C)，冷却方式(自然、水、LN₂)，岩石类型(砂岩、花岗岩)。
- **因变量（测量指标）**：P波速度，动态峰值应力/应变，弹性模量(P波模量)，微裂纹形貌特征，分形维数。
- **关键固定参数**：冲击速度10.35–10.48 m/s，加热速率2.5°C/min，保温时间2 h，冷却时间（水/LN₂ 1 h，自然12 h）。
- **重要公式**：SHPB应力‑应变计算公式(1)；P波模量 \( E_{P-wave} = \rho C^2 \) (公式2)。

## Reusable Claims
1. **砂岩动态强度水冷劣化最大**：在加热到800°C并以水冷处理后，砂岩的SHPB动态抗压强度显著低于液氮和自然冷却（73.3 MPa vs 85.2 和96.1 MPa），说明在水基钻井液环境下，高温砂岩的快速热交换能有效降低破碎阻力 [Xi 2022, pp. 8-10]。  
   *适用条件*：砂岩储层，井底温度可达800°C，冲击加载速率与实验相近（~10.4 m/s）。  
   *限制*：仅实验室尺度；未考虑围压、孔隙流体压力及化学作用。

2. **花岗岩对液氮冷却裂纹响应突出**：SEM表明800°C花岗岩经液氮冷却后微裂纹最密集，动态强度衰减与快速水冷相当，但自然冷却衰减较小 [Xi 2022, pp. 6-8, 10-10]。  
   *适用条件*：低孔隙度花岗岩，LN₂作为冷却介质辅助破碎；冲击加载条件类似。  
   *限制*：裂纹定量参数仅限于形貌特性，未关联渗透率变化。

3. **温度敏感性转折**：在400°C以下，砂岩温度敏感性高于花岗岩；超过400°C后花岗岩敏感性急剧增加，这可在钻井参数优化时作为岩石类型和温区划分的依据 [Xi 2022, pp. 10-10]。  
   *适用条件*：热‑力耦合条件类似，单调升温至目标温度后冷却。  
   *限制*：岩性单一（仅两种岩石），野外热力历史复杂，需考虑多次循环。

4. **P波速度可作为热损伤快速评价指标**：砂岩和花岗岩的P波速度衰减幅度与温度正相关，且与力学强度变化趋势一致，尤其花岗岩在600°C时速度衰减达60% [Xi 2022, pp. 6-8]。  
   *适用条件*：同种岩性、相同冷却路径。  
   *限制*：速度衰减仅间接反映微裂纹，不同孔隙构造可能造成非线性关系。

## Candidate Concepts
- [[geothermal reservoir rock]]
- [[thermal shock damage]]
- [[dynamic compressive strength]]
- [[fractal dimension]]
- [[split Hopkinson pressure bar (SHPB)]]
- [[P-wave velocity]] as thermal damage indicator
- [[microcrack morphology]]
- [[cooling rate effect]]
- [[temperature sensitivity of rock mechanics]]
- [[rock breaking efficiency in drilling]]

## Candidate Methods
- [[split Hopkinson pressure bar (SHPB) test]]
- [[ultrasonic velocity measurement]]
- [[scanning electron microscope (SEM)]]
- [[fractal analysis of fragmentation]]
- [[thermal treatment and controlled cooling]]
- [[P-wave modulus evaluation]]

## Connections To Other Work
- 本研究与高温岩石冷却后力学性质劣化的已有工作一致：前人发现加热温度升高导致P波速度、单轴抗压强度和弹性模量下降（如Xu and Karakus, 2018）[转引自 Xi 2022, pp. 1-2]。
- 在动态特性方面，本文引述的前人研究表明冷却速率对岩石动态损伤有显著影响，冷却速率越大损伤越严重（Shabelansky et al., 2014; Zhang et al., 2018a,b; Blanco‑Martín et al., 2018）[转引自 Xi 2022, pp. 2-3]。
- 与前人工作相比，本文首次系统对比了自然、水和液氮三种冷却对砂岩和花岗岩的动态响应与分形破碎特征，并提出了温度敏感性转折点，可与 [[thermal shock assisted rock breaking]] 和 [[geothermal drilling optimization]] 的概念相结合。

## Open Questions
- 分形维数随温度和冷却方式的具体变化规律未从索引片段中确认，能否用该参数定量预测破岩效率有待验证。
- 实际钻井中的多场耦合（围压、孔隙压力、钻井液循环）和冲击速率变化如何影响热‑力损伤尚不明确。
- 多次热循环和不同冷却介质（如混合钻井液）的作用未涉及。
- 微裂纹密度、连通性与渗透率、热导率演化的定量关系尚未深入分析。
- 大于800°C的超高温及接近0°C的极冷工况对岩石力学和破碎的影响有待研究。

## Source Coverage
本页依据论文索引中提供的8个片段（覆盖第1至10页），包括摘要、引言、实验过程、部分结果（超声波、SHPB力学特性、SEM形貌）以及讨论开头的前几段。覆盖重点偏向方法描述、基本力学参数和温度‑冷却方式的比较结论；碎片分形特征的**定量数据**和深入的动态破碎机制讨论未在片段中出现。因此，分形维数数值、更复杂的损伤演化模型、结论全文以及参考文献列表等关键信息暂缺，可能影响对完整实验证据链条的判断。
