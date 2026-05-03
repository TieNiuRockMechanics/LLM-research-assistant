---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "直剪试验 (Direct Shear Test)"
aliases:
  - "direct shear test on fractures"
  - "直剪试验"
sources:
  - "2024-zhang-changes-in-shear-properties-of-granite-fractures-subjected-to-cyclic-heating-and-air"
  - "2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne"
---

# 直剪试验 (Direct Shear Test)

## Purpose

在恒定法向应力（CNL）或恒定法向刚度（CNS）条件下，对岩石结构面施加剪切力，获得峰值和残余抗剪强度、剪切刚度和剪胀特性。
## Aliases

- direct shear test on fractures
- 直剪试验
## Workflow

上下剪切盒分别固定含裂隙岩样，施加法向力并稳定后，以恒定速率施加剪切位移，同步记录剪切力和法向位移。
## Inputs

- 含结构面试样
- 直剪仪
## Outputs

- 剪应力-剪位移曲线
- 峰值剪切强度 τp
- 摩擦角 φ 和粘聚力 c
- 剪胀曲线
## Assumptions

- 破坏沿预设结构面
- 剪切盒刚性足够
## Strengths

- 直接获取剪切参数
## Limitations

- 剪切速率和法向应力水平影响结果
- 不能实时观察裂纹扩展
## Related Concepts

- joint-roughness-coefficient
- thermal-damage
## Source Papers

- [2024-zhang-changes-in-shear-properties-of-granite-fractures-subjected-to-cyclic-heating-and-air](../papers/2024-zhang-changes-in-shear-properties-of-granite-fractures-subjected-to-cyclic-heating-and-air.md)
- [2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne](../papers/2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne.md)
