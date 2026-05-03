---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-bu-deterioration-of-equivalent-thermal-conductivity-of-granite-subjected-to-heating-cooling"
title: "Deterioration of Equivalent Thermal Conductivity of Granite Subjected to Heating-Cooling Treatment."
status: "draft"
source_pdf: "data/papers/2024 - Deterioration of equivalent thermal conductivity of granite subjected to heating-cooling treatment.pdf"
collections:
  - "zotero new"
citation: "Bu, Mohua, et al. \"Deterioration of Equivalent Thermal Conductivity of Granite Subjected to Heating-Cooling Treatment.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2024."
indexed_texts: "15"
indexed_chars: "72958"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "73257"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004098"
coverage_status: "full-index"
source_signature: "9dc448534010bfc5d24e5568914a83347d7a2745"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:20:45"
---

# Deterioration of Equivalent Thermal Conductivity of Granite Subjected to Heating-Cooling Treatment.

## One-line Summary
本文通过实验和数值模拟研究加热-冷却处理对花岗岩等效热导率（ETC）的恶化规律，揭示了加热温度与冷却速率共同作用下孔隙结构与微裂纹演化对热传导性能的影响机制。

## Research Question
不同冷却速率（空气冷却、水冷却、液氮冷却）如何影响高温花岗岩的等效热导率？加热与冷却过程中孔隙结构与微裂纹的演化如何导致热传导性能的恶化？

## Study Area / Data
- **岩石类型**：细粒花岗岩，取自中国东南沿海厦门湾-漳州盆地，矿物组成为石英32.4%、斜长石19.0%、钾长石45.2%、黑云母3.4%，平均P波速度4499 m/s，密度2.795 g/cm³，初始孔隙度约0.55% [Bu 2024, pp. 2-3]。
- **试件规格**：圆盘试件，直径50 mm，高径比约0.5，端部平整度约10 mm，粗糙度约3 mm [Bu 2024, pp. 2-3]。
- **热处理条件**：加热速率5°C/min，目标温度（20°C、150°C、300°C、450°C、600°C、750°C）保温2小时 [Bu 2024, pp. 3-6]。
- **冷却方式**：空气冷却、浸入20°C循环水冷却、液氮冷却（随后自然回温至20°C） [Bu 2024, pp. 3-6]。

## Methods
- **等效热导率（ETC）测量**：采用ISRM推荐的瞬态热线法，测量精度约3%，通过组合测量面取平均值 [Bu 2024, pp. 3-6]。
- **孔隙结构分析**：低场核磁共振（NMR），利用横向弛豫时间T₂ 分布表征孔径分布，并由信号幅度换算孔隙度分量 [Bu 2024, pp. 8-8]。
- **微裂纹观察**：光学显微镜（SD-3000A自动影像扫描系统）拍摄薄片，计算微裂纹线密度 [Bu 2024, pp. 10-12]。
- **数值模拟**：基于CT-GBM离散元模型，重建矿物分布异质性，采用光滑节理模型（SJ）和平行黏结模型（PB），模拟不同加热温度（150–750°C）和冷却速率（10、50、100、150、200°C/min）下的微裂纹扩展与有效热管数量变化 [Bu 2024, pp. 13-14]。

## Key Findings
1. **ETC与温度、冷却速率的关系**：ETC随加热温度升高呈非线性下降；相同加热温度下，冷却速率越快，ETC降幅越大；温度越高，冷却速率的影响越显著。例如，750°C时空气冷却、水冷却、液氮冷却后ETC分别下降44.06%、51.77%、61.56% [Bu 2024, pp. 3-6]。
2. **物理参数的相关性**：ETC与P波速度、密度均呈正相关关系，拟合R²≥0.9 [Bu 2024, pp. 6-8]。
3. **孔隙结构演化**：加热与冷却导致孔隙度增加，尤其是450–600°C区间因石英相变（573°C）造成急剧增长。相同温度下，液氮冷却后的孔隙度最高。ETC与孔隙度呈幂函数负相关（R² 0.96-0.993）[Bu 2024, pp. 8-10]。
4. **微裂纹密度**：微裂纹密度随温度和冷却速率增大而升高，以沿晶裂纹和穿晶裂纹（多在石英颗粒内）为主。ETC与微裂纹密度呈良好线性负相关（R² 0.973-0.995）[Bu 2024, pp. 10-12]。
5. **数值模拟揭示**：冷却过程中，边界快速降温形成大温度梯度，产生拉应力（最大拉力随冷却速率增加而增大），导致微裂纹从边缘向内部扩展；裂纹的产生减少有效热管数量，从而劣化热传导性能 [Bu 2024, pp. 14-17]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| ETC由室温的2.436 W/(m·K) 降至750°C空气冷却后的约1.36 W/(m·K)（降幅44.06%），液氮冷却后降至约0.938 W/(m·K)（降幅61.56%） | [Bu 2024, pp. 3-6] | 加热速率5°C/min，保温2h，干燥状态 | 图5展示三组冷却的ETC变化 |
| ETC与P波速度的幂函数拟合R²>0.9，与密度的幂函数拟合R²>0.9 | [Bu 2024, pp. 6-8] | 相同热处理条件 | 图7 a,b |
| 600°C时，空气冷却孔隙度0.61%→1.96%，水冷却→2.14%，液氮冷却→2.67% | [Bu 2024, pp. 8-10] | 由NMR T₂ 分布换算 | 图9a，Boltzmann拟合R²>0.99 |
| ETC与孔隙度呈负幂律关系，液氮冷却拟合R²=0.966 | [Bu 2024, pp. 8-10] | 干燥状态 | 图9b |
| 750°C时微裂纹密度：空气冷却1.39 mm⁻¹，水冷却1.73 mm⁻¹，液氮冷却2.02 mm⁻¹ | [Bu 2024, pp. 10-12] | 薄片基线法统计 | 图12a |
| ETC与微裂纹密度线性关系，水冷却R²=0.995 | [Bu 2024, pp. 10-12] | 干燥状态 | 图12b |
| 数值模拟显示，600°C初始，冷却速率200°C/min时最大拉力1.01×10⁵ N，裂纹总数最高 | [Bu 2024, pp. 14-17] | CT-GBM模型，冷却至20°C | 图17a, 图15 |
| 有效热管数量随微裂纹增加而减少，冷却速率越高，热管数量越少 | [Bu 2024, pp. 14-17] | 模型冷却模拟 | 图18b,c |

## Limitations
- 实验仅采用三种冷却方式（空气、水、液氮），未能精确控制连续冷却速率 [Bu 2024, pp. 17-17]。
- 所有ETC测试均在干燥条件下进行，未考虑含水状态的影响 [Bu 2024, pp. 17-17]。
- 数值模拟为二维（2D），计划将来建立三维（3D）模型 [Bu 2024, pp. 17-17]。

## Assumptions / Conditions
- 所有ETC测量均在干燥条件下进行 [Bu 2024, pp. 12-13]。
- 加热速率5°C/min且保温2小时以确保内外均温 [Bu 2024, pp. 3-6]。
- 瞬态热线法测量范围仅为探头径向10 mm区域，通过多面组合测量取平均以代表整体特性 [Bu 2024, pp. 3-6]。
- NMR 分析中忽略体弛豫和扩散弛豫，仅考虑表面弛豫，且对于花岗岩取r₂F_S=1×10⁻⁸ m/ms [Bu 2024, pp. 8-8]。
- 数值模型假设矿物颗粒为刚性体，热接触管与力学接触状态绑定 [Bu 2024, pp. 13-14]。

## Key Variables / Parameters
- 等效热导率 [[ETC]] (W/(m·K))
- 加热温度 (°C)
- 冷却速率 (°C/min)
- P波速度 (m/s)
- 密度 (g/cm³)
- 孔隙度 (%)
- 微裂纹密度 (mm⁻¹)
- 热管数量 (Np)
- 热应力 (N)
- 表面弛豫率与形状因子乘积 (r₂F_S)

## Reusable Claims
- 花岗岩ETC随加热温度升高非线性下降，且冷却速率越大下降越明显，高温下差异更显著 [Bu 2024, pp. 3-6]。
- 冷却过程产生的温度梯度导致拉应力，引发微裂纹从边界向内部扩展，并且裂纹产生使有效热管减少，从而劣化热传导 [Bu 2024, pp. 14-17]。
- 孔隙度与微裂纹密度的增加是ETC降低的主要原因，两者均与ETC呈良好的负相关函数关系 [Bu 2024, pp. 8-12]。
- 石英在573°C的相变引起体积急剧膨胀，是450–600°C区间结构损伤加剧的关键因素 [Bu 2024, pp. 10-12]。
- 液氮冷却即使在室温下也能对花岗岩产生结构损伤（孔隙度增加约21.8%），表明极低温度可独立诱发微裂纹 [Bu 2024, pp. 8-8]。
- 干燥条件下，低孔隙度花岗岩的ETC主要受矿物组成控制，而热损伤造成的孔隙和裂纹会显著削弱导热能力 [Bu 2024, pp. 1-2, 12-13]。

## Candidate Concepts
- [[equivalent thermal conductivity]]
- [[cooling rate]]
- [[thermal stress]]
- [[microcrack density]]
- [[porosity]]
- [[heating-cooling treatment]]
- [[grain-based model]]
- [[thermal pipe contact model]]
- [[quartz phase transition]]
- [[transient hot-wire method]]
- [[enhanced geothermal systems]]
- [[hot dry rock]]
- [[high geo-temperature tunnel]]

## Candidate Methods
- [[transient hot-wire method for ETC]]
- [[low-field NMR for pore structure]]
- [[optical microscopy and baseline intersection method for crack density]]
- [[CT-GBM discrete element numerical simulation]]
- [[Boltzmann function fitting for porosity evolution]]
- [[power-law fitting for ETC-porosity and ETC-density relationships]]

## Connections To Other Work
- 本研究结果与Li等（2021）和Wu等（2021）一致：水冷却后ETC低于空气冷却 [Bu 2024, pp. 12-13]。
- 图13比较了多篇文献中不同冷却方式下花岗岩归一化ETC的变化，证实冷却速率的影响具有普适性 [Bu 2024, pp. 12-13]。
- 模拟所用CT-GBM模型基于Guo等（2023c）的验证工作，模型参数和有效性已通过实验对比确认 [Bu 2024, pp. 13-14]。

## Open Questions
- 如何在实验中精确量化与控制连续的冷却速率，而非仅依赖三种冷却介质 [Bu 2024, pp. 17-17]。
- 含水状态（饱和或部分饱和）对加热-冷却后花岗岩ETC的影响尚未研究 [Bu 2024, pp. 17-17]。
- 三维热-力耦合数值模型对ETC劣化的模拟能力有待开发 [Bu 2024, pp. 17-17]。

## Source Coverage
本页面严格基于提供的15个索引片段编译完成，所有非空索引片段均已处理。索引文本总字符数72958，编译后源块字符数73257，覆盖率（按字符）为1.004。
