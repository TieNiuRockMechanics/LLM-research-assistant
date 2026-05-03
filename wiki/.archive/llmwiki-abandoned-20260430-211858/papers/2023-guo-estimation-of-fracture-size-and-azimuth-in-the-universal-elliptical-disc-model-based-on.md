---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-guo-estimation-of-fracture-size-and-azimuth-in-the-universal-elliptical-disc-model-based-on"
title: "Estimation of fracture size and azimuth in the universal elliptical disc model based on trace information."
status: "draft"
source_pdf: "data/papers/2023 - Estimation of fracture size and azimuth in the universal elliptical disc model based on trace information.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Guo, Jichao, et al. \"Estimation of fracture size and azimuth in the universal elliptical disc model based on trace information.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 15, 2023, pp. 1391-1405. doi:10.1016/j.jrmge.2022.07.018. Accessed 2026."
indexed_texts: "15"
indexed_chars: "73175"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:17:09"
---

# Estimation of fracture size and azimuth in the universal elliptical disc model based on trace information.

## One-line Summary
本文基于取样窗迹线信息，建立了普遍椭圆盘（UED）模型中裂隙尺寸和方位角参数的估计方法，推导了迹长均值与标准差的公式并通过蒙特卡洛模拟验证，提出了一种需要至少三个取样窗口的优化参数估计程序，并用假设案例证实了方法的可行性 [Guo 2023, pp. 1-1, 7-10]。

## Research Question
如何从露头或钻孔取样窗的迹线信息出发，可靠地逆推出普遍椭圆盘模型中的三个尺寸与方位相关参数——长轴长度、短‑长轴比和旋转角，从而为离散裂隙网络（DFN）建模提供输入 [Guo 2023, pp. 1-1, 1-2, 7-8]？

## Study Area / Data
本文未使用真实岩体数据。研究采用假设的案例和三维椭圆形离散裂隙网络进行方法验证，取样窗的迹长信息通过蒙特卡洛模拟生成，并以模拟结果作为“真值”来检验计算值与估计值的吻合程度 [Guo 2023, pp. 7-8, 9-10]。具体涉及的取样窗有三个不同产状的无限平面，其方位列于原文表3，但未在本索引片段中提供 [Guo 2023, pp. 7-8]。

## Methods
1. **迹长分布的理论推导**：基于普遍椭圆盘模型的几何关系及裂隙中心随机均匀分布的假定，建立迹长与裂隙几何参数（长轴长度a、短长轴比k、迹线与长轴夹角u、裂隙面与取样窗的二面角ε等）之间的立体学关系，导出迹长均值μl与方差σl²的公式，该公式涉及a的分布矩、k的期望及与u、方位分布相关的积分量l、s、h等 [Guo 2023, pp. 4-7]。
2. **公式验证**：利用蒙特卡洛模拟生成的裂隙网络和30个无限取样窗的迹线信息，将迹长均值和标准差的公式计算值与模拟“真值”比较，定义误差率ER [Guo 2023, pp. 7-8]。
3. **参数估计方法**：为从迹长推断UED模型尺寸与方位参数，预设参数分布形式（如示例中长轴服从负指数分布、短长轴比服从正态分布、方位服从Fisher分布、旋转角服从von Mises分布），通过三个不同产状的取样窗获得ml1、sl1、ml2、sl2、ml3、sl3，利用比值关系消去共同未知参数后，结合蒙特卡洛积分构建优化算法，估计各分布参数 [Guo 2023, pp. 8-10]。

## Key Findings
1. 推导出的迹长均值与标准差公式在蒙特卡洛验证中误差率小于5%，证实了表达式的正确性 [Guo 2023, pp. 7-8]。
2. 基于三窗口迹长统计量和预设分布，所建立的优化方法在假设案例中给出了与预设真值吻合较好的参数估计结果 [Guo 2023, pp. 1-1, 9-10]。
3. 过往研究表明，UED模型的精度表征指数（ARI）比不考虑短长轴比和长轴方向变化的非UED模型高出约20 % [Guo 2023, pp. 1-2]，说明考虑全部变量的UED模型是值得在工程中采用的。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 迹长均值与标准差的公式（式36、37）在蒙特卡洛模拟中误差率小于5% | [Guo 2023, pp. 7-8] | 裂隙长轴长度、短长轴比、方位和旋转角均假定有特定分布；采用30个无限取样窗 | 验证了立体学推导的正确性 |
| 基于三个取样窗的迹长统计及分布假设，优化算法估计的尺寸与方位参数与预设真值吻合 | [Guo 2023, pp. 1-1, 9-10] | 长轴设为负指数分布，短长轴比设为正态分布，需要三个非平行取样窗 | 说明逆算方法可行 |
| UED模型的精度表征指数（ARI）较非UED模型提高约20% | [Guo 2023, pp. 1-2] （引用Zheng et al. 2022） | 适用于天然裂隙的几何表示 | 支持推广UED模型的使用 |

## Limitations
- 研究仅依赖预设的裂隙参数分布形式（如负指数、正态等），实际岩体中分布可能与假设不符。
- 参数估计过程需要至少三个不同产状的无限取样窗，而实际露头或钻孔条件往往有限，未从索引片段确认作者是否讨论了有限窗口或非平面窗口的影响。
- 验证基于数值生成的假设裂隙网络和理想取样窗，未与真实岩体裂隙数据对比 [Guo 2023, pp. 1-1, 7-10]。
- 文中假定迹线完全由平面椭圆盘与平面取样窗相交产生，未考虑裂隙的弯曲、粗糙度或终止效应。

## Assumptions / Conditions
- 裂隙可视为平面椭圆盘，其尺寸和方位完全由长轴长度a、短长轴比k、裂隙面产状（方位角α、倾角β）以及旋转角γ描述 [Guo 2023, pp. 1-2, 2-4]。
- 裂隙中心在三维空间内随机、均匀分布 [Guo 2023, pp. 4-5]。
- 取样窗为无限延伸的平面，迹线可被完全观测。
- 进行参数估计时需预先设定裂隙参数的分布函数类型：例如长轴长度可采用负指数、对数正态或伽马分布；短长轴比可采用均匀、正态或伽马分布；产状符合Fisher分布；旋转角采用von Mises分布 [Guo 2023, pp. 8-9]。
- 在示例推导中将长轴设为负指数分布、短长轴比设为正态分布 [Guo 2023, pp. 8-10]。

## Key Variables / Parameters
- **a**：椭圆裂隙长轴长度，其均值记为μa，标准差σa [Guo 2023, pp. 2-7]。
- **k**：短轴与长轴长度比（0 < k ≤ 1），其均值μk，标准差σk [Guo 2023, pp. 2-4, 8-9]。
- **u**：迹线与椭圆长轴之间的夹角 [Guo 2023, pp. 4-5]。
- **γ**：椭圆盘绕自身法线旋转的角度（旋转角），控制长轴方向 [Guo 2023, pp. 8-9]。
- **ε**：裂隙面与取样窗平面间的二面角 [Guo 2023, pp. 2-4]。
- **μα，μβ，κ1等**：Fisher分布中描述裂隙产状集中度的参数 [Guo 2023, pp. 8-9]。
- **l**：迹线长度，其均值μl，标准差σl [Guo 2023, pp. 5-7]。
- **l， s， h**：推导过程中出现的积分量，其中l和s无物理意义，h与二阶矩有关 [Guo 2023, pp. 5-7, 9-10]。
- **Pt**：由椭圆盘产生的迹线占总迹线数的比例 [Guo 2023, pp. 4-5]。

## Reusable Claims
- **Claim**：在UED模型中，当裂隙中心均匀随机分布且裂隙面与取样窗平面均为平面时，迹长均值μl和方差σl²可以通过式(34)和(35)（或进一步整理的式36、37）由长轴a的分布矩、k的期望以及积分项s和h表达。**条件**：已知裂隙参数（a, k, 产状, γ）的概率密度函数。**证据**：[Guo 2023, pp. 5-7]推导并给出完整表达式；**限制**：仅适用于无限取样窗且所有截交迹线均可观测的理想情况，真实情形中需考虑截断和删失。
- **Claim**：要由迹长统计量反演UED模型的尺寸与方位参数，至少需要三个不同产状的取样窗所获得的迹长均值和标准差，并需先验假定各参数的分布形式。**条件**：三个取样窗二面角ε彼此不同，以保证s和h有差异。**证据**：[Guo 2023, pp. 9-10]建立三个窗口下的μl和σl方程组，并通过比值关系消去共同未知参数；**限制**：当分布预设与真实岩体不符时，估计结果会偏离。
- **Claim**：在满足分布假定的条件下，长轴长度可用负指数分布，短长轴比可用正态分布来描述，此时参数估计可以通过蒙特卡洛积分数值求解s和h并结合三窗口迹长统计量实现。**条件**：裂隙产状用Fisher分布，旋转角用von Mises分布。**证据**：[Guo 2023, pp. 8-10]以该组合为例进行了参数估计验证；**限制**：文中仅以假设案例演示，通用性需进一步验证。
- **Claim**：当长轴长度服从负指数分布时，迹长均值的公式化为μl = π(μa²+σa²)·E(k) / (4 s μa)，其中s为与k、u和产状分布相关的积分。**证据**：[Guo 2023, pp. 8-10] 式(50)；**限制**：此简化形式仅在特定分布下成立。

## Candidate Concepts
- [[universal elliptical disc (UED) model]]
- [[non-universal elliptical disc (non-UED) model]]
- [[circular disc model]]
- [[discrete fracture network (DFN)]]
- [[fracture geometric parameter estimation]]
- [[stereology of fractures]]
- [[trace length distribution]]
- [[elliptical fracture]]
- [[azimuth-related parameters]]

## Candidate Methods
- [[stereological relationship derivation]]
- [[Monte Carlo simulation]]
- [[optimization algorithm for inverse problems]]
- [[truncation correction (von Mises distribution)]]
- [[Fisher distribution fitting]]
- [[multi-window trace sampling]]
- [[goodness-of-fit testing for fracture distributions]]

## Connections To Other Work
- **与UED模型提出的研究**：本文建立在Zheng et al. (2022) 提出的UED模型基础上，该模型将天然裂隙理想化为可变旋转角、长轴长度和短长轴比的椭圆盘，而非固定的非UED模型 [Guo 2023, pp. 1-2]。
- **与早期裂隙尺寸推断工作**：文中参考了Zhang et al. (2002) 基于迹长分布推断非UED模型长轴长度的方法，并沿用了预设分布求解的思路；此外引用了Jin et al. (2014) 等基于迹长分布与尺寸分布的映射方法 [Guo 2023, pp. 7-8]。
- **与圆形盘模型**：作为对比基准，圆形盘模型因数学简单而广泛使用（Warburton, 1980a; Priest, 2004），但其无法反映真实裂隙的椭圆特性 [Guo 2023, pp. 1-2]。
- 从主题上可连接到：[[fracture size inference from borehole data]]、[[elliptical disc model generalization]]、[[stereological kernel for DFN construction]] 等。

## Open Questions
- 对于有限尺寸的取样窗以及截断、删失迹线，本文提出的公式和估计方法如何扩展？
- 若裂隙并非严格平面椭圆盘（如存在粗糙度、分叉或填充），模型假设的鲁棒性如何？
- 如何在地表仅有一个或两个优势取样面，或钻孔采样条件下实现参数估计？未从索引片段中确认作者是否给出了相关讨论。
- 对于分布先验的选取，是否存在客观的数据驱动方法（如基于迹线长度直方图的拟合优度检验）以代替主观假设？

## Source Coverage
本知识页依据了15条索引片段，覆盖了论文的标题摘要、引言、方法推导、公式验证、参数估计方法及假设案例的描述。片段集中反映了文章的理论核心与验证部分（pp. 1‑10），但对结果讨论的详细数值、敏感性分析、三维裂隙网络的具体构造以及结论部分的讨论可能缺失。未从片段中确认作者是否提供了误差的置信区间、不同分布组合的性能比较或实际工程应用的建议。因而，本页侧重于可复现的公式、假设和理论框架，但对“实际应用效果”和“局限性深入讨论”等部分现阶段无法充分记录。
