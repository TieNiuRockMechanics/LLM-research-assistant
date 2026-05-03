---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-sun-anisotropy-of-non-darcian-flow-in-rock-fractures-subjected-to-cyclic-shearing"
title: "Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing."
status: "draft"
source_pdf: "data/papers/2025 - Anisotropy of non-Darcian flow in rock fractures subjected to cyclic shearing.pdf"
collections:
  - "zotero new"
citation: "Sun, Zihao, et al. \"Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 6373-87, doi:10.1016/j.jrmge.2024.11.026."
indexed_texts: "15"
indexed_chars: "72207"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:54:52"
---

# Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing.

## One-line Summary
通过循环剪切实验与非达西流实验，揭示了粗糙岩石裂隙中粘性渗透率与惯性渗透率的各向异性演化规律：粘性渗透率差异仅存于正交方向，惯性渗透率差异存于正交与相反两个方向；随着剪切循环增加，正交差异增大、反向差异减小，并据此建立了两种渗透率的定量表征模型 [Sun 2025, pp. 1-2]。

## Research Question
循环剪切作用如何影响单粗糙裂隙中非达西流的各向异性？具体而言，粘性渗透率（kv）和惯性渗透率（ki）在不同方向（X+、X-、Y+、Y-）上的演化规律、以及导致方向差异的控制因素是什么？如何建立能够反映各向异性的渗透率表征模型？ [Sun 2025, pp. 1-2, 6-8]

## Study Area / Data
- 裂隙样本：取自中国山东省某采石场的红砂岩，基质渗透率在10⁻¹⁴~10⁻¹³ m²量级，远低于裂隙渗透率，后续流动实验中基质渗透率可忽略 [Sun 2025, pp. 3]。
- 样本组：共4组（J1–J4），每组6个粗糙裂隙样本（共24个），每个样本经历不同循环剪切次数（j=0~5，表示经历j次循环剪切） [Sun 2025, pp. 4]。
- 实验数据：对每个样本进行循环剪切实验，记录剪切应力、法向位移、剪切位移；剪切后通过3D激光扫描获取上下壁面点云；然后重新组装进行非达西流实验，共480次 [Sun 2025, pp. 4-5]。

## Methods
- 循环剪切实验：法向应力0.8 MPa，剪切位移速率2 mm/min，剪切位移幅度8 mm，沿X+方向初始剪切，自动换向，法向应力伺服控制精度 ±0.001 MPa。位移由LVDT测量 [Sun 2025, pp. 4-5]。
- 非达西流实验：使用Y-1000平流泵，测量各方向（X+、X-、Y+、Y-）在不同流量Q下的压降∇P。基于Forchheimer方程 ∇P = AQ + BQ² 拟合得到粘性系数A和惯性系数B，并通过A = 12μ/(w b_h³)、B = βρ/(w² b_h²) 计算等效水力开度b_h、粘性渗透率k_v = b_h²/12 和 惯性渗透率k_i = 1/(ρ B')（具体转换关系需结合片断推导，本页未完整给出） [Sun 2025, pp. 2-4]。
- 各向异性评价：对k_v定义ε = k_v_X / k_v_Y（正交方向比）；对k_i定义ε_XY = k_i_X+/k_i_Y+、ε_X = k_i_X+/k_i_X-、ε_Y = k_i_Y+/k_i_Y-，分别评价正交和反向差异 [Sun 2025, pp. 6-8]。
- 表面形态参数：采用Z₂（粗糙度一阶导数均方根）表征平行于某一方向的粗糙度，但指出Z₂不适用于描述k_i的四向差异。为此提出新的孔径方向性参数b_ε，该参数基于孔径沿流向扩张区域的比例，仅考虑扩张区域可能形成回流区，通过Grasselli各向异性粗糙度概念建立 [Sun 2025, pp. 8-11]。
- 裂隙模型重构：利用剪切前后点云数据，通过ICP算法对齐初始位置，结合法向位移监测重建不同循环后数字裂隙模型，用以计算Z₂和b_ε [Sun 2025, pp. 10-11]。

## Key Findings
1. 随着剪切循环次数增加，所有方向的k_v和k_i均下降，首次循环后降幅最大，随后趋于稳定，这主要归因于裂隙开度减小 [Sun 2025, pp. 6-8]。
2. 粘性渗透率k_v仅在正交方向（X与Y）存在显著差异，剪切循环越多，正交方向差异（ε）越大，且在4次循环后差异增速减缓，预期趋于稳定值；这是由于剪切沿X方向磨平了顺向突起，降低了流向阻力 [Sun 2025, pp. 6-8]。
3. 惯性渗透率k_i在四个方向（X+、X-、Y+、Y-）均存在显著差异，连线构成不规则形状。随循环增加，正交差异（ε_XY）逐渐增大，而反向差异（ε_X、ε_Y）逐渐减小。原因在于循环剪切主要改变沿流向的孔径分布，使得扩张区减少，收缩区增加，从而影响回流区的形成，导致相反方向的非线性效应差异降低 [Sun 2025, pp. 6-8, 10-11]。
4. 提出了表征k_i方向差异的参数b_ε，该值在四方向上差异明显，并随循环次数增加而减小。b_ε越高，表示孔径快速扩张的比例越大，非达西效应越强，k_i越小 [Sun 2025, pp. 10-11]。
5. 建立了k_v与b_h、以及k_i与b_ε之间的定量关系（具体方程未从索引片段中确认），实现了对非达西流各向异性的表征 [Sun 2025, pp. 1-2, 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 粘性渗透率仅正交方向存在显著差异，惯性渗透率四向均显著差异 | [Sun 2025, pp. 6-8] | 红砂岩粗糙裂隙，法向应力0.8 MPa，剪切幅度8 mm，循环次数0~5 | 基于4组裂隙的测试 |
| 随循环次数增加，k_v正交差异扩大，k_i正交差异亦扩大而反向差异减小 | [Sun 2025, pp. 6-8] | 同上 | 差异用比值ε、ε_XY等量化 |
| Z₂参数不适用于描述k_i的四向差异 | [Sun 2025, pp. 8-10] | 针对粗糙裂隙表面平行于流向的2D剖面计算 | 因k_i需考虑逆流方向的孔径变化 |
| b_ε能较好区分四方向的孔径非均匀性，且随循环下降 | [Sun 2025, pp. 10-11] | 使用Grasselli概念定义，仅计算孔径扩张区 | 需先重建正确数字裂隙模型 |
| k_v = b_h²/12 | [Sun 2025, pp. 10-11] | 基于等效水力开度，假设局部立方律有效 | 为经典平行板模型推广 |

## Limitations
未从索引片段中确认作者是否明确讨论了研究局限。基于实验设计的潜在局限性包括：仅针对单一岩性（红砂岩）和特定法向应力（0.8 MPa）；循环次数最多5次，未能捕获长期稳定行为；实验为实验室尺度，未考虑现场地应力、充填物及多裂隙相互作用；非达西流动实验假定流体为水，未涉及两相或多相流。

## Assumptions / Conditions
- 基质渗透率远低于裂隙渗透率，流动实验中可忽略 [Sun 2025, pp. 3]。
- 法向应力在剪切过程中保持恒定0.8 MPa，剪切位移幅度恒定8 mm，速度2 mm/min [Sun 2025, pp. 4-5]。
- 使用Forchheimer方程描述非达西流，假定Q与∇P的二次型关系适用于所测流量范围 [Sun 2025, pp. 3]。
- 等效水力开度b_h的概念适用，即用具有相同导水能力的平行板裂隙代替粗糙裂隙 [Sun 2025, pp. 3]。
- 在建立k_i表征模型时，假定仅孔径沿流向扩张的区域会形成回流区，从而主导非线性损失；采用Grasselli的各向异性粗糙度框架 [Sun 2025, pp. 10-11]。
- 数字裂隙模型重构基于ICP对齐初始接触位置，并利用法向位移监测数据恢复相应开度，假设点云还原的几何形态代表真实剪切后壁面 [Sun 2025, pp. 10-11]。

## Key Variables / Parameters
- k_v：粘性渗透率（m²） [Sun 2025, pp. 3]
- k_i：惯性渗透率（m） [Sun 2025, pp. 3]
- b_h：等效水力开度（m） [Sun 2025, pp. 3, 10-11]
- A, B：Forchheimer方程的粘性系数和惯性系数 [Sun 2025, pp. 3]
- ∇P：压力梯度；Q：体积流量 [Sun 2025, pp. 1-2, 3]
- ε (k_v_X/k_v_Y)：粘性渗透率正交各向异性系数 [Sun 2025, pp. 6-8]
- ε_XY, ε_X, ε_Y：惯性渗透率各向异性系数，分别对应X+-Y+、X+-X-、Y+-Y- [Sun 2025, pp. 6-8]
- Z₂：表面粗糙度一阶导数均方根 [Sun 2025, pp. 8-10]
- b_ε：孔径方向性参数，表征孔径沿流向扩张的比例 [Sun 2025, pp. 10-11]
- 剪切循环次数 j (0~5) [Sun 2025, pp. 4]

## Reusable Claims
1. **Claim:** 在循环剪切作用下，粗糙裂隙的粘性渗透率k_v表现出显著差异仅出现在正交流动方向之间，而惯性渗透率k_i则在正交与相反两个方向上都存在显著差异。  
   **Conditions:** 红砂岩裂隙，法向应力0.8 MPa，剪切幅度8 mm，沿X方向往复剪切，水流方向为X+、X-、Y+、Y-。  
   **Evidence:** [Sun 2025, pp. 6-8]。  
   **Limitations:** 仅针对该特定岩石和力学条件，不保证在其他岩性或应力下成立；k_v的方向差异评估仅依据X-Y对比。

2. **Claim:** 随着循环剪切次数增加，k_v的正交各向异性（ε）逐渐增大，而k_i的正交各向异性（ε_XY）也增大，但其反向各向异性（ε_X, ε_Y）逐渐减小。  
   **Conditions:** 剪切方向固定为X方向，样本经历1~5次循环。  
   **Evidence:** [Sun 2025, pp. 6-8]。  
   **Limitations:** 未观测到5次以上循环是否稳定，未考虑其他剪切方向的影响。

3. **Claim:** 可以用孔径方向性参数b_ε来表征k_i的方向差异，b_ε越大对应k_i越小，该参数仅统计沿流向孔径扩张区域的比例。  
   **Conditions:** 基于Grasselli的各向异性粗糙度概念，适用于具有非均匀孔径分布的裂隙。  
   **Evidence:** [Sun 2025, pp. 10-11]。  
   **Limitations:** b_ε的实际计算需高精度数字裂隙模型，现场尺度应用尚未验证；模型是否可推广至多相流未讨论。

4. **Claim:** 循环剪切导致沿剪切方向突起磨损、表面顺流向粗糙度降低，这是造成k_v和k_i正交方向差异随循环增大的主要原因。  
   **Conditions:** 剪切方向与流动方向正交时（如剪切沿X，而流沿Y）产生差异，仅单方向剪切。  
   **Evidence:** [Sun 2025, pp. 6-8]。  
   **Limitations:** 未量化磨损量与方向差异的直接关系；若剪切方向变化，结论可能不同。

## Candidate Concepts
- [[Non-Darcian flow]]
- [[Forchheimer equation]]
- [[viscous permeability]]
- [[inertial permeability]]
- [[rock fracture]]
- [[cyclic shearing]]
- [[hydraulic aperture]]
- [[aperture distribution]]
- [[surface roughness]]
- [[anisotropic roughness]]
- [[Z2 parameter]]
- [[recirculation zone]]
- [[cubic law]]

## Candidate Methods
- [[cyclic shear test]]
- [[non-Darcian flow experiment]]
- [[3D laser scanning]]
- [[Forchheimer equation fitting]]
- [[Grasselli's concept for directional roughness]]
- [[iterative closest point (ICP) alignment]]
- [[digital fracture model reconstruction]]
- [[aperture directional parameter (bε)]]

## Connections To Other Work
- 早期研究多利用压降梯度或流速评估裂隙流各向异性，而未直接使用k_v和k_i等内在渗透性质 [Sun 2025, pp. 2]。
- Egert et al. (2021) 提出非达西流各向异性受裂隙开度特征控制，开度越小各向异性越显著；与本研究k_v、k_i随开度减小而变化的趋势相关，但该研究未考察相反方向的差异 [Sun 2025, pp. 2]。
- Torkan et al. (2023) 发现正交方向流速差可达7%，归因于表面形态各向异性 [Sun 2025, pp. 2]。
- 以往对剪切影响的认识多集中在正交方向差异（剪切方向垂直的渗透率大于平行方向），例如 Li et al. (2019), Yang et al. (2019), Cardona et al. (2021) 等 [Sun 2025, pp. 2]。
- 本研究借鉴了Grasselli et al. (2003) 的各向异性粗糙度概念来构建b_ε参数 [Sun 2025, pp. 10-11]。
- 等效水力开度概念源自Zimmerman and Bodvarsson (1996) [Sun 2025, pp. 3]。

## Open Questions
- 当剪切循环次数足够大（ >5）时，k_v和k_i的各向异性是否会达到稳定值？稳定值取决于什么？ [未从索引片段中确认]
- 该方法和模型能否推广到不同岩性、不同法向应力、不同剪切方向或更复杂的裂隙网络？ [未从索引片段中确认]
- 流动中的真实回流区分布与b_ε参数之间的定量关系有待直接验证（如数值模拟或流动可视化），本页片段未提供此类验证 [未从索引片段中确认]
- 非线性流各向异性是否受流体性质（如粘度、密度）影响？ [未从索引片段中确认]

## Source Coverage
本页基于提供的15个索引片段整理，片段主要对应于论文的第1–11页（全文17页），覆盖了摘要、引言（部分）、实验方法、剪切与流动实验结果、以及模型构建的基本思路。具体而言，引言中的文献综述、实验设置、剪切曲线特征、k_v和k_i趋势、各向异性系数演化、以及b_ε定义与计算步骤均有片段支撑。但以下重要内容可能缺失：完整的k_v和k_i表征模型的具体方程形式、模型验证与对比、参数统计分析、讨论部分的更广泛对比或工程启示、结论章节、以及完整的参考文献列表。若需精确提取套用声言或数学关系，建议参考原文后续部分。
