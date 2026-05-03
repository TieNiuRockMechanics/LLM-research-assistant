---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit"
title: "Effects of High Temperature and Thermal Cycles on Fracture Surface's Roughness of Granite: An Insight on 3D Morphology."
status: "draft"
source_pdf: "data/papers/2025 - Effects of high temperature and thermal cycles on fracture surface's roughness of granite An insight on 3D morphology.pdf"
collections:
  - "zotero new"
citation: "Gu, Qixiong, et al. \"Effects of High Temperature and Thermal Cycles on Fracture Surface's Roughness of Granite: An Insight on 3D Morphology.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 810-26. doi:10.1016/j.jrmge.2024.04.025."
indexed_texts: "13"
indexed_chars: "62290"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62547"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004126"
coverage_status: "full-index"
source_signature: "b1cad2aa6fe5d6c6a4ad88bb2489bec4a6c2df55"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:20:24"
---

# Effects of High Temperature and Thermal Cycles on Fracture Surface's Roughness of Granite: An Insight on 3D Morphology.

## One-line Summary
高温与热循环通过矿物不均匀膨胀、脱水、氧化和石英相变等机制显著增大花岗岩断裂面粗糙度、各向异性及孔径，且粗糙度参数随温度呈Boltzmann分布，分形维数线性下降；热循环加剧损伤积累，在500 °C以上尤其明显。[Gu 2025, pp. 1-2, 16‑17]

## Research Question
高温和热循环如何影响花岗岩断裂面的三维形态粗糙度？具体包括：不同温度（25 °C～800 °C）和循环次数（1次和5次）下，粗糙度参数（JRC、三维高度、倾角、面积参数、分形维数）的变化规律、各向异性特征、断裂面孔径分布及其微观损伤机制。[Gu 2025, pp. 1-3, 16‑17]

## Study Area / Data
- **研究对象**：甘肃北山花岗岩，主要矿物成分为斜长石（32.44%）、石英（31.27%）、微斜长石（27.83%）、黑云母（8.46%）。[Gu 2025, pp. 2-3]
- **温度梯度**：25 °C、200 °C、300 °C、400 °C、500 °C、600 °C、700 °C、800 °C，加热速率8 °C/min，恒温2 h。[Gu 2025, pp. 3-5]
- **热循环**：最高循环5次；实验表明花岗岩物理力学性能劣化多发生在5次循环以内，因此本研究设定最大循环5次。[Gu 2025, pp. 3-5]
- **试样尺寸**：标准圆盘，ϕ25 mm × 50 mm，表面平整度误差≤±0.05 mm（满足ISRM建议）。[Gu 2025, pp. 3-5]

## Methods
1. **热处理与断裂面制备**  
   花岗岩试样按上述温度方案加热并冷却后，进行巴西劈裂试验（RMT‑150C试验机），获得上、下两个断裂面。[Gu 2025, pp. 3-5]

2. **三维形态采集**  
   使用Tianyuan FreeScan X5三维扫描仪获取断裂面点云，经Geomagic Control去噪、Surfer软件通过Kriging插值生成网格文件（采样间隔0.1 mm）。[Gu 2025, pp. 3-5]

3. **粗糙度量化**  
   - **JRC**：采用Tse和Cruden（1979）提出的经验公式JRC = 32.2 + 32.47 log₁₀ Z₂，其中Z₂为轮廓线一阶导数均方根。[Gu 2025, pp. 5-6]  
   - **三维粗糙度参数**：利用FSAT工具箱（Heinze et al., 2021）和自编MATLAB程序，以最小二乘面为参考面，计算高度参数（Sz, Z₂s）、倾角参数（θₛ, θ*ₘₐₓ/(C+1)）和面积参数（Rₛ, Tₛ）。[Gu 2025, pp. 5-8]  
   - **分形维数D**：采用结构函数法，利用关系式S(h) = ⟨[Z(x+h)-Z(x)]²⟩ = C h⁴⁻²ᴰ，通过log‑log线性拟合斜率计算D。[Gu 2025, pp. 8-13]  
   - **各向异性指数Iₚ**：基于不同方位角的粗糙度参数（JRC、Sz、D），按公式Iₚ=√[1/n Σ(pᵢ‑p̄)²]计算，Iₚ=0为各向同性，>0为各向异性。[Gu 2025, pp. 13-13]  
   - **断裂面孔径**：上下表面在闭合状态下，计算高程差，统计孔径分布并进行高斯函数拟合。[Gu 2025, pp. 13-16]

4. **微观机制分析**  
   - SEM：观察热处理前后矿物颗粒边界、微裂纹发育。  
   - XRD：分析矿物组成及其衍射强度变化，判断晶体结构改变。  
   - TG‑DTA：分析加热过程中的质量与热效应变化，识别脱水、相变等反应。[Gu 2025, pp. 13-16]

## Key Findings
1. **粗糙度参数的温度依赖性**  
   JRC、Sz、Z₂s、θₛ、θ*ₘₐₓ/(C+1)、Rₛ和Tₛ均随温度升高而增大，且在500 °C以下波动，500 °C以上急剧上升，变化规律符合Boltzmann函数分布。分形维数D则随温度线性下降，表明温度越高断裂面越粗糙。[Gu 2025, pp. 5-13, 16‑17]

2. **热循环的影响**  
   5次热循环后，所有粗糙度参数均较单次循环进一步增大，尤其在500 °C以上增幅显著，显示热循环对损伤的累积效应。当温度高于700 °C后，粗糙度增幅趋缓，因岩石已产生严重热损伤并形成较大孔隙空间，适应了热变形。[Gu 2025, pp. 5-13, 16‑17]

3. **各向异性特征**  
   断裂面粗糙度呈现明显的各向异性，温度越高、循环次数越多，各向异性越强。JRC、Sz较高的方向主要集中在20°～40°、60°～100°和140°～160°范围内。基于JRC和Sz计算的各向异性指数IJRC和ISz随温度波动上升，而基于D的指数变化不典型。[Gu 2025, pp. 13-13]

4. **断裂面孔径分布**  
   闭合状态下的孔径分布符合高斯函数，平均孔径随温度升高而增大（25 °C时0.665 mm→800 °C时1.058 mm），分布范围由0～0.6 mm扩大至0～3 mm，5次循环后进一步扩大至0～6.4 mm。高温和热循环使接触面积分散，优先流通道增多。[Gu 2025, pp. 13-16]

5. **微观损伤机理**  
   - 200 °C以下：自由水蒸发；200～300 °C：结合水、结晶水和部分结构水逃逸；300～500 °C：质量稳定，热应力较小；500 °C以上：结构水完全丧失，石英在约573 °C发生α→β相变，体积急剧膨胀，导致大量晶间与穿晶裂纹产生并连通。[Gu 2025, pp. 13-16]  
   - 热循环引起矿物交替膨胀与收缩，产生疲劳效应，使微裂纹不断萌生、扩展、加深，矿物颗粒脱落，形成剥离缺陷（700 °C时裂纹最大宽度达116.89 μm，800 °C后达68.54 μm），从而进一步增加粗糙度、各向异性和孔径。[Gu 2025, pp. 16-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| JRC与Z₂均随温度上升，500 °C以上急剧增大，满足Boltzmann函数拟合（R²>0.89） | [Gu 2025, pp. 5-6] | 25 °C‑800 °C，循环1次与5次 | JRC个别值超过20，提示Barton模型需改进 |
| 三维高度参数Sz、Z₂s随温度及循环次数增加，拟合Boltzmann函数（R²>0.79） | [Gu 2025, pp. 5-6] | 同上 | 500 °C‑600 °C跃升，600 °C后趋稳 |
| 倾角参数θₛ、θ*ₘₐₓ/(C+1)变化规律与高度参数一致，Boltzmann拟合R²>0.96 | [Gu 2025, pp. 6-8] | 同上 | 700 °C后增幅减小 |
| 面积参数Rₛ、Tₛ亦随温度、循环次数增大，Boltzmann拟合R²>0.963 | [Gu 2025, pp. 8-13] | 同上 | 500 °C后剧增，之后平衡 |
| 分形维数D随温度线性下降（结构函数法），5次循环后D更低 | [Gu 2025, pp. 8-13] | 同上 | 线性拟合R²>0.927 |
| 各向异性指数IJRC、ISz随温度波动上升，方向性显著（20°‑40°, 60°‑100°, 140°‑160°） | [Gu 2025, pp. 13-13] | 所有温度及循环 | ID变化不典型 |
| 断裂面孔径分布符合高斯分布，平均孔径从25 °C的0.665 mm增至800 °C的1.058 mm | [Gu 2025, pp. 13-16] | 闭合状态 | 5次循环后800 °C时达1.516 mm |
| XRD显示矿物组成不变，但500‑600 °C石英、黑云母、斜长石衍射强度突变 | [Gu 2025, pp. 13-16] | 不同温度与循环 | 循环后石英衍射强度下降，其他矿物波动增大 |
| TG曲线在200‑300 °C、500‑600 °C快速下降，DTA在573 °C出现吸热峰 | [Gu 2025, pp. 13-16] | 升温过程 | 对应脱水与石英相变 |
| SEM显示500 °C以下裂纹少且小，600 °C以上晶间与穿晶裂纹贯通成网，800 °C矿物碎裂脱落 | [Gu 2025, pp. 16-16] | 不同温度 | 热循环后剥离缺陷加剧（700 °C宽116.89 μm） |

## Limitations
1. 仅针对北山花岗岩一种岩性，结论向其他岩类的推广性未验证。[Gu 2025, pp. 2-3]
2. 最高温度800 °C，未涉及更高温条件下的行为。[Gu 2025, pp. 3-5]
3. 热循环仅5次，更长周期的影响未涉及；加热速率、恒温时间固定，未探讨不同加热制度的影响。[Gu 2025, pp. 3-5]
4. 断裂面通过巴西劈裂试验获得，与天然裂隙面的粗糙度特征可能存在差异。[Gu 2025, pp. 3-5]
5. 三维扫描采样间隔0.1 mm，可能平滑了更细观的结构信息。[Gu 2025, pp. 3-5]
6. 文中未提供采用自然冷却、水冷还是液氮冷却的明确说明，冷却方式对结果的影响未单独讨论。[Gu 2025, pp. 3-5，表1仅作为总结，未指明本试验所用冷却方式]

## Assumptions / Conditions
- **加热方案**：基于前人研究，选用25 °C~800 °C温度梯度和最大5次循环，加热速率8 °C/min，恒温2 h，以确保内外均匀加热。目前尚无统一的岩石热处理标准，该选择参照常见做法。[Gu 2025, pp. 3-5]
- **参考面选取**：因巴西劈裂产生的上下断裂面起伏差异较大，采用最小二乘拟合面作为基准面计算粗糙度参数。[Gu 2025, pp. 5-6]
- **粗糙度参数适用性**：JRC沿用Tse & Cruden（1979）经验公式，适用于本批花岗岩；当JRC>20时，Barton原始10条标准曲线的适用性值得商榷。[Gu 2025, pp. 5-6]
- **各向异性评价**：各向异性指数Iₚ基于所有方位角粗糙度参数的标准差计算，假定涵盖充分的方向信息。[Gu 2025, pp. 13-13]
- **孔径分析**：孔径定义为闭合状态下上下表面高程差，并假设分布服从高斯函数进行拟合。[Gu 2025, pp. 13-16]
- **微观测试**：XRD、TG‑DTA和SEM的观测结果代表取样点的特征，假定其能反映整体损伤趋势。[Gu 2025, pp. 13-16]

## Key Variables / Parameters
- **独立变量**：温度（25 °C, 200 °C, 300 °C, 400 °C, 500 °C, 600 °C, 700 °C, 800 °C）、热循环次数（1, 5）。
- **粗糙度响应变量**：
  - JRC（基于Z₂计算）。
  - 三维高度参数：总高度Sz，表面坡度均方根Z₂s。
  - 三维倾角参数：表面角度θₛ，表面粗糙度参数θ*ₘₐₓ/(C+1)。
  - 三维面积参数：表面粗糙度系数Rₛ，表面迂曲度系数Tₛ。
  - 分形维数D（结构函数法）。
- **各向异性参数**：基于JRC、Sz、D的各向异性指数IJRC、ISz、ID。
- **孔径参数**：平均孔径、孔径分布范围、高斯拟合参数（y₀, A, u, xc）。
- **材料物性参数**：矿物组成（XRD），热量‑质量变化（TG-DTA），微观形貌（SEM）。

## Reusable Claims
1. **适用于北山花岗岩在25 °C~800 °C、最多5次循环条件下：**
   - 断裂面粗糙度（JRC、三维高度、倾角、面积参数）随温度和循环次数增加而增大，变化规律可用Boltzmann函数描述。[Gu 2025, pp. 5-13, 16‑17]
   - 分形维数D随温度线性减小，可作为热损伤致粗糙化程度的指标。[Gu 2025, pp. 8-13, 16‑17]
   - 断裂面各向异性随温度升高增强，粗糙度较大方向集中在20°‑40°、60°‑100°和140°‑160°。[Gu 2025, pp. 13-13]
   - 闭合态断裂面孔径服从高斯分布，平均孔径从0.665 mm（25 °C）升至1.058 mm（800 °C），5次循环后升至1.516 mm。[Gu 2025, pp. 13-16]
2. **损伤机制通用描述（以本花岗岩为例）：**
   - 500 °C以下的损伤主要源于矿物不均匀膨胀、水分蒸发；500 °C以上石英α→β相变（~573 °C）引起的体积剧变是粗糙度陡增的主导因素。[Gu 2025, pp. 13-16]
   - 热循环通过交替热应力造成矿物颗粒的疲劳损伤，促进微裂纹扩展、贯通以及颗粒脱落，进一步增大粗糙度和孔径。[Gu 2025, pp. 16-16]
3. **方法学提示：**
   - 当JRC超过20时，需谨慎使用Barton标准曲线，建议基于三维参数综合评定。[Gu 2025, pp. 5-6]
   - 结构函数法计算分形维数在此类热损伤研究中表现稳定，线性拟合优度较高。[Gu 2025, pp. 8-13]
   - 多方位角粗糙度参数用于计算各向异性指数，能综合反映表面方向性差异，尤其JRC和Sz对应的指数更具灵敏度。[Gu 2025, pp. 13-13]

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[3D roughness parameters]]
- [[fractal dimension of rock fracture surface]]
- [[anisotropy index of roughness]]
- [[fracture aperture distribution]]
- [[thermal damage of granite]]
- [[quartz α-β phase transition]]
- [[intergranular and transgranular cracks]]
- [[fatigue damage by thermal cycles]]
- [[Boltzmann function fitting for roughness]]
- [[Gaussian distribution of aperture]]
- [[Brazilian splitting test for fracture surfaces]]

## Candidate Methods
- [[Tse and Cruden empirical JRC formula]]
- [[FSAT toolbox (Heinze et al.)]]
- [[structure function method for fractal dimension]]
- [[Kriging interpolation for surface reconstruction]]
- [[Gaussian fitting for fracture aperture]]
- [[SEM observation of thermally induced cracks]]
- [[XRD analysis of mineral crystallinity change]]
- [[TG-DTA for dehydration and phase transition identification]]
- [[3D laser scanning and point cloud processing]]
- [[anisotropy degree index (Ip)]]

## Connections To Other Work
- **粗糙度评价方法**：文中系统回顾了标准轮廓线法（Barton, 1973）、JRC（Barton & Choubey, 1977）、统计参数法（Tse & Cruden, 1979）、分形几何法（Xie et al., 1999）、综合参数法（Jiang et al., 2006）和三维形态描述法（Belem et al., 2000；Grasselli et al., 2002），并指出各方法局限性。[Gu 2025, pp. 2-2]
- **温度与循环对断裂面粗糙度的影响**：前人研究已表明花岗岩（Tang & Zhang, 2020; Wu et al., 2019）和砂岩（Ge et al., 2020; Dong et al., 2019）的粗糙度随温度和循环次数增加而增大，本文系统性验证并补充了三维参数和分形维数的演化规律。[Gu 2025, pp. 2-3]
- **热损伤机理**：与广泛认可的不均匀膨胀、矿物反应（David et al., 2012; Fan et al., 2017; Shen et al., 2023; Zhang et al., 2023）一致，本研究进一步通过XRD、TG‑DTA和SEM揭示了加热过程中水分逃逸与石英相变的关键作用。[Gu 2025, pp. 2-3, 13‑16]
- **JRC模型改进需求**：观测到JRC>20的现象，呼应了对Barton原始曲线的改进诉求。[Gu 2025, pp. 5-6]

## Open Questions
1. 本研究中JRC部分值超过20，Barton标准轮廓曲线无法涵盖，未来应如何建立高粗糙度花岗岩裂隙的JRC评定修正模型？[Gu 2025, pp. 5-6]
2. 热循环次数仅限5次，更长期循环（>100次）下的粗糙度演化是否会出现饱和或不同的损伤模式？[基于实验范围推断，未在文中直接讨论]
3. 不同冷却方式（自然冷却、水冷、液氮冷）对本试验结果的影响未被量化，后续可进行对照试验，区分热冲击与纯热循环的贡献。[Gu 2025, pp. 3-5，统计表提及多种冷却方式但本文未详细说明]
4. 石英相变导致的体积膨胀对粗糙度的定量贡献如何与其他矿物作用解耦？[Gu 2025, pp. 13-16]
5. 本试验为巴西劈裂导致的人工断裂面，自然裂隙面在相同热‑循环条件下的粗糙度响应是否一致？[Gu 2025, pp. 3-5]
6. 高温下花岗岩断裂面孔隙‑裂隙网络的空间连通性如何影响宏观渗透率？本文仅分析了静止状态下的孔径分布，未涉及渗流试验。[Gu 2025, pp. 13-16]

## Source Coverage
本文所有非空索引片段（共13个片段，62,290个字符）均已处理并纳入上述内容。编译后总字符数62,547，片段字符覆盖率100%，整体字符利用率约100.41%（因格式标记导致编译字符稍多）。片段来源于[Gu 2025]论文全文索引，无省略。
