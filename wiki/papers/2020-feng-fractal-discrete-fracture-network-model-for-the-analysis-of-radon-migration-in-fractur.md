---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-feng-fractal-discrete-fracture-network-model-for-the-analysis-of-radon-migration-in-fractur"
title: "Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media."
status: "draft"
source_pdf: "data/papers/2020 - Fractal discrete fracture network model for the analysis of radon migration in fractured media.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Shengyang, et al. \"Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media.\" *Computers and Geotechnics*, vol. 128, 2020, 103810. *ScienceDirect*, doi:10.1016/j.compgeo.2020.103810. Accessed 12 Feb. 2026."
indexed_texts: "10"
indexed_chars: "46766"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46926"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003421"
coverage_status: "full-index"
source_signature: "b0c55939241807f578306ece4d302309cae72b0b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:48:08"
---

# Fractal Discrete Fracture Network Model for the Analysis of Radon Migration in Fractured Media.

## One-line Summary

提出一种结合分形理论与离散裂隙网络（DFN）模型的新方法，用于模拟裂隙介质中氡气迁移，计算氡扩散系数与析出率，并通过露头验证与实验装置证实了模型的可靠性与鲁棒性。

## Research Question

如何考虑复杂裂隙结构，建立非传统模型以分析氡在裂隙介质中的迁移，突破传统基于均匀各向同性假设的数学模型带来的限制。具体包括：能否将分形理论融入DFN模型，有效描述裂隙几何统计特征，并用于预测氡迁移行为及代表性单元体（REV）的存在性。

## Study Area / Data

- **验证露头**：瑞典Forsmark场地AFM000053，面积645.5 m²，裂隙986条，\( D_f = 1.91 \), \( a = 2.5 \), \( \alpha = 1.85 \)，裂隙方位参数见表1[Feng 2020, pp. 3-4, 4‑5]。
- **案例露头**：中国衡阳大浦废弃铀矿附近露头，宽25 m，高19 m，提取裂隙145条，得到 \( D_f = 1.62 \), \( a = 2.39 \), \( \alpha = 1.49 \), 平均方位角 \( \mu_0 = 86.4^\circ \), Fisher常数 \( \kappa = 5.24 \)[Feng 2020, pp. 5-7, 7‑9]。
- **实验验证用DFN**：由铀尾矿、水泥与水固化制成，尺寸0.5 m × 0.5 m，内部预设裂隙结构，参数 \( D_f = 1.5 \), \( a = 3.5 \), \( \alpha = 1.85 \), \( \mu_0 = 45^\circ \), \( \kappa = 1 \)。氡源浓度139102 Bq/m³，低浓度8096 Bq/m³，介质产氡率0.12 Bq/m³/s[Feng 2020, pp. 4-5]。

## Methods

- **分形DFN生成**：采用一阶模型（Davy et al., 1990）描述裂隙中心与长度分布；二维时裂隙数量 \( n(l, L) \mathrm{d}l = \alpha L^{D_f} l^{-a} \mathrm{d}l \)；三维时修正为 \( D_f' = D_f+1 \), \( a' = a+1 \) 及相应尺度关系（Piggott, 1997；Kim and Schechter, 2009）。裂隙中心分布通过乘法级联过程（multiplicative cascade process）模拟，迭代地将域划分为 \( m=4 \)（2D）或 \( m=8 \)（3D）子域，满足 \( \sum P_i = 1 \) 及 \( \sum P_i^2 = (1/l_{\text{ratio}})^{D_f} \)[Feng 2020, pp. 1-1, 1‑2, 2‑3]。
- **裂隙方位**：采用von Mises‑Fisher分布，概率密度 \( f(\theta|\mu_0, \kappa) = \frac{e^{\kappa \cos(\theta-\mu_0)}}{2\pi I_0(\kappa)} \)，其中 \( \kappa = N_t/|r_n| \)。三维时利用Villaescusa方法生成倾向和倾角[Feng 2020, pp. 2-3, 3‑4]。
- **裂隙开度**：用Olson（2003）提出的开度‑长度相关法 \( d = 4f l^{0.5} \), \( f = \sqrt{\frac{K_{IC}(1-\nu^2)}{E}} \cdot \frac{K_{IC}}{8} \)，式中取 \( f = 7.0 \times 10^{-4} \)[Feng 2020, pp. 2-3]。三维裂隙形状为椭圆，并用“管道模型”近似替代椭圆裂隙进行流动与传输计算[Feng 2020, pp. 3-4]。
- **氡迁移模型**：稳态下单一裂隙内的氡浓度解析解为 \( c(x) = \frac{(c_0 - \frac{q}{\lambda}) e^{\beta_+ x} (e^{\beta_- L} - e^{\beta_- x}) + (c_L - \frac{q}{\lambda}) e^{\beta_- (L-x)} (e^{\beta_+ x} - e^{\beta_+ L})}{e^{\beta_- L} - e^{\beta_+ L}} \)，其中 \( \beta_{\pm} = \frac{v \pm \sqrt{v^2+4\lambda D}}{2D} \)。裂隙网络的节点通量平衡方程 \( \sum_{j} J_{ij}(c_i, c_j, q) = 0 \)，写成矩阵 \( Ax = b \)，利用稀疏矩阵算法求解。重复生成300次DFN实现以获得平均氡析出率 \( \bar{J_b} \) 和有效扩散系数 \( D_{\text{eff}} \)[Feng 2020, pp. 3-4, 4‑5]。开发了软件FDFNRn用于二维和三维分析[Feng 2020, pp. 4-5]。
- **REV确定**：以不同模型尺寸计算有效氡析出率的变异系数（Coefficient of Variation, CV），取CV = 5%为基准确定REV尺寸[Feng 2020, pp. 7-9]。

## Key Findings

1. **模型描述能力**：通过瑞典Forsmark露头验证，生成的DFN在裂隙中心对相关函数和长度分布趋势上与实测数据一致，能反映复杂裂隙的统计信息[Feng 2020, pp. 3-4, 4‑5]。
2. **实验验证**：自制实验装置测得的氡析出率为 \( 0.046 \pm 0.003 \) Bq/m²/s，理论计算值为0.049 Bq/m²/s，相对误差6.5%，验证了模型的有效性与准确性[Feng 2020, pp. 4-5]。
3. **案例应用**：对大浦露头生成含2163条裂隙的2D DFN，计算氡析出率为 \( (2.92 \pm 0.19) \times 10^{-3} \) Bq/m²/s，与实测 \( (4.53 \pm 0.62) \times 10^{-3} \) Bq/m²/s 处于同一数量级，表明模型可靠、稳健[Feng 2020, pp. 5-7, 7‑9]。3D DFN（15264条裂隙，域100 m × 100 m × 100 m）给出的析出率为 \( (2.11 \pm 0.18) \times 10^{-3} \) Bq/m²/s，略小于2D结果[Feng 2020, pp. 7-9]。
4. **代表性单元体（REV）**：不同长度指数 \( a \) 下，随模型尺寸增大，氡析出率变异系数减小，证实REV存在；REV尺寸随 \( a \) 增大而减小，遵循指数规律 \( L = 1.46 + 37511.46 \exp(-a/0.31) \)（\( R^2 = 0.9907 \)）[Feng 2020, pp. 7-9, 10‑11]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 生成的DFN与Forsmark露头的裂隙中心对相关函数一致 | [Feng 2020, pp. 3-4, Fig. 6] | 使用露头实测参数 \( D_f = 1.91, a = 2.5, \alpha = 1.85 \) | 验证了乘法级联过程模拟裂隙位置的有效性 |
| 生成DFN的长度分布趋势与露头吻合，但存在细节差异 | [Feng 2020, pp. 4-5, Fig. 7] | 一阶模型描述统计分布，不能反映所有细节 | 认为理论能反映给定尺度下的统计特征 |
| 实验DFN氡析出率实测 \( 0.046 \pm 0.003 \) Bq/m²/s，计算0.049 Bq/m²/s，相对误差6.5% | [Feng 2020, pp. 4-5] | 自制装置，参数 \( D_f = 1.5, a = 3.5, \alpha = 1.85, \mu_0=45^\circ, \kappa=1 \)，产氡率0.12 Bq/m³/s | 验证了模型对氡迁移预测的准确性 |
| 大浦露头案例：计算析出率 \( (2.92 \pm 0.19) \times 10^{-3} \) Bq/m²/s，实测 \( (4.53 \pm 0.62) \times 10^{-3} \) Bq/m²/s | [Feng 2020, pp. 5-7, 7‑9] | 二维DFN，2163条裂隙，\( D_f = 1.62, a = 2.39 \)，产氡率0.43 Bq/m³/s | 模型预测与实测同量级，验证可靠性 |
| 3D DFN预测大浦露头析出率 \( (2.11 \pm 0.18) \times 10^{-3} \) Bq/m²/s | [Feng 2020, pp. 7-9] | 三维参数由二维参数外推：\( D_f' = 2.62, a' = 3.39, \alpha' = 3.20 \)，倾向均值65°, κ=2 | 三维结果略低于二维，数据源于估算 |
| REV尺寸与长度指数 \( a \) 呈指数关系：\( L = 1.46 + 37511.46 \exp(-a/0.31) \) | [Feng 2020, pp. 7-9, Fig. 20] | 以变异系数5%为准则，\( a \) 取2.0, 2.2, 2.39, 2.6, 2.8 | \( a \) 增大，小裂隙增多，氡扩散短，更快达到REV |

## Limitations

所提模型未考虑微观结构（如微裂隙、微孔隙）对氡迁移的作用；三维裂隙方位参数部分基于估算而非严格的实测数据；天然裂隙的长度分布复杂，一阶模型无法描述所有细节[Feng 2020, pp. 4-5, 7‑9, 9‑10]。

## Assumptions / Conditions

- 裂隙介质中氡迁移为稳态，仅考虑扩散和达西对流，迁移方程基于均匀各向同性假设下的扩散-对流方程[Feng 2020, pp. 3-4]。
- 裂隙网络只考虑连通裂隙，孤立和“死端”裂隙不参与迁移[Feng 2020, pp. 3-4]。
- 裂隙内气体流速采用立方定律 \( v = \frac{9.8 \rho}{12\mu} \frac{d^2 H}{L} \)[Feng 2020, pp. 3-4]。
- 裂隙中心分布可用乘法级联过程生成，满足 \( \sum P_i = 1 \), \( \sum P_i^2 = (1/l_{\text{ratio}})^{D_f} \)，取二阶分形维数 \( D_2 = D_f \)[Feng 2020, pp. 1-2, 2‑3]。
- 裂隙长度服从一阶幂律分布 \( n(l, L) \mathrm{d}l = \alpha L^{D_f} l^{-a} \mathrm{d}l \)，三维模型通过维度提升和外推获得[Feng 2020, pp. 1-1, 1‑2]。
- 裂隙方位遵循von Mises‑Fisher分布，用露头统计得到的 \( \mu_0 \) 和 \( \kappa \) 描述[Feng 2020, pp. 2-3]。
- 裂隙开度与长度相关 \( d = 4 f l^{0.5} \)，比例系数 \( f = 7.0 \times 10^{-4} \) 视为常数[Feng 2020, pp. 2-3]。
- 每次模拟随机生成300次实现以获得稳定的平均结果[Feng 2020, pp. 4-5]。

## Key Variables / Parameters

- **分形参数**：二维分形维数 \( D_f \)、长度指数 \( a \)、正则化常数 \( \alpha \)；三维由二维推导 \( D_f' = D_f+1 \), \( a' = a+1 \), \( \alpha' = \alpha \frac{\Gamma(\frac{a'+2}{2})}{\Gamma(\frac{a+1}{2})} \)[Feng 2020, pp. 1-1, 1‑2, 5‑7]。
- **方位参数**：von Mises‑Fisher分布平均方位 \( \mu_0 \) 及集中参数 \( \kappa \)（2D）；三维需倾向、倾角及相应 \( \kappa \)[Feng 2020, pp. 2-3]。
- **裂隙几何**：长度 \( l \)，开度 \( d \)，比例系数 \( f \)（与断裂韧性 \( K_{IC} \)、杨氏模量 \( E \)、泊松比 \( \nu \) 相关）[Feng 2020, pp. 2-3]。
- **物理参数**：空气中氡扩散系数 \( D = 1.05 \times 10^{-5} \) m²/s，空气密度 \( \rho \)、动力粘度 \( \mu \)，氡衰变常数 \( \lambda \)，压力水头差 \( H \)[Feng 2020, pp. 3-4]。
- **边界与介质参数**：边界氡浓度 \( C_1, C_2 \)，介质产氡率 \( q \)，模型域尺寸 \( L \)[Feng 2020, pp. 5-7, 7‑9]。
- **输出量**：有效氡扩散系数 \( D_{\text{eff}} = J_{b\_diff}/\nabla c \)，氡析出率 \( J_b = \sum J_i S_i/S \)[Feng 2020, pp. 3-4]。

## Reusable Claims

- 将分形理论与DFN模型结合，可生成能反映天然裂隙统计特征（位置、长度、方位、开度）的二维和三维裂隙网络。[Feng 2020, pp. 1-1, 2‑3, 3‑4, 4‑5]
- 基于乘法级联过程的裂隙中心分布生成方法与实际露头的对相关函数一致，可用于模拟裂隙聚集性。[Feng 2020, pp. 3-4, 4‑5]
- 提出的氡迁移模型在实验DFN上验证，计算氡析出率与实测的相对误差约为6.5%。[Feng 2020, pp. 4-5]
- 模型应用于野外露头时，预测的氡析出率与实测值处于同一数量级，表明方法在天然条件下具有可靠性和鲁棒性。[Feng 2020, pp. 5-7, 7‑9]
- 在裂隙网络氡迁移模拟中存在代表性单元体（REV），其尺寸随长度指数 \( a \) 的增加而呈指数减小。[Feng 2020, pp. 7-9, 10‑11]

## Candidate Concepts

- [[Fractal Discrete Fracture Network]] (分形离散裂隙网络)
- [[Radon migration in fractured media]] (裂隙介质氡迁移)
- [[Representative Elementary Volume (REV)]] (代表性单元体)
- [[Multiplicative cascade process]] (乘法级联过程)
- [[von Mises-Fisher distribution]] (von Mises‑Fisher分布)
- [[First-order fracture length model]] (一阶裂隙长度模型)
- [[Pipe model for elliptical fractures]] (椭圆裂隙的管道模型)
- [[Fracture aperture-length correlation]] (裂隙开度‑长度相关性)

## Candidate Methods

- [[Fractal discrete fracture network generation using multiplicative cascade and first-order model]]
- [[Radon flux equilibrium solver for fracture networks via sparse matrix inversion]]
- [[REV size determination using coefficient of variation of radon exhalation rate]]
- [[Experimental validation of radon exhalation from synthetic DFN using RAD7 detector]]
- [[3D fracture network orientation generation by Villaescusa method]]

## Connections To Other Work

- 传统氡迁移模型基于均匀各向同性假设（Rogers and Nielson, 1991; Bates and Edwards, 1980; Mosley et al., 1997），本研究将其扩展到考虑分形裂隙网络。
- 离散裂隙网络（DFN）在渗流模拟中已广泛应用（Dong et al., 2018; Maillot et al., 2016），但此前未与氡迁移结合。
- 分形在裂隙描述中的优势曾被Velde et al. (1991)、Liu et al. (2015)、Miao et al. (2015)等证实，本研究沿用了分形维度与等效渗透率关联的思路。
- 裂隙网络生成借鉴了Davy et al. (1990)的一阶模型、Darcel et al. (2003)的级联过程、Olson (2003)的开度-长度关系等。
- REV的确定参考了Baghbanan and Jing (2007)及Min et al. (2004)使用变异系数的方法。

## Open Questions

- 如何将微裂隙和微孔隙对氡迁移的贡献纳入模型[Feng 2020, pp. 9-10]？
- 三维裂隙方位参数（倾向、κ）在实际应用中缺乏系统测量，如何从有限数据可靠推断？
- 模型对非稳态、多组分气体及温度梯度的适应性尚待研究。
- 指数规律 \( L \sim \exp(-a/0.31) \) 的普适性需在不同地质条件下检验。
- 三维DFN预测析出率略低于二维，其尺度效应和维度转换的物理机制值得深入探讨。

## Source Coverage

This article is fully indexed. All non‑empty source blocks (10 indexed fragments) were processed into the markdown page.  
Indexed texts: 10, indexed characters: 46,766, compiled characters: 46,926.  
Coverage ratio by blocks: 1.0, coverage ratio by chars: 1.003.  
Source signature: b0c55939241807f578306ece4d302309cae72b0b.
