---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi"
title: "Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2009 - Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Kim, Tae H., and David S. Schechter. \"Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks.\""
indexed_texts: "10"
indexed_chars: "46461"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:58:03"
---

# Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks

## One-line Summary
该论文开发并验证了一套基于分形离散裂缝网络（FDFN）的数值代码，用以估算基质孔隙度可忽略的I型天然裂缝性储层中具有尺度依赖性的裂缝孔隙度 [Kim year, pp. 1-1, 9-10]。

## Research Question
当天然裂缝性储层（NFR）基质孔隙度可以忽略不计时，如何利用从岩心、成像测井和露头图中获取的多尺度数据，系统且可靠地估算具有高度非均质性和尺度依赖特征的裂缝孔隙度？[Kim year, pp. 1-1]

## Study Area / Data
*   **验证与应用场景**：论文使用了合成裂缝网络进行代码验证，并应用了一个实际露头图数据进行演示 [Kim year, pp. 3-4, pp. 9-10]。
*   **实际数据来源**：分析了来自美国怀俄明州布里杰峡（Bridger Gap, Wyoming）的露头图，该区域调查范围约为 40m × 40m [Kim year, pp. 9-10]。
*   **裂缝孔径数据**：裂缝孔径生成时参考了来自斯普拉贝里趋势区（Spraberry Trend Area）岩心中人工裂缝的CT扫描数据 [Kim year, pp. 4-6]。

## Methods
*   **2D/3D FDFN 生成代码开发**：采用分形中心分布的一阶模型（First-Order Model）生成裂缝网络，因为其密度项 `a` 是与尺度无关的常数 [Kim year, pp. 1-2]。裂缝长度服从分形分布，其分形维数为 `Dl` [Kim year, pp. 1-2]。
*   **分形维度计算**：利用对相关函数（Pair Correlation Function, `C2(r) = 2Np(r) / N(N-1) = cr^{Dc}`）来计算裂缝中心分布的分形维数 `Dc` [Kim year, pp. 1-2]。
*   **裂缝几何生成**：裂缝走向（orientation）基于平台矢量数据，利用费歇尔（Fisher）分布生成 [Kim year, pp. 2-3]。通过验证Bour和Davy提出的幂律关系（`d(l) ∝ l^x, x = Dl/Dc`）来确保生成的裂缝网络几何形态的合理性，该关系描述了中心间距与裂缝长度的关联 [Kim year, pp. 3-4]。
*   **裂缝孔径生成**：摒弃了平行板模型的单一赋值法，采用修正的连续随机加法（corrected SRA）生成自仿射（self-affine）分形孔径场，其数学基础是分数布朗运动（`fBm`），由赫斯特指数 `H` 控制 [Kim year, pp. 2-3]。
*   **孔隙度估算方法**：提出一种两步法以高效估算裂缝孔隙度：首先利用二维FDFN代码估算裂缝孔隙度的分形维数 `Dfp`，再利用三维FDFN代码估算特定域尺寸下的初始裂缝孔隙度 `φ_{f0}`。结合两者，即可利用尺度依赖模型估算任意域尺寸下的裂缝孔隙度 [Kim year, pp. 7-9]。
*   **实际数据应用流程**：通过分析布里杰峡露头图，手动提取裂缝中心坐标，计算其中心分布和长度分布的分形维数与密度项，作为FDFN生成的直接输入参数 [Kim year, pp. 9-10]。

## Key Findings
*   **代码验证**：
    *   生成的二维与三维FDFN均能很好地匹配理论分形模型。二维生成的指数 `x`（0.7697）与理论值（0.7368）非常接近 [Kim year, pp. 3-4]。三维生成结果与理论值的最大误差不超过13.6%，表明代码能够反映真实裂缝网络的特征 [Kim year, pp. 6-7]。
    *   裂缝孔隙度表现出尺度依赖性，并具有分形特征，这与尺度依赖模型（如 Chang 和 Yortsos (1990) 的模型）相符 [Kim year, pp. 3-4, pp. 6-7]。
*   **2D与3D方法对比**：
    *   二维和三维方法估算的裂缝孔隙度分形维数 `Dfp` 几乎相同，因此计算速度更快的二维方法更适用于估算 `Dfp` [Kim year, pp. 7-9, pp. 9-10]。
    *   然而，三维方法估算的裂缝孔隙度绝对值更高，且在物理上更接近真实情况，因此在估算具体孔隙度数值上优于二维方法 [Kim year, pp. 7-9]。
*   **控制因素分析**：裂缝孔隙度的分形维数 `Dfp` 随裂缝中心分布分形维数 `Dc` 增加而减小（裂缝更密集），也随长度分形维数 `Dl` 增加而减小（短裂缝增多导致孔隙度降低）[Kim year, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 生成FDFN的间距-长度指数 `x` 为0.7697，与理论值0.7368非常接近 | [Kim year, pp. 3-4] | 二维FDFN，输入 `Dc=1.9, Dl=1.4`，域大小100m×100m | 验证了二维FDFN代码生成裂缝网络几何形态的准确性 |
| 33个二维FDFN的分形分析结果沿理论线分布，最大误差小于14% | [Kim year, pp. 3-4] | 二维生成代码验证 | 支撑了代码产生合理裂缝网络几何的结论 |
| 3D FDFN生成结果与理论值匹配，最大误差为13.6% | [Kim year, pp. 6-7] | 三维生成代码验证 | 验证了三维FDFN代码的可靠性 |
| 裂缝孔隙度表现出的分形维度与理论模型 (Eq. 9) 匹配良好，回归 `R²` 值高 | [Kim year, pp. 4-6, pp. 6-7] | 二维（Table 3）和三维（Table 5）验证，多种 `Dc`和`Dl`组合 | 证实了裂缝孔隙度是一个具有分形特征的尺度依赖变量 |
| 怀俄明州布里杰峡露头图的分析结果显示，裂缝中心分布分形维数为1.691，长度分布分形维数为1.266 | [Kim year, pp. 9-10] | 实际露头数据（约40m × 40m）应用 | 展示了将实际数据输入FDFN生成代码的完整流程 |

## Limitations
*   三维裂缝网络生成受到计算机内存和时间限制，其验证时的域尺寸变化步数（40个）少于二维（50个）[Kim year, pp. 6-7]。
*   三维空间中的裂缝形状被假定为圆盘（disc），这是一种为计算效率而做的几何简化 [Kim year, pp. 4-6]。
*   裂缝孔隙度绝对值较低（案例中小于1%），因为孔径生成基于特定岩心的人工裂缝CT扫描数据，可能不代表所有储层 [Kim year, pp. 4-6]。

## Assumptions / Conditions
*   **储层类型**：适用于Nelson (2001) 分类中的 I 型天然裂缝性储层，即基质孔隙度和渗透率均可忽略的储层 [Kim year, pp. 1-1]。
*   **裂缝分布模型**：裂缝网络基于分形理论，具体采用分形中心分布的一阶模型，其密度项 `a` 为常数，不随尺度变化 [Kim year, pp. 1-2]。
*   **裂缝走向模型**：裂缝走向假设服从费歇尔（Fisher）分布 [Kim year, pp. 2-3, 4-6]。
*   **裂缝形状**：在三维生成中，裂缝被假定为圆盘形 [Kim year, pp. 4-6]。
*   **孔径模型**：裂缝孔径被视作具有自仿射分形特征的场，采用分数布朗运动（fBm）模型和修正的连续随机加法（SRA）生成，而非采用平行板或孔径-长度正比关系 [Kim year, pp. 2-3]。

## Key Variables / Parameters
*   **`Dc` / `Dc3D`**：裂缝中心分布的分形维数（二维/三维），三维值为二维值加1 [Kim year, pp. 1-2, 4-6]。
*   **`Dl` / `Dl3D`**：裂缝长度分布的分形维数（二维/三维），三维值为二维值加1 [Kim year, pp. 1-2, 4-6]。
*   **`a` / `a3D`**：裂缝密度项。二维密度项 `a` 是常数，三维 `a3D` 由 `a` 经包含Gamma函数的公式Eq. 11转换得到 [Kim year, pp. 1-2, 4-6]。
*   **`H`**：赫斯特指数（Hurst exponent），用于控制自仿射裂缝孔径场的粗糙度 [Kim year, pp. 2-3]。
*   **`Dfp`**：裂缝孔隙度的分形维数，用于描述孔隙度随域尺寸变化的尺度特征 [Kim year, pp. 7-9]。
*   **`φ_{f0}`**：初始裂缝孔隙度，即特定域尺寸 `L0` 下的孔隙度值 [Kim year, pp. 7-9]。
*   **`K`**：Fisher 常数，用于描述裂缝走向（strike）相对于均值分布的离散程度 [Kim year, pp. 2-3]。

## Reusable Claims
*   **Claim 1**：对于裂缝网络，如果其中心间距 `d(l)` 与裂缝长度 `l` 满足幂律关系 `d(l) ∝ l^{Dl/Dc}`，则可以通过验证此关系来检验合成裂缝网络（如FDFN）的几何形态是否合理 [Kim year, pp. 3-4]。[**Evidence**: 论文利用此关系（Eq. 8）验证了33个二维FDFN，生成值与理论值匹配良好。**Conditions**: 适用于分形裂缝长度和中心分布。**Limitations**: 关系基于[[Bour Davy 1999]]和[[Bour et al 2002]]对实际裂缝数据的观测。]。
*   **Claim 2**：在无基质孔隙度的I型裂缝性储层中，裂缝孔隙度本身是一个具有分形特征的尺度依赖变量，而非定值，可以用分形维度 `Dfp` 来描述 [Kim year, pp. 3-4, 6-7]。[**Evidence**: 二维和三维FDFN验证均显示，不同域尺寸下的孔隙度符合尺度依赖模型（Eq. 9），`R²` 值很高。**Conditions**: 裂缝网络需满足分形分布特征。**Limitations**: 该结论基于合成FDFN的数值实验]。
*   **Claim 3**：估算裂缝孔隙度最有效的方法是两步法：先用高效但欠精确的二维模型确定孔隙度的分形特征（`Dfp`），再用高精度的三维模型校准其绝对量级（`φ_{f0}`）[Kim year, pp. 7-9, 9-10]。[**Evidence**: 研究发现2D和3D估算的 `Dfp` 几乎相同，但3D估算的孔隙度绝对值更优。**Conditions**: 该方法降低了三维代码的调用频次，能在保证精度的前提下显著缩短计算时间。**Limitations**: 需要分别开发和验证二维和三维代码。]。
*   **Claim 4**：直接将单个恒定孔径或孔径-长度正比关系赋予裂缝，会低估复杂性或高估裂缝孔隙度，不适合用于孔隙度估算 [Kim year, pp. 2-3]。[**Evidence**: 论文指出恒定孔径法不符合实际裂缝行为，而孔径-长度正比法仅适用于张性裂缝，会高估孔隙度。**Conditions**: 未从索引片段中确认。**Limitations**: 结论基于对以往方法的评述。]。

## Candidate Concepts
*   [[Fracture Porosity]]
*   [[Naturally Fractured Reservoirs (NFRs)]]
*   [[Fractal Discrete Fracture Networks (FDFN)]]
*   [[Type 1 NFR (Nelson 2001)]]
*   [[Fractal Length Distribution]]
*   [[Fractal Center Distribution]]
*   [[Scale-Dependent Porosity]]
*   [[Self-Affine Fractal Aperture]]
*   [[Fractal Dimension of Porosity]]

## Candidate Methods
*   [[Pair Correlation Function (Viseck 1992)]]
*   [[First-Order Fractal Model (Davy et al. 1990)]]
*   [[Fisher Distribution for Fracture Orientation]]
*   [[Fractional Brownian Motion (fBm)]]
*   [[Successive Random Addition (SRA)]]
*   [[Multiplicative Cascade Process (3D Fracture Center)]]
*   [[Bour's d(l) Power Law Validation]]

## Connections To Other Work
*   **裂缝网络理论基础**：该方法建立在[[Davy et al. 1990]]的一阶模型、[[Bour et al. 2002]]和[[Bour Davy 1999]]关于裂缝间距与长度的幂律关系、以及[[Chang Yortsos 1990]]的尺度依赖孔隙度模型之上 [Kim year, pp. 1-2, 3-4]。
*   **裂缝孔径建模对比**：该方法明确批评了将单一孔径、孔径服从对数正态分布、或孔径与长度成正比（如[[Tamagawa et al. 2002]]的工作）的建模方法，认为其不适合估算孔隙度；并引用了[[Vermilye and Sholtz 1995]]来论证孔径-长度比例关系仅适用于张性裂缝 [Kim year, pp. 2-3]。
*   **几何生成方法**：裂缝方位的生成引用了[[Priest 1993]]和[[Villaescusa 1993]]的方法。二维和三维密度项转换引用了[[Piggott 1997]]的方程 [Kim year, pp. 2-3, 4-6]。

## Open Questions
*   未从索引片段中确认该 FDFN 方法在除怀俄明州布里杰峡以外的其他实际 I 型储层案例中的广泛适用性和验证结果。
*   未从索引片段中确认三维裂缝中引入更复杂的几何形状（如多边形）是否会显著改变裂缝孔隙度的估算结果。
*   未从索引片段中确认代码对渗透率等其他流动相关属性的估算能力。
*   该模型对裂缝密度 `a` 和分形维度 `Dc`、`Dl` 等输入参数的敏感性程度未从当前片段中详细确认。

## Source Coverage
*   本页依据 10 个索引片段，内容涵盖了论文的摘要/引言、方法论的核心（二维与三维FDFN生成、关键方程Eq. 1-11）、结果验证、以及一个实际应用示例。
*   **覆盖偏重**：片段高度集中于方法论和验证部分，对详细的[[Bridger Gap]]露头数据分析过程（如图17-22之外的描述）和最终结论（第10节）提供了较完整的信息。
*   **可能缺失**：论文中对 I 型储层更详尽的背景讨论、完整的文献综述、更详细的敏感性分析、以及对估算结果不确定性的量化讨论可能缺失或不完整。论文中代码实现或计算性能的具体细节未从片段中完全确认。
