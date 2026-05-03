---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering"
title: "Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering."
status: "draft"
source_pdf: "data/papers/2010 - Lacunarity analysis of fracture networks Evidence for scale-dependent clustering.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Roy, Ankur, et al. “Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering.” *Journal of Structural Geology*, 2010."
indexed_texts: "7"
indexed_chars: "31389"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31527"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004396"
coverage_status: "full-index"
source_signature: "1846db79c3c5ca28eb104b23edba86e4d3b5bab8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:04:55"
---

# Lacunarity Analysis of Fracture Networks: Evidence for Scale-Dependent Clustering.

## One-line Summary
通过标准化缺项性（normalized lacunarity）分析量化裂隙网络的尺度依赖性聚类，发现挪威Hornelen盆地裂隙在小尺度上聚类更强，归因于从层控（stratabound）到非层控（non-stratabound）系统几何的过渡。

## Research Question
如何准确量化二维裂隙网络中裂隙分布的空间聚类程度，特别是在不同尺度下裂隙丰度差异显著时？裂隙聚类是否随观测尺度变化而呈现系统性地改变？[Roy 2010, pp. 1-1][Roy 2010, pp. 1-2][Roy 2010, pp. 2-4]

## Study Area / Data
- **Telpyn Point, 威尔士，英国**：一面积为247.6 m²区域内两组正交的充填脉状节理（走向200°的NS向和290°的EW向），发育于石炭纪砂岩中。NS组节理主要呈簇状分布，EW组为较大但稀疏的节理。原始裂隙图由Rohrbaugh et al. (2002) 提供，转换为545×578像素位图。[Roy 2010, pp. 2-4]
- **Hornelen盆地，挪威**：四幅由直升机在不同高度拍摄获得的嵌套裂隙图（Odling, 1997），面积分别为90 m×90 m（Map 4）、180 m×180 m（Map 5）、360 m×360 m（Map 6）和720 m×720 m（Map 7）。各图代表同一地区不同空间分辨率的裂隙系统子集，最短裂隙长度受限于图像分辨率，最长则受限于图幅。所有图均转换为1042×1042像素位图。[Roy 2010, pp. 4-4]

## Methods
- **滑动盒算法（Gliding-box algorithm）**：对位图化的裂隙图，以一定步长移动边长为r的方形盒（窗口），统计每个窗口内占据的像素数 s(r)，记录其均值 \(\bar{s}(r)\) 和方差 \(\sigma_s^2(r)\)。缺项性定义为 \(L(r) = \frac{Z_2(r)}{[Z_1(r)]^2} = \frac{\sigma_s^2(r)}{[\bar{s}(r)]^2} + 1\)，其中 \(Z_1(r)=\bar{s}(r), Z_2(r)=\sigma_s^2(r)+[\bar{s}(r)]^2\)。[Roy 2010, pp. 1-2][Roy 2010, pp. 2-4]
- **标准化缺项性（Normalized lacunarity）**：为消除裂隙丰度（即像素占据比例f）对缺项性的影响，提出新的标准化方法：\(L^*(r) = \frac{L(r)-L_{\min}}{L_{\max}-L_{\min}} = \frac{L(r)-1}{1/f - 1}\)，使数值在r=1时为1，r=r_t时为0，且完全去除丰度效应。与Plotnick et al. (1996)的对数归一化方法对比，新方法更有效地揭示了裂隙聚类特征。[Roy 2010, pp. 2-4][Roy 2010, pp. 4-4]
- **裂隙图数字化**：使用Matlab程序实现滑动盒算法，计算不同盒尺寸r下的 \(L^*\) 值，绘制 \(L^*(r)\)-r曲线（缺项性曲线）。[Roy 2010, pp. 2-4][Roy 2010, pp. 4-4]
- **统计分析**：对Hornelen盆地四幅图的 \(L^*(r)\) 值进行配对双尾t检验，评估尺度间差异显著性（95%置信水平）。[Roy 2010, pp. 4-4]

## Key Findings
- 在Telpyn Point裂隙网中，未标准化的缺项性曲线显示EW组（裂隙较少）的缺项性高于NS组（较密但更聚类），与目视判断相反。采用新标准化后，NS组（聚类更强）的 \(L^*\) 值显著高于EW组，正确反映了聚类差异。且两组同时绘制时，整体 \(L^*\) 曲线受NS组主导，表明最紧密的团聚控制了整个模式的缺项性特征。[Roy 2010, pp. 2-4][Roy 2010, pp. 4-4]
- 在Hornelen盆地，四幅图的标准化缺项性曲线存在统计显著差异。整体趋势为：图幅面积（或观测尺度）越小，\(L^*(r)\) 越大，即裂隙在小尺度上更为聚类。例如，Map 4（90 m×90 m）的 \(L^*\) 值大于Map 7（720 m×720 m）。[Roy 2010, pp. 4-4][Roy 2010, pp. 4-5]
- 该趋势解释为：在单个层理尺度（10米级），各岩层不构成明显力学单元，裂隙常穿越层理面，形成“非层控”（non-stratabound）系统，聚类明显。而在沉积旋回尺度（100-200 m），具不同岩性的旋回具有较高刚度差，可视为独立的力学单元，裂隙趋于“层控”（stratabound），间距规则。从Map 4到Map 7，随着可观察到的最大裂隙长度增加，旋回尺度的影响逐渐增强，裂隙系统由非层控向层控演化，导致缺项性递减。[Roy 2010, pp. 4-5][Roy 2010, pp. 5-6]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Telpyn Point地区NS组节理目视呈明显簇状，EW组稀疏且较不簇状。 | [Roy 2010, pp. 2-4] | 二维裂隙图，基于Rohrbaugh et al. (2002) | 用于验证新标准化方法的敏感性。 |
| 未标准化缺项性曲线显示EW组 > NS组，与新标准化后相反。 | [Roy 2010, pp. 2-4] | 对比图2a与图2c | Lmax = 1/f，低丰度导致夸大缺项性。 |
| 新标准化后NS组L*显著高于EW组；组合图L*接近NS组。 | [Roy 2010, pp. 2-4][Roy 2010, pp. 4-4] | Telpyn Point，f_NS约7倍f_EW | 支持标准化方法能完全消除丰度影响。 |
| Hornelen盆地四幅嵌套图的盒子维数Db无统计差异。 | [Roy 2010, pp. 4-4] | 表1，下界Db≈1.81–1.84 | 分形维度相近，但聚类特征不同，凸显缺项性分析的必要性。 |
| 配对t检验：Map4-5,5-6,6-7间L*值均存在显著差异（p<0.05）。 | [Roy 2010, pp. 4-4] | 四幅图各计算五个r值下的L* | 尺度越小L*越大，聚类越强。 |
| 航片显示Hornelen地区长裂隙（400–1500 m）间距规则（50–100 m）。 | [Roy 2010, pp. 4-5][Roy 2010, pp. 5-6] | 图5；沉积旋回厚度100–200 m | 支持大尺度趋向层控系统。 |

## Limitations
- 分析仅基于二维平面裂隙网络表征，未考虑三维裂隙连通性及方位变化的影响。[Roy 2010, pp. 1-2]
- Hornelen盆地数据源自直升机拍摄，虽为多尺度嵌套，但不同尺度下的最短裂隙检测受图像分辨率限制，可能引入部分尺度偏差。[Roy 2010, pp. 4-4]
- 缺项性曲线在超过一定盒尺后变化平缓，可能在r较大时区分度下降。[Roy 2010, pp. 2-4]

## Assumptions / Conditions
- 假定裂隙网络可合理通过二维像素图表示，且像素化过程保持裂隙分布特征不变。[Roy 2010, pp. 2-4]
- 在Hornelen盆地，沉积旋回顶部或底部的岩性接触面作为控制长裂隙终止的力学边界，而层理面在10米级尺度内不构成明显力学阻挡。[Roy 2010, pp. 4-5]
- 标准化缺项性计算中，Lmin = 1 对应盒尺寸覆盖整幅图时的极限值；Lmax = 1/f 对应盒尺寸为1像素时的极限值，该假设在所有模式中成立。[Roy 2010, pp. 2-4]

## Key Variables / Parameters
- **缺项性 L(r)**：原始尺度依赖的聚类度量。[Roy 2010, pp. 2-4]
- **标准化缺项性 L*(r)**：消除丰度影响后的缺项性，范围[0,1]，0为完全均匀，1为最大可能聚类（单像素水平）。[Roy 2010, pp. 2-4]
- **f**：裂隙像素占整个图像像素的比例，与裂隙密度相关。[Roy 2010, pp. 2-4]
- **盒尺寸 r**：滑动盒边长，通常在1到图幅全长之间取值。[Roy 2010, pp. 1-2]
- **裂隙长度分布范围**：Map 4 的裂隙长度模数为~1.7 m，范围0.15–52 m；Map 7 模数为~1.7 m，范围1.4–281 m。[Roy 2010, pp. 4-5]

## Reusable Claims
- 标准化缺项性 \(L^*(r)=\frac{L(r)-1}{1/f-1}\) 能够完全消除裂隙丰度对缺项性的影响，适用于不同密度裂隙网络的聚类对比。此方法优于Plotnick et al. (1996)的对数归一化方法。[Roy 2010, pp. 2-4][Roy 2010, pp. 4-4]
- 在裂隙丰度差异大的条件下，未标准化缺项性可能导致聚类排序错误，标准化是必要的。[Roy 2010, pp. 2-4]
- 裂隙网络的缺项性曲线可能由最紧密聚类的一组裂隙主导。[Roy 2010, pp. 4-4]
- 对于Hornelen盆地这类多尺度系统，裂隙聚类程度随尺度增大而减小，符合从床尺度的非层控系统向旋回尺度的层控系统过渡。该模式可推广到其他具有类似力学分层结构的沉积岩层序。[Roy 2010, pp. 4-5][Roy 2010, pp. 5-6]
- 裂隙网络的分形维度可能无法反映聚类差异，此时缺项性可作为补充的空间异质性度量。[Roy 2010, pp. 4-4]

## Candidate Concepts
- [[裂隙网络聚类]] (Fracture network clustering)
- [[缺项性]] (Lacunarity)
- [[层控与非层控裂隙]] (Stratabound vs. non-stratabound fractures)
- [[滑动盒算法]] (Gliding-box algorithm)
- [[尺度依赖性聚类]] (Scale-dependent clustering)
- [[力学单元]] (Mechanical unit)
- [[裂隙间距分布]] (Fracture spacing distribution)
- [[二维裂隙模式]] (Two-dimensional fracture pattern)
- [[标准化缺项性曲线]] (Normalized lacunarity curve)

## Candidate Methods
- [[滑动盒算法求缺项性]] (Gliding-box lacunarity computation)
- [[缺项性标准化公式]] (Normalized lacunarity formula: \(L^*=(L-1)/(1/f-1)\))
- [[配对t检验比较缺项性曲线]] (Paired t-test for lacunarity curve comparison)
- [[二维裂隙图转位图分析]] (Bitmap conversion of fracture maps for lacunarity)

## Connections To Other Work
- Plotnick et al. (1996) 提出缺项性分析作为空间模式的一般技术，并提出一种对数归一化方法，本文对其进行了改进。[Roy 2010, pp. 1-2][Roy 2010, pp. 2-4]
- Odling (1997) 与 Odling et al. (1999) 将Hornelen盆地裂隙系统界定为非层控系统，本文通过缺项性量化了其尺度依赖的演变。[Roy 2010, pp. 1-1][Roy 2010, pp. 4-5]
- Rohrbaugh et al. (2002) 提供了Telpyn Point裂隙图，本文以其为验证示例。[Roy 2010, pp. 2-4]
- Gillespie et al. (1999) 曾利用扫描线上裂隙间距的标准差与均值之比区分簇生与反簇生，本文提供了一种二维替代方法。[Roy 2010, pp. 1-2]
- 裂隙盒维数计算方面引用了Roy et al. (2007)的改进方法，但维数未能区分本例中的聚类变化。[Roy 2010, pp. 4-4]

## Open Questions
- 标准化缺项性与裂隙连通性之间的定量关系尚未阐明，对于流体流动和岩石强度预测很重要。[Roy 2010, pp. 5-6]
- 在更大的观测尺度（如地震反射数据覆盖范围）上，尺度依赖的聚类趋势是否依然成立？[Roy 2010, pp. 5-6]
- 其他沉积盆地或不同岩性组合中，缺项性-尺度关系的普适性有待验证。[Roy 2010, pp. 4-5]

## Source Coverage
全部7个非空索引片段均已处理，包含31527个字符的原始文献内容被完整编译。所有索引文本块（共7块，来源签名1846db79c3c5ca28eb104b23edba86e4d3b5bab8）均在本文中有所体现。源文本覆盖率（按块）：1.0；按字符：1.004396（因少量格式字符导致略超100%）。策略：单次编译，未进行迭代。
