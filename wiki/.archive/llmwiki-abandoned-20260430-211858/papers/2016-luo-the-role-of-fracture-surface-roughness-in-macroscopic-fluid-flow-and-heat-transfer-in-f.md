---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-luo-the-role-of-fracture-surface-roughness-in-macroscopic-fluid-flow-and-heat-transfer-in-f"
title: "The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2016 - The role of fracture surface roughness in macroscopic fluid flow and heat transfer in fractured rocks.pdf"
collections:
  - "zotero new"
  - "雷恩学派分形研究"
citation: "Luo, Shuang, et al. \"The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 87, 2016, pp. 29-38, doi:10.1016/j.ijrmms.2016.05.006."
indexed_texts: "8"
indexed_chars: "38845"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:12:14"
---

# The Role of Fracture Surface Roughness in Macroscopic Fluid Flow and Heat Transfer in Fractured Rocks.

## One-line Summary
利用离散裂隙网络模型系统评估裂隙面粗糙度（以节理粗糙度系数JRC为指标）的统计分布和力学-水力孔径转换模型对宏观渗流与对流传热过程的控制作用 [Luo 2016, pp. 1-2, 10]。

## Research Question
裂隙面粗糙度在单裂隙尺度已被证实影响水-力-热行为，但在复杂裂隙网络的宏观尺度，局部表面粗糙度的变化如何影响流体流动和热传导过程，并且这种影响在多大程度上取决于所采用的力学-水力孔径经验模型 [Luo 2016, pp. 1-2]。

## Study Area / Data
- **JRC现场数据**：
  - 瑞典Oskarshamn和Forsmark地区175个岩石裂隙样本的直剪试验反算JRC值 [Luo 2016, pp. 2-3]。
  - 伊朗Bakhtiary坝址106个岩石裂隙/层理面样本及3个原位直剪试验，基于分形维数估算JRC值 [Luo 2016, pp. 2-3]。
- **DFN几何参数**：基于英国Cumbria地区Sella场地的野外填图统计参数构建边长5 m的二维离散裂隙网络模型，该尺寸已超过代表性体积单元大小 [Luo 2016, pp. 4-5]。

## Methods
- **JRC分布拟合**：根据上述两个数据库，分别拟合出正态分布和对数正态分布，作为后续模型的粗糙度输入 [Luo 2016, pp. 3-4]。
- **力学-水力孔径关系**：采用两组经验模型将力学孔径E转换为水力孔径e：
  - Barton等（1985）模型：通常预测较小的e/E比值，且e/E依赖于E [Luo 2016, pp. 4-5, 9-10]。
  - Li & Jiang（2013）模型：预测较大的e/E比值，且e/E与E无关 [Luo 2016, pp. 4-5, 9]。
- **DFN数值模拟**：
  - 基于Sella场地几何参数，所有裂隙赋予固定力学孔径（6.5、65、650 mm），但通过不同JRC分布和e/E模型生成不同的水力孔径分布 [Luo 2016, pp. 5]。
  - 使用有限元法求解裂隙中Darcy流动和热传导方程，温度场在基质中采用热传导，裂隙中考虑对流换热，通过COMSOL的多物理场耦合和LU分解直接求解 [Luo 2016, pp. 4-5]。
  - 边界条件：右侧恒压注入50°C冷水，初始岩体温度200°C，上下边界绝热 [Luo 2016, pp. 5-6]。
- **计算案例**：91个实现，包括不同JRC分布（正态、对数正态）与e/E模型的组合，且每个组合生成多个随机实现以评估变异性 [Luo 2016, pp. 1, 6-9]。

## Key Findings
1. **JRC分布的影响**：在现场数据拟合中，Oskarshamn/Forsmark与Bakhtiary的JRC分别可用正态和对数正态分布描述，但不存在统一的概率分布 [Luo 2016, pp. 3-4]。在DFN模拟中，正态分布JRC的裂隙网络总渗透率低于对数正态分布的情形，热前缘移动相应更慢 [Luo 2016, pp. 9-10]。
2. **e/E模型的决定性作用**：
   - 若采用**Barton模型**，粗糙度对流动和传热影响显著。以机械孔径65 mm为例，考虑粗糙度后总流量较不考虑粗糙度的情形（Case 4）大幅下降：Case 1（正态分布JRC，Barton模型）降低93.8%，Case 2（对数正态分布JRC，Barton模型）降低71.7%，Case 3（另一种JRC分布组合，Barton模型）降低90.7% [Luo 2016, pp. 6]。
   - 若采用**Li & Jiang模型**，e/E比值较大且与机械孔径无关，粗糙度引起的流量变化很小，在首次近似中可忽略 [Luo 2016, pp. 6-9]。
3. **宏观响应变异性**：当使用Barton模型时，不同随机实现之间的流体流动和热突破曲线差异显著，需要多个实现才能表征行为；而使用Li & Jiang模型时，单个实现即足以预测宏观行为 [Luo 2016, pp. 9-10]。
4. **热突破特征**：Barton模型对应的DFN由于总流量小，出口温度突破曲线更为平缓且拖尾效应显著，热前缘推进速度明显慢于采用Li & Jiang模型的情形 [Luo 2016, pp. 6-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 使用Barton模型时，Case 1总流量比不考虑粗糙度的Case 4减少93.8%，Case 2减少71.7%，Case 3减少90.7% | [Luo 2016, pp. 6] | DFN模型边长5 m，机械孔径统一为65 mm，JRC分布为Case1正态/others，各案例结果为五个实现的平均值 | 流量通过归一化比较（基准值4.76×10⁻⁵ m²/s） |
| Li & Jiang模型下总流量变化极小，且与机械孔径大小无关 | [Luo 2016, pp. 6-9] | 对比机械孔径6.5、65、650 mm三种情况，模型参数独立于E | 对应图8和图9，文中说明Li & Jiang模型e/E比值接近常数 |
| DFN正态JRC分布比对数正态分布渗透率更低，热前缘更慢 | [Luo 2016, pp. 9-10] | 基于现场JRC数据的拟合参数，两种e/E模型下均观察到该趋势 | 文中作为主要结论之一 |
| 使用Barton模型时，不同随机实现的温度分布和热突破曲线差异大；Li & Jiang模型下多个实现几乎一致 | [Luo 2016, pp. 9-10] | 比较Case 1的五个随机实现，出口温度及温度场分布图像 | 作为结论3，说明实现数的要求 |
| 瑞典Oskarshamn/Forsmark的JRC数据可用正态分布描述，伊朗Bakhtiary的数据可用对数正态分布描述 | [Luo 2016, pp. 3-4] | 基于175个和106个样本的统计分析 | 但无统一通用分布 |

## Limitations
- 研究基于二维DFN模拟，已有研究指出二维分析不能近似估计三维等效渗透率 [Luo 2016, pp. 10]。因此，当前结论是否可推广至三维需系统验证 [Luo 2016, pp. 10]。
- 未考虑实际工程中裂隙粗糙度可能因力学过程变化，以及裂隙充填物（gouge material）的影响 [Luo 2016, pp. 10]。
- 所采用的多数力学-水力孔径经验模型未考虑高雷诺数下流体惯性效应，也未充分考虑裂隙匹配状态 [Luo 2016, pp. 4]。
- 模型中将所有裂隙的力学孔径设为同一常数，而实际裂隙网络中力学孔径可能变化，非完全由JRC控制 [Luo 2016, pp. 5]。
- 热边界条件为简化设定（恒定注入温度、绝热上下边界），忽略了三维热扩散和真实储层温度梯度 [Luo 2016, pp. 5-6]。

## Assumptions / Conditions
- DFN几何结构基于Sella场地的统计参数，该区域的特征不代表所有裂隙岩体 [Luo 2016, pp. 5]。
- 力学孔径统一赋值为6.5、65或650 mm，初始假设为常数 [Luo 2016, pp. 5]。
- 采用JRC正态和对数正态分布这两个统计模型，系基于两个特定场地的数据拟合，作为一般性研究假设 [Luo 2016, pp. 3-4]。
- 流体流动遵循Darcy定律，宏观热传输采用对流-传导耦合方程，忽略强惯性效应 [Luo 2016, pp. 4]。
- 岩体初始温度200°C，注入水50°C，所有模拟均为稳态流动与瞬态热传导的结合 [Luo 2016, pp. 5-6]。
- 模型仅考虑单一裂隙网络中流动，基质渗透率极低（孔隙度0.01），忽略基质渗流 [Luo 2016, pp. 5-6]。
- 力学-水力孔径模型均基于特定试验数据拟合，使用时直接外推至模拟条件 [Luo 2016, pp. 4]。

## Key Variables / Parameters
- **JRC**（节理粗糙度系数）：描述裂隙表面粗糙度的主要指标，服从正态或对数正态统计分布。
- **力学孔径 E**：假设为常数值（6.5, 65, 650 mm），是水力孔径计算的基础。
- **水力孔径 e**：由E和JRC通过经验模型计算得到，控制裂隙导流能力。
- **e/E 比值**：核心转换参数，Barton模型中取决于E和JRC，Li & Jiang模型中约等于常数。
- **总出口流量**：用于量化宏观渗透性的指标，归一化以比较各案例。
- **温度突破曲线与热前缘速度**：评价宏观热传输效率，受流量分布和通道化控制。
- **JRC分布类型**（正态 vs. 对数正态）：控制不同裂隙的粗糙度分配。
- **e/E经验模型选择**：Barton模型或Li & Jiang模型，为决定性因素。
- **机械孔径大小**：在Barton模型中影响e/E值，从而改变粗糙度的作用程度 [Luo 2016, pp. 6]。
- **随机实现数目**：在粗糙度强影响下（Barton模型）需多个实现以反映变异性 [Luo 2016, pp. 9-10]。

## Reusable Claims
1. 在DFN模型中，若采用Barton（1985）的力学-水力孔径关系，裂隙面粗糙度可导致总流量降低超过70%~93%，且流量对JRC分布和机械孔径大小敏感。**适用条件**：二维DFN，机械孔径恒定，JRC服从正态或对数正态分布，忽略充填物和力学变化。**限制**：Barton模型在低JRC时可能给出e/E>1的非物理值 [Luo 2016, pp. 4-6]。
2. 当使用Li & Jiang（2013）模型时，由于e/E比值接近常数且与机械孔径无关，裂隙面粗糙度对宏观流动和热传输的影响微弱，可在一阶近似中忽略。**适用条件**：二维DFN，e/E模化独立于E。**限制**：该模型可能低估粗糙度在特定条件下的作用，且在极端流态下未验证 [Luo 2016, pp. 6, 9-10]。
3. JRC的现场统计分布无统一形式，不同场址可能需要采用不同分布（如正态或对数正态），因而在进行区域尺度评估时必须采用场地特定数据。**证据**：瑞典与伊朗的数据呈现明显不同分布 [Luo 2016, pp. 3-4]。
4. 宏观热突破曲线的形状与流量通道化程度强相关：总流量越低、流动越集中在少数通道中，突破曲线越平缓，拖尾越长。**举证**：Barton模型下长尾效应显著，Li & Jiang模型则突破陡峭 [Luo 2016, pp. 6-9]。
5. 模拟结果的变异性受e/E模型选择控制：在粗糙度起主导作用时（如Barton模型），单个实现不足以代表整体行为，需要多个随机实现才能合理评估宏观流量和传热。**依据**：Case 1的五次实现流量和温度场均不相同 [Luo 2016, pp. 9-10]。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[joint roughness coefficient (JRC)]]
- [[hydraulic aperture]]
- [[mechanical aperture]]
- [[fracture surface roughness]]
- [[macroscopic fluid flow in fractured rocks]]
- [[convective heat transfer in fractured rocks]]
- [[channeling flow in fractures]]
- [[representative elementary volume (REV)]]
- [[temperature breakthrough curve]]
- [[thermal front propagation]]
- [[stochastic fracture network modeling]]

## Candidate Methods
- [[JRC estimation from direct shear tests]]
- [[JRC estimation from fractal dimension]]
- [[empirical models linking mechanical and hydraulic apertures]] (e.g., Barton, Li & Jiang)
- [[finite element method for coupled flow and heat transfer]]
- [[COMSOL Multiphysics for DFN simulation]]
- [[LU decomposition parallel sparse direct solver]]
- [[Darcy’s law for fracture flow simulation]]
- [[weak form contribution for heat exchange in fractures]]

## Connections To Other Work
- 文中引用的力学-水力孔径模型列表包含 Barton (1985), Zimmerman & Bodvarsson (1996), Rasouli & Hosseinian (2011), Li & Jiang (2013) 等，对比显示了不同模型预测的巨大差异 [Luo 2016, pp. 4]。
- 关于裂隙面粗糙度与水力特性关系的基础研究可追溯至 Patir & Cheng (1978) 的平均流动模型以及 Tsang & Witherspoon (1983) 对力学与水力特性的关联 [Luo 2016, pp. 10]。
- DFN模型的几何参数取自 Zhao et al. (2011) 关于应力对溶质运移影响的模拟工作，代表性体积单元相关论证参考 Min et al. (2004) [Luo 2016, pp. 5, 10]。
- 限制与扩展：Lang et al. 提出二维结果不能近似三维等效渗透率，提示本文结论需三维验证 [Luo 2016, pp. 10]；Guo et al. 指出实际工况中粗糙度会随力学过程变化，且可能存在岩屑充填 [Luo 2016, pp. 10]。
- 与热储开采相关研究可连接到 Shaik et al. (2011) 关于流体-岩石耦合传热的数值模拟 [Luo 2016, pp. 10]。

## Open Questions
- 在三维DFN中，粗糙度与各向异性流动和传热的耦合效应是否与二维结果一致？（文中明确指出需系统验证）[Luo 2016, pp. 10]。
- 当裂隙力学孔径并非恒定，且受应力-变形反馈控制时，粗糙度作用的定量评估如何变化？（文中未考虑力学过程）[Luo 2016, pp. 10]。
- 高流速下惯性效应（非达西流）与粗糙度的相互作用，在当前所用e/E模型中未体现，其对宏观传热可能产生的修正程度如何？
- 不同岩性、不同成因的裂隙粗糙度分布能否找到更具普适性的统计模型，而不限于两个特定场地的拟合？
- 裂隙充填物对水力孔径-热量传输的进一步削弱或改变尚未涉及。

## Source Coverage
本页综合来自论文的8个索引片段，覆盖摘要（引言背景与目的）、数据与方法（JRC数据库、e/E模型、DFM设置）、结果与分析（流量减少、温度突破）以及主要结论和部分参考文献。覆盖范围涉及论文大部分核心内容，但缺少完整的参数敏感性分析、部分详细公式以及扩展讨论的完整性。关键信息的缺失包括：并非所有91个实现的统计分布参数细节、裂隙网络确切的几何参数（如密度、长度分布）、JRC拟合的具体参数值（均值和方差），以及三维验证方向的具体建议。这些需查阅全文获得。
