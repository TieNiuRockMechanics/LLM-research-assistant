---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-heinze-a-dynamic-heat-transfer-coefficient-between-fractured-rock-and-flowing-fluid"
title: "A Dynamic Heat Transfer Coefficient between Fractured Rock and Flowing Fluid."
status: "draft"
source_pdf: "data/papers/2017 - A dynamic heat transfer coefficient between fractured rock and flowing fluid.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Heinze, Thomas, et al. \"A Dynamic Heat Transfer Coefficient between Fractured Rock and Flowing Fluid.\" *Geothermics*, vol. 65, 2017, pp. 10-16. doi:10.1016/j.geothermics.2016.08.007. Accessed 2026."
indexed_texts: "8"
indexed_chars: "36530"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36373"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.995702"
coverage_status: "full-index"
source_signature: "7d1ad62b8cda5632e4c72fe8977577dcc5ba57cf"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:29:33"
---

# A Dynamic Heat Transfer Coefficient between Fractured Rock and Flowing Fluid.

## One-line Summary
提出并验证了裂隙岩石与流动流体间的动态传热系数模型，该系数依赖裂隙开度、流速和热物性，能内在地适应局部非均质性与瞬态变化。

## Research Question
地热产能预测中，岩石与流体间的热交换参数在局部非热平衡(LTNE)框架下定义模糊。如何基于可测物理量建立一个能反映裂隙系统中空间异质性和时变性的动态传热系数？

## Study Area / Data
实验数据源自Zhao and Tso (1993)的78组单裂隙岩样稳态水流动实验。试样长102 mm，宽51 mm，含水平裂隙2b。水以Tin注入，Tout流出，上下恒温T0（图1）。流量、开度、温度变化范围见表1。现场模拟使用任意生成的500 m × 500 m裂隙网络（图2），开度服从正态分布（均值18.5 µm，标准差1 µm），背景渗透率10⁻¹⁶ m²，注入点超压10 MPa，初始流体与岩石温度120°C，注入水温30°C。

## Methods
将Zhao (2014)的稳态解析解中远场边界温度T0替换为局部岩石温度Tr(x)，通过极限R→0推导得动态传热系数：
\[ h = -\frac{v \rho_f c_f}{A x} \ln\left( \frac{T_f(x) - T_r(x)}{T_{in} - T_r(x)} \right) \]
该式允许在数值网格中逐点计算h。采用有限差分显式欧拉格式耦合求解岩石与流体温度方程，平流项用半拉格朗日立方样条插值。实验室模拟忽略基质扩散与压力效应，假设一维定常流速。现场模拟叠加非线性压力扩散方程，渗透率由裂隙开度经立方律求取，流体物性随温压变化。动态h被视为准静态（变化慢于时间步长）。

## Key Findings
- 模拟全部78组实验，动态h预测的出口温度与实测值偏差多在3°C内（图3），但整体偏高；140°C岩石温度时偏差>5°C，可能因实验数据自身不一致（表1）。
- 动态h沿裂隙显著变化：初期在入口附近数值高，向下游递减；稳态后h先增后降，约60 mm处降至静态h值以下（图4）。
- 动态h导致与静态h不同的流体温度剖面：注入后50 mm内温度即快速升至接近出口值，而静态h下温度沿裂隙全程缓慢上升（图5）。
- 现场尺度25年生产模拟显示，动态h的出流温度下降晚于恒定h但更急剧（图7）；h的时空演化与实验室尺度相似，峰值随时间从注入点向下游移动但受裂隙非均质影响趋势较模糊（图8）。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 动态传热系数表达式 \( h = -\frac{v \rho_f c_f}{A x} \ln\left( \frac{T_f(x) - T_r(x)}{T_{in} - T_r(x)} \right) \) | [Heinze 2017, pp. 2-4] | 基于Zhao (2014)解析解，取R→0；稳态局部应用 | 减少参数依赖性，适合局部化模拟 |
| 78组实验模拟：动态h预测出口温度大多在实测值±3°C内 | [Heinze 2017, pp. 4-5] (Fig. 3, Table 1) | 单裂隙，稳态，水为液相，压降<1 MPa | 140°C偏差大，可能与实验条件有关 |
| 动态h沿裂隙空间变化，且随时间演化 | [Heinze 2017, pp. 5] (Fig. 4) | 实验室尺度，稳态后约60 mm处低于恒定h | 与静态h空间均匀假设形成对比 |
| 动态h导致流体温度剖面在入口区快速达稳定 | [Heinze 2017, pp. 5] (Fig. 5) | 同实验条件 | 无实测剖面数据可供对比 |
| 现场模拟：动态h使生产温度下降稍晚但更快 | [Heinze 2017, pp. 5-6] (Fig. 7, 8) | 500 m×500 m任意裂隙网，生产25年 | 动态h绝对值低于实验室，因流速较低 |
| 模型仅需常规可测参数，可内在地适应流速和温度场变化 | [Heinze 2017, pp. 6] | 单相水，裂隙主导热交换 | 未纳入表面粗糙度等孔隙尺度特征 |

## Limitations
- 在最高岩石温度（140°C）时偏差较大（>5°C），该组实验数据自身存在不一致性（出口温度明显低于岩石温度，流速敏感性异常），可能受未知压力条件影响。
- 未考虑表面粗糙度或迂曲度，而已有数值研究（Luo et al., 2016）表明粗糙度对换热有显著影响。
- 动态h源自稳态推导，瞬态模拟中假定准静态有效，未验证剧烈瞬变工况。
- 缺乏沿裂隙的温度实测剖面，无法直接验证动态h预测的温升模式。

## Assumptions / Conditions
- 实验室模拟：忽略岩石基质热扩散（实验历时短、基质渗透率极低），一维定常流速，流体物性仅取决于温度（压力影响未计，因估计压降<1 MPa）。
- 推导简化：R → 0，将远场定温边界替换为局部岩石温度Tr(x)。
- 现场模拟：裂隙网络水平、忽略重力，每个裂隙单元仅含单裂隙，渗透率各向同性，热交换仅发生于裂隙，初始岩/流温度均匀（120°C）。
- 动态h准静态假设：系统演化时间步长内温度场变化足够缓慢。

## Key Variables / Parameters
- \( h \) — 传热系数 (W/m²°C)
- \( 2b \) — 裂隙开度 (µm)
- \( v \) — 流体真实速度 (mm/s)
- \( T_{in}, T_{out}, T_f, T_r, T_0 \) — 温度 (°C)
- \( \rho_f, c_f \) — 流体密度 (kg/m³) 与热容 (J/kg°C)
- \( K_r \) — 岩石导热系数 (W/m°C)
- \( A \) — 单位体积接触面积 (m⁻¹)
- \( k \) — 渗透率 (m²)，经由 \( k = b^2/12 \) 计算
- \( \phi \) — 孔隙度

## Reusable Claims
1. **动态传热系数可仅用局部温差与流速表达**：对于离散网格点i，  
   \( h_i = -\frac{v \rho_f c_f}{A \Delta x} \ln\left( \frac{T_{f,i} - T_{r,i}}{T_{f,i-1} - T_{r,i}} \right) \)  
   *条件*：局部热非平衡，裂隙流主导，变化缓于数值时间步。*限制*：适用于单裂隙或等效连续裂隙介质，粗糙壁面效果未纳入。[Heinze 2017, pp. 2-4]
2. **在单裂隙稳态实验中，该模型能以约3°C精度重现出口温度**，但存在系统偏高，尤以低流速、高岩石温度时显著。*条件*：开度15–30 µm，流速4–200 mm/s，岩石温度90–140°C，水为液相。*限制*：140°C时偏差>5°C；实验压力未公布，可能存在未知影响。[Heinze 2017, pp. 4-5]
3. **采用动态h导致流体温度在裂隙前端快速平衡，而恒定h导致渐进升温**，这对估计生产初期热突破有重要影响。*条件*：稳态单裂隙，边界加热。*限制*：缺少裂隙内温度实测验证。[Heinze 2017, pp. 5]
4. **现场裂隙网络模拟中，动态h使生产温度衰减延迟约数年，但开始后衰减更陡峭**。*条件*：500 m×500 m裂隙网络，非均质开度分布，单相水。*限制*：裂隙网络构型为任意设定，未校正粗糙度。[Heinze 2017, pp. 5-6]
5. **该模型所需参数均可通过标准室内实验或现场测试获取**（岩石导热系数、裂隙开度、流速、流体物性），降低了应用门槛。*条件*：具备基本岩样和水力测试数据。*限制*：未包含表面粗糙度等细微结构，可能需额外修正。[Heinze 2017, pp. 6]

## Candidate Concepts
- [[local thermal non-equilibrium]]
- [[fracture aperture]]
- [[heat transfer coefficient]]
- [[fracture surface roughness]]
- [[single fracture model]]
- [[dynamic permeability]]
- [[geothermal production simulation]]

## Candidate Methods
- [[finite difference explicit Euler scheme]]
- [[semi-Lagrangian advection scheme]]
- [[cubic spline interpolation]]
- [[cubic law permeability model]]
- [[Zhao and Tso (1993) experimental setup]]
- [[Zhao (2014) analytical heat transfer coefficient]]

## Connections To Other Work
- 直接继承并扩展了Zhao (2014)的稳态解析解，消除对远场边界R的依赖。
- 与Shaik et al. (2011)的长期模拟定性吻合：LTNE模型能捕捉生产后期温度急降。
- 指出Luo et al. (2016)关于裂隙粗糙度影响的数值研究，认为需要相应实验补充以集成进动态模型。
- 采用Zhao and Tso (1993)的78组实验作为验证基准。

## Open Questions
- 140°C岩温条件下理论与实验的显著偏离是否源于实验压力或两相效应？需重复实验并公开压力数据。
- 如何将表面粗糙度系统地纳入动态h公式？当前缺少可用的粗糙度-换热实验关系。
- 动态准静态假设在流速或温度剧烈波动（如间歇生产）时是否依然有效？
- 缺乏裂隙内温度分布的实测，无法确证动态h预测的快速升温剖面。
- 现场长期运行数据缺失，动态h在真实地热储层中的表现有待实际监测验证。

## Source Coverage
本页面完全基于提供的8个非空索引片段编译而成（总源文本36,530字符，编译文本36,373字符）。覆盖率：按块数100%（8/8），按字符数99.57%。所有源片段均已处理并标注。未引入片段外信息。
