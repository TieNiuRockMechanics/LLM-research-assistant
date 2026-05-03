---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-hu-damage-mechanism-and-heat-transfer-characteristics-of-limestone-after-thermal-shock-cycl"
title: "Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development."
status: "draft"
source_pdf: "data/papers/2022 - Damage mechanism and heat transfer characteristics of limestone after thermal shock cycle treatments based on geothermal development.pdf"
collections:
  - "论文"
citation: "Hu, Jianjun, et al. \"Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 160, 2022, p. 105269. Accessed 2026."
indexed_texts: "8"
indexed_chars: "39273"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36027"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.917348"
coverage_status: "full-index"
source_signature: "398aabc6334aa191180cc77193980ef9ab4553b8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:10:00"
---

# Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development.

## One-line Summary
本文通过循环热冲击实验（100 °C–500 °C，0–5次冷热循环）研究石灰岩的热损伤机制与导热特性，发现温度与循环次数显著降低其P波速度、热导率和抗拉强度，并建立三者间的线性关系，为碳酸盐岩地热储层开发提供理论支持。

## Research Question
在干热岩（HDR）地热开发中，冷水热冲击会改变岩石的物理力学性质（如孔隙度、渗透率、热导率）。针对碳酸盐岩地热储层研究较少的现状，本文探究不同温度与冷热循环次数对石灰岩热力学参数的影响及损伤机理。

## Study Area / Data
实验所用石灰岩采自中国石家庄附近，基质致密、热稳定性好，天然状态下无可见表面裂纹，平均体积密度2.65 g/cm³。所有试样取自同一块石灰岩，沿相同方向钻取，制成Ф50 × 100 mm长圆柱和Ф50 × 25 mm短圆柱，端面平行度误差≤±0.02 mm。实验设置5个温度等级（100、200、300、400、500 °C）与6种循环次数（0、1、2、3、4、5次），其中0次表示仅高温处理而不进行水中快冷。

## Methods
- **循环热冲击处理**：试样在马弗炉中以5 °C/min升温至目标温度，保温2 h后取出迅速水冷，再在50 °C干燥箱中烘干24 h，以此循环。
- **表面色度测量**：采用CIE‑L\*a\*b\*系统获取短圆柱试样的表面色度（L\*亮度，a\*绿‑红，b\*蓝‑黄）。
- **裂纹观察**：使用Supereye B007显微镜放大300倍观察表面裂纹。
- **热导率与P波速度**：分别用Xiangke DRE‑2C热导率仪和RSM‑SY5波速检测仪测试长圆柱试样。
- **抗拉强度**：用WAW‑1000D微机电液伺服试验机（最大轴向载荷1000 kN）对短圆柱试样进行巴西劈裂测试。
- **数值模拟**：借助COMSOL Multiphysics 5.4的固体传热模块，对直径5 cm、高度10 cm的圆柱试样进行瞬态热传导模拟，初始内部温度25 °C，边界温度100–500 °C，网格细化，加热时间60 min。

## Key Findings
1. **表面特征变化**：温度升高时L\*值增大（表面变亮），循环次数增加时L\*值减小（表面变暗）；a\*值无明显趋势且波动大；b\*值随温度和循环次数增加而升高（表面变黄）；300 °C后出现明显表面裂纹，且温度越高、循环次数越多，裂纹宽度和数量增加。

2. **热导率与P波速度**：当循环次数固定时，热导率随温度升高而降低；温度固定时，热导率随循环次数增加而降低（无处理到1次循环的热导率下降尤为显著）。P波速度随温度升高和循环次数增加均呈下降趋势。

3. **抗拉强度**：随温度变化分为两个阶段：100–200 °C因矿物弱膨胀使微裂纹闭合，强度略有升高；200–500 °C因矿物持续膨胀及热冲击效应，强度快速下降。温度恒定时，抗拉强度随循环次数增加而降低。例如500 °C下0次循环抗拉强度为4.31 MPa，5次循环降至2.13 MPa；0与5次循环间的降幅从100 °C的15.46%增至500 °C的50.56%。

4. **损伤因子**：基于P波速度定义的损伤因子D\_T（温度主导）和D\_L（循环次数主导）均随温度或循环次数增加而增大。

5. **参数间强线性相关**：热导率λ与P波速度Vp：λ = 0.36189 Vp + 0.9059（R²=0.9269）；抗拉强度σ与热导率λ：σ = 3.005 λ − 1.435（R²=0.8367）；抗拉强度σ与P波速度Vp：σ = 1.1547 Vp + 1.0567（R²=0.8738）。上述关系仅在Vp范围1.75–5.13 km/s、λ范围1.36–2.99 W/m·K内成立。

6. **内部传热数值模拟**：相同加热温度和加热时间下，循环次数越多试样中心温度越低；无热冲击试样随边界温度升高中心温度递增，但经历循环后500 °C时中心温度反而下降。加热过程内部升温分为两个阶段：0–15 min快速升温，15–30 min缓慢升温。

7. **损伤机理**：方解石晶体的各向异性热膨胀（轴向拉伸、径向压缩）导致晶间裂纹萌生与扩展，高温与冷热循环加剧了裂纹发育，最终削弱了热导率、波速和抗拉强度。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 温度升高时L\*值增大，循环次数增加时L\*值减小；b\*值均随两者增加而升高 | [Hu 2022, pp. 1-3] | 短圆柱试样，CIE‑L\*a\*b\*色度测量 | 表面变亮、变黄 |
| 300 °C后出现表面裂纹，500 °C且多循环时裂纹加宽增多 | [Hu 2022, pp. 3-5] | Supereye B007显微观察 | 温度与循环次数共同促进裂纹 |
| 热导率随温度升高而降低，随循环次数增加而降低 | [Hu 2022, pp. 5-6] | 长圆柱试样，Xiangke DRE‑2C测试 | 内部结构劣化导致 |
| P波速度随温度升高和循环次数增加均下降 | [Hu 2022, pp. 5-6] | RSM‑SY5波速检测仪 | 裂纹增加降低波速 |
| 抗拉强度在100‑200 °C略有上升后快速下降，500 °C时5次循环降幅达50.56% | [Hu 2022, pp. 5-6] | WAW‑1000D试验机，巴西劈裂 | 两阶段行为，热冲击影响显著 |
| 相同加热时间，循环次数越多中心温度越低；无循环时温度随边界温度升高而升高，经历循环后500 °C反而下降 | [Hu 2022, pp. 6-9] | COMSOL模拟，加热5 min与10 min | 热传导效率因损伤降低 |
| 热导率与P波速度的线性拟合：λ=0.36189Vp+0.9059，R²=0.9269 | [Hu 2022, pp. 9-10] | 长圆柱试样，实测数据回归 | 适用范围：Vp=1.75‑5.13 km/s，λ=1.36‑2.99 W/m·K |
| 抗拉强度与P波速度线性关系：σ=1.1547Vp+1.0567，R²=0.8738 | [Hu 2022, pp. 9-10] | 短圆柱试样，巴西劈裂数据 | 同一适用范围 |
| 方解石轴向膨胀、径向压缩导致晶间裂纹，热冲击加剧破坏 | [Hu 2022, pp. 10-12] | 引用Winkler (1994) 方解石热膨胀数据 | 损伤机理阐释 |

## Limitations
- 线性回归关系仅适用于限定的P波速度（1.75–5.13 km/s）和热导率（1.36–2.99 W/m·K）范围，外推需验证。
- 实验温度最高500 °C，循环次数最多5次，结果不能直接推广至更高温度或更长时间的热冲击疲劳。
- 试样为单一产地的致密石灰岩，未考虑岩石非均质性、天然裂隙或不同矿物组分的影响。
- 数值模拟仅考虑固体传热，未耦合渗流、力学变形和化学反应（THMC）等多场效应。
- 未进行微观结构（如SEM）或矿物相变化的直接观测，损伤机制基于现有热膨胀数据推断。

## Assumptions / Conditions
- 试样从同一块石灰岩沿同一方向钻取，以消除各向异性影响。
- 所有试样的初始状态无可见裂纹，假设均匀连续。
- 热冲击冷却是将高温试样直接浸入室温（约25 °C）水中快速冷却，模拟地热井注水过程。
- 热处理后试样在50 °C干燥箱中烘干24 h，确保水分影响降至最低。
- 数值模拟的初始内部温度设为25 °C，边界温度恒定，不考虑冷却水流动与相变。
- 损伤因子定义采用P波速度的平方比，假设初始状态为无损伤。

## Key Variables / Parameters
- 热处理温度：100、200、300、400、500 °C
- 冷热循环次数：0（仅高温）、1、2、3、4、5
- 表面色度：L\*（亮度）、a\*、b\*值
- P波速度（km/s）
- 热导率（W/m·K）
- 抗拉强度σ（MPa）
- 损伤因子：D\_T = 1 − (V\_PT/V\_P0)²，D\_L = 1 − (V\_PL/V\_P0)²
- 内部温度（数值模拟中心点温度）
- 加热时间：5 min、10 min、30 min等
- 方解石热膨胀系数（轴向c、径向b，数据源自Winkler, 1994）

## Reusable Claims
- **Claim 1**：石灰岩在多次冷热循环后，热导率随温度升高单调下降，且循环次数增加会进一步降低热导率。条件：加热温度100–500 °C，快速水冷，干燥后测量。限制：未考虑更高温度或长期循环。
- **Claim 2**：P波速度可用于间接评估石灰岩的热导率和抗拉强度，三者之间存在强线性关系（λ=0.36189 Vp+0.9059，R²=0.9269；σ=1.1547 Vp+1.0567，R²=0.8738），但适用区间为Vp=1.75–5.13 km/s、λ=1.36–2.99 W/m·K。
- **Claim 3**：石灰岩抗拉强度在100–200 °C范围内因微裂纹闭合而略有增加，此后随温度升高和循环次数增加快速下降，500 °C时5次循环强度损失可达50%以上。
- **Claim 4**：多次热冲击显著降低石灰岩的内部传热能力，相同加热条件下中心点温度随循环次数增加而降低，且500 °C时无热冲击试样的中心温度高于经循环试样。
- **Claim 5**：方解石晶体的各向异性热膨胀（轴向拉伸、径向收缩）是导致石灰岩热损伤的关键机理，循环热冲击通过反复扩张与收缩加剧晶间裂纹的萌生与扩展。

## Candidate Concepts
- [[thermal shock damage（热冲击损伤）]]
- [[damage factor based on P-wave velocity（基于P波速度的损伤因子）]]
- [[calcite thermal expansion（方解石热膨胀）]]
- [[geothermal carbonate reservoir（地热碳酸盐岩储层）]]
- [[hot dry rock (HDR)（干热岩）]]
- [[thermal shock fatigue（热冲击疲劳）]]
- [[heat transfer degradation（传热性能劣化）]]
- [[Winkler热膨胀数据]]
- [[CIE-L*a*b* color system（CIE‑L\*a\*b\*颜色体系）]]

## Candidate Methods
- [[thermal shock cycle treatment (heating + rapid water cooling)（热冲击循环处理：加热+水中快冷）]]
- [[P-wave velocity measurement（P波速度测量）]]
- [[DRE-2C thermal conductivity tester（DRE‑2C热导率测试仪）]]
- [[Brazilian tensile strength test（巴西劈裂抗拉强度测试）]]
- [[COMSOL Multiphysics solid heat transfer simulation（COMSOL固体传热模拟）]]
- [[microscopic crack observation with Supereye B007（Supereye B007显微裂纹观察）]]
- [[chromaticity analysis using CIE-L*a*b*（CIE‑L\*a\*b\*色度分析）]]

## Connections To Other Work
- **花岗岩与碱性花岗岩的循环热冲击**：Hu et al. (2021) 研究了碱性花岗岩在循环冷热后热物性的变化；Sun & Hu (2019) 探讨了快速冷却对花岗岩热扩散系数的影响。本文针对石灰岩进行类似研究，弥补了碳酸盐岩储层的空缺。
- **多次加热‑水冷循环对花岗岩的影响**：Yin et al. (2021) 发现了循环次数对花岗岩物理力学响应的作用，本研究中石灰岩亦表现出相似的劣化趋势，但损伤机理侧重于方解石热膨胀。
- **高温后岩石声波与力学性质**：Ge & Sun (2021)、Hu et al. (2018)、Liu & Xu (2013) 等分别研究了微波加热后辉长岩、高温后花岗岩和大理岩的力学与波速特征，本文的P波速度‑强度线性关系与此类研究一致。
- **碳酸盐岩地热储层渗透率变化**：Pandey et al. (2014) 通过THC模型预测热提取导致的裂缝渗透率变化，本文的热传导与裂纹扩展结果可为THMC耦合模型的构建提供参数。

## Open Questions
- 石灰岩在更高温度（>500 °C）和更多循环次数（>5）下的损伤演化规律尚未探明。
- 多场耦合（热‑水‑力‑化学）条件下热冲击石灰岩的渗流‑传热‑损伤相互作用机制需进一步研究。
- 方解石晶体微裂纹的定量表征与热膨胀参数的直接测量有助于验证损伤模型。
- 本文得到的线性经验公式能否适用于其他类型石灰岩或现场尺度的地层仍需验证。

## Source Coverage
本页面严格依据全部8个非空索引片段（indexed texts: 8, nonempty source blocks: 8）编写，未引入外部信息。所有片段均已被使用并编译，最终编译字符数36027，覆盖索引字符数39273，块覆盖率100%，字符覆盖率约91.7%（coverage_ratio_by_blocks: 1.0, coverage_ratio_by_chars: 0.917348）。覆盖状态为 full‑index，采用单遍 markdown 编译策略。
