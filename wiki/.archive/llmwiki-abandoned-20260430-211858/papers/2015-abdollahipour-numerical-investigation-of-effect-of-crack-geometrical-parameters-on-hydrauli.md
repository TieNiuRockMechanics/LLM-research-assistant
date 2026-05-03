---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2015-abdollahipour-numerical-investigation-of-effect-of-crack-geometrical-parameters-on-hydrauli"
title: "Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs."
status: "draft"
source_pdf: "data/papers/2015 - Numerical investigation on the effect of crack geometrical parameters in hydraulic fracturing process of hydrocarbon reservoirs.pdf"
collections:
  - "审稿人让引用"
citation: "Abdollahipour, A., et al. \"Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs.\" *Journal of Mining & Environment*, 22 Dec. 2015. Accessed 2026."
indexed_texts: "8"
indexed_chars: "35957"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:21:55"
---

# Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs.

## One-line Summary
利用高阶位移不连续法（HODDM）数值模拟初始裂纹几何参数（间距、长度、相位角）对水平井和垂直井水力压裂过程中裂纹扩展和干扰的影响，以优化裂缝布置 [Abdollahipour 2015, pp. 1-2]。

## Research Question
初始水力压裂裂缝的不同几何参数（模式、间距、裂缝长度和射孔相位角）如何影响裂纹的扩展、干扰与止裂，以及水平井和垂直井中最佳的裂缝布置方案是什么？ [Abdollahipour 2015, pp. 1-2]。

## Study Area / Data
- **数据来源**：基于现场数据来设定模型的几何和力学属性 [Abdollahipour 2015, pp. 2-3]，并引用了Yu等人[40]的气产量现场测量数据来验证模拟结果 [Abdollahipour 2015, pp. 6-8]。
- **验证数据**：使用文献中的实验室预置裂纹岩石类试件（直径60 mm，长度120 mm）裂纹扩展结果，来验证HODDM的裂纹扩展预测能力 [Abdollahipour 2015, pp. 4-6]。

## Methods
- **核心模拟方法**：使用了基于位移不连续法（DDM）的二维代码，并加入立方单元位移不连续（HODDM）以提高精度 [Abdollahipour 2015, pp. 2-3]。
- **裂纹尖端处理**：在每个裂纹尖端使用特殊裂纹尖端单元以提高裂纹附近奇异应力/位移的计算精度 [Abdollahipour 2015, pp. 3-4]。
- **断裂准则**：基于线弹性断裂力学，采用Erdogan和Sih提出的最大切向应力混合模式断裂准则来确定裂纹起裂角θ [Abdollahipour 2015, pp. 2-3]。
- **模型参数归一化**：提出并使用归一化参数 `β = S/L`（其中S为间距，L为裂缝长度）来推广分析结果 [Abdollahipour 2015, pp. 2-3]。
- **模拟方案**：
    - **水平井**：分为所有射孔裂缝（PFs）等长，以及具有不同长度（L1>L2）的两种组合进行模拟，每种组合下研究了不同的β值 [Abdollahipour 2015, pp. 6-8]。
    - **垂直井**：研究了两种常见的射孔相位角（φ = 60° 和 φ = 120°）及其与最大水平主应力（σH）方向的偏差角β的影响 [Abdollahipour 2015, pp. 8-9]。

## Key Findings
- **归一化参数β的最佳值**：在裂缝等长情况下，最佳结果出现在β = 1.0, 1.5, 和 2.0。由于更密的裂纹有助于提高渗透率，β = 1（即间距等于裂缝长度）可能是最佳情况，这与其它研究结果吻合 [Abdollahipour 2015, pp. 8-9]。
- **不同长度裂缝组合的影响**：当外侧裂缝更长时，最佳工况为β = 2.0；当内侧裂缝更长时，最佳工况为β = 1.25。所有射孔裂缝等长时裂纹扩展效果最好，而外侧裂缝更长且间距较小时裂纹扩展效果最差 [Abdollahipour 2015, pp. 8-9]。
- **裂纹干扰与止裂现象**：在特定裂纹模式（pattern）中观察到了裂纹干扰和裂纹止裂现象；较小的间距可能导致强烈的裂纹干扰，从而降低产量。这与Yu等人[40]的现场生产数据（间距小于100英尺时产量低）规律一致 [Abdollahipour 2015, pp. 1-2, 6-8]。
- **垂直井最佳相位角**：对于相位角φ = 120°，所有射孔裂缝均完全扩展（除垂直于σH的裂缝外），最佳效果可能在任意偏离σH的角度获得（β = 30° 和 90° 除外），结果优于φ = 60° [Abdollahipour 2015, pp. 8-9]。
- **数值方法验证**：
    - 通过与斜裂纹问题的解析解对比，HODDM在预测应力强度因子（SIFs）时的误差小于0.2% [Abdollahipour 2015, pp. 4-6]。
    - 数值模拟的裂纹扩展路径成功捕捉了实验室预置裂纹试件的实验结果，验证了HODDM的准确性和适用性 [Abdollahipour 2015, pp. 4-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| HODDM预测应力强度因子的误差小于0.2%。 | [Abdollahipour 2015, pp. 4-6] | 斜裂纹问题，包含最多4个裂纹尖端元素。 | 通过解析解验证数值方法精度。 |
| 数值模拟成功捕捉了实验室预置裂纹岩石试件的裂纹扩展行为。 | [Abdollahipour 2015, pp. 4-6] | 试件直径60 mm，长120 mm，含两条同路径裂纹（α=60°），与第三条裂纹成β角，单轴压缩。 | 验证HODDM模拟任意裂纹扩展的能力。 |
| 裂缝等长时，最佳归一化间距β为1、1.5、2，其中β=1（即间距等于长度）可能为最优。 | [Abdollahipour 2015, pp. 8-9] | 水平井，等长射孔裂缝，多裂缝扩展分析，最大20个扩展步。 | 考虑渗透率贡献，更近的裂缝更优。 |
| 裂缝长度不等时，较长裂缝位于外侧的最优β为2.0，位于内侧的最优β为1.25。 | [Abdollahipour 2015, pp. 8-9] | 水平井，两种长度（L1>L2）的射孔裂缝组合。 | 等长裂缝整体效果最佳。 |
| 垂直井中，相位角φ=120°优于φ=60°，几乎所有非垂直于σH的裂缝都能完全扩展。| [Abdollahipour 2015, pp. 8-9] | 垂直井，两种射孔相位角，不同偏离σH的角度。 | φ=120°时，β=30°和90°结果不佳。 |
| 裂缝间距小于裂缝长度（如间距<100 ft）时，因裂缝干扰导致产量低。 | [Abdollahipour 2015, pp. 6-8] | 引用Yu等人[40]的现场累计产气数据，裂缝长250 ft。 | 与本研究中观察到的裂纹干扰现象相印证。 |

## Limitations
- 模型基于二维假设，可能与真实三维裂缝扩展存在差异 [Abdollahipour 2015, pp. 2-3]。
- 岩石被假定为不渗透材料，且射孔裂缝中的压力是均匀的，可能不完全符合水力压裂中复杂的流-固耦合情况 [Abdollahipour 2015, pp. 2-3]。
- 裂纹扩展分析仅考虑了最多20个扩展步，可能未完全达到最终稳定状态 [Abdollahipour 2015, pp. 8-9]。
- 未从索引片段中确认：研究中是否考虑了天然裂缝、地层非均质性或水力压裂液的滤失效应。

## Assumptions / Conditions
- **岩石假设**：岩石被假设为不渗透的线弹性材料 [Abdollahipour 2015, pp. 2-3]。
- **应力条件**：井筒轴线与一个水平主应力方向对齐；模型深度为2500 m；远场主应力 σv = 64 MPa, σh = 47 MPa [Abdollahipour 2015, pp. 2-3]。
- **载荷条件**：射孔裂缝和井筒内压力为均匀的30 MPa [Abdollahipour 2015, pp. 2-3]。
- **力学属性**：弹性模量E = 40 GPa, 泊松比ν = 0.2, 断裂韧性KIC = 3 MPa√m, 抗压强度110 MPa, 抗拉强度17.5 MPa [Abdollahipour 2015, pp. 2-3]。
- **断裂准则**：起裂角由最大切向应力混合模式断裂准则确定 [Abdollahipour 2015, pp. 2-3]。
- **几何条件**：井筒半径R = 0.1 m [Abdollahipour 2015, pp. 2-3]。

## Key Variables / Parameters
- `β ( = S/L )`：归一化裂缝间距（间距S / 裂缝长度L），用于推广分析结果 [Abdollahipour 2015, pp. 2-3]。
- `S`：裂缝间距 [Abdollahipour 2015, pp. 2-3]。
- `L`：裂缝长度 [Abdollahipour 2015, pp. 2-3]。
- `φ`：垂直井射孔相位角 [Abdollahipour 2015, pp. 8-9]。
- `θ`：裂纹起裂角 [Abdollahipour 2015, pp. 2-3]。
- `σH, σv, σh`：最大水平主应力、垂向应力、远场水平主应力 [Abdollahipour 2015, pp. 2-3, 8-9]。
- `P`：射孔裂缝和井筒内压 [Abdollahipour 2015, pp. 2-3]。
- `KIC`：岩石断裂韧性 [Abdollahipour 2015, pp. 2-3]。
- `E, ν`：岩石弹性模量和泊松比 [Abdollahipour 2015, pp. 2-3]。

## Reusable Claims
1.  **观点**：水力压裂中，当多个等长初始裂缝的间距等于裂缝长度时，可在保持较高渗透率的同时实现较优的扩展效果，提供了一种可量化的优化准则。[证据] 本研究通过数值模拟发现等长裂缝在β=1时效果最佳，且此发现与现场生产数据（间距等于裂缝长度时产能最优）规律一致 [Abdollahipour 2015, pp. 6-8, 8-9]。[限制] 此结论基于不渗透岩石和均匀内压的二维线弹性模型。
2.  **观点**：在水平井多级压裂中，采用不等长裂缝设计会加剧近井筒区域的裂缝弯曲（tortuosity）和交叉，特别是当外侧裂缝长于内侧裂缝时，扩展效果比等长设计差。[证据] 数值模拟显示，外侧长裂缝组合在多种间距下发生了内侧裂缝与外层裂缝的交叉，而等长裂缝组合的扩展形态最优 [Abdollahipour 2015, pp. 6-8]。[限制] 研究限于两种特定长度组合，且为二维分析。
3.  **观点**：垂直井水力压裂采用120°相位角射孔，相较于60°相位角，更能适应井筒周围复杂的应力环境，使更多方位的射孔簇得以有效扩展。[证据] 模拟结果显示在120°相位角下，除垂直于最大水平主应力方向的裂缝外，几乎所有裂缝都能完全扩展，优于60°相位角 [Abdollahipour 2015, pp. 8-9]。[限制] 结论基于特定现场地应力（σv=64 MPa, σh=47 MPa）条件。
4.  **观点**：高阶位移不连续法（HODDM）结合特殊裂纹尖端单元，可以将二维线弹性断裂问题中的应力强度因子数值误差降低到0.2%以下，并能准确复现实验室中的裂纹扩展路径。[证据] 通过斜裂纹解析解和预置裂纹岩石试件实验双重验证 [Abdollahipour 2015, pp. 4-6]。[限制] 验证限于二维、静态或准静态裂纹扩展。

## Candidate Concepts
- [[Hydraulic Fracturing]]
- [[Crack Propagation]]
- [[Crack Interference / Stress Shadowing]]
- [[Fracture Spacing Optimization]]
- [[Perforation Phase Angle]]
- [[Near-Wellbore Tortuosity]]
- [[Linear Elastic Fracture Mechanics (LEFM)]]
- [[Crack Arrest]]

## Candidate Methods
- [[Higher Order Displacement Discontinuity Method (HODDM)]]
- [[Special Crack Tip Element]]
- [[Maximum Tangential Stress Criterion (Erdogan & Sih)]]
- [[Stress Intensity Factor (SIF) Calculation]]
- [[Numerical Rock Fracture Simulation]]
- [[Normalized Parameter Analysis (β)]]

## Connections To Other Work
- **方法关联**：本研究的核心方法HODDM是[[Displacement Discontinuity Method (DDM)]]的高阶改进版，常用于模拟[[Rock Fracture Propagation]]和[[Mining Engineering]]中的裂纹问题 [Abdollahipour 2015, pp. 2-3, 3-4]。
- **结论验证**：研究中关于裂缝干扰导致产量降低并发现在间距等于裂缝长度时存在最佳值的结论，与Yu等人[40]的现场生产数据分析结果一致 [Abdollahipour 2015, pp. 6-8]。
- **模型参数引用**：本研究使用的岩石力学参数和几何模型基于Rahman等人[26]的现场数据 [Abdollahipour 2015, pp. 2-3]。

## Open Questions
- 未从索引片段中确认：水力压裂液粘度、注入速率等施工参数对最佳裂缝几何参数的影响。
- 未从索引片段中确认：三维裂缝扩展、岩石的非均质性、天然裂缝激活、渗透性以及流-固耦合效应会如何改变文中得出的最佳归一化间距β和最佳相位角。
- 未从索引片段中确认：文中对“最佳”的定量评价标准是最大化产量、裂缝面积还是基于扩展步数的纯几何判断。片段提及“更好的生产” [Abdollahipour 2015, pp. 1-2]，但未给出其直接的量化指标。

## Source Coverage
本Wiki页基于提供的 **8** 个索引片段构建，覆盖了论文的摘要、引言、方法（HODDM原理与验证）、核心数值实验结果和结论部分。信息覆盖比较全面，能够勾勒出研究的主要框架和关键发现。然而，索引片段主要集中在论文的中后段，对引言（第1节）和部分参考文献的覆盖较少。关于“研究区/数据”的详细信息（除验证实验外）和完整的“讨论”部分可能缺失。所有信息均明确依据所给片段，未从片段中确认的内容已如实标注。
