---
type: "paper"
paper_id: "2003-darcel-cross-correlation-between-length-and-position-in-real-fracture-networks"
title: "Cross-correlation between Length and Position in Real Fracture Networks."
status: "draft"
source_pdf: "data/papers/2003 - Cross-correlation between length and position in real fracture networks.pdf"
citation: "Darcel, C., O. Bour, and P. Davy. \"Cross-correlation between Length and Position in Real Fracture Networks.\" *Geophysical Research Letters*, vol. 30, no. 12, 2003, p. 1650, doi:10.1029/2003GL017174."
indexed_texts: "5"
indexed_chars: "24226"
compiled_at: "2026-04-27T19:30:09"
---

# Cross-correlation between Length and Position in Real Fracture Networks.

## One-line Summary

By analyzing local geometrical properties of a dense multiscale fracture pattern, the study shows a positive correlation between fracture length and its mean distance to the nearest neighbor, following a power law \(d_c \propto l^{0.3}\), and an anisotropic shield area around each fracture whose long axis scales as \(l^{0.25-0.3}\) while the short axis is invariant [Darcel 2003, pp. 1-1, 4-4]。

## Research Question

Characterize statistically the correlations between the length and position of a fracture within a complex population of cracks, motivated by the fact that fracture length is a critical parameter for fracture growth (stress intensity factor varies as square root of length), but few studies have tried to characterize its role in fracture development in a complex population [Darcel 2003, pp. 1-1].

## Study Area / Data

Fracture data come from the Hornelen fracture network (Norway), consisting of seven fracture maps at different system sizes (T) within a 720 m × 720 m region, sampled from a self-similar system [Darcel 2003, pp. 2-3, Figure 1]. The data were provided by N. Odling [Darcel 2003, pp. 4-4].

## Methods

1. **Center-to-center distance**: For each fracture, the average distance to its nearest neighbor, \(d_c(l)\), is computed as a function of fracture length \(l\) [Darcel 2003, pp. 1-2].
2. **Shield area**: The average area around each fracture center within which no other fracture portion is lying is measured as a function of direction \(\theta\), yielding an ellipsoidal shape with axes \(d_k\) (parallel to fracture strike) and \(d_\perp\) (perpendicular to strike) [Darcel 2003, pp. 3-4].
3. **Normalization**: To compare across maps, \(d_c(l,T)\) is normalized by \(d_{min}(T)\) (the point-to-point distance in the absence of correlation), and length by \(l_{min}(T)\) [Darcel 2003, pp. 2-3].

## Key Findings

- There is a positive correlation between fracture position and fracture length: larger fractures are more isolated, with a larger distance from their center to the nearest neighbor [Darcel 2003, pp. 1-2]. The mean average distance scales as \(d_c(l) \propto l^{0.3}\) for small lengths over about one order of magnitude; for larger lengths, \(d_c\) is approximately constant (uncorrelated case) [Darcel 2003, pp. 2-3].
- The shield area is ellipsoidal: the long axis along fracture strike, \(d_k(l,T)\), increases as a power law with exponent \(\gamma = 0.25 \pm 0.05\); the short axis perpendicular to strike, \(d_\perp(l,T)\), is about constant with \(l\) and equal to the average size of non-fractured blocks (consistent with uncorrelated systems) [Darcel 2003, pp. 3-4].
- At small scale (< 1 m, which is bed thickness), the shield area is isotropic [Darcel 2003, pp. 1-1].
- For small fractures, \(d_k > l/2\) (fractures appear isolated and locally unconnected); for large fractures, \(d_k < l/2\) (fractures are on average locally connected) [Darcel 2003, pp. 3-4].
- The measured exponent ~0.3 for \(d_c\) is weak but consistent with the expected 0–1 range; randomization of lengths (keeping positions fixed) yields exponent 0, confirming correlation significance [Darcel 2003, pp. 2-3].

## Limitations

- **Resolution effects** due to varying system size \(T\) offset the curves of \(d_c\); the variations are simply due to resolution limits that vary from map to map [Darcel 2003, pp. 1-2].
- For the 18×18 m map, the exponent for \(d_k\) is slightly smaller than for other maps [Darcel 2003, pp. 3-4].
- An anisotropic shield shape and scaling may be modified by resolution effects, and an isotropic point can only be extrapolated from trends [Darcel 2003, pp. 3-4].
- The study only analyzes a single fracture network (Hornelen); generalization to other networks is not validated in the given fragments [未从索引片段中确认].

## Reusable Claims

- "The mean distance between a fracture center and its nearest neighbor is correlated to its length such as \(d_c \propto l^{0.3}\)." [Darcel 2003, pp. 1-1]
- "The long axis of the ellipsoidal shield area, along fracture strike, is correlated to \(l\) such as \(d_k \propto l^{0.25-0.3}\). The short axis remains invariant, about equal to the equivalent distance in a random fractal." [Darcel 2003, pp. 1-1]
- "At small scale (i.e., less than 1 m which is bed thickness) the shield area is isotropic." [Darcel 2003, pp. 1-1]
- "For the largest fractures, \(d_k < l/2\), meaning that fractures are in average locally connected." [Darcel 2003, pp. 3-4]
- "The absence of a statistical correlation between the position and length implies no relationship between distance to nearest neighbor and fracture length." [Darcel 2003, pp. 1-2]
- "An exponent of about 0.3 implies relatively weak correlations, but consistent with the expected range between 0 (uncorrelated) and 1 (apollonian model)." [Darcel 2003, pp. 2-3]

## Candidate Concepts

- [[fracture network]]
- [[dense multiscale fracture pattern]]
- [[center-to-center distance]]
- [[shield area]] (ellipsoidal, strike-aligned)
- [[self-similar fracture system]]
- [[random fractal]]
- [[Apollonian model]]
- [[stress interactions during fracture growth]]
- [[fracture length correlation]]
- [[resolution effect]]
- [[non-fractured block size]]
- [[positon-length cross-correlation]]

## Candidate Methods

- [[nearest neighbor analysis (center-to-center)]]
- [[normalization by d_min and l_min]]
- [[randomization test]] (shuffling lengths while fixing positions to test correlation)
- [[power-law scaling fit]] (exponent extraction)
- [[shield area computation]] (angular distance to nearest fracture in direction θ)

## Open Questions

- What is the physical mechanism linking the observed power-law exponents (0.3 for distance, 0.25 for long axis) to stress interactions during fracture growth? [未从索引片段中确认]
- How generalizable are these correlations to other fracture networks (e.g., tectonic faults, joints in different lithologies)? [未从索引片段中确认]
- Can the isotropic point (where \(d_k = d_\perp\)) be reliably determined, and does it correspond to a specific physical scale? [未从索引片段中确认]

## Source Coverage

- **p. 1-1**: Abstract and introduction: correlation of distance and length, shield area anisotropy, isotropic at small scale, stress constraints.
- **p. 1-2**: Method of center-to-center distance \(d_c\), absence of correlation implies constant \(d_c\), observation of positive correlation, resolution effects.
- **p. 2-3**: Normalization procedure (Fig 3), exponent 0.3 for small lengths, constant for large lengths, randomization test validates exponent.
- **p. 3-4**: Shield area ellipsoid, long axis scaling \(l^{0.25\pm0.05}\), short axis constant, isotropic point, connection threshold \(l/2\).
- **p. 4-4**: Conclusion: \(d_k \propto l^{0.25}\), \(d_\perp\) uncorrelated equal to block size, interpreted as remote mechanical interactions. Acknowledgments and references.
