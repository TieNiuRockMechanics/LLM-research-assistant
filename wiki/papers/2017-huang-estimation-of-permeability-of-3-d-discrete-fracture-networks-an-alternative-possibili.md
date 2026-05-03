---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-huang-estimation-of-permeability-of-3-d-discrete-fracture-networks-an-alternative-possibili"
title: "Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis."
status: "draft"
source_pdf: "data/papers/2017 - Estimation of permeability of 3-D discrete fracture networks An alternative possibility based on trace map analysis.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Huang, Na, et al. \"Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis.\" *Engineering Geology*, vol. 226, 2017, pp. 12-19. doi:10.1016/j.enggeo.2017.05.005."
indexed_texts: "9"
indexed_chars: "43334"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43481"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003392"
coverage_status: "full-index"
source_signature: "7e4f0b0c173fa3d5ab8b0f96ab5c4554963873ea"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:53:35"
---

# Estimation of Permeability of 3-D Discrete Fracture Networks: An Alternative Possibility Based on Trace Map Analysis.

## One-line Summary
基于84个三维离散裂隙网络（DFN）及其672个二维迹线图的分析，提出了一个利用二维迹线图渗透率和三维几何参数（裂隙密度、幂律长度指数）预测三维DFN无量纲等效渗透率的多变量回归模型，并通过与Lang方法对比验证了其适用性。[Huang 2017, pp. 1-2, 5-6, 7-8]

## Research Question
如何利用容易从露头迹线图获得的二维裂隙网络信息来估计三维离散裂隙网络的渗透率，同时避免直接三维计算的高昂成本与不可行性？[Huang 2017, pp. 1-2, 4-5]

## Study Area / Data
本研究使用计算生成的离散裂隙网络模型，未指定实际场地。数据包括：
- 84个三维DFN模型，其裂隙密度ρ范围为0.01 m⁻³至0.125 m⁻³，裂隙长度服从幂律分布，长度指数a为2.0至4.5。
- 对每个三维DFN，提取8个二维切面迹线图（平行于水力梯度方向，即x‑z平面），共672个二维DFN模型。
- 所有裂隙均假设为圆盘状，中心位置和方位均匀随机分布，隙宽均设为1 mm，基质渗透率忽略不计。
- 具体模型参数详见原文表1及附录A。[Huang 2017, pp. 2-4, 7-8]

## Methods
1. **三维DFN生成与流场模拟**  
   使用3DEC生成裂隙网络，通过自编代码（Huang et al., 2016）模拟流体流动。控制方程为Reynolds方程（式2），在裂隙交线处保证质量与流量连续（式3），边界条件为两对面定水头、其余面及裂隙边缘不透水（式4）。采用Galerkin法求解，计算等效渗透率K（式5），并转化为无量纲等效渗透率K₃D′ = K/K₀，其中K₀为隙宽1 mm的单平行板裂隙等效渗透率。[Huang 2017, pp. 2-4]

2. **二维切面流场模拟**  
   从每个三维DFN模型沿y轴均匀切取8个x‑z平面迹线图，使用UDEC（通用离散元程序）基于立方定律（式6）计算流动，边界条件与三维一致。最终同样得到无量纲等效渗透率K₂D′。[Huang 2017, pp. 4-4]

3. **回归模型建立**  
   分析K₃D′与裂隙密度ρ、幂律指数a及平均K₂D′的关系，通过多元回归得到预测式（式7）：  
   `K₃D′ = 1.046 K₂D′ + 456.332 ρ − 1.476 a`  
   仅使用ρ ≥ 0.0125 m⁻³的DFN（因更低密度切面可能不连通）进行回归，相关系数R² = 0.845。[Huang 2017, pp. 5-6]

4. **验证**  
   用ρ = 0.025–0.125 m⁻³的密集裂隙网络（共84个模型）将式（7）预测值与Lang et al. (2014)方法的结果对比，R² = 0.926。[Huang 2017, pp. 6-7]

## Key Findings
1. 三维DFN的无量纲等效渗透率K₃D′随裂隙密度ρ线性增加；在相同ρ下，K₃D′随幂律长度指数a的减小而增大，因为a越小，长裂隙主导流动路径。[Huang 2017, pp. 4-5, 2-2]
2. 当a = 2.0时，裂隙网络主要由少量长裂隙构成导流路径；a = 4.5时，连通性由大量小裂隙控制。（这与Bour and Davy (1998)的逾渗分析一致：a > 4时小裂隙控制连通性，1 < a < 3时流动可能强烈集中于少数大裂隙。）[Huang 2017, pp. 4-5]
3. 二维切面的无量纲等效渗透率K₂D′普遍低于对应的三维K₃D′，低估幅度约为10.45%–80.92%；即使原始三维网络是渗透的，某些切面仍可能不连通，特别是在低密度时。[Huang 2017, pp. 5-5]
4. 提出的多变量回归函数（式7）能够较好地预测三维DFN的渗透率，与直接模拟结果（R²=0.845）及Lang方法（R²=0.926）均吻合，适用于ρ = 0.025–0.125 m⁻³的广泛密度范围。[Huang 2017, pp. 5-7]
5. 该方法可利用露头迹线图建立的二维数值模型方便地获得ρ、a和K₂D’，从而对三维裂隙岩体渗透率进行一级近似估计。[Huang 2017, pp. 6-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| K₃D′随ρ线性增加，a=2.0时从3.63增至8.74，a=4.5时从1.56增至2.98。 | [Huang 2017, pp. 4-5] | ρ=0.01–0.0175 m⁻³，裂隙长径服从幂律分布，隙宽1 mm，基质不透水 | 线性拟合R²值在0.859–0.995之间。 |
| K₂D′比K₃D′低10.45%–80.92%，二维切面可能出现不连流路径。 | [Huang 2017, pp. 5-5] | ρ≥0.01 m⁻³，a=2.0–4.5，每模型切8个面 | 低密度时更明显。 |
| 回归公式：K₃D′=1.046K₂D′+456.332ρ−1.476a | [Huang 2017, pp. 5-6] | ρ≥0.0125 m⁻³，基于84×8=672个二维模型 | R²=0.845（与模拟值），量纲不一致但作为回归式接受。 |
| 对密集裂隙（ρ=0.025–0.125 m⁻³）的预测与Lang方法一致性高 | [Huang 2017, pp. 6-7] | 84个三维模型，384个二维切面 | R²=0.926 |
| a对连通性影响：a=2.0时长裂隙主导，a=4.5时小裂隙主导 | [Huang 2017, pp. 2-2, 4-5] | 基于生成网络观察及Bour & Davy (1998)逾渗透理论 | |

## Limitations
- 基质渗透率被忽略，仅适用于基质渗透率极低的裂隙岩体。考虑多孔基质时，裂隙与基质相互作用会使渗透率估计更复杂。[Huang 2017, pp. 6-7]
- 所有裂隙假设为光滑平面，隙宽均设为1 mm，未考虑隙宽非均质性及由此引起的沟道效应。隙宽变化可能增大三维与二维渗透率的差异。[Huang 2017, pp. 6-6]
- 模型域尺寸固定为20 m × 20 m × 20 m，未计算表征单元体积(REV)。低密度条件下模型可能未达到REV，尺度效应的影响需要进一步研究。[Huang 2017, pp. 6-7]
- 回归模型基于特定假设（圆形裂隙、幂律长度分布、均匀方位和位置随机），在裂隙形状、分布规律不同的情况下适用性未验证。
- 回归使用的二维渗透率为8个切面的平均值，未考虑方向性和渗透率张量的各向异性。

## Assumptions / Conditions
- 所有裂隙为圆形盘状，中心位置和方位均匀且独立随机分布。[Huang 2017, pp. 2-2]
- 裂隙隙宽恒定且均匀，均为1 mm，不考虑隙宽的空间变化。[Huang 2017, pp. 2-2]
- 裂隙长度服从幂律分布，长度指数a在2.0–4.5之间，具有上、下限lmin和lmax。[Huang 2017, pp. 2-2]
- 基质不透水，流体仅在相互连通的裂隙内流动。[Huang 2017, pp. 2-2]
- 流态为稳态层流，可用Reynolds方程描述。[Huang 2017, pp. 3-4]
- 二维切面平行于流动方向（x‑z平面），边界条件与三维模型一致。[Huang 2017, pp. 4-4]
- 回归模型成立要求ρ ≥ 0.0125 m⁻³，因为更低密度下切面可能无连续流动路径。[Huang 2017, pp. 5-6]

## Key Variables / Parameters
- `ρ` — 三维裂隙密度（单位体积裂隙中心数，m⁻³）
- `a` — 裂隙长度幂律分布的指数
- `lmin`, `lmax` — 裂隙长度的下限和上限
- `K` — 等效渗透率（m²），通过达西定律反算
- `K₀` — 单平行板裂隙等效渗透率（隙宽1 mm）
- `K₃D′` — 三维DFN无量纲等效渗透率（K/K₀）
- `K₂D′` — 二维切面无量纲等效渗透率（对每个三维模型取8个切面的平均值）
- `P32` — 单位体积裂隙面积（m²/m³），文中用于辅助分析

## Reusable Claims
1. 对于幂律长度分布且圆形裂隙的DFN，当a较小时（如2.0），导水网络主要由少量长裂隙构成；当a较大时（如4.5），连通性由大量小裂隙控制。[Huang 2017, pp. 2-2, 4-5]  
   *条件：裂隙位置与方位均匀随机，隙宽相同，基质不透水。*
2. 直接使用二维切面渗透率近似三维渗透率会低估10%–80%以上，尤其低密度时部分切面无导水路径，误差显著。[Huang 2017, pp. 5-5]  
   *条件：切面平行于水力梯度方向，裂隙网络满足上述假设。*
3. 基于二维平均渗透率、三维密度及长度指数的多变量回归式（K₃D′ = 1.046·K₂D′ + 456.332·ρ − 1.476·a）能以较高精度预测三维等效渗透率（R²=0.845），且适用于ρ=0.025–0.125 m⁻³的密集裂隙网络（与Lang方法对比R²=0.926）。[Huang 2017, pp. 5-7]  
   *限制：回归系数来自特定模型假设，量纲不一致但作为经验公式使用。*
4. 该方法提供了一种利用露头迹线图（二维DFN）快速近似估计三维裂隙岩体渗透率的途径，可作为一级近似用于工程实践。[Huang 2017, pp. 6-7]  
   *前提：可获取裂隙密度、长度分布指数和二维切面渗透率。*

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[dimensionless equivalent permeability]]
- [[trace map analysis]]
- [[power-law fracture length distribution]]
- [[fracture density]]
- [[fracture connectivity]]
- [[percolation theory]]
- [[2D vs 3D permeability discrepancy]]
- [[multi-variable regression model for permeability]]
- [[Reynolds equation for fracture flow]]
- [[cubic law]]
- [[representative elementary volume (REV)]]
- [[fracture aperture heterogeneity]]
- [[channeling effects]]

## Candidate Methods
- [[3DEC-based DFN generation and meshing]]
- [[Galerkin method for flow in 3D DFN]]
- [[UDEC for 2D trace map flow simulation]]
- [[multi-variable regression to relate 2D and 3D permeability]]
- [[Lang et al. (2014) method for 3D permeability from 2D cut planes]]

## Connections To Other Work
- **Balberg et al. (1984)**：推导了随机方位裂隙的二维与三维平均排除面积/体积，用于逾渗分析。[Huang 2017, pp. 2-2]
- **Darcel et al. (2003b)**：评估了分形裂隙网络的体视规则，推导了从二维测量外推三维长度分布的函数。[Huang 2017, pp. 2-2]
- **Zhao et al. (2015)**：建立了裂隙面三维分形维数与二维剖面轨迹分形参数的相关关系。[Huang 2017, pp. 2-2]
- **Mourzenko et al. (2011)**：给出了各向同性裂隙网络渗透率的表达式，并扩展到Fisher分布的各向异性网络。[Huang 2017, pp. 2-2]
- **Ebigbo et al. (2016)**：利用包含体等效介质模型预测渗透率，用到裂隙纵横比和基质/裂隙渗透率比。[Huang 2017, pp. 2-2]
- **Lang et al. (2014)**：提出用与三维模型无量纲密度相同的二维切面渗透率来近似三维渗透率；本文通过回归避开对切面密度的严格要求，并用该工作进行验证。[Huang 2017, pp. 2-2, 6-6]
- **Bour & Davy (1998)**：应用逾渗理论研究断层长度对连通性的影响，指出当a>4时小裂隙主导连通性，1<a<3时流动集中于大裂隙。[Huang 2017, pp. 4-5]
- **Huang et al. (2016)**：开发了本文所用的三维DFN流动模拟代码。[Huang 2017, pp. 4-4]
- **Liu et al. (2015)**：描述了二维DFN流动计算代码，本文用于切面模拟。[Huang 2017, pp. 4-4]

## Open Questions
- 当基质渗透率不可忽略时，裂隙-基质相互作用如何影响三维渗透率？如何修正回归模型？[Huang 2017, pp. 6-7]
- 裂隙隙宽非均质性（粗糙度、变化隙宽）引起的沟道效应对三维与二维渗透率差异的影响程度，以及如何将隙宽分布纳入预测模型？[Huang 2017, pp. 6-6]
- 模型尺度效应与REV的确定：何时模型尺寸足够代表等效渗透率？尺度对回归系数的影响如何？[Huang 2017, pp. 6-7]
- 裂隙形状（如多边形、椭圆）及非均匀方位分布（如Fisher分布）是否会显著改变二维与三维渗透率的关系？
- 回归公式（式7）在更广泛的裂隙密度范围（特别是ρ<0.0125 m⁻³）及不同边界条件下的适用性需要验证。
- 如何将本方法扩展到各向异性渗透率张量的预测，而不仅限于主方向等效渗透率？
- 剪切引起的隙宽剪胀、张开和闭合对渗透率变化的影响需要进一步研究。[Huang 2017, pp. 7-7]

## Source Coverage
本文档处理了论文全部索引片段，共计9个非空源块，字符覆盖率：源块数100%（9/9），源字符数43481（索引字符数43334，编译后43481，覆盖率~100.34%）。所有片段均已纳入上述各节，无遗漏。未使用独立于片段之外的信息，凡超出片段范围的推论均以“未确认”标记（本页为中文献，依靠片段内容组织，无额外推论）。
