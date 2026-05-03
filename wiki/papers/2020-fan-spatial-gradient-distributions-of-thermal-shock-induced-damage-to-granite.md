---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-fan-spatial-gradient-distributions-of-thermal-shock-induced-damage-to-granite"
title: "Spatial Gradient Distributions of Thermal Shock-Induced Damage to Granite."
status: "draft"
source_pdf: "data/papers/2020 - Spatial gradient distributions of thermal shock-induced damage to granite.pdf"
collections:
citation: "Fan, Lifeng, et al. \"Spatial Gradient Distributions of Thermal Shock-Induced Damage to Granite.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 12, 2020, pp. 917-926."
indexed_texts: "9"
indexed_chars: "43412"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43590"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.0041"
coverage_status: "full-index"
source_signature: "b247bedcf56f240d769c95540d27815536e0f445"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:37:40"
---

# Spatial Gradient Distributions of Thermal Shock-Induced Damage to Granite.

## One-line Summary
利用X射线CT技术和图像分析定量研究了热冲击引起的花岗岩损伤的空间梯度分布特征，发现快速水冷导致表面损伤最大、内部最小的梯度分布，且梯度随预热温度先增后降，在800 °C时梯度可忽略 [Fan 2020, pp. 1-1]。

## Research Question
- 快速冷却引起的热冲击如何在花岗岩内部形成空间梯度损伤分布？
- 预热温度如何影响这种空间梯度的大小和特征？
- 能否用三维CT技术定量表征这类梯度并揭示其机理？  
这些问题基于以下背景：已有研究表明热冲击会劣化岩石宏观物理力学性质，但对其三维空间梯度分布的定量CT研究尚属空白 [Fan 2020, pp. 1-2]。

## Study Area / Data
- **岩性**：花岗岩，取自山东省日照市；平均单轴抗压强度180 MPa，平均杨氏模量31.7 GPa [Fan 2020, pp. 2-3]。
- **矿物组成**：石英37%、斜长石36.2%、钾长石20.6%、云母2.7%、方解石2.5%、黏土矿物1%（D8‑ADVANCE X射线衍射仪） [Fan 2020, pp. 2-3]。
- **试件**：CT试件尺寸10 mm × 10 mm × 20 mm；共33块，按预热温度分为6组：25 °C、200 °C、400 °C、500 °C、600 °C、800 °C。每组6块（200–800 °C）或3块（25 °C）；每温度下3块快速冷却、3块缓慢冷却 [Fan 2020, pp. 2-3]。
- **CT扫描参数**：Nano Voxel‑2200系统，电压130 kV，电流80 mA，体素尺寸16 μm × 16 μm × 16 μm；分析区域为9.6 mm × 9.6 mm × 9.6 mm的立方体，以避开边缘硬化效应 [Fan 2020, pp. 3-5]。

## Methods
1. **热冲击处理**：以2.5 °C/min速率缓慢升温至目标温度，恒温3 h；快速冷却组立即浸入自来水，缓慢冷却组在关闭烘箱中冷至室温 [Fan 2020, pp. 2-3]。
2. **CT扫描与三维重建**：对处理后试件进行CT扫描，用Voxel Studio Recon软件将二维切片叠加重建三维体积数据 [Fan 2020, pp. 3-5]。
3. **损伤量化**：基于三维图像计算孔隙度 \(P = V_{\text{Pore}} / V_{\text{Total}} \times 100\%\) [Fan 2020, pp. 5-7]。
4. **空间梯度分析**：将立方体分析区域等体积划分为5个局部区域（区域1至区域5，由内向外），计算各区域孔隙度 \(P_i\)；  
   引入梯度参数 \(k_i = (P_{i+1} - P_i) / d_i\)（\(d_i\)为区域间距离）；当\(k_1, k_2, k_3, k_4\)均大于零时，视为存在空间梯度分布 [Fan 2020, pp. 7-8]。
5. **梯度拟合**：对各预热温度下快速冷却试件，将孔隙度与距中心距离进行线性拟合，以拟合斜率评价梯度大小 [Fan 2020, pp. 8-9]。

## Key Findings
1. 快速冷却引起的热冲击对花岗岩造成的损伤大于缓慢冷却 [Fan 2020, pp. 1-1]。
2. 快速冷却引起的热冲击可造成损伤的空间梯度分布：近表面损伤最大，内部损伤最小 [Fan 2020, pp. 1-1]。
3. 预热温度显著影响空间梯度：400–600 °C时梯度随温度升高而增大；600 °C以上梯度急剧减小；800 °C时梯度可忽略不计（损伤趋于均匀） [Fan 2020, pp. 1-1, 8-9]。
   - 图10显示400–600 °C下快速冷却的\(k_1\)–\(k_4\)均为正值，证实梯度存在；800 °C时出现正负交替，梯度效应不再明显 [Fan 2020, pp. 7-8]。
   - 图11显示快速冷却试件各局部区域孔隙度随距中心距离近似线性增加；图12显示梯度先增后降，800 °C时梯度接近零 [Fan 2020, pp. 8-9]。
4. 微观裂纹的发育过程：400 °C快速冷却后在长石矿物中出现新微裂纹；500 °C时裂纹向试件外边界集中；600 °C时低密度长石矿物中裂纹显著增多；800 °C时石英中出现穿晶裂纹并形成裂纹网络 [Fan 2020, pp. 3-5]。
5. 缓慢冷却处理的试件在500 °C后才观察到明显新微裂纹；各预热温度下缓慢冷却均未表现出类似快速冷却的梯度特征 [Fan 2020, pp. 3-5, 7-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 快速冷却造成更多损伤；孔隙度差异随温度升高而增大 | [Fan 2020, pp. 5-7], Fig. 7 | 花岗岩，25–800 °C，水冷/炉冷 | 缓慢冷却孔隙度始终低于快速冷却 |
| 400 °C、500 °C、600 °C快速冷却后k₁–k₄均>0，表明存在空间梯度分布 | [Fan 2020, pp. 7-8], Fig. 10a–c | 预热温度400–600 °C，水冷 | 缓慢冷却k值有正有负，无稳定梯度 |
| 800 °C快速冷却后部分k值<0，梯度可忽略 | [Fan 2020, pp. 7-8], Fig. 10d | 预热温度800 °C，水冷 | 损伤接近均匀 |
| 梯度随预热温度升高而增大，600 °C以上显著下降 | [Fan 2020, pp. 8-9], Fig. 12 | 400–800 °C，水冷 | 线性拟合斜率表征梯度 |
| 400 °C快速冷却后长石中出现新微裂纹；500 °C裂纹向外边界集中；600 °C裂纹在长石中显著增多；800 °C石英中出现穿晶裂纹并成网 | [Fan 2020, pp. 3-5], Fig. 5 | 各预热温度下水冷试件二维CT切片 | 缓慢冷却500 °C才见明显裂纹 |
| 分析区域（9.6 mm³立方体）避开了边缘硬化效应，选自试件内部12–611层（x,y）和325–924层（z） | [Fan 2020, pp. 3-5] | Nano Voxel‑2200 CT，体素16 μm | 边缘硬化效应使表面灰度偏高 |

## Limitations
- 本研究主要关注热冲击损伤的空间梯度分布特征，未对不同矿物（如石英、长石、云母）中的热裂纹进行定量分析，也未通过数值模拟揭示裂纹萌生机理 [Fan 2020, pp. 9-10]。
- CT分辨率（16 μm/体素）可能无法捕捉全部微裂纹，且分析区域局限于内部立方体，最外缘（受边缘硬化影响）被排除，可能低估近表面损伤 [Fan 2020, pp. 3-5]。
- 试件尺寸较小（10 mm × 10 mm × 20 mm），由小尺寸试件得出的损伤梯度规律在工程尺度上的适用性尚待验证 [Fan 2020, pp. 2-3]。
- 仅利用孔隙度（损伤体积占比）表征损伤，未结合波速、强度等宏观性质变化进行关联 [Fan 2020, pp. 1-1]。

## Assumptions / Conditions
- 热冲击损伤主要由快速水冷过程中的瞬时温度梯度引起，加热阶段（2.5 °C/min）的热冲击影响可忽略 [Fan 2020, pp. 2-3]。
- 二维CT切片叠加重建的三维数据能够真实反映孔隙和裂纹空间分布 [Fan 2020, pp. 3-5]。
- 区域划分基于等体积原则，并假设同组内各试件的响应一致（每组3个试件，取典型结果展示） [Fan 2020, pp. 2-3, 7-8]。
- 梯度参数\(k_i > 0\)（\(i=1,\dots,4\)）作为判断空间梯度分布存在的依据，但该判据仅适用于单调递增趋势；800 °C时实验误差可能导致局部波动 [Fan 2020, pp. 7-8]。
- 文中快速冷却对比仅限浸入自来水，未涵盖其他冷却介质（如液氮）的影响 [Fan 2020, pp. 9-10]。

## Key Variables / Parameters
- 预热温度\(T_{\text{pre}}\) (°C)：25, 200, 400, 500, 600, 800 [Fan 2020, pp. 2-3]
- 冷却方式：快速冷却（水冷）vs. 缓慢冷却（炉冷） [Fan 2020, pp. 2-3]
- 局部区域编号\(i\)：1～5（由内向外） [Fan 2020, pp. 7-8]
- 局部区域孔隙度\(P_i\) (%) [Fan 2020, pp. 7-8]
- 梯度参数\(k_i = (P_{i+1} - P_i) / d_i\) (mm⁻¹) [Fan 2020, pp. 7-8]
- 全区域孔隙度\(P\) (%) [Fan 2020, pp. 5-7]
- 距试件中心距离\(d\) (mm) [Fan 2020, pp. 8-9]
- 线性拟合斜率（梯度） [Fan 2020, pp. 8-9]
- 矿物成分：石英37%，斜长石36.2%，钾长石20.6%，云母2.7%，方解石2.5%，黏土1% [Fan 2020, pp. 2-3]
- CT体素尺寸：16 μm × 16 μm × 16 μm [Fan 2020, pp. 3-5]

## Reusable Claims
- 快速水冷引起的热冲击对花岗岩造成的损伤高于缓慢冷却，且差异随预热温度升高而增大 [Fan 2020, pp. 5-7]。
- 快速水冷可引起花岗岩损伤的空间梯度分布：近表面孔隙度最大，内部最小；缓慢冷却不具此特征 [Fan 2020, pp. 1-1, 7-8]。
- 梯度大小受预热温度控制：在400–600 °C范围内随温度升高而增大；超过600 °C后梯度显著下降；800 °C时梯度可忽略，此时裂纹贯通整个试件使损伤趋于均匀 [Fan 2020, pp. 8-9]。
- 三维CT结合局部区域划分和梯度参数\(k_i\)可有效定量表征热冲击损伤的空间梯度 [Fan 2020, pp. 7-8]。
- 对于花岗岩，400 °C即开始出现热冲击诱发的微裂纹（主要集中在长石中），600 °C后裂纹数量急剧增加，800 °C时形成穿晶裂纹网络 [Fan 2020, pp. 3-5]。

## Candidate Concepts
- [[热冲击（thermal shock）]]
- [[空间梯度损伤（spatial gradient damage）]]
- [[CT三维重建（3D CT reconstruction）]]
- [[孔隙度（porosity）]]
- [[梯度参数k_i]]
- [[边缘硬化效应（beam hardening）]]
- [[花岗岩矿物组成（quartz, plagioclase, K‑feldspar）]]
- [[热传导差异导致的温度梯度（small thermal conduction）]]
- [[热致微裂纹（thermally-induced microcracks）]]
- [[快速冷却（rapid cooling/water quenching）]]

## Candidate Methods
- [[缓慢预热+快速水冷热冲击实验（slow preheating + water quenching）]]
- [[高分辨率X射线CT扫描（Nano Voxel‑2200）]]
- [[基于二维切片的3D体积重建（Voxel Studio Recon）]]
- [[三维孔隙度计算（P = Vpore / Vtotal）]]
- [[等体积局部区域划分法（equal‑volume local regions）]]
- [[梯度参数k_i计算与判别]]
- [[线性拟合斜率评估空间梯度（gradient as slope of porosity‑distance line）]]

## Connections To Other Work
- **Kim et al. (2013)** 和 **Li et al. (2020)** 指出，热传导较差的材料（如花岗岩）中热冲击可产生空间梯度损伤，近表面损伤大于内部；本研究用CT定量验证了该现象 [Fan 2020, pp. 1-1]。
- **Kumari et al. (2017, 2018)** 发现快速冷却导致花岗岩强度和弹性模量下降更大，且热冲击提高孔隙率和渗透率；本研究的孔隙度结果与之相符 [Fan 2020, pp. 1-2]。
- **Wu et al. (2019)** 表明水温冷却时花岗岩抗拉强度最低，且该差异在预热温度高于600 °C时更显著；本文在600 °C以上观察到裂纹急剧增多和梯度衰减，可能解释强度转折 [Fan 2020, pp. 1-2, 8-9]。
- **Jin et al. (2019)** 和 **Rathnaweera et al. (2018)** 利用表面显微技术揭示了热冲击微裂纹劣化宏观特性的机理；本研究通过3D CT将观测拓展到三维梯度 [Fan 2020, pp. 1-2]。
- **Isaka et al. (2019)** 利用CT研究了热冲击对花岗岩孔隙连通性的影响，并观察到预热300 °C后试件外缘开始出现损伤；本研究系统量化了400 °C以上损伤的空间梯度，补充了前期观察 [Fan 2020, pp. 1-2]。
- **Jansen and Carlson (1993)** 用超声成像和声发射监测建立了热损伤梯度分布的概念；本研究首次采用3D CT给予定量支持 [Fan 2020, pp. 1-2]。

## Open Questions
- 尚需定量分析不同矿物（石英、长石、云母等）内部热冲击裂纹的萌生与扩展特征 [Fan 2020, pp. 9-10]。
- 需要建立数值模拟方法揭示热冲击致裂的微观机理，并与CT实验观测相互验证 [Fan 2020, pp. 9-10]。
- 本实验所用小尺寸试件得到的梯度规律在更大尺度岩石工程中的适用性有待研究 [Fan 2020, pp. 2-3]。
- 其他冷却介质（如液氮）造成的热冲击是否会产生相似或更强的梯度效应？ [Fan 2020, pp. 9-10]。
- 热冲击损伤的空间梯度与宏观物理力学性质（强度、波速、渗透率）的定量关系尚未建立 [Fan 2020, pp. 1-1]。

## Source Coverage
本文档全部基于提供的索引片段编译而成，未使用片段以外的任何信息。  
共处理**9个**非空源块，总计**43,590**字符（源片段总字符数43,412），覆盖率为**100%**（按块计为1.0，按字符计为1.0041）。  
源签名：`b247bedcf56f240d769c95540d27815536e0f445`，编译策略为单次直通Markdown生成。
