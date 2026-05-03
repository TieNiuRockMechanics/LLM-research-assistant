---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-lang-relationship-between-the-orientation-of-maximum-permeability-and-intermediate-principa"
title: "Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2018 - Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.pdf"
collections:
citation: "Lang, Philipp S., et al. \"Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.\" *Water Resources Research*, vol. 54, 2018, pp. 8734-8755. doi:10.1029/2018WR023189. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100524"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:19:11"
---

# Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.

## One-line Summary
本论文通过多尺度接触力学数值模拟，揭示在各向同性裂隙网络中，裂隙岩体的最大渗透率方向倾向于与中间主应力方向一致，这一现象源于剪切引起的单个裂隙导水率各向异性 [Lang 2018, pp. 1-1]。

## Research Question
裂隙岩体的宏观渗透率各向异性如何受远场三轴应力状态（尤其是中间主应力）和裂隙面剪切引起的导水率各向异性共同控制？ [Lang 2018, pp. 1-1, 1-2]

## Study Area / Data
研究基于 *数值模拟*，未使用特定野外研究区。  
- **裂隙网络**：生成具有各向同性分布的离散裂隙网络。  
- **单裂隙验证数据**：使用 Watanabe et al. (2008) 发表的实验数据对单一剪切裂隙的渗透率模型进行率定 [Lang 2018, pp. 8-10]。  
- **岩石材料参数**：未从索引片段中确认具体数值；摩擦系数为唯一可调整参数 [Lang 2018, pp. 2-4]。

## Methods
- **多尺度耦合框架**：构建了一个包含宏观离散裂隙网（DFM）与小尺度粗糙表面接触的“降尺度-升尺度”方法 [Lang 2018, pp. 2-4]。  
  - **DFM 尺度**：使用基于有限元的接触力学方法，求解三轴远场应力条件下裂隙网络的变形与摩擦滑移。材料假定为线弹性、均质、各向同性；裂隙面的法向与切向接触采用增广拉格朗日‑Uzawa 算法 [Lang 2018, pp. 7-8]。  
  - **单裂隙小尺度**：对网络中的每一条裂隙，根据其平均剪切位移 \( \bar{\delta}_T \) 和平均限定压力 \( \bar{p} \)，随机生成一对具有幂率谱粗糙度及小波长不匹配度的表面，计算弹性-理想塑性（无摩擦）接触下的 aperture 场，进而通过求解二维达西流得到裂隙导水率张量 \( \mathbf{K} = \mathrm{diag}(K_\parallel, K_\perp) \)，其中 \( K_\parallel \) 和 \( K_\perp \) 分别为平行与垂直于剪切位移方向的导水率 [Lang 2018, pp. 5-6, 6-7, 8-10]。  
- **渗透率升尺度**：将小尺度获得的裂隙导水率张量反馈到 DFM 中，在立方体域上求解全局流体压力场，最终计算宏观渗透率张量 [Lang 2018, pp. 8-10]。  
- **关键假设的裂隙开‑闭过程**：依次施加初始流体压力使裂隙打开，再卸载压力并施加远场三轴应力使裂隙闭合并发生滑移，以此模拟一种历史过程 [Lang 2018, pp. 7-8]。

## Key Findings
- **最大渗透率方向对齐于中间主应力**：在各向同性裂隙网络的数值试验中，宏观最大渗透率的方向与中间主应力（\( S_2 \)）的方向趋于一致 [Lang 2018, pp. 1-1]。  
- **力学机制**：裂隙面在最大主应力 \( S_1 \) 和最小主应力 \( S_3 \) 所构成的平面内滑动最为显著；单个粗糙裂隙在剪切位移后，其导水率在垂直于滑动方向上最大，从而在宏观上使得该方向的渗透率增强 [Lang 2018, pp. 1-1]。  
- **与前人二维研究的区别**：仅考虑各向同性裂隙导水率的二维模型通常得到最大渗透率对齐于最大主应力，而本三维模型揭示了中间主应力的关键作用 [Lang 2018, pp. 1-2]。  
- **模型验证**：单裂隙数值模型能够再现 Watanabe et al. (2008) 实验中渗透率随剪切位移的变化趋势 [Lang 2018, pp. 8-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 宏观最大渗透率方向与中间主应力方向对齐 | [Lang 2018, pp. 1-1] | 各向同性裂隙网络，三轴不等远场应力 | 三维计算，考虑剪切诱导裂隙导水率各向异性 |
| 单个剪切裂隙的导水率在垂直于剪切位移方向上最大 | [Lang 2018, pp. 1-1, 8-10] | 基于粗糙面接触与达西流模拟 | 仅利用摩擦系数一个可调参数 |
| 二维模型若假设裂隙导水率各向同性，则最大渗透率方向倾向于与最大主应力一致 | [Lang 2018, pp. 1-2] | 前人研究总结 | 与本文结果形成对比 |

## Limitations
- 索引片段中未给出完整的敏感性分析或参数不确定性讨论；具体适用范围（如应力比范围）未从索引片段中确认。  
- 岩石材料假定为线弹性、均质、各向同性，未考虑节理岩体的非均质与非线性（如扩容角演化、塑性屈服） [Lang 2018, pp. 7-8]。  
- 裂隙面粗糙度通过统计生成，mismatch 模型仅包含单一特征波长，未涉及化学作用、矿物充填或表面磨损的演化 [Lang 2018, pp. 4-6]。  
- 裂隙网络为各向同性生成，未覆盖各向异性网络或真实野外构造模式。

## Assumptions / Conditions
- 裂隙网络几何形态为各向同性分布 [Lang 2018, pp. 1-1]。  
- 基岩具有渗透性，并同时考虑基质与裂隙内的流动 [Lang 2018, pp. 2-4]。  
- 岩石材料为线弹性、均质、各向同性；摩擦行为遵循库仑摩擦定律，且摩擦系数为唯一可调参数 [Lang 2018, pp. 7-8] 及 [Lang 2018, pp. 2-4]。  
- 裂隙面的粗糙度谱服从径向平均的幂率分布，小波长范围内的不匹配度由 mismatch wavenumber \( q_m \) 控制，Hurst 指数取 0.8 [Lang 2018, pp. 4-5]。  
- 单裂隙接触问题简化为刚性复合表面与弹性半空间的等效问题，仅考虑法向弹性变形，忽略摩擦对接触面积的修正 [Lang 2018, pp. 5-6]。  
- 流体为单相、恒黏度牛顿流体，流动服从达西定律 [Lang 2018, pp. 6-7]。  
- 采用一种假设的“打开-闭合”加载历史，以模拟自然裂隙可能经历的初始流体张开与后期构造剪切过程 [Lang 2018, pp. 7-8]。

## Key Variables / Parameters
- **远场主应力**：\( S_1 \) (最大)、\( S_2 \) (中间)、\( S_3 \) (最小) [Lang 2018, pp. 1-1, 7-8]。  
- **裂隙剪切位移**：\( \delta_T \)，影响导水率各向异性 [Lang 2018, pp. 8-10]。  
- **单裂隙导水率张量**：\( K_\parallel \)（平行剪切方向）、\( K_\perp \)（垂直剪切方向） [Lang 2018, pp. 6-7, 8-10]。  
- **限定压力**：\( \bar{p} \)（法向压缩应力），控制裂隙闭合程度 [Lang 2018, pp. 8-10]。  
- **粗糙度参数**：Hurst 指数 \( H = 0.8 \)，mismatch wavenumber \( q_m \) [Lang 2018, pp. 4-5]。  
- **摩擦系数**：唯一可调整模型参数 [Lang 2018, pp. 2-4]。  
- **平行板等效水力学隙宽**：\( a_h \)，通过 \( K = a_h^2/12 \) 定义 [Lang 2018, pp. 6-7]。

## Reusable Claims
1. **中间主应力对齐准则**：对于具有统计各向同性的裂隙网络，宏观最大渗透率的方向与中间主应力方向对齐。此结论适用于三轴不等应力下、裂隙导水率由粗糙面剪切引起的各向异性所主导的岩体。[Lang 2018, pp. 1-1]（条件：裂隙网络各向同性，岩石线弹性，远场三轴应力；证据：三维数值模拟）  
2. **单裂隙剪切导水率各向异性**：粗糙裂隙面经历剪切位移后，导水率在垂直于剪切滑动方向上最大，这是应力诱导渗透率各向异性的基本单元机制。[Lang 2018, pp. 1-1, 8-10]（条件：法向压缩下粗糙面弹性接触，不考虑化学作用；证据：模型复现实测单裂隙渗透率数据）  
3. **多尺度耦合方法**：采用 DFM 与单裂隙粗糙面接触模型的双向耦合架构，可仅用摩擦系数一个自由参数重现实验室观测的剪切裂隙渗透率演化，并可推广至任意裂隙网络计算全场渗透率张量。[Lang 2018, pp. 2-4, 8-10]（条件：小尺度模型需事先获得裂隙尺寸与平均剪切/压缩参数；证据：与 Watanabe 等实验对比）  
4. **与二维研究的本质区别**：二维应力‑渗透率模型若忽略裂隙面剪切引起的各向异性导水率，会将最大渗透率方向错误地归结于最大主应力方向，掩盖了中间主应力的作用。[Lang 2018, pp. 1-2]（条件：裂隙导水率被假定为各向同性）

## Candidate Concepts
- [[fracture permeability anisotropy]]
- [[intermediate principal stress]]
- [[shear-induced dilation]]
- [[roughness mismatch]]
- [[contact mechanics]]
- [[principal stress rotation]]
- [[fracture network isotropy]]
- [[hydraulic aperture upscaling]]
- [[friction coefficient in fractures]]
- [[stress-dependent permeability]]

## Candidate Methods
- [[discrete fracture model (DFM)]]
- [[finite element contact mechanics]]
- [[augmented Lagrangian method]]
- [[power spectrum surface generation]]
- [[two-scale coupling approach]]
- [[Darcy flow simulation on rough fractures]]
- [[permeability tensorial upscaling]]
- [[elastoplastic contact model]]
- [[stochastic composite surface]]

## Connections To Other Work
- **前人二维应力‑渗透率研究**：Baghbanan & Jing (2008)、Jing et al. (2013) 等发现二维模型中最大渗透率方向平行于最大主应力，但其假设单裂隙导水率各向同性，未考虑中间主应力 [Lang 2018, pp. 1-2]。本文通过三维多尺度模型揭示了中间主应力的重要性，修正了该认识。  
- **剪切渗透率经验关系**：Barton et al. (1985) 等建立的裂隙水力学隙宽与剪切位移、法向应力的经验公式为本模型的物理机制提供定性对应 [Lang 2018, pp. 1-2]。  
- **裂隙‑断层系统渗透率各向异性**：Sibson (1996) 指出裂隙‑断层交汇方向可形成高渗透通道，与本研究的剪切导水率各向异性在机理上具有相似性 [Lang 2018, pp. 1-2]。  
- **粗糙面接触与流动模型**：Lang et al. (2016) 等开发的粗糙面生成与弹性接触方法构成本文小尺度模型的基础 [Lang 2018, pp. 5-6]。  
- 以上连接均基于索引片段中已确认的引用，未添加片段外的其他文献。

## Open Questions
- 当裂隙网络呈现强烈优势方向时，中间主应力对齐准则是否仍然成立？未从索引片段中确认。  
- 非各向同性、受构造历史影响的裂隙岩体（如存在断层损伤带）的渗透率‑应力关系如何演变？  
- 岩石非线性变形（如塑性、裂隙扩展）、多相流效应对“最大渗透率‑中间主应力”关系的影响尚待研究。  
- 在更大范围和现场应力实测数据下模型的普适性如何？未从索引片段中确认。

## Source Coverage
本页面依据论文的 **21个索引片段** 编写，这些片段集中覆盖了论文的 **摘要、引言、方法（岩石物理模型、数值实现）及单裂隙模型验证** 等部分（对应原文 pp. 1‑10 前后）。  
- **已覆盖**：研究动机、前人对比、多尺度耦合方法的理论与算法细节、关键假设、主要结论的定性描述。  
- **可能缺失**：详细的结果与参数敏感性分析（如不同应力比、裂隙密度下的渗透率张量变化）、完整的讨论、与更多实验数据的对比以及结论的定量表述。文中凡未能在索引片段中直接确认的信息均已标注。
