---
type: "paper"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks Correlating Fracture Aperture and Length.pdf"
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.\" *Geofluids*, vol. 2020, 2020, Article ID 8834666, 12 pp., doi:10.1155/2020/8834666."
indexed_texts: "11"
indexed_chars: "54860"
compiled_at: "2026-04-27T19:41:25"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.

## One-line Summary

本研究定量考察了考虑[[fracture aperture]]与[[fracture length]]相关性的裂隙多孔岩石的等效渗透率分布，发现平均无量纲等效渗透率与开度‑长度相关指数D呈指数关系，且对角线分量分布随最小裂隙长度和裂隙数量增加从幂律向对数正态再向正态转变，该转变速度随D增大而减慢。[Chen 2020, pp. 1-2]

## Research Question

在网格尺度上估算等效渗透率是大型裂隙多孔岩石数值模拟的关键问题，但等效裂隙模型的渗透率分布因复杂的裂隙特性而难以约束。本研究旨在定量研究裂隙开度与长度相关模型对裂隙多孔岩石等效渗透率分布的影响。[Chen 2020, pp. 1-2]

## Study Area / Data

未从索引片段中确认具体研究区。研究采用二维离散裂隙模型，裂隙开度与长度满足幂律关系 w = γ l^D，其中相关指数D在0.5至1.0之间变化，步长0.1，代表不同的裂隙岩石力学特性。[Chen 2020, pp. 2-3] 矩阵渗透率设为 k_m = 9.87×10⁻¹⁶ m² (1 md)，依据实际裂隙油气藏数据。[Chen 2020, pp. 3-5] 裂隙渗透率按 k_f = w²/12 计算。[Chen 2020, pp. 3-5]

## Methods

1. **离散裂隙模型生成**：基于幂律关系 w = γ l^D 生成裂隙，其中 D=1.0 对应孤立脉、断层等（线性关系），D≈0.5 对应恒定断裂韧性的张开型裂隙，0.5<D<1.0 对应接缝后松弛。[Chen 2020, pp. 2-3]
2. **多边界升尺度方法**：采用多边界表达式求解流动方程，通过逆向达西定律计算等效渗透率张量分量 k_xx、k_xy、k_yy。[Chen 2020, pp. 3-5]
3. **数值求解**：使用MRST代码求解裂隙与基质中的流动问题，基于质量守恒和达西定律，采用多点通量近似。基质和裂隙分别用二维三角形网格（0.2 m）和一维线网格（0.1 m）离散。[Chen 2020, pp. 3-5]
4. **验证**：对不同D值下的全贯穿裂隙，数值解与解析解吻合良好。[Chen 2020, pp. 3-5]
5. **统计分析**：绘制等效渗透率张量分量的直方图及拟合曲线，计算Spearman秩相关系数评估拟合强度，并建立平均无量纲等效渗透率与D的关系模型。[Chen 2020, pp. 5-7]

## Key Findings

- 当相关指数 D=0.5 时，对角线分量 k_xx 和 k_yy 呈幂律分布，非对角线分量 k_xy 呈正态分布；随着最小裂隙长度 l_min 和裂隙数量 N 增加，k_xx 和 k_yy 逐渐从幂律分布变为对数正态分布再变为正态分布。该转变速度随 D 增大而减慢。[Chen 2020, pp. 5-5]
- 对角线分量 k_xx 和 k_yy 的Spearman秩相关系数平均约为 -0.75，表明拟合强度较高。[Chen 2020, pp. 5-5]
- 平均无量纲等效渗透率 ⟨k'⟩ 与相关指数 D 呈指数关系：⟨k'⟩ = A·10^(B·D)，其中 A 在 10^1.4 至 10^2.4 范围，B 在 3.4 至 4.3 范围。非对角线分量绝对值 |k_xy| 也符合该指数模型。[Chen 2020, pp. 5-7] 系数 B 随 l_min 和 N 增加而增大，系数 A 变化不明显。[Chen 2020, pp. 5-7]
- 随着 D 从 0.5 增大至 1.0，等效渗透率各向异性（k_max/k_min）总体增大。[Chen 2020, pp. 9-10]
- 与恒定开度模型相比，裂隙长度‑开度相关性增加了离散裂隙模型和升尺度等效裂隙模型的非均质性。[Chen 2020, pp. 9-10]

## Limitations

- 裂隙受力学特性和周围岩石应力场的高度影响，不同开度模型（如基于本构模型的力学开度）对等效渗透率分布的影响有待进一步研究。[Chen 2020, pp. 9-10]
- 本研究离散裂隙模型为二维，是对三维模型的简化；研究三维裂隙多孔介质需要真实裂隙几何数据和高性能计算平台。[Chen 2020, pp. 9-10]

## Reusable Claims

- 当裂隙最小长度和数量增加时，等效渗透率对角线分量分布从幂律向对数正态和正态转变，且转变速度随相关指数D增大而减慢。[Chen 2020, pp. 5-5] [Chen 2020, pp. 1-2]
- 平均无量纲等效渗透率与裂隙开度‑长度相关指数D呈指数关系，系数A和B可通过回归获取，其中B随最小裂隙长度和裂隙数量增加而增大。[Chen 2020, pp. 5-7]
- 裂隙长度‑开度相关性增强等效渗透率场的非均质性及各向异性。[Chen 2020, pp. 9-10]
- 本研究支持Klimczak等（2017）、Leung和Zimmerman（2012）、Bisdom等（2016）关于不同开度模型对等效渗透率重要性的结论。[Chen 2020, pp. 7-9]

## Candidate Concepts

- [[fracture porous rock]]
- [[equivalent permeability]]
- [[discrete fracture model]]
- [[fracture aperture]]
- [[fracture length]]
- [[aperture-length correlation]]
- [[correlation exponent D]]
- [[fracture connectivity]]
- [[permeability tensor]]
- [[anisotropy]]
- [[MRST]]
- [[multiple boundary upscaling method]]
- [[power law distribution]]
- [[lognormal distribution]]
- [[normal distribution]]

## Candidate Methods

- [[multiple boundary upscaling method]]
- [[power law correlation between fracture aperture and length]]
- [[MRST code for flow simulation]]
- [[Spearman rank correlation for histogram fitting]]
- [[exponential model for average dimensionless equivalent permeability]]
- [[power law model for equivalent permeability]]

## Open Questions

- 不同力学开度模型（如基于本构模型的应力相关开度）如何影响二维及三维裂隙多孔岩石的等效渗透率分布？[Chen 2020, pp. 9-10]
- 在三维裂隙多孔介质中，裂隙开度‑长度相关性对等效渗透率分布的影响规律是否与二维一致？[Chen 2020, pp. 9-10]
- 如何将小尺度离散裂隙模型的等效渗透率分布有效链接到储层模型的大尺度场？[Chen 2020, pp. 9-10]

## Source Coverage

- pp. 1-2: One-line Summary, Research Question, Key Findings (Part)
- pp. 2-3: Methods (Discrete fracture model generation)
- pp. 3-5: Methods (Upscaling, validation), Key Findings (Spearman coefficient)
- pp. 5-5: Key Findings (Distribution transformation)
- pp. 5-7: Key Findings (Exponential model, coefficients)
- pp. 7-9: Discussion, Limitations
- pp. 9-10: Limitations (2D simplification, aperture models), Conclusions, Anisotropy
