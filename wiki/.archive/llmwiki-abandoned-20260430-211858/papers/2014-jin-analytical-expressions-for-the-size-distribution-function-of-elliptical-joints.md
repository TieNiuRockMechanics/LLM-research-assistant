---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2014-jin-analytical-expressions-for-the-size-distribution-function-of-elliptical-joints"
title: "Analytical Expressions for the Size Distribution Function of Elliptical Joints."
status: "draft"
source_pdf: "data/papers/2014 - Analytical expressions for the size distribution function of elliptical joints.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Jin, Wencheng, et al. \"Analytical Expressions for the Size Distribution Function of Elliptical Joints.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 70, 2014, pp. 201-211. DOI:10.1016/j.ijrmms.2014.04.017."
indexed_texts: "11"
indexed_chars: "53521"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:51:50"
---

# Analytical Expressions for the Size Distribution Function of Elliptical Joints.

## One-line Summary
本文推导了考虑节理方位耦合效应的椭圆节理尺寸分布（长轴概率密度函数）的解析表达式，假设节理为扁平椭圆盘，迹长分布可服从分形（幂律）、指数或多项式形式，并采用蒙特卡洛模拟验证了从迹长推断尺寸分布的方法。

## Research Question
如何从野外可测量的迹长分布精确推断岩体中三维椭圆节理的真实尺寸分布？传统方法假设节理相互平行，但实际节理具有空间方位。本文旨在建立耦合节理方位（倾角方向、倾角、旋转角）的体视学关系，并在不同迹长分布形式下获得尺寸分布的解析解，以解决“平行假设推导出的公式用于非平行节理现实”的悖论[Jin 2014, pp. 4]。

## Study Area / Data
本文未涉及特定野外研究区，主要通过数值模拟生成节理网络进行方法验证。模拟采用 RJNS3D 软件，生成两组椭圆节理，参数如表1所示，包括倾角方向／倾角、旋转角、轴比、密度以及长轴的均匀分布和正态分布两种情形[Jin 2014, pp. 7-9]。所有验证数据均来自模拟，无实际岩体露头数据。

## Methods
- **节理模型假设**：所有节理为扁平椭圆板，每个节理组具有相同的长轴与短轴之比 \(k\) 和固定的旋转角 \(\varphi\)；节理中心服从泊松分布，体积密度为 \(p_{30}\)；节理面的倾角方向 \(\theta\) 和倾角 \(\phi\) 服从二维概率密度函数 \(f(\theta,\phi)\) [Jin 2014, pp. 2-3]。
- **体视学关系推导**：基于 Zhang et al. [13] 的工作，重新定义角度，导出耦合节理和取样面方位的迹长三维概率函数（式15），进而得到适用于任意无限取样面的迹长概率密度函数 \(f(l)\) 与长轴概率密度函数 \(g(a)\) 的关系[Jin 2014, pp. 3-4]。
- **解析解推导**：针对三种迹长分布类型求解 \(g(a)\)：
  - **分形（幂律）分布**：互补累积分布函数为 \(G(l)=\eta_0^D l^{-D}\)，推导出 \(g(a)\) 的显式表达式（式24），其中含待定的最小长轴 \(\xi_0\)，通过数值积分确定[Jin 2014, pp. 4-6]。
  - **指数分布**：\(f(l)=Ae^{-Al}\)，利用分部积分和修正贝塞尔函数 \(BesselK\)，得到 \(g(a)\) 的解析式（式42），\(\xi_0\) 同样通过数值过程确定[Jin 2014, pp. 6-7]。
  - **多项式分布**：将迹长分布展开为多项式，通过递归关系求解积分，获得通用解（式52），并给出利用迭代确定 \(\xi_0\) 的步骤[Jin 2014, pp. 7]。
- **数值验证**：采用 Song and Lee [19] 的方法，基于 RJNS3D 生成的节理系统和取样窗口中的包含迹（contained traces），反估尺寸分布，与预设分布比较验证推导的正确性[Jin 2014, pp. 7-9]。

## Key Findings
1. 推导并证明：迹长分布 \(f(l)\) 与取样窗口和节理面的方位无关，这一结论被文献广泛使用，本文将其推广到非平行椭圆节理情形 [Jin 2014, pp. 4]。
2. 当节理方位被耦合进体视学关系时（式15），该关系可以退化为 Zhang et al. [13] 推导的平行椭圆节理迹长分布公式（式16），从而验证了整个推导过程的正确性 [Jin 2014, pp. 4]。
3. 对于迹长服从分形（幂律）分布的情况，长轴尺寸分布的解析解为 \( g(a) = \frac{ \sqrt{1/a^2 - 1/\xi^2} }{ \left( \frac{ \sqrt{\xi^2 - \xi_0^2} }{\xi} - \ln \frac{ \xi - \sqrt{\xi^2 - \xi_0^2} }{\xi_0} \right)^{-1} } \)，仅依赖于上界 \(\xi\) 和待定下界 \(\xi_0\) [Jin 2014, pp. 4-6]。
4. 对于指数型迹长分布，尺寸分布可表达为 \( g(a) = \frac{ A M \cdot BesselK[1, M A a] }{ BesselK[0, M A \xi_0] } \)，其中 \(BesselK\) 为第二类修正贝塞尔函数 [Jin 2014, pp. 6-7]。
5. 数值模拟结果（包含迹法）表明，所推导的解析关系能够较准确地反估椭圆节理的长轴尺寸分布，即使尺寸分布为均匀或正态形式，估计值与预设值吻合良好 [Jin 2014, pp. 7-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 迹长分布独立于取样窗口和节理面的方位的结论得到推广，本文推导中仍成立 | [Jin 2014, pp. 4] | 椭圆节理，耦合方位推导 | 由式15退化至式16的推导中自然显现 |
| 分形迹长分布下的尺寸分布解析解（式24），为PDF形式，需数值确定下界\(\xi_0\) | [Jin 2014, pp. 4-6] | 迹长互补累积分布为\(G(l)=\eta_0^D l^{-D}\)，\(\xi_0\)在\(\eta_0/M \sim \xi\)间迭代解出 | 示例中\(\xi_0=1.117\) |
| 指数迹长分布下的尺寸分布解析解（式42），含修正贝塞尔函数 | [Jin 2014, pp. 6-7] | 迹长PDF为\(f(l)=Ae^{-Al}\)，\(M>0, A>0\) | 需借助Mathematica积分，并由式(41)归一化确定\(\mu_a\) |
| 多项式迹长分布下的尺寸分布通用解（式52），可用递归关系(53)计算 | [Jin 2014, pp. 7] | 迹长PDF可展为多项式，需迭代确定\(\xi_0\)和\(\mu_a\) | 当k为奇/偶数时有不同终止条件 |
| 使用Song and Lee [19]的包含迹方法，通过RJNS3D模拟数据验证了尺寸分布估计的有效性 | [Jin 2014, pp. 7-9] | 取样窗口足够大以包含最大节理，迹线平行 | 模拟包含两组节理，分别假设均匀和正态长轴分布 |

## Limitations
- 所有推导基于节理为扁平椭圆盘的假设，实际节理形状可能更复杂；若节理非平面或非椭圆，关系式不再适用 [Jin 2014, pp. 2-3]。
- 迹长分布形式需预先假定（如分形、指数或多项式），对实际数据先需进行分布拟合，拟合不当将引入误差 [Jin 2014, pp. 4-7]。
- 解析解中含有的最小长轴 \(\xi_0\) 需要额外数值迭代确定，其准确性依赖初值和迹长数据下界的可靠性 [Jin 2014, pp. 7]。
- 模拟验证仅针对有限组参数和简单的尺寸分布（均匀、正态），未涵盖更复杂的现场情况；文中未给出与现场实测数据的直接对比 [Jin 2014, pp. 7-9]。
- 推导中假设节理中心服从均匀泊松分布，未考虑节理成簇或空间相关性 [Jin 2014, pp. 2-3]。

## Assumptions / Conditions
- 节理被简化为扁平椭圆盘，每个节理组内轴比 \(k\) 和旋转角 \(\varphi\) 恒定 [Jin 2014, pp. 2-3]。
- 节理中心在空间内呈均匀泊松分布，体积密度 \(p_{30}\) 为常数 [Jin 2014, pp. 2-3]。
- 节理面的倾角方向 \(\theta\) 和倾角 \(\phi\) 由二维概率密度函数 \(f(\theta,\phi)\) 描述，且与尺寸统计独立 [Jin 2014, pp. 2-3]。
- 取样面为无限大平面，用于建立尺寸与迹长的体视学关系；实际应用中，样品窗口被假定足够大以包含最大节理的迹长 [Jin 2014, pp. 7-9]。
- 迹长分布形式已知（分形、指数、多项式等），且在其定义域内连续可微 [Jin 2014, pp. 4-7]。
- 推导中认为距离 \(h\) 在0到 \(h_0\) 间均匀分布，该均匀性来自节理中心在空间的随机均匀假设 [Jin 2014, pp. 3-4]。

## Key Variables / Parameters
- \(a\) – 椭圆节理长轴（特征尺寸），其概率密度函数为 \(g(a)\) [Jin 2014, pp. 2-3]。
- \(l\) – 迹长，概率密度函数为 \(f(l)\)；取样下限 \(\eta_0\)，上限 \(\xi\) 或 \(B_2/M\) [Jin 2014, pp. 4-6]。
- \(k\) – 椭圆轴比（长轴/短轴）[Jin 2014, pp. 2-3]。
- \(\theta, \phi\) – 节理面倾角方向与倾角； \(\varphi\) – 旋转角（组内固定）[Jin 2014, pp. 2-3]。
- \(\alpha\) – 节理面与取样面的二面角 [Jin 2014, pp. 2-3]。
- \(M\) – 几何因子，与 \(\cos\alpha, k, \beta\) 相关，在最终关系中决定 l 与 a 的缩放 [Jin 2014, pp. 3-4]。
- \(\beta\) – 长轴与迹线垂线的特征角 [Jin 2014, pp. 2-3]。
- \(\mu_a\) – 长轴的平均值，用于归一化 [Jin 2014, pp. 4-6]。
- \(\xi_0\) – 最小长轴尺寸，由迭代数值确定 [Jin 2014, pp. 4-7]。
- \(D\) – 分形维数（幂律分布）[Jin 2014, pp. 4-6]。
- \(A\) – 指数分布速率参数 [Jin 2014, pp. 6-7]。
- \(p_{30}\) – 三维节理体积密度 [Jin 2014, pp. 2-3]。

## Reusable Claims
1. 对于长轴尺寸和方位均随机的椭圆节理，当取样面无限大时，迹长分布与取样面和节理面的方位无关，因此可用简化关系 \( f(l) = \frac{l}{M\mu_a} \int_{l/M}^{\infty} \frac{g(a)}{\sqrt{(Ma)^2 - l^2}} da \) 来联系尺寸与迹长 [Jin 2014, pp. 4]。  
   **条件**：节理为全空间内均匀泊松分布的椭圆盘，每个组内轴比和旋转角固定。**限制**：该独立性成立的前提是节理方位与尺寸统计独立；若存在相关，则耦合项不可忽略。

2. 当野外迹长数据可用互补累积分布 \(G(l) = \eta_0^D l^{-D}\) 良好拟合时，椭圆长轴的概率密度函数具有显式解析形式，仅含一个待定参数 \(\xi_0\)，并可利用归一化条件通过数值积分确定 [Jin 2014, pp. 4-6]。  
   **证据**：式(24)及算例中 \(\xi_0 = 1.117\)。**限制**：该解仅适用于迹长完全遵循单一分形律的情形；若迹长分布为其他形式，需采用相应的推导。

3. 利用包含迹（contained trace）的数量与尺寸密度之间的线性关系，可以通过计盒法在平行迹假设下反估椭圆节理的尺寸分布，Song and Lee [19] 的方法被证明对椭圆节理仍然有效 [Jin 2014, pp. 7-9]。  
   **条件**：取样窗口足够大以使得最大尺寸节理的迹成为包含迹；所有迹互相平行。**证据**：数值模拟中估计的尺寸分布与预设分布吻合。**限制**：若迹不平行或窗口截断严重，方法估计精度可能下降。

## Candidate Concepts
- [[elliptical joints]]  
- [[size distribution function]]  
- [[stereological relationship]]  
- [[trace length distribution]]  
- [[fractal distribution]]  
- [[contained trace]]  
- [[joint orientation]]  
- [[Poisson disk model]]  
- [[forward modeling]]  
- [[Crofton’s theorem]]

## Candidate Methods
- [[stereology-based size inference]]  
- [[analytical solution for joint size distribution]]  
- [[Song and Lee method]]  
- [[Monte Carlo simulation (RJNS3D)]]  
- [[iterative determination of minimum joint size]]  
- [[generating function approach for polynomial trace length]]

## Connections To Other Work
- 本文的体视学推导直接建立在 Zhang et al. [13] 的工作之上，其平行椭圆节理迹长关系式（本文式16）被作为退化形式重现 [Jin 2014, pp. 4]。  
- 前向建模（Forward modeling）的思想源于 Dershowitz et al. [6,7] 和 Paul et al. [8]，本文则采用反向推断路线 [Jin 2014, pp. 1-2]。  
- 迹长的分形分布被众多现场观察支持，文中引用了 Wong et al., Barton and Zoback, Hatton et al., Bour and Davy, La Pointe [32–36] 的工作 [Jin 2014, pp. 4-6]。  
- 在尺寸估计的实施上，采纳了 Song and Lee [19] 的包含迹方法 [Jin 2014, pp. 7-9]。  
- 奇异性问题与 Crofton’s theorem [17] 的应用在文献中被广泛讨论，本文通过直接解积分方程绕开了矩方法 [Jin 2014, pp. 4]。  
- 未从索引片段中确认与其他具体论文的直接方法对比关系，但可从主题上连接到 [[joint size inference from trace data]]、[[fracture network modeling]] 等领域。

## Open Questions
- 当节理轴比 \(k\) 并非全组恒定，或旋转角具有随机性时，本文解析框架如何扩展，未从索引片段中确认。  
- 对于非泊松分布的节理中心（例如成簇节理），现有的体视学关系是否仍然适用或可修正，文中未讨论。  
- 如何在实际有限窗口且存在严重截断的迹线数据下，稳定地确定迹长分布类型及下界 \(\xi_0\)，仍缺乏详细的方法指引。  
- 索引片段仅给出了针对均匀和正态长轴分布的模拟验证，对于其他重尾或混合分布的适用性尚待验证。

## Source Coverage
本页依据论文的 11 个索引片段撰写，覆盖了引言（问题提出与文献背景）、体视学关系推导（方法和关键步骤）、解析解导出（分形、指数、多项式三种情况）以及部分数值模拟验证（参数、方法、示意图）。**覆盖偏重**于理论推导和公式展开，对数值验证的统计指标、实际计算误差、程序实现细节等描述较少。**可能缺失的信息**包括：详细的模拟采样尺寸、估计误差分析、与现有其他推断方法（如前向建模）的定量对比结果、讨论与结论部分中对应用前景的阐述等。
