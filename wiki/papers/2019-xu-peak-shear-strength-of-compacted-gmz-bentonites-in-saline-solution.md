---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-xu-peak-shear-strength-of-compacted-gmz-bentonites-in-saline-solution"
title: "Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution."
status: "draft"
source_pdf: "data/papers/2019 - Peak shear strength of compacted GMZ bentonites in saline solution.pdf"
collections:
  - "审稿人让引用"
citation: "Xu, Yongfu. \"Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution.\" *Engineering Geology*, 2019, doi:10.1016/j.enggeo.2019.02.009. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42393"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42545"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003585"
coverage_status: "full-index"
source_signature: "53b75bf82f437e52f2987fb9693824075e2b5bfb"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:21:11"
---

# Peak Shear Strength of Compacted GMZ Bentonites in Saline Solution.

## One-line Summary
基于膨润土表面分形模型，提出包含渗透吸力的修正有效应力 `p' = p + π(p/π)^{Ds-2}`，可将不同浓度 NaCl 溶液中 GMZ 膨润土及其砂混合物的峰值剪切强度统一到同一条 Mohr‑Coulomb 破坏线上，内摩擦角与粘聚力保持恒定，不随盐浓度变化。

## Research Question
如何利用修正有效应力概念，表达并解释压实 GMZ 膨润土在不同浓度盐水溶液中的峰值剪切强度，使得不同孔液化学条件下的剪切强度可用同一条 Mohr‑Coulomb 线描述？

## Study Area / Data
- 材料：GMZ07 膨润土（主要矿物蒙脱石，伴生石英、斜长石、长石，表 1），福建标准砂（颗粒级配见 Fig. 4）。
- 溶液：蒸馏水及 NaCl 溶液，浓度 0, 0.2, 0.5, 1.0, 2.0 mol/L。
- 试验：不排水直剪试验（试样直径 5 cm，厚 1.5 cm，干密度约 1.5 g/cm³ 及 1∶1 砂‑膨润土混合物约 1.45 g/cm³，剪切速率 0.01 mm/min）；膨胀变形试验（oedometer，内径 61.8 mm，高 20 mm，初始试样高 12 mm）；氮吸附等温线测试（77 K），用于测定表面分形维数。
- 数据：归一化水体积与竖直应力的关系（蒸馏水及盐水）、直剪峰值强度（τ‑p 及 τ‑p' 平面）。

## Methods
1. 通过氮吸附等温线（式 14）和膨胀变形试验（式 3）测定 GMZ 膨润土表面分形维数 Ds。
2. 基于膨润土表面分形模型，推导修正有效应力，将渗透吸力化为等效力学作用（式 11→式 12）：
   `p' = p + π(p/π)^{Ds-2}`
   其中 p 为法向应力，π 为由 van’t Hoff 方程（式 4）计算的渗透吸力。
3. 用膨胀变形试验验证修正有效应力：绘制归一化水体积 Vw/Vm 与 p' 的双对数关系，检验其是否落在同一直线上（式 3，Fig. 7）。
4. 将修正有效应力代入 Mohr‑Coulomb 准则 `τf = c' + p' tan φ'`，分析直剪峰值强度数据，考察不同溶液浓度下的 τf‑p' 关系。

## Key Findings
1. GMZ07 膨润土的表面分形维数 Ds = 2.78，由氮吸附试验和膨胀变形试验两种独立方法给出相同值（Figs. 5–6）。
2. 归一化水体积 Vw/Vm 与修正有效应力 p' 在双对数图中呈单一线性关系，斜率 Ds − 3，与 NaCl 浓度无关（Fig. 7），验证了修正有效应力式(12)的正确性。
3. 在 τf‑p' 平面上，GMZ07 膨润土及 1∶1 砂‑膨润土混合物在蒸馏水和所有浓度 NaCl 溶液中的直剪数据均落在同一条直线上（Figs. 9a–b）。
4. 由此确定的本征摩擦角 φ' 为：GMZ07 膨润土 4.8°，1∶1 混合物 9.4°，均处于蒙脱石典型范围（4°~20°），且不随盐浓度变化。
5. 当法向应力超过约 1600 kPa 时，1∶1 混合物数据偏离线性，归因于高应力下砂粒直接接触，使摩擦表现接近砂粒摩擦（Fig. 9b）。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Ds = 2.78 由氮吸附等温线（P/P₀ 0.01–0.99）获得；膨胀变形试验给出相同 Ds。 | Figs. 5–6 [Xu 2019, pp. 5-6] | 氮吸附在 77 K 下进行；膨胀试验使用蒸馏水。 | 两种独立方法一致，R² > 0.99。 |
| 归一化水体积 Vw/Vm 与修正有效应力 p' 的双对数关系为一条直线，斜率 ≈0.22（=Ds‑3）。 | Fig. 7 [Xu 2019, pp. 5-6] | NaCl 0–2.0 mol/L，GMZ07 膨润土。 | 验证了式(12)的有效性，不同浓度数据合为一线。 |
| 直剪峰值强度数据在 τf‑p' 平面内可用单一直线拟合，GMZ07 膨润土 φ'≈4.8°。 | Fig. 9a [Xu 2019, pp. 6-7] | 蒸馏水及 0–2.0 mol/L NaCl，干密度 1.5 g/cm³。 | 表观 φ 随浓度增大而增大，但经修正应力后 φ' 为常数。 |
| 1∶1 砂‑膨润土混合物在 p' 较低时 φ'≈9.4°，但 p'>1600 kPa 时偏离线性。 | Fig. 9b [Xu 2019, pp. 6-7] | 干密度 1.45 g/cm³，NaCl 0–2.0 mol/L。 | 偏离归因于砂粒直接接触，高应力下摩擦特性趋近砂。 |

## Limitations
- 仅针对 GMZ07 膨润土及特定砂混合物，其他类型膨润土或配比的适用性未验证。
- 修正有效应力模型基于表面分形假设，可能不适用于非分形表面或非蒙脱石为主的黏土。
- 试验为不排水直剪，未探讨排水条件、应变速率及长期蠕变效应。
- 剪切速率固定为 0.01 mm/min，未考察速率影响。
- NaCl 浓度范围限于 0–2.0 mol/L，更高浓度或其他盐类（如 CaCl₂）的效果未知。
- 仅分析了峰值强度，不涉及残余强度或应变软化行为。
- 高应力下砂‑膨润土混合物的偏离原因缺乏微观观测直接支持。

## Assumptions / Conditions
- 膨润土颗粒表面的分形特征在溶液侵入后保持不变。
- 孔液中的渗透吸力可由 van’t Hoff 方程计算，并视为理想稀溶液行为。
- 渗透吸力与法向应力在修正有效应力中视作等效力，两者在分形模型框架内具有统一的力学作用。
- Mohr‑Coulomb 准则适用于描述修正有效应力下的峰值强度。
- 试验维持恒温（T ≈ 293 K），化学环境稳定。
- 砂‑膨润土混合物在低应力下视为均质体，砂粒不构成连续骨架。

## Key Variables / Parameters
- `p`：法向应力
- `π`：渗透吸力，由 `π = ν R T m φ` 确定（ν=1，T=293 K，m 为摩尔浓度，φ 为渗透系数）
- `Ds`：表面分形维数（GMZ07 为 2.78）
- `p' = p + π(p/π)^{Ds‑2}`：修正有效应力
- `Vw/Vm`：归一化水体积
- `φ'`：修正有效应力下的峰值摩擦角（GMZ07：4.8°；1∶1 混合物：9.4°）
- `c'`：对应的峰值粘聚力（为常数，具体值可从 τf‑p' 线截距获得，文中未单独列出数值）

## Reusable Claims
1. **Claim:** 对于 GMZ07 膨润土，修正有效应力 `p' = p + π(p/π)^{Ds-2}` 可将蒸馏水及 0–2.0 mol/L NaCl 溶液饱和条件下的峰值剪切强度统一为同一条 τf‑p' 线，摩擦角 φ' ≈ 4.8°，粘聚力 c' 恒定，不受盐浓度影响。  
**Conditions:** 干密度 ~1.5 g/cm³，不排水直剪，剪切速率 0.01 mm/min，Ds=2.78，T=293 K。  
**Source:** [Xu 2019, pp. 6-7] Figs. 8‑9.

2. **Claim:** 膨润土的表面分形维数可通过氮吸附等温线或膨胀变形试验测定；对于 GMZ07，Ds=2.78。该参数是构建修正有效应力的关键输入，可用于统一不同化学条件下的体变与强度行为。  
**Conditions:** 以蒙脱石为主的膨润土，表面具有分形特征，测试前需适当脱气处理。  
**Source:** [Xu 2019, pp. 5-6] Figs. 5‑6.

3. **Claim:** 归一化水体积与修正有效应力在双对数坐标中呈线性关系 `Vw/Vm = K (p')^{Ds-3}`，该关系与孔液盐浓度无关，可用于预测膨润土在不同化学条件下的持水状态。  
**Conditions:** 饱和状态，法向应力范围与试验一致，膨润土表面分形维数已知。  
**Source:** [Xu 2019, pp. 5-6] Eq. (3) 及 Fig. 7.

4. **Claim:** 当砂以 1∶1 质量比与 GMZ07 膨润土混合时，若修正有效应力不超过约 1600 kPa，峰值摩擦角 φ' 约为 9.4° 且恒定；超过该应力后，直剪数据偏离线性，宜考虑砂粒接触导致的额外摩擦贡献。  
**Conditions:** 干密度 1.45 g/cm³，福建标准砂，其余条件同膨润土试验。  
**Source:** [Xu 2019, pp. 6-7] Fig. 9b.

## Candidate Concepts
- [[修正有效应力]] incorporating osmotic suction via fractal model
- [[表面分形维数]] of bentonite (Ds)
- [[渗透吸力]] calculated by van't Hoff equation
- [[膨润土表面分形模型]] for water volume and stress
- [[Mohr‑Coulomb准则]] in modified effective stress space
- [[归一化水体积]] as a state variable
- [[砂‑膨润土混合物高应力偏离]]
- [[孔液化学对膨润土强度的统一描述]]

## Candidate Methods
- [[氮吸附等温线测定表面分形维数]]
- [[膨胀变形试验验证修正有效应力]]
- [[不排水直剪试验在不同盐浓度下]]
- [[基于分形模型的修正有效应力推导]]
- [[van’t Hoff渗透吸力计算]]
- [[双对数归一化水体积‑应力关系检验]]

## Connections To Other Work
- 本文修正有效应力式(12)与 Sridharan and Rao (1979) 的式(1)及 Rao and Thyagaraj (2007) 的式(2)同属修正有效应力范畴，但本文所有参数具有明确物理意义且可直接测定 [Xu 2019, pp. 1-2]。
- 针对 GMZ07 膨润土的直剪数据，Zhang et al. (2016b) 指出峰值摩擦角随盐浓度增大，而本文通过修正有效应力将其统一为常数 [Xu 2019, pp. 6-7]。
- 膨润土表面分形模型源自 Xu et al. (2003)，本文将其扩展至含盐条件下的剪切强度描述。
- Mesri and Olson (1970) 发现自由孔液电解质浓度对修正有效应力破坏包络线影响甚微，本文结果与此定性一致，并给出了定量的修正应力表达式。

## Open Questions
- 修正有效应力公式是否适用于其他盐溶液（如 CaCl₂、NaNO₃）或其他膨胀黏土（如高岭石‑蒙脱石混合层）？
- 在更宽的法向应力或更高浓度条件下，修正有效应力的线性关系是否需要进一步修正？
- 能否将同一框架推广至排水强度及残余强度分析？
- 高应力下砂‑膨润土混合物中砂粒接触的微观机理及其定量判据是什么？
- 温度变化对渗透吸力及表面分形参数的影响是否可忽略？
- 修正有效应力中的分形参数是否受干湿循环或化学循环的长期影响？

## Source Coverage
本页面基于全部 9 个非空索引片段编译而成。片段覆盖论文的所有主要部分（摘要、引言、理论、材料与方法、结果与讨论、结论）。索引文本总字符数 42,393，已处理字符数 42,545，按块覆盖比为 1.0，按字符覆盖比约为 1.0036，实现全文索引覆盖。所有证据均来自提供的源块，未加入外部知识。
