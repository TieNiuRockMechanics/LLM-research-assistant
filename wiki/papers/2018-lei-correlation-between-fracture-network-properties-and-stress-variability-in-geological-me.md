---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-lei-correlation-between-fracture-network-properties-and-stress-variability-in-geological-me"
title: "Correlation Between Fracture Network Properties and Stress Variability in Geological Media."
status: "draft"
source_pdf: "data/papers/2018 - Correlation Between Fracture Network Properties and Stress Variability in Geological Media.pdf"
collections:
citation: "Lei, Qinghua, and Ke Gao. “Correlation Between Fracture Network Properties and Stress Variability in Geological Media.” *Geophysical Research Letters*, 2018, doi:10.1002/2018GL077548."
indexed_texts: "10"
indexed_chars: "46811"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "47004"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004123"
coverage_status: "full-index"
source_signature: "5dfef909b462c35752293222b37441cfe5e8ed61"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:19:30"
---

# Correlation Between Fracture Network Properties and Stress Variability in Geological Media.

## One-line Summary
本文利用基于张量的数学框架，定量研究了在构造应力作用下裂隙网络几何特性（连通性、裂隙强度）与地质体应力场变异性之间的相关性。研究发现：局部应力扰动（用局部应力张量与平均应力张量的欧几里得距离度量）与局部裂隙强度呈正线性关系；当裂隙系统连通且处于临界摩擦滑动状态时，整体应力离散度（用有效方差度量）显著增强。

## Research Question
应力场是否与裂隙相关？若相关，如何相关？[*Lei & Gao, 2018, pp. 1-1*]

## Study Area / Data
- **合成裂隙网络**：基于幂律长度分布生成，域尺寸 \(L=10\)\ m，裂隙走向随机且各向同性，长度指数 \(a=1.5,\ 2.0,\ 2.5,\ 3.0,\ 3.5\)，平均裂隙强度 \(\bar{\gamma} = 2.5,\ 5.0\)\ m⁻¹，每种组合10个随机实现。
- **天然裂隙网络**：取自Hornelen盆地的露头图（Odling, 1997），通过旋转采样窗口（\(\theta=0^\circ,\ 36^\circ,\ 72^\circ,\ 108^\circ,\ 144^\circ\)）提取多个模式。分形参数：\(a=2.73,\ D=1.80\)，平均裂隙强度 \(4.05\)\ m⁻¹，局部强度方差 \(7.93\)\ m⁻²，渗流参数 \(p=5.60\)。
- **构造应力条件**：主应力正交加载，有效应力情形：(i) \(S_{xx}^\infty = 5.0\)\ MPa, \(S_{yy}^\infty = 5.0\)\ MPa（比值为1.0）；(ii) 10.0\ MPa与5.0\ MPa（比值为2.0）；(iii) 15.0\ MPa与5.0\ MPa（比值为3.0）。
- **裂隙摩擦系数**：\(\mu=0.6,\ 0.85,\ 1.0\)。
- **岩石材料参数**（Lama & Vutukuri, 1978; Zoback, 2007）：密度 \(2700\)\ kg/m³，杨氏模量 \(50.0\)\ GPa，泊松比 \(0.25\)，内摩擦系数 \(1.0\)，抗拉强度 \(20.0\)\ MPa，黏聚力 \(40.0\)\ MPa，I型断裂能释放率 \(158.4\)\ J/m²，II型 \(198.0\)\ J/m²。

## Methods
1. **裂隙网络生成与表征**：采用幂律模型（式1）描述长度分布；利用圆形窗口法（式3）计算局部裂隙强度 \(\gamma\)；通过渗流参数 \(p\)（式4）量化连通性，阈值 \(p_c\approx 5.8\)；用局部强度的方差 \(\sigma^2\) 评估非均质性。
2. **地质力学模拟**：使用混合有限-离散元法（FEMDEM）求解二维平面应变问题，离散元网格平均尺寸 \(0.05\)\ m。裂隙剪切强度满足库仑准则，当剪应力超过 \(\mu\sigma_n'\) 时发生摩擦滑动。不考虑残余应力，也不考虑裂隙形成过程中应力阴影对组织的影响。
3. **应力变异性张量量化**：
   - **局部应力扰动**：以欧几里得距离 \(d(\mathbf{S}_i, \bar{\mathbf{S}}) = \|\mathbf{S}_i - \bar{\mathbf{S}}\|_F\) 度量，其中 \(\bar{\mathbf{S}}\) 为全场的Fréchet均值（式8），已被证明等于远场构造应力张量（Gao et al., 2017；本文Figure S16验证）。
   - **整体应力离散度**：采用有效方差 \(V_e(\mathbf{S}) = \sqrt[\frac{1}{2}m(m+1)]{\det(\mathbf{\Omega})}\)，\(\mathbf{\Omega}\) 为应力向量 \(\mathbf{s}_i = [S_{xx,i},\ S_{xy,i},\ S_{yy,i}]^{\mathrm{T}}\) 的协方差矩阵（式12）。
4. **数据统计**：局部应力扰动值按对数正态分布处理，使用几何均值与标准差；散点图采用分箱统计并给出±1标准差误差棒（Figure 4, S10–S14）。

## Key Findings
1. **局部应力扰动与裂隙强度的线性正相关**：无论合成或天然裂隙网络，无论 \(\mu\) 与构造应力比如何，\(d(\mathbf{S}, \bar{\mathbf{S}})\) 随局部裂隙强度 \(\gamma\) 线性增大；其散度 \(h\)（各分箱内扰动值的总误差棒长度）亦与 \(\gamma\) 成线性关系[Lei & Gao, 2018, pp. 5-10, Figures 4, S10, S11]。相关系数强烈依赖于构造应力条件（Text S3, Figure S15）。
2. **应力扰动与剪切滑移的分布图像**：当 \(S_{xx}^\infty/S_{yy}^\infty=1\) 时应力与位移较均匀；随应力比升高（2.0, 3.0），沿大裂隙的剪切位移集中，应力扰动集中在裂隙尖端和交叉点，可能伴随脆性破坏（Figures 2, 3）[Lei 2018, pp. 5-10]。
3. **连通性对整体应变与应力变异性的控制**：
   - **总剪切应变 \(\varepsilon\)**：在未连通（\(p<p_c\)）时极低，主要由基质抵抗控制；一旦 \(p>p_c\)，\(\varepsilon\) 急剧增大，尤其在 \(S_{xx}^\infty/S_{yy}^\infty=3.0,\ \mu=0.6\) 时最显著（Figure 5左侧）。
   - **有效方差 \(V_e(\mathbf{S})\)**：当 \(p\) 接近并超过 \(p_c\) 时，\(V_e\) 大幅上升，且高应力比条件下增加更为剧烈；未连通区 \(V_e\) 几乎与 \(\mu\) 无关，连通区 \(V_e\) 随 \(\mu\) 增大而显著降低（Figure 5右侧）。
4. **天然裂隙模式的表现**：天然裂隙网接近渗流阈值（\(p\approx p_c\)），其 \(V_e\) 趋势与合成网络一致，但因其各向异性，\(V_e\) 的变异较大，受构造应力方向与优势裂隙方向的相对关系影响。
5. **综合结论**：在二维条件下，局部应力波动由局部裂隙密度线性控制；整体应力场离散度主要受裂隙网络连通性支配，当系统连通且处于临界摩擦滑动状态（应力比接近按库仑准则的理论值约3.1，\(\mu=0.6\)）时，应力变异最为显著。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 局部应力扰动 \(d(\mathbf{S},\bar{\mathbf{S}})\) 与局部裂隙强度 \(\gamma\) 呈正线性相关 | [Lei 2018, pp. 5-10] Figures 4a, S10a, S11a | 二维、不同 \(\mu\)、不同构造应力比 | 采用对数正态分布的几何均值，相关系数显著 |
| 同一分箱内 \(d\) 的散度 \(h\) 亦与 \(\gamma\) 线性相关 | [Lei 2018, pp. 5-10] Figures 4b, S10b, S11b | 同上 | 进一步确认系统性关联 |
| 总剪切应变 \(\varepsilon\) 和应力有效方差 \(V_e\) 随渗流参数 \(p\) 变化剧烈 | [Lei 2018, pp. 10-11] Figure 5 | 三种 \(\mu\) 与三种应力比 | 当 \(p>p_c\) 且 \(S_{xx}^\infty/S_{yy}^\infty=3\) 时增量最大 |
| 在未连通区 (\(p<p_c\)) \(V_e\) 与 \(\mu\) 无关，连通区 (\(p>p_c\)) \(V_e\) 随 \(\mu\) 增大而降低 | [Lei 2018, pp. 10-11] Figure 5 右列 | 三种应力比 | 表明连通状态下裂隙摩擦滑动主导应力分布 |
| 天然裂隙网 (\(p\approx 5.6\)) 的 \(V_e\) 符合合成网络趋势，但各向异性造成较大变化 | [Lei 2018, p.10] | 旋转采样窗口，不同 \(\theta\) | p≈pc 下的预测成立 |

## Limitations
- 研究局限于二维问题，未考虑三维效应[Lei 2018, pp. 1-2, 11]。
- 仅分析固定尺度 \(L=10\)\ m，未涉及尺度效应；但指出分形裂隙网络缺乏表征单元体可能引起复杂的应力变异性尺度效应[Lei 2018, pp. 10-11]。
- 合成裂隙生成时未考虑应力阴影对裂隙组织的抑制作用[Lei 2018, pp. 2-4]，即裂隙分布可能比实际情况更均匀。
- 假设裂隙模式与当代构造应力场无相关性，且忽略残余应力影响[Lei 2018, pp. 1-2]。
- 裂隙力学行为仅考虑库仑摩擦滑动，未单独分析新生裂纹扩展对应力场的影响（尽管FEMDEM方法具备该能力，但本研究未深入探讨）[Lei 2018, pp. 4-5, 10]。
- 未讨论应力-渗流耦合效应。

## Assumptions / Conditions
- 裂隙为预先存在且无序分布（合成网络：位置和方向随机、各向同性，分形维数 \(D=2.0\)）。
- 裂隙长度服从幂律分布，上下限为 \(l_{\min}=0.2\)\ m，\(l_{\max}=500\)\ m (\(\gg L\))。
- 岩块为线弹性均质，裂隙剪切遵循库仑准则。
- 外荷载为正交主应力，平面应变状态。
- 采用Fréchet均值定义平均应力张量，且该均值等于远场构造应力。

## Key Variables / Parameters
- \(\gamma\)：局部/平均裂隙强度（总长度/面积）
- \(\sigma^2\)：局部裂隙强度方差
- \(a\)：幂律长度指数
- \(D\)：分形维数（合成网络固定为2.0）
- \(p\)、\(p_c\)：渗流参数及其阈值（~5.8）
- \(\mu\)：裂隙摩擦系数（0.6, 0.85, 1.0）
- \(S_{xx}^\infty/S_{yy}^\infty\)：构造应力比（1, 2, 3）
- \(d(\mathbf{S}_i,\bar{\mathbf{S}})\)：局部应力扰动的欧几里得距离
- \(V_e(\mathbf{S})\)：应力场的有效方差
- \(\varepsilon\)：总剪切应变

## Reusable Claims
- **Claim 1**: 在含预先存在、摩擦性裂隙的二维岩体中，局部应力张量与远场均值的欧几里得距离与局部裂隙强度（以圆形窗口测量的总长度/面积）之间存在正线性关系。*条件：裂隙无内聚力，围岩线弹性，库仑摩擦滑动主导。*[Lei 2018, pp. 5-10, 11]
- **Claim 2**: 裂隙网络的整体应力变异可用有效方差 \(V_e\)（由应力向量协方差阵的几何均值求得）表征，当渗流参数超过约5.8且系统处于临界滑动状态时，\(V_e\) 急剧增大。*条件：二维幂律分布裂隙，无残余应力，不与当代应力相关，不考虑尺度效应。*[Lei 2018, pp. 10-11]
- **Claim 3**: 在未连通裂隙系统中，应力场离散度受基质阻抗主导，与裂隙摩擦系数无关；在连通系统中，离散度随摩擦系数增大而降低，表明裂隙滑移成为主控因素。*条件同Claim 2，且加载为高差应力时表现最明显。*[Lei 2018, pp. 10-11]
- **Claim 4**: 对具有多组定向裂隙的真实天然网络，其应力变异性与合成网络在渗流阈值附近的行为一致，但各向异性导致变异幅度增大，受控于构造应力与优势裂隙组的相对方位。*条件：裂隙取自Hornelen盆地露头，二维分析，材料参数固定。*[Lei 2018, pp. 10]

## Candidate Concepts
- [[fracture network connectivity]]
- [[percolation threshold]]
- [[power law length scaling]]
- [[effective variance of stress]]
- [[local fracture intensity]]
- [[tensor-based stress analysis]]
- [[stress perturbation]]
- [[critically stressed state]]
- [[Euclidean distance between stress tensors]]
- [[fracture-induced stress variability]]

## Candidate Methods
- [[finite-discrete element method (FEMDEM)]]
- [[circular window method for fracture intensity]]
- [[Fréchet mean of stress tensors]]
- [[effective variance from covariance matrix]]
- [[unstructured mesh for fracture-rich domains]]
- [[hybrid finite-discrete element modelling]]

## Connections To Other Work
- 继承与发展了 Gao & Harrison (2016, 2018) 的张量应力分析方法，克服常规标量/向量分析将应力大小与方向解耦的缺陷，这一缺陷曾被 Hudson & Cooling (1988) 指出。
- 延续了渗流理论在裂隙网络分析中的应用（Bour & Davy, 1997; Robinson, 1983, 1984），并利用渗流参数 \(p\) 解释应力分布过渡现象。
- 与 Davy et al. (2010) 和 de Dreuzy et al. (2001a, 2001b) 所揭示的裂隙连通性对水力学行为的影响相呼应，说明连通性同样控制着力学（应力）行为。
- 所观察到的应力扰动与裂隙几何的关系，可能为现场观测到的应力方向/大小的分形特征（Day-Lewis et al., 2010; Shamir & Zoback, 1992）提供力学解释。
- 现场应力测量（Barton & Zoback, 1994; Martin & Chandler, 1993）表明构造应力被断层/裂隙扰动，本文的数值框架为定量分析此类扰动提供了工具。

## Open Questions
- 在分形裂隙网络中（缺乏代表性单元体），应力变异性是否存在尺度依赖？尤其是临界滑动状态下，不同尺度如何影响 \(V_e\) 与 \(d\)？（论文指出尺度效应待研究）
- 三维裂隙网络的连通性-应力变异关系如何？三维渗流阈值及滑移激活与二维异同？
- 若同时考虑残余应力、裂隙生长过程中的应力阴影，合成网络的应力扰动-强度线性关系是否仍然成立？
- 新裂隙的起裂与扩展（FEMDEM可模拟）对应力场分布的反作用如何影响局部与整体变异性？
- 在更广泛参数范围（不同岩石弹性模量、内聚力、初始地应力类型）下，线性相关性及 \(V_e \sim p\) 趋势的鲁棒性？
- 能否通过裂隙几何（长度、方向、密度）和构造应力状态直接预测应力有效方差，从而为地震预测或工程选址提供快速评估指标？

## Source Coverage
所有已索引的非空片段（共10段，覆盖原论文第1页至第13页，作者Lei & Gao, 2018）均已处理。按块覆盖比=1.0，按字符覆盖比=1.004（完整索引，有微小冗余），未使用任何片段外信息。来源签名：`5dfef909b462c35752293222b37441cfe5e8ed61`，单次编译策略。
