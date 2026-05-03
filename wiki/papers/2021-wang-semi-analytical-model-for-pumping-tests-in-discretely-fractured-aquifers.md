---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-wang-semi-analytical-model-for-pumping-tests-in-discretely-fractured-aquifers"
title: "Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers."
status: "draft"
source_pdf: "data/papers/2021 - Semi-analytical model for pumping tests in discretely fractured aquifers.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Wang, Lei, et al. \"Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers.\" *Journal of Hydrology*, vol. 593, 2021, p. 125737. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72524"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "68535"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.944998"
coverage_status: "full-index"
source_signature: "63966f85df6ceab8464c1eb1e7b5eaef5abf83e1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:45:07"
---

# Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers.

## One-line Summary
提出一种新颖的半解析模型，用于研究含多条随机分布、有限导水能力裂隙的离散裂隙承压含水层中抽水试验的井筒降深瞬态行为，模型仅需对裂隙分段，通过拉普拉斯空间耦合条件建立矩阵并用高斯消去法求解，结果表明降深导数曲线上的“谷”数目不仅与介质类型有关，更与裂隙密度、导水能力、长度、方位、分布及井位密切相关[Wang 2021, pp. 1-1][Wang 2021, pp. 13-14]。

## Research Question
如何构建一个能考虑任意分布、任意相交、有限导水能力裂隙的离散裂隙网络抽水试验半解析模型，以精确模拟井筒降深瞬态响应，并定量揭示裂隙参数（密度、长度、导水能力、方位、分布）以及抽水井位置对降深及降深导数曲线形态（尤其是“谷”的数目与特征）的影响[Wang 2021, pp. 1-1][Wang 2021, pp. 13-14]？

## Study Area / Data
本文未涉及具体野外试验数据，为理论模型研究。模型通过与前人解析解（Cinco‑Ley and Meng, 1988 有限导水垂直裂缝井；Gringarten et al., 1974 无限导水垂直裂缝井）对比验证[Wang 2021, pp. 9-9]。分析案例均为合成裂隙网络，包括平行不相交裂隙、随机方位不相交裂隙、相交裂隙网络，并设置不同井位与裂隙参数工况[Wang 2021, pp. 10-13]。

## Methods
### 基本假设
模型假设固定如下[Wang 2021, pp. 1-2][Wang 2021, pp. 2-3]：
(1) 承压含水层无限水平、等厚，水力传导系数 \(K_m\) 与储水系数 \(S_{sm}\) 处处均一，顶底板隔水。
(2) 抽水过程中忽略温度变化。
(3) 各井以恒定流量 \(Q\) 抽水，可与裂隙相交或不交。
(4) 含水层中发生二维达西渗流；抽水井半径为 \(r_w\)。
(5) 裂隙宽度远小于长度，裂隙内为一维流。
(6) 离散裂隙系统含 \(N_f\) 条裂隙，每条裂隙长度 \(L_{fn}\)、水力传导系数 \(K_{fn}\)、宽度 \(w_{fn}\)、与 x 轴夹角 \(\theta_n\)、起点坐标 \((x_{ofn}, y_{ofn})\) 已知。

### 含水层模型
含水层中水头（降深）控制方程包含井源汇项和裂隙源汇项；通过傅里叶与拉普拉斯变换得到拉普拉斯空间中的降深解析解表达式（6.1）–（6.4）[Wang 2021, pp. 3-5]。该解利用格林函数形式将任一点降深表示为井流量和各裂隙表面流量沿裂隙长度上的积分。

### 离散裂隙模型
将裂隙系统分为单节点模型（一端封闭）和双节点模型（两端有节点）[Wang 2021, pp. 5-6]。忽略裂隙储水能力，认为裂隙内流动瞬时达拟稳态，建立一维降深方程（8）；在裂隙壁应用流量等效条件（11），将裂隙流与含水层流耦合。对方程进行无量纲化与拉普拉斯变换，得到裂隙节点降深与裂隙段流量之间的关系（23）、（24）[Wang 2021, pp. 6-7]。

### 耦合与半解析求解
将裂隙表面离散为 \(2N_{fn}\) 段，形成包含裂隙表面流量、节点流量、节点降深的未知向量（27）。利用裂隙表面处含水层降深与裂隙降深连续性条件（28）、节点质量守恒方程（29）以及裂隙段流量与节点流量关系（30）–（32），建立拉普拉斯空间中的线性方程组，方程总数与未知数相等[Wang 2021, pp. 7-9]。采用高斯消去法求解，再将解代入（7‑1）求得任意位置降深（包括井筒降深），最后通过 Stehfest 数值拉普拉斯反演算法得到实域降深[Wang 2021, pp. 8-9]。该方法仅需对裂隙分段，无需网格化整个含水层。

## Key Findings
(1) 本模型与 Cinco‑Ley and Meng (1988) 的单条有限导水裂缝井解吻合良好，且模型更通用[Wang 2021, pp. 9-9]。
(2) 对一条裂缝附近的抽水井，降深导数曲线呈现早期径向流、中间过渡流（出现一个“谷”）、晚期拟径向流三个阶段；裂缝距离越短、长度越长、导水能力越高，“谷”越深且出现时间越早；井靠近裂缝端点时降深损失最大[Wang 2021, pp. 9-10]。
(3) 裂缝数目增加会导致新的“谷”出现，且头损失随裂缝数增加而增大[Wang 2021, pp. 10-11]。
(4) 在平行不相交裂缝网络中，井位靠近长裂缝且位于网络中心时“谷”开口大、持续时间长，三“谷”出现；井靠近短裂缝则出现单“谷”；远离裂缝时“谷”浅且短[Wang 2021, pp. 11-12]。
(5) 在随机方位不相交裂缝网络中，长裂缝附近的井头损失最小，降深导数形态强烈依赖井位，可出现一或两个“谷”[Wang 2021, pp. 12-13]。
(6) 在相交裂缝网络中，井与连通裂缝网络相交时头损失最小，降深导数无“谷”；井靠近或相交孤立裂缝时，出现一或两个“谷”[Wang 2021, pp. 13-14]。
(7) “谷”的数目主要受裂缝密度、长度、导水能力、分布以及井位控制，与传统双重介质模型仅取决于储水系数和窜流系数的结论截然不同[Wang 2021, pp. 13-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 模型与 Cinco‑Ley & Meng (1988) 的解在有限导水裂缝井工况下一致（\(C_{fD}=5,15,60,300\)，\(L_{fD}=2\)，井位于裂缝中心） | [Wang 2021, pp. 9-9] | 单条裂缝，井穿过裂缝，恒定流量抽水，承压无限含水层 | 模型适用范围更广，可处理非相交、相交网络 |
| 井靠近单条裂缝时，降深导数出现一个“谷”，其深度和出现时间随裂缝距离、长度、导水能力变化 | [Wang 2021, pp. 9-10] | \(D=0.03,0.05,0.1\)；\(L_{fD}=0.5,2,4\)；\(C_{fD}=2,20,300\)；井在裂缝附近 | 早期径向流段、过渡段、晚期拟径向流段清晰 |
| 裂缝数量增加引入新的“谷”，如四条裂缝时出现第二个“谷”于 \(t_D\approx0.3\) | [Wang 2021, pp. 10-11] | 四条平行裂缝顺序远离井 | 第一条裂缝主要控制第一“谷” |
| 在平行不相交裂缝网络中，井靠近长裂缝且位于网络中心时，降深导数显示三个“谷” | [Wang 2021, pp. 11-12] | 27条裂缝平行分布，井位坐标 \((0.4,0.84)\) | “谷”的形状受周围不同长度裂缝共同作用 |
| 在相交裂缝网络中，井与连通裂缝网络相交时，降深导数无“谷”；井靠近孤立裂缝时出现两个“谷” | [Wang 2021, pp. 13-14] | 16条相交裂缝+4条孤立裂缝，井位 \(( -1.06,3.15)\) 等 | 相交井头损失最小 |

## Limitations
- 仅适用于二维、均质、等厚、无限水平承压含水层，未考虑非均质性、各向异性或边界影响[Wang 2021, pp. 2-3]。
- 裂隙内假定为拟稳态流（忽略裂隙储水），因此极早期（裂隙储集效应显著时段）的响应未考虑；文献指出该偏差在很短时间内消失[Wang 2021, pp. 5-6]。
- 含水层与裂隙间的交换采用流量等效条件，未考虑裂隙壁的额外表皮效应。
- 模型为线性达西流，未涉及非达西流或裂隙开度变化。
- 数值实现采用均匀分段，裂隙端部的网格加密效果未讨论。
- 仅针对单相水流，未考虑溶质运移、多相流或温度变化[Wang 2021, pp. 2-3]。

## Assumptions / Conditions
1. 承压含水层无限延伸，水平，均质，厚度 \(b\)、渗透系数 \(K_m\)、贮水率 \(S_{sm}\) 恒定，顶底边界封闭[Wang 2021, pp. 2-3]。
2. 抽水过程中温度不变[Wang 2021, pp. 2-3]。
3. 井以恒定流量 \(Q\) 工作，可与裂隙相交或不交[Wang 2021, pp. 2-3]。
4. 含水层中为二维达西流，井半径为 \(r_w\)[Wang 2021, pp. 2-3]。
5. 裂隙宽度远小于长度，裂隙内为沿长度方向的一维流[Wang 2021, pp. 2-3]。
6. 裂隙参数（长度、导水能力、方位、位置）给定，且每条裂隙用宽度、起点坐标、与 x 轴夹角描述[Wang 2021, pp. 2-3]。
7. 裂隙内流动拟稳态，忽略裂隙储水能力（瞬时响应假定）[Wang 2021, pp. 5-6]。
8. 裂隙壁两侧流量与含水层水力梯度满足等效条件[Wang 2021, pp. 5-6]。
9. 节点处遵循质量守恒（无井时总流量为零；有井时等于井流量）[Wang 2021, pp. 7-8]。
10. 所有推导在拉普拉斯空间进行，最终通过 Stehfest 数值反演获得实域解[Wang 2021, pp. 8-9]。

## Key Variables / Parameters
- 含水层参数：\(T_m = K_m b\) (承压含水层导水系数)，\(S_m = S_{sm} b\) (储水系数)，\(s_m\) (降深)。
- 裂隙参数：\(L_{fn}\) (单条裂缝长度)，\(K_{fn}\) (裂缝渗透系数)，\(w_{fn}\) (裂缝宽度)，\(\theta_{fn}\) (裂缝与 x 轴夹角)，\(C_{fDn}=K_{fn} w_n / (K_m L_r)\) (无量纲裂缝导水能力)，\(L_{fDn}=L_{fn}/L_r\) (无量纲长度)。
- 井参数：\(Q\) (抽水流量)，\(Q_{r}\) (参考流量)，\(L_r\) (参考长度)，\(r_{wD}\) (无量纲井半径，文中取 0.001)，井位置 \((x_w, y_w)\) 或无量纲 \((x_{wD}, y_{wD})\)。
- 无量纲量：\(s_{mD} = 4\pi T_m s_m / Q_r\) (含水层无量纲降深)，\(t_D = T_m t / (S_m L_r^2)\) (无量纲时间)，\(q_{fDn,1}, q_{fDn,2}\) (裂隙表面无量纲流量)，\(\tilde{Q}_{fDwi}\) (节点无量纲流量)，\(\tilde{s}_{fDwi}\) (节点无量纲降深)。
- 拉普拉斯空间参数：\(p\) (拉普拉斯变换时间变量)，上标 \(\tilde{}\) 表示拉普拉斯量。
- 离散参数：\(N_f\) (裂缝总数)，\(N_{fn}\) (每条裂缝单表面分段数)，\(\Delta x_{fDn}\) (无量纲段长)。

## Reusable Claims
- 在有限导水离散裂隙承压含水层中，抽水井若与连通裂缝网络相交，井筒降深损失最小，降深导数不出现“谷”；若井位于富裂缝基质中但不与裂缝相交，则会出现浅“谷”[Wang 2021, pp. 13-14]。**条件**：符合前述基本假设，恒定流量抽水。**局限**：二维、拟稳态裂隙流、均质基质。
- 单条裂缝附近的抽水井，降深导数曲线上的“谷”深度随裂缝距离减小、裂缝长度增加、裂缝导水能力增大而加深；但导水能力超过某一阈值后，降深损失变化可忽略[Wang 2021, pp. 9-10]。**条件**：单一有限导水裂缝，井未穿过裂缝。**局限**：仅限于拟稳态裂隙流，未考虑裂隙储集效应。
- 离散裂隙网络中降深导数曲线上的“谷”数目由裂缝密度、裂缝长度、导水能力、裂缝分布以及井与裂缝的相对位置共同决定，与传统的 Warren‑Root 双重介质模型中仅由储水系数和窜流系数控制的结论形成对比[Wang 2021, pp. 13-14]。**条件**：离散承压含水层，恒定流量抽水。**局限**：取决于模型假设。
- 所提出的半解析方法只需对裂隙分段，无需对全区域网格化，即可求解复杂相交/非相交裂隙网络中的井筒降深，且通过拉普拉斯空间高斯消去法和 Stehfest 反演实现高效计算[Wang 2021, pp. 1-2][Wang 2021, pp. 8-9]。**条件**：上述基本假设成立。**局限**：当裂缝数量极大时，矩阵规模可能显著增大；数值反演的精度受 Stehfest 算法参数影响。

## Candidate Concepts
- [[discrete fracture network]]
- [[semi-analytical model]]
- [[pumping test]]
- [[drawdown derivative curve]]
- [[Laplace domain solution]]
- [[pseudo-steady state flow]]
- [[finite conductivity fracture]]
- [[fracture network intersection]]
- [[wellbore drawdown]]
- [[double porosity model]]
- [[mass balance at nodes]]
- [[type curve analysis]]
- [[extended well model]]

## Candidate Methods
- [[Laplace transform]]
- [[Fourier transform]]
- [[Gaussian elimination]]
- [[Stehfest numerical inversion]]
- [[source-sink method]]
- [[fracture discretization]]
- [[Green’s function]]
- [[continuity condition at fracture wall]]
- [[flux equivalence principle]]

## Connections To Other Work
- 与 Warren & Root (1963) 的双重孔隙度模型比较：传统模型降深导数形态仅取决于储水系数和窜流系数，本研究指出在离散裂缝网络中“谷”的数目和形状与裂缝几何及井位密切相关，补充并超越双重介质框架[Wang 2021, pp. 1-1][Wang 2021, pp. 13-14]。
- 与 Cinco‑Ley & Meng (1988) 的有限导水垂直裂缝井解对比：本研究模型在单缝相交情况下与该解一致，且可推广至多缝、非相交及相交网络[Wang 2021, pp. 9-9]。
- 与 Gringarten et al. (1974) 的无限导水裂缝解对比：当设定为无限导水且井穿过裂缝时，降深曲线完全吻合；但本研究可计算井与裂缝分离工况，并考虑有限导水能力[Wang 2021, pp. 9-9]。
- 与 Chen et al. (2016) 的多裂缝水平井半解析模型关联：Chen 等通过人工判断流向处理裂缝相交，本研究采用节点质量守恒实现自动流量重分配，简化了相交流计算[Wang 2021, pp. 8-8]。
- 引用前人双重介质模型（Kazemi, 1969; Moench, 1984; Hamm & Bidaux, 1996; Lods & Gouze, 2004 等）以及离散裂缝数值模拟（Olorode et al., 2013; Xu et al., 2017）作为研究背景与对比基准[Wang 2021, pp. 1-2]。

## Open Questions
None specified in the fragments. Potential extensions could include unsteady fracture flow (fracture storage), three-dimensional effects, fracture skin, non‑Darcy flow, or heterogeneous matrix, but these are not discussed in the paper.

## Source Coverage
All 15 non‑empty indexed fragments were processed. Total indexed characters: 72,524; compiled source characters: 68,535; coverage ratio by characters: 0.944998. Source signature: 63966f85df6ceab8464c1eb1e7b5eaef5abf83e1. The compilation is based exclusively on the supplied fragments, with no interpolation of authors, pages, data, or conclusions beyond the indexed text.
