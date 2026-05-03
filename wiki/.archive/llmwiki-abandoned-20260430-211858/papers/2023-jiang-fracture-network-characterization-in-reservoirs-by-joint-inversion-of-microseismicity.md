---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity"
title: "Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification."
status: "draft"
source_pdf: "data/papers/2023 - Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data Method Development and Verification.pdf"
collections:
citation: "Jiang, Zhenjiao, Lisa Maria Ringel, Peter Bayer, and Tianfu Xu. \"Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.\" American Geophysical Union, 2023."
indexed_texts: "22"
indexed_chars: "106616"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:35:10"
---

# Fracture Network Characterization in Reservoirs by Joint Inversion of Microseismicity and Thermal Breakthrough Data: Method Development and Verification.

## One-line Summary
开发了一种基于贝叶斯原理的联合反演方法，利用微震事件云与热突破数据共同推断储层中离散裂缝网络的数量、几何形态和孔径 [Jiang 2023, pp. 1-1]。

## Research Question
在深层裂隙储层中，由于钻孔数量有限、传统水力-示踪试验难以实施，如何仅凭已有的微震监测和热突破信号，可靠地重建控制流体流动与传热的水力活跃裂缝网络的空间配置及关键参数？ [Jiang 2023, pp. 1-1, 2-3]。

## Study Area / Data
- **测试场景**：方法在二维增强型地热系统储层剖面中进行了验证，包括一个由4条裂缝组成的简化案例，以及一个从真实露头数据提取的17条裂缝复杂案例，用于评估反演捕捉裂缝骨架和预测不同注采方案下出水温度的能力 [Jiang 2023, pp. 8-9]。
- **先验数据来源**：微震事件云（3D空间分布）；钻孔成像提供的裂缝组方向的范围分布（均匀分布）和可识别的最小裂缝数量；钻孔中通过区分钻井诱发裂缝与原位裂缝确定的原始裂缝数目 [Jiang 2023, pp. 3-4]。
- **观测数据**：热突破曲线，即采出流体温度随时间变化的序列，其测量误差假设服从零均值正态分布 [Jiang 2023, pp. 6-7]。
- 其余具体场地信息未从索引片段中确认。

## Methods
- **整体框架**：由先验信息定义、微震事件驱动的初始裂缝几何生成、流-热正向模拟和基于贝叶斯定理的裂缝网络可逆跳马尔可夫链蒙特卡洛（rjMCMC）反演四部分组成 [Jiang 2023, pp. 3-4]。
- **先验设定**：裂缝数量服从以钻孔识别裂缝数为下限的均匀整数分布；各裂缝组的取向服从已知上下界的均匀分布；孔径取先验概率分布 [Jiang 2023, pp. 3-4]。
- **初始几何生成**：从微震事件云中随机选择参考点并赋予从先验中采样的方向，将距离小于定位误差容忍度的事件视为被该裂缝包含。通过投影和坐标极差确定裂缝长度（二维），重复该过程生成符合方向与数量先验的裂缝网络。优化目标是最小化所有裂缝与未被包含事件之间的平均欧拉距离 \(L_s\) [Jiang 2023, pp. 4-5]。
- **正向模型**：采用开源代码THERMAID求解稳态达西流和基质-裂隙热传递方程，计算采出温度。模型忽略温度和压力对流体密度与粘度的影响，且未耦合力学过程，仅表征储层刺激后的最终裂缝状态 [Jiang 2023, pp. 6-7]。
- **贝叶斯反演（rjMCMC）**：通过三种步长（更新孔径、增加一条裂缝并重新生成几何、删除一条裂缝并重新生成几何）扰动当前裂缝参数。接受概率基于Metropolis-Hastings-Green准则，比较提议状态与当前状态的后验比值。经历“burn-in”阶段后，迭代收敛，并生成一系列可行的离散裂缝网络实现 [Jiang 2023, pp. 7-8]。
- **似然函数**：基于观测温度与正向模拟温度之差平方和，并除以测量误差方差，构建拟合优度 \([L_t]\) [Jiang 2023, pp. 6-7]。

## Key Findings
- 提出的联合反演程序已通过两个二维案例进行了验证：简单案例用于直接评估裂缝数目、取向、位置、长度和孔径的反演精度；复杂案例用于考察方法捕捉裂缝网络骨架及在变化注采条件下预测出水温度的能力 [Jiang 2023, pp. 8-9]。
- 具体的定量反演误差、收敛行为和后验分布特征未从索引片段中确认。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 微震事件分为“湿事件”（水力压裂直接诱发）和“干事件”（应力/压力变化在远处断层激活的滑动），包含干事件会高估水力裂缝几何，需通过事件发生时间与压裂井距离关系等诊断分析来区分 | Jiang 2023, pp. 2-3 | 需拥有微震事件的发生时间、震级频率和与井距离数据 | 大多数压裂能量消耗在非震张性变形和流体摩擦，剪切变形和尖端活动不一定反映孔径 |
| 钻孔成像揭示裂缝组方向多呈共轭分布，可将方向先验设为均匀分布；需区分钻井诱发裂缝，以原始裂缝数量作为最小裂缝数量 | Jiang 2023, pp. 3-4 | 需具备钻孔成像测井资料；深层钻孔诱导裂缝可能高估活跃裂缝数 | 方向先验需要定义各组的上下界 |
| 基于微震事件的初始裂缝网络生成算法通过最小化 \(L_s = \frac{\sum_{i=1}^{n_f} \sum_{j=1}^{p} \|d_{i,j}\|}{n_f p_f}\) 来实现几何拟合 | Jiang 2023, pp. 4-6 | 使用被裂缝包含的事件数量加权；欧拉距离容忍度等于微震定位的最大误差 | 该步骤仅提供几何初始解，不直接保证水力连通性 |
| 流-热正向模拟采用稳态达西流和热传递方程，在不考虑密度、粘度温度依赖和力学耦合下求取出水温度 | Jiang 2023, pp. 6-7 | 模型假设裂缝网络为最终状态，忽略储层刺激过程中的动态变化 | 使用THERMAID开源代码，二维有限差分法求解 |
| rjMCMC算法通过更新、增加和删除三种操作实现跨维度参数空间探索，接受概率 \(A = \min\left[1, \frac{p(T_{obs}|r')}{p(T_{obs}|r)} \cdot \frac{\pi(r')}{\pi(r)} \cdot \frac{q(r|r')}{q(r'|r)}\right]\) | Jiang 2023, pp. 7-8 | 三操作的选择概率通过自适应规则动态调整；需要足够多的迭代次数以确保收敛 | 更新步骤中孔径扰动服从标准正态分布 |

## Limitations
- 当前方法仅在二维情景下开发和验证，尚未扩展到实际三维裂缝网络表征。
- 正向模型未考虑温度与压力对流体物性（密度、粘度）的影响，也未耦合力学过程，仅适用于储层刺激完成后的静态裂缝网络描述 [Jiang 2023, pp. 6-7]。
- 方法强烈依赖微震事件的定位精度，且需要有效的干/湿事件鉴别手段，否则几何反演结果易产生偏差 [Jiang 2023, pp. 2-3]。
- 先验信息（方向范围、最小裂缝数）的准确性依赖钻孔资料的质量和数量，深层储层常面临钻孔不足的困境 [Jiang 2023, pp. 1-1, 3-4]。
- 索引片段未覆盖结果与讨论部分，因此对算法的收敛速度、参数后验分布的宽度、以及计算成本等具体限制无法评估。

## Assumptions / Conditions
- 裂缝网络可简化为二维离散裂缝网络，忽略三维扭转和网络连通性的复杂细节。
- 表征对象为储层刺激后的最终水力活跃裂缝网络，不考虑裂缝的扩展和闭合过程 [Jiang 2023, pp. 6-7]。
- 流体为不可压缩，基质和裂缝中的流动均满足达西定律；热传递中基质与裂缝间存在局部热交换 [Jiang 2023, pp. 6-7]。
- 微震事件的定位误差服从一个固定容许值，低于该误差的事件被认为归属于某条裂缝 [Jiang 2023, pp. 5]。
- 热突破曲线的观测误差呈零均值正态分布且标准差已知或可估计 [Jiang 2023, pp. 6-7]。
- 先验参数（裂缝组方向区间、最小裂缝数）可以通过钻孔成像测井可靠获取；对于深层井，需能有效区分钻井诱发和原有裂缝 [Jiang 2023, pp. 3-4]。

## Key Variables / Parameters
- \(n_f\)：裂缝数量，作为跨维参数由rjMCMC采样 [Jiang 2023, pp. 7-8]
- \(s\)：裂缝取向，从均匀先验分布 \(U(s_{min}, s_{max})\) 中抽样 [Jiang 2023, pp. 3-4]
- \(b\)：裂缝孔径，由更新步骤中的正态扰动调整 [Jiang 2023, pp. 7-8]
- \(L_s\)：微震事件与裂缝网络间的平均距离，用于初始几何优化 [Jiang 2023, pp. 4-5]
- \(L_t\)：观测与模拟出水温度的加权均方根误差，作为似然函数的核心 [Jiang 2023, pp. 6-7]
- \(\sigma\)：温度测量误差的标准差 [Jiang 2023, pp. 6-7]
- \(A\)：Metropolis-Hastings-Green接受概率，控制参数更新 [Jiang 2023, pp. 7-8]
- 裂缝长度（由投影坐标极差确定）与裂缝位置（由微震参考点和方向推导）为派生变量，但不作为独立采样参数。

## Reusable Claims
1. 在深层储层仅具备少量钻孔和微震监测的条件下，利用微震事件云生成初始裂缝几何、再通过热突破数据反演调整裂缝数量、方向和孔径的方法，能够实现对水力活跃裂缝网络的有效推断；其前提是能够区分湿微震事件和干微震事件，且热突破曲线具有足够分辨度 [Jiang 2023, pp. 1-1, 2-3, 6-7]。
2. 应用可逆跳变MCMC允许裂缝数量作为随机变量，通过“增加-删除”操作跨越不同参数维度，避免预先固定裂缝条数带来的过参数化或欠拟合问题，但需要大量迭代来保证后验收敛 [Jiang 2023, pp. 7-8]。
3. 基于均匀先验的方向模型与由钻孔成像约束的裂缝组方向相结合，既能保留地质信息又保持贝叶斯框架的灵活性；不过，若忽略钻井诱发裂缝的剔除，裂缝数量将可能被高估 [Jiang 2023, pp. 3-4]。
4. 由于微震事件只反映几何范围而不直接表征水力连通性，耦合热突破数据是必要的：流动和热传输模拟使得最终裂缝网络的连通程度和孔径受实测温度响应严格约束 [Jiang 2023, pp. 2-3, 6-7]。
5. 目标函数 \(L_s\) 和 \(L_t\) 的联合最小化策略提供了几何拟合与流动模拟之间的桥梁，但在高维、多相或三维问题中其权重与计算效率的平衡仍有待研究 [Jiang 2023, pp. 4-6, 6-7]。

## Candidate Concepts
[[discrete fracture network]], [[microseismicity]], [[thermal breakthrough]], [[Bayesian inversion]], [[rjMCMC]], [[hydraulic tomography]], [[fracture reservoir]], [[enhanced geothermal system]], [[preferential flow path]], [[fracture characterization]]

## Candidate Methods
[[joint inversion]], [[MCMC]], [[forward heat transport modeling]], [[THERMAID]], [[uncertainty quantification]], [[transdimensional inversion]], [[microseismic event localization]]

## Connections To Other Work
- 本研究在对离散裂缝网络反演时引用了Somogyvári et al. (2017)的跨维反演算法（rjMCMC），作为参数维度可变采样的核心基础 [Jiang 2023, pp. 2-3]。
- 在裂缝表征方法的讨论中，列举了大量对比文献：连续介质方法（如Day-Lewis et al. 2000; Illman et al. 2009）和离散裂缝模型（如Afshari Moein et al. 2018; Maillot et al. 2016）的应用场景与局限 [Jiang 2023, pp. 1-2]。
- 微震事件与裂缝几何关系方面，引用了Cornet (2000)、Shapiro et al. (1999)等关于微震机制讨论的文献，以及Maxwell et al. (2008, 2015a)关于能量分配与震源性质的结论 [Jiang 2023, pp. 2-3]。
- 方法学上可连接到其他利用水力层析成像（如Illman et al. 2009）或示踪试验反演裂缝网络的方案，但未在片段中建立直接算法关联。

## Open Questions
- 从微震事件中可靠识别“湿事件”并剔除“干事件”的具体诊断标准及其对反演结果敏感性的定量评估，未在索引片段中确认。
- 三维裂缝网络的反演性能以及计算效率的可行性尚未可知。
- 正模型忽略的温度、压力对流体属性的影响在实际深层地热储层中是否会引起显著偏差，未从片段中确认分析。
- 联合反演中微震几何误差与热拟合误差之间的权重分配策略未被详细讨论。
- 现场数据（如真实EGS场地）的应用验证和与传统方法的对比尚缺。

## Source Coverage
本页内容依据提供的22个索引片段中的8个片段（覆盖论文第1至9页）编写，主要包括引言、方法、测试案例设置等章节。片段缺失了结果、讨论与结论部分，因此无法反映反演精度的定量指标、收敛行为、与其他方法的详细对比、以及实际现场适用性的讨论。此外，插图与数据表格均未包含在片段中，部分参数定义（如测量标准差的具体数值）和计算细节可能缺失。
