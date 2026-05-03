---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-snowdon-analysis-of-crystalline-rock-permeability-versus-depth-in-a-canadian-precambrian-ro"
title: "Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting."
status: "draft"
source_pdf: "data/papers/2021 - Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Snowdon, Andrew P., et al. \"Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.\" *Earth and Space Science*, vol. 8, no. 8, 2021, e2020EA001610."
indexed_texts: "22"
indexed_chars: "109446"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "108972"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.995669"
coverage_status: "full-index"
source_signature: "dd0b1ccc0eac502ed32acf77d79e352036a054c2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:54:16"
---

# Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.

## One-line Summary
This study compiles and analyzes historical AECL hydrogeologic data to develop novel five-parameter logistic functions describing the mean permeability versus depth relationships for equivalent porous media (EPM) rock mass and fracture zones (FZs) within plutonic Precambrian crystalline rocks of the Canadian Shield [Snowdon 2021, pp. 1-1].

## Research Question
How does permeability vary with depth in Precambrian plutonic crystalline rock within the Canadian Shield for both the equivalent porous media (EPM) rock mass and fracture zones (FZs), and can a generalized quantitative relationship be developed from historical data? [Snowdon 2021, pp. 1-2].

## Study Area / Data
The study area encompasses seven AECL research areas (RAs) on the Canadian Shield, with quantitative data from five: Chalk River (Grenville Province, quartz monzonitic orthogneisses/paragneisses), East Bull Lake (Superior/Southern Province border, gabbro-anorthosite), Atikokan (Superior Province, biotite-hornblende granite), Whiteshell (Superior Province, Lac du Bonnet Batholith granite), and the Underground Research Laboratory (URL) (associated with Whiteshell RA) [Snowdon 2021, pp. 3-6]. Data were compiled from over 100 technical reports, journal articles, and conference proceedings written between 1975 and 1996 [Snowdon 2021, pp. 1-1]. An initial dataset of 549 permeability records was extracted from a global database by Achtziger-Zupančič et al. (2017) and supplemented with additional AECL data including fracture details [Snowdon 2021, pp. 6-6].

## Methods
The methodology involves data compilation, categorization, and analysis.

1.  **Data Compilation**: Permeability records were compiled. Missing temperature data were inferred using linear extrapolation from available RA-specific temperature gradients (e.g., 9.9°C/km at URL, 10.09°C/km at Whiteshell) [Snowdon 2021, pp. 6-8]. Depth-specific density and dynamic viscosity were calculated using methods from Batzle and Wang (1992) based on temperature, pressure, and TDS. TDS was determined from a linear trend fitted to 516 data points up to 1,600 mBGS and constant at 300 g/L below that [Snowdon 2021, pp. 7-7].
2.  **Data Categorization**: Based on AECL borehole logs (television and acoustic televiewer), data were classified into three categories: (a) **Equivalent Porous Media (EPM)** rock mass: intact rock, sealed/infilled fractures, and limited connectivity fractures [Snowdon 2021, pp. 1-2, 8-8]; (b) **Fracture Zones (FZs)**: domains of enhanced permeability with extensive hydraulically connected fractures [Snowdon 2021, pp. 1-2]; (c) **Aggregate Media (AM)**: the complete dataset combining EPM and FZ data [Snowdon 2021, pp. 1-1, 1-2].
3.  **Data Analysis**: A 200 m moving average window was applied to log10-transformed permeability values to identify a trend [Snowdon 2021, pp. 8-9]. Extreme outliers were identified and removed using the Interquartile Method (IQR) with a factor of 3 [Snowdon 2021, pp. 9-9]. A novel five-parameter logistic growth curve (Equation 6) was fit to the resulting mean permeability versus depth trend [Snowdon 2021, pp. 9-10]. The statistical significance of the fitted functions was evaluated using p-values and a normalized sensitivity analysis [Snowdon 2021, pp. 10-10, 13-15].

## Key Findings
- **Permeability Decreases with Depth**: Both EPM rock mass and FZ permeability generally decrease with depth. EPM rock mass exhibits a sharp decrease above 500 mBGS, while FZ permeability decreases more gradually over 1,000 m [Snowdon 2021, pp. 9-9, 15-15].
- **Quantitative Difference**: Fracture zone permeability is at least two orders-of-magnitude higher than EPM rock mass permeability at all depths, and their permeability ranges do not overlap even at depth [Snowdon 2021, pp. 15-15, 16-16].
- **Novel Fitting Function**: A five-parameter logistic function (Equation 6) effectively quantifies the mean permeability-depth relationship, outperforming power law and simple logarithmic functions, particularly at shallow depths [Snowdon 2021, pp. 11-13, 14-15]. The logistic function has the form:
  \[
  \log_{10}(k) = \frac{\alpha - \beta}{1 + \left(\frac{d}{\gamma}\right)^\delta} ^{\epsilon} + \beta
  \]
  where \(k\) is permeability, \(d\) is depth, and \(\alpha, \beta, \gamma, \delta, \epsilon\) are fitting parameters [Snowdon 2021, pp. 9-10].
- **Fitted Parameters**: The fitted parameters for the EPM rock mass, FZs, and AM are provided in Table 1 of the source paper. The R² values for the logistic function fits to the moving average are 0.9465 (EPM), 0.9424 (AM), and 0.9631 (FZ) [Snowdon 2021, pp. 13-15].
- **Permeability Limits**: The raw data suggests a lower limit of approximately \(10^{-21} \text{ m}^2\) for EPM rock mass and \(10^{-19} \text{ m}^2\) for FZs, which may be related to equipment limitations [Snowdon 2021, pp. 9-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Five-parameter logistic function (Eq. 6) fits the mean permeability-depth trend. | [Snowdon 2021, pp. 15-16] | Canadian Shield Precambrian plutonic rock. | For EPM, R²=0.9465; for FZs, R²=0.9631. |
| Fracture zone permeability is >2 orders-of-magnitude higher than EPM rock mass. | [Snowdon 2021, pp. 15-16] | All investigated depths at AECL research areas. | Permeability ranges do not overlap even at depth. |
| EPM rock mass permeability decreases sharply above 500 mBGS. | [Snowdon 2021, pp. 15-15] | Canadian Shield plutons. |
| A power law or logarithmic function cannot appropriately represent permeabilities at shallow depths. | [Snowdon 2021, pp. 11-13] | Canadian Shield data. | These functions approach infinity (asymptote) at the surface. |
| Outliers identified using IQR method | [Snowdon 2021, pp. 13-13] | A 200 m moving window, outlier factor = 3*IQR. | 7 extreme outliers in EPM data, 3 in FZ data. |
| A 200m moving window was chosen for mean calculation. | [Snowdon 2021, pp. 9-9] | Window length chosen as a balance between smoothing and noise. | Window lengths of 50m and 100m were too noisy; 500m did not fit the data well. |

## Limitations
- The data were collected from research areas chosen to represent typical Canadian Shield plutons, not actual candidate sites for a DGR; the reported relationships are general and not site-specific [Snowdon 2021, pp. 1-1].
- The lower limit of permeability in the data (\(10^{-21} \text{ m}^2\) for EPM) may represent a limitation of the field testing equipment rather than an actual rock property [Snowdon 2021, pp. 9-10].
- The gneissic rock trend in the rock-type analysis appears truncated due to sparse measurements at depth, making it potentially unrepresentative of deep conditions [Snowdon 2021, pp. 10-11].
- Some data points appear to be misclassified between EPM and FZ data sets, or are outliers that were not explicitly identified as fracture zones in original AECL reports [Snowdon 2021, pp. 9-10].
- The aggregate media (AM) category cannot represent the discrete physics of fracture zones in a model [Snowdon 2021, pp. 1-2].

## Assumptions / Conditions
- All research areas are located on plutons within the Canadian Shield and are considered geologically stable, representative of Precambrian crystalline rock [Snowdon 2021, pp. 1-1, 3-5].
- The EPM rock mass domain includes intact rock, sealed/infilled fractures, and hydraulically disconnected fractures, and it is assumed that finite nonconductive fractures affect the EPM's aggregate hydrological properties [Snowdon 2021, pp. 1-2, 8-8].
- For converting hydraulic conductivity to permeability, missing temperature data was inferred via linear extrapolation; TDS concentration was assumed to follow a linear trend with depth to 1,600 mBGS and constant at 300 g/L below that; fluid density and viscosity were calculated based on models by Batzle and Wang (1992) [Snowdon 2021, pp. 6-8].
- For a permeability measurement from a packer test over a borehole interval, the measured value is assumed to be uniform over that entire interval [Snowdon 2021, pp. 8-9].

## Key Variables / Parameters
- **Permeability (\(k\))**: [m²], the primary variable of interest [Snowdon 2021, pp. 1-2].
- **Depth (\(d\))**: [m], specified in meters below ground surface (mBGS) [Snowdon 2021, pp. 9-10].
- **Rock Category**: EPM rock mass, Fracture Zone (FZ), or Aggregate Media (AM) [Snowdon 2021, pp. 1-1].
- **Logistic Function Parameters (\(\alpha, \beta, \gamma, \delta, \epsilon\))**: Parameters defining the fitted logistic curve where \(\alpha\) is the log10 mean permeability at surface, \(\beta\) is the log10 mean permeability at infinite depth, \(\gamma\) is the inflection depth, \(\delta\) is the rate of decrease, and \(\epsilon\) shifts the curve's symmetry [Snowdon 2021, pp. 9-10, 13-15].
- **Fluid Properties**: Temperature (°C), Total Dissolved Solids (TDS) [g/L], fluid density (\(\rho\)) [g/cm³], dynamic viscosity (\(\eta\)) [cP] [Snowdon 2021, pp. 6-8].
- **Rock Type**: Granite, gneiss, gabbro [Snowdon 2021, pp. 10-11].

## Reusable Claims
- Mean permeability versus depth for EPM rock mass and fracture zones in Canadian Shield plutonic rock can be effectively modeled with a five-parameter logistic function, unlike power law or simple logarithmic functions that fail at shallow depths [Snowdon 2021, pp. 11-13, 15-16].
- Fracture zone permeability in Precambrian crystalline rock is consistently >2 orders-of-magnitude higher than EPM rock mass permeability, and their ranges do not overlap at any depth [Snowdon 2021, pp. 15-16].
- In this Precambrian setting, EPM rock mass permeability decreases sharply above 500 mBGS and more slowly at depth, whereas FZ permeability decreases more gradually to a depth of over 1,000 m before reaching its lower bound [Snowdon 2021, pp. 15-15].
- Using an aggregate media (AM) approach that does not separate FZs from EPM rock mass results in a permeability-depth relationship biased toward the EPM curve, due to the much larger number of EPM data points [Snowdon 2021, pp. 15-16].
- The lower limit of measurable permeability in the compiled dataset is ~\(10^{-21} \text{ m}^2\) for the EPM rock mass, which may be an instrument limitation rather than a true rock property [Snowdon 2021, pp. 9-10].

## Candidate Concepts
- [[Fracture reservoir]] / [[Fractured media]]
- [[Deep Geologic Repository (DGR)]]
- [[Equivalent Porous Media (EPM)]]
- [[Fracture Zone]]
- [[Permeability-depth relationship]]
- [[Canadian Shield]]
- [[Crystalline rock]]
- [[Atomic Energy of Canada Limited (AECL)]]
- [[Nuclear Fuel Waste Management]]

## Candidate Methods
- [[Data Compilation and Harmonization]]
- [[Hydraulic conductivity to permeability conversion]]
- [[Interquartile Method (IQR) for Outlier Detection]]
- [[Moving Average Window Analysis]]
- [[Five-parameter Logistic Curve Fitting]]
- [[Normalized Sensitivity Analysis]]
- [[Batzle and Wang (1992) fluid property calculation]]

## Connections To Other Work
- This work expands on the global permeability database of Achtziger-Zupančič et al. (2017) by adding detailed fracture information for Canadian Shield sites [Snowdon 2021, pp. 6-6].
- The study contrasts its novel logistic fit with power-law functions typically used for hydrological processes [Snowdon 2021, pp. 8-8] and logarithmic functions used in previous permeability-depth studies by Manning and Ingebritsen (1999), Ingebritsen and Manning (2010), and Achtziger-Zupančič et al. (2017) [Snowdon 2021, pp. 8-8, 15-15].
- The findings align with the statement by W. Sanford (2017) that the decreasing trend of permeability with depth had not been well quantified [Snowdon 2021, pp. 2-2].

## Open Questions
- Is the observed lower permeability limit (\( \sim 10^{-21} \text{ m}^2 \) for EPM) a rock property or an equipment limitation? [Snowdon 2021, pp. 9-10]
- Can the shape of the five-parameter logistic function be predicted from maximum and minimum permeability and a measure of how quickly permeability approaches the minimum, without needing a full dataset to fit? [Snowdon 2021, pp. 13-15]
- Without additional deep data for gneissic and gabbroic rocks, is the generalized trend truly representative of all rock types in the Canadian Shield? [Snowdon 2021, pp. 10-11]

## Source Coverage
All nonempty indexed fragments were processed. This page was compiled from 22 indexed source blocks (109,446 characters), achieving a coverage ratio of 1.0 by blocks and approximately 0.996 by characters. The compilation utilized a single-pass strategy from a fully indexed source.
