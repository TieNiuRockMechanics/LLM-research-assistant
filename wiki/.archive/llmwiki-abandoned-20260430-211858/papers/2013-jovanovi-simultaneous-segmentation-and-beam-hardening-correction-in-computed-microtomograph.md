---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph"
title: "Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores."
status: "draft"
source_pdf: "data/papers/2013 - Simultaneous segmentation and beam-hardening correction in computed microtomography of rock cores.pdf"
collections:
citation: "Jovanović, Zoran, et al. “Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores.” *Computers & Geosciences*, 2013, doi:10.1016/j.cageo.2013.03.015."
indexed_texts: "9"
indexed_chars: "41922"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:44:33"
---

# Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores.

## One-line Summary
本文提出一种针对圆柱形岩石岩心的计算机显微断层扫描（μCT）后重建校正方法，利用射束硬化伪影（BHA）作为径向函数这一特性，在同一过程中实现物相分割与射束硬化校正 [Jovanovi 2013, pp. 1-1]。

## Research Question
如何在不预先知晓X射线光谱或多矿物地质样本衰减系数的前提下，解决多色X射线CT中因射束硬化伪影（BHA）导致的物相分割困难？[Jovanovi 2013, pp. 1-1]

## Study Area / Data
未从索引片段中确认具体研究区域的地理位置。实验数据来源于圆柱形岩石岩心样品的μCT扫描，包括铝圆柱和塑料圆柱体模，以及花岗岩真实岩心样本 [Jovanovi 2013, pp. 6-8]。

## Methods
- **基于BHA的径向函数特性分割**：观察到圆柱形样品中，单相的重建衰减值是距离圆柱中心距离的径向函数（射束硬化曲线）。通过提取该曲线、为每相构建仅含该相的“人工对象”、计算人工对象与重建图像的算术差并确认相位存在位置（差值约等于0±标准差），实现对不同物相的迭代分割 [Jovanovi 2013, pp. 6-7]。
- **平行束几何下BHA的数学建模**：基于van de Casteele等人对信号谱双模态能量分布的观测，推导了平行束几何下，可将BHA描述为矩形函数的逆Radon变换，最终解为沿半径方向变化的反比例函数：$f(r) = \frac{K}{\pi\sqrt{R^2 - r^2}}$ [Jovanovi 2013, pp. 4-5]。模拟结果证实了单相圆柱体模中衰减值的径向依赖性 [Jovanovi 2013, pp. 5-5]。
- **分割流程的六步执行**：(i) 提取某一相位的射束硬化曲线；(ii) 构造仅由该相位组成的“人工对象”；(iii) 计算人工对象与重建图像间的算术差；(iv) 差值在零附近（±标准差）确认该相位存在；(v) 差值超出标准差范围则确认其他相位存在；(vi) 对所有固相重复此流程，直至所有相分布被解算 [Jovanovi 2013, pp. 7-7]。

## Key Findings
- **BHA的径向依赖性**：在轴对称的圆柱形样本中，BHA表现为一个径向函数，即同一组分在距圆柱中心相同距离处的重建衰减值相同 [Jovanovi 2013, pp. 1-1, 5-6]。
- **衰减值曲线的形状**：衰减值沿径向遵循指数或抛物线形的“射束硬化曲线”，自中心向外围增加，并在接近边缘处出现一个“隆起（bump）”。隆起的具体位置和形状取决于材料，使用金属箔片过滤后，某些材料的隆起可能消失 [Jovanovi 2013, pp. 6-6]。
- **非圆柱形样本的不适用性**：对于非圆柱形样本，BHA不再是单纯的径向函数，而是随角度变化，因此该方法可能过于复杂且不切实际 [Jovanovi 2013, pp. 8-8]。
- **分割有效性验证**：提出的方法能够利用BHA本身来区分不同材料，并在此过程中生成一个无射束硬化的图像 [Jovanovi 2013, pp. 1-1]。对花岗岩样本的测试显示，通过该方法可以区分石英、钾长石、钠质斜长石和钙质斜长石等主要造岩矿物相，尽管最暗的相（石英、钾长石、钠质斜长石）在误差范围内与钙质斜长石存在重叠 [Jovanovi 2013, pp. 6-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 圆柱形样品中，同一物相在距中心相同距离处的重建衰减值恒定，表现为径向函数。 | [Jovanovi 2013, pp. 5-6] | 样品形状必须为圆柱形，且切片垂直于长轴（z轴）方向。 | 这是该方法的核心观测基础。 |
| 衰减值沿径向遵循指数或抛物线形曲线，边缘存在隆起。 | [Jovanovi 2013, pp. 6-6] | 使用μCT扫描圆柱样品。 | 隆起的形状和幅度与被扫描材料及滤波条件有关。 |
| 花岗岩样本中，最暗矿物相（石英、钾长石、Na-斜长石）的BHA曲线在误差范围内重叠，但可与钙质斜长石（灰色）区分。 | [Jovanovi 2013, pp. 8-8] | 从花岗岩样本的μCT数据中提取。 | 说明该方法对成分相近的矿物相的分辨率有限。 |
| 模拟证明，平行束几何下单相圆柱体的重建图像，其值遵循 $f(r) = \frac{K}{\pi\sqrt{R^2 - r^2}}$ 形式的径向分布。 | [Jovanovi 2013, pp. 4-5] | 数学推导基于平行束几何假设，模拟基于K=1的单相圆柱体模。 | 数学推导结果与实验观察到的径向依赖性一致。 |
| 样品顶部和底部区域位于Tam-Danielsson窗口之外，其重建数据有问题，必须切掉，不能进行分割。 | [Jovanovi 2013, pp. 6-6] | 使用Feldkamp算法进行重建的锥束CT系统。 | 明确了该方法的轴向有效范围。 |

## Limitations
- **样品形状限制**：该方法严格依赖于样品的圆柱形状。对于非圆柱形或不规则形状的地质样品，BHA不再是简单的径向函数，因此该方法不切实际或无法应用 [Jovanovi 2013, pp. 8-8]。
- **区分度的物理限制**：如果不同物相的射束硬化曲线在测量的标准差范围内存在重叠，该方法无法将其区分开来 [Jovanovi 2013, pp. 7-7, 8-8]。
- **有效区域限制**：圆柱样品顶部和底部的区域落在锥束CT的Tam-Danielsson窗口之外，重建结果不可靠，因此这些区域不能被分割，必须从图像中切除 [Jovanovi 2013, pp. 6-6]。
- **数学模型的适用性限制**：文中提出的数学推导仅针对平行束几何，未扩展到桌面μCT常用的锥束几何 [Jovanovi 2013, pp. 5-5]。对于圆柱形样品，该方法依赖于Feldkamp重建算法 [Jovanovi 2013, pp. 5-6]。
- **无法确认其在多矿物、复杂结构孔隙岩石中的普适性**：虽然实验包括花岗岩，但索引片段未提供对更广泛的复杂地质样本的定量验证结果。

## Assumptions / Conditions
- **样本几何假设**：该方法基于样本为垂直安装的、轴向对称的圆柱体这一前提 [Jovanovi 2013, pp. 5-6]。
- **重建算法假设**：应用于圆柱形样本时，假设使用了Feldkamp等人（1984）的锥束CT重建算法 [Jovanovi 2013, pp. 5-6]。
- **数据前提**：不要求预先知晓X射线光谱或各物相的衰减系数 [Jovanovi 2013, pp. 1-1]。
- **物理前提**：基于van de Casteele等观测到的信号谱可分解为双模态能量分布的物理基础 [Jovanovi 2013, pp. 3-4]，以及该BHA模型可在平行束几何下简化的数学假设。

## Key Variables / Parameters
- **$r$**：圆柱样品的径向坐标（距中心的距离）[Jovanovi 2013, pp. 4-5]。
- **$R$**：圆柱样品的半径 [Jovanovi 2013, pp. 4-5]。
- **$K$**：常数，由矩形函数 $\Pi(R/2\xi)$ 定义 [Jovanovi 2013, pp. 4-5]。
- **$\xi$, $\Phi$**：Radon空间坐标，$\Phi$为投影角，$\xi$为投影线上的位置 [Jovanovi 2013, pp. 4-4]。
- **$f(r)$**：重建图像的径向函数分布，理论推导为 $f(r) = \frac{K}{\pi\sqrt{R^2 - r^2}}$ [Jovanovi 2013, pp. 5-5]。
- **射束硬化曲线（Beam-hardening curve）**：实验提取的衰减值随径向距离变化的曲线 [Jovanovi 2013, pp. 6-6]。
- **标准差（Standard Deviation）**：用于判断算术差是否约等于零，以确认物相存在与否的误差阈值 [Jovanovi 2013, pp. 7-7]。

## Reusable Claims
- **Claim 1**: 在多色μCT中，圆柱形样品的射束硬化伪影（BHA）导致的重建衰减值是距离其中心距离的径向函数，这允许在不知道光谱和衰减系数的情况下，通过提取该径向关系来区分不同物相 [Jovanovi 2013, pp. 1-1, 5-6]。
- **Claim 2**: 提取某一物相的“射束硬化曲线”后，可通过构建仅含该相的“人工对象”并与原始重建图像求差，若某体素的差值在该相标准差范围内（约等于零），则可判定该体素属于此物相 [Jovanovi 2013, pp. 7-7]。这为多矿物岩石的定量分析提供了一种“使用伪影进行分割”的新思路。
- **Claim 3**: 在平行束几何假设下，利用范德卡斯蒂尔等人观察到的双模态能量分布特性，可将BHA对均匀圆柱体投影的贡献模拟为一个矩形函数，其重建图像在空间域的解析解为 $f(r) = \frac{K}{\pi\sqrt{R^2 - r^2}}$，这为从第一性原理上理解BHA的径向依赖性提供了数学基础 [Jovanovi 2013, pp. 4-5]。

## Candidate Concepts
- [[Beam-hardening artifact (BHA)]] (射束硬化伪影)
- [[Polychromatic X-ray computed tomography]] (多色X射线计算机断层扫描)
- [[Post-reconstruction correction]] (后重建校正)
- [[Image segmentation in geologic samples]] (地质样本图像分割)
- [[Radon space]] (Radon空间)
- [[Bimodal energy distribution]] (双模态能量分布)
- [[Tam-Danielsson window]] (Tam-Danielsson窗口)

## Candidate Methods
- [[Linearization method for beam hardening]] (射束硬化线性化校正法)
- [[Dual energy CT method]] (双能CT方法)
- [[Pre-filtering method for BHA]] (射束硬化预过滤法)
- [[Sinogram correction method]] (正弦图校正法)
- [[Feldkamp cone-beam reconstruction algorithm]] (Feldkamp锥束重建算法)

## Connections To Other Work
- 本文的BHA数学分析部分直接基于**Van de Casteele等人（2002, 2004）**关于信号谱可被描述为双模态能量分布的观察 [Jovanovi 2013, pp. 3-4]，但后者提出的方法需要先分割图像以进行多组分样品校正，而本文的方法则利用BHA本身来实现分割。
- 论文指出相关校正方法，如预过滤法、线性化法和双能法的局限性，这些方法在应用于组分未知的复杂地质样品时失效，这构成了本文工作的背景 [Jovanovi 2013, pp. 1-3]。
- 论文应用了**Feldkamp等人（1984）**的算法进行锥束CT图像重建 [Jovanovi 2013, pp. 5-6]，并引用了**Danielsson等人（1997）**和**Tam等人（1998）**关于Tam-Danielsson窗口的理论来解释图像边缘数据不可靠的原因 [Jovanovi 2013, pp. 6-6]。

## Open Questions
- 如何将文中基于平行束几何的数学推导扩展到桌面μCT常用的锥束几何，以实现非圆柱形样本的分割与BHA校正？[Jovanovi 2013, pp. 8-8]
- 对于不同矿物相的BHA曲线存在严重重叠的复杂岩石样本，该方法的适用性和准确性极限如何？未从索引片段中确认。
- 射束硬化曲线在边缘“隆起”的具体物理成因及其在不同材料、不同扫描参数下的普适性规律是什么？未从索引片段中确认。

## Source Coverage
本页面依据9个索引片段编写，覆盖了论文的摘要、引言、方法（数学分析、分割流程）、部分结果与讨论以及结论。覆盖全面性较高，包含了核心创新点的完整逻辑链和验证结果。然而，索引片段**不包含**详细的实验参数、完整的定量分割精度评估数据（如各种岩石类型的混淆矩阵）、以及与非圆柱形样本对比的详细实验。论文中可能存在的更多讨论、未来研究细节和致谢之后的内容也未体现在片段中。
