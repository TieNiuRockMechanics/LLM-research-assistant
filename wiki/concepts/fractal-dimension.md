---
type: "concept"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "分形维数"
aliases:
  - "fractal dimension"
  - "D"
  - "D0"
  - "Dc"
  - "D2"
  - "Db"
  - "Dt"
  - "D_3D"
  - "分形维数"
  - "Fractal Dimension"
  - "盒计数维数"
  - "分形拓扑维数"
sources:
  - "1987-hirata-fractal-structure-of-spatial-distribution-of-microfracturing-in-rock"
  - "1990-letters-to-nature-nature-letters-to-nature"
  - "1992-davy-experimental-discovery-of-scaling-laws-relating-fractal-dimensions-and-the-length-dist"
  - "1995-cowie-multifractal-scaling-properties-of-a-growing-fault-population"
  - "1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks"
  - "2001-bonnet-scaling-of-fracture-systems-in-geological-media"
  - "2002-bour-a-statistical-scaling-model-for-fracture-network-geometry-with-validation-on-a-multisc"
  - "2003-darcel-stereological-analysis-of-fractal-fracture-networks"
  - "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
  - "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
  - "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
  - "2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces"
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
  - "2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering"
  - "2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia"
  - "2014-miao-a-fractal-analysis-of-permeability-for-fractured-rocks"
  - "2015-zhao-three-dimensional-fractal-distribution-of-the-number-of-rock-mass-fracture-surfaces-an"
  - "2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac"
  - "2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones"
  - "2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin"
  - "2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b"
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
  - "2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture"
---

# 分形维数

## Definition

描述裂隙网络空间分布、长度分布或表面粗糙度自相似性的标度指数。常用盒计数维数 D0、关联维数 D2、分形拓扑维数 Dt 等，值越高表示填充越密或形态越复杂。
## Aliases

- fractal dimension
- D
- D0
- Dc
- D2
- Db
- Dt
- D_3D
- 分形维数
- Fractal Dimension
- 盒计数维数
- 分形拓扑维数
## Boundary

仅在有限的无标度区间内有效；不同计算方法（盒计数、关联积分等）结果可能不同；实际裂隙系统可能存在特征尺度使得分形假设不成立。
## Related Methods

- box-counting-method
- correlation-integral
- divider-method
- updated-h-l-method
- two-point-correlation-function
- lacunarity-analysis
- normalized-correlation-integral-method
- fractal-per-model
- fractal-topography-modeling
## Related Claims

- fracture-length-power-law
- fractal-distribution-of-fractures
- DL-equals-DS-minus-1
- fractal-length-distribution-satisfied
- scaling-regimes-common
- fracture-networks-in-deep-boreholes-exhibit-fractal-correlation-dimension-0-8-0-9
- fractal-dimension-uniqueness
- thermal-crack-fractal-dimension-cooling-rate
- mining-crack-fractal-dimension-saturation
- fractal-dimension-decreases-with-thermal-damage
- fractal-dimension-links-to-permeability
## Source Papers

- [1987-hirata-fractal-structure-of-spatial-distribution-of-microfracturing-in-rock](../papers/1987-hirata-fractal-structure-of-spatial-distribution-of-microfracturing-in-rock.md)
- [1990-letters-to-nature-nature-letters-to-nature](../papers/1990-letters-to-nature-nature-letters-to-nature.md)
- [1992-davy-experimental-discovery-of-scaling-laws-relating-fractal-dimensions-and-the-length-dist](../papers/1992-davy-experimental-discovery-of-scaling-laws-relating-fractal-dimensions-and-the-length-dist.md)
- [1995-cowie-multifractal-scaling-properties-of-a-growing-fault-population](../papers/1995-cowie-multifractal-scaling-properties-of-a-growing-fault-population.md)
- [1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks](../papers/1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks.md)
- [2001-bonnet-scaling-of-fracture-systems-in-geological-media](../papers/2001-bonnet-scaling-of-fracture-systems-in-geological-media.md)
- [2002-bour-a-statistical-scaling-model-for-fracture-network-geometry-with-validation-on-a-multisc](../papers/2002-bour-a-statistical-scaling-model-for-fracture-network-geometry-with-validation-on-a-multisc.md)
- [2003-darcel-stereological-analysis-of-fractal-fracture-networks](../papers/2003-darcel-stereological-analysis-of-fractal-fracture-networks.md)
- [2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc](../papers/2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc.md)
- [2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to](../papers/2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to.md)
- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md)
- [2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces](../papers/2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces.md)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
- [2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering](../papers/2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering.md)
- [2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia](../papers/2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia.md)
- [2014-miao-a-fractal-analysis-of-permeability-for-fractured-rocks](../papers/2014-miao-a-fractal-analysis-of-permeability-for-fractured-rocks.md)
- [2015-zhao-three-dimensional-fractal-distribution-of-the-number-of-rock-mass-fracture-surfaces-an](../papers/2015-zhao-three-dimensional-fractal-distribution-of-the-number-of-rock-mass-fracture-surfaces-an.md)
- [2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac](../papers/2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac.md)
- [2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones](../papers/2017-lai-a-review-on-pore-structure-characterization-in-tight-sandstones.md)
- [2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin](../papers/2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin.md)
- [2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b](../papers/2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b.md)
- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
- [2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture](../papers/2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture.md)
