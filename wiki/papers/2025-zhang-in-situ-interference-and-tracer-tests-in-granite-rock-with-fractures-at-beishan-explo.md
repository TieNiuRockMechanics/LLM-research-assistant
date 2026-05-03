---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo"
title: "In-Situ Interference and Tracer Tests in Granite Rock with Fractures at Beishan Exploration Tunnel, China."
status: "draft"
source_pdf: "data/papers/2025 - In-situ interference and tracer tests in granite rock with fractures at Beishan exploration tunnel, China.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhang, Jintong, et al. \"In-Situ Interference and Tracer Tests in Granite Rock with Fractures at Beishan Exploration Tunnel, China.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 192, 2025, article 106166, doi:10.1016/j.ijrmms.2025.106166."
indexed_texts: "14"
indexed_chars: "69450"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "66564"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.958445"
coverage_status: "full-index"
source_signature: "a198bd92fcc9d05d493065c9c4858352c07ecbc6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:13:33"
---

# In-Situ Interference and Tracer Tests in Granite Rock with Fractures at Beishan Exploration Tunnel, China.

## One-line Summary
本研究在中国北山勘探隧道进行了地质与水力学综合调查，通过岩心编录、钻孔声波电视（BHTV）、 Slug干扰试验、自然梯度示踪试验和偶极示踪试验，系统表征了花岗岩裂隙的水力传导系数、水力连通性、地下水流向及溶质运移参数，揭示了裂隙网络非均质性对优先流通道和弥散主导迁移的控制作用。

## Research Question
如何精确刻画高放废物处置库围岩（结晶花岗岩）中裂隙的水文地质特性，以评估放射性核素潜在迁移路径？

## Study Area / Data
- **地点**：中国甘肃省北山勘探隧道（BET），位于北山高放废物处置地下实验室阶段[Zhang 2025, pp. 2-3]。
- **岩性**：片麻状黑云母二长花岗岩与黑云母花岗闪长岩，低孔隙度，裂隙网络控制流体迁移[Zhang 2025, pp. 2-3]。
- **气候与水文**：半干旱气候，年均降水量55~73 mm，蒸发超过3000 mm，无常年地表水，地下水主要为基岩裂隙水[Zhang 2025, pp. 2-3]。
- **钻孔**：九个垂直钻孔（A1-3, A1-4, A2-1, A2-2, A2-3, A2-4, A2-5, A3-3, A3-4），直径70 mm，深度4~12 m，围绕一条可见透水性裂隙布置[Zhang 2025, pp. 3-4]。
- **裂隙数据**：岩心编录与BHTV识别出两套可见裂隙组；第一组倾角45.45°~77.84°，方位151.72°~177.18°；第二组倾角63.48°~71.77°，方位254.66°~294.33°[Zhang 2025, pp. 3-4]；钻孔A1-3, A2-4, A3-3无水力响应[Zhang 2025, pp. 4-5]。
- **试验类型与参数**：
  - Slug干扰试验：8个钻孔（A1-3, A1-4, A2-1, A2-3, A2-4, A2-5, A3-3, A3-4）；使用KGS模型估计水力传导系数[Zhang 2025, pp. 4-6]。
  - 天然梯度示踪试验：注入孔A2-3（2 L, 100 g/L NaCl），监测70天；注入孔A2-5（500 mL, 100 g/L NaCl），监测13天；测量TDS[Zhang 2025, pp. 5-6]。
  - 偶极示踪试验：10组正反向试验，A2-3为主孔与其他孔配对；注入500 mL, 100 g/L NaCl溶液，注/抽速率50 mL/min，持续约24小时[Zhang 2025, pp. 5-6]。

## Methods
1. **地质调查**：岩心编录与高分辨率BHTV成像，识别裂隙位置、产状、开度，选取开度>5 mm且与可见裂隙产状相近的裂隙作为潜在导水裂隙[Zhang 2025, pp. 3-4]。
2. **Slug干扰试验**：在源孔快速抽水（10–30 s）产生瞬时水位变化，在观测孔用CT2X传感器记录压力及TDS变化；利用KGS解析模型（无压含水层、部分贯穿井、侧向无限延伸）反演径向水力传导系数K[Zhang 2025, pp. 4-6]。
3. **水力连通系数（HCC）**：定义HCC为观测孔最大水位降深与抽水孔最大水位降深之比，并用累积HCC量化入流与出流连通性；HCC越接近1表示连通性越强[Zhang 2025, pp. 5-6]。
4. **天然梯度示踪试验**：在自然水力梯度下瞬时注入NaCl示踪剂，长期监测TDS浓度变化，推断主流向[Zhang 2025, pp. 5-6]。
5. **偶极强制梯度示踪试验**：在注水-抽水双井间进行脉冲注入NaCl溶液，监测抽水孔三个不同深度传感器的TDS变化，采用归一化质量通量（y_i = c_i M_0 / q_out）拟合解析模型[Zhang 2025, pp. 5, 8-9]。
6. **等效流动通道模型**：假设一维等效通道中移流-弥散为主，忽略基质扩散，单通道解析解（式2）及多通道叠加（式3）；反演参数包括等效通道长度X_i、达西速度u_i、纵向弥散度α_L和回收率R_Mi[Zhang 2025, pp. 9-10]。
7. **数据有效性**：用裂隙迂曲度（等效通道长度/直线距离）验证参数合理性，与文献推荐范围1.1–3.0比对[Zhang 2025, pp. 9-10]。

## Key Findings
- 两套可见裂隙组被识别，其中一组与隧道揭露裂隙相似[Zhang 2025, pp. 3-4]。
- 钻孔A1-3, A2-4, A3-3在Slug干扰试验中无水位响应，与其他钻孔无水力连通[Zhang 2025, pp. 4-5]。
- 水力传导系数估计为4.93E-08至2.30E-06 m/s（表3）[Zhang 2025, pp. 6]。
- 中心钻孔A2-3的总HCC值最高（3.60），表明其与周围钻孔整体连通性最强；HCC矩阵不对称，反映裂隙网络非均质和各向异性[Zhang 2025, pp. 6]。
- 天然梯度示踪证实地下水流向由A2-5流向A2-3再流向A2-1；另存在A2-5至A3-4的路径[Zhang 2025, pp. 6-7]。
- 偶极示踪资料拟合得出达西速度0.064–0.209 m/h，纵向弥散度0.083–0.365 m，回收率0.012–0.285（表4）[Zhang 2025, pp. 9]。
- 单通道裂隙（A2-3与A2-1、A2-2之间）迂曲度低于1.2，为优先流通道；双通道裂隙（A2-3与A2-5、A1-4、A3-4之间）至少有一通道迂曲度大于1.5，弥散主导迁移[Zhang 2025, pp. 9-10]。
- 纵向弥散度随流径长度增加而增大的趋势与已有研究一致[Zhang 2025, pp. 10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水力传导系数：A1-4 3.95E-07, A2-1 9.30E-08, A2-2 9.80E-08, A2-3 9.80E-08, A2-5 2.30E-06, A3-4 4.93E-08 m/s | [Zhang 2025, pp. 6, Table 3] | Slug干扰试验，KGS模型，无压含水层假设 | 钻孔A1-3、A2-4、A3-3无法计算参数 |
| HCC矩阵与累积值：A2-2和A2-3的总HCC均为3.60，最高；A2-5为0.77，最低；矩阵不对称 | [Zhang 2025, pp. 6, Fig. 6] | Slug干扰试验，以最大水位降深比计算HCC | 表明裂隙网络非均质、各向异性 |
| 天然梯度示踪：A2-3注入后A2-1 NaCl浓度由0.09升至1.11 g/L，A2-5和A3-4稳定；A2-5注入后A2-3升至2.53 g/L，A3-4升至3.13 g/L | [Zhang 2025, pp. 6-7, Fig. 7] | 天然水力梯度，NaCl示踪，监测TDS | 推断路径A2-5→A2-3→A2-1和A2-5→A3-4 |
| 偶极示踪拟合参数：达西速度0.064–0.209 m/h，纵向弥散度0.083–0.365 m，回收率0.012–0.285，R²>0.85 | [Zhang 2025, pp. 9, Table 4] | 强制梯度，脉冲注入，等效流动通道模型反演 | 单通道裂隙达西速度较高；双通道裂隙弥散度范围更广 |
| 裂隙迂曲度：单通道<1.2，双通道至少有一条>1.5，范围1.1–2.2 | [Zhang 2025, pp. 9-10, Fig. 10] | 等效通道长度/直线距离，对比文献推荐范围1.1–3.0 | 低迂曲度对应优先流，高迂曲度对应弥散主导 |

## Limitations
- 仅分析了单裂隙和双裂隙系统的水力、输运特性，对三个或更多共存裂隙的复杂裂隙带参数估计不足[Zhang 2025, pp. 10]。
- 使用的NaCl迹剂为保守性（非吸附），不能直接表征吸附性核素的迁移行为[Zhang 2025, pp. 10]。
- 研究中未对钻孔进行分段封隔，可能同时与多条裂隙连通，导致部分参数混合[Zhang 2025, pp. 10]。
- 自然梯度示踪试验中传感器故障导致A1-4数据缺失[Zhang 2025, pp. 6]；部分偶极试验TDS动态范围偏窄（2500~2800 mg/L），可能因强优势通道导致浓度波动受限[Zhang 2025, pp. 8]。
- 天然流场对正反向偶极试验结果产生显著影响，流径差异可能导致回收率与峰值不通[Zhang 2025, pp. 8-9]。

## Assumptions / Conditions
- Slug干扰试验采用无压含水层、侧向无限延伸、部分贯穿井的KGS模型假定[Zhang 2025, pp. 4-5]。
- 等效流动通道模型中假设一维通道内移流与流体动力弥散为主，忽略基质扩散（因试验持续短）[Zhang 2025, pp. 9]。
- 单通道或多通道均假设各通道内流速和弥散系数恒定[Zhang 2025, pp. 9]。
- 注入NaCl溶液被视为保守示踪剂，无明显吸附、衰减或化学作用[Zhang 2025, pp. 5]。
- 自然梯度试验中认为“盘状”源随地下水流迁移，且天然流动方向稳定[Zhang 2025, pp. 5]。
- 偶极试验中注/抽速率恒定且相等（50 mL/min），忽略井筒储存影响[Zhang 2025, pp. 5-6]。

## Key Variables / Parameters
- 水力传导系数 K（m/s）[Zhang 2025, Table 3]
- 水力连通系数 HCC（无量纲）及其累积入流、出流值[Zhang 2025, Fig. 6]
- 天然梯度示踪中的NaCl浓度变化（TDS，mg/L或g/L）[Zhang 2025, Fig. 7]
- 归一化质量通量 y_i（1/h）与 residence time[Zhang 2025, Eq. 1]
- 等效通道长度 X_i（m）[Zhang 2025, Table 4]
- 达西速度 u（m/h）[Zhang 2025, Table 4]
- 纵向弥散度 α_L（m）[Zhang 2025, Table 4]
- 回收率 R_M（%）[Zhang 2025, Table 4]
- 裂隙迂曲度（等效通道长度/直线距离）[Zhang 2025, Fig. 10]
- 裂隙产状（倾角、方位）、开度（mm）[Zhang 2025, Table 1]

## Reusable Claims
- 在低渗透花岗岩中，通过Slug干扰试验与提出的HCC可量化钻孔间水力连通性的空间非均质和各向异性（条件：多个观测井同时监测瞬时水位变化）。[Zhang 2025, pp. 5-6]
- 分段式天然梯度示踪策略（先中心孔后外围孔）能降低钻孔布置偏差对试验结果的影响，准确刻画自然流方向（条件：已知初始水力连通性分布）。[Zhang 2025, pp. 6-7]
- 归一化质量通量耦合等效流动通道模型反演可有效获得裂隙岩体中单/双通道的达西速度、弥散度等迁移参数，且模型拟合优度R²>0.85（条件：短时强制梯度、保守示踪剂、忽略基质扩散）。[Zhang 2025, pp. 9]
- 裂隙迂曲度低于1.5指示单通道优先流、高于1.5则提示多通道弥散主导运移，可作为快速评判迁移通道类型的指标（条件：已知等效通道长度与井间距）。[Zhang 2025, pp. 9-10]
- 纵向弥散度随流径长度增加而增大的标度律在花岗岩裂隙中也适用，与多孔介质中的规律一致。[Zhang 2025, pp. 10, Fig. 11]

## Candidate Concepts
- [[slug interference test]]
- [[hydraulic connectivity coefficient (HCC)]]
- [[natural gradient tracer test]]
- [[dipole tracer test]]
- [[equivalent flow channel model]]
- [[normalized mass flux]]
- [[fracture tortuosity]]
- [[preferential flow pathway]]
- [[dispersivity-scale relationship]]
- [[fracture hydraulic conductivity]]

## Candidate Methods
- [[core logging and BHTV fracture identification]]
- [[KGS analytical model for slug test]]
- [[slug interference test with multiple observation wells]]
- [[natural gradient tracer injection and TDS monitoring]]
- [[pulse injection dipole tracer test]]
- [[analytical inversion of BTC using equivalent channel model]]
- [[HCC matrix analysis for inter-well connectivity]]

## Connections To Other Work
- 本研究的裂隙迂曲度范围（1.1–2.2）与文献推荐的裂隙岩石迂曲度1.1–3.0一致[Zhang 2025, pp. 9-10, citing Hakami & Larsson 1996; Pardo-Iguzquiza et al. 2011]。
- 观测到的纵向弥散度随尺度增大趋势与Gelhar et al. (1992)及Stichler et al. (2008)的汇总数据吻合[Zhang 2025, pp. 10, Fig. 11]。
- 偶极示踪试验方法及等效通道模型在之前的多处核废料研究场地（如瑞典Stripa、Aspö，瑞士Grimsel，日本釜石矿山、瑞浪URL）有应用[Zhang 2025, pp. 2]。
- 天然梯度示踪试验对钻孔布置的敏感性在其他研究（如Goeppert & Goldscheider 2021; Weatherill et al. 2006）中亦有讨论[Zhang 2025, pp. 2]。

## Open Questions
- 如何将分段封隔技术引入Slug试验和示踪试验，以更精确地分离多条交叉裂隙的水力响应？[Zhang 2025, pp. 10]
- 吸附性核素（如铯、锶）在类似花岗岩裂隙中的迁移参数如何获得？[Zhang 2025, pp. 10]
- 多分支复杂裂隙网络（三个及以上共存通道）的等效水力-输运参数反演方法需要进一步发展。[Zhang 2025, pp. 10]
- 天然水流场与强制梯度场耦合作用下，正反向示踪试验回收率差异的机理需借助更精细的三维裂隙网络数值模型澄清。[Zhang 2025, pp. 8-9]
- 裂隙迂曲度与弥散度的定量本构关系是否可推广至更大尺度？[Zhang 2025, pp. 9-10]

## Source Coverage
本页面完全基于提供的14个索引片段（非空源块）编撰。所有非空索引片段均已处理，源块编译覆盖率（按块数）为 1.0，按字符数覆盖率为 0.9584。片段来自 Zhang et al. (2025) 正文1-12页，源文件指纹 a198bd92fcc9d05d493065c9c4858352c07ecbc6。所有事实性陈述均锚定于上述片段内标注的页码范围，无外部发明。
