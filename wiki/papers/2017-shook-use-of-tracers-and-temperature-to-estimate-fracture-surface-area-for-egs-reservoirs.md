---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-shook-use-of-tracers-and-temperature-to-estimate-fracture-surface-area-for-egs-reservoirs"
title: "Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs."
status: "draft"
source_pdf: "data/papers/2017 - Use of tracers and temperature to estimate fracture surface area for EGS reservoirs.pdf"
collections:
citation: "Shook, G. Michael, and Anna Suzuki. “Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs.” *Geothermics*, vol. 67, 2017, pp. 40-47. *ScienceDirect*, doi:10.1016/j.geothermics.2016.12.006."
indexed_texts: "8"
indexed_chars: "39939"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "40005"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.001653"
coverage_status: "full-index"
source_signature: "ed902738dafc1fcbaa0bbe26e68b6ef12be4aea1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:50:08"
---

# Use of Tracers and Temperature to Estimate Fracture Surface Area for EGS Reservoirs.

## One-line Summary
提出了一个利用保守示踪剂与温度解析解的工作流程，先通过示踪测试估计裂缝的扫掠孔隙体积和流动几何形态，再迭代求解单裂隙或多裂隙（含损伤带）系统的换热表面面积，以支撑EGS储层设计和长时行为优化。[Shook 2017, pp. 1-2; pp. 3-4; pp. 7]

## Research Question
如何同时利用示踪剂和温度数据，在解析框架下估算EGS储层的关键不确定性——控制换热的裂缝表面面积A，并考虑存在多个裂缝或损伤带时的叠加方法？[Shook 2017, pp. 1-2; pp. 3-4]

## Study Area / Data
- **模型设置**：单井对垂直裂缝组，裂缝半长99 m，高75 m，孔径0.02 m，基质宽642.66 m以保证半无限介质；井仅完井于裂缝。  
- **岩石与流体性质**：见表1（密度、比热容、热导率等），初始温度200 °C，初始压力9800 kPa，注入水温度25 °C，注入速率2 kg/s。  
- **示踪剂注入方案**：先注入纯水1小时，再注入含10%示踪剂的水1小时，随后切换为追踪水（无示踪剂）长期注入。  
- **案例1**：单一裂缝，渗透率恒定1.0×10⁻¹¹ m²；案例2：一条主裂缝两侧各有一个损伤带，渗透率和孔隙度不同（见表1）。[Shook 2017, pp. 3-4; pp. 4-5]

## Methods
1. **示踪测试获取孔隙体积与流动几何**  
   - 通过保守示踪剂段塞测试，利用公式(8)计算井对间总扫掠孔隙体积\(V_S\)，其中校正了示踪剂采出比例以避免多井和泄漏影响。  
   - 构建动态流动容量–储存容量（F‑Φ）曲线（公式(11)(12)），由其斜率陡变点识别不同流动路径（损伤带或不同裂缝），并分配各路径的体积流量和孔隙体积（公式(9)(10)）。  
   - 单一F‑Φ曲线斜率恒定表明单一流动路径；斜率变化则指示多条路径。[Shook 2017, pp. 2-3; pp. 3-4]

2. **温度解析解与表面面积反算**  
   - 基于Gringarten & Sauty (1975)的解析解，将产出温度\(T_w\)表示为可测变量（热物性、\(V_p\)）和控制变量（q）的函数(7)，未知量为表面面积A。  
   - 对单裂隙，直接迭代优化A使模型温度\(T_M\)与现场温度\(T_F\)的残差平方和（目标函数OF）最小。  
   - 对多流动路径（如损伤带），先利用F‑Φ曲线获得各路径的\(q_i\)和\(V_{pi}\)，再对每个路径分别使用(7)式，最后按流量加权叠加温度历史（公式(15)），进而联合反算各路径的表面面积。[Shook 2017, pp. 2-3; pp. 3-4]

3. **验证与放大流程**  
   - 用TOUGH2生成“真实”油藏响应（包括示踪物浓度、温度史），再根据上述工作流反推表面面积，并与输入的“真实”值比较。  
   - 进一步利用估计的裂缝性质，优化注入速率以满足允许温度降幅的约束，并扩展到多井多裂缝组，给出热功率与电功率的计算方法（公式(16)(17)）以及最小裂缝组间距公式(18)。[Shook 2017, pp. 3-4; pp. 6-7]

## Key Findings
- 工作流能准确估计扫掠孔隙体积：例1相对误差2.2%，例2相对误差约2.66%。  
- 单一裂缝情况下，随温度数据截止时刻变短（\(T_D\)从1降至0.05），表面面积估算值从14492.8 m³变为13442.3 m³，误差在2.4%~9.5%之间（真实值14,850 m²）。  
- 存在损伤带时，采用F‑Φ曲线分配和叠加反演，联合估计的表面面积为15,269.1 m²（\(T_D=0.5\)），相对误差仅-2.82%，最大绝对误差0.99 °C。若实验过早终止（仅测到25%温度变化），所估表面面积将高估晚期温度，凸显数据充分采集的必要性。  
- 利用估计的性质进行速率优化：可以找到在两年或一年内温度降幅不超10%的最大注入速率，并证实更高早期功率与长期可持续性之间存在权衡。  
- 尺度放大可行：通过叠加多个裂缝组（满足最小间距）和多对生产井，可计算累积发电量以辅助设计。

[Shook 2017, pp. 4-5; pp. 5-6; pp. 6-7]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 示踪测试计算的\(V_S\)=130.76 m³（真实值133.65 m³），相对误差2.2% | [Shook 2017, pp. 4] | 单一裂缝，k=1e-11 m²，注入2 kg/s，示踪剂1小时 | 示例1基础状况 |
| 利用完整温度史（\(T_D=1\)）估得A=14492.8 m²（真实14850 m²），误差2.4%；若只用到\(T_D=0.05\)，A=13442.3 m²，误差9.5% | [Shook 2017, pp. 4, Table 2] | 同示例1，示踪-温度联合反演 | 随截止时刻提前，误差增大但仍在可接受范围 |
| 示例2（主裂缝+两损伤带）F‑Φ曲线分配三个流径，联合反演表面面积：当\(T_D=0.5\)时，\(A_{est}=15269.1\) m²，相对误差‑2.82%，最大温度误差0.99 °C | [Shook 2017, pp. 5, Table 4] | 三流径，不同k与φ，叠加温度解 | 方法在非均质条件下依然准确 |
| 利用估算参数进行速率优化：可找出使2年期温度降≤10%的最大注入速率，预测的温度曲线与TOUGH2“真实”曲线吻合良好 | [Shook 2017, pp. 5-6, Fig. 8] | 例2特性，单井对，优化注入速率为约束 | 可直接用于早期设计 |
| 多井多裂缝组叠加时，裂缝组间距需满足\(L = 4 \sqrt{K_R t / (\rho C_p)_T}\)，以防温度前缘相互干扰 | [Shook 2017, pp. 6-7, Eq. 18] | 半无限边界要求 | 否则解析解过于乐观 |

## Limitations
- 方法假设基岩无渗透率，即不存在流体漏失；若基质有渗透性导致漏失，当前解析解不适用。  
- 多个裂缝组（fracture packs）必须布置得足够远，确保温度前缘在关注时间内不会相互干扰，否则半无限边界条件被破坏。  
- 现场测试需要在大量热量被采出之前、以低于破裂压力的速率进行，且持续时间足够长，以便获取充分的数据（尤其是温度出现明显变化）来可靠估计表面面积；早终止测试会高估晚期温度。  
- 仅针对单对井的裂缝系统进行了验证；多井多裂缝组的放大虽给出原理，但未在文中用数值模型证实。  
- 假设热物性为常数，尽管文献指出其引入约10%误差，但未在文中详细检验对表面面积估算的影响。

[Shook 2017, pp. 1-2; pp. 7-8]

## Assumptions / Conditions
- 裂缝内的流动为一维，岩石基质仅发生热传导，无对流。  
- 使用Gringarten & Sauty (1975)解析解所依赖的半无限边界条件（\(z\to\infty\)时\(T_R=T_I\)）。  
- 裂缝孔隙度\(\phi\)的影响是二阶的，研究中取0.7‑0.95均未见明显差异。  
- 注入和产出速率固定为2 kg/s（验证算例），且注入压力不超过岩石破裂压力。  
- 示踪剂为保守性，无吸附或反应损失，可用于计算扫掠孔隙体积和F‑Φ曲线。  
- 在叠加多流径温度解时，假设各流径的流体混合充分，产出温度可按流量加权平均。  
- 当扩展至多个裂缝组时，假定每组裂缝性质相同（对称注入）以简化计算。

[Shook 2017, pp. 2-3; pp. 6-7]

## Key Variables / Parameters
- \(A\)：裂缝表面面积，m²（主待估量）。  
- \(V_p\)：裂缝孔隙体积，m³（由示踪测试的\(t^*\)和q求得）。  
- \(q_i, V_{pi}\)：第i条流径的体积速率和孔隙体积（通过F‑Φ曲线分配）。  
- \(T_w(t), T_R(z,t)\)：裂缝内水温与岩石温度，°C。  
- \(\kappa = K_R/(\rho C_p)_R\) 等热物性（比热容、密度、热导率）。  
- \(t^*, \tau\)：平均停留时间与单条流线的停留时间，由F‑Φ斜率给出。  
- \(F, \Phi\)：动态流动容量与储存容量，用于识别多流径并分配属性。  
- \(T_D\)：无量纲温度，决定数据截止程度。  
- \(L\)：裂缝组最小间距，m。

[Shook 2017, pp. 1-3; pp. 6-7]

## Reusable Claims
- 将Gringarten‑Sauty温度解显式表达为可测量（\(V_p\)、热物性）或可控制（q）的形式，可使表面面积A成为唯一未知数，配合非线性求解器直接估计。  
- 保守示踪剂测试结合F‑Φ曲线不仅能给出总扫掠孔隙体积，还能分辨出具有不同停留时间的流动单元（裂缝或损伤带），从而为多流径叠加提供定量输入。  
- 当存在多个流动通道时，可分别对每条通道使用一维解析解，然后按流量加权叠加所得温度曲线，实现表面面积的联合反演，该方法在含两个损伤带的算例中表现良好（相对误差约3%）。  
- 现场实验中，如能维持注入速率直至产出温度产生明显变化（例如\(T_D<0.5\)），即可获得较可靠的表面面积估计，并有能力预测长期热产出。  
- 基于估计的表面面积和孔隙体积，可优化注入/产出速率以满足特定温度降约束，并可直接用于计算多井多裂缝组的总热功率和电功率（利用Moon & Zarrouk 2012的效率公式）。  
- 缩放至多裂缝组时，必须通过特征热扩散长度公式\(L = 4\sqrt{K_R t / (\rho C_p)_T}\)确保裂缝组间间距，否则解析解将过度乐观。

[Shook 2017, pp. 2-4; pp. 6-7]

## Candidate Concepts
- [[EGS reservoir]]  
- [[fracture surface area]]  
- [[flow geometry]]  
- [[F‑Phi curve]]  
- [[tracer mean residence time]]  
- [[pore volume swept]]  
- [[damage zone]]  
- [[superposition of temperature solutions]]  
- [[semi‑infinite boundary condition]]  
- [[specific surface area]]  
- [[dimensionless temperature]]  
- [[heat mining]]  
- [[fracture pack]]  
- [[conservative tracer]]

## Candidate Methods
- [[analytical solution for fracture-matrix heat transfer]]  
- [[tracer test interpretation using temporal moments]]  
- [[dynamic flow-storage capacity (F‑Φ) analysis]]  
- [[non‑linear solver for surface area estimation]]  
- [[superposition of 1D temperature solutions]]  
- [[injection‑rate optimization under temperature constraint]]  
- [[scale‑up to multiple well pairs and fracture sets]]  
- [[thermal power and electric power calculation]]  
- [[numerical verification with TOUGH2]]

## Connections To Other Work
- Carslaw & Jaeger (1959), Gringarten & Sauty (1975), Lauwerier (1955)：提供了单裂隙-基质中一维换热解析解的原始框架。  
- Stopa & Wojnarowski (2004)：指出常热物性假设引入约10%误差，支持本工作依赖的热物性简化。  
- Robinson & Tester (1984), Robinson et al. (1988)：曾用类似解析表达式通过调节表面面积拟合两EGS项目温度史，并提出需要联合示踪确定裂隙空间分布。  
- Shan & Pruess (2005)：使用扩散性示踪估算比表面面积\(A/V_B\)。  
- Pruess & Doughty (2010)：利用温度作为示踪剂的“吞吐”测试推断热交换面积的变化，但未给出表面面积的直接计算。  
- Dean et al. (2015)：利用阳离子交换和数值模拟估算裂缝表面面积，但依赖模拟参数的准确性。  
- Shook & Forsmann (2005), Shook et al. (2009)：建立了从示踪数据提取动态F‑Φ曲线的方法，用于表征流动几何和非均质性。  
- Wu et al. (2008)：给出F‑Φ曲线斜率等于\(t^*/\tau\)的理论依据，为本工作识别多流径提供基础。  
- Moon & Zarrouk (2012)：提供了二元地热电站的热效率经验公式，用于电功率计算。  
- Pruess (2006)：提出超临界CO₂作为EGS工质，本研究建议可结合工质特性修改工作流。

[Shook 2017, pp. 1-2; pp. 7-8 references list]

## Open Questions
- 若基质存在一定渗透率或流体漏失，现有的解析解和工作流应如何修正？作者指出这需要进一步研究。  
- 本方法是否适用于“增强型”EGS（位于水热型储层侧翼，存在先存裂隙）？利用F‑Φ曲线对裂缝批次的归并可能有助于简化，但仍需验证。  
- 如何在更多种裂缝几何和非均质性条件下（例如密度更复杂的损伤带网络）验证方法的鲁棒性？  
- 现场试验中，是否存在更优的示踪剂注入方案或温度数据采集策略，以缩短测试周期并提高估算精度？  
- 当注入速率本身随时间变化或者储层漏失不可忽略时，第4节提出的速率优化与放大方法是否仍然直接适用？  
- 对于使用不同工质（如超临界CO₂）的EGS，调整工质热物性后，本工作流是否需要额外的标定或修正步骤？

[Shook 2017, pp. 7]

## Source Coverage
所有8个非空索引片段均已处理并编入本页面。覆盖统计：编译源块数8，覆盖率（按块）1.0，按字符覆盖率约1.001653，源签名ed902738dafc1fcbaa0bbe26e68b6ef12be4aea1，核查状态为full-index，单次Markdown编译完成。
