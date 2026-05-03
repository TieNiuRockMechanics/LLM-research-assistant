---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-zhu-impacts-of-t-type-intersections-on-the-connectivity-and-flow-in-complex-two-dimensional"
title: "Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2023 - Impacts of T-type intersections on the connectivity and flow in Complex two-dimensional fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhu, Weiwei, et al. \"Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks.\" *Engineering Geology*, vol. 320, 2023, p. 107122. doi:10.1016/j.enggeo.2023.107122. Accessed 2026."
indexed_texts: "11"
indexed_chars: "53939"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "51252"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.950184"
coverage_status: "full-index"
source_signature: "4e03f4b679cd947be4d1d8a1474ea796dc8f28fc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:49:32"
---

# Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks.

## One-line Summary
系统研究了T型交叉对复杂二维裂缝网络连通性及流体流动（单相渗透率与两相产气量）的影响，通过基于规则的裂缝生长算法构建具有大量T型交叉的动力学裂缝网络，并对比原始随机网络，发现大多数动力学裂缝网络具有更好的连通性与更高的流动能力，但流动结果受出入口裂缝数量显著影响。

## Research Question
T型交叉（T-type intersections）对复杂二维裂缝网络的连通性和地下流体流动（包括单相渗透率和两相累积产气量）有何影响？其影响在不同几何参数（裂缝长度分布、中心位置聚集度、方位集中度）下的规律如何？

## Study Area / Data
- **数据来源**：基于露头统计的合成裂缝网络（非特定现场）。裂缝长度服从幂律分布，指数 \(a\) 取值2.0（小裂缝为主）、2.5、3.0（更小裂缝）；裂缝中心位置采用分形空间密度分布，分形维数 \(F_D\) 取1.5（强聚集）、1.7、2.0（均匀）；方位服从 von Mises-Fisher 分布，浓度参数 \(\kappa\) 取0（均匀）、5、10（高度集中）。通过田口方法正交设计9种组合，每种生成10个实现，共计90个裂缝网络。系统尺寸为100任意单位，最小裂缝长度10单位。所有网络为过逾渗状态（裂缝强度为逾渗时强度的两倍）。
- **流动模拟条件**：单相流假设基质不可渗透，左边界200 kPa，右边界0 kPa，上下边界封闭；两相流模拟页岩气产出过程，基质渗透率1.0微达西，裂缝渗透率10达西，初始地层压力30,000 kPa，水平井中部定压10,000 kPa，模拟10天。
- **对照网络**：原始裂缝网络不含T型交叉，动力学裂缝网络通过生长算法生成，两者具有相同的方位分布、裂缝数量密度 \(P_{20}\) 和裂缝强度 \(P_{21}\)。

## Methods
- **裂缝网络构建**：使用 HatchFrac 软件生成 SDFN（Zhu et al., 2022c），依据选定统计参数依序添加裂缝，直至达到过逾渗状态。
- **动力学裂缝网络生成**：基于成核-生长-终止规则的裂缝生长算法（Davy et al., 2010, 2013）。成核数等于原始网络裂缝数，生长方向与原始裂缝一致；生长速度设为 \(v_i = l_c + \text{rand}(0, \beta \cdot l_i / l_{\max})\)，其中 \(l_c = 5\) 单位/步，\(\beta=2.0\)；终止条件为裂缝尖端遇到大裂缝。通过调节随机部分匹配规定的 \(P_{21}\)。
- **拓扑与连通性分析**：对最大连通簇计算连通性指数 \(C_B = (4N_X + 3N_T)/N_B\)，其中 \(N_X\) 为X型节点数，\(N_T\) 为T型节点数，\(N_B\) 为分支数（由 \(N_B = 0.5(N_I + 3N_T + 4N_X)\) 计算）。
- **流动模拟**：单相流与两相流模拟使用 UNCONG（Li et al., 2015），嵌入离散裂缝网络处理。两相模拟中气体压缩性与黏度随压力变化，相对渗透率曲线见原文图6。
- **敏感性分析**：采用输入/输出相关法计算几何参数与响应之间的相关系数 \(\rho\)。

## Key Findings
1. **T型交叉比例**：原始裂缝网络几乎不含T型交叉，而动力学裂缝网络的平均T型交叉占比为0.32。
2. **连通性提升**：90个案例中，多数动力学裂缝网络的最大连通簇包含的裂缝数量更多，但总交叉点数更少（77/90减少）；连通性指数 \(C_B\) 在所有案例中均等于或高于原始网络（仅一个案例略低于1.0）。因此，动力学裂缝网络能用更少的交叉点连接更多的裂缝。
3. **单相渗透率**：68%（61/90）的动力学裂缝网络渗透率高于原始网络，最大提高3.5倍。小裂缝主导（大 \(a\)）且强聚集（小 \(F_D\)）的动力学网络渗透率提升更显著；方位集中度 \(\kappa\) 的影响不单调。
4. **两相产气量**：77%（69/90）的动力学网络累积产气量更高，最大提升1.4倍。同样，小裂缝和强聚集有利于生产比提高，但方位集中度 \(\kappa\) 显示出负面作用。
5. **流动与连通性关系**：渗透率、产气量与连通性指数呈正相关（如原始网络渗透率与 \(C_B\) 相关系数0.61，动力学网络0.63），但二者并不等价。流动结果受出入口（与边界相交的裂缝数）强烈影响：单相流中入口/出口数与渗透率相关系数高达0.78–0.97；两相流出口数与产气量相关系数0.69–0.74。连通性指数对渗透率比和产气量比的相关系数更高（约0.54–0.71）。
6. **参数敏感性**：几何参数对原始与动力学网络流动响应的敏感性有差异。\(a\) 和 \(\kappa\) 对原始及动力学网络渗透率、产气量有正相关；\(F_D\) 对渗透率负相关（聚集增强渗透），但对产气量正相关（聚集可能不利于产气）。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 动力学裂缝网络平均T型交叉占比0.32，原始网络几乎为0 | Fig. 7, 正文第5-6页 | 90个正交案例，覆盖不同几何参数 | T型交叉普遍由生长算法产生 |
| 77/90案例中动力学网络的总交叉点数少于原始网络 | Fig. 9(b), 正文第5-6页 | 连通性指数几乎全部更高 | 交叉点数量不代表连通性 |
| 86/90案例的动力学网络连通性指数高于或等于原始网络 | Fig. 9(a), 正文第5页 | 除一例外均增强 | 连通性定义见公式(1) |
| 68%案例渗透率提升，最大3.5倍 | Fig. 10, 正文第5-6页 | 单相流，恒定压力边界 | 小裂缝（a大）和强聚集（FD小）贡献更大 |
| 77%案例产气量提升，最大1.4倍 | Fig. 12, 正文第6-7页 | 两相流，水平井定压生产 | 同样小裂缝和强聚集有正向影响 |
| 渗透率与出入口数相关系数0.78-0.97 | Table 3, 正文第8页 | 原始与动力学网络分别计算 | 出入口数对绝对流动值影响极强 |
| 连通性指数与渗透率比的相关系数0.67-0.71 | Table 3, 正文第8页 | 比出入口数与比的相关系数更高 | 连通性对比值影响较大 |
| 连通性指数与产气量相关系数0.65-0.85 | Table 3, 正文第8页 | 动力学网络更高 | 连通性好，产气量不一定最高 |

## Limitations
- 未考虑裂缝孔径变化（假设为恒定），实际裂缝受压缩、胶结等影响会有非均质开度（第8-9页）。
- 裂缝生长算法采用简化规则（定生长速度 \(n=0\)，仅以遇到大裂缝为停止条件），未耦合复杂岩石类型、应力状态和断裂力学精细计算（第1-2页，第8页）。
- 仅对比了原始与动力学两类网络，未与真实露头配对比较，因为现实中难以构建无T型交叉的对应网络（第8页）。
- 流动模拟做了较大简化：基质单相流中假设不可渗透，两相流中仅模拟了10天，未考虑复杂流体性质与多种边界条件（第4页，第8页）。
- 结果基于二维网络，但流动模拟将裂缝视为3D恒高对象，推广至三维需进一步验证（第4页）。

## Assumptions / Conditions
- 裂缝网络为过逾渗状态（裂缝强度为逾渗强度的2倍），所有网络均处于连通状态。
- 单相流模拟中基质完全不可渗透；裂缝内为层流（雷诺数 \(O(10^{-3})\)）。
- 两相流模拟中基质渗透率1.0 μD，裂缝渗透率10 D，设定恒定井底流压，模拟期10天。
- 裂缝生长过程中，成核数等于原始网络裂缝数，生长方向与原始裂缝一致，生长速度恒定且含随机分量，裂缝尖端相遇大裂缝即停止；暂未考虑多期次、多应力状态。
- 裂缝几何参数（长度、中心位置、方位）相互独立，分布形式固定；网络不含V型交叉（文中将V型归入T型计数）。
- 二维系统尺寸100单位，裂缝最低长度10单位，流动模拟时将长度单位视为米。

## Key Variables / Parameters
- **Independent geometrical parameters**: 幂律长度分布指数 \(a\)（2.0, 2.5, 3.0）；分形空间密度维数 \(F_D\)（1.5, 1.7, 2.0）；方位浓度参数 \(\kappa\)（0, 5, 10）。
- **Network descriptors**: T型交叉比例 \(N_T/(N_T+N_X)\)；最大簇裂缝数比 \(N_{lc}/N_t\)；最大簇裂缝长度比 \(L_{lc}/L_t\)；连通性指数 \(C_B\)；交叉点/裂缝数 \(I_{pf}\)。
- **Flow responses**: 单相渗透率 \(k\)；两相10天累积产气量 \(G_p\)；渗透率比 \(k_{\text{kin}}/k_{\text{orig}}\)；产量比 \(G_{p,\text{kin}}/G_{p,\text{orig}}\)。
- **Boundary-related variables**: 单相流入/出口裂缝数量；两相流中与水平井相交的出口裂缝数。
- **Correlation coefficients**: \(\rho\) 用于敏感性分析。

## Reusable Claims
- Claim: 基于规则裂缝生长算法生成的动力学裂缝网络，相比无T型交叉的原始SDFN，在相同裂缝方位和强度下，能用更少的交叉点连接更多的裂缝进入最大连通簇，且连通性指数 \(C_B\) 显著提高。 [Zhu 2023, pp. 5-6]
- Claim: 在过逾渗的二维复杂裂缝网络中，T型交叉的存在使多数情况（68%）的单相渗透率得到提升，尤其当裂缝以小尺度为主（幂律指数 \(a\) 较大）且空间聚集度强（分形维 \(F_D\) 小）时提升更为明显；方位集中度的影响不单调。 [Zhu 2023, pp. 5-6, Fig. 10]
- Claim: 对两相页岩气生产模拟，动力学裂缝网络在77%的案例中表现出更高的10天累积产气量，小裂缝主导和强聚集同样促进产量比提高，但方位集中度 (\(\kappa\)) 表现出负面作用。 [Zhu 2023, pp. 6-7, Fig. 12]
- Claim: 裂缝网络的连通性（用 \(C_B\) 衡量）与流动结果（渗透率、产气量）呈正相关，但二者并不等价；流动结果受边界相连的裂缝（入口/出口）数量强烈影响，其相关系数可达0.69–0.97，远高于仅凭连通性的解释力。 [Zhu 2023, pp. 7-8, Table 3]
- Claim: 连通性指数与流动比值（渗透率比、产量比）的相关性优于与绝对流动值的相关性，表明 \(C_B\) 更适合表征T型交叉带来的相对网络连通性变化，而非直接预测流动能力。 [Zhu 2023, pp. 8-9, Table 3]

## Candidate Concepts
- [[T-type intersections]]
- [[X-type intersections]]
- [[stochastic discrete fracture network (SDFN)]]
- [[kinematic fracture network]]
- [[rule-based fracture growth]]
- [[connectivity index (CB)]]
- [[percolation]]
- [[over-percolative state]]
- [[power-law length distribution]]
- [[fractal spatial density]]
- [[von Mises-Fisher distribution]]
- [[single-phase flow simulation]]
- [[two-phase flow simulation]]
- [[inlet/outlet effect]]
- [[topology of fracture networks]]
- [[Taguchi method]]

## Candidate Methods
- [[HatchFrac (DFN modeling software)]]
- [[nucleation-growth-arrest algorithm]]
- [[topological connectivity analysis (CB)]]
- [[UNCONG (embedded discrete fracture model)]]
- [[correlation-based sensitivity analysis]]
- [[Taguchi orthogonal array design]]
- [[Two-sample Kolmogorov-Smirnov test]]

## Connections To Other Work
- 与 Davy et al. (2010, 2013) 和 Maillot et al. (2016) 的成核-生长-终止方法一脉相承，但本文扩展至更复杂的几何分布（非均匀方位、聚集中心），并系统对比了连通性和流动响应。 [Zhu 2023, pp. 2-3]
- 确认 Bour and Davy (1998) 和 Zhu et al. (2018) 的结论：单位裂缝交叉点数 \(I_{pf}\) 不能作为复杂裂缝网络连通性的有效指标。 [Zhu 2023, pp. 5]
- 与 Zhu et al. (2021) 的发现一致：流量结果与连通性相关但不等效，并进一步指出了出入口数量的控制作用。 [Zhu 2023, pp. 7-8]
- 引用了大量露头调查文献（如 Watkins et al., 2015）指出真实网络中T型交叉占比可达74-76%，为研究提供了现实基础。 [Zhu 2023, pp. 1-2]
- 两相流模拟相对渗透率曲线取自 Zhu et al. (2022a)，裂缝网络生成软件参考 Zhu et al. (2022c)。 [Zhu 2023, pp. 4-5]

## Open Questions
- 更真实的裂缝生长过程需耦合力学计算，如何将地应力、裂缝间相互作用和不同岩石断裂韧性纳入复杂网络的生长规则，使T型交叉的分布更具物理基础？ [Zhu 2023, pp. 8]
- 多期次、多优势方位裂缝组的T型交叉形成机理及对连通性和各向异性流动的影响如何？ [Zhu 2023, pp. 8]
- 当考虑裂缝开度非均质性、复杂流体性质（如非牛顿流体）以及真实三维网络时，本文的结论是否仍成立？ [Zhu 2023, pp. 8-9]
- 能否直接利用露头图构建不含T型交叉的对应网络，以进一步验证合成网络的发现？ [Zhu 2023, pp. 8]
- 在更接近真实生产的边界条件（如多井、变流量）下，T型交叉对采收率等长期生产指标的影响如何？

## Source Coverage
- **Indexed fragments processed**: 11 nonempty fragments, total 53939 indexed characters.
- **Compiled source blocks**: 11, total 51252 characters.
- **Coverage ratio (by blocks)**: 1.0
- **Coverage ratio (by characters)**: 0.950184
- **Compilation strategy**: single-pass-markdown
- **All non-empty indexed fragments have been incorporated**; no external facts were added. Claims are directly tied to [Zhu 2023, pp. X] labels from the provided source blocks.
