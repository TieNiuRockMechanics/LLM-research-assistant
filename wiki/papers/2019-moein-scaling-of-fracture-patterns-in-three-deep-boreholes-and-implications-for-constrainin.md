---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin"
title: "Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models."
status: "draft"
source_pdf: "data/papers/2019 - Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.pdf"
collections:
  - "1文章:2D-3D分形关系"
  - "2文章钻孔裂缝分形关系"
citation: "Moein, Mohammad Javad Afshari, et al. \"Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.\" *Rock Mechanics and Rock Engineering*, vol. 52, 2019, pp. 1723-1743. DOI: 10.1007/s00603-019-1739-7."
indexed_texts: "19"
indexed_chars: "93064"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "92203"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990748"
coverage_status: "full-index"
source_signature: "242cc2dd388478692ea23f79439a42f6f8a3532b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:27:23"
---

# Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.

## One-line Summary
提出一种生成一、二、三维[[分形离散裂隙网络]]的方法，该网络遵循双幂律模型；通过合成网络和三个深钻实测数据，证明二维点相关函数是估算一维裂隙分布分形维数的最稳定方法，且仅凭钻孔一维裂隙间距无法约束二维/三维网络的分形标度参数。

## Research Question
如何可靠地量化深钻孔中一维裂隙间距的分形标度特性？从一维钻孔裂隙数据能否以及如何约束二维和三维裂隙网络的[[分形维数]]（相关维数 \(D\) 和长度指数 \(a\)）？

## Study Area / Data
- **巴塞尔**（瑞士）Basel‑1 井（5 km 深），基底为 monzogranite（Häring et al. 2008），裂隙总数为 1164 条，识别出 6 个优势组（Ziegler et al. 2015）。[Moein 2019, pp. 13-14, Table 1]
- **苏尔茨苏福雷**（法国）GPK3 和 GPK4 井（各约 5 km 深），基底为 porphyric monzogranite 和 two‑mica granite，裂隙总数分别为 1926 和 2115 条，各识别 7 个优势组（Valley and Genter 2007; Ziegler et al. 2015）。[Moein 2019, pp. 14-16, Table 2]
- 数据来源：声波钻孔成像测井，裂隙通过正弦波拟合提取，深度转换为真垂直深度（TVD）。[Moein 2019, pp. 13-14]
- 分析仅考虑前四个最发育的裂隙组，其余组合裂隙数过少无法进行分形分析。[Moein 2019, pp. 15-16]

## Methods
- **合成裂隙网络生成**：采用乘性级联过程（Multiplicative Cascade process）在 1D/2D/3D 域中生成服从[[双幂律模型]] \(n(l, L)dl = \alpha L^D l^{-a} dl\) 的裂隙分布，其中 \(D\) 为裂隙中心的相关维数，\(a\) 为长度指数。流程包括分形密度场生成（通过概率乘性过程）、随机赋位（离散逆变换法）和根据长度指数分配长度。[Moein 2019, pp. 3-6]
- **边界效应处理**：对超出域的裂隙采用“完全移除”或“截断（trimming）”两种方式，分析其对相关函数和长度分布的影响。[Moein 2019, pp. 6-8]
- **分形维数估算技术对比**：在已知 \(D_{1D}=0.75\) 的合成一维裂隙分布上，对比[[二维点相关函数]]（two‑point correlation function）、[[盒计数法]]（box‑counting）和裂隙间距的[[幂律分布拟合]]三种方法。[Moein 2019, pp. 12-14]
- **一维分形维数估算**：对 Basel‑1、GPK3 和 GPK4 的全部裂隙及按组分别计算两两点相关函数 \(C(r) = \frac{2}{N_t(N_t-1)} N_p(r) \sim r^D\)，在 log‑log 图上取局部斜率作为 \(D_{1D}\)，窗口宽 25 点，无重叠滑动，每十倍程取四个斜率值。最佳拟合水平线区间取 2–200 m（或更大）作为分形段。[Moein 2019, pp. 14-16]
- **体视学分析**：在 2D（512 m × 512 m）和 3D（500 m 域）合成 DFN 上，沿密集扫描线（间距 1 m）计算一维相关维数 \(D_{1D}\)，并探讨其与 \(D_{2D}\)/\(a_{2D}\) 或 \(D_{3D}\)/\(a_{3D}\) 的理论关系（Darcel et al. 2003b 公式）的吻合性。[Moein 2019, pp. 9-12]

## Key Findings
- **二维点相关函数是唯一可靠的一维分形维数估算方法**：在对已知 \(D_{1D}=0.75\) 的合成数据测试中，盒计数法无恒定斜率区；间距幂律分布仅出现短平台且范围远小于一个量级；相关函数给出清晰、稳定且与输入一致的分形维数。[Moein 2019, pp. 13-14]
- **几何边界处理对相关维数影响小，但截断能更好保留长度分布的幂律特征**：移除或截断超出域的裂隙对 2D 网络的相关函数及斜率影响不大，但移除会显著耗尽所有尺度的长度分布，截断仅使长度分布在大裂隙处偏离。[Moein 2019, pp. 6-8]
- **三个深钻孔裂隙分布均为分形，且尺度跨越至少两个量级**：
  - 全裂隙数据集：\(D_{1D}\) 在 Basel‑1 为 0.86±0.03（2–200 m），GPK3 为 0.88±0.02（2–1000 m），GPK4 为 0.87±0.06（2–1000 m）。[Moein 2019, pp. 16, Table 3]
  - 分优势组分析：各井前四个组 \(D_{1D}\) 在 0.65–0.75 之间，分形段仍至少跨越两个量级。[Moein 2019, pp. 15-16, Table 3]
- **苏尔茨两口井相距很近（上部 1 km 仅 30 m），但 \(D_{1D}\) 在垂向和横向上近似恒定，表明岩体裂隙网络的分形特性在取样范围内是均匀的**。[Moein 2019, pp. 18-19]
- **无法从一维钻孔数据反演二维或三维分形标度参数**：
  - 对 2D 合成网络：当 \(a_{2D} \leq 2\) 且 \(D_{2D} \geq a_{2D}\) 时，扫描线给出 \(D_{1D} \approx 1\)，符合理论式 (15)；但当 \(D_{2D} \leq a_{2D}\) 时，实测 \(D_{1D}\) 与理论式 (16) 偏差显著。\(a_{2D}=2.5\) 时，\(D_{1D}\) 对所有 \(D_{2D}\) 均高估理论式 (17)。裂隙具有优势方位时，结论相同。[Moein 2019, pp. 9-10, 12]
  - 对 3D 合成网络（\(a_{3D}=3.5\)）：无论 \(D_{3D}\) 取值，扫描线 \(D_{1D}\) 平均接近 1，无法区分不同的 \(D_{3D}\)，即使已知长度指数。[Moein 2019, pp. 12]
- **合成一维分形裂隙间距生成的乘性级联过程验证了方法合理性**：1D 概率场生成后，采用离散逆变换随机赋点，无需分配长度。[Moein 2019, pp. 12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 合成 1D 数据 (D=0.75) 仅两点相关函数给出正确且稳定的分形维数；盒计数法无平台，间距幂律法平台短而不明显 | [Moein 2019, pp. 12-14] | 1D 合成扫描线长 512 m，1000 个随机点，乘性级联生成 | 图 8 展示了三种方法的对比 |
| 边界处理对相关维数影响小：移除或截断超出域的裂隙，相关函数斜率仍接近预设 D=1.5；截断更有利于保持长度分布的幂律形态 | [Moein 2019, pp. 6-8, 图 4] | 2D 域 100 m × 100 m，a=1.5 或 2.5，D=1.5 | 移除会使长度分布全尺度偏离；截断只在大裂隙处偏离 |
| Basel‑1 全部裂隙 D1D=0.86±0.03 (范围 2‑200 m)；GPK3: 0.88±0.02 (2‑1000 m)；GPK4: 0.87±0.06 (2‑1000 m) | [Moein 2019, pp. 16, 图 14, Table 3] | 分析方法：两点相关函数，窗口 25 点，最佳水平线拟合 | 分形段至少两个量级 |
| 三个钻孔中分优势组后的 D1D 值在 0.65–0.75 之间 (如 Basel‑1 Set1: 0.75±0.08，Set3: 0.65±0.16)，仍跨至少两个量级 | [Moein 2019, pp. 15-16, Table 3] | 每组仅用该组裂隙，TVD，相关函数法 | 裂隙数少的组未分析 |
| 3D DFN 的体视实验：D1D 平均≈1，无法反推 D3D | [Moein 2019, pp. 12, 图 7] | a3D=3.5，随机方位，D3D 在 2.1‑2.9 变化 | 图 7 显示 D1D 接近 1 且与 D3D 变化无显著关系 |
| 2D 体视实验：当 a2D≤2 且 D2D≥a2D 时 D1D≈1；D2D<a2D 时 D1D 偏离理论式；当 a2D>2 时 D1D 普遍高估 | [Moein 2019, pp. 9-10, 图 6] | 随机方位和两正交方位结果一致，α 调整以保持足够数量裂隙 | 图 6a,b,c,d 显示偏离情况 |
| Levy‑Lee 飞行法生成的 DFN 输出 D 与输入不一致，不适合应用 | [Moein 2019, pp. 4] | 因有限域效应（Darcel 2002） | 本研究采用乘性级联法 |

## Limitations
- 仅凭一维钻孔数据无法唯一确定 2D 或 3D 的分形标度参数（D 和 a），即使长度指数已知，反演仍严重欠定。[Moein 2019, pp. 19-20]
- 体视学分析基于特定的合成网络生成规则（乘性级联 + 双幂律模型），未考虑裂隙间的力学相互作用。[Moein 2019, pp. 19]
- 钻孔裂隙数据集可能受成像分辨率限制，过于细小的裂隙未被识别，可能影响分形区间的下限。[Moein 2019, pp. 13]
- 分形维数估算依赖于选取的分形区段，文中虽给出最佳拟合水平线，但斜率仍有一定波动。[Moein 2019, pp. 15-16]
- 优势组分析仅针对每组的前四组，其他组裂隙数过少不能可靠分析。[Moein 2019, pp. 15] 
- 合成数据中边界处理仅测试了移除和截断两种方式，未考虑周期性等其他处理方法。[Moein 2019, pp. 6-8]

## Assumptions / Conditions
- 裂隙网络可视为分形对象，其空间分布和长度分布分别由相关维数 \(D\) 和长度指数 \(a\) 描述，且服从双幂律模型（Davy et al. 1990）。[Moein 2019, pp. 3]
- 在生成合成 DFN 时，长度指数 \(a\) 取值范围为 1.3‑3.5，2D 相关维数 \(D\) 为 1‑2，3D 的 \(D\) 参考未报道值，取值 2.1‑2.9。[Moein 2019, pp. 3-4, 9‑10]
- 钻孔裂隙数据的分形分析未区分裂隙是否充填、是否导水，仅基于几何位置。[Moein 2019, pp. 14]
- 合成网络的裂隙方位先假设为随机，后补充测试了正交方位，以验证普遍性。[Moein 2019, pp. 10]
- 分形维数估算时，两点相关函数在 log‑log 图上的局部斜率由 25 点窗口无重叠滑动计算，每十倍程取四个值，最佳拟合水平线对应的范围视为分形段。[Moein 2019, pp. 15]

## Key Variables / Parameters
- \(D\)（相关维数）：描述裂隙中心空间聚簇程度；2D 中取值范围 1‑2，3D 中 >2；合成验证时 2D 取值 1.1‑1.9，3D 取值 2.1‑2.9。[Moein 2019, pp. 3, 9, 12]
- \(a\)（长度指数）：控制裂隙长度分布幂律的指数，值越大，小裂隙比例越高；合成分析取 1.5、2.5 和 3.5。[Moein 2019, pp. 3, 6, 9, 12]
- \(l_{\min}\)（最小裂隙长度）：由域尺寸 \(L\) 和迭代次数 \(n\) 确定，\(l_{\min}=L/2^n\)，用于限制迭代次数和总裂隙数。[Moein 2019, pp. 4]
- \(\alpha\)（裂隙密度常数）：标度常数，与 D 和 a 共同决定裂隙总数 \(N_t = \frac{\alpha}{a-1} L^D l_{\min}^{-(a-1)}\)。[Moein 2019, pp. 4]
- \(D_{1D}\)：沿钻孔或扫描线的一维裂隙交点分布的相关维数；实测值：全部裂隙 0.86‑0.88，分组的 0.65‑0.75。[Moein 2019, pp. 16, Table 3]
- \(C(r)\)：两点相关函数，由裂隙中心间距小于 \(r\) 的对数比例定义，计算时取对数均匀分布的 \(r\)。[Moein 2019, pp. 3-4]

## Reusable Claims
以下主张可直接用于科学写作，但需结合本研究的条件和局限性：
- [[二维点相关函数（two‑point correlation function）]]是估计一维钻孔裂隙分布分形维数最稳定、最可靠的方法，优于盒计数法和间距幂律分布拟合法 [Moein 2019, pp. 13-14]。
- 在巴塞尔和苏尔茨深钻孔中，所有裂隙的 \(D_{1D}\) 介于 0.86–0.88 之间，按优势组分析 \(D_{1D}\) 在 0.65–0.75 之间，均呈现至少两个量级的幂律标度，表明这些岩体中的裂隙网络具有分形组织 [Moein 2019, pp. 16, Table 3]。
- 即使已知裂隙长度指数 \(a\)，也无法从一维钻孔裂隙间距的相关维数唯一地推断二维或三维网络的标度参数（\(D_{2D}, a_{2D}\) 或 \(D_{3D}, a_{3D}\)）[Moein 2019, pp. 12, 19‑20]。
- 在生成分形 DFN 时，采用乘性级联过程结合离散逆变换法可产生严格满足双幂律模型的网络，且输出相关维数经两点相关函数验证与输入一致 [Moein 2019, pp. 5-7]。
- 对合成二维 DFN，将超出域边界的裂隙截断（trimming）较完全移除更能保持长度分布的幂律性质，同时相关维数几乎不受影响 [Moein 2019, pp. 6-8]。
- 在 2D 合成网络上，扫描线导出的 \(D_{1D}\) 与 \(a_{2D}\) 和 \(D_{2D}\) 的关系仅在部分区间符合 Darcel et al. (2003b) 的理论式，而在其他区间存在过渡区或系统性偏离，该结论不依赖裂隙方位 [Moein 2019, pp. 9-10]。
- 生成一维分形点分布时，可简化乘性级联过程：只需两个初始概率，每次迭代分割为两个子域，无需考虑长度分配 [Moein 2019, pp. 12]。

## Candidate Concepts
- [[分形离散裂隙网络（Fractal DFN）]]
- [[双幂律模型（Dual power-law model）]]
- [[相关维数（Correlation dimension）]]
- [[长度指数（Length exponent）]]
- [[两点相关函数（Two-point correlation function）]]
- [[乘性级联过程（Multiplicative cascade process）]]
- [[盒计数维数（Box-counting dimension）]]
- [[裂隙间距幂律分布（Fracture spacing power-law）]]
- [[体视学关系（Stereological relationships）]]
- [[自组织临界性（Self-organized criticality）]]
- [[增强型地热系统（EGS）]]
- [[声波钻孔成像测井（acoustic televiewer）]]

## Candidate Methods
- [[基于乘性级联的分形DFN生成]]（1D/2D/3D）
- [[离散逆变换法（discrete inverse transform）进行点模式赋位]]
- [[两点相关函数估算分形维数（1D）]]
- [[多尺度裂隙网络体视学分析（1D→2D/3D 扫描线实验）]]
- [[几何边界处理（移除/截断）对网络统计的敏感性分析]]
- [[对数均匀取点计算相关积分]]
- [[25点无重叠滑动窗口计算局部斜率]]
- [[水平线最佳拟合确定分形段和标准差]]

## Connections To Other Work
- 本文采用的双幂律模型源自 Davy et al. (1990)，后由 Darcel et al. (2003b) 推导了 2D↔1D 和 3D↔2D 的体视学关系，本文验证了这些关系仅在部分条件下成立 [Moein 2019, pp. 3, 9‑12]。
- 与 Bour et al. (2002) 对 Hornelen 盆地 2D 露头的研究一致，两点相关函数比盒计数法更适宜揭示裂隙中心的分形特征 [Moein 2019, pp. 13, 18]。
- 与 Ledésert et al. (1993) 在 Soultz 的 EPS1 井数据对比，其报道的盒维数 0.6–0.8 与本文的相关维数 0.65–0.88 范围接近，但本文方法更稳定 [Moein 2019, pp. 19]。
- Afshari Moein et al. (2018a, 2018b) 提出的基于应力波动和诱导微震的分形成像方法，可作为补充信息以约束裂隙网络的三维标度 [Moein 2019, pp. 2-3, 19]。
- 文中提及的合成 DFN 生成方式与 Harthong et al. (2012) 和 Verscheure et al. (2012) 的乘性级联实现一致，但本文给出了详细的随机赋值步骤 [Moein 2019, pp. 4-5]。

## Open Questions
- 能否将力学相互作用（如应力阴影效应）引入裂隙网络生成，从而获得更真实的第二阶关系？目前的模型仅为一阶，未包含 D 和 a 的内在联系 [Moein 2019, pp. 3, 19]。
- 钻孔分形维数 \(D_{1D}\approx 0.86-0.88\) 是否意味着裂隙网络接近“饱和”状态？其与裂隙生长过程和应力波动的定量关系仍不清楚 [Moein 2019, pp. 18-19]。
- 除了诱导地震的空间分布外，还有哪些可观测信息（如钻孔破坏反映的应力涨落）可用于改善一维数据对三维网络标度的约束？[Moein 2019, pp. 19]
- 在不同构造环境和岩性中，一维裂隙分形维数的普遍性如何？是否需要更大规模的深钻孔和地下实验室数据验证？[Moein 2019, pp. 20]
- 三点或多点相关方法能否从一维数据中提取更多的聚类信息，从而部分缓解欠定问题？[未明确提及，但属于自然延伸]

## Source Coverage
所有 19 个非空索引片段均已处理，编译源字符数 92,203，总索引字符数 93,064，分块覆盖率 100%，字符覆盖率 99.07%。本文档仅基于上述片段构建，未引入片段外信息。
