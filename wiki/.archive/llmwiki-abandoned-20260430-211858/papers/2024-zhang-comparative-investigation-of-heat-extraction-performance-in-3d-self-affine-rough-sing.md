---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-zhang-comparative-investigation-of-heat-extraction-performance-in-3d-self-affine-rough-sing"
title: "Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid."
status: "draft"
source_pdf: "data/papers/2024 - Comparative investigation of heat extraction performance in 3D self-affine rough single fractures using CO2,N2O and H2O as heat transfer fluid3D.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhang, Jiansong, et al. \"Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid.\" *Renewable Energy*, vol. 235, 2024, p. 121309. doi:10.1016/j.renene.2024.121309."
indexed_texts: "12"
indexed_chars: "59008"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:49:34"
---

# Comparative Investigation of Heat Extraction Performance in 3D Self-Affine Rough Single Fractures Using CO₂, N₂O and H₂O as Heat Transfer Fluid.

## One-line Summary
在核心尺度（φ50×100 mm）3D自仿射粗糙单裂缝中，基于NIST热物性数据与热-流耦合模型，对比CO₂、N₂O和H₂O的采热性能，发现CO₂和N₂O的出口平均温度和采热率基本一致且均低于水 [Zhang 2024, pp. 1-1]。

## Research Question
在增强型地热系统（EGS）核心尺度粗糙单裂缝中，不同传热流体（CO₂、N₂O、H₂O）在恒定入口流速变入口温度、及恒定入口温度变入口流速条件下的采热性能差异如何？ [Zhang 2024, pp. 1-1]

## Study Area / Data
本研究为数值模拟，不涉及具体地理区域。裂缝几何基于分形自仿射函数生成，代表干热岩（HDR）岩心尺度单裂缝；流体热物性来源于NIST REFPROP 9.1数据库，温度范围37–300 °C、压力30 MPa [Zhang 2024, pp. 4-7, 7-8]。

## Methods
采用Weierstrass-Mandelbrot (W-M)函数构建3D自仿射粗糙裂缝几何，节理粗糙度系数JRC=12.38，分形维数D=2.5，尺度常数G=1.5，样本长度L=100 mm [Zhang 2024, pp. 4-7]。利用NIST数据拟合CO₂、N₂O和H₂O的密度、比热容、导热系数、动力粘度随温度变化的构方程（式9–式16） [Zhang 2024, pp. 7-8]。建立热-流（TH）耦合数值模型，求解质量、动量和能量守恒方程，流体热物性实时更新；出口压力恒为30 MPa，岩石外边界温度200 °C，初始温度37 °C，裂缝宽度1 mm [Zhang 2024, pp. 8-11]。模型通过已有水和CO₂实验出口温度验证，最大误差分别为3.8%和2.4% [Zhang 2024, pp. 8-11]。对比在不同入口流速（0.005, 0.015, 0.025 m/s）和入口温度（37, 47, 57 °C）下的出口平均温度（式29）和采热率HER（式30） [Zhang 2024, pp. 11-12]。

## Key Findings
- CO₂和N₂O在裂缝出口的瞬态平均温度和采热率基本一致，且均低于H₂O；提高入口流速和温度时该差距保持 [Zhang 2024, pp. 1-1, 12-14]。
- 入口流速升高（0.005→0.025 m/s）显著增强热对流，导致裂缝表面沿分割线的温度起伏加剧；入口温度升高（37→57 °C）对温度分布曲线形态的影响小于流速变化，即流速为主导因素 [Zhang 2024, pp. 12-14]。
- CO₂和N₂O因热物性（密度、比热容、粘度、导热系数）相似，沿分割线的温度波动趋势高度一致 [Zhang 2024, pp. 12-14]。
- 在裂缝边缘区域（x=10 mm和x=40 mm），H₂O温度初期低于CO₂和N₂O，随后迅速攀升并在出口附近与两者趋同；在裂缝内部（x=20 mm与x=30 mm），H₂O温升较平缓 [Zhang 2024, pp. 12-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| CO₂与N₂O的出口平均温度和HER基本相同，且均低于H₂O。 | [Zhang 2024, pp. 1-1, 12-14] | JRC 12.38粗糙裂缝，30 MPa，200 °C岩壁，入口流速0.005–0.025 m/s，入口温度37–57 °C。 | 结论基于TH耦合模型与NIST拟合物性。 |
| 入口流速增大导致热对流效应更显著，温度沿分割线的波动加剧。 | [Zhang 2024, pp. 12-14] | 分割线位置x=10,20,30,40 mm。 | 流速变化比入口温度变化对温度分布影响更大。 |
| 裂缝边缘H₂O温度初期低于CO₂和N₂O，后升高并在末端收敛；内部区域收敛较缓。 | [Zhang 2024, pp. 12-14] | 入口流速0.005–0.025 m/s，入口温度37–57 °C。 | 归因于热物性差异。 |
| 水和CO₂出口温度模型验证误差分别≤3.8%和≤2.4%。 | [Zhang 2024, pp. 8-11] | 水数据来源未指明，CO₂数据来自Jiang Peixue实验 [22]。 | 验证了数值模型可靠性。 |

## Limitations
未从索引片段中确认作者明确列出的局限性。可推断的局限包括：仅针对单一JRC（12.38）和特定分形参数；未考虑化学作用、相变或流体-岩石反应；热物性拟合仅在37–300 °C、30 MPa下有效；验证数据有限（仅出口温度）；核心尺度结果向现场尺度的外推存在不确定性 [Zhang 2024, pp. 1-1, 8-11]。

## Assumptions / Conditions
- 裂缝几何为W-M函数生成的3D自仿射粗糙面，JRC=12.38，D=2.5，G=1.5，L=100 mm，裂缝宽度1 mm [Zhang 2024, pp. 4-7, 8-11]。
- 流体物性仅为温度的函数（压力恒定30 MPa），取自NIST REFPROP 9.1，并拟合为多项式 [Zhang 2024, pp. 7-8]。
- 岩石外边界温度恒为200 °C，初始全场温度37 °C，出口压力30 MPa [Zhang 2024, pp. 8-11]。
- 流动为单相层流，无相变与化学反应，壁面无滑移。
- TH耦合通过实时更新密度、比热容、导热系数、粘度实现。
- 性能评价采用出口平均温度和HER，稳态定义为出口平均温度不随时间变化 [Zhang 2024, pp. 11-12]。

## Key Variables / Parameters
- 裂缝几何：D (2.5)，G (1.5)，L (100 mm)，JRC (12.38)，裂缝宽度 (1 mm) [Zhang 2024, pp. 4-7]。
- 操作条件：入口流速v_in (0.005, 0.015, 0.025 m/s)，入口温度T_in (37, 47, 57 °C)，岩壁温度 (200 °C)，出口压力 (30 MPa) [Zhang 2024, pp. 8-11]。
- 流体热物性：ρ(T), Cp(T), k(T), μ(T)，由多项式（式9–式16）给出 [Zhang 2024, pp. 7-8]。
- 性能指标：出口平均温度（式29），采热率HER (P, 式30)，进出口温差 ΔT_out [Zhang 2024, pp. 11-12]。

## Reusable Claims
1. **对于JRC=12.38的3D自仿射粗糙单裂缝，在30 MPa和200 °C岩壁温度下，CO₂和N₂O的出口平均温度与采热率在0.005–0.025 m/s入口流速范围内几乎相等，且始终低于H₂O。** 该结论基于NIST物性实时耦合的TH模型，验证误差≤3.8%，适用于核心尺度分析，但未包含化学-力学效应 [Zhang 2024, pp. 1-1, 8-14]。
2. **裂缝表面温度分布起伏主要受入口流速控制，而非入口温度；提高流速会加剧温度沿流线的波动。** 在CO₂、N₂O和H₂O中均观察到该行为，CO₂与N₂O因热物性相似而波动趋势一致 [Zhang 2024, pp. 12-14]。
3. **H₂O在裂缝边缘区域初始温度低于CO₂和N₂O，但随后迅速攀升并在出口附近趋同；在裂缝内部，H₂O温升较缓，收敛迟滞。** 该空间非均匀性源于各流体的比热容和导热系数差异 [Zhang 2024, pp. 12-14]。
4. **利用W-M函数生成粗糙裂缝并结合NIST REFPROP 9.1拟合的热物性方程，可建立高精度核心尺度TH耦合模型，出口温度预测误差≤3.8%（水）和2.4%（CO₂）。** 这种方法适用于对比不同传热流体的核心尺度采热性能 [Zhang 2024, pp. 4-11]。

## Candidate Concepts
- [[Enhanced Geothermal System]]
- [[Heat Transfer Fluid]]
- [[Self-affine fracture]]
- [[Weierstrass-Mandelbrot function]]
- [[Joint Roughness Coefficient (JRC)]]
- [[Thermo-hydraulic coupling]]
- [[Core-scale experiment]]
- [[Hot Dry Rock]]
- [[Supercritical fluid]]
- [[NIST REFPROP]]

## Candidate Methods
- [[Weierstrass-Mandelbrot fractal surface generation]]
- [[Coupled thermo-hydraulic modeling]]
- [[NIST-based property fitting]]
- [[Mean outlet temperature calculation]]
- [[Heat extraction rate (HER) evaluation]]
- [[Model validation with experimental outlet temperatures]]

## Connections To Other Work
- Wang Chunguang [21] 同样发现提高入口温度和流速可增强采热率；本文在此基础上对比了三种流体 [Zhang 2024, pp. 1-3]。
- Jiang Peixue [22] 的CO₂在0.2 mm光滑裂缝中对流换热实验数据被用于本模型验证，出口温度最大误差2.4% [Zhang 2024, pp. 8-11]。
- Huang M. et al. (2020) [18] 在垂直光滑裂缝中比较CO₂、N₂O和H₂O，得出N₂O采热功率高于CO₂且稳定运行时间长于H₂O-EGS；本粗糙裂缝结果则显示N₂O与CO₂性能相近且均低于H₂O，表明裂缝粗糙度可能改变流体间的相对优势 [Zhang 2024, pp. 3-4]。
- 与现场尺度随机离散裂缝网络研究（如Zhang, J. et al. 2022 [12]; He, R. H. et al. 2022 [15]）互补：核心尺度单裂缝研究可减少场尺度不确定性，但需注意尺度升级 [Zhang 2024, pp. 3-4]。

## Open Questions
未从索引片段中确认作者提出的开放问题。可能需要进一步研究的主题包括：不同JRC和分形参数的影响、其他超临界流体、长期运行热衰减、化学反应与溶解/沉淀、以及核心尺度到现场尺度的放大准则。索引片段未提供相关讨论。

## Source Coverage
本页基于全部12个索引片段，覆盖了摘要、引言、方法（W-M函数生成几何、NIST热物性拟合、TH模型及边界条件）、模型验证、以及结果与讨论（出口平均温度、温度分布、HER对比）。片段未包含的部分可能包括：更详细的数值求解设置、网格无关性分析、敏感性研究、完整的讨论和结论段落。核心定量发现可从现有片段中充分提取，但模型局限性与未来研究方向的信息缺失。
