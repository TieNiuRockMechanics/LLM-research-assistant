---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties"
title: "Spectral-Type Simulation of Spatially Correlated Fracture Set Properties."
status: "draft"
source_pdf: "data/papers/1985 - Spectral-type simulation of spatially correlated fracture set properties.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Miller, Stanley M., and Leon E. Borgman. \"Spectral-Type Simulation of Spatially Correlated Fracture Set Properties.\" *Mathematical Geology*, vol. 17, no. 1, 1985, pp. 41-42."
indexed_texts: "5"
indexed_chars: "23086"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "22651"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.981157"
coverage_status: "full-index"
source_signature: "6e1f88d63431ac6cf71166f19203e0dedb4be665"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:57:24"
---

# Spectral-Type Simulation of Spatially Correlated Fracture Set Properties.

## One-line Summary
利用快速傅里叶变换的谱分析方法，能够高效地模拟具有空间相关性的裂隙组属性（如方位、间距、迹长和波状起伏），其协方差函数由变异函数导出，适用于正态分布和指数分布的数据。

## Research Question
如何高效地生成具有实测空间自相关结构的裂隙组属性人工数据，从而为岩体建模提供符合实际统计特征的输入？该研究聚焦于利用谱型模拟方法同时处理正态与指数分布的裂隙特征，并保持指定的方差和变异函数。

## Study Area / Data
- 研究未指定具体工区；数据来源为一般性野外裂隙测绘[Miller 1985, pp. 1-2]。
- 示例模拟采用 256 个裂隙数据点：正态分布模拟针对倾角（dip）和倾角方向（dip direction），指数分布模拟针对间距、迹长等属性[Miller 1985, pp. 3-5, 10-11]；Fig.1, Fig.2。
- 变异函数沿裂隙组平均矢量计算，滞后距离常以裂隙个数而非实际距离为单位[Miller 1985, pp. 1-2]。

## Methods
1. **变异函数估计**：从实测裂隙数据中，沿平均矢量计算变异函数 \(\gamma(h) = \frac{1}{2N} \sum_{i=1}^N [Z(x_i) - Z(x_i+h)]^2\)，其中 \(h\) 为滞后距（裂隙数或距离）[Miller 1985, pp. 1-2]。
2. **协方差函数导出**：在平稳假设下，由 \(C(h) = \sigma^2 - \gamma(h)\) 得到协方差函数[Miller 1985, pp. 2-3]。
3. **谱密度计算**：对协方差函数数字化后，通过离散傅里叶变换（FFT）计算谱密度 \(S_m = \Delta h \sum_{n=0}^{N-1} C_n e^{-i2\pi m n/N}\)[Miller 1985, pp. 2-3]。
4. **正态属性模拟**：  
   - 生成独立的标准正态随机数 \(Z\)、\(Z'\)（均值 0，方差 1）。  
   - 按谱密度分配傅里叶系数的方差：当 \(m=0\) 或 \(m=N/2\) 时，\(\text{Var}(U_m) = T S_m\)，\(\text{Var}(V_m)=0\)；否则 \(\text{Var}(U_m) = \text{Var}(V_m) = T S_m/2\)（其中 \(T=N\Delta h\)）。  
   - 构造系数 \(U_m = Z [\text{Var}(U_m)]^{1/2}\)，\(V_m = Z' [\text{Var}(V_m)]^{1/2}\)，并利用共轭对称性补全其余系数。  
   - 逆 FFT 得到零均值序列，最后加上原始均值[Miller 1985, pp. 3-5]。
5. **指数属性模拟**：  
   - 利用指数分布与卡方分布（自由度 2）的关系：若 \(U\) 为指数变量，则 \(U = X^2 + Y^2\)，其中 \(X, Y\) 为相互独立的零均值正态变量，方差 \(\sigma^2 = \mu_U/2\)（\(\mu_U\) 为指数分布均值）。  
   - 指数协方差与正态协方差的关系为 \(C_U(h) = 4 C^2(h)\)，故用于正态模拟的协方差 \(C(h) = [C_U(h)/4]^{1/2}\)。  
   - 分别模拟两组具有该 \(C(h)\) 与 \(\sigma^2\) 的正态序列，再逐点求平方和即得指数序列[Miller 1985, pp. 5-10, 10-11]。
6. **块金效应处理**：可采用两种方式——在协方差函数零滞后附近构造急剧上升，或频域内添加白噪声常数[Miller 1985, pp. 11]。

## Key Findings
- 谱模拟方法在 DECsystem‑20 上处理 256 个数据点仅需 0.60 秒（正态）和 0.82 秒（指数），计算效率极高[Miller 1985, pp. 10-11]。
- 生成的模拟数据在均值、方差及变异函数形态上均与实测数据吻合良好（参见 Fig. 1 和 Fig. 2）[Miller 1985, pp. 3-5, 10-11]。
- 无论是正态分布的产状要素，还是指数分布的间距、迹长等，本方法均能有效重现其空间自相关结构[Miller 1985, pp. 3-5, 10-11]。
- 该方法未纳入不同属性间的交叉相关性，但已有后续工作表明可通过扩展的频域模拟处理互相关[Miller 1985, pp. 10-11]。
- 需注意数字化间隔的选择以避免频率混叠，同时傅里叶变换隐含的周期性假设在实际应用中应被正确认识[Miller 1985, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 裂隙组属性（产状、间距、迹长、波状起伏）常具有空间相关性 | [Miller 1985, pp. 1-2] | 基于野外测绘数据 | 可用变异函数描述 |
| 变异函数计算公式：\(\gamma(h) = \frac{1}{2N} \sum [Z(x_i)-Z(x_i+h)]^2\) | [Miller 1985, pp. 1-2] | 沿裂隙组平均矢量，\(h\) 为滞后距（裂隙数） | 用于估计空间相依性 |
| 协方差与变异函数关系：\(C(h) = \sigma^2 - \gamma(h)\) | [Miller 1985, pp. 2-3] | 协方差平稳过程 | 引自 Journel (1974) |
| 谱密度是协方差函数的离散傅里叶变换，对实数数据为实偶函数 | [Miller 1985, pp. 2-3] | 协方差数字化且对称 | 由 FFT 快速计算 |
| 正态属性模拟：生成独立标准正态数，按谱密度分配傅里叶系数方差后逆 FFT，再加均值 | [Miller 1985, pp. 3-5] | 实值平稳数据，系数方差见式(5)-(8) | 零均值序列+原始均值 |
| 指数属性与卡方分布关系：\(U = X^2 + Y^2\)，指数协方差 \(C_U(h)=4 C^2(h)\) | [Miller 1985, pp. 5-10, 10-11] | \(X,Y\) 服从 \(N(0,\sigma^2)\)，\(\sigma^2=\mu_U/2\) | \(C(h)=\sqrt{C_U(h)/4}\) |
| 256 点模拟耗时：正态 0.60 s，指数 0.82 s（DECsystem‑20） | [Miller 1985, pp. 10-11] | 两种分布模拟对比 | 效率优势明显 |
| 块金效应可通过协方差原点附近陡升或频域加白噪声引入 | [Miller 1985, pp. 11] | 实际变异函数常有块金 | 两种替代方案 |
| 方法未考虑不同属性间的互相关性，但可扩展 | [Miller 1985, pp. 10-11] | 各属性单独模拟 | 后续研究已初步解决 |

## Limitations
- 未模拟裂隙组不同属性（如产状与间距）之间的互相关，仅能分别独立生成[Miller 1985, pp. 10-11]。
- 傅里叶变换将数据视为周期函数，在边界的重复性假设可能与实际不符，需谨慎解释[Miller 1985, pp. 10-11]。
- 若协方差函数数字化间隔选择不当，可能导致频率混叠，影响谱密度估计精度[Miller 1985, pp. 10-11]。
- 块金效应的模拟方法较为近似，尤其是高频特性的捕捉可能存在偏差[Miller 1985, pp. 11]。
- 模拟效果依赖于变异函数模型的合理性及协方差平稳假设的成立[Miller 1985, pp. 1-2]。

## Assumptions / Conditions
- 裂隙组内随机过程为**协方差平稳**：协方差仅依赖于滞后距，且均值和方差恒定[Miller 1985, pp. 1-2]。
- 滞后距常以**裂隙个数**度量，而非实际距离[Miller 1985, pp. 1-2]。
- 裂隙数据为**实数**，其协方差函数关于零滞后对称，谱密度相应地实偶对称[Miller 1985, pp. 2-3]。
- 裂隙属性服从**正态分布**（如倾角、倾角方向）或**指数分布**（如间距、迹长、波状起伏），且指数分布可利用卡方分布关系转换为正态平方和[Miller 1985, pp. 1-2, 5-10]。
- 协方差函数的数字化需满足**采样定理**以避免混叠，并选择足够的周期 \(T= N \Delta h\)[Miller 1985, pp. 10-11]。
- 模拟中使用的傅里叶系数在频域被视为**非平稳但互不相关**[Miller 1985, pp. 2-3]。

## Key Variables / Parameters
- \(h\)：滞后距（裂隙数或实际距离）
- \(\gamma(h)\)：变异函数值
- \(C(h)\)：协方差函数值
- \(\sigma^2\)：总体方差
- \(S_m\)：离散谱密度
- \(A_m = U_m - i V_m\)：傅里叶系数
- \(N\)：数据点数
- \(\Delta h\)：协方差数字化间隔
- \(T = N \Delta h\)：周期
- \(Z, Z'\)：标准正态随机数
- \(\mu_U\)：指数分布均值
- \(C_U(h)\)：指数变量协方差
- 块金效应处理中频域白噪声常数

## Reusable Claims
- 裂隙组方位、间距、迹长和波状起伏等几何属性普遍存在空间自相关，可用变异函数量化[Miller 1985, pp. 1-2]。
- 基于快速傅里叶变换的谱模拟方法，能够利用协方差函数高效生成具有指定空间相关结构的人工裂隙数据，计算耗时短[Miller 1985, pp. 1-2, 10-11]。
- 对于正态分布属性，模拟核心是生成互不相关的傅里叶系数，其方差由谱密度赋值，再经逆 FFT 得到空间相关序列[Miller 1985, pp. 3-5]。
- 指数分布属性（如间距、迹长）可通过模拟两组独立正态序列后求平方和来实现，所需正态协方差为指数协方差的平方根除以 2[Miller 1985, pp. 5-10]。
- 变异函数与协方差函数的关系 \(C(h) = \sigma^2 - \gamma(h)\) 提供了从实测变异函数获取模拟所需协方差函数的直接途径[Miller 1985, pp. 2-3]。
- 块金效应可通过在协方差函数零滞后处构造陡升，或在频域添加白噪声成分加以近似[Miller 1985, pp. 11]。
- 当前方法假定各裂隙属性独立，不能直接联合模拟跨属性的互相关结构，但概念上可扩展至多变量频域模拟[Miller 1985, pp. 10-11]。

## Candidate Concepts
- [[spatial correlation]]
- [[variogram]]
- [[covariance function]]
- [[spectral density]]
- [[fast Fourier transform]]
- [[Fourier coefficients]]
- [[normal distribution]]
- [[exponential distribution]]
- [[chi-squared distribution]]
- [[nugget effect]]
- [[aliasing]]
- [[stationary process]]
- [[frequency-domain simulation]]
- [[fracture set]]
- [[fracture orientation]]
- [[fracture spacing]]
- [[trace length]]
- [[fracture waviness]]

## Candidate Methods
- [[spectral-type simulation]]
- [[FFT-based simulation]]
- [[Monte Carlo simulation]]
- [[variogram estimation]]
- [[covariance stationary process modeling]]
- [[nugget effect handling]]
- [[exponentially distributed property simulation]]
- [[frequency-domain white noise addition]]

## Connections To Other Work
- 变异函数‑协方差关系引自 Journel (1974) 的地质统计学成果[Miller 1985, pp. 2-3]。
- 裂隙几何统计分布的研究参考了 Robertson (1970), Call et al. (1976), Cruden (1977), Baecher (1983) 等，表明产状常似正态，间距、迹长等常似指数或对数正态[Miller 1985, pp. 1-2]。
- 传统的 Monte Carlo 模拟因忽略空间相关性而不足以生成真实裂隙网络（Call & Nicholas, 1978），本文方法弥补了这一缺陷[Miller 1985, pp. 1-2]。
- 频域模拟的理论基础来自 Borgman (1973a, 1973b) 的谱分析著作，以及 Taheri (1980) 的多维模拟工作[Miller 1985, pp. 3-5, 11-12]。
- 作者先前在裂隙空间依赖性分析（Miller, 1979, 1982）中已应用地球统计学和谱方法，本文是对其的深化与扩展[Miller 1985, pp. 2-3, 11-12]。

## Open Questions
- 如何将谱模拟方法从单一属性扩展至多属性，以同时保持实测的**互相关结构**（已在后续研究中被提及，但本文未详述）[Miller 1985, pp. 10-11]。
- 对于非平稳或具有趋势的裂隙数据，**方差稳定性假设**不再成立时的模拟策略尚需探讨[Miller 1985, pp. 1-2]。
- 块金效应的最优模拟方式，特别是如何精确重构变异函数原点附近的**高频成分**，仍需进一步验证[Miller 1985, pp. 11]。
- 不同裂隙组间以及同一组内不同**尺度**下的空间相关性是否服从相似的谱结构，尚未有系统对比[Miller 1985, pp. 1-2]。
- 利用本方法模拟的裂隙网络在**岩体力学行为预测**中的有效性需通过更多工程实例来评估（未在本文中论证）。

## Source Coverage
本页面已处理全部 5 个非空索引片段，共覆盖有效原文字符约 22,651 个。按片段块计，覆盖率为 100%（5/5）；按字符计，覆盖率为 98.12%（22,651/23,086）。所有片段均已编入，未遗漏任何实质性内容。未使用的字符主要为拼接边界的少量格式损失，不影响信息完整性。
