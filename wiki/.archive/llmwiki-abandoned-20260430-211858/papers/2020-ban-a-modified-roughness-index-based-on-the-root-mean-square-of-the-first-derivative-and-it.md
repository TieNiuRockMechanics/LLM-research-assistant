---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-ban-a-modified-roughness-index-based-on-the-root-mean-square-of-the-first-derivative-and-it"
title: "A Modified Roughness Index Based on the Root Mean Square of the First Derivative and Its Relationship with Peak Shear Strength of Rock Joints."
status: "draft"
source_pdf: "data/papers/2020 - A modified roughness index based on the root mean square of the first derivative and its relationship with peak shear strength of rock joints.pdf"
collections:
  - "zotero new"
citation: "Ban, Liren, et al. \"A Modified Roughness Index Based on the Root Mean Square of the First Derivative and Its Relationship with Peak Shear Strength of Rock Joints.\" *Engineering Geology*, vol. 279, 2020, p. 105898."
indexed_texts: "13"
indexed_chars: "61911"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:02:05"
---

# A Modified Roughness Index Based on the Root Mean Square of the First Derivative and Its Relationship with Peak Shear Strength of Rock Joints.

## One-line Summary
基于一阶导数均方根（\(Z_2\)）提出考虑正坡角凸体贡献与剪切方向的改进粗糙度指标 \((Z_2)_{ds}\)，并通过60个节理的直剪试验建立其与峰值剪切强度（PSS）的线性关系，该关系可消除采样间距影响。[Ban 2020, pp. 1-1]

## Research Question
如何改进传统 \(Z_2\) 粗糙度指标，使其能够反映剪切方向对节理峰值剪切强度的贡献，并建立更合理的粗糙度‑强度经验关系？

## Study Area / Data
- **人工节理**：通过花岗岩巴西劈裂获得5种形貌表面（J‑1~J‑5），再以3D打印模具浇筑水泥砂浆制成人工节理，共计60个试件。[Ban 2020, pp. 2-3, pp. 3-4]
- **天然节理**：将J‑1形貌雕刻于湖北鄂州红砂岩（细砂结构，主要矿物为长石、石英）上，制备12个天然节理试件，用于模型验证。[Ban 2020, pp. 3-4]
- **直剪条件**：人工节理在多种法向应力下进行；天然节理施加法向应力0.5, 1, 1.5, 2, 2.5, 3 MPa，总剪切位移10 mm。[Ban 2020, pp. 4-5]

## Methods
1. **形貌获取**：采用3D激光扫描仪（LK‑G500系列，采样间隔0.25 mm）获取节理表面点云，并利用双线性插值获取任意方向的轮廓数据。[Ban 2020, pp. 2-3, pp. 5-7]
2. **指标构建**：基于 \(Z_2\) 只考虑正坡角凸体对剪切强度的贡献，提出 \((Z_2)_d\)（式5）并发展为含方向性的投影指标 \((Z_2)_{ds}\)（式9），计算特定剪切方向下平行轮廓的均值。[Ban 2020, pp. 5-5, pp. 5-7]
3. **力学试验**：对人工和天然节理进行直剪试验，记录峰值剪切强度并分析磨损区位置。[Ban 2020, pp. 4-5, pp. 7-8]
4. **关系建立**：定义 \(q = \tau_p / \sigma_n\)，分析 \(q\) 与 \((Z_2)_{ds}\) 的线性关系，并结合Patton模型与材料抗拉强度提出PSS预测公式。[Ban 2020, pp. 7-8]

## Key Findings
- \((Z_2)_{ds}\) 能够显著反映节理粗糙度的各向异性，不同剪切方向的粗糙度值可相差数倍（如J‑1在300°–345°约为0.04，120°–180°可达0.13）。[Ban 2020, pp. 5-7]
- PSS与法向应力、表面形貌以及剪切方向均相关；法向应力增大导致更多凸体相互作用，PSS上升。[Ban 2020, pp. 4-5]
- 剪切试验后的节理磨损位置与等效倾角大且破坏模式为非剪胀的区域高度一致，验证了 \((Z_2)_{ds}\) 力学含义的合理性。[Ban 2020, pp. 7-8]
- \(q\) 与 \((Z_2)_{ds}\) 呈清晰线性关系，据此可建立不受采样间隔影响的新PSS关系。[Ban 2020, pp. 1-1, pp. 7-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| \(q\)（\(\tau_p/\sigma_n\)）与 \((Z_2)_{ds}\) 呈线性关系 | [Ban 2020, pp. 7-8] | 人工节理（1 mm增量连续凸体等效），直剪正向 | 线性关系式具体形式未在片段中给出 |
| PSS 随法向应力、表面形貌和剪切方向变化 | [Ban 2020, pp. 4-5] | 60个节理直剪试验；人工节理两组重复性高 | 天然节理试验用于验证模型适用性 |
| \((Z_2)_{ds}\) 在0°–360°方向具有显著各向异性 | [Ban 2020, pp. 5-7] | 1 mm采样间隔，15°方向间隔，J‑1~J‑5表面 | 不同方向的最大与最小粗糙度差异明显 |
| 节理磨损区与等效倾角大、非剪胀破坏区域一致 | [Ban 2020, pp. 7-8] | 正向剪切方向，对比剪切后表面与等效倾角分布 | 非剪胀区在图上用圆圈标出，与磨损位置吻合 |
| \((Z_2)_d\) 仅累加正坡角凸体的高差平方 | [Ban 2020, pp. 5-5] | 采用 \(\max[(y_{i+1}-y_i), 0]\)，表征抵抗剪切的凸体 | 若线性关系成立，则 \((Z_2)_d\) 可代表凸体贡献 |
| 人工节理内摩擦角35°，基本摩擦角32°；天然红砂岩抗压强度54 MPa，基本摩擦角28° | [Ban 2020, pp. 3-4, pp. 4-5] | 材料基础参数 | 用于建立PSS模型 |
| 3D打印人工节理试件具有良好均匀性和重复性 | [Ban 2020, pp. 4-5] | 两组相同条件下PSS值非常接近 | 确保了试验数据的可靠性 |

## Limitations
- 未从索引片段中确认模型在高法向应力（>3 MPa）或大尺寸节理下的适用性。
- 提出的线性关系仅基于1 mm采样的等效连续凸体假设，片段中未解释如何从机理上消除采样间距影响。
- 仅对五种花岗岩劈裂形貌和一种红砂岩雕刻形貌进行验证，表面类型的覆盖度有限。
- 片段未提供完整的预测模型数学表达式及统计分析（如相关系数），其外推能力待确认。
- 方向性的评估采用15°间隔，可能遗漏更精细的各向异性特征。

## Assumptions / Conditions
- 仅正向坡角（迎着剪切方向）的凸体提供抗剪贡献，且其贡献与高差 \(\max[(y_{i+1}-y_i), 0]\) 存在线性关系。[Ban 2020, pp. 5-5]
- 节理壁的抗拉强度与圆柱体试样一致，且凸体破坏以拉伸为主。[片段引用Ghazvinian et al., 2012]
- 非剪胀破坏模式由几何参数 \(f = h/l\) 控制，存在临界值 \(f_c\)。[Ban 2020, pp. 5-5]
- 等效连续凸体以1 mm间距替代真实形貌，且认为该间距已能合理反映粗糙度在计算 \((Z_2)_{ds}\) 时的特征。[Ban 2020, pp. 7-8]
- 直剪试验的侧向边界条件未在片段中详述，假定为无侧限常规直剪。

## Key Variables / Parameters
- \((Z_2)_{ds}\)：改进的考虑方向性的粗糙度指标
- \(Z_2\)：原始一阶导数均方根粗糙度
- \((Z_2)_d\)：只计入正坡角的中间指标
- \(\tau_p\)：峰值剪切强度（PSS）
- \(\sigma_n\)：法向应力
- \(q = \tau_p / \sigma_n\)：归一化强度比
- \(\theta\)：剪切方向（0°~360°）
- \(i_p\)：峰值剪胀角
- \(\phi_b\)：基本摩擦角
- \(f_c\)：凸体几何临界高长比
- \(\Delta x\)：采样间隔（本研究中为1 mm或0.25 mm）

## Reusable Claims
- **Claim 1**: 岩石节理粗糙度指标若只考虑正坡角凸体（即迎着剪切方向的高差分量），能更好地反映其力学贡献，因为背向凸体不参与抗剪。[Ban 2020, pp. 5-5]  
  *Conditions*: 适合于带有方向性的剪切过程，凸体高度差与抗剪贡献近似线性关系。  
  *Limitations*: 若凸体存在非线性贡献（如复杂互锁），该线性假设可能不足。
- **Claim 2**: 节理粗糙度具有显著各向异性，使用方向性指标 \((Z_2)_{ds}\) 可量化为随剪切方向变化的数值，其极值可相差数倍；因此工程评价必须指定剪切方向。[Ban 2020, pp. 5-7]  
  *Conditions*: 基于3D扫描后双线性插值计算各方向轮廓；采样间隔和方向间隔会影响分辨率。
- **Claim 3**: 剪切后节理表面的磨损位置与等效倾角大且破坏模式为非剪胀区的区域高度一致，表明等效倾角可作为判断磨损的几何指标。[Ban 2020, pp. 7-8]  
  *Conditions*: 正向剪切，人工花岗岩‑水泥砂浆节理；未确认在天然节理中的推广。
- **Claim 4**: 在试验法向应力范围内（0.5~3 MPa），归一化强度比 \(q\) 与 \((Z_2)_{ds}\) 呈线性关系，该关系可避免采样间隔对粗糙度评价的干扰。[Ban 2020, pp. 1-1, pp. 7-8]  
  *Conditions*: 适用于1 mm采样间隔构建的等效连续凸体；需要进一步验证不同采样间隔下的有效性。

## Candidate Concepts
- [[Peak Shear Strength (PSS)]]
- [[Roughness Index \(Z_2\)]]
- [[Derivative Root Mean Square]]
- [[Anisotropy of Joint Roughness]]
- [[Shear Directionality]]
- [[Equivalent Dip Angle]]
- [[Dilative and Non-dilative Failure]]
- [[3D Laser Scanning of Rock Joints]]
- [[Brazilian Tensile Fracture]]
- [[Engraved Rock Joints]]
- [[Patton’s Dilatancy Model]]
- [[Basic Friction Angle]]

## Candidate Methods
- [[Root Mean Square of the First Derivative (\(Z_2\))]]
- [[Bilinear Interpolation for Roughness Profile]]
- [[Grasselli’s 3D Apparent Dip Distribution]]
- [[Triangular Element Based 3D Roughness Analysis]]
- [[3D Printing for Artificial Joint Replication]]
- [[Multiple Fractal Dimensions for Joint Roughness]]
- [[Direct Shear Test of Rock Joints]]

## Connections To Other Work
- 在粗糙度量化方面，本文从 Belem et al. (2000) 的表面多参数描述和 Homand et al. (2001) 的3D \(Z_2\) 发展而来，但首次在 \(Z_2\) 框架中引入方向性和正坡角机械贡献。[Ban 2020, pp. 1-2]
- 文中借鉴了 Grasselli et al. (2002) 关于只有正倾角凸体贡献强度的观点，但将其简化为轮廓一阶导数形式，而非三角网格上的视倾角分析。[Ban 2020, pp. 5-5]
- 力学解释上引用了 Kwon et al. (2010) 的长方体凸体剪胀/非剪胀破坏模式，以及 Ghazvinian et al. (2012) 关于拉伸破坏控制的思想，从而将抗拉强度纳入关系推导。[Ban 2020, pp. 5-5, pp. 7-8]
- PSS模型基于 Patton (1966) 的峰值摩擦角与剪胀角表达式，并参考 Xia et al. (2014) 的剪胀角‑法向应力反比关系。据此建立用于人工与天然节理的统一线性形式。[Ban 2020, pp. 7-8]
- 3D打印和雕刻工艺参照 Jiang et al. (2020) 及 Jiang et al. (2016a, b) 的验证，确保了试件重复性。[Ban 2020, pp. 4-5]

## Open Questions
- 文中提出的 \((Z_2)_{ds}\) 与PSS的线性关系是否适用于极高法向应力或不同尺度？能否从理论上证明消除采样间距影响的一般性条件？未从索引片段中确认。
- 该指标如何与基于面积的三维粗糙度参数（如 Grasselli 参数）进行系统性对比，尤其是对复杂三维互锁形貌的预测能力，片段中未展开。
- 对于反向剪切或循环剪切条件下的粗糙度退化，\((Z_2)_{ds}\) 的演化规律尚不明确。

## Source Coverage
本页综合使用了索引的13个片段，涵盖了摘要、引言部分文献综述、人工/天然节理制备、改进粗糙度指标定义、剪切试验结果、磨损区分布及线性关系建立的要点。然而，片段缺失完整的公式推导（如式9至式10之间的详细过程）、表1的具体试验数据、图5的拟合方程参数、对采样间隔影响的定量消解说明以及讨论/结论部分。因此，关于模型精度、普适性验证细节和讨论中的深层机理尚无法完整呈现。
