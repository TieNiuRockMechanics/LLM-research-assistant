---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2007-feng-zengchao-二维孔隙裂隙双重介质逾渗规律研究-c4077ace"
title: "二维孔隙裂隙双重介质逾渗规律研究."
status: "draft"
source_pdf: "data/papers/二维孔隙裂隙双重介质逾渗规律研究_冯增朝.pdf"
collections:
citation: "Feng Zengchao, Zhao Yangsheng, and Lü Zhaoxing. \"二维孔隙裂隙双重介质逾渗规律研究.\" 物理学报, vol. 56, no. 5, May 2007, pp. 2796-2801."
indexed_texts: "2"
indexed_chars: "8685"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "8683"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99977"
coverage_status: "full-index"
source_signature: "834a5c62df68758969eb62f822af93be7d3443a5"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:11:09"
---

# 二维孔隙裂隙双重介质逾渗规律研究.

## One-line Summary
本文在孔隙介质逾渗理论基础上，引入裂隙通道，提出了二维孔隙裂隙双重介质的逾渗研究方法，通过数值计算揭示了孔隙率、裂隙分形维数和裂隙数量分布初值与逾渗概率的关系，并给出了逾渗阈值的数学表达式。[Feng 2007, pp. 1-5]

## Research Question
当前逾渗理论的研究仅局限于孔隙介质，忽略了裂隙这一主要的渗流通道，导致孔隙介质的逾渗理论不能与地质体（如煤层、油气储层）的渗流现象很好地符合。因此，需要研究孔隙裂隙双重介质的逾渗规律。[Feng 2007, pp. 1-5]

## Study Area / Data
本研究为理论研究，采用数值模拟方法。研究对象为二维平面模型，使用正方形网格（L×L，本文中取L=250）进行数值试验。[Feng 2007, pp. 1-5]

## Methods
1.  **孔隙分布**：在L×L的正方形网格中，按照给定的孔隙率n，将孔隙随机分布在网格的格子上。被孔隙占据的格子记为1（空隙），否则记为0（实体）。[Feng 2007, pp. 1-5]
2.  **裂隙生成**：使用二维裂隙迹线的分形参数描述裂隙。裂隙数量尺度服从分形关系式 N(δ) = N0·δ^(-D)，其中N0为裂隙数量分布初值，D为裂隙的分形维数。按给定的N0与D，生成各级尺度的裂隙，并随机分布于网格中。当裂隙落入某一格子且其长度大于格子尺度的1/2时，该格子记为1（空隙）。[Feng 2007, pp. 1-5]
3.  **介质叠加**：将孔隙和裂隙在网格中的[0, 1]分布按0+0=0，0+1=1，1+1=1的准则叠加，形成孔隙裂隙双重介质的最终网格分布。[Feng 2007, pp. 1-5]
4.  **逾渗概率计算**：编制计算机程序，寻找网格中的最大连通团，其包含的格子数量为M(L)。逾渗概率定义为 P(n, N0, D) = M(L)/L²，即空隙点属于最大连通团的概率。通过改变n、D、N0，获得逾渗概率的临界曲线。[Feng 2007, pp. 1-5]

## Key Findings
1.  孔隙和裂隙是影响逾渗现象的两个重要因素。当介质中包含裂隙时，发生逾渗的临界孔隙率减小；反之，当孔隙率增加时，发生逾渗的裂隙临界分形维数降低。[Feng 2007, pp. 1-5]
2.  孔隙裂隙双重介质发生逾渗转变的逾渗阈值是孔隙率n、裂隙分形维数D与裂隙数量分布初值N0三因素的数学组合，其数学表达式为：f(n, N0, D) = n_p^c - n - N0 * exp(-9.8687) * exp(4.7917D)，其中n_p^c为孔隙介质的临界孔隙率（取0.59275）。[Feng 2007, pp. 5-6]
3.  当f(n, N0, D) < 0时，介质内部没有跨越团，不发生逾渗转变，介质不可渗透；当f(n, N0, D) ≥ 0时，介质内部出现跨越团，发生逾渗转变，介质可以渗透。[Feng 2007, pp. 5-6]
4.  当孔隙率n=0时，临界分形维数Dc与裂隙数量分布初值N0满足关系：N0 = 8194.4 * exp(-4.6493 * Dc)。[Feng 2007, pp. 1-5]
5.  当裂隙分形维数D=1时，临界孔隙率nc与裂隙数量分布初值N0满足关系：nc = 0.59275 - 0.0097 * N0。[Feng 2007, pp. 1-5]
6.  当裂隙数量分布初值N0=e时，临界孔隙率nc与裂隙分形维数D满足关系：nc = 0.59725 - 0.0002 * exp(4.6578D)。[Feng 2007, pp. 1-5]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 逾渗阈值数学表达式：f(n, N0, D) = n_p^c - n - N0 * exp(-9.8687) * exp(4.7917D) | [Feng 2007, pp. 5-6] | 二维正方形网格模型 | n_p^c为孔隙介质临界孔隙率，取0.59275 |
| 当f(n, N0, D) ≥ 0时，孔隙裂隙双重介质发生逾渗转变，可以渗透。 | [Feng 2007, pp. 5-6] | 二维正方形网格模型 | 逾渗转变的判据 |
| 孔隙介质发生逾渗转变的临界孔隙率 n_c = 59.3% | [Feng 2007, pp. 1-5] | 二维正方形网格，N0=0（无裂隙） | 与经典结果59.275%接近 |
| 当孔隙率n=0时，N0 = 8194.4 * exp(-4.6493 * Dc) | [Feng 2007, pp. 1-5] | 二维正方形网格，n=0 | 相关系数r²=0.995 |
| 当D=1时，nc = 0.59275 - 0.0097 * N0 | [Feng 2007, pp. 1-5] | 二维正方形网格，D=1 | 相关系数r²=0.9976 |
| 当N0=e时，nc = 0.59725 - 0.0002 * exp(4.6578D) | [Feng 2007, pp. 1-5] | 二维正方形网格，N0=e | 相关系数r²=0.9916 |

## Limitations
1.  本文仅研究了二维平面模型正方形网格的逾渗规律。对于其他形式的网格（如三角形、六边形）以及三维立体情况，在以后的研究中再做讨论。[Feng 2007, pp. 1-5]

## Assumptions / Conditions
1.  孔隙在网格中随机分布。[Feng 2007, pp. 1-5]
2.  裂隙的分布服从分形几何规律，其数量与尺度满足关系式 N(δ) = N0·δ^(-D)。[Feng 2007, pp. 1-5]
3.  裂隙在网格中的位置与方位是随机分布的。[Feng 2007, pp. 1-5]
4.  当裂隙落入某一格子中，其长度大于格子尺度的1/2时，才认为该格子为孔隙网格（记为1）。[Feng 2007, pp. 1-5]
5.  孔隙和裂隙对网格状态的贡献采用叠加规则（0+0=0，0+1=1，1+1=1）。[Feng 2007, pp. 1-5]

## Key Variables / Parameters
-   **孔隙率 (n)**：网格中被孔隙占据的格子比例。[Feng 2007, pp. 1-5]
-   **裂隙分形维数 (D)**：描述裂隙分布复杂程度的参数。[Feng 2007, pp. 1-5]
-   **裂隙数量分布初值 (N0)**：分形关系式 N(δ) = N0·δ^(-D) 中的常数。[Feng 2007, pp. 1-5]
-   **逾渗概率 (P)**：空隙点属于最大连通团的概率，P = M(L)/L²。[Feng 2007, pp. 1-5]
-   **等效孔隙率 (n_e)**：孔隙裂隙双重介质中，由孔隙和裂隙共同贡献的有效孔隙率。[Feng 2007, pp. 5-6]
-   **临界孔隙率 (n_c)**：发生逾渗转变时的孔隙率阈值。[Feng 2007, pp. 1-5]
-   **临界分形维数 (D_c)**：发生逾渗转变时的裂隙分形维数阈值。[Feng 2007, pp. 1-5]

## Reusable Claims
1.  **条件**：在二维正方形网格的孔隙裂隙双重介质模型中。**主张**：逾渗转变的发生由孔隙率n、裂隙分形维数D和裂隙数量分布初值N0共同决定，其阈值满足数学表达式 f(n, N0, D) = n_p^c - n - N0 * exp(-9.8687) * exp(4.7917D)。当f≥0时，介质可渗透。[Feng 2007, pp. 5-6]
2.  **条件**：对于孔隙率n=0的纯裂隙介质。**主张**：发生逾渗转变的临界分形维数Dc与裂隙数量分布初值N0呈指数衰减关系：N0 = 8194.4 * exp(-4.6493 * Dc)。[Feng 2007, pp. 1-5]
3.  **条件**：对于裂隙分形维数D=1的介质。**主张**：临界孔隙率nc随裂隙数量分布初值N0的增加而线性减小，关系为 nc = 0.59275 - 0.0097 * N0。[Feng 2007, pp. 1-5]

## Candidate Concepts
-   [[percolation theory]]
-   [[porous medium]]
-   [[fractured medium]]
-   [[double-medium]]
-   [[percolation threshold]]
-   [[fractal geometry]]
-   [[fractal dimension]]
-   [[connectivity]]
-   [[spanning cluster]]

## Candidate Methods
-   [[numerical simulation]]
-   [[Monte Carlo method]] (implied by random distribution)
-   [[fractal modeling]]
-   [[cluster analysis]]

## Connections To Other Work
1.  本研究基于Hammersley (1957)提出的孔隙介质逾渗理论。[Feng 2007, pp. 1-5]
2.  裂隙的描述采用了分形几何学方法，参考了相关研究。[Feng 2007, pp. 1-5]
3.  论文引用了逾渗理论在多个领域（如材料科学、地球物理）的应用研究。[Feng 2007, pp. 1-5]

## Open Questions
1.  其他形式的网格（如三角形、六边形）以及三维立体情况下，孔隙裂隙双重介质的逾渗规律如何？[Feng 2007, pp. 1-5]

## Source Coverage
所有非空索引片段均已处理。索引文本数量：2，索引字符数：8685。编译源块数量：2，编译源字符数：8683。覆盖率按块计算为1.0，按字符计算为0.99977。覆盖状态为full-index。[Coverage audit data provided]
