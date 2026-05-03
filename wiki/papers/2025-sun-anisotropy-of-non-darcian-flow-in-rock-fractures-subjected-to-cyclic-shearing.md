---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-sun-anisotropy-of-non-darcian-flow-in-rock-fractures-subjected-to-cyclic-shearing"
title: "Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing."
status: "draft"
source_pdf: "data/papers/2025 - Anisotropy of non-Darcian flow in rock fractures subjected to cyclic shearing.pdf"
collections:
  - "zotero new"
citation: "Sun, Zihao, et al. \"Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 6373-87, doi:10.1016/j.jrmge.2024.11.026."
indexed_texts: "15"
indexed_chars: "72207"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "72512"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004224"
coverage_status: "full-index"
source_signature: "3ab09b79e8fa424c58aed05c3278bfac1d89ec63"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:55:44"
---

# Anisotropy of Non-Darcian Flow in Rock Fractures Subjected to Cyclic Shearing.

## One-line Summary
循环剪切作用下岩石单裂隙非达西流各向异性演化规律——正交方向黏性渗透率差异显著，而惯性渗透率在正交和相反方向均存在差异；随剪切循环增加正交差异增大、相反差异减小；基于方向性几何参数 Z₂ 和孔径方向性参数 bε 建立了黏性与惯性渗透率的表征模型。

## Research Question
1. 岩石裂隙在循环剪切荷载下，非达西流在四个方向（X⁺、X⁻、Y⁺、Y⁻）的各向异性特征如何？
2. 循环剪切过程如何影响黏性渗透率（kv）和惯性渗透率（ki）的各向异性演化？
3. 能否建立能够区分方向性的渗透率定量表征模型？

## Study Area / Data
- 岩性：山东某采石场的红砂岩，基岩渗透率约 10⁻¹³–10⁻¹⁴ m²，可忽略[Sun 2025, pp. 2-4]。
- 裂隙样本：通过巴西劈裂生成原岩裂隙，经 CNC 雕刻复制为四个组（J1–J4），每组 6 个非吻合裂隙，尺寸 150 mm × 150 mm × 80 mm[Sun 2025, pp. 2-4]。
- 循环剪切次数：0、1、2、3、4、5 次循环，共 24 个样本。
- 流态测试：每个样本在四个方向（平行剪切方向 X⁺/X⁻，垂直剪切方向 Y⁺/Y⁻）以 5 个恒定流量（100–900 mL/min）进行 480 次非达西渗流实验[Sun 2025, pp. 12-13]。
- 几何数据：每次剪切后采用三维激光扫描获取裂隙面点云（精度 X/Y ±0.2 mm, Z ±1 mm），构建数字裂隙模型[Sun 2025, pp. 4-5, 10-11]。

## Methods
- 循环剪切实验：恒法向荷载（CNL）条件，法向应力 0.8 MPa，剪切速率 2 mm/min，剪切振幅 8 mm，方向沿 X 轴往复[Sun 2025, pp. 4-5]。
- 非达西流实验：采用 Y-1000 平流泵，恒定流量注入，通过进水/出水水箱切换实现四个流动方向；入口、出口压力传感器记录，60 Hz 采样，1 分钟均值作为读数[Sun 2025, pp. 4-5]。
- 数据处理：用 Forchheimer 方程（−∇P = AQ + BQ²）拟合得到黏性系数 A 和惯性系数 B，进而换算为黏性渗透率 kv = 12μ/(w bh³) 但文中实际 kv 由拟合直接给出（根据 Eq. 6，kv = μ/(A w bh?) 实际推导需对照原文，但可从拟合结果提取 kv 和 ki）[Sun 2025, pp. 2-4, 5-6]。
- 方向性几何参数：
  - 使用 X 方向和 Y 方向的 Z₂（剖面一阶导数均方根）表征正交方向的粗糙度差异[Sun 2025, pp. 8-10]。
  - 提出孔径方向性参数 bε：将裂隙上下壁面相减得到三维孔径表面，三角剖分后统计沿流动方向孔径扩张倾角大于临界值的面积，通过 Γ 函数拟合得到综合参数 bε，反映各方向回流区形成概率[Sun 2025, pp. 10-11]。
- 表征模型构建：
  - kv 模型采用基于 Z₂ 和平均孔径 bm 的指数形式：kv = l₁ bm exp(l₂ Z₂^{l₃} bm^{l₄})，用 J1、J3、J4 数据拟合[Sun 2025, pp. 11-12]。
  - ki 模型采用幂律关系：ki = h₁ kv^{h₂} bε^{h₃}，同样用 72 组方向数据拟合[Sun 2025, pp. 11-12]。
  - 用 J2 组数据独立验证[Sun 2025, pp. 11-12]。
- 临界雷诺数计算：结合 Forchheimer 方程与非线性压降占 10% 的条件，推导 Rec = (12^{1/2} √(ki) )/(9 √(kv))，用于确定相反方向出现渗透率差异的临界条件[Sun 2025, pp. 12-13]。

## Key Findings
1. **黏性渗透率各向异性**：kv 仅在正交方向（X 与 Y）存在显著差异，相反方向（X⁺与 X⁻，Y⁺与 Y⁻）基本一致。随剪切循环增加，正交方向差异增大，Y 向 kv 下降幅度大于 X 向，kv 各向异性系数 ε 逐渐增大，并在约 4 次循环后趋于稳定[Sun 2025, pp. 5-6]。
2. **惯性渗透率各向异性**：ki 在四个方向均有明显差异。随循环次数增加，正交方向差异（εXY）逐渐增大，而相反方向差异（εX、εY）逐渐减小并趋向 1[Sun 2025, pp. 6-8]。
3. **孔径方向性参数**：提出的 bε 能够区分四个方向的几何差异，该参数随循环次数增加而减小，首次剪切后下降最显著[Sun 2025, pp. 10-11]。
4. **表征模型性能**：基于 Z₂ 的 kv 模型对 36 组正交方向数据 R² = 0.960，基于 kv 和 bε 的 ki 模型对 72 组四方向数据 R² = 0.899；J2 独立验证 kv 模型 R² = 0.972，ki 模型 R² = 0.856[Sun 2025, pp. 11-12]。
5. **临界条件**：相反方向出现渗透率差异的临界雷诺数 Rec 随剪切循环增加而减小，说明经剪切后岩石裂隙更易表现出方向性流态差异，但差异幅度本身逐渐降低[Sun 2025, pp. 12-13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 四个方向的 kv 形成“菱形”形状，相反方向 kv 大致相等，正交方向差异随循环增大 | Sun 2025, pp. 5-6, Fig. 5 | CNL 0.8 MPa, 剪切振幅 8 mm, red sandstone non-mated fractures | kv 各向异性系数 ε 定义为 X 向与 Y 向渗透率之比 |
| ki 在四个方向呈不规则形状，正交和相反方向均存在差异；εXY 随循环增大，εX、εY 趋近 1 | Sun 2025, pp. 6-8, Figs. 7 & 8 | 同上 | 回流区分布不对称是主因 |
| bε 在四方向存在显著差异，随循环次数增加而下降 | Sun 2025, pp. 10-11, Fig. 10 | 裂隙数字模型基于剪切后点云重建 | bε 根据 Grasselli 概念从孔径表面计算 |
| kv 模型 R² = 0.960, ki 模型 R² = 0.899; 独立验证 J2 组 kv R² = 0.972, ki R² = 0.856 | Sun 2025, pp. 11-12, Fig. 13 | 建模未使用 J2 | ki 模型精度受裂隙形貌敏感性和强各向异性影响 |
| 相反方向 Rec 最小值随循环次数增加而降低 | Sun 2025, pp. 12-13, Fig. 14 | 临界条件基于非线性压降 10% 准则 | 孔径减小与粗糙退化共同作用 |

## Limitations
1. 非达西流实验在剪切完成后进行，未实现实时耦合，虽剪切速率较低（2 mm/min）可视为准静态，但无法捕捉动态剪切–流动耦合过程中的瞬态行为[Sun 2025, pp. 12-13]。
2. 实验中清除了磨损碎屑（gouge materials），未考虑碎屑产生与运移对渗透率的降低效应，可能导致高估[Sun 2025, pp. 13-14]。
3. 样本尺寸固定为 150 mm × 150 mm，存在尺寸效应，结论对更大尺度裂隙的适用性需验证[Sun 2025, pp. 13-14]。
4. 法向应力仅采用 0.8 MPa 一档，未研究不同法向应力下各向异性演化规律[Sun 2025, pp. 13-14]。

## Assumptions / Conditions
- 流体为不可压缩地下水，流动满足恒温、稳态纳维-斯托克斯方程[Sun 2025, pp. 2-2]。
- 基质渗透率极低，可忽略[Sun 2025, pp. 2-4]。
- 法向荷载恒定（CNL）、剪切过程准静态，忽略动力效应[Sun 2025, pp. 4-5]。
- 非达西流可用 Forchheimer 方程描述[Sun 2025, pp. 2-4]。
- 黏性渗透率仅与裂隙几何相关，可用立方律衍生关系表征[Sun 2025, pp. 2-4]。
- 惯性渗透率的各向异性主要源于孔径沿流向的非均匀扩张，形成回流区；仅当孔径扩张角超过临界值 θcr 时才形成回流区，且可用 Grasselli 的统计模型描述[Sun 2025, pp. 10-11]。

## Key Variables / Parameters
- **黏性渗透率 kv**：衡量裂隙线性的导水能力，由 Forchheimer 方程拟合得到[Sun 2025, pp. 2-4]。
- **惯性渗透率 ki**：衡量非线性惯性效应强度[Sun 2025, pp. 2-4]。
- **各向异性系数 ε**：kv 在 X 向与 Y 向比值[Sun 2025, pp. 5-6]。
- **各向异性系数 εXY, εX, εY**：分别表示 ki 在正交和相反方向比值的因子[Sun 2025, pp. 6-8]。
- **粗糙度参数 Z₂**：剖面一阶导数均方根，可区分正交方向[Sun 2025, pp. 8-10]。
- **孔径方向性参数 bε**：基于孔径表面倾角统计的积分值，区分四个方向[Sun 2025, pp. 10-11]。
- **临界雷诺数 Rec**：非达西效应占 10% 对应的雷诺数，用于判定相反方向出现差异的临界条件[Sun 2025, pp. 12-13]。

## Reusable Claims
1. 非达西流岩石裂隙的黏性渗透率仅在垂直于剪切方向与平行于剪切方向之间存在显著差异，随循环剪切次数增加，该正交差异逐渐增大（条件：红砂岩、非吻合裂隙、CNL 0.8 MPa、剪切振幅 8 mm）[Sun 2025, pp. 5-6]。
2. 惯性渗透率在平行与垂直剪切方向、以及正反向均呈现各向异性，且随剪切循环正交差异增大、反向差异减小（条件同上）[Sun 2025, pp. 6-8]。
3. 基于 Grasselli 思想的孔径方向性参数 bε 能够有效捕捉四个流动方向的几何差异，可用于惯性渗透率方向性建模（条件：需获取裂隙三维孔径表面）[Sun 2025, pp. 10-11]。
4. 幂律形式 ki = h₁ kv^{h₂} bε^{h₃} 可较好预测多方向惯性渗透率，独立验证 R² 约 0.86（条件：红砂岩裂隙、CNL 0.8 MPa）[Sun 2025, pp. 11-12]。
5. 循环剪切后相反方向出现渗透率差异的临界雷诺数降低，表明工程中即使较低 Re 下也可能出现明显方向性流量偏差（条件：裂隙经剪切磨损）[Sun 2025, pp. 12-13]。

## Candidate Concepts
- [[rock fractures]]
- [[non-Darcian flow]]
- [[viscous permeability]]
- [[inertial permeability]]
- [[flow anisotropy]]
- [[cyclic shearing]]
- [[constant normal load (CNL)]]
- [[Forchheimer equation]]
- [[recirculation zones]]
- [[directional aperture parameter]]
- [[critical Reynolds number]]
- [[fracture roughness]]
- [[aperture spatial distribution]]
- [[anisotropy factor ε]]

## Candidate Methods
- [[cyclic shear test under CNL]]
- [[3D laser scanning of fracture surfaces]]
- [[CNC carving for fracture replication]]
- [[non-Darcian flow experiment with constant flow rate]]
- [[Forchheimer fitting for kv and ki]]
- [[Grasselli’s roughness parameterization]]
- [[ICP algorithm for post-shear geometry alignment]]
- [[critical Reynolds number criterion (10% nonlinear pressure drop)]]
- [[nonlinear least squares regression]]

## Connections To Other Work
- Zhu et al. (2019) 发现粗糙裂隙正交方向压力梯度显著各向异性；本文进一步将其推广到 kv、ki 的四方向分析[Sun 2025, pp. 1-2]。
- Egert et al. (2021) 认为小孔径下非达西流各向异性更强，与本文剪切后孔径减小、各向异性增大的趋势相符[Sun 2025, pp. 1-2]。
- Zhao & Zhou (2020)、Marchand et al. (2020) 等主要研究正交方向 Darcian 各向异性；本文扩展至非达西和相反方向[Sun 2025, pp. 1-2, 12-13]。
- Zhou et al. (2019) 提出多孔介质中 ki = ω kv^α 的普适关系；本文引入 bε 考虑了方向性，超越了单方向的通用关系[Sun 2025, pp. 11-12]。
- Grasselli et al. (2002, 2003) 的各向异性粗糙度描述被用于构建孔径方向性参数[Sun 2025, pp. 10-11]。
- 循环剪切下裂隙表面磨损效应对渗透率的影响与 Hou et al. (2016)、Hu et al. (2022) 等的研究相关联[Sun 2025, pp. 2-2, 14-14]。

## Open Questions
1. 在多循环、高法向应力和含碎屑充填条件下，非达西各向异性如何演变？现有模型是否仍然有效？
2. 尺寸效应如何影响四方向渗透率各向异性以及临界雷诺数？能否建立尺度放大的方向性模型？
3. 考虑剪切/流动完全耦合的实时动态渗透率各向异性需要何种实验或数值手段支持？
4. bε 参数中临界倾角 θcr 的选取目前依赖全局拟合，是否存在不依赖拟合的理论确定方法？

## Source Coverage
所有非空索引片段均已处理，共 15 个索引块，覆盖 72,207 字符，编译后总字符 72,512。资料来源覆盖率：按块计 1.0，按字符计 1.004。参考文献片段中的冗余页面头尾导致字符轻微超出，未多出实质内容。
