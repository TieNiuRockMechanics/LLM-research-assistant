---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-hu-damage-mechanism-and-heat-transfer-characteristics-of-limestone-after-thermal-shock-cycl"
title: "Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development."
status: "draft"
source_pdf: "data/papers/2022 - Damage mechanism and heat transfer characteristics of limestone after thermal shock cycle treatments based on geothermal development.pdf"
collections:
  - "论文"
citation: "Hu, Jianjun, et al. \"Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 160, 2022, p. 105269. Accessed 2026."
indexed_texts: "8"
indexed_chars: "39273"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:01:27"
---

# Damage Mechanism and Heat Transfer Characteristics of Limestone after Thermal Shock Cycle Treatments Based on Geothermal Development.

## One-line Summary

This paper experimentally and numerically investigates the effects of thermal shock fatigue (1-5 heating/cooling cycles at 100°C-500°C) on the physico-mechanical properties and heat transfer of limestone for geothermal development in carbonate reservoirs. [Hu 2022, pp. 1-1]

## Research Question

How do multiple thermal shock cycles (heating and cooling) at different temperatures affect the damage mechanism, physical properties (chromaticity, P-wave velocity, thermal conductivity), and mechanical properties (tensile strength) of limestone, and how do these changes in turn influence its internal heat transfer characteristics for Hot Dry Rock (HDR) geothermal development in carbonate reservoirs? [Hu 2022, pp. 1-1]

## Study Area / Data

The study analyzes limestone samples collected for experimental testing. The specific geological origin or formation of the limestone is not specified in the provided fragments. Limestone specimens were prepared in two sizes: short cylinders and long cylinders (5 cm diameter, 10 cm height for numerical simulation) [Hu 2022, pp. 3-5]. The study focuses on geothermal carbonate reservoirs due to a noted lack of research compared to granite or sandstone [Hu 2022, pp. 1-3].

## Methods

The experimental and numerical methods employed are as follows:
- **Thermal Treatment:** Limestone specimens were subjected to 1, 2, 3, 4, or 5 heating and cooling cycles at target temperatures of 100°C, 200°C, 300°C, 400°C, and 500°C in a muffle furnace. Cooling was achieved through water quenching. [Hu 2022, pp. 1-1]
- **Chromaticity Measurement:** The color change of the limestone surface was measured using the CIE L*a*b* international standard color system after thermal treatments. [Hu 2022, pp. 3-5]
- **Physical and Mechanical Properties Testing:** P-wave velocity and thermal conductivity were measured on long cylindrical samples. The specific testing machines for P-wave velocity and thermal conductivity are not detailed in the segments. Uniaxial tensile strength was obtained using a hydraulic servo testing machine with a maximum axial load of 1000 kN and a force measurement range of 2%–100%. [Hu 2022, pp. 3-5]
- **Correlation Analysis:** Linear regression was performed to establish relationships between P-wave velocity, tensile strength, and thermal conductivity. [Hu 2022, pp. 9-10]
- **Numerical Simulation:** Internal heat transfer was simulated using the solid heat transfer module in COMSOL Multiphysics 5.4 software. The simulation used cylindrical models (5 cm diameter, 10 cm height) with an initial internal temperature of 25°C and external boundary conditions set to the target temperatures (100°C-500°C). A very small physical field control grid was used for a transient heat transfer simulation with a heating time of 60 minutes. [Hu 2022, pp. 3-5]

## Key Findings

1.  **Color Change:** With increasing temperature (for a fixed number of cycles), the brightness (L*) and yellowness (b*) of the limestone surface increased. As the number of cycles increased at a constant temperature, the sample color changed to yellow and became dull. [Hu 2022, pp. 10-10]
2.  **Crack Development:** The number and width of surface cracks increased with temperature, especially above 300°C, and with the number of cycles. [Hu 2022, pp. 10-10]
3.  **Degradation of Properties:** Thermal conductivity, P-wave velocity, and tensile strength all decreased with an increase in both temperature and the number of thermal shock cycles. The degradation was attributed to thermal expansion damage to calcite crystals. [Hu 2022, pp. 10-10]
4.  **Property Correlations:** A strong linear relationship was established between the three measured parameters.
    *   P-wave velocity and thermal conductivity are strongly correlated (Equation: λ = 0.36189 Vp + 0.9059, R² = 0.9269). [Hu 2022, pp. 9-10]
    *   Tensile strength and thermal conductivity are correlated (Equation: σ = 3.005λ - 1.435, R² = 0.8367). [Hu 2022, pp. 9-10]
    *   Tensile strength and P-wave velocity are correlated (Equation: σ = 1.1547 Vp + 1.0567, R² = 0.8738). [Hu 2022, pp. 9-10]
    These correlations suggest P-wave velocity is a convenient proxy to evaluate trends in tensile strength and thermal conductivity. [Hu 2022, pp. 10-10]
5.  **Heat Transfer Impairment:** Numerical simulations showed that for the same heating time and temperature, a higher number of cycles resulted in a lower internal central point temperature of the sample. [Hu 2022, pp. 6-9] Heat treatment temperature and the number of cycles significantly affected the internal heat transfer. [Hu 2022, pp. 10-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| P-wave velocity, thermal conductivity, and tensile strength decrease with increasing temperature (for constant cycles) and increasing cycles (for constant temperature). | [Hu 2022, pp. 1-3] | Limestone samples, 1-5 heating/cooling cycles, 100°C-500°C. | Water quenching was used for cooling. |
| Strong linear correlation between P-wave velocity and thermal conductivity: λ = 0.36189 Vp + 0.9059, R² = 0.9269. | [Hu 2022, pp. 9-10] | Post-quenching cycle measurements. | P-wave velocity can be used to estimate thermal conductivity. |
| Linear correlation between tensile strength and thermal conductivity: σ = 3.005λ - 1.435, R² = 0.8367. | [Hu 2022, pp. 9-10] | Post-quenching cycle measurements. | Note the intercept is -1.435. |
| Linear correlation between tensile strength and P-wave velocity: σ = 1.1547 Vp + 1.0567, R² = 0.8738. | [Hu 2022, pp. 9-10] | Post-quenching cycle measurements. | Relationship used to suggest P-wave velocity as a proxy for tensile strength. |
| Surface L* (brightness) and b* (yellowness) increase with temperature; color becomes yellow and dull with more cycles. | [Hu 2022, pp. 10-10] | Limestone, measured with CIE L*a*b* system. | Chromaticity changes serve as an indicator of thermal damage. |
| In numerical simulation, internal center temperature after fixed heating time is lower for samples with a higher number of thermal cycles. | [Hu 2022, pp. 6-9] | COMSOL simulation, transient heat transfer, 5-10 min heating. | Demonstrates impairment of heat transfer rate due to thermal shock damage. |

## Limitations

- **Micro-mechanism vs. Macro-property Link:** The relationship between macroscopic physical properties (P-wave velocity, tensile strength, etc.) and microscopic changes in crystal structure or crack networks is suggested but not deeply explored. The paper states the need for further investigation of "the damage mechanism and the seepage heat transfer of limestone under the coupling of multiple fields such as thermal-hydrological-mechanical-chemical." [Hu 2022, pp. 10-10]
- **Simulation Scope:** The numerical simulation focused on the effect of cracks on "heat transfer, not on fluid flow"[Hu 2022, pp. 10-10], which is a critical component of geothermal reservoir analysis. Seepage heat transfer under multi-field coupling is identified as future work. [Hu 2022, pp. 10-10]

## Assumptions / Conditions

- **Thermal Shock Method:** Damage was induced by heating samples in a furnace and then rapidly cooling them by water quenching. This specific method defines the thermal shock type. [Hu 2022, pp. 1-1]
- **Cycles and Temperatures:** The experimental results are valid for the conditions tested: 1 to 5 cycles and temperatures from 100°C to 500°C. Extrapolation beyond these ranges is not directly supported by the data. [Hu 2022, pp. 1-3]
- **Numerical Model:** The COMSOL simulation assumed cylindrical geometry (5cm x 10cm), an initial uniform internal temperature of 25°C, and external boundary conditions equal to the target temperature. The simulation used the solid heat transfer module. [Hu 2022, pp. 3-5]
- **Property Correlations:** The derived linear equations (Equations 3, 4, 5) are empirical correlations based on the specific limestone type and thermal treatment conditions tested. Their applicability to other rock types or thermal histories is not confirmed. [Hu 2022, pp. 9-10]

## Key Variables / Parameters

- **Independent Variables:** Heat treatment temperature (°C), Number of heating/cooling cycles (1–5), heat transfer time (min). [Hu 2022, pp. 1-1]
- **Dependent Variables (Physical):** Chromaticity (L*, a*, b* values), P-wave velocity (Vp), Thermal conductivity (λ). [Hu 2022, pp. 1-3]
- **Dependent Variables (Mechanical):** Uniaxial tensile strength (σ). [Hu 2022, pp. 1-3]
- **Derived/Model Parameters:** Internal sample temperature (°C), Thermal damage factor (DT, DL). [Hu 2022, pp. 9-10]
- **Correlation Metrics:** Coefficient of determination (R²). [Hu 2022, pp. 9-10]

## Reusable Claims

- **Claim 1:** For limestone subjected to quenching thermal shocks, both increased temperature and increased cycle number independently cause a decrease in P-wave velocity, thermal conductivity, and tensile strength, and an increase in surface cracks. This holds for 1-5 cycles and 100-500°C conditions. [Hu 2022, pp. 10-10]
- **Claim 2:** In thermally damaged limestone, a strong linear relationship exists where thermal conductivity (λ) increases with increasing P-wave velocity (Vp), defined by λ = 0.36189 Vp + 0.9059, with an R² of 0.9269. This suggests P-wave velocity can be a non-destructive proxy for thermal property assessment. [Hu 2022, pp. 9-10]
- **Claim 3:** In thermally damaged limestone, uniaxial tensile strength (σ) increases with increasing thermal conductivity (λ), defined by σ = 3.005λ - 1.435, with an R² of 0.8367. [Hu 2022, pp. 9-10]
- **Claim 4:** Pre-existing thermal shock damage in limestone, quantified by a higher number of thermal cycles, reduces its rate of internal heat transfer. This was validated by numerical simulation showing lower core temperatures after a fixed heating period for samples with more damage cycles. [Hu 2022, pp. 6-9]
- **Claim 5:** The CIEL*a*b* color space is a valid system for monitoring thermal damage in limestone; increased temperature results in higher L* (brightness) and b* (yellowness) values. [Hu 2022, pp. 10-10]

## Candidate Concepts

- [[Hot Dry Rock (HDR)]]
- [[Geothermal Carbonate Reservoir]]
- [[Thermal Shock Fatigue]]
- [[Rock Thermal Damage]]
- [[P-wave Velocity Correlation]]
- [[Fracture Reservoir]] (mentioned as a reference for prior work on granite fissures [Hu 2022, pp. 12-12])
- [[Thermal-Hydrological-Mechanical-Chemical (THMC) Coupling]]
- [[Microcracking]]

## Candidate Methods

- [[CIE L*a*b* Color Measurement for Rock Damage]]
- [[Thermal Conductivity Measurement of Rocks]]
- [[P-wave Anisotropy Measurement]]
- [[Brazilian Tensile Strength Test (Uniaxial)]] (implied by tensile strength test of cylindrical samples [Hu 2022, pp. 3-5])
- [[COMSOL Multiphysics Solid Heat Transfer Module]]
- [[Linear Regression Analysis for Petrophysical Properties]]
- [[Water Quenching Thermal Cycling]]

## Connections To Other Work

- This study positions itself against prior work that predominantly focused on high-temperature tests for HDR in **granite** and **sandstone**, noting a scarcity of studies on **carbonate reservoirs** [Hu 2022, pp. 1-3]. It references [[Hot Dry Rock]] development concepts.
- The methodology of using chromaticity for damage assessment was adapted from a similar technique applied to **fly ash cement mortar** by Zhang et al. [Hu 2022, pp. 3-5].
- The finding that P-wave velocity decreases after high-temperature treatment aligns with prior findings in other rock types [Hu 2022, pp. 5-5]. The paper references studies on the mechanical and physical property variations of **granite** and **sandstone** after high-temperature treatment [Hu 2022, pp. 12-12].
- Future work identified needs to connect the damage mechanism to more complex multi-physics couplings, connecting to concepts like [[Thermal-Hydrological-Mechanical-Chemical (THMC) Models]] [Hu 2022, pp. 10-10].

## Open Questions

- What is the specific mechanism linking calcite crystal structure fatigue to macroscopic property degradation, and how does it differ from granite? [Hu 2022, pp. 1-1]
- How do the thermal shock-induced cracks affect fluid flow and coupled seepage heat transfer in a limestone reservoir? [Hu 2022, pp. 10-10]
- What are the long-term effects of more than 5 cycles on the mechanical and hydraulic properties of limestone, and is there a damage stabilization point?
- Can the linear correlations between P-wave velocity, thermal conductivity, and tensile strength be generalized to other carbonate rocks with different porosities, textures, and mineralogies?

## Source Coverage

This wiki page is based on 8 indexed fragments from the paper, covering the abstract, introduction, subsections of the methodology (thermal treatment, numerical simulation method), parts of the results section (surface characteristics, thermal conductivity and P-wave velocity, tensile strength, heat transfer simulation), discussion (correlation analysis), and conclusions.

Coverage is weighted towards the **Results** and **Conclusion** sections, providing a detailed view of the experimental findings and established correlations. Gaps exist for a complete understanding of the **Methodology**, as the exact testing equipment and procedures for P-wave velocity, thermal conductivity, and chromaticity are not detailed in the fragments. The **Discussion** of the damage mechanism (relating microstructural changes to macro properties) is only represented in a high-level summary within the conclusions. A detailed microstructural analysis (e.g., SEM, mineralogical quantification) that may have been performed is not captured in these fragments. The full **Introduction** listing prior art in detail, and the full **reference list** beyond what is shown on the last page, are missing.
