---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity"
title: "Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification."
status: "draft"
source_pdf: "data/papers/2023 - Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data Method Development and Verification.pdf"
collections:
citation: "Jiang, Zhenjiao, Lisa Maria Ringel, Peter Bayer, and Tianfu Xu. \"Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.\" American Geophysical Union, 2023."
indexed_texts: "22"
indexed_chars: "106616"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "106119"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.995338"
coverage_status: "full-index"
source_signature: "50b34f4204788d3d4ead3a0df0511c8f0220f0ea"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:40:43"
---

# Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.

## One-line Summary
提出一种联合微震（MS）事件和热突破数据的贝叶斯反演方法，利用可逆跳马尔可夫链蒙特卡洛算法（rjMCMC）在二维离散裂隙网络（DFN）中推断裂隙数量、几何形态和开度，并通过合成案例验证该方法在预测热产出时误差低于5%。

## Research Question
如何利用通常在增强型地热系统和非传统油气储层中获取的微震监测数据和热示踪试验数据，联合反演以高分辨率刻划深部储层中的离散裂隙网络，从而提高流动和热输运预测的可靠性？

## Study Area / Data
研究基于两个二维合成测试案例，未使用实际现场数据，但提供了可用于方法验证的合成数据集：
- **简单案例**：包含4条裂隙的二维剖面，位于深度1500–1600米，假设地热储层条件（初始温度100℃、压力20 MPa）。合成微震事件云带有±10 m的均匀噪声；热突破曲线由30天试生产模拟生成，并叠加标准差为1.0°C的正态噪声。 [Jiang 2023, pp. 9-10]
- **露头案例**：基于中国共和盆地野外露头照片提取的17条裂隙网络，假设埋深1500–1600米，初始温度100℃、压力20 MPa。合成4000个微震事件；热突破曲线含有标准差0.1°C的测量误差。用于反演的数据包括由5条钻孔揭露的裂隙给出的先验信息（最小裂隙数5、方位范围55°–70°和‑25°–‑35°），以及30天试生产期间三个观测位置的热突破曲线。独立验证采用另一组注入/抽取方案。 [Jiang 2023, pp. 11-12]
- 提供的数据和代码可通过Harvard Dataverse获取（Jiang, 2022a, 2022b）。 [Jiang 2023, pp. 20]

## Methods
- **先验信息利用**：根据钻孔成像确定最小裂缝数（nmin）和裂隙方位的均匀分布范围；裂隙水力开度假定服从10⁻⁴–10⁻² m的对数均匀分布。 [Jiang 2023, pp. 3-4]
- **基于微震事件的DFN生成**：假设微震事件已滤除“干”事件，仅使用“湿”事件云。通过随机选取一个微震事件作为参考位置、采样一个方位，并将距离小于微震定位最大误差的微震事件投影到该无限裂缝上，估算裂缝长度和中心坐标。重复上述过程直至生成预设数量（nf）的裂缝。 [Jiang 2023, pp. 4-6]
- **正演模型**：采用嵌入式离散裂缝模型（EDFM）分别求解基质和裂缝中的稳态流动方程与瞬态热输运方程，使用开源代码THERMAID。 [Jiang 2023, pp. 6-7]
- **反演算法**：采用可逆跳马尔可夫链蒙特卡洛（rjMCMC）按Bayes定理更新裂缝数量（nf）、方位（s）和开度（b），而裂缝中心位置和长度由微震事件预先确定。更新操作包括“更新”（仅扰动开度）、“添加”（增加一条裂缝并重新生成网络）和“删除”（减少一条裂缝并重新生成网络）。接受准则采用Metropolis-Hastings-Green公式，其中提案概率比依赖于裂缝与微震事件匹配的优劣。 [Jiang 2023, pp. 7-9]
- **收敛与验证**：以计算与观测温度之间的RMSE降至测量误差以下作为收敛判据；通过燃烧期后的多条链样本生成裂缝概率图，并利用独立条件下的热突破曲线验证预测能力。 [Jiang 2023, pp. 11-12]

## Key Findings
- 在简单案例中，联合反演成功识别出所有裂缝，隐藏裂缝的中心位置误差<3.0 m，半长误差<0.5 m，方位误差<5°，开度估计在0.24–0.68 mm（真实值1.0 mm）。 [Jiang 2023, pp. 13-14]
- 微震定位误差（Em）低于相邻裂缝最小间距（Dm）的1.5倍是可靠分离相邻裂缝的前提条件；当Em超过1.5 Dm时，相邻裂缝可能被合并为一条具有较大开度的裂缝。 [Jiang 2023, pp. 14-15]
- 在露头案例中，联合反演推断的裂缝数量为14–16条（真实值17条），开度估计均值3.6 mm（真实值1.0 mm），裂缝骨架的高概率区域与真实网络一致。使用独立验证数据时，热突破温度预测的平均误差小于1.0°C（约温度变化的4%）。 [Jiang 2023, pp. 17-18]
- 与仅用温度数据的传统反演相比，加入微震数据可将燃烧期从>1000次迭代缩短至约400次，显著降低裂缝长度的高估倾向和预测温度的不确定性，并使验证阶段的温度预测误差从>5°C降至<1°C。 [Jiang 2023, pp. 18-19]
- 敏感性分析表明，裂缝数量、开度和方位对流出温度敏感，且不同观测位置对不同参数敏感，多位置监测有助于约束不同裂缝参数。 [Jiang 2023, pp. 12-13]
- 方法对热导率变化不敏感，考虑密度驱动流可略微改善裂缝方位估计，而加入压力观测对本案例提升有限；钻孔处裂缝方位未知时，隐藏裂缝的长度估计不确定性增大。 [Jiang 2023, pp. 15-17]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 联合反演可准确识别隐藏裂缝：中心位置误差<3.0 m，半长误差<0.5 m，方位误差<5° | [Jiang 2023, pp. 13-14] | 简单案例（4条裂缝），微震定位误差±10 m，先验方位范围±10° | 开度略微低估（0.24–0.68 mm vs. 1.0 mm） |
| 微震误差Em < 1.5 Dm时可正确分离裂缝，Em = 1.5 Dm时裂缝数量仍可确定，但Em = 40 m (≈2 Dm)时数量出现波动 | [Jiang 2023, pp. 14-15] | 简单案例，Dm = 20 m（相邻平行裂缝间距） | 高误差下裂缝被合并，开度补偿性增大 |
| 露头案例中联合反演裂缝数量14–16条，开度均值3.6 mm，热突破验证预测误差<1.0°C（约4%） | [Jiang 2023, pp. 17-18] | 17条裂缝案例，微震事件4000个，最小裂缝数5 | 较少的裂缝数被较大的开度补偿 |
| 联合反演比纯温度反演更快收敛（燃烧期约400 vs. >1000次迭代），验证温度误差<1°C vs. >5°C | [Jiang 2023, pp. 18-19] | 露头案例，100条独立链 | 微震数据提供几何约束，提升效率和精度 |
| 提高基质热导率至8.0 W/(m·°C)不影响反演精度；考虑密度驱动流略微改善裂隙方位估计 | [Jiang 2023, pp. 15-16] | 简单案例，其他条件同基案 | 计算量因密度驱动流显著增加 |
| 钻孔处裂缝方位已知是准确估计隐藏裂缝长度的有利条件 | [Jiang 2023, pp. 16-17] | 简单案例，对比未知方位的情形 | 未知方位时MS事件可能被错误归类到相邻裂缝 |

## Limitations
- 方法目前仅在二维合成案例中验证，尚未应用于实际现场三维问题。 [Jiang 2023, pp. 19-20]
- 当微震定位误差较大（Em > 1.5 Dm）时，相邻裂缝可能被合并，导致裂缝数量低估和开度高估。 [Jiang 2023, pp. 14-15, 19]
- 微事件云仅使用“湿”事件；干事件的排除依赖预处理方法，实际应用可能存在偏差。 [Jiang 2023, pp. 3-4]
- 正演模型未考虑流体压力和温度对密度、黏度的影响（除敏感性测试外），也未耦合力学效应，仅适用于表征储层改造后的最终裂缝状态。 [Jiang 2023, pp. 6-7]
- 三维扩展时计算效率可能成为瓶颈；当前正演模型（THERMAID）的二维有限差分求解速度尚可，但三维复杂网络下需要高性能DFN模拟器（如DFNWORKS）。 [Jiang 2023, pp. 19-20]
- 热示踪在三维储层中可能因强热耗散导致温度响应微弱，实践中可能需要结合保守或反应性示踪剂。 [Jiang 2023, pp. 19-20]

## Assumptions / Conditions
- 微震事件已通过基于密度的空间聚类和震源机制分析等手段滤除了“干”事件，只保留发生在活化裂缝上的“湿”事件。 [Jiang 2023, pp. 3-4]
- 裂缝方位遵循均匀分布（两组共轭裂缝集），水力开度服从对数均匀分布。 [Jiang 2023, pp. 3-4]
- 流动为稳态，热输运为瞬态，基质渗透率极低（10⁻²⁰ m²），裂缝为主要流动通道。 [Jiang 2023, pp. 6-7]
- 裂缝形状在二维问题中为线单元，在可扩展的三维情形中可假设为平面矩形。 [Jiang 2023, pp. 19-20]
- 反演期间模型边界条件（压力和温度）保持不变。 [Jiang 2023, pp. 9]
- 裂缝参数（数量、方位、开度）相互独立，且先验分布不受后续数据影响。 [Jiang 2023, pp. 7-8]

## Key Variables / Parameters
- **裂缝数量** (nf)：整数，最小值为钻孔揭露的裂缝数，无上限，通过 rjMCMC 的加减操作更新。
- **裂缝方位** (s)：连续变量，两组共轭方向的均匀分布，在 rjMCMC 中随裂缝数量变化而更新。
- **水力开度** (b)：连续变量，对数均匀分布 (10⁻⁴–10⁻² m)，在“更新”步骤中通过正态扰动调整。
- **裂缝中心位置** (x, y) 和长度 (l)：由选定的微震事件投影确定，不直接作为反演参数，但在每次重新生成裂缝网络时更新。
- **观测数据**：热突破温度 (Tobs) 和微震事件的空间坐标；合成案例中温度观测的测量误差标准差为1.0°C（简单案例）或0.1°C（露头案例）。 [Jiang 2023, pp. 9-11]
- **控制参数**：微震定位最大允许误差（决定投影容差）、先验方位范围、最小裂缝数。

## Reusable Claims
- 在微震定位误差不超过相邻裂缝间距的1.5倍的条件下，联合MS和热示踪数据反演能够准确识别裂缝数量、位置和长度，且误差显著低于原始MS定位误差。 [Jiang 2023, pp. 14-15]
- 该方法仅需最小裂缝数和粗略的方位范围作为先验信息，配合热突破曲线和微震事件云，即可构建高精度DFN，适合深部储层数据稀缺的场景。 [Jiang 2023, pp. 20]
- 加入微震数据可以大幅缩短rjMCMC的燃烧期（例如从>1000次降至约400次），并提高热突破验证预测的准确度，证明MS和温度数据具有互补性。 [Jiang 2023, pp. 18-19]
- 反演得到的裂缝集合能够以低于5%的误差预测不同生产方案下的热产出，表明所推断的DFN具有良好的预测能力。 [Jiang 2023, pp. 17-18, 20]
- 方法对基质热导率不敏感，且可通过考虑密度驱动流进一步提升裂缝方位估计的精度，但需权衡计算成本。 [Jiang 2023, pp. 15-16]
- 该方法框架可拓展至三维，只需将方位参数替换为倾向/走向，并将裂缝长度替换为长度和宽度。 [Jiang 2023, pp. 19-20]

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[reversible jump Markov chain Monte Carlo (rjMCMC)]]
- [[microseismic cloud]]
- [[wet microseismic events]]
- [[thermal breakthrough curve]]
- [[embedded discrete fracture model (EDFM)]]
- [[fracture aperture]]
- [[Bayesian inversion]]
- [[transdimensional inversion]]
- [[fracture network tomography]]

## Candidate Methods
- [[joint inversion of microseismicity and thermal data]]
- [[prior sampling from borehole logs]]
- [[fracture network generation from MS events]]
- [[embedded discrete fracture model forward modeling]]
- [[Metropolis-Hastings-Green acceptance criterion]]
- [[single-chain and multi-chain rjMCMC]]
- [[fracture probability map from posterior realizations]]
- [[independent validation with alternative injection/extraction scenarios]]

## Connections To Other Work
- 连续介质反演模型（如Illman et al., 2009; Brauchler et al., 2013）将裂隙网络平滑为渗透率张量，适用于密集裂隙网络，但可能低估裂隙渗透率和高估基质渗透率。 [Jiang 2023, pp. 1-2]
- 离散裂隙网络（DFN）生成常依赖露头统计和钻孔数据，并假设长度分布遵循幂律（Marrett et al., 1999），但缺乏水力连通性约束。 [Jiang 2023, pp. 2-3]
- Somogyvári et al. (2017) 和 Ringel et al. (2019, 2021) 发展了基于水力/示踪层析成像的跨维反演方法来推断DFN，本研究在其基础上引入微震数据以加速收敛和降低不确定性。 [Jiang 2023, pp. 3-4]
- 微地震用于约束裂缝几何形状的工作已有报道（如Aminzadeh et al., 2013; Fadakar Alghalandis et al., 2013），但此类方法往往忽略水力连通性；本研究通过联合热数据弥补这一不足。 [Jiang 2023, pp. 3-4]

## Open Questions
- 如何在三维复杂裂缝网络中以可接受的计算成本实现联合反演，并且能否直接耦合MS事件生成的物理过程（如剪切和拉伸变形）到rjMCMC框架中？ [Jiang 2023, pp. 19-20]
- 在现场条件下，微震事件的“湿/干”分类和定位误差可能比合成案例更复杂，对方法在真实深部储层中的表现还需要进一步检验。 [Jiang 2023, pp. 3-4]
- 方法是否可以有效整合其他类型的数据（如压力、化学示踪剂）以进一步降低不确定性，尤其是在热示踪信号微弱的高温储层中？ [Jiang 2023, pp. 19-20]
- 在高度裂隙化的储层中（裂缝间距很小），方法的合并倾向是否会导致对渗流和传热行为的显著误估？是否有改进的策略来识别密集团簇？ [Jiang 2023, pp. 14-15, 19]

## Source Coverage
本页面基于论文全部22个非空索引片段生成，共处理了106,119字符（占源文总字符的99.5%），覆盖了自引言至结论的所有主要部分。所有证据均来自提供的片段，未使用摘要之外的未索引信息。
