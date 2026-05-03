---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-feng-study-on-a-damage-model-and-uniaxial-compression-simulation-method-of-frozen-thawed-ro"
title: "Study on a Damage Model and Uniaxial Compression Simulation Method of Frozen–Thawed Rock."
status: "draft"
source_pdf: "data/papers/2022 - Study on a Damage Model and Uniaxial Compression Simulation Method of Frozen–Thawed Rock.pdf"
collections:
  - "zotero new"
citation: "Feng, Qiang, et al. \"Study on a Damage Model and Uniaxial Compression Simulation Method of Frozen–Thawed Rock.\" *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 187–211. doi:10.1007/s00603-021-02645-2."
indexed_texts: "15"
indexed_chars: "71541"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:20:40"
---

# Study on a Damage Model and Uniaxial Compression Simulation Method of Frozen–Thawed Rock.

## One-line Summary
通过饱和黄砂岩冻融循环及单轴压缩试验，基于耗散能比相对变化建立冻融损伤模型，评估其精度，并建立数值模拟方法 [Feng 2022, pp. 1-2]。

## Research Question
如何建立准确的冻融岩石损伤模型以及相应的单轴压缩数值模拟方法，以定量评价寒冷区工程岩体的冻融损伤程度 [Feng 2022, pp. 1-2]。

## Study Area / Data
- **岩石类型**：饱和黄砂岩，取自新疆地区，试验温度模拟新疆历史最低‑30 °C 和夏季最高 30 °C [Feng 2022, pp. 2-5]。
- **矿物成分**：α‑石英 83.8%，斯石英 1.3%，α‑鳞石英 2.3%，β‑鳞石英 3.9%，高岭石 8.7% [Feng 2022, pp. 2-5]。
- **微观结构**：层状结构，整体致密 [Feng 2022, pp. 2-5]。
- **冻融循环方案**：‑30 °C ~ 30 °C，每周期 9 h（冻结 4 h、融化 4 h，升降温各 30 min），循环次数 N = 0、20、40、60、100 [Feng 2022, pp. 2-5]。
- **测试项目**：孔隙度、P 波波速、单轴压缩应力‑应变曲线 [Feng 2022, pp. 5-7]。

## Methods
1. **室内试验**：利用高低温试验箱、TAW‑1000 三轴压力机、超声波脉冲发生器、气体孔隙度仪进行物理与力学参数测试 [Feng 2022, pp. 2-5]。
2. **能量计算**：基于应力‑应变曲线计算总能量 \(U\)、弹性应变能 \(U_e\) 和耗散能 \(U_d\)（卸载模量由弹性模量近似）[Feng 2022, pp. 7-9]。
3. **损伤模型建立**：定义耗散能比 \(\lambda_N = \frac{U_d^N}{U^N}\)，根据其相对变化建立冻融损伤因子 \(D\)，并与基于静弹性模量、动弹性模量、孔隙度、P 波波速、总能量五种常见损伤模型对比 [Feng 2022, pp. 9-14]。
4. **数值模拟方法**：建立细观参数与冻融循环次数的函数关系，实现冻融后饱和砂岩单轴压缩的数值模拟，并与试验应力‑应变曲线、峰值应力、峰值应变和能量规律进行验证 [Feng 2022, pp. 1-2]。模拟具体使用的软件或平台未从索引片段中确认。

## Key Findings
- 随冻融循环次数 \(N\) 增加，饱和黄砂岩单轴抗压强度、弹性模量和 P 波波速逐渐降低，峰值应变和平均孔隙度逐渐增大 [Feng 2022, pp. 1-2][Feng 2022, pp. 5-7]。
- 能量演化可分为初始压密、弹性、屈服和破坏后四个阶段；峰前总能量、弹性应变能和耗散能均随 \(N\) 指数衰减，弹性能占比增加，耗散能占比降低，表明冻融加重劣化但破坏剧烈程度减弱 [Feng 2022, pp. 9-11]。
- 基于耗散能比的损伤模型演化曲线与动弹性模量、总能量模型接近，介于静弹性模量与动弹性模量模型之间 [Feng 2022, pp. 13-14]。
- 以单轴抗压强度和峰值应变为指标对该模型进行精度评价，并与五种常用损伤模型对比，耗散能比模型具有良好可靠性 [Feng 2022, pp. 1-2][Feng 2022, pp. 13-14]。具体对比细节未从索引片段中完全确认。
- 数值模拟方法得到的应力‑应变曲线、峰值应力、峰值应变和能量演化与试验结果吻合良好，验证了方法的可靠性 [Feng 2022, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 0次冻融循环平均孔隙度 9.8%，100次增至12.08% | [Feng 2022, pp. 5-7] | 饱和黄砂岩，气体孔隙度仪 | 孔隙度增量随 N 增大 |
| 0次冻融循环平均 P 波速 2724 m/s，100次降至 2065 m/s，衰减率 24.22% | [Feng 2022, pp. 5-7] | N=0,20,40,60,100 | 波速衰减率随循环次数递增 |
| 峰前总能量拟合公式 \(U=175.86e^{-0.00477N}\) (R²=0.92) | [Feng 2022, pp. 9-11] | 饱和黄砂岩，单轴压缩 | 总能量随 N 指数减小 |
| 耗散能拟合公式 \(U_d=41.79e^{-0.01008N}\) (R²=0.98) | [Feng 2022, pp. 9-11] | 同上 | 耗散能衰减最快 |
| 静弹性模量拟合 \(E_N=10.59e^{-0.00757N}\) (R²=0.98) | [Feng 2022, pp. 11-13] | 饱和黄砂岩 | 用于建立静弹模损伤因子 |
| 平均孔隙度线性拟合 \(p_N=9.719+0.0227N\) (R²=0.98) | [Feng 2022, pp. 11-13] | 饱和黄砂岩 | 用于孔隙度损伤因子 |
| 六种损伤因子中，耗散能比模型介于静弹模和动弹模之间 | [Feng 2022, pp. 13-14] | N=0~100 | 比较基准为损伤因子-循环次数曲线 |

## Limitations
- 所提损伤模型与数值模拟方法仅针对饱和黄砂岩和特定冻融温度范围（‑30~30 °C）验证，对其他岩性或非饱和条件的适用性未从索引片段中确认。
- 精度评价虽与五种常见模型对比，但仅采用单轴抗压强度和峰值应变两项指标，且对比数据仅来自本试验及 Deng et al. (2019) 部分数据 [Feng 2022, pp. 13-14]。
- 数值模拟方法的详细实现步骤、细观参数标定过程及采用的软件平台在索引片段中未充分披露。

## Assumptions / Conditions
- **应变等价假设**（Lemaitre, 1984）：损伤材料的应变响应可由无损材料的本构关系用有效应力代替名义应力得到 [Feng 2022, pp. 11-13]。
- 能量计算中将卸载模量近似为加载弹性模量 [Feng 2022, pp. 7-9]。
- 岩石试样饱和，冻融过程温度均匀，冻结-融化各阶段时间基于中心温度测试确定 [Feng 2022, pp. 2-5]。
- 损伤因子 D 取值 0（完整）至 1（完全损伤）[Feng 2022, pp. 11-13]。

## Key Variables / Parameters
- \(N\)：冻融循环次数（0, 20, 40, 60, 100）
- \(p_N\)：冻融后平均孔隙度 (%)
- \(v_N\)：冻融后平均 P 波波速 (m/s)
- \(E_N\)：静弹性模量 (GPa)
- \(U\)、\(U_e\)、\(U_d\)：总能量、弹性应变能、耗散能 (kJ/m³)
- \(\lambda_N\)：耗散能比（\(U_d / U\)）
- \(D\)：冻融损伤因子
- 拟合参数：指数衰减系数、线性增长系数等

## Reusable Claims
- 对于饱和黄砂岩，在‑30~30 °C冻融循环下，平均孔隙度随冻融循环次数线性增加，关系为 \(p_N = 9.719 + 0.0227N\) (R²=0.98) [Feng 2022, pp. 11-13]。  
- 冻融后饱和黄砂岩的峰前总能量随 N 增加呈指数衰减，\(U = 175.86e^{-0.00477N}\) (R²=0.92)，其耗散能衰减系数最大 [Feng 2022, pp. 9-11]。  
- 以耗散能比相对变化定义的损伤因子建立的模型，其演化趋势介于常规静弹性模量与动弹性模量损伤模型之间，可避免单一指标可能带来的偏大或偏小估计 [Feng 2022, pp. 13-14]。  
- 该耗散能比损伤模型在预测单轴抗压强度和峰值应变方面，与试验结果一致性较好，且对比五种常见模型显示出相当的精度 [Feng 2022, pp. 1-2][Feng 2022, pp. 13-14]。  
- 通过建立细观参数与冻融循环次数的函数关系，可实现对冻融后岩石单轴压缩响应的数值模拟，模拟结果在应力‑应变曲线、峰值及能量特征上均能复现试验 [Feng 2022, pp. 1-2]。

## Candidate Concepts
- [[freeze-thaw damage]]
- [[dissipated energy ratio]]
- [[energy evolution in rock]]
- [[yellow sandstone]]
- [[uniaxial compression strength degradation]]
- [[cold region rock mechanics]]
- [[porosity increase due to freeze-thaw]]

## Candidate Methods
- [[freeze-thaw cycle test]]
- [[uniaxial compression test]]
- [[energy analysis (rock)]]
- [[dissipated energy ratio damage model]]
- [[empirical damage factor fitting]]
- [[mesoscopic parameter-based numerical simulation]]
- [[calibration with experimental stress-strain curves]]

## Connections To Other Work
- 与 **Deng et al. (2019)** 的总能量损伤模型进行了直接对比，本文耗散能比模型在强度与峰值应变预测方面表现更优 [Feng 2022, pp. 13-14]。
- 损伤模型建立参考了 **Lemaitre (1984)** 的应变等价性假设 [Feng 2022, pp. 11-13] 和 **Zhang et al. (2020)** 的孔隙度损伤变量定义 [Feng 2022, pp. 11-13]。
- 能量计算与损伤评价背景涉及 **Gao et al. (2020)**（能量耗散比冻融损伤模型）、**Wang et al. (2017)** 及 **Chen et al. (2016)** 等对耗散能的应用 [Feng 2022, pp. 2-2]。
- 动态弹性模量模型引用了 **Hassanzadegan et al. (2014)** 和 **Petersen et al. (2007)** 的研究 [Feng 2022, pp. 2-2]。
- 数值模拟前期工作包括 **Zuber and Marchand (2004)** 的有限元冻胀分析、**Duan et al. (2013)** 的 THM 耦合模型以及 **Fan et al. (2013)** 的 ANSYS 冻融开裂预测 [Feng 2022, pp. 2-2]。

## Open Questions
- 耗散能比损伤模型在不同岩性、非饱和状态及复杂应力路径下的普适性尚未从索引片段中确认。
- 数值模拟方法中细观参数与冻融循环次数的具体函数形式及标定流程细节未在片段中呈现。
- 长期冻融‑力学耦合作用下的损伤累积规律和疲劳效应未涉及。

## Source Coverage
本页基于 15 个索引片段编写，覆盖摘要、引言（损伤模型综述、数值模拟方法综述）、试验材料与仪器、冻融循环方案、力学与物理测试结果、能量演化规律、损伤模型推导与比较、以及数值模拟验证的概述。片段提供了强度、孔隙度、波速、能量拟合等核心数据，但部分试验原始数据（如单轴抗压强度、弹性模量的具体值）仅以表格编号提及而未列出，数值模拟方法的详细建模过程（如细观参数取值、模拟软件、网格划分等）在片段中基本缺失。因此，本页对试验总体结果、能量分析和损伤模型比较的描述较为完整，但对数值模拟技术细节的描述有限。
