---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-ma-experimental-research-on-the-heat-transfer-characteristics-of-fluid-flowing-through-rock"
title: "Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures."
status: "draft"
source_pdf: "data/papers/2023 - Experimental research on the heat transfer characteristics of fluid flowing through rock with intersecting fractures.pdf"
collections:
citation: "Ma, Yueqiang, et al. \"Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures.\" *Geothermics*, vol. 107, 2023, 102587."
indexed_texts: "13"
indexed_chars: "64180"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:27:01"
---

# Experimental Research on the Heat Transfer Characteristics of Fluid Flowing through Rock with Intersecting Fractures.

## One-line Summary
通过室内实验与解析推导，研究了水流经单裂隙、双交叉裂隙和三交叉裂隙花岗闪长岩样时的对流换热系数、水力传导特性，揭示了加载-卸载过程中围压对渗流与传热的不可逆影响。[Ma 2023, pp. 1-10]

## Research Question
单一裂隙与多交叉裂隙通道在水流流动过程中的对流换热系数如何推导与比较？围压加载与卸载过程如何影响裂隙岩体的等效水力开度、水力传导系数和渗透率？多裂隙网络的换热机理与单一裂隙有何异同？[Ma 2023, pp. 1-2, 6-9]

## Study Area / Data
- 岩样取自吉林省德惠市后山地区，岩性为晚印支期花岗闪长岩，灰白色、致密、无明显天然裂隙。[Ma 2023, pp. 2-3]
- 人工制备三种柱状试样：单裂隙(Sample I，直径49.5 mm，高99 mm)、双交叉裂隙(Sample II，直径49.1 mm，高100 mm)、三交叉裂隙(Sample III，直径48.7 mm，高99.9 mm)。采用直径1 mm线切割机加工，裂隙面平整光滑。因材料损失，最终直径均＜50 mm。[Ma 2023, pp. 2-3]
- 实验条件：岩样整体加热并保持恒温85°C；围压范围5、10、15、20、25 MPa，加载与卸载两种路径；注入蒸馏水，体积流量5、10、15、20、25 ml/min；监测进出口水温与压力。[Ma 2023, pp. 3-5, Tab. 2]
- 未从索引片段中确认每组实验的重复次数及其统计变异信息。

## Methods
1. **实验装置**：自研干热岩模拟系统，包含围压、渗透压力、温控、试样夹持与数据采集子系统。工作参数：流速0~45 ml/min，温度0~200°C，围压0~40 MPa。[Ma 2023, pp. 2-3]
2. **对流换热系数计算**：
   - 单裂隙基于Bai et al. (2017b) 总换热系数模型，假设岩柱内壁面温度T_r0、外壁恒温T_c，水温T_w(y)以进出口平均值近似，公式为 h = Q/[4LR(½(T_r0+T_c)-T_w(y))]。[Ma 2023, pp. 3-4]
   - 文中汇编并比较了五种文献公式（表3, 包括Zhao 2014, Bai et al. 2017b 等），并利用Bai et al. (2017b) 的实验数据进行验证。[Ma 2023, pp. 4-5]
   - 多裂隙处理为等效大裂隙，渗流截面积按 A_I = πDb, A_II = πD·(b₁+b₂), A_III = πD·(b₁+b₂+b₃) 计算。[Ma 2023, pp. 5-6]
3. **渗流参数计算**：
   - 水力传导系数 K、渗透率 k 通过达西定律推导，考虑温度对水的密度 ρ_w、比热容 c_w、动力粘度 μ 的影响，采用多项式拟合（0~100°C）：ρ_w(T), c_w(T), μ(T) 表达式(16)-(18)。[Ma 2023, pp. 5-6]
   - 等效水力开度通过渗流数据反算。[Ma 2023, pp. 6]
4. **加卸载实验**：先逐级加载围压(5→25 MPa)，再逐级卸载(25→5 MPa)，每级稳定后测量注入压力与进出口温度，计算水力传导系数与换热系数。[Ma 2023, pp. 6-9]

## Key Findings
- **换热系数公式评估**：在综述的五个公式中，Zhao(2014) 公式得出负系数，其余公式趋势一致但数值有差异；Bai et al.(2017b) 公式(式II)采用水温线性分布假设，导致其计算值低于基于非线性假设的公式V；大流量时公式IV的增幅大于其他公式。[Ma 2023, pp. 4-5]
- **加载过程渗流特性**：三种岩样的水力传导系数和渗透率均随围压增大而下降，主要机制是裂隙面法向应力增大导致裂隙开度减小。光滑平坦裂隙面的接触状态是控制渗流的主因。[Ma 2023, pp. 6-9]
- **卸载过程不可逆性**：相同围压水平下，卸载时的注入压力普遍高于加载时。单裂隙试样卸载时注入压力增加0.5~2.44 MPa，双交叉裂隙增加0.05~0.66 MPa，三交叉裂隙增加0~0.014 MPa。对应地，水力传导系数在卸载后低于加载时（例如20 MPa围压下，三裂隙试样卸载时159.24 μm/s 对 加载时167.97 μm/s），表明加载过程造成了不可逆塑性变形，裂隙渗流能力不能完全恢复。[Ma 2023, pp. 9-10]
- **多裂隙效应**：随裂隙数量增加，卸载-加载注入压力差值减小，反映多裂隙网络对应力的调整能力或损伤分布的变化。三裂隙岩样加载-卸载渗流差异最小。[Ma 2023, pp. 9-10]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 五种总换热系数公式中，仅 Zhao(2014) 得出负值，其余正值且趋势基本一致。 | [Ma 2023, pp. 4-5] | 引用 Bai et al.(2017b) 实验数据；花岗岩试样单裂隙，水温85°C，围压/流量未指定 | 公式I (Zhao 2014) 基于轴向线性温升假设，不适用于该实验条件。 |
| Bai et al.(2017b) 公式(式II)计算的换热系数低于公式V，因式II假设水温沿程线性分布。 | [Ma 2023, pp. 4-5] | 同样数据 | 公式V来源未在片段中指明。 |
| 单裂隙试样加载过程注入压力随围压增大而升高，水力传导系数下降。 | [Ma 2023, pp. 6-9] | 光滑裂隙面，85°C，流量1~25 ml/min，围压5~25 MPa | 图7、图8展示趋势。 |
| 卸载-加载注入压力差：单裂隙0.5~2.44 MPa，双裂隙0.05~0.66 MPa，三裂隙0~0.014 MPa。 | [Ma 2023, pp. 9-10] | 85°C，流量1 ml/min下对比 | 三裂隙变化最小。 |
| 卸载时水力传导系数低于加载时（如20 MPa，1 ml/min，三裂隙159.24 μm/s vs 167.97 μm/s）。 | [Ma 2023, pp. 9-10] | 围压20 MPa，流量1 ml/min，三裂隙岩样 | 卸载后渗透能力未恢复。 |

## Limitations
- 未从索引片段中确认论文自身明确陈述的局限性章节。根据实验描述可推断若干限制：裂隙表面均为线切割光滑面，未考虑天然裂隙的粗糙度与接触面积变化；施加围压后未直接测量力学开度，只能反算等效水力开度；实验仅使用蒸馏水作为流体，未考虑其他工质；温度固定在85°C，未探索温度效应对换热与变形的影响；所有实验均为单次加载-卸载循环，未涉及多次循环或长期效应。[Ma 2023, pp. 2-3, 9-10]（以上为基于片段的合理推断，非原文直接列出）

## Assumptions / Conditions
- 换热推导假设：岩样外壁恒温 T_c；水深温度分布可用进出口平均温度代替；基于 Bai et al.(2017b) 的径向线性温度假设。[Ma 2023, pp. 3-4]
- 多裂隙换热简化：将双裂隙或三裂隙视为一个等效大裂隙，换热面积按实际渗流截面积加倍。[Ma 2023, pp. 5-6]
- 渗流计算假设达西定律适用，水力梯度和平均流速足够低。
- 裂隙面为线切割形成，不考虑粗糙度，接触状态由围压控制。
- 流体物性仅考虑温度影响，采用0~100°C范围内的多项式拟合，忽略压力对密度和粘度的影响。[Ma 2023, pp. 5-6]
- 实验中岩样整体初始温度固定为85°C，外界室温条件未从片段中确认。

## Key Variables / Parameters
- **对流换热系数** h (W/m²·K) 公式(1)、(I-V)
- **水力传导系数** K (μm/s)
- **等效水力开度** b (mm) 及多裂隙开度 b₁,b₂,b₃
- **渗透率** k (m²)
- **围压** (5~25 MPa)
- **注入流量** q_v 或流速 (5~25 ml/min)
- **温度** T_c (85°C岩石外壁), T_in, T_out
- **水物性**：ρ_w(T), c_w(T), μ(T) 多项式系数 [Ma 2023, pp. 5-6]
- **注入压力** (MPa)

## Reusable Claims
1. **光滑裂隙加载渗流规律**：对于光滑的平直裂隙面，围压从5 MPa增大到25 MPa时，水力传导系数和渗透率单调下降，主要控制因素为法向应力引起的裂隙闭合。[Ma 2023, pp. 6-9]
   - *适用条件*：裂缝表面平整、无填充物；常温~85°C；流体为蒸馏水。
   - *限制*：未考虑粗糙度及复杂裂隙网络。

2. **加卸载渗流不可逆性**：经过一次围压加载-卸载循环后，相同围压下岩样的水力传导系数不能恢复至初始加载水平，表明存在不可逆塑性变形。[Ma 2023, pp. 9-10]
   - *证据*：单裂隙注入压力增幅0.5–2.44 MPa，双/三裂隙增幅更小；水力传导系数数据（如20 MPa，三裂隙159.24 μm/s vs 167.97 μm/s）。
   - *限制*：单次循环；光滑裂隙；花岗闪长岩。

3. **多裂隙渗流差异**：与单裂隙相比，含两条或三条交叉裂隙的岩样在卸载过程中注入压力增量显著减小，说明多裂隙结构能缓解渗流能力的不可逆损失。[Ma 2023, pp. 9-10]
   - *适用*：同等实验条件和裂隙粗糙度；需要注意三裂隙增量接近0 MPa可能出现测量误差边界。

4. **多裂隙换热等效处理**：对于具有 n 条交叉裂隙的岩样，可通过将换热面积按各裂隙渗流截面积之和进行扩展来估算总换热系数，即 A_eff = Σ πD b_i。[Ma 2023, pp. 5-6]
   - *前提*：各裂隙几何相似、水流均匀分配。
   - *限制*：仅由片段中的推导陈述，未提供实验直接验证该等效处理的换热误差。

5. **对流换热系数公式比较**：采用进出口水温平均近似时，基于线性分布假设的 Bai et al.(2017b) 公式（式II）给出偏保守的换热系数，大流量下公式IV的增幅更显著。[Ma 2023, pp. 4-5]
   - *数据源*：Bai et al.(2017b) 已发表数据。
   - *提示*：公式IV来源未在片段中指明。

## Candidate Concepts
- [[convective heat transfer coefficient in fractured rock]]
- [[equivalent hydraulic aperture]]
- [[hydraulic conductivity of fractures]]
- [[irreversible deformation in rock fractures]]
- [[loading-unloading seepage behavior]]
- [[multi-fracture heat transfer]]
- [[hydro-thermal-mechanical coupling in geothermal reservoirs]]
- [[geothermal energy exploitation]]
- [[hot dry rock simulation experiment]]

## Candidate Methods
- [[convective heat transfer coefficient analytical derivation]]
- [[experimental determination of fracture hydraulic conductivity under confining pressure]]
- [[wire-cutting preparation of rock samples with intersecting fractures]]
- [[laboratory hot dry rock simulation system]]
- [[temperature-dependent fluid property polynomial fitting for reduction]]
- [[loading and unloading test protocol for rock fractures]]

## Connections To Other Work
- 直接引用并比较了 Zhao (2014) 和 Bai et al. (2017b) 的换热系数公式，指出 Zhao 公式不适用于该实验条件，而 Bai 公式与其它公式趋势一致但数值偏小。[Ma 2023, pp. 4-5]
- 与 Jiang et al. (2017) 等研究相似，关注于初始温度、流量对换热的影响，但本文固定岩温85°C，将变量锁定在裂隙几何与围压路径。[Ma 2023, pp. 1-2]
- 在渗流力学分析中，与前人关于应力作用下裂隙开度变化的研究一致，如 Luo et al. (2017) 等讨论的围压影响。[Ma 2023, pp. 1-2]
- 潜在的连接主题：[[enhanced geothermal system (EGS) heat extraction models]]，[[fracture network permeability evolution under stress]], 以及 [[convective heat transfer coefficient for supercritical CO2]]（与 Jiang et al. 2017 对照流体差异）。

## Open Questions
- 多裂隙等效为单一大裂隙计算换热系数的误差有多大？实际流量分配不均会如何影响？未从索引片段中确认。
- 多次加卸载循环下不可逆变形的累积效应如何？未从索引片段中确认。
- 裂隙面粗糙度或充填物对换热和渗流的影响为何？文中仅提及光滑面，未比较。
- 实验结果如何外推到现场尺度（米至千米级裂隙网络）？未讨论。
- 实验中的温度仅85°C，更高温度（如150~200°C）下的换热规律和岩石热力学响应如何？未确认。

## Source Coverage
本页依据论文的13个索引片段生成，覆盖了引文信息、摘要、引言（部分）、实验方法、数据推导步骤和结果与讨论的一部分（至加卸载对比）。片段主要集中在前中段，缺失具体的实验数据表格、完整换热系数值、岩样力学与热学参数、详细的温度场分布、结论部分以及可能存在的误差分析。有关三裂隙的具体流道结构、流量分配测量或可视化信息未出现。因此，定量结论（如换热系数具体数值、不确定度）以及更广泛的敏感性讨论无法呈现。
