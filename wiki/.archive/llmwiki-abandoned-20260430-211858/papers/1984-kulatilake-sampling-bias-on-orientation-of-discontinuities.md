---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "1984-kulatilake-sampling-bias-on-orientation-of-discontinuities"
title: "Sampling Bias on Orientation of Discontinuities."
status: "draft"
source_pdf: "data/papers/1984 - Sampling bias on orientation of discontinuities.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Kulatilake, P. H. S. W., and T. H. Wu. \"Sampling Bias on Orientation of Discontinuities.\" *Rock Mechanics and Rock Engineering*, vol. 17, 1984, pp. 243–253."
indexed_texts: "3"
indexed_chars: "12155"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T10:36:14"
---

# Sampling Bias on Orientation of Discontinuities.

## One-line Summary
论文提出了一种考虑不连续面有限尺寸的定向采样偏差几何校正方法，将节理视为薄圆盘，推导其与垂直矩形窗口的交切概率，并通过实例表明该校正量可能很小 [Kulatilake 1984, pp. 1–11]。

## Research Question
如何在节理定向调查中，针对有限尺寸的不连续面（而非无限大平面）与有限暴露窗口的交切概率，修正由此引入的观测频率偏差？ [Kulatilake 1984, pp. 1–5]

## Study Area / Data
未从索引片段中确认具体野外数据来源地点，但参考文献中提及了俄亥俄州的 Conemaugh 组页岩 (Condit 1912; Williams 1982)。片段中仅提到“for the same pair of observations”给出了一个计算示例（如倾角30°、倾角方向170°），并提及表2中列出了各观测方向的校正后数量和频率，但原始观测数据本身未在片段中提供 [Kulatilake 1984, pp. 10–11]。

## Methods
1. **不连续面模型**：将节理视为直径为 \(D\) 的薄圆盘，其方向由倾角 \(\theta\) 与倾角方向 \(\alpha\) 定义 [Kulatilake 1984, pp. 1–5]。
2. **采样面**：垂直的矩形窗口，宽 \(w\)、高 \(h\) [Kulatilake 1984, pp. 1–5]。
3. **概率推导**：交切概率与圆盘中心为使圆盘与窗口相交所需的体积成正比。通过几何分析，得到圆盘与窗口相交的概率表达式（式14–15），并针对圆盘倾向位于窗口面两侧的两种情况给出修正公式（式18–19） [Kulatilake 1984, pp. 5–10]。
4. **简化情况**：当窗口尺寸远大于圆盘直径（\(h/D\to\infty\)，\(w/D\to\infty\)）时，概率简化为与 \(D(\cos^2\theta\sin^2\beta+\cos^2\beta)^{1/2}\) 成正比，其中 \(\beta\) 取决于走向与窗口的相对方位 [Kulatilake 1984, pp. 5–10]。
5. **偏差校正**：定义加权函数 \(W\)，用于修正观测方向频率。实例中计算了不同 \(D/h\) 比值下的无偏频率 [Kulatilake 1984, pp. 10–11]。

## Key Findings
- 对于文中所用的观测数据，偏差校正量很小，校正后的相对频率对 \(D/h\) 在 1 到 0 范围内的变化不敏感 [Kulatilake 1984, pp. 10–11]。
- 示例中，当 \(D/h\to0\) 时，倾角30°、倾角方向170°的加权系数为1.15，无偏频率仅从0.999变为0.029（基于总数40.3），整体影响有限 [Kulatilake 1984, pp. 10–11]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|-------------|-------|
| 圆盘与垂直矩形窗口相交的概率正比于体积，得到概率表达式 (15) 及对两种定向情况的公式 (18) | [Kulatilake 1984, pp. 5–10] | 圆盘直径为 \(D\)，窗口宽 \(w\)、高 \(h\)；圆盘中心位置均匀随机分布 | 推导基于几何体积比，未考虑截断或遮挡效应 |
| 当 \(h/D\to\infty\)，\(w/D\to\infty\) 时，概率简化形式为 \(D(\cos^2\theta\sin^2\beta+\cos^2\beta)^{1/2}\) 及相关变体 | [Kulatilake 1984, pp. 5–10] | 窗口尺寸远大于圆盘尺寸 | 该简化形式可作为大窗口下的近似加权函数 |
| 实例中加权函数 \(W(30^\circ,170^\circ, D, h/D\to\infty, w/D\to\infty)\) = 1.15，无偏数量为观测值乘以此系数 | [Kulatilake 1984, pp. 10–11] | 基于特定观测数据（可能为页岩节理） | 校正前后频率变化小 |

## Limitations
- 仅考虑垂直矩形采样窗口，未处理水平或倾斜窗口的情况 [Kulatilake 1984, pp. 1–11]。
- 不连续面被严格假定为薄圆盘，未检验其他形状（如多边形、椭圆）的适用性 [Kulatilake 1984, pp. 1–5]。
- 推导基于圆盘中心位置在空间内均匀分布的假设，未考虑成簇或非均匀分布 [未从索引片段中确认]。
- 实例中偏差影响较小，但结论可能强烈依赖于具体的数据集方向分布，普适性未经验证。
- 未考虑多重遮掩、截断或仅出露部分节理迹线等实际测量限制。

## Assumptions / Conditions
- 不连续面可模型化为薄圆形盘，直径 \(D\) 有限 [Kulatilake 1984, pp. 1–5]。
- 采样面为一理想的垂直矩形平面窗口 [Kulatilake 1984, pp. 1–5]。
- 圆盘中心位置在三维空间内均匀随机分布，交切概率与中心所在的体积成正比 [Kulatilake 1984, pp. 1–5]。
- 推导针对两种相对定向情况（倾向在窗口面的一侧或另一侧）分别给出公式 [Kulatilake 1984, pp. 5–10]。

## Key Variables / Parameters
- \(D\)：圆盘直径。
- \(\theta\)：圆盘的倾角。
- \(\alpha\)：圆盘的倾角方向（或与之相关的 \(\beta\)，\(\beta\) 取决于走向与窗口平面的几何关系）。
- \(w\)，\(h\)：矩形窗口的宽度和高度。
- \(W(\theta,\beta,D,h,w)\)：加权函数，用于校正观测方向频率，在无限大窗口极限下简化 [Kulatilake 1984, pp. 10–11]。

## Reusable Claims
1. 有限直径圆形节理与垂直矩形窗口的交切概率，在窗口尺寸远大于圆盘直径时，只与 \(D\) 和角度组合 \((\cos^2\theta\sin^2\beta+\cos^2\beta)^{1/2}\) 成正比，而不依赖于窗口尺寸 [Kulatilake 1984, pp. 5–10, eq. 17]。  
2. 当圆盘倾向位于采样面某一侧时，需采用 \([ \cos^2\theta\sin^2\beta+\cos^2\beta ]^{1/2}\) 对应的公式；若倾向位于另一侧，加权函数形式会变化为 \([ \cos^2\theta\cos^2\beta+\sin^2\beta ]^{1/2}\) [Kulatilake 1984, pp. 5–10]。  
3. 在实际页岩节理数据中应用此偏差校正后，发现校正量很小，说明在该数据集上 Terzaghi 型的方向偏差并不显著，且相对频率对 \(D/h\) 比率不敏感 [Kulatilake 1984, pp. 10–11]。

## Candidate Concepts
- [[sampling bias]]
- [[discontinuity orientation]]
- [[joint survey correction]]
- [[geometric probability]]
- [[circular disc model]]
- [[finite size joint]]
- [[exposure window effect]]

## Candidate Methods
- [[weighting function correction]]
- [[Terzaghi correction]]
- [[probability of intersection derivation]]
- [[thin disc intersection model]]

## Connections To Other Work
- 本文沿袭了 Terzaghi (1965) 对无限大平面不连续面的定向偏差校正思路，但将其扩展到有限尺寸的圆盘形不连续面 [Kulatilake 1984, pp. 1–5]。
- 文中引用 Baecher et al. (1977) 和 Bridges (1976) 的圆盘节理模型，以及 Glynn et al. (1978) 的泊松平面模型，作为将节理视为圆盘或平面的背景 [Kulatilake 1984, pp. 1–5]。
- 未从索引片段中确认与其他校正方法（如基于迹线长度的偏差修正）的直接对比，但可从主题上连接到涉及 [[scanline sampling bias]] 和 [[window sampling]] 的方法。

## Open Questions
- 对于非垂直窗口（如水平或倾斜露头面）的偏差如何校正？[未从索引片段中确认]
- 圆盘直径的分布（而非仅固定直径）会如何影响加权函数？[未从索引片段中确认]
- 当节理形状偏离圆形（如实测为多边形或不等轴椭圆）时，推导公式是否仍然适用？[未从索引片段中确认]
- 文中所用实验数据集的具体方向分布和样本量是多少，校正是否对不同的方向分布都保持微小？[未从索引片段中确认]

## Source Coverage
本页面全部信息来自三个索引片段，覆盖了论文的引言、概率推导过程（式1–19）以及一个数值校正示例。片段未包含完整的观测数据表（只有表2的片段推导）、详细的讨论部分，也未涉及该方法对其他几何属性（如迹长、间距）偏差的处理。因此，关于数据集的完整背景、与其他偏差校正方法的系统比较，以及在实际岩体工程中的应用建议等重要内容，均未能从索引片段中确认。
