---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-yin-simulation-based-investigation-on-the-accuracy-of-discrete-fracture-network-dfn-represe"
title: "Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation."
status: "draft"
source_pdf: "data/papers/2020 - Simulation-based investigation on the accuracy of discrete fracture network (DFN) representation.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yin, Tingchang, and Qingfa Chen. \"Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation.\" *Computers and Geotechnics*, 2020, doi:10.1016/j.compgeo.2020.103487."
indexed_texts: "13"
indexed_chars: "62121"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:30:45"
---

# Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation.

## One-line Summary
通过模拟裂缝数据采集与二次建模，研究离散裂缝网络表征技术的准确性：几何属性波动小，但部分模型的力学性质与原始模型存在显著差异，表明 DFN 表征在整体上稳健但工程应用需谨慎 [Yin 2020, pp. 1-1].

## Research Question
DFN 表征技术中，基于二维采样窗口获取的裂缝数据经校正后构建的二次 DFN 模型（SCDFN）与原始 DFN 模型（ODFN）在几何和力学性质上的吻合程度如何？该表征方法的准确性和稳健性如何？[Yin 2020, pp. 1-1].

## Study Area / Data
研究区为中国广西某矿 No. 3 矿块，岩石类型为石灰岩。完整岩石单轴抗压强度约 104 MPa，抗拉强度约 4.7 MPa [Yin 2020, pp. 2-3]。裂缝以 NW、ENE、SSE 走向为主，倾角中等到高陡；存在三个关键裂缝组，间距约 0.2–10 m，迹长约 0.5–4 m，裂缝壁主要为平滑至平直 [Yin 2020, pp. 2-3]。通过同质构造域识别方法确认该矿块裂缝分布在统计上均质（所有统计 p 值 > 0.05） [Yin 2020, pp. 2-3]。巷道相互交叉，有利于在不同方位露头上采集裂缝数据以减小方位偏差 [Yin 2020, pp. 2-3]。原始 DFN 模型输入参数参见 Table 1（三个裂缝组的尺寸分布、平均半径、Fisher 分布常数、平均产状及体积密度）[Yin 2020, pp. 3-4].

## Methods
1. **原始 DFN 模型构建**：基于研究区裂缝统计参数，利用 3DEC 生成一个 60 m × 100 m × 50 m 的 ODFN 模型，并进行了与实际迹长图的对比验证 [Yin 2020, pp. 3-4]。
2. **虚拟采样窗口与裂缝数据采集**：在 ODFN 模型内设置虚拟矩形采样窗口（如产状 120°/60°，尺寸 40 m × 27 m），通过旋转 ODFN 模型（旋转角 Δα/Δβ）改变采样窗口方向 [Yin 2020, pp. 3-4]。确定裂缝与窗口的交切线（迹线），输出视倾角、迹长、产状等信息 [Yin 2020, pp. 3-4]。
3. **裂缝数据处理与 SCDFN 模型构建**：
   - 识别裂缝组 [Yin 2020, pp. 4-6]。
   - 基于测得迹长，利用包含 N₀、N₁ 等修正项的公式估计真实平均迹长 μₗ，再反演出裂缝直径的分布（均值和标准差）[Yin 2020, pp. 4-6]。
   - 根据处理后参数生成 SCDFN 模型，通过对比 SCDFN 与 ODFN 模型在相同采样窗口内的迹线图相似性（P20、P21 值及密度、方位几何特征）进行试错校准与验证，直至二者匹配 [Yin 2020, pp. 6-7]。最后旋转 SCDFN 模型以恢复真实裂缝方位 [Yin 2020, pp. 6-7]。
4. **几何与力学性质确定**：
   - 几何 REV 分析：生成尺寸递增的 DFN 模型，观察 P30、P32 等密度指标的波动，确定表征单元体尺寸 [Yin 2020, pp. 7-9]。
   - 力学性质数值试验：构建混合 DEM‑DFN 模型，赋予完整岩石和裂缝材料属性（Mohr‑Coulomb 塑性模型、Coulomb 滑移模型），计算等效弹性模量、抗压强度等；由于大型模型计算困难，采用 Kulatilake et al. 提出的子模型方法，通过递增子模型尺寸并调整黏聚力和摩擦角估算等效力学参数 [Yin 2020, pp. 9-10]。

## Key Findings
- SCDFN 模型的几何属性（如 P30、P32）随模型尺寸增大波动较小，与 ODFN 模型的一致性较好 [Yin 2020, pp. 1-1]。
- 部分 SCDFN 模型的力学属性（如等效弹性模量、强度）与 ODFN 模型有显著差异，表明 DFN 表征虽整体稳健，但工程应用中需谨慎对待其力学预测 [Yin 2020, pp. 1-1]。
- 通过旋转模型和逆旋转校正，能够合理恢复 SCDFN 模型中裂缝的真实产状 [Yin 2020, pp. 6-7]。
- 大尺寸 DFN‑DEM 模型（>20 m）数值实验极耗时且易生成网格失败，需借助子模型近似方法 [Yin 2020, pp. 9-10]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SCDFN 模型几何属性（密度指标）波动不显著，DFN 表征几何稳健性高 | [Yin 2020, pp. 1-1] | 基于研究区三个裂缝组的 DFN，窗口尺寸 40 m × 27 m，产状 120°/60° | 定性判断，具体波动数值见 P30、P32 图（未从片段确认详细数字） |
| 部分 SCDFN 模型力学性质与 ODFN 模型明显不同 | [Yin 2020, pp. 1-1] | 数值试验采用 DEM‑DFN 混合模型，材料属性见表 6、表 7 | 力学差异的具体模型条件未从片段中明确 |
| SCDFN 模型校准后，P20 值均为 0.2796 m⁻²，P21 值分别为 0.6757 m/m² 和 0.6686 m/m²，差异极小 | [Yin 2020, pp. 6-7] | 采样窗口尺寸 40 m × 27 m，产状 120°/60° | 说明迹线密度和总迹长高度一致 |
| 裂缝直径分布反演基于真实迹长分布，用修正公式处理截断偏差 | [Yin 2020, pp. 4-6] | 公式涉及 N₀/N、N₁/N 比值和视倾角 φ | 具体公式 (3a)–(3c) 为片段原文 |
| 研究区裂缝数据统计均质（p>0.05），适合采用统一 DFN 输入参数 | [Yin 2020, pp. 2-3] | 均质性检验方法见 [22] | 为保证表征准确性提供基础 |

## Limitations
- 力学性质评估受限于大尺寸模型的计算可行性，只能通过子模型方法近似等效参数，可能引入额外偏差 [Yin 2020, pp. 9-10]。
- SCDFN 模型校准依赖试错法，调整输入参数范围仅“狭窄”，存在一定的主观性 [Yin 2020, pp. 6-7]。
- 分析基于单一研究站点的裂缝系统和特定岩石力学参数，结论外推性未从片段中确认。
- 未从索引片段中确认讨论部分是否涉及不确定性量化或与其他方法的交叉验证。

## Assumptions / Conditions
- 裂缝形状假设为圆盘（disc-shaped），利用 3DEC 生成 DFN [Yin 2020, pp. 3-4]。
- 裂缝尺寸分布、方位分布等遵循特定概率模型（正态或对数正态，Fisher 分布）[Yin 2020, pp. 1-2]。
- 由采样窗口获得的裂缝数据需经过校正才能用于构建 DFN，校正方法包括尺寸、截断、删节偏差的处理 [Yin 2020, pp. 1-2]。
- SCDFN 模型校准标准是迹线图几何特征（密度、产状）与 ODFN 相似，忽略力学响应的直接匹配 [Yin 2020, pp. 6-7]。
- 数值试验中假设完整岩石和裂缝服从 Mohr-Coulomb 和 Coulomb 滑移模型，采用表 6 和表 7 给出的力学参数 [Yin 2020, pp. 9-10]。
- 子模型方法继承 Kulatilake et al. 的假设：逐级放大时，新的黏聚力和摩擦角与原有裂缝组合可代表等效连续体行为 [Yin 2020, pp. 9-10]。

## Key Variables / Parameters
- **裂缝几何参数**：平均裂缝半径 μ_D，标准差 σ_D，体积密度 λ_v，Fisher 分布常数 κ，平均倾向/倾角 [Yin 2020, pp. 3-4]。
- **采样窗口参数**：方位（如 120°/60°）、尺寸（40 m × 27 m），旋转角 Δα/Δβ [Yin 2020, pp. 3-4]。
- **迹线测量与校正参数**：测得平均迹长 μ_m，真实平均迹长 μ_l，N₀（两端都在窗外的迹线条数）、N₁（一端在窗外）、N（总迹线数），视倾角 φ [Yin 2020, pp. 4-6]。
- **密度指标**：P20（单位面积迹线条数）、P21（单位面积迹线总长）、P30（单位体积裂缝条数）、P32（单位体积裂缝面积）[Yin 2020, pp. 6-7, 7-9]。
- **力学参数**：完整岩石的密度、UCS、σ_t、E、μ、C、φ_r；裂缝的法向刚度 JKN、剪切刚度 JKS、黏聚力 C_f、摩擦角 φ_f [Yin 2020, pp. 9-10]。
- **模型尺寸与 REV**：用于评估几何和力学属性稳定性的递增模型尺寸 [Yin 2020, pp. 7-9]。

## Reusable Claims
- 在裂缝均质性得到验证（p>0.05）的岩体中，基于二维窗口采样并经过科学校正后构建的 DFN 模型，其几何属性（如裂缝线密度、面密度）能够很好地复现原始裂缝网络的统计特征 [Yin 2020, pp. 1-1, 6-7]。**条件**：采样窗口足够大，且产状能够覆盖主要裂缝组以减少方位偏差；**证据**：SCDFN 与 ODFN 的 P20、P21 几乎相等，P30、P32 波动小；**限制**：推广至其他岩性及更复杂裂缝形态（非圆盘）时需额外验证。
- 尽管几何表征稳健，基于 SCDFN 模型的等效力学性质（如弹性模量、强度）可能与真实值之间存在不容忽视的差异，因此在将 DFN 用于岩体工程稳定性分析等力学预测时，应结合原位试验或增加安全冗余 [Yin 2020, pp. 1-1, 9-10]。**条件**：模型尺寸大于 20 m 时计算可能失败，若采用子模型近似，需注意其假设对等效参数的影响；**证据**：部分 SCDFN 力学结果与 ODFN 偏差大；**限制**：未从片段确认偏差的具体量级和发生频率。
- 为了纠正二维采样窗口带来的方位偏差，可通过旋转原始 DFN 模型来完成多方位采样，生成 SCDFN 后再通过逆旋转恢复真实裂缝产状，这种方法能够保持裂缝网络的整体方位结构 [Yin 2020, pp. 3-4, 6-7]。**条件**：需准确记录旋转角度，且裂缝系统具有统计均质性；**证据**：成功构建并验证了 SCDFN 模型；**限制**：仅针对 Fisher 分布假设条件。

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Sampling window bias]]
- [[Representative Element Volume (REV)]]
- [[Fracture size distribution estimation]]
- [[Fracture orientation bias]]
- [[Structural domain homogeneity]]
- [[DEM-DFN hybrid modeling]]
- [[Fracture persistence power law]]
- [[Censoring and truncation biases]]
- [[Equivalent continuum approach]]

## Candidate Methods
- [[Virtual sampling window with model rotation]]
- [[Fisher constant estimation from fracture data]]
- [[Trace length correction methods (N0, N1 formulas)]]
- [[P30 and P32 analysis for REV determination]]
- [[Sub-model method for upscaling mechanical properties (Kulatilake et al.)]]
- [[3DEC discrete element method for DFN]]
- [[DFN model calibration by trace map matching]]

## Connections To Other Work
- 文中引用的 Kulatilake et al. 子模型方法用于解决大尺寸 DFN‑DEM 模型的计算难题 [Yin 2020, pp. 9-10]，隶属于等效连续体方法范畴，可与 [[Equivalent continuum upscaling]] 概念连接。
- 均质结构域识别采用了文献 [22] 的方法，可关联 [[Structural domain identification for rock masses]]。
- 裂缝迹长估计和偏差校正引用了文献 [13–18]，可连接到 [[Fracture bias correction in scanline surveys]] 与 [[Stereology-based fracture parameter estimation]]。
- 未从索引片段中确认与其他具体 DFN 准确性比较研究（如 DFN 与 DFN 井）的直接引文关系。

## Open Questions
- 未从索引片段中确认 SCDFN 模型力学性质偏差的系统性来源（例如是裂缝连通性差异还是应力路径影响）。
- 该研究未讨论 SCDFN 模型在不同窗口尺寸或不同窗口产状下的敏感性，其准确性边界未明确。
- 未从片段中确认是否对不同类型裂缝网络（如非均质或聚类分布）进行了类似分析。
- 文章是否提出了实用的误差控制准则或安全系数建议，未从索引片段中获知。

## Source Coverage
本页面依据该论文的 13 个索引片段撰写，覆盖了摘要、研究区描述、裂缝数据处理方法、SCDFN 模型构建与校准流程、几何与力学性质分析部分。片段未包含完整的讨论、结论及部分附录细节；关于 SCDFN 与 ODFN 力学差异的具体数值、统计检验结果、敏感性分析等可能留存在论文正文中但未见于给出的索引片段。因此，本 Wiki 未能呈现全文的量化细节和部分验证对照。
