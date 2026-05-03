---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties"
title: "Spectral-Type Simulation of Spatially Correlated Fracture Set Properties."
status: "draft"
source_pdf: "data/papers/1985 - Spectral-type simulation of spatially correlated fracture set properties.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Miller, Stanley M., and Leon E. Borgman. \"Spectral-Type Simulation of Spatially Correlated Fracture Set Properties.\" *Mathematical Geology*, vol. 17, no. 1, 1985, pp. 41-42."
indexed_texts: "5"
indexed_chars: "23086"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T10:37:49"
---

# Spectral-Type Simulation of Spatially Correlated Fracture Set Properties.

## One-line Summary
提出一种利用快速傅里叶变换（FFT）的谱分析方法，用于高效模拟在空间上具有相关性的裂隙组几何属性（如方位、间距、迹长等）[Miller 1985, pp. 1-2, 10-11]。

## Research Question
如何高效地模拟裂隙组中具有空间相关性（自相关性）的几何属性，如方位、间距、迹长和弯曲度？[Miller 1985, pp. 1-2]

## Study Area / Data
未从索引片段中确认。论文提及使用“通过野外填图收集的裂隙组数据”（fracture set data collected by field mapping）来估计变异函数，但未提及具体的研究区域[Miller 1985, pp. 1-2]。模拟示例中的一个属性为倾角（Dip），其分布直方图被用于展示，但具体数据来源未说明[Miller 1985, pp. 5-10]。

## Methods
该方法的核心是利用谱分析（spectral-type simulation）来模拟裂隙属性，其步骤如下：
1.  **估计变异函数与协方差函数**：基于野外填图获得的裂隙组数据，沿裂隙组平均矢量方向计算目标属性的实验变异函数，其中滞后距（lag）通常以裂隙数量而非实际距离来衡量。然后，通过公式 `C(h) = σ² - γ(h)` 从变异函数得到协方差函数，其中 `γ(h)` 是变异函数值， `σ²` 是估计方差 [Miller 1985, pp. 2-5]。
2.  **计算谱密度**：谱密度是协方差函数的傅里叶变换。在离散形式下，谱密度 `Sm` 通过对数字化的协方差函数 `Cn` 进行傅里叶变换计算得出 [Miller 1985, pp. 2-5]。这一步骤通过快速傅里叶变换（FFT）算法高效实现 [Miller 1985, pp. 1-2]。
3.  **生成傅里叶系数**：生成一组非相关的、非平稳的傅里叶系数。[Miller 1985, pp. 2-5]。
4.  **赋予方差并进行逆变换**：根据第2步计算出的谱密度，为生成的傅里叶系数赋予适当的方差。然后，对这些系数进行逆傅里叶变换，以生成具有期望方差和变异函数特征的模拟数据 [Miller 1985, pp. 1-2]。
5.  **针对不同分布的模拟**：
    *   **正态分布数据**：上述通用步骤即可实现 [Miller 1985, pp. 1-2]。
    *   **指数分布数据**：通过生成两个独立、均值为0、方差 `σ² = μ_U / 2` 的正态分布序列，其协方差函数 `C(h)` 由期望的指数分布协方差函数 `C_U(h)` 通过 `C(h) = [C_U(h) / 4]^{1/2}` 推导得出。然后，将这两个正态模拟数据的平方相加 `U_i = X_i^2 + Y_i^2`，即可得到具有正确均值和协方差函数的指数分布模拟值 [Miller 1985, pp. 5-10]。

## Key Findings
*   谱分析模拟方法能有效生成具有指定空间相关结构（变异函数）的裂隙组属性 [Miller 1985, pp. 10-11]。
*   该方法在计算上十分高效，利用了快速傅里叶变换（FFT）的速度优势。示例中，在 DECsystem-20 计算机上模拟256个数据点仅需0.60至0.82秒的CPU时间 [Miller 1985, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 模拟的裂隙属性表现出期望的空间相关性，即正确的协方差函数。 | [Miller 1985, pp. 10-11] | 用于正态分布和指数分布数据。 | 逆傅里叶变换产生具有所需方差和变异函数特征的模拟值 |
| 模拟256个指数分布的裂隙数据耗时0.82秒。 | [Miller 1985, pp. 10-11] | 示例运行于DECsystem-20计算机。 | 验证了方法的高计算效率。 |
| 指数分布模拟值 `U_i` 的生成公式：`U_i = X_i^2 + Y_i^2`。 | [Miller 1985, pp. 5-10] | `X_i` 和 `Y_i` 是具有特定协方差的正态分布序列。 | 基于指数变量服从自由度为2的卡方分布这一统计特性。 |
| 协方差函数 `C(h)` 可以从估计的变异函数 `γ(h)` 通过 `C(h) = σ² - γ(h)` 直接获得。 | [Miller 1985, pp. 2-5] | 引用自 Journel, 1974。 | 这是连接地质统计学与谱模拟的关键步骤。 |

## Limitations
未从索引片段中确认。

## Assumptions / Conditions
*   裂隙组属性是**空间相关**的，可以通过自相关或变异函数来描述 [Miller 1985, pp. 1-2]。
*   用于模拟的协方差函数是**真实且对称**的，导致其对应的谱密度也是实对称的 [Miller 1985, pp. 2-5]。
*   数据被假设为**平稳**的，因为空间相关的平稳数据集在傅里叶变换后会生成非相关的傅里叶系数 [Miller 1985, pp. 2-5]。
*   模拟的参照系是裂隙组的**平均矢量** [Miller 1985, pp. 1-2]。
*   对于指数分布的模拟，假设指数随机变量服从自由度为2的卡方分布 [Miller 1985, pp. 5-10]。

## Key Variables / Parameters
*   `Z(x_i)`：在位置 `x_i` 的样本值 [Miller 1985, pp. 2-5]。
*   `h`：滞后距（lag distance），可为实际距离或裂隙数量 [Miller 1985, pp. 2-5]。
*   `γ(h)`：估计的变异函数值 [Miller 1985, pp. 2-5]。
*   `C(h)` / `C n`：估计的协方差函数值及其数字化形式 [Miller 1985, pp. 2-5]。
*   `S m`：谱密度的离散值 [Miller 1985, pp. 2-5]。
*   `σ²` / `o²`：数据的估计方差 [Miller 1985, pp. 2-5]。
*   `μ_U`：指数分布数据的均值 [Miller 1985, pp. 10-11]。
*   `X_i`, `Y_i`：用于构造指数分布数据的独立正态分布变量 [Miller 1985, pp. 5-10]。
*   `Af`：谱密度频率的离散间隔，`Af = 1/(NAh)` [Miller 1985, pp. 2-5]。

## Reusable Claims
1.  **协方差函数获取**：裂隙组属性的空间协方差函数可以直接通过该属性的实验变异函数（`γ(h)`）和总体方差（`σ²`），使用关系式 `C(h) = σ² - γ(h)` 获得。这要求数据已用于计算变异函数。[Miller 1985, pp. 2-5]
2.  **谱模拟核心**：对于平稳、空间相关的数据，其傅里叶变换会产生非相关的傅里叶系数。通过赋予这些系数与谱密度（协方差函数的傅里叶变换）一致的方差，再进行逆傅里叶变换，即可生成保留原始空间结构的模拟数据。[Miller 1985, pp. 2-5]
3.  **指数分布数据模拟方法**：要模拟具有特定协方差函数 `C_U(h)` 和均值 `μ_U` 的指数分布变量 `U`，可以先生成两个独立的、均值为0的正态分布序列 `X` 和 `Y`，其协方差函数需满足 `C(h) = [C_U(h) / 4]^{1/2}`，方差为 `μ_U / 2`。然后令 `U = X² + Y²` 即可。该方法的统计基础是：指数分布变量与自由度为2的卡方分布变量的关系。[Miller 1985, pp. 5-10]
4.  **计算效率**：利用快速傅里叶变换（FFT）的谱分析方法模拟空间相关裂隙属性，计算效率极高，在早期计算系统上即可在秒级时间内完成数百个数据点的模拟。[Miller 1985, pp. 10-11]

## Candidate Concepts
*   [[spatial correlation]]
*   [[fracture reservoir]]
*   [[spectral density]]
*   [[variogram]]
*   [[covariance function]]
*   [[autocorrelation]]
*   [[FFT (Fast Fourier Transform)]]

## Candidate Methods
*   [[FFT (Fast Fourier Transform)]]
*   [[spatial correlation analysis]]
*   [[variogram fitting]]
*   [[spectral simulation]]
*   [[exponential distribution simulation]]

## Connections To Other Work
*   论文引用了 Journel (1974) 关于变异函数和协方差函数关系 `C(h) = σ² - γ(h)` 的工作 [Miller 1985, pp. 2-5]。
*   论文引用了 Miller (1979, 1982) 关于将球形变异函数模型应用于裂隙数据的研究 [Miller 1985, pp. 2-5]。
*   论文引用了 Borgman (1973a) 关于实值数据协方差函数和谱密度对称性的研究 [Miller 1985, pp. 2-5]。
*   论文引用了 Taheri (1980) 关于平稳数据傅里叶变换产生非相关系数的概念 [Miller 1985, pp. 2-5]。
*   论文引用了 Mood, Graybill, and Boes (1974) 中关于卡方变量与正态变量关系的统计特性 [Miller 1985, pp. 5-10]。
*   论文引用了 Anderson (1958) 关于期望值推导的统计关系 [Miller 1985, pp. 5-10]。

## Open Questions
未从索引片段中确认。

## Source Coverage
本页内容基于提供的 **5** 个索引片段，总覆盖页数为 **12** 页。这些片段覆盖了论文的摘要、引言、方法的核心公式与推导、模拟示例（通过频率分布直方图简要展示）和结论。
*   **覆盖偏重**：片段对**方法**部分的覆盖最为详尽，详细记录了变异函数、协方差函数、谱密度的公式以及针对正态和指数分布数据的模拟流程。
*   **可能缺失的信息**：片段对实际**案例研究**的数据详情（如研究区位、数据量、具体地质背景）覆盖较少，仅展示了部分结果的图形（如倾角直方图）但缺少详细解释。此外，关于方法的**局限性**和**讨论**部分信息完全缺失。
