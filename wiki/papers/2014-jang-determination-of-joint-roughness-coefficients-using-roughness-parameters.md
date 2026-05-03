---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
title: "Determination of Joint Roughness Coefficients Using Roughness Parameters."
status: "draft"
source_pdf: "data/papers/2014 - Determination of Joint Roughness Coefficients Using Roughness Parameters.pdf"
collections:
  - "粗糙裂隙渗流"
citation: "Jang, Hyun-Sic, et al. \"Determination of Joint Roughness Coefficients Using Roughness Parameters.\" *Rock Mechanics and Rock Engineering*, vol. 47, no. 6, 2014, pp. 2061-2073. doi:10.1007/s00603-013-0535-z."
indexed_texts: "9"
indexed_chars: "42558"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42750"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004511"
coverage_status: "full-index"
source_signature: "1e236696a735d9ab9dd1dfef881af196a795f788"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:21:24"
---

# Determination of Joint Roughness Coefficients Using Roughness Parameters.

## One-line Summary

本研究对标准粗糙度廓线进行精密数字化，采用幂律方程建立节理粗糙度系数（JRC）与各类粗糙度参数（统计参数、二维不连续粗糙度参数、分形维数）的关系；发现所有关系对第4条廓线（JRC 6–8）的偏差均超过±5%，并证实分形维数应在整个分规范围内测定，粗糙度参数与采样间隔不独立[Jang 2014, pp. 1-2, 12-13]。

## Research Question

如何利用高精度数字化的10条标准粗糙度廓线，通过统计参数（Z₂、SF、Rₚ）、二维不连续粗糙度参数（θ*max/(C+1)2D）以及分形维数（D）和归一化截距（an）精确确定JRC？同时评估采样间隔和分规范围选取对参数与JRC关系的影响。

## Study Area / Data

- **数据来源**：Barton与Choubey (1977)基于136次岩石节理直剪试验定义的10条标准粗糙度廓线[Jang 2014, pp. 1-2, 2-3]。
- **JRC范围**：每条廓线分配了JRC范围（0–2至18–20），括号内为反分析精确值[Jang 2014, pp. 2-3]，如第4条廓线（花岗岩）JRC 6–8（精确值6.7）。
- **数字化处理**：廓线以1200 dpi扫描转换为位图，使用Origin软件以0.1 mm采样间隔数字化，并额外生成0.5、1.0、2.0 mm间隔的三组廓线[Jang 2014, pp. 2-3]。
- **廓线尺寸**：大多数廓线水平长度约99.0 mm；第7条最短（96.0 mm），第8条最长（101.0 mm）[Jang 2014, pp. 2-3]。
- **特殊廓线**：第4条（JRC 6–8）在各种关系中普遍偏离±5%范围，统计特性异于其他廓线[Jang 2014, pp. 1-2]。

## Methods

1. **统计参数计算**  
   按公式(1)–(3)计算Z₂（均方根一阶导数）、SF（结构函数）和Rₚ（粗糙度廓线指数）[Jang 2014, pp. 3-5]。
2. **二维粗糙度参数**  
   基于Tatone与Grasselli (2010)方法，从正向和反向方向测定标准廓线的平均θ*max/(C+1)2D值[Jang 2014, pp. 7-8]。
3. **分形分析（分割器法）**  
   利用分割器法计算分形维数D（通过logL(r)–log r斜率）和归一化截距an（即截距除以廓线长度）[Jang 2014, pp. 8-10]。  
   分两种回归范围：  
   - 整个分规范围  
   - “合适范围”（suitable range，排除端点平坦段），对比相关性[Jang 2014, pp. 8-10]。
4. **幂律方程建模**  
   采用统一形式 JRC = aP^b + c（P为粗糙度参数）拟合各参数与JRC的关系[Jang 2014, pp. 5-7]。
5. **采样间隔影响评估**  
   分别在0.1、0.5、1.0、2.0 mm四种采样间隔下计算所有粗糙度参数，比较关系式的变化及估算误差[Jang 2014, pp. 10-12]。
6. **与前人公式对比**  
   将本研究建立的JRC与参数关系与Tse & Cruden (1979)、Maerz et al. (1990)、Yu & Vayssade (1991)、Tatone & Grasselli (2010)等文献公式进行比较[Jang 2014, pp. 3-8, 12-13]。

## Key Findings

- **高相关性但第4廓线异常**：所有统计参数（Z₂, SF, Rₚ-1）与JRC的幂律关系R²均超过0.96（如Z₂关系式R²=0.972，SF关系式R²=0.972，Rₚ-1关系式R²=0.973），但第4条廓线（JRC 6–8）偏差均超过±5%[Jang 2014, pp. 1-2, 3-7]。该廓线统计特性轻微异于其他廓线，反映出标准廓线的不一致性[Jang 2014, pp. 12-13]。
- **2D粗糙度参数**：θ*max/(C+1)2D与JRC关系式（17）R²=0.978，第4条廓线同样偏离±5%边界；本研究与Tatone & Grasselli (2010)的结果几乎一致，说明双方数字化均精确[Jang 2014, pp. 7-8, 12-13]。
- **分形维数测定范围**：采用整个分规范围回归的D与JRC相关性高（R²=0.990），而仅使用“合适范围”的R²降至0.852，且第4–8廓线的D显著偏离最佳拟合曲线。因此，分形维数应使用整个分规范围估算，与Kulatilake et al. (1997)的建议相反[Jang 2014, pp. 8-10]。
- **归一化截距**：an与JRC亦高度相关，且无论采用整个范围还是合适范围回归，相关系数均较高；提供新幂律关系式（26）[Jang 2014, pp. 10]。
- **采样间隔依赖性**：Z₂、Rₚ-1、θ*max/(C+1)2D和D随采样间隔增大而减小，但SF随采样间隔增大而迅速增大（0.1 mm时SF接近零）。粗糙度参数与采样间隔不独立，不同间隔下JRC关系式不同，若误用关系式将导致JRC估算误差，差异可达2.67–4.72（以0.1 mm Z₂值代入2.0 mm关系式为例）[Jang 2014, pp. 1-2, 10-12]。
- **与前人公式对比**：Tse & Cruden (1979)和Maerz et al. (1990)的公式误差较大，可能因早期数字化精度不足；Yu & Vayssade (1991)和Tatone & Grasselli (2010)的关系式估算值大多落在±5%范围内，与本研究相近[Jang 2014, pp. 12-13]。
- **幂律方程普适性**：各种参数与JRC的关系均可用同一幂律形式描述，不同参数的回归系数列于表2[Jang 2014, pp. 5-7, 10-12]。

## Core Evidence Table

| 证据 | 来源 | 条件 / 背景 | 备注 |
| --- | --- | --- | --- |
| 第4廓线在所有粗糙度参数关系中偏差超过±5% | [Jang 2014, pp. 1-2, 3-5, 5-7, 7-8] | 10条标准廓线，0.5 mm采样间隔 (部分讨论中涵盖其他间隔) | 反映该廓线统计差异 |
| Z₂与JRC幂律关系 R²=0.972，式(7) | [Jang 2014, pp. 3-5] | SI=0.5 mm | 除第4廓线外JRC均在±5%内 |
| SF与JRC幂律关系 R²=0.972，式(10) | [Jang 2014, pp. 5] | SI=0.5 mm | 同样第4廓线偏离 |
| Rp-1与JRC幂律关系 R²=0.973，式(14) | [Jang 2014, pp. 5-7] | SI=0.5 mm | 第4廓线偏离 |
| θ*max/(C+1)2D与JRC关系 R²=0.978，式(17) | [Jang 2014, pp. 7-8] | SI=0.5 mm | 第4廓线偏离±5% |
| 全范围分形维数D与JRC R²=0.990，式(25) | [Jang 2014, pp. 8-10] | 分割器法，整个分规范围 | 优于“合适范围” (R²=0.852) |
| 归一化截距an与JRC关系式(26) | [Jang 2014, pp. 10] | 合适范围回归 | 任意范围均高相关 |
| 采样间隔影响：Z2等随间隔增大而减小，SF随间隔剧增 | [Jang 2014, pp. 10-12] | 四种SI (0.1~2.0 mm) | 误用关系式导致JRC偏差2.67-4.72 |
| Yu & Vayssade (1991)和Tatone & Grasselli (2010)公式的JRC估算值基本在±5%内 | [Jang 2014, pp. 12-13] | 0.5 mm SI | 数字化精度验证 |

## Limitations

- 所有基于标准廓线建立的关系均对第4条廓线（JRC 6–8）存在系统性偏差，无法通过单一全局关系完全消除[Jang 2014, pp. 1-2, 12-13]。
- 分形维数若仅采用“合适范围”估算，与JRC的相关性显著降低（R²从0.990降至0.852），不宜用于JRC估算[Jang 2014, pp. 8-10]。
- 粗糙度参数均受采样间隔影响，SF参数在细间隔下对微小数字化误差极为敏感，导致JRC估算不稳定[Jang 2014, pp. 10-12]。
- 本文结论仅基于10条标准廓线，未包括三维实际节理面及不同岩性的更大样本[Jang 2014, pp. 2-3, 12-13]。

## Assumptions / Conditions

- 以Barton与Choubey (1977)确定的10条标准廓线及其反分析JRC值为基准，假设这些基准值是正确的[Jang 2014, pp. 2-3]。
- 数字化采用1200 dpi扫描和0.1 mm最小采样间隔，假定能够精确捕获廓线特征[Jang 2014, pp. 2-3]。
- JRC与各粗糙度参数的关系遵循幂律方程 JRC = aP^b + c，该形式能涵盖此前文献中的对数、线性、平方根等关系[Jang 2014, pp. 5-7]。
- 分割器法假设粗糙度廓线具备自仿射特性；二维粗糙度参数假设剪切过程中仅在正方位倾角的区域发生接触[Jang 2014, pp. 7-10]。

## Key Variables / Parameters

- **JRC**：节理粗糙度系数（无量纲）
- **Z₂**：均方根一阶导数（mm⁻¹）
- **SF**：结构函数（mm）
- **Rₚ**：粗糙度廓线指数，常用Rₚ-1（无量纲）
- **θ*max/(C+1)2D**：二维不连续粗糙度参数（无量纲）
- **D**：分形维数（介于1和2之间）
- **an**：归一化截距（dimensionless，从log L(r)–log r图的截距除以水平长度）
- **SI**：采样间隔（mm）
- **r**：分规值（divider value，mm）

## Reusable Claims

- 在0.5 mm采样间隔下，JRC可通过幂律关系从Z₂准确估算（JRC = 51.16·Z₂^0.531 – 11.44），适用于除类似第4条廓线的多数情况；需注意该关系对第4廓线的偏差超过±5%[Jang 2014, pp. 3-5]。
- 分形维数D应在分割器法的整个分规范围内回归，而非仅用“合适范围”，以获得与JRC更高的相关性（R²=0.990）；此结论与Kulatilake et al. (1997)相反[Jang 2014, pp. 8-10]。
- 无论采用何种回归范围，归一化截距an均与JRC显著相关，可作为一种替代分形参数用于JRC评估[Jang 2014, pp. 10]。
- 粗糙度参数（Z₂, SF, Rₚ, θ*max/(C+1)2D, D）均依赖于采样间隔，因此用于估算JRC的关系式必须与对应的采样间隔匹配，否则将导致系统性误差[Jang 2014, pp. 10-12]。
- SF对采样间隔极为敏感，在较细间隔（如0.1 mm）下接近零，易产生较大JRC估算波动；相比之下，分形维数D受采样间隔影响更小[Jang 2014, pp. 1-2, 10-12]。

## Candidate Concepts

- [[Joint Roughness Coefficient (JRC)]]
- [[Standard Roughness Profiles]]
- [[Barton–Choubey 1977 profiles]]
- [[2D Discontinuity Roughness Parameter]]
- [[Self-affine roughness]]
- [[Divider method for fractal dimension]]
- [[Suitable range (fractal analysis)]]
- [[Normalized intercept an]]
- [[Sampling interval dependency]]
- [[Power law JRC relationship]]

## Candidate Methods

- [[Statistical roughness parameter calculation (Z2, SF, Rp)]]
- [[2D roughness parameter from contact inclination analysis]]
- [[Fractal dimension estimation by whole-range divider method]]
- [[Power law equation fitting for JRC]]
- [[Multi-sampling-interval digitization strategy]]
- [[Precision digitization of standard profiles at 1200 dpi]]

## Connections To Other Work

- 与Barton & Choubey (1977)定义的标准粗糙度廓线直接关联，JRC基准值取自该文献[Jang 2014, pp. 1-3]。
- 统计参数关系与Tse & Cruden (1979)、Yu & Vayssade (1991)、Tatone & Grasselli (2010)等对比，指出早期数字化可能的精度问题[Jang 2014, pp. 3-7, 12-13]。
- 二维粗糙度参数方法继承自Grasselli & Egger (2003)的三维参数概念，并直接比较了 Tatone & Grasselli (2010)的公式[Jang 2014, pp. 7-8]。
- 分形维数测定范围选择与Kulatilake et al. (1997)提出的“合适范围”观点相左，本文主张全范围回归更优[Jang 2014, pp. 8-10]。
- 采样间隔对粗糙度参数的影响与Miller et al. (1990)、Yu & Vayssade (1991)、Chun & Kim (2001)等的发现一致[Jang 2014, pp. 10-12]。

## Open Questions

- 第4条标准廓线为何在统计特性上异于其他廓线，是否反映了Rock Joint的某些未被表征的物理属性？[Jang 2014, pp. 1-2, 12-13]
- 使用全部分规范围估算的D与JRC相关性更高，其背后的物理机制是什么？是否因“合适范围”丢失了长波或短波信息？[Jang 2014, pp. 8-10]
- 如何建立与采样间隔无关的粗糙度表征方法，或标准化的采样间隔推荐值？[Jang 2014, pp. 10-12]
- 二维粗糙度参数和分形参数在三维真实节理面上的适用性及与剪切强度的直接关联仍有待验证[Jang 2014, pp. 7-8, 12-13]。

## Source Coverage

本文采用全部9个经索引的文本片段（共42558个字符，非空源块9个），所有片段均已被处理并纳入页面内容。编译后页面总字符数约42750，覆盖比（按源块计）1.0，按字符计约1.004511，达到完全覆盖（full-index）。源文件特征码：1e236696a735d9ab9dd1dfef881af196a795f788。所有声明均直接来自提供的索引片段，未添加外部信息。
