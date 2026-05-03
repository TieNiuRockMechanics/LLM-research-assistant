---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using"
title: "Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography."
status: "draft"
source_pdf: "data/papers/2017 - Surface roughness characterization of open and closed rock joints in deep cores using X-ray computed tomography.pdf"
collections:
  - "zotero new"
citation: "Diaz, Melvin, et al. \"Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography.\" *International Journal of Rock Mechanics & Mining Sciences*, www.elsevier.com/locate/ijrmms. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42296"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42488"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004539"
coverage_status: "full-index"
source_signature: "83903002fd13fee4ec9e307a7ab63d32c62ddefc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:27:03"
---

# Surface Roughness Characterization of Open and Closed Rock Joints in Deep Cores Using X-ray Computed Tomography.

## One-line Summary
本研究利用 X 射线 CT 扫描技术对约 4.2 km 深处花岗岩岩心中的开放与闭合岩石节理进行表面粗糙度定量，揭示了显著的粗糙度各向异性以及两类节理在形貌参数上的高度相似性。

## Research Question
如何利用 X 射线 CT 技术获取深层岩心中闭合节理的三维形貌？在 >4 km 深度下，开放节理与闭合节理的粗糙度参数（JRC、偏度、峰度、最大高度）及其各向异性特征有何异同？ [Diaz 2026, pp. 1-2]

## Study Area / Data
- 地点：韩国浦项地区 EGS 项目 PX‑2 井 [Diaz 2026, pp. 1-2]
- 岩心深度：4219–4223 m [Diaz 2026, pp. 1-2]
- 岩性：中粒花岗岩，无风化迹象 [Diaz 2026, pp. 1-2]
- 岩心规格：直径 10 cm，总长度 3.6 m [Diaz 2026, pp. 1-2]
- 节理样本：5 条开放节理（OJ-1 ~ OJ‑5）与 2 条闭合节理（CJ‑1, CJ‑2），与取芯方向夹角介于 10°–30° 之间 [Diaz 2026, pp. 1-2; pp. 2-4]
- 补充：岩心观测时两个主要节理组，一组与取芯方向约呈 80° 相交，另一组约呈 20°；闭合节理通过 CT 证实 [Diaz 2026, pp. 1-2]

## Methods
- **X 射线 CT 扫描**：采用韩国 KICT 的 X‑EYE CT 系统。各段扫描参数见表 1，温度 21 °C，湿度 31%，曝光时间 1 s，投影数 1800。体素数据用于 3D 渲染并提取节理表面（尤对闭合节理唯一可行）[Diaz 2026, pp. 2-4]
- **表面点云生成**：评估四种粗糙度参数随网格尺寸的变化后，选择固定正方形网格尺寸 0.1 mm 生成点云 [Diaz 2026, pp. 4-5]
- **粗糙度参数**：
  - JRC 采用 Li & Zhang (2015) 公式：\[JRC = 158.7575 + 3.9076 \, \lambda\]，其中 \(\lambda = a/L\)（a 为轮廓最大高度，L 为投影长度），采样间隔 0.4 mm [Diaz 2026, pp. 2-4]
  - 偏度 (Rsk)、峰度 (Rku) 按公式 (3)(4) 计算 [Diaz 2026, pp. 2-4]
  - 三维最大高度 Sz 按公式 (5) 计算 [Diaz 2026, pp. 4-5]
  - 所有参数通过自主代码在全校验方向上生成轮廓后计算。
- **各向异性分析**：在 18 个方向（每 10° 逆时针）上提取间距 2.5 mm 的轮廓，计算每个方向的 JRC、Rsk、Rku，取平均值时仅保留距均值一个标准差内的测量值 [Diaz 2026, pp. 4-5]
- **椭圆拟合**：对每个节理的 JRC 方向数据采用最小二乘椭圆拟合，重新确定最大与最小 JRC 值及其精确方向 [Diaz 2026, pp. 6-8]
- **尺度依赖性评估**：在 OJ‑1、OJ‑4、OJ‑5 上由中心开始逐步扩大正方形采样窗口（边长增量 2.5 mm），观察平均 JRC 及最大 JRC 方向的变化 [Diaz 2026, pp. 5-6]

## Key Findings
1. 闭合节理与开放节理在表面积、最大高度 Sz、偏度、峰度、平均 JRC（椭圆拟合后）以及最大 JRC 方向上数值相似，暗示共同起源 [Diaz 2026, pp. 6-8]
2. 所有节理均呈现明显粗糙度各向异性，最大与最小 JRC 比值介于 1.16–1.54 [Diaz 2026, pp. 8-10]
3. 经椭圆拟合后，7 条节理的最大 JRC 方向平均值为 161.2°（自节理底板倾角线逆时针测量），标准差仅 5.4° [Diaz 2026, pp. 8-10]
4. JRC 具有尺度依赖性，当采样面积达到一定阈值后收敛；而最大 JRC 的方向在较小面积下即已稳定 [Diaz 2026, pp. 5-6]
5. 偏度和峰度分析：大多数节理相对对称；OJ‑2、OJ‑4、OJ‑5 的偏度绝对值 >0.2；OJ‑5 为尖峭峰态 (leptokurtic)；OJ‑3、OJ‑4、OJ‑5 显示出峰度的方向性 [Diaz 2026, pp. 5-6]
6. 与法国 Soultz‑sous‑Forêts EPS‑1 井岩心中节理的 JRC（10.84, 16.98, 9.5）相比，浦项岩心 JRC 范围（6.6~19.2）与之重叠，但深度更大（4.2 km vs. 1.3~2.1 km）[Diaz 2026, pp. 8-10]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| OJ‑1 最大 JRC 12.5，最小 8.6，比值 1.5，方向 163.7° | [Diaz 2026, pp. 8-10] Table 3 | 全表面椭圆拟合 | |
| CJ‑1 平均 JRC 11.7，最大 12.6，最小 10.9，比值 1.16 | [Diaz 2026, pp. 8-10] Table 3 | 全表面 | 各向异性最弱 |
| 点云网格尺寸 0.1 mm 时粗糙度参数稳定，Rp 和 Z2 在 >1 mm 后下降显著 | [Diaz 2026, pp. 4-5] | OJ‑1 测试 | Ra, Rq 变异系数 <0.025 |
| JRC 收敛阈值：OJ‑1 1600 mm², OJ‑4 6006 mm², OJ‑5 1406 mm² | [Diaz 2026, pp. 5-6] | 正方形采样区 | 收敛标准：相邻窗口平均 JRC 差异 ≤1 |
| OJ‑3 最大高度 Sz=20.1 mm，OJ‑5 Sz=3.7 mm | [Diaz 2026, pp. 2-4] Table 2 | | |
| 最大 JRC 方向平均值 161.2°，标准差 5.4° | [Diaz 2026, pp. 8-10] | 7 条节理椭圆拟合 | |
| OJ‑5 平均峰度 3.37，为尖峭峰态 | [Diaz 2026, pp. 5-6] | | 其它节理多数 2.5~2.9 |

## Limitations
- 样本量小（5 条开放，2 条闭合），统计代表性受限 [Diaz 2026, pp. 8-10]
- JRC 计算仅使用 Li & Zhang (2015) 单一方程，未对比其他关系式 [Diaz 2026, pp. 2-4]
- 各向异性测量仅基于 18 个方向，可能遗漏更细致的变化 [Diaz 2026, pp. 4-5]
- 闭合节理的表征完全依赖 CT 密度差异，若愈合矿物与围岩密度接近则难以辨识 [Diaz 2026, pp. 2-4]
- 未对不同扫描参数（如电压、滤波）可能造成的表面细节差异进行系统分析 [Diaz 2026, pp. 2-4]

## Assumptions / Conditions
- 所用 JRC 公式被认为不受采样间距影响 [Diaz 2026, pp. 2-4]
- 固定点云网格尺寸 0.1 mm 可充分捕捉粗糙度特征 [Diaz 2026, pp. 4-5]
- 剔除超出一个标准差的值可提高各方向代表性 [Diaz 2026, pp. 4-5]
- 各向异性分布可用椭圆近似 [Diaz 2026, pp. 6-8]
- CT 能可靠区分闭合节理界面 [Diaz 2026, pp. 2-4]

## Key Variables / Parameters
- 点云网格尺寸：0.1 mm [Diaz 2026, pp. 4-5]
- JRC 公式：JRC = 158.7575 + 3.9076 λ [Diaz 2026, pp. 2-4]
- JRC 轮廓采样间距：0.4 mm [Diaz 2026, pp. 4-5]
- 各向异性测量方向数：18（间隔 10°）[Diaz 2026, pp. 4-5]
- 轮廓线间距：2.5 mm [Diaz 2026, pp. 4-5]
- 节理与取芯方向夹角：10°–30° [Diaz 2026, pp. 1-2]
- 三维最大高度 Sz [Diaz 2026, pp. 2-4]

## Reusable Claims
- 利用 X 射线 CT 可在深层岩心中有效提取闭合节理表面形貌并开展粗糙度定量分析（若存在密度差异）[Diaz 2026, pp. 2-4]
- 同一井段内开放与闭合节理的粗糙度参数（Sz、平均 JRC、偏度、峰度、主方向）高度一致，指示共同起源 [Diaz 2026, pp. 6-8]
- 约 4.2 km 深处的花岗岩节理，其最大 JRC 方向集中于 ~161°（逆时针自节理底板倾角线），可作为古应力方向的间接指示 [Diaz 2026, pp. 8-10]
- JRC 的尺度依赖性在采样面积达到一定阈值后收敛，而最大 JRC 方向在较小面积下即已稳定 [Diaz 2026, pp. 5-6]

## Candidate Concepts
- [[粗糙度各向异性]]
- [[节理粗糙度系数 (JRC)]]
- [[X射线CT岩石节理提取]]
- [[深层闭合节理]]
- [[JRC 尺度依赖性]]
- [[椭圆拟合方向分析]]
- [[尖峭峰态 / 平缓峰态]]
- [[古应力方向估算]]
- [[EGS 储层节理粗糙度]]
- [[点云网格尺寸敏感性]]

## Candidate Methods
- [[基于 X 射线 CT 的岩石节理三维表面重构]]
- [[多方向 JRC 各向异性测量法]]
- [[最小二乘椭圆拟合确定粗糙主方向]]
- [[体素点云网格优化]]
- [[Li & Zhang (2015) 的 λ-based JRC 公式]]
- [[粗糙度参数集 (Sz, Rsk, Rku, JRC) 联合表征]]

## Connections To Other Work
- 与 Soultz‑sous‑Forêts EPS‑1 井节理粗糙度（Z2 值换算的 JRC）处于同一数量级，但该研究深度更大 [Diaz 2026, pp. 8-10]
- 方向性分析方法参照 Huang & Doong (1990) 的多方向 JRC 评估思路 [Diaz 2026, pp. 4-5]
- 观测到的粗糙度各向异性可能影响剪切扩容各向异性 (Koyama et al., 2006) 和流体流动各向异性 (Yeo et al., 1998)，进而影响 EGS 井位布局 [Diaz 2026, pp. 8-10]
- 文内提及 Ledésert et al. (1993) 发现节理粗糙度随深度增加而降低的趋势，本研究未直接进行分形对比 [Diaz 2026, pp. 8-10]

## Open Questions
- 在其他深度或不同构造环境的深层岩心中，是否同样存在一致的 ~161° 方向性？ [Diaz 2026, pp. 8-10]
- 闭合节理的愈合物质组成对粗糙度参数的具体影响如何？ [Diaz 2026, pp. 6-8]
- 若更换 JRC 公式（如 Tse & Cruden 的 Z2 或 SF 式），各向异性结论是否改变？ [Diaz 2026, pp. 2-4]
- 最大 JRC 方向与原地应力方向之间的直接关联尚需进一步验证 [Diaz 2026, pp. 8-10]
- 提高 CT 扫描分辨率能否捕捉更细微的结构进而改变尺度依赖性收敛阈值？ [Diaz 2026, pp. 4-5]

## Source Coverage
所有非空索引片段均已处理。共 9 个源块，总计 42488 字符，块覆盖率 1.0，字符覆盖率 1.0045。源签名：83903002fd13fee4ec9e307a7ab63d32c62ddefc，覆盖状态：full-index。本文所有陈述均来自提供的片段 [Diaz 2026]。
