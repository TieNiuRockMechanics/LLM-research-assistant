---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac"
title: "A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks."
status: "draft"
source_pdf: "data/papers/2016 - A fractal model based on a new governing equation of fluid flow in fractures for characterizing hydraulic properties of rock fracture networks.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Liu, Richeng, et al. \"A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks.\" *Computers and Geotechnics*, vol. 75, 2016, pp. 57-68. doi:10.1016/j.compgeo.2016.01.025. Accessed 2026."
indexed_texts: "12"
indexed_chars: "59438"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59353"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99857"
coverage_status: "full-index"
source_signature: "77ca9b6b4592295a198e74e8dc7f2e1a686b0053"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:14:52"
---

# A Fractal Model Based on a New Governing Equation of Fluid Flow in Fractures for Characterizing Hydraulic Properties of Rock Fracture Networks.

## One-line Summary

本文提出了一种基于分形裂缝长度分布和新立方律控制方程的离散裂缝网络（DFN）模型，通过数值模拟量化了裂缝分形维数、模型尺寸和随机数对等效渗透率的影响，并验证了流量与隙宽的 **\(e^{6-D_T}\)** 关系比经典立方律更符合现场实测数据。

## Research Question

本研究针对三个核心问题展开 [Liu 2016, pp. 2-3]：
1. 推导一种考虑裂缝面外（out‑of‑plane）几何形态的单裂缝流体流动新控制方程；
2. 在不同尺度下验证所提出的分形裂缝长度分布模型的有效性；
3. 评估分形维数（\(D_f\) 和 \(D_T\)）、DFN 模型尺寸以及用于生成裂缝的随机数对等效渗透率的影响。

## Study Area / Data

### 参数来源
- 裂隙最小迹长 \(l_\text{min}=0.5\ \text{m}\)，最大迹长 \(l_\text{max}=500\ \text{m}\)（比值 0.001），这些借用自 Baghbanan & Jing (2008) 对真实岩体的研究 [Liu 2016, pp. 4-5]。
- 分形维数 \(D_f\) 范围 1.3～1.8，低于该范围裂缝难以有效连通，高于该范围岩体过于破碎，自然界极少存在 [Liu 2016, pp. 4-5]。
- 裂隙开度与长度的关系采用文献中张开型（penny‑shaped）裂缝的理论模型：最大张开位移 \(e_\text{max}=a_0 L^{0.5}\)，其中 \(a_0\) 与材料断裂韧度、泊松比和弹性模量相关；平均开度 \(e_\text{avg}=(\pi e_\text{max})/4\)，并假设裂缝深度 \(W\) 等于迹长 \(L\) [Liu 2016, pp. 3-4]。

### 验证数据
- 用 Klimczak et al. (2010) 汇编的多组天然张开型裂缝（如 Shiprock dikes、Florence Lake veins、Culpeper veins 等）的现场实测数据验证新控制方程 [Liu 2016, pp. 8-9]。
- 分形长度分布验证通过计算不同 \(D_f\) 下裂缝数量–长度关系的幂律指数 \(a\)，并与 Dverstop & Anderson (1989)、Tsang et al. (1996)、Bour & Davy (1997)、De Dreuzy (2001) 等文献中的范围进行对比 [Liu 2016, pp. 8, Table 3]。

## Methods

### 分形裂缝长度生成
- 裂缝迹长由 \(l_i = l_\text{min} / (1-R_i)^{2/D_f}\) 生成，其中 \(R_i\in(0,1)\) 为随机数，\(D_f\) 为表征裂缝几何分布的分形维数 [Liu 2016, pp. 2-3]。
- 裂缝总数 \(N_t\) 与最大迹长相关，模型尺寸变化时通过 \(N'_t = N_t L_n^2 / \left[ \exp\left(\frac{D_f - a''}{b''}\right) - c'' \right] \sum_{i=1}^{N_t} l_i\) 更新，其中回归参数 \(a''=0.4594\), \(b''=0.2797\), \(c''=8.4968\)，仅适用于遵循式(1)且中心点、方位均匀随机分布的 DFN [Liu 2016, pp. 4-5]。

### 单裂缝流动新控制方程
- 考虑粗糙度导致的迂曲度：\(L_t = e^{1-D_T} L^{D_T}\)，\(D_T\in[1,2]\) [Liu 2016, pp. 3-4]。
- 结合张开型裂缝的隙宽–长度关系和裂缝宽度 \(W=L\)，代入经典立方律（式(2)）得到：
  \[
  Q = \frac{4^{3-2D_T} \rho g}{3\mu} (\pi a_0)^{4-2D_T} e^{6-D_T} \nabla h
  \]
  即流量与 \(e^{6-D_T}\) 成正比；当 \(D_T=1\) 且不考虑面外几何（\(W=L=1\)）时退化为立方律 \(Q\propto e^3\) [Liu 2016, pp. 3-4, Appendix A]。

### DFN 生成与数值模拟
- 针对 \(D_f=1.4,1.5,1.6\) 分别建立大型原 DFN（边长 28 m, 19 m, 11 m），再从中提取不同尺寸的小网络（如 \(D_f=1.4\) 时边长 0.5～25 m）[Liu 2016, pp. 5-7]。
- 使用 10 组独立随机数（每组含中心点、方位、裂缝长度三套随机数）生成网络，共 1290 个 DFN [Liu 2016, pp. 5, 7]。
- 边界条件：上下边界不透水，左右边界施加定水头梯度产生水平渗流；当左右边界流量相等时视为稳态，按达西定律计算等效渗透率 \(K\) [Liu 2016, pp. 5-7]。

### REV 与敏感性分析
- 通过不同随机数下等效渗透率随边长的变化，计算最大方差 \(V_M\)，以 \(V_M\) 基本恒定的边长作为 REV [Liu 2016, pp. 9-10]。
- 分别固定其他两套随机数，考察中心点、方位、裂缝长度各自随机数对渗透率的影响 [Liu 2016, pp. 9-11]。

## Key Findings

1. **裂缝长度分布验证**  
   生成裂缝的数量–长度关系服从幂律分布 \(n(l,0.5)= a l^{-\alpha}\)，指数 \(\alpha\) 随 \(D_f\) 增大而减小，满足线性关系 \(\alpha = -2.22D_f + 5.61\)。当 \(D_f\in[1.0,2.0]\) 时，\(\alpha\) 范围为 1.17～3.39，与文献中现场实测和理论值（0.0～3.5）吻合 [Liu 2016, pp. 7-8, Table 3]。

2. **新控制方程与实测对比**  
   多组现场数据拟合的流量–隙宽指数在 4.56～4.98 之间，对应 \(D_T\) 约 1.02～1.44；平均指数 4.96（\(D_T\approx1.04\)），远偏离立方律的 3。考虑面外几何后，即使 \(D_T=1.04\)，其粗糙度已超过 JRC=20（\(D_T=1.02\)），说明立方律在天然裂缝中可能引起显著偏差 [Liu 2016, pp. 8-9, Fig. 7]。

3. **随机数的影响**  
   - 等效渗透率对裂缝长度随机数最敏感，其方差 \(V_M\) 远大于中心点或方位随机数产生的方差。裂缝长度分布是控制网络几何的一阶参数，中心点和方位为二阶参数 [Liu 2016, pp. 9-11]。
   - 随 \(D_f\) 增大，REV 尺寸减小：\(D_f=1.4\) 时 REV≈17 m，\(D_f=1.5\) 时 6 m，\(D_f=1.6\) 时 3 m。因为高 \(D_f\) 下更多长裂缝贯穿模型，形成较均匀的流动通道，在较小尺度即可获得稳定渗透率 [Liu 2016, pp. 9-10]。

4. **\(D_T\) 对等效渗透率的影响**  
   等效渗透率随 \(D_T\) 增加呈指数下降（拟合 \(R^2=1\)），\(D_T\) 从 1 增至 2 可导致渗透率变化两个数量级。不同 \(D_f\) 的模型遵循各自的指数衰减规律，其系数主要取决于 \(D_f\) [Liu 2016, pp. 11, Fig. 11]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 生成的裂缝长度–数量符合幂律分布 \(n(l) \propto l^{-\alpha}\)，\(\alpha\) 与 \(D_f\) 线性相关 | [Liu 2016, pp. 7-8, Table 2, Fig. 6] | \(D_f=1.3-1.8\)，\(l_\text{min}=0.5\) m，\(l_\text{max}=500\) m，不同模型边长 | \(\alpha\) 范围 1.64–2.75，与文献一致 |
| 流量 \(Q\propto e^{6-D_T}\) 比经典立方律 \(Q\propto e^3\) 更符合多组现场测量数据，拟合指数 4.56–4.98，对应 \(D_T\) 1.02–1.44 | [Liu 2016, pp. 8-9, Fig. 7] | 数据来自 Klimczak et al. (2010)，包括不同岩性张开型裂缝 | 平均指数 4.96 (\(D_T=1.04\)) |
| 等效渗透率对裂缝长度随机数的方差最大；中心点和方位随机数的影响明显较小 | [Liu 2016, pp. 9-11, Figs. 8-10] | \(D_f=1.4,1.5,1.6\)，10 组随机数，不同模型边长 | 裂缝长度为一阶参数 |
| REV 尺寸随 \(D_f\) 增大而减小（\(D_f=1.4\) 时 ~17 m，1.5 时 ~6 m，1.6 时 ~3 m） | [Liu 2016, pp. 9-10, Figs. 8-10(d)] | 定水头边界，水平流动 | \(V_M\) 稳定时对应的边长作为 REV |
| 等效渗透率随 \(D_T\) 增加呈指数下降，\(D_T\) 相差 1 可使渗透率变化两个数量级 | [Liu 2016, pp. 11, Fig. 11] | \(D_f=1.4,1.5,1.6\)，固定模型尺寸 9 m | 不同 \(D_f\) 的指数律系数不同 |
| 分形长度分布模型可生成与天然裂缝网络一致的幂律分布，\(\alpha\) 与文献中实测范围相符 | [Liu 2016, pp. 8, Table 3] | 对比 Dverstorp & Anderson (1989)、Tsang et al. (1996) 等 | 模型有效 |

## Limitations

- 流体流动模拟仅针对 \(D_f=1.4,1.5,1.6\) 的 DFN 进行，\(D_f=1.7\) 和 1.8 的模型因裂缝过于密集而计算能力不足以完成渗流计算 [Liu 2016, pp. 5-7]。
- 裂缝开度与长度的关系仅适用于张开型（penny‑shaped）裂缝，且假设裂缝深度 \(W\) 严格等于迹长 \(L\)，不适用于剪切型或撕裂型裂缝 [Liu 2016, pp. 3-4]。
- 新控制方程中的 \(D_T\) 需要通过裂缝表面粗糙度测量或等效换算确定，文中仅通过现场数据反推，缺乏直接标定方法 [Liu 2016, pp. 8-9]。
- 所有 DFN 的中心点和方位均采用均匀随机分布，未考虑天然裂缝可能的方向聚集特性 [Liu 2016, pp. 4-5]。
- 边界条件仅模拟水平方向定水头梯度，未探究其他渗流方向和各向异性渗透率张量 [Liu 2016, pp. 5-7]。

## Assumptions / Conditions

- 岩石基质不透水，渗流仅发生在连通裂缝中（DFN 基本假设）[Liu 2016, pp. 1]。
- 裂缝长度分布服从分形定律，且可通过 \(D_f\) 唯一表征 [Liu 2016, pp. 2-3]。
- 裂缝开度与长度满足次线性关系 \(e_\text{max}=a_0 L^{0.5}\)，平均开度与最大张开位移满足 \(e_\text{avg}=(\pi/4)e_\text{max}\)，且裂缝宽度 \(W=L\) [Liu 2016, pp. 3-4]。
- 单裂缝中流体为层流，适用立方律局部形式，但通过迂曲度 \(D_T\) 修正粗糙度和面外几何的影响 [Liu 2016, pp. 3-4]。
- 生成 DFN 时，裂缝中心点和方位均匀随机分布，孤立裂缝和死端裂缝被删除 [Liu 2016, pp. 4-5]。
- 模型边界为上下不透水、左右恒水头差 [Liu 2016, pp. 5-7]。
- 式(10)中回归参数 \(a'', b'', c''\) 仅适用于裂缝长度由式(1)生成且中心点和方位均匀随机的 DFN [Liu 2016, pp. 4-5]。

## Key Variables / Parameters

- \(D_f\)：裂缝网络骨架分形维数，表征裂缝几何分布特征（宏观）[Liu 2016, pp. 2-3]。
- \(D_T\)：单裂缝表面粗糙度导致的迂曲度分形维数，影响裂隙内流动路径非线性（微观）[Liu 2016, pp. 3-4]。
- \(l_\text{min}, l_\text{max}\)：最小、最大裂缝迹长 [Liu 2016, pp. 2-3]。
- \(a_0\)：裂缝最大张开位移与长度关系中的比例系数，与材料断裂韧度、泊松比、弹性模量相关 [Liu 2016, pp. 3-4]。
- \(e\)：水力隙宽，等于平均张开位移 [Liu 2016, pp. 3-4]。
- \(R_i\)：用于生成裂缝长度、中心点和方位的 (0,1) 均匀随机数 [Liu 2016, pp. 2-3, 4-5]。
- \(a\) (幂律指数)：裂缝长度–数量关系 \(n(l)\propto l^{-\alpha}\) 的指数，与 \(D_f\) 线性相关 [Liu 2016, pp. 7-8]。
- \(N_t, N'_t\)：裂缝总数及不同模型边长下的更新总数 [Liu 2016, pp. 4-5]。
- \(L_n, L_T\)：目标 DFN 边长及参考模型边长 [Liu 2016, pp. 4-5]。
- \(K\)：等效渗透率，通过达西定律反算 [Liu 2016, pp. 9]。
- \(V_M\)：不同随机数下等效渗透率的最大方差，用于判断 REV [Liu 2016, pp. 9-10]。

## Reusable Claims

1. **流量‑隙宽关系修正**：对于考虑面外几何和表面粗糙度的单裂缝，流量与隙宽的 \((6-D_T)\) 次方成正比；当 \(D_T\) 略大于 1 时，指数可达 4～5，显著高于立方律的 3，更符合天然张开型裂缝的现场测量数据 [Liu 2016, pp. 8-9, Fig. 7]。
2. **分形长度生成有效性**：利用 \(l_i = l_\text{min} / (1-R_i)^{2/D_f}\) 生成的裂缝网络，其数量–长度关系严格遵循幂律分布，且幂律指数 \(\alpha\) 与 \(D_f\) 呈线性关系 \(\alpha = -2.22D_f + 5.61\)，该关系可覆盖文献中多数实测范围 (\(\alpha\approx1.2-3.4\)) [Liu 2016, pp. 7-8, Eqs. 12-13]。
3. **随机数敏感性**：在基于蒙特卡洛的 DFN 生成中，裂缝长度分布的随机性对等效渗透率的影响远大于裂缝位置和方位的随机性，因此在实际建模中应优先控制长度分布的可靠性 [Liu 2016, pp. 9-11]。
4. **REV 与 \(D_f\) 的关系**：裂缝网络的分形维数 \(D_f\) 越高（即长裂缝占比越大），达到渗透率稳定的 REV 尺寸越小；当 \(D_f>1.5\) 时，REV 可能仅为数米量级 [Liu 2016, pp. 9-10, Figs. 8-10]。
5. **迂曲度对渗透率的量级影响**：\(D_T\) 每增加 0.1 可使等效渗透率下降数倍，整个 \(D_T\) 从 1 到 2 的变化导致渗透率两个数量级的变化 [Liu 2016, pp. 11, Fig. 11]。

## Candidate Concepts

- [[离散裂隙网络 (DFN)]]
- [[分形维数 Df]]
- [[迂曲度分形维数 DT]]
- [[张开型 (penny‑shaped) 裂缝]]
- [[裂缝长度‑数量幂律分布]]
- [[代表单元体 (REV)]]
- [[等效渗透率]]
- [[面外几何 (out‑of‑plane geometry)]]
- [[蒙特卡洛裂缝生成]]
- [[立方律 / 修正立方律]]

## Candidate Methods

- [[基于分形理论的裂缝长度生成](Eq. 1)]](l_i = l_min / (1-R_i)^{2/Df})
- [[单裂缝流量控制方程](Eq. 9)]]（考虑面外几何和迂曲度）
- [[DFN 渗透率数值模拟](定水头边界)]]
- [[裂缝数量随模型尺度的更新](Eq. 11)]]
- [[REV 确定方法（最大方差 V_M 稳定准则）]]
- [[随机数敏感性分析（控制变量法）]]

## Connections To Other Work

- 裂缝长度幂律分布与 De Dreuzy et al. (2001)［11］、Bour & Davy (1997)［8］等一致，且所得指数范围覆盖 Dverstop & Anderson (1989) 的 1.7、Tsang et al. (1996) 的 3.0 [Liu 2016, pp. 8, Table 3]。
- 张开型裂缝的隙宽–长度次线性关系来自 Olson (2003)［45］和 Klimczak et al. (2010)［26］；本模型将其引入 DFN 并耦合面外几何 [Liu 2016, pp. 3-4]。
- 迂曲度分形模型借鉴 Yu & Cheng (2002)［59］、Yu et al. (2002)［60］的多孔介质思想，并用于单裂缝 [Liu 2016, pp. 3-4]。
- 与 Liu et al. (2015)［33］的前期固定边长模型相比，本文验证了模型在不同尺度下的适用性，并明确了 REV 尺寸与 \(D_f\) 的关系 [Liu 2016, pp. 2-3]。
- 等效渗透率对裂缝长度随机数的敏感性与 Jafari & Babadagli (2009)［20,21］关于裂缝密度和长度是最关键参数的结论一致 [Liu 2016, pp. 1-2, 10-11]。

## Open Questions

- 文中所给 \(D_T\) 的取值仅通过现场流量数据反推，如何通过岩石裂缝表面形貌测量直接标定 \(D_T\) 仍有待研究 [Liu 2016, pp. 8-9]。
- 对于 \(D_f=1.7\) 和 1.8 的高密度网络，受限于计算资源未进行渗流模拟，这些情形下的 REV 和敏感性规律是否仍成立尚不明确 [Liu 2016, pp. 5-7]。
- 模型假设所有裂缝均为张开型且 \(W=L\)，裂缝深度分布和混合断裂模式（剪切/撕裂）的影响需进一步评估 [Liu 2016, pp. 3-4]。
- 文中仅考虑了均匀随机分布的裂缝方位，天然裂缝的方向聚集性（如优势组）对等效渗透率和 REV 的影响值得探讨 [Liu 2016, pp. 4-5]。
- 未来需要将模型应用于真实场地，结合实测水力试验数据，验证并改进模型，可能引入隙宽分布、交点数等额外参数 [Liu 2016, pp. 11-12]。

## Source Coverage

所有非空的已索引文档片段均被处理。覆盖统计：按片段块计覆盖率 100%（12/12），按字符计覆盖率 99.86%（59,353 / 59,438 字符）。本次编译为单次通过 Markdown 生成，未遗漏任何提供内容。
