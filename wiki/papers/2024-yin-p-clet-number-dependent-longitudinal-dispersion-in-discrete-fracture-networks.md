---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks"
title: "Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Péclet-Number-Dependent Longitudinal Dispersion in Discrete Fracture Networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yin, Tingchang, et al. \"Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks.\" *Water Resources Research*, 2024, doi:10.1029/2024WR038437. Accessed 2026."
indexed_texts: "25"
indexed_chars: "124689"
nonempty_source_blocks: "25"
compiled_source_blocks: "25"
compiled_source_chars: "125183"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003962"
coverage_status: "full-index"
source_signature: "592d86b68b46b37af8e72295520e1952e5d7d200"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:40:07"
---

# Péclet‐Number‐Dependent Longitudinal Dispersion in Discrete Fracture Networks.

## One-line Summary
通过大量三维随机离散裂缝网络（DFNs）的数值模拟，本研究揭示了纵向弥散系数 \(D_L\) 的 Péclet 数依赖性，提出了一种考虑大裂缝影响的新 Péclet 数 \(Pe_c\)，并发现当平流主导时，无量纲纵向弥散系数可由一个关于裂缝密度和域尺寸的普适有限尺寸标度函数描述。

## Research Question
如何基于裂缝网络结构（密度、尺寸分布、走向）和 Péclet 数预测纵向弥散系数？能否找到一个统一的标度关系，使得不同裂缝参数下的弥散行为可以用单一方程描述？

## Study Area / Data
本研究未采用实际场地数据，而是通过随机生成 28 组不同参数的三维离散裂缝网络（DFNs）进行模拟。裂缝形态为正方形，域尺寸 \(L_m\) 至少为裂缝尺寸期望值的 10 倍。裂缝密度以无量纲化密度 \(\rho'\) 表示，其范围为 \( \rho_c' \approx 2.31 \) 至 4 倍 \(\rho_c'\)。裂缝尺寸分布包括单一直径、幂律、对数正态和均匀分布四种；裂缝走向由 Fisher 分布描述；孔径和导水率与尺寸呈幂律关系（\(b = \gamma R^\beta\)）并满足立方律。模拟方案涵盖了 Péclet 数从 \(10^{-3}\) 到 \(+\infty\) 的广泛范围。

## Methods
1. **裂缝网络生成**：在立方域内生成正方形裂缝，中心位置均匀分布，走向服从 Fisher 分布，尺寸采用四种分布类型，详细参数如表 1 所示。关键无量纲密度 \(\rho' = \rho \cdot \mathbb{E}[V_{\text{ex}}]\) 被用来统一表征网络连通性（Mourzenko et al., 2011; Yin et al., 2022, 2023）[Yin 2024, pp. 7-8]。
2. **流动模拟**：假设缓慢、稳态、不可压缩流，求解简化的 Navier-Stokes 方程。采用混合杂交有限元方法（MHFEM）保证通量连续性，施加恒定水头边界条件[Yin 2024, pp. 5-5]。
3. **溶质运移模拟**：通过离散时间随机游走方法模拟粒子追踪，方程 \( x_{t+\delta t} = x_t + \mathbf{v}(x_t)\delta t + \mathbf{z} \sqrt{2 D_m \delta t} \)。根据 \(Pe\) 选择初始条件和交点混合规则：\(Pe > 1\) 时采用通量加权初始条件和出流加权混合规则；\(Pe \leq 1\) 时采用均匀分布初始条件和等概率混合规则[Yin 2024, pp. 6-7]。
4. **弥散系数计算**：纵向弥散系数 \(D_L = \frac{1}{2} d\sigma_L / dt\)，其中 \(\sigma_L\) 为粒子纵向位移方差。仅当方差随时间线性变化时视为渐近弥散[Yin 2024, pp. 13-14]。
5. **新 Péclet 数定义**：为考虑大裂缝影响，引入特征长度 \(L_c = (\mathbb{E}[l^6] / \mathbb{E}[l^3])^{1/3}\)，重新定义 \(Pe_c = \mathbb{E}[|\mathbf{v}|] \cdot L_c / D_m\)[Yin 2024, pp. 17-18]。同时基于达西流速定义了 \(Pe_D\)[Yin 2024, pp. 18-19]。
6. **有限尺寸标度假设**：对于平流主导弥散，提出标度形式 \(\langle D_L'' \rangle \cdot L'^{\omega/\nu} = F[(\rho' - \rho_c') L'^{1/\nu}]\)，其中 \(D_L'' = D_L / (\mathbb{E}[|\mathbf{v}|] \cdot L_c)\)，\(L' = L_m / L_c\)，\(\nu = 0.88\)，\(\omega/\nu = -1\)[Yin 2024, pp. 19-20]。

## Key Findings
- **渐近弥散判据**：当无量纲密度 \(\rho' > 2.5 \rho_c'\) 时，纵向位移方差随时间呈线性增长，表明达到渐近弥散状态。这一阈值通过拟合优度 \(R_D\) 和可视化检查确定，对高 \(Pe\) 情形尤其明显。随密度增加，弯曲度下降，首次通过时间（FPT）分布趋于钟形，暗示更均匀的裂隙间混合[Yin 2024, pp. 12-16]。
- **Péclet 数主导影响**：无量纲纵向弥散系数 \(D_L' = D_L / D_m\) 同时依赖于 \(Pe\) 和 \(\rho'\)，但 \(Pe\) 的影响远强于 \(\rho'\)。以 \(Pe_c\) 为横坐标时，所有情景的数据点坍缩为一条单一曲线：\(Pe_c \ll 1\) 时 \(D_L'\) 几乎不变且略小于 1，\(Pe_c \gg 1\) 时遵循幂律关系（拟合指数 0.97）[Yin 2024, pp. 16-19]。
- **转变点**：\(Pe_c \approx 1\) 是 \(D_L'\) 对 \(\rho'\) 依赖性的转变点：低于此值时 \(D_L'\) 随 \(\rho'\) 增加而增大，高于此值时随 \(\rho'\) 增加而减小[Yin 2024, pp. 18-19]。
- **有限尺寸标度普适性**：对于 \(Pe_c \ge 10\) 的平流主导弥散，采用 \(D_L'' = D_L / (\mathbb{E}[|\mathbf{v}|] \cdot L_c)\) 后，所有情景的数据坍缩为一条单调递减的标度函数 \(F[(\rho' - \rho_c') L'^{1/\nu}]\)，表明弥散系数可以通过包含密度和域尺寸的单一函数描述[Yin 2024, pp. 19-21]。
- **利用易得参数预测**：基于达西流速的 Peclet 数 \(Pe_D\) 同样显示幂律关系（指数 0.95），暗示在实际工程中可使用现场可测的平均达西流速和裂缝统计参数估算弥散系数[Yin 2024, pp. 18-19]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 渐近弥散出现在 \(\rho' > 2.5 \rho_c'\) | [Yin 2024, pp. 15-16] | 域尺寸约为裂缝平均尺寸的10倍以上，不同 \(Pe\) 和尺寸分布均适用 | 基于拟合优度 \(R_D\) 和无量纲长度 \(L_a'\) 双重验证 |
| 当 \(Pe_c \gg 1\)，\(\langle D_L' \rangle \sim Pe_c^{0.97}\) | [Yin 2024, pp. 18-19] | 所有模拟情景，引入 \(L_c\) 重新计算 \(Pe_c\) | 去除尺寸异质性的影响后数据坍缩 |
| \(Pe_c \approx 1\) 是 \(D_L'\) 密度依赖性的转折点 | [Yin 2024, pp. 18-19] | 适用于渐近弥散状态 (\(\rho' > 2.5 \rho_c'\)) | \(Pe_c<1\) 时弥散随密度增；\(Pe_c>1\) 时随密度减 |
| 平流主导弥散遵循有限尺寸标度 \(D_L'' \cdot L' = F[(\rho'-\rho_c') L'^{1/\nu}]\) | [Yin 2024, pp. 19-20] | \(Pe_c \ge 10\)，\(\nu=0.88\)，\(\omega/\nu=-1\) | 标度函数为递减函数，不同裂缝参数的数据坍缩 |
| 使用 \(Pe_D\) 计算同样获得幂律关系 | [Yin 2024, pp. 18-19] | 基于达西流速，计算简单 | 指数略低 (0.95)，适合现场应用 |

## Limitations
- 仅将裂缝网络视为唯一的导水通道，未考虑岩石基质的渗透性和基质-裂缝间的相互作用，这在基质渗透率不可忽略时可能引入偏差[Yin 2024, pp. 21-21]。
- 模拟采用正方形裂缝和固定幂律孔径-尺寸关系，可能与天然裂缝的几何复杂性不完全一致[Yin 2024, pp. 3-4]。
- 有限尺寸标度假设在接近 \( \rho_c' \) 时由于渐近弥散未观测到而未被验证，且标度函数是否适用于不同混合规则或强基质扩散情形尚不明确[Yin 2024, pp. 20-21]。
- 模拟中保持固定域尺寸，未探讨不同域尺寸下的渐近行为，尽管通过 \(L'\) 包含了尺寸效应[Yin 2024, pp. 19-20]。

## Assumptions / Conditions
- 裂缝为三维正方形平面，忽略厚度，孔径与尺寸通过幂律关联并满足立方律[Yin 2024, pp. 4-5]。
- 流动为缓慢、稳态、不可压缩，可用达西型方程描述[Yin 2024, pp. 5-5]。
- 粒子追踪采用离散时间随机游走，交点处采用完全混合规则（出流加权或等概率）[Yin 2024, pp. 6-7]。
- 仅考虑充分渗流（\(\rho' > \rho_c'\)）的网络，以保证域内存在连通的裂缝团[Yin 2024, pp. 8-9]。
- 通过 \(Pe\) 值确定初始粒子分布和交点混合模式：\(Pe>1\) 采用通量加权注入和出流权重分配；\(Pe \le 1\) 采用均匀注入和等概率分配[Yin 2024, pp. 9-10]。

## Key Variables / Parameters
- **无量纲密度** \(\rho' = \rho \cdot \mathbb{E}[V_{\text{ex}}]\)：捕捉尺寸多分散性和走向各向异性对连通性的影响，临界值 \(\rho_c' \approx 2.31\)[Yin 2024, pp. 7-8]。
- **Péclet 数** \(Pe = \mathbb{E}[|\mathbf{v}|] \cdot \mathbb{E}[R] / D_m\) 及修改版 \(Pe_c = \mathbb{E}[|\mathbf{v}|] \cdot L_c / D_m\)，特征长度 \(L_c = (\mathbb{E}[l^6] / \mathbb{E}[l^3])^{1/3}\)[Yin 2024, pp. 7-8, 17-18]。
- **纵向弥散系数** \(D_L\)，无量纲形式 \(D_L' = D_L / D_m\)，及标度形式 \(D_L'' = D_L / (\mathbb{E}[|\mathbf{v}|] \cdot L_c)\)[Yin 2024, pp. 13-14, 19-20]。
- **域尺寸比** \(L' = L_m / L_c\)，关联有限尺寸影响[Yin 2024, pp. 19-20]。
- **弯曲度** \(\tau_{\chi}\)：由粒子轨迹或平均流速定义，随 \(\rho'\) 增加呈幂律衰减[Yin 2024, pp. 10-11]。
- **首次通过时间** \(\tau\) 及其无量纲形式 \(\tau' = \tau / \tau_c\)，其中 \(\tau_c = \mathbb{E}[R] / \mathbb{E}[|\mathbf{v}|]\)[Yin 2024, pp. 11-12]。

## Reusable Claims
- 在给定域尺寸下，无量纲密度 \(\rho' > 2.5 \rho_c'\) 可确保纵向弥散达到渐近状态，此时 \(D_L\) 可由位移方差的时间导数定值，且方差呈线性增长[Yin 2024, pp. 15-16]。
- 对于任何裂缝尺寸分布和走向，若采用考虑大裂缝影响的 Péclet 数 \(Pe_c\)，无量纲纵向弥散系数 \(D_L'\) 在 \(Pe_c \gg 1\) 时与 \(Pe_c\) 呈指数约 0.97 的幂律关系[Yin 2024, pp. 18-18]。
- 在平流主导弥散区域 (\(Pe_c \ge 10\))，无量纲弥散系数 \(D_L''\) 可通过有限尺寸标度函数 \(F[(\rho'-\rho_c') L'^{1/\nu}]\) 统一描述，该函数随密度和域尺寸单调递减[Yin 2024, pp. 19-20]。
- 标度定律中的临界指数取 \(\nu=0.88\) 和 \(\omega/\nu=-1\) 可以使多种裂缝网络的数据坍缩；此处的 \(\omega\) 不同于经典逾渗值[Yin 2024, pp. 19-20]。
- 达西速率定义的 Péclet 数 \(Pe_D\) 同样能产生幂律关系，表明在现场应用中可通过易获取的宏观参数预测弥散[Yin 2024, pp. 18-19]。

## Candidate Concepts
- [[离散裂缝网络 (DFN)]]
- [[纵向弥散]]
- [[Péclet 数]]
- [[渐近弥散]]
- [[非菲克/反常输运]]
- [[首次通过时间分布]]
- [[弯曲度]]
- [[逾渗阈值]]
- [[有限尺寸标度]]
- [[尺寸异质性]]
- [[弥散系数]]

## Candidate Methods
- [[混合杂交有限元法 (MHFEM)]]
- [[粒子追踪/随机游走]]
- [[连续时间随机游走 (CTRW)]]
- [[有限尺寸标度假设]]
- [[Fisher 分布定向]]
- [[通量加权注入]]
- [[完全混合规则]]

## Connections To Other Work
- Huseby et al. (2001) 在三维单分散 DFN 中发现 \(D_L'\) 与 \(Pe\) 的幂律关系，本研究在更复杂的 DFN 中验证并扩展了此发现，并通过引入 \(Pe_c\) 和数据坍缩强化了普适性[Yin 2024, pp. 2-3, 18-19]。
- 与一般多孔介质类似，\(Pe \ll 1\) 时弥散近乎有效扩散，\(Pe \gg 1\) 时弥散主要由速度非均质性控制；本研究中 \(Pe_c \approx 1\) 的转变点与 Bear (2012) 等文献一致[Yin 2024, pp. 2-3, 18-19]。
- Bernabé et al. (2016) 发现弥散系数随配位数增加而减小，本研究中 \(\rho'\) 增加（等效配位数增加）导致平流主导弥散下降，与之一致[Yin 2024, pp. 2-3]。
- 弯曲度-密度标度与逾渗理论预测一致，\(\tau_{\chi} \propto |\rho'-\rho_c'|^{-0.25}\) 符合 Hunt & Sahimi (2017) 的框架[Yin 2024, pp. 10-11]。
- 有限尺寸标度分析与 Yin et al. (2023) 的渗透率论文相呼应，但无量纲弥散呈现递减而非递增趋势[Yin 2024, pp. 19-20]。

## Open Questions
- 当 \(\rho'\) 接近 \(\rho_c'\) 时，如何评估弥散系数的密度依赖性？现有的标度函数是否适用于该区域？[Yin 2024, pp. 20-21]
- 对于极低 \(Pe\)（扩散主导），\(D_L'\) 随密度增加而上升，其有限尺寸标度形式如何？[Yin 2024, pp. 20-21]
- 考虑岩石基质扩散时，Péclet 数依赖性是否依然成立？标度函数是否需要修正？[Yin 2024, pp. 21-21]
- 不同的交点混合规则（如流线路由）在中等 \(Pe\) 下是否显著影响渐近弥散和标度关系？[Yin 2024, pp. 6-7, 16-16]
- 标度关系中临界指数 \(\omega/\nu = -1\) 的理论依据是什么？是否可推广至更广泛的混乱介质？[Yin 2024, pp. 19-20]

## Source Coverage
本文所有非空索引片段（共25个）均被处理并用于构建本页。覆盖统计：索引文本块数25，索引字符数124,689；源编译块数25，编译字符数125,183；块覆盖率100%，字符覆盖率约1.004。本页内容完全基于提供的索引片段，未引入外部事实或推测。
