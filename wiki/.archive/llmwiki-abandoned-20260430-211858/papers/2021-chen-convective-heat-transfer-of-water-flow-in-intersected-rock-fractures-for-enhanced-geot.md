---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-chen-convective-heat-transfer-of-water-flow-in-intersected-rock-fractures-for-enhanced-geot"
title: "Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction."
status: "draft"
source_pdf: "data/papers/2022 - Convective heat transfer of water flow in intersected rock fractures for enhanced geothermal extraction.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Chen, Yuedu, Zhihong Zhao, and Huan Peng. \"Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2021."
indexed_texts: "12"
indexed_chars: "57853"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:55:40"
---

# Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.

## One-line Summary
本文通过构建一系列三维交叉粗糙裂隙模型，模拟研究了死端裂隙（DEF）的几何特征（交叉角、孔径、长度与连通性）对增强地热系统中水-热耦合传热行为的影响，指出粗糙环流、90°交叉角、较长长度和流动网络化有益于提高热提取效率。[Chen 2021, pp. 1-1]

## Research Question
研究问题包括：（1）理解三维交叉粗糙裂隙中流体流动与传热的行为；（2）测定死端裂隙（DEF）与主流裂隙（MFF）的几何配置（交叉角、孔径、长度、连通性）如何影响热提取，为增强地热系统提供设计依据。[Chen 2021, pp. 2-3]

## Study Area / Data
本研究为数值模拟，未涉及特定地理区域。计算几何由含一条水平主流裂隙和一条/多条死端裂隙的立方体区域构成。粗糙裂隙的孔径异质性分布基于真实粗糙岩石裂隙，但具体生成方法未从索引片段中确认。模型验证采用二维单裂隙解析解，参数取自花岗岩与水（如壁温 120°C、注入水温 30°C、水密度 1000 kg/m³、水比热 4200 J/(kg·K)、花岗岩比热 1000 J/(kg·K)、花岗岩导热系数 2.4 W/(m·K)）。[Chen 2021, pp. 3-4]

## Methods
构建了三维平板与粗糙交叉裂隙模型，并基于有限元法进行热-水流-固耦合（仅考虑水热耦合）数值模拟。通过求解包含温度相关参数的流动与传热控制方程，实现速度场与温度场的双向耦合。模型验证采用二维单裂隙模型解析解，数值与解析结果的最大误差为1.4%。[Chen 2021, pp. 3-4]

共设定三组模拟场景：（I）不同交叉角（30°、45°、60°、90°）的平板与粗糙模型，注入速度分别为 0.0002 m/s、0.002 m/s 和 0.2 m/s；（II）DEF 不同孔径（0.082–0.432 mm）和长度（2–15 mm），注入速度为 0.0002 m/s、0.002 m/s 和 0.02 m/s；（III）不同连通性的 DEF 配置（单个 DEF、三条未连通 DEF、七条连通 DEF 构成网络），注入速度与场景 II 相同。边界条件为入口恒速注水、出口零压力梯度，裂隙壁温保持恒定。[Chen 2021, pp. 4-7]

## Key Findings
- 粗糙 DEF 内形成环形流线，冷锋呈现椭圆分布；相比平板 DEF，粗糙 DEF 中的流体流动增强了传热。[Chen 2021, pp. 1-1, pp. 7-10]
- 出口水温增量 ΔTout 和热产率比 Qr 在交叉角 90° 时最大，随交叉角减小而下降。[Chen 2021, pp. 1-1]
- 增大 DEF 长度能提高 ΔTout 和 Qr；而增大 DEF 孔径反而导致这两个指标先显著下降、随后趋于平缓。[Chen 2021, pp. 1-1, pp. 12-14]
- 仅增加未连通的 DEF 数量对热提取的改善有限；将 DEF 与 MFF 连接形成流动网络，可获得更显著的热产率提升。[Chen 2021, pp. 1-1, pp. 10-12]
- 流体进入 DEF 的深度随注入速度增加而加大；粗糙裂隙中沿 DEF 的流速分布非均匀且存在局部高速区，平板裂隙中则衰减较快。[Chen 2021, pp. 10-12]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 出口水温增量 ΔTout 与热产率比 Qr 在交叉角 90° 时最大，随角度减小而降低。 | [Chen 2021, pp. 1‑1, Fig. 18] | 场景 I：平板与粗糙裂隙，交叉角 30°、45°、60°、90°；三种注入速度。 | 粗糙与平板模型均呈现该趋势。 |
| 增大 DEF 孔径（0.082→0.232 mm）导致 ΔTout 与 Qr 显著下降，之后趋于平稳。 | [Chen 2021, pp. 12‑14, Fig. 19a,c] | 场景 II：变化孔径；注入速度 0.0002、0.002、0.02 m/s。 | 原因为孔径增大导致 DEF 内流速降低。 |
| 增大 DEF 长度（2→15 mm）导致 ΔTout 与 Qr 上升。 | [Chen 2021, pp. 12‑14, Fig. 19b,d] | 场景 II：变化长度；注入速度 0.0002、0.002、0.02 m/s。 | 更长 DEF 内流速更高，促进热交换。 |
| 连接多个 DEF 形成网络时的热产率明显高于孤立 DEF 配置。 | [Chen 2021, pp. 1‑1, pp. 10‑12, Fig. 16] | 场景 III：模型 M0(单 DEF)、M1(3 条未连通 DEF)、M2(7 条连通 DEF)；三种注入速度。 | 高温流动路径的形成强化了热提取。 |
| 粗糙 DEF 内出现环形流线，局部高速区位于交叉处；v/v₀ 沿 DEF 呈非线性衰减。 | [Chen 2021, pp. 7‑10, Fig. 10, Fig. 17] | 粗糙裂隙模型，注入速度 0.0002 m/s 等。 | 平板 DEF 中无环形流线，速度衰减更快。 |

## Limitations
- 模型验证仅采用二维单裂隙解析解，缺乏三维交叉裂隙的实验或现场观测数据标记 [Chen 2021, pp. 3-4]。
- 模拟仅考虑水-热耦合，未纳入热弹性、孔隙弹性等力学过程对裂隙开度的动态影响 [Chen 2021, pp. 1-2]。
- 研究尺度为毫米至厘米级小型岩块，所得结论向储层尺度的外推性未从索引片段中确认。
- 粗糙裂隙的孔径分布生成细节及对普适性的影响未在片段中说明。
- 壁温假设为恒定，未考虑岩石基质热量衰竭导致的非稳态边界效应。

## Assumptions / Conditions
- 流体为不可压缩牛顿流体，流动为层流。
- 岩石基质不透水，热量交换仅通过裂隙壁面的热传导进行。
- 裂隙壁面温度恒定（120°C），注入水温固定为 30°C。
- 流-热耦合通过温度依赖的物性参数（密度、比热、黏度、导热系数）以及对流项中的速度场实现。
- 模型边界为入口恒速注入、出口零压力梯度；计算域为立方体，包含一条水平 MFF 和预设的 DEF。
- 三种注入速度分别设定为 0.0002 m/s、0.002 m/s 和 0.02 m/s（或 0.2 m/s，视场景而定）。[Chen 2021, pp. 3-7]

## Key Variables / Parameters
- ΔTout（出口水温增量，Tout − T₀）
- Qr（热产率比，Q/Q₀）
- 注入速度 v_inj
- DEF 机械孔径（0.082–0.432 mm）
- DEF 长度（2–15 mm）
- 交叉角（30°、45°、60°、90°）
- 归一化流速比 v/v₀（沿 DEF 长度方向）
- 水与花岗岩的热物性参数（ρ_w=1000 kg/m³, Cp_w=4200 J/(kg·K), Cp_r=1000 J/(kg·K), K_r=2.4 W/(m·K)）[Chen 2021, pp. 3-4, pp. 12-14]

## Reusable Claims
1. **粗糙死端裂隙的环流增强传热**：相比平板裂隙，粗糙 DEF 因孔径异质性产生环形流线，增加低温流体与热岩壁的接触面积，从而提高出口水温与热产率。适用条件：裂隙壁面粗糙度明显，产生可辨识的局部流动通道。证据：[Chen 2021, pp. 1-1, pp. 7-10]。限制：仅针对毫米级单交叉裂隙，粗糙度特征与天然裂隙的对应关系尚未标定。
2. **90° 交叉角对热提取最有利**：当 DEF 与 MFF 垂直相交时，DEF 内流速渗透最深，热产率最高；交叉角减小会导致热提取效率单调下降。适用条件：单条 DEF 与 MFF 相交，无其他裂隙干扰。证据：[Chen 2021, pp. 1-1, Fig. 18]。限制：未考虑裂隙网络中的复杂交叉和多分支效应。
3. **长度效应优于孔径效应**：加长 DEF 可持续提高热产率，而扩径反而降低热产率（初期下降明显，后期趋缓）。因此，通过水力压裂延长裂隙长度比单纯扩大开度更有利于热开采。适用条件：注入速度在 0.0002 m/s 至 0.02 m/s 范围内，DEF 孔径范围 0.082–0.432 mm。证据：[Chen 2021, pp. 12-14]。限制：未考虑压裂导致的粗糙度改变和孔径‑长度的耦合关系。
4. **连通性对热提取的放大作用**：孤立增加死端裂隙数量对热提取的提升微乎其微；只有当 DEF 相互连通形成有效流动网络时，才可大幅度增加热产率。适用条件：网络内部存在有效的压力驱动流动。证据：[Chen 2021, pp. 1-1, pp. 10-12]。限制：仅对比了特定网络配置（3 条未连通 vs. 7 条连通），网络拓扑的优化参数未涵盖。

## Candidate Concepts
- [[enhanced geothermal system]]
- [[fracture reservoir]]
- [[dead-end fracture]]
- [[main flow fracture]]
- [[convective heat transfer in fractures]]
- [[rough fracture]]
- [[heterogeneous aperture distribution]]
- [[flow channeling]]
- [[cold front geometry]]
- [[heat production ratio]]
- [[fracture connectivity]]

## Candidate Methods
- [[3D intersected fracture modeling]]
- [[hydrothermal coupling simulation]]
- [[analytical solution for single fracture heat transfer]]
- [[velocity ratio analysis along fracture]]
- [[parametric study of fracture geometry]]
- [[finite element method for coupled flow and heat transport]]

## Connections To Other Work
- 本文与 Ma et al. (2020) 共同关注交叉裂隙对冷锋形态的影响，并指出裂缝空间分布控制热量抽取的均匀性；本文使用三维粗糙交错模型进一步量化了 DEF 几何的作用。
- 与 Shi et al. (2019a) 的发现一致：过多的孤立优先流动通道可能加速热突破，而较长且连通良好的裂隙对长期热提取更有利。本文通过连通性模拟为此提供了新的计算证据。
- 与 Salimzadeh et al. (2018) 等热‑力‑水耦合研究相比，本文仅考虑水热耦合，属于简化情况，但可为后续引入热‑力学效应的模拟提供基准。
- 方法上可与 [[thermo-poroelastic effects on fracture aperture]]、[[discrete fracture network modeling]] 及 [[field-scale heat extraction simulation]] 等方向建立联系。

## Open Questions
- 本文仅针对简单单交叉几何，天然裂隙网络的复杂拓扑、多尺度和非均质性如何影响传热仍需研究。
- 将恒定壁温边界替换为动态岩石降温边界后，长期热产率和冷锋演化趋势会发生何种变化。
- 热应力诱发的裂隙开度变化（热‑力耦合）会如何影响沟槽效应和网络连通性，进而改变热开采效率。
- 粗糙度的统计描述方法和尺度效应如何影响传热规律的可推广性。
- 在模型尺度上进行实验验证（例如微流体或岩心驱替实验）能否复现环形流线和冷锋形状。
以上问题均未从索引片段中确认。

## Source Coverage
本知识页基于 12 个索引片段构建，覆盖了摘要、引言、研究目的、方法描述、模拟场景、流场与温度场结果、以及部分讨论文字。摘要提供了主要发现的浓缩版，方法章节较为完整地给出了计算域、边界条件与验证细节，结果部分呈现了流线、温度分布的关键定性信息，讨论部分抽取了交叉角、孔径、长度和连通性的影响规律。

**缺失部分**：索引片段未包含文章的最终结论、研究意义、未来工作计划等末尾章节。定量结果（如全部模拟的 ΔTout 和 Qr 数值）仅以文字描述形式出现，无法提供完整的表格化证据。粗糙裂隙的孔径分布生成算法与统计特征也未在片段中明确陈述。因此，本页可能在定量细节、模型假设的深层推导以及与研究趋势的联系方面不够充分。
