---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "多尺度离散裂隙网络建模"
aliases:
  - "multi-scale DFN modelling"
sources:
  - "2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model"
---

# 多尺度离散裂隙网络建模

## Purpose

针对潜山裂缝性储层裂缝发育的多尺度性，采用“确定性+随机”的分层次建模策略，将不同尺度、不同数据来源的裂缝信息整合到统一的离散裂缝网络模型中。
## Aliases

- multi-scale DFN modelling
## Workflow

利用地震相干体和蚂蚁追踪等属性，直接提取大中尺度裂缝的三维分布，形成确定性模型；从岩心和成像测井识别和拾取中小尺度裂缝的密度、产状和长度；对缺少成像测井的井，通过建立常规测井计算的裂缝孔隙度与 FMI 裂缝密度的经验关系推算裂缝密度；以地震属性体（如裂缝-断层距离）为约束，利用序贯高斯模拟建立裂缝密度三维模型；在该密度模型的约束下，运用随机方法模拟生成多组系的中小尺度 DFN。
## Inputs

- 三维地震数据
- 钻孔中断点数据
- 岩心、成像测井（FMI）和常规测井数据
## Outputs

- 整合了从地震到岩心多源信息的 DFN 模型
- 裂缝孔隙度和渗透率的粗化模型
## Assumptions

- 裂缝发育受断层控制，密度与断层距离负相关
- 中小尺寸裂缝的中心密度分布可由序贯高斯模拟近似
- 高角度构造裂缝的常规测井裂缝孔隙度与 FMI 裂缝强度存在正相关
## Strengths

- 充分利用了不同尺度地球物理和地质数据来协同约束模型
- 解决了无 FMI 井区裂缝密度测算的难题
## Limitations

- 地震资料品质不佳时裂缝确定性拾取不可靠
- 序贯高斯等随机算法不能模拟真实裂缝网络的非平稳性和层次相关性
- 粗化后丢失了大量离散裂缝的连通拓扑信息
## Related Concepts

- discrete-fracture-network
- fracture-reservoir
## Source Papers

- [2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model](../papers/2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model.md)
