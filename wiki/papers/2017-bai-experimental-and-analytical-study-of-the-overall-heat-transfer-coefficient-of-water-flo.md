---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-bai-experimental-and-analytical-study-of-the-overall-heat-transfer-coefficient-of-water-flo"
title: "Experimental and Analytical Study of the Overall Heat Transfer Coefficient of Water Flowing through a Single Fracture in a Granite Core."
status: "draft"
source_pdf: "data/papers/2017 - Experimental and analytical study of the overall heat transfer coefficient of water flowing through a single fracture in a granite core.pdf"
collections:
citation: "Bai, Bing, et al. \"Experimental and Analytical Study of the Overall Heat Transfer Coefficient of Water Flowing through a Single Fracture in a Granite Core.\" *Applied Thermal Engineering*, vol. 116, 2017, pp. 79-90. doi:10.1016/j.applthermaleng.2017.01.020."
indexed_texts: "11"
indexed_chars: "53069"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53257"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003543"
coverage_status: "full-index"
source_signature: "b3180e2e57aa868be04d7f69110d4125c0201e07"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:55:44"
---

# Experimental and Analytical Study of the Overall Heat Transfer Coefficient of Water Flowing through a Single Fracture in a Granite Core.

## One-line Summary

通过实验与解析方法研究水流经花岗岩单裂隙时的整体换热系数（OHTC），评估并改进现有公式，提出新公式E，揭示流量与裂隙宽度对换热效率的影响。[Bai 2017, pp. 1-2]

## Research Question

如何准确表征水流与高温花岗岩裂隙壁面之间的整体换热系数（OHTC）？现有公式存在预测异常值（负值或极大值）的缺陷，本研究旨在：
- 开展新的单裂隙水流—换热实验，补充公开实验数据；
- 基于实验数据对比验证现有四种OHTC公式；
- 提出一种能克服现有公式缺陷的新OHTC公式。[Bai 2017, pp. 2-2]

## Study Area / Data

实验所用花岗岩采自中国福建省，制成ϕ50 mm×100 mm圆柱试样，通过巴西劈裂法形成单一裂隙。[Bai 2017, pp. 2-4] 试样基本物理性质及矿物组成见表1。[Bai 2017, pp. 4-5] 实验在围压0、3、6 MPa及围温70、80、90、100 °C条件下进行，水流速率为5、8、10、13、15、18、20、25、30、35 mL/min，共120组工况。[Bai 2017, pp. 4-5] 实验数据全部公开于表3和表4。[Bai 2017, pp. 5-5][Bai 2017, pp. 6-7] 裂隙宽度通过图像测量法与侧向变形修正获得。[Bai 2017, pp. 2-4]

## Methods

实验系统为自主研发的多场三轴试验系统，包括伺服加载、温度控制、流体注入及数据采集子系统。[Bai 2017, pp. 2-4] 加热环置于三轴室外，用隔热套减少热损失；采用ISCO泵恒流注水，并用耐热胶带防止进水管在油中预热。[Bai 2017, pp. 2-4] 数据处理采用牛顿冷却定律与二维半圆盘热传导模型，引入岩壁温度沿径向线性分布假设，并取裂隙中心壁温Ti0等于进出口水温平均值（经验证偏差＜0.11%），推导得公式E：[Bai 2017, pp. 5-6]  
h = cp qw u d (Tw2 − Tw1) / [L (Tc − (Tw1 + Tw2)/2)]  
或等价形式。[Bai 2017, pp. 6-7] 同时对比了文献中四种公式（A~D），如表5所列。[Bai 2017, pp. 7-10] 不确定度分析依据Holman方法，得出公式E的误差传播特性。[Bai 2017, pp. 11-12]

## Key Findings

1. 获得了40组裂隙流动换热实验记录，丰富该领域公开数据集。[Bai 2017, pp. 1-2][Bai 2017, pp. 10-11]  
2. 公式C预测的OHTC多为负值，不推荐在与本研究相似条件下使用；公式B在低流量时合理，高流量（＞20 mL/min）时出现极大值或负值；公式A、D、E预测稳定，其中D与E最为接近。[Bai 2017, pp. 10-11]  
3. 分母含减法项并引入较多变量是导致异常值的直接原因；推导出各公式出现负OHTC的必要条件（表6）。[Bai 2017, pp. 10-11]  
4. 提出的公式E仅在注入水温过分接近油温时接近分母零点，但该类实验无实际意义，因此公式E在实用中几乎不产生异常值；该公式理论严谨、形式简洁，推荐使用。[Bai 2017, pp. 11-12]  
5. 用公式E分析得：OHTC与流量正相关，与裂隙宽度负相关（宽裂隙换热效率降低），且多数OHTC—裂隙宽度曲线的斜率相近。[Bai 2017, pp. 11-12]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 40组全工况实验数据（表3、表4） | [Bai 2017, pp. 5-5][Bai 2017, pp. 6-7] | 围温70~100 °C，围压0~6 MPa，流量5~35 mL/min | 包含进出口水温、裂隙宽度、压差等 |
| 公式C预测大部分OHTC为负值 | [Bai 2017, pp. 7-10] | 本实验条件 | 在8 mL/min时出现绝对值极大的负值 |
| 公式B在流量≥30 mL/min时出现极大或负OHTC | [Bai 2017, pp. 10-11] | 0 MPa围压、100 °C | 30 mL/min时OHTC为43634.4 W/(m²K) |
| 公式D与E的OHTC值最接近（图13） | [Bai 2017, pp. 10-11] | 全部测试条件 | 低流量时E略高，高流量（~30 mL/min）时D略高 |
| 各公式产生负OHTC的必要条件（不等式8-10） | [Bai 2017, pp. 10-11] | 本实验常数条件 | 不等式左、右侧随流量变化（图14） |
| 公式E的测量不确定度最大14.7%，多数＜8% | [Bai 2017, pp. 11-12] | 基于误差传播公式A.3 | 误差随流量增大而下降 |
| OHTC—裂隙宽度曲线斜率相近 | [Bai 2017, pp. 11-12] | 用公式E计算 | 不同围温下分A~D子图 |

## Limitations

- 实验不确定度主要源于温度、流量、尺寸测量，公式E的相对不确定度最大约14.7%，多数在8%以内。[Bai 2017, pp. 11-12]
- 模型假设：岩体不透水、无热辐射、无热损失；忽略裂隙壁曲率；采用二维简化；Ti0用进出口水温平均代替（虽经验证偏差0.11%）。[Bai 2017, pp. 5-6]
- 实验温度≤100 °C，未观察到矿物溶解，但高温长时间下溶解问题需专门关注。[Bai 2017, pp. 5-5]
- 部分出口水温数据可能存在未达到热平衡而提前记录（如80 °C、30和35 mL/min两点），已剔除。[Bai 2017, pp. 5-5]
- 公式推广性：仅针对单裂隙、低流速、小温差工况验证，其他流体或条件需进一步测试。[Bai 2017, pp. 11-12]

## Assumptions / Conditions

- 稳态流动与传热，无轴压差，试样处于静水压力环境。[Bai 2017, pp. 2-4]
- 岩体导热系数视为常数（表1），水物性为定值。[Bai 2017, pp. 11-12]
- 半圆盘内温度沿径向线性分布（式3）；裂隙壁中心温度Ti0 ≈ (Tw1+Tw2)/2。[Bai 2017, pp. 5-6]
- 忽略水流渗入岩石，因花岗岩渗透率极低。[Bai 2017, pp. 5-6]
- 裂隙宽度变形仅由岩石侧向变形修正，忽略两半岩块的压缩。[Bai 2017, pp. 2-4]
- 公式E推导中不考虑Cp和ρ的变化。[Bai 2017, pp. 11-12]

## Key Variables / Parameters

- Tc：围温（油温），K或°C [Bai 2017, pp. 2-4]
- Tw1, Tw2：裂隙进口、出口水温 [Bai 2017, pp. 2-4]
- Q (qV)：体积流量，mL/min [Bai 2017, pp. 4-5]
- d：裂隙平均宽度，μm [Bai 2017, pp. 2-4]
- L：试样长度，m [Bai 2017, pp. 2-2]
- R：试样半径，m [Bai 2017, pp. 2-4]
- h：整体换热系数，W/(m²K) [Bai 2017, pp. 5-6]
- cp,w：水的定压比热，J/(kg K) [Bai 2017, pp. 2-4]
- ρw：水密度，kg/m³ [Bai 2017, pp. 2-4]
- Kr, Kw：岩石、水的导热系数，W/(m K) [Bai 2017, pp. 2-4]
- Le：半裂隙块等效厚度，m [Bai 2017, pp. 5-6]

## Reusable Claims

- 在围温70–100 °C、围压0–6 MPa、流量5–35 mL/min条件下，公式E能稳定给出非负OHTC值，且最大相对不确定度低于15%。[Bai 2017, pp. 11-12]  
- OHTC与水流速正相关，裂隙宽度增大导致OHTC减小。[Bai 2017, pp. 11-12]  
- 公式C在本实验条件下普遍给出负OHTC，不宜采用。[Bai 2017, pp. 10-11]  
- 公式B仅在低流量（＜20 mL/min）下适用，高流量时出现异常值。[Bai 2017, pp. 10-11]  
- 分母含减法项且变量多的OHTC公式易产生异常值，其出现条件可由不等式定量描述（表6）。[Bai 2017, pp. 10-11]

## Candidate Concepts

- [[整体换热系数]] (OHTC)
- [[裂隙换热]] 
- [[增强型地热系统]] (EGS)
- [[干热岩]] (HDR)
- [[单裂隙水流]]
- [[热对流系数]]
- [[裂隙宽度]]
- [[换热效率]]
- [[围压效应]]
- [[实验室尺度热流测试]]

## Candidate Methods

- [[多场三轴试验系统]]
- [[巴西劈裂法]]
- [[图像法测裂隙宽度]]
- [[恒流注水实验]]
- [[牛顿冷却定律反算换热系数]]
- [[二维半圆盘热传导解析解]]
- [[线性温度剖面假设]]
- [[误差传播分析]] (Holman方法)
- [[恒温边界热传导问题]]

## Connections To Other Work

- 早期单裂隙花岗岩换热实验：Zhao (1992)、Zhao and Brown (1992)、Zhao and Tso (1993)、Tso and Zhao (1994)，均采用ϕ50×100 mm圆柱试样，为本文实验原理基础。[Bai 2017, pp. 1-2]
- Ogino et al. (1999) 利用圆盘裂隙进行强制对流换热实验，给出二维传质传热系数。[Bai 2017, pp. 1-2]
- Lu and Xiang (2012) 使用米级规则裂隙花岗岩模型进行流动换热实验。[Bai 2017, pp. 2-2]
- 现有OHTC公式来源：Zhao (1992) 提出方法B；Huang et al. (2016) 和 Zhang et al. (2015) 更新半圆盘温度解得到方法D；Zhao (2014) 提出方法C但出现负值。[Bai 2017, pp. 7-10]
- 本文公式E的Ti0近似方法在Bai et al. (2016) 中通过数值模拟验证。[Bai 2017, pp. 5-6]

## Open Questions

- 公式C在不同数据集下表现差异巨大的原因尚需深入探究。[Bai 2017, pp. 10-11]
- 裂隙表面非均匀粗糙度对局部换热系数的影响未在此OHTC模型中体现。[Bai 2017, pp. 2-4]
- 高温（>100 °C）及长时间运行下的水岩反应（溶解/沉淀）是否改变换热特性尚不清楚。[Bai 2017, pp. 5-5]
- 公式E对其他工作流体（如CO₂）及更大流量范围的适用性有待检验。[Bai 2017, pp. 11-12]
- 当前分析仅针对单裂隙，多裂隙或裂隙网络中的OHTC行为需进一步研究。

## Source Coverage

所有非空索引片段（共11个）均已处理，源文块使用率100%，字符覆盖率约100.35%，资源签名b3180e2e57aa868be04d7f69110d4125c0201e07，编译策略为单次直接生成。提供证据完全来自[Bai 2017]的11个索引片段。
