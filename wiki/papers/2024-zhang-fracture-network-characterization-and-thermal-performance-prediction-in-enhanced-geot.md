---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot"
title: "Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model."
status: "draft"
source_pdf: "data/papers/2025 - Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete.pdf"
collections:
citation: "Zhang, Kun, and Hui Wu. \"Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.\" *Water Resources Research*, 2024, doi:10.1029/2024WR039452. Accessed 2026."
indexed_texts: "20"
indexed_chars: "98108"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "98541"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004414"
coverage_status: "full-index"
source_signature: "8b11d742c41e0875aa2bfda16b187c0b839a407b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:26:01"
---

# Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.

## One-line Summary
该研究提出一种集成反演框架，通过固定几何背景裂缝网络参数化、协方差矩阵自适应进化策略（CMA‑ES）及嵌入式离散裂缝模型（EDFM），利用保守/吸附双示踪剂与压力数据表征增强型地热系统（EGS）裂缝网络，并实现对长期热采性能的准确预测与不确定性量化 [Zhang 2024, pp. 1-1, 6‑7].

## Research Question
如何利用有限的井中示踪剂突破曲线及压力观测数据，高维且病态地反演深层增强型地热储层中未知数量、位置、产状与开度的裂缝网络，并在此基础上可靠预测储层长期热产出？ [Zhang 2024, pp. 1-2, 2‑3]

## Study Area / Data
- **研究案例**：三个合成EGS案例（Case 1：简单正交裂缝网络，9条裂缝；Case 2：复杂裂缝网络，含一条主水力裂缝与15条天然裂缝；Case 3：三维裂缝网络，含椭圆与矩形裂缝且开度非均匀） [Zhang 2024, pp. 7-8].
- **观测数据**：注入井以脉冲方式释放示踪剂，生产井监测40小时的保守与吸附两种示踪剂突破曲线（BTC），每条BTC含105个数据点；同时记录注入‑生产井间稳态压差作为辅助约束 [Zhang 2024, pp. 8-9].
- **储层条件**：基质为低渗干热岩（渗透率1×10⁻²⁰ m²），饱和水；2D案例初始温度200℃、压力34 MPa；3D案例考虑地温梯度，中深部温度200℃、压力30 MPa [Zhang 2024, pp. 8-9].
- **热产出参考数据**：50年生产温度曲线（井底条件），用于验证反演模型的预测能力 [Zhang 2024, pp. 8-9, 14].

## Methods
1. **裂缝网络参数化**  
   - 采用固定几何的背景裂缝网络（19×19条正交裂缝用于2D，9×9条用于3D），每条裂缝由三个参数描述：有效段中心位置 \(x_c\)、有效段长度 \(x_l\)、有效段均匀开度 \(x_a\)；两端设过渡段，开度从 \(x_a\) 平滑递减至默认极小值（0.04 mm），无效段不参与流动 [Zhang 2024, pp. 3-4].
   - 该参数化既回避裂缝数目不确定问题，又通过调整各裂缝有效段组合出近似真实裂缝的水力等效网络 [Zhang 2024, pp. 2-3, 19].

2. **反演算法：CMA‑ES**  
   - 采用协方差矩阵自适应进化策略（CMA‑ES），以正态分布采样候选解，利用加权重组与协方差自适应更新最优搜索方向 [Zhang 2024, pp. 4-5].
   - 适应度函数：模拟与观测示踪剂及压差的马氏距离 \(O(\mathbf{x}) = (\mathbf{y}_{obs} - \mathbf{y}(\mathbf{x}))^T \mathbf{C}_D^{-1} (\mathbf{y}_{obs} - \mathbf{y}(\mathbf{x}))\) [Zhang 2024, pp. 4-5].
   - 对裂缝参数实施正态得分变换后反演 [Zhang 2024, pp. 6].
   - 种群大小设为30，最大迭代2000代，使用“pycma”开源实现 [Zhang 2024, pp. 11, 4‑5].

3. **不确定性评估**  
   - 执行多次独立CMA‑ES运行（15次/3次），收集各运行终止时的低误差解集合 \(S_d = \{ \mathbf{x}: \delta(\mathbf{x}) \le \hat{\delta} \}\)，合并为整体后验模型集 [Zhang 2024, pp. 5-6].
   - 终止准则：以归一化示踪浓度RMSE低于预设阈值（Case1: 0.023; Case2: 0.005; Case3: 0.03）后，再额外运行200代以防止模式坍塌，从最后一代抽取后验实现 [Zhang 2024, pp. 11-12, 15, 17].

4. **正演模型：EDFM**  
   - 基于嵌入式离散裂缝模型的非拟合网格，分别求解基质与裂缝中的单相流、热量输运及示踪剂运移方程（吸附‑弥散方程）；裂缝渗透率按立方定律由开度计算 [Zhang 2024, pp. 6-7].
   - 利用开源多物理场平台GEOS实施，溶质运移仅在裂缝中求解 [Zhang 2024, pp. 7].

5. **整体反演‑预测流程**  
   - 每次迭代用CMA‑ES更新参数→构建裂缝网络→嵌入矩阵网格→EDFM计算示踪剂与压差→计算适应度→更新参数，直至满足终止准则；随后用后验模型集进行50年热采预测 [Zhang 2024, pp. 7].

## Key Findings
- 该框架能捕获“真实”裂缝网络中的主要流动通道与水力连通性，即使背景裂缝几何与真实裂缝取向不一致（如Case 2），也能获得与示踪剂数据高度匹配的水力等效模型 [Zhang 2024, pp. 12, 16‑17].
- 相比先验模型，后验模型显著降低了长期生产温度的预测不确定性；Case 1平均预测误差＜6°C，Case 3早期10年内平均误差＜8°C [Zhang 2024, pp. 14, 17, 18‑19].
- 通过控制RMSE终止阈值可平衡数据拟合质量与参数不确定性，阈值过大会高估不确定性，过小则导致模型坍塌 [Zhang 2024, pp. 12, 15].
- CMA‑ES能够探索多模态参数空间，多次独立运行可提供合理的后验不确定性分布，适用于实际储层反演 [Zhang 2024, pp. 19-20].
- 三维案例中，即使反演模型将真实非均匀开度场近似为均匀开度，仍能将生产温度预测误差控制在10°C以内 [Zhang 2024, pp. 18].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 后验示踪剂BTC与参考BTC高度吻合，Case 1保守示踪剂RMSE≈0.023，Case 2 RMSE≈0.005，Case 3 RMSE≈0.03 | [Zhang 2024, pp. 12 Fig.7, 15 Fig.12, 17 Fig.15] | 使用了终止阈值后的后验模型集；3D案例采用0.03阈值 | 双示踪剂联合反演有效约束了流动与吸附特征 |
| 后验模型生产温度预测显著优于先验：Case 1整体平均误差＜6°C，Case 2误差更低，Case 3早期10年平均误差＜8°C | [Zhang 2024, pp. 14 Fig.10, 17 Fig.14, 19 Fig.17] | 50年热采模拟，注水温度50℃ | 后验预测区间覆盖参考温度曲线 |
| 多次独立CMA‑ES运行所得后验模型参数空间集中且保有多样性，如Case 1中14/15次运行达到阈值，参数空间适度收缩 | [Zhang 2024, pp. 12-14, Fig.8] | RMSE阈值0.023时，裂缝开度与长度后验分布集中 | 表明该方法可量化参数不确定性 |
| 3D案例中反演模型的均匀开度近似导致预测误差略大于2D案例，但整体仍可接受（平均误差＜10°C） | [Zhang 2024, pp. 18-19] | 真实裂缝开度非均匀分布，反演模型仅有一致开度 | 反演框架对非均匀性具有一定的鲁棒性 |

## Limitations
- 框架难以精细解析裂缝空间分布细节，限制了其在精确井位部署等工程决策中的应用 [Zhang 2024, pp. 19-20].
- CMA‑ES的终止准则依赖具体问题，RMSE阈值需经验确定，缺乏普遍自适应方法 [Zhang 2024, pp. 11, 20].
- 当前正演模型未耦合应力‑裂缝演化或强烈水岩反应等物理机制，预测能力局限于纯热‑流过程 [Zhang 2024, pp. 20].
- 反演采用均匀有效开度假设，无法还原裂缝内部的非均匀开度场，可能导致流动通道刻画偏差 [Zhang 2024, pp. 18].

## Assumptions / Conditions
- 背景裂缝网络几何（密度、取向）根据露头、岩心、地应力等先验信息预设，反演期间固定不变 [Zhang 2024, pp. 3, 9‑10].
- 每条背景裂缝的有效孔缝由中心、长度和均匀开度三参数定义，过渡段开度平滑连接有效段与无效段（默认开度0.04 mm），无效段不参与流动 [Zhang 2024, pp. 3-4].
- 示踪剂测试期间储层温度场几无变化，忽略水密度随温压的变化；保守与吸附示踪剂联合反演时，基质中示踪剂运移可忽略 [Zhang 2024, pp. 7, 8].
- 热模拟中采用局部热平衡假设，裂缝与基岩同步换热 [Zhang 2024, pp. 6].
- 储层为饱和水，基质极低渗（10⁻²⁰ m²），流体为单相水；裂缝渗透率遵从立方定律 [Zhang 2024, pp. 6].
- 边界条件：流体无流动边界，热模拟绝热边界；注入井定流量，生产井定压 [Zhang 2024, pp. 8-9].

## Key Variables / Parameters
- 裂缝有效中心位置 \(x_c\)、有效长度 \(x_l\)、有效开度 \(x_a\) [Zhang 2024, pp. 3-4]
- 示踪剂突破曲线浓度观测值 \(\mathbf{y}_{obs}\) 与模拟值 \(\mathbf{y}(\mathbf{x})\) [Zhang 2024, pp. 4-5]
- 示踪剂浓度RMSE终止阈值 \(\hat{\delta}\) [Zhang 2024, pp. 11-12, 15]
- CMA‑ES种群大小 λ（=30）、最大迭代代数（2000）、学习率 \(c_1, c_\eta\) [Zhang 2024, pp. 4-5, 11]
- 裂缝‑基质交换面积 \(A_{m,f}\)、非均质长度标度、热物性（见表1） [Zhang 2024, pp. 6-7, 9]

## Reusable Claims
- **具有固定几何背景裂缝网络与非均匀开度的参数化方法**能在不预设裂缝数量的情况下，形成能近似真实裂缝流动特性的水力等效网络，适用于高维病态裂缝反演 [Zhang 2024, pp. 3-4, 19].
- **条件**：背景裂缝的密度与取向需通过地质信息大致约束；采用有效段‑过渡段‑无效段的参数化，有效段开度为常数。
- **CMA‑ES算法配合多次独立运行与合适的终止准则**可同时实现最优裂缝参数反演与不确定性量化，并避免模式坍塌 [Zhang 2024, pp. 5-6, 12‑13, 19‑20].
- **条件**：使用双示踪剂及压力数据联合约束；终止RMSE阈值需根据问题特性调试；实施多次（例如≥15次）独立运行。
- **EDFM与CMA‑ES的集成**大幅降低了裂缝反演中因几何更新引起的重网格化成本，使随机优化类方法在裂缝表征中成为可行选择 [Zhang 2024, pp. 2-3, 7].
- **条件**：利用EDFM非拟合网格，仅更新裂缝网格；正演模拟在GEOS框架中实现。
- **基于水力等效的后验裂缝模型能够准确预测EGS长期热产出**，即使反演模型几何与真实网络有偏差，只要示踪剂和压力数据匹配良好，热预测误差可控制在约10°C以内 [Zhang 2024, pp. 14, 16‑17, 18‑19].
- **条件**：后验模型须通过多个低误差解构成的后验集合来表征；预测期不超过所验证的50年范围。

## Candidate Concepts
- [[enhanced geothermal system (EGS)]]
- [[hot dry rock (HDR)]]
- [[fracture network characterization]]
- [[covariance matrix adaptation evolution strategy (CMA-ES)]]
- [[embedded discrete fracture model (EDFM)]]
- [[tracer breakthrough curve (BTC)]]
- [[sorptive tracer]]
- [[conservative tracer]]
- [[hydraulic equivalence]]
- [[uncertainty quantification]]
- [[multi-modal optimization]]
- [[mode collapse (CMA-ES)]]
- [[cubic law (fracture permeability)]]
- [[local thermal equilibrium]]

## Candidate Methods
- [[background fracture network parameterization]]
- [[CMA-ES with multiple independent runs]]
- [[EDFM-based forward simulation for tracer/heat transport]]
- [[joint inversion of conservative and sorptive tracers]]
- [[normal-score transformation for CMA-ES]]
- [[RMSE threshold-based termination criterion]]
- [[ensemble-based posterior uncertainty assessment from multiple CMA-ES runs]]

## Connections To Other Work
- 裂缝网络参数化维度缩减策略：与固定裂缝数量/产状后再反演的工作（如 Dorn et al. 2013; Klepikova et al. 2014; Somogyvári et al. 2017）相比，本文采用密集背景网络及非均匀开度，等效性更强且无需预设裂缝数目 [Zhang 2024, pp. 1-2, 3].
- 反演方法选择：与MCMC/rjMCMC等方法相比，CMA‑ES可通过多次运行探索多模态参数空间，提供不确定性分析，并对高维病态问题更稳健 [Zhang 2024, pp. 19-20].
- EDFM应用：已有EDFM用于油气藏裂缝反演（如 Jiang et al. 2022; Liu et al. 2023; Yao et al. 2018），本文将其扩展到EGS热‑流‑示踪剂耦合问题 [Zhang 2024, pp. 2-3].
- 深度学习参数化：与基于GAN、VAE的裂缝网络参数化相比，本文基于物理约束的几何参数化可直接在反演框架内调整，无须预训练 [Zhang 2024, pp. 2].
- 终止准则参考：Grayver & Kuvshinov (2016) 提出多起点CMA‑ES避免模式坍塌，本文将该策略用于裂缝反演并对比不同阈值的影响 [Zhang 2024, pp. 5-6, 11‑12].

## Open Questions
- 如何纳入额外地球物理/地质数据（如微震、应力数据）进一步约束背景裂缝几何，以改善裂缝空间分辨能力？ [Zhang 2024, pp. 20]
- 能否开发自适应的终止准则，减少对经验RMSE阈值的依赖，使CMA‑ES在不同尺度和数据噪声下自动稳健收敛？ [Zhang 2024, pp. 20]
- 若考虑应力‑裂缝张开/闭合、化学溶蚀沉淀等耦合过程，当前的参数化与反演框架需如何扩展，以维持预测能力？ [Zhang 2024, pp. 20]
- 在更稀疏的背景裂缝网络下，反演结果能否依然捕获关键流动通道？背景裂缝密度与计算成本、表征精度的最优权衡是什么？ [Zhang 2024, pp. 19]
- 三维场应用中，能否通过逐步细化策略（如先反演宏观连通性，再细化开度分布）进一步提升非均匀裂缝网络的表征精度？ [Zhang 2024, pp. 18-19]

## Source Coverage
所有20个非空索引片段均已处理，覆盖率为：片段（block）覆盖比1.0，字符（char）覆盖比1.004414。全部片段来自Zhang & Wu (2025) 的论文全文，已完整编译为上述LLM Wiki页面。
