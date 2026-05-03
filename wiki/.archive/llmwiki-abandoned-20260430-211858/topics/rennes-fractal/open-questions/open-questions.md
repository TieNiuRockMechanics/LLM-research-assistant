---
type: "open-question"
status: "draft"
compiled_at: "2026-04-27T19:50:47"
title: "Open Questions"
---

# Open Questions

## 法向和剪切变形同时作用下的裂缝力学与水力行为如何耦合？

现场裂缝通常同时承受法向和剪切应力，但目前多数实验只研究单一变形模式，缺乏对耦合效应下渗透率演化规律的认识。

### Source Papers

- [1980-witherspoon-validity-of-cubic-law-for-fluid-flow-in-a-deformable-rock-fracture](../papers/1980-witherspoon-validity-of-cubic-law-for-fluid-flow-in-a-deformable-rock-fracture.md)

## 如何将二维DFN反演方法可靠地推广到三维真实地质环境？

大多数反演方法基于二维模型，但天然裂缝系统和工程应用是三维的，三维反演面临计算成本和几何复杂性的巨大挑战。

### Source Papers

- [2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h](../papers/2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h.md)
- [2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity](../papers/2023-jiang-fracture-network-characterization-in-reservoirs-by-joint-inversion-of-microseismicity.md)

## 裂缝尺寸与导水率之间真正的函数关系是什么？如何从现场数据约束？

当前模型采用不同的相关性（完全相关、半相关、不相关）导致流动预测差异显著，但缺乏可靠的现场数据来确定真实关系。

### Source Papers

- [2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations](../papers/2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations.md)

## 不同场地和岩性下，裂缝网络统计参数（分形维数D、幂律指数a）的通用性与控制因素是什么？

虽然许多网络显示相似标度行为，但参数的具体值变化很大，其物理控制因素（如应力历史、岩性、构造背景）尚待阐明。

### Source Papers

- [2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech](../papers/2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech.md)

## 当基质渗透率不可忽略时，裂缝网络的等效水力行为如何量化？

大多数DFN研究假设基质不渗透，但许多实际场地（如碳酸盐岩、风化岩石）基质具有显著渗透性，裂缝-基质相互作用会改变整体流动和传输。

### Source Papers

- [2024-r-mhild-hybrid-discrete-fracture-network-inversion-of-hydraulic-tomography-data-from-a-frac](../papers/2024-r-mhild-hybrid-discrete-fracture-network-inversion-of-hydraulic-tomography-data-from-a-frac.md)

## 如何将缝洞（vug）等非平面不连续体纳入DFN模型？

碳酸盐岩储层中常存在溶蚀孔洞，其形态和流动行为与平面裂缝差异大，现有DFN方法多局限于平面裂缝。

### Source Papers

- [2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v](../papers/2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v.md)

## 机器学习生成的DFN能否直接用于物理模拟，以及如何保证其地质力学一致性？

GAN等方法可快速生成视觉逼真的裂缝网络，但这些网络可能与应力-应变历史不一致，需要开发物理约束的生成模型。

### Source Papers

- [2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces](../papers/2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces.md)
- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)

## 不同时空尺度下热-水-力-化学（THMC）耦合过程的相互作用机制及实时预测方法？

地下工程涉及从分钟到千年的多过程耦合，现有模型缺乏高效预测工具，亟需发展机器学习代理模型加速模拟并量化不确定性。

### Source Papers

- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md)
