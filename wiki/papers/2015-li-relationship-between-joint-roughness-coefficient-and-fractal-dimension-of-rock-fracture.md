---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
title: "Relationship between Joint Roughness Coefficient and Fractal Dimension of Rock Fracture Surfaces."
status: "draft"
source_pdf: "data/papers/2015 - Relationship between joint roughness coefficient and fractal dimension of rock fracture surfaces.pdf"
collections:
  - "zotero new"
  - "分形"
citation: "Li, Yanrong, and Runqiu Huang. \"Relationship between Joint Roughness Coefficient and Fractal Dimension of Rock Fracture Surfaces.\" *International Journal of Rock Mechanics & Mining Sciences*, 2015. doi:10.1016/j.ijrmms.2015.01.007. Accessed 2026."
indexed_texts: "8"
indexed_chars: "37489"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "37533"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.001174"
coverage_status: "full-index"
source_signature: "306c84e5a99bd54cfaaa0391f6ce3df3c654a49c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:04:25"
---

# Relationship between Joint Roughness Coefficient and Fractal Dimension of Rock Fracture Surfaces.

## One-line Summary
本研究回顾了基于分形维数（D）估计岩石节理粗糙度系数（JRC）的方法，更新了h–L方法，并基于112条轮廓线提出了新的一组经验方程，表明compass-walking和更新的h–L方法估计的D与JRC密切相关，而box-counting方法相关较弱。

## Research Question
如何可靠地使用分形维数（D）估计岩石节理粗糙度系数（JRC），并解决现有经验公式之间的不一致性？[Li 2015, pp. 1-1]

## Study Area / Data
数据集由112条岩石节理轮廓线组成，包括10条标准JRC轮廓线[2]和从文献中收集的102条轮廓线（12条来自Grasselli [38]，26条来自Bandis等 [39]，64条来自Bandis [40]）[Li 2015, pp. 4-5]。轮廓线投影长度范围72至119.6 mm，JRC值范围0.4至20[Li 2015, pp. 4-5]。岩石类型多样，包括砂岩、石灰岩、大理岩、花岗岩、片麻岩、板岩、辉绿岩和粉砂岩，风化程度从新鲜到中等风化[Li 2015, pp. 5-6]。节理为拉裂隙，从良好互锁的平面解理裂缝到不良互锁的膜覆盖壁[Li 2015, pp. 5-6]。

## Methods
- **分形维数确定方法**：使用了三种方法：
  - **Compass-walking**（分规法）：通过设定半径r的圆规沿轮廓线测量，计算log N vs log r的斜率得到D，或采用变体计算Nr vs r的斜率[Li 2015, pp. 1-2]。
  - **Box-counting**（盒计数法）：将轮廓线置于均匀网格，计数所需盒子数G，绘制log G vs log ε的斜率得到D[Li 2015, pp. 1-2]。
  - **更新h–L方法**：原h–L方法[25,26]需要识别高阶凹凸体，主观性强。本研究更新为：在去除趋势的轮廓线上构建最小二乘线，用交点分割轮廓线，测量每段的基底长度L和极值振幅h，取平均后代入公式 D = log 4 / log {2(1 + cos[arctan(2h/L)])} [Li 2015, pp. 5-6]。
- **数据数字化**：由于无原始数字数据，从PDF出版物图像导入AutoCAD，设置坐标系统，以0.4 mm间隔构建垂直线，追踪轮廓线，导出坐标[Li 2015, pp. 5-6]。此过程可能引入重采样误差[Li 2015, pp. 5-6]。
- **趋势去除与自动化**：自编程序去除线性趋势，使轮廓线水平对齐，并执行数据验证和D计算[Li 2015, pp. 5-6]。
- **回归分析**：基于112条轮廓线的JRC（由Barton–Bandis剪切强度模型反算得到）与D进行线性和非线性回归，得出新经验方程[Li 2015, pp. 6-8]。

## Key Findings
1. 现有经验公式之间存在很大差异，主要因为推导所用数据点有限（多基于10条标准轮廓线）、D确定方法不一致以及JRC赋值不一致（如部分研究使用奇数JRC值而非Barton-Choubey值）[Li 2015, pp. 1-1, 4-5]。
2. 基于10条标准轮廓线的公式可能不足以可靠地估计JRC[Li 2015, pp. 6-8]。
3. 本研究更新的h–L方法避免了识别高阶凹凸体的主观性，可由计算机程序自动执行[Li 2015, pp. 5-6, 8-8]。
4. Compass-walking（Dc）和更新h–L方法（Dh–L）估计的D与JRC呈良好的线性关系，数据点紧凑；Box-counting（Db）与JRC的线性关系较弱（R=0.6730）[Li 2015, pp. 6-8]。
5. 提出了六个新经验方程（E1–E6），其中使用Dc–1的幂律方程E4（R=0.8544）和使用Dh–L–1的幂律方程E6（R=0.8088）以及线性方程E1和E3被推荐。E6因Dh–L易于计算而具有优先实用性[Li 2015, pp. 8-8]。

## Core Evidence Table
| 证据 | 来源 | 条件 | 注释 |
|------|------|------|------|
| 19个已发表的经验方程汇总在表1中，包括方程、使用的方法、相关系数、采样间隔、JRC0、D范围及是否基于标准轮廓线。 | [Li 2015, pp. 2-4] | 方法包括compass-walking、box-counting、h–L；数据源多样。 | 揭示了方法间不一致性和JRC赋值差异（如奇数JRC值与标准值）。 |
| 112条轮廓线（10标准+102文献）的D测量结果与JRC的关系图（图8、9）：Dc、Dh-L与JRC线性趋势明显，Db数据点分散。 | [Li 2015, pp. 6-8] | 轮廓线长度72–119.6mm，采样间隔约0.4mm，岩石类型多样。 | 视觉显示Db与JRC的弱相关性，支持推荐Dc和Dh-L。 |
| 新方程E1–E6的系数及相关统计（表3）：E1: JRC=1331.07Dc−1328.44, R=0.8242; E2: JRC=196.77Db−195.95, R=0.6730; E3: JRC=1240.46Dh−L−1235.19, R=0.8335; E4: JRC=520.28(Dc−1)^0.7588, R=0.8544; E5: JRC=2.72e^{26.876(Db−1)}, R=0.7717; E6: JRC=118.89(Dh−L−1)^0.4343, R=0.8088。 | [Li 2015, pp. 8-8] | 方程基于112条轮廓线；采样间隔0.4mm。 | E4和E6具有较高R，且适用于光滑轮廓（JRC0=0），E1和E3也有较好相关性。 |
| 文献中标准轮廓线JRC赋值不一致：一些研究者使用奇数（1,3,5,…），一些使用Barton和Choubey的值（0.4,2.8,5.8,…），导致公式偏差。 | [Li 2015, pp. 4-5] | 标准轮廓线的JRC范围0–20。 | 此差异是导致文献公式变化的原因之一。 |
| 更新h–L方法使用最小二乘线分割轮廓线，测量每个分段的基底长度L和极值振幅h，然后计算D。 | [Li 2015, pp. 5-6] | 假定去除趋势后的轮廓线可用交点分割，测量极值。 | 避免了原有方法的主观性，可由程序执行。 |
| 建议方程适用于实验室尺度，因为所用轮廓线长度72–119.6mm；采样间隔应为约0.4mm；更大样本量可改进方程。 | [Li 2015, pp. 8-8] | 轮廓线长度窄范围；数据来自文献。 | 局限性明确。 |

## Limitations
- 使用的112条轮廓线长度范围72–119.6mm，较窄，因此方程主要适用于实验室尺度，需要更大型轮廓线进一步研究[Li 2015, pp. 8-8]。
- 数据由从出版物图像数字化得到，可能引入重采样误差[Li 2015, pp. 5-6]。
- 现有数据集仅含112条轮廓线，更大样本量可能有助于验证或改进经验方程[Li 2015, pp. 8-8]。
- 采样间隔固定为约0.4mm，改变采样间隔可能影响D与JRC的关系[Li 2015, pp. 8-8]。
- 本研究的JRC值通过Barton–Bandis剪切强度模型反算，可能受该模型本身不确定性的影响[Li 2015, pp. 4-5, 6-8]。

## Assumptions / Conditions
- 假设分形维数D的值域为1（完全光滑）到小于2（极端起伏），符合分形几何理论[Li 2015, pp. 1-1]。
- 假设JRC可仅由分形维数估计，且D-1作为自变量能较好适应光滑平面（JRC=0）[Li 2015, pp. 2-4, 6-8]。
- 假设采用约0.4mm采样间隔是合理且易于实现的[Li 2015, pp. 8-8]。
- 假设轮廓线去除线性趋势后，其粗糙度特征可由最小二乘线分割的h、L平均值表征[Li 2015, pp. 5-6]。

## Key Variables / Parameters
- **JRC**（Joint Roughness Coefficient）：节理粗糙度系数，范围0–20，用于Barton剪切强度准则[Li 2015, pp. 1-1]。
- **Dc**（Fractal dimension by compass-walking）：分规法确定的分形维数[Li 2015, pp. 1-2]。
- **Db**（Fractal dimension by box-counting）：盒计数法确定的分形维数[Li 2015, pp. 1-2]。
- **Dh–L**（Fractal dimension by h–L method）：h–L方法确定的分形维数[Li 2015, pp. 1-2, 5-6]。
- **采样间隔**：本研究中为0.4mm[Li 2015, pp. 8-8]。
- **轮廓线长度**：72–119.6mm（实验室尺度）[Li 2015, pp. 4-5, 8-8]。
- **JRC0**：方程估算的光滑平面JRC值[Li 2015, pp. 2-4]。
- **相关系数R**：衡量方程拟合优度[Li 2015, pp. 8-8]。

## Reusable Claims
1. 仅基于10条标准JRC轮廓线的经验方程可能不可靠，因为数据点太少，不足以捕获JRC与D的全部变异[Li 2015, pp. 1-1, 6-8]。
2. 更新的h–L方法通过最小二乘线分割轮廓线并测量每段L、h，避免了主观识别高阶凹凸体，实现了可重复的D计算[Li 2015, pp. 5-6]。
3. 对于实验室尺度（轮廓线长度72–120mm，采样间隔0.4mm）的岩石节理，compass-walking和更新的h–L方法测得的D与JRC线性关系较强（R>0.82），且数据点紧凑；box-counting方法的相关性较弱（R≈0.67），不推荐用于JRC估计[Li 2015, pp. 6-8]。
4. 推荐使用本研究的方程E4（JRC=520.28(Dc−1)^0.7588, R=0.8544）或E6（JRC=118.89(Dh–L−1)^0.4343, R=0.8088），这些方程适用于光滑平面（JRC0=0）且具有较高相关系数，并可根据实际精确度需求选择Dc或Dh–L[Li 2015, pp. 8-8]。
5. 应用经验方程时必须采用与方程推导时相同的D确定方法，否则将引入显著偏差[Li 2015, pp. 2-4]。

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[Fractal dimension (D)]]
- [[Rock joint roughness]]
- [[Barton’s shear strength criterion]]
- [[Compass-walking method]]
- [[Box-counting method]]
- [[h–L method]]
- [[Standard JRC profiles]]
- [[Peak shear strength]]
- [[Scale effect]]
- [[Trend removal]]
- [[Sub-planar joint]]
- [[Sampling interval]]
- [[Fracture roughness quantification]]

## Candidate Methods
- [[Compass-walking fractal dimension estimation]]
- [[Box-counting fractal dimension estimation]]
- [[Updated h–L method for fractal dimension]]
- [[Trend removal using least-square line]]
- [[Digitization of rock joint profiles from images]]
- [[Automatic asperity segmentation and measurement]]
- [[Linear and power-law regression for JRC prediction]]

## Connections To Other Work
- 本研究引用了Barton (1973)的剪切强度准则和Barton & Choubey (1977)的10条标准轮廓线，作为JRC概念的基础[Li 2015, pp. 1-1]。
- 引用了Turk等 (1987)和Carr & Warriner (1987)早期将分形维数用于岩石节理粗糙度的研究[Li 2015, pp. 1-1]。
- 回顾了Xie & Pariseau (1994)和Askari & Ahmadi (2007)的原始h–L方法，并进行了更新[Li 2015, pp. 1-2, 5-6]。
- 比较了众多后续研究提出的经验方程（表1），包括Maerz & Franklin (1990), Lee et al. (1990), Zhou & Xiong (1996), Xu et al. (2012)等[Li 2015, pp. 2-4]。
- 数据来源包括Grasselli (2001), Bandis et al. (1983)和Bandis (1980)的轮廓线，表明数据集整合了多个研究[Li 2015, pp. 4-5, 8-8]。

## Open Questions
- 适用于更大尺度（现场尺度）岩石节理的D–JRC关系仍需研究，因为当前方程基于实验室尺度轮廓线[Li 2015, pp. 8-8]。
- 采样间隔对D–JRC相关性影响的系统性研究尚未充分开展，目前推荐0.4mm，但其他间隔下的方程可能不同[Li 2015, pp. 8-8]。
- 更大样本量（超过112条）的验证可能进一步完善经验方程[Li 2015, pp. 8-8]。
- 不同风化程度和岩石类型对D–JRC关系的影响是否可忽略，文中未深入探讨[Li 2015, pp. 4-5]。
- 原始h–L方法与更新方法的差异及其对JRC预测精度的定量比较仍有待开展[Li 2015, pp. 5-6]。

## Source Coverage
所有8个非空索引片段均已处理，覆盖率为：索引文本块数8，编译源块数8，编译源字符数37533，覆盖率（按块）1.0，覆盖率（按字符）1.001174。源签名为306c84e5a99bd54cfaaa0391f6ce3df3c654a49c，编译策略为single-pass-markdown。所有陈述均来源于提供的片段。
