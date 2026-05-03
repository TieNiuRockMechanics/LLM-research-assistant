---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks"
title: "Linking Structural and Transport Properties in Three-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2019 - Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.pdf"
collections:
citation: "Hyman, J. D., et al. \"Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.\" *Journal of Geophysical Research: Solid Earth*, vol. 124, 2019, pp. 1185-1204. doi:10.1029/2018JB016553."
indexed_texts: "18"
indexed_chars: "87894"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "88283"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004426"
coverage_status: "full-index"
source_signature: "6282752bcbeb1ba14928d4a11e82b6bdfea3bdb1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T00:43:23"
---

# Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.

## One-line Summary
本文通过直接数值模拟，研究了幂律裂隙长度分布的三维稀疏离散裂隙网络（DFN）中结构特性与溶质穿透行为之间的联系，发现频繁的速度转变是关键，流管模型仅在近场有效，而基于入口速度分布条件的伯努利连续时间随机游走（CTRW）模型能够合理预测突破曲线。

## Research Question
如何将裂隙网络的几何与拓扑性质直接链接至宏观传输观测值（例如溶质穿透曲线）？现有的平均传输模型参数化往往缺少多孔介质属性与观测流动/传输特性之间的直接联系，亟需确定网络结构中哪些特征控制着粒子运动中的速度转变［Hyman 2019, pp. 1-2］。

## Study Area / Data
研究采用三个三维合成离散裂隙网络，均置于 1 km 立方域内，裂隙中心位置均匀分布，方向随机。裂隙半径 \( r \) 服从截断幂律分布，指数 \( \alpha \) 分别为 1.6（网络 1）、2.2（网络 2）和 2.6（网络 3），最小半径 \( r_0 = 1 \)（无量纲），最大半径 \( r_u = 100 \)。生成的三个网络具有几乎相同的无量纲裂隙强度 \( P_{32} \approx 0.4 \)，但其逾渗密度 \( p^* \)（分别为 93、23、14）和拓扑结构截然不同［Hyman 2019, pp. 2-4; Table 1］。裂隙开度 \( b \) 通过正相关幂律 \( b = \gamma r^\beta \)（\( \gamma = 5.0 \times 10^{-4}, \beta = 0.5 \)）关联至半径［Hyman 2019, pp. 2-3］。

## Methods
使用 dfnWorks 工作流生成 DFN，并进行稳态流和纯平流传输模拟。流控制方程基于平行板立方定律，全域施加 1 MPa 压力差，侧向为无流边界，忽略重力与基质扩散。粒子以流量加权注入模式从 \( x=0 \) 平面注入，在裂隙交叉处实施完全混合。欧拉速度场由 PFLOTRAN 求解，通过 walkabout 粒子追踪获得拉格朗日量（100 万粒子用于 BTC，10 万粒子用于速度 PDF 与相关分析）［Hyman 2019, pp. 5-7］。网络拓扑采用图论表征：裂隙为节点，相交为边，并引入入口/出口边界节点，计算最短拓扑路径（SPL）、度分布和同配系数 \( r \)［Hyman 2019, pp. 4-5; Appendix C］。传输模型方面，比较了随机对流流管模型和伯努利 CTRW 模型，后者以空间速度相关长度 \( \ell_c \) 和曲折度 \( \chi(x_1) \) 为基础，并条件化于入口速度分布 \( p_0(v) \) 或稳态分布 \( p_\ell(v) \)［Hyman 2019, pp. 10-13］。

## Key Findings
1. 裂隙强度相同的三个网络展现出完全不同的逾渗密度和拓扑：网络 1、2 中存在少数大型“枢纽”裂隙可直接连接进出口，而网络 3 的最短路径包含 11 个裂隙［Table 1; Hyman 2019, pp. 4-5］。
2. 欧拉速度分布随 \( \alpha \) 增大而整体降低；空间拉格朗日速度 PDF 与通量加权欧拉 PDF 在高速度段一致，但在低速度段因有限域效应而偏离［Hyman 2019, pp. 7-8］。
3. 流管模型在近入口控制平面（\( x_1 = 25 r_0 \)）对网络 1、2 预测较好，但随距离增加而恶化；对网络 3 在所有距离均高估尾部，表明恒定流速假设不成立，粒子路径由频繁的速度转变主导［Hyman 2019, pp. 10, 14］。
4. 速度相关长度 \( \ell_c \) 分别约为 35、25.3 和 15 \( r_0 \)（网络 1→3），对应的入口至出口平均速度转变次数约为 3.56、5.2 和 17.33，与最短路径趋势一致［Hyman 2019, pp. 11-13］。
5. 以入口速度分布为条件的伯努利 CTRW 模型较好地复现了全部三个网络在不同距离处的 BTC；对于网络 3，条件化至关重要，因 \( p_0(v) \) 与稳态 \( p_\ell(v) \) 差异显著［Hyman 2019, pp. 13-14, Figure 12］。
6. 曲折度 \( \chi \) 随距离增大，网络 3 的渐近曲折度 \( \chi_\infty = 2.71 \) 最高，网络 1、2 分别为 1.36 和 1.47，反映了方向无序程度的差异［Hyman 2019, pp. 8-9］。
7. 所有 BTC 均呈现非费克幂律拖尾，无法由单一的等效对流‑弥散方程描述［Hyman 2019, pp. 9-10］。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 三个 DFN 的 \( P_{32} \approx 0.4 \)，但 \( p^* \) 分别为 93、23、14，SPL 分别为 1、2、11 | [Hyman 2019, Table 1, pp. 4-5] | 幂律指数 1.6/2.2/2.6；域 100 \( r_0 \); \( r_u=100 r_0 \) | 逾渗密度和最短路径直接反映拓扑差异 |
| 流管模型仅能预测网络 1 和 2 在 \( x_1=25 r_0 \) 的 BTC，在出口及网络 3 全部失败 | [Hyman 2019, pp. 10, 14, Figure 7] | 使用入口速度分布 \( p_0(v) \) 和曲折度 | 恒定流速假设失效 |
| CTRW（条件化）预测的 BTC 在所有网络和控制平面均与直接数值模拟吻合 | [Hyman 2019, pp. 13-14, Figures 10‑12] | \( \ell_c \) 来自速度相关函数，\( \chi \) 来自粒子路径 | 速度转变频率是关键控制因素 |
| \( \ell_c \) 分别为 35、25.3、15 \( r_0 \)；对应平均转变次数 3.56、5.2、17.33 | [Hyman 2019, pp. 11-13] | 等距速度采样，沿流线 | 短相关长度 + 高曲折度 → 更多速度转变 |
| BTC 均显示幂律尾部，超出等效对流‑弥散模型能力 | [Hyman 2019, pp. 9-10, Figure 6] | 100 万粒子，流量加权注入 | 非费克行为是系统特征 |

## Limitations
研究仅包含三个具有单一裂隙强度（\( P_{32} \approx 0.4 \)）的合成网络，且幂律指数与参数选择有限。模拟未计入基质扩散、重力、裂隙内开度不均等实际因素。CTRW 预测依赖于需预先测量的曲折度及相关长度，实际中不易获得。粒子数为 100 万，受存储限制。作者明确指出当前结果仅为初步验证，需要更多系统检验［Hyman 2019, pp. 14-15］。

## Assumptions / Conditions
- 基岩完全不渗透，流动仅存于裂隙，无基质扩散［Hyman 2019, pp. 5-6］。
- 稳态层流，符合平行板立方定律；裂隙内开度均匀，且与半径通过固定幂律正相关［Hyman 2019, pp. 2-4］。
- 纯平流传质，裂隙交叉处完全混合，基于通量加权选择出口裂隙［Hyman 2019, pp. 6-7］。
- 流量加权注入模式，初始质量分布正比于局部通量［Hyman 2019, p. 7］。
- 无重力的水平压力驱动（1 MPa 全梯度），侧向无流动边界［Hyman 2019, p. 6］。
- 裂隙网络无空间关联，仅受长度幂律分布和截断控制。
- 速度相关函数与曲折度基于有限域计算，尚未达到渐近平稳。

## Key Variables / Parameters
- 幂律长度分布指数 \( \alpha \)（1.6, 2.2, 2.6）
- 裂隙半径范围 \( r_0=1, r_u=100 \)（无量纲）
- 裂隙开度 \( b \) 及开度‑半径幂律参数 \( \gamma=5\times10^{-4}, \beta=0.5 \)
- 裂隙强度 \( P_{32} \)（均约 0.4）
- 逾渗密度 \( p^* \)（网络 1: 93; 网络 2: 23; 网络 3: 14）
- 最短拓扑路径 SPL（1, 2, 11）
- 同配系数 \( r \)（所有网络均 <0，呈异配混合）
- 欧拉速度 PDF \( p_e(v) \)、空间拉格朗日速度 PDF \( p_\ell(v) \)、入口速度 PDF \( p_0(v) \)
- 曲折度 \( \chi(x_1) \) 与其渐近值 \( \chi_\infty \)（1.36, 1.47, 2.71）
- 速度相关长度 \( \ell_c \)（35, 25.3, 15 \( r_0 \)）
- 平均速度转变次数 \( n(x_1) = \chi(x_1) x_1 / \ell_c \)
- 控制平面距离 \( x_1 \)（25, 50, 100 \( r_0 \)）
- 突破曲线互补累积分布 \( F(t, x_1) \)

## Reusable Claims
1. 在裂隙强度相近且开度与大小正相关的三维 DFN 中，幂律指数 \( \alpha \) 较小的网络（1.6–2.2）由少数大型“枢纽”裂隙主导，粒子仅需极少量速度转变，流管模型可在近场近似预测 BTC；当 \( \alpha \) 较大（2.6）或距离增大时，频繁的速度转变使流管模型失效。（条件：\( P_{32} \approx 0.4 \)，纯平流，完全混合；限制：未涵盖基质扩散或非稳态流。）
2. 基于空间速度相关长度 \( \ell_c \) 和曲折度 \( \chi \) 的伯努利 CTRW 模型，在条件化于入口速度分布后，能有效预测稀疏 DFN 中不同距离处的非费克 BTC，尤其适用于速度转变频繁的网络。（条件：需获得 \( p_0(v) \)、\( \ell_c \) 和 \( \chi \)；适用于连通、平流主导的裂隙系统。）
3. 裂隙网络的异配混合（\( r < 0 \)）意味着高连通度的大型裂隙与众多低连通度小裂隙相连，强化了流动通道化和速度对比，是产生非费克突破行为的重要结构因素。（条件：幂律长度分布、正相关开度、无基质交换。）
4. 幂律指数不同的网络可通过图论参数（最短路径长度、度分布、同配系数）和宏观逾渗密度 \( p^* \) 有效区分，且这些参数与传输行为（如速度转变次数和 BTC 形状）存在直接关联。（条件：三维圆盘裂隙网络、均匀取向。）
5. 当入口速度分布与稳态速度分布差异显著时（如以短裂隙为主的密集网络），必须对 CTRW 进行初始速度条件化，否则近场 BTC 预测将严重失准，凸显注入模式对传输预测的重要性。（条件：流量加权注入、完全混合规则。）

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[power law fracture length distribution]]
- [[percolation density (p*)]]
- [[graph representation of fracture networks]]
- [[assortativity coefficient]]
- [[cubic law (fracture flow)]]
- [[streamtube model]]
- [[continuous time random walk (CTRW)]]
- [[Bernoulli velocity process]]
- [[space-Lagrangian velocity PDF]]
- [[velocity correlation length]]
- [[tortuosity in fractured media]]
- [[non‑Fickian transport]]
- [[flow channeling]]
- [[shortest topological path]]
- [[ergodicity in velocity distributions]]

## Candidate Methods
- [[dfnWorks simulation framework]]
- [[particle tracking in DFN]]
- [[LaGriT meshing toolbox]]
- [[PFLOTRAN flow solver]]
- [[walkabout particle tracker]]
- [[feature rejection algorithm (fram)]]
- [[graph‑based topology analysis with source/target vertices]]
- [[Dijkstra’s algorithm for SPL]]
- [[stochastic convective streamtube model]]
- [[Bernoulli CTRW time‑domain model]]
- [[Boltzmann equation for velocity‑time joint PDF]]
- [[numerical integration of cubic law in fracture networks]]

## Connections To Other Work
- Hyman et al. (2015) 开发了 dfnWorks 及 walkabout 粒子追踪，为本文提供数值基础［Hyman 2019, pp. 2-3］。
- de Dreuzy et al. (2012) 指出三维裂隙网络的宏观结构影响流场，但未直接关联传输属性，本研究填补此空白［Hyman 2019, p. 1］。
- Becker & Shapiro (2003) 的随机对流流管模型被直接检验，证实在近场和强连通网络中有效，但在速度转变频繁时失效［Hyman 2019, pp. 1-2, 10］。
- Dentz et al. (2016) 发展的伯努利 CTRW 框架被应用于裂隙网络的粒子速度序列建模［Hyman 2019, pp. 2, 13］。
- 图论表征方法源自 Hyman et al. (2017)，并扩展以考察最短路径和节点度混合［Hyman 2019, pp. 4-5］。
- Bonnet et al. (2001) 综述确认了幂律裂隙长度分布的自然普遍性，成为本研究参数选择的依据［Hyman 2019, p. 1］。
- 关于逾渗理论在裂隙网络中的应用参考了 Bour & Davy (1997, 1998)、Berkowitz & Balberg (1993) 等［Hyman 2019, pp. 3-4］。

## Open Questions
- 模型对于其他 \( P_{32} \) 值以及更宽泛的 \( \alpha \) 范围的适用性尚待检验。
- 若引入基质扩散、重力或裂隙内开度变异，速度转变机制和 CTRW 的预测效果将如何变化？
- 能否仅从可观测的静态网络属性（如密度、度分布）直接推估 \( \ell_c \) 和曲折度，以便现场应用？
- 注入模式改变（如均匀注入）或考虑非平稳流速分布时，条件化的必要性及方式如何调整？
- 在足够大的网络尺度下，渐近曲折度和稳态速度分布是否足以完整描述传输，还是仍需局部拓扑信息？

## Source Coverage
本页面已完整处理并整合全部 18 个非空索引片段，覆盖论文全文（等效于）[Hyman 2019, pp. 1-20]。来源片段签名 6282752bcbeb1ba14928d4a11e82b6bdfea3bdb1，编译后块数 18，编译字符数 88,283，块覆盖率 1.0，字符覆盖率 1.004426。所有声明均基于所供片段，无外部添加。
