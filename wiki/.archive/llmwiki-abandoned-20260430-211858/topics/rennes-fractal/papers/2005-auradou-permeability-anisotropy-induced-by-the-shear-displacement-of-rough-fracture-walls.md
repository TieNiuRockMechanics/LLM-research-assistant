---
type: "paper"
paper_id: "2005-auradou-permeability-anisotropy-induced-by-the-shear-displacement-of-rough-fracture-walls"
title: "Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls."
status: "draft"
source_pdf: "data/papers/2005 - Permeability anisotropy induced by the shear displacement of rough fracture walls.pdf"
citation: "Auradou, H., et al. \"Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls.\" *Water Resources Research*, vol. 41, 2005, W09423. doi:10.1029/2005WR003938."
indexed_texts: "13"
indexed_chars: "60819"
compiled_at: "2026-04-27T19:32:13"
---

# Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls.

## One-line Summary

本研究通过实验和数值模拟揭示，粗糙裂缝壁之间的剪切位移会产生孔径场各向异性，从而导致渗透率各向异性，最大渗透率方向垂直于剪切位移方向 [Auradou 2005, pp. 1-1, 6-6]。

## Research Question

剪切位移如何改变裂缝孔径场的统计特性，并进而引起渗透率在平行和垂直于剪切位移方向上的差异？具体地，研究者试图定量建立孔径涨落与渗透率各向异性的关系，并通过实验和数值模拟验证理论预测 [Auradou 2005, pp. 1-1, 6-6]。

## Study Area / Data

- **实验模型**：使用从实际岩石铸型得到的透明裂缝模型，裂缝壁具有自仿射粗糙表面，Hurst 指数 z = 0.75 ± 0.05 [Auradou 2005, pp. 2-3]。实验在固定平均孔径 a₀ = 1 mm 下进行，施加不同大小和方向的剪切位移（沿 x 或 y 方向），并确保壁面不接触以避免剪切诱导的扩张效应 [Auradou 2005, pp. 1-2]。
- **数值模型**：使用傅里叶合成方法生成自仿射表面，Hurst 指数设为 0.8，平均表面波动幅度（1 mm 距离上）设为 0.25 mm，平均孔径约 1 mm，以匹配实验条件 [Auradou 2005, pp. 6-7]。

## Methods

- **实验方法**：将染色流体从裂缝中心点径向注入以驱替透明流体，通过图像分析测量光强与局部孔径和浓度的关系（Beer-Lambert 关系），获取浓度分布图 [Auradou 2005, pp. 3-4]。利用侵入区的惯性张量特征值比 l₊/l₋ 确定渗透率主方向和各向异性程度，该比值在侵入区回旋半径 Rg > 30 mm 后趋于稳定 [Auradou 2005, pp. 4-5, 5-6]。渗透率比 k⊥/k∥ = (l₊/l₋)² [Auradou 2005, pp. 4-5]。
- **数值方法**：采用格子 Boltzmann 方法计算裂缝内速度场，该方法特别适合复杂几何中的流动计算 [Auradou 2005, pp. 6-7]。数值模拟的裂缝孔空间由自仿射表面与其平移副本之间的区域定义，剪切位移施加在 (x,y) 平面内，最大位移至首次出现接触点 [Auradou 2005, pp. 6-7]。

## Key Findings

1. **各向异性方向**：剪切位移存在时，染色流体侵入区呈现明显的各向异性，长轴（最大流速方向）垂直于剪切位移方向 [Auradou 2005, pp. 3-4]。
2. **渗透率比测量**：对于固定剪切位移方向，惯性张量特征值比 l₊/l₋ 在 Rg > 30 mm 后达到自相似稳定值，可用于表征渗透率各向异性。不同剪切位移方向导致不同的各向异性程度（例如沿 x 轴位移时 l₊/l₋ ≈ 1.05，沿 y 轴时 ≈ 1.15）[Auradou 2005, pp. 5-6]。
3. **孔径涨落与剪切位移的标度关系**：孔径方差 σₐ(u) = C u^z，其中 z = 0.75，与 Hurst 指数一致，表明剪切位移引入了与粗糙度标度一致的孔径涨落 [Auradou 2005, pp. 6-6]。
4. **相关长度各向异性**：孔径相关长度在剪切位移方向上更小，在垂直方向上更大，这导致沿大相关长度方向（垂直于位移）形成连续通道，增强该方向渗透率 [Auradou 2005, pp. 6-6]。
5. **理论预测**：简单模型预测，平行于剪切位移的渗透率随孔径方差增加而线性减小，垂直于剪切位移的渗透率则线性增加 [Auradou 2005, pp. 1-1]。

## Limitations

- 实验只能测定渗透率各向异性比，无法获得渗透率的绝对值 [Auradou 2005, pp. 1-2]。
- 实验中裂缝壁保持不接触，避免了剪切诱导的扩张效应，但实际裂缝可能发生接触并改变渗透率 [Auradou 2005, pp. 1-2]。
- 当粗糙度相对于平均孔径较大（例如接近接触时），润滑近似失效，需使用完整流动描述 [Auradou 2005, pp. 6-7]。
- 数值模拟采用生成的自仿射表面，与真实裂缝表面可能存在差异，且仅考虑了单裂缝情况。未从索引片段中确认扩展到裂缝网络的应用。

## Reusable Claims

- 剪切位移引入的孔径场各向异性使得渗透率呈现各向异性，最大渗透率方向总是垂直于剪切位移方向 [Auradou 2005, pp. 6-6]。
- 孔径涨落的方差与剪切位移大小满足幂律关系 σₐ(u) ∝ u^z，其中 z 为裂缝壁的 Hurst 指数 [Auradou 2005, pp. 6-6]。
- 在径向注入实验中，渗透率比 k⊥/k∥ 可通过侵入区惯性张量特征值比的平方获得：(l₊/l₋)² [Auradou 2005, pp. 4-5]。
- 同一裂缝中不同方向剪切位移可能产生不同程度的各向异性，但同一方向正反向位移结果相似 [Auradou 2005, pp. 5-6]。
- 孔径相关长度在剪切位移方向上减小，在垂直方向上增大，导致沿垂直方向形成优先流动通道 [Auradou 2005, pp. 6-6]。

## Candidate Concepts

- [[permeability anisotropy]]
- [[shear displacement]]
- [[rough fracture]]
- [[self-affine surface]]
- [[aperture field]]
- [[correlation length anisotropy]]
- [[Hurst exponent]]
- [[radial injection]]
- [[inertia tensor]]
- [[Beer-Lambert relation]]

## Candidate Methods

- [[radial injection experiment]]
- [[image analysis for aperture measurement]]
- [[lattice Boltzmann method]]
- [[Fourier synthesis method for self-affine surfaces]]
- [[lubrication approximation]]
- [[inertia tensor analysis for anisotropy quantification]]

## Open Questions

- 当剪切位移导致壁面接触时，接触区域的分布如何进一步影响渗透率各向异性？未从索引片段中确认。
- 在不同应力条件下（如法向应力变化），剪切位移引起的各向异性是否可逆或随时间演化？未从索引片段中确认。
- 如何将单裂缝的渗透率各向异性行为集成到裂缝网络模型中，以预测大尺度流动？未从索引片段中确认。
- 该研究的结论是否适用于其他岩石类型或具有不同粗糙度标度指数的裂缝？未从索引片段中确认。

## Source Coverage

本页基于以下片段撰写：[Auradou 2005, pp. 1-1], [Auradou 2005, pp. 1-2], [Auradou 2005, pp. 2-3], [Auradou 2005, pp. 3-4], [Auradou 2005, pp. 4-5], [Auradou 2005, pp. 5-6], [Auradou 2005, pp. 6-6], [Auradou 2005, pp. 6-7]。共 8 个索引片段。
