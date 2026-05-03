---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-xu-peak-shear-strength-of-compacted-gmz-bentonites-in-saline-solution"
title: "Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution."
status: "draft"
source_pdf: "data/papers/2019 - Peak shear strength of compacted GMZ bentonites in saline solution.pdf"
collections:
  - "审稿人让引用"
citation: "Xu, Yongfu. \"Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution.\" *Engineering Geology*, 2019, doi:10.1016/j.enggeo.2019.02.009. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42393"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:45:54"
---

# Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution.

## One-line Summary
修正有效应力概念（考虑渗透吸力的分形模型）能够统一描述不同浓度NaCl溶液中压实GMZ膨润土的峰值剪切强度，所有数据在Mohr-Coulomb准则下落在同一直线上。[Xu 2019, pp. 1-1]

## Research Question
如何利用考虑渗透吸力的修正有效应力概念，准确表征和预测压实GMZ膨润土在盐水溶液中的峰值剪切强度行为？[Xu 2019, pp. 1-1]

## Study Area / Data
- **材料**：GMZ07膨润土（主要含蒙脱石，伴生石英、斜长石和长石）及福建标准砂。[Xu 2019, pp. 4-5]
- **表面分形维数**：GMZ07膨润土 Ds = 2.78，由氮吸附等温线测定。[Xu 2019, pp. 5-6]
- **试样参数**：压实GMZ07膨润土及其与砂的1:1混合物，干密度分别约为1.5 g/cm³ 和1.45 g/cm³，直径5 cm，厚度1.5 cm。[Xu 2019, pp. 5-6]
- **试验流体**：蒸馏水和NaCl溶液（浓度 0、0.2、0.5、1.0、2.0 mol/L）。[Xu 2019, pp. 5-6]
- **剪切条件**：剪切速率 0.01 mm/min，不排水条件。[Xu 2019, pp. 5-6]

## Methods
- **不排水直剪试验**：对饱和试样在不同垂直压力下进行剪切。[Xu 2019, pp. 1-1][Xu 2019, pp. 5-6]
- **修正有效应力**：采用公式 p’ = p + π(p/π)^(Ds-2)，其中 p 为法向应力，π 为渗透吸力，Ds 为表面分形维数。该公式基于膨润土表面分形模型推导。[Xu 2019, pp. 1-1]
- **渗透吸力计算**：π 通过 van’t Hoff 方程 π = ν R T m φ 确定，其中 ν 为层间阳离子价态，R = 8.31 J/(mol·K)，T = 293 K，m 为摩尔浓度，φ 为渗透系数（根据 Lang (1967) 方法计算）。[Xu 2019, pp. 3-4]
- **分形维数测定**：氮吸附等温线法，按 Avnir 和 Jaroniec (1989) 的方法，利用 ln(V_ads) 与 ln(P0/P) 的线性关系求解 Ds（P/P0 = 0.01–0.99，R² > 0.99）。[Xu 2019, pp. 5-6]
- **强度准则**：Mohr-Coulomb 准则 τ_f = c’ + p’ tan φ’，以修正有效应力 p’ 为自变量进行分析。[Xu 2019, pp. 1-1]

## Key Findings
1. 若直接使用总应力分析，GMZ07膨润土及1:1混合物的内摩擦角随NaCl溶液浓度增大而假性增大，且高浓度、高法向应力下数据偏离Mohr-Coulomb准则。[Xu 2019, pp. 6-7]
2. 采用修正有效应力 p’ 后，所有直剪试验数据（蒸馏水及0–2.0 mol/L NaCl溶液）在 τ_f – p’ 平面上汇聚于同一直线，严格满足Mohr-Coulomb准则，峰值摩擦角和黏聚力与溶液浓度无关。[Xu 2019, pp. 1-1][Xu 2019, pp. 6-7]
3. 统一的有效内摩擦角：GMZ07纯膨润土为4.8°，1:1膨润土-砂混合物为9.4°，均落在蒙脱石典型内摩擦角范围（4°–20°，Mitchell and Soga, 2005）之内。[Xu 2019, pp. 6-7]
4. 1:1混合物在高法向应力（>1600 kPa）下偏离统一直线，归因于砂颗粒直接接触并主导了摩擦特性。[Xu 2019, pp. 6-7]
5. 修正有效应力概念能够准确表征盐水溶液对压实膨润土峰值强度的影响，提供了统一的分析框架。[Xu 2019, pp. 1-1]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 峰值剪切强度在 τ_f-p’ 平面上可统一表述，与溶液浓度无关 | [Xu 2019, pp. 1-1] | 蒸馏水及0–2.0 mol/L NaCl，不排水直剪 | 修正有效应力包含渗透吸力与表面分形维数 |
| GMZ07膨润土表面分形维数 Ds = 2.78 | [Xu 2019, pp. 5-6] | 氮吸附法，P/P0 0.01–0.99，R²>0.99 | 用于修正有效应力计算 |
| 统一内摩擦角：膨润土 φ’=4.8°，混合 φ’=9.4° | [Xu 2019, pp. 6-7] | 修正有效应力分析，所有浓度数据 | 符合蒙脱石内摩擦角范围（4–20°, Mitchell and Soga 2005） |
| 高法向应力（>1600 kPa）下1:1混合物偏离Mohr-Coulomb准则 | [Xu 2019, pp. 6-7] | 高浓度NaCl，高应力 | 归因于砂粒直接接触 |
| 渗透吸力 π 由 van’t Hoff 方程 π = ν R T m φ 确定 | [Xu 2019, pp. 3-4] | T=293 K，ν根据层间阳离子价态，φ由公式(5)计算 | 取决于溶液浓度和温度 |

## Limitations
- 分析仅限于峰值剪切强度，未涉及残余强度或峰后软化行为。[Xu 2019, pp. 1-1] [未从索引片段中确认]
- 试验仅针对GMZ07膨润土和一种砂配比（1:1），其他类型膨润土、不同混合比或不同盐类溶液的适用性未验证。[未从索引片段中确认]
- 修正有效应力概念的有效性局限于恒定化学条件、恒定体积（或恒定应变率）及恒定温度（参照 Graham et al. 1992 的适用范围）。[Xu 2019, pp. 2-3]
- 1:1混合物在高应力下偏离统一直线，表明当砂骨架成为荷载主要承担者时，统一准则失效。[Xu 2019, pp. 6-7]
- 试验所用法向应力的具体上限及低压范围的充分性未在索引片段中完全确认。[未从索引片段中确认]

## Assumptions / Conditions
- 膨润土表面具备分形特性，表面分形维数 Ds 可度量表面粗糙度，并控制吸附水体积与应力的关系。[Xu 2019, pp. 3-4]
- 修正有效应力 p’ = p + π(p/π)^(Ds-2) 可将力学作用与渗透吸力效应统一描述，该表达由分形模型导出。[Xu 2019, pp. 1-1][Xu 2019, pp. 4-5]
- 试样在剪切前已充分饱和（溶液注入10小时），膨胀达到稳定。[Xu 2019, pp. 5-6]
- 直剪过程维持不排水条件，孔隙流体化学组成视为恒定。[Xu 2019, pp. 1-1]
- Mohr-Coulomb 准则适用于描述峰值强度，且修正有效应力下的 c’ 和 φ’ 为与溶液浓度无关的材料常数。[Xu 2019, pp. 1-1]
- 渗透吸力按理想稀溶液的 van’t Hoff 方程计算，渗透系数 φ 依据 Lang (1967) 的关系式确定。[Xu 2019, pp. 3-4]

## Key Variables / Parameters
- **p’**：修正有效应力（kPa）[Xu 2019, pp. 1-1]
- **p**：法向总应力（kPa）[Xu 2019, pp. 1-1]
- **π**：渗透吸力（kPa），由溶液浓度和温度决定 [Xu 2019, pp. 3-4]
- **Ds**：表面分形维数（无量纲），GMZ07 = 2.78 [Xu 2019, pp. 5-6]
- **τ_f**：峰值剪切强度（kPa）[Xu 2019, pp. 1-1]
- **c’**：有效黏聚力（kPa）[Xu 2019, pp. 1-1]
- **φ’**：有效内摩擦角（°）[Xu 2019, pp. 1-1]
- **ν**：层间阳离子价态 [Xu 2019, pp. 3-4]
- **R**：通用气体常数，8.31 J/(mol·K) [Xu 2019, pp. 3-4]
- **T**：绝对温度，293 K [Xu 2019, pp. 3-4]
- **m**：NaCl溶液摩尔浓度（mol/L）[Xu 2019, pp. 3-4]
- **φ**：渗透系数 [Xu 2019, pp. 3-4]
- **干密度**：1.5 g/cm³（膨润土）、1.45 g/cm³（混合）[Xu 2019, pp. 5-6]
- **剪切速率**：0.01 mm/min [Xu 2019, pp. 5-6]

## Reusable Claims
1. **Claim:** 压实GMZ膨润土在蒸馏水和不同浓度NaCl溶液（0–2.0 mol/L）中的峰值剪切强度，可由统一的修正有效应力 p’ = p + π(p/π)^(Ds-2) 结合 Mohr-Coulomb 准则描述；在此框架下，有效内摩擦角和黏聚力是与溶液浓度无关的常数。[Xu 2019, pp. 1-1][Xu 2019, pp. 6-7]  
   - **Conditions:** 不排水直剪条件；干密度约1.5 g/cm³（纯膨润土）；法向应力范围避免砂骨架接触占主导（对于混合物需注意应力上限）。需已知材料的表面分形维数 Ds。  
   - **Evidence:** 所有试验点在 τ_f–p’ 平面上落在同一直线，获得统一的强度参数（膨润土 φ’=4.8°，混合 φ’=9.4°）。[Xu 2019, pp. 6-7]  
   - **Limitations:** 对于砂-膨润土混合物，当法向应力超过约1600 kPa时，砂粒直接接触导致统一关系失效；理论基础要求恒定化学组成和温度条件。未验证是否适用于其他盐类或多价阳离子溶液。

2. **Claim:** 膨润土的表面分形维数 Ds 可通过氮吸附等温线在相对压力 P/P0 = 0.01–0.99 范围内可靠测定，GMZ07的 Ds 为2.78。[Xu 2019, pp. 5-6]  
   - **Conditions:** 使用 ASAP 2010 M+C 分析仪，77 K，样品105 °C脱气12小时。适用于粉末状GMZ膨润土。  
   - **Evidence:** 线性拟合优度 R² > 0.99。[Xu 2019, pp. 5-6]  
   - **Limitations:** Ds 值可能受样品预处理和吸附质种类影响；不同来源膨润土需单独标定。

3. **Claim:** 盐水溶液浓度增加会导致按总应力分析的内摩擦角假性增大，这种表观变化源于渗透吸力的贡献；采用修正有效应力后可消除此效应，还原真实的强度参数。[Xu 2019, pp. 6-7]  
   - **Conditions:** 适用于GMZ膨润土及1:1砂-膨润土混合物，NaCl浓度0–2.0 mol/L，法向应力不超过混合物出现砂骨架主导的阈值。  
   - **Evidence:** 总应力下内摩擦角随浓度变化，修正有效应力下所有数据归一于同一直线。[Xu 2019, pp. 6-7]  
   - **Limitations:** 未从索引片段确认是否适用于其他电解液体系；需要知道材料的 Ds 和溶液渗透吸力。

## Candidate Concepts
- [[modified effective stress]]
- [[osmotic suction]]
- [[surface fractal dimension]]
- [[Mohr-Coulomb criterion]]
- [[peak shear strength]]
- [[compacted bentonite]]
- [[GMZ bentonite]]
- [[high-level nuclear waste repository]]
- [[diffuse double layer]]
- [[interparticle forces]]

## Candidate Methods
- [[undrained direct shear test]]
- [[nitrogen adsorption isotherm for fractal dimension]]
- [[van’t Hoff equation for osmotic suction]]
- [[fractal model for bentonite surface]]
- [[oedometer saturation and shear transfer procedure]]

## Connections To Other Work
- **Mokni et al. (2014)** 使用单一本构应力描述剪切强度，得到唯一线性破坏包线，与本研究的统一修正有效应力思路一致。[Xu 2019, pp. 2-3]
- **Graham et al. (1992)** 指出有效应力概念可在恒定化学、体积（或恒定应变率）和温度条件下描述压实黏土的力学行为，为本文设定限制条件提供了理论背景。[Xu 2019, pp. 2-3]
- **Sridharan and Prakash (1999)** 对蒙脱土不排水强度机制的解释（双电层水的粘性剪切阻力）与本文研究对象GMZ膨润土高度相关。[Xu 2019, pp. 2-3]
- **Barbour and Fredlund (1989)** 提出的渗透固结概念涉及颗粒间净斥力‑引力变化，可在机理上联系到修正有效应力中的渗透吸力贡献。[Xu 2019, pp. 2-3]
- **Tiwari and Ajmera (2015)** 和 **Di Maio and Scaringi (2016)** 的研究分别揭示了孔隙溶液浓度变化对黏土强度及边坡稳定性的显著影响，支持了本研究的研究动机，但未建立直接定量联系。[Xu 2019, pp. 1-2]
- 与 **Rao and Thyagaraj (2007)** 的净竖向应力表达式以及 **Zhang et al. (2016a)** 的体积变化研究，在片段中仅作为背景文献提及，未显示直接对比或定量改进。[Xu 2019, pp. 1-2][Xu 2019, pp. 2-3]

## Open Questions
- 修正有效应力方法在循环荷载、蠕变或高温等核废料处置库复杂工况下的适用性如何？[未从索引片段中确认]
- 该方法是否适用于其它盐类（如CaCl₂）或多组分地下盐水，能否同样使用分形修正有效应力框架实现归一化？[未从索引片段中确认]
- 残余强度或峰后软化行为能否沿用此统一准则？[未从索引片段中确认]
- 表面分形维数 Ds 是否随干密度、初始含水率或制样工艺变化，进而影响统一强度线的唯一性？[未从索引片段中确认]
- 对于砂‑膨润土混合物，导致统一准则失效的砂含量界限和应力水平缺乏系统界定。[未从索引片段中确认]

## Source Coverage
本页依据该论文的9个索引片段编写，主要覆盖了摘要、部分引言、模型推导（分形与渗透吸力）、材料与方法、主要结果和结论。缺少完整的引言文献回顾、所有试验数据图表（如膨胀曲线、吸附等温线图、直剪曲线）、详细的公式推导过程以及微观机理讨论。修正有效应力公式(12)的具体形式在片段中不完整，仅从摘要和结论确认了最终表达式。试验的统计变异性、平行试样数量等信息未从索引片段中获得。
