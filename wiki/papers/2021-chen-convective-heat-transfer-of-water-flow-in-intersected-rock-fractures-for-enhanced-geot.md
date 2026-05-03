---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-chen-convective-heat-transfer-of-water-flow-in-intersected-rock-fractures-for-enhanced-geot"
title: "Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction."
status: "draft"
source_pdf: "data/papers/2022 - Convective heat transfer of water flow in intersected rock fractures for enhanced geothermal extraction.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Chen, Yuedu, Zhihong Zhao, and Huan Peng. \"Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2021."
indexed_texts: "12"
indexed_chars: "57853"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "58116"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004546"
coverage_status: "full-index"
source_signature: "426b566094c90c751fc2db56a0f2c59fe983c7b0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:08:58"
---

# Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.

## One-line Summary
本文通过构建一系列三维交叉粗糙裂隙模型进行流动换热模拟，揭示了死端裂隙（DEF）的产状（交叉角度、隙宽、长度及连通性）对增强型地热系统（EGS）中换热行为的影响，发现粗糙DEF中环状流线导致椭圆状冷锋分布，且90°交叉角及增加交叉DEF长度和连通性有利于提高热提取。[Chen 2021, pp. 1-1]

## Research Question
研究核心问题：（1）理解三维交叉粗糙裂隙（真实非均质隙宽）中的对流换热行为，尤其当存在死端天然裂隙时；（2）确定影响交叉裂隙换热的主要几何因素，包括交叉角度、隙宽、长度和连通性，以指导增强型地热系统裂隙网络优化设计。[Chen 2021, pp. 2-3]

## Study Area / Data
本研究为数值模拟研究，无特定野外场地。建立的几何模型基于实验室尺度的巴西劈裂诱发张裂隙和天然花岗岩裂隙的扫描数据，通过升尺度构建边长2 m的立方体计算域，内嵌一条水平主流通道（MFF）与一条或多条交叉死端裂隙（DEF）。初始温度为423.15 K（对应约4000 m深储层），注水温度313.15 K。边界条件：顶、底、背面为恒温423.15 K，裂隙面及侧面为不透水和无滑移边界，出口、入口及前端为绝热。[Chen 2021, pp. 3-4]

## Methods
采用三维交叉裂隙模型进行流动-换热瞬态模拟，假设花岗岩基质相对于裂隙为不可渗透、局部热平衡（LTE）、低流速下惯性力可忽略，控制方程采用Stokes方程和能量守恒方程，并通过温度依赖的流体物性实现水-热耦合。模型验证采用二维单裂隙解析解，最大误差仅1.4%。网格数为约1400万四面体单元。模拟时长240 h，时间步长0.3 h。设置三个模拟情景：
- 情景 I：改变交叉角（20°, 55°, 90°, 125°, 155°），对比板状与粗糙裂隙，注水速度0.0002、0.002、0.2 m/s。
- 情景 II：改变DEF的机械隙宽（0.082~0.432 mm）和长度（2~15 mm），注水速度0.0002、0.002、0.02 m/s。
- 情景 III：改变交叉DEF的数量与连通性（单条、三条不连通、七条连通），注水速度同上。
输出参数：平均出口水温 \(T_{out}\) 和总产热量 \(Q\)，以及相应增量 \(ΔT_{out}\) 和产热比 \(Q_r\)。[Chen 2021, pp. 3-7]

## Key Findings
1. 交叉DEF显著影响裂隙岩体内的流动与换热。板状裂隙中流线均匀，而粗糙裂隙中出现沟流效应；粗糙DEF中产生环状流线，导致冷锋呈不规则椭圆形分布。[Chen 2021, pp. 7-10, 14-14]
2. 使用板状裂隙模拟会误估温度演化和热产量。粗糙模型中 \(ΔT_{out}\) 和 \(Q_r\) 随交叉角变化显著，在90°时达到最大，随交叉角减小而降低；且粗糙度有利于增加换热量。[Chen 2021, pp. 10-12]
3. 延长被激活的DEF长度有利于增加热产量，但增大DEF隙宽并非必要；仅增加非连通的交叉DEF数量对热提取提升有限，将这些DEF与MFF连通形成流动网络才能显著提高热产量。[Chen 2021, pp. 12-14]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 粗糙DEF中出现环状流线，导致不规则椭圆冷锋分布 | [Chen 2021, pp. 7-10] | 交叉角90°，注水速度0.002 m/s | 沟流效应加剧非均匀降温 |
| 粗糙模型中 \(ΔT_{out}\) 和 \(Q_r\) 在90°交叉角时最大 | [Chen 2021, pp. 10-12] | 情景I，粗糙模型，3种注水速度 | 板状模型变化不明显 |
| 增大DEF隙宽（0.082→0.432 mm）对温度分布影响很小，\(ΔT_{out}\) 和 \(Q_r\) 先降后平 | [Chen 2021, pp. 12-14] | 情景II，0.02 m/s | 较大隙宽导致DEF内流速降低 |
| 延长DEF长度（2→15 mm）显著扩大低温区，\(ΔT_{out}\) 和 \(Q_r\) 上升 | [Chen 2021, pp. 12-14] | 高注水速度下更明显 | 更长裂隙增加换热面积且流速更高 |
| 连通交叉DEF（M2）比孤立DEF（M1）显著提升 \(ΔT_{out}\) 和 \(Q_r\) | [Chen 2021, pp. 14-14] | 情景III，0.002 m/s、0.02 m/s | 仅增加非连通DEF数量效果有限 |

## Limitations
- 本研究仅考虑水-热（HT）耦合，未考虑热-力或孔隙弹性效应（THM耦合），可能忽略应力引起的隙宽变化。[Chen 2021, pp. 14-14]
- 模型尺寸（2 m）和时间尺度（10 d）较小，井下实际应用需进行升尺度研究。[Chen 2021, pp. 14-14]
- 未讨论注入井和生产井与裂隙网络的连通性影响。[Chen 2021, pp. 14-14]

## Assumptions / Conditions
- 花岗岩基质相对于裂隙可视为不可渗透，裂隙为流体和热量传输的主要通道。[Chen 2021, pp. 2-3]
- 采用局部热平衡（LTE）假设，即裂隙表面与流体在局部点温度连续。[Chen 2021, pp. 2-3]
- 流动为低雷诺数，惯性力可忽略，控制方程简化为Stokes方程。[Chen 2021, pp. 2-3]
- 模拟初始温度为423.15 K，注水温度313.15 K；流体物性随温度变化。[Chen 2021, pp. 3-4]
- 裂隙几何为升尺度自实验室扫描数据，MFF为张裂隙，DEF为天然裂隙表面。[Chen 2021, pp. 3-4]
- 边界条件：裂隙面不透水、无滑移，侧面绝热，顶/底/背面恒温。[Chen 2021, pp. 3-4]

## Key Variables / Parameters
- 几何变量：交叉角（20°, 55°, 90°, 125°, 155°）；DEF机械隙宽（0.082, 0.232, 0.382, 0.432 mm）；DEF长度（2, 5, 10, 15 mm）；DEF数量及连通性（单条、三不连通、七连通）。[Chen 2021, pp. 4-7]
- 注入水流速：0.0002 m/s、0.002 m/s、0.02 m/s（情景I含0.2 m/s）。[Chen 2021, pp. 4-7]
- 输出变量：平均出口水温 \(T_{out}\)、总产热量 \(Q\)、水温增量 \(ΔT_{out}\)、产热比 \(Q_r\)。[Chen 2021, pp. 7-7]
- 物性参数：花岗岩密度2643 kg/m³，比热1000 J/(kg·K)，热导率2.4 W/(m·K)。[Chen 2021, pp. 3-4]

## Reusable Claims
- 在粗糙死端交叉裂隙中，环状流线导致冷锋呈不规则椭圆形扩展，该现象在低流速（0.002 m/s）下已明显。[Chen 2021, pp. 7-10]
- 与板状裂隙相比，粗糙裂隙的 \(ΔT_{out}\) 和 \(Q_r\) 更高，表明粗糙度对热提取有增益作用。[Chen 2021, pp. 10-12]
- 当主流裂隙与死端裂隙的交叉角为90°时，热产量达到最大，随交叉角减小而递减；该规律在粗糙模型中表现明显，板状模型中不显著。[Chen 2021, pp. 10-12]
- 延长DEF被激活的长度可提升热产量，而增大其隙宽并无明显收益；延长长度同时提高了DEF内流速和换热面积。[Chen 2021, pp. 12-14]
- 仅增加不与主流裂隙连通的DEF数目对热提取提升微小；将DEF与主流裂隙连通形成网络可显著增加热产量。[Chen 2021, pp. 14-14]
- 低流速下交叉角对温度场演化影响很小；高流速下交叉角的影响放大。[Chen 2021, pp. 10-10]

## Candidate Concepts
- [[死端裂隙（Dead-End Fracture, DEF）]]
- [[三维交叉粗糙裂隙]]  
- [[沟流效应（Channeling flow）]]  
- [[对流换热]]  
- [[冷锋椭圆分布]]  
- [[裂隙网络连通性]]  
- [[粗糙度增强换热]]  
- [[局部热平衡（LTE）]]  
- [[增强型地热系统（EGS）]]

## Candidate Methods
- [[三维裂隙流动换热模拟]]  
- [[Stokes方程低雷诺数裂隙流]]  
- [[水-热（HT）耦合瞬态求解]]  
- [[基于扫描数据的裂隙几何升尺度建模]]  
- [[温度依赖流体物性参数耦合]]  
- [[出口水温与总产热量评估指标]]  
- [[1400万四面体网格裂隙精化]]

## Connections To Other Work
- 前人研究多将裂隙简化为光滑平行板或均匀粗糙面，忽略真实非均质隙宽导致的沟流效应，本文证实异质隙宽显著影响换热评估，与 Chen and Zhao (2020) 的结论一致。[Chen 2021, pp. 1-2, 2-3]
- 交叉角对换热的影响与 Ma et al. (2020) 的研究结果相呼应，但本文进一步在三维粗糙裂隙中验证。[Chen 2021, pp. 10-12]
- DEF长度的积极效果与 Qu et al. (2017) 的发现吻合；增加非连通裂隙数量效果有限的结论则部分支持 Shi et al. (2019a) 的观点。[Chen 2021, pp. 12-14]
- 本文指出仅增加DEF数量未必有效，必须形成连通流动路径，这与 Fu et al. (2016) 关于强连通裂隙网络虽降低水力阻抗但不一定提升热产量的讨论形成对比。[Chen 2021, pp. 1-2]

## Open Questions
- 如何将本研究的2 m尺度、10 d周期结果升尺度至实际工程规模？[Chen 2021, pp. 14-14]
- 考虑热-水-力（THM）全耦合时，温度应力引起的裂隙隙宽变化对换热行为的影响如何？[Chen 2021, pp. 14-14]
- 注入井与生产井相对于交叉裂隙网络的位置如何影响热突破和采收率？[Chen 2021, pp. 14-14]
- 周期性改变注采井别能多大程度缓解沟流效应并延长产热寿命？[Chen 2021, pp. 14-14]

## Source Coverage
所有12个非空索引片段均已处理，未遗漏任何原文块。源块覆盖率（blocks）为1.0，字符覆盖率（chars）为1.004546（因片段截取边界可能包含少量重叠，总字符数微超原始片段总和）。文献来源：Chen, Yuedu, Zhihong Zhao, and Huan Peng. “Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.” *Journal of Rock Mechanics and Geotechnical Engineering* 14 (2022): 108–122.
