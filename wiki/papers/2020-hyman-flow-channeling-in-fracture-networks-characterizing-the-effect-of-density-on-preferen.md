---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-hyman-flow-channeling-in-fracture-networks-characterizing-the-effect-of-density-on-preferen"
title: "Flow Channeling in Fracture Networks: Characterizing the Effect of Density on Preferential Flow Path Formation."
status: "draft"
source_pdf: "data/papers/2020 - Flow Channeling in Fracture Networks Characterizing the Effect of Density on Preferential Flow Path Formation.pdf"
collections:
citation: "Hyman, Jeffrey D. \"Flow Channeling in Fracture Networks: Characterizing the Effect of Density on Preferential Flow Path Formation.\" *Water Resources Research*, vol. 56, 2020, e2020WR027986. doi:10.1029/2020WR027986."
indexed_texts: "22"
indexed_chars: "107399"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "107885"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004525"
coverage_status: "full-index"
source_signature: "9fe6c079728e3a9e3b2aab292675caeb81c894ae"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:45:57"
---

# Flow Channeling in Fracture Networks: Characterizing the Effect of Density on Preferential Flow Path Formation.

## One-line Summary
本文通过一组半通用三维离散裂隙网络（DFN）模拟，分析网络密度如何影响优先流路径（流道）的形成，并引入基于图论的流道量化方法，发现网络尺度流道化程度随密度增大而降低，但在低密度连通网络中流动反而更均匀。

## Research Question
如何量化裂隙网络中的流动通道化（flow channeling）程度？网络密度（network density）如何影响优先流路径的形成和传输行为？——本研究旨在“孤立网络密度这一最大尺度对优先流形成的影响”并提供“定量测量流道化程度的方法”[Hyman 2020, pp. 2-3]。

## Study Area / Data
- **网络类型**：半通用（semigeneric）三维离散裂隙网络（DFN），不针对特定场地，但参数借鉴野外观察[Hyman 2020, pp. 2-3]。
- **生成参数**：立方域边长 $L=50\,\text{m}$，断裂为平面圆盘，半径 $r$ 服从截断幂律分布，指数 $\alpha=1.8$，下限 $r_0=1\,\text{m}$，上限 $r_u=10\,\text{m}$。方向从 Fisher 分布采样（集中度参数 $\kappa \approx 0$，均值法向量 $(0,0,1)$），产生无序网络。裂隙中心服从均匀泊松过程[Hyman 2020, pp. 3-4]。
- **密度设计**：采用无量纲密度 $p' = p/p_c$，临界密度 $p_c \approx 750$ 条裂隙。取 $p' = 2, 3, 5, 10$，每个密度生成 10 个网络，共 40 个网络。仅保留连接入流与出流边界的连通子网络进行分析[Hyman 2020, pp. 4-4]。
- **水力特性**：水力开度与半径正相关 $b = 5.0 \times 10^{-4} \sqrt{r}$（基于现场数据），裂隙内开度恒定，不考虑内部粗糙度[Hyman 2020, pp. 3-4]。

## Methods
- **模拟平台**：使用 dfnWorks 套件（FRAM 生成网络、LaGriT 网格化、pflotran 求解流动、walkabout 粒子追踪）[Hyman 2020, pp. 3-3]。
- **流动模拟**：稳态雷诺方程 $\nabla \cdot (b^3 \nabla P) = 0$，沿 $x$ 轴施加 $1\,\text{kPa}$ 压差，基质不渗透，无基质扩散。用非结构化有限体积法求解，并重构欧拉速度场 $\mathbf{u}(\mathbf{x})$[Hyman 2020, pp. 4-6]。
- **传输模拟**：被动示踪粒子，入口平面通量加权注入 $10^5$ 个粒子，纯对流，交点混合采用完全混合模型[Hyman 2020, pp. 6-6]。
- **结构表征**：
  - **拓扑观测量**：节点度分布均值 $\mu(d)$ 与方差 $\sigma(d)$、Pearson 配类系数 $P$、图节点连通性 $n_c$、香农熵 $H$（基于度中心性）[Hyman 2020, pp. 6-6]。
  - **几何观测量**：裂隙强度 $P_{32}$ 与连通子网 $cP_{32}$、连通裂隙半径分布、裂隙面交线间距分布[Hyman 2020, pp. 6-7]。
- **流道量化方法**：
  - **欧拉方法**：流动通道密度指示器 $d_Q = \frac{1}{V} \cdot \frac{(\sum_f S_f |Q_f|)^2}{\sum_f S_f Q_f^2}$，以及活跃表面积比 $d_Q/P_{32}$ 和 $d_Q/cP_{32}$[Hyman 2020, pp. 7-7]。
  - **拉格朗日方法**：
    - 粒子参与比 $\pi$（基于通过每条裂隙的粒子数）[Hyman 2020, pp. 7-8]。
    - 流拓扑图（flow topology graph）及 $k$ 最短路径集成流率 $\pi_k = n \left( \sum_{\{i,j\}\in p_k} \frac{1}{\pi_{i,j}} \right)^{-1}$，用于构建流径重要性等级[Hyman 2020, pp. 8-8]。
    - 粒子迂曲度 $\chi = \lambda(x_L,\mathbf{a})/x_L$ 和突破曲线（BTC）$\psi(t,x_L)$[Hyman 2020, pp. 7-7]。

## Key Findings
1. **连通性随密度增强**：$p'=2$ 时仅约 4% 的裂隙参与连通网络，$p'=10$ 时达 54%（表 1）。节点连通性 $n_c$ 从 1（所有流须经过同一裂隙）增至 29.6，香农熵单调上升[Hyman 2020, pp. 8-9]。
2. **连通网络裂隙分布偏差**：相比预设分布，连通网络更倾向保留大裂隙、移除小裂隙；随密度增加偏差减小（图 2 左）。交线间距随密度增大而变短（图 2 右）[Hyman 2020, pp. 9-10]。
3. **流道化程度与密度的非单调关系**：
   - 全生成网络中，$d_Q/P_{32}$ 与粒子参与比 $\pi$ 随密度单调增加，即流道化减弱（表 2）[Hyman 2020, pp. 10-10]。
   - **连通网络内部**：$p'=2$ 时 $d_Q/cP_{32} \approx 0.65$、$\hat{\pi} \approx 0.24$；$p'=5$ 时降至约 0.43 和 0.11，$p'=10$ 回升至 0.60 和 0.11（表 2）。低密度网络中流动因结构强制而更均匀，高密度网络中流道位置由连通性、几何和水力特性共同决定，活跃面积占比反而下降[Hyman 2020, pp. 15-15]。
4. **路径重要性等级**：集成流率 $\pi_k$ 随 $k$ 衰减：$p'=2$ 急剧下降（单一主通道），$p'=10$ 缓慢下降（多条路径流率相近），表明流道化程度随密度升高而降低（图 4）[Hyman 2020, pp. 12-13]。
5. **传输特征**：
   - **迂曲度**：低密度网络受结构约束，各实现迂曲度分布差异大；高密度实现间行为一致（图 5）[Hyman 2020, pp. 13-13]。
   - **突破曲线**：低密度曲线峰值窄而高，高密度疏散、峰值变宽（图 6）。所有密度的拖尾均呈幂律衰减 $\psi(\tau)\propto \tau^{-\alpha}$，$p'=2,3,5$ 的 $\alpha\approx 2.7$，$p'=10$ 的 $\alpha\approx 3.1$[Hyman 2020, pp. 13-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 低密度（$p'=2$）网络中仅约 4% 裂隙形成连通网络，节点连通性 $n_c=1$ | [Hyman 2020, pp. 8-9], Table 1 | 截断幂律半径分布，$p_c\approx 750$，10 个实现 | 结构强制所有流动通过单一裂隙 |
| 连通网络中 $d_Q/cP_{32}$ 在 $p'=2$ 最高（0.65），$p'=5$ 最低（0.43），$p'=10$ 回升至 0.60 | [Hyman 2020, pp. 10-12], Table 2 | 稳态流，1kPa 压差，孔径-半径相关 | 低密度下流动虽仅限连通区但分布较均匀 |
| 集成流率 $\pi_k$ 衰减率：$p'=2$ 急剧下降，$p'=10$ 平缓下降 | [Hyman 2020, pp. 12-13], Fig. 4 | $k$ 最短路径基于粒子数倒数权重 | 量化了流径等级差异 |
| 突破曲线拖尾幂律指数：$p'=2,3,5$ 约 2.7，$p'=10$ 约 3.1 | [Hyman 2020, pp. 13-14], Fig. 6 | 时间无量纲化于各密度集的首达时间 | 流道化影响粒子对速度场的采样 |

## Limitations
- **模型假设简化**：仅考虑裂隙内均匀开度，未含内部粗糙度引起的次裂隙尺度流道；基质完全不渗透且无扩散[Hyman 2020, pp. 3-4]。
- **网络生成方式单一**：仅使用泊松式（Poissonian）DFN，未考虑成核生长等其他生成机制，这些机制可能改变拓扑和流道特征[Hyman 2020, pp. 16-16]。
- **参数固定**：仅改变裂隙数量，其余参数（幂律指数、方向分布、孔径-半径关系等）固定，未系统探讨其他长度尺度（如孔径变异）的相对影响[Hyman 2020, pp. 16-17]。
- **未经验证**：结果仅基于数值模拟，未与现场示踪试验直接对比[Hyman 2020, pp. 2-2]。

## Assumptions / Conditions
- 裂隙为平面圆盘，中心均匀分布，半径服从截断幂律（$\alpha=1.8$，$r\in[1,10]\,\text{m}$），方向均匀覆盖球面（Fisher $\kappa\approx0$）[Hyman 2020, pp. 3-4]。
- 水力开度 $b$ 仅与半径相关且在单条裂隙内恒定，相关关系 $b=5.0\times10^{-4}\sqrt{r}$[Hyman 2020, pp. 3-4]。
- 流动为稳态层流，满足雷诺方程；传输为纯对流，粒子被动，无基质扩散，交点混合采用完全混合模型[Hyman 2020, pp. 4-6]。
- 入口粒子通量加权注入，总粒子数 $10^5$ 已收敛[Hyman 2020, pp. 4-6]。
- 流动场由 1kPa 沿 x 轴压差驱动，其余边界无流[Hyman 2020, pp. 4-6]。
- 仅分析连接入、出流边界的连通子网络，移除孤立簇[Hyman 2020, pp. 4-4]。

## Key Variables / Parameters
- **密度**：无量纲密度 $p'=p/p_c$，$p_c\approx750$ 按截断三阶矩定义[Hyman 2020, pp. 3-4]。
- **网络结构**：裂隙总数 $N$，连通裂隙数 $\hat{N}$，百分比 $\%$；节点度均值 $\mu(d)$ 与方差 $\sigma(d)$、配类系数 $P$、节点连通性 $n_c$、香农熵 $H$[Hyman 2020, pp. 6-6]。
- **几何**：$P_{32}$（生成网络裂隙强度），$cP_{32}$（连通网络裂隙强度），交线距离分布[Hyman 2020, pp. 6-7]。
- **流道化指标**：$d_Q$、$d_Q/P_{32}$、$d_Q/cP_{32}$；粒子参与比 $\pi$（全网络）与 $\hat{\pi}$（连通网络）；集成流率 $\pi_k$[Hyman 2020, pp. 7-8]。
- **传输**：粒子迂曲度 $\chi$、突破曲线 $\psi(t,x_L)$、拖尾幂律指数 $\alpha$[Hyman 2020, pp. 7-7,13-14]。

## Reusable Claims
- **Claim 1**：在基于泊松过程、截断幂律半径分布的三维 DFN 中，网络密度 $p'$ 由低于临界值 2 倍增至 10 倍时，全网络尺度的流道化程度（以 $d_Q/P_{32}$ 或 $\pi$ 衡量）单调降低[Hyman 2020, pp. 10-10]。**条件**：须满足稳态流、孔径-半径正相关、方向均匀等假设。
- **Claim 2**：低密度（如 $p'=2$）连通网络内部，流动因结构强制而比中高密度网络更均匀（$d_Q/cP_{32}$ 更高），但整个生成网络中流动集中于少数连通裂隙[Hyman 2020, pp. 15-15]。**限制**：此均匀性特指连通子网，不适用于全网络。
- **Claim 3**：通过流拓扑图的 $k$ 最短路径集成流率 $\pi_k$ 的衰减速率可量化流道化程度：衰减越快，流道化越强[Hyman 2020, pp. 12-13]。**适用**：需先完成粒子追踪，且网络具有图表示。
- **Claim 4**：网络密度影响突破曲线形态：低密度下峰值窄、分散小，高密度下峰值宽、分散大；所有密度均呈现幂律拖尾，但衰减指数在最高密度（$p'=10$）略大（~3.1 vs ~2.7）[Hyman 2020, pp. 13-14]。**条件**：纯对流、无基质扩散。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[flow channeling / preferential flow path]]
- [[percolation parameter]]
- [[network density]]
- [[graph representation of fracture networks]]
- [[flow topology graph]]
- [[Eulerian and Lagrangian observables]]
- [[particle participation ratio]]
- [[k-shortest paths flow hierarchy]]
- [[tortuosity distribution]]
- [[breakthrough curve]]
- [[power-law tail of travel times]]

## Candidate Methods
- [[dfnWorks simulation suite]]
- [[FRAM meshing for discrete fracture networks]]
- [[steady-state Reynolds equation solver]]
- [[particle tracking in DFN]]
- [[graph-based topological characterization (degree, assortativity, node connectivity, Shannon entropy)]]
- [[flow channeling density indicator (d_Q)]]
- [[flow topology graph construction and weighting]]
- [[integrated flow rate from k-shortest paths (π_k)]]
- [[flux-weighted particle injection]]

## Connections To Other Work
- 与 **Sherman et al. (2020)** 相关：他们研究了密度对传输的影响，但未系统联系结构属性与流道形成或提出新的流道比较方法[Hyman 2020, pp. 1-2]。
- 流道化概念和测量继承自 **Maillot et al. (2016)** 的参与比 $d_Q$ 及固体物理中的参与比思想[Hyman 2020, pp. 7-7]。
- 图论表征方法借鉴 **Huseby et al. (1997)**、**Hyman et al. (2017, 2018)** 等[Hyman 2020, pp. 6-6]。
- 关于非菲克传输模型（CTRW, fADE）的适用性讨论，见于 **Berkowitz et al. (2006)**、**Neuman & Tartakovsky (2009)** 等，本文指出稀疏网络中使用这些模型需额外信息[Hyman 2020, pp. 16-16]。

## Open Questions
- 其他 DFN 生成机制（如成核生长模型）如何影响流道化？[Hyman 2020, pp. 16-16]
- 次尺度（裂隙内粗糙度）与网络尺度的交互如何改变优先流路径的形成和等级？[Hyman 2020, pp. 16-16]
- 能否对影响流道化的地球物理因素进行影响排序？[Hyman 2020, pp. 16-16]
- 在更高密度网络中，连续介质模型或非菲克模型（CTRW/fADE）的适用边界如何更精确地界定？[Hyman 2020, pp. 16-16]
- 流道化如何影响地球化学反应反馈与非均质结构演化？[Hyman 2020, pp. 16-17]

## Source Coverage
已处理全部 22 个非空索引片段。总索引字符数 107,399，编译字符数 107,885，片段覆盖比（按区块）1.0，字符覆盖比 1.004525。源签名：9fe6c079728e3a9e3b2aab292675caeb81c894ae。处理策略：single-pass-markdown。
