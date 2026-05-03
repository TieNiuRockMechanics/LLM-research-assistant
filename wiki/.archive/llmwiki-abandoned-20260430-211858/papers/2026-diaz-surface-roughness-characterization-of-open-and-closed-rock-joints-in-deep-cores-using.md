---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using"
title: "Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography."
status: "draft"
source_pdf: "data/papers/2017 - Surface roughness characterization of open and closed rock joints in deep cores using X-ray computed tomography.pdf"
collections:
  - "zotero new"
citation: "Diaz, Melvin, et al. \"Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography.\" *International Journal of Rock Mechanics & Mining Sciences*, www.elsevier.com/locate/ijrmms. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42296"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:57:28"
---

# Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography.

## One-line Summary
利用X射线CT扫描技术对浦项增强地热系统（EGS）4.2 km深度岩心中的开放与闭合节理进行表面粗糙度及方向异性定量表征，并讨论了粗糙度各向异性对地下流体流动和井位布置的意义。[Diaz 2026, pp. 1-2, 6-8]

## Research Question
能否利用X射线CT技术从深部岩心（>4 km）中提取闭合节理的表面形态，并全面描述其粗糙度与各向异性？目前针对超过4 km深度节理的粗糙度表征十分欠缺，未能为深部耦合水‑力过程提供基础参数。[Diaz 2026, pp. 1-2]

## Study Area / Data
- **地点**：韩国浦项地区EGS项目PX‑2井，取心深度4219‑4223 m，岩心直径10 cm，总长3.6 m。[Diaz 2026, pp. 1-2]
- **岩性**：中粒花岗岩，无风化迹象。[Diaz 2026, pp. 1-2]
- **节理样品**：共7个节理表面，包括5个开放节理（OJ‑1至OJ‑5）和2个闭合节理（CJ‑1、CJ‑2）。节理面与取心方向夹角在10°–30°之间。[Diaz 2026, pp. 2-4]
- **对比数据**：引用了法国Soultz‐sous‑Forêts地热场EPS‑1井1.3‑2.1 km深度花岗岩断裂的粗糙度数据（JRC）进行浅部比较。[Diaz 2026, pp. 8-10]

## Methods
1. **X射线CT扫描与表面提取**：对整段岩心进行工业CT扫描，利用体素数据重建三维体积。开放节理可直接提取表面，闭合节理则依据界面两侧密度差异识别并渲染出节理面。[Diaz 2026, pp. 2-4]
2. **点云生成与网格分辨率**：设定固定方形网格尺寸0.1 mm生成点云，该值通过评估四个粗糙度参数随网格尺寸的变化而确定。[Diaz 2026, pp. 2-4, 3.1节未完整]
3. **方位校正**：对点云拟合平面，估计节理面相对于取心方向的角度。[Diaz 2026, pp. 2-4]
4. **粗糙度参数计算**：
   - 采用Li和Zhang [21]的公式计算节理粗糙度系数（JRC），采样间距沿每条剖面为0.4 mm。[Diaz 2026, pp. 2-4, 4-5]
   - 计算偏度（Rsk）、峰态（Rku）和最大表面高度Sz（三维参数）。这些参数由自编代码在生成的一系列剖面上求取。[Diaz 2026, pp. 4-5]
5. **各向异性评价**：参照Huang和Doong[24]的方法，沿18个方向（每10°逆时针）生成间距2.5 mm的剖面，计算各方向的JRC、Rsk、Rku。取每个方向在±1标准差范围内的测量值平均作为代表值。利用对称性获得共36个方向的极坐标图。[Diaz 2026, pp. 4-5, 5-6]

## Key Findings
1. **表面形貌参数**：节理表面角度6.2°–22.9°，面积58.6–174.5 cm²，最大高度Sz范围为3.7–20.1 mm（表2）。闭合节理CJ‑1和CJ‑2的Sz分别为11.5 mm和11.7 mm。[Diaz 2026, pp. 6-8]
2. **偏度与峰态特征**：
   - 多数表面相对对称，但OJ‑2、OJ‑4、OJ‑5的绝对偏度平均值>0.2，显著不对称。[Diaz 2026, pp. 5-6]
   - OJ‑2（峰态2.7）和OJ‑4（2.47）呈低峰态（platykurtoic），OJ‑5（3.37）呈高峰态（leptokurtoic）。OJ‑3、OJ‑4、OJ‑5显示峰态的方向性，最大值分别出现在30°、120°、160°方向。[Diaz 2026, pp. 5-6]
3. **粗糙度各向异性**：
   - 不同节理的各向异性程度不一：OJ‑1和OJ‑2最大/最小JRC比值仅为1.18和1.16，而其他节理比值最高达1.54。[Diaz 2026, pp. 6-8]
   - 拟合后所有表面的最大JRC方向相似，平均约为161.2°。[Diaz 2026, pp. 6-8]
4. **采样面积效应**：随着采样方形面积从中心向外扩大，平均JRC值变化，但最大JRC的方位角趋于稳定（图8）。[Diaz 2026, pp. 6-8]
5. **深度对比**：与EPS‑1井较浅部（1.3‑2.1 km）的花岗岩节理JRC（计算值9.5‑16.98）相比，本研究的JRC值处于相同范围内，但需注意Z2对采样距离敏感。更值得关注的是本研究中所有节理表现出相似的最大粗糙度方向。[Diaz 2026, pp. 8-10]
6. **工程意义**：粗糙度各向异性很可能影响流体沿节理面的流动方向和剪切扩容行为，应在EGS注采井布局设计中予以考虑。[Diaz 2026, pp. 6-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 节理表面与取心方向夹角6.2°–22.9°，Sz值3.7–20.1 mm | [Diaz 2026, pp. 6-8] Table 2 | 7个节理表面，取自4.2 km深度花岗岩，X射线CT提取 | 包含OJ和CJ；CJ‑1 Sz = 11.5 mm, CJ‑2 Sz = 11.7 mm |
| OJ‑5峰态3.37，为leptokurtic；OJ‑2、OJ‑4偏度>0.2且峰态<3 | [Diaz 2026, pp. 5-6] | 所有18个方向测量的平均值；偏度阈值0.2（Hildebrand标准） | OJ‑2、OJ‑4为platykurtic |
| 节理JRC各向异性比可达1.54，最大JRC方向平均约161.2° | [Diaz 2026, pp. 6-8] Fig.9 | 以最大可能方形采样面积计算；18个方向±1σ内平均 | OJ‑1、OJ‑2比值为1.18、1.16 |
| EPS‑1井1.56‑2.07 km深度花岗岩JRC为9.5‑16.98，与本研究范围重叠 | [Diaz 2026, pp. 8-10] | 使用Z2及Tse and Cruden方程换算；采样距离影响结果 | 本研究深度岩心为粒玄岩（granodiorite）？未从片段中确认岩性差异，仅提花岗岩对比 |
| 随采样面积增大，最大JRC的方向趋于稳定 | [Diaz 2026, pp. 6-8] Fig.8 | OJ‑1, OJ‑4, OJ‑5，从中心逐渐扩大方形区域 | 平均JRC值有变化，但方向收敛 |

## Limitations
- 样本数量有限（7个节理面），仅来自单一井位（PX‑2）的单一岩性，结果推广至其他地质背景需谨慎。 [Diaz 2026, pp. 2-4]
- JRC参数计算对采样距离、网格大小等尺度敏感，不同参数选择可能影响数值。 [Diaz 2026, pp. 8-10]
- 闭合节理的CT渲染依赖于密度差异，若充填物密度与基岩接近则可能难以准确提取表面。 [Diaz 2026, pp. 2-4]
- 未从索引片段中确认具体统计不确定性或重复性分析。

## Assumptions / Conditions
- X射线CT能够通过体素密度差异可靠地区分闭合节理界面与围岩。[Diaz 2026, pp. 2-4]
- 点云生成所用的0.1 mm正方形网格能够充分解析本研究所需尺度上的粗糙度特征（已通过随网格尺寸变化的粗糙度参数评估选定）。[Diaz 2026, pp. 2-4]
- JRC的计算采用Li和Zhang的公式 [21]，假定该公式适用于所分析的节理表面。[Diaz 2026, pp. 2-4]
- 各向异性分析中，以10°间隔覆盖360°、剖面间距2.5 mm的取样方案可反映表面的方向性变化。[Diaz 2026, pp. 4-5]
- 采用±1标准差过滤异常值后取平均值，能得到各方向的代表性粗糙度值。[Diaz 2026, pp. 4-5]

## Key Variables / Parameters
- **表面粗糙度参数**：JRC（节理粗糙度系数）、偏度（Rsk）、峰态（Rku）、最大表面高度（Sz）[Diaz 2026, pp. 2-4]
- **剖面统计量**：均方根一阶导数Z2（用于JRC计算）[Diaz 2026, pp. 8-10]
- **采样尺度参数**：
  - 点云网格尺寸：0.1 mm [Diaz 2026, pp. 2-4]
  - JRC剖面采样距离：0.4 mm [Diaz 2026, pp. 4-5]
  - 各向异性剖面间距：2.5 mm [Diaz 2026, pp. 4-5]
  - 各向异性方向间隔：10° [Diaz 2026, pp. 4-5]
- **几何参数**：节理面与取心方向的夹角（°）、节理面积（cm²）、最大峰值高度（mm）、最低谷深（mm）[Diaz 2026, pp. 6-8] Table 2
- **粗糙度各向异性指标**：最大/最小JRC比值，最大JRC方向（°）[Diaz 2026, pp. 6-8]

## Reusable Claims
1. **闭合节理表面获取**：利用X射线CT体素数据根据密度差异可成功提取深部岩心中闭合节理的三维表面，弥补传统轮廓仪的不足。[Diaz 2026, pp. 2-4] （适用条件：岩心直径10 cm，扫描分辨率足够分辨节理充填物与基岩的密度差异；限制：密度差异不明显时可能失效）
2. **网格分辨率确定方法**：可通过评估多个粗糙度参数随正方形网格尺寸变化的趋势，为点云生成选择合理的固定网格尺寸。本研究中0.1 mm网格使Ra、Rq稳定，而Rp和Z2在<1 mm与>1 mm时趋势不同。[Diaz 2026, pp. 2-4, 3.1节概述] （证据限制：仅展示趋势，未从片段看到完整图表）
3. **各向异性表征方案**：对节理面以10°间隔、使用±1σ过滤的剖面测量JRC、偏度与峰态，可有效揭示粗糙度的方向性，且最大JRC方位角随采样面积增大而趋向稳定。[Diaz 2026, pp. 4-5, 6-8] （适用：需对每个方向生成多条剖面；限制：剖面间距2.5 mm，针对本研究面积尺度）
4. **粗糙度各向异性比值**：最大与最小JRC的比值可作为衡量节理面粗糙度各向异性的定量指标，配合最大JRC的绝对方向值，可为分析古应力方向或流体流动优势通道提供约束。[Diaz 2026, pp. 6-8] （证据：本研究中比值1.16-1.54；所有表面最大JRC方向相似，平均161.2°）
5. **深度与粗糙度关系需谨慎**：同一地区不同深度节理的JRC数值范围可能重叠，仅凭JRC平均值难以区分深度效应；更可靠的标志可能是各节理的最大粗糙度方向的系统一致性，这可能反映古应力场。[Diaz 2026, pp. 8-10] （限制：基于单一地点两个深度段对比，未推广到其他区域）

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[surface roughness anisotropy]]
- [[closed joint]]
- [[X-ray computed tomography for rock cores]]
- [[enhanced geothermal system (EGS)]]
- [[skewness of rock joint profiles]]
- [[kurtosis of rock joint profiles]]
- [[maximum surface height (Sz)]]
- [[paleo-stress and fracture roughness]]
- [[fluid flow anisotropy in fractures]]
- [[shear dilation of rock joints]]

## Candidate Methods
- [[X-ray CT surface extraction from density contrast]]
- [[Li and Zhang JRC equation]]
- [[Tse and Cruden JRC equation]]
- [[Huang and Doong roughness anisotropy method]]
- [[point cloud generation from voxel data]]
- [[plane fitting for joint orientation correction]]
- [[profile-based 2D roughness parameter mapping]]

## Connections To Other Work
- **JRC基准定义**：研究使用JRC表征粗糙度，其概念源于Barton和Choubey [16] 的10条标准剖面及随后的方程化工作。 [Diaz 2026, pp. 1-1]
- **JRC计算公式**：选用了Li和Zhang [21] 的公式，并提及Tse和Cruden [22] 的基于Z2的JRC方程，后者用于与EPS‑1数据的对比计算。 [Diaz 2026, pp. 1-1, 8-10]
- **粗糙度各向异性分析框架**：沿用了与Huang和Doong [24] 类似的多方向剖面评估方法。 [Diaz 2026, pp. 4-5]
- **流体流动与剪切各向异性**：引述Yeo等 [41] 关于流体沿节理面各向异性流动的发现，以及Koyama等 [42] 关于剪切过程中扩容各向异性的成果，用以支持粗糙度各向异性对EGS性能的影响论证。 [Diaz 2026, pp. 6-8]
- **较浅部断裂对比**：引用EPS‑1井断裂分形维度随深度增加而增加（粗糙度减小）的研究 [44]，并计算了对应深度JRC值进行比较。未从索引片段中确认该研究的确切作者和年份。 [Diaz 2026, pp. 8-10]

## Open Questions
- 在这些深度节理中观察到的最大JRC方向一致性在更大区域或不同应力史条件下是否仍成立？未从索引片段中确认。
- 闭合节理的粗糙度如何具体影响裂缝导流能力和密封能力？未从片段中获知相关实验或模拟验证。
- 本方法对不同岩性和充填物类型的闭合节理提取效果如何？片段中只涉及花岗岩中的单一井位。
- 粗糙度各向异性与岩石力学参数（如剪切强度）的直接定量关系尚未在片段中建立。

## Source Coverage
本页内容基于提供的9个索引片段，片段覆盖了论文的引言（部分）、样品与方法、部分结果（表2、偏度/峰态描述、JRC各向异性图及分析）、与EPS‑1井对比讨论以及结论的起始部分。主要包含：
- 引言（研究动机与背景）
- 样品采集（PX‑2井、深度、岩性、节理类型）
- X射线CT提取过程与点云生成
- 粗糙度参数定义与各向异性分析方法
- 关键定量结果（表面形貌、偏度/峰态、JRC各向异性、尺度效应）
- 与较浅部花岗岩节理的对比

**可能缺失的信息**：
- 完整的结论段落（仅截取前几句）。
- 对Z2、JRC计算公式等更详细的数学表达。
- 网格尺寸选择的完整评估数据（仅概述）。
- 全部参考文献清单及各引用的具体对应。
- 可能的局限性与未来工作讨论的完整内容。
