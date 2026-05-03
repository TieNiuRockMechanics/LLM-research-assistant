---
type: "paper"
paper_id: "2018-lang-relationship-between-the-orientation-of-maximum-permeability-and-intermediate-principa"
title: "Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2018 - Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.pdf"
citation: "Lang, Philipp S., et al. \"Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.\" *Water Resources Research*, vol. 54, 2018, pp. 8734–8755. doi:10.1029/2018WR023189. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100524"
compiled_at: "2026-04-27T19:39:04"
---

# Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.

## One-line Summary

本研究通过接触力学数值模拟发现，在各向同性裂缝网络条件下，裂缝岩石的最大渗透率方向倾向于与中间主应力方向对齐，这一关系源于剪切滑移导致的渗透率各向异性。

## Research Question

研究问题为：裂缝岩石的宏观渗透率各向异性如何受中间主应力的影响？传统二维研究假设裂缝渗透率各向同性且忽略中间主应力，本研究旨在通过三维接触力学模型揭示裂缝滑移、应力场与渗透率方向的内在联系 [Lang 2018, pp. 1-2]。

## Study Area / Data

未从索引片段中确认具体实地研究区域。研究基于数值生成的岩石粗糙裂缝表面数据，并与已发表的实验数据（如 Watanabe et al., 2008; Nemoto et al., 2009）进行验证性比较 [Lang 2018, pp. 4-6, pp. 8-10]。使用的表面数据来自 Novaculite 岩石的测量迹线 [Lang 2018, pp. 4-5]。

## Methods

采用两尺度耦合的接触力学数值方法。在岩石尺度，将裂缝视为平面不连续面，使用离散裂缝模型（DFM）和有限元方法求解摩擦接触问题，计算剪切位移和法向应力，采用基于间隙的增强拉格朗日算法处理接触约束 [Lang 2018, pp. 7-8]。在单个裂缝尺度，为其构建粗糙表面模型，通过将两张错位表面在围压下弹性接触求解出机械开度，进而计算渗透率张量 [Lang 2018, pp. 8-10]。裂缝表面的粗糙度通过功率谱密度（PSD）分析进行随机生成，采用两种方法：Brown（1995）方法和 Candela 等（2009）方法 [Lang 2018, pp. 5-6]。渗透率通过有限体积法求解两套宏观压力边界条件获得，裂缝渗透率被表示为平行于和垂直于剪切位移方向的对角张量 [Lang 2018, pp. 6-7]。全宏观渗透率张量通过对 DFM 尺度流量进行压力-流速关系计算获得 [Lang 2018, pp. 2-4]。

## Key Findings

1. 在各向异性裂缝网络中，当裂缝网络为各向同性时，裂缝岩石的最大渗透率方向倾向于与中间主应力方向对齐 [Lang 2018, pp. 1-1]。
2. 该现象的原因：裂缝在最大和最小主应力平面内发生最显著的滑移，而单个裂缝的渗透率在垂直于滑移的方向最为显著 [Lang 2018, pp. 1-1]。
3. 最小渗透率方向倾向于与最小主应力方向一致 [Lang 2018, pp. 1-1]（未从索引片段中确认具体表述，仅从“最大”方向推断）。
4. 剪切位移导致裂缝两侧表面错位，形成各向异性开度场，渗透率在滑移垂直方向大于平行方向 [Lang 2018, pp. 6-7]。

## Limitations

未从索引片段中确认本研究的局限性。可能局限包括：假设材料为线弹性、各向同性、均质；未考虑化学、热效应或基质孔隙-裂缝耦合；模型仅针对各向同性裂缝网络得出上述结论。具体限制需查阅论文全文。

## Reusable Claims

- 在各向同性裂缝网络中，裂缝岩石的最大渗透率方向与中间主应力方向对齐 [Lang 2018, pp. 1-1]。
- 剪切位移方向控制单个裂缝的渗透率各向异性，垂直于位移方向的渗透率最大 [Lang 2018, pp. 1-1, pp. 6-7]。
- 裂缝的显著剪切滑移主要发生在最大和最小主应力平面内 [Lang 2018, pp. 1-1]。
- 所提出的两尺度耦合数值方法可计算任意裂缝网络的宏观渗透率张量，仅需摩擦系数作为唯一可调参数 [Lang 2018, pp. 2-4]。
- 粗糙裂缝表面的复合表面在低频（大波长）处呈现幂律谱，在剪切位移尺度以上表面相关性消失 [Lang 2018, pp. 4-5]。
- 弹性接触产生的接触点尺寸分布呈幂律分布，与直接观测一致 [Lang 2018, pp. 5-6]。
- 裂缝法向刚度主要受大波长粗糙度控制，可据此将 DFM 尺度与小尺度解耦 [Lang 2018, pp. 6-7]。

## Candidate Concepts

- [[fracture reservoir]]
- [[permeability anisotropy]]
- [[intermediate principal stress]]
- [[shear-induced transmissivity]]
- [[discrete fracture network (DFN)]]
- [[rough fracture surface]]
- [[composite surface]]
- [[power spectral density (PSD)]]
- [[Hurst exponent]]
- [[elastic contact mechanics]]
- [[upscaling permeability]]

## Candidate Methods

- [[contact mechanics-based numerical approach]]
- [[two-scale coupling method for fractured rocks]]
- [[finite element method for frictional contact]]
- [[finite volume method for single-fracture flow]]
- [[discrete fracture model (DFM) with rough surface submodel]]
- [[stochastic surface generation using power spectrum]]
- [[mismatched surface method for shear fractures]]
- [[augmented Lagrangian-Uzawa contact algorithm]]
- [[harmonic averaging of shear displacement and confining pressure]]
- [[quarter-point tetrahedral elements for crack tip]]

## Open Questions

未从索引片段中确认。可能的未解决问题包括：在不同裂缝渗透率各向异性强度下的方向关系敏感性；三维各向异性裂缝网络的验证；温度、化学作用及时间效应的影响；实验室尺度与现场尺度的外推有效性。

## Source Coverage

本页面主要基于论文摘要（pp. 1-1, 1-2）、方法部分（pp. 2-4, pp. 4-6, pp. 6-8, pp. 8-10）以及引言中对前人工作的评述。未覆盖论文的讨论、结论和附录部分。所有引用的页码均来自提供的索引片段。
