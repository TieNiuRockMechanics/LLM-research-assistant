---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
title: "A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC."
status: "draft"
source_pdf: "data/papers/2010 - A new 2D discontinuity roughness parameter and its correlation with JRC.pdf"
collections:
  - "zotero new"
citation: "Tatone, Bryan S. A., and Giovanni Grasselli. “A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC.” *International Journal of Rock Mechanics & Mining Sciences*, vol. 47, 2010, pp. 1391–1400. doi:10.1016/j.ijrmms.2010.06.006."
indexed_texts: "9"
indexed_chars: "40328"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T13:14:13"
---

# A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC.

## One-line Summary
提出一个基于二维剖面线段倾角累积分布的粗糙度参数 $\theta^*_{max}/(C+1)_{2D}$，并通过与 Barton 标准 JRC 剖面的比较建立二者之间的经验关系。

## Research Question
- 如何将 Grasselli 等人发展的三维不连续面粗糙度评估思想系统地移植到二维剖面，形成一个可计算的 2D 粗糙度参数？[Tatone 2010, pp. 1-2]
- 由多个方向的二维剖面获得的“伪 3D”粗糙度值与完整的三维分析结果之间的一致性与偏差如何？[Tatone 2010, pp. 1-2]
- 新的二维粗糙度参数与工程中广泛使用的节理粗糙度系数 (JRC) 是否存在稳定的经验关系？[Tatone 2010, pp. 1-2]

## Study Area / Data
- **二维‑三维对比数据**：一块 200 mm × 200 mm 的石灰岩拉伸断裂面，从数字化表面提取 6 组、每组 11 条、间距 30° 的二维剖面 [Tatone 2010, pp. 3-5]。
- **JRC 标定数据**：Barton 与 Choubey 的 10 条标准 JRC 剖面（JRC 值 0.4～18.7）[Tatone 2010, pp. 5-8]。剖面经 1200 DPI 扫描后，在 AutoCAD 中以 0.5 mm 间隔重新数字化，对齐至最佳拟合线水平 [Tatone 2010, pp. 5-8]。
- 现场原位数据**未从索引片段中确认**。

## Methods
- **二维粗糙度评估方法**（与 Grasselli 三维方法同构）[Tatone 2010, pp. 2-3]：
  1. **剖面获取**：直接使用剖面梳或从三角不规则网络 (TIN) 表面模型中提取。
  2. **剖面对齐**：对每个剖面进行最佳拟合线性回归，旋转使其回归线水平，以此建立测量倾角的基线。
  3. **剖面分析**：计算剖面中线段在给定倾角阈值 $\theta^*$ 以上的归一化长度 $L_{\theta^*}$。
  4. **粗糙度度量**：采用非线性最小二乘回归拟合累积分布 $L_{\theta^*} = L_0 \left( \frac{\theta^*_{max}}{\theta^*} \right)^C$，得到两个参数 $\theta^*_{max}$（最大视倾角）与 $C$（形状拟合参数），以 $\theta^*_{max}/(C+1)_{2D}$ 作为每个方向的二维粗糙度指标 [Tatone 2010, pp. 3-3]。
- **二维与三维比较**：将多个方向的二维粗糙度值绘制在极坐标图上，构成伪 3D 粗糙度估计，再与同一表面由三维方法得到的值进行比较 [Tatone 2010, pp. 3-5]。
- **JRC 关联建立**：以 0.5 mm 和 1.0 mm 两种采样间隔重新数字化标准剖面后，分别计算统计参数 $Z_2$ 与 $R_P$，并拟合 JRC‑$Z_2$ 和 JRC‑$R_P$ 的经验方程 [Tatone 2010, pp. 5-8]。
  - 0.5 mm 间隔：$JRC = 51.85 (Z_2)^{0.60} - 10.37$  
  - 1.0 mm 间隔：$JRC = 55.03 (Z_2)^{0.74} - 6.10$  
  - $R_P$ 的关系见原式 (6)、(7)，此处不重复 [Tatone 2010, pp. 5-8]。
- 进一步计算各标准剖面在两个方向下的 $\theta^*_{max}/(C+1)_{2D}$ 值（见表 2 和表 3），作为建立与 JRC 直接经验关系的基础 [Tatone 2010, pp. 8-9]。具体的 $\theta^*_{max}/(C+1)_{2D}$‑JRC 回归方程**未从索引片段中确认**。

## Key Findings
- 所提出的 $\theta^*_{max}/(C+1)_{2D}$ 可从任意二维剖面单向或双向量化粗糙度，其定义完全模拟 Grasselli 的三维参数 [Tatone 2010, pp. 3-3]。
- 利用多方向二维剖面获得的伪 3D 粗糙度估计与三维总体结果定性一致，但存在不可忽视的偏差 [Tatone 2010, pp. 3-5]。
- 二维剖面可能完全遗漏未被剖面线穿过的关键表面特征，从而导致粗糙度、各向异性以及相对剪切阻力的错误表征 [Tatone 2010, pp. 5-5]。
- 即使在同一方向上邻近的剖面，粗糙度值也可能同时高估或低估真实三维值，因此建议每个方向采集多条剖面，并以均值与上下界的形式报告 [Tatone 2010, pp. 5-5]。
- 基于重新数字化的标准 JRC 剖面所得的 $Z_2$‑JRC 和 $R_P$‑JRC 经验方程，与已有文献中的同类关系高度吻合 [Tatone 2010, pp. 5-8]。
- 标准剖面在不同方向下计算的 $\theta^*_{max}/(C+1)_{2D}$ 值与 JRC 标称值之间存在明显的单调相关趋势（见表 2、表 3），可支撑建立经验关联的可行性，但具体回归关系**未从索引片段中确认**。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 二维粗糙度度量定义为 $\theta^*_{max}/(C+1)_{2D}$，基于 $L_{\theta^*} = L_0 (\theta^*_{max}/\theta^*)^C$ | [Tatone 2010, pp. 3-3] | 剖面已对齐至最佳拟合线水平；仅考虑无充填的清洁不连续面 | 参数 $C$ 由非线性最小二乘拟合确定 |
| 从石灰岩断裂面提取的 6×11 条二维剖面可绘制极坐标图，与三维粗糙度值直接对比 | [Tatone 2010, pp. 3-5] | 剖面来自 200 mm×200 mm 拉伸断裂面；分析方向覆盖 0° – 360° | 伪 3D 估计与真实 3D 值之间存在偏差 |
| 同一方向、相邻位置的二维剖面会同时高估或低估三维粗糙度，建议采集多条剖面并报告上下界 | [Tatone 2010, pp. 5-5] | 二维剖面只反映被横截部分的形貌；非横截特征被忽略 | 提示仅依赖少量 2D 剖面具有高风险 |
| 新拟合的 $JRC$–$Z_2$ 和 $JRC$–$R_P$ 方程与已有文献的关系密切一致 | [Tatone 2010, pp. 5-8] | 采样间隔分别为 0.5 mm 和 1.0 mm；基于重新数字化的 10 条标准剖面 | 表明重新数字化和拟合策略的可靠性 |
| 表 2 和表 3 给出了 10 条标准剖面在两个方向下的 $\theta^*_{max}/(C+1)_{2D}$ 值 (0.5 mm 和 1.0 mm 间隔) | [Tatone 2010, pp. 8-9] | 剖面已重新对齐；分析方向分为正向(左→右)和反向(右→左) | 数值随 JRC 增加整体上升，但存在方向不对称性 |

## Limitations
- 二维剖面只能表征被剖面线交切的表面形貌，未交切的重要几何特征会被完全忽略，可能导致粗糙度和各向异性的误判 [Tatone 2010, pp. 5-5]。
- 在单一方向使用少量剖面时，二维粗糙度估计可能显著高估或低估对应的三维值，即使采用多剖面平均也仅能部分缓解 [Tatone 2010, pp. 5-5]。
- 标准 JRC 剖面的原始数据由剖面梳获得，其固有水平采样间隔为 0.5 – 1.0 mm，小于此间隔的数字化不会增加真实形貌信息，甚至可能引入梳齿带来的阶跃状伪影 [Tatone 2010, pp. 5-5]。
- $\theta^*_{max}/(C+1)_{2D}$ 与 JRC 之间具体的经验回归方程**未从索引片段中确认**，现有片段仅给出了中间参数 $Z_2$、$R_P$ 与 JRC 的关系。

## Assumptions / Conditions
- 研究假设不连续面为**无充填、清洁**的硬岩节理或裂缝面，粗糙度是影响剪切强度的主导因素 [Tatone 2010, pp. 1-2]。
- 二维分析方法要求所有剖面均已通过线性回归对齐，即剖面宏观倾向被移除，所有倾角均以相对于平均平面的视倾角度量 [Tatone 2010, pp. 2-3]。
- 采用 $\theta^*_{max}/(C+1)_{2D}$ 作为综合粗糙度指标，意味着粗糙度信息的绝大部分可由 $\theta^*_{max}$ 和 $C$ 这两个参数概括，这一假定源于 Grasselli 三维方法的经验基础 [Tatone 2010, pp. 3-3]。
- 在建立与 JRC 的关系时，默认 10 条标准剖面的 JRC 值（由 Barton 与 Choubey 给出）为“真值”，且重新数字化过程未扭曲原剖面形态 [Tatone 2010, pp. 5-8]。
- 经验方程（如式 (4)–(7)）仅适用于与标准剖面相同或极其相似的采样间隔 (0.5 mm 与 1.0 mm)，**未从索引片段中确认**是否可推广至其他间隔或野外实测剖面。

## Key Variables / Parameters
- $\theta^*$：视倾角阈值（°），评价线段陡峭程度的临界角 [Tatone 2010, pp. 3-3]。
- $\theta^*_{max}$：沿分析方向的剖面最大视倾角（°），反映最陡线段的上限 [Tatone 2010, pp. 3-3]。
- $C$：无量纲拟合参数，表征视倾角累积分布的形状（曲率），通过非线性最小二乘回归求得 [Tatone 2010, pp. 3-3]。
- $\mathbf{\theta^*_{max}/(C+1)_{2D}}$：论文提出的核心二维粗糙度参数（°），综合了最大倾角与分布形状 [Tatone 2010, pp. 3-3]。
- $L_{\theta^*}$ 与 $L_0$：归一化线段长度，分别为对应某一倾角阈值和 0° 阈值时，倾角大于该阈值的线段长度占总剖面长度的比例 [Tatone 2010, pp. 3-3]。
- $\mathbf{Z_2}$：剖面一阶导数均方根，常用统计粗糙度参数 [Tatone 2010, pp. 5-8]。
- $\mathbf{R_P}$：轮廓粗糙度指标，反映剖面起伏幅度 [Tatone 2010, pp. 5-8]。
- **采样间隔**：剖面数字化或采集时的水平点间距（本文中为 0.5 mm 和 1.0 mm），显著影响粗糙度参数的绝对值及 JRC 经验方程的系数 [Tatone 2010, pp. 5-5, 5-8]。

## Reusable Claims
- 对于对齐至平均平面的无充填岩石节理二维剖面，其视倾角累积分布可以用 $L_{\theta^*} = L_0 (\theta^*_{max}/\theta^*)^C$ 良好描述，拟合得到的 $C$ 和 $\theta^*_{max}$ 共同构成粗糙度参数 $\theta^*_{max}/(C+1)_{2D}$。此参数对分析方向敏感，正向与反向可能得出不同数值。[Tatone 2010, pp. 3-3] 限制：仅针对已消除宏观起伏的二维剖面；$C$ 的拟合质量依赖于剖面长度与数据点数，且剖面必须能代表所关注方向的粗糙度。
- 采用多方向二维剖面绘制的极坐标图可以提供“伪 3D”粗糙度估计，但其数值与真实三维分析结果存在偏差，主要因为二维剖面无法感知未被其穿过的表面形貌。[Tatone 2010, pp. 3-5] 条件：需要较高密度的方向覆盖（如每 30° 一组）且各方向有多条平行剖面取均值，以降低随机误差。
- 当使用 2D 粗糙度参数进行工程评价时，必须在每个分析方向采集多条剖面，报告均值及上下界，并明确承认可能遗漏关键形貌特征的风险。[Tatone 2010, pp. 5-5] 限制：即使采用多条剖面，仍可能低估各向异性及局部的极端粗糙体。
- 若采用与原始剖面梳相同的采样间隔 (0.5 mm 或 1.0 mm) 重新数字化 Barton 标准 JRC 剖面，则基于 $Z_2$ 或 $R_P$ 的 JRC 经验方程与已有文献高度吻合，可用于该间隔下的 JRC 估计。[Tatone 2010, pp. 5-8] 前提：剖面必须按最佳拟合线水平对齐；采样间隔偏离 0.5 – 1.0 mm 时方程未经检验。
- 使用小于 0.5 mm 的采样间隔对原始剖面梳获取的剖面进行再数字化，不会恢复更精细的表面信息，反而可能计入梳齿造成的阶跃伪影，因此不宜用于提高 JRC 估计精度。[Tatone 2010, pp. 5-5] 适用条件：仅适用于从剖面梳复制的剖面图，而非现代高精度三维扫描直接获取的剖面。

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[rock discontinuity roughness]]
- [[2D profilometry]]
- [[3D surface roughness]]
- [[Barton-Bandis shear criterion]]
- [[fracture surface topography]]
- [[anisotropy of rock joints]]
- [[shear strength of rock joints]]
- [[standard JRC profiles]]

## Candidate Methods
- [[non-linear least-squares regression]]
- [[profile digitization from scanned images]]
- [[triangulated irregular network (TIN) extraction]]
- [[polar plot for directional roughness]]
- [[pseudo-3D roughness analysis]]
- [[Z2 statistical parameter]]
- [[RP roughness profile index]]
- [[linear regression alignment of profiles]]
- [[cumulative distribution of asperity inclination]]

## Connections To Other Work
- 方法直接承袭并简化自 **Grasselli** 等人的三维粗糙度评估体系 (如 $\theta^*_{max}/(C+1)$ 参数) [Tatone 2010, pp. 1-2, 9-10]。
- 标定时依赖 **Barton & Choubey** 的 10 条标准 JRC 剖面及其 JRC 定义，确保与经典 JRC 系统的兼容性 [Tatone 2010, pp. 5-5, 5-8]。
- 与基于 $Z_2$ 或 $R_P$ 的 JRC 经验关系（例如文献中早前提出的方程）进行比较，表明新拟合的方程与前期工作一致 [Tatone 2010, pp. 5-8]。
- 概念上与 [[fracture roughness parameterization]]、[[directional shear resistance]] 以及 [[quantitative rock joint description]] 等主题关联；未来可进一步与 [[full-field 3D optical measurement]] 及 [[contact area evolution during shear]] 等工作结合。

## Open Questions
- $\theta^*_{max}/(C+1)_{2D}$ 与 JRC 之间精确的回归方程形式、决定系数及适用范围**未从索引片段中确认**。
- 该二维参数在不同岩石类型、不同风化程度以及不同制样方式（天然节理 vs. 人工拉伸破坏），是否仍然与三维参数保持稳定关系，**未从索引片段中确认**。
- 当用于不规则、强烈各向异性的表面时，多剖面取均值能否充分代表真实三维粗糙度，其误差的统计分布尚不明确。
- 论文仅讨论了无剪切位移的初始表面，参数在剪切带演化过程中的变化，以及能否与 [[shear strength degradation models]] 结合，**未从索引片段中确认**。
- 若采用激光扫描或摄影测量获得更高分辨率的三维数据并从中提取剖面，采样间隔大幅变化时，现有方法是否依然适用，需要进一步检验。

## Source Coverage
本页依据论文的 **9 个索引片段** 撰写，覆盖了引言、二维方法详述、伪 3D 比较、局限性、JRC 剖面数字化与回归方程建立的主要过程。但明显缺失：  
- 完整的 $\theta^*_{max}/(C+1)_{2D}$ 与 JRC 最终经验方程及其统计指标；  
- 二维‑三维比较的全部定量结果与误差分析；  
- 讨论部分对其他影响因素（如采样长度、剖面长度、岩石类型）的深入分析；  
- 结论与对未来工作的建议。  
因此，本页对于“与 JRC 的相关性”这一核心主题，仅能提供至中间步骤的量化数据，最终关系未能从片段中复现。
