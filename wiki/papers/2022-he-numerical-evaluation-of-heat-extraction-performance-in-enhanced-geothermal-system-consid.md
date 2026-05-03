---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid"
title: "Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures."
status: "draft"
source_pdf: "data/papers/2022 - Numerical evaluation of heat extraction performance in enhanced geothermal system considering rough-walled fractures.pdf"
collections:
  - "zotero new"
citation: "He, Renhui, et al. \"Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures.\" *Renewable Energy*, vol. 188, 2022, pp. 524-44. doi:10.1016/j.renene.2022.02.067. Accessed 2026."
indexed_texts: "18"
indexed_chars: "87795"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "88146"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003998"
coverage_status: "full-index"
source_signature: "02714661d9ffb9ee9cd4293c8b77d41fbc533c45"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:50:26"
---

# Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures.

## One-line Summary

该研究通过 144 个离散裂隙网络（DFN）模型，对比平行板与粗糙壁面裂隙，结合热-水-力（THM）耦合数值模拟，系统评估了不同裂隙方向、模型尺寸和隙宽非均质度下增强型地热系统（EGS）的采热性能，并提出了定量表征粗糙壁效应的两个比值指标 [He 2022, pp. 1-2] [He 2022, pp. 18-20]。

## Research Question

在 EGS 数值模型中，用粗糙壁面裂隙替代平行板假设是否会显著改变热提取性能？裂隙方向、隙宽大小与分布形式、模型尺寸以及传热系数的取值如何影响该差异？如何量化粗糙壁效应？ [He 2022, pp. 1-3]

## Study Area / Data

研究并非依托某一具体地热田，而是建立理论模型。裂隙粗糙度（JRC）的统计分布形式基于现场实测数据的统计分析：正态分布基于 Oskarshamn/Forsmark 数据 [45]，对数正态分布基于 Bakhtiary 数据 [46] [He 2022, pp. 6-8]。模型计算域为 2D 水平剖面，模拟深度约 3 km，初始温度 200°C，初始压力 30 MPa [He 2022, pp. 8-9]。所有材料参数见表 3 [He 2022, pp. 8-10]。

## Methods

几何模型为二维 DFN，包含三组裂隙方向（C1: 30°/150°; C2: 45°/135°; C3: 60°/120°）和四种模型尺寸（S1: 20 m×20 m, S2: 100 m×100 m, S3: 500 m×500 m, S4: 1000 m×1000 m），裂隙迹长服从正态分布 [He 2022, pp. 4-6]。粗糙壁面裂隙通过水力隙宽表征：e<sub>h</sub> = e<sub>m</sub><sup>2</sup> / JRC<sup>2.5</sup>，机械隙宽 e<sub>m</sub> 取 20 µm、100 µm、500 µm 三种；JRC 分布分为正态（RN）和对数正态（RL）及对应的平均值平行板模型（PN、PL），共计 144 个模型 [He 2022, pp. 6-8]。采用 THM 全耦合控制方程，在 COMSOL Multiphysics 中求解，并用单裂隙解析解与热固结问题验证 [He 2022, pp. 3-4]。边界条件：注水井温度 60°C、压力按 2×10⁴ Pa/m 梯度施加，其余边界隔热、法向位移约束 [He 2022, pp. 8-9]。网格经敏感性分析后约为 40,000 个三角形单元 [He 2022, pp. 8-9]。

## Key Findings

1. 粗糙壁面模型与平行板模型的压力和温度分布特征差异显著，主要由隙宽分布形式决定。裂隙方向越接近流动方向（注入井至采出井），峰值采热速率越高、总采热周期越短 [He 2022, pp. 11-14] [He 2022, pp. 17-18]。
2. 平行板模型的热提取率峰值出现更早且更大，其总热提取量始终高于粗糙壁面模型，而采热持续期更短。定义的 **时间比**（粗糙模型采热时长/平行板时长）与 **热量比**（粗糙模型总吸热量/平行板总吸热量）可定量评价粗糙壁效应 [He 2022, pp. 14-15]。
3. 粗糙壁效应主要受机械隙宽和粗糙度分布影响：e<sub>m</sub> = 20 µm 时，粗糙模型的热量比低至 0.10‑0.55；e<sub>m</sub> = 100 µm 时，RN 模型的热量比为 0.82‑0.86，时间比为 1.65‑1.85，RL 模型相应为 0.94‑0.99 和 1.25‑1.55；e<sub>m</sub> = 500 µm 时，热量比均高于 0.96，粗糙壁效应极小。正态 JRC 分布的粗糙壁效应强于对数正态分布 [He 2022, pp. 15-16]。
4. 传热系数（h）取值对出口水温的影响与模型尺寸有关：模型尺寸越大，不同 h 造成的温度偏差越小；S4 模型中偏差普遍小于 1。对小型模型（如 20 m×20 m），h 的影响不可忽略。动态传热系数与常数系数的结果无显著差异，无需为追求动态描述而增加计算成本 [He 2022, pp. 16-18]。
5. 删除孤立、未连通裂隙的简化 DFN 模型，其温度分布特征与原模型基本一致；但由于考虑 THM 耦合，出口水温曲线存在偏差，且偏差随裂隙与流向夹角增大而减小。当夹角较大时，可使用简化模型以提高计算效率 [He 2022, pp. 18-20]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 平行板模型的热提取率峰值出现更早、峰值更高，总采热期更短 | [He 2022, pp. 14-15] | C1+S3，e<sub>m</sub>=100 µm，RL vs PL | 基于平均水力隙宽 80.39 µm 模型的对比 |
| e<sub>m</sub>=100 µm 时，RN 模型的热量比为 0.82‑0.86，时间比为 1.65‑1.85；RL 模型的热量比为 0.94‑0.99，时间比为 1.25‑1.55 | [He 2022, pp. 15-16] | 所有尺寸和方向，RN/RL 相对于 PN/PL | 图中读出近似范围 |
| e<sub>m</sub>=20 µm 时，RN 模型热量比约 0.10‑0.35，RL 模型约 0.25‑0.55 | [He 2022, pp. 15-16] | 同上 | 粗糙壁效应极显著 |
| e<sub>m</sub>=500 µm 时，所有模型热量比均 >0.96 | [He 2022, pp. 15-16] | 同上 | 粗糙壁效应可忽略 |
| 不同传热系数下，S4 模型（1000 m×1000 m）的出口水温偏差 Δ < 1 | [He 2022, pp. 17-18] | C1，e<sub>m</sub>=100 µm，h 取 20‑3000 W/m²·K | 大尺寸模型中 h 取值影响很小 |
| 简化 DFN 模型与原始模型出口水温的偏差在 C3 模型中几乎可忽略 | [He 2022, pp. 18-20] | C3+S3，e<sub>m</sub>=100 µm，平行板和粗糙壁面 | 裂隙方向偏离流向后简化合理 |

## Limitations

- 模型为二维水平剖面，未考虑三维效应 [He 2022, pp. 4-5]。
- 未包含化学作用与热辐射 [He 2022, pp. 2-3]。
- 仅考虑水作为工作流体、单相流，未对比其他工质 [He 2022, pp. 2-3]。
- 岩石基质简化为均质各向同性，且不考虑初始地应力 [He 2022, pp. 2-3] [He 2022, pp. 8-9]。
- 裂隙渗透率随应力变化的经验公式采用特定参数，未检验不同函数形式的影响 [He 2022, pp. 3-4]。
- 粗糙壁效应的评价基于特定的 JRC‑水力隙宽关系，未验证其他表征方法 [He 2022, pp. 6-8]。

## Assumptions / Conditions

- 岩石基质视为多孔介质，渗透率远小于裂隙，裂隙是主要流动通道 [He 2022, pp. 2-3]。
- 流体流动符合达西定律；工作流体为单相水，始终以液态存在 [He 2022, pp. 2-3]。
- 热交换采用局部热非平衡（LTNE）理论，对流换热由牛顿冷却定律描述 [He 2022, pp. 2-3]。
- 岩石基质温度场由等效热传导方程描述，忽略内部对流项 [He 2022, pp. 3-4]。
- 裂隙渗透率变化服从 k<sub>f</sub> = k<sub>0</sub> exp(-σ<sub>n</sub>' / σ*)，σ* = 10 MPa，初始 k<sub>0</sub> = e<sub>h</sub><sup>2</sup>/12 [He 2022, pp. 3-4]。
- 模型不考虑初始地应力；初始温度 200°C，初始压力 30 MPa [He 2022, pp. 8-9]。
- 注水井温度恒定 60°C，左右边界压力差按 2×10⁴ Pa/m 梯度给定，四周边界法向位移约束，上下边界不透水 [He 2022, pp. 8-9]。
- 裂隙 JRC 统计分布基于 Oskarshamn/Forsmark（正态）和 Bakhtiary（对数正态）现场数据 [He 2022, pp. 6-8]。
- 模拟总时长根据不同模型选取，时间步长 1 天，收敛容差 10⁻⁶ [He 2022, pp. 8-9]。

## Key Variables / Parameters

- **几何与裂隙变量**：模型尺寸（S1‑S4）、裂隙组方向（C1‑C3）、机械隙宽 e<sub>m</sub>（20 µm, 100 µm, 500 µm）、JRC 分布类型（RN, RL）、水力隙宽 e<sub>h</sub> [He 2022, pp. 4-8]。
- **物理参数**：岩石密度 ρ<sub>s</sub> = 2700 kg/m³，比热 C<sub>s</sub> = 1000 J/kg/K，导热系数 λ<sub>s</sub> = 3.0 W/m/K，弹性模量 E = 25 GPa，泊松比 ν = 0.25，热膨胀系数 α<sub>T</sub> = 2.0×10⁻⁶ 1/K，孔隙度 ε = 0.0001，基质渗透率 k<sub>s</sub> = 1×10⁻¹⁸ m²；水的参数见表 3 [He 2022, pp. 8-10]。
- **传热与流动参数**：传热系数 h（常数 3000 W/m²/K 或动态模型），注水温度 60°C，参考温度 T<sub>ref</sub> = 60°C [He 2022, pp. 8-9] [He 2022, pp. 16-18]。
- **评价指标**：平均出口水温 T<sub>out</sub>（式20）、单位长度热提取率 P（式21）、时间比（式22）、热量比（式23）、温度偏差 Δ（式26） [He 2022, pp. 14-15] [He 2022, pp. 17-18]。

## Reusable Claims

- 在 EGS 数值评估中，若将裂隙简化为平行板，会高估采热峰值、总热提取量并缩短采热生命周期；考虑粗糙壁面可更准确评价产能与寿命 [He 2022, pp. 14-15]。
- 粗糙壁效应可通过两个比值指标量化：**时间比**（粗糙/平行板采热时长）和**热量比**（粗糙/平行板总热提取量），二者主要受机械隙宽和 JRC 分布形式控制 [He 2022, pp. 15-16]。
- 当裂隙机械隙宽≥500 µm 时，粗糙壁效应对热提取的影响可忽略；当 e<sub>m</sub> ≤ 20 µm 时，效应极强（热量比可低至 0.1） [He 2022, pp. 15-16]。
- 正常态分布的 JRC（RN）产生的粗糙壁效应强于对数正态分布（RL），表现为更低的热量比和更大的时间比 [He 2022, pp. 15-16]。
- 对于边长 ≥ 1000 m 的模型，出口水温对传热系数取值不敏感，采用常数 h = 3000 W/m²/K 是合理的；但在小尺寸模型（20 m）中，h 的影响不可忽略 [He 2022, pp. 17-18]。
- 当裂隙主方向与流向夹角较大（如 60°/120°）时，使用删除未连通裂隙的简化 DFN 模型所造成的出口水温偏差可忽略不计，可用于高效计算；但在裂隙近顺流向条件下，偏差显著，不宜简化 [He 2022, pp. 18-20]。

## Candidate Concepts

- [[rough-walled fracture]]
- [[aperture heterogeneity]]
- [[discrete fracture network (DFN)]]
- [[thermal-hydraulic-mechanical (THM) coupling]]
- [[local thermal non-equilibrium (LTNE)]]
- [[joint roughness coefficient (JRC)]]
- [[heat extraction rate]]
- [[time ratio index]]
- [[heat recovery ratio index]]
- [[simplified DFN model]]
- [[convective heat transfer coefficient]]
- [[mechanical aperture]]

## Candidate Methods

- [[numerical simulation with THM coupling in COMSOL]]
- [[DFN modeling with stochastic aperture distribution]]
- [[two-index quantitative evaluation of rough-walled effect]]
- [[dynamic vs constant heat transfer coefficient analysis]]
- [[simplified DFN model for computational efficiency]]
- [[JRC-based hydraulic aperture characterization]]
- [[mesh sensitivity analysis for DFN models]]

## Connections To Other Work

- 本研究在离散裂隙网络建模中直接考虑了粗糙壁面，不同于多数将裂隙视为平行板的研究（如 Sun et al. [13], Yao et al. [14]），弥补了平行板假设的不足 [He 2022, pp. 1-3] [He 2022, pp. 14-15]。
- 采用了 Zhao [28] 提出的基于流速的归一化传热系数模型，并利用 Bai et al. [42] 的实验数据拟合了新的动态关系式 h/h₀ = 1.28(v/v₀)^0.51 [He 2022, pp. 16-17]。
- 与 Luo et al. [36] 和 Chen et al. [37] 类似，在宏观 DFN 中引入粗糙壁面，但本研究通过系统改变尺寸、隙宽、方向等参数，并提出了定量评价指标 [He 2022, pp. 2-3] [He 2022, pp. 15-16]。
- 结果印证了 Shi et al. [35] 的结论：平行板模型会高估 EGS 产能，同时指出该高估程度取决于裂隙方向与隙宽大小 [He 2022, pp. 2-3] [He 2022, pp. 14-16]。
- 对 Chen et al. [37] 和 Li et al. [38] 的粗糙壁面模型进行了扩展，证明动态传热系数并非必要，且大小模型的 h 敏感性不同 [He 2022, pp. 16-18]。

## Open Questions

- 文中未讨论的方面：三维模型中粗糙壁效应的表现、多相流或超临界工质的影响 [He 2022, pp. 2-3]。
- 粗糙壁效应的评价指标是否适用于更复杂的裂隙网络（如包含天然与人工裂隙并存）有待验证 [He 2022, pp. 2-3]。
- 传热系数在不同尺度模型中的最佳取值规则仍需进一步明确，尤其对中等尺寸模型（如 100 m） [He 2022, pp. 17-18]。
- 单一裂隙 JRC‑水力隙宽关系（e<sub>h</sub> = e<sub>m</sub><sup>2</sup>/JRC<sup>2.5</sup>）在实际裂隙网络中的适用性及不确定性未探讨 [He 2022, pp. 6-8]。

## Source Coverage

所有 18 个非空索引片段均已处理，覆盖全文所有内容。按数据块计覆盖率为 1.0，按字符计覆盖率为 1.003998（编译后字符数 88146 vs 索引字符数 87795）。
