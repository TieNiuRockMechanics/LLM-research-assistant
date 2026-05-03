---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-nie-a-new-method-for-three-dimensional-fracture-network-modelling-for-trace-data-collected"
title: "A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window."
status: "draft"
source_pdf: "data/papers/2020 - A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Nie, Zhenbang, et al. \"A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.\" *Rock Mechanics and Rock Engineering*, vol. 53, 2020, pp. 1145-1161, doi:10.1007/s00603-019-01969-4."
indexed_texts: "13"
indexed_chars: "63131"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:55:52"
---

# A New Method for Three-Dimensional Fracture Network Modelling for Trace Data Collected in a Large Sampling Window.

## One-line Summary

本研究提出一种基于大采样窗口裂隙迹线数据的三维裂隙网络建模新方法，核心是通过随机数学从迹长推导裂隙圆盘直径，并在大藤峡水电站下游岩体中验证了其可行性 [Nie 2020, pp. 1-2]。

## Research Question

如何基于大面积露头采集的无截尾偏差的裂隙迹长数据，快速且准确地确定三维裂隙圆盘尺寸（直径）、密度和产状，以生成可靠的三维裂隙网络模型？ [Nie 2020, pp. 3-4]。

## Study Area / Data

- **研究区**：大藤峡（Datengxia）水电站泄水闸下游岩体，具体为下游剖面 #28 的岩体 [Nie 2020, pp. 8-9]。
- **地层与岩性**：
  - 属早泥盆世（Lower Devonian）的那高岭组（D1n）和郁江组（D1y）灰岩 [Nie 2020, pp. 8-9]。
  - 建模对象排除了 D1n 和 D1y1-1 地层（由于软层间距小，裂隙常被截断），专注于 D1y1-2 和 D1y1-3 地层（软层间距10-20米，通常大于裂隙尺寸1-6米）。[Nie 2020, pp. 8-9]。
- **现场数据**：
  - 对裂隙进行了分组，D1y1-3 分为 2 组（158条, 119条），D1y1-2 分为 2 组（308条, 82条）。[Nie 2020, pp. 9-11]。
  - 收集了各组裂隙的**迹长（Trace Length）**、**倾向（Dip Direction）**、**倾角（Dip Angle）** 的均值和标准差 [Nie 2020, pp. 9-11, Table 2]。
  - 现场采集窗口面积记为 `A` [Nie 2020, pp. 6-8]。

## Methods

1.  **裂隙圆盘直径确定（核心创新）**：
    - **基本假设**：裂隙为圆盘状 [Nie 2020, pp. 2-3]。
    - **目标**：从现场采集的迹长（`2ch`）数据推导出三维空间中的裂隙圆盘半径（`r`）及其概率分布函数（PDF）[Nie 2020, pp. 3-4]。
    - **关键流程**：
        a. 假设裂隙圆盘与揭露面的交切关系（`u` 为圆心到迹线的垂直距离），生成均匀随机数 `u/r ~ U(0,1)` [Nie 2020, pp. 4-5]。
        b. 根据迹长平方的期望 `E(ch2)` 计算出半径平方的期望 `E(r2) = 1.5 * E(ch2)` [Nie 2020, pp. 4-5, pp. 5-6, Table 2]。
        c. 指定 `r2` 的一种分布类型（如正态、伽马、对数正态、负指数分布），通过**试错法**调整其方差 `D(r2)`，使得生成的随机 `ch2` 数据集的方差与现场采集迹长的方差 `D(ch2)` 相等 [Nie 2020, pp. 4-5]。
        d. 使用卡方检验（Chi-square test）确定 `r2` 的最优分布类型 [Nie 2020, pp. 9-11]。
        e. 将 `r2` 的随机数开方得到 `r` 的随机数，并将其等分为 `X` 个区间，通过公式计算各区间的裂隙数量分布，最终生成三维空间中的裂隙半径 `r'` 及其 PDF [Nie 2020, pp. 5-6]。

2.  **裂隙产状与密度确定**：
    - **产状**：虽然现场采集的产状是取样于三维空间的样本，但方法直接将其用于表征三维空间中的裂隙产状 [Nie 2020, pp. 6-8]。
    - **密度**：采用**试错法**确定裂隙数量 `n`。通过不断调整 `n`，使得三维裂隙网络与一个和现场揭露面同产状的虚拟平面的交切面上，产生的迹线数量 `N'` 满足 `N' = (A'/A) * N`（其中 `N` 为现场采集到的裂隙数，`A'` 和 `A` 分别是虚拟交切面和现场采集面的面积）[Nie 2020, pp. 6-8]。

3.  **三维裂隙网络生成**：
    - 裂隙中心点位置服从齐次泊松（Poisson）模型，随机生成三维坐标 [Nie 2020, pp. 6-8]。
    - 结合已生成的裂隙圆盘尺寸、产状和中心点坐标，使用蒙特卡洛模拟（Monte Carlo simulation）合成所有几何信息，生成最终的三维裂隙网络 [Nie 2020, pp. 6-8]。

## Key Findings

- **方法可行性验证**：对于 D1y1-2 和 D1y1-3 地层的各组裂隙，通过生成的三维裂隙网络与一个和原始露头产状一致的虚拟平面相交，得到了模拟迹线。该模拟迹线的**统计特征与现场露头采集的迹线特征高度相似**（“highly similar”），从而证明了所提方法的可行性 [Nie 2020, pp. 1-2]。
- **方法效率**：该方法因其采集于大采样窗口的数据不存在截尾偏差，并且使用简单公式生成随机数，因此操作**简便、快速**，避免了复杂的迹线截尾校正等程序 [Nie 2020, pp. 3-4, pp. 5-6]。
- **直径与迹长的关系**：无论 `r2` 符合何种分布（正态、伽马、对数正态、负指数），其数学期望的比值 `E(r2)/E(ch2)` 始终在 1.5 左右（测试中范围为 1.48–1.54）[Nie 2020, pp. 5-6]。
- **小裂隙影响评估**：现场可能无法采集的小尺寸裂隙会导致 `E(ch2)` 和 `D(ch2)` 的值产生偏差，但这种由截断（truncation）引起的差异在工程实践中是**可接受的**（“relatively small and thus acceptable”）[Nie 2020, pp. 4-5]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 模拟迹线与现场迹线的统计特征高度相似。 | [Nie 2020, pp. 1-2] | 方法验证，大藤峡水电站研究区域，D1y1-2 和 D1y1-3 地层。 | 推断方法可行性的直接证据。 |
| E(r2) 与 E(ch2) 的比值稳定在 1.5 左右。 | [Nie 2020, pp. 5-6] | 测试了伽马、对数正态、正态、负指数四种分布类型，不同的参数组合。 | 这是该方法中一个固定的数学转换关系。 |
| 小裂隙截断造成的 `E(ch2)` 和 `D(ch2)` 偏差在工程上可接受。 | [Nie 2020, pp. 4-5] | 该声明在方法部分提出，在讨论部分(Sect. 6)有提及。 | 未从索引片段中确认具体的数值偏差分析。 |

## Limitations

- **小裂隙截断效应**：方法承认现场采集会遗漏微小裂隙，虽然声明其影响在工程上可接受，但这仍然是一个潜在的偏差来源，可能导致模型对裂隙尺寸和数量的估计存在误差 [Nie 2020, pp. 4-5]。
- **裂隙形状假设**：整个模型基于裂隙是圆盘的理想化假设，未考虑真实裂隙形状的复杂性 [Nie 2020, pp. 2-3]。
- **产状偏差处理**：未从索引片段中确认该方法如何具体处理或校正由露头方向引起的裂隙产状采样偏差（Terzaghi 偏差）。片段提到前人提出了不同方法，但未说明本研究的具体措施 [Nie 2020, pp. 2-3]。
- **模型验证范围**：验证仅在一个研究区域（大藤峡水电站下游）进行，其在不同地质条件和构造背景下的普适性未从索引片段中确认。
- **尺度效应**：未从索引片段中确认模型在处理超出研究区尺寸的尺度效应时的有效性。

## Assumptions / Conditions

- **基本几何假设**：裂隙被视为圆形薄盘 [Nie 2020, pp. 2-3]。
- **样本代表性**：现场收集的裂隙迹线数据在统计上能代表大采样窗口内的真实裂隙分布。
- **通过性假设**：为简化分析并保证工程安全，假设裂隙是**贯穿的（through-going）**，即它们可以穿透软层而不被截断 [Nie 2020, pp. 8-9]。
- **空间分布**：裂隙中心点在三维空间中的分布遵循齐次泊松模型（Homogeneous Poisson Model），即完全随机分布 [Nie 2020, pp. 6-8]。
- **数学关系**：裂隙迹长平方的期望值 `E(ch2)` 与圆盘半径平方的期望值 `E(r2)` 之间存在固定的数学关系 `E(r2) = 1.5 * E(ch2)` [Nie 2020, pp. 4-5]。
- **数据特征**：该方法适用于大采样窗口，其特点是数据包含大量完整的裂隙几何信息，且不存在截尾偏差 [Nie 2020, pp. 3-4]。

## Key Variables / Parameters

- `ch`: 半迹长 (Half-trace length) [Nie 2020, pp. 1-2, pp. 4-5]
- `r`: 裂隙圆盘半径 (Radius of fracture disc) [Nie 2020, pp. 4-5]
- `r'`: 推导出的三维空间中的裂隙圆盘半径 (Final simulated radius of fracture discs in 3D space) [Nie 2020, pp. 5-6]
- `u`: 圆心到迹线的垂直距离 [Nie 2020, pp. 4-5]
- `E(x)`: 期望值 (Expected value) [Nie 2020, pp. 4-5]
- `D(x)`: 方差 (Standard deviation) [Nie 2020, pp. 4-5]
- `N`: 现场采集的裂隙数量 [Nie 2020, pp. 6-8]
- `N'`: 模拟得到的虚拟交切面上的迹线数量 [Nie 2020, pp. 6-8]
- `n`: 三维裂隙网络中的裂隙总数（密度） [Nie 2020, pp. 6-8]
- `A`: 现场采集面积 [Nie 2020, pp. 6-8]
- `A'`: 三维裂隙网络与虚拟露头面的交切面积 [Nie 2020, pp. 6-8]
- `X`: 半径等分区间数，用于计算半径分布 [Nie 2020, pp. 5-6]

## Reusable Claims

- **Claim 1**: 对于一个基于迹线数据的三维裂隙圆盘网络模型，当假设裂隙为圆盘且其与采样面随机相交时，迹长平方的期望值 `E(ch2)` 和圆盘半径平方的期望值 `E(r2)` 之间存在固定转换关系 `E(r2) = 1.5 * E(ch2)`。该关系经多种分布类型（伽马、对数正态、正态、负指数分布）的数值模拟验证 [Nie 2020, pp. 5-6]。
- **Claim 2**: 验证三维裂隙网络模型合理性的一个有效方法是，用与原露头产状一致的虚拟平面切割模型得到模拟迹线，并将其统计特征（如迹长分布）与现场采集迹线进行对比 [Nie 2020, pp. 1-2]。
- **Claim 3**: 对于大采样窗口的裂隙数据，由于遗失小裂隙导致的迹长统计参数偏差在工程实践上是可接受的，可用此数据进行三维裂隙网络建模 [Nie 2020, pp. 4-5]。

## Candidate Concepts

- [[fracture network modelling]]（三维裂隙网络建模）
- [[trace data]]（迹线数据）
- [[fracture disc diameter]]（裂隙圆盘直径）
- [[sampling window]]（采样窗口）
- [[soft layer]]（软层）
- [[through-going fracture]]（贯穿裂隙）
- [[Monte Carlo simulation]]（蒙特卡洛模拟）
- [[Poisson model]]（泊松模型）

## Candidate Methods

- [[Chi-square test for distribution fitting]]（卡方分布拟合检验）
- [[trial-and-error method for parameter determination]]（参数试错确定法）
- [[random number generation for geometric parameters]]（几何参数的随机数生成）
- [[Monte Carlo method for fracture network synthesis]]（裂隙网络合成的蒙特卡洛方法）
- [[intersection of virtual plane for validation]]（虚拟平面交切验证方法）
- [[trace length to disc radius derivation]]（迹长到圆盘半径的推导法）
- [[statistical comparison for model validation]]（模型验证的统计对比法）

## Connections To Other Work

- **裂隙形状假设**：本文假设裂隙为圆盘，延续了 Kulatilake and Wu (1986) 等人的研究传统 [Nie 2020, pp. 2-3]。
- **采样偏差**：文中提及 Terzaghi (1965), Priest (1985) 和 Wathugala et al. (1990) 等在处理裂隙产状采样偏差方面的贡献 [Nie 2020, pp. 2-3]。
- **裂隙平均迹长与尺寸/密度计算**：文中引用了 Priest and Hudson (1981), Kulatilake and Wu (1984, 1986), Priest (1993) 和 Oda (1982) 等在研究平均迹长、裂隙三维尺寸和密度计算方面的前期工作 [Nie 2020, pp. 2-3]。
- **数据采集技术**：文章提及三维激光扫描和近景数字摄影测量等新技术在大面积裂隙采集中的应用，是该方法的数据来源背景 [Nie 2020, pp. 3-4]。
- **领域主题连接**：可从主题上连接到 [[fracture reservoir]]、[[rock mass quality assessment]]、[[slope stability analysis]] 和 [[geostatistics]] 等候选概念。

## Open Questions

- 对于产状并非完全随机、显示强烈择优方位的裂隙组，该方法是否完全无需进行产状偏差校正？
- 该方法在处理被软层或其它结构面大量截断的非贯穿性裂隙网络时的适用性如何？[Nie 2020, pp. 8-9 提到这种情况会让建模更复杂]
- 该方法中未详细讨论裂隙的力学及水力开度特性，这些信息如何整合到此几何模型中？
- 能否将该方法扩展应用于非平面露头或隧道掌子面上收集的迹线数据？未从索引片段中确认。

## Source Coverage

本页依据来自[Nie 2020]的13个索引片段进行编写。这些片段主要涵盖了论文的摘要、引言、方法（第2章）、研究区与数据（第3章）、建模结果与验证（第4章）等关键部分。覆盖内容包括论文的核心算法流程、关键公式、研究区概况和部分结果。然而，索引片段未能覆盖：
- 详细的案例研究背景介绍。
- 讨论部分（第6章），例如对小裂隙截断影响的详细量化分析。
- 最终结论部分。
- 除迹长统计特征外的其它详细模型验证结果。
- 详细列出所有符号的列表信息（片段中仅部分出现）。
