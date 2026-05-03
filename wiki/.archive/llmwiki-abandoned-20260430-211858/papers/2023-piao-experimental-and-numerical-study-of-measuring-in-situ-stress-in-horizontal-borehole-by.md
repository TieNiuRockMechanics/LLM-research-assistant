---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-piao-experimental-and-numerical-study-of-measuring-in-situ-stress-in-horizontal-borehole-by"
title: "Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method."
status: "draft"
source_pdf: "data/papers/2023 - Experimental and numerical study of measuring in-situ stress in horizontal borehole by hydraulic fracturing method.pdf"
collections:
citation: "Piao, Shenghao, et al. \"Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method.\" *Tunnelling and Underground Space Technology*, vol. 141, 2023, 105363. Accessed 2026."
indexed_texts: "12"
indexed_chars: "56980"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:20:46"
---

# Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method.

## One-line Summary
本文通过理论推导、真三轴实验和 ABAQUS 数值模拟，建立了水平钻孔中水力压裂地应力测量的解释原理，揭示了水平钻孔中裂缝起始位置、泵压响应及裂缝形态与注入速率的关系，为水平定向勘察提供了地应力测量支撑 [Piao 2023, pp. 1-1]。

## Research Question
如何将水力压裂（HF）地应力测量方法从传统垂直钻孔推广至水平钻孔，建立适用于水平钻孔的破裂压力、闭合压力和重开压力与该处三维地应力的定量解释关系？[Piao 2023, pp. 1-1, 2-3]

## Study Area / Data
- **工程依托**：中国天山胜利隧道水平定向钻探地质勘察项目 [Piao 2023, pp. 1-1]。
- **实验岩样**：隧道沿线主要岩性为花岗岩，采用 300×300×300 mm 立方体花岗岩试件，中心预制 20 mm 直径孔井，内置铜管并用环氧植筋胶固结 [Piao 2023, pp. 5-6]。
- **实验分组**：采用四种注入速率：2 ml/min、4 ml/min、8 ml/min 和 11 ml/min [Piao 2023, pp. 5-6]。
- **数值模型**：ABAQUS 三维模型，包含 42960 个 C3D8RP 单元和 2000 个零厚度粘性单元；三轴围压 σₓ = 10 MPa, σᵧ = 8 MPa, σ_z = 12 MPa，孔井平行于 Z 轴；模拟了 11 ml/min（A 组）和 2 ml/min（B 组）两种注入曲线 [Piao 2023, pp. 9-10]。

## Methods
### 理论框架
以改进的倾斜钻孔模型为基础，通过坐标旋转（地理坐标系、地应力坐标系、钻孔坐标系）将远场地应力张量转换至钻孔坐标系，并考虑有效应力原理（σᵢⱼ = Sᵢⱼ - δᵢⱼ Pₚ），建立水平钻孔中地应力方向、大小与水力压裂参数的关系 [Piao 2023, pp. 2-5]。

### 实验设计
利用 HXYL‑II 气‑液压裂模拟器进行真三轴水力压裂流‑固耦合实验，该平台包含真三轴模块、水力压裂模块和声发射模块。8 个声发射探头按特定坐标布置在试件表面，实时定位破裂源 [Piao 2023, pp. 5-7]。

### 数值模拟
采用 ABAQUS 有限元软件，在孔壁附近和隔离段加密网格，沿断裂面批量插入零厚度粘性单元，使用 Maxs Damage 模型模拟起裂与扩展。初始地应力直接给定，忽略自重，孔井中心注入点施加环形集中流量，约束条件为仅允许法向位移的六面约束 [Piao 2023, pp. 9-10]。

## Key Findings
1. **水平钻孔裂缝起始位置**：与垂直钻孔裂缝集中在孔底不同，水平钻孔由于流体在完井段自由流动，初始微裂纹首先出现在钻孔中部。这导致泵压呈非线性上升，且在达到破裂压力 P_b 后，后续压力难以维持裂缝张开 [Piao 2023, pp. 8-9]。
2. **注入速率的影响**：注入速率与破裂压力 P_b 呈正相关；注入速率越大，试件更早达到破裂所需最小压力。破裂后裂缝长度更大、宽度更窄，该趋势与在垂直井中的观察一致 [Piao 2023, pp. 6-9]。
3. **声发射特征**：花岗岩高阻抗、高强度导致接收信号具有大幅值、长持续时间和高频带集中的特征，与已有研究一致。注入速率越高，潜在破裂点数量和破裂体积越大 [Piao 2023, pp. 6-8]。
4. **裂缝网络形态**：部分实验组（A、D 组，高注入速率或特定条件）出现两个相互连通的裂缝面，对应更高的信号幅值和更分散的能量；而 B、C 组仅呈现单一裂缝面，可能与花岗岩复杂结构有关 [Piao 2023, pp. 6-8]。
5. **保证数据准确性的操作**：由于水平井中 P_r 测量前压力不稳定，规定在 P_r 之后再测量闭合压力 P_s [Piao 2023, pp. 8-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水平钻孔中裂缝起始于钻孔中部，而非底部；泵压非线性上升 | [Piao 2023, pp. 8-9] | 花岗岩试件，无预存裂缝的水平孔 | 与垂直井行为不同，是水平钻孔的特殊性 |
| 注入速率与 P_b 正相关，注入速率越快，P_b 越大 | [Piao 2023, pp. 8-9] | 2～11 ml/min 范围，三轴应力固定 | 可复现的实验规律 |
| 高注入速率下裂缝长度更大、宽度更窄，与垂直井观察一致 | [Piao 2023, pp. 6-8] | 引用 Chuprakov 等 (2014) 和 Chen 等 (2016) 的垂直井结果 | 宏观裂缝形态的一致性 |
| 声发射信号大幅值、长持续时间、高频集中 | [Piao 2023, pp. 6-8] | 花岗岩高强度、高阻抗 | 与 Xing 等 (2019) 研究类似 |
| A 和 D 组出现两个相互连通的裂缝面，B 和 C 组为单一裂缝面 | [Piao 2023, pp. 6-8] | 注入速率和能量分散度不同 | 可能与岩石非均质性有关 |
| 数值模型中粘性单元损伤基于位移达到 5 mm 判断 | [Piao 2023, pp. 9-10] | 独立模式，名义应力 5 MPa，粘度系数 0.001 | 模拟参数设定，用于重现实验 |

## Limitations
未从索引片段中确认完整的局限性论述。从实验与模拟描述可推断的局限包括：
- 实验仅针对花岗岩一种岩性，结论向其他岩类推广需谨慎。
- 实验室尺度（300 mm 立方体）与实际工程钻孔的尺寸效应未讨论。
- 数值模拟假设材料均匀、粘性单元各向同性损伤，且仅模拟了单一应力场（σₓ=10 MPa, σᵧ=8 MPa, σ_z=12 MPa）和两种注入速率。
- 本文未涉及含天然裂隙或孔隙压力变化较大的情况。
- 未从索引片段中确认对 P_s、P_r 计算地应力的定量公式是否最终确定或在现场实际钻孔中得到验证。

## Assumptions / Conditions
- **适用钻孔类型**：水平钻孔（偏差角 φ=90°）[Piao 2023, pp. 3-5]。
- **力学框架**：线弹性断裂力学（参考已有 HF 理论），有效应力原理，点应力准则等经典假定 [Piao 2023, pp. 1-2]。
- **理论推导假设**：地应力主轴与地理坐标系可通过 Euler 角旋转表达，忽略钻井扰动引起的塑性区 [Piao 2023, pp. 3-5]。
- **实验假设**：试件为完整、无预存宏观裂缝的花岗岩；井壁与铜管环氧胶结良好，可视为连续体 [Piao 2023, pp. 5-6]。
- **数值模型假设**：粘性单元厚度为 0，Maxs Damage 采用独立模式，损伤起始于位移超过 5 mm；忽略自重，直接施加初始有效应力；孔隙比初始设定为 0.2 [Piao 2023, pp. 9-10]。

## Key Variables / Parameters
- **水力压裂压力参数**：破裂压力 P_b、闭合压力 P_s、重开压力 P_r [Piao 2023, pp. 1-2]。
- **注入速率**：2, 4, 8, 11 ml/min [Piao 2023, pp. 5-6]。
- **三维地应力**：最大、中间、最小主应力 S₁, S₂, S₃ 及其方向（Euler 角 α, β, γ）[Piao 2023, pp. 3-5]。
- **钻孔几何参数**：方位角 δ，偏差角 φ（对于水平孔 φ=90°）[Piao 2023, pp. 3-5]。
- **应力变换矩阵**：地理‑地应力‑钻孔坐标系旋转张量 R_S, R_b [Piao 2023, pp. 3-5]。
- **有效应力**：σᵢⱼ = Sᵢⱼ - δᵢⱼ Pₚ，其中 Pₚ 为孔隙压力 [Piao 2023, pp. 4-5]。
- **数值模型参数**：围压 σₓ=10 MPa, σᵧ=8 MPa, σ_z=12 MPa；粘性单元名义应力 5 MPa，临界位移 5 mm，粘度系数 0.001；初始孔隙比 0.2 [Piao 2023, pp. 9-10]。
- **声发射参数**：探头坐标（8 个特定位置）、信号幅值、持续时间、频谱 [Piao 2023, pp. 6-8]。
- **裂缝几何**：长度、宽度、连通性、裂缝面数量 [Piao 2023, pp. 6-8]。

## Reusable Claims
1. “在水平钻孔（无预存裂缝）中，水力压裂的初始裂缝并非在孔底形成，而是在钻孔中部产生，这导致泵压呈非线性上升且达到 P_b 后难以维持裂缝张开。” [Piao 2023, pp. 8-9]（适用于完整硬岩水平孔，注入流体未形成稳定封隔的情况）
2. “注入速率与破裂压力 P_b 呈正相关，较高的注入速率导致试样更快达到破裂所需最小压力，且形成的裂缝长度更大、宽度更窄，该规律与垂直井中的观察一致。” [Piao 2023, pp. 6-9]（条件：花岗岩，流量范围 2～11 ml/min，恒定三轴应力）
3. “为保证水平孔 HF 数据准确性，应在测量重开压力 P_r 之后再测量闭合压力 P_s。” [Piao 2023, pp. 8-9]（操作准则，基于实验期间压力不稳定的现象）
4. “声发射信号在花岗岩水力压裂中具有大幅值、长持续时间和高频集中的特征，可用于精确定位破裂位置和评价破裂体积。” [Piao 2023, pp. 6-8]（支持声发射作为水平孔 HF 监测手段）
5. “基于坐标旋转方法，可将任意产状钻孔处的远场地应力张量变换至钻孔坐标系，从而使经典 HF 解释原理得以推广至倾斜和水平钻孔。” [Piao 2023, pp. 3-5]（理论框架，适用于线弹性、忽略扰动区的分析）

## Candidate Concepts
- [[horizontal directional investigation]]
- [[in-situ stress measurement]]
- [[hydraulic fracturing method]]
- [[breakdown pressure]]
- [[shut-in pressure]]
- [[reopening pressure]]
- [[acoustic emission monitoring]]
- [[cohesive zone model]]
- [[true triaxial test]]
- [[fracture network]]

## Candidate Methods
- [[coordinate system transformation for borehole stress]]
- [[true triaxial hydraulic fracturing simulation]]
- [[acoustic emission source localization]]
- [[ABAQUS cohesive element insertion]]
- [[Maxs Damage model for fracture propagation]]
- [[time-frequency analysis of AE signals]]

## Connections To Other Work
- 本文直接建立在倾斜钻孔水力压裂模型之上，通过增强前人的坐标系旋转方法，将解释原理推广至水平钻孔 [Piao 2023, pp. 1-1, 2-3]。
- 水平钻孔中裂缝长度‑宽度随注入速率的变化趋势，引用了 Chuprakov 等 (2014) 和 Chen 等 (2016) 在垂直井中的观测作为类比 [Piao 2023, pp. 6-8]。
- 声发射信号特征与 Xing 等 (2019) 的研究结论一致 [Piao 2023, pp. 6-8]。
- 理论部分引用了点应力准则（Nuimer et al. 1975）和 ISRM 建议方法的经典工作（Haimson 1978, Makówka 2015）[Piao 2023, pp. 1-2]。
- 文中提及 Gao 等 (2020)、Synn 等 (2015)、Xie 等 (2017)、Zeng 等 (2015) 对倾斜/水平钻孔水力压裂的探索，但指出多数工作集中于裂缝网络或油气开采，而对水平钻孔地应力测量解释原理研究甚少 [Piao 2023, pp. 2-3]。

## Open Questions
- 未从索引片段中确认是否给出了基于实验和数值结果的定量地应力计算公式，该公式是否已在现场水平钻孔中得到验证。
- 不同岩性（如沉积岩、变质岩）、节理发育岩体以及存在初始孔隙压力梯度条件下，裂缝起始位置和泵压响应的变化规律尚待研究。
- 水平钻孔中多裂缝连通的控制因素及对 P_s、P_r 解释的影响需进一步量化。
- 数值模拟中仅考虑了一种应力状态和两种注入速率，参数敏感性分析未充分展开。

## Source Coverage
本页依据论文的 12 个索引片段编写，覆盖了摘要、引言、理论推导部分、实验方法、主要实验结果和部分数值模拟设置。片段未包含完整的数值模拟结果分析、讨论章节及最终结论的详细展开，亦缺少显式的局限性论述和与现场实测的对比。因此，定量地应力计算公式的具体形式及验证情况、参数敏感性研究等内容在本页面中标记为未确认。
