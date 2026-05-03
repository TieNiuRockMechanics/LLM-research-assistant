---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales"
title: "Roughness of Fault Surfaces over Nine Decades of Length Scales."
status: "draft"
source_pdf: "data/papers/unknown-year - Roughness of fault surfaces over nine decades of length scales.pdf"
collections:
  - "粗糙裂隙渗流"
citation: "Candela, Thibault, et al. “Roughness of Fault Surfaces over Nine Decades of Length Scales.” *Journal of Geophysical Research*, vol. 117, B08409, 2012, doi:10.1029/2011JB009041."
indexed_texts: "27"
indexed_chars: "133631"
nonempty_source_blocks: "27"
compiled_source_blocks: "27"
compiled_source_chars: "134280"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004857"
coverage_status: "full-index"
source_signature: "85b38d30aacde16bb7ae398076c5a2829fc7fa49"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:57:30"
---

# Roughness of Fault Surfaces over Nine Decades of Length Scales.

## One-line Summary
本研究在九个数量级长度尺度（50 µm 至 50 km）上测量了五个出露断层和十三条地震地表破裂的粗糙度，发现其具有各向异性自仿射（anisotropic self-affine）特性，可用两个 Hurst 指数描述：沿滑移方向约 0.58，垂直滑移方向约 0.81，且该几何描述可延伸覆盖九个数量级 [Candela 2012, pp. 1-1]。

## Research Question
断层粗糙度控制着断层的力学行为、传输特性及三维架构 [Candela 2012, pp. 1-1]。本研究旨在通过统一统计工具（傅里叶功率谱分析）考察不同地质背景下出露断层表面与地震破裂迹线的自仿射标度特性，以确定是否在整个九数量级尺度上存在一致的几何描述，并量化 Hurst 指数与前置因子（pre‑factor）的波动 [Candela 2012, pp. 1-2]。

## Study Area / Data
**出露断层表面（3D 地形数据，尺度 50 µm–10 m）：**
- Vuache‑Sillingy 断层（法国，灰岩，走滑，滑移 10–30 m）
- Corona Heights 断层（美国，燧石，走滑，数米–>1 km）
- Bolu 断层（土耳其，灰岩，走滑，20 m–85 km）
- Dixie Valley 断层（美国，流纹岩，正断，数米–3–6 km）
- Magnola 断层（意大利，灰岩，正断，数米–>500 m） [Candela 2012, pp. 2-5]

**地震地表破裂（2D 剖面，尺度 200 m–50 km）：**
13 条大型大陆地震破裂迹线，包括 Owens Valley、Haiyuan、Gobi‑Altay、Superstition Hills、Luzon、Landers、Zirkuh、Hector Mine、Kashmir、Chi‑Chi、Wenchuan、Hebgen Lake、Borah Peak [Candela 2012, pp. 5-5; 8-9]。

## Methods
- **扫描设备**：LiDAR（场测，空间分辨率 1–30 mm）、激光轮廓仪（实验室，20 µm）、白光干涉仪（WLI，1–2 µm）[Candela 2012, pp. 1-1; 5-8]。
- **数据处理**：将 3D 点云转换为 2D+1D 数据集，沿不同方向提取剖面，经线性插值至规则间距；去除线性趋势（首末点连线）并施加 3% 余弦锥形窗 [Candela 2012, pp. 9-10]。
- **功率谱分析**：计算各剖面傅里叶功率谱，按波数级数平均，得到自仿射指数 H（Hurst 指数）和前置因子 C。H 由功率谱 P(k) ∝ k^(-1-2H) 拟合获得 [Candela 2012, pp. 2-2; 9-11]。对地震破裂迹线进行类似处理，但仅分析二维剖面 [Candela 2012, pp. 8-9]。

## Key Findings
- 五个出露断层在 0.05 mm 至 10 m 尺度上呈现各向异性自仿射特性：**沿滑移方向 Hk = 0.58 ± 0.07，垂直滑移方向 H⊥ = 0.81 ± 0.04** [Candela 2012, pp. 10-11]。
- Hurst 指数在各断层间一致，前置因子则存在空间变异 [Candela 2012, pp. 11-14]。
- 13 条地震破裂迹线在 200 m–50 km 尺度上可用单一自仿射指数 0.8 ± 0.1 描述，与断层垂直滑移方向的 H⊥ 相符 [Candela 2012, pp. 14-16]。
- 尽管扫描断层与破裂迹线之间存在数据空白，当前测量在误差范围内支持九数量级尺度下的一致性几何描述 [Candela 2012, pp. 1-1; 21-22]。
- 一旦积累少量位移（约数米），断层几何复杂性即不再随滑移量显著变化，暗示存在再粗化机制 [Candela 2012, pp. 22-23]。

## Core Evidence Table
| 证据 | 来源 | 条件 | 注释 |
|------|------|------|------|
| 五个出露断层的 Hurst 指数 Hk = 0.58 ± 0.07（滑移方向） | [Candela 2012, pp. 10-12] Table 1b, Fig. 7 | 出露滑动面，三种设备组合 (LiDAR + 激光轮廓仪 + WLI)，尺度 0.05 mm–10 m | 对 41 个子表面独立计算；指数在 2σ 内一致 |
| 同一组断层的 H⊥ = 0.81 ± 0.04（垂直滑移方向） | [Candela 2012, pp. 10-12] Table 1b, Fig. 7 | 同上 | 各向异性明显 |
| 13 条地震破裂迹线的 Hurst 指数 HR = 0.8 ± 0.1 | [Candela 2012, pp. 14-16] Table 2, Fig. 12 | 2D 破裂迹线，尺度 200 m–50 km；分割段与重建迹线分析 | 与 H⊥ 一致；走滑、逆冲、正断破裂均适用 |
| 前置因子在不同断层子表面间变化明显（功率谱垂直偏移） | [Candela 2012, pp. 12-14] Fig. 8, Fig. 9, Table 3 | LiDAR 尺度下同一断层多个 patch | 反映自然变异性，需大量样本捕捉均值 |
| 断层粗糙度与总滑移量无明显相关（滑移 > 数米后） | [Candela 2012, pp. 16-18, 21-22] Fig. 10, Fig. 12b | 出露断层和破裂迹线 | 支持几何复杂性可持续保持的观点 |
| 混合效应导致破裂迹线主要反映垂直滑移的粗糙度 | [Candela 2012, pp. 18-21] Fig. 14 | 合成表面测试与天然断层 patch 对比 | Hurst 指数对角度变化非线性敏感；前置因子线性响应 |

## Limitations
- 扫描断层表面（<10 m）与地震破裂迹线（>200 m）之间存在尺度和数据类型的缺口 [Candela 2012, pp. 1-1; 21-22]。
- 破裂迹线为二维剖面，无法直接获取全三维各向异性信息，且实际采样方向因垂直滑动分量和地形起伏而混合滑移‑垂直方向成分 [Candela 2012, pp. 18-21]。
- 断层总位移估算具有较大不确定性，影响滑移‑粗糙度关系分析 [Candela 2012, pp. 2-4, 8-9]。
- 部分断层（如 Magnola）可能受风化影响，但作者认为在研究所用尺度上影响不显著 [Candela 2012, pp. 5-5]。
- LiDAR 数据在波长 < 50 mm 时噪声淹没信号；故分析下限设置为 0.05 mm [Candela 2012, pp. 10-11]。
- 断层形成时的深度条件（围压、温度、应变速率等）难以精确限定 [Candela 2012, pp. 5-5]。

## Assumptions / Conditions
- 粗糙度满足自仿射标度：dx → λ dx, dz → λ^H dz，且傅里叶功率谱呈幂律形式 P(k) ∝ k^(-1-2H) [Candela 2012, pp. 1-2, 9-10]。
- 趋势去除仅使用首末点直线，以最大限度保留大尺度信息 [Candela 2012, pp. 9-10]。
- 对剖面施加 3% 余弦锥形窗以优化傅里叶变换，测试表明其对结果影响很小 [Candela 2012, pp. 10-10; 25-26]。
- 对于 LiDAR 数据，光谱分析仅应用于 0.05–10 m 波长范围，此时信号高于仪器噪声 [Candela 2012, pp. 10-11]。
- 破裂迹线重采样（规则间距）不改变大尺度标度行为，仅产生一小尺度截断区域 [Candela 2012, pp. 25-27]。

## Key Variables / Parameters
- Hk：沿滑移方向的 Hurst 指数（全局值为 0.58 ± 0.07 或简化为 0.6）[Candela 2012, pp. 10-12]
- H⊥：垂直滑移方向的 Hurst 指数（全局值为 0.81 ± 0.04 或简化为 0.8）[Candela 2012, pp. 10-12]
- HR：地震破裂迹线的 Hurst 指数（0.8 ± 0.1）[Candela 2012, pp. 14-16]
- 前置因子 Ck, C⊥：控制给定尺度的粗糙度幅度，因断层而异 [Candela 2012, pp. 1-2, 12-14]
- 扫描设备的空间分辨率 dx 和垂直精度 dz [Candela 2012, pp. 4-5] Table 1b
- 波长范围：50 µm–10 m（出露断层）；200 m–50 km（破裂迹线）[Candela 2012, pp. 1-1]
- 功率谱 P(k) [Candela 2012, pp. 9-10]

## Reusable Claims
- 断层滑动表面的粗糙度可用各向异性自仿射模型描述，其 Hurst 指数在滑移方向约为 0.6，在垂直滑移方向约为 0.8，适用于从 50 µm 到至少 10 m 的尺度范围。受同一滑动面不同子区域的前置因子变异性的限制 [Candela 2012, pp. 10-12, 12-14]。
- 大型大陆地震的地表破裂迹线具有自仿射粗糙度，Hurst 指数约为 0.8 ± 0.1，与出露断层表面在垂直滑移方向上的指数一致，覆盖从数百米到约 50 km 的尺度 [Candela 2012, pp. 14-16]。
- 出露断层表面的各向异性自仿射几何特性与地震破裂迹线的几何特性在九数量级长度尺度上相容，尽管存在几百米到十米级的数-据空白 [Candela 2012, pp. 21-22, 23-23]。
- 当断层已经积累数米以上的位移后，其粗糙度幅度（前置因子）与总滑移量无显著相关，说明几何复杂性可被持续保持 [Candela 2012, pp. 16-18, 22-22]。
- 由于混合效应，地表破裂迹线的 Hurst 指数主要反映断层垂直滑移方向的粗糙度，而非纯滑移方向；前置因子则随混合程度线性变化 [Candela 2012, pp. 18-21]。

## Candidate Concepts
- [[fault roughness]]
- [[self-affine scaling]]
- [[anisotropic roughness]]
- [[Hurst exponent]]
- [[Fourier power spectrum]]
- [[pre-factor variability]]
- [[fault maturity]]
- [[earthquake surface rupture]]
- [[corrugation lens]]
- [[scale-free process]]
- [[asperity squeeze]]
- [[off-fault damage]]
- [[roughness-slope relationship]]

## Candidate Methods
- [[LiDAR scanning]]
- [[laser profilometry]]
- [[white light interferometry]]
- [[Fourier power spectrum analysis]]
- [[self-affine profile extraction]]
- [[geometric matching of multi-scale scans]]
- [[resampling of rupture traces]]

## Connections To Other Work
- 研究结果与 Bistacchi 等（2011）报告的古地震深度断层 Hurst 指数（0.6–0.8，0.5 mm–500 m）一致，后者填补了本工作的数据空白 [Candela 2012, pp. 22-22]。
- 发现断层在滑移 >10 m 后粗糙度不随位移显著变化，与 Sagy 等（2007）关于大滑移断层的观测一致，也与 Brodsky 等（2011）的“平滑作用在滑移 >10 m 后非常微弱”的结论吻合 [Candela 2012, pp. 22-22]。
- 破裂迹线的标度特性支持 Klinger（2010）关于断层分段长度与地震成因壳厚度相关且与滑移量无关的观点 [Candela 2012, pp. 22-22]。
- 与前人基于断层自身多尺度裂隙网络控制粗糙度的猜想一致，并与断裂力学中大尺度粗糙度由长程弹性相互作用脉生的思想相呼应 [Candela 2012, pp. 22-23]。
- 断层粗糙度影响地震力学过程的数值模拟（如 Candela 等 2011a，2011b；Schmittbuhl 等 2006；Dunham 等 2011）可直接得益于本文提供的真实几何参数 [Candela 2012, pp. 18-18]。

## Open Questions
- 扫描断层表面（<10 m）与地震破裂迹线（>200 m）之间数百米量级的数据空缺仍需通过新的中尺度测量（如 Bistacchi 等 2011 的补充）进一步闭合 [Candela 2012, pp. 22-22, 23-23]。
- 地表变形测量（尤其是逆冲破裂迹线受滑坡干扰）是否完全代表深部断层几何，仍需更多约束 [Candela 2012, pp. 8-8]。
- 地表破裂迹线主要反映垂直滑移方向粗糙度，在约 10 km 以上尺度的各向异性表现如何尚不明确 [Candela 2012, pp. 18-21]。
- 维持断层几何复杂性的再粗化机制（如动态分支、断层泥润滑）尚无定量约束 [Candela 2012, pp. 22-23]。
- 白光干涉仪数据中 0.05 mm 处频谱弯曲是否对应粒子尺度的物理过程转变（如晶界/晶内破裂）有待专门研究 [Candela 2012, pp. 22-23]。
- 前置因子的系统差异（如逆冲/正断层迹线稍高于走滑迹线）是否反映某种系统性控制因素尚未解决 [Candela 2012, pp. 14-16]。

## Source Coverage
所有 27 个非空索引片段均被纳入本页面，未遗漏任何片段。编译后源区块 27 个，字符数 134，280。片段覆盖度：按区块计 1.0，按字符计 1.00486（即对源文档的完整再现，覆盖率超过 100%）[Candela 2012, pp. coverage audit data]。
