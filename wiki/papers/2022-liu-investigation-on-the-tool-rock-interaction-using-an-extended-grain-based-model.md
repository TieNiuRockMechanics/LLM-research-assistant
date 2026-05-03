---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-liu-investigation-on-the-tool-rock-interaction-using-an-extended-grain-based-model"
title: "Investigation on the Tool-Rock Interaction Using an Extended Grain-Based Model."
status: "draft"
source_pdf: "data/papers/2022 - Investigation on the Tool-Rock Interaction Using an Extended Grain-Based Model.pdf"
collections:
  - "part3-2"
citation: "Liu, Weiji, et al. \"Investigation on the Tool-Rock Interaction Using an Extended Grain-Based Model.\" *KSCE Journal of Civil Engineering*, vol. 26, no. 6, 2022, pp. 2992-3006. DOI: 10.1007/s12205-022-2197-4. Accessed 2026."
indexed_texts: "12"
indexed_chars: "58981"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "58453"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991048"
coverage_status: "full-index"
source_signature: "15d85fbb3c52d9165e36724dd0e3ff3028a3e7b8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:44:23"
---

# Investigation on the Tool-Rock Interaction Using an Extended Grain-Based Model.

## One-line Summary
该研究利用一种扩展的颗粒基模型，结合数字图像处理技术，建立了考虑真实矿物分布与晶粒结构的非均质花岗岩离散元模型，系统研究了PDC切削与楔形压头侵入过程中微裂纹萌生、扩展规律及力响应，发现晶间拉伸裂纹与晶内剪切裂纹占主导，侧向压力对岩石切削岩屑体积影响不大，但却是影响侵入破岩效率的直接因素，为优化破岩参数和工具设计提供了依据。[Liu 2022, pp. 1-2][Liu 2022, pp. 13-14]

## Research Question
在深层硬地层钻井中，如何通过数值模拟揭示非均质花岗岩在与切削刀具和压入刀具相互作用时微裂纹的萌生、扩展及汇聚过程，以及侧向压力、切削深度等因素对破岩效率、岩屑形成和刀具受力特征的影响机制？[Liu 2022, pp. 1-2][Liu 2022, pp. 2-2]

## Study Area / Data
岩石样品取自中国湖北省随州的花岗岩，主要矿物成分为斜长石（21.9%）、钠长石（47.5%）、石英（19.3%）和黑云母（9.3%），晶粒尺寸较大、形状清晰，便于图像处理。[Liu 2022, pp. 3-4] 通过表面处理后获取数字图像，利用图像处理软件调节亮度和颜色通道识别四种矿物晶粒形状，提取出晶粒边界图像，并缩放至与实际岩样相同尺寸，再嵌入到颗粒流模型中。[Liu 2022, pp. 3-4]

## Methods
采用基于PFC2D的扩展颗粒基模型（Extended GBM）。模型构建步骤如下：
- 利用数字图像处理技术从花岗岩样品表面图像中提取真实的不规则晶粒边界，替代传统的Voronoi多边形，形成更贴近实际的矿物分布与晶粒镶嵌结构。[Liu 2022, pp. 3-4]
- 晶粒内部采用平行黏结模型（PBM），晶粒边界采用光滑节理模型（SJM），根据矿物类型分组赋予各矿物不同的PBM微观参数；所有六类矿物界面（斜长石‑钠长石、斜长石‑石英、斜长石‑黑云母、钠长石‑石英、钠长石‑黑云母、石英‑黑云母）的SJM参数均简化为同一组参数。[Liu 2022, pp. 3-4]
- 通过单轴压缩试验（UCS）和巴西劈裂试验（BTS）标定微观参数，颗粒半径范围为0.075–0.125 mm，UCS模型含35,078个颗粒，尺寸50 mm×25 mm；BTS模型含13,644个颗粒，直径25 mm；加载速率0.1 m/s。标定后UCS误差1.82%，弹性模量误差2.39%，BTS误差9.4%，所有参数误差在10%以内。标定得到的微观参数见表3。[Liu 2022, pp. 4-6][Liu 2022, pp. 6-8? Table 3 in pp. 6-7 but parameters listed in pp. 6-8 fragment]
- 岩石切削模拟：PDC刀具直径12 mm，后倾角15°，切削深度0.8、1.2、1.6、2.0 mm，模型底边固定Y方向，左右两侧施加0、10、20、30 MPa侧向压力，总切削距离5 mm，模型含35,078个颗粒。[Liu 2022, pp. 6-7]
- 岩石压入模拟：楔形刀具楔角90°和120°，刀尖半径1 mm，压入速度0.1 m/s，最大压深1.5 mm，岩石模型尺寸60 mm×50 mm，含84,061个颗粒，侧向压力0、10、20、30 MPa。[Liu 2022, pp. 10-12]
- 监测裂纹类型（晶内拉伸、晶内剪切、晶间拉伸、晶间剪切）、数量、岩屑体积、切削力或压入力曲线。[Liu 2022, pp. 6-13]

## Key Findings
1. 在岩石切削和压入过程中，始终产生四类微裂纹：晶内拉伸裂纹、晶内剪切裂纹、晶间拉伸裂纹、晶间剪切裂纹，其中晶间拉伸裂纹和晶内剪切裂纹占主导，几乎不出现晶间剪切裂纹。[Liu 2022, pp. 13-14]
2. 切削过程中，裂纹总数在切削初期突然增加，其增量与切削力峰值直接相关：峰值出现时裂纹总数增加，峰值越大、越密集，裂纹增幅越明显；当峰值很低时裂纹数量几乎不变，曲线近似水平，这是因为刀具尚未接触的区域已被提前破坏。[Liu 2022, pp. 13-14][Liu 2022, pp. 8-10]
3. 无侧向压力时，压入产生的径向裂纹路径绕过大颗粒、穿过大颗粒薄弱点或沿晶界扩展，径向裂纹主要由晶间拉伸裂纹和少量穿晶的晶内剪切裂纹组成。[Liu 2022, pp. 13-14][Liu 2022, pp. 10-12]
4. 侧向压力是影响岩石压入破岩效率的关键因素：增大侧向压力明显抑制径向裂纹的萌生和扩展，裂纹数量急剧减少，破岩效率低；侧向压力对压入力影响很小，可能原因是远场侧向压力对压头尖端周围应力场的影响远小于自由面的存在。[Liu 2022, pp. 13-14][Liu 2022, pp. 12-13]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 嵌入真实晶粒边界的扩展GBM模型能够重现花岗岩切削与压入的宏观力学行为和微裂纹特征，标定误差<10% | [Liu 2022, pp. 4-6] | 颗粒半径0.075–0.125 mm，UCS和BTS试验标定 | 该模型为全部分析的基础 |
| 切削中晶间拉伸裂纹始终占主导，晶间剪切裂纹几乎为0，晶内裂纹主要为剪切型 | [Liu 2022, pp. 6-8][Liu 2022, pp. 8-10] | PDC刀具，后倾角15°，Dc=0.8–2.0 mm，Pc=0–30 MPa | 切削距离5 mm时的统计结果 |
| 当Dc=1.6 mm时，切削深度线通过弱区（4号晶粒及大量晶界），裂纹对侧向压力不敏感，岩屑体积异常大 | [Liu 2022, pp. 6-8] | 侧向压力0–30 MPa | 弱区与直接损伤区重叠导致大量晶间拉伸裂纹持续萌生 |
| 在Pc=30 MPa时，晶粒过度挤压导致远离损伤区出现大量晶间拉伸裂纹，裂纹总数再度上升 | [Liu 2022, pp. 6-8] | 切削模型，侧向压力30 MPa | 与Pc=20 MPa时裂纹总数下降形成对比，说明存在一个压制晶界开裂的中间压力区间 |
| 无侧向压力时压入产生贯穿岩石的径向裂纹，路径绕过粗晶粒或沿晶界扩展 | [Liu 2022, pp. 10-12] | 楔角90°和120°，P0=0 | 径向裂纹以晶间拉伸裂纹为主 |
| P0≥20 MPa时径向裂纹受抑制，压入破岩效率低 | [Liu 2022, pp. 10-12][Liu 2022, pp. 13-14] | 楔角90°和120° | 侧向压力为影响压入效率的直接因素 |
| 压入力对侧向压力不敏感，不同P0下两种楔角刀具的力曲线差异不大 | [Liu 2022, pp. 12-13] | 楔角90°和120°，P0=0–30 MPa，压深1.5 mm | 可能因压头尖端周围应力场受自由面主导 |
| 晶间拉伸裂纹的数量变化趋势与裂纹总数一致性高于晶内剪切裂纹 | [Liu 2022, pp. 12-13][Liu 2022, pp. 8-10] | 切削和压入过程 | 裂纹总数的主要贡献者是晶间拉伸裂纹 |

## Limitations
- 模型为二维（PFC2D），无法完全反映三维裂纹形态和三维晶粒互锁效应。[Liu 2022, pp. 2-3]
- 六种矿物界面的SJM参数统一赋值，实际不同矿物接触界面力学性质可能存在差异，标定结果依赖于该简化假设。[Liu 2022, pp. 3-4]
- 标定和模拟仅针对一种花岗岩（随州花岗岩），结论的普适性需在其他岩石类型中验证。[Liu 2022, pp. 3-4]
- 模拟采用的加载速率为恒定值（切削速度/压入速度固定），未考虑实际钻井中的动态冲击和速度变化。
- 未考虑钻井液压力、孔隙流体等井下环境因素。
- 切削深度仅取离散值0.8–2.0 mm，侧向压力最大30 MPa，未能连续扫参。

## Assumptions / Conditions
- 岩石被视为由不同矿物颗粒组成的非均质集合体，晶粒内部采用平行黏结模型，晶粒界面采用光滑节理模型。[Liu 2022, pp. 3-4]
- 颗粒为刚性体，颗粒间作用力与力矩按牛顿第二定律和力‑位移定律更新。[Liu 2022, pp. 2-3]
- 所有矿物内PBM接触的摩擦系数均设为0.5，平行黏结半径乘子为1.0。[Table 3, Liu 2022, pp. 6-7]
- 岩石模型底边Y方向固定，左右两侧施加均布侧向压力，未考虑地应力梯度。
- 刀具视为刚体，不考虑磨损。
- 校准中假设当模拟宏观参数（UCS、弹性模量、BTS）与实验值误差小于10%时，微观参数即为合理。[Liu 2022, pp. 4-6]
- 分析裂纹时，将接触断裂类型按位置（晶内/晶间）和模式（拉伸/剪切）分类。[Liu 2022, pp. 6-10]

## Key Variables / Parameters
**输入变量/控制参数**：
- 切削深度 $D_c$ (0.8, 1.2, 1.6, 2.0 mm)
- 侧向压力 $P_c$ (切削模型) 或 $P_0$ (压入模型) (0, 10, 20, 30 MPa)
- 压入刀具楔角 (90°, 120°)
- PDC刀具后倾角 (15°)

**材料微观参数**（标定后）：
- 颗粒半径范围：7.5×10⁻⁵～1.25×10⁻⁴ m
- 矿物密度：2,600～2,850 kg/m³
- PBM参数：接触模量4.01～10.35 GPa，法向/切向刚度比1.0～2.0，平行黏结拉伸强度106.22～120.0 MPa，黏结内聚力37.18～42.0 MPa，摩擦角30°
- SJM参数（所有界面统一）：法向/切向刚度1×10¹³ N/m，黏结拉伸强度6.0 MPa，黏结内聚力75.0 MPa，摩擦角65°，摩擦系数0.7

**输出变量**：
- 四类裂纹数量（总裂纹数及各类数量）
- 岩屑体积（通过断裂颗粒近似表征）
- 切削力/压入力时程曲线及峰值特征
- 直接损伤区与间接损伤区范围

## Reusable Claims
1. 在PDC切削花岗岩（后倾角15°）的过程中，无论侧向压力在0～30 MPa间如何变化，晶间拉伸裂纹始终是数量最多的裂纹类型，其次为晶内剪切裂纹，晶间剪切裂纹几乎为零；这一微裂纹类型分布结构可作为硬岩切削数值模型的检验判据。[Liu 2022, pp. 6-10][Liu 2022, pp. 13-14]
2. 对于脆性花岗岩切削，侧向压力对岩屑体积无显著影响，而切削深度是决定岩屑大小的主控因素。因此在钻井参数优化中，应优先通过调节切削深度来控制破岩效率，而非依赖围压的改变。[Liu 2022, pp. 8-10][Liu 2022, pp. 13-14]
3. 在楔形刀具压入花岗岩时，若缺乏侧向压力（或侧向压力很低），径向裂纹容易贯穿岩石，裂纹路径呈现“选择性”，即绕过粗大颗粒或沿晶界及颗粒弱面扩展；该选择性扩展规律可用于预测断裂面走向。[Liu 2022, pp. 10-12][Liu 2022, pp. 13-14]
4. 当侧向压力增大至20 MPa及以上时，径向裂纹的萌生与扩展被显著抑制，导致压入方式破岩效率极低，因此在大侧向压力条件下不建议采用压入破岩方式。[Liu 2022, pp. 13-14][Liu 2022, pp. 10-12]
5. 楔形压头压入力对远场侧向压力不敏感，其可能机理是压头尖端应力场主要由自由面控制，远场围压影响较小。这一现象可用于简化压入力预测模型，忽略中等侧向压力的修正项。[Liu 2022, pp. 12-13][Liu 2022, pp. 13-14]
6. 在切削和压入两种工具-岩石相互作用模式下，裂纹总数的增长均与力曲线的峰值出现同步，且峰值越大、越密集，裂纹增幅越明显；当力曲线处于低值平台时，微裂纹数量几乎不增加。该关系可用于实时监控破岩过程中的损伤演化。[Liu 2022, pp. 8-10][Liu 2022, pp. 12-13]

## Candidate Concepts
- [[extended grain-based model]]
- [[heterogeneous granite]]
- [[digital image processing for rock modeling]]
- [[microcrack type classification]]
- [[intergranular tensile crack]]
- [[intragranular shear crack]]
- [[grain boundary strengthening by lateral pressure]]
- [[radial crack inhibition]]
- [[lateral pressure insensitivity of indentation force]]
- [[rock cutting efficiency]]
- [[rock indentation efficiency]]
- [[parallel bond model (PBM)]]
- [[smooth joint model (SJM)]]
- [[particle flow code (PFC2D)]]
- [[calibration of discrete element model]]
- [[direct damage zone]]
- [[indirect damage zone]]
- [[cutting chips volume]]
- [[weak area effect on crack propagation]]

## Candidate Methods
- [[extended grain-based model with real grain shape embedding]]
- [[digital image processing for mineral boundary extraction]]
- [[PFC2D simulation of PDC cutter rock cutting]]
- [[PFC2D simulation of wedge indentation]]
- [[microscopic parameter calibration via UCS and BTS tests]]
- [[crack type counting and classification in DEM]]
- [[cutting force-crack correlation monitoring]]
- [[indentation force-indentation depth curve analysis]]

## Connections To Other Work
- 该研究在传统Voronoi多边形颗粒基模型（GBM）基础上，采用数字图像处理技术提取真实岩石晶粒边界，克服了Voronoi多边形平滑边界的不足，同时参考了Peng等（2017; 2019）和Zhang等（2020）的GBM框架，但注重了晶粒锯齿状不规则互锁结构。[Liu 2022, pp. 3-4]
- 切削力学和压入力学的基本区分参照Nishimatsu（1972）、Kalyan等（2015）等文献，模型所用PDC切削及楔形压入与室内实验（如Cheng等2019；Liu等2007；Zhu等2017）相呼应。
- 侧向压力对压入力的不敏感性可由线弹性断裂力学中近尖端应力场受自由表面控制的理论解释，即远场围压效应被自由表面主导的应力奇异性所淹没。
- 裂纹类型以晶间拉伸裂纹为主的现象与许多脆性结晶岩在低围压下的微裂纹扩展模式一致，例如Saadat和Taheri（2019; 2020）的黏结颗粒基模型模拟结果。
- 研究中切削力峰值与裂纹突增同步的发现与声发射监测原理相通，可为室内试验和现场监测提供数值依据。

## Open Questions
- 三维扩展GBM模型（考虑真实三维晶粒形状）对裂纹扩展和破岩效率的预测与二维结果的差异如何？
- 若对不同矿物界面赋予差异化的SJM参数（如斜长石‑石英界面与黑云母‑钾长石界面性质不同），结论中的裂纹主导类型和数量趋势是否会改变？
- 切削速度、冲击载荷和热‑力耦合效应对微裂纹演化有何影响？现有恒定低速条件是否适用于实际钻井工况？
- 钻井液压压力、孔隙流体及地层温度如何与工具‑岩石相互作用耦合，影响裂纹萌生和扩展？
- 该模型在页岩、碳酸盐岩等其他岩类中的适用性以及相应的微观参数标定路径。
- 侧向压力对压入力的不敏感性是否存在一个阈值，超过该阈值后远场围压开始影响压头尖端的应力场？
- 如何在工程中利用文中发现的“弱区重叠导致岩屑体积异常”现象，主动设计切削路径以提升破岩效率？

## Source Coverage
本页面由全部12个索引片段编译而成。经审计，非空源文本块共计12块，已全部处理；覆盖字符数58,453字（片段总字符数58,981字），覆盖比率（按块）为1.0，覆盖比率（按字）约为99.1%，未发生片段遗漏或伪造内容。所有事实性主张均忠实于源片段提供的证据。 [Source signature: 15d85fbb3c52d9165e36724dd0e3ff3028a3e7b8]
