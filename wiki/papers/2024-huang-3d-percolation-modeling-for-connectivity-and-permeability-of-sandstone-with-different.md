---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-huang-3d-percolation-modeling-for-connectivity-and-permeability-of-sandstone-with-different"
title: "3D Percolation Modeling for Connectivity and Permeability of Sandstone with Different Pore Distribution Characteristics."
status: "draft"
source_pdf: "data/papers/2024 - 3D Percolation Modeling for Connectivity and Permeability of Sandstone with Different Pore Distribution Characteristics.pdf"
collections:
  - "论文"
citation: "Huang, Xudong, et al. \"3D Percolation Modeling for Connectivity and Permeability of Sandstone with Different Pore Distribution Characteristics.\" *Natural Resources Research*, vol. 33, no. 1, Feb. 2024, pp. 191-, https://doi.org/10.1007/s11053-023-10277-2."
indexed_texts: "13"
indexed_chars: "62122"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62337"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003461"
coverage_status: "full-index"
source_signature: "2814fa01915b6fea164d3cd49ec4132921f7b2bd"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:18:59"
---

# 3D Percolation Modeling for Connectivity and Permeability of Sandstone with Different Pore Distribution Characteristics.

## One-line Summary
提出一种引入粒子分布因子M和膨胀滤波器D的改进三维site percolation模型，用以生成具有不同孔隙分布特征的虚拟砂岩，并系统研究M、D和孔隙度(P)对渗透阈值、孔隙连通性和绝对渗透率的影响 [Huang 2024, pp. 1-2][Huang 2024, pp. 19-21].

## Research Question
如何通过数值方法准确确定具有不同颗粒尺寸和类型的砂岩储层的渗透阈值、孔隙连通性和渗透率的变化规律，以克服经典site percolation模型（渗透阈值31.16%）不适用于自然多孔材料的问题 [Huang 2024, pp. 2-3][Huang 2024, pp. 19-21].

## Study Area / Data
- 真实砂岩CT数字岩心：三块孔隙分布特征明显不同的砂岩CT数字岩心，包括致密砂岩（低P、弱连通性）和P分别为17.5%、25.3%的砂岩 [Huang 2024, pp. 5-6]。
- 虚拟砂岩模型尺寸：L = 120, 140, 160, 180, 200体素；对于渗透率计算，假设模型边长1000 μm（体素尺寸5 μm³） [Huang 2024, pp. 6-10][Huang 2024, pp. 17-19]。
- 数值模拟量：在不同M（1, 2, 5, 10, 20, 30, 40）、D（1, 3, 5, 7）和L组合下进行了14,000组数值模拟 [Huang 2024, pp. 6-10]。
- 渗透率计算流体参数：流体为液态水，粘度0.001 Pa·s；入口压力1.5 MPa，出口压力0.1 MPa [Huang 2024, pp. 17-19]。

## Methods
- 三维虚拟砂岩生成方法：在site percolation模型中引入粒子分布因子M和球形膨胀滤波器D。M控制每次生成固体颗粒的初始大小和形状随机性；M越大，颗粒越大、形状越复杂。膨胀滤波器算法在改变孔隙度(P)的同时赋予孔隙-喉道结构可接受的变形 [Huang 2024, pp. 1-2][Huang 2024, pp. 3-5]。
- 具体生成步骤：在扩展的三维数组Y中通过Monte Carlo随机赋值固体体素（体积分数f），删除体积不等于M的颗粒；截取中央数组Z并控制其固体体积百分比≤0.5%；通过“0+0=0, 0+1=1, 1+1=1”规则合并Z和X，持续迭代填充直至P低于2% [Huang 2024, pp. 3-5]。
- 渗透阈值确定：基于有限尺度标度理论(FSS)，利用修正双曲正切函数拟合不同L下的渗透概率曲线R_X^L(P)，求取P_c(L)和过渡宽度Δ(L)；通过线性拟合P_c(L)－Δ(L)关系，外推得到无限尺度下的渗透阈值P_c [Huang 2024, pp. 5-6][Huang 2024, pp. 6-10]。
- 渗透率计算：基于“孔隙-喉道-孔隙”网络模型（球棍模型），使用Poiseuille定律和Darcy定律，仅考虑贯穿整个介质沿流动方向的连通孔喉网络贡献的绝对渗透率 [Huang 2024, pp. 15-17][Huang 2024, pp. 17-19]。

## Key Findings
- 渗透阈值(P_c)随M和D增大而降低。实例：当(M, D)从(1,1)增至(40,7)时，P_c从22.53%降至4.94%；当D≥3时，无论M如何，P_c均低于10% [Huang 2024, pp. 6-10][Huang 2024, pp. 19-21]。
- 随着M增大，P_c的下降趋势变缓。例如D=1时，M从1增至10，P_c下降0.0857；M从10增至40，P_c仅下降0.0078 [Huang 2024, pp. 10-13]。
- 相同P下，孔隙连通性随M和D增大而增强。M和D越大，虚拟砂岩中孔喉数量越少、单一孔喉尺寸越大，促进孔隙簇聚结和连通 [Huang 2024, pp. 13-15][Huang 2024, pp. 15-17][Huang 2024, pp. 19-21]。
- 有效孔隙度(EP)随P演化在接近P_c时快速增大。M与EP呈正相关 [Huang 2024, pp. 13-15]。
- 绝对渗透率(k)对颗粒尺寸敏感，随M和D增大而增加。相同P和M下，D=7时的渗透率通常是D=1时的4倍以上 [Huang 2024, pp. 17-19][Huang 2024, pp. 19-21]。
- 与真实砂岩对比：当P<19%时，真实砂岩渗透率分布在虚拟砂岩(M, D)=(40,7)的范围内；当P>19%时，真实砂岩渗透率高于任何(M, D)组合下的虚拟砂岩，可能与体素尺寸不匹配有关 [Huang 2024, pp. 17-19]。
- 仅依据孔隙度预测砂岩渗透率会产生较大误差 [Huang 2024, pp. 19-21]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 虚拟砂岩可通过改变M和D的组合重建，与真实砂岩在P、迂曲度、配位数上高度相似 | [Huang 2024, pp. 5-6] | 对比真实砂岩CT数字岩心与虚拟砂岩 | 图5展示了致密砂岩和P=17.5%、25.3%砂岩的对比 |
| 渗透阈值 P_c 随M和D增大而下降：(M,D)=(1,1)时P_c=0.2253；(M,D)=(40,7)时P_c=0.0494 | [Huang 2024, pp. 10-13] | Table 1数据；14,000组模拟 | 误差范围由max(|P^I_c(∞)-P^A_c(∞)|,|P^U_c(∞)-P^A_c(∞)|)确定 |
| D≥3时，无论M取值，渗透阈值均低于10% | [Huang 2024, pp. 19-21] | 全部Virtual sandstone组合 | 暗示天然砂岩渗透阈值通常低于10%甚至5% |
| 相同P下，增大M和D会减少孔喉数量、增大单孔喉尺寸、增强连通性 | [Huang 2024, pp. 13-15][Huang 2024, pp. 15-17] | 代表性结果：M=2和10；D=1,3,5,7 | 图9和图11提供支持 |
| 绝对渗透率对颗粒尺寸敏感：相同P和M下，D=7时k可达D=1时的4倍以上 | [Huang 2024, pp. 17-19] | Table 2数据 | 实例：P=0.10, M=10 时 k(D=7)=515.99 mD，k(D=1)=0 mD |
| 真实砂岩渗透率在P>19%时超出虚拟砂岩预测范围，可能因体素尺寸不匹配 | [Huang 2024, pp. 17-19][Huang 2024, pp. 19-21] | 与Revil et al. (2014)和Payton et al. (2022)的真实砂岩对比 | 图14展示 |
| M增大时P_c下降趋势减缓：D=1时M从1到10 P_c下降0.0857，M从10到40仅下降0.0078 | [Huang 2024, pp. 10-13][Huang 2024, pp. 13-15] | D=1 时 M=1,10,40 数据点 | 归因于固体颗粒增大导致孔隙空间整合，但效应饱和 |

## Limitations
- 虚拟砂岩的体素尺寸（5 μm³）可能在高孔隙度条件下与真实砂岩不匹配，导致渗透率被低估 [Huang 2024, pp. 19-21]。需要进一步研究确定不同孔隙度下虚拟砂岩的合适体素尺寸 [Huang 2024, pp. 19-21]。
- 渗透率计算假设流体为不可压缩牛顿流体、层流，且流动不随时间变化 [Huang 2024, pp. 15-17]。
- 由于篇幅限制，仅展示了部分代表性结果进行孔隙连通性和孔喉结构分析 [Huang 2024, pp. 13-15][Huang 2024, pp. 15-17]。

## Assumptions / Conditions
- 三维阵列中值1代表固体基质，0代表孔隙空间 [Huang 2024, pp. 3-5]。
- 膨胀滤波器为球形 [Huang 2024, pp. 3-5]。
- 每轮生成中阵列Z的固体体积百分比≤0.5%以控制孔隙度变化速率，防止渗透阈值显著误差 [Huang 2024, pp. 3-5][Huang 2024, pp. 5-6]。
- 渗透阈值P_c采用有限尺度标度外推至无限尺度，基于关系式P_c(L)-P_c ∝ L^{-1/ν}和P_c(L)-P_c ∝ Δ(L) [Huang 2024, pp. 5-6][Huang 2024, pp. 6-10]。
- 孔隙连通性采用C大簇连通性定义：仅将最大孔隙簇视为连通孔隙 [Huang 2024, pp. 13-15]。
- 渗透率计算中的孔喉网络模型将孔隙视为球体，喉道视为细杆 [Huang 2024, pp. 15-17]。

## Key Variables / Parameters
- M：粒子分布因子，控制每次生成固体颗粒的初始大小和形状随机性 [Huang 2024, pp. 1-2][Huang 2024, pp. 3-5]。
- D：球形膨胀滤波器尺寸，控制颗粒最终尺寸并影响孔隙-喉道结构 [Huang 2024, pp. 1-2][Huang 2024, pp. 3-5]。
- P：孔隙度 [Huang 2024, pp. 1-2]；EP：有效孔隙度（最大孔隙簇体积占总介质体积比例） [Huang 2024, pp. 13-15]。
- Connectivity：连通性（最大孔隙簇体素/所有可渗透体素） [Huang 2024, pp. 13-15]。
- P_c(L)：有限尺度渗透阈值；P_c(∞)：无限尺度渗透阈值 [Huang 2024, pp. 5-6][Huang 2024, pp. 6-10]。
- k：绝对渗透率（mD），通过Poiseuille和Darcy定律计算 [Huang 2024, pp. 17-19]。
- L：模型边长（体素） [Huang 2024, pp. 3-5]。
- f：目标固体体积百分比；q_ij：孔隙间流量；g_ij：水力传导率；r_ij, l_ij：喉道半径和长度 [Huang 2024, pp. 3-5][Huang 2024, pp. 15-17]。

## Reusable Claims
- 天然砂岩的渗透阈值通常低于10%，在某些情况下甚至低于5%；只有当虚拟砂岩的膨胀滤波器D不小于3时，才能与真实砂岩的迂曲度、配位数等参数相匹配 [Huang 2024, pp. 19-21]。
- 经典简单立方site percolation模型的渗透阈值（31.16%）远高于实际砂岩（可低于4%），如本研究中(M,D)=(40,7)对应的P_c=4.94% [Huang 2024, pp. 2-3][Huang 2024, pp. 10-13]。
- 砂岩的渗透率受到固体颗粒尺寸的强烈控制；在相同孔隙度下，颗粒尺寸差异可导致渗透率相差4倍以上，因此仅凭孔隙度无法可靠预测渗透率 [Huang 2024, pp. 19-21]。
- 粒子分布因子M的效应存在饱和：当M增大到一定程度后，渗透阈值的进一步下降极为有限 [Huang 2024, pp. 13-15]。

## Candidate Concepts
- [[虚拟砂岩]]
- [[渗透阈值]]
- [[site percolation模型]]
- [[粒子分布因子M]]
- [[膨胀滤波器D]]
- [[有限尺度标度理论]]
- [[孔隙连通性]]
- [[C大簇连通性]]
- [[孔喉网络模型]]
- [[绝对渗透率]]
- [[Poiseuille定律]]
- [[三维CT数字岩心]]

## Candidate Methods
- [[基于改进site percolation的三维虚拟砂岩重构]]
- [[Monte Carlo随机赋值生成颗粒]]
- [[膨胀/收缩算法约束孔隙度变化]]
- [[利用修正双曲正切函数拟合渗透概率曲线]]
- [[基于FSS外推无限尺度渗透阈值]]
- [[基于孔喉网络模型和Poiseuille定律的绝对渗透率计算]]

## Connections To Other Work
- 经典 site percolation 模型的渗透阈值（31.16%）不适用于天然多孔材料；前人研究发现油页岩渗透阈值8%–12% (Kang et al. 2014)，砂岩渗透阈值可低至3.94% (Liu et al. 2021) [Huang 2024, pp. 2-3]。
- 膨胀/收缩算法此前已被广泛用于基于CT图像确定砂岩渗透阈值 (Liu & Regenauer-Lieb, 2021) [Huang 2024, pp. 3-5]。
- 与 Fontainebleau 砂岩的渗透率对比参照了 Revil et al. (2014) 和 Payton et al. (2022) 的数据 [Huang 2024, pp. 17-19][Huang 2024, pp. 19-21]。

## Open Questions
- 不同孔隙度下虚拟砂岩的合适体素尺寸如何确定，以消除高P条件下与真实砂岩的渗透率偏差 [Huang 2024, pp. 19-21]。
- 在当前提出的方法框架下，如何进一步改善对高孔隙度(>19%)砂岩渗透率的预测准确性 [Huang 2024, pp. 17-19]。
- M和D的物理意义与真实砂岩成岩作用（压实、胶结程度、填充物）之间的定量对应关系尚未明确 [Huang 2024, pp. 2-3]。

## Source Coverage
全部13个非空索引片段均已处理并用于本Wiki页面编译；覆盖率为1.0（按片段块数）或1.003（按字符数），实现了对该论文全文的完整索引覆盖 [Compile audit metadata].
