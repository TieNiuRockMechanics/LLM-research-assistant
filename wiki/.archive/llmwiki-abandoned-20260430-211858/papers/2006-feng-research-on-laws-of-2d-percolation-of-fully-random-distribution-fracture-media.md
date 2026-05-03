---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2006-feng-research-on-laws-of-2d-percolation-of-fully-random-distribution-fracture-media"
title: "Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media."
status: "draft"
source_pdf: "data/papers/2006 - Research on laws of 2D percolation of fully random distribution fracture media.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Zengchao, et al. “Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media.” *Chinese Journal of Rock Mechanics and Engineering*, vol. 25, no. Supp. 2, Oct. 2006, pp. 3904-05."
indexed_texts: "2"
indexed_chars: "7167"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:22:52"
---

# Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media.

## One-line Summary
本文基于裂缝分形分布规律，通过数值模拟研究了全随机分布裂隙介质的二维逾渗现象，并获得了包含裂缝分形维数和初始分形常数的逾渗阈值数学表达式 [Feng 2006, pp. 1-5]。

## Research Question
如何描述和确定全随机分布裂隙介质（Fully Random Distribution Fracture Media）在二维条件下的逾渗规律及其逾渗阈值？[Feng 2006, pp. 1-5]。

## Study Area / Data
未从索引片段中确认。

## Methods
- 基于裂缝数量分形规律，提出了适用于全随机分布裂隙介质逾渗研究的模拟方法 [Feng 2006, pp. 1-5]。
- 采用数值模拟方法对二维逾渗现象及规律进行研究 [Feng 2006, pp. 1-5]。

## Key Findings
1.  **介质分类**：根据介质中裂缝的方向性，将孔隙-裂隙介质分离为部分随机分布裂隙介质、分组分布裂隙介质和全随机分布裂隙介质 [Feng 2006, pp. 1-5]。
2.  **逾渗阈值表达式**：通过数值模拟，获得了包含裂缝分形维数（\( D \)）、初始分形常数（\( N_0 \)）和孔隙率的逾渗阈值数学表达式 [Feng 2006, pp. 1-5]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 基于裂缝数量分形规律，提出了一种可用于全随机分布裂隙介质逾渗的模拟方法。 | [Feng 2006, pp. 1-5] | 介质为全随机分布裂隙介质，裂缝数量满足分形分布规律 \( N(\delta) = N_0\delta^{-D} \)。 | 具体模拟步骤未从索引片段中确认。 |
| 获得了包含裂缝分形维数与孔隙率的逾渗阈值数学表达式。 | [Feng 2006, pp. 1-5] | 基于提出的数值模拟方法。 | 最终表达式的具体形式未在索引片段中给出。 |
| 逾渗阈值（\( p_c \)）在特定情况下与经典逾渗值（\( p_c = 0.59275 \)）有联系。 | [Feng 2006, pp. 5-5] | 未从索引片段中确认具体条件。 | 原文提到“।༣ੱ (pc = 0.59275) ݔ ഒ ູ 0”，可能指在某些参数下其阈值与此经典值吻合或有偏差。 |

## Limitations
- 索引片段仅为论文摘要和部分引言及方法描述，缺失完整的模型建立、数值模拟细节、结果分析和讨论。
- 未从索引片段中确认研究样本来源、模型尺寸、边界条件等具体实验参数。
- 无法获知文章结论的局限性和作者未来工作建议。

## Assumptions / Conditions
- **介质分类假设**：根据裂缝方向，将介质分为三类，其中本文聚焦于“全随机分布裂隙介质” [Feng 2006, pp. 1-5]。
- **分形分布假设**：假设裂缝的数量服从分形分布规律 \( N(\delta) = N_0\delta^{-D} \)，其中 \( \delta \) 为尺度，\( N(\delta) \) 为大于该尺度的裂缝数量，\( N_0 \) 为初始分形常数，\( D \) 为分形维数 [Feng 2006, pp. 1-5]。
- **模型假设**：模拟在一个 \( L \times L \) 的网格上进行，最大连通团簇定义为在该网格中跨越整个模型区域的连通裂缝集合 [Feng 2006, pp. 1-5]。

## Key Variables / Parameters
- **\( D \)**：裂缝分形维数 [Feng 2006, pp. 1-5]。
- **\( N_0 \)**：裂缝的初始分形常数 [Feng 2006, pp. 1-5]。
- **\( N(\delta) \)**：尺度大于 \( \delta \) 的裂缝数量 [Feng 2006, pp. 1-5]。
- **\( \delta \)**：用于裂缝分形统计的尺度 [Feng 2006, pp. 1-5]。
- **\( n \)**：裂缝数量（或概率）的控制参数，用于表征逾渗状态 [Feng 2006, pp. 1-5]。
- **\( n_c \)**：逾渗阈值对应的临界 \( n \) 值 [Feng 2006, pp. 1-5]。
- **\( P_{\infty}(n) \)**：无限大网格中出现跨越团簇的概率，\( P_{\infty}(n) = 0 \) 在 \( n < n_c \) 时，\( P_{\infty}(n) \neq 0 \) 在 \( n = n_c \) 时 [Feng 2006, pp. 1-5]。
- **\( p_c = 0.59275 \)**：被提及的经典逾渗阈值参考值 [Feng 2006, pp. 5-5]。
- **孔隙率**：逾渗阈值的数学表达式包含此参数 [Feng 2006, pp. 1-5]。

## Reusable Claims
1.  **介质类型定义**：对于裂隙介质逾渗问题，根据裂缝的定向性，可以划分为三种类型：部分随机分布、分组分布和全随机分布。此分类是基于物理机制对裂隙介质模型的简化假设 [Feng 2006, pp. 1-5]。
2.  **分形模拟方法有效性**：基于裂缝数量分形分布规律（\( N(\delta) = N_0\delta^{-D} \)）构建的二维数值模拟方法，可以有效用于研究全随机分布裂隙介质的逾渗规律。证据是该方法成功获得了逾渗阈值表达式。此结论的成立条件是裂缝系统满足分形统计特征 [Feng 2006, pp. 1-5]。
3.  **逾渗阈值公式的构成**：全随机分布裂隙介质的二维逾渗阈值可以表示为一个包含裂缝分形维数（\( D \)）、初始分形常数（\( N_0 \)）和孔隙率的函数。该公式的具体形式未从索引片段中确认 [Feng 2006, pp. 1-5]。

## Candidate Concepts
- [[Fully random distribution fracture media]]
- [[Porosity and fracture double-media (孔隙-裂隙双重介质)]]
- [[Percolation threshold]]
- [[Fracture fractal dimension]]
- [[2D percolation of fracture networks]]

## Candidate Methods
- [[Fractal-based numerical simulation for percolation]]
- [[Connectivity analysis in fractured media]]

## Connections To Other Work
- **基于引文标题的候选连接 (Candidate Connections)**：
    - **分形岩石力学**：[Feng 2006] 引用了谢和平 1996 年著作《分形-岩石力学导论》[Feng 2006, pp. 5-5]，表明其裂缝分形建模的理论基础来源之一是 [[fractal rock mechanics]]。
    - **作者自引**：[Feng 2006] 的方法学似乎建立在作者此前的工作之上，引用了多篇自有的相关研究，如煤体中的逾渗机理 [Feng 2005]、裂隙煤岩逾渗机制 [Feng 2004, pp. 1-5] 和岩体裂隙三维分形分布规律 [Feng 2005, pp. 5-5]，表明此为同一团队的系列研究，致力于构建完整的裂隙介质逾渗理论。

## Open Questions
- 论文推导出的逾渗阈值数学表达式的具体函数形式是什么？[未从索引片段中确认]
- 部分随机分布、分组分布和全随机分布三种介质在二维逾渗行为上有何具体差异？[未从索引片段中确认]
- 数值模拟是如何具体实现“全随机分布”这一条件的（例如方向角分布函数）？[未从索引片段中确认]
- 除了裂缝数量分形，是否考虑了裂缝长度、开度等其他几何参数的分形特性？[未从索引片段中确认]

## Source Coverage
本 Markdown 页面完全依据提供的 2 个索引片段（包含摘要、引言、方法简介和参考文献）生成。这些片段提供了研究背景、核心方法思路和主要结论框架，但**严重缺失**详细的模型建立、数值模拟实现过程、完整的结果数据分析以及与现有理论对比的讨论部分。因此，本文档无法覆盖论文的完整论证过程和所有量化结果。
