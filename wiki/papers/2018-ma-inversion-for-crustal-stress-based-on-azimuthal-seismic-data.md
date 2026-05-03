---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-ma-inversion-for-crustal-stress-based-on-azimuthal-seismic-data"
title: "Inversion for Crustal Stress Based on Azimuthal Seismic Data."
status: "draft"
source_pdf: "data/papers/2018 - 基于方位地震数据的地应力反演方法.pdf"
collections:
  - "part4-2"
citation: "Ma, Ni, et al. \"Inversion for Crustal Stress Based on Azimuthal Seismic Data.\" *Chinese Journal of Geophysics*, vol. 61, no. 2, Feb. 2018, pp. 697-706, doi:10.6038/cjg2018L0183."
indexed_texts: "7"
indexed_chars: "31038"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31124"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.002771"
coverage_status: "full-index"
source_signature: "ef000f03d74b3bfa1dccccef8db414f58747c280"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:30:11"
---

# Inversion for Crustal Stress Based on Azimuthal Seismic Data.

## One-line Summary
本文基于正交各向异性（OA）介质理论，利用叠前方位地震数据反演弹性参数和各向异性参数，进而估算正交各向异性水平应力差异比（ODHSR），用以评价页岩储层是否易于水力压裂成网。

## Research Question
如何利用方位地震数据反演地层的正交各向异性水平应力差异比（ODHSR），以指导页岩气储层的水力压裂改造，寻找易于形成复杂裂缝网络的区域？

## Study Area / Data
研究区为中国东部某全方位地震勘探工区（工区具有较为复杂的断裂构造，裂缝系统较为发育）[Ma 2018, pp. 6-9]。所用数据为处理得到的6个不同方位、每个方位包含3个入射角（θ=8°, 16°, 24°）的共18个分方位部分角度叠加道集，并从中选取6个叠前方位地震数据进行叠前方位弹性阻抗反演（方位角 φ=15° 和 105°，分别对应图4所示道集）[Ma 2018, pp. 6-9]。

## Methods
1. **方位各向异性弹性阻抗反演**：基于Rüger (1996)的HTI介质方位反射系数近似方程（式1）及Connolly (1999)的弹性阻抗推导思路，利用标准化方位弹性阻抗方程（式4）进行叠前方位地震反演，获得6个不同方位、不同入射角的弹性阻抗数据体；再通过线性化方程（式5）和矩阵求解（式6）提取纵波速度α、横波速度β、密度ρ以及HTI各向异性参数δ(V)、ε(V)、γ(V) [Ma 2018, pp. 2-3, 3-6]。
2. **VTI各向异性参数转换**：利用Thomsen (1986)关系 γ(V) = -γ/(1+2γ) 将HTI参数转换为VTI各向异性参数γ，用于后续正交各向异性应力计算 [Ma 2018, pp. 3-6]。
3. **正交各向异性水平应力差异比估算**：基于马妮等 (2017)推导的正交各向异性介质地应力近似公式（式14、15），计算最大与最小水平地应力的差异比 ODHSR = (σy - σx)/σy，其近似公式为（式16），其中需要弹性参数（VP0、VS0、ρ）和裂缝法向弱度ZN（由ΔN导出，ΔN=-ε(V)/(2g(1-g))）[Ma 2018, pp. 3-6]。
4. **数值模拟与敏感性分析**：通过改变横波速度、密度、VTI各向异性参数γ等，分析单一参数变化对ODHSR的影响，并评估10%误差下各参数的敏感性 [Ma 2018, pp. 6-9]。
5. **实际应用验证**：将上述流程应用于实际工区，得到ODHSR层切片，识别低值区域，指导水力压裂 [Ma 2018, pp. 6-9]。

## Key Findings
- 基于正交各向异性介质的ODHSR近似公式能够综合考虑垂直裂缝扰动（HTI特征）和水平层理（VTI背景）的影响，更符合实际页岩储层 [Ma 2018, pp. 3-6]。
- 数值模拟表明：ODHSR随横波速度和裂缝法向弱度增大而增大，密度对ODHSR基本无影响；横波速度误差对ODHSR估算的影响远大于VTI各向异性参数γ的误差 [Ma 2018, pp. 6-9]。
- 实际工区应用显示，井A所在区域为ODHSR低值区，表明该处易于压裂形成复杂裂缝网络，有利于提升储层渗透率和采收率；ODHSR层切片能有效识别储层中易压裂成网的区域 [Ma 2018, pp. 6-9]。
- ODSHR的理想取值范围为0～0.2，但实际工区可能更广泛；低值意味着最大与最小水平地应力接近，地层延展性差，易形成网状裂缝 [Ma 2018, pp. 3-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|-------------|-------|
| 正交各向异性水平应力差异比（ODHSR）近似公式：ODHSR = 2V²S0ρ(2γ+1)Z_N / [1+2V²S0ρ(2γ+1)Z_N] | [Ma 2018, pp. 3-6] | 假设OA介质、水平应变为零、垂直主应力存在 | Z_N与裂缝法向弱度ΔN相关，ΔN取值范围0～1 |
| 数值实验：横波速度从1500 m/s增至3000 m/s时，ODHSR随横波速度增加而上升；密度从1800 kg/m³增至3000 kg/m³时ODHSR保持不变 | [Ma 2018, pp. 6-9] | 固定其他参数（α=4300 m/s, γ=0.025, ΔN=0.01~0.8） | 证明密度项在公式中因法向柔度定义而被抵消 |
| 参数误差敏感性：横波速度±10%引起的ODHSR变化量远大于VTI各向异性参数γ±10%的变化量；γ值越大，其对ODHSR的影响越显著 | [Ma 2018, pp. 6-9] | 模型参数同前 | 提示横波速度反演精度对ODHSR估算至关重要 |
| 实际工区ODHSR层切片显示井A处为ODHSR低值区域 | [Ma 2018, pp. 6-9] | 中国东部某全方位地震工区，方位数据为φ=15°/105°，θ=8°/16°/24° | 低值区指示易于压裂成网 |
| 基于方位弹性阻抗反演可稳定提取纵波速度、横波速度、密度及各向异性参数 | [Ma 2018, pp. 6-9] | 使用标准化方位弹性阻抗方程（式4）和至少6个不同方位-入射角的阻抗数据体 | 反演结果如图6所示 |

## Limitations
- 地应力近似公式基于正交各向异性介质线性滑动理论，假设岩石为有界且水平方向应变为零，与真实地层可能存在偏差 [Ma 2018, pp. 3-6]。
- ODHSR的估算精度依赖于叠前方位地震反演获得的弹性参数和各向异性参数的准确性，尤其是横波速度和裂缝法向弱度的误差会直接影响结果 [Ma 2018, pp. 6-9]。
- 实际资料测试仅在一个工区进行，ODHSR的理想取值范围（0～0.2）可能不适用于所有地质背景 [Ma 2018, pp. 3-6]。
- 方法中使用了HTI介质向VTI介质各向异性参数的转换关系（Thomsen, 1986），该关系在强各向异性情况下可能存在误差 [Ma 2018, pp. 3-6]。
- 未讨论纵波各向异性参数ε和δ的反演误差对ODHSR的影响（数值模拟部分仅分析了横波速度和γ的误差）[Ma 2018, pp. 6-9]。

## Assumptions / Conditions
- 实际页岩储层可等效为正交各向异性（OA）介质，即同时存在水平层理（VTI背景）和垂直裂缝（HTI扰动）[Ma 2018, pp. 3-6]。
- 地下岩石有界且不能移动，因此水平方向的应变设为零（Iverson, 1995）[Ma 2018, pp. 3-6]。
- 存在垂直方向主应力和两个水平方向主应力 [Ma 2018, pp. 3-6]。
- 使用线性滑动理论（Schoenberg & Sayers, 1995）将OA柔度矩阵近似为VTI背景柔度矩阵与裂缝扰动柔度矩阵之和 [Ma 2018, pp. 3-6]。
- 叠前方位地震数据需包含至少6个不同方位和入射角的道集，且已完成标准化处理（Whitcombe, 2002）[Ma 2018, pp. 2-3]。

## Key Variables / Parameters
- 弹性参数：纵波速度α (VP0)、横波速度β (VS0)、密度ρ
- HTI各向异性参数：δ(V)、ε(V)、γ(V)
- VTI各向异性参数：γ (通过γ(V)换算)
- 裂缝法向弱度：ΔN = -ε(V) / [2g(1-g)]，其中 g = (VS0/VP0)²
- 裂缝柔度矩阵元素：Z_N = ΔN / [M(1-ΔN)]，M = λ+2μ (λ, μ为拉梅常数)
- 正交各向异性水平应力差异比：ODHSR = (σy - σx) / σy （式16）

## Reusable Claims
- 正交各向异性水平应力差异比（ODHSR）是评价地层是否易于压裂成网的有效参数：低值指示水平两向应力差异小，易形成网状裂缝；高值指示水平两向应力差异大，易形成定向排列裂缝 [Ma 2018, pp. 3-6]。
- ODHSR近似公式（式16）可利用方位地震反演得到的弹性参数和各向异性参数直接计算，避免了直接测量地应力的局限性 [Ma 2018, pp. 3-6]。
- 密度对ODHSR近似公式的计算结果无影响，因此反演中密度参数的不稳定性不会传递到应力差异比估算中 [Ma 2018, pp. 6-9]。
- 横波速度的估计误差对ODHSR的影响大于VTI各向异性参数γ的误差，因此在反演流程中应优先保证横波速度的精度 [Ma 2018, pp. 6-9]。
- 基于标准化方位弹性阻抗方程的叠前反演能稳定提取HTI各向异性参数，进而通过转换关系获得VTI各向异性参数，用于正交各向异性应力计算 [Ma 2018, pp. 2-3, 3-6]。

## Candidate Concepts
- [[orthorhombic differential horizontal stress ratio (ODHSR)]]
- [[azimuthal elastic impedance]]
- [[pre-stack azimuthal seismic inversion]]
- [[orthorhombic (OA) medium]]
- [[linear slip theory]]
- [[fracture-induced anisotropy]]
- [[horizontal transverse isotropy (HTI)]]
- [[vertical transverse isotropy (VTI)]]
- [[normal fracture weakness ΔN]]
- [[hydraulic fracturing in shale]]

## Candidate Methods
- [[azimuthal anisotropic elastic impedance inversion]]
- [[estimation of ODHSR from seismic data]]
- [[orthorhombic stress approximation using elastic and anisotropic parameters]]
- [[conversion from HTI to VTI anisotropy parameters (Thomsen)]]
- [[standardized elastic impedance normalization (Whitcombe)]]

## Connections To Other Work
- 引用了马妮等 (2017) 构建的正交各向异性介质地应力公式及ODHSR概念 [Ma 2018, pp. 2-3, 3-6]。
- 继承并拓展了Gray等 (2010a,b,c, 2012) 基于地震数据估算水平应力差异比的方法，将介质从HTI推广到OA [Ma 2018, pp. 2-3]。
- 采用了Rüger (1996) 的HTI介质方位反射系数近似方程和Connolly (1999) 的弹性阻抗推导思想 [Ma 2018, pp. 2-3]。
- 使用了Schoenberg & Sayers (1995) 的线性滑动理论构建OA介质柔度矩阵 [Ma 2018, pp. 3-6]。
- 利用Thomsen (1986) 的弱各向异性参数关系实现HTI与VTI参数转换 [Ma 2018, pp. 3-6]。
- 标准化弹性阻抗处理参考了Whitcombe (2002) [Ma 2018, pp. 2-3]。

## Open Questions
- 如何进一步降低横波速度和各向异性参数反演误差，以提高ODHSR估算的可靠性？
- 不同地质背景下（如强各向异性、非正交裂缝系统）ODHSR近似公式的适用范围和修正方法是什么？
- ODSHR的理想阈值（0～0.2）是否具有普适性，还是需要根据具体工区通过实测应力数据校准？
- 裂缝法向弱度ΔN的准确估算对ODHSR影响显著，但ΔN依赖于ε(V)反演，如何单独评估ΔN的不确定性？
- 该方法在纵横波速度比、各向异性强度等条件变化的复杂储层中的稳健性如何？

## Source Coverage
All 7 indexed fragments (31038 indexed characters, 31124 compiled characters) were processed with a single-pass markdown compilation. Coverage ratio by blocks: 1.0; coverage ratio by characters: 1.002771. Source signature: ef000f03d74b3bfa1dccccef8db414f58747c280. Compile strategy: single-pass-markdown.
