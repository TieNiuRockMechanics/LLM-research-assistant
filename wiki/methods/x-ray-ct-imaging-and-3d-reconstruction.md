---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "X 射线 CT 成像与三维重构"
aliases:
  - "X-ray CT"
  - "micro-CT"
  - "industrial CT"
  - "3D computed tomography"
  - "实时CT"
  - "CT scanning"
  - "CT-3D reconstruction"
sources:
  - "2019-isaka-quantification-of-thermally-induced-microcracks-in-granite-using-x-ray-ct-imaging-and"
  - "2023-li-structural-properties-and-failure-characteristics-of-granite-after-thermal-treatment-and"
  - "2023-fan-stress-water-coupling-effects-on-failure-of-sandstone-based-on-real-time-ct-technology"
  - "2023-fan-a-real-time-visual-investigation-on-microscopic-progressive-fatigue-deterioration-of-gr"
  - "2025-he-spatial-variability-and-quantitative-characterization-of-thermal-shock-damage-in-sandsto"
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
  - "2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using"
---

# X 射线 CT 成像与三维重构

## Purpose

无损获取岩石内部三维结构，用于可视化、量化孔隙、裂缝网络及其连通性。可在加载过程中实时扫描（原位加载 CT）。
## Aliases

- X-ray CT
- micro-CT
- industrial CT
- 3D computed tomography
- 实时CT
- CT scanning
- CT-3D reconstruction
## Workflow

将试样置于旋转台上进行 X 射线扫描；采集投影图像并重构为灰度体数据；经滤波、阈值分割、三维渲染，提取孔隙/裂缝网络；可计算孔隙度、裂缝密度、分形维数等；实时加载 CT 需在专用加载台上进行。
## Inputs

- 岩石试样
- CT 扫描系统
- 可选：原位加载装置
## Outputs

- 三维灰度图像
- 分割后孔隙-裂隙网络
- 孔隙度
- 裂缝宽度
- 连通性
## Assumptions

- X 射线衰减与密度相关
- 阈值分割能准确区分固相与缺陷
## Strengths

- 高分辨率三维定量可视化
## Limitations

- 分辨率与样品尺寸矛盾
- 高密度矿物易产生伪影
- 实时扫描时间分辨率较低
## Related Concepts

- porosity
- mesoscopic-damage
- pore-structure-evolution
## Source Papers

- [2019-isaka-quantification-of-thermally-induced-microcracks-in-granite-using-x-ray-ct-imaging-and](../papers/2019-isaka-quantification-of-thermally-induced-microcracks-in-granite-using-x-ray-ct-imaging-and.md)
- [2023-li-structural-properties-and-failure-characteristics-of-granite-after-thermal-treatment-and](../papers/2023-li-structural-properties-and-failure-characteristics-of-granite-after-thermal-treatment-and.md)
- [2023-fan-stress-water-coupling-effects-on-failure-of-sandstone-based-on-real-time-ct-technology](../papers/2023-fan-stress-water-coupling-effects-on-failure-of-sandstone-based-on-real-time-ct-technology.md)
- [2023-fan-a-real-time-visual-investigation-on-microscopic-progressive-fatigue-deterioration-of-gr](../papers/2023-fan-a-real-time-visual-investigation-on-microscopic-progressive-fatigue-deterioration-of-gr.md)
- [2025-he-spatial-variability-and-quantitative-characterization-of-thermal-shock-damage-in-sandsto](../papers/2025-he-spatial-variability-and-quantitative-characterization-of-thermal-shock-damage-in-sandsto.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
- [2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using](../papers/2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using.md)
