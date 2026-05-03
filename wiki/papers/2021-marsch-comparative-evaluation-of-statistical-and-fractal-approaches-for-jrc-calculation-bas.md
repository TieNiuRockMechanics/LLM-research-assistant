---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-marsch-comparative-evaluation-of-statistical-and-fractal-approaches-for-jrc-calculation-bas"
title: "Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces."
status: "draft"
source_pdf: "data/papers/2021 - Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.pdf"
collections:
  - "zotero new"
citation: "Marsch, Kristofer, and Tomas M. Fernandez-Steeger. \"Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.\" *Rock Mechanics and Rock Engineering*, vol. 54, 2021, pp. 1897-1917. doi:10.1007/s00603-020-02348-0. Accessed 2026."
indexed_texts: "18"
indexed_chars: "87843"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "87125"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991826"
coverage_status: "full-index"
source_signature: "00008758e9c00d7fe19216cff09dc9e0f3114695"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:02:43"
---

# Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.

## One-line Summary
基于超过40,000条自然岩石轮廓的对比分析表明，简单统计参数Z2足以可靠地确定JRC类别；分形方法（compass walking、FFT谱分析）在处理非典型轮廓时未能提供一致或更优的结果，而RMS‑COR法结果与Z2吻合，但未增加实质优势。 [Marsch 2021, pp. 1-2, 18–20]

## Research Question
是否对于任意岩石轮廓，无论采用统计方法还是分形方法，都能得到相同的节理粗糙度系数（JRC）？并且，在现存工具中，哪一种是最简单、直观且可靠的方法？ [Marsch 2021, pp. 2-3]

## Study Area / Data
- **数据来源**：六块不同岩类的岩石试样（玄武岩、花岗岩、石灰岩、片岩、砂岩），通过拉伸断裂获得新鲜表面。 [Marsch 2021, pp. 12-13]
- **表面扫描**：使用GOM ATOS结构光扫描仪获取高分辨率三维模型，分辨率约47–61点/mm²。 [Marsch 2021, pp. 12-13]
- **轮廓提取**：在每块试样上，以1 mm×1 mm网格滑动100 mm长的虚拟轮廓仪，共提取出超过40,000条轮廓，每条轮廓经过去趋势和1 mm插值处理。 [Marsch 2021, pp. 12-14]
- **粗糙度分类**：试样按ISRM (1978)分为I（粗糙台阶状）至VII（粗糙平面状），覆盖了宽广的粗糙度范围。 [Marsch 2021, pp. 12-13]

## Methods
采用了统计和分形两大类方法，均以Tatone (2009)公开的、已去趋势的1 mm采样典型轮廓作为统一参照。 [Marsch 2021, pp. 3-4, 8–9]

- **统计参数法**  
  - 以 **Z2**（轮廓一阶导数的均方根）为代表，使用 Tatone & Grasselli (2010) 的关联式：`JRC = 55.03·(Z2)^0.74 – 6.1`。 [Marsch 2021, pp. 5]  
  - 其他常用统计参数（σi、SF、Rp）已被证明与Z2高度可互换，故Z2可作为统计方法的“代理”。 [Marsch 2021, pp. 5, 8–9]

- **分形方法**  
  - **RMS‑COR法**：计算不同顶点间隔(dv)下高度差的标注差σ(dh)，在双对数坐标中拟合得Hurst指数 *H*，并将截距换算为幅度参数σδh(1 mm)；限定dv≤0.1L（L=轮廓长度）以抑制有限长度效应。 [Marsch 2021, pp. 5-6, 8–9]  
    JRC关联式：`JRC = -4.3 + 54.6·σδh(1mm) + 4.3·H`（Stigsson & Mas Ivars, 2019）。 [Marsch 2021, pp. 6]  
  - **功率谱分析（FFT）**：将轮廓转换到频域，由功率谱的斜率得 *H*，结合截距计算σδh(1 mm)，并用同一关联式求JRC。 [Marsch 2021, pp. 6-7]  
    为匹配原作者，也测试了垂直调整和64点滑动窗口（取最大σδh）等预处理方式。 [Marsch 2021, pp. 9-11, 15–17]  
  - **Compass walking**：采用Lee et al. (1990)的半径集（r=2,4,6,8,10 mm）计算分形维数 *Dcomp*，并按其二次关联式（Eq. 8）和 Turk et al. (1987) 的线性式（Eq. 9）分别估算JRC。 [Marsch 2021, pp. 7-8, 11–12]

所有算法均用Matlab实现，数据和代码已公开（Marsch, 2020）。 [Marsch 2021, pp. 3, 12, 20]

## Key Findings

1. **对典型剖面的再评估**  
   - 当对输入轮廓进行**简单去趋势并插值至1 mm**后，不同数字化的Z2值变得一致，JRC偏差可控制在0.5以内。 [Marsch 2021, pp. 8-9]  
   - RMS‑COR法在dv=0.1L时与已有参考值吻合最好；FFT谱分析对输入数据敏感，不同数字化之间差距较大；compass walking对所选半径集高度敏感，相同轮廓不同半径可导致JRC差达8‑9点。 [Marsch 2021, pp. 8-12]

2. **自然岩石轮廓上的对比**  
   - **Compass walking**：所有试样上JRC值极度离散，常覆盖整个0‑20范围，且大量产生负值，完全失效。 [Marsch 2021, pp. 14-15]  
   - **FFT谱分析**：无论采用简单去趋势、垂直调整还是64点窗口，JRC_FFT的离散度始终很大（跨度≥12.5 JRC点），且与Z2‑JRC的系统偏差不稳定。 [Marsch 2021, pp. 14-17]  
   - **RMS‑COR法**：在所有试样上，JRC_RMS‑COR均与JRC_Z2高度一致，散点紧贴1:1线，离散度极小。 [Marsch 2021, pp. 14-17]  
   - **原因剖析**：当采样间隔为1 mm时，`σδh(1mm) = Z2`；且幅度参数对JRC的贡献是Hurst指数的十余倍，因此RMS‑COR实质上是另一种统计相关，而非纯分形方法。 [Marsch 2021, pp. 17-18]

3. **总体结论**  
   - 基于典型剖面建立的分形关联，在推广到任意自然轮廓时普遍失效。唯一可靠的分形衍生方法（RMS‑COR）并不比直接使用Z2更优越。  
   - 在现有的10 cm尺度JRC估计框架下，**用Z2确定JRC类别已足够**，推荐工作流程：①测量并数字化轮廓 → ②去趋势、插值至1 mm → ③计算Z2并代入Tatone & Grasselli (2010)式。 [Marsch 2021, pp. 18-21]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Z2与JRC_Z2结果在去趋势且1 mm采样后对数字化的敏感度很低，不同数字化数据可得到一致的JRC | [Marsch 2021, pp. 8-9] | 使用Tatone (2009)、Li & Zhang (2015)、Stigsson & Mas Ivars (2019)三种典型剖面数字化的对比 | 去趋势和1 mm插值是关键预处理 |
| 对于全部六类自然岩石，JRC_RMS‑COR与JRC_Z2高度吻合，散点贴近1:1线 | [Marsch 2021, pp. 14-17, Figs. 14–16] | 轮廓去趋势、dv≤0.1L、1 mm采样 | 幅度参数σδh(1mm)与Z2等价是数学必然 |
| JRC_compass (Lee et al.) 波动极大，常超出0‑20范围，甚至出现负值 | [Marsch 2021, pp. 14-15, Fig. 14] | 半径集r=2,4,6,8,10 mm；使用Lee et al. (1990)二次关联式 | 对半径集的选择极其敏感 |
| JRC_FFT变异性大，无论何种预处理均无法消除与Z2方法的系统偏差 | [Marsch 2021, pp. 14-17, Figs. 14–16] | 测试了简单去趋势、垂直调整、64点窗口三种预处理 | 非周期性轮廓引起谱泄漏是重要因素 |
| 统计参数σi、SF、Rp与Z2高度可互换（R²≈1） | [Marsch 2021, pp. 5, 8] | 基于Tatone (2009)的典型剖面 | σi = 54.79·Z2+0.25, SF=Z2², Rp≈0.414·Z2²+0.0188·Z2+0.9991 |
| 原始典型剖面分辨率仅1 mm，数字化时采用更细采样无意义 | [Marsch 2021, pp. 2-3] | 原始剖面来自触针式轮廓仪，直径1 mm，已低通滤波 | 过高分辨率不会增加有效信息 |

## Limitations

- 原始典型剖面为触针式手工测量并图纸转绘，分辨率低、无法避免人为误差，其质量造成的固有不确定性不可量化。 [Marsch 2021, pp. 2-3]
- 所有JRC相关式均基于仅10条典型剖面拟合，可能过度拟合，且未通过大量独立机械试验校准。 [Marsch 2021, pp. 18-20]
- 本研究未进行直接剪切试验，无法评估几何JRC与实际力学响应的关系。 [Marsch 2021, pp. 20-21]
- 二维轮廓的代表性选择仍依赖主观，尚未建立客观的轮廓筛选准则。 [Marsch 2021, pp. 20-21]
- RMS‑COR法虽表现良好，但其自身也受有限长度效应影响，需要人工设定顶点区间上限。 [Marsch 2021, pp. 8-9]
- Compass walking和FFT的结果说明，分形理论在低分辨率且自仿射轮廓上的实现高度依赖于算法细节，可重复性较低。 [Marsch 2021, pp. 11-12, 18]

## Assumptions / Conditions

- 所有JRC相关性均以Barton & Choubey (1977)的10条典型剖面为基准。 [Marsch 2021, pp. 2-3]
- 为使不同方法可比较，轮廓必须**去除整体趋势**并**等间距插值至1 mm**（与原始仪器分辨率一致）。 [Marsch 2021, pp. 8-9]
- 分形方法必须同时提供幅度参数（σδh）和Hurst指数（或分形维数）才能合理约束JRC。 [Marsch 2021, pp. 5]
- RMS‑COR法采用的顶点间隔上限定为轮廓长度的10% (dv ≤ 0.1L)。 [Marsch 2021, pp. 8-9]
- Compass walking使用Lee et al. (1990)的半径集（2,4,6,8,10 mm），半径的选择对结果影响很大。 [Marsch 2021, pp. 11-12]
- 功率谱分析中，仅当采用与Stigsson & Mas Ivars (2019)一致的预处理（如垂直调整、64点窗口）时，其补偿修正公式才有意义；但本研究证明该做法未能根本改善性能。 [Marsch 2021, pp. 9-11, 15–17]

## Key Variables / Parameters

- **Z2**：轮廓的一阶导数均方根，离散形式为 √[1/(N‑1)·∑(yᵢ₊₁−yᵢ)²] / dx 。 [Marsch 2021, pp. 5]
- **JRC_Z2**：由 Z2 经 `JRC = 55.03·Z2^0.74 – 6.1` (Tatone & Grasselli, 2010) 换算。 [Marsch 2021, pp. 5]
- **σδh(dx)**：在顶点间隔 dx 下高度差的标准差；当 dx=1 mm 时 σδh(1mm) 与 Z2 数值相等。 [Marsch 2021, pp. 17-18]
- **H (Hurst 指数)**：通过 RMS‑COR 或 FFT 在双对数坐标中线性回归得到；RMS‑COR 法可能低估 H，FFT 法可能高估 H。 [Marsch 2021, pp. 5-7]
- **JRC_RMS‑COR**：`JRC = -4.3 + 54.6·σδh(1mm) + 4.3·H` (Stigsson & Mas Ivars, 2019)。 [Marsch 2021, pp. 6]
- **Dcomp (compass 分形维数)**：由 compass walking 算法得到；JRC 关联式有 `JRC = –0.87804 + 37.7844·((D−1)/0.015) – 16.9304·((D−1)/0.015)²` (Lee et al., 1990) 和线性式 `JRC = –1138.6 + 1141.6·D` (Turk et al., 1987)。 [Marsch 2021, pp. 7-8]

## Reusable Claims

1. **Z2 作为 JRC 代理的充分性**  
   “当轮廓已去趋势且采样间隔为 1 mm 时，仅使用 Z2 即可确定 JRC 类别，无需采用更复杂的分形参数。”  
   *(条件: 基于 Barton 10 条典型剖面的关联，轮廓长度 100 mm；不适用于要求高精度 JRC 的后继力学分析。)* [Marsch 2021, pp. 18-21]

2. **RMS‑COR 与 Z2 的等价性**  
   “对于 1 mm 采样的去趋势轮廓，RMS‑COR 得到的幅度参数 σδh(1mm) 数学上等于 Z2，因此 RMS‑COR 方法并不能提供超越 Z2 的额外信息。”  
   *(条件: dv 限制为 ≤0.1L，且关联式中 σδh 项的权重远大于 H 项。)* [Marsch 2021, pp. 17-18]

3. **Compass walking 不适用于自然岩石轮廓 JRC 估计**  
   “基于 compass walking 的 JRC 关联在非典型轮廓上产生极度离散、甚至负值的 JRC，该方法的适用性仅限于与拟合时相同的典型轮廓。”  
   *(条件: 半径集、关联式均沿用 Lee et al. (1990) 的设置。)* [Marsch 2021, pp. 14-15, 18]

4. **FFT 功率谱分析在 JRC 估计中的失效**  
   “仅用 FFT 功率谱分析推算 JRC 时，即使经过垂直调整或窗口化，仍无法获得与统计方法一致的可靠结果，其原因在于轮廓的非周期性导致谱泄漏。”  
   *(条件: 使用 Stigsson & Mas Ivars (2019) 的 JRC 关联式，轮廓长度 100 mm。)* [Marsch 2021, pp. 14-17, 18]

5. **预处理规范的重要性**  
   “对轮廓进行简单线性去趋势并重采样至 1 mm，是保证不同源数据 JRC 结果可比较的最低限度预处理。”  
   *(条件: 轮廓原始采样间隔不偏离 1 mm 过多。)* [Marsch 2021, pp. 8-9]

6. **典型剖面数据库的局限**  
   “所有基于 10 条典型剖面的 JRC 关联均受限于原始数据的低分辨率与稀疏性，不应被赋予超过其固有精度的 JRC 小数位。”  
   *(条件: 仅限使用 Barton & Choubey 典型剖面的关联，无后续力学检验。)* [Marsch 2021, pp. 2-3, 18–20]

## Candidate Concepts

- [[JRC]]
- [[粗糙度幅度参数 σδh]]
- [[分形维数 D]]
- [[Hurst 指数 H]]
- [[自仿射轮廓]]
- [[统计粗糙度参数 Z2]]
- [[RMS‑COR 方法]]
- [[功率谱分析 FFT]]
- [[Compass walking 方法]]
- [[轮廓去趋势]]
- [[采样间隔]]
- [[有限长度效应]]
- [[滑动窗口轮廓提取]]

## Candidate Methods

- [[Z2 计算]]
- [[Tatone & Grasselli (2010) JRC 关联]]
- [[RMS‑COR 算法]]
- [[FFT 功率谱分析]]
- [[Compass walking 分维计算]]
- [[结构光三维扫描]]
- [[100 mm 虚拟轮廓仪提取]]
- [[简单线性去趋势与 1 mm 插值]]
- [[Stigsson & Mas Ivars (2019) JRC 关联式]]

## Connections To Other Work

- **Tatone (2009)** 公开了第一条系统化去趋势的 1 mm 典型剖面数据，成为本研究及许多后续工作的基础。 [Marsch 2021, pp. 3-4]
- **Tse & Cruden (1979)**、**Yu & Vayssade (1991)** 等早期统计参数工作，其使用的 σi、SF、Rp 已被证明与 Z2 高度可互换。 [Marsch 2021, pp. 5, 8–9]
- **Lee et al. (1990)** 和 **Turk et al. (1987)** 的 compass walking 关联式在本研究被重新审视，并确认其在非典型轮廓上失效。 [Marsch 2021, pp. 7-8, 14–15]
- **Stigsson & Mas Ivars (2019)** 提出了结合 Hurst 指数与 σδh 的 RMS‑COR / FFT 两参数关联式，本研究沿用了该式并检验了其稳定性和前提。 [Marsch 2021, pp. 5-7]
- **Kulatilake et al. (2006)** 和 **Den Outer et al. (1995)** 指出了岩石节理的自仿射性质及 compass walking 的理论缺陷，本研究的数值实验给予了实证支持。 [Marsch 2021, pp. 5]
- **Magsipoc et al. (2019)** 和 **Li & Huang (2015)** 汇总了多种 2D/3D 粗糙度表征方法，为本研究提供了方法学背景。 [Marsch 2021, pp. 2, 5]

## Open Questions

- 如何客观、可重复地从三维剪切表面选取最具代表性的二维轮廓，以避免当前“主观选择代表性轮廓”带来的偏差？ [Marsch 2021, pp. 20-21]
- 需要大量几何测量与直接剪切试验的配对数据，以建立不依赖 10 条典型剖面的、有明确力学意义的 JRC 几何估计方法。 [Marsch 2021, pp. 18-20]
- 在更长或更短的测量尺度上，统计参数（如 Z2）与分形参数（如 H, σδh）的行为如何，其对 JRC 的贡献是否会改变？ [Marsch 2021, pp. 2-3, 20]
- 是否应将三维粗糙度参数（如 Grasselli & Egger, 2003）而非二维轮廓作为 JRC 估计的新基准？ [Marsch 2021, pp. 2, 20]

## Source Coverage

所有非空索引片段均已处理。共处理 **18 个片段**，总计 **87,125 个字符**，字符覆盖率 **99.18%**（基于编译后源块统计）。无遗漏信息。
