---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "X 射线 CT 图像中的射线束硬化校正及其在多孔介质中的应用"
sources:
  - "2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph"
  - "2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma"
---

# X 射线 CT 图像中的射线束硬化校正及其在多孔介质中的应用

## Central Question

如何有效地识别和校正高密度、非均质地质材料 CT 图像中的射线束硬化伪影，并将校正后的图像用于更准确的矿物相分割和裂隙参数提取？
## Synthesis

在岩石物理和构造地质研究中，微米/纳米 CT 是关键技术，但多色 X 射线导致的射线束硬化伪影（图像中心区域变暗的“杯状”伪影）会严重干扰对矿物相的密度判识和图像分割。对圆柱形岩心的后重建校正证明 BHA 是径向对称的函数。对简单圆柱体，可利用单相材料的径向衰减曲线，通过指数拟合（μ = μ0 e^(-k√(R²-r²))）构建仿真图像，然后从原图中减去，实现分割与校正的同步化。对于更复杂的或非柱状的地质样品，专家可以导向的迭代样条优化法（Ketcham 与 Hanna, 2014），它可以寻找能最小化选定 ROI 内 CT 数方差的最优样条校正函数，无需预知 X 射线能谱。这两种途径在应对高原子序数矿物、孔洞或多物相复杂样品时各有利弊。
## Evidence Chain

- Jovanović 等人（2013）验证了在圆柱形地质岩心（蒸发岩、花岗岩）中，BHA 遵循径向函数，并展示了基于差值图像的逐相分割法（radial-bha-correction）。
- Ketcham 与 Hanna（2014）证明了基于样条函数和专家定义 ROI 的迭代优化法在高度非均质且几何不规则的样品（如沥青混凝土、生物化石）中也能有效校正 BHA 并限制次级伪影（spline-based-bh-correction）。
## Disagreements / Tensions

- 哪种是最佳的目标函数？Ketcham 与 Hanna (2014) 通过铜立方体实验发现，仅用固相 ROI 优化可以使内部均匀但边缘感观变差；而联合空气和固相 ROI（双物质）优化可以改善几何边界（如边角更直）但却使内部精度下降。这意味着没有一种通用的“最佳”校正函数，校正的效果取决于用户的使用目的（密度保真度 vs 尺寸测量精度）。
## Boundary Conditions

- 两种方法都假设主要伪影来自于射线束硬化，并对散射、环状伪影等其他噪声非常敏感。
- Jovanović 等人的径向函数法要求试样是精确的垂直圆柱体，而 Ketcham 与 Hanna 的方法需要用户有丰富经验选取不受其它伪影干扰的 ROI。
## Writing Uses

- 在数字岩石物理或 CT 图像处理的方法论章节中，结合用户目的讨论 BHA 的影响及现有校正方案的局限性。
- 为其他研究者提供在缺乏光谱信息的台式 CT 设备上如何做定量分割的参考操作流程。
## Source Papers

- [2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph](../papers/2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph.md)
- [2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma](../papers/2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma.md)
