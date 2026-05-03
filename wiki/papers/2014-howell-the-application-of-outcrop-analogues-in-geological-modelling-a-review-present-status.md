---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-howell-the-application-of-outcrop-analogues-in-geological-modelling-a-review-present-status"
title: "The Application of Outcrop Analogues in Geological Modelling: A Review, Present Status and Future Outlook."
status: "draft"
source_pdf: "data/papers/2014 - The application of outcrop analogues in geological modelling a review, present status and future outlook.pdf"
collections:
  - "part4-1"
citation: "Howell, John A., et al. \"The Application of Outcrop Analogues in Geological Modelling: A Review, Present Status and Future Outlook.\" *Sediment-Body Geometry and Heterogeneity: Analogue Studies for Modelling the Subsurface*, edited by A. W. Martinius et al., Geological Society of London, 2014, pp. 1-25. Geological Society Special Publications, no. 387. DOI: 10.1144/SP387.12. Accessed 2026."
indexed_texts: "25"
indexed_chars: "123941"
nonempty_source_blocks: "25"
compiled_source_blocks: "25"
compiled_source_chars: "124546"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004881"
coverage_status: "full-index"
source_signature: "d110129accc62eb7267e54c2f34d13d9272ae36b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:36:18"
---

# The Application of Outcrop Analogues in Geological Modelling: A Review, Present Status and Future Outlook.

## One-line Summary
综述露头类似物在地质建模中的应用历史、数据分类（硬数据、软数据、训练图像、动态生产数据）及其在建模工作流中的使用方法，分析挑战、不同沉积环境的案例及未来展望，强调正确选择类比和量化几何数据对降低地下不确定性的关键作用。

## Research Question
如何在数据极度稀疏的地下储层建模中有效选择、收集和应用露头类似物（特别是定量几何数据）以准确表征储层构型并降低预测不确定性？同时，讨论四种不同类比数据类型（硬数据、软数据、训练图像、动态类比数据）在建模工作流各阶段的应用现状、潜在误差来源及未来发展方向。

## Study Area / Data
研究并非单一地理区域，而是系统回顾全球范围内多个克拉通和造山带露头的类比数据收集与应用，涵盖河流、风成、滨岸、深海等碎屑岩沉积环境。引用的露头数据库和案例包括：
- Book Cliffs（美国犹他州）的海相滨岸和海岸平原露头，用于获取砂体几何和层序地层信息[Howell 2014, pp. 3-4][Howell 2014, pp. 10-11]
- Blackhawk 组（犹他州）的虚拟露头与储层建模[Howell 2014, pp. 4-5]
- SAFARI 项目数据库（挪威石油公司联合项目）中的河流-浅海砂体尺寸统计[Howell 2014, pp. 3-4][Howell 2014, pp. 6-7]
- Wax Lake 三角洲现代类比作为训练图像[Howell 2014, pp. 6-7]
- 风成系统：犹他、纳米比亚和英国中、古生代露头[Howell 2014, pp. 11-12]
- 河流系统：Escanilla 组（西班牙）、Esplugafreda 组、Lourinha 组（葡萄牙）等的定量砂体几何数据库[Howell 2014, pp. 12-13]
- 平行/边缘海系统：Blackhawk 组、Ferron 砂岩、Panther Tongue 段（犹他）等用于获取砂体宽度-厚度关系、页岩隔夹层尺寸及斜层几何[Howell 2014, pp. 13-14]
- 深海系统：Ainsa 盆地（西班牙）、Tanqua Karoo（南非）、Morillo 组等用于量化水道单元几何、连通性及细粒物质覆盖比例[Howell 2014, pp. 14-16]
- 本卷收录论文涵盖河流、滨岸、深海等多种环境，以及 LiDAR 和虚拟露头技术应用[Howell 2014, pp. 15-16]

## Methods
本文为综述性方法论文，总结并分类了露头类比数据在储层建模中的使用方法，未进行新的野外数据采集或建模实验。主要的方法框架包括：
- 将类比数据分为四类：软数据（概念模型、相组合关系）、硬数据（砂体几何尺寸统计）、训练图像（用于多点地质统计学）、类比生产数据（来自成熟相似油田的动态数据）[Howell 2014, pp. 1-2][Howell 2014, pp. 5-7]
- 描述典型储层建模工作流七个阶段中各类类比数据的应用：问题定义与类比选择、概念地质模型、构造框架建立、网格化、静态相建模（主体）、岩石物理属性建模以及多尺度建模与粗化[Howell 2014, pp. 7-9]
- 讨论数据收集方法演变，从比例素描、光拼图到地面激光扫描（LiDAR）、直升机载LiDAR和虚拟露头技术，以及GPR等浅层地球物理手段[Howell 2014, pp. 4-5][Howell 2014, pp. 9-10]
- 分析类比选择、数据收集与存储、露头2D-3D转换、不完整砂体测量、采样偏差等实际挑战[Howell 2014, pp. 9-11]
- 按沉积环境（风成、河流、滨岸、深海）系统回顾过去的定量类比研究，强调标准化、尺度匹配及数据可访问性的重要性[Howell 2014, pp. 11-16]
- 展望未来技术趋势，包括摄影测量（UAV）、超光谱扫描、自由遥感数据（如Google Earth）的应用，以及目的性数据库（SAFARI, FAKTS）的发展和多点统计直接利用露头训练图像[Howell 2014, pp. 16-17]

## Key Findings
- 露头类似物是补充地下井和地震数据不足的关键手段，能提供储层构型的几何尺寸、空间关系和连通性信息[Howell 2014, pp. 1-2]。
- 类比数据可分为四类：硬数据（砂体几何）、软数据（相概念关系）、训练图像（用于MPS）和类比生产数据（用于动态模拟）[Howell 2014, pp. 1-2][Howell 2014, pp. 5-7]。
- 没有完美的类似物，选择类比必须回答“在哪些方面相似？”的问题，且可能需要组合多个类似物[Howell 2014, pp. 2-3]。
- 露头数据收集技术从早期素描发展到现代LiDAR和虚拟露头，极大提高了精度和三维测量能力，但仍存在2D向3D推断的挑战[Howell 2014, pp. 4-5][Howell 2014, pp. 9-11]。
- 露头类似物在建模工作流的不同阶段发挥作用：软数据主导概念模型阶段，硬数据和训练图像主导静态相建模阶段[Howell 2014, pp. 7-8]。
- 各沉积环境（风成、河流、滨岸、深海）的定量砂体尺寸数据库揭示了系统内的自然变异性，但普遍存在数据点分散、缺乏标准化的问题[Howell 2014, pp. 11-15]。
- 露头细粒相（页岩、碳酸盐胶结层）往往暴露不足，导致其在类比文献中被低估[Howell 2014, pp. 9-10]。
- 露头岩石物性（孔渗）因风化、成岩差异难以直接类比地下，但可提供相对渗透率结构和概念信息[Howell 2014, pp. 9-10]。
- 未来趋势包括无人机摄影测量、超光谱岩性识别、自由遥感数据利用以及构建支持直接生成训练图像的露头数据库[Howell 2014, pp. 16-17]。

## Core Evidence Table

| Evidence                                        | Source                        | Conditions/Scale                               | Notes                                                      |
| ----------------------------------------------- | ----------------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| 四种类比数据类型：硬数据、软数据、训练图像、生产数据 | Howell et al. 2014, pp. 1-2, 5-7 | 适用于碎屑岩储层建模                         | 软数据提供定性关系，硬数据提供定量几何信息               |
| 储层建模工作流中类比数据的应用阶段               | Howell et al. 2014, pp. 7-9    | 7步线性-迭代工作流，需根据建模目标选择        | 强调相建模阶段是硬数据应用核心                           |
| 没有“完美”类似物，选择须基于特定相似特征       | Howell et al. 2014, pp. 2-3    | 每个油藏系统独特，需明确相似性                | 可组合多个类似物（例：Scarborough 气田，Glenton et al. 2013） |
| 砂体宽度-厚度关系等几何数据常用作对象建模约束   | Howell et al. 2014, pp. 6-7    | 定量数据来自露头直接测量                      | 早期如 SAFARI 项目已收集大量此类数据                     |
| 虚拟露头技术（地面/机载LiDAR）提高数据精度和3D度| Howell et al. 2014, pp. 4-5, 16-17 | 需要陡峭、良好暴露的露头，成本较高           | 未来摄影测量可能降低成本                                 |
| 露头细粒相暴露不足导致几何数据偏差               | Howell et al. 2014, pp. 9-10   | 植被和风化覆盖影响                             | 建议使用陡崖露头和虚拟露头改善                            |
| 河流砂体尺寸数据库揭示系统内变异性               | Howell et al. 2014, pp. 12-13  | 河流类型（曲流河、辫状河等）差异大             | 需谨慎记录测量对象（单一点坝或复合体）                     |
| 滨岸体系砂体几何受波浪/潮汐/河流主导过程控制    | Howell et al. 2014, pp. 13-14  | 基于 Galloway (1975) FWT 分类                 | 净进积与净退积影响砂体连通性                             |
| 深海水道单元宽度-厚度比范围大，水道底泥披覆盖率>60%影响采收率 | Howell et al. 2014, pp. 14-16 | 实例来自 Ainsa 盆地、Karoo 盆地等           | Barton et al. 2010 指出泥披覆盖超过60%时影响采收率        |
| 场景式建模可避免单一基础模型的锚定偏差          | Howell et al. 2014, pp. 2-3, 16-17 | Bentley & Smith 2008 提出                     | 多个类比数据集提供多样化场景                               |

## Limitations
- 综述性质，未提供新的一次数据，所引用的案例均来自已发表文献或内部报告，可能存在数据未公开、标准不统一的问题[Howell 2014, pp. 3-5, 10]。
- 讨论仅针对碎屑岩储层，碳酸盐岩未涵盖[Howell 2014, pp. 1-2]。
- 露头类比数据固有的局限性：露头规模可能不足以代表整个油藏（如50-100米高的露头对应千米级油藏）、露头方向与砂体主轴的夹角导致尺寸测量偏差、不完整砂体的边界截断问题[Howell 2014, pp. 9-11]。
- 露头岩石物性受风化与成岩差异影响，不能直接搬运至地下模型，仅提供相对渗透率结构信息[Howell 2014, pp. 9-10]。
- 细粒沉积物暴露差，导致文献中对页岩/泥岩隔夹层的尺寸数据不足[Howell 2014, pp. 9-10]。
- 缺乏统一的术语和数据格式，阻碍数据库整合和大规模数据挖掘[Howell 2014, pp. 10]。
- 对未来展望的预测较为宽泛，未提供具体的技术路线或验证案例。

## Assumptions / Conditions
- 假设地下储层与露头类似物在沉积过程和构型方面足够相似，可以外推几何参数[Howell 2014, pp. 2-3]。
- 假设收集的露头数据具有代表性，且采样能充分覆盖自然变异性[Howell 2014, pp. 9-10]。
- 建模工作流基于典型的工业流程，以角点网格和基于对象的/基于像元的地质统计学方法为主[Howell 2014, pp. 7-8]。
- 静态相建模是控制岩石物理属性分布的根本，因此露头数据的主要价值在于提供相的三维分布[Howell 2014, pp. 8-9]。
- 所述挑战和方法适用于常规碎屑岩油气藏，非常规资源（如页岩油）未包括在内。

## Key Variables / Parameters
- **砂体宽度/厚度比**：对象建模中定义河道或砂坝形态的关键输入[Howell 2014, pp. 6-7]。
- **砂体定向尺寸与走向**：需校正古流向以得到真实宽度和长度[Howell 2014, pp. 11]。
- **隔夹层（页岩/胶结层）长度**：控制储层内流动障碍的有效性[Howell 2014, pp. 6-7, 14-15]。
- **相带厚度和退覆角**：用于截断高斯模拟或像元建模[Howell 2014, pp. 6-7]。
- **相之间的横向/垂向转换关系**：概念模型和训练图像的核心内容[Howell 2014, pp. 8-9]。
- **水道泥披覆盖率**：影响深海储层连通性的关键阈值（>60%）[Howell 2014, pp. 15]。
- **露头的三维度**：用崖线长度与所在面积的比率度量[Howell 2014, pp. 11]。

## Reusable Claims
- “Given that no two geological systems are identical, it follows that there is no such thing as the perfect analogue.” [Howell 2014, pp. 2-3] → 条件：类比选择必须基于预设的关键储层参数；选择需回答“在哪些方面相似？”。
- 硬数据（几何尺寸）用于条件对象建模和基于像元的建模，软数据（概念关系）用于指导模型框架和情景生成。[Howell 2014, pp. 5-6] → 应用时需匹配建模阶段。
- 细粒相在露头上暴露不足导致其尺寸在文献中被低估，使用此类数据时应意识到可能偏差。[Howell 2014, pp. 9-10] → 必须结合优良露头或虚拟露头技术校正。
- 露头岩石物性不能直接代替地下物性，但可以提供同一种相内部的相对渗透率结构趋势。[Howell 2014, pp. 9-10] → 可结合地下井的岩心数据建立关联。
- 多点地质统计（MPS）训练图像可直接从露头生成，但需要采集能够表达形状和空间关系的定量数据。[Howell 2014, pp. 6-7, 16] → 未来发展方向。
- 当露头尺寸不足以覆盖整个储层时，可组合多个类似物或采用基于过程的模型生成训练图像。[Howell 2014, pp. 2-3, 15] → 实例包括 Glenton et al. 2013 的 Scarborough 气田。

## Candidate Concepts
- [[outcrop analogue]] (露头类似物)
- [[reservoir modelling workflow]] (储层建模工作流)
- [[sediment-body geometry]] (沉积体几何)
- [[soft data vs hard data]] (软数据与硬数据)
- [[training image]] (训练图像)
- [[multi-point statistics (MPS)]] (多点统计)
- [[LiDAR virtual outcrop]] (LiDAR虚拟露头)
- [[process-based modelling]] (基于过程的建模)
- [[sequence stratigraphy control]] (层序地层控制)
- [[fluvial reservoir connectivity]] (河流储层连通性)
- [[deep-water channel drape]] (深水水道泥披)
- [[shoreface clinoform barriers]] (滨岸斜层隔夹层)
- [[hierarchical stratigraphic scale]] (层序地层尺度)

## Candidate Methods
- [[object-based stochastic modelling]] (基于对象的随机建模)
- [[pixel-based modelling with variograms]] (基于像元变差函数建模)
- [[multi-scale REV modelling]] (多尺度表征单元体建模)
- [[ground-based and helicopter-mounted LiDAR]] (地面与直升机载LiDAR)
- [[photogrammetry from UAV]] (无人机摄影测量)
- [[GPR for shallow 3D imaging]] (探地雷达浅层三维成像)
- [[synthetic seismic from outcrop]] (露头合成地震记录)
- [[behind-outcrop boreholes]] (露头后钻孔)
- [[composite analogue selection]] (复合类似物选择)
- [[scenario-based approach]] (基于情景的方法)

## Connections To Other Work
- 与早期经典类似物应用的联系：Glennie (1970, 1972, 1986) 现代沙漠类比 Rotliegend 储层；Weber (1987) 美国西部风成砂岩类比 Groningen 气田[Howell 2014, pp. 3-4]。
- 与早期随机建模工作的联系：Zeito (1965) 页岩长度统计；Haldorsen & Lake (1984)、Begg & King (1985) 随机页岩建模；Fielding & Crane (1987) 河道砂体建模[Howell 2014, pp. 3-4]。
- 与本卷收录论文的整合：作为“Sediment-Body Geometry and Heterogeneity”专题卷的引言，总结了各篇论文在河流（Alsop et al. 2013; Pranter et al. 2013）、滨岸（Massey et al. 2013; Rarity et al. 2013）、深海（Eschard et al. 2013）以及技术方法（Rittersbacher et al. 2013; Keogh et al. 2014）上的贡献[Howell 2014, pp. 15-16]。
- 与多点统计方法的联系：Caers & Zhang (2004) 提出 MPS 整合地质类似物，本文认为训练图像可直接源自露头量化数据[Howell 2014, pp. 6-7, 16]。
- 与多尺度建模的联系：引用 Ringrose et al. (2005, 2008) 和 Nordahl et al. (2005, 2014) 的工作，强调露头数据在表征单元体尺度建模中的必要性[Howell 2014, pp. 8-9, 15]。
- 与基于过程的建模的联系：Aas et al. (2014) 用 CFD 模拟浊积岩事件，可用于生成训练图像或直接构建地层构型[Howell 2014, pp. 15-16]。
- 与表面建模新范式的联系：Jackson et al. (2013) 提出脱离网格的表面建模方法，更利于非结构化模拟[Howell 2014, pp. 16]。

## Open Questions
- 如何建立行业统一的露头数据标准和术语体系，以实现不同来源数据的无缝整合？[Howell 2014, pp. 10]
- 如何系统量化并纳入露头数据本身的自然变异性和测量不确定性？[Howell 2014, pp. 9-10]
- 对于大尺度储层（数百米至千米级砂体），如何确保露头规模足够，或者如何合理组合多尺度、多位置的类似物信息？[Howell 2014, pp. 10]
- 细粒相（页岩、泥岩、碳酸盐胶结层）的几何数据严重不足，如何改进采集方法以修正预测偏差？[Howell 2014, pp. 9-10]
- 露头岩石物性（孔隙度、渗透率）受风化与成岩改造，如何建立更稳健的露头-地下物性转换模型？[Howell 2014, pp. 9-10]
- 多点地质统计（MPS）直接从露头生成训练图像的具体工作流和技术规范尚待成熟。[Howell 2014, pp. 16]
- 基于过程的模型（如CFD沉积模拟）在多大程度上可以替代或补充露头类似物，其验证标准是什么？[Howell 2014, pp. 15-16]
- 如何利用免费遥感数据自动提取现代沉积体系的几何参数并系统集成到类比数据库中？[Howell 2014, pp. 16]

## Source Coverage
所有非空的索引片段（共25个片段）均已处理并使用于本页面。编译后的源文本字符数为124,546（索引字符数123,941），覆盖率为100%（按片段计），覆盖比按字符计为1.0049。来源文件签名为 d110129accc62eb7267e54c2f34d13d9272ae36b，所有声明的证据均来自 Howell et al. 2014 这一单一文献的索引内容，未添加未经验证的外部事实。
