---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
title: "Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer."
status: "draft"
source_pdf: "data/papers/2011 - Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.pdf"
collections:
  - "zotero new"
citation: "Bae, Dae-seok, et al. \"Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.\" *Rock Mechanics and Rock Engineering*, vol. 44, 2011, pp. 497–504. DOI: 10.1007/s00603-011-0134-9."
indexed_texts: "6"
indexed_chars: "27268"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:11:21"
---

# Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.

## One-line Summary
提出一种利用钻孔电视（BHTV）图像的扫描圆技术，结合分形几何定量估算节理粗糙度系数（JRC），并构建了基于 Barton 标准剖面的 JRC‑分形维数（D）三阶多项式关系式，为从钻孔数据高效获取岩体节理粗糙度提供了方法 [Bae 2011, pp. 1-8]。

## Research Question
如何从钻孔电视图像中快速、可靠地评估岩体节理粗糙度系数（JRC），以克服传统岩芯直线扫描线法取样困难、方向代表性不足和处理工作量大等问题？

## Study Area / Data
研究基于某地下工程的侏罗纪花岗岩钻孔，深度 EL. 67.0–67.6 m [Bae 2011, pp. 2-3]。使用声波/光学钻孔电视（BHTV）获得的孔壁图像，声波图像分辨率为 1 像素/mm，光学照片图像分辨率可达 20 像素/mm [Bae 2011, pp. 2-3]。数据处理在 WellCAD 环境中完成。节理粗糙度的标定采用 Barton 的 10 条标准粗糙度剖面（JRC 范围 0–20）[Bae 2011, pp. 1-6]。

## Methods
1. **从 BHTV 图像提取节理粗糙度剖面**：将孔壁图像上呈正弦曲线状的节理椭圆展开，通过设定参考正弦曲线确定节理的倾角和倾向。在参考线上等间距设置与其垂直的标尺条，覆盖整个椭圆周长，形成扫描圆，从而提取出一条连续的粗糙度剖面 [Bae 2011, pp. 2-3]。
2. **分形维数计算**：采用分规法（divider method），用 1、2、4、8、16、32、64 mm 七级标尺长度 r 测量剖面长度，通过 log(N·f/r) 对 log(r) 的线性段斜率得到分形维数 D [Bae 2011, pp. 3-6]。
3. **JRC‑D 关系标定**：同样用分规法计算 Barton 的 10 条标准剖面的 D 值（表 1），建立 JRC 范围与 D 的三阶多项式关系（式 2）：JRC(D) = 7,811,778.9281 D³ − 23,723,041.6842 D² + 24,014,672.3562 D − 8,103,409.7809 [Bae 2011, pp. 3-6]。
4. **应用与验证**：对花岗岩钻孔中的节理应用扫描圆技术求得 D，再由式 2 得到 JRC 值，并与同段岩芯的三个直线扫描线（机械轮廓仪，间距 1 mm）得出的 JRC 值（6.00、8.82、10.29）进行对比 [Bae 2011, pp. 6-7]。

## Key Findings
- 扫描圆技术能够从 BHTV 图像的椭圆周长中提取连续的粗糙度剖面，为节理提供平均 JRC 值，并可结合半圆扫描评估方向性各向异性范围 [Bae 2011, pp. 7-8]。
- 用 Barton 的 10 条标准剖面拟合出的三阶多项式（式 2）良好地描述了 JRC 与分形维数 D 的关系，可用于由分形维数直接估算 JRC 范围 [Bae 2011, pp. 3-6]。
- 所选侏罗纪花岗岩节理的扫描圆 JRC 值为 9.6，落在岩芯三个直线扫描线 JRC 值（6.00–10.29）之间，被认为更能代表该节理面的平均粗糙度 [Bae 2011, pp. 6-7]。
- 该方法可在 WellCAD 工作环境下批量处理大量钻孔数据（如累积长度数千米的钻孔），显著提高了大型地下工程（如放射性废物处置设施）前期岩体分类中节理粗糙度数据的获取效率与可靠性 [Bae 2011, pp. 7-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|--------|
| Barton 标准剖面的 JRC 范围与分形维数 D 的关系被拟合为三阶多项式（式 2），用于由 D 预估 JRC。 | [Bae 2011, pp. 3-6] | 所用标尺 r = 1,2,4,8,16,32,64 mm；分形维数通过分规法求得。 | 多项式系数给出至小数点后 4 位。 |
| Barton 标准剖面的分形维数 D 实测值（部分）：JRC 0–2 对应 D=1.000395；JRC 2–4 对应 D=1.000885；JRC 4–6 对应 D=1.001553；JRC 6–8 对应 D=1.002749。 | [Bae 2011, pp. 3-6] | 与 Lee et al. (1990) 的 D 值进行了对比，存在微小差异。 | 原文表 1 未完整给出所有 JRC 范围的 D 值。 |
| 花岗岩钻孔中某节理由扫描圆技术得到的 JRC 为 9.6，更接近岩芯三个直线扫描所得 JRC（6.00、8.82、10.29）的均值。 | [Bae 2011, pp. 6-7] | 对比基于同一节理面；直线扫描线沿倾向方向以 1 mm 间隔提取。 | 扫描圆值被视为更能代表平均粗糙度。 |
| 当钻孔壁因高倾角节理或断层破裂带而出现图像不匹配时，可借助岩芯照片进行对比修正。 | [Bae 2011, pp. 6-7] | 条件：钻孔破碎带、节理倾角高，可能产生图像上下尖灭缺失。 | 未明确给出修正的具体操作流程。 |
| 通过半圆扫描可以获取节理粗糙度方向各向异性的范围。 | [Bae 2011, pp. 7-8] | 未给出具体各向异性计算案例。 | 建议与直剪试验配合校准。 |

## Limitations
- 在高倾角节理或断裂带附近，BHTV 图像上下盘可能出现机械破碎导致的错位，需要人工通过岩芯照片平滑修正，主观性强且会增加工作量 [Bae 2011, pp. 6-7]。
- 分形维数的计算依赖所选标尺范围（1–64 mm），该方法在不同标尺范围下对 JRC 预估的影响未进行系统讨论。
- 三阶多项式仅拟合自 Barton 的 10 条标准剖面，并未通过大量天然节理的粗糙度与直剪试验进行广泛校准；文中明确指出仍需结合直剪试验做对比研究 [Bae 2011, pp. 7-8]。
- 扫描圆技术仅能给出沿椭圆的连续剖面，对于节理面的三维起伏特征（如平台、阶步）仍存在信息压缩，由此带来的不确定性未从索引片段中确认。
- 半圆扫描给出的方向各向异性范围仅作为概念提出，其具体算法和有效性验证未提供。

## Assumptions / Conditions
- 假设节理粗糙度剖面具有统计自仿射分形特征，可通过分形维数 D 表征 [Bae 2011, pp. 1-2]。
- 分规法计算 D 要求 r 小于总剖面长度；文中采用的 1–64 mm 满足了此条件 [Bae 2011, pp. 3-6]。
- BHTV 图像的分辨率（最优 20 像素/mm）足以捕捉决定 JRC 的中小型粗糙度特征。
- 预设 Barton 的 10 条标准剖面覆盖了 JRC 0–20 的全范围，且分形维数与 JRC 的关系在此区间内连续、可用单一多项式近似。
- 孔壁椭圆展开获得的二维剖面能够代表节理面的整体粗糙特性，忽略三维几何的局部偏差。
- 提取剖面时需手动或半自动确定参考线及标尺线，假定操作者的选择有足够一致性。

## Key Variables / Parameters
- JRC：节理粗糙度系数，取值范围 0–20 [Bae 2011, pp. 1-2]。
- D：分形维数，由分规法斜率求得 [Bae 2011, pp. 3-6]。
- 分规标尺长度 r (mm)：1、2、4、8、16、32、64 [Bae 2011, pp. 3-6]。
- 式 2 的三阶多项式系数 [Bae 2011, pp. 3-6]。
- BHTV 图像分辨率：1 像素/mm（声波）至 20 像素/mm（光学）[Bae 2011, pp. 2-3]。
- 节理产状：倾向（dip direction）和倾角（dip angle），通过拟合正弦曲线获得 [Bae 2011, pp. 2-3]。

## Reusable Claims
- **Claim 1**：利用 BHTV 图像椭圆圆周的扫描圆提取的粗糙度剖面可得到一个平均 JRC 值，该值比沿倾向的单个直线扫描线更全面，尤其适合岩体分类。条件：孔壁图像完整、节理可辨认；限制：当节理面存在严重三维起伏或高角度时，代表性需结合半圆扫描验证。[Bae 2011, pp. 6-8]
- **Claim 2**：使用分规法（r = 1–64 mm）计算 Barton 标准剖面的分形维数，可通过三阶多项式（式 2）将 D 转换为 JRC，实现对粗糙度的工程尺度估算。条件：分形维数计算采用相同的标尺系列和表达式；限制：该标定仅基于理想化标准剖面，直接用于天然节理可能导致偏差。[Bae 2011, pp. 3-6]
- **Claim 3**：扫描圆技术在 WellCAD 环境中能够半自动处理大量钻孔节理数据，显著减少人工提取直线扫描线的工作量。条件：拥有 BHTV 成像数据和 WellCAD 软件；限制：前提是能够自动或半自动提取节理正弦曲线作为参考线。[Bae 2011, pp. 7-8]
- **Claim 4**：半圆扫描可提供对节理粗糙度方向各向异性范围的初步估计，但该方法的定量可靠性和普适性仍需通过定向直剪试验校准。[Bae 2011, pp. 7-8]

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[fracture roughness]]
- [[Barton standard profiles]]
- [[fractal dimension]]
- [[divider method]]
- [[borehole televiewer (BHTV)]]
- [[scan circle technique]]
- [[rock mass classification]]
- [[shear strength of rock joints]]
- [[anisotropy of joint roughness]]
- [[WellCAD]]
- [[mechanical profilometry]]
- [[dip direction and dip angle]]

## Candidate Methods
- [[scan line method]]
- [[photo-analysis techniques for roughness]]
- [[laser scanning for roughness]]
- [[mechanical profilometry]]
- [[fractal geometry for rock joints]]
- [[borehole imaging processing]]
- [[sine curve fitting for joint orientation]]
- [[half-circle scan method]]

## Connections To Other Work
- 本研究直接建立在 Barton and Choubey (1977) 的 JRC 概念及十条标准剖面的基础上。
- 分形维数用于量化节理粗糙度的思路与 Brown and Scholtz (1985)、Carr and Warriner (1987)、Lee et al. (1990)、Odling (1994) 等一致；并特别将本研究的标准剖面分形维数与 Lee et al. (1990) 的结果进行了对比。
- 在粗糙度测量方法上，引用了 Franklin et al. (1986, 1988) 等的照片分析技术、Fardin et al. (2004) 的激光扫描以及 Unal et al. (2004) 的数字摄影测量方法，但强调这些方法仅限于少量样品，而本技术可处理大量钻孔数据。
- 文中提到进一步需要结合直接剪切试验（如 Kulatilake et al. 1995, 2006 等关于各向异性峰值剪切强度的研究）来验证和扩展扫描圆获得的 JRC 值的工程实用性。

## Open Questions
- 半圆扫描量化的方向各向异性如何定量耦合到各向异性剪切强度准则中？未从索引片段中确认。
- 该技术对于除花岗岩外的其他岩石类型、风化节理或含有填充物的节理的适用性如何？未从索引片段中确认。
- 在超出 1–64 mm 的标尺范围外，分形维数与 JRC 的三阶多项式关系是否仍然成立？
- 扫描圆给出的平均 JRC 值与直剪试验得到的不同方向剪切强度之间的定量关系是否可靠？文中明确指出需要大量对比试验。
- 如何处理孔径变化、井壁崩落等导致的 BHTV 图像失真对粗糙度剖面提取的影响？未从索引片段中确认。

## Source Coverage
本知识页依据本论文的 6 个索引片段构建，覆盖了引言、方法（包括扫描圆操作步骤、分形维数计算与标准剖面标定）、研究案例结果、讨论与结论的主要内容。对 Barton 标准剖面的分形维数数据仅显示了部分 JRC 范围的 D 值，未包含完整的表 1 和图 2–5 的详细数值。关于该技术的自动化程度、三维验证测试以及与其他工程项目的集成情况等信息，在现有片段中未深入提供或完全缺失。
