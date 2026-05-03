---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2015-ziegler-characterisation-of-natural-fractures-and-fracture-zones-of-the-basel-egs-reservoir"
title: "Characterisation of Natural Fractures and Fracture Zones of the Basel EGS Reservoir Inferred from Geophysical Logging of the Basel-1 Well."
status: "draft"
source_pdf: "data/papers/2015 - Characterisation of Natural Fractures and Fracture Zones of the Basel EGS Reservoir inferred from Geophysical Logging of the Basel-1 Well.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Ziegler, Martin, et al. \"Characterisation of Natural Fractures and Fracture Zones of the Basel EGS Reservoir Inferred from Geophysical Logging of the Basel-1 Well.\" *Proceedings World Geothermal Congress 2015*, Melbourne, Australia, 19-25 Apr. 2015."
indexed_texts: "12"
indexed_chars: "55440"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:17:41"
---

# Characterisation of Natural Fractures and Fracture Zones of the Basel EGS Reservoir Inferred from Geophysical Logging of the Basel-1 Well.

## One-line Summary
基于对深达 5 km 的 Basel-1 井的地球物理测井（尤其是超声波井眼成像 UBI 数据），识别并刻画了结晶基底中的天然裂缝与裂缝密集带，并借助新型粘滑校正方法显著改善了深部图像质量，从而获得了更可靠的裂缝分布与方向特征 [Ziegler 2015, pp. 1-1, 1-2, 5-5]。

## Research Question
如何从质量受粘滑效应影响的基岩深孔 UBI 图像中，系统区分天然裂缝与钻井诱导裂缝，定量描述裂缝频率的空间分布与方位分组，并在此基础上识别可能影响储层力学与流动行为的高裂缝频率带。未从索引片段中确认是否提出了明确的水力耦合问题。

## Study Area / Data
- **地点**：瑞士西北部巴塞尔市，上莱茵地堑南部 Basel 地块 [Ziegler 2015, pp. 2-3]。
- **井**：Basel-1 钻孔，近似垂直，深度 5009 m（自转盘面算起），完钻于 2006 年 [Ziegler 2015, pp. 1-2]。
- **数据段**：地球物理测井覆盖 2.6 km（花岗岩古风化面以下约 100 m）至 5.0 km，包括：
  - 超声波井眼成像 (UBI)、双井径、自然伽马能谱、声波全波列 (p 波与 s 波速度)、密度、井温 [Ziegler 2015, pp. 1-1, 3-4]。
  - 岩屑分析结果作为岩性约束 [Ziegler 2015, pp. 1-1, 2-3]。
- **岩性**：主要岩性由钻屑分析确定为黑云母花岗岩、二长花岗岩和正长岩 [Ziegler 2015, pp. 7-10]。

## Methods
1. **UBI 数据预处理**：针对 4.7 km 以下因工具粘滑运动导致的严重图像畸变，利用加速度计数据开发了一种新颖的校正方法，恢复真实图像 [Ziegler 2015, pp. 1-1, 4-5]。
2. **天然裂缝识别与分类**：
   - 天然裂缝定义为沿井壁呈完整正弦轨迹的反射特征，归类为 “确定” (certain) 天然裂缝；那些终止于已知天然裂缝、无完整正弦轨迹的特征被归为 “不确定” (uncertain) [Ziegler 2015, pp. 4-5]。
   - 钻井诱导裂缝 (如轴状 A-DITF、雁列状 E-DITF 等) 通过其与井壁几何关系的特殊性及与应力诱发井壁破坏的空间关系予以排除 [Ziegler 2015, pp. 4-5]。
   - 不能明确归属的特征标记为 “不确定”，视为潜在天然裂缝 [Ziegler 2015, pp. 4-5]。
3. **裂缝频率与裂缝密集带识别**：
   - 计算随深度的裂缝线密度 (fractures/m) [Ziegler 2015, pp. 5-5]。
   - 将剖面分为两段 (2.6–2.65 km 与 2.65–3.0 km) 以去除背景趋势，获得残余裂缝频率。10 m 平均窗下，残余频率 ≥ 0.5 fractures/m 的区间视为高裂缝频率，连接相邻段形成 FZ-10m 带；两侧若残余频率 ≥ 0.25 fractures/m 也并入该带。2 m 平均窗下，以 ≥ 1 fractures/m 为主阈值，并对长度 ≤ 4 m 的段使用更高阈值 ≥ 3 fractures/m，相邻 ≥ 0.5 fractures/m 区间也并入，形成 FZ-2m 带 [Ziegler 2015, pp. 5-5]。
4. **裂缝组方向分析**：通过极点等面积投影聚类，在 200 m 间隔内识别出多达 6 个潜在裂缝组 [Ziegler 2015, pp. 1-1, 5-5]。
5. **低波速与低密度异常带识别**：通过目视识别密度和 p 波速度剖面中低于局部背景的负异常段，标记为低密度区 (LDZ) 和低速度区 (LVZ)。作者指出此过程为临时性，可能未捕获所有异常 [Ziegler 2015, pp. 5-5]。

## Key Findings
- **裂缝数量与深度趋势**：总共识别出 1164 条天然裂缝，其中确定裂缝 875 条，不确定裂缝 289 条。不确定裂缝的比例随深度增加，由顶部约 14% 上升至最深段约 63% [Ziegler 2015, pp. 5-7]。裂缝频率整体随深度降低：近顶部 (约 2.6 km) 约 3.1 fractures/m，3.0 km 以下降至约 0.3 fractures/m [Ziegler 2015, pp. 1-1]。
- **与前人研究的对比**：经过粘滑校正后，在 >4.7 km 的裸眼段识别出的天然裂缝数量少于此前研究 [Ziegler 2015, pp. 1-1, 5-7]。不同研究间的裂缝总数存在显著差异，局部差异位置已汇总于文中 Table 4 [Ziegler 2015, pp. 7-10]。
- **高裂缝频率带**：应用 10 m 窗识别出 29 个 FZ-10m 带，长度可达 100 m；应用 2 m 窗识别出 43 个 FZ-2m 带，长度可达 28 m。4 km 以下二者分布几乎一致 [Ziegler 2015, pp. 5-7]。
- **裂缝密集带与物性异常**：2.6–3.0 km 段的高裂缝频率与低 p 波速度和低动态杨氏模量明显相关，但密度受其影响较小。总共拾取 37 个局部低速 / 低密度异常带，其中 22 个同时显示两种低异常 [Ziegler 2015, pp. 7-10]。
- **裂缝组复杂性与分布**：沿井筒的 200 m 深度区间内呈现最多 6 个裂缝组的复杂格局，具体方位参数未从索引片段中确认 [Ziegler 2015, pp. 1-1, 5-5]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 识别天然裂缝总数 1164 条，其中 875 条确定，289 条不确定 | [Ziegler 2015, pp. 5-7] | UBI 数据经粘滑校正和人工判别 | 不确定裂缝占比 14% (浅部)–63% (4.6–5.0 km) |
| 裂缝频率：2.6 km 附近约 3.1 frac/m，3.0 km 以下降至约 0.3 frac/m | [Ziegler 2015, pp. 1-1] | 基于确定与不确定裂缝合并频率 | 未说明使用何种平均窗长 |
| 应用 10 m 窗识别 FZ-10m 带 29 个，最大长度 100 m；2 m 窗识别 FZ-2m 带 43 个，最大长度 28 m | [Ziegler 2015, pp. 5-7] | 阈值设定见 Methods 节 | 4 km 以下两种窗长结果几乎相同 |
| 识别 37 个低速或 / 和低密度异常带（LDZ/LVZ），其中 22 个兼具两者 | [Ziegler 2015, pp. 7-10] | 目视识别，作者注明为临时性方法 | 未给出具体阈值；2.6–3.0 km 处裂缝高频带与低 vP 和低 E 相关 |
| 经加速度计校正后，在 >4.7 km 裸眼段识别的天然裂缝少于此前研究 | [Ziegler 2015, pp. 1-1] | 与 Fabbri (2011) 及 Ladner (2014, pers. comm.) 结果对比 | 具体数量差异未从片段中确认 |
| UBI 井径与机械井径一致，表明 UBI 未出现信号丢失 | [Ziegler 2015, pp. 3-4] | 工具居中，记录速度 4 m/min | 排除了因返回脉冲超时导致的误差 |

## Limitations
- 仅基于单井数据，裂缝组及裂缝带的横向延伸未约束。识别裂缝密集带和低物性异常的高度依赖于所选窗长和阈值 [Ziegler 2015, pp. 5-5]。
- 区分天然与钻井诱导裂缝存在固有困难，尤其是部分不确定裂缝可能造成裂缝总数的偏差；深部不确定比例升高进一步增加了不确定性 [Ziegler 2015, pp. 5-7]。
- 低速 / 低密度带的拾取采用临时视觉方法，可能遗漏部分异常带或引入主观性 [Ziegler 2015, pp. 5-5]。
- 未从索引片段中确认裂缝的水力开启性及其与地应力场的直接关系。
- 粘滑校正过程细节未在片段中展开，其残余误差对裂缝识别的影响未知。

## Assumptions / Conditions
- UBI 工具居中，井壁反射声波的测量未出现信号超时，并基于流体速度将传播时间转换为井径 [Ziegler 2015, pp. 3-4]。
- 天然裂缝的可识别性依赖于其呈现完整正弦轨迹；部分断裂终止于已知天然裂缝的特征被排除，可能低估了真实裂缝数量 [Ziegler 2015, pp. 4-5]。
- 裂缝频率背景趋势的去除假设 2.6–3.0 km 段存在明显差异，将其一分为二以获取统一背景 0.3 fractures/m [Ziegler 2015, pp. 5-5]。
- 井壁崩落对裂缝视倾角的影响小于 3°，因此未对倾角进行非圆柱井眼校正 [Ziegler 2015, pp. 4-5]。

## Key Variables / Parameters
- **裂缝线密度** (fractures/m) 及残余裂缝频率 (residual fracture frequency)
- **裂缝组极点聚类** 所定义的组数 (最多 6 组)
- **窗长与阈值**：10 m 窗 ‑ 主阈值 0.5 frac/m，合并阈值 0.25 frac/m；2 m 窗 ‑ 主阈值 1 frac/m，短段阈值 3 frac/m，合并阈值 0.5 frac/m
- **岩石物性**：p 波速度 (vP)、密度 (ρb)、动态杨氏模量
- **井筒几何**：UBI 井径 (CSA)、机械井径
- **深度范围**：2600–5000 m；关键转换深度 3000 m、4677 m (粘滑起始)
- **裂缝分类**：确定 (certain) 天然裂缝、不确定 (uncertain) 天然裂缝、钻井诱导裂缝 (A-DITF, E-DITF, DIF)

## Reusable Claims
- **粘滑校正改善 UBI 图像**：在 4.7 km 以下裸眼段，利用随附加速度计数据对 UBI 日志进行粘滑校正，可显著提高图像质量，从而减少基于失真图像误判的天然裂缝数量。校正后的裂缝数少于早期研究 [Ziegler 2015, pp. 1-1]。适用条件：工具存在明显卡顿，且记录了处理所需的加速度计信息；限制：校正效果受原始数据质量影响，且仅在本文所述井段得到验证。
- **裂缝频率随深度衰减**：在巴塞尔基底，天然裂缝频率从约 2.6 km 的 3.1 frac/m 急剧降至 3.0 km 以下的约 0.3 frac/m，表明风化带或浅部应力释放对裂缝密集度贡献显著 [Ziegler 2015, pp. 1-1]。适用条件：结晶基底，古风化面以下；限制：深度趋势可能受岩性变化影响。
- **裂缝组方向表现出沿井的复杂性**：在 200 m 间隔内可检测到多达 6 个裂缝组，说明单一构造体制不足以解释全井段的裂缝取向 [Ziegler 2015, pp. 1-1]。具体方位未提供，必须配合详细的构造背景使用。
- **高裂缝频率对岩石动力模量影响显著**：深度 2.6–3.0 km 的高裂缝频率带同时对应低 p 波速度和低动态杨氏模量，但密度变化不大；因此联合 p 波速度与裂缝频率有助于识别力学性质弱化带 [Ziegler 2015, pp. 7-10]。适用条件：完整结晶岩基质，裂缝为主要控制物性差异的因素；限制：该相关性在更深处是否成立有待检验。

## Candidate Concepts
- [[增强型地热系统 (EGS)]]
- [[天然裂缝储层]]
- [[超声波井眼成像 (UBI)]]
- [[粘滑运动校正]]
- [[钻井诱导裂缝 (A-DITF, E-DITF)]]
- [[裂缝频率剖面]]
- [[裂缝组方向聚类]]
- [[裂缝密集带 (FZ-10m, FZ-2m)]]
- [[低速异常带 (LVZ)]]
- [[低密度异常带 (LDZ)]]
- [[上莱茵地堑]]
- [[结晶基底]]
- [[动态杨氏模量]]
- [[古风化带]]

## Candidate Methods
- [[基于加速度计数据的 UBI 图像校正]]
- [[基于完整正弦轨迹的天然裂缝识别]]
- [[钻井诱导裂缝分类法]]
- [[滑动窗残余频率分析与阈值化]]
- [[极点等面积投影与聚类分析]]
- [[低物性异常带目视识别]]

## Connections To Other Work
- 文中对比了 Fabri (2011) 和 Ladner (2014, pers. comm.) 对该井 UBI 数据的早期裂缝解释，指出裂缝总数及局部频段存在显著差异 [Ziegler 2015, pp. 5-7]。
- 上莱茵地堑的构造背景引用了 Laubscher (2001), Dèzes et al. (2004), 及 Ustaszewski 和 Schmid (2007) 等关于断块划分与地震成因的工作 [Ziegler 2015, pp. 2-3]。
- 主题上可与 [[EGS 储层裂缝网络建模]]、[[地热储层水力耦合]]、[[钻孔成像裂缝解释标准]] 等方法性概念相连。还可连接到 [[Basel EGS 注水诱发地震]] 的序列研究，因该井正是 2006 年发生 ML 3.4 微震的 Basel-1 孔 [Ziegler 2015, pp. 1-2]。

## Open Questions
- 文中识别的裂缝组和裂缝密集带如何影响流体流动通道和储层渗透率的各向异性？未从索引片段中确认有水力测试的对比。
- 断裂带内的具体充填矿物（如石英、方解石）是否影响物性且天然裂缝的持续性（长度）如何？片段未提供。
- 低速度/密度异常带是否全部对应于含水的开放裂缝带，是否存在少量粘土矿物蚀变造成的假异常？临时目视法可能掩盖部分真异常 [Ziegler 2015, pp. 5-5, 7-10]。
- 识别出的裂缝组与上莱茵地堑断层系统（如 NNE 向莱茵断层、Hercynian 向 NW-SE 断层）的具体关联性如何？片段仅提及复杂格局，未给出与特定构造的匹配结果。

## Source Coverage
本 Wiki 页面基于所提供的 12 个索引片段编写，涵盖摘要、引言、研究区背景、数据与方法、部分结果与初步解释。未见完整的讨论与分析章节、全部表格数据及最终结论。因此，关于裂缝组具体产状、FZ 带有无明确力学或地质成因解释、全井段裂缝与物性异常的定量统计对比等可能缺失。
