---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s"
title: "Multiscale Damage and Thermal-Stress Evolution Characteristics of Rocks with Thermal Storage Potential under Thermal Shocks."
status: "draft"
source_pdf: "data/papers/2024 - Multiscale damage and thermal-stress evolution characteristics of rocks with thermal storage potential under thermal shocks.pdf"
collections:
  - "zotero new"
citation: "Yang, Zheng, et al. \"Multiscale Damage and Thermal-Stress Evolution Characteristics of Rocks with Thermal Storage Potential under Thermal Shocks.\" *Journal of Energy Storage*, vol. 83, 2024, 110631. Accessed 2026."
indexed_texts: "16"
indexed_chars: "78941"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:14:21"
---

# Multiscale Damage and Thermal-Stress Evolution Characteristics of Rocks with Thermal Storage Potential under Thermal Shocks.

## One-line Summary
该研究通过实验和新型热‑力学颗粒基模型（TM‑GBM），首次揭示了热冲击下含热储能潜力花岗岩在加热、冷却及单轴加载过程中的多尺度损伤与热应力演化特征 [Yang 2024, pp. 1-2]。

## Research Question
热冲击引起的不可逆损伤如何影响高温岩石的物理力学性质？加热与冷却过程中花岗岩内部的多尺度裂纹萌生、热应力分布及力学响应有何差异？如何用数值方法实时追踪实验室难以监测的热损伤演化？ [Yang 2024, pp. 1-2]

## Study Area / Data
- **岩石类型**：粗粒花岗岩，取自中国长沙，认为具有良好导热和热容，适合岩石基热储能系统 [Yang 2024, pp. 2-4]。
- **试样规格**：圆柱体，直径50 mm，高100 mm；矿物晶粒尺寸小于试样直径的1/20，以保证均匀性 [Yang 2024, pp. 2-4]。
- **矿物组成（XRD）**：石英38.4%，长石39.1%，黑云母20.7% [Yang 2024, pp. 2-4]。
- **实验分组**：1组对照（无热处理） + 4组热冲击处理，目标温度分别为100、200、300和400 °C，每组3个试样 [Yang 2024, pp. 2-4]。

## Methods
1. **热冲击实验**：将试样直接放入已预热至目标温度的炉中，实现快速热传导和热冲击，而非传统缓慢升温 [Yang 2024, pp. 2-4]。处理后进行单轴压缩试验，获取应力‑应变曲线及力学参数。
2. **数值模拟**：开发了一种热‑力学颗粒基模型（TM‑GBM）。
   - 利用数字图像处理（DIP）对真实花岗岩表面图像进行矿物颗粒提取（灰度阈值分割：黑云母<135，石英136‑171，长石>172），并经矢量化后在PFC2D中生成初始颗粒模型 [Yang 2024, pp. 5-6]。
   - 通过Voronoi镶嵌实现更精细的矿物填充，最小颗粒半径0.18 mm，最大0.28 mm，能够区分沿晶和穿晶破坏 [Yang 2024, pp. 5-6]。
   - 热模型基于傅里叶热传导定律和牛顿第二定律，考虑颗粒热膨胀导致半径变化（ΔR = αRΔT），引起平行粘结间力的改变 [Yang 2024, pp. 6-7]。
   - 模型微观参数通过室内试验标定（例如UCS 124.0 MPa实验 vs 124.6 MPa模拟，弹性模量31.1 GPa vs 30.9 GPa，R²>0.999） [Yang 2024, pp. 7-9]。
3. **模拟流程**：先加热至目标温度（边界设置稳定热源），再冷却至25 °C（边界设定恒温），最后进行单轴压缩加载，对应实验全过程 [Yang 2024, pp. 9-11]。

## Key Findings
- **临界温度**：300 °C是花岗岩热冲击损伤的临界温度。低于该温度时，应力、应变和热裂纹演化不显著；超过后，热裂纹明显增多，应变显著增加 [Yang 2024, pp. 4-5]。
- **裂纹矿物相关性**：加热和冷却过程中，热诱导裂纹数量与温度正相关；石英中的穿晶裂纹数量显著多于长石和黑云母 [Yang 2024, pp. 1-2]。
- **加热与冷却差异**：在相同热冲击温度下，加热过程产生的热应力大小和热诱导裂纹数量均显著低于冷却过程 [Yang 2024, pp. 1-2]。
- **模型验证**：TM‑GBM能再现25 °C下花岗岩的宏观力学性质（UCS和弹性模量误差极小）和Y形剪切破坏模式，证实其可靠性 [Yang 2024, pp. 7-9]。
- **模拟优势**：TM‑GBM可区分沿晶张拉、沿晶剪切、穿晶张拉和穿晶剪切四种裂纹类型，克服了实验室在高温环境下无法实时监测内部热应力和裂纹演化的局限 [Yang 2024, pp. 2-2][Yang 2024, pp. 5-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 300 °C为花岗岩热冲击损伤阈值，超过后裂纹和应变显著增大 | [Yang 2024, pp. 4-5] | 直接放入100~400 °C炉中加热，SEM观察和应变数据 | 基于微观表面粗糙度、裂纹数量和应变变化综合判断 |
| 石英中热诱导穿晶裂纹数量远多于长石和黑云母，裂纹数量与温度正相关 | [Yang 2024, pp. 1-2] | 加热和冷却阶段，温度100~400 °C | 摘要结论，未提供具体统计数值 |
| 同一热冲击温度下，加热引起的热应力大小和裂纹数量显著低于冷却过程 | [Yang 2024, pp. 1-2] | TM‑GBM模拟，对比加热和冷却阶段 | 原文强调冷却过程的损伤更大 |
| TM‑GBM标定后UCS误差0.48%，弹性模量误差0.64% (实验124.0 MPa/31.1 GPa vs 模型124.6 MPa/30.9 GPa) | [Yang 2024, pp. 7-9] | 单轴压缩，25 °C，对照试样 | R²>0.999，模拟缺失压密阶段导致峰值应变略低 |
| 实验破坏模式为Y形剪切，TM‑GBM模拟的碎片形态和裂纹分布与之吻合 | [Yang 2024, pp. 7-9] | 单轴压缩加载，对照试样 | 验证模型在微观结构上的代表性 |

## Limitations
- 实验热冲击温度上限仅为400 °C，更高温度（如600 °C以上）下的损伤特性未从索引片段中确认。
- 数值模型为二维PFC2D，虽然前人认为二维可近似解决三维问题 [Yang 2024, pp. 5-6]，但可能低估三维颗粒互锁和裂纹的复杂路径，尤其对于非均质热传导。
- 冷却过程使用25 °C恒温边界，未考虑不同冷却速率（如水冷、风冷）的影响，片段未提及。
- 未从索引片段中确认模型是否考虑含水率、矿物相变（如α‑β石英转变）等高温特殊效应。
- 实验每组仅3个试样，统计代表性可能有限。

## Assumptions / Conditions
- **热传导**：假设颗粒间热流遵循傅里叶定律，热接触为热管网络，材料内部仅通过热传导传递热量 [Yang 2024, pp. 6-7]。
- **热膨胀**：颗粒半径线性膨胀，ΔR = αRΔT，且热膨胀系数恒定，未考虑温度依赖性 [Yang 2024, pp. 6-7]。
- **力学本构**：颗粒间采用线弹性平行粘结模型，强度参数已标定，但未从片段中明确是否考虑高温下参数的劣化规律 [Yang 2024, pp. 6-7]。
- **矿物识别**：基于灰度阈值（<135黑云母，136‑171石英，>172长石）分割，假设矿物边界仅由灰度决定 [Yang 2024, pp. 5-6]。
- **初始条件**：试样初始均为室温25 °C，无初始微裂纹 [Yang 2024, pp. 9-11]。
- **热冲击定义**：试样直接放入目标温度炉中，模拟工程急热工况，而非缓慢升温 [Yang 2024, pp. 2-4]。

## Key Variables / Parameters
- 热冲击温度：100、200、300、400 °C。
- 热膨胀系数（α）：未给出具体数值，但在公式 (1) 中使用 [Yang 2024, pp. 6-7]。
- 矿物微观力学参数：杨氏模量、粘结强度、摩擦系数等（见表2，部分数值为：石英颗粒E₍ball₎=40 GPa，穿晶粘结σ=180 MPa，沿晶粘结c=130 MPa等） [Yang 2024, pp. 6-7]。
- 力学宏观指标：单轴抗压强度（UCS=124.0 MPa）、弹性模量（31.1 GPa） [Yang 2024, pp. 7-9]。
- 模型尺寸：高100 mm，宽54 mm（二维截面） [Yang 2024, pp. 5-6]。
- 颗粒半径范围：0.18~0.28 mm [Yang 2024, pp. 5-6]。
- 模型评价指标：决定系数R²>0.999 [Yang 2024, pp. 7-9]。
- 热传导方程中的温度分布参数：Tₓ₀, T_y₀，见公式(7) [Yang 2024, pp. 9-11]。

## Reusable Claims
- **热冲击临界温度识别**：“对于该粗粒花岗岩，300 °C可视为热冲击损伤的临界温度，当温度超过该阈值后，热诱导裂纹显著发展且应变急剧增大。”[Yang 2024, pp. 4-5] 适用条件：直接加热冲击方式，花岗岩试样直径50 mm，加热至上限400 °C。限制：仅适用于本批矿物组成和粒径分布的岩石，推广至其他岩类需验证。
- **矿物选择性开裂**：“在加热和冷却热冲击下，石英内部产生的穿晶裂纹数量远多于长石和黑云母，且裂纹总量与温度呈正相关。”[Yang 2024, pp. 1-2] 适用条件：花岗岩含约38%石英，热冲击温度100~400 °C。证据来自SEM和TM‑GBM模拟定性比较，未给出精确定量比例。
- **冷却损伤大于加热**：“在同一热冲击温度水平下，冷却过程诱发的热应力大小和裂纹数量均显著高于加热过程。”[Yang 2024, pp. 1-2] 适用条件：先加热至均温再冷却，冷却介质为25 °C恒温壁面。限制：仅基于数值模拟，未从片段中确认是否有实验验证。
- **TM‑GBM模型精度**：“经矿物分布和微观参数标定后，TM‑GBM可准确复现室温下单轴压缩强度和弹性模量（误差<1%），并能再现Y形宏观剪切破坏模式。”[Yang 2024, pp. 7-9] 适用条件：二维模型，使用DIP提取真实矿物图案，标定基于实测UCS和弹性模量。限制：模型缺失压密阶段，可能导致峰值应变略低。

## Candidate Concepts
[[thermal shock]], [[granite]], [[thermal energy storage]], [[multi-scale damage]], [[thermally induced crack]], [[intergranular crack]], [[intragranular crack]], [[uniaxial compressive strength]], [[grain-based model]], [[heat conduction]], [[Fourier’s law]], [[mineral heterogeneity]], [[thermal expansion mismatch]], [[digital image processing]], [[Voronoi tessellation]]

## Candidate Methods
[[discrete element method]], [[thermo-mechanical coupling]], [[PFC2D]], [[scanning electron microscopy (SEM)]], [[X-ray diffraction (XRD)]], [[grain-based model (GBM)]], [[parallel bond model]], [[thermal pipe model]], [[computational tomography scanning (CT)]], [[digital image processing (DIP)]]

## Connections To Other Work
- 本文在引言中明确提及Cundall [19] 奠基的离散元方法 [Yang 2024, pp. 2-2]；并引用了Tian et al. [24] 的cluster模型、Guo et al. [25] 基于CT扫描的GBM、Li et al. [26] 结合DIP的GBM等，表明TM‑GBM是在这些方法基础上的延伸，克服了传统DEM不能区分沿晶和穿晶裂纹、不能真实反映矿物分布的局限 [Yang 2024, pp. 2-2]。
- 本文强调冷却损伤常被忽略，而该方法首次同时模拟加热‑冷却‑加载全过程，与已有仅研究加热或高温后力学特性的工作形成互补 [Yang 2024, pp. 1-2][Yang 2024, pp. 9-11]。

## Open Questions
- 加热与冷却两阶段裂纹数量和热应力差异的具体机制（如矿物各向异性热膨胀、冷却收缩速率不均匀的贡献）未从索引片段中深入阐明。
- 更高温度（>400 °C）或多次热循环下的累积损伤、疲劳效应未涉及。
- TM‑GBM中冷却过程的热应力分布和裂纹扩展是否受边界冷却速率影响，片段未提供敏感性分析。
- 从实验室热冲击到实际热储能储层尺度的相似性转换未讨论。
- 未从索引片段中确认是否将热物性参数（热导率、热容）的温度相关性纳入模型。

## Source Coverage
本页基于论文的10个索引片段（共16个片段，其余6个片段未提供），覆盖摘要、引言（部分）、实验方法、建模流程、模型验证和部分模拟流程说明。能够提取出研究动机、关键方法和主要结论。但缺少专门的讨论章节、完整的温度‑裂纹定量统计结果、冷却阶段的热应力分布云图以及结论部分等细节，因此一些数值证据和机理解释可能存在缺失。若需补充详细的热损伤机制和参数敏感性分析，应获取全文索引片段。
