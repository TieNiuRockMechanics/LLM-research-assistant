---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1999-bour-clustering-and-size-distributions-of-fault-patterns-theory-and-measurements"
title: "Clustering and Size Distributions of Fault Patterns: Theory and Measurements."
status: "draft"
source_pdf: "data/papers/1999 - Clustering and size distributions of fault patterns Theory and measurements.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Bour, Olivier, and Philippe Davy. \"Clustering and Size Distributions of Fault Patterns: Theory and Measurements.\" *Geophysical Research Letters*, vol. 26, no. 13, 1 July 1999, pp. 2001-2004."
indexed_texts: "5"
indexed_chars: "22452"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "22125"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.985436"
coverage_status: "full-index"
source_signature: "f8666143c30a8f46206958ed98837bb4806624dd"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:44:48"
---

# Clustering and Size Distributions of Fault Patterns: Theory and Measurements.

## One-line Summary
断层系统的空间分布（分形维数 D）与尺寸分布（频率-长度指数 a）通过一个新的标度律 $x = (a-1)/D$ 相关联，该标度律描述断层与其较大最近邻断层的平均距离；在圣安德烈亚斯断层系统中的测量结果支持该关系，但不支持先前模型中的 $a = D+1$ [Bour 1999, pp. 1-1]。

## Research Question
断层网络的丛集性（分形维数 D）与断层长度分布的幂律指数（a）之间存在何种定量关系？ [Bour 1999, pp. 1-1]

## Study Area / Data
- **数据来源**: 南圣安德烈亚斯断层系统（San Andreas fault system），使用 Jennings (1988) 编制的 1:750,000 比例尺地图。  
- **范围**: 仅包括从墨西哥边境到大约北纬 35 度线之间的陆上断层。  
- **样本量**: 数字化断层共 3499 条，观测下限约 1 km。 [Bour 1999, pp. 1-2][Bour 1999, pp. 2-4]

## Methods
1. **理论推导**: 基于分形覆盖的定义（Mandelbrot, 1982），假设移除小断层后断层网络仍保持分形，推导出断层长度 l 的中心到最近较大邻居的平均距离 d(l) 与累积计数 C(l) 的关系 $d(l) \propto C(l)^{-1/D}$，并利用 $C(l) \sim l^{-(a-1)}$（$a>1$）得到 $d(l) \sim l^{x}$，其中 $x = (a-1)/D$。 [Bour 1999, pp. 1-1]
2. **数值试验**: 生成具有指定 D 和 a 的二维断层系统，测量 d(l) 并验证 $x$ 的理论预测。 [Bour 1999, pp. 1-1][Bour 1999, pp. 1-2]
3. **现场数据分析**:  
   - **分形维数 D**: 使用两点相关函数 $C_2(r) \sim r^D$ 计算。  
   - **长度分布指数 a**: 对密度分布 n(l) 和累积分布 C(l) 进行幂律拟合，并采用修正幂律模型（附录 B）以考虑有限尺寸效应（$p(l) = (A-l)^2/A^2$）。  
   - **距离标度指数 x**: 计算 d(l) 与 l 的关系，同样使用修正模型校正边界效应。  
   - **最小距离标度指数 y**: 测量断层到任意最近邻居（不论长度）的距离 $d_c(l) \sim l^y$。 [Bour 1999, pp. 1-2][Bour 1999, pp. 2-4][Bour 1999, pp. 4-4]

## Key Findings
1. **理论关系成立**: $x = (a-1)/D$，数值模拟结果与理论预测高度一致。 [Bour 1999, pp. 1-1]
2. **圣安德烈亚斯断层测量值**:  
   - 分形维数 $D = 1.65 \pm 0.05$（两点相关函数，约两个量级）。  
   - 长度分布指数 $a = 1.90 \pm 0.1$（结合密度与累积分布修正模型）。  
   - 距离标度指数 $x$：简单幂律拟合给出 $x\approx 0.6$，修正模型给出 $x=-0.56\pm0.1$（理论期望为 $0.55$）。  
   - $d(l) \sim C(l)^{-1/D}$ 关系验证，得到 $D\approx1.64$，与相关积分结果一致。 [Bour 1999, pp. 2-4]
3. **与先前模型不符**: $a = D+1$ 的关系（如 King, 1983; Turcotte, 1986）不成立，该关系对应的特殊情形 $x=1$ 未在数据中观察到。 [Bour 1999, pp. 4-4]
4. **断层位置与长度相关**: $d_c(l) \sim l^y$，其中 $y=0.25$，表明大断层的最近邻居距离更大，小断层围绕大断层呈反丛集分布，与 Ackermann & Schlische (1997) 的结果一致。 [Bour 1999, pp. 4-4]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 理论关系 $x = (a-1)/D$ 推导 | [Bour 1999, pp. 1-1] | 假设移除小断层后网络仍分形；$a>1$；$C(l)\sim l^{-(a-1)}$ | 定义 $d(l)$ 为断层中心到最近更大长度邻居的距离 |
| 二维数值模拟验证 $x$ | [Bour 1999, pp. 1-1][Bour 1999, pp. 1-2] | 生成指定 $a$ 和 $D$ 的断层分布 | 测量 $d(l)$ 标度指数与理论吻合良好 |
| 圣安德烈亚斯断层 $D$ 测量 | [Bour 1999, pp. 2-4] | 两点相关函数 $C_2(r)$；系统大小约 400 km | $D = 1.65 \pm 0.05$，范围约两个量级 |
| 圣安德烈亚斯断层 $a$ 测量 | [Bour 1999, pp. 2-4] | 密度分布 $n(l)$ 在 3–20 km 区间；修正模型考虑有限尺寸效应 | $a \approx 1.90 \pm 0.1$（修正模型 $a=1.88$ 等） |
| 圣安德烈亚斯断层 $x$ 测量 | [Bour 1999, pp. 2-4] | 简单幂律在 1–9 km 区间；修正模型全范围 | 简单模型 $x\approx 0.6$；修正模型 $x=-0.56\pm0.1$（理论值 0.55） |
| $d(l) \sim C(l)^{-1/D}$ 验证 | [Bour 1999, pp. 2-4] | 利用实测 $C(l)$ 计算 $d(l)$ | 导出 $D \approx 1.64$ |
| $d_c(l) \sim l^y$, $y=0.25$ | [Bour 1999, pp. 4-4] | 断层到任意邻居距离；数据精度有限 | 表明位置-长度正相关，大断层邻居更远 |

## Limitations
- 数据为二维大陆尺度图，三维效应未考虑。  
- 有限尺寸效应和截断效应影响幂律拟合范围，仅部分区间可用简单幂律。  
- $d_c(l)$ 的指数 $y$ 因数据不准确而谨慎对待。 [Bour 1999, pp. 4-4]
- 修正模型假设 $p(l) = (A-l)^2/A^2$ 未考虑断层方向影响。 [Bour 1999, pp. 4-4]
- 分析局限于一个断层系统，普适性待更多案例验证。 [未明确，但暗示]

## Assumptions / Conditions
- 断层中心为空间分形分布，且移除小断层后网络仍保持分形。  
- 频率-长度分布遵循幂律 $n(l) = c l^{-a}$，且 $a > 1$。  
- 系统尺寸 $A$ 远大于断层长度，边界效应用概率函数修正。  
- $d(l)$ 定义为断层中心间距离，不代表迹线距离。 [Bour 1999, pp. 1-1][Bour 1999, pp. 4-4]

## Key Variables / Parameters
- $D$：断层中心的分形维数（相关维数）。  
- $a$：长度分布密度 $n(l)$ 的指数。  
- $x$：$d(l) \sim l^{x}$ 中的指数，理论值为 $x = (a-1)/D$。  
- $y$：$d_c(l) \sim l^{y}$ 中的指数，表征位置-长度相关程度，范围 $[0, x]$。 [Bour 1999, pp. 1-2]

## Reusable Claims
1. 在假定断层网络移除小断层后仍保持分形的条件下，断层长度 $l$ 与其最近更大邻居的平均距离 $d(l)$ 服从 $d(l) \propto l^{(a-1)/D}$，其中 $D$ 为分形维数，$a$ 为长度分布的幂律指数（$a > 1$）[Bour 1999, pp. 1-1]。
2. 实验数据（圣安德烈亚斯断层）表明 $D \approx 1.65$，$a \approx 1.9$，所得 $x \approx 0.55$ 不支持 $a = D + 1$ 这一广泛引用的模型关系 [Bour 1999, pp. 4-4]。
3. $d_c(l) \sim l^{y}$ 的标度律（$y$ 介于 0 和 $x$ 之间）可检测断层位置与长度的相关性；圣安德烈亚斯断层呈现 $y \approx 0.25$，表明大断层邻居间距更大 [Bour 1999, pp. 4-4]。
4. 在分析有限区域内的断层系统时，须用 $p(l) = (A-l)^2/A^2$ 等模型修正长度分布和距离标度的边缘效应，否则常规幂律拟合可能失真 [Bour 1999, pp. 4-4]。

## Candidate Concepts
- [[fracture reservoir]]  
- [[fault clustering]]  
- [[scaling law]]  
- [[fragmentation model]]  
- [[power-law distribution]]  
- [[two-point correlation function]]  
- [[excluded volume]]  
- [[anticlustering of small faults]]

## Candidate Methods
- [[correlation integral for fractal dimension]]  
- [[modified power-law model for edge effects]]  
- [[nearest-neighbor distance scaling analysis]]  
- [[numerical generation of fractal fault networks]]

## Connections To Other Work
- **先前理论模型**: King (1983) 和 Turcotte (1986) 的碎裂模型给出 $a = D+1$，相当于 $x=y=1$；本文证明该关系不适用于圣安德烈亚斯断层。 [Bour 1999, pp. 1-1][Bour 1999, pp. 4-4]
- **Ackermann & Schlische (1997)**: 发现小断层在大断层周围反丛集，本文的 $y>0$ 与此一致。 [Bour 1999, pp. 4-4]
- **Davy et al. (1990; 1992)**: 讨论了分形维数与长度分布指数的关系，本文引入了新的距离标度律。 [Bour 1999, pp. 1-1]
- **Cowie et al. (1995)**: 模拟断层生长过程，但此前 a 与 D 的关系研究不足。 [Bour 1999, pp. 1-1]

## Open Questions
- 如何将此类标度关系推广到三维断层网络？ [Bour 1999, pp. 4-4]
- 标度律的力学成因——断层系统动力学中的相互作用如何导致 $x$ 和 $y$ 的具体数值？ [Bour 1999, pp. 4-4]
- 其他断层带（如不同构造背景）是否满足同样的 $x = (a-1)/D$ 关系？ [未明确]
- $d_c(l)$ 指数 $y$ 的精确测定及其物理解释。 [Bour 1999, pp. 4-4]

## Source Coverage
所有非空索引片段均已处理。  
- 索引文本块数：5  
- 索引字符总数：22452  
- 编译后源码块数：5  
- 编译后源码字符数：22125  
- 片段覆盖率（按块计）：100%  
- 片段覆盖率（按字符计）：98.54%  
- 源文件签名：f8666143c30a8f46206958ed98837bb4806624dd  
- 编译策略：单次通行 Markdown 汇编
