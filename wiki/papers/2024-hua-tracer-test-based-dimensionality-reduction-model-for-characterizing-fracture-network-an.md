---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-hua-tracer-test-based-dimensionality-reduction-model-for-characterizing-fracture-network-an"
title: "Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer."
status: "draft"
source_pdf: "data/papers/2024 - Tracer-test-based dimensionality reduction model for characterizing fracture network and predicting flow and transport in fracture aquifer.pdf"
collections:
citation: "Hua, Cong, et al. \"Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer.\" *Journal of Hydrology*, vol. 630, 2024, 130773. Accessed 2026."
indexed_texts: "15"
indexed_chars: "73524"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "69978"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.951771"
coverage_status: "full-index"
source_signature: "72c0d06b9bca1549770f3a83570f048af2dde0b1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:50:56"
---

# Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer.

## One-line Summary
本研究基于跨孔示踪试验测得的示踪剂突破曲线（TBC）的拐点数目，构建了一种降维模型（DRM）来表征裂隙网络的优势流动路径，并在实验室3D打印物理模型和场地尺度合成裂隙网络中验证了该模型在不同抽水速率下预测流出浓度和温度的精度（相对误差低于10%）。[Hua 2024, pp. 1-1, 1-2, 5-6, 11-12]

## Research Question
如何在缺乏预设裂隙属性信息的情况下，利用实际可观测的示踪突破曲线（TBC）建立针对裂隙网络的降维模型（DRM），以解决裂隙介质高异质性反演的不适定性问题，并实现不同抽注速率下渗流与溶质/热量运移的准确预测。[Hua 2024, pp. 1-2, 2-3]

## Study Area / Data
- **实验室物理模型**：一个包含7条随机交切裂隙的透明3D‑打印裂隙网络模型（尺寸355 mm × 175 mm × 157 mm，裂隙长度3.0 cm～21.0 cm，宽度15.7 cm，隙宽1.0 mm，采用幂律分布和Fisher分布），入口和出口分别位于模型左右两侧。通过脉冲注入含NaCl和蓝色染料的60 ℃热水，记录出口电导率（EC）换算为示踪剂浓度，并用热像仪监测表面温度。[Hua 2024, pp. 3-4]
- **数值模型数据**：利用COMSOL Multiphysics求解裂隙内水流、溶质运移和裂隙-基质热传导方程，模型经实验室观测数据验证，得到匹配的示踪剂浓度曲线和温度趋势。[Hua 2024, pp. 4-5]
- **场地尺度合成模型**：一个横向1000 m、垂向200 m的花岗岩裂隙网络（50条裂隙，隙宽1.0 mm，长度200 m～500 m，共轭裂隙组），以双井（间距300 m）抽注进行示踪试验，获得2 m³/min和3 m³/min抽水速率下的TBC。[Hua 2024, pp. 5-6, 11-12]

## Methods
1. **实验室3D打印物理模拟**：搭建透明裂隙网络模型与双空间水箱、注射泵、流量计、电导率计和热像仪联用的实验系统，实施冷水-热水脉冲示踪试验，观测裂隙内染料分布和出口TBC与温度。[Hua 2024, pp. 3-4]
2. **数值建模与验证**：在COMSOL中建立与原物理模型相同几何的裂隙‑基质耦合模型，求解达西流、对流‑弥散方程和热传导方程，通过调整基质空气‑树脂权重系数使计算TBC与观测吻合，验证数值模型的有效性。[Hua 2024, pp. 4-5]
3. **降维模型（DRM）构建**：基于TBC的拐点（浓度峰值及浓度下降阶段的异常缓慢点，即负梯度峰值）数目确定优势流路径数量，建立由等数量平行裂隙组成的DRM，利用示踪剂浓度的实测值与计算值拟合反演平行裂隙的尺寸、隙宽和间距或基质渗透率。[Hua 2024, pp. 5-5, 8-8]
4. **模型测试**：在实验室尺度，以630 mL/min抽水速率下的TBC构建DRM，预测200 mL/min、600 mL/min和1200 mL/min下的示踪剂浓度和出口温度，计算相对误差RI；在场地尺度，以2 m³/min下的TBC构建DRM，预测3 m³/min下的浓度。[Hua 2024, pp. 5-6, 10-11]

## Key Findings
1. 在抽注双井驱动的裂隙网络中，渗流和传输主要受数量有限、几何位置稳定的优先流动路径控制。在实验所用的7条交切裂隙模型中，识别出上、中、下三条优先路径，且在不同抽注速率（200 mL/min～1200 mL/min）下路径的相对流量顺序不变。[Hua 2024, pp. 6-7]
2. 示踪突破曲线（TBC）的形状与优势流路径数量直接相关：TBC中的拐点（浓度峰值与浓度下降段异常缓慢点）的数量等于优势流动路径的数量。在3D打印模型中观测到三个拐点，对应三条优先路径；场地尺度合成模型中仅观测到一个浓度峰带长尾，对应一条优先路径。[Hua 2024, pp. 8-8, 11-12]
3. 基于TBC拐点数构建的平行裂隙降维模型（DRM），其裂隙参数通过反演TBC确定，能够在独立于建模抽水速率的条件下预测出口示踪剂浓度和温度。在实验室尺度，最大预测相对误差低于10%（浓度预测误差7.6%以内，温度预测误差7.0%以内），且随抽水速率增大，预测精度提高。[Hua 2024, pp. 10-10]
4. 在场地尺度合成模型中，DRM（含一条裂隙与等效基质）对3 m³/min抽水速率下浓度的预测相对误差低于6.2%，表明该降维方法具备推广到野外尺度的潜力。[Hua 2024, pp. 11-12]
5. 为保障DRM预测精度，建议示踪试验采用低于未来资源开采的抽水速率，因为较低抽水速率下TBC拐点更易辨识，受测量误差影响更小。[Hua 2024, pp. 8-8, 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 3D打印裂隙模型中染料运移和热图像显示存在三条优先流动路径 | [Hua 2024, pp. 6-7], Fig.2 | 抽注速率630 mL/min，裂隙几何固定 | 实验室直接观察 |
| 数值模拟显示三条优先路径的流量在200~1200 mL/min范围内保持稳定排序（上>中>下） | [Hua 2024, pp. 7-8], Fig.8 | 裂隙几何、井位、温度差异不变，仅改变抽注速率 | 抽注速率增大时优先流增强，但路径结构不变 |
| TBC在200 mL/min下出现三个拐点（1个浓度峰+2个下降缓慢点），与三条优先路径对应 | [Hua 2024, pp. 8-8], Fig.10a5 | 抽注速率200 mL/min | 拐点时间与各路径示踪剂到达时间吻合 |
| 630 mL/min下的TBC反演得到两平行裂隙DRM（代表合并后的上、下路径），预测200、600、1200 mL/min浓度误差分别为7.6%、3.2%、1.52%，温度误差7.0%、2.5%、1.3% | [Hua 2024, pp. 10-10], Figs.11,12 | 裂隙网中基质极低渗透，温度<100°C | 预测精度随抽注速率升高而提高 |
| 场地尺度模型以2 m³/min TBC构建单裂隙+基质DRM，预测3 m³/min TBC误差低于6.2% | [Hua 2024, pp. 11-12], Fig.14 | 合成花岗岩裂隙网，50条裂隙，双井，保守示踪剂 | 用等效基质代表次要流径 |

## Limitations
- DRM基于裂隙发育于极低渗透围岩的假设建立，未考虑可渗透岩石基质中的流动和传输。[Hua 2024, pp. 11-12]
- 研究仅针对双井（一对抽注井）驱动的情况，多井系统下的适用性有待考察。[Hua 2024, pp. 11-12]
- 数值模型未考虑温度超过100°C时扩散率和热交换率的温度依赖性，深层高温条件下需进一步讨论。[Hua 2024, pp. 12-12]
- 高抽注速率下TBC的第二拐点可能变得模糊，受现场测量误差影响可能无法识别，导致DRM中路径数估算偏差。[Hua 2024, pp. 8-8]
- 实验室热像仪测量的是裂隙表面温度，与裂隙内流体实际温度存在偏差，但数值模型显示温度和浓度的趋势一致。[Hua 2024, pp. 4-4]
- DRM中的裂隙尺寸和隙宽不代表原始裂隙的实际值，而是反映合并多个流径后等效的输运能力。[Hua 2024, pp. 9-10]

## Assumptions / Conditions
- 裂隙网络中基质（围岩）的渗透性和孔隙度极低，水流和溶质运移仅在裂隙内发生；热量则在裂隙和基质中均有传导。[Hua 2024, pp. 4-4]
- 抽注过程以对流为主导，分子扩散和热弥散的影响可忽略。[Hua 2024, pp. 4-5]
- 温度低于100°C，忽略温度对溶质弥散系数、水与岩石热容和导热系数的影响。[Hua 2024, pp. 4-5]
- 裂隙隙宽均匀，采用平行板模型（达西定律）描述裂隙渗流。[Hua 2024, pp. 4-4, Table 1]
- 示踪剂为保守溶质（NaCl），脉冲注入，不考虑吸附和化学反应。[Hua 2024, pp. 3-4]
- 裂隙几何和井位固定时，优先流动路径的相对强度在不同抽注速率下保持稳定，仅流量绝对值变化。[Hua 2024, pp. 7-8]
- TBC的拐点（浓度峰值和浓度下降速率异常缓慢点）可由浓度-时间导数（负值和峰值）识别。[Hua 2024, pp. 5-5, 8-8]
- DRM中平行裂隙的距离、尺寸、隙宽通过拟合TBC整体浓度时间序列确定，不直接对应实际单条裂隙的物理参数。[Hua 2024, pp. 8-10]

## Key Variables / Parameters
| Variable / Parameter | Description | Typical Value / Range (from study) | Source |
|----------------------|-------------|-----------------------------------|--------|
| Number of inflection points (concentration peaks, slowness points) | 指示优势流路径数量 | 3 (lab), 1 (field-scale) | [Hua 2024, pp. 8-8, 11-12] |
| Fracture aperture, d | 裂隙水力隙宽，用于平行板模型计算渗透率 (k = d²/12) | 0.56–1.15 mm (inverted DRM) | [Hua 2024, pp. 8-10, Table 2] |
| Fracture size (length, width) | 平行裂隙的几何尺寸，影响热量交换面积和流动时间 | 0.34 m×0.16 m, 0.60 m×0.16 m (lab DRM); 350 m×400 m (field DRM) | [Hua 2024, pp. 10-10, Table 2; pp. 11-12] |
| Distance between parallel fractures | DRM中两平行裂隙的间距，控制流体间相互作用 | 0.13 m (lab DRM) | [Hua 2024, pp. 10-10, Table 2] |
| Pumping rate (injection/extraction) | 抽水/注水速率，影响TBC尖峰及预测误差 | 200–1200 mL/min (lab), 2–3 m³/min (field) | [Hua 2024, pp. 8-8, 11-12] |
| Tracer concentration at outlet | 出口示踪剂浓度，用于拟合DRM参数 | observed and simulated | [Hua 2024, pp. 4-5, 10-11] |
| Outflow temperature | 出口流体温度，用于验证DRM预测能力 | lab up to ~60°C (pulse) | [Hua 2024, pp. 4-5, 10-11] |
| Relative error (RI) | 评估DRM预测性能的指标 | <10% (lab), <6.2% (field) | [Hua 2024, pp. 5-5, Eq.7, 10-11] |
| Weight coefficient θ in matrix mixture | 数值模型中代表空气与树脂比例的参数，校准时调整使模拟与观测吻合 | adjusted to 0.86 | [Hua 2024, pp. 4-5] |

## Reusable Claims
1. 在抽注双井的复杂裂隙含水层中，当基质渗透性极低且对流占主导时，示踪剂突破曲线（TBC）中出现的拐点（浓度峰值及浓度下降速率异常缓慢点）数量与优势流动路径数量相等。该关系在抽注速率变化（200 mL/min至1200 mL/min，即6倍范围内）情况下仍成立。[Hua 2024, pp. 8-8] **条件**：裂隙几何和井位固定，温度差引起的密度流未改变路径排序。
2. 利用TBC拐点数量确定的平行裂隙降维模型（DRM）可以在不依赖原始裂隙网络几何信息的情况下，通过反演TBC得到等效裂隙参数，进而精确预测独立于模型构建抽注速率的出口示踪剂浓度和温度，相对误差低于10%。预测精度随抽注速率增加而提高，因为高速率下次要流径的贡献减弱。[Hua 2024, pp. 10-10, 11-12] **条件**：抽注速率不低于构建DRM所用的速率，且基质渗透性可忽略。
3. 在场地尺度应用中，若TBC呈现单一浓度峰带长尾（无多个明显拐点），可构建单一裂隙嵌入等效基质的DRM，该模型仍能以较高精度（RI < 6.2%）预测不同抽注速率下的示踪剂浓度。[Hua 2024, pp. 11-12] **条件**：合成裂隙网络由一个主导路径和众多交集无序的次级路径组成，这些次级路径的集体效应可通过等效孔隙基质参数表达。
4. 为保证DRM的构建可靠性，示踪试验宜采用低于未来生产运行的抽注速率，以便清晰识别TBC中的拐点，避免测量误差掩盖弱拐点。[Hua 2024, pp. 8-8, 11-12] **条件**：裂隙网络几何稳定，抽注速率差异在6倍以内。

## Candidate Concepts
- [[dimensionality reduction model (DRM)]]
- [[tracer breakthrough curve (TBC)]]
- [[preferential flow path]]
- [[fracture network]]
- [[discrete fracture network (DFN)]]
- [[equivalent porous medium (EPM)]]
- [[3D-printed fracture model]]
- [[inflection point (concentration peak / slowness point)]]
- [[parallel fracture model]]
- [[dipole well injection-extraction]]
- [[density-driven flow]]
- [[hydraulic tomography]]
- [[transdimensional Bayesian inversion]]

## Candidate Methods
- [[3D printing (digital light projection)]]
- [[COMSOL Multiphysics finite element simulation]]
- [[tracer test with dual-space injection system]]
- [[electrical conductivity (EC) logging for tracer concentration]]
- [[thermal camera monitoring for fracture surface temperature]]
- [[Levenberg-Marquardt algorithm for parameter inversion]]
- [[flow-rate-weighted tracer concentration averaging]]
- [[power law distribution for fracture length]]
- [[Fisher distribution for fracture orientation]]
- [[relative error (RI) as predictive performance metric]]
- [[gradient analysis of TBC to identify slowness points]]

## Connections To Other Work
- 传统裂隙网络模拟多采用等效多孔介质（EPM）或离散裂隙网络（DFN），前者计算效率高但保真度低，后者保真度高但计算成本大。本研究的降维模型旨在平衡精度与效率。[Hua 2024, pp. 1-1]
- 已有多种降维技术用于非均质介质反演，如奇异值分解、离散小波变换、自编码神经网络和生成对抗网络等，但这些DRM通常需要预设的地下结构，而本文提出的DRM直接基于可观测的TBC，更具实用性。[Hua 2024, pp. 1-2]
- 在裂隙表征方面，水力层析成像（hydraulic tomography）和跨维贝叶斯反演可用于推断2D/3D裂隙几何，但受限于钻孔数据和计算量。本文的DRM通过TBC拐点数目减少参数维度，为解决反演不适定性提供了一种新思路。[Hua 2024, pp. 1-2]
- 文中提及的embedded fracture models、pipe network models、graph network models等也为多尺度建模提供了参考。[Hua 2024, pp. 1-1]

## Open Questions
- 当围岩本身具有可观的渗透性时，如何扩展DRM以同时表征裂隙和基质中的流动与传输？[Hua 2024, pp. 11-12]
- 在多井（两个以上）联合抽注的场景下，TBC形状与优势流路径的关系如何，DRM的构建策略需要哪些调整？[Hua 2024, pp. 11-12]
- 对于温度超过100 ℃的深层地热储层，流体热物性和裂隙‑基质热交换对温度的依赖性如何在DRM中体现并影响预测精度？[Hua 2024, pp. 12-12]
- 如何降低高抽注速率下TBC第二拐点“弱化”引起的DRM模型阶次（平行裂隙数量）误判风险？[Hua 2024, pp. 8-8]
- DRM中代表等效基质渗透率和孔隙度的参数在真实场地的获取（如通过常规测试）及与原始裂隙网络中次要流径的对应关系有待进一步研究。[Hua 2024, pp. 11-12]

## Source Coverage
本页面完全依据所提供15个非空索引片段（文本块）编译而成。所有15个片段均已纳入处理，编译后的源文本利用率按片段计为100%（coverage_ratio_by_blocks = 1.0），按字符计约为95.2%（coverage_ratio_by_chars ≈ 0.951771）。未引入任何索引片段之外的作者、数据或结论。源文件签名为72c0d06b9bca1549770f3a83570f048af2dde0b1。
