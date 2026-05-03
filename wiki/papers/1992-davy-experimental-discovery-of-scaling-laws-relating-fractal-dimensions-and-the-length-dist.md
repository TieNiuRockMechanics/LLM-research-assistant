---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1992-davy-experimental-discovery-of-scaling-laws-relating-fractal-dimensions-and-the-length-dist"
title: "Experimental Discovery of Scaling Laws Relating Fractal Dimensions and the Length Distribution Exponent of Fault Systems."
status: "draft"
source_pdf: "data/papers/1992 - Experimental discovery of scaling laws relating fractal dimensions and the length distribution exponent of fault systems.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Davy, Philippe, et al. \"Experimental Discovery of Scaling Laws Relating Fractal Dimensions and the Length Distribution Exponent of Fault Systems.\" *Geophysical Research Letters*, vol. 19, no. 4, 21 Feb. 1992, pp. 361-63."
indexed_texts: "5"
indexed_chars: "21669"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "21463"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990493"
coverage_status: "full-index"
source_signature: "9138ea694731745607b53e0f4eada91e197e4597"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:08:52"
---

# Experimental Discovery of Scaling Laws Relating Fractal Dimensions and the Length Distribution Exponent of Fault Systems.

## One-line Summary
Laboratory fault patterns are self-similar, and the generalized fractal dimensions \(D_q\) are governed by the scaling law \(D_0 \approx b\) and \(D_{q>1} \approx b + 2 - a\) where \(b\) is the fractal dimension of fault barycenters and \(a\) is the exponent of the fault length distribution (valid for \(2 \le a \le 3\) as observed in the experiments).

## Research Question
Why does the capacity (box‑counting) fractal dimension \(D_0\) of experimental fault patterns differ from the higher‑order generalized dimensions \(D_{q \ge 1}\), even though the patterns appear to be essentially homogeneous fractals? Can the fractal dimensions be expressed in terms of simpler measures such as the exponent of the fault length distribution and the spatial clustering of fault centres?

## Study Area / Data
- **Data source:** Laboratory experiments scaled for gravity, designed to model continental collision (e.g., the India–Asia collision) [Davy 1992, pp. 1-1].
- **Model setup:** A layered sandwich representing the lithosphere: a brittle upper layer (uncemented quartz sand) over two silicone putty layers (different viscosities and densities, simulating ductile crust and ductile mantle), floating on golden syrup (asthenosphere) [Davy 1992, pp. 1-1].
- **Deformation:** A rectangular wedge was pushed into the system at constant velocity, producing buckling in front of the indenter and penetrative planar deformation at large distances [Davy 1992, pp. 1-1].
- **Experiments analysed:** Seven experiments at the same deformation stage, each differing in the strength (viscosity) of the silicone layers [Davy 1992, pp. 1-2].
- **Measured quantities:** Fault patterns were digitised; the number \(p(l, r) dl\) of faults with length in \([l, l+dl]\) and barycentre in a disk of radius \(r\) was determined. From this the exponents \(a\) and \(b\), and the generalised dimensions \(D_q\) were computed [Davy 1992, pp. 1-1, 1‑2].

## Methods
- **Fault counting:** The joint distribution of fault length and barycentre position within a disk of radius \(r\) was fitted to the form  
  \(p(l, r) dl = (a-1) \, l_{\min}^{a-1} \, N_t \, (r/L)^b \, (l_{\min}/l)^a \, dl\),  
  giving the fractal dimension \(b\) of fault barycentres and the length‑distribution exponent \(a\) (with \(2 < a < 3\) in these experiments) [Davy 1992, pp. 1-1].
- **Capacity dimension** \(D_0 \equiv D_f\): Obtained from the cumulative fault length \(L(r) \propto r^{D_f}\) inside a disk of radius \(r\) [Davy 1992, pp. 1-1].
- **Generalised dimensions** \(D_q\) (for \(q = 0, 1, 2, 3, \dots\)): Computed using the box‑counting method described in Grassberger (1983) and Hentschel & Procaccia (1983); the \(D_q\) characterise the homogeneity of the fractal geometry [Davy 1992, pp. 1-1, 1‑2].
- **Derivation of scaling relations:** The \(q\)‑th moment of the fault length distribution \(L_q(r)\) was evaluated analytically using Eq. (1), separating contributions from faults smaller and larger than the disk radius \(r\) [Davy 1992, pp. 2-3 – 3‑1].

## Key Findings
1. **Difference between \(D_0\) and \(D_{q \ge 1}\):** In all seven experiments, \(D_0\) was significantly smaller than \(D_{q \ge 1}\), while the \(D_{q \ge 1}\) were approximately equal, suggesting an essentially homogeneous fractal structure [Davy 1992, pp. 1-2].
2. **First scaling law – capacity dimension:** \(D_0 \approx b\) is independent of \(a\). A least‑squares fit gave \(b - D_0 = 0.01\,a - 0.07 \approx 0.05\) over the range \(2 < a < 2.5\) [Davy 1992, pp. 1-2].
3. **Second scaling law – higher‑order dimensions:** For \(q \ge 1\) (and more generally for \(2+q > a\)),  
   \(D_q = b + 2 - a\).  
   The experimental fit yielded \(b - D_2 = a - 1.95\), i.e., \(D_2 \approx b + 1.95 - a\), in excellent agreement with the analytical prediction [Davy 1992, pp. 1-2 – 2‑1].
4. **Analytical derivation:** Using Eq. (1), the \(q\)‑th moment \(L_q(r)\) was shown to have two regimes:  
   - For \(2+q \le a\) (including \(q=0\)): \(D_q = b\).  
   - For \(2+q > a\) (including \(q \ge 1\) when \(2 < a < 3\)): \(D_q = b + 2 - a\).  
   This explains both the constancy of \(D_0\) and the dependence of \(D_{q \ge 1}\) on \(a\) [Davy 1992, pp. 2-2 – 3‑1].
5. **Implications for earthquake scaling:** The exponent \(a\) is related to the Gutenberg–Richter \(B\)‑value by \(a = 1 + 3B/c\). Therefore, for a fixed \(b\), the fractal dimension of large faults becomes \(D_q = b + 1 - 3B/c\). The observation of varying \(a\) across experiments with different rheologies reconciles the apparent conflict with the “universal” \(B\)‑value of the single Earth [Davy 1992, pp. 3-1].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Fault patterns are self‑similar; \(p(l, r) dl\) follows Eq. (1). | [Davy 1992, pp. 1-1] | Sand‑silicone‑syrup model; wedge indentation. | \(a_{\min}\) is smallest detectable fault; \(N_t\) total faults larger than \(l_{\min}\). |
| \(D_0\) is systematically lower than \(D_{q \ge 1}\); \(D_{q \ge 1}\) are nearly equal. | [Davy 1992, pp. 1-2, Fig. 1] | Seven experiments with different silicone strengths. | Error bar on \(D_q\) estimated ±0.05. |
| \(b - D_0\) constant around −0.07, independent of \(a\). | [Davy 1992, pp. 1-2, Fig. 2] | \(a\) in range 2–2.5. | Small offset may reflect finite‑size effects. |
| \(b - D_2\) increases linearly with \(a\): \(b - D_2 = a - 1.95\). | [Davy 1992, pp. 1-2, Fig. 2] | Same experiments. | Equivalent to \(D_2 = b + 2 - a\) within error. |
| Analytical derivation gives \(D_q = b\) for \(2+q \le a\) and \(D_q = b+2-a\) for \(2+q > a\). | [Davy 1992, pp. 2-2 – 3‑1] | Eq. (1) assumed; disk‑based moment calculation. | Explains the observed behaviour for \(q=0\) and \(q \ge 1\). |
| Exponent \(a\) fluctuates between 2 and 2.5 in the experiments; literature values for natural faults are 2.1–2.6. | [Davy 1992, pp. 1-2] | Multiple experiments; references listed. | Consistent with Villemin & Sunwoo (1987), Gudmundsson (1987), Hirata (1989), Main et al. (1990). |
| Relationship between \(a\) and Gutenberg–Richter \(B\): \(a = 1 + 3B/c\). | [Davy 1992, pp. 3-1] | From Sornette D. et al. (1991). | \(c\) is a constant (usually the exponent of the moment–magnitude relation). |

## Limitations
- The derived scaling laws were validated only for \(2 \le a \le 3\) as found in the experiments [Davy 1992, pp. 1-1, 2‑2].
- Numerical determination of exponents carries uncertainties (e.g., ±0.05 for \(D_q\), ±0.1 for \(a\)) [Davy 1992, pp. 1-2].
- The small offset \(b - D_0 \approx 0.05\) could be due to a different sensitivity to finite‑size effects [Davy 1992, pp. 1-2].
- The relation \(a = 1 + 3B/c\) links fault length distribution to earthquake statistics but does not imply a universal fractal dimension for all tectonic settings; \(a\) varies with rheology [Davy 1992, pp. 3-1].

## Assumptions / Conditions
- **Model assumptions:** The laboratory lithosphere is a brittle‑ductile sandwich scaled for gravity; the results are applicable to continental‑collision settings [Davy 1992, pp. 1-1].
- **Self‑similarity:** The fault patterns are assumed to be self‑similar and can be described by Eq. (1) [Davy 1992, pp. 1-1].
- **Disk‑based measurement:** Fractal dimensions are derived from faults whose barycentres lie within a disk of radius \(r\); the contribution of larger faults is taken as proportional to \(r\) [Davy 1992, pp. 2-1].
- **Range of \(a\):** The analytical regime \(2+q > a\) holds for \(q \ge 1\) only if \(a < 3\), a condition satisfied in all experiments and in most natural fault systems [Davy 1992, pp. 1-2, 2‑2].

## Key Variables / Parameters
- **\(a\)**: Exponent of the fault length distribution; governs the relative abundance of large faults. Range 2–2.5 in experiments, 2.1–2.6 in nature [Davy 1992, pp. 1-1, 1‑2].
- **\(b\)**: Fractal (capacity) dimension of fault barycentres; equals \(D_0\) to a good approximation [Davy 1992, pp. 1-1, 1‑2].
- **\(D_q\)**: Generalised fractal dimension of order \(q\); for \(q \ge 1\) they are essentially equal in the experiments [Davy 1992, pp. 1-2].
- **\(N_t\)**: Total number of faults larger than \(l_{\min}\) in the system of size \(L\) [Davy 1992, pp. 1-1].
- **\(L\)**: System size [Davy 1992, pp. 1-1].
- **\(B\)**: Gutenberg–Richter \(b\)‑value (not to be confused with the barycentre dimension \(b\)) [Davy 1992, pp. 3-1].

## Reusable Claims
1. **Claim:** For self‑similar fault patterns described by Eq. (1), the capacity dimension \(D_0\) equals the fractal dimension \(b\) of fault barycentres, independent of the length‑distribution exponent \(a\).  
   **Conditions:** Self‑similarity holds; \(a\) in the range 2–3.  
   **Limitations:** A small systematic offset ≈0.05 may be present due to finite‑size effects.  
   **Source:** [Davy 1992, pp. 1-2, 2‑2].
2. **Claim:** For the same fault systems, the higher‑order generalised dimensions (\(q \ge 1\) when \(a \in [2,3)\)) are given by \(D_q = b + 2 - a\).  
   **Conditions:** The fault length distribution follows a power law with exponent \(a\); faults with different lengths share the same geometrical scaling.  
   **Limitations:** The derivation assumes that the fraction of a large fault inside a disk of radius \(r\) scales as \(r\).  
   **Source:** [Davy 1992, pp. 2-2 – 3‑1].
3. **Claim:** Because \(a = 1 + 3B/c\) (from Sornette D. et al., 1991), the fractal dimension of large faults can be written as \(D_q = b + 1 - 3B/c\). This provides a bridge between fault geometry and earthquake statistics.  
   **Conditions:** Applicable only when \(a < 2+q\).  
   **Limitations:** The relationship depends on the constant \(c\), and \(a\) varies with tectonic rheology; hence the derived \(D_q\) is not universal.  
   **Source:** [Davy 1992, pp. 3-1].

## Candidate Concepts
- [[fault length distribution exponent]]
- [[fractal dimension of fault barycenters]]
- [[generalized fractal dimensions Dq]]
- [[capacity dimension D0]]
- [[homogeneous fractals]]
- [[Gutenberg-Richter b-value relation]]
- [[box-counting method]]
- [[self-similar fault patterns]]
- [[brittle-ductile sandwich model]]
- [[fractal growth processes]]

## Candidate Methods
- [[laboratory sand-silicone collision experiments]]
- [[box-counting for multifractal dimensions]]
- [[joint length-barycenter distribution measurement]]
- [[qth moment calculation for fractal analysis]]
- [[disk-based cumulative length scaling]]

## Connections To Other Work
- **Observations of natural fault fractals:** Okubo & Aki (1987), Aviles et al. (1987), Scholz & Cowie (1990). These studies report self‑similar fault patterns, motivating the laboratory investigation [Davy 1992, pp. 1-1].
- **Fault length distributions in nature:** Villemin & Sunwoo (1987), Gudmundsson (1987), Hirata (1989), Main et al. (1990) report \(a\) in the range 2.1–2.6, consistent with the experimental range 2–2.5 [Davy 1992, pp. 1-2].
- **Previous attempts to link fractal dimensions and \(B\)‑values:** Aki (1981), King (1983), Turcotte (1989). These attempts are described as misleading because they use only the \(B\)‑value (hence only \(a\)) without the second geometrical exponent \(b\) [Davy 1992, pp. 3-1].
- **Fractal growth models:** The formation of fault patterns is compared to fractal growth processes, providing a mechanism for the appearance of homogeneous fractals (Sander 1986; Niemeyer et al. 1984) [Davy 1992, pp. 3-1].
- **Previous experimental and theoretical work by the same group:** Sornette A. et al. (1990), Davy et al. (1990), Sornette D. et al. (1991). These papers describe the experimental setup, the fault growth model, and the dispersion of \(b\)‑values [Davy 1992, pp. 1-1, 1‑2, 3‑1].

## Open Questions
- The presented scaling laws are derived for the specific regime \(2 \le a \le 3\). It is not confirmed how they extend when \(a\) lies outside this range.
- The experiments used a fixed indentation geometry and a layered brittle‑ductile system. Whether the relation \(D_q = b + 2 - a\) holds for other tectonic settings (e.g., distributed extension) remains an open question.
- The physical mechanism that sets the exponent \(a\) in the experiments is not discussed in detail; controlling parameters (layer viscosities, thicknesses) are identified as influencing \(a\), but a predictive model is not provided.
- The small but systematic offset between \(b\) and \(D_0\) warrants further investigation to discriminate between finite‑size effects and a genuine geometrical difference.

## Source Coverage
All indexed non‑empty source blocks (5 fragments) were processed, covering 5 of 5 blocks (100%). The total indexed character count was 21,669, of which 21,463 characters (99.05%) are included in the compiled fragments. No additional sources were used.
