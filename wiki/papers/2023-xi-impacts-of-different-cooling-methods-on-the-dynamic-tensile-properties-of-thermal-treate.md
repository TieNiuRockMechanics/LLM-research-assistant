---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-xi-impacts-of-different-cooling-methods-on-the-dynamic-tensile-properties-of-thermal-treate"
title: "Impacts of Different Cooling Methods on the Dynamic Tensile Properties of Thermal-Treated Granite."
status: "draft"
source_pdf: "data/papers/2023 - Impacts of different cooling methods on the dynamic tensile properties of thermal-treated granite.pdf"
collections:
  - "part2"
  - "zotero new"
  - "论文"
citation: "Xi, Yan, et al. \"Impacts of Different Cooling Methods on the Dynamic Tensile Properties of Thermal-Treated Granite.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 169, 2023, 105438. doi:10.1016/j.ijrmms.2023.105438. Accessed 2026."
indexed_texts: "16"
indexed_chars: "78369"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "73067"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.932346"
coverage_status: "full-index"
source_signature: "6cf7b5b112ab49277efd8a65d4043fadc5db18c0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:44:29"
---

# Impacts of Different Cooling Methods on the Dynamic Tensile Properties of Thermal-Treated Granite.

## One-line Summary
高温花岗岩经三种冷却（自然冷却、水冷、液氮冷却）后，其动态拉伸强度、P波波速及能量吸收均随温度升高非线性下降，液氮冷却的劣化效应最显著，为干热岩钻井破岩效率优化提供依据。

## Research Question
- 不同冷却方式（自然冷却、水冷、液氮冷却）如何影响热致花岗岩的动态拉伸力学性质、热冲击损伤及能量演化过程？
- 不同高温与冷却条件下花岗岩的动态拉伸破坏模式与破坏机制如何变化？

## Study Area / Data
- **研究区**：湖南省岳阳市细粒花岗岩。
- **样品**：取自同一岩块的直径50 mm、高25 mm的巴西圆盘试样，端面平整度控制在0.05 mm内。
- **矿物组成（XRD）**：石英28.2%，钾长石27.4%，云母22.2%，斜长石17.3%。
- **试验变量**：
    - 温度水平：25°C（对照）、200°C、400°C、500°C、600°C、800°C。
    - 冷却方式：自然冷却（空冷）、水冷却、液氮（LN₂）冷却。
    - 每种条件3个试样。
- **加热与冷却**：箱式炉以2.5°C/min升温至目标温度后恒温3 h，出炉后立即冷却，冷却持续4 h，所有冷却后试样在50°C烘干3 h。
- **测试方法**：超声波波速检测（透射法），直径50 mm的SHPB动态拉伸（巴西劈裂）试验，气压统一0.20 MPa，冲头速度约6.3 m/s，高速摄像（52,000 fps）与DIC应变分析。

## Methods
- **物理性质测试**：HS-YS2A型岩石声波仪测量P波波速（加热前后），计算相对波速与热损伤值。
- **动态拉伸试验**：SHPB装置（冲头、入射杆、透射杆均为50 mm合金钢，弹性模量210 GPa），动态力平衡检验。动态拉伸强度由式σ(t)=2P(t)/(πDB)计算，其中P(t)由三波应变求得。
- **破坏过程分析**：高速摄像记录冲击破坏全过程，DIC技术获取表面应变场演化。
- **能量计算**：基于一维应力波理论计算入射能W_I、反射能W_R、透射能W_T，耗散能W_D=W_I−W_R−W_T，并近似视为吸收能。
- **热损伤定义**：利用加热前后波速与密度计算热损伤因子D_V(T)=1−(ρ₁c₁²)/(ρ₀c₀²)。
- **统计分析**：波速、强度、能量及损伤因子与温度关系采用指数函数或Logistic模型拟合。

## Key Findings
1. **P波波速与热损伤**：随着热处理温度升高，三种冷却方式下P波波速均非线性降低；同一温度下，液氮冷却造成的波速降幅最大，水冷次之，自然冷却最小。热损伤因子随之增大，在500°C时三种冷却间差异最显著，800°C时差异几乎消失。
2. **动态拉伸强度**：随温度升高强度非线性下降；500°C后强度急剧降低（与573°C左右石英α-β相变有关）。同一温度下，液氮冷却的强度最低，水冷中等，自然冷却最高。
3. **破坏模式与机制**：所有试样均呈巴西劈裂破坏，产生中心拉伸裂纹与端部楔形剪切区。温度升高，中心裂纹出现时间延迟（室温约76.9 μs，800°C达307.5 μs），楔形区面积增大；同一温度下液氮冷却破坏区域最大。破坏顺序：先拉伸裂纹从中心向两端扩展，后出现次生剪切裂纹，形成X型破坏区或三角形剪切带。
4. **能量演化**：能量-时间曲线分四个阶段：弹性变形、裂纹生成、裂纹扩展、能量平台。温度升高，反射能增大，透射能和吸收能减小；最终吸收能随热损伤值增加而降低（初始损伤值>0.6后陡降）。吸收能与动态拉伸强度呈线性正相关（R²=0.98）。三种冷却中，液氮冷却对能量变化的影响最显著。
5. **冷却方式效应量化**：液氮冷却造成的热损伤最大，例如500°C时自然冷却、水冷、液氮冷却热损伤值分别为0.57、0.60、0.64；800°C时分别达0.95、0.96、0.97。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|-------------|-------|
| P-wave velocity decreases nonlinearly with temperature; LN₂ cooling causes the greatest reduction at each temperature (e.g., at 600°C: natural cooling 1420 m/s, water 1319 m/s, LN₂ 1204 m/s). | [Xi 2023, pp. 5-7] | Granite heated 25–800°C, three cooling methods, prior to dynamic testing. | Relative Vp fitted by exponential function (R²=0.97). |
| Dynamic tensile strength under LN₂ cooling is always the lowest; at 800°C, values are 7.22, 4.94, 3.64 MPa for natural, water, LN₂ cooling respectively. | [Xi 2023, pp. 7-8, Table 2] | SHPB Brazilian tests, impact velocity ~6.3 m/s. | Strength decrease accelerated above 500°C. |
| Thermal damage factor increases with temperature; LN₂ cooling yields the highest damage (0.636 at 500°C, 0.967 at 800°C) versus water (0.595, 0.959) and natural (0.572, 0.954). | [Xi 2023, pp. 10-12, Table 3] | Damage defined via P-wave velocity and density. | Logistic model fit well (R²≈0.98). |
| Time to central crack increases from 76.9 μs (25°C) to 307.5 μs (800°C) under natural cooling. | [Xi 2023, pp. 8-10] | High-speed camera observation. | Failure mode still similar; no distinct X-shaped damage at 800°C due to pre-existing cracks. |
| Final absorbed energy decreases with increasing thermal damage; LN₂ cooling leads to the fastest decrease. At initial damage >0.6, absorbed energy drops sharply. | [Xi 2023, pp. 15-16] | Energy calculated from SHPB waves. | Linear relation between absorbed energy and dynamic tensile strength. |
| Specimen failure process: tensile crack initiates in center, then secondary shear cracks develop, forming triangular crushed zones. Shear and tensile failure zones increase with temperature and are largest under LN₂ cooling. | [Xi 2023, pp. 8-10, Figs. 12-15] | DIC and high-speed imaging. | Failure mechanism consistent across cooling methods but extent differs. |

## Limitations
- 试样为单一细粒花岗岩，结论推广至其他岩性需谨慎。
- SHPB试验采用统一冲击气压（0.20 m/s），未考虑不同加载速率的影响；但文中指出加载率影响已被前人广泛研究，本次主要关注温度与冷却方法。
- 能量分析中忽略了摩擦耗散，但认为涂抹凡士林后摩擦能可忽略；吸收能近似取耗散能，可能有系统偏差。
- 冷却过程为持续4小时，实际钻井中冷却时间可能不同；此外，水温和液氮温度在冷却过程中假定保持恒定。
- 烘干处理可能未完全排除含水率影响，尽管在50°C下进行了3小时烘干。
- 热损伤定义仅基于P波波速和密度，未直接表征微裂隙数量或尺寸。

## Assumptions / Conditions
- 试样符合应力均匀性假设，适用于巴西圆盘动态劈裂试验。
- SHPB试验中试样达到动态应力平衡（入射波+反射波≈透射波）。
- 岩石为均质各向同性（矿物成分已知，但岩石内部天然非均质可能影响结果）。
- 加热速率2.5°C/min足够慢以避免热冲击，恒温3h保证内部温度均匀。
- 冷却4小时后试样温度恢复至室温，后续烘干去除表面水分。
- 能量计算中，破碎吸收能约占耗散能的95%，以耗散能近似代替吸收能。
- 热损伤分析中假定密度变化较小，损伤主要由波速平方项主导。

## Key Variables / Parameters
- **温度**：25, 200, 400, 500, 600, 800°C
- **冷却方式**：自然冷却、水冷、液氮冷却
- **P波波速** (m/s)
- **相对波速** (c₁/c₀)
- **热损伤因子** D_V
- **动态拉伸强度** σ (MPa)
- **能量**：入射能、反射能、透射能、吸收能 (J)
- **破坏过程参数**：中心裂纹出现时间 (μs)，剪切破坏区、拉伸破坏区面积（定性）

## Reusable Claims
- **Claim 1**：对于细粒花岗岩，在200–800°C区间内，P波波速随加热温度升高呈非线性下降，且冷却方式的影响显著，液氮冷却造成的波速衰减明显大于水冷和自然冷却。该结论可用于利用波速变化评估不同类型钻井液对热储层损伤的程度。
- **Claim 2**：花岗岩动态巴西抗拉强度随温度升高而降低，且在500°C后加速下降，主要归因于石英相变；液氮冷却进一步劣化强度，使其低于水冷和自然冷却。这提示在干热岩冲击钻井中采用低温液氮作为循环介质可降低岩石抗拉强度，有利于提高破岩效率。
- **Claim 3**：基于P波波速定义的热损伤因子可有效量化不同冷却方式造成的热冲击损伤，其随温度升高而增大，且液氮冷却在500°C时表现出最大差异，至800°C时差异缩减。该参数可用于评价不同冷却制度的损伤程度。
- **Claim 4**：花岗岩动态拉伸破坏过程：首先出现中心拉伸裂纹，然后端部形成剪切破坏区，最终形成X型或三角形失效区。温度升高使中心裂纹出现时间延迟，并使剪切和张拉破坏区面积增大。此规律可辅助解释热致损伤岩石的破坏时序。
- **Claim 5**：花岗岩冲击破坏过程中，吸收能与动态拉伸强度呈线性正相关（R²=0.98）；温度升高导致吸收能降低。液氮冷却下，试样达到相同拉伸强度所需吸收能更少，表明液氮作为钻井液可能降低破岩能耗。

## Candidate Concepts
- [[Hot dry rock (HDR)]]
- [[Dynamic tensile strength]]
- [[Split Hopkinson pressure bar (SHPB)]]
- [[Thermal shock damage]]
- [[P-wave velocity damage factor]]
- [[Brazilian disc test]]
- [[Digital image correlation (DIC)]]
- [[Liquid nitrogen cooling]]
- [[Energy evolution in rock fracture]]
- [[Quartz α-β phase transition]]
- [[Percussive drilling]]

## Candidate Methods
- [[P-wave velocity measurement (ultrasonic pulse transmission)]]
- [[SHPB dynamic Brazilian test]]
- [[High-speed photography for rock fracture]]
- [[DIC-based strain field analysis]]
- [[Thermal damage evolution modeling (logistic fit)]]
- [[Energy calculation from stress wave theory]]
- [[Dynamic force balance check in SHPB testing]]

## Connections To Other Work
- 前人研究（如Fan et al. 2017, Yin et al. 2015）主要关注热致花岗岩的动态压缩性能或自然冷却下的动态拉伸，本研究扩展至不同冷却方式的对比，特别是液氮冷却，与Fan et al. (2021) 热循环花岗岩冷却方式的研究呼应。
- 文中引用Chaki et al. (2008) 关于热损伤对波速影响的工作，显示冷却方式对波速的额外效应。
- 与Zhang et al. (2014) 的Brazilian测试建议一致，采用SHPB进行动态拉伸。
- 能量分析方法基于Zhang et al. (2000) 等前人工作，并补充了热损伤与吸收能的关联。

## Open Questions
- 不同加载速率下冷却方式的影响是否具有相同趋势（本研究固定冲击速度）？
- 微观裂纹的定量表征（如CT扫描或薄片分析）能否进一步解释冷却方式造成损伤差异的机制？
- 多次热循环或更复杂冷却路径（如交替冷却）对动态拉伸性能的影响如何？
- 实际钻井过程中，高温高压、钻井液循环与机械冲击的耦合作用尚未模拟。
- 液氮冷却引起的温度梯度与热应力分布定量分析缺乏。

## Source Coverage
All 16 non-empty indexed source blocks were processed (16/16, 100% coverage). Total indexed characters: 78369; compiled source characters: 73067 (coverage ratio ~93.2%). No content outside the supplied fragments is used.
