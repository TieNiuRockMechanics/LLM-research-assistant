---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-g-mez-a-non-parametric-discrete-fracture-network-model"
title: "A Non-parametric Discrete Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2023 - A Non-parametric Discrete Fracture Network Model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Gómez, Santiago, et al. \"A Non-parametric Discrete Fracture Network Model.\" *Rock Mechanics and Rock Engineering*, vol. 56, no. 5, 2023, pp. 3255-3278. doi:10.1007/s00603-022-03194-y."
indexed_texts: "17"
indexed_chars: "84828"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "84049"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990817"
coverage_status: "full-index"
source_signature: "cc7af56100b8c86d5b84958ac85dccd4e1895cde"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:06:31"
---

# A Non-parametric Discrete Fracture Network Model.

## One-line Summary
开发了一种基于非参数核密度估计（KDE）和方向‑线性统计的离散裂缝网络（DFN）模型，用于联合表征裂缝方向和尺寸分布，并通过摄影测量数据在采石场高墙面进行了验证。[Santiago 2023, pp. 1-2]

## Research Question
如何构建一个非参数DFN模型，能够在无分布假设下联合估计裂缝方向和尺寸的密度函数，同时校正截断、截尾、尺寸及方向等采样偏差，并利用二维迹线观测反演三维圆盘尺寸分布？[Santiago 2023, pp. 2-3]

## Study Area / Data
- **地点**：西班牙托莱多省Almonacid de Toledo的El Aljibe采石场，开采糜棱岩。[Santiago 2023, pp. 4-4]
- **数据来源**：12个爆破高墙面的摄影测量模型，采样尺度约10 mm。[Santiago 2023, pp. 4-4]
- **结构域**：一条大型伸展断层将12个迹线图分为两个结构域：DS1（TM1‑TM6）和DS2（TM7‑TM12），断层附近裂缝密度增大。[Santiago 2023, pp. 4-4]
- **面方向**：12个面方向相似，倾向228.54±4°，倾角22.98±3.59°（圆平均±标准差）。[Santiago 2023, pp. 4-4]
- **迹线特征**：表1给出了各面尺寸、迹线条数、总长度、平均长度、P21以及完整、半有界、有界迹线的百分比。完整迹线占85%以上，有界迹线仅在5个爆破中出现。DS1平均P21=0.72 m⁻¹，DS2平均P21=1.23 m⁻¹。[Santiago 2023, pp. 4-5]
- **数据格式**：点云和不连续面特征（倾角、倾向、多段线点坐标）以.csv格式处理。[Santiago 2023, pp. 4-4]

## Methods
1. **方向‑线性核密度估计**：采用García-Portugués et al. (2013)的联合KDE，以von Mises‑Fisher核为方向核，高斯核为线性核，并使用对数变换确保正的尺寸支撑。[Santiago 2023, pp. 5-6]
2. **最优带宽选择**：方向带宽选用规则‑拇指（ROT）选择器，但为避免多模态失效，仅取最似然极点周围45°内的数据计算；线性带宽采用极大似然交叉验证（MLCV）选择。[Santiago 2023, pp. 6-7]
3. **迹线长度至裂缝尺寸的估计**：利用Bertrand悖论第3种解法（弦心在参考半径上均匀分布），建立迹线长度L与直径D的关系 (L = D√(1-U²(0,1))，等价于Warburton关系。[Santiago 2023, pp. 7-8]
4. **截断偏差校正**：引入混合随机变量Ξ，构造不完全伪迹线长度 l↕ 与直径D的关系 (l↕ = D·Ψ)，其中Ψ的分布由参数p（半有界迹线比例）控制。[Santiago 2023, pp. 8-9]
5. **尺寸与方向偏差校正**：通过加权函数 w(z) = z^γ 校正尺寸偏差，通过 w_i = (1 - (μ^T X_i)²)^{-1/2} 校正方向偏差（Terzaghi校正）。γ由模拟中相交圆盘尺寸直方图与真实直方图的比值拟合得到，非平面条件下γ>1。[Santiago 2023, pp. 11-13]
6. **概率截断**：用对数‑逻辑分布函数 F(l)=1/(1+(l/α)^{-β}) 作为概率滤波器，α为50%被观测概率对应的迹线长度，β控制陡度。通过随机优化最大化模拟与实验直方图间的Kolmogorov‑Smirnov检验P值来标定α和β。[Santiago 2023, pp. 13-14]
7. **模型标定**：迭代计算p和γ直至收敛，并通过匹配实验P21调整体积密度P30。最终P30估计公式为 ⌈(Σ l_i / \bar{l})·(N/TF)⌉ / V。[Santiago 2023, pp. 13-14]
8. **随机采样**：对方向‑线性KDE进行随机采样生成圆盘，圆盘与三角化表面的交点采用SurfaceIntersection.m（基于Moller 1998的三角形/三角形相交算法），计算出伪迹线长度。[Santiago 2023, pp. 4,10]

## Key Findings
1. 非参数方向‑线性KDE能够有效联合表征裂缝方向与迹线长度分布，无需预先划分裂缝组或假定参数分布形式。[Santiago 2023, pp. 2-3]
2. Bertrand悖论第3种解法可作为从迹线分布推导圆盘尺寸分布的有效工具，且与Warburton公式一致。[Santiago 2023, pp. 16-17]
3. 校正截断、截尾、尺寸和方向偏差后，模型生成的伪迹线长度分布和极点图与实验观测在统计上相似。以TM1为例，模拟相交圆盘数与实验迹线条数一致。[Santiago 2023, pp. 14-16]
4. 12个迹线图的P21与P32呈显著线性相关（DS1和DS2的P值均＜0.05），验证了模型有效性；P30与P21、P32则无显著相关，因为P30仅反映支撑点密度而缺失尺寸信息。[Santiago 2023, pp. 16-17]
5. 与传统DFN工具（FracMan®）的结果对比，本模型的P21‑P32关系落在同一线性趋势内，尤其是DS2域。[Santiago 2023, pp. 16-17]
6. 概率截断参数α从TM1到TM12递减，表明在跨过断层的域中较短的迹线更多地被标记。[Santiago 2023, pp. 14-15]
7. 模型计算时间大部分（65.2%）消耗在三角形/三角形相交上，其次为迭代更新（21%）、概率滤波器标定（5.5%）和随机采样（5.3%）。[Santiago 2023, pp. 16-17]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 非参数方向‑线性KDE可联合表征裂缝方向与尺寸分布，无需假设参数形式 | [Santiago 2023, pp. 2-3] | 使用von Mises‑Fisher核和高斯核；方向带宽ROT和改进选择，线性带宽MLCV | 首次将非参数方法用于联合方向‑尺寸估计 |
| 利用Bertrand悖论第3种解法建立的迹线长度‑直径关系 L=D√(1-U²) 与Warburton关系等价 | [Santiago 2023, pp. 7-8,16-17] | 圆盘形状、无穷大平面假设；通过数值模拟验证 | 为从非参数迹线分布推求圆盘尺寸提供理论基础 |
| 加权函数 w(z)=z^γ 可校正尺寸偏差，γ在非平面条件下>1（本研究中1.13‑1.48） | [Santiago 2023, pp. 11-13] | 通过模拟均匀直径圆盘与三角化高墙面相交的直方图比值拟合 | γ显著不为1，表明非平面表面对尺寸偏差的影响 |
| 对数‑逻辑概率滤波器 F(l)=1/(1+(l/α)^{-β}) 可同时校正截断与分辨能力导致的漏记 | [Santiago 2023, pp. 13-14] | α和β通过K‑S检验P值最大化标定 | 赋予模型一定的尺度不变性 |
| 12个高墙面模型的P21与P32显著线性相关，且与传统DFN结果一致 | [Santiago 2023, pp. 16-17] | DS1: R²=…, p<0.05; DS2: R²=…, p<0.05 | 支持模型有效性，但P30与P21/P32无显著相关 |

## Limitations
- 方向带宽ROT选择器在多模态方向密度下失效，需手动限定最似然极点周围45°区域计算。[Santiago 2023, pp. 6-7]
- 模型假设所有裂缝均为扁平圆形，未考虑椭圆等更复杂形状。[Santiago 2023, pp. 3-4]
- 裂缝位置采用均匀泊松点过程，未考虑可能的聚类或排斥效应。[Santiago 2023, pp. 4-4]
- 迹线长度至圆盘直径的反演依赖于Bertrand悖论的特定选择，其结果分布类型可能与真实分布有差异。[Santiago 2023, pp. 16-17]
- 概率截断函数仅含两个参数，可能过度简化实际观测偏差的复杂性。[Santiago 2023, pp. 13-14]

## Assumptions / Conditions
- 裂缝被建模为扁平的圆形圆盘。[Santiago 2023, pp. 3-4]
- 裂缝中心点服从体积域内的均匀泊松点过程。[Santiago 2023, pp. 4-4]
- 裂缝方向与尺寸相互独立。[Santiago 2023, pp. 5-5]
- 迹线长度‑圆盘尺寸关系建立在无穷大平面假设上；有限面造成的截断偏差通过混合随机变量校正。[Santiago 2023, pp. 8-9]
- 截尾偏差采用对数‑逻辑概率滤波器描述，其参数α、β通过最大化模拟与实验直方图的K‑S检验P值确定。[Santiago 2023, pp. 13-14]
- 方向偏差校正采用Terzaghi类加权，并假设测量面平均法向量μT可代表非平面表面。[Santiago 2023, pp. 11-13]

## Key Variables / Parameters
- **方向‑线性核带宽**：h（方向带宽），g（线性带宽）[Santiago 2023, pp. 5-6]
- **截断参数**：p（半有界迹线比例）[Santiago 2023, pp. 8-9]
- **尺寸偏差指数**：γ（加权幂指数）[Santiago 2023, pp. 11-13]
- **概率截断参数**：α（尺度参数，m），β（陡度参数）[Santiago 2023, pp. 13-14]
- **裂缝强度**：P30（体积密度，m⁻³），P21（面积迹线长度密度，m⁻¹），P32（面积裂缝面积密度，m⁻¹）[Santiago 2023, pp. 1-2,14]
- **圆盘尺寸与迹线长度**：D（圆盘直径），L（完全伪迹线长度），l↕（不完全伪迹线长度）[Santiago 2023, pp. 1-2,7-8]

## Reusable Claims
- 非参数方向‑线性KDE可以联合估计裂缝方向与尺寸的密度函数，避免预先划分裂缝组和假设参数分布，适用于多模态方向数据。[Santiago 2023, pp. 2-3,5-6] 条件：需选择合适的核函数和带宽；方向带宽ROT仅在主模态周围可用，多模态时需局部处理。
- 基于Bertrand悖论第3种解法的关系式 L=D√(1-U²) 可有效从迹线长度分布推导圆盘尺寸分布，且与Warburton公式等价。[Santiago 2023, pp. 7-8,16-17] 条件：适用于扁平圆盘、无穷大平面假设；有限面效应需额外校正。
- 通过加权函数 w(z)=z^γ 校正尺寸偏差，γ可通过模拟圆盘与真实表面相交的尺寸直方图比值估计，非平面条件下γ>1。[Santiago 2023, pp. 11-13] 条件：需要表面三角网格和大量圆盘模拟。
- 对数‑逻辑概率滤波器能够以连续概率方式处理截断偏差，使模型能够包含比现场观测更短的裂缝，赋予模型一定的尺度不变性。[Santiago 2023, pp. 13-14] 条件：需通过优化算法标定α和β。
- 裂缝强度P21与P32的线性相关性可作为DFN模型验证的准则，因为两者均包含尺寸信息；P30因仅反映点数而不宜单独用于验证。[Santiago 2023, pp. 16-17] 条件：适用于同一结构域内、相同统计分布的裂缝系统。

## Candidate Concepts
- [[Non-parametric Discrete Fracture Network]]
- [[Directional-linear kernel density estimation]]
- [[Bertrand paradox No.3]]
- [[Poisson point process]]
- [[Censoring bias in fracture traces]]
- [[Truncation bias]]
- [[Size bias]]
- [[Orientation bias]]
- [[Weighting function for sampling bias]]
- [[Probabilistic truncation filter]]
- [[Pseudo-trace length]]
- [[P21-P32 linear relationship]]

## Candidate Methods
- [[Directional-linear KDE with von Mises-Fisher and Gaussian kernels]]
- [[Log-transformed kernel for positive support]]
- [[ROT bandwidth selector with mode restriction]]
- [[MLCV bandwidth selector for linear data]]
- [[Trace length-to-disk size estimation via Bertrand paradox]]
- [[Mixed random variable for censoring correction]]
- [[Power-law weighting for size bias correction]]
- [[Terzaghi-type weighting for orientation bias]]
- [[Log-logistic probabilistic filter for truncation]]
- [[Random sampling of directional-linear KDE]]
- [[Monte Carlo calibration of P30 using P21 matching]]

## Connections To Other Work
- 模型引用了García-Portugués et al. (2013)的方向‑线性核密度估计理论。[Santiago 2023, pp. 3-4]
- 迹线长度与圆盘尺寸的关系与Warburton (1980a)的公式等价，并通过Bertrand (1888)悖论建立联系。[Santiago 2023, pp. 7-8]
- 采样偏差的分类和校正基于Baecher (1983)、Kulatilake & Wu (1984)、Priest & Hudson (1981)等经典工作。[Santiago 2023, pp. 3-4]
- 传统DFN建模方法（如FracMan®）在Bernardini et al. (2022)中用于比较，本模型的结果与之在P21‑P32关系上一致。[Santiago 2023, pp. 16-17]
- 圆盘尺寸分布与迹线长度分布的矩关系验证参照了Zhang et al. (2002)的公式。[Santiago 2023, pp. 16-17]
- 非平面表面相交计算采用了Moller (1998)的三角形‑三角形相交算法。[Santiago 2023, pp. 4-4]

## Open Questions
- 非参数方向‑线性KDE在多模态方向密度下的全局带宽选择策略仍需研究，当前使用的局部ROT方法可能丢失次要模态的信息。[Santiago 2023, pp. 6-7]
- 模型假设裂缝为扁平圆形，对于天然岩体中常见的非圆形（如椭圆）或不规则形状的适用性有待验证。[Santiago 2023, pp. 3-4]
- 概率截断函数的形式与参数是否能迁移至不同尺度或不同观测手段的数据集尚不清楚。[Santiago 2023, pp. 13-14]
- 模型采用均匀泊松点过程，若实际裂缝呈现聚类或排斥分布，将如何影响P30‑P21关系？[Santiago 2023, pp. 4-4]
- 模型中方向与尺寸被假设独立，在强构造作用下该假设可能不成立，如何扩展到相依情形？[Santiago 2023, pp. 5-5]

## Source Coverage
All non-empty indexed fragments have been processed. Indexed fragments: 17; indexed characters: 84,828; nonempty source blocks: 17; compiled source blocks: 17; compiled source characters: 84,049; coverage ratio by blocks: 1.0; coverage ratio by chars: 0.990817.来源一致性签名：cc7af56100b8c86d5b84958ac85dccd4e1895cde。所有事实性陈述均来自以上处理的索引片段，未添加额外信息。
