---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-voorn-porosity-permeability-and-3d-fracture-network-characterisation-of-dolomite-reservoir"
title: "Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples."
status: "draft"
source_pdf: "data/papers/2015 - Porosity, permeability and 3D fracture network characterisation of dolomite reservoir rock samples.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Voorn, Maarten, et al. \"Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples.\" *Journal of Petroleum Science and Engineering*, 2014, doi:10.1016/j.petrol.2014.12.019. Accessed 1 Jan. 2026."
indexed_texts: "19"
indexed_chars: "92032"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "92454"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004585"
coverage_status: "full-index"
source_signature: "d56c383131576784b058aab87d91e6810c0efa66"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:59:57"
---

# Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples.

## One-line Summary
本文探索使用非破坏性3D X射线显微CT（μCT）结合薄片分析和围压下的渗透率测量，对奥地利维也纳盆地Hauptdolomit组白云岩储层岩石样本的孔隙度、渗透率和3D裂缝网络进行综合表征，重点利用多尺度Hessian裂缝滤波（MSHFF）提取窄裂缝参数。

## Research Question
如何高效分析致密白云岩中的天然裂缝网络，并利用3D μCT成像、2D薄片分析和实验室渗透率测定等方法，从损伤带到断层核的不同断层岩样本中获取孔隙度、裂缝开度、裂缝密度和裂缝方位等参数？

## Study Area / Data
- **地点**：奥地利维也纳盆地（Vienna Basin）前新近纪基底，取自井眼钻心的上三叠统（诺利阶）Hauptdolomit组白云岩。该区从20世纪60年代起进行天然气勘探与生产。  
- **样本**：7个柱塞尺寸（直径2–3 cm）样本，取自密集裂缝的白云岩，涵盖根据野外工作解释的断层带结构：损伤带（仅裂缝）、裂缝+角砾岩过渡、镶嵌角砾岩、以及初成–中成碎裂岩（断层核）。样本具体信息见Table 1，深度范围2795–3320 m。白云石结构以亚自形至自形为主，含方解石、黄铁矿脉及孔隙充填物，粘土（伊利石、高岭石）含量在不同部位有差异 [Voorn 2014, pp. 2-3, 3-3]。  
- **断层带分类概念**：远离主断层的未损伤岩石 → 裂缝密度增加，出现多向裂缝且间距<1 cm → 镶嵌角砾岩带（部分方解石胶结）→ 断层核部的碎裂岩（基质含量逐渐增加）。此分类基于岩心推断，存在解释性 [Voorn 2014, pp. 2-3]。

## Methods
- **3D X射线显微CT（μCT）**：使用Rayscan 250E扫描仪，X射线源225 kV微焦点，铜预滤波，分辨率(12.5–20 µm)³/体素。扫描后通过滤波反投影重建3D体积。为减少噪声，每个投影平均4–5次，不使用中值滤波等额外滤波 [Voorn 2014, pp. 3-3]。  
- **图像处理与分割**：应用多尺度Hessian裂缝滤波（MSHFF，基于Voorn et al., 2013），对不同高斯尺度结果加权组合以增强最窄特征。滤波后采用全局阈值二值化，再用27-连接岛屿滤波移除<20体素的噪声。由此获得二值分割的裂缝/孔隙体 [Voorn 2014, pp. 3-5]。  
- **孔隙度**：二值数据中孔隙体素与总体素数之比，归一化到100%。此值依赖于数据质量、分辨率和处理选择，可能部分反映操作员选择 [Voorn 2014, pp. 5-6]。  
- **裂缝开度**：使用FIJI的Local Thickness插件，在分割后的孔隙空间中拟合最大内切球，球直径代表局部开度。分布经体积加权校正后乘以扫描分辨率，以直方图显示。受μCT分辨率限制，小开度检测不足 [Voorn 2014, pp. 5-6]。  
- **裂缝密度**：采用体定义：裂缝密度 (m⁻¹) = 总裂缝表面积 (m²) / 样本体积 (m³)。由开度分布导出：每个开度类的体积除以该开度（体素边长）得到表面积，再求和。转换后用于相对比较 [Voorn 2014, pp. 6-6]。  
- **裂缝方位**：在二值数据上重新计算Hessian矩阵，取每个孔隙体素对应最大Hessian本征值的本征向量（裂缝面法向），在MATLAB中绘制极点密度图（归一化相对最大值），使较大裂缝自动权重更高 [Voorn 2014, pp. 6-6]。  
- **薄片分析**：从μCT扫描后的柱塞上制作2D薄片，SEM‑BSE图像经全局亮度/对比度校正后自动或手动拼接（分辨率约(1.1–1.7 µm)²/像素）。用Otsu全局阈值分割，比较微米级孔隙和结构细节。薄片显示裂缝开度通常小于μCT结果，尤其在窄裂缝处因部分体积效应影响 [Voorn 2014, pp. 6-6]。  
- **渗透率实验**：
  - 气体渗透率（部分2 cm直径样本）：室温下以氮气为孔隙流体，蒸馏水为围压介质。下游压力固定为大气压，上游最大0.5 MPa变流量，依据Darcy定律（压缩气体）计算视渗透率，再经Klinkenberg或Forchheimer校正获取固有渗透率。围压视为有效围压（孔隙压力较低）。3 cm直径样本未做围压实验，仅在常压下测氮气渗透率（无校正，可能有±25%误差）[Voorn 2014, pp. 6-8]。  
  - 水渗透率（3 cm直径样本）：以自来水为孔隙流体，Multitherm PG‑1s油为围压介质。轴向压力和径向压力分别控制，使用差分压力传感器，以Darcy线性形式计算。测试了轴向/径向压力、流反转和时间停流的影响，确认径向压力为主导，流反转无显著影响，无显著时间依赖性 [Voorn 2014, pp. 8-10]。  
  - 加载/卸载路径：对一个含单裂缝样本（Schönkirchen T32-430）进行了加载‑卸载循环，观察渗透率滞后行为 [Voorn 2014, pp. 12-14]。  
- **渗透率实验前后μCT对比**：对样本Prottes TS1-4p进行实验前/后扫描并3D刚性配准，目视检验无明显差异，表明渗透率下降来自亚分辨率尺度的变化 [Voorn 2014, pp. 14-14]。  
- **统计裂纹模型尝试**：应用Gueguen & Dienes (1989)的各向同性圆柱形裂纹模型，利用几何平均开度、孔隙度和连通分数f=1，结果高估达3-5个数量级，可能因各向异性、变量非独立及基质连通性影响，建议使用基于真实图像的有限元或格子玻尔兹曼模拟 [Voorn 2014, pp. 14-15]。

## Key Findings
1. **μCT提取能力**：利用MSHFF能成功从柱塞级裂缝白云岩中提取体孔隙度、裂缝开度分布、裂缝密度和裂缝方位（极图），流程可部分自动化 [Voorn 2014, pp. 14-15]。  
2. **断层带差异**：不同断层岩类型的μCT特征和渗透行为有明显差异。
   - 损伤带裂缝样本：中等孔隙度和渗透率，具有一至两个优势裂缝方位，裂缝密度中到高。
   - 角砾岩/过渡样本：最高孔隙度和渗透率，裂缝方位分散，裂缝密度高，孔径分布最宽（如Schönkirchen T91‑5p）。
   - 碎裂岩样本：最低孔隙度和渗透率，裂缝密度较低，无优势方位 [Voorn 2014, pp. 10-11; 12-12]。  
3. **多尺度孔隙度对比**：μCT孔隙度（0.9–4.2%）< 实验室孔隙度（He法3.8–9.7%，水饱和法更高）< 薄片孔隙度（4.2–14.1%）。μCT只能捕捉大于分辨率的裂缝和大孔，实验室可测连通孔隙（含部分微孔），薄片包含非连通微孔 [Voorn 2014, pp. 11-11]。  
4. **开度特征**：样本Schönkirchen T91‑5p（裂缝+角砾岩）具有最大开口孔径，2 cm直径样本的系统开度分布小于3 cm的同类样本，归因于μCT分辨率和模糊效应，因此建议同类研究使用相同尺寸样本 [Voorn 2014, pp. 11-12]。  
5. **渗透率–围压关系**：所有样品渗透率随围压增加而降低，大部分降幅发生在20 MPa以下（气体实验范围更大）。角砾岩样品渗透率下降最平缓，损伤带裂缝样品下降最快，碎裂岩最低。碎裂岩水渗透实验可能受非稳态效应影响，使结果可信度较低 [Voorn 2014, pp. 12-12]。  
6. **渗透率滞后**：加载‑卸载路径有显著滞后，卸载后渗透率低于初始值。即使未超过前置最大压力，额外渗透率损失也可发生。因此实验室测得的渗透率只是相对近似，难以直接代表原始储层条件 [Voorn 2014, pp. 12-14]。  
7. **实验前后μCT无可见变化**：压‑流实验后的μCT配准图像几乎无差异，指示渗透率衰减来自亚体素的开度变化或微小闭合，需更高分辨率或原位实验检测 [Voorn 2014, pp. 14-14]。  
8. **简易渗透率模型失败**：Gueguen–Dienes统计模型高估渗透率3–5个数量级，即使降低f、使用较小的几何平均开度和低孔隙度，偏差仍大；说明复杂裂缝网络需借助数值模拟 [Voorn 2014, pp. 14-15]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| μCT分割孔隙度范围0.9–4.2% | Table 2, Fig. 7d | 分辨率12.5–20 µm³/voxel | 实验室孔隙度3.8–9.7%，薄片4.2–14.1% |
| 裂缝密度202–481 m⁻¹，与μCT孔隙度比值不恒定 | Table 2, Fig. 7e | 裂缝密度定义：总裂缝表面积/体积 | 主要薄裂缝样本的密度/孔隙度比值更高 |
| 开度分布显示Schönkirchen T91‑5p（角砾+裂隙）明显左偏宽分布，2 cm样本整体开度小于3 cm | Fig. 8 | 局部厚度法，体积加权 | 建议固定样本尺寸 |
| 裂缝方位：损伤带样本有清晰极密（图左侧两例），角砾岩散乱，碎裂岩无优势 | Fig. 7f | 归一化相对最大值投影 | 体素对应面法向极点 |
| 渗透率–围压曲线：损伤带裂隙样本（方框）下降最陡；角砾岩（菱形）起始最高且平缓；碎裂岩（三角）最低 | Fig. 7g | 气体渗透（开放符号）或水渗透（封闭符号） | 星号代表非围压气体渗透（无校正） |
| 水渗透实验：轴对称下径向压力才是实际围压；流反向和停流没有显著影响 | Fig. 6 | 单一裂隙样本（Schönkirchen T32-430） | 揭示围压闭合为主控 |
| 卸载后渗透率不可逆降低（滞后），即使未超过历史最大压力 | Fig. 10 | 同一样本，水渗透，加载-卸载路径 | 可能与微凸体破坏或剪切位移有关 |
| 压‑流实验前后μCT配准图像无可见差异 | Fig. 11 | 样本Prottes TS1‑4p，15 µm³分辨率 | 渗透率下降源于亚分辨率变化 |
| 统计裂纹模型（Eq. 5.1–5.2）过估渗透率10³–10⁵倍 | Sections 5.7, Eq. 5.2 | 孔隙度、几何平均开度、f=1 | 建议采用FEM或Lattice Boltzmann |

## Limitations
- μCT分辨率不足，无法探测微孔隙和极窄裂缝，因此μCT得出的孔隙度常为最低值。  
- 样品筛选只能取不崩解的岩石，存在自然抽样偏差，且样本尺寸（直径2–3 cm）远未达到代表性基本体积（REV）。  
- 裂缝开度受部分体积效应影响而偏高，窄裂缝尤甚。  
- 裂缝方位缺少井眼参考方向，无法与井下数据直接对比。  
- 渗透率实验采用各向同性围压，未考虑真实储层应力各向异性；低渗透碎裂岩的水渗透实验可能受非稳态流影响，结果不确定。  
- 无法自动分离单一裂缝，因此不能可靠测定裂缝间距、长度或粗糙度。  
- 围压渗透率测量显示路径依赖，所得值仅为相对比较，不能直接等同原位渗透率。  
- 使用的统计裂纹模型过于简化，不适用于含复杂网络和基质贡献的样本。

## Assumptions / Conditions
- 基于钻井岩心推导的断层带分类（损伤带→断层核）带有解释性质，并非空间位置的确切证据。  
- 二值分割假设MSHFF结合全局阈值能有效分离裂缝孔隙与岩石基质，并移除绝大部分噪声。  
- 裂缝表面积计算假定每个开度类的总体素除以开度（球体直径）能等价于表面积，且球体完全重叠。  
- 渗透率测定基于Darcy流动假设成立；气体渗透率通过Klinkenberg（κ>10⁻¹⁵ m²）或Forchheimer校正；水渗透率采用线性Darcy公式。  
- 围压视为有效围压，因为孔隙流体压力远小于围压。  
- 统计裂纹模型假设各向同性、2D圆柱形裂纹，且变量（半开度、半径、间距）统计独立，所有裂纹对流动有贡献。

## Key Variables / Parameters
- μCT扫描分辨率（体素长度）  
- 多尺度Hessian参数（高斯尺度组合权重）  
- 分割全局阈值  
- 裂缝开度几何平均值  
- 裂缝密度（m⁻¹）  
- 裂缝极点方位密度图  
- 三种孔隙度值（实验室He/水饱和、μCT总孔隙度、薄片平均孔隙度）  
- 气体/水渗透率随有效围压的变化曲线  
- 有效围压  
- 断层岩岩相类别（损伤带、角砾过渡、断层核）  
- 矿物成分（白云石结构、方解石/黄铁矿脉、粘土分布）

## Reusable Claims
- 3D μCT配合多尺度Hessian滤波（MSHFF）可对裂缝性白云岩柱塞样本进行非破坏性、大部分自动化的结构参数提取。 [Voorn 2014, pp. 1-1, 3-1, 3-5]  
- μCT测定的裂缝开度因部分体积效应而偏高，且分辨率限制最小可测开度，因此在比较样本时建议统一尺寸。 [Voorn 2014, pp. 6-6, 11-12]  
- 断层带中损伤带裂缝样品的渗透率随围压下降幅度最大，角砾岩样品下降幅度最小，碎裂岩样品渗透率极低。 [Voorn 2014, pp. 12-12]  
- 渗透率存在显著的加载-卸载滞后，实验室围压实验所得值不能直接作为原位渗透率，但可用于相对比较。 [Voorn 2014, pp. 12-14]  
- 基于统计裂纹模型的解析解会严重高估此类岩石的渗透率，需采用真实图像导入的数值模拟。 [Voorn 2014, pp. 14-15]  
- μCT孔隙度远低于薄片和实验室法，可视为对渗透率起主导作用的宏观裂缝/大孔体系孔隙度。 [Voorn 2014, pp. 11-11]  
- 裂缝密度除以μCT孔隙度的比值可半定量反映裂缝开度特征：高比值代表以窄小裂隙为主。 [Voorn 2014, pp. 11-12, Table 2]

## Candidate Concepts
- [[Hessian-based fracture filtering (MSHFF)]]
- [[Fracture aperture distribution (local thickness)]]
- [[Fracture density (surface to volume ratio)]]
- [[Fracture orientation from Hessian eigenvectors]]
- [[Dolomite fault zone classification (damage zone, mosaic breccia, cataclasite)]]
- [[Porosity scale discrepancy (μCT vs lab vs thin section)]]
- [[Permeability reduction under confining pressure]]
- [[Loading-unloading permeability hysteresis]]
- [[Statistical crack model (Gueguen & Dienes, 1989)]]
- [[Klinkenberg and Forchheimer corrections]]

## Candidate Methods
- [[3D μCT imaging of narrow-fractured dolomite plugs]]
- [[Automated MSHFF segmentation with weighted scale averaging]]
- [[Local Thickness plugin for 3D aperture distribution]]
- [[Hessian eigenvector stereographic projection for fracture orientation]]
- [[Stitched SEM-BSE thin-section overviews with Otsu thresholding]]
- [[Gas permeability under confining pressure with Klinkenberg/Forchheimer correction]]
- [[Water permeability under controlled radial/axial pressure]]
- [[3D rigid registration of pre- and post-flow μCT scans]]

## Connections To Other Work
- 引用Nelson (2001)和Aguilera (1995)作为裂缝性储层分析框架，说明裂缝在储层评价中的重要性。  
- μCT应用参考文献包括Ketcham & Carlson (2001)、Cnudde et al. (2006)、Kaestner et al. (2008)等综述；裂缝提取方面列举了Keller (1998)、Montemagno & Pyrak‑Nolte (1999)、Zabler et al. (2008)、Watanabe et al. (2011)等。  
- 本研究核心处理流程基于Voorn et al. (2013)提出的多尺度Hessian裂缝滤波。  
- 薄片分割采用Otsu (1979)阈值法，SEM拼接自行开发或使用Microsoft ICE。  
- 渗透率计算公式与装置参考Heap et al. (2014)（气体装置）、Tanikawa & Shimamoto (2006)（Klinkenberg校正）等。  
- 加载‑卸载路径依赖行为类似Faulkner & Rutter (2000)、Selvadurai & Glowacki (2008)的观测。  
- 统计裂缝模型源自Gueguen & Dienes (1989)，文中也提到Hoyer et al. (2012)和Degruyter et al. (2010)的数值模拟工作。

## Open Questions
- 如何从密集交叉的裂缝网络中自动分离单条裂缝，以获取裂缝间距和长度？  
- 能否通过更高分辨率成像（如synchrotron CT）捕捉渗透率降低所对应的微米级结构变化？  
- 如何将柱塞尺度的裂缝参数上推到储层尺度，并确定符合REV要求的合理组合？  
- 若用真实储层应力场下的非各向同性加载替代各向同性围压，渗透率响应的差异有多大？  
- 碎裂岩样品中气体渗透率与水渗透率的明显差异（后者下降更剧烈）是真实物理还是实验假象？

## Source Coverage
- 所有提供的非空索引片段（共19个）均已被处理并用于构建此页面。  
- 索引字符数：92,032；源字符数：92,454；按块覆盖率1.0；按字符覆盖率1.004585；编译策略为 single‑pass‑markdown。
