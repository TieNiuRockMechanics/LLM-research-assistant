---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi"
title: "Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures."
status: "draft"
source_pdf: "data/papers/2017 - Experimental study on the effect of fracture geometric characteristics on the permeability in deformable rough-walled fractures.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Chen, Yuedu, et al. \"Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 98, 2017, pp. 121-140. doi:10.1016/j.ijrmms.2017.07.003. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72590"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "72913"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00445"
coverage_status: "full-index"
source_signature: "8bef7229674636a2f654bd7584b27091bc2eff6d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:12:06"
---

# Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.

## One-line Summary
This experimental study quantifies how three fracture geometric characteristics (FGC) – the size of apertures of interconnected void spaces, contact areas, and heterogeneous distribution of interconnected void spaces – evolve with confining stress and control the permeability of deformable rough-walled fractures, and proposes an improved FGC model that outperforms the classic Yeo model in matching measured hydraulic apertures.

## Research Question
How do the geometric characteristics of deformable rough-walled fractures – including aperture size of interconnected void spaces, contact ratio, and the heterogeneity of interconnected void distribution – quantitatively affect fracture permeability under varying confining stresses, and how can a model that integrates these characteristics improve upon existing models like Cubic Law and Yeo’s model? [Chen 2017, pp. 1-2]

## Study Area / Data
- **Samples**: Six single fractured sandstone specimens (Φ50 mm × 100 mm) taken from sedimentary strata at a depth of 100 m to 150 m in Xiegou coal mine, Shanxi Province, China. Divided into three grain‑size groups: fine (FA, FB), medium (MA, MB), coarse (CA, CB). [Chen 2017, pp. 5-6, Table 2]
- **Mechanical properties** (UCS, Young’s modulus, Poisson ratio) for each sample are summarized in Table 2: for example, fine sandstones had UCS 61–73 MPa, E 8.85–9.39 GPa; medium sandstones had UCS 51–69 MPa, E 7.94–8.56 GPa; coarse sandstones had UCS 55–63 MPa, E 6.78–7.91 GPa. [Chen 2017, pp. 5-6, Table 2]
- **Fracture creation**: Samples split using straight splitting wedges (modified Brazilian technique). [Chen 2017, pp. 6,10]
- **Morphology data**: Upper and lower fracture surfaces scanned by a non‑contact 3D laser scanner (precision 0.01 mm in x‑y, 0.01 mm out‑of‑plane) before and after hydraulic tests; point‑cloud data digitized with SURFER v.11.0.642. [Chen 2017, pp. 10-11]
- **Hydraulic tests**: Steady‑state flow tests in a triaxial cell under confining stresses ranging from 1 MPa to 30–40 MPa (increments adapted to grain size). Distilled water injected; flow rate measured by electronic balance (precision 0.0001 g); pressures by transducers (resolution 0.01 MPa); axial/radial displacements by extensometers (precision 1 µm). [Chen 2017, pp. 10-11]
- **Fluid properties**: Dynamic viscosity of distilled water (standard value), density used in Reynolds number calculation. [Chen 2017, pp. 10-11]

## Methods
- **Fracture morphology measurement**: Point‑cloud data matching method.
  1. Scan exterior of intact fractured sample to obtain reference coordinates P_ext.
  2. Open sample, scan exterior P~_ext and fracture surface P~_frac of each half.
  3. Match P~_ext to P_ext via coordinate transformation to infer P_frac.
  4. Fit surfaces with high‑precision meshes (0.01 mm grid spacing). Compute initial aperture e_I₀ at each grid point from z‑elevations of top and bottom surfaces.
  5. Under confining stress, calculate aperture e_I = e_I₀ – ∆e, where ∆e is the continuously monitored average closure magnitude. [Chen 2017, pp. 3-5]
- **Identification of void spaces and contacts**: Contact defined as e_I ≤ 10 µm; void spaces e_I > 10 µm. Isolated void regions (surrounded by contacts, no contribution to seepage) are identified and excluded from interconnected void spaces via iterative algorithm. [Chen 2017, pp. 3-5, 11-12]
- **Representation parameters for FGC**:
  - **Effective mechanical aperture (e′_m)**: Arithmetic average aperture of interconnected void spaces, e′_m = (Σ e_I)/N_cv, where N_cv is number of grid points in interconnected voids. [Chen 2017, pp. 4-5, Eq. 5]
  - **Contact ratio (ω)**: Ratio of contact areas (e_I ≤ 10 µm) to total fracture area, ω = N_cont/N_pt, where N_pt is total grid points. [Chen 2017, pp. 5, Eq. 6]
  - **Relative fractal dimension (D*Δ)**: Heterogeneity of interconnected void distribution.
     * Compute fractal dimension D of the 3D cavity formed by interconnected void spaces using a modified Cubic Covering method – the ultra‑thin square plate (UTSP) covering method. The number of UTSPs needed to cover the cavity at measurement scale δ is N_sum(δ); D = – slope of log‑log plot of N_sum(δ) vs δ. [Chen 2017, pp. 5-6, Eqs. 7‑9]
     * Define DΔ = D – D₀, where D₀ is the fractal dimension of parallel plates with the same e′_m. Relative fractal dimension: D*Δ = log₁₀(DΔ / DΔ_ref), where DΔ_ref is the value at σ₃ = 0 MPa. [Chen 2017, pp. 6,10, Eq. 10]
- **Hydraulic test and permeability calculation**:
  - For each confining stress, linear flow stage identified where Darcy’s law holds (Re < 0.001–3.5). Hydraulic aperture e_h derived from the linear portion of P–Q curves using Cubic Law (Eqs. 1‑2). [Chen 2017, pp. 10-11]
  - Fracture permeability k = e_h²/12. [Chen 2017, pp. 1, Eq. 2]
- **FGC model formulation**: e_h = (1 – 1.1ω)⁴ (1 + 2 D*Δ)^(3/5) e′_m [Chen 2017, pp. 16, Eq. 16] and corresponding permeability expression k = (e′_m)² (1 – 1.1ω)⁸ (1 + 2 D*Δ)^(6/5) / 12. [Chen 2017, pp. 16, Eq. 17]
- **Comparison model**: Yeo model e_h = <e_m> [1 – 1.5(s/<e_m>)^(3/2)] (1 – 2.4c), where s is standard deviation of apertures, c contact ratio, and <e_m> mechanical aperture (all points). [Chen 2017, pp. 16, Eq. 15]

## Key Findings
- The FGC representation parameters show distinct, stress‑dependent trends:
  - **Effective mechanical aperture e′_m** decreases with increasing confining stress. Coarse samples CA, CB had lowest reduction rate (30.2% and 32.8%); fine samples FA, FB had largest reduction rates (55.5% and 50%). All curves fitted well with e′_m = e₁ + e_{m+1} exp(–σ₃/K). [Chen 2017, pp. 11-12, Fig. 12, Table 3]
  - **Contact ratio ω** increases and then stabilizes. Residual contact ratios of fine and medium sandstones are larger than coarse ones. FA increased from 3% to 49% (Δ≈46%); MA increased from 6% to 55% (Δ≈42%); coarse CA increased only ≈6%. Exponential fits ω = ω₁ + ω_{n+1} exp(–σ₃/K) describe the data well. [Chen 2017, pp. 12-13, Fig. 13]
  - **Relative fractal dimension D*Δ** (heterogeneity) shows nonlinear growth with confining stress, fitted by D*Δ = a + b exp(c σ₃). Correlation coefficients > 96.1%. [Chen 2017, pp. 14-15, Fig. 15, Eq. 14, Table 4]
- **FGC model vs. Yeo model**:
  - Both models show similar trends with Cubic Law, but FGC model agrees better with experimental e_h for all sandstone types. [Chen 2017, pp. 16, Fig. 16]
  - Yeo model predicts negative e_h for MA, MB, CA, CB at higher stresses, over‑exaggerating contact effect; FGC model avoids this by a weaker contact term (1 – 1.1ω)⁴. [Chen 2017, pp. 16]
  - For fine sandstone FA, neglect of heterogeneous distribution and isolated voids in Yeo model causes larger deviation; FGC model corrects this with D*Δ and exclusion of isolated spaces. [Chen 2017, pp. 16, Fig. 16]
- **General behavior**: The three FGC parameters influence hydraulic aperture e_h: e_h positively correlates with e′_m, negatively with ω and D*Δ. The FGC model reduces to Cubic Law when e′_m = e_h, ω = 0, and D*Δ = 0. [Chen 2017, pp. 16-17]
- **Normal stiffness K** for each sample summarised in Table 3 (ranging from 0.111 GPa/mm for CB to 0.765 GPa/mm for MB). [Chen 2017, pp. 13, Table 3]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| e′_m of fine sandstone FA decreases from 180 µm to 80 µm (55.5% reduction) over σ₃ = 0–30 MPa. Fine FB: 140 µm to 70 µm (50% reduction). | [Chen 2017, pp. 11-12, Fig. 12] | Samples FA, FB; linear flow stage; confining stress range 0–30 MPa. | Largest reduction among grain sizes. |
| e′_m of coarse sandstone CA decreases from ~320 µm to ~220 µm (~30.2% reduction); CB ~310 µm to ~210 µm (~32.8% reduction). | [Chen 2017, pp. 11-12, Fig. 12] | Samples CA, CB; linear flow stage; σ₃ up to ~18 MPa (CA) and ~29 MPa (CB). | Residual e′_m larger than other groups. |
| Contact ratio ω of FA increases from 3% at 0 MPa to 49% at 30 MPa (Δ ~ 46%). MA increases from 6% to 55% (Δ ~ 42%). Coarse CA increases only ~6 percentage points. | [Chen 2017, pp. 12-13, Fig. 13] | All σ₃ levels; threshold contact e ≤ 10 µm. | Fine and medium sandstones show much larger absolute increase. |
| Relative fractal dimension D*Δ for FA changes from 0 (σ₃=0) to –2.33913 (σ₃=29 MPa). Fitted by D*Δ = a + b exp(c σ₃) with R² > 0.961. | [Chen 2017, pp. 14-15, Fig. 15, Table 4] | All σ₃ levels; optimal initial UTSP thickness ξ₀ = 5×10⁻⁵ mm for D calculation. | Log‑based relative fractal dimension increases (becomes less negative) with stress. |
| Hydraulic aperture e_h predicted by Yeo model becomes negative for samples MA, MB, CA, CB at high σ₃ (e.g., MA at σ₃ ≈ 10 MPa). FGC model e_h remains positive and matches experimental values. | [Chen 2017, pp. 16, Fig. 16] | Linear flow stage; all samples. | Yeo’s term (1–2.4c) over‑exaggerates contact effect; FGC term (1–1.1ω)⁴ corrects it. |
| For fine FA, FGC model gives e_h closer to experiment than Yeo model; Yeo model deviates more because neglects heterogeneity and isolated voids. | [Chen 2017, pp. 16, Fig. 16a] | Sample FA; σ₃ = 0–30 MPa. | FGC model includes D*Δ and uses only interconnected voids. |
| Normal stiffness K fitted from e′_m = e₁ + e_{m+1} exp(–σ₃/K) ranges from 0.111 (CB) to 0.765 GPa/mm (MB). | [Chen 2017, pp. 13, Table 3] | All samples, isotropic normal loading. | Derived from closure vs. stress. |
| Reynolds number in linear flow stages: Re < 0.001 – 3.5 across samples. | [Chen 2017, pp. 11, Fig. 8] | Linear portion of P–Q curves; Darcy flow valid. | Confirms analysis is within Darcian regime. |
| Standard deviation s of apertures (all void spaces) for FA: 0.1883 at 0 MPa, decreasing to 0.1869 at 30 MPa; for CA: 0.7092 at 0 MPa to 0.7043 at 29 MPa. | [Chen 2017, pp. 18-20, Table 5] | All apertures (including isolated) for Yeo model input. | Coarse samples have much larger initial s. |

## Limitations
- The study is confined to small‑scale (Φ50 mm × 100 mm) laboratory fractures; upscaling to field‑scale fractured rock masses remains an open challenge. [Chen 2017, pp. 18]
- Nonlinear flow regimes (inertial effects, fracture dilation) were excluded; only linear Darcy flow was analysed. [Chen 2017, pp. 11]
- The point‑cloud matching method assumes no irreversible surface degradation; only average closure is used to update apertures, ignoring localised shear or asperity damage. [Chen 2017, pp. 4,10]
- Contact definition relies on a 10 µm threshold dictated by scanner accuracy; true contact might occur at smaller scales. [Chen 2017, pp. 4-5]
- The relative normal displacement was assumed macroscopically uniform and relative shear sliding between fracture surfaces was not considered. [Chen 2017, pp. 13]
- Fractal dimension determination is sensitive to the choice of initial UTSP thickness ξ₀; optimal value was found by sensitivity analysis but may not be universal. [Chen 2017, pp. 14]
- The FGC model was validated only on the six tested sandstones; generalisation to other lithologies or fracture types is not yet confirmed.

## Assumptions / Conditions
- **Linear flow (Darcy’s law) is valid** in the initial portion of each Q–P curve; Reynolds numbers were well below the onset of nonlinearity. [Chen 2017, pp. 10-11]
- **Isolated void spaces** (surrounded by contact areas) contribute nothing to flow and are excluded from the effective percolation network. [Chen 2017, pp. 2-3,11]
- **Contact** is defined by e_I ≤ 10 µm, based on the 3D scanner’s out‑of‑plane accuracy of 0.01 mm (10 µm). [Chen 2017, pp. 4-5]
- **Average closure magnitude** ∆e is uniform across the fracture; fracture aperture at each grid point is simply e_I₀ – ∆e, ignoring localised deformation. [Chen 2017, pp. 4]
- **Fracture surfaces** are assumed not to undergo significant degradation or chemical dissolution during testing; point‑cloud matching before/after test validates this. [Chen 2017, pp. 10]
- **Fracture width and length** are constant; the sample is sealed with heat‑shrink sleeve and PVC tape to prevent leakage through matrix. [Chen 2017, pp. 10-11]
- **Quasi‑static loading**: Confining stress increments were applied stepwise and held constant during each hydraulic measurement. [Chen 2017, pp. 10-11]
- **Fracture surfaces** are considered isotropic in terms of statistical properties; no preferential flow direction was imposed other than the axial direction.

## Key Variables / Parameters
- **e′_m** – effective mechanical aperture (µm or mm), arithmetic mean of interconnected void apertures. [Chen 2017, pp. 4-5, Eq. 5]
- **ω** – contact ratio (dimensionless), area fraction of contacts. [Chen 2017, pp. 5, Eq. 6]
- **D*Δ** – relative fractal dimension (dimensionless), log‑scaled heterogeneity index of interconnected void space distribution. [Chen 2017, pp. 6,10, Eq. 10]
- **e_h** – hydraulic aperture (mm), back‑calculated from Cubic Law using measured Q and ∇P. [Chen 2017, pp. 1, Eq. 2, 11]
- **k** – fracture permeability (m² or equivalent), k = e_h²/12. [Chen 2017, pp. 1, Eq. 2]
- **σ₃** – confining stress (MPa), applied normal to fracture. [Chen 2017, pp. 10-11]
- **K** – normal stiffness of fracture (GPa/mm), fitted from e′_m vs σ₃ curves. [Chen 2017, pp. 11, Table 3]
- **∆e** – average closure (mm), monitored during loading. [Chen 2017, pp. 4]
- **δ₀** – initial measurement scale (mesh spacing, 0.01 mm). [Chen 2017, pp. 4]
- **ξ₀** – optimal initial UTSP thickness (5×10⁻⁵ mm used for final D calculation). [Chen 2017, pp. 14]
- **Re** – Reynolds number, ρQ/(µw). [Chen 2017, pp. 11, Eq. 11]
- Lithological parameters: grain size group, UCS, Young’s modulus E, Poisson ratio ν (Table 2). [Chen 2017, pp. 5-6]

## Reusable Claims
- **Claim**: In deformable rough‑walled fractures, the effective mechanical aperture (average of interconnected void apertures) decreases with confining stress following an exponential form e′_m = e₁ + e_{m+1} exp(–σ₃/K), and the reduction rate is larger in finer‑grained sandstones.  
  *Condition*: Sandstones with 0 MPa < σ₃ ≤ 30 MPa, linear Darcy flow, no shear displacement.  
  [Chen 2017, pp. 11-12, Fig. 12, Eq. 12]

- **Claim**: Contact ratio ω increases with confining stress and saturates; the residual contact ratio of fine and medium sandstones exceeds that of coarse sandstones. The trend can be fitted by ω = ω₁ + ω_{n+1} exp(–σ₃/K).  
  *Condition*: Same test conditions; contact defined at 10 µm threshold.  
  [Chen 2017, pp. 12-13, Fig. 13, Eq. 13]

- **Claim**: The heterogeneity of interconnected void distribution (quantified by relative fractal dimension D*Δ) increases nonlinearly with confining stress and is well described by D*Δ = a + b exp(c σ₃).  
  *Condition*: Fractal dimension computed using UTSP covering method with optimal initial thickness ξ₀ = 5×10⁻⁵ mm; sandstone fractures.  
  [Chen 2017, pp. 14-15, Fig. 15, Eq. 14, Table 4]

- **Claim**: The hydraulic aperture e_h can be expressed as e_h = (1 – 1.1ω)⁴ (1 + 2 D*Δ)^(3/5) e′_m (FGC model). This model outperforms the classic Yeo model for all tested grain‑size groups, especially at high contact ratios where Yeo’s model yields negative e_h.  
  *Condition*: Deformable rough‑walled fractures with isolated voids precluded; Darcy flow; sandstone.  
  [Chen 2017, pp. 16, Fig. 16, Eq. 16]

- **Claim**: The FGC model reduces to the Cubic Law (e_h = e′_m, or e_h = e_m) when contact ratio ω = 0 and relative fractal dimension difference D*Δ = 0, i.e., a smooth parallel plate.  
  *Condition*: Parallel‑plate idealization is a special case of the FGC model.  
  [Chen 2017, pp. 16-17]

- **Claim**: Fracture permeability k of RWF under normal stress can be expressed as a function of the three FGC parameters: k = (e′_m)² (1 – 1.1ω)⁸ (1 + 2 D*Δ)^(6/5) / 12.  
  *Condition*: Same conditions as above; provides a way to link hydro‑mechanical behavior to stress field via Eqs. 12‑14 for e′_m, ω, and D*Δ.  
  [Chen 2017, pp. 16, Eq. 17]

- **Claim**: The point‑cloud data matching method provides high‑resolution (0.01 mm) non‑destructive 3D fracture morphology, enabling calculation of aperture distributions without surface damage.  
  *Condition*: Requires scanning before assembly and after disassembly; assumes no irreversible surface changes during loading.  
  [Chen 2017, pp. 3-5]

## Candidate Concepts
- [[fracture geometric characteristics (FGC)]]
- [[rough-walled fracture (RWF)]]
- [[effective mechanical aperture]]
- [[contact ratio]]
- [[relative fractal dimension]]
- [[interconnected void spaces]]
- [[isolated void spaces]]
- [[percolation network]]
- [[UTSP covering method]]
- [[point-cloud data matching method]]
- [[Cubic Law]]
- [[Yeo model]]
- [[FGC model]]
- [[hydraulic aperture]]
- [[Darcy flow]]
- [[normal stiffness of fracture]]
- [[triaxial hydraulic test]]

## Candidate Methods
- [[point-cloud data matching for fracture morphology]]
- [[UTSP covering method for fractal dimension]]
- [[iterative isolation of interconnected voids]]
- [[high-precision triaxial flow tests on fractured samples]]
- [[Reynolds number check for Darcy flow validity]]
- [[exponential fitting of FGC parameters vs. stress]]
- [[FGC model formulation from hydraulic aperture]]

## Connections To Other Work
- **Cubic Law**: The study treats the Cubic Law (k = e_h²/12) as the baseline; the FGC model is a generalisation that reduces to Cubic Law for smooth parallel plates. [Chen 2017, pp. 1]
- **Yeo (2001) model**: Directly compared with the proposed FGC model. Yeo’s model uses mean aperture, standard deviation, and contact ratio but neglects heterogeneity of interconnected voids. The FGC model shows better agreement, especially for fine sandstones and high contact ratios. [Chen 2017, pp. 16]
- **Tortuosity concepts**: Extends works by Cook et al. (1990) (out‑of‑plane/in‑plane tortuosity), Zimmerman et al. (1992) (contact area effect), and Souley et al. (2015) (evolution of preferential flow paths) by adding a quantitative heterogeneity descriptor (relative fractal dimension). [Chen 2017, pp. 2]
- **Fracture roughness and fractal studies**: Builds on prior fractal descriptions of fracture surfaces (e.g., Brown 1987; Develi & Babadagli 2015; Ju et al. 2013) by applying fractal characterisation to the 3D cavity of interconnected void spaces rather than just surface roughness. [Chen 2017, pp. 2, 14]
- **Contact ratio and aperture measurements**: Aligns with earlier works that measured contact ratio under stress (e.g., Sharifzadeh et al. 2008; Hakami & Stephansson 1993; Bertels et al. 2001) and validates the exponential increase trend. [Chen 2017, pp. 13]
- **Non‑destructive morphology measurement**: The point‑cloud data matching method overcomes limitations of destructive profilometry, low‑resolution CT, and costly NMRI (cf. Table 1 review). [Chen 2017, pp. 3-4]
- **Hydromechanical coupling**: The study provides a direct link between FGC representation parameters and permeability, enabling numerical simulation of flow in deformable fractures when combined with stress‑stiffness relations. [Chen 2017, pp. 17]

## Open Questions
- **Field‑scale applicability**: How can the FGC model, derived from small laboratory fractures, be upscaled to field‑scale fractured rock masses where fractures occur in networks and 3D connectivity is more complex? Numerical methods and geophysical prospecting techniques need to be developed to bridge this gap. [Chen 2017, pp. 18]
- **Nonlinear flow regimes**: The present study only addresses Darcian flow. The extension of the FGC model to include inertial effects, fracture dilation, and multiphase flow remains to be explored. [Chen 2017, pp. 11, 18]
- **Generalisation to other rock types**: The findings were obtained on three sandstone grain‑size groups. Whether the same relationships hold for other lithologies (e.g., granite, limestone) with different surface roughness, stiffness, and grain‑scale heterogeneity is unknown. [Chen 2017, pp. 18]
- **Contact threshold sensitivity**: The definition of contact as e ≤ 10 µm is dictated by scanner resolution. How much would small changes in this threshold affect the computed FGC parameters and model predictions? [Chen 2017, pp. 5]
- **Fracture surface evolution**: The assumption of uniform closure and negligible surface degradation may fail under higher stresses or cyclic loading. Investigating localised damage, gouge production, and chemical dissolution could refine the model. [Chen 2017, pp. 10, 18]

## Source Coverage
All 15 non‑empty indexed fragments (pages 1‒20) were processed to compile this page.  
Coverage ratios: by blocks = 1.0; by characters = 1.00445 (indexed chars 72,590 vs compiled 72,913).  
Fragments indexed: 15; source signature: 8bef7229674636a2f654bd7584b27091bc2eff6d.  
No fragment was omitted; all source evidence is traceable to the original paper via page ranges.
