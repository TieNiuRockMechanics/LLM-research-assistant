---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-li-characterization-of-a-jointed-rock-mass-based-on-fractal-geometry-theory"
title: "Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory."
status: "draft"
source_pdf: "data/papers/2019 - Characterization of a jointed rock mass based on fractal geometry theory.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Li, Lichen, et al. \"Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory.\" *Bulletin of Engineering Geology and the Environment*, vol. 78, 2019, pp. 6101-6110. https://doi.org/10.1007/s10064-019-01526-x."
indexed_texts: "8"
indexed_chars: "38776"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38907"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003378"
coverage_status: "full-index"
source_signature: "d318af8719f34364184845a35ad86351f6a3af48"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:42:11"
---

# Characterization of a Jointed Rock Mass Based on Fractal Geometry Theory.

## One-line Summary

本文基于分形几何理论，通过 Schmidt 等面积投影网格化计算节理方向的分形维数，推导了节理间距与迹长的分形概率密度函数，并利用 3DEC 5.0 的 DFN 模块重建现场岩体；对比传统分布模型表明，分形方法能更准确地反映节理参数的实际分布特征。

## Research Question

岩体节理参数（方向、间距、迹长）是否普遍具有分形或幂律特征？能否利用分形几何理论建立比传统概率模型更合理的统计描述，并构建有效的离散裂隙网络（DFN）？

## Study Area / Data

- **研究区**：中国四川省某露天石灰石矿。
- **数据采集**：采用测线法，布设 12 条测线（平均长度 15 m），共测量 547 条节理，经偏差校正后保留 535 条。半迹长取测线上方部分 [Li 2019, pp. 2-3]。
- **节理分组**：利用模糊 K‑means 算法将方向数据划分为 3 组（图 2）[Li 2019, pp. 2-3]。
- **常用概率模型拟合**：
  - 方向：Fisher 分布，参数见表 1（各组 K=16.2~35.5）。
  - 间距：负指数分布，参数见表 2。
  - 迹长：负指数分布，参数见表 3。

## Methods

### 方向分形维数计算
- 网格化方法：将极点绘制于 Schmidt 下半球等面积投影，编写 VBA 程序自动生成等面积单元，统计包含极点的单元数 N 与等效边长 d，再拟合 ln(d)–ln(N) 斜率获得盒计数维数 D [Li 2019, pp. 3-4]。
- 自相似范围：本研究取 (ln4, ln6.5) [Li 2019, pp. 3-4]。

### 间距与迹长分形描述
- 基本思路：统计超过某间距（或长度）水平的节理数 N(s)，绘制 ln(N(s))–ln(s) 直线，斜率即为间距维数 D_s（或 D_l）[Li 2019, pp. 4-5]。
- 分形概率密度函数推导：
  - 由累积关系 N(s) = a·s^{-D_s} 推得 f(s) = D_s·s_{\min}^{D_s}·s^{-(D_s+1)} （迹长同理）[Li 2019, pp. 4-5]。
  - 累积概率函数：F(s) = 1 - (s_{\min}/s)^{D_s} [Li 2019, pp. 5]。
  - 适用条件：需满足 (s_{\min}/s_{\max})^{D_s} ≈ 0 [Li 2019, pp. 5]。

### DFN 建模与对比
- 数值平台：3DEC 5.0 内置 DFN 模块。
- 模型域 30 m×30 m×30 m，节理位置均匀分布。
- 参数化：
  - 方向：仍用 Fisher 分布生成。
  - 尺寸与数量：由分形迹长分布→圆盘半径（利用 l = πr/4），并依据线密度换算体积密度计算节理总数，再通过 FISH 自定义分布随机生成间距与迹长 [Li 2019, pp. 7]。
- 验证：在三维截面设置虚拟测线，比较模拟与实测的平均间距、迹长。

## Key Findings

1. **方向分形维数的信息量**：分形维数综合反映了节理数量和极点离散度，而 Fisher 常数仅反映离散度；在数据不满足 Fisher 分布时，分形维数仍可作为可靠指标 [Li 2019, pp. 3-4]。
2. **间距与迹长的分形拟合优势**：所有分组的 ln(N)–ln(s) 均呈强线性（图 5），推导的分形概率密度函数在小间距段与实测数据几乎重合，而负指数分布在小间距区明显偏离（图 6）[Li 2019, pp. 4-6]。
3. **分形 DFN 的重建能力**：生成的 3205 条节理在三维剖面上呈现随方向变化的不均匀分布，反映了岩体的不连续、非均质和各向异性；虚拟测线得到的平均间距与迹长与现场数据误差可接受（如 X‑Z 截面向距 0.42 m 对应现场 0.35 m）[Li 2019, pp. 7-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 方向分形维数的自相似范围(ln4, ln6.5)内拟合相关系数均 >0.99 | [Li 2019, pp. 3-4] | Schmidt 等面积投影，面积 A=10^5，3组极点 | 支持方向数据具有分形特征 |
| Fisher 常数最小的 Set 2 (K=16.2) 分形维数 D=0.57，而非最大；节理数最多的 Set 1 (214 条) 分形维数 D=0.62 | [Li 2019, pp. 3-4, Table 4] | 模糊 K‑means 分组；Fisher 常数越小离散度越大 | 分形维数同时受节理数量和离散度影响 |
| Set 1 间距数据分形分布与现场数据吻合，15–55 cm 段负指数分布高估比例，分形曲线几乎无偏差 | [Li 2019, pp. 5, Fig. 6] | 对比基于 Sen & Kazi (1984) 的有限测线负指数分布 | 引入 s_min 和 D_s 使小间距拟合显著改善 |
| DFN 模型生成节理数量：Set 1: 1319, Set 2: 858, Set 3: 1028，总计 3205 | [Li 2019, pp. 7] | 30×30×30 m 域，节理位置均匀 | 基于体积密度估算 |
| X‑Z 截面虚拟测线平均间距 0.42 m（实测 0.35 m），平均迹长 2.75 m（实测 3.32 m） | [Li 2019, pp. 8, Table 7] | 每条测线长度与现场一致 | 差异来源于随机生成，整体在可接受范围 |

## Limitations

- 方向数据的分形维数仅用作表征，DFN 中仍沿用 Fisher 分布生成方向，未能直接利用分形维数进行蒙特卡洛模拟 [Li 2019, pp. 8-9]。
- DFN 模型是节理网络的统计描述，并非实际重建；验证仅检验了平均间距和迹长，未考察连通性、粗糙度等其他属性 [Li 2019, pp. 8]。
- 分形间距／迹长函数的推导依赖 (s_min/s_max)^D ≈ 0 近似，若数据范围不足则该条件可能不成立 [Li 2019, pp. 5]。
- 本研究基于单一露天石灰岩矿，分形特性在其他岩体或构造区域的普适性尚未检验。

## Assumptions / Conditions

- 节理简化为薄圆盘（面积无限大），方向服从 Fisher 分布或均匀分布 [Li 2019, pp. 5-7]。
- 半迹长与圆盘半径满足 l = πr/4（体视学换算）[Li 2019, pp. 7]。
- 节理体积密度可由线密度 λ_d 经 λ_v = λ_d / (2π∫R∫f(r)drdR) 转换 [Li 2019, pp. 7]。
- 测线数据已校正方向和尺寸偏差 [Li 2019, pp. 2-3]。

## Key Variables / Parameters

- **分形维数**：D_orientation (0.52–0.62), D_spacing (1.22–1.64), D_trace (1.58–1.92) [Li 2019, Tables 4,6].
- **最小间距/长度**：s_min (3–10 cm), l_min (20–50 cm) [Li 2019, Table 6].
- **Fisher 常数**：K (16.2–35.5) [Li 2019, Table 4].
- **模型尺度**：域 30 m × 30 m × 30 m，生成域范围 ±20 m [Li 2019, pp. 7].

## Reusable Claims

1. **分形维数与 Fisher 常数的互补性**  
   “分形维数同时包含节理数量和极点离散度信息，可替代 Fisher 常数用于方向分布表征，尤其适用于不满足 Fisher 分布的数据。”  
   *条件*：采用 Schmidt 等面积网格化，自相似范围需经验确定，投影面积固定为 10^5 [Li 2019, pp. 3-4].

2. **分形间距/迹长概率密度函数**  
   “f(s) = D_s·s_min^{D_s}·s^{-(D_s+1)} 形式的分布能更精准地还原节理间距数据，尤其在低间距区间明显优于传统负指数分布。”  
   *条件*：满足 (s_min/s_max)^{D_s}≈0，数据已校正；该方法不依赖测线长度 [Li 2019, pp. 4-6].

3. **分形 DFN 重建的可行性**  
   “将分形间距/迹长分布通过自定义 FISH 函数注入 3DEC，可生成反映岩体非均质各向异性的节理网络，且模拟平均参数与实测一致。”  
   *条件*：方向仍用 Fisher 分布；尺寸换算应用 l=πr/4；体积密度由线密度积分得到 [Li 2019, pp. 7-8].

4. **分形方法的普适性提示**  
   “分形几何是刻画岩体不连续、非均质、各向异性特征的通用工具，但需确定各参数的自相似范围与最小阈值。” [Li 2019, pp. 2,8].

## Candidate Concepts

- [[fractal dimension of joint orientation]]
- [[fractal probability density function for joint spacing]]
- [[self-similarity range in rock fractures]]
- [[Schmidt equal-area meshing method]]
- [[Fisher constant vs fractal dimension]]
- [[DFN modelling with fractal distribution]]
- [[joint roughness coefficient (JRC)]]
- [[rock mass quality (RMQ)]]
- [[box-counting dimension]]
- [[Cantor dust method in fracture analysis]]
- [[negative exponential distribution for joint spacing]]
- [[Monte Carlo simulation of joint geometry]]

## Candidate Methods

- [[Schmidt projection meshing for box-counting dimension]]
- [[equal-area patch network for orientation fractals]]
- [[fractal cumulative probability transformation for random generation]]
- [[3DEC DFN generator with FISH distribution]]
- [[stereological relation (l = πr/4) for disk radius]]
- [[volume density estimation from scanline data]]
- [[fuzzy K-means clustering for joint set identification]]

## Connections To Other Work

- 方向分形维数计算沿袭 Chen et al. (2007) 的等面积网格法和 Zhan et al. (2017) 的多重分形研究 [Li 2019, pp. 3-4]。
- 分形维数与岩体质量关联：Bagde et al. (2002) 用 Schumann 分布将 RMR、UCS 与分形数关联 [Li 2019, pp. 2]。
- 分形用于节理粗糙度 (JRC) 及岩体质量 (RMQ)：Kulatilake et al. (1997, 2006) [Li 2019, pp. 2]。
- 节理间距的 Cantor 尘埃分析：Velde et al. (1991)；二维分形长度‑渗透性模型：Liu et al. (2015) [Li 2019, pp. 2]。
- 迹长‑圆盘半径关系及体积密度推导：Warburton (1980) 和 Oda (1988) [Li 2019, pp. 7]。
- 有限测线下改进负指数分布：Sen & Kazi (1984)，本研究用作对比 [Li 2019, pp. 5]。

## Open Questions

- 如何直接利用方向的分形维数生成随机产状数据？文中建议研究“平均方向+分形维数”的组合分布形式 [Li 2019, pp. 8-9]。
- 分形模型能否推广到节理粗糙度、孔径、充填物等其他几何参数？
- 不同地质条件下自相似范围是否稳定？(s_min/s_max)^D ≈ 0 的阈值普适性如何？
- 基于分形 DFN 的力学和渗流模拟是否较传统模型具有显著改进？

## Source Coverage

All 8 non‑empty indexed fragments were processed.  
- Coverage by blocks: 100% (8/8).  
- Coverage by characters: 100.34% (38907 compiled characters vs 38776 indexed characters).  
No additional sources were used.
