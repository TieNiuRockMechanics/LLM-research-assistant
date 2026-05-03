---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-huang-fluid-friction-and-heat-transfer-through-a-single-rough-fracture-in-granitic-rock-und"
title: "Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure."
status: "draft"
source_pdf: "data/papers/2016 - Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.pdf"
collections:
citation: "Huang, Xiaoxue, et al. \"Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.\" 11 Apr. 2016. Accessed 1 Jan. 2026."
indexed_texts: "7"
indexed_chars: "31551"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:53:40"
---

# Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.

## One-line Summary
实验研究了围压下花岗岩单裂隙中水的摩擦压降与强制对流换热，获得了基于雷诺数和相对粗糙度的Poiseuille数与Nusselt数经验关联式，并利用粗糙度‑粘度模型(RVM)成功复现了粗糙度导致的流动阻力增大和传热减弱现象。

## Research Question
现有对高温岩体地热系统中粗糙裂隙的流动摩擦与传热特性理解不足，特别是表面条件与传热系数之间的关系尚不明确。本文旨在通过花岗岩单裂隙对流实验，建立无量纲参数Po与Nu随Re和相对粗糙度变化的经验关系，并引入粗糙度‑粘度模型以从机理上解释和预测粗糙表面的影响。

## Study Area / Data
实验对象为圆柱形花岗岩岩样，利用巴西劈裂法制造一条单裂隙，并施加围压模拟地下应力状态 [Huang 2016, pp. 2-4]。所获经验公式基于90个实验数据点，覆盖三种围压水平 (Pc = 0, 3, 6 MPa) 及相应的相对粗糙度条件 [Huang 2016, pp. 4-5]。

## Methods
实验通过控制油温将岩石外表面加热至设定温度并保持恒定；去离子水以5–35 mL/min的流量通过裂隙，记录进出口水温、压降及外壁温度 [Huang 2016, pp. 2-4]。根据流量、压降和裂隙几何计算Poiseuille数Po、Reynolds数Re以及相对粗糙度Ra/2Rh。平均Nusselt数Nu通过推导的公式（式(6)）由测得的温度及岩石与流体物性计算 [Huang 2016, pp. 4-5]。为解析粗糙度效应，采用粗糙度‑粘度模型，将有效粘度μeff表示为流体粘度与粗糙度粘度之和，并通过求解动量方程获得速度分布，进而预测流动与换热 [Huang 2016, pp. 5-7]。

## Key Findings
- 粗糙裂隙内的Po和Nu显著偏离光滑矩形宏通道的层流理论值：流动摩擦增大，换热系数则比平行平板理论值低约两个数量级 [Huang 2016, pp. 1-1, 5-5]。
- Po随Re增加而下降，且下降斜率随Re增大逐渐减小；围压增大使裂隙开度减小，相对粗糙度增大，导致Po和Nu均升高 [Huang 2016, pp. 4-5]。
- 根据三种围压条件（Ra/2Rh = 0.148, 0.1526, 0.1539）得到了Po与Re的幂律经验关系式（7a）-（7c） [Huang 2016, pp. 4-5]。
- Nu随无量纲加热长度Lh⁺减小而迅速增大，在小Lh⁺阶段尤为明显 [Huang 2016, pp. 7-8]。
- 采用RVM的有效粘度替代流体粘度后，数值预测结果与实验流量数据吻合良好；粗糙度引起的边界层增厚一方面增加总剪切应力导致压降升高，另一方面降低近壁面速度梯度和温度梯度，从而削弱了换热 [Huang 2016, pp. 5-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Po = 96×2.3053 Re⁻⁰·²⁹⁰²  at Ra/2Rh = 0.148 (Pc = 0 MPa) | [Huang 2016, pp. 4-5] | 单相水层流，圆柱花岗岩裂隙 | 基于90个实验点，式(7a) |
| Po = 96×2.3728 Re⁻⁰·¹⁷²³ at Ra/2Rh = 0.1526 (Pc = 3 MPa) | [Huang 2016, pp. 4-5] | 同上 | 式(7b) |
| Po = 96×2.4268 Re⁻⁰·¹⁵⁷⁵ at Ra/2Rh = 0.1539 (Pc = 6 MPa) | [Huang 2016, pp. 4-5] | 同上 | 式(7c) |
| Nu比定壁温平板层流理论值7.54小约两个数量级 | [Huang 2016, pp. 5-5] | 层流，H/W→0 | 大相对粗糙度导致 |
| RVM的流量预测与实验数据吻合良好 | [Huang 2016, pp. 5-7] | 有效粘度修正，边界层效应 | 图6比较 |

## Limitations
- 实验仅在单一人造裂隙中进行，其粗糙度结构和分布可能不代表天然裂隙的全部特征。
- 流量上限受限于保证液压不超围压，限制了可达到的雷诺数范围。
- 实验工质为单相去离子水，未涵盖两相流或大幅变物性工况。
- RVM模型中的经验系数A依赖实验标定，其向其他裂隙类型的推广性尚未验证。
- 未从索引片段中确认实验的温度范围、岩石热导率的具体取值及其温度依赖性，以及Nusselt数关联式的完整表达式。

## Assumptions / Conditions
- 裂隙被视为高宽比H/W趋近于0的矩形截面，流动近似为两无限大平行板间的层流。
- 岩石外表面温度均匀且等于周围油温，并以此通过稳态导热推算裂隙表面温度。
- 流体（水）和岩石的热物理性质视为常数。
- 裂隙粗糙度的影响可通过空间分布的粗糙度粘度来等效模拟。
- 流动为充分发展的层流，忽略轴向速度变化。

## Key Variables / Parameters
Poiseuille数 (Po), Nusselt数 (Nu), Reynolds数 (Re), 相对粗糙度 (Ra/2Rh), 无量纲加热长度 (Lh⁺), 有效粘度 (μeff), 粗糙度粘度 (μr), 裂隙开度 (δ), 围压 (Pc), 岩石外表面温度 (To), 体积流量 (Q), 粗糙度Reynolds数 (Rek), Prandtl数 (Pr), 摩擦因子 (f), 水力直径 (Dh), 粗糙度 (Ra) [Huang 2016, pp. 2-4, 5-7].

## Reusable Claims
- 对于具有高相对粗糙度的花岗岩裂隙中单相水流层流，Po与Re的幂律关系受相对粗糙度控制：相对粗糙度越大，Po随Re下降的指数绝对值越小 [Huang 2016, pp. 4-5]。该结论基于式(7a)-(7c)的三组实验拟合，适用于类似粗糙度级别的人工张性裂隙。
- 在粗糙裂隙中，Nu可比经典光滑平板理论值降低两个数量级，且其值在较短的无量纲加热长度处急剧增大 [Huang 2016, pp. 5-5, 7-8]。使用此结论时应注意其基于恒定裂隙开度与层流假设。
- 粗糙度‑粘度模型通过引入与Rek相关的有效粘度可以解释和预测粗糙裂隙中的摩擦增大和传热抑制，其预测与实验数据吻合 [Huang 2016, pp. 5-7]。该方法需要根据具体裂隙标定经验系数A，可能适用于微裂隙或类微通道流动。

## Candidate Concepts
- [[enhanced geothermal system]]
- [[single fracture flow]]
- [[surface roughness]]
- [[roughness-viscosity model]]
- [[Poiseuille number]]
- [[Nusselt number]]
- [[forced convection in fractures]]
- [[confining pressure effect on fracture]]
- [[fracture aperture]]

## Candidate Methods
- [[experimental convective heat transfer in rock fractures]]
- [[dimensionless correlation]]
- [[Brazilian splitting method]]
- [[effective viscosity approach]]
- [[numerical simulation with roughness-viscosity model]]
- [[fracture flow pressure drop measurement]]

## Connections To Other Work
- 前人研究指出，岩石裂隙中的对流换热受表面粗糙度主导 [Zhao and Tso, refs.6,7]，本文在此基础上通过无量纲分析和RVM模型定量建立了粗糙度与Po、Nu的关系。
- 采用的粗糙度‑粘度模型借鉴自微管和微通道流动研究 [Mala and Li, ref.14] 并拓展至岩石裂隙 [Huang 2016, pp. 5-7]。
- 研究结果可为增强型地热系统(EGS)中裂隙流动与换热模拟提供更准确的基元关系，与EGS数值模拟模型 [e.g., refs.8,9] 在概念上互补。
- 未从索引片段中确认与其他具体岩石裂隙传热实验的直接对比数据。

## Open Questions
- 在更高温度、更宽相对粗糙度范围内，Po与Nu的关联式如何演变？是否能形成统一的基于相对粗糙度的普适公式？
- 当提高系统压力以避免相变时，是否可获得更广雷诺数范围的稳定数据，从而验证惯性效应或非达西效应的影响？
- RVM模型中的经验系数A能否通过裂隙表面几何形态的统计参数直接预估，从而避免对实验标定的依赖？
- 该单裂隙结果如何有效拓展到具有不同开度分布和裂隙网络的储层尺度建模？

## Source Coverage
本页面依据7个索引片段编写，覆盖了摘要、引言、实验方法、数据简化、部分结果与讨论、RVM模型原理及结论。片段提供了关键公式和结论性陈述，但缺少完整的实验参数范围（如温度、岩样尺寸）、Nu关联式的具体代数形式、详细的图形数据以及不确定性分析的完整表格。部分结果（如Lh⁺对Nu的影响规律）仅给出定性描述，定量关系未从片段中完全确认。
