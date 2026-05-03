---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin"
title: "High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes."
status: "draft"
source_pdf: "data/papers/2023 - High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.pdf"
collections:
citation: "Jalali, Mohammadreza, et al. “High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.” *Water Resources Research*, vol. 59, no. 5, 2023."
indexed_texts: "18"
indexed_chars: "85343"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "85066"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.996754"
coverage_status: "full-index"
source_signature: "f9715803345f4cbd3e2fe40a6a4b795b31f7f726"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:47:01"
---

# High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.

## One-line Summary

通过等效多孔介质（EPM）三维旅行时层析与离散裂缝网络（DFN）二维可逆跳MCMC反演的结合，对Meuse/Haute-Marne地下研究实验室的气动交叉孔数据进行了高分辨率表征，重建了开挖诱导裂缝网络的水力性质与几何形状，并验证了概念模型。

## Research Question

在黏土岩放射性废物处置库中，开挖隧道会形成相互连通的诱导裂缝网络。核心问题为：如何精确识别这些裂缝的几何形态，并表征其随时间的温度‑水‑力（THM）行为，以评估诱导裂缝是否会成为放射性核素迁移通道。本研究旨在利用气动交叉孔测试数据，结合连续介质和离散介质两类反演方法，高分辨率重建诱导裂缝网络的水力性质和空间结构，从而验证并改进基于应力场的概念模型[Jalali 2023, pp. 1-1; pp. 16-17]。

## Study Area / Data

研究地点为法国Meuse/Haute-Marne地下研究实验室（URL）的GER巷道。该实验室位于Callovo-Oxfordian黏土岩中，GER巷道平行于最小水平主应力方向。数据来自隧道底板上9个垂直钻孔（OHZ6151–OHZ6159），孔间距约0.7–2.0 m[Jalali 2023, pp. 2-4; pp. 3-4]。

- **气动测试**：18次恒流量注气测试，306个理论上可用的交叉孔压力干扰，筛选后采用151个干扰用于旅行时层析，原因包括信噪比高、避开井筒损伤区等[Jalali 2023, pp. 4-5; pp. 5-6]。
- **钻孔特征**：每个孔配备双封隔器系统，间隔位置a（靠近隧道底板，约1.2–2.5 m深度）和b（更深，约3.0–4.3 m深度）。注气速率在位置a约为18–29 L/min，在位置b约为0.15–2.84 L/min[Jalali 2023, pp. 4-5，表1]。
- **裂缝统计**：收集了GER巷道29个垂直钻孔（含上述9个孔）中共272条裂缝的产状与深度，划分为延伸裂缝和剪切裂缝两组[Jalali 2023, pp. 10-11]。

## Methods

研究采用两阶段反演策略，将等效多孔介质（EPM）的旅行时层析作为第一步，然后利用其结果约束并解释离散裂缝网络（DFN）反演。

1. **等效多孔介质—旅行时层析（EPM inversion）**
   - 基于Vasco等人（2000）的渐近方法，将瞬态压力峰值旅行时与水力扩散系数的倒数联系起来，利用射线追踪技术求解eikonal方程[Jalali 2023, pp. 5-6，公式1]。
   - 使用GEOTOM3D软件进行SIRT（同时迭代重建）反演，采用交错网格法将模型域从6×6×4粗网格加密至36×36×24单元，体素尺寸0.26 m（水平）×0.57 m（垂直）[Jalali 2023, pp. 6-7]。
   - 数据预处理包括：小波去噪、多项式拟合及解析求导，以获取压力信号的一阶导数[Jalali 2023, pp. 6-7，图3]。
   - 最终生成三维扩散系数层析图，扩散系数范围约1×10⁻¹至4×10⁻⁴ m²/s[Jalali 2023, pp. 7-8]。

2. **离散裂缝网络反演（DFN inversion）**
   - 采用贝叶斯框架下的跨维度可逆跳马尔可夫链蒙特卡洛（rjMCMC）方法，校准裂缝的位置、长度和数量[Jalali 2023, pp. 9-10]。
   - 模型更新包括裂缝添加、删除和位移三种操作，接受率由似然比和提议比决定[Jalali 2023, pp. 9-10，公式2]。
   - 前向模型为二维隐式有限差分裂缝网络流动模型，假设基质不透水，裂缝段传导性依立方程计算。边界条件包括：隧道表面0.5 m深处施加常大气压、深度2.8 m处设置裂缝开度边界以反映延伸裂缝和剪切裂缝的不同水力开度、以及实测的注气压力边界[Jalali 2023, pp. 12-13]。
   - 仅使用两个裂缝组：延伸裂缝倾角80°，剪切裂缝倾角40°。等效2D水力开度根据MULTISIM估算结果缩放至0.3–4.4 mm范围[Jalali 2023, pp. 11-12，表2]。
   - 反演针对三个平行于隧道轴线的二维剖面进行，每个剖面使用7‑12个压力干扰数据的前200 s记录[Jalali 2023, pp. 10-11]。

## Key Findings

- **3D扩散系数层析图**揭示高扩散区集中在隧道底板附近，并向开挖推进的相反方向倾斜，与chevron结构的凹凸形状一致，但层析图本身仅显示模糊的高扩散异常，未能清晰呈现chevron构造的完整轨迹[Jalali 2023, pp. 7-9; pp. 15-16]。
- **2D裂缝概率图**（三个平行剖面）均展现出相似的裂缝模式：一条高概率的垂直倾斜延伸裂缝连接着上部与下部的水平剪切裂缝，且该结构在三个剖面中的水平位置相同（约x=80 cm），支持在三维空间中内插得到chevron结构[Jalali 2023, pp. 13-15]。
- 上部水平剪切裂缝在所有剖面中均具有高出现概率；剖面1和2还重建出与隧道表面相连的高概率裂缝通道，与现场观察到的延伸裂缝露出情况相符[Jalali 2023, pp. 13-15]。
- 实测压力曲线与DFN模拟结果的对比表明，大部分干扰能被很好地拟合；位于模型下部的干扰信号幅值极小（部分<1 kPa），拟合偏差较大，主要归因于数据质量限制和模型简化[Jalali 2023, pp. 15-16]。
- 综合结果验证了Armand等人（2014）提出的诱导裂缝网络概念模型，即巷道底板中的chevron结构由延伸裂缝和剪切裂缝组成，倾向与开挖方向相反[Jalali 2023, pp. 16-17]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 三维扩散系数层析图中，最高扩散值（1×10⁻¹ m²/s）出现在隧道底板附近，沿OHZ6158与OHZ6159间的半圆区域，随深度增加扩散值下降超过两个数量级（至4×10⁻⁴ m²/s）。 | [Jalali 2023, pp. 7-8, 图4] | 151个干扰数据，交错网格单元大小0.26×0.26×0.57 m，高轨迹密度，无覆盖盲区。 | 扩散值分布暗示chevron结构的倾斜方向。 |
| 三个平行隧道轴线的二维DFN反演剖面均在不同位置重建出垂直倾斜的高概率裂缝（x≈80 cm），连接上部与下部水平剪切裂缝。 | [Jalali 2023, pp. 13-15, 图6] | 仅使用前200 s压力数据，裂缝组倾角80°和40°，等效2D水力开度0.3‑4.4 mm（表2）。 | 该一致性表明方法稳健，且可内插为三维chevron形状。 |
| 上部水平剪切裂缝在所有剖面中概率高；剖面1和2有高概率裂缝延伸至隧道表面（0.5 m深度边界）。 | [Jalali 2023, pp. 13-15, 图6] | 隧道表面设为常大气压边界，与现场观察相符。 | 指示隧道表面附近存在高渗透通道。 |
| DFN模型对剖面1的压力响应拟合中，上部水平干扰（IV）拟合质量极高，即使小幅压力波动（几帕）也能再现；下部干扰（I）信号被低估约2 kPa。 | [Jalali 2023, pp. 15-16, 图7] | 200 s压力数据，1 Hz采样；前向模型假设基质不透水，仅两个裂缝组。 | 表明模型能捕捉主要裂缝连通特征，但下部区域受到简化和低信噪比影响。 |
| 从MULTISIM分析得到位置a的等效气体渗透率比位置b高约两个数量级（如2.8×10⁻⁶ m/s对比1.7×10⁻⁸ m/s），对应于延伸裂缝与剪切裂缝的分布差异。 | [Jalali 2023, pp. 4-5, 表1] | 假设孔隙度15%（取自18次测试平均值），单相流，压缩性忽略。 | 数值证明隧道近场裂缝渗透性远高于远场。 |

## Limitations

- 模型下部（深度较大区域）的压力信号幅值极小，部分不足1 kPa，受限于压力传感器的精度和实验设备，导致拟合质量偏低[Jalali 2023, pp. 15-17]。
- 前向模型对实际条件做了大量简化：仅采用两个裂缝组（倾角80°和40°），而真实诱导裂缝网络可能包含更多方向组合[Jalali 2023, pp. 16-17]。
- 等效2D水力开度通过手动拟合选定干扰得出，且被设置为深度分段常数（以2.8 m为界），未纳入反演参数优化。过小或过大的开度可由算法通过生成平行裂缝或延长裂缝路径来补偿，但裂缝开度的非唯一性仍存在[Jalali 2023, pp. 16-17]。
- 假定岩石基质完全不渗透，忽略了Callovo-Oxfordian黏土岩固有的低渗透性基质的贡献，这可能在下部裂缝密度低、裂缝开度小的区域造成偏差[Jalali 2023, pp. 16-17]。
- 裂缝统计来源于岩芯编录，可能因岩芯采收率不足（尤其在强破碎的EDZ近隧道段）而导致统计不确定性，尽管已合并29个孔的272个裂缝以减少偏差[Jalali 2023, pp. 10-11]。

## Assumptions / Conditions

- 流动为单相气体流动，注气诱发压力差小于0.5 bar，气体压缩性变化可忽略[Jalali 2023, pp. 3-4]。
- 井筒储存效应通过插入杜洛塑料体积缩减器已被大幅减小，区间体积约为0.001 m³[Jalali 2023, pp. 4-5]。
- 孔隙度统一设定为15%，该值由18次气动测试的压力曲线通过MULTISIM分析得到的平均值，代表基质与裂缝网络的综合效应[Jalali 2023, pp. 4-5]。
- 裂缝统计中线性裂缝强度P10=2.0 m⁻¹，并假定面裂缝强度P21等于P10[Jalali 2023, pp. 11-12]。
- DFN反演前向模型仅离散裂缝网络，且裂缝壁假定为平行的光滑平板，适用于立方定律[Jalali 2023, pp. 12-13]。
- 深度超过2.8 m的裂缝段，其等效2D水力开度按1/5至1/10的比例缩小，反映延伸裂缝和剪切裂缝的水力差异[Jalali 2023, pp. 12-13]。
- 所有岩石中裂缝均为开挖诱导形成，无构造裂缝[Jalali 2023, pp. 2-4]。

## Key Variables / Parameters

- 水力扩散系数（D）：反演范围1×10⁻¹–4×10⁻⁴ m²/s[Jalali 2023, pp. 7-8]
- 裂缝产状：延伸裂缝倾角80°，剪切裂缝倾角40°，主要倾向方向N65°E（与开挖方向平行）[Jalali 2023, pp. 11-12]
- 裂缝面密度（P21）：2.0 m⁻¹[Jalali 2023, pp. 11-12]
- 等效2D水力开度：延伸裂缝0.3–3.0 mm，剪切裂缝0.32–3.2 mm，具体见表2[Jalali 2023, pp. 12-13]
- 注气速率与持续时间：见表1[Jalali 2023, pp. 4-5]
- 流体性质：气体动力黏度1.5×10⁻⁵ Pa·s，压缩系数1.0×10⁻⁶ 1/Pa，密度1.1606 kg/m³（20°C）[Jalali 2023, pp. 12-13]
- 旅行时（tpeak）及压力一阶导曲线[Jalali 2023, pp. 5-6; 图3]
- 数据集：151个压力干扰用于EPM；每2D剖面7–12个干扰用于DFN反演[Jalali 2023, pp. 5-6; pp. 10-11]

## Reusable Claims

- 将旅行时层析成像的EPM结果用作先验约束，可以显著提高DFN反演对裂缝网络空间几何形状的解释力，验证了Dong等人（2019）提出的策略在野外尺度的适用性[Jalali 2023, pp. 5-6; pp. 16-17]。
- 在开挖诱导裂缝表征中，基于气动交叉孔数据的旅行时层析能够以高空间分辨率识别chevron结构的大致位置和倾向，但单一EPM反演无法给出清晰的离散裂缝轨迹[Jalali 2023, pp. 7-9; pp. 15-16]。
- 跨维度rjMCMC反演出多个独立剖面中相同位置的垂直倾斜高概率裂缝，可作为三维裂缝网络几何内插的可靠依据，从而验证概念模型[Jalali 2023, pp. 13-15; pp. 16-17]。
- 在气体测试的短时低压条件下，忽略基质渗透性的DFN前向模型可以充分拟合多数观测压力干扰，但在裂缝密度低、信号弱的区域可能低估压力响应[Jalali 2023, pp. 15-17]。
- 裂缝开度是根据单孔模拟结果手动设定的，反演算法会通过增加平行裂缝或延长连接路径来补偿开度设置偏差，这提示单纯依靠水力信号反演不能唯一确定裂缝开度，需结合示踪或其它信息[Jalali 2023, pp. 16-17]。

## Candidate Concepts

- [[excavation-induced fracture network (EDZ)]]
- [[equivalent porous media (EPM) tomography]]
- [[discrete fracture network (DFN) inversion]]
- [[transdimensional reversible jump MCMC]]
- [[travel time-based hydraulic tomography]]
- [[pneumatic cross-hole testing]]
- [[chevron fractures]]
- [[Callovo-Oxfordian clay rock]]
- [[Meuse/Haute-Marne URL]]
- [[fracture probability map]]
- [[Bayesian inversion for hydrogeology]]

## Candidate Methods

- [[travel time tomographic inversion with eikonal equation]]
- [[SIRT and staggered grid reconstruction]]
- [[wavelet de-noising for pressure derivative estimation]]
- [[rjMCMC with fracture addition/deletion/shift]]
- [[2D finite difference gas flow in discrete fractures]]
- [[equivalent 2D hydraulic aperture scaling]]
- [[MULTISIM borehole simulator for single-hole test analysis]]

## Connections To Other Work

- 本研究直接延续了Vasco等人（2000）的旅行时水力层析理论和Brauchler等人（2003, 2011, 2013）的野外应用，将方法延伸到黏土岩中的开挖诱导裂缝[Jalali 2023, pp. 5-6]。
- DFN反演框架基于Somogyvári等人（2017）的示踪层析反演方法，并将其适配至气动压力层析[Jalali 2023, pp. 9-10]。
- 所验证的概念模型来源于Armand等人（2014, 2017）对URL的详细结构和水力研究，该项工作提供了巷道底板chevron结构的构造描述[Jalali 2023, pp. 2-4; pp. 16-17]。
- Vesselinov等人（2001a, 2001b）在Apache Leap研究场址进行的三维气动反演工作为本次高分辨率随机成像奠定了基础[Jalali 2023, pp. 1-2]。
- 将EPM和DFN联合解释的思路与Dong等人（2019）提出的等价性研究一脉相承[Jalali 2023, pp. 5-6]。

## Open Questions

- 将传输（如示踪）信息集成到反演中，是否能有效降低裂缝开度与几何参数之间的非唯一性[Jalali 2023, pp. 16-17]？
- 在DFN反演中引入更多或可变的裂缝组，会不会导致反演问题不适定？有何办法通过附加地质信息约束来缓解这一问题[Jalali 2023, pp. 16-17]？
- 若考虑黏土岩基质的气体渗透性，如何在不显著增加计算负担的前提下改进前向模型，以提高深部低渗透区域的拟合效果[Jalali 2023, pp. 16-17]？
- 从2D裂缝概率图到全三维裂缝网络的稳健外推方法尚需发展和验证，特别是如何利用多个非平行剖面约束三维连通性[Jalali 2023, pp. 15-16]。

## Source Coverage

所有非空索引片段（共18个）均被纳入本页面处理。总索引字符数85,343，编译使用字符数85,066。区块覆盖率为1.0，字符覆盖率约为0.9968（single‑pass）。信息来源严格限定于提供的[Jalali 2023]片段，未引用或补充外部信息。
