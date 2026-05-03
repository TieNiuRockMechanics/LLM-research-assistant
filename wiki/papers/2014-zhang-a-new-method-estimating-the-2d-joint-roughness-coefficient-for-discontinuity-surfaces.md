---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces"
title: "A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses."
status: "draft"
source_pdf: "data/papers/2014 - A new method estimating the 2D Joint Roughness Coefficient for discontinuity surfaces in rock masses.pdf"
collections:
  - "zotero new"
citation: "Zhang, Guangcheng, et al. \"A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses.\" *International Journal of Rock Mechanics and Mining Sciences*, 2014."
indexed_texts: "8"
indexed_chars: "35819"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "35994"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004886"
coverage_status: "full-index"
source_signature: "ff0664a474e6844ef2ca8c88984d4ea0d0f96b3f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:08:48"
---

# A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses.

## One-line Summary
提出一种新的粗糙度指数λ，该指数结合了节理面起伏幅值和考虑剪切方向的修正均方根，通过逻辑函数能将λ准确转换为二维节理粗糙度系数（JRC），从而改善节理剪切强度与导水开度的估计。

## Research Question
如何更准确地定量估算节理粗糙度系数（JRC），以克服传统方法（如Z₂）仅依赖平均倾斜角而忽略幅值与剪切方向影响的缺陷？

## Study Area / Data
- 基准剖面：Barton的10条标准JRC剖面；Bandis (1980) 的64条节理剖面。
- 文献验证数据：来自 Grasselli & Egger [38], Yang et al. [20], Odling [39], Bakhtar & Barton [40], Ozvan et al. [41] 的剖面，长度50‑1003 mm。
- 实验验证：重庆鸡尾山滑坡灰岩中的5个节理试样（ID: JW02-1BL, JW02‑2BL, JW03‑1BL, JW03‑2BL, JW03‑3BL）。表面以1 mm×1 mm精度三维扫描，沿Y方向（剪切方向）截取二维剖面，进行直剪试验，并通过施密特锤试验获得JCS=20.815 MPa，倾角试验获得基本摩擦角34°。

## Methods
1. **平均高度与平均线确定**
   - 对每条二维剖面，通过迭代过程（迭代1000次）寻找一条参考线，使剖面各点到该线的平均垂直距离最小。
   - 平均高度h定义为该最小平均距离，对应的水平线即为平均线（满足累积宽度百分比=50%的条件）。
   - 计算公式：\( h_{av} = \frac{1}{L} \sum_{i=1}^{N} \frac{|y_{i+1}+y_i|(x_{i+1}-x_i)}{2L} \)[Zhang 2014, pp. 3-5]。

2. **修正均方根 Z'₂**
   - 仅考虑沿剪切方向的正倾角（max(0, Δy/Δx)），以反映各向异性。
   - 对等间距剖面：\( Z'_{2} = \sqrt{\frac{1}{M} \sum_{i=1}^{M} \left(\frac{\max(0, y_{i+1}-y_i)}{\Delta x}\right)^2} \)[Zhang 2014, pp. 3-5]。

3. **粗糙度指数 λ**
   - 结合幅值比与倾角效应：\( \lambda = \left(\frac{h}{L}\right)^{\alpha} \cdot (Z'_{2})^{1-\alpha} \) ，其中 α=1/3（由拟合确定）。

4. **λ–JRC 逻辑模型**
   - 基于 Bandis [37] 的64条剖面拟合得到逻辑函数[Zhang 2014, pp. 5-6]：
     \[
     \text{JRC}_{\text{suggested}} = \frac{40}{1+e^{-20\lambda}} - 20
     \]
   - 上、下限：
     \[
     \text{JRC}_{\text{upper}} = \frac{40}{1+e^{-30\lambda}} - 20, \quad \text{JRC}_{\text{lower}} = \frac{40}{1+e^{-15\lambda}} - 20
     \]

5. **验证**
   - 利用上述模型计算文献剖面及鸡尾山试样的JRC，并代入Barton的JRC–JCS模型（τ = σₙ tan(JRC log₁₀(JCS/σₙ)+φ_b)）估算剪切强度，与直剪试验结果比较。

## Key Findings
- 传统Z₂方法未考虑幅值，会高估JRC，尤其在高法向应力下预估剪切强度偏大。
- 提出的λ指数通过结合h/L和Z'₂，能更准确地估计JRC。对10条标准剖面及多源文献数据的验证表明，计算值与已知值一致表1，[Zhang 2014, pp. 5-8]。
- 鸡尾山灰岩直剪试验验证：λ建议值估算的剪切强度与试验值吻合良好，而Z₂方法在高法向应力（如3.32 MPa）下显著高估表2，[Zhang 2014, pp. 6-8]。
- JRC、剪切强度以及E/e（机械开度与导水开度之比）均对λ敏感，敏感区间为λ=0.05–0.20（对应JRC ≈10–18）[Zhang 2014, pp. 5-6]。

## Core Evidence Table

| Evidence / Source / Conditions / Notes |
|----------------------------------------|
| **λ的定义与α=1/3**：式(12) — [Zhang 2014, pp. 5] — 基于Bandis 64条剖面拟合得到常数，适用于二维剖面。 |
| **JRC逻辑函数**：式(14)–(15) — [Zhang 2014, pp. 5-6] — 拟合数据为Bandis(1980)，上下限反映变异。 |
| **文献JRC对比**：表1 — [Zhang 2014, pp. 6-8] — 涵盖11组不同长度剖面，λ计算的JRCsuggested均在报道值附近。 |
| **直剪试验验证**：表2，图13 — [Zhang 2014, pp. 6-8] — 灰岩试样，y向剪切；λ方法的τsuggested更接近τtest，而Z₂方法在高σₙ下高估。 |
| **敏感性分析**：图9、10 — [Zhang 2014, pp. 5-6] — 基于JRC–JCS模型和E/e关系，λ=0.05–0.20时参数变化剧烈。 |

## Limitations
- 论文未明确讨论方法的适用边界。从提出过程可推断：
  - 仅适用于二维剖面，未给出三维推广形式。
  - 拟合常数α=1/3来自Bandis(1980)的数据集，对其他岩性或风化程度的普适性未经充分检验。
  - 平均线的确定依赖迭代过程，可能对剖面数字化精度敏感。
  - 验证样品数量有限（5个灰岩），且限于高陡边坡环境。

## Assumptions / Conditions
- 剪切强度遵循Barton的JRC–JCS模型式1，[Zhang 2014, pp. 1-3]。
- 节理粗糙度各向异性，仅剪切方向的正倾角对强度有贡献，负倾角忽略。
- 平均线由“累积宽度百分比=50%”的条件唯一确定，并使其两侧的面积和最小。
- 逻辑函数形式适用于所有二维剖面，且上下限能够包络实测JRC变异。
- α=1/3为经验常数，由曲线拟合而得。

## Key Variables / Parameters
- λ：新粗糙度指数
- h：平均高度（平均线至剖面各点的平均垂直距离）
- L：剖面长度
- Z'₂：修正均方根（仅正倾角）
- JRCsuggested，JRCupper，JRClower：建议值及上下限
- τ：峰值剪切强度
- σₙ：有效法向应力
- ϕb：基本摩擦角
- JCS：节理壁单轴抗压强度
- E/e：机械开度与导水开度之比
- α：权重指数，取1/3

## Reusable Claims
1. 对于二维节理剖面，可用粗糙度指数λ= (h/L)^(1/3) · (Z'₂)^(2/3) 和逻辑函数JRCsuggested=40/(1+e^(-20λ))-20 来估计JRC，其上、下限由JRCupper=40/(1+e^(-30λ))-20和JRClower=40/(1+e^(-15λ))-20给出（条件：剖面沿剪切方向，且α=1/3基于现有数据拟合）。[Zhang 2014, pp. 5-6]
2. 当λ在0.05–0.20范围内时，JRC、剪切强度及E/e对λ变化最为敏感，这一区间的JRC估值需格外谨慎。[Zhang 2014, pp. 5-6]
3. 仅考虑正倾角的Z'₂结合h/L，能有效改善Z₂对高起伏剖面JRC的低估问题，从而在高法向应力下提供更准确的剪切强度估计。[Zhang 2014, pp. 6-8]
4. 本文提出的λ–JRC关系考虑了剪切方向和幅值，因此可用于各向异性节理的定向粗糙度评价。[Zhang 2014, pp. 1-3, 3-5]

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[Root Mean Square (Z2)]]
- [[Modified Root Mean Square (Z'2)]]
- [[Roughness Index λ]]
- [[Mean height of asperities]]
- [[Logistic function]]
- [[Barton's JRC–JCS model]]
- [[Hydraulic aperture ratio E/e]]
- [[Jiweishan rockslide]]
- [[Scale effect on JRC]]

## Candidate Methods
- [[Z2 method]]
- [[λ method for JRC]]
- [[Mean line determination (cumulative width 50%)]]
- [[Digital profilometry]]
- [[Laser scanning]]
- [[Direct shear test]]
- [[Schmidt hammer rebound test]]
- [[Tilt test]]

## Connections To Other Work
- 与Tse & Cruden (1979)和Yang et al. (2001)的Z₂–JRC关系式对比，指出Z₂忽略幅值的缺点。
- 参考Barton (1981)提出的H/L尺度效应图形方法，从中提取数据拟合出逻辑函数，据此将H/L融入新指数。
- 提及Tatone & Grasselli (2010)的方向性参数θ*ₘₐₓ/(C+1)₂D，但指出其未同时考虑幅值和剪切方向。
- 与分形维数方法（Lee et al., 1990）和粗糙度剖面指数Rp（Maerz et al., 1990）并列讨论。

## Open Questions
- 如何将λ方法推广至三维节理表面，以完整反映粗糙度的各向异性？
- 常数α=1/3是否对不同岩性、风化程度和节理类型保持稳定？
- 在大尺度（>1 m）现场节理上，该方法以及上限、下限公式的适用性需进一步验证。
- λ对JRC、E/e的敏感区间（0.05–0.20）是否受JCS、σₙ等参数影响，文中未深入分析。

## Source Coverage
本次编写使用了全部8个非空索引片段（覆盖文中的摘要、引言、方法、推导、实验结果及参考文献等）。按片段块数计覆盖率为1.0，按字符数计覆盖率为1.00488（原始索引字符35,819，编译后35,994字符）。所有陈述均来源于所提供的索引证据，未添加外部信息。
