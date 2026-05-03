---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "有限元法 (Finite Element Method, FEM)"
aliases:
  - "FEM"
  - "有限单元法"
sources:
  - "2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid"
  - "2022-xiong-a-three-dimensional-coupled-thermo-hydro-model-for-geothermal-development-in-discrete"
  - "2021-zhao-experimental-study-on-the-physico-mechanical-properties-and-temperature-field-evolutio"
---

# 有限元法 (Finite Element Method, FEM)

## Purpose

求解固体力学、热传导、流体流动等偏微分方程的通用数值方法，广泛应用于岩石力学宏观变形与耦合过程模拟。
## Aliases

- FEM
- 有限单元法
## Workflow

将连续求解域离散为有限个单元，通过形函数插值，建立代数方程组求解。常用于 THM 耦合、等效连续介质模型等。
## Inputs

- 几何模型
- 材料本构模型及参数
- 边界和初始条件
## Outputs

- 应力场、位移场
- 温度场、孔隙压力场
- 塑性区分布
## Assumptions

- 材料通常假设为连续等效介质
## Strengths

- 计算精度高
- 适合求解连续介质耦合问题
## Limitations

- 模拟大变形或离散裂纹扩展需要特殊处理（XFEM、损伤力学、重剖分）
## Related Concepts

- equivalent-porous-medium
## Source Papers

- [2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid](../papers/2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid.md)
- [2022-xiong-a-three-dimensional-coupled-thermo-hydro-model-for-geothermal-development-in-discrete](../papers/2022-xiong-a-three-dimensional-coupled-thermo-hydro-model-for-geothermal-development-in-discrete.md)
- [2021-zhao-experimental-study-on-the-physico-mechanical-properties-and-temperature-field-evolutio](../papers/2021-zhao-experimental-study-on-the-physico-mechanical-properties-and-temperature-field-evolutio.md)
