---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-wu-effect-of-cooling-methods-on-mechanical-behaviors-and-thermal-damage-distributions-of-gr"
title: "Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations."
status: "draft"
source_pdf: "data/papers/2023 - Effect of cooling methods on mechanical behaviors and thermal damage distributions of granite Experiments and simulations.pdf"
collections:
  - "zotero new"
citation: "Wu, Yangchun, et al. \"Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations.\" *Geothermics*, vol. 114, 2023, 102796. doi:10.1016/j.geothermics.2023.102796. Accessed 2026."
indexed_texts: "14"
indexed_chars: "65529"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:08:38"
---

# Effect of Cooling Methods on Mechanical Behaviors and Thermal Damage Distributions of Granite: Experiments and Simulations.

## One-line Summary
通过实验和数值模拟，比较了缓慢加热后水冷与空冷两种冷却方式对花岗岩力学行为、声发射特征和热损伤分布的不同影响，揭示了冷却方式控制热应力分布和损伤严重程度的内在机制。 [Wu 2023, pp. 1-2]

## Research Question
不同冷却方法（水冷 vs. 空冷）如何影响高温花岗岩的拉伸强度、声发射活动及热损伤的空间分布？其根本原因是什么？ [Wu 2023, pp. 1-2]

## Study Area / Data
- **试样**：实验室制备的花岗岩巴西圆盘，主要矿物成分为石英（28.6%）、长石（55.1%）、云母（11.5%）和绿泥石（4.8%），由 XRD 测定。 [Wu 2023, pp. 3-3]
- **实验数据**：不同初始温度（200–600 °C，步长 100 °C）处理后试样的质量、体积、密度、纵波波速；巴西劈裂试验的载荷‑位移曲线、抗拉强度；加载过程中的声发射计数与累积计数、DIC 表面应变场图像；试样表面冷却过程中的温度‑时间序列（用于模型验证）。 [Wu 2023, pp. 3-3, 3-5, 5-6, 6-6, 6-8]

## Methods
- **热处理**：以 2 °C/min 的速率升温至目标温度 (200–600 °C)，保温 3 h，随后分别进行水冷（放入 20 °C 水中）或空冷（空气中自然冷却），并用红外测温枪监测表面温度直至接近介质温度。 [Wu 2023, pp. 3-3]  
- **巴西劈裂试验**：干燥后的试样表面制作散斑，采用伺服试验机进行加载，同步利用 DIC 系统记录表面应变场，以及 AE 系统采集声发射信号。 [Wu 2023, pp. 3-3, 6-6]  
- **数值模拟**：使用 COMSOL 软件建立与试样同尺寸的模型，考虑热传导、表面对流换热（牛顿冷却定律）、热应变及热‑力耦合方程，输入比热容 850 J/(kg·°C)、密度 2640 kg/m³、弹性模量 9.3 GPa 等参数，模拟不同冷却介质下的温度场演化和热应力分布。 [Wu 2023, pp. 6-8]

## Key Findings
- **抗拉强度**：相同初始温度下，水冷试样的抗拉强度始终低于空冷试样，且随温度升高强度下降更显著。 [Wu 2023, pp. 5-6]  
- **声发射特征**：水冷试样在压密阶段的 AE 计数比空冷更密集；随初始温度升高，空冷试样的累积 AE 计数持续增加，而水冷试样的累积 AE 计数先增加后减少。 [Wu 2023, pp. 6-6, 6-8]  
- **热损伤分布**：冷却方法对应力分布和热损伤分布有决定性影响。**空冷试样**的拉伸应力和热损伤呈随机分布，主要受控于矿物热膨胀系数的非均质性；**水冷试样**的拉伸应力和热损伤集中在试样表面，主要受控于温度梯度。水冷造成的热损伤比空冷更严重。 [Wu 2023, pp. 1-2, 6-8]  
- **物理性质**：水冷下试样的质量、体积、密度和波速的变化率均大于空冷，例如 600→20 °C 水冷后波速下降更剧烈，与力学强度降低一致。 [Wu 2023, pp. 3-5, 5-6]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水冷试样的抗拉强度低于空冷试样，且随温度升高差异增大 | [Wu 2023, pp. 5-6] | 加热速率 2 °C/min，保温 3 h，巴西劈裂试验；初始温度 200–600 °C | 图 6、7 展示载荷‑位移曲线和归一化强度 |
| 水冷试样压密阶段 AE 计数比空冷更密集；累积 AE 计数的温度响应趋势不同（空冷单调增，水冷先增后减） | [Wu 2023, pp. 6-6, 6-8] | 同上，同步采集 AE | 图 8、9 提供时间历程曲线 |
| 空冷热损伤分布随机，由热膨胀系数非均质性控制；水冷热损伤集中在表面，由温度梯度控制 | [Wu 2023, pp. 1-2, 6-8] | 实验（DIC）与数值模拟联合分析 | 摘要及模型描述 |
| 水冷造成的物理性质退化更严重：600→20 °C 水冷后质量变化‑0.33%，体积变化 3.2%，密度变化‑3.43%；空冷相应为‑0.28%，2.64%，‑2.85% | [Wu 2023, pp. 3-5] | 加热条件同上，冷却至 20 °C | 表 1 及图 5 |
| 对流换热系数差异导致水冷速率远大于空冷，决定了传热行为 | [Wu 2023, pp. 1-2, 3-5] | 冷却阶段观察与模型 | 水冷平均冷却速率 0.50 °C/s（200 °C）到 1.39 °C/s（600 °C），空冷 0.05 °C/s 到 0.16 °C/s |
| 试样破坏过程呈明显脆性，但水冷试样在 500 °C 以上出现一定延性特征 | [Wu 2023, pp. 5-6] | 巴西劈裂试验，加载至破坏 | 与 Wu et al. (2019) 的结论一致 |

## Limitations
未从索引片段中确认。

## Assumptions / Conditions
- 采用 2 °C/min 的加热速率，以避免加热阶段产生热损伤（依据 Chen et al. (2017) 报道的临界加热率 5 °C/min）。 [Wu 2023, pp. 2-2]  
- 保温 3 h 以保证试样内外温度均匀。 [Wu 2023, pp. 3-3]  
- 数值模拟中假设对流换热满足牛顿冷却定律，材料为线弹性，热物性与力学参数为常数（片段仅给出部分参数值：比热容、密度、弹性模量；泊松比及其他参数未确认）。 [Wu 2023, pp. 6-8]  
- 热损伤主要由温度梯度和矿物热膨胀系数不匹配产生的热应力导致，不考虑化学或相变作用。 [Wu 2023, pp. 2-3]  
- DIC 与 AE 系统能准确反映表面及内部微裂纹活动，未确认系统标定和测量误差。  

## Key Variables / Parameters
- 初始加热温度 T₀ (200–600 °C)  
- 冷却介质（水、空气）及相应的对流换热系数 h [W/(m²·K)]  
- 冷却速率（平均 °C/s）  
- 巴西劈裂抗拉强度 σ_t，归一化强度 δ = σ_t(T)/σ_t(T₀) [Wu 2023, pp. 5-6]  
- 纵波波速 v_p 及其变化率  
- 声发射计数、累积 AE 计数  
- 表面应变场（DIC 应变值）  
- 热膨胀系数 β，热应变 ε_th [Wu 2023, pp. 6-8]  
- 温度梯度 ∂T/∂n  
- 力学参数：弹性模量（9.3 GPa）、泊松比（未确认）、拉梅常数 λ 和 μ [Wu 2023, pp. 6-8]  
- 热物性参数：比热容 c (850 J/(kg·°C))、密度 (2640 kg/m³) [Wu 2023, pp. 6-8]  

## Reusable Claims
- **Claim 1**：对于本文所用花岗岩，在 200–600 °C 初始温度下，水冷试样的抗拉强度始终低于空冷试样，且两者差距随温度升高而扩大。[Wu 2023, pp. 5-6]（条件：2 °C/min 加热、3 h 保温、巴西劈裂试验；限制：仅对此花岗岩和该温度范围成立。）  
- **Claim 2**：水冷试样在巴西劈裂的压密阶段表现出比空冷试样更高的声发射活动，说明水冷能引发更多预存微裂纹或更显著的初始损伤。[Wu 2023, pp. 6-6]（条件：同上；限制：未区分原生孔隙与热致裂纹贡献。）  
- **Claim 3**：随初始温度升高，空冷试样的累积声发射计数单调上升，而水冷试样的累积声发射计数先增加后减小，表明水冷在高温下可能形成宏观缺陷导致声发射特征转变。[Wu 2023, pp. 6-8]（条件：200–600 °C，巴西加载；限制：缺少微观观测直接证实。）  
- **Claim 4**：空冷条件下，热损伤和拉伸应力在试样内部分布随机，主要由矿物热膨胀系数的非均质性控制；水冷条件下，损伤与应力集中于试样表面，主要由瞬态温度梯度控制。[Wu 2023, pp. 1-2, 6-8]（条件：实验结果与 COMSOL 模拟共同支持；限制：模型假设理想界面换热，未考虑表面沸腾等现象。）  
- **Claim 5**：水冷造成的物理性质退化（质量、体积、密度、波速）比空冷更剧烈，与强度降低一致。[Wu 2023, pp. 3-5]（条件：加热温度 200–600 °C；限制：未考虑冷却过程中可能的水‑岩化学反应。）  

## Candidate Concepts
- [[thermal damage]]  
- [[Brazilian tensile strength]]  
- [[temperature gradient]]  
- [[thermal stress]]  
- [[heterogeneity of thermal expansion coefficient]]  
- [[convective heat transfer coefficient]]  
- [[acoustic emission (AE)]]  
- [[digital image correlation (DIC)]]  
- [[cooling rate]]  
- [[heat treatment (rock)]]  

## Candidate Methods
- [[COMSOL multiphysics]]  
- [[DIC method]]  
- [[AE monitoring]]  
- [[infrared thermometry]]  
- [[Brazilian disc test]]  
- [[slow heating (2°C/min)]]  
- [[water quenching]]  
- [[air cooling]]  
- [[XRD mineral analysis]]  

## Connections To Other Work
- 本研究结果与 **Zhu et al. (2021)** 和 **Kang et al. (2021)** 一致，即水冷导致花岗岩的纵波波速、强度等力学参数比空冷下降更大。 [Wu 2023, pp. 3-5, 5-6]  
- **Chen et al. (2017)** 提出的 5 °C/min 临界加热率被采纳为实验加热速率（2 °C/min）的依据，以避免加热阶段损伤。 [Wu 2023, pp. 2-2]  
- 与 **Jin et al. (2019)** 的结论一致，即快速冷却（水冷）比慢速冷却产生更多微裂纹，导致物理‑力学性能显著下降和渗透率激增。 [Wu 2023, pp. 2-2]  
- **Zhao et al. (2016, 2018)** 提出高温岩石水力压裂的主要热刺激机制是井筒附近高温度梯度的形成，本文的表面主导损伤分布与该观点在主题上相关。 [Wu 2023, pp. 2-3]  

## Open Questions
未从索引片段中确认。

## Source Coverage
本页依据 14 个索引片段，覆盖了论文摘要、引言（部分）、实验方案、部分结果（物理性质、拉伸强度、声发射与 DIC 特征）以及数值模型设置。片段主要集中于结果与分析的前半部分，对于模拟结果的完整验证、材料泊松比等参数、热传导系数等未予提供，可能遗漏了讨论部分的深层机理和结论段落。页数范围从第 1 页至第 8 页（片段编号 1–8），但部分高页数片段仅给出方程和模型设置的开头，后续章节（如更多模拟验证、讨论、结论）信息缺失。
