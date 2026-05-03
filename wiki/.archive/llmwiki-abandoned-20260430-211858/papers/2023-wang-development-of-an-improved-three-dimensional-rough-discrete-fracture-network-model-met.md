---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-wang-development-of-an-improved-three-dimensional-rough-discrete-fracture-network-model-met"
title: "Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application."
status: "draft"
source_pdf: "data/papers/2023 - Development of an improved three-dimensional rough discrete fracture network model Method and application.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wang, Peitao, et al. \"Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application.\" *International Journal of Mining Science and Technology*, 2023, doi:10.1016/j.ijmst.2023.10.004. Accessed 2026."
indexed_texts: "12"
indexed_chars: "56413"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:00:21"
---

# Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application.

## One-line Summary
提出一种基于 Weierstrass-Mandelbrot (W-M) 分形函数的三维粗糙离散裂隙网络（RDFN3D）建模方法，以统一表征岩体结构面粗糙度，并实现了模型向有限元与离散元数值模拟代码的导出。[Wang 2023, pp. 1-1]

## Research Question
如何建立能够考虑结构面粗糙度与波状起伏的三维离散裂隙网络（DFN）模型，并将分形数学表征与实际节理粗糙系数（JRC）建立定量联系，以克服传统光滑裂隙网络（DFN3D）在描述真实岩体结构面时的不足？[Wang 2023, pp. 1-1, 3-4]

## Study Area / Data
未从索引片段中确认具体野外研究区域或工程案例的数据来源。论文主要基于数值生成的 W-M 曲面和蒙特卡洛方法构建的裂隙网络，以及对比数值模拟结果。实际岩体数据未在片段中详述。

## Methods
- **粗糙表面表征**：采用 W-M 分形函数生成三维粗糙曲面。关键控制参数为分形维数 D、高度幅度 G 和表面精度 Pr。通过改变 D、G、Pr 生成不同粗糙度的曲面，并分析各参数对表面高度、起伏度和峰值数量的影响。[Wang 2023, pp. 4-7]
- **与 JRC 的关联**：将标准 JRC 剖面（0-2 至 18-20）映射为 W-M 函数生成的 3D 曲面，通过反演得到对应的 D 和 G 参数，建立分形参数与 JRC 的量值关系。表 1 列出了不同 JRC 范围的推荐 W-M 参数值。[Wang 2023, pp. 7-9]
- **RDFN3D 建模**：基于蒙特卡洛方法，将 W-M 粗糙曲面按照给定的产状（倾向、倾角）、迹长、密度等概率分布随机放置在三维空间内，构建三维粗糙离散裂隙网络。模型假设曲面厚度为零。[Wang 2023, pp. 9-9]
- **数值模拟接口**：使用 MATLAB 生成模型并导出为 DXF 文件或 PFC3D 命令代码，实现与 COMSOL Multiphysics（连续方法）和 PFC3D（非连续方法）的衔接。[Wang 2023, pp. 13-14]

## Key Findings
- **分形参数的影响**：
  - D 值增加会显著降低曲面绝对高度，表面变得更光滑；D=2.5 条件固定时已用于多组对比。[Wang 2023, pp. 4-7]
  - G 值增大使曲面高度增大，粗糙度增加，但峰值数量不变。[Wang 2023, pp. 4-7]
  - Pr 值决定网格数量，Pr 降低时峰值数量减少；Pr 为 0 时得到光滑平面。[Wang 2023, pp. 4-7]
- **W-M 参数与 JRC 的定量对应**：针对长度 100 mm 的标准 JRC 剖面，给出从 JRC 0–2 到 18–20 对应的 W-M 参数组合，例如 JRC=0–2 时 D≈2.52, log(G)≈-6.2；JRC=16–18 时 D≈2.47, log(G)≈-5.5。[Wang 2023, pp. 7-9, Table 1]
- **RDFN3D 模型实现**：成功构建了含一组或三组粗糙裂隙的 RDFN3D 模型，并能生成各向剖面，显示粗糙迹线。模型可导出至 PFC3D 颗粒流模型和 COMSOL 有限元模型，为考虑粗糙度的力学与渗流分析提供了基础。[Wang 2023, pp. 9-13, 13-14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 增加分形维数 D，曲面绝对高度急剧减小，表面变光滑 | [Wang 2023, pp. 4-7] | G=10⁻⁵，Pr=50，L=10 cm，Ls=0.1 cm | 对应图 2 |
| 增大 G，曲面高度增大，粗糙度增加，峰值数量不受影响 | [Wang 2023, pp. 4-7] | D=2.5，Pr=50 | 对应图 3 |
| 精度 Pr 减小，峰值数量减少；Pr=0 获得光滑平面 | [Wang 2023, pp. 4-7] | G=10⁻⁵，D=2.5 | 对应图 4 |
| W-M 参数可定量拟合 JRC 剖面，给出 JRC 3D 对应值（如 JRC 0–2: D=2.52, log(G)=-6.2；JRC 16–18: D=2.47, log(G)=-5.5） | [Wang 2023, pp. 7-9, Table 1] | 长度 100mm 标准 JRC 剖面，x=50 mm 提取 2D 轮廓 | 参数基于拟合得到 |
| RDFN3D 模型可导出 DXF 与 PFC3D 命令，用于有限元和离散元模拟；但数值模型因网格划分限制常简化，含较少裂缝 | [Wang 2023, pp. 13-14] | MATLAB 生成，转换至 PFC3D 和 COMSOL | 网格划分错误在裂缝过多时出现 |

## Limitations
- **建模复杂性**：3D 粗糙结构面网络表征和建模机制复杂，以往研究多停留在光滑结构面。本文虽提出 W-M 方法，但生成网络需依赖大量参数输入，实际工程中获取精确分形参数仍有难度。[Wang 2023, pp. 3-4]
- **数值模型简化**：在有限元模拟中，因网格剖分限制，地质模型需简化，导致数值模型中的裂缝数量少于数字 RDFN3D 模型，可能丢失部分结构细节。[Wang 2023, pp. 13-14]
- **参数适用性**：文中所提 W-M 参数与 JRC 对应关系是基于典型 100 mm 剖面建立，对于其他尺度或非标准粗糙度形态的适用性未明确验证。未从索引片段中确认是否讨论了尺度效应。
- **验证不完整**：片段仅提及“the reliability of the RDFN3D...”后文缺失，因此模型的可靠性论证细节未能从片段中完全确认。

## Assumptions / Conditions
- 所模拟的岩体结构面具有分形特征，可使用 W-M 函数描述。[Wang 2023, pp. 4-4]
- 裂隙网络生成基于蒙特卡洛方法，假定裂隙中心位置符合均匀分布，产状、迹长等几何参数按给定概率分布随机生成。[Wang 2023, pp. 9-9, 9-13]
- 生成的粗糙曲面厚度假定为零。[Wang 2023, pp. 9-9]
- 单个曲面表征参数 D、G、Pr 控制，且能够通过拟合映射到 JRC 等级。[Wang 2023, pp. 7-9]
- 模型导出和数值模拟时假设网格划分合理，忽略过密裂缝带来的划分困难（实际会进行简化）。[Wang 2023, pp. 13-14]

## Key Variables / Parameters
- **W-M 分形参数**：分形维数 D、高度幅度 G、表面精度 Pr、频率相关参数 M、样品尺寸 L、最小分辨率 Ls、最高频率指数 nmax（片段中设定 L=100 mm, Ls=1 mm 等）。[Wang 2023, pp. 4-7]
- **裂隙网络几何参数**：各组裂缝的倾向、倾角、迹长、密度（traces/cm³）、隙宽；案例 I 中 D=2.5, G=10⁻⁷, Pr=15 等。[Wang 2023, pp. 9-13, Table 3]
- **粗糙度指标**：节理粗糙度系数 JRC 及其对应的 3D 分形参数。[Wang 2023, pp. 7-9, Table 1]

## Reusable Claims
1. **D 对粗糙度的减控作用**：在固定 G 和 Pr 下，增大分形维数 D 会使得 W-M 曲面高度急剧降低，表面更平滑；这一结论适用于 L=100mm, G=10⁻⁵, Pr=50 的条件，且由数值曲面图像印证。[Wang 2023, pp. 4-7]
2. **G 对粗糙度的提升作用**：在固定 D 和 Pr 下，增大幅度 G 将增加曲面绝对高度和粗糙度，但峰的数量不改变；该结论基于 D=2.5, Pr=50, L=100mm 的 W-M 生成曲面。[Wang 2023, pp. 4-7]
3. **Pr 对表面复杂性的影响**：表面精度 Pr 减小使峰值数量减少，Pr=0 时光滑平面出现；当 Pr 增大时表面网格增多，起伏度增强但不改变整体曲面形状（如 D、G 固定时）。[Wang 2023, pp. 4-7]
4. **W-M 参数与 JRC 的映射**：对于标准 JRC 剖面，可用 W-M 函数生成的二维轮廓与 JRC 分级对应的 3D 曲面建立联系，不同 JRC 区间有定量参数组合（例：JRC 4–6 时 D=2.50, log(G)≈-5.9）。该映射条件为样本长度 100 mm，且基于反演结果，适用于快速生成具有指定粗糙度的裂隙网络。[Wang 2023, pp. 7-9, Table 1]
5. **RDFN3D 模型的可移植性**：建立的粗糙裂隙网络模型可导出为 DXF 或 PFC3D 命令，在 COMSOL 和 PFC3D 中模拟；但需注意在有限元中网格划分限制要求模型中的裂缝数量少于实际数字模型，否则会产生错误。[Wang 2023, pp. 13-14]

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Roughness|粗糙度]]
- [[Weierstrass-Mandelbrot function]]
- [[Fractal Geometry]]
- [[Joint Roughness Coefficient (JRC)]]
- [[Monte Carlo method]]
- [[3D geological modeling]]
- [[Rock mechanics]]
- [[Drawing Exchange Format (DXF)]]
- [[PFC3D]]
- [[COMSOL Multiphysics]]
- [[Fracture network modeling]]
- [[Structural plane characterization]]

## Candidate Methods
- [[RDFN3D modeling]]
- [[W-M fractal surface generation]]
- [[Monte Carlo stochastic fracture generation]]
- [[JRC estimation from fractal parameters]]
- [[Numerical simulation with PFC3D and COMSOL]]
- [[DFN export to DXF]]

## Connections To Other Work
- **JRC 的经典定义**：文中使用了 Barton 和 Choubey [36] 提出的节理粗糙度系数（JRC）作为粗糙度表征基准，并与分形参数关联。[Wang 2023, pp. 3-4]
- **裂隙网络体密度估计**：RDFN3D 建模需线密度、面密度与体密度转换，段中引用了 Kulatilake 等 [49] 和 Wu 等 [50] 建立的关系。[Wang 2023, pp. 9-9]
- **DFN 模型改进**：引用张等 [29] 基于 DFN 的流动模型，以及郑等 [30] 提出的椭圆盘 DFN 模型以克服圆盘假设的局限，均体现了前人在网络几何表征上的发展。[Wang 2023, pp. 2-3]
- 此外，可从主题上连接到 [[fracture reservoir]]、[[hydraulic fracturing]] 等领域的裂隙网络模拟工作，但片段中未直接提及。

## Open Questions
- 所提 W-M 参数与 JRC 的对应关系是否适用于原位大尺度岩体或动态加载下节理粗糙度的演化？未从索引片段中确认。
- RDFN3D 模型在复杂渗流‑应力耦合分析中的适用性如何，尤其在裂缝数量受限时能否保留主要力学行为？未从索引片段中确认。
- 模型生成与实际岩体裂隙几何的统计等效性验证方法和结果未在片段中详述。
- 分形参数的反演是否可以直接从三维扫描数据中获得？未从索引片段中确认。

## Source Coverage
本词条基于 12 个索引片段编写，内容覆盖论文摘要、引言（问题背景与 DFN 局限性）、W-M 粗糙表面表征方法、分形参数影响讨论、W‑M 与 JRC 映射表的建立、RDFN3D 建模原理与案例、以及数值模拟接口实现。部分内容可能来自正文结果章节和讨论部分，但具体数值模拟结果细节（如力学、流动行为的定量对比）以及完整结论在片段中未充分展开。特别是关于“the reliability of the RDFN3D...”的后续验证结果缺失，导致无法完全确认模型可靠性论证的全貌。
