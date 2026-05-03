---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-bao-geometrical-heterogeneity-of-the-joint-roughness-coefficient-revealed-by-3d-laser-scann"
title: "Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning."
status: "draft"
source_pdf: "data/papers/2020 - Geometrical heterogeneity of the joint roughness coefficient revealed by 3D laser scanning.pdf"
collections:
  - "zotero new"
citation: "Bao, Han, et al. \"Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning.\" *Engineering Geology*, vol. 265, 2020, 105415, doi:10.1016/j.enggeo.2019.105415."
indexed_texts: "7"
indexed_chars: "33205"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:50:33"
---

# Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning.

## One-line Summary
本研究利用三维激光扫描技术揭示了同一组节理的节理粗糙度系数（JRC）存在显著的几何异质性，具体表现为采样间隔效应、各向异性以及符合对数正态分布的大变异性 [Bao 2020, pp. 1-1, pp. 1-2, pp. 5-8].

## Research Question
本研究旨在探究节理粗糙度系数的分布特征，具体包括：
1.  确定在JRC计算中，剖面线和数字点的采样间隔产生影响的阈值，并研究该阈值与粗糙度之间的关系 [Bao 2020, pp. 1-1, pp. 1-2]。
2.  揭示并量化同一组节理的JRC在空间上的各向异性分布及概率分布特征 [Bao 2020, pp. 1-1, pp. 1-2].

## Study Area / Data
- **研究地点：** 样本采集自中国陕西省的关山铁路隧道 [Bao 2020, pp. 1-1]。
- **样本信息：** 共采集了31个节理样本，均属于同一节理组，其优势产状为209° ∠71° [Bao 2020, pp. 1-1]。岩性为闪长岩 [Bao 2020, pp. 3-5]。节理面上有可见的剪切擦痕，可用于确定剪切方向 [Bao 2020, pp. 2-3]。
- **数据采集设备：** 使用手持式三维激光扫描仪（Handyscan 3D）获取节理面形态的初始点云信息，扫描仪分辨率为0.05 mm，激光束光斑为0.04 mm [Bao 2020, pp. 2-3]。
- **研究区域：** 从扫描点云中选取了边长为10 cm的研究区域 [Bao 2020, pp. 2-3]。

## Methods
1.  **节理形态数字化：**
    *   通过贴定位点并进行慢速往返扫描，获取节理面的三维空间信息 [Bao 2020, pp. 2-3]。
    *   使用Geomagic软件提取研究区域的三维扫描信息 [Bao 2020, pp. 2-3]。
    *   采用Jiang et al. (2016)的方法，在间距为0.05 mm的正交网格内对点云进行插值 [Bao 2020, pp. 2-3]。
2.  **JRC计算：**
    *   基于剪切擦痕确定0度剪切方向，并以15°为间隔顺时针截取不同方向的剖面线 [Bao 2020, pp. 3-5]。
    *   采用分形理论量化节理粗糙度。首先通过公式（1）计算分形维数D，再利用D与JRC的经验关系式（2）计算JRC值（Xie and Pariseau, 1994）[Bao 2020, pp. 2-3]。
        *   Eq. (1): `D = lg 4 / lg{2[1 + cos arctan(2h/L)]}` (其中h和L是高阶粗糙度的平均高度和平均基底长度) [Bao 2020, pp. 3-5]。
        *   Eq. (2): `JRC = 85.2671(D - 1)^0.5679` [Bao 2020, pp. 2-3]。
3.  **采样间隔效应分析：**
    *   通过改变剖面线间隔和数字点间隔，评估其对计算JRC值的影响 [Bao 2020, pp. 3-5]。
    *   分析数字点采样间隔的阈值与JRC值之间的定量关系，建立公式（3）[Bao 2020, pp. 3-5]。
        *   Eq. (3): `y = 1.8314e^(-x/0.067)` (其中y是采样点间隔的阈值，x是JRC值) [Bao 2020, pp. 3-5]。
4.  **分布特征分析：**
    *   对31个样本在各个方向上的JRC值取平均值，研究该节理组的各向异性分布 [Bao 2020, pp. 3-5]。
    *   通过K-s检验发现JRC服从对数正态分布，并比较了算数平均值与基于分布函数的期望值之间的差异 [Bao 2020, pp. 5-8]。

## Key Findings
- **采样间隔效应与阈值：** JRC计算值受剖面线和数字点采样间隔的影响。存在一个阈值，当采样间隔小于该阈值时，JRC值保持恒定；超过该阈值后，JRC值开始变化 [Bao 2020, pp. 3-5, pp. 5-8]。
    - 剖面线的采样间隔阈值为4 mm，该阈值与节理的粗糙度无关 [Bao 2020, pp. 1-1, pp. 5-8]。
    - 数字点的采样间隔阈值则受节理粗糙度影响，与JRC值呈负指数关系 [Bao 2020, pp. 1-1, pp. 3-5]。
- **JRC的各向异性：** 同组节理的JRC值在不同方向上表现出显著的各向异性 [Bao 2020, pp. 1-1, pp. 3-5]。
- **JRC的变异性与概率分布：** 同一方向上，不同样本间的JRC值存在很大变异。统计分析表明，JRC并不遵循正态分布，而是符合对数正态分布 [Bao 2020, pp. 1-1, pp. 5-8, pp. 8-9]。
- **计算方式对比：** 基于对数正态分布函数计算出的JRC期望值，普遍大于算数平均值，最大差异可达23.1%。研究认为期望值能更合理地反映JRC的真实信息 [Bao 2020, pp. 5-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| --- | --- | --- | --- |
| 数字点采样间隔存在阈值，小于此阈值时JRC恒定，大于时JRC可变；该阈值与JRC呈负指数关系（Eq. 3）。 | [Bao 2020, pp. 3-5] | 基于10条不同粗糙度的剖面线数据得出。 | 该阈值会影响JRC评估的准确性。|
| 剖面线采样间隔阈值为4 mm，且独立于节理粗糙度。 | [Bao 2020, pp. 1-1] | 适用于所研究的闪长岩节理样本。 | 可作为同类研究制定采样方案的参考。|
| 同组节理的JRC值表现出显著的各向异性。 | [Bao 2020, pp. 3-5] | 基于31个样本在0°~180°方向，每隔15°计算的JRC平均值。| 各向异性对岩体剪切强度和渗流的各向异性有直接影响。|
| JRC值的概率分布符合对数正态分布，而非正态分布。| [Bao 2020, pp. 5-8] | 通过K-s统计检验得出。| 这一发现为JRC的统计分析提供了更合理的分布模型。|
| JRC的分布函数期望值大于算术平均值，最大差异23.1%。| [Bao 2020, pp. 5-8] | 结论基于对数正态分布模型。| 表明使用期望值作为JRC的代表值可能更为合理。|

## Limitations
- 未从索引片段中确认样本数量（31个）对于泛化到其他类型节理或地质条件的有效性。
- 研究结论主要基于闪长岩节理样本和特定的分形理论计算方法（Xie and Pariseau, 1994），其对其他岩性或计算方法的适用性未从索引片段中确认。
- 剖面线采样间隔阈值（4 mm）的具体适用范围（例如，是否受节理尺寸影响）未从索引片段中确认。

## Assumptions / Conditions
- **同组节理假设：** 研究基于31个样本属于同一节理组且具有相似形成机制的假设，从而可以通过平均化处理来研究该组的各向异性分布 [Bao 2020, pp. 3-5]。
- **粗糙度量化方法：** 采用Xie and Pariseau (1994)提出的基于分形理论的JRC计算公式，该公式建立了分形维数D与JRC的经验关系 [Bao 2020, pp. 2-3]。
- **剪切方向定义：** 节理面上的剪切擦痕方向被定义为0°剪切方向，作为各向异性测量的基准 [Bao 2020, pp. 2-3, pp. 3-5]。
- **采样阈值定义：** JRC从恒定变为可变的拐点被定义为采样间隔的阈值 [Bao 2020, pp. 3-5]。

## Key Variables / Parameters
- **节理粗糙度系数 (JRC):** 表征节理物理力学行为的关键指标 [Bao 2020, pp. 1-1]。
- **分形维数 (D):** 用于量化节理几何形态的中间参数，通过公式（1）计算 [Bao 2020, pp. 2-3]。
- **采样间隔 (Sampling Interval):** 包括剖面线间隔和数字点间隔，是影响JRC计算准确性的关键控制因素 [Bao 2020, pp. 1-1]。
- **采样间隔阈值 (Threshold of Sampling Interval):** JRC值从稳定转为变化的临界间隔值。剖面线间隔阈值为固定值（4 mm），数字点间隔阈值是与JRC呈负指数关系的变量 [Bao 2020, pp. 1-1, pp. 3-5]。
- **方向 (Direction):** 以剪切方向为0°的顺时针角度，用于刻画JRC的各向异性 [Bao 2020, pp. 3-5]。

## Reusable Claims
- **Claim 1:** 在使用Xie and Pariseau (1994)分形方法基于三维激光扫描数据计算JRC时，为确保计算值的稳定性，剖面线采样间隔应小于4 mm，此阈值与节理本身的粗糙度无关 [Bao 2020, pp. 1-1, pp. 5-8]。（限制条件：此阈值在闪长岩节理样本上验证，可能不适用于所有岩性或计算方法。）
- **Claim 2:** 数字点采样间隔的阈值（y）与节理粗糙度系数（JRC，x）之间存在负指数关系，可表示为 `y = 1.8314e^(-x/0.067)`。因此，对于更光滑的节理（低JRC），可以容忍较大的采样间隔，反之则需要更高的采样分辨率 [Bao 2020, pp. 3-5]。（证据来源：基于10条不同粗糙度剖面线的实验数据拟合。）
- **Claim 3:** 即使是同一组节理，其JRC值也表现出显著的各向异性和遵从对数正态分布的统计变异性。因此，使用单一方向、单一测线的JRC值，或用算术平均值代表该组节理的粗糙度具有局限性 [Bao 2020, pp. 5-8]。（证据来源：对31个样本多方向JRC值的统计分析。）
- **Claim 4:** 相比算术平均值，采用对数正态分布函数的期望值作为JRC的代表值能更合理地反映真实概率分布特征，两者之间的差异可能高达23.1% [Bao 2020, pp. 5-8]。（限制条件：此结论基于JRC服从对数正态分布这一统计发现。）
- **Claim 5:** 无论剖面线采样间隔如何，JRC计算结果都存在显著的[[各向异性]]，并且不同方向上JRC值的变异性也很大 [Bao 2020, pp. 1-1, pp. 5-8]。（未从索引片段中确认各向异性程度的具体量化指标。）

## Candidate Concepts
- [[Joint Roughness Coefficient]]
- [[Fractal Dimension]]
- [[Sampling Effect]]
- [[Scale Effect]]
- [[Anisotropy]]
- [[Log-normal Distribution]]
- [[Rock Joint Morphology]]
- [[Shear Strength of Rock Joints]]

## Candidate Methods
- [[3D Laser Scanning]]
- [[Fractal Theory for Rock Joints]]
- [[Geomagic (Software)]]
- [[Statistical Distribution Fitting]]

## Connections To Other Work
- **采样间隔的影响：** 本研究的出发点建立在先前研究基础上，这些研究已经确认采样间隔会影响分形维数（Lee et al., 1990; Bae et al., 2011; Xia et al., 2014）和JRC计算（Jang et al., 2014; Li and Huang, 2015）[Bao 2020, pp. 1-2]。本研究在此基础上，进一步确定了发生影响的阈值。
- **JRC的各向异性和概率分布：** 本文对JRC各向异性的研究是先前关于粗糙度空间分布研究的延续（Chen et al., 2016; Chen et al., 2017; Liu et al., 2018; Wang et al., 2019）[Bao 2020, pp. 1-2]。
- **JRC各向异性的后果：** 研究指出，JRC的各向异性会显著影响岩体的剪切行为（Yang et al., 2001; Zheng and Qi, 2016; Kumar and Verma, 2016; Meng et al., 2018; Zhou et al., 2019）和节理渗流的不确定性（Roy and Singh, 2016; Luo et al., 2016; Yin et al., 2019b）[Bao 2020, pp. 1-2]。
- **主题连接：** 本研究可连接到关于[[岩石节理剪切强度准则]]、[[裂隙渗流]]、[[岩体稳定性分析]]等领域的文献，为这些研究提供更精确的粗糙度输入参数。也可以连接到使用其他粗糙度量化方法（如[[Variogram Method]]）的工作 [Bao 2020, pp. 8-9]。

## Open Questions
- 其他不同岩性、不同成因类型节理的剖面线采样间隔阈值是否也是4 mm，还是具有普适性阈值？
- 如何将该研究发现的JRC对数正态分布特征和各向异性，系统地集成到岩体剪切强度准则和数值模拟模型中？
- 基于该研究成果，能否发展出标准化的三维JRC测试与采样规范，以消除采样效应对工程评价的影响？[Bao 2020, pp. 5-8]

## Source Coverage
本页依据7个索引片段生成，这些片段主要覆盖了论文的摘要、引言（部分）、方法、关键结果和结论部分。关于研究区域的详细地质背景、样本的详细描述、结果的具体数据（如图表细节）、讨论部分的完整内容以及所有参考文献细节，在当前片段中覆盖不完整或缺失。特别是，对于“分布特征”部分仅进行了概括性描述，缺少对各向异性分布图的详细解读。
