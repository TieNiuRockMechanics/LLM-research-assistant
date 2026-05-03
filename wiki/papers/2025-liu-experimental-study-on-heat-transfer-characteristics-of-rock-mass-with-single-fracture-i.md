---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-liu-experimental-study-on-heat-transfer-characteristics-of-rock-mass-with-single-fracture-i"
title: "Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir."
status: "draft"
source_pdf: "data/papers/2025 - Experimental study on heat transfer characteristics of rock mass with single fracture in geothermal reservoir.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Liu, Keliu, et al. \"Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir.\" *Thermal Science and Engineering Progress*."
indexed_texts: "20"
indexed_chars: "96895"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "91500"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.944321"
coverage_status: "full-index"
source_signature: "b31533692eac3828b2828d8f6623c2327a841bf1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:23:28"
---

# Experimental Study on Heat Transfer Characteristics of Rock Mass with Single Fracture in Geothermal Reservoir.

## One-line Summary
通过实验研究了含单一非连通裂隙的花岗岩在加热与注水过程中的温度场动态演化与传热机制，量化了裂隙对基质热传导的阻碍效应，并揭示了热源温度与注水流速对对流换热的控制规律。

## Research Question
地热储层中，非连通裂隙如何影响岩石基质的热传导路径与传热效率？热源温度（\( T_0 \)）和注水流速（\( q_w \)）对裂隙岩体热传导与对流换热特性的调控作用是什么？裂隙倾角对热阻和热通量的阻碍效应如何定量描述？

## Study Area / Data
- **样品来源**：青海省共和盆地龙才沟印支期花岗岩，矿物组成以石英（25%）、长石（40~45%）、角闪石（10~15%）、黑云母（10~15%）为主，非均质性显著 [Liu unknown-year, pp. 2-3]。
- **实验环境**：太原理工大学，恒定室内温度 \( T_i = 27^\circ \text{C} \) [Liu unknown-year, pp. 3-4]。
- **试件规格**：200 mm × 100 mm × 200 mm 立方体花岗岩，切割45°贯穿裂隙（宽度未明确），钻设模拟井筒与58个温度传感器盲孔，以及裂隙上、下端2个传感器，共60个测温点 [Liu unknown-year, pp. 3-4]。
- **数据采集**：多通道数据记录仪（TOPRE TP9000，64通道，精度±0.1°C）实时记录加热9 h与注水9 h全过程温度 [Liu unknown-year, pp. 4-5]。

## Methods
1. **实验系统**：自研裂隙岩体对流换热系统，包含恒速循环注水子系统（泵精度±2%，流量计精度±1%）、恒温热源子系统（温度均匀性±1°C，控制范围0~90°C）、多通道温度数据采集子系统、自动补水子系统 [Liu unknown-year, pp. 4-4]。
2. **实验方案**：  
   - 加热阶段：热源温度 \( T_0 = 60, 70, 80, 90^\circ \text{C} \)，试样底部30 mm浸入热源，连续加热9 h。  
   - 注水阶段：加热后立即以 \( q_w = 0.5, 1.0, 1.5, 2.0, 2.5 \text{ L/min} \) 向裂隙注入25°C循环水，持续9 h。  
   - 每组实验结束后自然冷却至室温，再进行下一组 [Liu unknown-year, pp. 4-5]。
3. **温度场重构**：利用MATLAB二维线性插值计算60个测点的全局温度分布，并计算温度梯度（\( \nabla T \)）及热通量（傅里叶定律）[Liu unknown-year, pp. 6-6]。
4. **阶段划分**：基于温度变化速率定义缓慢升温（I₁）、快速升温（I₂）、二次缓慢升温（I₃）、温度稳定（I₄）以及冷却过程中的快速冷却（II₁）、缓慢冷却（II₂）、缓慢升温（II₃）、温度稳定（II₄） [Liu unknown-year, pp. 10-10, 15-15]。
5. **不确定性分析**：使用误差传播公式计算基质温度 \( T_r \) 最大不确定度 3.62%，循环水温度 \( T_w \) 最大不确定度 4.25% [Liu unknown-year, pp. 5-6]。
6. **数值模拟**：建立与实验一致的二维模型，改变裂隙倾角 \( \theta = 0^\circ, 15^\circ, 30^\circ, 45^\circ, 60^\circ, 75^\circ, 90^\circ \)，求解瞬态热传导平衡方程，分析倾角对顶部平均热通量和稳态温度分布的影响 [Liu unknown-year, pp. 19-20]。

## Key Findings
1. **升温过程阶段化**：70°C热源下，裂隙花岗岩升温分为四个阶段：  
   - I₁（缓慢升温）持续3~24 min，温度变化平缓；  
   - I₂（快速升温）持续42~84 min，加热速率 0.11~0.54 °C/min（近热源处最高达1.55 °C/min）；  
   - I₃（二次缓慢升温）持续152~196 min，速率 0.03~0.04 °C/min；  
   - I₄（温度稳定）后续无明显变化 [Liu unknown-year, pp. 10-10]。
2. **稳定加热温度（\( T_h \)）区域差异性**：  
   - 同一测点，\( T_h \) 随 \( T_0 \) 升高而增加；  
   - 裂隙左侧 \( T_h \) 随垂直距离 \( d_v \) 呈二次指数衰减（\( T_h = \exp(a - b d_v + c d_v^2) \)），右侧则线性下降（\( T_h = A - B d_v \)）；  
   - 当 \( T_0 \) 从60°C升至90°C，左侧终端温升幅度比右侧更小（如CC线终端温升衰减56.46%，DD线衰减48.51%），表明左侧对热源增强的响应更弱 [Liu unknown-year, pp. 11-12]。
3. **注水后冷却与再升温**：  
   - 经历II₁（快速冷却，平均15 min）、II₂（缓慢冷却，25 min）、II₃（缓慢升温，358 min）、II₄（温度稳定，142 min）；  
   - 越靠近裂隙或注入点的测点，达到峰值低温的时间更短，冷却温差和升温温差更大，表明其对对流换热贡献更大 [Liu unknown-year, pp. 16-16]。
4. **循环水温度（\( T_w \)）控制规律**：  
   - 稳定 \( T_w \) 随 \( q_w \) 线性增加（\( R^2 \geq 0.9928 \)），随 \( T_0 \) 指数增加（\( T_w = \exp(a - b T_0 + c T_0^2) \)，\( R^2 \geq 0.9965 \)）；  
   - \( T_0 \) 对 \( T_w \) 的提升效果强于 \( q_w \)（例如 \( T_0 \) 从60→90°C，\( T_w \) 增幅14.7~20.1%；\( q_w \) 从0.5→2.5 L/min，\( T_w \) 增幅5.0~9.9%）[Liu unknown-year, pp. 16-18]。
5. **裂隙对传热的阻碍效应**：  
   - 等效热阻网络分析表明，水平裂隙热阻远大于垂直裂隙（式(8)），因为空气热导率（<0.03 W/m·K）比花岗岩（2.5~4.5 W/m·K）低两个数量级；  
   - 数值模拟显示，相同 \( T_0 \) 下，裂隙倾角从0°增至90°，顶部平均热通量增加40.31%（70°C时从204.02升至286.26 W/m²）；  
   - 顶部水平中心线稳态温度随倾角增大而升高，且左侧温度显著低于右侧；裂隙倾角为0°和90°时温度对称分布，中间角度左右热阻差异先增后减 [Liu unknown-year, pp. 18-20]。
6. **传热机制**：加热过程以基质热传导为主，裂隙内空气对流忽略；注水过程为基质导热与裂隙壁对流传热的耦合，温度梯度方向均背离裂隙壁，表明热量从岩体向裂隙壁传递 [Liu unknown-year, pp. 13-13, 18-19]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 加热阶段划分：I₁ ≤ 24 min，I₂ 42~84 min（0.54°C/min），I₃ 152~196 min（0.04°C/min） | [Liu unknown-year, pp. 10-10] | \( T_0=70^\circ\text{C} \)，监测点#05~#54 | 近热源点#3、#5未经历I₁直接进入I₂ |
| 裂隙左侧 \( T_h \) 非线性衰减（二次指数），右侧线性衰减 | [Liu unknown-year, pp. 12-12] | 监测线CC、EE（左侧）和DD、FF（右侧），\( T_0=60,70,80,90^\circ\text{C} \) | 拟合方程 \( R^2\geq0.99 \) |
| 冷却阶段II₁~II₂温差：点#21降18.6°C，#38降12.0°C vs 线BB近裂隙点降16.4°C、14.1°C | [Liu unknown-year, pp. 15-16] | \( T_0=70^\circ\text{C}, q_w=0.5 \text{ L/min} \) | 越近裂隙温降越大 |
| 稳定 \( T_w \) 随 \( q_w \) 线性增长：\( T_w = 2.05 q_w + 40.13 \) (60°C) | [Liu unknown-year, pp. 18-18] | \( q_w=0.5~2.5\text{ L/min} \) | 所有工况 \( R^2>0.99 \) |
| 稳定 \( T_w \) 随 \( T_0 \) 指数增长：\( T_w = \exp(4.0089 - 0.0148 T_0 + 1.2846\times10^{-4} T_0^2) \) (0.5 L/min) | [Liu unknown-year, pp. 18-18] | \( T_0=60~90^\circ\text{C} \) | \( R^2=0.997 \) |
| 倾角0°→90°，顶部平均热通量从204.02升至286.26 W/m²（+40.31%） | [Liu unknown-year, pp. 20-20] | \( T_0=70^\circ\text{C} \) 数值模拟 | 模拟底部加热，顶部绝热 |
| 基质温度测量最大不确定度3.62%，循环水4.25% | [Liu unknown-year, pp. 5-6] | 误差传递分析 | 系统精度±3%保温，传感器±0.3% |

## Limitations
- 实际地热储层中裂隙多为网络化，且存在非达西流动、粗糙度、接触面积等复杂因素，本研究仅针对单一、光滑、非连通裂隙，未考虑裂隙几何参数的多变性 [Liu unknown-year, pp. 21-21]。
- 温度监测点分布有限（58个基质内+2个裂隙内），对裂隙尖端及复杂路径的捕捉可能不足。
- 实验未实时测量裂隙宽度变化、流体压力及热-力耦合效应，数值模拟仅考虑倾角影响，未纳入裂隙张开度、渗透率等动态参数 [Liu unknown-year, pp. 21-21]。
- 实验周期固定（各9 h），未探讨长期运行或间歇式注采工况下的热恢复特性。
- 不确定度分析仅涵盖设备精度，环境温度波动和试样内部初始温度场的不均匀性未严格标定。

## Assumptions / Conditions
- 加热过程中，裂隙内空气流速极低，其热对流和热辐射影响可忽略，裂隙传热仅考虑导热 [Liu unknown-year, pp. 18-18]。
- 裂隙两表面平行且间距极小，辐射角系数≈1，无外部辐射交换 [Liu unknown-year, pp. 18-18]。
- 注水阶段，裂隙内空气被完全驱替，传热为水与壁面间的对流换热。
- 数值模型边界：底部30 mm为恒温加热区，其余边界绝热；花岗岩热容和密度均匀 [Liu unknown-year, pp. 19-20]。
- 等效热阻分析中，岩石基质视为各向同性，热导率取固定值（花岗岩2.5~4.5 W/m·K，空气<0.03 W/m·K）[Liu unknown-year, pp. 18-19]。
- 所有实验在室内温度27°C下进行，试样初始温度与室温平衡。

## Key Variables / Parameters
| Variable | Symbol | Unit | Description |
|----------|--------|------|-------------|
| 热源温度 | \( T_0 \) | °C | 60, 70, 80, 90 |
| 注水流速 | \( q_w \) | L/min | 0.5, 1.0, 1.5, 2.0, 2.5 |
| 垂直距离 | \( d_v \) | mm | 测点至热源的垂向距离 |
| 裂隙倾角 | \( \theta \) | ° | 数值模拟中0°~90° |
| 稳定加热温度 | \( T_h \) | °C | 加热540 min后温度 |
| 稳定循环水温度 | \( T_w \) | °C | 注水9 h后出口水温 |
| 阶段转换时间 | \( \tau_{sh}, \tau_{rh}, \tau_h \) | min | 缓慢升温结束、快速升温结束、稳定开始时间 |
| 加热速率 | - | °C/min | 各阶段温升速率 |
| 热通量 | \( Q \) | W/m² | 由温度梯度经傅里叶定律计算 |
| 等效热阻 | \( R_{hf}, R_{vf} \) | K/W | 水平/垂直裂隙的串联/并联热阻 |
| 温度梯度 | \( \nabla T \) | °C/mm | 等温面法向温度变化率 |

## Reusable Claims
1. **裂隙花岗岩升温阶段划分**：当底部恒定加热（70°C）时，距热源不同距离的测点依次经历缓慢升温（≤24 min）、快速升温（0.11~0.54°C/min）、二次缓慢升温（0.03~0.04°C/min）和稳定阶段 [Liu unknown-year, pp. 10-10]。  
   *条件*：试件尺寸200×100×200 mm³，单向加热，裂隙倾角45°。
2. **左侧非线性、右侧线性衰减规律**：含倾斜非连通裂隙时，裂隙左侧 \( T_h \) 与 \( d_v \) 呈二次指数衰减（\( R^2>0.99 \)），右侧呈线性下降（\( R^2>0.99 \)），可作为参数化模型的依据 [Liu unknown-year, pp. 12-12]。  
   *条件*：热源温度60~90°C，裂隙倾角45°，空气充填。
3. **循环水温度线性/指数关系**：稳定 \( T_w \) 与 \( q_w \) 线性相关（斜率约0.93~2.05），与 \( T_0 \) 指数相关；\( T_0 \) 的影响权重高于 \( q_w \) [Liu unknown-year, pp. 18-18]。  
   *条件*：单裂隙，注水持续9 h，系统达稳态。
4. **裂隙倾角-热阻-热通量关系**：裂隙倾角增大，等效热阻减小，顶部平均热通量增加；0°→90°时，热通量提升可达40%，且顶部水平温度分布对称性随倾角变化 [Liu unknown-year, pp. 20-20]。  
   *条件*：数值模拟，底部恒温，其它面绝热，花岗岩热导率均匀。
5. **近裂隙测点对对流换热的贡献**：注水过程中，离裂隙或注入点越近，达到峰值低温的时间越短，且冷却/升温温差越大，这些测点可作为热提取效率的敏感指标 [Liu unknown-year, pp. 16-16]。  
   *条件*：单裂隙，流速0.5 L/min，热源70°C。
6. **传热机制分区**：加热阶段基质导热占主导；注水阶段为基质导热+裂隙壁对流换热，温度梯度指向裂隙，表明热量由岩体向裂缝传递 [Liu unknown-year, pp. 13-18]。  
   *条件*：空气导热忽略，水为换热介质。

## Candidate Concepts
- [[single fracture geothermal reservoir]]
- [[heat conduction stage division (I1-I4)]]
- [[fracture hindrance effect on thermal conduction]]
- [[equivalent thermal resistance network (horizontal/vertical)]]
- [[non-Darcy rough discrete fracture network (NR-DFN)]]
- [[thermo-hydro-mechanical (THM) coupling]]
- [[convective heat transfer coefficient in fractures]]
- [[fracture dip angle effect on heat flux]]
- [[two-dimensional temperature interpolation]]
- [[steady-state thermal equilibrium in fractured rock]]

## Candidate Methods
- [[multi-channel real-time temperature monitoring for fractured rock]]
- [[water-jet cutting of artificial single fracture in granite]]
- [[two-dimensional linear interpolation for temperature field reconstruction]]
- [[Fourier’s law based heat flux and temperature gradient calculation]]
- [[uncertainty propagation analysis for thermal experiments]]
- [[transient heat conduction balance equation for finite element simulation]]
- [[constant-speed circulating water injection system]]
- [[constant-temperature water/oil bath heating source]]
- [[stage division by temperature variation rate thresholds]]

## Connections To Other Work
- 与已有的单裂隙传热研究一致：Huang et al. (2019) 利用3D打印粗糙裂隙发现垂直流向的大粗糙度增强传热，平行流向则减少有效传热面积；Peng et al. (2021) 基于分形理论指出裂隙面分形维数越大越易激发湍流、影响边界层厚度 [Liu unknown-year, pp. 1-2]。
- 数值模拟方面，Liu et al. (2021) 对比二维/三维单裂隙模型，提出用裂隙表面积表征传热系数的经验函数；Xue et al. (2021) 采用复合单元法推导裂隙岩体传热控制方程；Chen et al. (2022) 通过相交裂隙模型分析死端裂隙几何效应，发现粗糙死端裂隙促进传热 [Liu unknown-year, pp. 1-2]。
- 基质导热方面，Zhou et al. (2022) 的解析模型强调横向热传导是控制温度时空分布的关键参数，且裂隙张开度和间距影响显著；Zhu et al. (2023) 数值模拟证实裂隙倾角影响热导率 [Liu unknown-year, pp. 1-2]。
- 本研究填补了非连通裂隙对基质热传导阻碍效应实验数据的不足，并通过等效热阻分析将几何因素（倾角）与传热效率联系起来。

## Open Questions
- 复杂裂隙网络（多条裂隙、不同长度、张开度、表面粗糙度、交叉角度）中，传热通道的动态竞争与整体热提取效率如何量化？
- 热-力-化学多场耦合下，裂隙的起裂、扩展及渗透率演化对长期地热开采的传热性能有何影响？
- 如何实现裂隙尖端、粗糙壁面等局部区域的高分辨率实时温度成像？
- 非达西流动（惯性效应）与裂隙粗糙度耦合下的对流换热系数如何准确标定？
- 裂隙连通性（从孤立到完全贯通）的阈值及其对热储开采经济性的影响规律尚不清楚。

## Source Coverage
本页面编译自论文的全部20个非空索引片段，覆盖字符数96,895，编译后正文引用字符数91,500，覆盖率94.43%。Source signature: b31533692eac3828b2828d8f6623c2327a841bf1。所有片段均被处理并整合，无遗漏。
