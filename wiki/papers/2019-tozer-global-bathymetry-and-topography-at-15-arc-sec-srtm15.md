---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-tozer-global-bathymetry-and-topography-at-15-arc-sec-srtm15"
title: "Global Bathymetry and Topography at 15 Arc Sec: SRTM15+."
status: "draft"
source_pdf: "data/papers/2019 - Global Bathymetry and Topography at 15 Arc Sec SRTM15+.pdf"
collections:
  - "山西断裂地质构造"
citation: "Tozer, B., et al. \"Global Bathymetry and Topography at 15 Arc Sec: SRTM15+.\" *Earth and Space Science*, 2019, doi:10.1029/2019EA000658."
indexed_texts: "17"
indexed_chars: "81479"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81844"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00448"
coverage_status: "full-index"
source_signature: "15bfc4b1d041fccbf790361dc16b9e18c211c460"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T00:34:08"
---

# Global Bathymetry and Topography at 15 Arc Sec: SRTM15+.

## One-line Summary

SRTM15+V2.0 是一个融合最新船测水深、多卫星高度计重力反演水深和陆地 DEM 的全球 15 弧秒（赤道约 500 m）高程网格，船测约束覆盖仅占洋底 10.84%，高度计预测水深在深海的均方根误差约 ±150 m。

## Research Question

如何融合大量新增的船载声学测深数据和新一代卫星高度计（CryoSat-2, SARAL/AltiKa, Jason‑2）数据，生产一个空间采样间隔 15 弧秒的全球统一水深与地形网格，并评估其改进的精度、空间分辨率和误差特性。

## Study Area / Data

- **海洋水深**：全球海洋，纬度 ±80° 至部分高纬度区域，来自船载单波束/多波束测量及卫星高度计反演预测水深。
- **陆地地形**：纬度 85°N–60°N 使用 ArcticDEM，60°N–56°S 使用 SRTM CGIAR‑CSI V4.1，56°S–62°S 使用 ASTER GDEM V2，62°S–90°S 使用 REMA。
- **船测数据集**：包含 NGDC_UNOLS, JAMSTEC, NGDC_GEODAS, SIO_MISC, NGA, AGSO, IBCAO, GEOMAR, GEBCO_IHO, CCOM, NOAA_US, NGA_DNC, IFREMER, LAKES, 3DGBR, NA VOCEANO 等机构提供的 >33.6 百万个经质量控制与编辑的 15 弧秒格点。
- **高度计数据**：CryoSat‑2 48 个月、SARAL/AltiKa 14 个月（原文表 3 中 AltiKa 累计 33 个月，新增 12 个月）、Jason‑2 12 个月的非重复轨道海面斜率测量，用于构建重力模型 V27。
- **辅助数据**：GSHHG 海岸线、IBCAO v3 北极网格（>80°N）、EGM96 大地水准面模型（用于大地高到正高转换）。

## Methods

1. **预测水深生成（1 分网格，±80°）**  
   - 将船测水深格网化到 1 分墨卡托网格（张力样条，拉力因子 0.6），并与 GEBCO 1 分手绘等深线浅水网格合并，形成无重力参与的初始水深。  
   - 用高斯滤波（0.5 增益波长 160 km）分离低通和高通成分；对重力异常做相同滤波。  
   - 通过拉普拉斯方程将高通重力向下延到低通水深深度，并用深度依赖的 Wiener 滤波器（长度尺度 5.9 km）稳定求解。  
   - 在重叠的区域（搜索半径约 160 km，动态调整）内对高通声学水深与延拓后的高通重力做稳健线性回归，得到区域性的水深‑重力比率（线性相关系数图），对沉积覆盖导致的非线性区还估计正/负重力下的斜率。  
   - 将比率网格乘以高通‑延拓重力得到高通预测水深，再与低通水深相加。  
   - 最后用船测点重置真实水深，并用最小曲率插值将周围预测值“抛光”至测量值，海岸线点约束零深度并移除伪岛屿。  

2. **15 弧秒全球水深（移除‑插值‑恢复）**  
   - 将 1 分预测水深和 IBCAO v3（>80°N）插值到像素注册的 15 弧秒（6 个重叠纬度带，拉力因子 0.35）。  
   - **移除**：计算船测点处的预测水深残差，并距离真实测深 ≥10 km 的格点添加零值，抑制外推震荡。  
   - **插值**：用张力三次样条（拉力 0.55）在 6 个带内分别插值残差/零值网格。  
   - **恢复**：将插值残差与预测基础网格相加，得到与船测数据无缝吻合的 15 弧秒水深。  

3. **陆地地形拼接**  
   - 将 ArcticDEM、SRTM CGIAR‑CSI V4.1、ASTER GDEM V2、REMA 统一至 WGS84 地理坐标、像素注册、15 弧秒分辨率（高斯滤波σ 6 倍对应 1 km 波长或块中值‑表面插值），并用 EGM96 模型将 ArcticDEM 和 REMA 的大地高转换为正高。  
   - 按优先顺序拼接（grdblend），用 GSHHG 海岸线裁剪以隔离陆地。  

4. **最终合成**  
   - 将陆地网格与海洋网格沿 GSHHG 海岸线合并，所有网格节点像素注册。

## Key Findings

1. SRTM15+V2.0 的船测数据覆盖了洋底面积的 10.84%（15 弧秒）和 18.29%（30 弧秒），较 SRTM15_PLUS 提升 1.24%。  
2. 卫星重力模型 V27 的相干性截止波长由 ~21.5 km 改善至 ~12.5 km（半波长分辨率从 ~11.25 km 提升至 ~6.25 km），均方根精度从 2.05 mGal（V18）提高至 1.33 mGal。  
3. 高度计预测水深的均方根误差在深海约 ±150 m，海岸至陆坡区约 ±180 m，且误差更符合拉普拉斯分布而非高斯分布。  
4. 新加入的多波束数据（如 MH370 搜索区、Mendocino 复合测线、SWIM 等）大幅提升了局部短波长信息，例如 MH370 区域 V2.0 的功率谱在 ≤20 km 波长比 V1 高约 10–500 倍。  
5. 陆地部分因 ArcticDEM 和 REMA 的引入，高纬度和南极的地形细节显著改善，且通过大地水准面修正消除了 SRTM15_PLUS 中的长波系统误差。

## Core Evidence Table

| Evidence                                                                                                                          | Source                               | Conditions                                              | Notes                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 船测约束格点占全球洋底 10.84%（15 弧秒）                                                                                         | Table 2 & 正文 pp. 3-4               | 15 弧秒网格，数据经去重、编辑                          | 来自 NGA、JAMSTEC 等新增数据                                                             |
| 重力模型 V27 与船测重力比较的均方根误差 1.33 mGal，相干半波长 6.25 km                                                              | Fig. 2 & 正文 pp. 5-6                 | 基于全球船测重力的对比                                   | V18 的对应值为 2.05 mGal、11.5 km 半波长                                                |
| 预测水深在深海的均方根误差 ±150 m，近岸 ±180 m                                                                                   | Fig. 8 & 正文 pp. 11-12              | 与 50 条独立船测航线对比                                 | 近岸不确定性更大，误差分布接近拉普拉斯                                                   |
| 1 分预测水深网格（V27）的全球线性相关系数（水深‑重力）在沉积覆盖薄区高，被厚沉积区（如老洋盆、宽陆架）低（≤0.3）                   | Fig. 3 & 正文 pp. 7-8                 | 12–160 km 波长带                                       | 低相关区假定平坦海底                                                                     |
| MH370 搜索区多波束数据使 V2.0 在 ≤20 km 波长的功率比 V1 高 10–500 倍，相干性在 ≥12 km 保持 >0.5                                     | Fig. 6 & 正文 pp. 11                 | 多波束与预测水深对比                                     | 预测水深在 >12 km 波长可捕获特征，短波长信息来自多波束                                   |
| 全球陆地部分的高纬度影像因 ArcticDEM 和 REMA 的替换消除了 ASTER 的轨道条带，并修正了大地高到正高的偏差                            | Fig. 5 & 正文 pp. 9-11               | 纬度 >60°N 和 >60°S                                   | 长波变化由大地水准面改正引起                                                             |
| 全球测高双峰分布：最深模态在 ~5100 m 和 ~4250 m，解释为岩石圈冷却沉降和板内火山热点隆起                                        | Fig. 9 & 正文 pp. 13-14              | 100 m 间隔的全球测高曲线                               | 与 Smith and Sandwell (1997) 随机再加热模型一致                                         |

## Limitations

- 尽管新增了大量船测数据，但全球洋底仍有约 89.16% 的区域（15 弧秒）未得到船载声学约束，水深来自重力场预测，空间分辨率约 6 km（半波长）。  
- 预测水深在沉积厚覆盖区和大陆边缘的校准困难，水深‑重力关系可能非线性，仅采用分正/负重力斜率近似。  
- 岸线匹配使用 GSHHG，局部可能偏移数百米，在 15 弧秒分辨率下被认为可接受，但高分辨率应用中需注意。  
- 误差分布虽整体近似拉普拉斯，但不同航次间有变异，尚未按地质环境精细分类。  
- 陆地 DEM 如 ArcticDEM 和 REMA 为“首次回波”高程，可能包含植被或浅表覆盖物而非裸地，在 15 弧秒尺度下影响被认为可接受。

## Assumptions / Conditions

- 在沉积物较薄、地形起伏远小于平均海深的区域，水深‑重力传递函数为常数（由地壳‑海水密度差决定，2,800 kg/m³ 对应 13.25 m/mGal），因此可用线性回归。  
- 当重力与水深的线性相关系数 ≤0.3 时，假定海底平坦，将水深‑重力比设为零。  
- 向下延拓采用的 Wiener 滤波器长度（5.9 km）是基于当前重力格网分辨率与噪声水平的经验选择；未来重力模型改善可进一步缩短。  
- 船测水深被假定为“地面真值”，用于校准预测水深和插值残差，其自身含有的导航、声速改正等误差未在预测不确定性中单独量化。  
- 各陆地 DEM 均已转换为 WGS84 地理坐标和大地水准面参考（正高），且拼接在 GSHHG 零等深线处连续。

## Key Variables / Parameters

- 网格采样间隔：15 arc sec（像素注册）  
- 重力‑水深 Wiener 滤波器长度：5.9 km  
- 高低通分离的高斯滤波波长：160 km（0.5 增益）  
- 1 分预测网格的张力样条拉力因子：0.6  
- 15 弧秒插值拉力因子：0.35（初始插值）、0.55（残差插值）  
- 高程正高转换参考大地水准面：EGM96  
- 重力模型版本：V27.1  
- 主要高度计测距精度：AltiKa 20.5 mm，CryoSat‑2 43.7 mm，Jason‑2 43.0 mm  

## Reusable Claims

- 在 15 弧秒网格分辨率下，全球洋底仅有约 10.84% 的区域被船载声学数据直接约束，其余由卫星重力场反演，半波长分辨率约 6 km。（条件：当前公开船测数据集，未包含保密数据）  
- 在深海（远离海岸和陆坡），高度计预测水深的均方根误差约为 ±150 m，近岸区域增至 ±180 m，且误差更符合拉普拉斯分布。（条件：与独立船测航线对比）  
- 重力模型 V27 的最小可恢复重力异常半波长约为 6.25 km（相干性 ≥0.25），对应预测水深能分辨间距大于 ~6 km 的狭窄特征。  
- 在沉积物极厚的区域（线性相关系数 ≤0.3），水深‑重力关系失效，模型默认海底平坦并设比率为零，这类区域的预测水深不确定性可能更大。  
- 使用张力样条与移除‑插值‑恢复方法可将低分辨率预测水深和稀疏船测数据融合为无缝 15 弧秒网格，且在船测点吻合，空白区域平滑过渡。

## Candidate Concepts

- [[卫星高度计测深]]（satellite altimetry bathymetry）  
- [[预测水深]]（predicted bathymetry）  
- [[重力‑水深传递函数]]（gravity‑topography transfer function）  
- [[移除‑插值‑恢复]]（remove‑interpolate‑restore）  
- [[Wiener 滤波器]]（Wiener filter for downward continuation）  
- [[拉普拉斯误差分布]]（Laplacian error distribution）  
- [[全球测高双峰分布]]（bimodal global hypsometry）  
- [[海底平坦假设]]（flat‑seafloor assumption for low correlation）  
- [[大地水准面校正]]（geoid correction, EGM96）  
- [[像素注册]]（pixel registration）  

## Candidate Methods

- [[高频重力向下延拓与拉普拉斯方程]]  
- [[重叠区段线性/非线性回归建立水深‑重力比]]  
- [[二维快速傅里叶变换（FFT）多带高斯滤波]]  
- [[张力样条格网化（surface）]]（GMT surface with tension）  
- [[块中值重采样（blockmedian）与再格网化]]  
- [[多带移除‑插值‑恢复，附加零值抑制外推]]  
- [[多源DEM拼接与垂直基准统一（grdblend, grdsample, grdmath）]]  

## Connections To Other Work

- 该模型是 SRTM 系列数字高程模型的延续，直接前身包括 SRTM30_PLUS (Becker et al., 2009) 和 SRTM15_PLUS (Olson et al., 2016)，预测水深算法源于 Smith and Sandwell (1994, 1997)。  
- 重力模型 V27 及波形重跟踪技术承袭自 Sandwell & Smith (2005, 2009)、Garcia et al. (2014) 和 Zhang & Sandwell (2017)。  
- 全球测高曲线及峰值的解释与 Smith and Sandwell (1997)、Sandwell and Smith (2001) 的板块冷却‑随机再加热模型一致。  
- 船测数据贡献方包括 NGA、JAMSTEC、GA (MH370 搜索)、SWIM 和 CCOM/SIO Mendocino 等区域调查，分别对应各自的文献。  
- 未来计划与 Seabed 2030 (Mayer et al., 2018) 高度互补，并准备吸纳 SWOT 宽刈幅高度计和 ICESat‑2 激光测深数据。

## Open Questions

- 如何进一步获取并向公众开放目前尚属私有的船测数据，以提高全球约束比例？  
- 沉积厚覆盖区（如老洋盆、宽陆架）的非线性水深‑重力关系能否用更复杂的物理模型（而非简单双斜率）改善？  
- 各航次预测误差分布差异背后的地质/海洋学机制是什么（Sepúlveda et al., 2019 正在研究）？  
- 当前 15 弧秒网格是否足以捕捉大陆边缘陡峭地形和海底噪声在近岸模型（如海啸传播）中的效应？  
- 新一代 SWOT 宽刈幅雷达和 ICESat‑2 激光测深能够将浅水区的空间分辨率和精度提高到什么程度？  
- 全球深海测深的覆盖率在不依赖船舶声学的前提下，是否存在通过重力场进一步逼近亚公里分辨率的理论极限？

## Source Coverage

本页面的所有内容均严格依据论文的 17 个已索引片段汇编而成。  
- 已被处理的非空源块数量：17  
- 源块字符总数：81,479  
- 编译后覆盖的源块数：17  
- 编译输出字符数：81,844  
- 字符覆盖率：100.45%（因 Markdown 格式增加少量字符）  

所有非空索引片段均被完整处理，无遗漏。
