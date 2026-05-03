---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2006-song-estimation-of-a-joint-diameter-distribution-by-an-implicit-scheme-and-interpolation-te"
title: "Estimation of a Joint Diameter Distribution by an Implicit Scheme and Interpolation Technique."
status: "draft"
source_pdf: "data/papers/2006 - Estimation of a joint diameter distribution by an implicit scheme and interpolation technique.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Song, Jae-Joon. \"Estimation of a Joint Diameter Distribution by an Implicit Scheme and Interpolation Technique.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 43, 2006, pp. 512-519. doi:10.1016/j.ijrmms.2005.09.009. Accessed 2026."
indexed_texts: "7"
indexed_chars: "32617"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "32760"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004384"
coverage_status: "full-index"
source_signature: "511c2bbed32aa74d2e034b71c517654f0514e6b5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T12:54:07"
---

# 基于隐式方案和插值技术的节理直径分布估计

## One-line Summary
本文提出一种从窗口内截断迹长分布直接估计节理直径分布的隐式方法，并利用B样条插值进一步提高小样本下的估计精度，同时可附带获得体积频率。

## Research Question
如何在不依赖无限窗口迹长分布的前提下，仅从野外实测的截断迹长样本中准确估计节理组的直径分布，并提升小样本量下的估计可靠性？

## Study Area / Data
本研究基于蒙特卡洛虚拟采样窗生成数据：[Song 2006, pp. 4-5]  
- 虚拟节理圆盘服从对数正态分布（均值5 m，标准差2.5 m）；  
- 矩形采样窗尺寸54 m × 20 m，水平放置；  
- 节理组产状030/45；  
- 体积频率从0.01 m⁻³~0.4 m⁻³调节以改变样本规模；  
- 仅采集截断迹长（contained trace）作为样本；  
- 每组体积频率下重复10次，计算平均误差；  
- 非平行节理情形采用Fisher分布（K=15, 25, 35）测试。  
无具体矿区或野外数据，全部基于虚拟模拟。

## Methods
1. **隐式最小二乘估计（L.S.M.）** [Song 2006, pp. 2-4]  
   - 假设节理为Poisson圆盘模型，同组节理平行；  
   - 推导截断迹长数量与直径分布的积分关系（式4），离散化后得到线性方程组（式11）；  
   - 通过最小化理论与实测迹长频数误差平方和，形成矩阵方程 \[A_{kj}\]\{c\_j\} = \{b\_k\}，用逐次超松弛法（SOR）求解直径分布；  
   - 任意初始λ\_V（体积频率）可求解，最终分布归一化后λ\_V可由面积还原。

2. **对比显式方法（D.C.）** [Song 2006, pp. 4-5]  
   - 采用Song & Lee (2001)的显式方案：先估计无限窗口迹长分布，再通过数值积分反演直径分布（式13），需要面频率和迹长累积分布。

3. **B样条插值平滑** [Song 2006, pp. 5-7]  
   - 对截断迹长方图采用非周期B样条（三阶、五阶、七阶混合函数）平滑；  
   - 将平滑后的分布代入L.S.M.估计直径分布；  
   - 比较不同阶数及无插值时的估计误差。

4. **验证与评估**  
   - 蒙特卡洛模拟：预定义直径分布，比较估计分布与真实分布的绝对面积误差之和。

## Key Findings
- 隐式方案（L.S.M.）与显式方案（D.C.）在整体样本规模下精度相当，但在截断迹长数量小于100时，L.S.M.误差明显更小，对实际工程中常遇到的小样本更具优势 [Song 2006, pp. 5-6]。  
- L.S.M.可附带获得体积频率，其估计误差百分比在各样本量下均低于D.C.（见表1） [Song 2006, pp. 5-6]。  
- 即使节理组内产状非平行（Fisher分布κ=15~35），L.S.M.估计误差未发生显著变化，方法无需修正 [Song 2006, pp. 6-7]。  
- 引入B样条插值能有效降低直径分布估计误差，对小样本效果更显著；三阶B样条使平均误差降至仅用L.S.M.的约80% [Song 2006, pp. 7-8]。  
- 当采用七阶混合函数时，相对于无B样条情况，误差降低约40%（对数正态、正态、指数直径分布下均验证） [Song 2006, pp. 7-8]。

## Core Evidence Table
| 证据 | 出处 | 条件 | 备注 |
|------|------|------|------|
| L.S.M.误差在样本量<100时低于D.C. | [Song 2006, pp. 5-6, Figs. 4-5] | 平行节理，对数正态直径，矩形窗 | 误差定义为面积差异绝对值和 |
| L.S.M.估计的体积频率误差百分比小于D.C. | [Song 2006, pp. 5-6, Table 1] | 多组体积频率，平均误差低估 | 如Nc_all=410.2时误差5.9% vs 11.2% |
| Fisher分布下L.S.M.误差与平行工况无显著差异 | [Song 2006, pp. 6-7, Fig. 6] | κ=15~35，窗口和直径分布相同 | 表明方法适用于非平行节理 |
| B样条（3阶）插值使平均误差降至L.S.M.的约80% | [Song 2006, pp. 7-8, Fig. 8] | 对数正态直径，变动样本量 | 小样本改善更明显 |
| 7阶B样条相较于无B样条，误差降低约40% | [Song 2006, pp. 7-8, Figs. 9-11] | 对数正态、正态、指数直径分布 | 5阶与7阶在小样本下效果相近 |

## Limitations
- 显式推导基于节理组内迹线平行的假设，但测试表明对非平行节理仍适用，然而未提供严格理论证明 [Song 2006, pp. 2-3, 6-7]。  
- 采样时假设窗口足够大以忽略截断偏差（censoring bias），该问题被列为后续工作 [Song 2006, pp. 2-3]。  
- 仅通过蒙特卡洛模拟验证，缺乏实际野外数据对比 [Song 2006, pp. 4-8]。  
- B样条阶数的选择缺乏通用准则，文中仅测试了3~7阶 [Song 2006, pp. 7-8]。

## Assumptions / Conditions
- 节理形状为圆形薄盘（Poisson disc model），中心点随机均匀分布 [Song 2006, pp. 1-2]。  
- 同一组节理相互平行，迹线在窗口内平行 [Song 2006, pp. 2-3]。  
- 采样窗口足够大，截断偏差可忽略 [Song 2006, pp. 2-3]。  
- 直径分布和迹长分布可由离散直方图近似，迹长与直径采用相同组距dl [Song 2006, pp. 3-4]。  
- 迹长分布及其导数连续，B样条平滑为此假设服务 [Song 2006, pp. 5-6]。

## Key Variables / Parameters
- \( N_c^i \)：第i个迹长分组的截断迹长实测数量 [Song 2006, pp. 3-4]。  
- \( A_c^l \)：迹长l对应的截断迹长中心点区域面积（式1） [Song 2006, pp. 2-3]。  
- \( \varphi \)：节理面法线与窗口面的锐夹角 [Song 2006, pp. 3-4]。  
- \( \lambda_V \)：体积频率（节理中心点在三维空间的密度） [Song 2006, pp. 3-4]。  
- \( c_j \)：第j个直径分组的概率值（分布列） [Song 2006, pp. 3-4]。  
- \( a_{ij} \)：系数矩阵元素，反映直径j对迹长i的贡献（式7） [Song 2006, pp. 3-4]。  
- \( k \)：B样条混合函数的阶数（3,5,7） [Song 2006, pp. 5-7]。

## Reusable Claims
- **声明1**：从窗口截断迹长方图直接构建线性方程组（式11），通过最小二乘求解直径分布，无需中间转换无限窗口迹长分布。在蒙特卡洛模拟中，当截断迹长数量少于100时，该方法比Song & Lee (2001)的显式转换法误差更低 [Song 2006, pp. 5-6]。  
- **声明2**：同一求解过程中，若初始体积频率设为1，所得直径分布的面积即为真实的体积频率，因此该方法可同时估计体积频率，且误差低于基于面频率和平均直径的间接计算 [Song 2006, pp. 3-4, 5-6]。  
- **声明3**：先对截断迹长方图进行非周期B样条平滑（7阶混合函数），再代入最小二乘估计，可使直径分布估计误差较直接使用直方图降低约40%，且效果在样本量小于200时尤其显著 [Song 2006, pp. 7-8]。

## Candidate Concepts
- [[截断迹长]]（contained trace length）  
- [[节理直径分布]]（joint diameter distribution）  
- [[隐式方案]]（implicit scheme）  
- [[最小二乘估计]]（least square method）  
- [[体积频率]]（volumetric frequency）  
- [[Poisson圆盘模型]]  
- [[B样条插值]]  
- [[混合函数阶数]]  
- [[显式转换法]]（direct conversion）  
- [[蒙特卡洛验证]]

## Candidate Methods
- [[基于截断迹长直方图的直径分布隐式估计]]（implicit diameter estimation from contained trace histogram）  
- [[逐次超松弛法求解直径分布矩阵方程]]  
- [[B样条平滑直方图]]  
- [[蒙特卡洛模拟评价估计误差]]  
- [[面频率-体积频率-平均直径关系法]]（可用于体积频率计算对比）

## Connections To Other Work
- 该方法在Song & Lee (2001)基础上提出，免去了其先求无限窗口迹长分布的步骤，直接利用截断迹长直方图 [Song 2006, pp. 1-5]。  
- 矩阵推导的积分关系源于Warburton (1980)的直径-迹长公式 [Song 2006, pp. 1-2]。  
- 窗口迹长采样区的面积计算参考了Priest (1993)、Zhang & Einstein (1998)等的工作 [Song 2006, pp. 2-4]。  
- 体积频率的对比利用了Mauldon (1998)的点估计法 [Song 2006, pp. 5-6]。  
- 截断偏差的处理思路与La Pointe et al. (1993)关于迹长类型比例的估计有关 [Song 2006, pp. 2-3]。

## Open Questions
- 如何结合截断迹和切割迹（dissecting trace）的比例校正截断偏差，文中仅列为待做工作 [Song 2006, pp. 2-3]。  
- 在真实野外非平行节理场景中，未提供系统偏差的定量分析，仅通过Fisher分布模拟表明可用 [Song 2006, pp. 6-7]。  
- B样条阶数的自适应选择或其与直方图分组数的关系尚待研究 [Song 2006, pp. 7-8]。  
- 未验证该方法在节理产状变化剧烈、窗口形状复杂情况下的表现。

## Source Coverage
已处理的全部7个非空索引片段均纳入本文档，覆盖情况如下：片段数7/7（覆盖率1.0），字符数32760/32617（覆盖率100.4%），来源签名511c2bbed32aa74d2e034b71c517654f0514e6b5，编译策略为单次全量Markdown。
