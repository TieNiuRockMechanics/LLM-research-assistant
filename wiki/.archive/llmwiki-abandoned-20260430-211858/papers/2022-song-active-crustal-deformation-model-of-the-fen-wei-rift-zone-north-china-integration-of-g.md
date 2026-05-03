---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-song-active-crustal-deformation-model-of-the-fen-wei-rift-zone-north-china-integration-of-g"
title: "Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets."
status: "draft"
source_pdf: "data/papers/2022 - Active crustal deformation model of the Fen–Wei rift zone, North China Integration of geologic, geodetic, and stress direction datasets.pdf"
collections:
  - "山西断裂地质构造"
citation: "Song, Shangwu, et al. \"Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets.\" *Frontiers in Earth Science*, vol. 10, 2022, doi:10.3389/feart.2022.964800."
indexed_texts: "16"
indexed_chars: "78787"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:40:26"
---

# Active Crustal Deformation Model of the Fen–Wei Rift Zone, North China: Integration of Geologic, Geodetic, and Stress Direction Datasets.

## One-line Summary
本研究利用运动学有限元模型 NeoKinema，联合反演地质断层滑动速率、大地测量 GPS 速度场和主压应力方向数据，构建了汾渭裂谷（FWRZ）的长期活动地壳形变模型，以约束其低应变运动学特征并评估地震危险性 [Song 2022, pp. 1-2]。

## Research Question
研究旨在通过整合多种运动学数据集，回答关于汾渭裂谷长期地壳形变的四个具体问题 [Song 2022, pp. 3-4]：
1.  裂谷内长期断层活动的总体特征是什么？
2.  沿东西向秦岭山脉是否存在显著的构造挤出？
3.  山西地堑系的剪切和伸展应变分布如何？
4.  裂谷内哪些区域表现出强震潜力？

## Study Area / Data
**研究区**：中国北部的汾渭裂谷（FWRZ），该区域是青藏高原挤出构造与西太平洋俯冲远程效应影响下的活动地壳形变过渡带。裂谷由一系列呈左阶雁列式分布的线性断陷盆地组成 [Song 2022, pp. 2-3]。研究中模拟了80条活动断层 [Song 2022, pp. 5-7]。

**数据源**：
*   **地质断层滑动速率**：32条断层晚第四纪的长期滑动速率和标准差，作为模型的先验约束 [Song 2022, pp. 5-7]。
*   **大地测量 GPS 速度场**：468个GPS基准站速度，均相对于稳定的欧亚板块。数据来自 Hao et al. (2021)，并已排除汶川地震和日本东北地震的同震及震后形变影响。对于震间锁定效应，使用了负位错模型（统一锁定深度1-15公里）进行校正 [Song 2022, pp. 7]。
*   **主压应力方向**：来自世界应力图计划（WSM 2016），共541个数据，主要来源于震源机制解和水压致裂法 [Song 2022, pp. 7-9]。

## Methods
使用运动学有限元程序 **NeoKinema** (Bird and Liu, 2007)，通过加权最小二乘法联合拟合更新的地质滑动速率、大地测量速度和应力方向数据集，反演最优的长期断层滑动速率和水平形变场 [Song 2022, pp. 4-5]。

模型的目标函数 Π 包含三项 [Song 2022, pp. 4-5]：
1.  预测大地测量速度与观测值的拟合。
2.  预测断层滑动速率与地质长期滑动速率的拟合。
3.  连续体（非断层单元）的应变率最小化和各向同性约束。

模型构建了一个包含1,069个节点和540个三角形单元的有限元网格，网格边长在20至100公里之间 [Song 2022, pp. 5-7]。

**参数确定**：
*   **连续体刚度系数 (μ)**：通过L2范数误差拟合测试（图3），在0.01-1的范围内选定 [Song 2022, pp. 7-9]。
*   **参考长度 (L0) 和参考面积 (A0)**：在 L0 > 1.65 × 10⁴ m 后拟合改进不再显著，而 A0 > 2.2 × 10⁹ m² 时大地测量和断层滑动速率误差减小，但连续体刚度和应力方向误差增加。通过权衡选定最优组合（图4）[Song 2022, pp. 7-9]。

## Key Findings
1.  **低应变背景**：汾渭裂谷是一个典型的低应变运动学环境，大多数活动断层预测的滑动速率低于1毫米/年 [Song 2022, pp. 9-10]。
2.  **有限构造挤出**：从鄂尔多斯地块南部到秦岭山脉的总左旋剪切速率约为1毫米/年，表明沿近东西向秦岭山脉的构造挤出有限。左旋剪切作用表现为弥散性，而非集中在个别断层上 [Song 2022, pp. 10-11]。
3.  **山西地堑系的变形分布**：山西地堑系中部显示出约0.5毫米/年的显著右旋剪切，并向南北两端递减。大同盆地和运城盆地分别对应约1.1-1.2毫米/年的地壳伸展 [Song 2022, pp. 10-11]。
4.  **地震空区与潜在地震危险性**：预测的地震活动性与历史地震记录对比揭示了一些显著的地震空区，特别是在大同盆地、韩城盆地和运城盆地，表明这些区域具有较高的潜在地震危险性 [Song 2022, pp. 14-15]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 大多数活动断层滑动速率 < 1 mm/a | [Song 2022, pp. 9-10] (Table 2, Figure 6) | 模型最优解 | 反映了晚第四纪低应变运动学背景 |
| 鄂尔多斯地块与秦岭间的总左旋剪切速率约为 1 mm/a | [Song 2022, pp. 10-11] (Figure 7) | 模型预测的长期速度场 | 指示有限构造挤出 |
| 山西地堑系中部右旋剪切约 0.5 mm/a，大同和运城盆地伸展约 1.1-1.2 mm/a | [Song 2022, pp. 10-11] (Figure 8, Figure 9) | 模型预测的应变率场 | 右旋剪切向南北两端递减 |
| 铁炉子断裂左旋走滑速率仅 0.13 ± 0.11 mm/a | [Song 2022, pp. 9-10] (Figure 6B) | 模型预测结果 | 显著低于晚第四纪地质估计的 0.5-1.25 mm/a，可能因弥散剪切或观测误差 |
| 大同、韩城、运城盆地存在地震空区 | [Song 2022, pp. 14-15] (Figure 12) | 模型预测地震活动率与历史记录对比 | 指示较高潜在地震危险性 |

## Limitations
*   模型反演的质量依赖于输入地质滑动速率的不确定性，这些不确定性受到地质年代学约束的限制 [Song 2022, pp. 9-10]。
*   对于次级地震源（secondary seismic sources）的预测能力可能不足，导致在显著性检验中出现差异 [Song 2022, pp. 14-15]。
*   模型预测的震源深度不能特异性地指示未来地震的确切深度 [Song 2022, pp. 14-15]。

## Assumptions / Conditions
*   **运动学模型**：NeoKinema 模型假设断层滑动速率和连续体应变场代表长期（稳态）的永久变形 [Song 2022, pp. 4-5]。
*   **先验约束**：将晚第四纪地质断层滑动速率作为先验约束条件 [Song 2022, pp. 5-7]。
*   **GPS速度校正**：为获得长期形变，假设GPS速度受到震间断层锁定的影响，并通过一个统一锁定深度为1-15公里的负位错模型进行校正 [Song 2022, pp. 7]。
*   **应力方向数据**：假设主压应力方向数据（主要来自震源机制解）能代表长达10³年的地壳形变特征 [Song 2022, pp. 7-9]。
*   **断层几何**：模型包含了80条具有清晰地表迹线和倾角的主要活动断层，排除了缺少历史强震记录或晚第四纪强震地貌证据的次级断层 [Song 2022, pp. 5-7]。

## Key Variables / Parameters
*   **观测/约束变量**：观测大地测量速度 (r.), 观测地质长期滑动速率 (rm) 及其误差 (σm) [Song 2022, pp. 4-5]。
*   **模型预测变量**：预测大地测量速度 (p.), 预测断层滑动速率 (pm), 模型应变率 (pn) [Song 2022, pp. 4-5]。
*   **模型控制参数**：连续体刚度系数 (μ), 参考长度 (L0), 参考面积 (A0) [Song 2022, pp. 7-9]。

## Reusable Claims
*   **Claim 1: 低速率断层的运动学约束需要多源数据联合反演**：对于滑动速率普遍低于1毫米/年的活动裂谷（如汾渭裂谷），单一的GPS数据难以探测断层运动，而地质数据无法精确约束区域尺度形变。通过 NeoKinema 联合反演地质滑动速率、GPS速度和应力方向数据，可以有效弥补单一数据源的不足，获得最优的长期地壳形变模型。证据：模型成功应用于低应变的FWRZ，融合了三类数据（地质、大地测量、应力）。限制：反演结果的质量依赖于地质速率的不确定性（即测年约束）[Song 2022, pp. 3-4]。
*   **Claim 2: 构造挤出可能以弥散剪切而非单一断层滑动实现**：沿东西向秦岭山脉的总左旋剪切速率约1毫米/年，为有限的构造挤出。但模型预测的关键断层（铁炉子断裂）的走滑速率远低于地质估计，表明该剪切作用是弥散分布在整个剪切带而非局部化在个别断层上。证据：模型预测的铁炉子断裂左旋走滑速率（0.13 ± 0.11 mm/a）远低于地质估计（0.5-1.25 mm/a），而区域速度场支持弥散性剪切。限制：差异可能源于断层活动的时变性或观测误差，其根本原因尚未完全确定 [Song 2022, pp. 9-10]。
*   **Claim 3: 裂谷盆地内的伸展可能非单一由侧向剪切引起**：山西地堑系中部的右旋剪切（~0.5 mm/a）向两端递减，并在大同和运城盆地转化为~1.1-1.2毫米/年的地壳伸展。但模型分析表明，这些显著的伸展不能完全归因于中部右旋剪切引起的终端效应（terminal effects）。证据：模型预测的剪切和伸展应变分布模式。限制：产生这种不匹配的非剪切伸展分量的驱动机制，未从索引片段中确认 [Song 2022, pp. 10-11]。

## Candidate Concepts
*   [[intra-continental rifting]] (大陆内部裂陷)
*   [[transtensional tectonics]] (拉分构造)
*   [[low-strain kinematic setting]] (低应变运动学背景)
*   [[seismic gap]] (地震空区)
*   [[extrusion tectonics]] (挤出构造)
*   [[far-field subduction effect]] (远程俯冲效应)
*   [[kinematic finite-element model]] (运动学有限元模型)

## Candidate Methods
*   [[NeoKinema]]
*   [[joint inversion of geologic and geodetic data]]
*   [[GPS velocity field correction for interseismic locking]]
*   [[negative dislocation model]]
*   [[World Stress Map data integration]]
*   [[weighted least-squares method for kinematic constraint fitting]]

## Connections To Other Work
*   **在方法上连接**：本研究的联合反演方法（使用NeoKinema）与应用于意大利中部低应变拉张带的类似研究直接关联，引用了 Carafa et al., 2020 作为成功案例 [Song 2022, pp. 3-4]。
*   **在主题上连接**：本研究的方法论可与以下工作进行对比或扩展：
    *   与仅使用地质数据估计的FWRZ特定断层滑动速率进行对比，如 [[Deng et al., 1994; Xu et al., 2013; Middleton et al., 2017]] [Song 2022, pp. 4-5]。
    *   与仅使用GPS数据估计的盆地伸展率进行对比，如 [[Zhao et al., 2017]] [Song 2022, pp. 4-5]。
    *   对比本研究涉及的GPS数据来源 [[Hao et al., 2021]] 和其处理方法。
*   **在区域动力学上连接**：研究区的构造活动被置于青藏高原挤出（如 [[Zhang et al., 1995; Tapponnier et al., 2001]]）和西太平洋俯冲远程效应（张-渤地震带，如 [[Zhang et al., 2018; Hao et al., 2020]]）两大构造域过渡的背景下 [Song 2022, pp. 2-3]。

## Open Questions
*   在铁炉子断裂上观察到的模型预测走滑速率与晚第四纪地质估计值之间的显著差异，是由断层活动的时变性（time-varying fault motion）、大地测量和/或地质测量的观测误差，还是由弥散剪切机制造成的？这需要进一步研究 [Song 2022, pp. 9-10]。
*   大同盆地和运城盆地显著的、不能完全由中部右旋剪切的终端效应解释的地壳伸展，其明确的动力学来源是什么？未从索引片段中确认。
*   模型预测地震活动率时，对次级地震源的适用性或局限性，其背后具体的物理机制是什么？未从索引片段中确认。

## Source Coverage
本知识页基于论文的16个索引片段生成。这些片段覆盖了论文的摘要（第1-2页）、引言/背景（第2-5页）、方法学理论及建模细节（第4-9页）、部分结果（第9-11页）和部分讨论（第14-15页）。覆盖包含了研究问题、方法的核心部分和关键发现，但可能缺失完整的讨论、详细的地震活动性对比分析、以及所有结果图表的完整解释。关于次级地震源预测局限性的具体机制，以及部分断层的完整数据表，未能从当前片段中完全确认。
