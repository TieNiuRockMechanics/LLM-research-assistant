---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-ma-heat-transfer-by-water-flowing-through-rough-fractures-and-distribution-of-local-heat-tr"
title: "Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction."
status: "draft"
source_pdf: "data/papers/2018 - Heat transfer by water flowing through rough fractures and distribution of local heat transfer coefficient along the flow direction.pdf"
collections:
citation: "Ma, Yueqiang, et al. \"Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction.\" *International Journal of Heat and Mass Transfer*, vol. 119, 2018, pp. 139-147. doi:10.1016/j.ijheatmasstransfer.2017.11.102."
indexed_texts: "8"
indexed_chars: "37344"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "37488"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003856"
coverage_status: "full-index"
source_signature: "62f43e0c945ea7efe200ba5e3f887e79fca473cd"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:37:38"
---

# Heat Transfer by Water Flowing through Rough Fractures and Distribution of Local Heat Transfer Coefficient along the Flow Direction.

## One-line Summary
采用3D打印技术制造不同粗糙度裂隙面的试件，结合实验与3DEC数值模拟，研究了水流经粗糙裂隙的换热特性，表明局部换热系数沿流向在入口处最大后趋于恒定，裂隙面粗糙度影响局部波动。

## Research Question
水流经粗糙裂隙的局部换热系数沿流动方向如何分布？裂隙面粗糙度（以节理粗糙度系数JRC表征）对总换热系数及局部换热系数的分布有何影响？

## Study Area / Data
本研究数据来自实验室模拟试验和数值模拟。实验采用3D打印技术制作的三种表面粗糙度不同的圆柱形混凝土试件（直径25 mm，长度100 mm），其节理粗糙度系数JRC分别为0–2、10–12和18–20（标准典型剖面）。实验在自主研发的干热岩实验室模拟系统上进行，外表面温度维持90 °C，体积流量设定为5、10、15和20 ml/min。数值模拟采用3DEC离散元程序建立与实验一致的模型。

## Methods
- **实验系统**：干热岩实验室模拟系统，包括ISCO泵供液、围压控制（1 MPa）、温度控制（电加热至90 °C）和热电偶采集进出口流体温度、岩石外壁温度等数据。试件采用3D打印技术制造，以精确控制裂隙面粗糙度。实验步骤包括放置试件、密封、围压加载、加热至稳定、以设定流量注水并记录稳态温度[Ma 2018, pp. 2-4]。
- **数值模拟**：使用3DEC建立水-试件-裂隙模型，裂隙内流体流动简化为层流，遵循简化Navier–Stokes方程；热传输包括流体对流、流体内部导热和岩石导热；流体与岩石间按牛顿冷却定律换热。网格数量约12485–12639，时间步长1.5 s，共15000步至稳态。边界条件和初始参数与实验一致[Ma 2018, pp. 4-6]。
- **数据处理**：
  - 局部换热系数 \( h_0 \) 通过离散化沿流向元素，由热平衡方程导出：  
    \[
    Q = c_p q_v \rho_w (t_2 - t_1) = h_0 A (T_w - T_r)
    \]
    结合换热面积计算得到公式 (9) [Ma 2018, pp. 6-7]。
  - 总换热系数采用Bai[6]的公式 (10)，基于进出口水温与外壁温度计算。
  - 雷诺数 \( Re = \frac{2 q_v}{d \nu} \)，普朗特数 \( Pr = \frac{\nu}{a} \)，努塞尔数 \( Nu = \frac{h l}{\lambda} \)，并拟合了 \( Nu = C Re^n Pr^m \) 形式的关联式 (15) [Ma 2018, pp. 6-7]。

## Key Findings
1. 裂隙面粗糙度显著影响水流经岩石的换热特性；总换热系数随JRC值增大而增大（恒定流量下）[Ma 2018, pp. 8-9]。
2. 总换热系数与体积流量呈正相关（JRC固定）[Ma 2018, pp. 6-7]。
3. 水温沿流向并非线性上升；采用进出口平均水温代替裂隙内平均水温会低估总换热系数[Ma 2018, pp. 8-9]。
4. 局部换热系数沿流向在入口处达到最大值，随后下降并趋于相对恒定值；裂隙面曲折度引起局部波动：当标准剖面凸起时，局部换热系数达到局部最大值，凹下时达局部最小值（因流速差异）[Ma 2018, pp. 7-8]。
5. 体积流量不改变局部换热系数沿流向的分布形态，但绝对值随流量增大而升高（裂隙面曲折度不变时）[Ma 2018, pp. 8-9]。
6. 数值模拟与实验出口水温误差最大仅0.82%，验证了模型的正确性[Ma 2018, pp. 7-8]。
7. 实验 Reynolds 数范围为4.64–21.31，Nu与Re、Pr的拟合关系如式(15)所示[Ma 2018, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 局部换热系数 \(h_0\) 沿流向先升后降，入口处最大，随后趋于稳定；局部波动与剖面凹凸对应 | [Ma 2018, pp. 7-8] | 流量20 ml/min，三种JRC（0–2,10–12,18–20），数值模拟结果 | 对比标准剖面，凸起处流速低致 \(h_0\) 局部极大；凹下处高致局部极小 |
| 总换热系数随JRC增大而增大；固定JRC时总换热系数与流量正相关 | [Ma 2018, pp. 6-7] | 外壁90°C，流量5–20 ml/min，三种JRC试件，实验测定 | 采用Bai[6]公式(10)计算 |
| 水温沿流向分布近似对数曲线，非线性上升 | [Ma 2018, pp. 7-8] | 数值模拟，流量20 ml/min，三种粗糙裂隙 | 与Zhao[5]一致性 |
| 数值模拟出口水温与实验对比误差<0.82% | [Ma 2018, pp. 7-8] | 流量20 ml/min | 验证模型可靠性 |
| 局部换热系数分布形状不受流量影响，但绝对值随流量增大 | [Ma 2018, pp. 8-9] | JRC 18–20，流量5/10/15/20 ml/min |  |
| 雷诺数范围4.64–21.31，与Nu/Pr^{1/3}呈正相关 | [Ma 2018, pp. 6-7] | 全部实验工况 | 拟合的关联式如式(15) |
| 3D打印技术可精确控制裂隙面曲折度，用于制作不同JRC试件 | [Ma 2018, pp. 2-4] | 试件长度100 mm，直径25 mm | JRC 0–2, 10–12, 18–20标准剖面 |

## Limitations
- 研究仅限于层流状态（Re最大约21），未考虑湍流情况。
- 试件尺寸较小（直径25 mm，长100 mm），尺度效应未讨论。
- 仅采用三种JRC值（0–2、10–12、18–20），不足以完全表征所有天然裂隙粗糙度。
- 数值模拟假设岩石基质不透水，忽略基质内流体流动。
- 实验与模拟均采用恒定外壁温度90 °C，未研究不同温度水平的影响。
- 局限于单裂隙，未涉及裂隙网络或裂隙开度变化。

## Assumptions / Conditions
- 裂隙中水流为层流，忽略惯性效应，流体流仅发生在裂隙内，岩石基质不透水[Ma 2018, pp. 4-6]。
- 热传输考虑流体对流、流体内部导热和岩石导热；流体与岩石之间的换热遵循牛顿冷却定律[Ma 2018, pp. 4-6]。
- 数值模拟中达到稳态的判断为孔隙压力不再变化[Ma 2018, pp. 4-6]。
- 实验时围压1 MPa以密封并高于流体压力，防止外漏[Ma 2018, pp. 2-4]。
- 局部换热系数推导基于每个离散元素进出口水温差与内壁平均温度[Ma 2018, pp. 6-7]。
- 总换热系数计算公式(10)假定试件半径方向温度呈线性分布[Ma 2018, pp. 6-7]。
- 水流与试件初始温度均匀（外壁90 °C，水初温按实验设定）[Ma 2018, pp. 4-6]。

## Key Variables / Parameters
- [[节理粗糙度系数 (JRC)]]：0–2, 10–12, 18–20
- 体积流量 \(q_v\)：5, 10, 15, 20 ml/min
- 外壁温度 \(T_c\)：90 °C
- 局部换热系数 \(h_0\) (W/(m²·K))
- 总换热系数 \(h_{total}\) (W/(m²·K))
- 水温 \(T_{in}, T_{out}\)，裂隙内表面温度 \(T_r\)，水流平均温度 \(T_w\)
- 雷诺数 \(Re\)，普朗特数 \(Pr\)，努塞尔数 \(Nu\)
- 几何参数：试件直径 d=0.025 m，长度 L=0.1 m
- 热物性：试件密度1900 kg/m³，导热系数1.15 W/(m·°C)，比热993 J/(kg·°C)；水密度1000 kg/m³，导热系数0.68 W/(m·°C)，比热4208 J/(kg·°C)[Ma 2018, pp. 4-6]

## Reusable Claims
- 水在粗糙裂隙中流动时，局部换热系数在入口端达到最大值，随后沿流向急剧下降并趋于恒定（恒定外壁温度和稳定流量下）[Ma 2018, pp. 8-9]。
- 裂隙面粗糙度（JRC）增加会增大总换热系数，同时加剧局部换热系数沿程的波动幅度（凸起处局部值高，凹下处局部值低）[Ma 2018, pp. 8-9]。
- 水温沿粗糙裂隙的上升不是线性的，使用进出口算术平均水温代替裂隙内平均水温会导致换热系数被低估[Ma 2018, pp. 8-9]。
- 体积流量的增减仅改变局部换热系数的绝对值大小，不改变其沿流向的分布形状（裂隙几何固定时）[Ma 2018, pp. 8-9]。
- 3D打印技术可用于制造具有预定JRC剖面的裂隙试件，实现粗糙度精确控制，适用于换热实验研究[Ma 2018, pp. 2-4]。
- 对于实验条件（外壁90°C，流量5–20 ml/min，JRC 0–20），总换热系数与流量正相关，且随JRC增大而增大，可拟合 \(Nu = C Re^n Pr^m\) 形式关联式[Ma 2018, pp. 6-7]。

## Candidate Concepts
- [[局部换热系数 (local heat transfer coefficient)]]
- [[节理粗糙度系数 (JRC)]]
- [[3D打印裂隙试件]]
- [[粗糙裂隙换热]]
- [[总换热系数 (Bai公式)]]
- [[牛顿冷却定律 (Newton’s law of cooling)]]
- [[3DEC离散元热-流耦合模拟]]
- [[对数型水温分布]]

## Candidate Methods
- [[3D打印制造可控粗糙裂隙试件]]
- [[干热岩实验室模拟系统 (hot dry rock testing system)]]
- [[基于3DEC的离散裂隙网络热-流耦合数值模拟]]
- [[局部换热系数离散计算方法 (式9)]]
- [[总换热系数Bai模型 (式10)]]
- [[Reynolds/Prandtl/Nusselt数相似性关联式拟合]]

## Connections To Other Work
- 总换热系数随JRC增大而增大，与Zhao[3]关于粗糙度影响换热的观点一致[Ma 2018, pp. 8-9]。
- 水温非线性上升与Zhao[5]的结论一致[Ma 2018, pp. 8-9]。
- 局部换热系数入口处高、沿程下降与Dirker等[8]在环状流道的研究结果类似[Ma 2018, pp. 1-1]。
- 总换热系数公式(10)引自Bai[6]的线性温度分布假设[Ma 2018, pp. 6-7]。
- 实验装置描述参考Li等[23]的详细说明[Ma 2018, pp. 2-4]。
- 粗糙度对流体流动与换热的影响与Luo等[21]、Huang[22]的工作相关联[Ma 2018, pp. 1-2]。
- 数值方法中使用的热对流方程基于3DEC用户手册[25]和Itasca文献[Ma 2018, pp. 4-6]。

## Open Questions
- 对于更大范围JRC（包括极粗糙或极光滑）和更大流量（进入湍流）时，局部换热系数的分布规律是否仍符合文中的描述？
- 不同外壁温度（如高于90 °C）下，局部与总换热系数的量值及分布特征如何变化？
- 真实裂隙中开度变化与表面粗糙度的耦合作用对局部换热系数的影响尚未揭示。
- 裂隙网络条件下流向局部换热系数的传播与单裂隙结果有何异同？
- 三维打印材料（如混凝土）的热物性与天然花岗岩的差异是否会显著影响换热规律的外推？
- 能否建立基于裂隙剖面几何参数的局部换热系数预测模型？

## Source Coverage
本页所有内容均来自提供的8个非空索引片段，无额外杜撰。总计编译源块8个，编译字符37488，覆盖率（按块计）1.0，（按字符计）1.003856。所有片段均已处理，标记为[Ma 2018, pp. X–Y]对应原始片段页码范围。
