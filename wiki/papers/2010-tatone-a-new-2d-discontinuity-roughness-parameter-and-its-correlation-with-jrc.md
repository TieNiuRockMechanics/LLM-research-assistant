---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
title: "A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC."
status: "draft"
source_pdf: "data/papers/2010 - A new 2D discontinuity roughness parameter and its correlation with JRC.pdf"
collections:
  - "zotero new"
citation: "Tatone, Bryan S. A., and Giovanni Grasselli. “A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC.” *International Journal of Rock Mechanics & Mining Sciences*, vol. 47, 2010, pp. 1391-1400. doi:10.1016/j.ijrmms.2010.06.006."
indexed_texts: "9"
indexed_chars: "40328"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "40534"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005108"
coverage_status: "full-index"
source_signature: "fa67197ca03da1ab7b10cde69cd6fc0e5eef97f3"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:53:21"
---

# A New 2D Discontinuity Roughness Parameter and Its Correlation with JRC.

## One-line Summary
本文提出了一种类比于三维粗糙度评价方法的二维不连续面粗糙度参数 \(y^*_{\max}/(C+1)_{\text{2D}}\)，建立了其与节理粗糙度系数(JRC)的经验关系（针对0.5 mm和1.0 mm采样间隔），并比较了二维伪三维粗糙度估计与真实三维粗糙度值。

## Research Question
1. 提出一种与先前三维方法类似的二维粗糙度评价方法。
2. 比较由二维方法得到的伪三维粗糙度估计与三维方法所得值的异同。
3. 建立新的二维参数 \(y^*_{\max}/(C+1)_{\text{2D}}\) 与常用的节理粗糙度系数(JRC)之间的经验关系，以辅助巴顿–班迪斯剪切强度准则的应用。[Tatone 2010, pp. 1-2]

## Study Area / Data
- **标准JRC剖面**：Barton和Choubey (1977)发表的10条标准粗糙度剖面，分别对应0.4至18.7的JRC值。[Tatone 2010, pp. 3-5]
- **石灰岩拉伸断裂面**：尺寸200 mm × 200 mm，用于比较二维与三维粗糙度值。[Tatone 2010, pp. 3-4]
- **数字化方法**：原版印刷图以1200 DPI扫描，在AutoCAD中缩放到实际尺寸，以0.5 mm间隔追踪剖面；重新对齐使最佳拟合直线水平。[Tatone 2010, pp. 5-6]
- 为确保数字化正确，将Z2和RP值与Tse and Cruden (1979)、Yu and Vayssade (1991)等已发表数据对比，结果吻合。[Tatone 2010, pp. 6-7]

## Methods
### 二维粗糙度评价方法
1. **剖面获取**：直接使用表面轮廓仪测量或从三角化不规则网格(TIN)表面模型中提取。[Tatone 2010, pp. 1-2]
2. **剖面对齐**：通过最佳拟合线性回归线（或最佳拟合平面）将剖面旋转至水平，使坐标轴沿剖面方向。[Tatone 2010, pp. 2-3]
3. **剖面分析**：指定分析方向（正向或反向），计算剖面各线段相对于该方向的倾角 \(y^*\)，确定超过递增倾角阈值的线段累积长度比，称为归一化长度 \(L_{y^*}\)。[Tatone 2010, pp. 2-3]
4. **二维粗糙度计算**：对 \(L_{y^*}\) 与 \(y^*\) 的累积分布用以下方程进行非线性最小二乘拟合，得二维参数 \(y^*_{\max}/(C+1)_{\text{2D}}\)：
   \[
   L_{y^*}=L_0\left(\frac{y^*_{\max}-y^*}{y^*_{\max}}\right)^C
   \]
   其中 \(L_0\) 为倾角大于0°的归一化长度，\(y^*_{\max}\) 为最大倾角，\(C\) 为无量纲拟合参数。[Tatone 2010, pp. 3-4]

### 与JRC相关的经验关系建立
- 对重对齐的标准JRC剖面以0.5 mm和1.0 mm间隔采样，分别计算正向与反向的 \(y^*_{\max}/(C+1)_{\text{2D}}\) 及平均值。
- 以幂函数形式拟合平均值与已知JRC的关系，获得公式(8)和(9)。[Tatone 2010, pp. 7-8]

## Key Findings
1. **二维与三维粗糙度对比**：在石灰岩断裂面上，所有分析方向上二维值均将对应三维值包围在内，二维平均值与三维值的偏差在1%~11%之间。[Tatone 2010, pp. 3-4]
2. **各向异性估计**：由二维平均值获得的伪三维粗糙度各向异性比（最大/最小粗糙度）与真实三维各向异性比相差小于7%，椭圆主轴方向差25°以内。[Tatone 2010, pp. 3-4]
3. **新的JRC经验方程**：对于0.5 mm和1.0 mm采样间隔，JRC可由平均 \(y^*_{\max}/(C+1)_{\text{2D}}\) 估计：
   - 0.5 mm间隔：\( \text{JRC} = 3.95\left(y^*_{\max}/(C+1)_{\text{2D}}\right)^{0.7} - 7.98 \) (8)
   - 1.0 mm间隔：\( \text{JRC} = 2.40\left(y^*_{\max}/(C+1)_{\text{2D}}\right)^{0.85} - 4.42 \) (9)
   [Tatone 2010, pp. 7-8]
4. **数字化验证**：重新计算的标准剖面的Z2和RP值与已发表数值高度一致，证明数字化程序可靠。[Tatone 2010, pp. 6-7]

## Core Evidence Table
| 证据 | 来源 | 条件/限制 | 注释 |
|------|------|-----------|------|
| 二维粗糙度平均值接近三维值，偏差≤11% | [Tatone 2010, pp. 3-4] | 石灰岩拉伸断裂，11条剖面，6个方向 | 所有方向的二维值均包围三维值 |
| 伪三维各向异性比与三维值相差＜7% | [Tatone 2010, pp. 3-4] | 同上表面 | 仅66条剖面，方向步长30° |
| 0.5 mm采样间隔下JRC方程(8) | [Tatone 2010, pp. 7-8] | 采样间隔0.5 mm，剖面已重新对齐 | 基于平均 \(y^*_{\max}/(C+1)_{\text{2D}}\) |
| 1.0 mm采样间隔下JRC方程(9) | [Tatone 2010, pp. 7-8] | 采样间隔1.0 mm，剖面已重新对齐 | 同上 |
| 重新计算的Z2值与已发表值吻合 | [Tatone 2010, pp. 6-7] | 0.5和1.0 mm采样间隔 | 对照Tse & Cruden, Yu & Vayssade等 |
| 单独二维剖面可能高估或低估三维粗糙度 | [Tatone 2010, pp. 4-5] | 二维方法固有局限 | 建议每个方向多剖面取平均 |
| 剖面梳本身忽略小于采样间隔的特征，并可能引入台阶状假象 | [Tatone 2010, pp. 5-6] | 原始JRC剖面系剖面梳获取 | 采样间隔敏感性的根源 |

## Limitations
- 二维剖面仅采样被剖面线切割的地形特征，可能遗漏影响各向异性或抗剪性的关键几何结构。[Tatone 2010, pp. 4-5]
- 同一方向、相近位置的二维粗糙度值既可高估也可低估真实三维值，存在较大的空间变异性。[Tatone 2010, pp. 4-5]
- 标准JRC剖面最初由剖面梳以固定水平间隔获取，无法捕捉小于采样间隔的形貌，且复描时可能增添阶状特征，减小采样间隔并不会增加真实信息。[Tatone 2010, pp. 5-6]
- Z2、RP等统计参数及其与JRC的经验关系均对采样间隔敏感，使用时必须保持采样间隔一致。[Tatone 2010, pp. 5-6]

## Assumptions / Conditions
- 粗糙度评价以剖面最佳拟合直线（或最佳拟合平面）作为倾角测量的参照。[Tatone 2010, pp. 2-3]
- 采用归一化长度 \(L_{y^*}\) 的累积分布与方程(1)完美拟合，其参数 \(C\) 由非线性最小二乘回归求得。[Tatone 2010, pp. 3-4]
- 分析方向仅限正向或反向，分别代表沿剪切方向的两个可能移动方向。[Tatone 2010, pp. 2-3]
- 新JRC关系基于平均 \(y^*_{\max}/(C+1)_{\text{2D}}\)，隐含假设正向和反向粗糙度对称有效。[Tatone 2010, pp. 7-8]

## Key Variables / Parameters
- \(y^*_{\max}/(C+1)_{\text{2D}}\)：二维粗糙度参数（由拟合参数 \(y^*_{\max}\) 和 \(C\) 导出）
- JRC：节理粗糙度系数（离散数值 0.4 – 18.7）
- 采样间隔：剖面点距，0.5 mm 或 1.0 mm
- 分析方向（forward/reverse）
- \(L_{y^*}\)：超过给定倾角阈值 \(y^*\) 的线段累计归一化长度
- Z2、RP：用于验证的统计参数（均方根一阶导数、粗糙度轮廓参数）

## Reusable Claims
1. **声明**：当采用0.5 mm采样间隔时，可由平均 \(y^*_{\max}/(C+1)_{\text{2D}}\) 按式(8)估算JRC，公式为 \(JRC = 3.95\,(y^*_{\max}/(C+1)_{\text{2D}})^{0.7} - 7.98\)。  
   **条件**：剖面已对齐至最佳拟合水平线，采样间隔严格为0.5 mm，适用对象为类似于Barton标准剖面的节理。  
   **来源**：[Tatone 2010, pp. 7-8]

2. **声明**：当采用1.0 mm采样间隔时，可由平均 \(y^*_{\max}/(C+1)_{\text{2D}}\) 按式(9)估算JRC，公式为 \(JRC = 2.40\,(y^*_{\max}/(C+1)_{\text{2D}})^{0.85} - 4.42\)。  
   **条件**：同上，采样间隔1.0 mm。  
   **来源**：[Tatone 2010, pp. 7-8]

3. **声明**：对石灰岩拉伸断裂面，按30°间隔提取的66条二维剖面的平均粗糙度与三维 \(y^*_{\max}/(C+1)\) 的偏差在1%~11%之间，且各向异性主轴误差约25°。  
   **条件**：表面尺寸200 mm，剖面方向覆盖0°~360°；仅限此特定样本。  
   **来源**：[Tatone 2010, pp. 3-4]

4. **声明**：单独一条二维剖面的粗糙度值可能高估或低估三维值，为获得有代表性的伪三维粗糙度，应在同方向采集多条剖面取平均值。  
   **条件**：适用于基于二维剖面进行各向异性分析的场景。  
   **来源**：[Tatone 2010, pp. 4-5]

5. **声明**：标准JRC剖面经重新对齐（旋转角度≤2°）后，与原始印刷剖面几乎不可分辨，但其倾角分布更符合方法所需的最佳拟合直线参考系。  
   **条件**：对齐过程以所有剖面整体的最佳拟合直线为准（第4 – 6条除外）。  
   **来源**：[Tatone 2010, pp. 5-6]

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[2D roughness parameter]]
- [[y*max/(C+1)2D]]
- [[angular threshold concept]]
- [[normalized length Ly*]]
- [[pseudo-3D roughness]]
- [[roughness anisotropy]]
- [[sampling interval]]
- [[profile alignment]]
- [[Barton-Bandis shear criterion]]
- [[triangulated irregular network (TIN)]]

## Candidate Methods
- [[2D roughness evaluation methodology]]
- [[extraction of 2D profiles from TIN surfaces]]
- [[digitization of standard JRC profiles]]
- [[non-linear least squares fitting for cumulative distribution]]
- [[polar plot comparison for roughness anisotropy]]
- [[verification of digitization via Z2 and RP]]

## Connections To Other Work
- Barton与Choubey (1977) 提出的10条标准JRC剖面是本研究建立新关系的基础。[Tatone 2010, pp. 3-5]
- 三维粗糙度评价方法继承自Grasselli等 (2002, 2003) 及Tatone与Grasselli (2009)，本工作为其二维类比。[Tatone 2010, pp. 1-2]
- 与Tse和Cruden (1979)、Maerz等 (1990)、Yu和Vayssade (1991) 的Z2/JRC、RP/JRC关系进行比较，数字化结果一致。[Tatone 2010, pp. 6-7]
- 采样间隔对JRC经验关系的影响与Hsiung等 (1993) 的观察相呼应。[Tatone 2010, pp. 5-6]

## Open Questions
- 增加更多方向和更多剖面能否进一步缩小二维伪三维粗糙度与真三维参数之间的差异？[Tatone 2010, pp. 3-4]
- 本方法在其它岩性、更大尺寸或更复杂不连续面上的适用性尚未检验。（文本未给出）
- 剖面梳带来的台阶状假象对基于小采样间隔的参数影响程度需定量评估。[Tatone 2010, pp. 5-6]
- 正向与反向粗糙度参数不对称性（表2、表3）如何系统地纳入剪切强度估计，文中未给出方案。[Tatone 2010, pp. 7-8]

## Source Coverage
本页面由 Tatone & Grasselli (2010) 的全部9个非空索引片段编译而成。索引总字符数：40328，编译后源字符数：40534，字符覆盖率：1.005。所有非空源块均被处理，无遗漏片段。
