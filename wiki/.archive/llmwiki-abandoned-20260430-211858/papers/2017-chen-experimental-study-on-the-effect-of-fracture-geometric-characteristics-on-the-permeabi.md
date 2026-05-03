---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi"
title: "Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures."
status: "draft"
source_pdf: "data/papers/2017 - Experimental study on the effect of fracture geometric characteristics on the permeability in deformable rough-walled fractures.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Chen, Yuedu, et al. \"Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 98, 2017, pp. 121-140. doi:10.1016/j.ijrmms.2017.07.003. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72590"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:43:50"
---

# Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.

## One-line Summary
本文通过实验研究了粗糙裂缝的几何特征对可变形裂缝渗透率的定量影响，提出了基于有效机械隙宽、接触比和相对分形维数的裂缝几何特征模型 [Chen 2017, pp. 1-2]。

## Research Question
裂缝几何特征如何定量影响可变形粗糙壁裂缝的渗透率，特别是在应力作用下？具体研究裂缝连通空隙的隙宽大小、接触面积和连通空隙的异质性分布这三种几何特征与水力特性的定量关系 [Chen 2017, pp. 1-2]。

## Study Area / Data
*   **样本**：六块单一裂缝砂岩样本，根据颗粒大小分为三组 [Chen 2017, pp. 1-2, 6-10]。
*   **样本类型**：粗粒（CA, CB）、中粒（MA, MB）、细粒（FA, FB）砂岩 [Chen 2017, pp. 10-11]。
*   **实验条件**：在不同围压（σ3）下进行流体流动测试 [Chen 2017, pp. 10-11]。

## Methods
*   **裂缝形态测量**：开发了一种“点云数据匹配法”（point-cloud data matching method），利用3D扫描仪，通过坐标变换间接获取非加载条件下的裂缝表面空间坐标，避免了传统接触式方法对裂缝的破坏，并具有0.01 mm的栅格空间分辨率 [Chen 2017, pp. 1-2, 3-5]。
*   **裂缝几何特征表征参数计算**：
    *   **有效机械隙宽（e′m）**：仅考虑对渗流有贡献的连通空隙的平均隙宽，排除了孤立空隙 [Chen 2017, pp. 3-5, 6-10]。
    *   **接触比（ω）**：定义为接触面积与裂缝总面积之比 [Chen 2017, pp. 5-6, 6-10]。
    *   **相对分形维数（D*Δ）**：用于表征连通空隙空间分布异质性的参数。通过改进的超薄方块覆盖法（UTSP covering method）计算裂缝空隙三维腔体的分形维数 (D)，再减去等效平行板的分形维数 (D0) 得到绝对分形维数(DΔ)，最后标准化为相对分形维数 D*Δ = log₁₀(DΔ / DΔ_ref) [Chen 2017, pp. 6-10]。
*   **渗透率测试**：采用水力实验，在多个围压下进行，通过雷诺数（Reynolds number）验证了分析在达西流（Darcy flow）条件下有效 [Chen 2017, pp. 10-13]。
*   **模型建立与对比**：建立了“FGC模型”，将裂缝几何特征表征参数与变形裂缝中的渗透率定量关联起来，并与经典的Yeo模型进行了比较 [Chen 2017, pp. 3-5]。

## Key Findings
*   **Darcy流验证**：实验流量具有线性阶段，对应雷诺数很小（不同样本小于0.001到3.5），表明分析处于Darcy流有效范围内 [Chen 2017, pp. 11-13]。
*   **隙宽变化**：随着围压增加，连通空隙的隙宽（e′m）减小，呈现负相关。不同颗粒大小样本的减小速率不同，粗粒样本减小速率最低（30.2%和32.8%），细粒样本减小速率最高（55.5%和50%） [Chen 2017, pp. 11-13]。
*   **机械隙宽与有效机械隙宽的差异**：机械隙宽（em）普遍大于有效机械隙宽（e′m），原因在于 e′m 排除了孤立空隙的影响。粗粒样本两者差异小于中粒样本，细粒样本差异最大 [Chen 2017, pp. 11-13]。
*   **裂缝特性演化**：未加载状态下裂缝表面存在大量孤立空隙；随着应力增加，部分连通空隙会转变为孤立空隙 [Chen 2017, pp. 11-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 有效机械隙宽随围压增加呈负相关，粗粒样本减小速率最低（~30%），细粒最高（~50-55%） | [Chen 2017, pp. 11-13] | 六块不同粒径单裂缝砂岩，围压增加条件下 | 定量展示了隙宽演化的粒径敏感性。 |
| 雷诺数小（<0.001至3.5），表明实验流动处于Darcy流范围 | [Chen 2017, pp. 11-13] | 在不同围压和注水压力下，对所有样本的线性流阶段测量 | 确保了后续基于Darcy流的分析是有效的。 |
| 机械隙宽em普遍大于有效机械隙宽e′m，且差异在细粒样本中最大 | [Chen 2017, pp. 11-13] | 不同粒径砂岩样本，不同荷载条件 | 证实了排除孤立空隙（e′m）对于准确表征流动空隙尺寸的重要性。 |
| 应力增加导致部分连通空隙转变为孤立空隙 | [Chen 2017, pp. 11-13] | 所有样本，加载过程 | 阐明了裂缝内部空隙网络随应力演化的关键机制。 |

## Limitations
*   **样本数量与类型**：实验仅基于六块砂岩样本，且均为单一裂缝，结论向更复杂的裂缝网络的推广性未从索引片段中确认。
*   **实验条件**：流态被验证在Darcy流范围内，但更高流速下的非Darcy流效应（如Forchheimer流）未被涵盖 [Chen 2017, pp. 11-13]。
*   **模型通用性**：新建立的FGC模型仅与Yeo模型进行了比较，与其他现有模型（如基于Joint Roughness Coefficient (JRC)的模型）的普适性对比未从索引片段中确认。
*   **力学耦合**：研究的重点是围压对渗透率的影响，但可能未考虑剪切位移等其他力学作用对裂缝几何和水力特性的影响（未从索引片段中确认）。

## Assumptions / Conditions
*   **有效流动空间**：模型中仅连通空隙对渗透率有贡献，孤立空隙被排除在外 [Chen 2017, pp. 3-5]。
*   **流态**：裂缝中的流体流动被认为是层流，且服从达西定律 [Chen 2017, pp. 11-13]。
*   **裂缝几何模型**：裂缝的几何特征被抽象为连通空隙的尺寸、接触面积和异质性三个参数，并假设相对分形维数（D*Δ）可以有效表征连通空隙空间分布的异质性 [Chen 2017, pp. 3-5, 6-10]。
*   **初始状态**：相对分形维数（D*Δ）的计算是以围岩压力σ3=0 MPa时的绝对分形维数（DΔ_ref）为参考点 [Chen 2017, pp. 6-10]。

## Key Variables / Parameters
*   **有效机械隙宽（effective mechanical aperture， e′m）**：连通空隙的平均隙宽，是影响渗透率的直接尺寸参数 [Chen 2017, pp. 1-2, 6-10]。
*   **接触比（contact ratio， ω）**：裂缝表面接触面积与总面积的比值 [Chen 2017, pp. 1-2, 6-10]。
*   **相对分形维数（relative fractal dimension， D*Δ）**：表征连通空隙分布异质性的无量纲参数 [Chen 2017, pp. 1-2, 6-10]。
*   **围压（confining stress， σ3）**：施加的应力，是驱动裂缝几何特征变化的关键外部条件 [Chen 2017, pp. 10-13]。
*   **雷诺数（Reynolds number， Re）**：用于判别流态的准则数 [Chen 2017, pp. 11-13]。
*   **机械隙宽（mechanical aperture， em）**：裂缝的平均隙宽，用于与e′m对比 [Chen 2017, pp. 11-13]。

## Reusable Claims
*   **Claim 1**: 在评价粗糙裂缝的渗透性时，仅考虑连通空隙（即排除受接触区域包围的孤立空隙）对于获得准确的表征参数（如有效机械隙宽e′m）至关重要，因为孤立空隙对渗流没有贡献 [Chen 2017, pp. 3-5]。
*   **Claim 2**: 随着围压的增加，粗糙裂缝中的连通空隙会部分转变为孤立空隙，这使得有效机械隙宽（e′m）的减小幅度大于机械隙宽（em），特别是在细粒岩石中这种差异更为显著 [Chen 2017, pp. 11-13]。
*   **Claim 3**: 岩石颗粒大小是影响裂缝渗透率应力敏感性的重要地质因素。由粗粒砂岩构成的裂缝，其渗透率在应力作用下衰减速率低于细粒砂岩 [Chen 2017, pp. 11-13]。
*   **Claim 4**: 裂缝渗透率的表征需要综合考虑连通空隙的尺寸（由e′m表征）、接触面积（由ω表征）以及连通空隙的空间分布异质性（由D*Δ表征） [Chen 2017, pp. 1-2]。单纯的表面粗糙度不足以全面描述扭曲的渗流通道 [Chen 2017, pp. 2-3]。

## Candidate Concepts
*   [[fracture geometric characteristics]]
*   [[rough-walled fracture]]
*   [[effective mechanical aperture]]
*   [[contact ratio]]
*   [[relative fractal dimension]]
*   [[interconnected void spaces]]
*   [[cubic law deviation]]
*   [[tortuosity]]
*   [[fracture reservoir]]

## Candidate Methods
*   [[point-cloud data matching method]]
*   [[UTSP covering method]]
*   [[cubic covering method]]
*   [[modified Brazilian technique]]
*   [[Darcy flow test]]

## Connections To Other Work
*   本研究建立在以往关于裂缝粗糙度对流体流动影响的研究之上，提及了Lomize、Louis、Barton等人引入的联合粗糙度系数（JRC）等概念 [Chen 2017, pp. 2-3]。
*   研究继承了Cook等人 (Characterisation of the FGC by using two kinds of tortuosities) 和Yeo等人 (incorporation of the mean value and standard deviation of fracture apertures and the contact areas into the key characteristics of tortuosity) 关于裂缝几何特征及迂曲度的工作，并进一步引入了连通空隙异质性这一新特征 [Chen 2017, pp. 2-3]。
*   在实验方法上，本文提出的“点云数据匹配法”旨在克服传统方法如机械触针式表面轮廓仪（破坏表面）、X射线CT（低空间分辨率）、核磁共振成像（高成本）等的缺点 [Chen 2017, pp. 3-5]。
*   在分形方法上，本文改进的“超薄方块覆盖法”是基于传统的“立方体覆盖法”，并与分形理论先驱Mandelbrot的工作有渊源关系 [Chen 2017, pp. 6-10]。

## Open Questions
*   **有效机械隙宽（e′m）和渗透率之间在加载过程中的具体函数关系（即FGC模型）是什么？** 未从索引片段中确认。
*   **相对分形维数（D*Δ）与渗透率（或水力隙宽）之间的定量关系是怎样的？** 未从索引片段中确认。
*   **该FGC模型与经典Yeo模型的比较结果如何？** 谁更优以及各自的适用条件是什么？未从索引片段中确认。
*   **结论能否推广到其他类型的岩石或包含多条裂缝的复杂裂缝网络？** 未从索引片段中确认。
*   **剪切作用下的裂缝几何特征演化及其对渗透性的影响是什么？** 未从索引片段中确认。

## Source Coverage
本Markdown页面基于该论文的15个索引片段（涵盖pp. 1-13），覆盖了摘要、引言、理论背景和方法论部分，对创新点（FGC模型、点云数据匹配法）的定义有较详细覆盖。结果部分主要覆盖了隙宽演化的定性趋势和粒径效应，但涉及相对分形维数（D*Δ）、接触比（ω）与渗透率关系的定量结果（如FGC模型公式、与Yeo模型的对比评价）、完整的实验数据以及详细的讨论和结论部分，在提供的片段中不完整或完全缺失。因此，本页面对完整模型的构建、验证和最终结论的描述是不充分的。
