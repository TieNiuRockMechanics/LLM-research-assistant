---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-wang-development-of-an-improved-three-dimensional-rough-discrete-fracture-network-model-met"
title: "Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application."
status: "draft"
source_pdf: "data/papers/2023 - Development of an improved three-dimensional rough discrete fracture network model Method and application.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wang, Peitao, et al. \"Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application.\" *International Journal of Mining Science and Technology*, 2023, doi:10.1016/j.ijmst.2023.10.004. Accessed 2026."
indexed_texts: "12"
indexed_chars: "56413"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "56654"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004272"
coverage_status: "full-index"
source_signature: "378c5ee94209c5551cfebf98ce94b8f688af92f1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:18:00"
---

# Development of an Improved Three-Dimensional Rough Discrete Fracture Network Model: Method and Application.

## One-line Summary

提出基于Weierstrass-Mandelbrot（W-M）函数的三维粗糙离散裂隙网络（RDFN3D）建模方法，建立了分形参数与节理粗糙度系数（JRC）的定量关系，并通过PFC3D与COMSOL验证了粗糙度对力学和渗流行为的显著影响。

[Wang 2023, pp. 1-1] [Wang 2023, pp. 14-15]

## Research Question

如何建立能够真实反映节理表面粗糙度特征的三维离散裂隙网络模型，并量化分形参数（分形维数 D、高度振幅 G、表面精度 Pr）与标准JRC曲线的对应关系，进而分析粗糙裂隙网络对岩体力学破坏模式和流体渗流路径的控制作用。

[Wang 2023, pp. 1-1] [Wang 2023, pp. 3-4] [Wang 2023, pp. 4-5] [Wang 2023, pp. 14-15]

## Study Area / Data

研究采用理论建模与数值模拟相结合，未明确指定特定工程现场。案例中使用了来自石碌铁矿露天矿的斜坡结构面照片（JRC 14-16）用于参数匹配示例，但实际构建的RDFN3D模型为虚拟生成的裂隙网络（模型尺寸100 mm × 100 mm × 100 mm）。[Wang 2023, pp. 4-5] [Wang 2023, pp. 7-9]

数值模拟部分引用了Huang et al. (2021) 的绿色砂岩物理力学参数（试样尺寸50 mm × 100 mm，密度2.17 g/cm³，抗压强度29.80 MPa，弹性模量8.40 GPa，泊松比0.290），并在PFC3D中建立了150 mm × 150 mm × 150 mm的节理岩体模型。[Wang 2023, pp. 13-14]

## Methods

1. **粗糙表面表征**：采用修改的W-M函数（Yan & Komvopoulos, 1998）生成三维分形表面，其控制参数为分形维数 D（2 < D < 3）、分形粗糙度 G（>0）、频率参数 c（取1.5）和折叠峰数 M（取10），并引入表面精度 Pr（网格分辨率）控制生成的点云密度。[Wang 2023, pp. 3-5]

2. **JRC定量匹配**：通过调整 D 和 G，生成十组标准JRC曲线（0–20）对应的三维粗糙表面，并利用Tatone & Grasselli (2010) 的公式（JRC_Z2 = 55.03·Z2^0.74 - 6.1，其中Z2为表面轮廓一阶导数的均方根）计算二维剖面JRC值，建立Log(G)和D与JRC的对应关系表。[Wang 2023, pp. 4-7]

3. **RDFN3D构建流程**：基于Monte Carlo方法，根据现场统计的节理产状（倾向、倾角）、迹长、体积密度等参数，将对应JRC的W-M曲面按随机位置和方向放置，形成粗糙离散裂隙网络。表面厚度初始设为零，后续可通过偏移考虑开度。通过MATLAB将节点坐标导出为DXF或TXT文件，供AutoCAD、COMSOL和PFC3D使用。[Wang 2023, pp. 7-9]

4. **案例对比**：设计三组案例：I 组仅含一组高持久性粗糙裂隙；II 组含三组高持久性裂隙（同时有DFN3D对照）；III 组含三组低持久性裂隙（DFN3D对照），分析不同参数对网络形态的影响。[Wang 2023, pp. 9-13]

5. **数值验证**：在PFC3D中建立粗糙结构面的合成岩体（SRM）模型，采用线性平行粘结模型，节理单元粘结强度设为完整岩石的1%，进行单轴压缩模拟；在COMSOL中基于达西定律模拟定水头条件下单个粗糙面及交叉裂缝中的渗流场，比较RDFN3D与DFN3D的破坏模式和流速分布。[Wang 2023, pp. 13-16]

## Key Findings

1. 分形参数对表面形态的影响规律：增大D使表面起伏频率降低、趋于平滑；增大G使起伏幅值增加但不改变峰数量；减小Pr降低网格精度，表面波动数减少，当Pr=1时退化为光滑平面。[Wang 2023, pp. 4-5][Wang 2023, pp. 7-9]

2. JRC与W-M参数的定量关系：针对100 mm标准轮廓线，得到Log(G)和D的组合可匹配JRC 0–20范围的十条曲线，对应的JRC3D值（由2D剖面计算）与标准JRC一致，为岩体结构面的三维重建提供了参考参数。[Wang 2023, pp. 7]

3. 力学响应差异：PFC3D模拟显示，RDFN3D模型的峰值抗压强度（58.11 MPa）略高于DFN3D模型（55.70 MPa），表明节理粗糙度可提高节理岩体的压缩承载能力，且破坏模式受起伏度显著影响，但峰前应力-应变曲线基本重合。[Wang 2023, pp. 13-14]

4. 渗流行为差异：COMSOL模拟表明，粗糙裂缝中的流体在凹凸区域形成高流速和低流速区，流动方向受起伏形态影响，流场比光滑裂缝更不均匀。裂缝网络的粗糙度和空间连通性对渗流模式起主导作用。[Wang 2023, pp. 14-16]

5. 模型导出与应用：成功将RDFN3D模型输出为DXF、PFC3D命令流及STL格式，实现了在商业有限元、离散元软件中的直接建模，拓宽了粗糙裂隙网络在岩体工程分析中的应用前景。[Wang 2023, pp. 13][Wang 2023, pp. 16]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 修改的W-M函数可生成具有分形特征的粗糙表面，参数D、G、Pr分别控制起伏频率、幅值和表面复杂度 | [Wang 2023, pp. 3-5] | L=10 cm, Ls=0.1 cm, nmax=11, M=10, γ=1.5; D=2.3-2.9, G=10^-7~10^-3, Pr=4-50 | 当Pr=1时表面为光滑平面 |
| 十组标准JRC轮廓可与特定W-M参数组合匹配，JRC3D计算值与标准JRC一致 | [Wang 2023, pp. 7] | Pr=20, M=10, L=100, Ls=0.1, γ=1.5; Log(G)范围-6.2至-5.5, D范围2.46至2.52 | JRC3D通过Tatone & Grasselli (2010)公式计算 |
| RDFN3D模型峰值强度58.11 MPa，DFN3D模型55.70 MPa，粗糙度增加压缩承载力 | [Wang 2023, pp. 13-14] | 单轴压缩，模型尺寸150 mm立方体，颗粒流线性平行粘结模型，节理粘结强度1% | 绿色砂岩参数来自Huang et al. (2021) |
| 粗糙裂缝中流动方向受起伏影响，形成高/低速区，光滑裂缝流场均匀 | [Wang 2023, pp. 14-16] | 进水口水压1 kPa，出水口0 kPa，渗透系数1×10^-8 m²，流体密度1000 kg/m³，粘度1.001×10^-6 Pa·s | 基于COMSOL达西流模拟 |

## Limitations

1. 生成的粗糙表面与天然结构面的对应关系仅为初步的视觉和经验匹配，未建立严格的定量映射方法，尚缺乏实际岩体结构面三维扫描数据的系统验证。[Wang 2023, pp. 7]

2. RDFN3D模型中的裂隙厚度（开度）初始设为零，未考虑天然裂隙的开度分布，需在后续建模中通过偏移处理。[Wang 2023, pp. 7-9]

3. 有限元数值模拟中，网格划分是瓶颈，成千上万的粗糙表面难以成功划分网格，导致数值模型中的裂隙数量远少于地质模型，限制了大规模工程应用。[Wang 2023, pp. 13][Wang 2023, pp. 16]

4. PFC3D模拟中使用的节理微力学参数粘结强度固定为1%的完整岩石强度，缺少对天然节理力学参数的校准，且模型尺寸较小，未探讨尺寸效应。[Wang 2023, pp. 13-14]

5. 文中仅给出三组确定性案例，未对参数空间（如不同D、G、Pr组合及裂隙几何统计分布）进行系统敏感性分析。[Wang 2023, pp. 9-13]

## Assumptions / Conditions

- 假定岩体结构面具有分形特征，即局部与整体统计自相似，可用W-M函数描述。[Wang 2023, pp. 3-4]
- 三维结构面在生成时视为零厚度的表面，初始开度为0。[Wang 2023, pp. 7-9]
- W-M函数中频率参数γ固定为1.5，叠加峰数M固定为10，随机相位角u_m,n在[0, 2π]内均匀分布。[Wang 2023, pp. 4][Wang 2023, pp. 7]
- 裂隙空间位置服从均匀分布，产状按统计均值和标准差随机生成。[Wang 2023, pp. 7-9]
- 数值模拟中，岩石基质采用线性平行粘结模型，节理单元强度为完整岩石的1%，节理面法向和切向力学行为未独立定义。[Wang 2023, pp. 13-14]
- 渗流模拟假设达西流，裂隙壁不透水，仅考虑裂隙内流动，忽略基质渗透性。[Wang 2023, pp. 14-16]

## Key Variables / Parameters

- **分形维数 D**（2 < D < 3）：控制表面起伏频率，值越大表面越平滑。[Wang 2023, pp. 4-5]
- **分形粗糙度 G**（>0）：控制表面最大起伏幅值，值越大表面越粗糙。[Wang 2023, pp. 4-5]
- **表面精度 Pr**（>0）：网格采样点数，值越高表面细节越丰富，Pr=1时为光滑平面。[Wang 2023, pp. 4-5][Wang 2023, pp. 7-9]
- **截止长度 Ls**：限制最高起伏频率，决定nmax。[Wang 2023, pp. 4]
- **节理粗糙度系数 JRC**：通过标准轮廓线（0-20）与2D剖面计算值JRC3D关联。[Wang 2023, pp. 7]
- **裂隙几何参数**：倾向、倾角、迹长、体积密度、开度（初始为0）。[Wang 2023, pp. 7-9][Wang 2023, pp. 9-13]
- **岩石力学参数**：试样密度、抗压强度、弹性模量、泊松比。[Wang 2023, pp. 13-14]
- **渗流参数**：流体的密度、动力粘度、裂隙渗透系数、边界水头。[Wang 2023, pp. 14-16]

## Reusable Claims

- 对于分形维数D越高、分形粗糙度G越小的W-M表面，其起伏频率越低、幅值越小，表面趋于平滑；当表面精度Pr=1时，生成光滑平面。这一规律适用于假设表面具有统计自相似特征的岩体结构面建模。[Wang 2023, pp. 4-5][Wang 2023, pp. 7-9]
- 在Pr=20、M=10、L=100 mm、Ls=0.1 mm、γ=1.5的条件下，通过调整Log(G)（-6.2至-5.5）和D（2.46至2.52）可实现JRC从0-2到18-20的十条标准曲线的匹配，为W-M函数参数选择提供了量化参考。[Wang 2023, pp. 7]
- 粗糙离散裂隙网络（RDFN3D）模型相较于光滑DFN3D模型，可略微提高节理岩体的单轴抗压峰值强度（增幅约4.3%），且破坏模式受结构面起伏控制，峰前应力-应变曲线差异不大。[Wang 2023, pp. 13-14]
- 粗糙裂隙中的流体在凸起和凹陷区域产生高低流速分区，流向受表面起伏影响，导致渗流场不均匀性显著高于光滑裂隙；裂缝网络的粗糙度和空间连通性共同控制整体渗流模式。[Wang 2023, pp. 14-16]
- 通过将MATLAB生成的点云坐标导出为DXF或TXT格式，可实现RDFN3D模型在PFC3D、COMSOL等离散元与有限元软件中的导入，为粗糙裂隙岩体的数值模拟提供了可行路径，但有限元网格划分仍是应用瓶颈。[Wang 2023, pp. 13][Wang 2023, pp. 16]

## Candidate Concepts

- [[离散裂隙网络]]
- [[粗糙离散裂隙网络模型]]
- [[Weierstrass-Mandelbrot分形函数]]
- [[节理粗糙度系数]]
- [[合成岩体]]
- [[等效岩体]]
- [[分形维数]]
- [[裂隙连通性]]
- [[裂隙渗流]]
- [[颗粒流程序]]

## Candidate Methods

- [[W-M分形曲面生成]]
- [[基于JRC曲线的分形参数标定]]
- [[蒙特卡罗裂隙网络建模]]
- [[DXF点云导出与建模]]
- [[PFC3D合成岩体数值试验]]
- [[COMSOL裂隙流达西模拟]]
- [[三维粗糙表面轮廓Z2计算]]

## Connections To Other Work

- 利用Barton和Choubey [36] 提出的JRC标准曲线作为粗糙度标定依据，通过Tatone和Grasselli [48] 的Z2计算公式实现W-M曲面与JRC的定量关联。[Wang 2023, pp. 7]
- 继承Yan和Komvopoulos [46] 的修正W-M函数，用于生成三维分形粗糙表面。[Wang 2023, pp. 3-4]
- 基于Kulatilake等 [49] 及Wu等 [50] 的节理网络几何统计和体积密度估算方法，构建离散裂隙网络。[Wang 2023, pp. 7-9]
- 采用Robinson [24] 的裂隙连通渗透理论思路，以及Li等 [27,28] 关于裂隙连通性参数（交线长度等）的研究，讨论了粗糙度对连通性及渗流的影响。[Wang 2023, pp. 14-16]
- 承袭Wang等 [45] 的二维粗糙离散裂隙网络（RDFN2D）概念，将其扩展至三维。[Wang 2023, pp. 2-3]

## Open Questions

- 如何通过三维激光扫描或摄影测量获取实际岩体结构面的点云数据，反算出对应的W-M分形参数（D, G），实现从真实结构面到数学模型的精确映射？[Wang 2023, pp. 7]
- 在有限元数值模拟中，如何解决大量粗糙表面网格划分困难的问题，使RDFN3D模型能应用于实际工程尺度的力学分析？[Wang 2023, pp. 16]
- 粗糙裂隙网络中考虑变开度（如力学开度、水力开度）和充填物时，其力学-渗流耦合行为的演化规律如何？[Wang 2023, pp. 14-16]
- 不同应力路径（如剪切、真三轴）下，粗糙结构面的破坏演化与峰后行为如何受分形参数组合的影响？[Wang 2023, pp. 13-14]
- 文中参数标定基于单一采样长度（100 mm），当结构面尺寸变化时，W-M参数与JRC的匹配关系是否具有尺度不变性？[Wang 2023, pp. 4-5]

## Source Coverage

本页面依据所提供的全部12个非空源片段编写，覆盖了原文所有索引内容。源文本总字符数56413，编译后字符数56654，覆盖率100%。所有声明均直接源自所标记的源片段，未添加外部信息。
