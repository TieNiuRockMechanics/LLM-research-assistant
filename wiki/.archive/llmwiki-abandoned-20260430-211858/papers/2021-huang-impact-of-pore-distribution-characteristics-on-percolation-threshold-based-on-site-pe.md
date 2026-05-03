---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-huang-impact-of-pore-distribution-characteristics-on-percolation-threshold-based-on-site-pe"
title: "Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory."
status: "draft"
source_pdf: "data/papers/2021 - Impact of pore distribution characteristics on percolation threshold based on site percolation theory.pdf"
collections:
citation: "Huang, Xudong, et al. \"Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory.\" *Physica A*, vol. 570, 2021, article 125800. doi:10.1016/j.physa.2021.125800."
indexed_texts: "12"
indexed_chars: "56285"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:52:02"
---

# Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory.

## One-line Summary
通过引入孔隙分布因子m改进经典点逾渗模型，数值模拟发现二维和三维多孔介质的逾渗阈值随m增大而降低，揭示了孔隙合并形成较大团簇是阈值下降的机理 [Huang 2021, pp. 1-2]。

## Research Question
孔隙分布特征如何影响基于点逾渗理论的多孔介质逾渗阈值？特别是，当每次生成的孔隙体积（用占有点数m表示）变化时，二维和三维体系的逾渗阈值如何变化？[Huang 2021, pp. 1-2]

## Study Area / Data
未提及具体自然研究区。研究对象为基于二维方形晶格和三维简单立方晶格的点逾渗模型生成的数值多孔介质，系统尺寸L分别为200–1000 (2D) 和120–200 (3D)，孔隙分布因子m取 1, 2, 5, 10, 15, 20, 25, 30, 35, 40。研究背景提及油页岩热解后或可溶盐矿溶浸后的多孔介质具有不规则形状和复杂尺寸分布，以此说明引入多占位系统的必要性 [Huang 2021, pp. 2-3] [Huang 2021, pp. 3-4] [Huang 2021, pp. 6-7] [Huang 2021, pp. 7-10]。

## Methods
提出一种改进的点逾渗填充方法，通过引入孔隙分布因子m（表示新生成孔隙占用的点数）扩展经典模型。每次随机位置生成体积为m的孔隙；若新孔隙与已有孔隙部分或完全重叠，则视为合并；这与不允许重叠的随机顺序吸附模型不同，因此不会出现堵塞态 [Huang 2021, pp. 2-3]。用数组表示多孔介质，0为固相，1为孔隙。记录孔隙度、孔隙数量分布、孔隙尺寸分布及最大团簇尺寸，并检测开放边界条件下的逾渗团簇 [Huang 2021, pp. 3-4]。采用有限尺寸标度技术，通过拟合逾渗概率与孔隙度的关系确定有效阈值，并利用Pc(L)与过渡宽度Δ(L)的线性关系外推得到无限大系统的全局逾渗阈值Pc(∞) [Huang 2021, pp. 4-6]。模拟使用Python编写，在个人计算机上运行约100天 [Huang 2021, pp. 3-4]。

## Key Findings
- **2D方形晶格**：当m从1增至40时，逾渗阈值从59.27%单调下降至38.38%。拟合经验关系为 Pc = 59.35603 m^{-0.11332} (R² = 0.997) [Huang 2021, pp. 6-7]。
- **3D简单立方晶格**：逾渗阈值同样随m增大而下降，从m=1时的31.16%降至m=40时的8.65% [Huang 2021, pp. 10-12]。
- **机理**：相同孔隙度下，m越大，孔隙数量越少，孔隙更容易重叠合并形成大团簇，降低逾渗阈值。孔隙体积分布的异质性随m增大而增强 [Huang 2021, pp. 7-10]。
- **临界指数**：3D模型的临界相关长度指数ν与随机逾渗的普适类值7/8在允许误差内一致，表明模型属于同一普适类 [Huang 2021, pp. 7-10]。
- 当m=1时，2D和3D阈值分别为59.27%和31.16%，与已有经典结果一致 [Huang 2021, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 2D逾渗阈值：m=1时59.27%，m=40时38.38%；3D逾渗阈值：m=1时31.16%，m=40时8.65% | [Huang 2021, pp. 6-7] [Huang 2021, pp. 10-12] | 2D方形晶格 (L=200–1000)；3D简单立方晶格 (L=120–200)；每次状态5000次模拟；有限尺寸标度外推至L→∞ | 含误差估计，参见原文表1和表2 |
| 2D Pc−m经验关系：Pc = 59.35603 m^{-0.11332} (m=1,2,3...40, R²=0.997) | [Huang 2021, pp. 6-7] | m=1–40 | 仅从模拟数据拟合，无理论推导 |
| 相同孔隙度(2D 45%; 3D 15%)下，m增大导致孔隙数量减少、团簇尺寸增大 | [Huang 2021, pp. 7-10] [Huang 2021, pp. 10-12] | 2D: m=1,10,40, 孔隙度45%; 3D: m=1,10,40, 孔隙度15% | 图解分析 |
| 3D临界指数ν与7/8在误差范围内一致 | [Huang 2021, pp. 7-10] | 3D模型，不同m值 | 普适类归属证据 |

## Limitations
- 未从索引片段中确认对2D模型临界指数ν是否与已知普适类一致进行了讨论。
- 模型生成的孔隙形状虽随机，但每次生成的孔隙体积固定为m个位点，能否完全表征自然多孔介质的复杂几何未从索引片段中确认 [Huang 2021, pp. 2-2]。
- 模拟仅在方形和简单立方晶格上进行，结果对其他晶格类型的适用性未从索引片段中确认。
- 计算资源限制：所有模拟结果需在个人计算机上运行约100天才获得，这可能限制了可探索的参数空间 [Huang 2021, pp. 3-4]。

## Assumptions / Conditions
- 孔隙位置完全随机，新孔隙可部分或全部与已有孔隙重叠，并视为合并 [Huang 2021, pp. 2-3]。
- 每次生成的孔隙体积固定为m个位点；相同m下各种孔隙形状生成概率相等 [Huang 2021, pp. 2-3] [Huang 2021, pp. 3-4]。
- 逾渗由开放边界条件下团簇从一个边界面跨越至对面边界面判定 [Huang 2021, pp. 4-6]。
- 使用有限尺寸标度理论，假设过渡宽度Δ(L) ∝ L^{-1/ν}，并利用Pc(L)与Δ(L)的线性关系求无限大系统阈值 [Huang 2021, pp. 4-6]。

## Key Variables / Parameters
- **m**：孔隙分布因子，表示每次新生成孔隙占用的点数 [Huang 2021, pp. 1-2]。
- **L**：系统尺寸 (2D: L=200–1000; 3D: L=120–200) [Huang 2021, pp. 6-7] [Huang 2021, pp. 7-10]。
- **Pc**：逾渗阈值（由有限尺寸标度外推至无穷大系统的极限）[Huang 2021, pp. 4-6]。
- **ν**：临界相关长度指数 [Huang 2021, pp. 4-6]。
- **Δ(L)**：逾渗过渡宽度 [Huang 2021, pp. 4-6]。
- **R_X^L(P)**：尺寸为L的系统在孔隙度P下的逾渗概率，X对应不同判据(U, A, I) [Huang 2021, pp. 4-6]。
- 孔隙数量分布、孔隙体积分布（PDF/CDF）、等效孔径、最大团簇尺寸 [Huang 2021, pp. 7-10]。

## Reusable Claims
- 在基于点逾渗的填充模型中，若新孔隙允许与已有孔隙重叠并合并，孔隙分布因子m增大将单调降低二维和三维体系的逾渗阈值；此效应的机理是孔隙数量的减少促进了大团簇的形成与合并 [Huang 2021, pp. 1-2] [Huang 2021, pp. 7-10]。
- 对于二维方形晶格和三维简单立方晶格，逾渗阈值Pc随m的变化可用经验幂律关系描述 (2D: Pc = 59.35603 m^{-0.11332}, R²=0.997)；当m=1时，阈值回归经典值(2D 59.27%, 3D 31.16%) [Huang 2021, pp. 6-7] [Huang 2021, pp. 10-12]。
- 该方法不会产生堵塞态，因此可在任意孔隙度下生成多孔介质；这与基于不允许重叠的随机顺序吸附模型有根本区别 [Huang 2021, pp. 2-3]。

## Candidate Concepts
- [[site percolation]]
- [[percolation threshold]]
- [[pore distribution factor]]
- [[finite-size scaling]]
- [[universality class]]
- [[multiple-occupation system]]
- [[random porous media generation]]
- [[pore cluster merging]]
- [[jamming state]]
- [[CT image analysis with percolation]]

## Candidate Methods
- [[site percolation model with variable occupation number]]
- [[finite-size scaling for percolation threshold]]
- [[pore network generation by overlapping site clusters]]
- [[numerical simulation of 3D porous media]]
- [[pore size distribution analysis (PDF/CDF)]]

## Connections To Other Work
- 引用Cornette等人的多点占用模型(Ref. [47]), 但区别在于本模型允许新孔隙与已有孔隙重叠合并，因此避免堵塞态，并得到更低的逾渗阈值 [Huang 2021, pp. 2-3] [Huang 2021, pp. 6-7]。
- 提及传统连续逾渗理论中常将孔隙形状简化为规则几何体，而本论文的点逾渗模型在点位足够小时可以模拟任意形状的孔隙，并能与CT图像像素建立一一对应关系 [Huang 2021, pp. 2-2]。
- 提到部分天然多孔介质（如油页岩）的逾渗阈值远低于理想均质多孔介质的阈值，为本研究的动机来源之一 [Huang 2021, pp. 2-2]。

## Open Questions
- 所提出的模型及阈值–m关系如何在真实多孔介质（如油页岩CT图像）上进行验证和应用？[Huang 2021, pp. 2-2] 未从索引片段中确认。
- 孔隙合并规则（部分/完全重叠即合并）在物理上对应于哪些具体地质或工程过程？未从索引片段中确认。
- 不同晶格类型（如面心立方、体心立方）或其他空间维度下，Pc–m的标度关系是否具有普适性？未从索引片段中确认。

## Source Coverage
本页基于给定12个索引片段撰写。片段涵盖摘要、引言、方法、部分结果与讨论。覆盖了核心模型构建、模拟参数、主要2D和3D阈值数据、机理分析和基本结论。缺少对临界指数ν在2D情形的讨论、误差分析的详细方法、与其他逾渗模型更深入的系统比较、以及所有图表数据的完整列表。部分材料性质（如逾渗过渡宽度Δ的具体拟合参数）未在片段中展开。
