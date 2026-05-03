---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur"
title: "Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures."
status: "draft"
source_pdf: "data/papers/2017 - Numerical modeling of the effects of roughness on flow and eddy formation in fractures.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Briggs, Scott, et al. \"Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 9, 2017, pp. 105-15. doi:10.1016/j.jrmge.2016.08.004. Accessed 10 Oct. 2026."
indexed_texts: "13"
indexed_chars: "62044"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62288"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003933"
coverage_status: "full-index"
source_signature: "ad7c1b5f7cc14551a9bd41ef96ab3d5d8b13c1ed"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:17:32"
---

# Numerical Modeling of the Effects of Roughness on Flow and Eddy Formation in Fractures.

## One-line Summary
利用格子Boltzmann方法（LBM）系统研究了断裂粗糙度对水流和涡流形成的影响，揭示了随雷诺数（Re）增加的有效水力隙宽、Izbash系数和Forchheimer参数的变化，并提出一个基于涡流增长的三区非线性流动模型。

## Research Question
断裂表面粗糙度如何影响流体在断裂中的流动模式与涡流生成？随着雷诺数从0.01提升到500，有效水力隙宽、非线性流动参数（Izbash和Forchheimer系数）以及涡流体积如何变化 [Briggs 2017, pp. 1-1]？

## Study Area / Data
- **合成断裂**：通过SynFrac软件生成，具有控制的分形维度（Hurst指数从1到0.65），断裂长度100 mm，算术平均隙宽1.7 mm，无接触点 [Briggs 2017, pp. 3-5]。
- **天然白云岩断裂**：来自一块含缝合线的白云岩样本，长约280 mm，宽210 mm，厚70 mm。使用ATOS II三维立体形貌测量系统获取表面高度，提取一条16 mm长的二维剖面，平均隙宽0.1 mm [Briggs 2017, pp. 3-5][Briggs 2017, pp. 3-5]。

## Methods
- **数值模拟**：采用二维九速格子Boltzmann方法（LBM），在GPU上通过CUDA实现。碰撞采用BGK近似，周期性边界条件，重力驱动，无进出口效应 [Briggs 2017, pp. 2-3][Briggs 2017, pp. 3-3]。
- **流动方程**：基于Hagen-Poiseuille分析解推导有效水力隙宽，利用重力加速度转换为速度增量驱动流体 [Briggs 2017, pp. 3-3]。
- **非线性模型拟合**：对模拟结果使用Forchheimer二次方程（i = a₁q + bq²）和Izbash幂律方程（i = cqᵇ）进行拟合 [Briggs 2017, pp. 3-5]。
- **粗糙度表征**：采用角阈值粗糙度参数（Tatone & Grasselli, 2010）量化表面粗糙度，同时使用Hurst指数 [Briggs 2017, pp. 5-5]。
- **涡流体积计算**：依据有效水力隙宽与总隙宽之比推算，并通过流线分离阈值线验证，误差在10%以内 [Briggs 2017, pp. 8-9]。
- **弯曲度计算**：以流动最快流线的实际路径长度除以断裂投影长度 [Briggs 2017, pp. 9-10]。

## Key Findings
- **涡流形成与粗糙度**：涡流在Re ≈ 1开始出现，随Re增大显著生长；粗糙度越大，相同Re下涡流体积越大，有效水力隙宽越低 [Briggs 2017, pp. 1-1][Briggs 2017, pp. 5-6]。
- **三区非线性模型**：
  - **Zone I（Re < 1）**：有效隙宽几乎不变，但绝对数值受初始断裂几何影响 [Briggs 2017, pp. 6-8]。
  - **Zone II（Re ≈ 1 至约30）**：涡流快速增长，有效隙宽下降速率增大 [Briggs 2017, pp. 6-8]。
  - **Zone III（Re > 30）**：涡流增长速率减缓，有效隙宽下降速率减小，流动转为强非线性，可用Forchheimer方程描述，Izbash幂指数随粗糙度增大而升高（例如从1.05增到1.22）[Briggs 2017, pp. 6-8][Briggs 2017, pp. 6-8]。
- **参数影响**：Forchheimer线性系数a₁和惯性系数b均随粗糙度增加而增大；Izbash系数c和指数b在Zone III亦随粗糙度增加 [Briggs 2017, pp. 6-8]。
- **弯曲度**：弯曲度随粗糙度增加而升高，并与Re呈非线性关系，总体趋势近似三区变化 [Briggs 2017, pp. 9-10]。
- **方向依赖性**：在SynFrac默认参数及Re < 100时，正向与反向流动差异小于1%，说明生成的断裂无明显方向性 [Briggs 2017, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Eddy formation starts around Re ≈ 1, grows significantly with Re | [Briggs 2017, pp. 1-1] | LBM simulations, synthetic & natural fractures, 0.01 ≤ Re ≤ 500 | Consistent with previous studies (e.g., Zimmerman et al., 2004) |
| Relative effective hydraulic aperture decreases with increasing roughness for same Re | [Briggs 2017, pp. 5-6] | Synthetic fractures with H = 0.65 to 1, mean aperture 1.7 mm | Aperture reduction due to secondary flows |
| Three-zone behavior in effective aperture vs. Re | [Briggs 2017, pp. 6-8] | Synthetic & dolomite fractures; zone boundaries at Re ≈ 1 and Re ≈ 30 (synthetic) | Similar to Chaudhary et al. (2011) for porous media |
| Forchheimer coefficients a₁ and b increase with roughness (H = 1: a₁=0.5, b=0.27; H = 0.65: a₁=0.78, b=5.76) | [Briggs 2017, pp. 6-8] | Fitted for entire Re range (0.01–500) | |
| Izbash exponent in Zone III increases with roughness (H = 1: β=1.05; H = 0.65: β=1.22) | [Briggs 2017, pp. 6-8] | Fitted separately for Zones I&II and Zone III | Zone I β = 1 for all fractures |
| Eddy volume ratio reaches ~0.3 for H = 0.65 at high Re | [Briggs 2017, pp. 8-9] | From effective aperture and streamline threshold method | Method validation error <10% |
| Tortuosity increases with roughness and varies nonlinearly with Re | [Briggs 2017, pp. 9-10] | Defined by fastest streamline length | |
| Reversed flow direction shows <1% variation in effective aperture for Re<100 | [Briggs 2017, pp. 9-10] | SynFrac default settings | Roughness anisotropic parameter also varied ~1% |

## Limitations
- 二维模拟无法捕捉接触点对有效隙宽和弯曲度的三维效应 [Briggs 2017, pp. 3-5]。
- 模拟断裂不含接触点，实际断裂中接触区域会改变流动路径 [Briggs 2017, pp. 3-5]。
- 天然白云岩断裂长度仅16 mm，不能完全代表较大尺度断裂行为 [Briggs 2017, pp. 3-5]。
- LBM在松弛参数s接近0.5时引入数值误差，但整体趋势仍可接受 [Briggs 2017, pp. 3-3]。
- 合成断裂使用固定失配长度15 mm，可能影响表面相关结构 [Briggs 2017, pp. 5-5]。

## Assumptions / Conditions
- 二维层流、不可压缩流体 [Briggs 2017, pp. 3-3]。
- 重力驱动，无外加压力或速度边界 [Briggs 2017, pp. 3-3]。
- 周期性边界条件模拟无限长断裂段 [Briggs 2017, pp. 3-3]。
- 格子速度≤0.1 lu/ts以减小可压缩性误差 [Briggs 2017, pp. 3-3]。
- 合成断裂算术平均隙宽固定为1.7 mm，标准偏差1 mm，各向异性因子1 [Briggs 2017, pp. 3-5]。
- 粗糙度仅以分形维数或Hurst指数控制，未模拟多尺度粗糙度叠加的全部复杂性 [Briggs 2017, pp. 5-5]。

## Key Variables / Parameters
- Reynolds number (Re): 0.01 – 500 [Briggs 2017, pp. 3-3]
- Hurst exponent (roughness): 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0 [Briggs 2017, pp. 5-5]
- Angular threshold roughness: 9.62°–27.29° [Briggs 2017, pp. 5-6]
- Mean aperture: synthetic 1.7 mm, dolomite 0.1 mm [Briggs 2017, pp. 3-5]
- Effective hydraulic aperture (2a_eff) [Briggs 2017, pp. 3-5]
- Eddy volume ratio [Briggs 2017, pp. 8-9]
- Forchheimer coefficients a₁, b [Briggs 2017, pp. 6-8]
- Izbash coefficients c, β [Briggs 2017, pp. 6-8]
- Tortuosity [Briggs 2017, pp. 9-10]

## Reusable Claims
- 粗糙断裂中涡流在Re ≈ 1时形成，并随Re增加而生长，导致有效水力隙宽降低 [Briggs 2017, pp. 1-1]。
- 有效水力隙宽与Re的关系可用三区模型描述：Zone I常隙宽（Re<1），Zone II快速下降（1<Re<~30），Zone III下降减缓且流动呈强非线性（Re>~30） [Briggs 2017, pp. 6-8]。
- Forchheimer方程可涵盖整个Re范围（0.01–500），其系数a₁和b随粗糙度增大而增大 [Briggs 2017, pp. 6-8]。
- Izbash幂定律在Zone III指数随粗糙度增加（从~1.05增至1.22），而在低Re区为线性（β=1） [Briggs 2017, pp. 6-8]。
- 涡流体积比随Re增加而单调增大，粗糙度越高，最终涡流体积越大 [Briggs 2017, pp. 8-9]。
- 弯曲度随粗糙度增加，且与Re呈非线性关系，高Re下粗糙断裂弯曲度显著上升 [Briggs 2017, pp. 9-10]。
- 对于Re<100，合成断裂正反向流动差异小于1%，默认SynFrac设置产生的断裂无明显方向性 [Briggs 2017, pp. 9-10]。

## Candidate Concepts
- [[fracture flow]]
- [[roughness]]
- [[eddy formation]]
- [[lattice Boltzmann method]]
- [[effective hydraulic aperture]]
- [[Izbash law]]
- [[Forchheimer equation]]
- [[three-zone nonlinear flow model]]
- [[Hurst exponent]]
- [[fracture generation using SynFrac]]
- [[angular threshold roughness]]
- [[tortuosity]]
- [[gravity-driven flow]]
- [[periodic boundary condition]]
- [[secondary flows in fractures]]

## Candidate Methods
- [[Lattice Boltzmann method (LBM) two-dimensional nine-velocity BGK]]
- [[SynFrac synthetic fracture generator]]
- [[ATOS II 3D stereo-topometric surface measurement]]
- [[gravity-driven flow simulation with periodic boundary conditions]]
- [[effective hydraulic aperture calculation from LBM flow rate]]
- [[eddy volume threshold streamline method]]
- [[Forchheimer and Izbash nonlinear regression fitting]]
- [[tortuosity estimation via fastest streamline path length]]

## Connections To Other Work
- 涡流引发非线性流动的发现与Chaudhary et al. (2011) 在孔隙介质中的三区模型一致 [Briggs 2017, pp. 1-2]。
- 三区模型在断裂中的适用性扩展了Skjetne et al. (1999) 和Zimmerman et al. (2004) 的工作 [Briggs 2017, pp. 6-8]。
- 粗糙度对有效隙宽的影响与Brush and Thomson (2003) 的3D Stokes/Navier-Stokes模拟结果相符 [Briggs 2017, pp. 1-2]。
- 大尺度粗糙特征控制主涡流位置，小尺度粗糙增加涡流复杂性，印证了Zou et al. (2015) 的结论 [Briggs 2017, pp. 2-3]。
- Forchheimer和Izbash关系的适用性与Qian et al. (2011)、Cherubini et al. (2012) 等实验研究一致 [Briggs 2017, pp. 1-2]。

## Open Questions
- 接触点对三区模型及涡流发展的定量影响待研究 [Briggs 2017, pp. 3-5]。
- 三维模拟中涡流体积比、弯曲度与二维结果的差异程度未明确 [Briggs 2017, pp. 3-5]。
- 粗糙度参数（角阈值与Hurst指数）与流动非线性参数之间是否存在通用映射关系 [Briggs 2017, pp. 5-6]。
- 更高雷诺数（Re>500）下过渡到湍流时三区模型的延续性未探索 [Briggs 2017, pp. 6-8]。

## Source Coverage
本页面完全基于提供的13个非空索引片段编译而成，所有片段均被处理。源文本字符覆盖率（coverage_ratio_by_chars）为1.003933（即片段总字符数62288，编译引用字符62288，略有超出因文本截断拼接），片段覆盖率（coverage_ratio_by_blocks）为1.0。未添加任何外部信息。所得论断均直接源自索引标注的源位置 [Briggs 2017, pp. X-Y]。
