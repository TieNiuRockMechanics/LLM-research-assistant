---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-r-mhild-hybrid-discrete-fracture-network-inversion-of-hydraulic-tomography-data-from-a-frac"
title: "Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site."
status: "draft"
source_pdf: "data/papers/2024 - Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site.pdf"
collections:
citation: "Römhild, Lukas, et al. “Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site.” *Water Resources Research*, vol. 60, no. 7, 2024."
indexed_texts: "18"
indexed_chars: "87979"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "87553"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.995158"
coverage_status: "full-index"
source_signature: "8d4c929db5998e347203736f6836ebd3d766dce3"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:27:27"
---

# Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data from a Fractured-Porous Field Site.

## One-line Summary

提出一种考虑裂隙与基质双重流动的混合离散裂隙网络反演方法，并将其成功应用于德国哥廷根现场的水力层析数据反演，结果经独立热示踪试验验证，表明该方法可显著改进裂隙‑多孔介质场地的流‑运移建模。

## Research Question

能否扩展已有的离散裂隙网络反演方法，建立综合考虑离散裂隙和可渗透基质流动的混合模型，从而更准确地表征裂隙‑多孔介质场地，即避免单独使用连续介质模型或忽略基质渗透性的经典DFN模型的局限？该研究直接回应了这一需求，声称“a combined (hybrid) approach considering flow in both discrete fractures and the porous matrix becomes necessary” [Lukas 2024, pp. 3-5]。

## Study Area / Data

研究区位于德国哥廷根大学北校区，地处Leinetalgraben东翼。地质背景属复杂构造环境，岩性主要为Keuper阶的粘土序列和粉‑砂岩交互层；上部14 m为第四纪石灰岩与粘土岩，14 m以下为含方解石矿化及铁氧化物薄膜的中、下Keuper碎屑岩[Lukas 2024, pp. 3-5]。

现场布设5口80 m深的地下水井（十字形），井间水平距离1.9–3 m；每口井配备九个滤管段（各长5 m，间隔3 m粘土回填），顶部8 m为套管[Lukas 2024, pp. 3-5]。2018年4月开展了跨孔多深度抽水试验：在井O的四个层段（O2‑O5）以约30 l min⁻¹速率抽水，在井M的对应层段（M2‑M5）监测压力响应，形成层析配置；其中M5因高噪声被剔除，最终保留12条压降曲线[Lukas 2024, pp. 3-5]。此外，现场还进行了分布式光纤测温热示踪试验，用于独立验证反演结果 [Lukas 2024, pp. 3-5]。

## Methods

研究采用两种反演方案并进行对比：

1. **基于连续介质的走时反演**：定义水力走时为源‑接收点之间的线积分（公式1），利用小波去噪和多项式回归对压降曲线提取走时（取一阶导数绝对值最大值）[Lukas 2024, pp. 5-6]。在开源框架**pyGIMLi**中，使用广义高斯‑牛顿法和Dijkstra算法进行射线追踪反演，得到水力扩散系数**D**分布；若需**K**，则乘以均一的单位储水率**Sₛ=5×10⁻⁵ m⁻¹**（据P. Qiu, 2020）[Lukas 2024, pp. 5-6]。网格垂直分辨率0.5 m、水平分辨率1 m；源‑接收位置简化为位于层段顶部或底部的离散点[Lukas 2024, pp. 5-6]。

2. **混合离散裂隙网络反演**：将裂隙视为1D线元（假设裂隙面内水头恒定），基质为2D连续介质，二者均遵循达西定律和质量守恒，采用有限单元法求解，网格通过**Gmsh**生成并保形离散化裂隙‑基质交线 [Lukas 2024, pp. 6-7]。反演基于贝叶斯框架，使用**马尔可夫链蒙特卡洛**采样方法评估后验分布；参数更新包括裂隙的生成/删除（可逆跳MCMC）以及位置、长度和导水系数扰动 [Lukas 2024, pp. 6-7]。仅使用各信号的前100 s以捕捉最动态的响应信息 [Lukas 2024, pp. 6-7]。

   模型域竖直方向0 至‑60 m，水平方向‑10 m至12 m，左右边界设为零水头，顶底为不流动边界[Lukas 2024, pp. 6-7]。基质参数固定为**K=10⁻⁶ m s⁻¹**、**Sₛ=5×10⁻⁵ m⁻¹**（据单井抽水试验和标准曲线反演，K范围约3.4×10⁻⁷至1.3×10⁻⁶ m s⁻¹）[Lukas 2024, pp. 7-7]；裂隙参数先验范围见表1，其中导水系数K介于**10⁻⁴–10⁰ m s⁻¹**，长度0.5–10 m，位置限定在层段附近区域[Lukas 2024, pp. 6-7]。裂隙产状基于钻孔电视数据，固定三类倾角：**‑0.94°、‑26.31°、49.64°** [Lukas 2024, pp. 7-7]。

## Key Findings

1. 走时反演显示在**‑25 m附近存在高扩散系数带连接M3和O3层段**，但因源‑接收点简化为顶部，无法准确确定该高渗透带的精确深度 [Lukas 2024, pp. 7-9]。
2. 混合DFN反演得到的**裂隙概率图（FPM）**揭示在**‑22 m至‑30 m深度区间裂隙密度最高**，与走时反演的高导带位置一致；但DFN模型进一步识别出两条主要导水断裂（断裂A和B），并显示了多级间接连接[Lukas 2024, pp. 9-10]。
3. 验证热示踪试验模拟表明，混合DFN模型**准确重现了断裂A和B的位置、温度幅度和时间‑行为特征**（深度误差极小），而连续介质走时反演仅识别出与断裂B对应的高导带，且**温度幅度显著偏小、突破时间延迟**，未能预测出断裂A的热异常[Lukas 2024, pp. 13-14]。因此，混合DFN结果的预测质量明显优于连续介质模型。
4. 测试不同基质K值发现，若基质K取值过高，则几乎不产生裂隙（基质即解释数据）；若K过低或忽略基质（纯DFN反演），模拟压降信号过快，无法拟合现场数据。因此，**对本场地而言，包含非零基质渗透性的混合DFN模型是必要的**[Lukas 2024, pp. 10-11]。

## Core Evidence Table

| 证据 | 来源 | 条件/上下文 | 备注 |
|------|------|------------|------|
| 混合DFN反演需要非零基质渗透性，纯DFN反演数据拟合效果差 | [Lukas 2024, pp. 10-11] | 图5及附图S1、S2展示不同基质K值的反演结果 | 表明裂隙‑多孔介质场地不能简化为纯裂隙模型 |
| 断裂A和B的温度预测与实测高度吻合（深度、幅度和时间过程），连续介质模型预测较差 | [Lukas 2024, pp. 13-14] | 图7、图8；断裂A存在个体实现间的高度变异性，但集合平均几乎完美预测 | 必须考虑随机集合平均，而非单一实现 |
| 走时反演得到的‑25 m高扩散区推断为断裂B，但深度不确定、幅度偏小 | [Lukas 2024, pp. 13-14] | 图2c、图7中部，图8b | 连续介质走时反演无法精确刻画单个裂隙 |
| 混合DFN模型的后验集合裂隙概率图显示‑22至‑30 m深度存在高概率裂隙带 | [Lukas 2024, pp. 9-10] | 图3b；基于序列稀疏，每100次实现计算一次 | FPM可用于空间不确定性可视化 |
| 基质参数选择显著影响反演结果：K过高则不产生裂隙，K过低则信号拟合差 | [Lukas 2024, pp. 10-11] | 图5及文本说明；比较了10⁻⁶、10⁻⁸ m/s和忽略基质三种情况 | 基质K的合理预定义对该方法至关重要 |

## Limitations

- 混合DFN模型中基质参数**K**和**Sₛ**目前均固定为常数，未作为反演变量；选取合理基质参数值具有挑战性，直接影响反演结果和裂隙数量 [Lukas 2024, pp. 15-16]。
- 模型为二维，忽略了三维效应和钻孔效应（如垂直热扩散、剩余热积累），可能影响曲线形状及温度预测细节 [Lukas 2024, pp. 13-14]。
- 裂隙的某些性质（孔径、裂隙**Sₛ**）固定为常数，未参与反演；假定单一裂隙内**K**不变[Lukas 2024, pp. 7-7]。
- 混合DFN反演计算成本高（标准PC运行4–5天），且需要设置边界条件并依赖较多先验信息（裂隙产状等） [Lukas 2024, pp. 15-16]。连续介质走时反演虽对此场地不完全适用，但计算仅需15–20秒 [Lukas 2024, pp. 14-15]。
- 当前场的HT实验配置（孔距小但层段长）不利于走时反演精细分辨导水特征的确切深度[Lukas 2024, pp. 14-15]。

## Assumptions / Conditions

- 裂隙简化为一维直线，裂隙面内水头恒定，给水-储水过程符合达西定律 [Lukas 2024, pp. 6-7]。
- 基质为二维连续各向同性多孔介质；计算域左右边界为零定水头（自然流场可忽略），上下边界为不流动 [Lukas 2024, pp. 6-7]。
- 裂隙产状分为三类固定倾角（依据钻孔电视）且在整个反演过程中保持不变; 各裂隙方位等概率选取 [Lukas 2024, pp. 7-7]。
- 裂隙导水系数**K**的先验范围设定为10⁻⁴–10⁰ m s⁻¹，长度0.5–10 m，位置限定在‑15 至‑46 m深度及‑8 至10 m水平范围内 [Lukas 2024, pp. 6-7]。
- 热示踪模拟时补充假定：岩石密度2700 kg m⁻³，基质的孔隙度0.3、裂隙孔隙度0.8，并使用文献中的热参数（导热系数、比热容）[Lukas 2024, pp. 11-13]。
- 计算域水平延伸约10 m以避免边界效应, 但长裂隙仍能连接边界以模拟远场水流 [Lukas 2024, pp. 6-7]。
- 单位储水率**Sₛ**在全域（走时反演和混合DFN模型基质）取常数值**5 × 10⁻⁵ m⁻¹**[Lukas 2024, pp. 5-6][Lukas 2024, pp. 7-7]。

## Key Variables / Parameters

- **D** (水力扩散系数) / **K** (水力传导系数) / **k** (渗透率)：混合DFN模型矩阵**K = 10⁻⁶ m s⁻¹**，裂隙**K**为反演参数(先验10⁻⁴–10⁰ m s⁻¹) [Lukas 2024, pp. 7-7][Lukas 2024, pp. 6-7]。
- **Sₛ** (单位储水率)：基质**Sₛ = 5 × 10⁻⁵ m⁻¹**[Lukas 2024, pp. 7-7]；走时反演也使用同一数值进行**D→K**转换 [Lukas 2024, pp. 5-6]。
- 裂隙参数(θ)：中心位置、长度 (0.5 – 10 m)、导水系数**K** (常数于单一裂隙内)；孔径固定为0.002 m，裂隙**Sₛ**固定为10⁻⁵ m⁻¹ [Lukas 2024, pp. 7-7]。
- 裂隙倾角固定集合：**‑0.94°**, **‑26.31°**, **49.64°**[Lukas 2024, pp. 7-7]。
- HT实验参数：泵流量约30 l min⁻¹ (具体值按实测记录输入正演模型)，层段长5 m、间隔3 m [Lukas 2024, pp. 3-5]。
- 热示踪参数：注入流量25 l min⁻¹，注入水温约20°C，环境温度约9°C，持续5 h [Lukas 2024, pp. 11-13]。

## Reusable Claims

- 对裂隙‑多孔介质场地，**考虑基质渗透性的混合DFN反演能显著改进流场和热运移模拟的精度**：与纯裂隙DFN或连续介质反演相比，混合模型能同时识别主要导水断裂并预测其热响应（位置、幅度和时间过程） [Lukas 2024, pp. 13-14][Lukas 2024, pp. 10-11]。
- **若基质水力传导系数选取不当**（过高或过低），将导致DFN反演失败（零星裂隙或信号过速） [Lukas 2024, pp. 10-11]。
- **混合DFN反演结果具有随机性**，使用集合平均（而非单一实现）对运移预测至关重要，尤其当断裂与井筒间存在基质间隙时个体实现间差异显著 [Lukas 2024, pp. 13-14]。
- 连续介质走时反演能快速识别高导区，但在**长层段‑短孔距的HT配置下无法精细分辨单个裂隙的位置和属性** [Lukas 2024, pp. 14-15]。
- 贝叶斯DFN反演可直接使用含噪原始数据，避免去噪和走时拾取引入的主观误差 [Lukas 2024, pp. 7-7][Lukas 2024, pp. 15-16]。

## Candidate Concepts

- [[hydraulic tomography]]
- [[discrete fracture network inversion]]
- [[hybrid DFN model / discrete fracture matrix model]]
- [[Markov chain Monte Carlo]]
- [[fracture probability map]]
- [[travel time inversion]]
- [[thermal tracer tomography]]
- [[fractured-porous aquifer]]
- [[Bayesian inversion framework]]

## Candidate Methods

- [[hybrid DFN stochastic inversion with reversible jump MCMC]]
- [[continuum travel time inversion using pyGIMLi + Dijkstra’s algorithm]]
- [[finite element forward model for coupled fracture–matrix flow (Gmsh, conforming mesh)]]
- [[sequence thinning for posterior ensemble evaluation]]
- [[wavelet denoising and polynomial regression for travel time picking]]
- [[thermal tracer test forward simulation in COMSOL with imported DFN/continuum property fields]]

## Connections To Other Work

- 与仅忽略基质流动的 **classical DFN inversion** （Ringel et al., 2021; 2022） 形成对比，本研究证明裂隙‑多孔介质场地必须计入基质渗透性 [Lukas 2024, pp. 15-16]。
- 前人走时反演（Yang et al., 2020；Liu et al., 2022）已应用于同一场地，本研究以此作为基线，显示混合DFN模型具有更优越的精细表征和预测能力 [Lukas 2024, pp. 13-14]。
- 将 Fischer et al. (2020) 在 **karstic aquifer** 采用的 coupled discrete‑continuum 反演理念拓展至其他裂隙‑多孔介质场地 [Lukas 2024, pp. 15-16]。
- 未来可与 **geothermal reservoir characterization** 需求结合，因高温含水层储热系统性能对 K 及其各向异性最敏感（Heldt et al., 2023）[Lukas 2024, pp. 15-16]。

## Open Questions

- 目前基质K、Sₛ均采用固定值。若将其作为反演变量，能否进一步提高模型拟合优度并减少主观性？ [Lukas 2024, pp. 16-16]
- 如引入空间可变的基质属性或原位井筒效应，会如何改变反演结果和不确定度？ [Lukas 2024, pp. 16-16]
- 在仅有单孔可利用的地热场景，该混合DFN反演的可靠性和分辨率是否足够？ [Lukas 2024, pp. 16-16]
- 增设更智能的建议分布（如利用地球物理数据或参数间相关性）能否缩短计算耗时？ [Lukas 2024, pp. 16-16]
- 三维DFN和热‑水‑力多场耦合下的验证仍待系统合成与现场试验 [Lukas 2024, pp. 16-16]。

## Source Coverage

所有 18 个非空索引片段均已被处理并用于构建本页（区块覆盖率 100%，字符覆盖率约 99.5%）。来源特征码：`8d4c929db5998e347203736f6836ebd3d766dce3`。数据未使用代码围栏输出。
