---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-kulatilake-non-stationarity-heterogeneity-scale-effects-and-anisotropy-investigations-on-na"
title: "Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method."
status: "draft"
source_pdf: "data/papers/2021 - Non-stationarity, heterogeneity, scale effects, and anisotropy investigations on natural rock joint roughness using the variogram method.pdf"
collections:
  - "zotero new"
citation: "Kulatilake, Pinnaduwa H. S. W., et al. \"Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method.\" *Bulletin of Engineering Geology and the Environment*, vol. 80, 2021, pp. 6121-43. doi:10.1007/s10064-021-02321-3. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72917"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "72269"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991113"
coverage_status: "full-index"
source_signature: "69cba5759fc45926df5b2f8072e2c871847739c5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:33:37"
---

# Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method.

## One-line Summary
利用变异函数法对 1 m × 1 m 天然岩石节理面进行粗糙度量化，揭示非平稳性影响可忽略、粗糙度非均质性主导尺度效应争议、并清晰展示剪切断裂引起的显著各向异性。

## Research Question
如何准确量化天然岩石节理的粗糙度？非平稳性、非均质性、节理尺寸及方向对基于自仿射分形的变异函数法所计算的粗糙度参数（分形维数 D 与振幅参数 Kv）有何影响？文献中关于粗糙度尺度效应的矛盾结论是否源于对表面非均质性的忽略？

## Study Area / Data
- **地点**：中国浙江省常山县青石镇和尚弄采石场（Heshangnong quarry）[Kulatilake 2021, pp. 4-6]。
- **岩性**：灰绿色板岩，原岩为奥陶系泥质灰岩轻度变质形成[Kulatilake 2021, pp. 4-6]。
- **节理面**：从板岩上切取的天然剪切断裂面，整体尺寸 1100 × 1100 mm²，研究核心区域为 1000 × 1000 mm²，以避免运输造成的边缘损伤[Kulatilake 2021, pp. 4-6]。该尺寸仅覆盖“不平整度”（unevenness）而未包含大尺度“波浪度”（waviness）[Kulatilake 2021, pp. 4-6]。
- **数据获取**：采用 Metra Scan 750 三维激光扫描系统，精度 0.030 mm，按 0.5 mm 间隔在两个正交方向（X 与 Y）数字化表面高度 Z；X 方向近似现场剪切方向；各点空间定位分辨率 ±0.10 mm[Kulatilake 2021, pp. 6-7]。共获得超过 1700 条轮廓线用于计算[Kulatilake 2021, pp. 1-2, 21-22]。

## Methods
- **粗糙度量化核心方法**：自仿射分形变异函数法（variogram method），遵循 Kulatilake 等（1998）的精细化流程[Kulatilake 2021, pp. 3-3, 6-7]：
  - 对轮廓线 Z(X)，计算滞后距 h 下的半变异函数 2γ(X,h) = E[(Z(X+h)−Z(X))²]。
  - 若早期 2γ 随 h 呈幂律 2γ = Kv·h^(2H)，则分形维数 D = 2−H，Kv 为振幅参数，并综合参数 D×Kv 衡量整体粗糙度[Kulatilake 2021, pp. 6-7]。
  - 参数计算条件：通过 h·d = 1.76 确定最小滞后距（d 为数据密度，此处 d=2 /mm），以 1.2 倍乘因子生成 7 个 h 值，要求 log(2γ)−log(h) 线性回归相关系数 R > 0.85 才确认幂律成立[Kulatilake 2021, pp. 6-7, 7-9]。
- **非平稳性检验**：对 1000 mm 与 500 mm 的 Z-Y 轮廓线，分别使用原始粗糙度数据和去除全局线性趋势后的“残差粗糙度”数据计算 D、Kv、D×Kv，比较差异。趋势角范围 −1.9° 至 +1.0°[Kulatilake 2021, pp. 7-9]。
- **非均质性分析**：在 X、Y 两个方向上按不同长度（1000、500、250、125 mm）和不同位置截段提取轮廓线，分别计算粗糙度参数，并统计均值、变幅、变异系数（CV）[Kulatilake 2021, pp. 9-11, 11-16]。
- **尺度效应分析**：将均质段（0–250 mm 与 250–500 mm 合并对比 0–500 mm 段）的结果独立比较，以消除非均质性影响；同时将各长度所有截段混合统计，以在含非均质影响下观察尺度效应[Kulatilake 2021, pp. 11-16, 16-17]。
- **各向异性与视觉粗糙度关联**：比较 X 方向（沿脊槽轴）与 Y 方向（垂直脊槽轴）的 D、Kv、D×Kv 统计值；选取不同视觉粗糙度等级的轮廓线，与计算参数对照[Kulatilake 2021, pp. 17-18, 18-21]。

## Key Findings
- **非平稳性影响可忽略**：原始轮廓与去除线性趋势后轮廓的 D、Kv、D×Kv 均值及变异系数几乎一致，表明由全局线性趋势（−1.9°~+1.0°）引起的非平稳性对变异函数参数无影响[Kulatilake 2021, pp. 7-9, Table 2]。
- **显著性非均质性**：Z-Y 轮廓线的 750–1000 mm 段粗糙度参数均值最高、变异性最大，与 0–750 mm 段存在显著差异；0–500 mm 段则相对均质。Z-X 方向非均质性远低于 Z-Y 方向[Kulatilake 2021, pp. 9-11, 11-16, Tables 3-4]。
- **尺度效应主要由非均质性控制**：在均质段（0–250 mm 与 250–500 mm 合并对比 0–500 mm）上，D、Kv、D×Kv 均值几乎不变，尺度效应几乎不存在。将不同截段混合统计时，Z-Y 方向仅表现出微小的尺度效应，Z-X 方向则无尺度效应[Kulatilake 2021, pp. 11-16, 16-17, Tables 5-7]。作者认为文献中矛盾的尺度效应报道极可能源于对表面非均质性的忽视[Kulatilake 2021, pp. 3-4, 17-18, 21-22]。
- **显著各向异性**：X 方向（脊槽轴向）的 D、Kv、D×Kv 均值明显低于 Y 方向，与剪切断裂主剪切方向近平行于 X 的直观判断一致[Kulatilake 2021, pp. 18-21, Tables 6-7]。
- **视觉粗糙度与计算参数一致性**：D、Kv、D×Kv 均随轮廓视觉粗糙度增加而单调增大[Kulatilake 2021, pp. 17-18, Figs. 13-19]。
- **方法可靠性**：超过 1700 条轮廓线的计算提供了高度一致的结果，证明遵循严格准则的变异函数法是准确的粗糙度量化方法[Kulatilake 2021, pp. 1-2, 21-22]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 非平稳性对 D、Kv、D×Kv 无影响：原始与残差数据均值、CV 几乎相等 | [Kulatilake 2021, pp. 7-9, Table 2] | 1000 mm 和 500 mm Z-Y 轮廓，线性趋势角 −1.9° 到 +1.0° | 残差处理未改变任何统计特征 |
| Z-Y 轮廓 750–1000 mm 段 D 均值 1.378，Kv 均值 0.0812，D×Kv 均值 0.1177，CV 最高达 0.6053（D×Kv），显著高于 0–750 mm 段 | [Kulatilake 2021, pp. 11-16, Table 4] | 250 mm 长的 Z-Y 轮廓，取 78 条有效轮廓（R>0.85） | 该段为强非均质、高粗糙度区域 |
| 均质段尺度效应缺失：合并 0–250 mm 和 250–500 mm Z-Y 段（202 条），D 均值 1.1235，Kv 0.0360，与 0–500 mm 段（101 条）D 1.1232、Kv 0.0359 几乎一致 | [Kulatilake 2021, pp. 11-16, Table 5] | 只保留 0–500 mm 的均质部分 | 无尺寸效应，均质是关键 |
| 混合所有截段后 Z-Y 方向尺度效应轻微：1000 mm 段 D 1.2458, Kv 0.0564；500 mm D 1.1830, Kv 0.0543；250 mm D 1.1769, Kv 0.0455 | [Kulatilake 2021, pp. 17-18, Table 7] | 包含非均质 750–1000 mm 段，381 条 250 mm 有效廓线 | 均值略有上升，但 CV 较大 |
| Z-X 方向无尺度效应且 D、Kv 均远低于 Z-Y：1000 mm Z-X 均 D=1.1342, Kv=0.0091；而 Z-Y 的 1000 mm 均 D=1.2458, Kv=0.0564 | [Kulatilake 2021, pp. 17-18, Tables 6 & 7] | X 为剪切方向，Y 正交方向 | 各向异性显著 |
| D×Kv 随视觉粗糙度单调递增，在 1000 mm Z-Y 轮廓中从最光滑的约 0.04 增至最粗糙的约 0.16 | [Kulatilake 2021, pp. 17-18, Figs. 13-19] | 整体表面轮廓 | 验证参数的物理意义 |

## Limitations
- 研究仅针对一块 1 m × 1 m 板岩剪切断裂面，可能不具普适性。
- 节理面尺寸覆盖的是粗糙度中“不平整度”部分，不含大尺度“波浪度”，结论对更大尺度波浪度的适用性未知[Kulatilake 2021, pp. 4-6]。
- 非平稳性检验仅考虑了全局线性趋势，其他形式非平稳性未涉及[Kulatilake 2021, pp. 7-9]。
- 尺度效应分析依赖于变异函数法的特定准则（h·d=1.76、增量因子 1.2、R>0.85），其他自仿射方法或参数选择可能得出不同结论[Kulatilake 2021, pp. 3-3, 6-7]。
- 未讨论测量分辨率变化对粗糙度参数的单独影响，虽然文中指出分辨率影响可能强于样本尺寸[Kulatilake 2021, pp. 3-4]。

## Assumptions / Conditions
- 轮廓线被假定为具有平稳增量的高斯过程，均值零[Kulatilake 2021, pp. 6-7]。
- 早期变异函数满足幂律关系是计算 D 与 Kv 的前提，需通过 R>0.85 验证[Kulatilake 2021, pp. 6-7]。
- 采用 Kulatilake 等（1998）推荐的保守关系 hd=1.76 确定最小滞后距，适用于 D 未知（1.0–1.7）的轮廓[Kulatilake 2021, pp. 6-7]。
- 数据数字化间距 0.5 mm，数据密度 d=2 /mm；测量分辨率 ±0.10 mm[Kulatilake 2021, pp. 6-7]。
- 非均质性与尺度效应关系的解释基于该特定节理表面，即 750–1000 mm 段的显著非均质是产生轻微尺度效应的源头[Kulatilake 2021, pp. 16-17]。

## Key Variables / Parameters
- **分形维数 D**（自相关度量）
- **振幅参数 Kv**（轮廓振幅度量）
- **联合粗糙度参数 D×Kv**
- **滞后距 h**（用于计算变异函数）
- **数据密度 d**（单位长度数据点数）
- **轮廓方向**（X 方向平行脊槽/剪切方向，Y 方向正交）
- **轮廓长度**（125, 250, 500, 1000 mm）
- **轮廓位置与截段**（如 0–250 mm, 750–1000 mm 等）
- **线性趋势角及残差粗糙度**
- **线性相关系数 R**（验证幂律的阈值 0.85）

## Reusable Claims
- **Claim 1**: 对于天然岩石节理轮廓，由幅度在 −1.9° 至 +1.0° 内的全局线性趋势引起的非平稳性，对变异函数法计算的分形维数 D 和振幅参数 Kv 没有可观测影响。  
  *条件*：轮廓数据密度 2/mm，滞后距按 hd=1.76 准则选取；不排除更大幅度趋势或其他非平稳形式。  
  *来源*：[Kulatilake 2021, pp. 7-9, Table 2]。
- **Claim 2**: 节理表面粗糙度参数的尺度效应（随样本尺寸变化）本质上由表面非均质性控制；若表面足够均质，则不存在由尺寸引起的粗糙度参数变化。  
  *条件*：使用变异函数法，并遵循作者建议的严格计算准则；仅针对该板岩节理的“不平整度”尺度。  
  *来源*：[Kulatilake 2021, pp. 11-16, Tables 5-7; pp. 16-17, 21-22]。
- **Claim 3**: 对于剪切成因的岩石节理，沿剪切方向（X）的粗糙度参数（D、Kv、D×Kv）显著低于垂直剪切方向（Y），变异函数法能可靠揭示这种各向异性。  
  *条件*：该节理面具有明显平行 X 方向的脊槽结构；数字化间距 0.5 mm。  
  *来源*：[Kulatilake 2021, pp. 18-21, Tables 6-7]。
- **Claim 4**: 计算参数 D×Kv 能综合反映轮廓的自相关与振幅特征，其数值随视觉粗糙度增加而单调增大，是可靠的粗糙度量指标。  
  *条件*：适用于变异函数法且满足幂律假设（R>0.85）。  
  *来源*：[Kulatilake 2021, pp. 17-18, Figs. 13-19; pp. 21-22]。

## Candidate Concepts
- [[岩石节理粗糙度 (rock joint roughness)]]
- [[自仿射分形 (self-affine fractal)]]
- [[变异函数法 (variogram method)]]
- [[分形维数 D (fractal dimension D)]]
- [[振幅参数 Kv (amplitude parameter Kv)]]
- [[粗糙度非均质性 (roughness heterogeneity)]]
- [[粗糙度各向异性 (roughness anisotropy)]]
- [[尺度效应 (scale effect)]]
- [[非平稳性 (non-stationarity)]]
- [[节理不平整度 (unevenness)]]
- [[数据密度与采样间隔 (data density and sampling interval)]]

## Candidate Methods
- [[变异函数法粗糙度量化 (variogram-based roughness quantification)]]
- [[轮廓线性趋势去除 (linear detrending)]]
- [[分形参数一致性检验 (fractal parameter consistency check via R>0.85)]]
- [[基于均质段与非均质段分组的尺度效应分离 (separation of scale effect by homogeneous vs heterogeneous segments)]]
- [[三维激光扫描数字化节理表面 (3D laser scanning for joint surface digitisation)]]

## Connections To Other Work
- 文中指出许多文献对粗糙度尺度效应得出矛盾结论（如 Bandis et al. 1981; Fardin et al. 2001, 2004; Cravero et al. 2001; Leal-Gomes 2003; Fardin 2008; Tatone & Grasselli 2013），本研究将原因归于未考虑的粗糙度非均质性[Kulatilake 2021, pp. 3-4]。
- 与更早的变异函数法研究（Kulatilake et al. 1998）一致，严格遵循 hd=1.76 等准则才能获得可靠参数[Kulatilake 2021, pp. 3-3, 6-7]。
- 各向异性结果与 Kulatilake et al.（1995, 2006）、Ge et al.（2014）的变异函数与改进 divider 法相互印证[Kulatilake 2021, pp. 3-3, 4-6]。
- 所用数字化数据来源于 Yong et al.（2018）及 Du et al.（2021）的同一采石场研究[Kulatilake 2021, pp. 4-6, 6-7]。

## Open Questions
- 该结论（尺度效应主要由非均质引起）能否推广到其他岩性、其他断裂类型（如张性断裂、层理面）以及包含更大波浪度的节理面？
- 若采用不同的自仿射分形方法（如频谱法、粗糙度‑长度法）并保持同样的非均质控制，是否也能得出无内在尺度效应的结论？
- 除全局线性趋势外，其他形式的非平稳性（如二次趋势、方差非平稳）对变异函数参数的影响如何？
- 当测量分辨率变化时，非均质与尺度效应的交互作用是否依然以非均质为主导？
- 是否存在一个定量的非均质性指标（如基于局部 D、Kv 的空间异质性指数），可用于预判节理表面是否会出现尺度效应？

## Source Coverage
本页面的所有事实性声明均来源于已索引的 15 个非空 source block。共处理已编译 source 字符 72,269 个（总索引字符 72,917），覆盖率为 99.1%（按字符计），各 block 均被使用，覆盖率 1.0（按 block 计）。无新增或推测性内容。索引片段涵盖论文全文关键部分：[Kulatilake 2021, pp. 1-2] 至 [Kulatilake 2021, pp. 22-23]。
