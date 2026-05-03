---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "热损伤花岗岩的力学响应与跨尺度模拟"
sources:
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
  - "2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展"
  - "2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems"
---

# 热损伤花岗岩的力学响应与跨尺度模拟

## Central Question

从矿物热膨胀到宏观动态断裂，热损伤如何通过多尺度裂缝网络传递并控制岩石的强度、脆性和渗透性？
## Synthesis

基于PFC颗粒流模拟（Zhai 2025）识别的热裂纹三阶段演化，结合热冲击实验（Zhu 2025冷却对比）和文献荟萃（解经宇2025），一致表明高温和快速冷却导致微裂纹密度/分形维数上升、强度线性下降和渗透率数量级增加。PFC-FDEM跨尺度映射方法（Zhai 2025）将这些微观损伤定量桥接到动态断裂响应，揭示能量分配从弹性储存转向断裂耗散，并确认0.6倍剪切波速为多裂纹扩展临界速度。EGS储层改造（Lei 2026）则可利用这些力学规律，通过热刺激和循环冷却优化裂缝网络，但工程三难的权衡在热致裂场景下同样成立。
## Evidence Chain

- PFC模拟显示裂纹密度指数增长（Zhai 2025）
- 遇水/液氮冷却导致渗透率激增和强度锐减（Zhu 2025）
- 综述归一化强度拟合公式证实冷却介质影响（解经宇2025）
- PFC-FDEM映射实现微观-宏观应力响应（Zhai 2025）
- EGS需平衡连通性与地震风险（Lei 2026）
## Disagreements / Tensions

- 空气冷却在某些条件下可闭合天然裂缝、提高强度（Zhu 2025），与普遍强度劣化趋势有差异。
## Boundary Conditions

- 当前多维模拟限于二维和小尺寸岩样
- 全耦合热-力-化学作用未纳入
- 不同花岗岩矿物组成差异影响损伤阈值
## Writing Uses

- 可用于设计EGS储层的热冲击策略
- 为深部高地温工程提供强度预测公式
## Source Papers

- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
- [2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展](../papers/2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展.md)
- [2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems](../papers/2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems.md)
