---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2009-zhao-investigation-of-fractal-distribution-law-for-the-trace-number-of-random-and-grouped-f"
title: "Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass."
status: "draft"
source_pdf: "data/papers/2009 - Investigation of fractal distribution law for the trace number of random and grouped fractures in a geological mass.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhao, Yangsheng, et al. \"Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 46, no. 8, 2009, pp. 1347-1355."
indexed_texts: "7"
indexed_chars: "32362"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T13:03:08"
---

# Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass.

## One-line Summary
本研究介绍了一种研究地质体裂隙数量分形分布的方法，验证了随机和按走向分组的裂隙迹线数均遵循分形规律，并发现岩石强度与弹性模量的乘积与裂隙分形维数之间存在幂函数关系。[Zhao 2009, pp. 1-1]

## Research Question
地质体裂隙分布是否存在某种普适性规律？具体而言：裂隙数量的随机分布是否遵循分形规律；按走向分组后，各组裂隙是否仍遵循分形规律，且其分形维数是否因方向而异；在同一地层序列的不同岩性中，裂隙分形维数与岩石强度和模量之间存在何种关系？[Zhao 2009, pp. 1-1]

## Study Area / Data
研究数据源自中国多个煤矿区：
- **现场原位观测**：选取煤矿井下巷道（如回风巷、运输巷）的典型煤壁剖面，原始观测尺度为 1 m × 1 m 或 0.5 m × 0.5 m。[Zhao 2009, pp. 2-3]
- **实验室观测**：对来自中国 20 多个煤矿区的煤样进行观测，原始方形区域边长 L₀ = 100 mm；也对显微尺度（L₀ = 1 mm）的煤样裂隙进行了统计。[Zhao 2009, pp. 2-3]
- **地质图件分析**：数据来自中国山西的轩岗、汾西、东山等煤矿区，使用了包括总地质图（比例尺 2000–2400 m）和煤层断层图（比例尺 270–1200 m）在内的多尺度图件。[Zhao 2009, pp. 1-1][Zhao 2009, pp. 3-4]
- **钻孔岩芯分析**：对山西介休的 1002 号（深度 609 m）、1006 号（深度 581 m）和太原东山的 Test 6-1 号（深度 100 m）三个地质钻孔的岩芯进行了裂隙统计和力学测试。[Zhao 2009, pp. 5-6]

## Methods
采用一种改进的二维盒计数法来精确描述裂隙数量（而非百分比）随尺度的分布。其步骤为：选定初始尺度 L₀ 的区域，统计长度 ≥ L₀ 的裂隙数量 N；然后将区域边长依次减半（L₀/2, L₀/4…），在对应尺度的网格内统计长度 ≥ 该网格边长的裂隙数量 [Zhao 2009 pp. 1-2]。裂隙迹线数 N 与网格尺度 L 的关系遵循公式：
**N = N₀ * (L / C₀)^D**
其中，N₀ 是裂隙数量分布的原始值；C₀ 是特征尺度；D 是分形维数，代表单位尺度地质体内的裂隙数量 [Zhao 2009 pp. 1-2]。文中将 N₀=1, C₀=1 的情况定义为“标准情况” [Zhao 2009, pp. 2-3]。该方法被视为对 La Pointe (1988) 方法的改进，因为它关注了确定的裂隙数量而非百分比 [Zhao 2009, pp. 1-2]。

## Key Findings
1.  **随机分布遵循分形规律**：地质体裂隙的随机分布在从 2400 m 到 1 mm 的尺度范围内均与分形规律良好吻合。研究样本来自中国 13 个煤矿区。[Zhao 2009, pp. 1-1]
2.  **分组分布仍遵循分形规律**：受构造运动影响，地质体裂隙表现出明显的方向性和各向异性。按走向对裂隙进行分组后（例如主裂隙与次裂隙），每组裂隙的分布仍然遵循分形规律，但不同走向组的分形维数存在一定差异。例如，在东山煤矿的石灰岩中，100°方向主裂隙组分形维数为 1.7095，170°方向次裂隙组为 1.3732，25°方向组为 1.4532。[Zhao 2009, pp. 1-1][Zhao 2009, pp. 3-4]
3.  **分形维数与岩石力学性质的幂律关系**：对经历相似构造运动的同一沉积地层中的样品进行力学实验表明，同一地层中裂隙数量的分形维数与岩石的强度和弹性模量的乘积存在良好的幂函数关系。强度和弹性模量乘积越大的岩石，其裂隙分形维数也越大，反之亦然。拟合方程的相关系数在 80.9% 到 93.18% 之间。[Zhao 2009, pp. 1-1][Zhao 2009, pp. 5-6]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 随机裂隙分布在 2400 m–1 mm 尺度内符合分形规律，样本来自中国 13 个煤矿区。 | [Zhao 2009, pp. 1-1] | 研究尺度范围；中国 13 个煤矿区的地质体。 | 发现具有普适性。 |
| 按走向分组后，各组裂隙仍遵循分形规律，但分形维数不同。数据来自山西轩岗、汾西、东山煤矿区。 | [Zhao 2009, pp. 1-1] | 构造运动导致显著的方向性和各向异性。 | 示例：东山矿石灰岩 100° 主裂隙 D=1.7095，170° 次裂隙 D=1.3732。 |
| 裂隙分形维数 D 与强度和弹性模量的乘积 Q 之间存在幂函数关系。例如，1006 孔水平方向拟合方程为 Q = 394.4 * D^4.1299，相关系数 85%；1002 孔垂直方向为 Q = 1408 * D^2.2383，相关系数 80.9%。 | [Zhao 2009, pp. 5-6] | 样品来自山西介休的 1002 孔、1006 孔和太原东山的 Test 6-1 孔。适用于经历了相似构造运动的同一沉积序列的不同岩性。 | 乘积越大，分形维数越大。相关系数最高达 93.18% (Test 6-1 水平方向)。 |
| 裂隙迹线数 N 与网格尺度 L 关系为 N = N₀(L/C₀)^D。 | [Zhao 2009, pp. 1-2] | 基于改进的二维盒计数法。 | D 是分形维数。N₀=1, C₀=1 时定义为标准情况。 |

## Limitations
未从索引片段中确认。

## Assumptions / Conditions
- **方法假设**：所采用的改进二维盒计数法能够通过统计大于或等于网格边长的裂隙来准确描述裂隙数量的分形特征 [Zhao 2009, pp. 1-2]。
- **实验条件**：研究岩石强度、模量乘积与分形维数关系的力学实验，是基于经历了相似构造运动历史的同一套沉积地层中的样品进行的 [Zhao 2009, pp. 1-1]。
- **数据条件**：方向性分析的前提是裂隙由构造运动产生，表现出显著的方向性和各向异性，因此可以按走向进行分组 [Zhao 2009, pp. 1-1]。

## Key Variables / Parameters
- **D (Fractal Dimension)**：分形维数，单位尺度地质体内的裂隙数量表征 [Zhao 2009, pp. 1-2]。
- **N (Fracture Trace Number)**：裂隙迹线数量。统计门槛为在特定尺度(L)的网格内，长度 ≥ L 的裂隙 [Zhao 2009, pp. 1-2]。
- **L (Grid Scale)**：观测网格的边长尺度 [Zhao 2009, pp. 1-2]。
- **N₀**：裂隙数量分布的原始值 [Zhao 2009, pp. 1-2]。
- **C₀**：特征尺度参数 [Zhao 2009, pp. 1-2]。
- **Q**：岩石强度 (UCS) 与弹性模量的乘积 (Product of strength and elastic modulus) [Zhao 2009, pp. 5-6]。
- **Strike Group**：裂隙的走向分组（如主裂隙、次裂隙），用于研究各向异性 [Zhao 2009, pp. 3-4]。

## Reusable Claims
1.  **Claim**: 地质体中裂隙数量的随机分布在宽达数个数量级（2400 m 至 1 mm）的尺度范围内符合分形规律。
    -   **Conditions**: 适用于本研究涉及的中国 13 个煤矿区的地质体。
    -   **Evidence**: [Zhao 2009, pp. 1-1]
2.  **Claim**: 在构造运动导致的各向异性地层中，按走向分组的裂隙迹线数量仍然各自遵循分形规律，但不同走向组的分形维数不同。这表明可以分别对各优势方向的裂隙组进行分形表征。
    -   **Conditions**: 适用于构造运动显著、裂隙具有明显方向性的地质体。
    -   **Evidence**: [Zhao 2009, pp. 1-1] (东山煤矿石灰岩实例)。
3.  **Claim**: 在经历相似构造历史的同一地层序列中，不同岩性的裂隙分形维数 D 与岩石强度与弹性模量的乘积 Q 之间存在幂函数关系 (Q ∝ D^k)，即越坚硬（高强度高模量）的岩石，其裂隙网络的分形维数越高。
    -   **Conditions**: 局限于经历过相似构造运动的地层；关系通过特定钻孔（如 Jiexiu 1002, 1006）的岩芯实验建立。
    -   **Evidence**: [Zhao 2009, pp. 1-1][Zhao 2009, pp. 5-6]
4.  **Claim**: 一种改进的二维盒计数法，通过统计“在尺度 L 的网格内，长度 ≥ L 的裂隙数量 N”来建立 N 与 L 的幂律关系，可以更精确地确定裂隙数量的分形维数，而非仅统计有裂隙的网格百分比。
    -   **Conditions**: 应用于二维露头、图件或样品表面的裂隙分析。
    -   **Evidence**: [Zhao 2009, pp. 1-2] (公式 N = N₀(L/C₀)^D)。

## Candidate Concepts
- [[Fractal Dimension]]
- [[Box Counting Method]]
- [[Geological Mass Fracture]]
- [[Fracture Trace Number]]
- [[Fracture Network Characterization]]
- [[Rock Mechanics Properties]] (强度与弹性模量乘积)
- [[Anisotropy of Fractures]]
- [[Scale Invariance]]
- [[Sedimentary strata]]

## Candidate Methods
- [[2D Box Counting for Fractures]]
- [[Fractal Analysis of Fracture Traces]]
- [[Fracture Strike Grouping Analysis]]
- [[Borehole Core Fracture Logging]]
- [[Power Law Fitting of Geomechanical Data]]

## Connections To Other Work
- 本研究明确提及并改进自 La Pointe (1988) 的“分形裂隙密度表征”方法，指出其统计的是裂隙百分比而非确定数量 [Zhao 2009, pp. 1-2]。
- 索引片段中引用多篇文献，涉及裂隙盒计数 [[Box Counting Method]]、裂隙网络建模、迹线长估计等主题，如 Barton and Larsen (1985), Hirata (1989), Kulatilake et al. (1993), Mauldon (1998) 等 [Zhao 2009, pp. 6-6]，显示本工作处于裂隙几何表征和岩石力学的交叉领域。
- 从主题上，本工作可与以下概念和方法关联：[[Fractal Geometry in Geology]] (如 Mandelbrot 1982, Turcotte 1989)、[[Discrete Fracture Network (DFN)]]、[[Scanline Sampling]]、[[Rock Mass Quality Characterization]]。

## Open Questions
- 未从索引片段中确认。

## Source Coverage
本页依据论文的 7 个索引片段生成。片段覆盖了摘要、方法介绍、关键结果（随机分布、分组分布、与力学性质关系）以及部分数据和参考文献。内容主要偏向**摘要/结论**和**部分方法/结果**展示，但似乎缺失了关于采样策略、岩石力学实验细节、数据拟合优度检验的完整方法论讨论以及深入的讨论部分。可能缺失了引言中对更广泛背景的阐述以及结论中对工程应用的详细讨论。
