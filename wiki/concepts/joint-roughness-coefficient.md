---
type: "concept"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "节理粗糙度系数 (JRC)"
aliases:
  - "Joint Roughness Coefficient"
  - "JRC"
  - "节理粗糙度系数"
  - "joint roughness coefficient"
  - "rock joint roughness"
sources:
  - "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
  - "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
  - "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
  - "2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces"
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
  - "2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces"
  - "2019-ban-new-roughness-parameters-for-3d-roughness-of-rock-joints"
  - "2020-ban-a-modified-roughness-index-based-on-the-root-mean-square-of-the-first-derivative-and-it"
  - "2020-bao-geometrical-heterogeneity-of-the-joint-roughness-coefficient-revealed-by-3d-laser-scann"
  - "2021-marsch-comparative-evaluation-of-statistical-and-fractal-approaches-for-jrc-calculation-bas"
  - "2023-barton-advances-in-joint-roughness-coefficient-jrc-and-its-engineering-applications"
  - "2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn"
  - "2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit"
  - "2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using"
---

# 节理粗糙度系数 (JRC)

## Definition

用于量化岩石节理表面粗糙程度的无量纲经验参数，范围通常 0–20（或更高）。JRC 值越大，表面越粗糙，对抗剪强度和渗流特性影响显著。
## Aliases

- Joint Roughness Coefficient
- JRC
- 节理粗糙度系数
- joint roughness coefficient
- rock joint roughness
## Boundary

具有尺度效应（尺寸越大 JRC 越小）和各向异性；视觉对比法易产生系统性低估；不同数字化方法和采样间隔可导致结果差异。
## Related Methods

- visual-comparison-method-for-jrc
- statistical-parameter-for-jrc
- 2d-roughness-parameter-evaluation
- fractal-dimension-for-jrc
- scan-circle-technique
- updated-h-l-method
- lambda-method-for-jrc
- Z2-calculation
- laser-surface-scanning
- jrc-jcs-model
- multi-direction-jrc
- li-zhang-jrc-formula
## Related Claims

- JRC-relationship-sampling-interval-dependent
- JRC-4th-profile-deviation
- D-to-JRC-relation-method-dependent
- JRC-smooth-walls-ignored
- visual-comparison-underestimates-jrc-by-2-3-units
- 3d-roughness-parameters-correlate-with-jrc
- jrc-increases-with-temperature-and-cycles
- jrc-alone-insufficient-to-predict-shear-strength
- jrc-anisotropy-convergence
- deep-jrc-stress-direction
- Z2-sufficient-for-JRC
- fractal-methods-not-necessary-for-JRC
- claim-jrc-scale-effect
## Source Papers

- [2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc](../papers/2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc.md)
- [2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to](../papers/2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to.md)
- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md)
- [2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces](../papers/2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces.md)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
- [2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces](../papers/2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces.md)
- [2019-ban-new-roughness-parameters-for-3d-roughness-of-rock-joints](../papers/2019-ban-new-roughness-parameters-for-3d-roughness-of-rock-joints.md)
- [2020-ban-a-modified-roughness-index-based-on-the-root-mean-square-of-the-first-derivative-and-it](../papers/2020-ban-a-modified-roughness-index-based-on-the-root-mean-square-of-the-first-derivative-and-it.md)
- [2020-bao-geometrical-heterogeneity-of-the-joint-roughness-coefficient-revealed-by-3d-laser-scann](../papers/2020-bao-geometrical-heterogeneity-of-the-joint-roughness-coefficient-revealed-by-3d-laser-scann.md)
- [2021-marsch-comparative-evaluation-of-statistical-and-fractal-approaches-for-jrc-calculation-bas](../papers/2021-marsch-comparative-evaluation-of-statistical-and-fractal-approaches-for-jrc-calculation-bas.md)
- [2023-barton-advances-in-joint-roughness-coefficient-jrc-and-its-engineering-applications](../papers/2023-barton-advances-in-joint-roughness-coefficient-jrc-and-its-engineering-applications.md)
- [2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn](../papers/2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn.md)
- [2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit](../papers/2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit.md)
- [2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using](../papers/2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using.md)
