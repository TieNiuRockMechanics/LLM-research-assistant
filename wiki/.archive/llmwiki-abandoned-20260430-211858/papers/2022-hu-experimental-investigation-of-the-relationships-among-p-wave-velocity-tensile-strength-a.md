---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-hu-experimental-investigation-of-the-relationships-among-p-wave-velocity-tensile-strength-a"
title: "Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment."
status: "draft"
source_pdf: "data/papers/2022 - Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.pdf"
collections:
  - "靳一作以外的"
citation: "Hu, Yuefei, et al. \"Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.\" *Natural Resources Research*, vol. 31, no. 2, 2022. doi:10.1007/s11053-022-10020-3. Accessed 2026."
indexed_texts: "12"
indexed_chars: "58576"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:21:21"
---

# Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.

## One-line Summary
本研究通过实验分析了高温（最高600°C）处理后花岗岩的P波速度、抗拉强度和I型断裂韧性之间的定量关系，并提出了基于P波速度的损伤因子和一个新的岩石脆性指标 [Hu 2022, pp. 1-2]。

## Research Question
花岗岩在经过不同高温处理后，其物理参数（P波速度）与力学参数（抗拉强度、I型断裂韧性）之间存在怎样的定量关系，以及如何利用无损检测技术评估热损伤程度？[Hu 2022, pp. 1-2]

## Study Area / Data
- **岩石类型**：花岗岩 [Hu 2022, pp. 1-2]。
- **试样制备**：将花岗岩加工成巴西圆盘和半圆弯曲（SCB）试样用于力学测试 [Hu 2022, pp. 3-5]。
- **温度处理**：共设置6个热处理温度组（100, 200, 300, 400, 500, 600 °C）和一个室温对照组（20 °C）。试样以2 °C/min速率加热，恒温2小时后在炉内自然冷却至室温 [Hu 2022, pp. 3-5]。

## Methods
- **物理性质测量**：在热处理前后，测量试样的质量和P波速度。质量使用精度0.01g的电子天平测量；P波速度使用NM-4B非金属超声波检测分析仪测量，每个试样测三次取平均值 [Hu 2022, pp. 3-5]。
- **力学性质测试**：
    - **抗拉强度测试**：通过巴西劈裂试验进行，加载速率控制为0.002 mm/s。依据ISRM建议公式 `σt = 2P_max / (πDt)` 计算 [Hu 2022, pp. 3-5]。
    - **I型断裂韧性测试**：通过半圆弯曲（SCB）试验进行，加载速率控制为0.002 mm/s。依据公式 `K_IC = (P_max * sqrt(πa)) / (2RB) * Y'` 计算，其中Y'为无量纲应力强度因子 [Hu 2022, pp. 3-5]。
- **数据分析**：定义并计算了热损伤因子（`D_v1`, `D_v2`），以及抗拉强度与断裂韧性的比率 `α` 作为脆性衡量指标 [Hu 2022, pp. 10-13]。

## Key Findings
- **温度对物理/力学性质的影响**：随温度升高，花岗岩的质量、P波速度（`vp`）和抗拉强度（`σt`）逐渐下降。I型断裂韧性（`K_IC`）从室温（20 °C）至100 °C略有增加，超过100 °C后逐渐下降 [Hu 2022, pp. 1-2]。从20 °C到600 °C，P波速度从4356 m/s降至1053 m/s，降幅达75.8% [Hu 2022, pp. 5-6]。
- **P波速度与力学性质的关系**：高温处理后，花岗岩的 `vp` 与 `σt` 和 `K_IC` 均表现出强正线性关系 [Hu 2022, pp. 12-13]。拟合公式为 `σt = 1.436 + 1.228 * vp` (R²=0.980) 和 `K_IC = -0.175 + 0.500 * vp` (R²=0.924) [Hu 2022, pp. 12-13]。
- **脆性指标（α）**：定义了比率 `α = σt / K_IC`。`α` 值随温度升高而增加，与温度呈指数关系。在室温至400 °C区间变化微小（最小值3.108出现在100 °C），超过400 °C后迅速增大，在600 °C时达到9.065 [Hu 2022, pp. 9-10]。`α` 可作为衡量岩石脆性的指标，其增大表明岩石脆性减弱、延性增强 [Hu 2022, pp. 10-12]。
- **损伤因子**：基于P波速度的热损伤因子（`D_v1`, `D_v2`）能够很好地表征400 °C以下和400 °C以上花岗岩力学性能的退化 [Hu 2022, pp. 1-2, 12-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| `vp` 从室温的4356 m/s降至600 °C的1053 m/s | [Hu 2022, pp. 5-6] | 花岗岩，加热速率2 °C/min，恒温2h，炉内自然冷却 | 降幅75.8%。数据见表3。 |
| `K_IC` 从20 °C的1.75 MPa·m^1/2增至100 °C的2.03，随后单调下降至600 °C的0.31 | [Hu 2022, pp. 5-6] | 花岗岩，加热速率2 °C/min，恒温2h，炉内自然冷却 | 数据见表3。 |
| `σt` 从20 °C的6.52 MPa单调下降至600 °C的2.81 MPa | [Hu 2022, pp. 5-6] | 花岗岩，加热速率2 °C/min，恒温2h，炉内自然冷却 | 数据见表3。 |
| `σt` 与 `vp` 的线性拟合关系式 `σt = 1.436 + 1.228 vp` (R²=0.980) | [Hu 2022, pp. 12-13] | 室温至600 °C热处理后 | 拟合优度很高。 |
| `K_IC` 与 `vp` 的线性拟合关系式 `K_IC = -0.175 + 0.500 vp` (R²=0.924) | [Hu 2022, pp. 12-13] | 室温至600 °C热处理后 | 拟合优度很高。 |
| `α` (`σt/K_IC`) 值与温度的指数关系式 `α = 3.403 + 0.010 exp(0.011T)` (R²=0.987) | [Hu 2022, pp. 9-10] | 整个试验温度范围20-600 °C | `α` 从约3.1增至9.065。 |
| 温度超过400 °C时，`α` 值迅速增加；400 °C时试样中出现明显热微裂纹 | [Hu 2022, pp. 6-10] | 花岗岩 | 微观结构损伤与宏观脆性指标变化一致。 |

## Limitations
- 该研究仅限于一种特定花岗岩，结论对其他岩性的普适性需进一步验证 [Hu 2022, pp. 1-2]。
- 加热路径为缓慢加热和自然冷却，研究结论不适用于有热冲击（如快速冷却）的场景 [Hu 2022, pp. 5-6]。
- `α` 作为脆性指标的提出是基于单一岩石类型的实验结果，其在更广泛岩石中的适用性 [Hu 2022, pp. 10-12] 未从索引片段中确认。
- 最高试验温度为600 °C，更高温度下的关系未从索引片段中确认。在此温度下，结构水的比例无法估计 [Hu 2022, pp. 5-6]。

## Assumptions / Conditions
- **缓慢热作用**：实验排除了热冲击的影响，所有试样均为缓慢加热（2 °C/min）和炉内自然冷却，这有利于更准确地反映温度效应 [Hu 2022, pp. 5-6]。
- **均匀损伤假设**：基于P波速度定义的损伤因子（`D_v1`, `D_v2`）假设热损伤在试样中是均匀的。
- **测量条件一致性**：P波速度的测量使用了凡士林作为耦合剂以确保换能器与试样之间的良好接触 [Hu 2022, pp. 3-5]。
- **加载速率恒定**：巴西劈裂和SCB试验均采用0.002 mm/s的恒定加载速率，排除了加载速率对强度的影响 [Hu 2022, pp. 3-5]。

## Key Variables / Parameters
- **关键变量**：温度（T, °C）、P波速度（`vp`, m/s）、抗拉强度（`σt`, MPa）、I型断裂韧性（`K_IC`, MPa·m^1/2）。
- **衍生参数**：
    - **脆性指标**：`α = σt / K_IC` [Hu 2022, pp. 9-10]。
    - **热损伤因子**：`D_v1 = 1 - v_T / v_0`，`D_v2 = 1 - (v_T / v_0)^2` [Hu 2022, pp. 12-13]。
    - **力学性能损伤因子**：`D_σ = 1 - σ_T / σ_0`，`D_KIC = 1 - K_ICT / K_IC0` [Hu 2022, pp. 12-13]。
- **拟合公式及参数**：
    - `σt`-`vp` 线性关系：斜率1.228，截距1.436 [Hu 2022, pp. 12-13]。
    - `K_IC`-`vp` 线性关系：斜率0.500，截距-0.175 [Hu 2022, pp. 12-13]。
    - `α`-T 指数关系：`α = 3.403 + 0.010 exp(0.011T)` [Hu 2022, pp. 9-10]。
    - `D_v1`-T 关系：`D_v1 = -0.018 + 1.230×10^-3 T` [Hu 2022, pp. 12-13]。

## Reusable Claims
1.  对于经过缓慢加热和自然冷却处理的花岗岩，其P波速度（`vp`）与抗拉强度（`σt`）之间存在强线性关系（`σt = 1.436 + 1.228 vp`, R²=0.980），这一关系适用于评估20-600 °C范围内的热损伤 [Hu 2022, pp. 12-13]。
2.  对于经过缓慢加热和自然冷却处理的花岗岩，其P波速度（`vp`）与I型断裂韧性（`K_IC`）之间存在强线性关系（`K_IC = -0.175 + 0.500 vp`, R²=0.924），这一关系适用于评估20-600 °C范围内的热损伤 [Hu 2022, pp. 12-13]。
3.  参数 `α = σt / K_IC` 可作为岩石的脆性指标。对于本研究中的花岗岩，α值随温度升高（20-600 °C）呈指数增加（`α = 3.403 + 0.010 exp(0.011T)`, R²=0.987），α值增大指示岩石从脆性向延性转变 [Hu 2022, pp. 9-10]。
4.  对于花岗岩，温度超过400 °C是导致其微观结构出现明显热裂纹，进而导致脆性指标α和P波速度发生显著变化的温度阈值 [Hu 2022, pp. 6-10]。

## Candidate Concepts
- [[thermal damage]]
- [[brittleness index]]
- [[mode-I fracture toughness]]
- [[P-wave velocity]]
- [[Brazilian splitting test]]
- [[semi-circular bend (SCB) test]]
- [[ductility-brittleness transition temperature]]
- [[ultrasonic non-destructive testing]]

## Candidate Methods
- [[Brazilian splitting test for tensile strength]]
- [[semi-circular bend (SCB) test for fracture toughness]]
- [[ultrasonic pulse velocity measurement]]
- [[damage factor characterization using P-wave velocity]]
- [[polynomial fitting of physical properties vs. temperature]]

## Connections To Other Work
- **与前人经验公式的联系**：文中引用了Haberfield和Johnston (1989)、Zhang (2002)、Vavro和Soucek、Wang等人得出的σt与KIC的线性关系，但指出这些关系因岩石类型、测试方法和条件（如温度、加载速率）不同而有显著差异 [Hu 2022, pp. 2-3, 9-10]。本研究在此基础上，探讨了温度对同一类岩石σt-KIC关系的影响。
- **与脆性指标研究的联系**：文中将提出的脆性指标α与Stripa花岗岩的微裂纹初始温度（300 °C）、BS花岗岩的脆-延性转变温度阈值（250 °C）以及CF大理石的延性特征温度（>400 °C）进行了比较和讨论，认为α的显著增加温度可能与岩石的脆-延性转变温度相关 [Hu 2022, pp. 10-12]。
- **与P波速度研究的联系**：研究结果与Fan et al. (2017), Yang et al. (2017), Jin et al. (2019) 等的结果进行了对比，发现升温导致花岗岩P波速度下降是一个普遍现象 [Hu 2022, pp. 5-6]。其结论支持使用基于P波速度的损伤因子来评估力学性能退化，与Zhi et al. (2012), Sun et al. (2017) 的方法一致 [Hu 2022, pp. 12-13]。

## Open Questions
- 本研究提出的脆性指标α及其与温度的关系，在砂岩、大理岩、辉长岩等其他不同岩性岩石中是否具有普适性？[Hu 2022, pp. 10-12]
- 在超过600 °C的更高温度区间，P波速度与力学性质之间是否仍能保持强线性关系？[Hu 2022, pp. 5-6]
- 不同冷却方式（如快速冷却/热冲击）对这些关系和损伤因子的影响如何？[Hu 2022, pp. 5-6]
- 未从索引片段中确认裂纹密度、孔隙率等微观结构参数与宏观参数（`vp`, `σt`, `K_IC`）的直接定量关系。

## Source Coverage
本知识页依据索引片段中的12个片段生成，覆盖了论文的摘要、引言、材料与方法、大部分结果和讨论章节。信息相对完整，包含了实验数据、拟合公式和关键结论。可能缺失的信息包括：关于试验材料的详细矿物学描述、具体的微观结构观测（如SEM）细节、以及其他类型岩石完整的数据对比表。部分讨论和结论部分的完整性未从索引片段中确认。
