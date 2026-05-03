---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-xi-experimental-investigations-of-compressive-strength-and-thermal-damage-capacity-characte"
title: "Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes."
status: "draft"
source_pdf: "data/papers/2020 - 不同冷却模式下花岗岩强度对比与热破坏能力表征试验研究.pdf"
collections:
  - "part2"
  - "郤"
citation: "Xi, Baoping, et al. \"Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 39, no. 2, Feb. 2020, pp. 286-300. doi:10.13722/j.cnki.jrme.2019.0782."
indexed_texts: "5"
indexed_chars: "23421"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:45:33"
---

# Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes.

## One-line Summary
通过比较 20 °C 空气自然冷却与 20 °C 恒温水冷却两种模式下高温花岗岩的单轴抗压强度及表面降温规律，引入热冲击因子定量表征不同冷却介质的损伤能力，揭示水冷造成的热损伤与强度劣化显著强于空气冷却 [Xi 2020, pp. 1-4]。

## Research Question
不同冷却模式（空气自然冷却 vs. 恒温水冷却）如何影响 250–600 °C 高温处理后花岗岩的单轴抗压强度？能否用热冲击因子定量评价冷却过程中的热破坏能力并建立其与强度劣化的关系？

## Study Area / Data
未从索引片段中确认花岗岩的产地及地质背景。

## Methods
- **试件制备与加热**：花岗岩试件（尺寸 φ50 mm×100 mm，[Xi 2020, pp. 8-12] 提及），以 3–5 °C/h 的速率加热至目标温度（250、300、350、400、500、600 °C），保温 3 h [Xi 2020, pp. 4-8]。
- **冷却模式**：分为两组——① 20 °C 空气中自然冷却；② 20 °C 恒温水中冷却（热冲击冷却） [Xi 2020, pp. 1-4]。
- **单轴压缩试验**：对冷却后试件进行单轴压缩，加载速率 0.001 mm/s [Xi 2020, pp. 4-8]。
- **温度与温度梯度监测**：测量试件表面温度随时间变化，记录冷却过程中测点温度梯度，特别关注表面以下 5 mm 内（AB 段）的温度梯度 [Xi 2020, pp. 8-12]。
- **传热数值模拟**：建立不同冷却介质环境下的传热数值模型，引入热冲击因子 ω（单位：°C/(m·s)）描述热对岩石的损伤能力 [Xi 2020, pp. 1-4][Xi 2020, pp. 12-14]。

## Key Findings
1. 20 °C 水冷模式下花岗岩的单轴抗压强度在相同温度条件下均低于空气自然冷却模式，水冷强度约为对应空气冷却的 85%–90% [Xi 2020, pp. 4-8]。
2. 水冷过程中的温度梯度和热冲击因子远大于空气冷却。以 600 °C 初始温度为例，水冷时表面最大温度梯度达 57 204 °C/m，而空气冷却仅为 3 022 °C/m，两者相差约 18.93 倍 [Xi 2020, pp. 8-12]。
3. 热冲击因子 ω 的最大值随初始温度升高而增大：空气冷却从 250 °C 的 95.2 °C/(m·s) 增至 600 °C 的 302.2 °C/(m·s)；水冷却从 250 °C 的 11 383 °C/(m·s) 增至 600 °C 的 28 602 °C/(m·s) [Xi 2020, pp. 12-14]。
4. 抗压强度与最大热冲击因子之间存在良好的定量关系。空气冷却下为线性关系：σ_c = −0.4571 ω + 211.34 (R²=0.9794)；水冷却下为对数关系：σ_c = −104.23 ln (ω) + 1131 (R²=0.9534) [Xi 2020, pp. 12-14]。
5. 冷却初期（前 10 s）热冲击最为剧烈，温降速率和温度梯度均达到峰值，此后迅速衰减 [Xi 2020, pp. 8-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水冷下单轴抗压强度为对应空气冷却的 85%–90% | [Xi 2020, pp. 4-8] | 加热 250–600 °C，保温 3 h，单轴压缩 0.001 mm/s | 具体数值见表 1 |
| 600 °C 时水冷表面温度梯度是空气冷的 18.93 倍 (57 204 vs. 3 022 °C/m) | [Xi 2020, pp. 8-12] | 表面以下 5 mm 内测量 | 冷却初期 10 s 内差别最大 |
| 600 °C 时水冷热冲击因子 28 602 °C/(m·s)，空气冷为 302.2 °C/(m·s) | [Xi 2020, pp. 12-14] | 最大热冲击因子 ω_max | 见表 2 |
| 空气冷强度与 ω 线性拟合 R²=0.9794 | [Xi 2020, pp. 12-14] | σ_c = −0.4571ω + 211.34 | 适用于 250–600 °C |
| 水冷强度与 ω 对数拟合 R²=0.9534 | [Xi 2020, pp. 12-14] | σ_c = −104.23 lnω + 1131 | 适用于 250–600 °C |

## Limitations
索引片段中未明确讨论研究局限性。可能存在的限制包括：仅考虑 20 °C 单一冷却介质温度；试验为实验室小尺寸试件；未涉及多循环热冲击、不同升温速率或三维应力状态。

## Assumptions / Conditions
- 加热过程缓慢且均匀，以 3–5 °C/h 升温，避免热冲击损伤 [Xi 2020, pp. 4-8]。
- 冷却介质（空气、水）温度恒定为 20 °C。
- 热冲击因子 ω 的定义基于温度梯度测量，假定其能综合表征冷却引发的热损伤能力 [Xi 2020, pp. 1-4]。
- 单轴压缩试验的承载方式为位移控制，速率 0.001 mm/s，且试件端面效应忽略不计。

## Key Variables / Parameters
- **初始加热温度**：250, 300, 350, 400, 500, 600 °C
- **冷却模式**：20 °C 空气自然冷却；20 °C 恒温水冷却（热冲击）
- **单轴抗压强度 σ_c**（MPa）
- **热冲击因子 ω**（°C/(m·s)），特别是其最大值 ω_max
- **温度梯度**（°C/m），尤其是试件表面下 5 mm 内
- **降温速率**（°C/s），特别是前 10 s 的瞬态值
- **热应力**（从温度场计算）

## Reusable Claims
1. 对于加热至 250–600 °C 并保温 3 h 的花岗岩，切换至 20 °C 水冷其单轴抗压强度降为相同温度条件下 20 °C 空气冷却的 85%–90%。证据：表 1 强度对比 [Xi 2020, pp. 4-8]。适用条件：类似升降温历程的花岗岩，尺寸相近。
2. 在 600 °C 初始温度下，20 °C 水冷产生的最大温度梯度约为 57 184 °C/m，是空气冷却（～3 022 °C/m）的约 18.9 倍，表明水冷的热冲击强度远高于空气冷 [Xi 2020, pp. 8-12]。适用条件：试件表面 5 mm 内，可推广至类似热边界。
3. 空气冷却模式下，花岗岩抗压强度与最大热冲击因子满足线性衰退关系 σ_c = −0.4571ω + 211.34 (R²=0.9794)；水冷却模式下满足对数衰退关系 σ_c = −104.23 lnω + 1131 (R²=0.9534) [Xi 2020, pp. 12-14]。适用条件：250–600 °C 单次加热-冷却，单轴加载，相同花岗岩。

## Candidate Concepts
[[thermal shock]], [[cooling rate]], [[uniaxial compressive strength]], [[granite]], [[thermal damage]], [[heat transfer coefficient]], [[temperature gradient]], [[thermal stress]], [[thermal shock factor]]

## Candidate Methods
[[uniaxial compression test]], [[heat transfer numerical simulation]], [[surface temperature measurement]], [[thermal shock factor characterization]]

## Connections To Other Work
- 片段提及 Kumari 等 [17-19] 研究了不同冷却处理对花岗岩温度依赖性力学行为的影响，用于对比分析冷却模式的效果 [Xi 2020, pp. 14-15]。具体关系未从片段确认。
- 片段提及唐世斌等 [14] 对岩石低温致裂的理论与数值模拟，以及鲍春艳等 [13] 对冷却收缩导致表面等间距裂缝的数值模拟，作为热-力耦合背景下损伤机制的支撑 [Xi 2020, pp. 14-15]。可与 [[thermal cracking]]、[[cooling-induced fracture]] 等领域连接。
- 可从主题上连接到其他热-力耦合岩石损伤研究，如 [[thermal spallation drilling]]、[[geothermal reservoir stimulation]] 等。

## Open Questions
- 未从索引片段中确认长期或多循环热冲击下花岗岩的损伤累积规律。
- 其他冷却介质（如不同温度的盐水、油、液氮）对强度劣化的影响未涉及。
- 未探讨三轴应力状态下热损伤的演化，以及渗透率变化的关联。
- 热冲击因子在其他岩石类型（如砂岩、大理岩）中的适用性尚待验证。

## Source Coverage
本页基于 5 个索引片段（pp. 1-15 的零散段落）编写，覆盖了论文的摘要、方法描述、主要实验结果和部分讨论。由于 OCR 识别乱码，部分实验细节（如试件取样深度、数值模拟具体参数）可能不全；引言、参考文献全貌及部分图表解读缺失。重要试验结果表（表 1、表 2）及强度-热冲击关系式已包含，但附加试验（如巴西劈裂）未从片段中确认。总体可支撑核心结论，但完整的实验条件与讨论中的对比分析细节可能不完整。
