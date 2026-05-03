---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-wu-effect-of-temperature-dependent-rock-thermal-conductivity-and-specific-heat-capacity-on"
title: "Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System."
status: "draft"
source_pdf: "data/papers/2023 - Effect of temperature-dependent rock thermal conductivity and specific heat capacity on heat recovery in an enhanced geothermal system.pdf"
collections:
  - "论文"
citation: "Wu, Hui, et al. \"Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System.\" *Rock Mechanics Bulletin*, 2023. DOI: 10.1016/j.rockmb.2023.100045."
indexed_texts: "8"
indexed_chars: "38627"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38777"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003883"
coverage_status: "full-index"
source_signature: "c36fab65ae2a3fbfacfbd8d7a9818eb70cf66128"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:22:29"
---

# Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System.

## One-line Summary
本文通过在单裂隙场尺度增强地热系统（EGS）模型中引入温度依赖的热导率和比热容，发现温度降低导致的热导率上升与比热容下降对热产出具有相反且大致抵消的效应，因此采用室温下测定的恒定热参数可获得可接受的EGS热性能预测。

## Research Question
岩石热导率（\(K\)）与比热容（\(C_p\)）随温度变化如何影响增强地热系统（EGS）的长期热回收性能？在热采过程中，温度下降引起的 \(K\) 增大与 \(C_p\) 减小的综合效应是否显著？[Wu 2023, pp. 1-1, 1-3]

## Study Area / Data
- **模型域**：3000 × 3000 × 3000 m³ 的场尺度三维模型，内含一条直径 800 m 的水平主导裂隙，注入井与生产井间距 500 m [Wu 2023, pp. 3-3]。
- **初始条件**：裂隙深度处初始温度 200 °C，垂直温度梯度 40 °C/km，初始压力 34 MPa（静水压力）[Wu 2023, pp. 3-3]。
- **温度依赖函数**：采用 Fu et al. (2019) 的方程描述热导率-温度关系，Berman and Brown (1985) 的方程描述比热容-温度关系；拟合数据来自 Fu et al. (2019) 的花岗闪长岩热导率实验与 Vosteen and Schellschmidt (2003) 的变质岩比热容实验（方程集1）。敏感性分析中引入另一套对温度更敏感的方程集2 [Wu 2023, pp. 3-3, 5-6]。
- **岩石与水参数**：参考 Table 1，包括基质渗透率 \(1 \times 10^{-16}\) m²，基质孔隙度 0.01，岩石密度 2700 kg/m³，水密度 887.2 kg/m³，水比热容 4460 J/kg/K，水的动力粘度 \(1.42 \times 10^{-4}\) Pa·s 等 [Wu 2023, pp. 3-5]。

## Methods
- **数值平台**：使用 LLNL 开发的 GEOS 多物理场并行仿真平台进行热-水耦合模拟 [Wu 2023, pp. 3-3]。
- **裂隙模型**：分别采用均匀隙宽（0.3 mm）与非均匀隙宽（对数正态随机场，均值 0.3 mm，标准差 0.3 mm，相关长度 100 m）。隙宽层厚度为 4 mm，等效孔隙度 \(\phi = w/H\)，等效渗透率 \(k = w^3/12H\) [Wu 2023, pp. 3-3]。
- **运行条件**：以 20 L/s 注入 50 °C 水（部分情境采用 30 °C 与 70 °C），生产井底压力恒定 34 MPa；模型边界对流体和热量均为不渗透 [Wu 2023, pp. 3-3]。
- **热参数处理**：设置七种对比情形：(1) 恒 \(K\) 与 \(C_p\)（室温或储层温度）；(2) 仅 \(K\) 随 \(T\) 变；(3) 仅 \(C_p\) 随 \(T\) 变；(4) \(K\) 与 \(C_p\) 均随 \(T\) 变。通过热突破曲线与生产寿命评估效应 [Wu 2023, pp. 5-5]。
- **热导率-比热容乘积分析**：在恒 \(K, C_p\) 和变 \(K, C_p\) 条件下对比 \(K \cdot C_p\) 值对生产温度的影响 [Wu 2023, pp. 6-7]。

## Key Findings
1. **温度依赖变化的幅度**：在方程集1下，温度从 200 °C 降至 50 °C 时，\(K\) 增加 20.5%（2.19→2.64 W/m/K），\(C_p\) 减小 12.9%（934.7→814.0 J/kg/K）；采用更敏感的方程集2时，\(K\) 增加 34.8%，\(C_p\) 减小 18.8% [Wu 2023, pp. 5-5, 6-7]。
2. **对热突破曲线的影响**：考虑 \(K(T)\) 使产出温度升高（热传导加速）；考虑 \(C_p(T)\) 使产出温度降低（热传导削弱）；二者效应相反，综合效应相对较小 [Wu 2023, pp. 5-5, 7-7]。
3. **恒室温参数的可接受性**：用室温（20 °C）下的恒定 \(K、C_p\) 预测的产出温度略高于全变参数情形。均匀隙宽时生产寿命（产出温度 <120 °C）被高估 3.9%，非均匀隙宽时高估 6.8%；采用更敏感方程时室温参数仅高估 1.5% [Wu 2023, pp. 5-6, 6-7]。
4. **生产寿命对注入温度的响应**：注入温度越低，温度对比越大，\(K、C_p\) 变化更显著，但热突破更快，生产寿命更短；生产寿命的相对偏差随注入温度升高略有增大 [Wu 2023, pp. 5-6, 6-7]。
5. **\(K \cdot C_p\) 控制热性能**：热产出主要依赖于 \(K \cdot C_p\) 乘积。在温度下降过程中，\(K \cdot C_p\) 仅微增（方程集1下 +5%，方程集2下 +9%），因此室温恒定参数可给出相近的预测。该依赖性与 Gringarten et al. (1975) 的解析解一致 [Wu 2023, pp. 7-7]。

## Core Evidence Table
| Evidence                                                                                       | Source                          | Conditions                                                                               | Notes                                                                                     |
|------------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 温度从 200 °C 降至 50 °C，\(K\) 增加 20.5%，\(C_p\) 减小 12.9%                                | [Wu 2023, pp. 5-5]              | 方程集1，均匀隙宽，注入温度 50 °C                                                       | 发生在注入点附近                                                                          |
| 考虑 \(K(T)\) 的产出温度 > 考虑 \(C_p(T)\) 的产出温度；\(K(T)\) 的影响大于 \(C_p(T)\)            | [Wu 2023, pp. 5-5]              | 通过七种情形的热突破曲线对比                                                             | 均匀与非均匀隙宽均适用                                                                    |
| 室温恒定 \(K, C_p\) 比全变参数高估生产寿命 3.9%（均匀隙宽）与 6.8%（非均匀隙宽）               | [Wu 2023, pp. 5-6]              | 方程集1，注入温度 50 °C，生产温度门槛 120 °C                                             | 生产寿命分别为 23.3 年（变参数）与 24.2 年（室温参数）                                   |
| 采用更敏感方程集2时，室温恒定参数仅高估生产寿命 1.5%                                          | [Wu 2023, pp. 6-7]              | 方程集2，均匀隙宽，注入温度 50 °C                                                       | 变参数寿命 25.9 年，室温参数 26.3 年                                                      |
| \(K \cdot C_p\) 乘积在温度降低过程中仅增加 5%（方程集1）和 9%（方程集2）                       | [Wu 2023, pp. 7-7]              | 温度从 200 °C 至 50 °C                                                                   | 乘积的微小变化解释室温预测的可接受性                                                      |
| 热突破曲线与恒定 \(K \cdot C_p\) 相同的情形几乎重合                                           | [Wu 2023, pp. 7-7]              | 对比温度依赖 \(K, C_p\) 情形与恒定 \(K \cdot C_p\) 情形（如 2080 W·J/m/kg/K²）             | 进一步证明热性能主要由 \(K \cdot C_p\) 控制                                               |

## Limitations
- 未考虑压力变化对 \(K\) 和 \(C_p\) 的影响，仅基于文献中温度效应占主导的结论 [Wu 2023, pp. 1-3, 3-3]。
- 模型为单裂隙场尺度，未涉及复杂裂隙网络、多场耦合（如力学变形、化学作用）的影响。
- 裂隙开度的非均匀性仅考虑了单一统计实现，未评估不确定性范围。
- 温度依赖方程仅采用两组经验拟合，未覆盖全部岩石类型与温度区间可能的非线性特征。

## Assumptions / Conditions
- 静水压力初始场，垂直温度梯度 40 °C/km [Wu 2023, pp. 3-3]。
- 注入速率恒定 20 L/s，产出井底压力恒定 34 MPa [Wu 2023, pp. 3-3]。
- 模型边界对流体和热量均为不渗透 [Wu 2023, pp. 3-3]。
- 水与岩石基质的热物理参数（除 \(K, C_p\) 外）均设为恒定（参见 Table 1）[Wu 2023, pp. 3-5]。
- 生产寿命定义为产出温度降至 120 °C 的时刻 [Wu 2023, pp. 5-6]。

## Key Variables / Parameters
- 岩石热导率 \(K\)（随温度变化）
- 岩石比热容 \(C_p\)（随温度变化）
- 裂隙开度（均匀与非均匀分布）
- 注入温度 \(T_{inj}\)（30, 50, 70 °C）
- 岩石温度 \(T\)
- \(K \cdot C_p\) 乘积
- 生产温度（产出水温）
- 生产寿命（产出温度跌破 120 °C 的时间）

## Reusable Claims
1. **室温参数可用性**：对于温度降幅典型的单裂隙 EGS（如初始 200 °C、注入 50 °C），假定室温（20 °C）下测定的恒定 \(K\) 和 \(C_p\) 进行热模拟，所得热突破曲线与考虑全变参数的结果相差很小，生产寿命的高估在 7% 以内（原文均匀隙宽 3.9%，非均匀隙宽 6.8%）；若 \(K, C_p\) 对温度更敏感，高估可能进一步缩小至 1.5%。[Wu 2023, pp. 7-7]
2. **\(K \cdot C_p\) 主导性**：单裂隙 EGS 的长期热产出主要受控于热导率与比热容的乘积 \(K \cdot C_p\)。当温度下降导致 \(K\) 升、\(C_p\) 降时，乘积仅微幅变化（+5%~+9%），因此热性能对温度依赖的 \(K\) 和 \(C_p\) 并不敏感。[Wu 2023, pp. 7-7]
3. **效应抵消**：温度依赖的 \(K\) 增大（正效应）与 \(C_p\) 减小（负效应）在热产出上相互抵消，使得单独考虑某一参数的恒定假设可能引入显著偏差，但若同时采用室温恒定值则可获得工程可接受的预测。[Wu 2023, pp. 7-7]
4. **注入温度影响**：降低注入温度虽加剧 \(K、C_p\) 变化幅度，但同时加快热突破，缩短生产寿命；在标准生产寿命评估中，温度依赖参数引入的相对偏差随注入温度升高而略增。[Wu 2023, pp. 5-6]

## Candidate Concepts
- [[enhanced geothermal system]]
- [[fracture reservoir]]
- [[temperature-dependent thermal conductivity]]
- [[specific heat capacity temperature dependence]]
- [[thermal breakthrough curve]]
- [[production life span]]
- [[K·Cp product]]
- [[uniform aperture]]
- [[heterogeneous aperture]]
- [[field-scale EGS model]]
- [[thermo-hydro coupling]]

## Candidate Methods
- [[GEOS simulator]]
- [[single-fracture model]]
- [[sequential gaussian simulation for aperture]]
- [[temperature-dependent K and Cp parameterization]]
- [[comparative case analysis (constant vs. variable K/Cp)]]
- [[thermal breakthrough curve analysis]]
- [[production life span calculation from threshold temperature]]

## Connections To Other Work
- 引用 Lee and Deming (1998) 汇总的 117 组热导率数据及六种温度修正方程，证实热导率随温度升高而降低 [Wu 2023, pp. 1-3]。
- 引用 Vosteen and Schellschmidt (2003) 的多种岩石热导率、热容量实验，强调温度对热参数的压倒性影响 [Wu 2023, pp. 1-3]。
- 引用 Fu et al. (2019) 的花岗岩类高温高压热导率数据，用于拟合本研究所用的温度依赖方程 [Wu 2023, pp. 3-3]。
- 引用 Gringarten et al. (1975) 的无限域单裂隙解析解，其结果表明热产出与 \(K \cdot C_p\) 密切相关，本研究数值结果与之吻合 [Wu 2023, pp. 7-7]。
- 与 Zhang et al. (2022) 的核心尺度模型形成对照，后者虽考虑了温度依赖但尺度太小，无法模拟真实 EGS 条件，本文以此为基础放大至场尺度 [Wu 2023, pp. 1-3]。

## Open Questions
- 温度依赖的热参数在含多重裂隙网络、三维复杂几何的 EGS 中是否仍可被室温恒定值近似？[Wu 2023, pp. 1-3]
- 当同时考虑压力依赖（尤其深部储层）时，温度与压力的耦合效应会否改变 \(K, C_p\) 的净变化方向与幅度？
- 长期运行中，水岩化学作用可能改变裂隙渗透性及岩石热参数，室温假定是否仍然稳健？
- 对于初始温度更高（>300 °C）或注入流体温度极低的系统，\(K \cdot C_p\) 乘积的变异性是否会显著增大，需要实测方程支持。

## Source Coverage
所有 8 个非空索引片段均已处理，覆盖率达到：source_blocks 8/8 (100%)，source_chars 38627/38627 (100%)，编译后字符数 38777，签名 c36fab65ae2a3fbfacfbd8d7a9818eb70cf66128。未引入任何片段外的作者、数据或结论。
