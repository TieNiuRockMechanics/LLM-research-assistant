---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-yoon-effect-of-fracture-characteristics-on-groundwater-flow-adjacent-to-high-level-radioact"
title: "Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository."
status: "draft"
source_pdf: "data/papers/2024 - Effect of fracture characteristics on groundwater flow adjacent to high-level radioactive waste repository.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yoon, Won Woo, et al. \"Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository.\" *Journal of Hydrology*, vol. 629, 2024, 130593."
indexed_texts: "22"
indexed_chars: "108857"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:55:04"
---

# Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository.

## One-line Summary
本研究通过二维数值模型评估高放废物处置库释热引起的压力积聚与温度升高对裂隙岩体地下水流的影响，揭示早期压力驱动径向流与晚期浮力驱动垂向流的控制机制转换，以及裂隙几何特征对裂隙流的调节作用 [Yoon 2024, pp. 1-2]。

## Research Question
高放废物处置库的衰变热如何引起压力积聚与温度升高？这些热-水过程如何影响花岗岩围岩中裂隙（单裂隙、交叉裂隙及离散裂隙网络）的地下水流特征？裂隙几何特征（方向、高度、侧向位置、密度、连通性）如何在不同时间尺度上调节裂隙流？[Yoon 2024, pp. 1-2]。

## Study Area / Data
- **研究区概念模型**：基于韩国KRS处置库概念模型；围岩为结晶花岗岩，深度未从索引片段中确认 [Yoon 2024, pp. 2-2]。
- **模型域与边界**：二维数值模型；顶边界设定压力梯度0.001，温度20°C；底边界为无流动边界，温度80°C（地温梯度0.03°C/m）；侧向边界为无流动和热绝缘边界 [Yoon 2024, pp. 2-3]。
- **罐体热源**：通过先期开发的三维罐体模型模拟罐体表面温度随时间的变化，计算裂变产物和锕系元素的释热 [Yoon 2024, pp. 3-4]。
- **材料分区**：模型包含膨润土缓冲/回填材料、开挖损伤区（EDZ）和花岗岩围岩；具体材料参数见表2 [Yoon 2024, pp. 5-6]。
- **裂隙网络**：构建了单裂隙、双裂隙及离散裂隙网络（DFN）模型；裂隙几何特征包括方向、高度、侧向位置、密度和连通性 [Yoon 2024, pp. 1-2]。

## Methods
- **数值模型**：二维多孔介质模型，耦合地下水流和热传导控制方程；在矩阵和裂隙中分别求解压力和温度，压力梯度控制质量交换，温度梯度控制能量交换 [Yoon 2024, pp. 4-5]。
- **控制方程**：
  - 地下水流：基于达西定律，考虑压力梯度和热致浮力项 [Yoon 2024, pp. 6-7]。
  - 热传导：多孔介质有效热容采用加权算术平均，有效热导率采用加权几何平均 [Yoon 2024, pp. 4-5]。
  - 裂隙流与传热：在裂隙切向上应用控制方程 [Yoon 2024, pp. 5-5]。
- **边界条件与参数**：顶、底、侧边界分别指定水头、无流动、热绝缘等条件；水的物理属性（密度、黏度、热导率、热容）随温度变化的关系采用经验方程（表1）；花岗岩、EDZ、膨润土的材料属性见表2 [Yoon 2024, pp. 2-6]。
- **热源实现**：三维罐体模型采用Malbrain et al. (1982)的公式计算释热Q\_c(t)，然后输入二维模型作为热源 [Yoon 2024, pp. 3-4]。
- **裂隙模型**：
  - 单裂隙：不同方向（0°、30°、60°、90°）的裂隙置于处置库右侧100 m处 [Yoon 2024, pp. 7-7]。
  - 双裂隙：不同高度、侧向位置和角度的组合，具体情形未从索引片段中完全确认 [Yoon 2024, pp. 8-9]。
  - DFN：不同密度和连通性的离散裂隙网络 [Yoon 2024, pp. 1-2]。
- **分析指标**：压力积聚、温度升高、地下水流线、裂隙流速（最大流速和平均流速u\_avg\_f）、压力梯度与浮力项的时序对比 [Yoon 2024, pp. 5-7]。

## Key Findings
- **早晚期流态转换**：处置后早期（0.1年）压力积聚至1.68×10⁷ Pa，引发径向流；晚期（2000年）压力回落至静水压力，浮力主导垂向流；至30,000年，压力与温度完全恢复至初始状态 [Yoon 2024, pp. 5-7]。
- **流速响应分异**：不同介质（膨润土、EDZ、花岗岩）中的压力消散和升温导致的流速局部极小值与第二峰值出现时间不同；EDZ的流速可高于初始流速5个数量级 [Yoon 2024, pp. 7-7]。
- **单裂隙方向效应**：
  - 早期径向流阶段，水平裂隙（0°）的平均裂隙流速最大（1.32×10³ m/yr），垂直裂隙（90°）最小（1.81×10² m/yr）。
  - 晚期浮力驱动阶段，垂直裂隙（90°）的平均裂隙流速在140年内快速增大，在1,600年达到峰值（2.27 m/yr），并在240-12,000年间超过水平裂隙。
  - 裂隙流速的大小与方向随时间演化，并受裂隙方向和区域流场的共同控制 [Yoon 2024, pp. 7-8]。
- **双裂隙几何影响**：不同高度、侧向位置和角度的双裂隙组合影响流场与裂隙流的相互作用；具体结果未从索引片段中确认 [Yoon 2024, pp. 8-9]。
- **DFN密度与连通性**：早期阶段，较高密度和连通性的裂隙网络并未导致平均裂隙流速增加；压力积聚主要通过少数优先路径发生流动；晚期阶段，对流循环流明显 [Yoon 2024, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|:---|:---|:---|:---|
| 早期（0.1年）处量库中心压力达1.68×10⁷ Pa，温度达54°C，引发径向地下水流 | [Yoon 2024, pp. 5-6] | 二维多孔介质模型，花岗岩围岩，罐体释热边界 | 径向流由压力积聚驱动 |
| 晚期（2000年）压力回至静水压力，温度保持69°C，浮力驱动垂向对流 | [Yoon 2024, pp. 6-7] | 同上 | 浮力项ρw·g致流场转向 |
| 早期水平裂隙（0°）平均流速最大（1.32×10³ m/yr），垂直裂隙（90°）最小（1.81×10² m/yr） | [Yoon 2024, pp. 7-8] | 单裂隙，距处置库中心右侧100 m | 径向流与水平裂隙方向一致 |
| 晚期垂直裂隙流速于1,600年达峰值2.27 m/yr，并在240-12,000年内超过水平裂隙 | [Yoon 2024, pp. 7-8] | 同上 | 垂向对流与垂直裂隙方向一致 |
| EDZ最大流速达1.88×10⁻¹ m/yr，比初始流速高5个数量级 | [Yoon 2024, pp. 7-7] | EDZ渗透率1×10⁻¹⁶ m²，靠近热源 | EDZ高流速由高渗透率和热-水耦合驱动 |
| 30000年后压力（4.93×10⁶ Pa）与温度（39°C）恢复至初始状态，流速恢复至区域地形控制值 | [Yoon 2024, pp. 6-7] | 模型边界条件为区域流场背景梯度0.001 | 系统最终回归准稳态 |

## Limitations
- **模型维度**：采用二维数值模型，无法刻画三维优先通道和热对流的三维复杂性；适用性受限于二维假设 [Yoon 2024, pp. 1-1]。
- **裂隙网络复杂性**：DFN模拟的具体参数范围和网络实现细节索引片段未充分覆盖；更高密度与连通性在早期的效应需进一步验证 [Yoon 2024, pp. 1-2]。
- **过程耦合深度**：未从索引片段中确认是否包含溶质运移、化学作用、力学变形或两相流等耦合过程。
- **时间跨度**：仅模拟至30,000年；更长时间尺度下的系统演化（如膨润土劣化、裂隙自封闭）未讨论。
- **参数不确定性**：材料参数和裂隙参数取自特定工况，其不确定性影响未评估 [Yoon 2024, pp. 5-6]。

## Assumptions / Conditions
- **连续多孔介质假设**：花岗岩、EDZ和膨润土被视为等效连续多孔介质，流动满足达西定律 [Yoon 2024, pp. 4-5]。
- **水属性随温度变化**：密度、黏度、热导率和热容通过经验方程计算，适用于0–100°C [Yoon 2024, pp. 5-6]。
- **边界条件假设**：顶边界为固定压力梯度0.001；底边界和侧边界为无流动和热绝缘；地温梯度固定为0.03°C/m [Yoon 2024, pp. 2-3]。
- **热源解耦**：罐体表面温度预先用三维模型计算，再作为边界条件赋予二维模型；罐体间对称边界等效为无限重复 [Yoon 2024, pp. 3-4]。
- **裂隙流动假设**：裂隙内流动模型未从索引片段中明确（可能为立方定律或等效连续裂缝）；裂隙传热限于切向 [Yoon 2024, pp. 5-5]。
- **流体不可压缩或Boussinesq近似**：模型在压力驱动和浮力项的处理暗示Boussinesq近似，但未从索引片段中明确。
- **无化学反应或溶质运移**：模型仅考虑水流和传热 [Yoon 2024, pp. 1-2]。

## Key Variables / Parameters
- **变量**：压力p (Pa)，温度T (°C 或 K)，地下水流速u (m/yr)，裂隙流速u\_f / u\_avg\_f (m/yr)，时间t (年)，压力梯度∇p，浮力项ρ\_w g [Yoon 2024, pp. 5-7]。
- **材料参数**：
  - 渗透率k：花岗岩1×10⁻¹⁷ m²，EDZ 1×10⁻¹⁶ m²，膨润土缓冲1×10⁻¹⁹ m²，回填1×10⁻¹⁸ m² [Yoon 2024, pp. 5-6]。
  - 孔隙度n：花岗岩0.05，EDZ 0.2，膨润土0.4–0.42 [Yoon 2024, pp. 5-6]。
  - 热导率λ\_m：花岗岩和EDZ 2.9 W/(m·K)；膨润土按式(12)计算 [Yoon 2024, pp. 5-6]。
- **裂隙几何参数**：方向（0°至90°）、高度、侧向位置、密度、连通性 [Yoon 2024, pp. 7-8]。
- **温度相关水参数**：密度ρ\_w(T)、动力黏度μ(T)、热导率λ\_w(T)、热容C\_p,w(T)由表1经验式确定 [Yoon 2024, pp. 5-6]。
- **热源项**：Q\_c(t) 按式(1)–(2)计算 [Yoon 2024, pp. 3-4]。
- **控制数**：压力梯度∇p与浮力项ρ\_w g的差值作为流速驱动力 [Yoon 2024, pp. 6-7]。

## Reusable Claims
- **Claim 1**：在高放废物处置库花岗岩围岩中，0.1年尺度的早期压力积聚可引起径向流，而2000年尺度的晚期温度升高通过浮力驱动垂向对流，形成流场方向的根本性转换 [Yoon 2024, pp. 5-7]。**适用条件**：渗透率极低（<1×10⁻¹⁶ m²）的结晶岩，罐体释热满足式(1)–(2)，边界压力梯度小（0.001）。**证据**：压力峰值1.68×10⁷ Pa，温度峰值∼69°C，流线转向图。**限制**：二维模型，未考虑区域三维地形和应力-渗流耦合。
- **Claim 2**：单裂隙与区域流场的相对方向控制裂隙流速的时间演化：径向流阶段平行于流场的水平裂隙流速最高，浮力对流阶段平行于垂向流的垂直裂隙流速可能反超 [Yoon 2024, pp. 7-8]。**适用条件**：裂隙位于热源侧方100 m，裂隙开度与渗透率模型隐含特定立方关系（未从片段确认），单裂隙隔离于其他裂隙。**证据**：0°与90°裂隙的平均流速时序曲线交叉。**限制**：结果可能依赖于裂隙等效渗透率模型和裂隙带宽度，未评估裂隙间距和网络效应。
- **Claim 3**：EDZ因高渗透率（1×10⁻¹⁶ m²）和紧邻热源，可产生比初始流场高5个数量级的峰值流速，且压力消散后仍保留较高流速直至温度降低 [Yoon 2024, pp. 7-7]。**适用条件**：EDZ渗透率比母岩高1个数量级以上，位于热传导显著区域。**证据**：EDZ峰值流速1.88×10⁻¹ m/yr vs. 初始1.45×10⁻⁵ m/yr。**限制**：EDZ孔隙度和渗透率在模型中为定值，未考虑裂缝自愈合或时效变化。
- **Claim 4**：早期阶段裂隙网络的平均流速不随密度和连通性单调增加，而主要通过少数优先路径发生流动 [Yoon 2024, pp. 1-2]。**适用条件**：DFN中压力驱动径向流瞬态阶段。**证据**：摘要陈述。**限制**：DFN具体参数范围和统计度量未从片段确认，需更多模型实现和敏感性分析验证。

## Candidate Concepts
- [[fractured aquifer]] / [[fracture flow]] / [[preferential flow pathway]]
- [[discrete fracture network (DFN)]]
- [[excavation damaged zone (EDZ)]]
- [[buoyancy-driven convection]] / [[density-driven flow]]
- [[heat transfer in porous media]]
- [[hydraulic fracturing]] / [[fracture connectivity]]
- [[geologic disposal of high-level radioactive waste]] / [[natural barrier system]]

## Candidate Methods
- [[numerical simulation]] / [[2-dimensional thermal-hydrological coupling]]
- [[darcys law with buoyancy term]]
- [[effective thermal conductivity geometric mean]]
- [[finite element fracture flow]]
- [[model order reduction for THM]]
- [[pressure-temperature sequential coupling in fractured media]]

## Connections To Other Work
- 文中直接引用的相关研究包括：Malbrain et al. (1982) 的释热公式 [Yoon 2024, pp. 3-4]；Harris et al. (2015)、Runchal and Maini (1980)、Tsang and Pruess (1987) 在浮力对流预测上的工作 [Yoon 2024, pp. 6-7]；Long et al. (1982) 关于裂隙网络表征的重要性 [Yoon 2024, pp. 2-2]。
- 从主题上，本文与以下方向可建立连接：
  - 裂隙岩体热-水-力耦合数值模拟（如 [[THM coupled model in crystalline rock]]）
  - 裂隙方向对热致浮动流的影响（如 [[fracture orientation and convective flow]]）
  - EDZ水力特性演化（如 [[permeability evolution in EDZ]]）
  - 裂隙网络密度与连通性对溶质运移的控制（如 [[DFN connectivity and flow channeling]]）
  - 处置库热输出时序建模（如 [[decay heat source term in repository simulation]]）

## Open Questions
- 三维模型中裂隙优先通道、热对流混合过程的差异性及其对流速空间分布的定量影响未从索引片段中确认。
- 更高密度与连通性裂隙网络在早期压力驱动阶段为何未增加平均流速？其物理机制（如流动通道化与局部压力屏蔽）需进一步分析 [Yoon 2024, pp. 1-2]。
- 模型的长期有效性（>30,000年）以及膨润土相变、裂隙矿物沉淀的反馈效应未涉及。
- 双裂隙和DFN的详细工况与参数敏感性分析结果未在索引片段中呈现，无法判断裂隙交互作用的普适规律。
- 未从索引片段中确认模型是否有验证对比或现场数据支持。

## Source Coverage
本页依据22个索引片段编写，覆盖了论文的摘要、引言、方法（控制方程、参数表、边界条件）、部分结果（单裂隙方向效应、早期与晚期流态转换、EDZ流速）和少量讨论。重要内容如双裂隙结果细节、DFN模拟的全部工况与分析、全面讨论与结论部分未从索引片段中充分获取，可能导致对模型适用范围和结论稳健性的理解不完整。因此，DFN和双裂隙部分的报道是基于有限摘要信息进行的有限推断。
