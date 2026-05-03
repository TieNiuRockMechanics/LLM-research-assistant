---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne"
title: "Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network."
status: "draft"
source_pdf: "data/papers/2025 - Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.pdf"
collections:
  - "zotero new"
citation: "Tian, Yongchao, et al. \"Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 9089-9125. doi:10.1007/s00603-025-04566-w."
indexed_texts: "26"
indexed_chars: "128191"
nonempty_source_blocks: "26"
compiled_source_blocks: "26"
compiled_source_chars: "126984"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990584"
coverage_status: "full-index"
source_signature: "867dcbedcee5ccc9d2f06e8dbe2b9d6b6d5cbd80"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:12:55"
---

# Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.

## One-line Summary

通过85块砂岩的巴西劈裂试验获取结构面，三维扫描提取41,760条剖面，经熵权‑TOPSIS排序等距选取100条剖面，采用数控雕刻制备结构面试样并在法向应力2 MPa下直剪，基于JRC‑JCS模型反算JRC值，建立了可靠、完备的剖面‑形态参数‑JRC数据集；利用因子分析消除形态参数信息重叠，构建以角度因子和高度因子为输入、JRC为输出的PSO‑RBF神经网络模型，实现对结构面表面形态的准确评估。

## Research Question

现有结构面形态量化方法（如目视对比法、直尺法、统计参数法、分形法等）存在缺乏严谨性的JRC值确定方式，且已有剖面‑JRC数据集因低清晰度、难以准确匹配、JRC值域宽泛、尺寸不一致等缺陷，难以满足精细研究需求；单一形态参数无法全面反映表面形态信息。如何利用系统直剪试验建立高可靠性数据集，并开发能融合多参数信息的表面形态评估模型？

## Study Area / Data

- 岩石类型：取自四川自贡的白色砂岩 [Tian 2025, pp. 17-18]。
- 巴西劈裂制样：85块砂岩，包含10块350 mm×350 mm×200 mm、45块150 mm×150 mm×150 mm、30块100 mm×100 mm×100 mm；筛选后合格试样为8块350 mm×350 mm、38块150 mm×150 mm、25块100 mm×100 mm [Tian 2025, pp. 12-13]。
- 三维激光扫描：FreeScan Combo计量级扫描仪，通过Geomagic与MATLAB处理点云，以0.25 mm采样间隔提取剖面，共获得41,760条剖面 [Tian 2025, pp. 13-15]。
- 剖面选取：利用熵权‑TOPSIS方法对41,760条剖面进行粗糙度排序，等间距（间距417条）选出100条剖面，编号J1–J100 [Tian 2025, pp. 15-17]。
- 数控雕刻试样：将所选100条剖面扩展为100 mm×100 mm×50 mm的三维结构面模型，在自贡白色砂岩上用DS‑4040三轴数控雕刻机加工制备 [Tian 2025, pp. 17-18]。
- 直剪试验条件：常法向荷载2 MPa，位移控制，剪切速率0.01 mm/s，目标位移8 mm [Tian 2025, pp. 18-19]。
- 砂岩基本力学参数：单轴抗压强度93.11 MPa，抗拉强度2.27 MPa，基本摩擦角25.3° [Tian 2025, pp. 17-18]。

## Methods

1. **代表性形态参数确定**：统计Rock Mechanics and Rock Engineering (RMRE) 2019年1月至2024年3月参数出现频率，结合物理意义，选定Z₂、θ\*ₘₐₓ/(C+1)、CLA、RMS、Rₚ、R\_z、Sₚ、θₐᵥₑ共8个参数 [Tian 2025, pp. 2-3]。
2. **原有剖面‑JRC数据集缺陷分析**：系统分析Barton (1976)、Bandis (1980)、Bandis et al. (1983)、Grasselli (2001)的剖面图与JRC值，指出清晰度低、匹配困难、值域宽泛、传统测量局限性、试验反算法主观性、目视对比法主观性、试样尺寸不一致七类不足 [Tian 2025, pp. 5-10]。
3. **新剖面‑JRC数据集建立**：
   - 三维激光扫描与点云处理：Geomagic手动/全局配准、降噪、去除离群点；MATLAB中坐标系重构（保证XOY、YOZ、XOZ平面相互垂直）、点云坐标调整、以0.25 mm间隔点云均匀化、剖面提取（100 mm×100 mm试样提取384条/个，150 mm×150 mm提取560条/个，350 mm×350 mm提取1360条/个） [Tian 2025, pp. 13-15]。
   - 剖面粗糙度排序：计算7个形态参数（不包括θ\*ₘₐₓ/(C+1)），采用熵权‑TOPSIS法评估各剖面贴近度，排序后等距选出J1–J100剖面 [Tian 2025, pp. 15-17]。
   - 数控雕刻与直剪试验：将J1–J100剖面延伸为三维模型，雕刻成100 mm×100 mm×50 mm试样，在法向应力2 MPa下进行直剪，记录载荷‑位移曲线 [Tian 2025, pp. 17-19]。
   - JRC反算：依据JRC‑JCS模型 \( \tau_p = \sigma_n \tan(\phi_b + JRC \log(JCS/\sigma_n)) \) 反算各试样对应剖面的JRC值，形成剖面‑形态参数‑JRC数据集 [Tian 2025, pp. 19-20]。
4. **形态参数与JRC关系建立**：分别建立8个参数与JRC的单参数回归模型，对比角度型参数（θ\*ₘₐₓ/(C+1)、θₐᵥₑ、Z₂、Rₚ）和高度型参数（RMS、CLA、Sₚ、R\_z）的预测精度 [Tian 2025, pp. 20-23]。
5. **因子分析**：对J1–J100的8个参数进行KMO检验（0.800）和Bartlett球形检验（显著0.000），通过主成分分析提取公因子，经Varimax旋转得到“角度因子”（F1）和“高度因子”（F2），累计解释方差95.145%，并计算因子得分 [Tian 2025, pp. 24-27]。
6. **PSO‑RBF神经网络建模**：以两条公因子为输入、JRC为输出构建RBF网络；采用粒子群优化算法（20个粒子，200次迭代，c1=1.4，c2=1.7）优化网络参数，适应度函数为RMSE；80条剖面训练，20条测试 [Tian 2025, pp. 27-30]。
7. **模型对比**：与传统RBF、DNN、线性回归、LSTM、随机森林、XGBoost、SVR等模型比较，选用R²、MAE、MBE、RMSE、MAPE等指标评估 [Tian 2025, pp. 30-34]。

## Key Findings

1. 已有文献中剖面JRC值主要依赖主观对比和粗糙面直剪反算，存在数据质量与尺寸不一等问题；基于100组数控雕刻结构面建立的剖面‑形态参数‑JRC数据集可靠性显著优于传统数据集 [Tian 2025, pp. 5-12]。
2. 8个代表性形态参数按其物理意义可分为角度型参数（Z₂、θ\*ₘₐₓ/(C+1)、Rₚ、θₐᵥₑ）和高度型参数（CLA、RMS、R\_z、Sₚ），同类参数间高度相关；因子分析提取的角度因子和高度因子可解释95.145%的方差，有效消除信息重叠 [Tian 2025, pp. 24-27]。
3. 单一参数预测JRC的Pearson相关系数均低于0.8，即使最优的θ\*ₘₐₓ/(C+1)和θₐᵥₑ（相关系数0.82、0.79）也难以准确评估粗糙度；角度型参数整体预测性能优于高度型参数 [Tian 2025, pp. 20-23]。
4. PSO‑RBF神经网络模型在测试集上平均相对误差5.9%，R²=0.5728，MAE=0.1025，MAPE=4.79%，综合性能优于线性回归、随机森林、XGBoost等模型，无过拟合和系统偏差 [Tian 2025, pp. 30-34]。
5. 基于100条剖面的JRC反算值，提出新的9组标准剖面（JRC区间0‑3、3‑6、6‑9、9‑11、11‑13、13‑15、15‑17、17‑19、19‑21），可作为更严谨的目视评价参照 [Tian 2025, pp. 23-24]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Z₂是历年出现频率最高的形态参数 | [Tian 2025, pp. 2-3] | RMRE 2019‑2024年统计 | 8个代表性参数之一 |
| 原有剖面‑JRC数据集存在七类缺陷（如清晰度低、匹配不准、尺寸不一等） | [Tian 2025, pp. 5-7] | 针对Barton (1976)、Bandis (1980)、Grasselli (2001)等 | 建议排除Bandis et al. (1983)数据 |
| Barton标准剖面雕刻试样直剪反算的JRC值与原始标定差异显著 | [Tian 2025, pp. 7-8] | 三级法向应力直剪 | 粗糙度排序亦发生改变 |
| 100组直剪试验参数统计：峰值强度1.6–2.5 MPa，峰值位移0.8–2.1 mm，残余强度1.2–1.8 MPa，残余强度比0.58–0.94，剪切刚度1.5–3.4 MPa/mm | [Tian 2025, pp. 18-19] | 2 MPa法向应力 | 峰值位移和剪切刚度离散系数达0.21‑0.22 |
| 单参数与JRC的Pearson相关系数：θ\*ₘₐₓ/(C+1) 0.82，θₐᵥₑ 0.79，Z₂ 0.79，Rₚ 0.78，RMS 0.67，CLA 0.65，R\_z 0.65，Sₚ 0.64 | [Tian 2025, pp. 20] | 100条剖面反算JRC | 所有相关系数<0.8，角度型优于高度型 |
| 因子分析：KMO=0.800，Bartlett显著性0.000；两个公因子累计贡献率95.145% | [Tian 2025, pp. 24-27] | 100剖面8参数 | F1为角度因子，F2为高度因子 |
| PSO‑RBF模型测试集平均相对误差0.059，R²=0.5728，MAE=0.1025，RMSE=0.1366，MAPE=4.79% | [Tian 2025, pp. 30, 33‑34] | 训练80/测试20 | 优于线性回归、随机森林、XGBoost等 |
| 新标准剖面9组，每组从对应JRC区间选出 | [Tian 2025, pp. 23-24] | 剖面平滑、JRC居区间中值、参数排序一致 | 可替代Barton标准剖面 |

## Limitations

- 直剪试验仅在法向应力2 MPa下进行，未覆盖其他应力水平 [Tian 2025, pp. 18-19]。
- 岩石类型仅限于自贡白色砂岩，未验证其他岩性 [Tian 2025, pp. 17-18]。
- 人工雕刻表面与天然粗糙面的微细观特征可能存在差异 [Tian 2025, pp. 17-18]。
- 样本量100组，对神经网络而言仍属较小规模，模型泛化能力需更多数据检验 [Tian 2025, pp. 19-20]。
- 模型基于二维剖面信息构建，未直接利用三维形貌参数 [Tian 2025, pp. 13-15]。
- 剪切方向仅为单一方向，未考虑粗糙度各向异性 [Tian 2025, pp. 7, 11]。
- 试验中峰值位移和剪切刚度离散性较大，可能受机械误差与人为误差影响 [Tian 2025, pp. 19-20]。

## Assumptions / Conditions

- 法向应力2 MPa，代表中等高度边坡的自重应力水平 [Tian 2025, pp. 18-19]。
- JRC反算采用JRC‑JCS模型，假定JCS等于完整岩石单轴抗压强度，基本摩擦角25.3° [Tian 2025, pp. 18, 20]。
- 采样间隔0.25 mm认为足以捕捉有效粗糙信息 [Tian 2025, pp. 13]。
- JRC分组时，0‑3区间定为平直线（JRC=0），其余每组选一代表性剖面 [Tian 2025, pp. 23]。
- 因子分析前采用标准差标准化，KMO>0.8和Bartlett检验显著确认数据适用 [Tian 2025, pp. 24-25]。
- PSO参数设置：粒子数20，最大迭代200，学习因子c1=1.4，c2=1.7 [Tian 2025, pp. 27]。
- 训练/测试按80:20比例随机划分 [Tian 2025, pp. 27]。

## Key Variables / Parameters

- **形态参数**：[[Z₂]]、[[θ*max/(C+1)]]、[[CLA]]、[[RMS]]、[[Rp]]、[[Rz]]、[[Sp]]、[[θave]] [Tian 2025, pp. 2-3]。
- **粗糙度系数**：[[JRC]]（节理粗糙度系数） [Tian 2025, pp. 1]。
- **力学参数**：峰值强度τₚ、法向应力σₙ、基本摩擦角φ_b、节理壁抗压强度JCS [Tian 2025, pp. 7, 18]。
- **直剪试验指标**：[[峰值位移]]、[[残余强度]]、[[残余强度比]]、[[剪切刚度]] [Tian 2025, pp. 18-19]。
- **因子分析公因子**：[[角度因子]]（F1）、[[高度因子]]（F2） [Tian 2025, pp. 27]。
- **网络超参数**：PSO粒子数、迭代次数、学习因子c1,c2；RBF扩展速度 [Tian 2025, pp. 27]。
- **模型评估指标**：R²、MAE、MBE、RMSE、MAPE [Tian 2025, pp. 30]。

## Reusable Claims

1. 现有文献中的剖面‑JRC数据集（Barton, 1976; Bandis, 1980; Grasselli, 2001等）因清晰度低、匹配不准、值域宽泛、尺寸不一致等原因，不适用于精细的形态量化研究，引用时需审慎 [Tian 2025, pp. 5-10]。
2. 基于100组数控雕刻结构面直剪试验建立的剖面‑形态参数‑JRC数据集，覆盖JRC约1.5–14，可靠性与完备性显著优于传统数据集，可用于验证或训练形态评估模型 [Tian 2025, pp. 15-17, 20]。
3. 8个常用形态参数可归纳为角度型参数（Z₂, θ\*ₘₐₓ/(C+1), Rₚ, θₐᵥₑ）和高度型参数（CLA, RMS, R\_z, Sₚ），同类参数信息高度重叠；通过因子分析提取的角度因子与高度因子可解释95.1%的总方差 [Tian 2025, pp. 24-27]。
4. 单参数不可能精确预测JRC，即使最优参数θ\*ₘₐₓ/(C+1)和θₐᵥₑ的Pearson相关系数也仅约0.8，角度型参数预测性能整体优于高度型参数 [Tian 2025, pp. 20-23]。
5. 以角度因子和高度因子为输入的PSO‑RBF神经网络模型，在测试集上平均相对误差约5.9%，且无明显过拟合和系统偏差，推荐作为结构面粗糙度评估的优先模型 [Tian 2025, pp. 30-34]。
6. 新提出的9组标准剖面可作为Barton标准剖面的改进方案，每组剖面均从具有明确JRC反算值的自然扩展结构面中选取 [Tian 2025, pp. 23-24]。
7. 直剪试验曲线可分为压密、弹性增长、塑性增长、峰后四个阶段，峰后具有恒定、缓慢下降、急剧下降三种模式，分别对应不同的粗糙面退化机制 [Tian 2025, pp. 18-19]。

## Candidate Concepts

- [[结构面表面形态]] (Surface morphology of structural plane)
- [[节理粗糙度系数(JRC)]] (Joint Roughness Coefficient)
- [[代表性形态参数]] (Representative morphology parameters)
- [[剖面‑形态参数‑JRC数据集]] (Profile‑morphology parameter‑JRC dataset)
- [[角度型参数与高度型参数]] (Angle‑type and height‑type parameters)
- [[因子分析降维]] (Factor analysis for dimensionality reduction)
- [[角度因子与高度因子]] (Angle factor and height factor)
- [[PSO‑RBF神经网络]] (PSO‑RBF neural network)
- [[标准剖面系列]] (Standard profile series)
- [[直剪试验峰后行为]] (Post‑peak behavior in direct shear)
- [[数控雕刻结构面]] (CNC‑engraved structural planes)

## Candidate Methods

- [[剖面目视对比法]] (Visual comparison method)
- [[直尺法]] (Straight‑edge method)
- [[试验结果反算法]] (Experimental result inversion method)
- [[统计参数法]] (Statistical parameter method)
- [[分形几何法]] (Fractal geometry method)
- [[熵权‑TOPSIS方法]] (Entropy weight‑TOPSIS)
- [[三维激光扫描与点云处理]] (3D laser scanning and point cloud processing)
- [[数控雕刻技术 (CNC engraving)]]
- [[常法向荷载直剪试验]] (Direct shear test under constant normal load)
- [[JRC‑JCS模型反算]] (Back‑calculation via JRC‑JCS model)
- [[主成分分析与Varimax旋转]] (PCA with Varimax rotation)
- [[PSO算法优化RBF网络]] (Particle swarm optimization for RBF network)
- [[模型性能比较指标 (R², MAE, MAPE等)]] (Model evaluation metrics)

## Connections To Other Work

- 系统梳理了Barton (1976)、Bandis (1980)、Bandis et al. (1983)、Grasselli (2001)的剖面‑JRC数据集，指出其不足，并建议排除Bandis et al. (1983)数据 [Tian 2025, pp. 8-12]。
- 与Tse and Cruden (1979)、Yu and Vayssade (1991)、Yang et al. (2001)、Tatone and Grasselli (2010)、Li and Zhang (2015)等的经验模型对比，发现历史模型在新数据集上预测误差较大（相对误差普遍>0.15） [Tian 2025, pp. 20]。
- 形态参数选取参考了多篇文献的频率统计，Z₂在历年RMRE中出现频率最高，与Gao et al. (2015)、Du et al. (2022)等一致 [Tian 2025, pp. 2-3]。
- 因子分析思路与Zhang et al. (2014)、He et al. (2024)等尝试多参数联合表达形态特征的研究相联系 [Tian 2025, pp. 2, 24]。
- 模型对比引入DNN、LSTM、随机森林、XGBoost、SVR等，与岩石力学领域机器学习应用趋势相呼应 [Tian 2025, pp. 30-34]。

## Open Questions

- 模型在不同法向应力水平（如高应力>2 MPa或低应力）下的适用性尚待验证 [Tian 2025, pp. 18-19]。
- 仅基于二维剖面信息，如何有效融合三维形貌参数（如三维粗糙度指标）以进一步提高评估精度？ [Tian 2025, pp. 13, 29]
- 新提出的标准剖面系列能否推广至其他岩性（如花岗岩、大理岩）及不同成因结构面？ [Tian 2025, pp. 17-18]
- 剪切方向与粗糙度各向异性的影响未被纳入，未来需开展多方向剪切试验并引入方向性参数 [Tian 2025, pp. 7, 11]。
- 因子分析仅提取两个公因子，是否存在更高阶交互作用，可否通过增加样本量进一步挖掘？ [Tian 2025, pp. 24-27]
- PSO‑RBF神经网络在更大规模数据集上的泛化能力及实时预测潜力需进一步测试 [Tian 2025, pp. 30]。

## Source Coverage

本文档基于论文全部已索引片段编写。共处理26个非空源块，总计128,191个字符索引。已编译源块数26，编译源字符数126,984。所有非空索引片段均已使用。覆盖比率（按块计）1.0，覆盖比率（按字符计）0.990584。索引签名：867dcbedcee5ccc9d2f06e8dbe2b9d6b6d5cbd80。状态：完整索引，单次编译。
