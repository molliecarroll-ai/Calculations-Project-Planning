---
name: s1-process-emissions
description: >-
  Scope 1 industrial process emissions methodology: cement clinker and
  calcination CO2, lime, glass, soda ash, ammonia production, iron & steel
  carbon balance, aluminum smelting PFCs (CF4/C2F6 anode effects), nitric and
  adipic acid N2O, semiconductor fluorinated gases (CF4, NF3, SF6, CHF3),
  hydrogen production. Use for CEMS vs. stoichiometric mass balance vs. IPCC
  Tier 1 production-based methods, process-vs-combustion classification at the
  same facility, feedstock vs. fuel carbon, and abatement/destruction credits
  (N2O catalytic destruction, HFC-23 abatement). Covers IPCC 2006 Vol. 3
  (IPPU) defaults and sector tools (WBCSD-CSI/GCCA cement, IAI aluminum,
  worldsteel).
---

# Scope 1 — Industrial Process Emissions

Process emissions arise from chemical or physical transformation of materials
— not from fuel combustion for energy: calcination of carbonates (cement,
lime, glass, soda ash), reduction of ores and use of carbon anodes/electrodes
(steel, aluminum, ferroalloys), catalytic oxidation byproducts (nitric/adipic
acid N2O), feedstock conversion (ammonia, hydrogen, methanol), and fluorinated
gas use in etching/deposition (semiconductors). Gases: CO2, N2O, PFCs
(CF4/C2F6), SF6, NF3, HFC-23. Governing documents: GHG Protocol Corporate
Standard ch. 4; IPCC 2006 Guidelines vol. 3 (IPPU) with the 2019 Refinement;
sector calculation tools (WBCSD-CSI/GCCA Cement CO2 and Energy Protocol, IAI
Aluminium Sector GHG Protocol, worldsteel CO2 methodology); 40 CFR Part 98
sector subparts. Cross-cutting conventions (GWP sets, boundaries, EF
hierarchy, answering style) live in the `ghg-protocol` skill — follow them
rather than restating them here.

## Boundary & classification

- **Process vs. combustion at the same facility.** Split every plant's scope 1
  into stationary combustion (fuel burned for energy → `s1-stationary-
  combustion`) and process emissions (this skill), even when both occur in the
  same device. Canonical example: a cement kiln — coal/petcoke/alternative
  fuels burned to heat the kiln = **stationary combustion**; CO2 released by
  calcining CaCO3 in the raw meal = **process**. Report both in scope 1 but
  calculate and disclose them separately; national reporting (Part 98 subpart
  H) and the sector tools require the split. Same logic for lime kilns, glass
  furnaces (fuel vs. carbonate batch), and steel (fuel vs. reductant).
- **Feedstock vs. fuel use of fossil inputs.** When natural gas, coal, or
  petcoke enters the process as a **feedstock or reductant** (natural gas
  reformed to H2/NH3, coke reducing iron ore, anode carbon in aluminum
  cells), the resulting CO2 is a process emission — do not also count that
  same carbon under fuel combustion. Take feedstock quantities out of the
  fuel-combustion activity data or the carbon is double counted. Carbon
  **stored in products** (urea, methanol, carbon black, plastics) is
  subtracted from the process balance and accounted where released (if ever).
- **Abatement/destruction credits.** Emissions may be reduced for gases
  destroyed on site (N2O catalytic/thermal decomposition, HFC-23 thermal
  oxidation, semiconductor point-of-use abatement) **only** with a documented
  destruction efficiency and abatement-system uptime; credit = EF × DF ×
  utilization, never a blanket "abated" flag. Unverified vendor DE claims are
  a classic audit finding — use measured DE or conservative defaults, and
  never credit downtime hours.
- **CO2 captured or transferred**: CO2 recovered for urea, carbonation, or
  sale is deducted from process emissions only per the applicable rules
  (IPCC treats urea CO2 as stored until urea use; sold CO2 that is later
  released is not automatically deductible under the Corporate Standard —
  disclose treatment). CCS accounting requires the storage chain to be
  documented; flag rather than resolve silently.
- **Routing notes**: on-site wastewater/landfill CH4 → `s1-fugitive-emissions`
  (or classify as process — be consistent); F-gas leakage from refrigeration
  at an industrial site → `s1-fugitive-emissions`; purchased clinker (not
  produced) → scope 3 category 1. Biogenic carbonate/biomass carbon in the
  process (rare) → biogenic line per the `ghg-protocol` skill §5.

## Method ladder

| Tier | Method | Data basis | Use when |
|---|---|---|---|
| 1 | CEMS (continuous emissions monitoring) | Measured stack concentration × flow | CEMS installed and QA'd (Part 75/98 quality); large regulated plants |
| 2 | Stoichiometric / site mass balance | Production output or raw-material inputs with measured composition | Plant-level production and chemistry data exist (the sector-tool default) |
| 3 | Production × IPCC Tier 1 default EF | Product tonnage only | No composition data; screening; smaller plants |
| 4 | Capacity / benchmark estimation | Nameplate capacity × utilization × sector intensity | No production data (e.g., pre-acquisition screening) |

### Tier 1 — CEMS

**When:** a certified CO2 (or N2O) CEMS with stack-flow monitoring exists —
common at US cement, acid, and power-adjacent plants under 40 CFR Part 98/75.
**Data:** hourly concentration (%CO2 or ppm N2O) × volumetric flow, summed.

```
E = Σ_hours (C_gas × Q_stack × ρ_gas)     # concentration × flow × density
```

**Pitfall:** CEMS measures the **combined** stack — combustion + process CO2
together. To report the split, subtract calculated combustion CO2 (fuel data ×
EF) from the CEMS total, or use the sector tool's allocation. Missing-data
substitution rules (Part 75) must be applied, not zeros. Biomass-derived CO2
in the stack must be separated to the biogenic line (fuel records or ASTM
D6866 sampling).

### Tier 2 — Stoichiometric mass balance (sector-tool method)

**When:** production quantities and material chemistry are known. This is the
default in the sector tools and Part 98; uncertainty ±2–7% typically.

**Cement — clinker (output) method** (WBCSD-CSI/GCCA protocol; IPCC Tier 2):

```
E_CO2 = Clinker_t × EF_clinker + CKD_correction

EF_clinker = CaO_fraction × (44.01/56.08) + MgO_fraction × (44.01/40.30)
           ≈ 0.65 × 0.785 = 0.51 t CO2/t clinker for 65% CaO (site-measured
             CaO/MgO from raw-meal or clinker analysis; correct for
             non-carbonate Ca/Mg sources such as slag or fly ash)
CKD_correction: CO2 from calcined cement-kiln dust leaving the kiln system,
             typically +1.5–2% (IPCC default correction factor 1.02 if
             unmeasured — 2006 vintage, verify)
```

**Cement/lime/glass — carbonate input method** (IPCC Tier 3 form):

```
E_CO2 = Σ_i (M_carbonate,i × EF_i × F_calcination,i)
EF_CaCO3 = 0.4397 t CO2/t carbonate;  EF_MgCO3 = 0.5220 t CO2/t carbonate
(stoichiometric, exact); F_calcination usually 1.00 (complete)
```

**Ammonia — feedstock carbon balance** (IPCC 2006 vol. 3 ch. 3.2):

```
E_CO2 = Feedstock_t (or GJ) × C_content × (44.01/12.011) − CO2_recovered_for_urea

CO2 stored in urea = Urea_t × (44.01/60.06) ≈ 0.733 t CO2/t urea
(that carbon is accounted for on urea use — downstream or scope 3;
disclose the treatment)
```

**Iron & steel — site carbon balance** (worldsteel method; IPCC Tier 2):

```
E_CO2 = [Σ C_inputs − Σ C_outputs] × (44.01/12.011)
C_inputs:  coke, coal, natural gas (reductant share), electrodes, charged
           scrap/DRI/hot metal carbon, limestone/dolomite flux carbon
C_outputs: carbon in crude steel (~0.1–1%), slag, sold coke-oven/blast-furnace
           gas, tar and other sold byproducts
```

**Worked example (cement, clinker method):** plant produces 100,000 t clinker;
lab-measured CaO 65.0%, MgO 1.0% (all from carbonates); CKD correction 1.02.

```
EF = 0.650 × 0.785 + 0.010 × 1.092 = 0.510 + 0.011 = 0.521 t CO2/t clinker
E  = 100,000 t × 0.521 × 1.02 = 53,142 t CO2 (process only)
```
Kiln fuel (say 350,000 GJ of coal) is calculated separately as stationary
combustion. **Pitfalls:** using cement instead of clinker tonnage (see traps
below); ignoring non-carbonate CaO in alternative raw materials (overstates);
skipping CKD (understates 1–2%).

**Worked example (ammonia):** 50,000 t NH3 from natural gas conventional
reforming; total feedstock+fuel EF 1.694 t CO2/t NH3 (IPCC 2006 Table 3.1
default, modern plant — verify); 30,000 t urea produced on site.

```
Gross:            50,000 × 1.694            = 84,700 t CO2
Stored in urea:   30,000 × 0.733            = 21,990 t CO2
Net process CO2:  84,700 − 21,990           = 62,710 t CO2
```

### Tier 3 — Production × IPCC Tier 1 default EF

**When:** only product tonnage is known. **Data:** annual production per
product. All defaults below are **IPCC 2006 GL vol. 3 (2006 vintage; check
the 2019 Refinement and current national factors before use):**

```
E = Production_t × EF_default   (per gas; convert N2O/PFCs to CO2e with the
                                 inventory's GWP set — `ghg-protocol` skill §4)
```

| Product / process | Default EF | Source table |
|---|---|---|
| Cement clinker | 0.52 t CO2/t clinker (incl. 2% CKD) | IPCC 2006 v3 ch. 2.2 |
| Lime — high-calcium | 0.75 t CO2/t lime | IPCC 2006 v3 Table 2.4 |
| Lime — dolomitic | 0.77 t CO2/t lime | IPCC 2006 v3 Table 2.4 |
| Glass (unadjusted batch) | 0.20 t CO2/t glass × (1 − cullet ratio) | IPCC 2006 v3 ch. 2.4 |
| Soda ash — natural (trona) production | 0.097 t CO2/t soda ash | IPCC 2006 v3 ch. 2.5 |
| Soda ash — use (consumption) | 0.415 t CO2/t consumed | IPCC 2006 v3 ch. 2.5 |
| Ammonia (nat. gas, conventional reforming) | 1.694 t CO2/t NH3 | IPCC 2006 v3 Table 3.1 |
| Nitric acid N2O — high-pressure plant | 9 kg N2O/t HNO3 | IPCC 2006 v3 Table 3.3 |
| Nitric acid N2O — medium-pressure | 7 kg N2O/t HNO3 | IPCC 2006 v3 Table 3.3 |
| Nitric acid N2O — atmospheric/low-pressure | 5 kg N2O/t HNO3 | IPCC 2006 v3 Table 3.3 |
| Nitric acid N2O — with NSCR abatement | 2 kg N2O/t HNO3 | IPCC 2006 v3 Table 3.3 |
| Iron & steel — BOF crude steel | 1.46 t CO2/t steel | IPCC 2006 v3 Table 4.1 |
| Iron & steel — EAF crude steel | 0.08 t CO2/t steel | IPCC 2006 v3 Table 4.1 |
| Pig iron (not processed to steel) | 1.35 t CO2/t | IPCC 2006 v3 Table 4.1 |
| Aluminum — anode CO2, prebake (CWPB) | 1.6 t CO2/t Al | IPCC 2006 v3 Table 4.10 |
| Aluminum — anode CO2, Søderberg | 1.7 t CO2/t Al | IPCC 2006 v3 Table 4.10 |
| Aluminum PFC Tier 1 — CWPB | 0.4 kg CF4/t Al; 0.04 kg C2F6/t Al | IPCC 2006 v3 Table 4.15 |

**Aluminum PFC Tier 2 — slope method** (preferred whenever anode-effect
process data exist; IAI/IPCC Table 4.16, 2006 vintage — verify):

```
CF4_kg/t Al  = S_CF4 × AEM          # AEM = anode-effect minutes per cell-day
C2F6_kg/t Al = CF4 × F_C2F6/CF4

CWPB:  S_CF4 = 0.143 kg CF4/t Al per AEM;  F = 0.121
SWPB:  S_CF4 = 0.272;                      F = 0.252
VSS:   S_CF4 = 0.092;                      F = 0.053
```

**Worked example (aluminum smelter):** 200,000 t Al, CWPB technology,
measured AEM = 0.50 anode-effect minutes/cell-day:

```
CF4:  0.143 × 0.50 = 0.0715 kg/t × 200,000 t = 14,300 kg = 14.30 t CF4
C2F6: 14,300 × 0.121 = 1,730 kg = 1.73 t C2F6
CO2e (AR6): 14.30 × 7,380 + 1.73 × 12,400 = 105,534 + 21,452 ≈ 126,986 t
CO2e (AR5): 14.30 × 6,630 + 1.73 × 11,100 = 94,809 + 19,203  ≈ 114,012 t
Anode CO2:  200,000 × 1.6 = 320,000 t CO2 (process, separate from PFCs)
```

**Nitric acid with abatement** (IPCC 2006 eq. 3.6):

```
E_N2O = P_HNO3 × EF × (1 − DF × ASUF)
DF = destruction factor (measured; NSCR ~0.80–0.90+, catalytic tertiary units
     often >0.90 — use plant-specific test data)
ASUF = abatement system utilization factor (uptime fraction)
```

**Worked example:** 20,000 t HNO3, medium-pressure plant (7 kg N2O/t),
tertiary catalytic abatement with measured DF 0.85 running 90% of production
hours:

```
E_N2O = 20,000 × 7 × (1 − 0.85 × 0.90) = 140,000 × 0.235 = 32,900 kg = 32.9 t N2O
CO2e (AR6) = 32.9 × 273 = 8,982 t CO2e   (AR5: 32.9 × 265 = 8,719 t)
Unabated it would have been 140 t N2O ≈ 38,220 t CO2e (AR6).
```

**Semiconductors:** IPCC 2006 v3 ch. 6 Tier 1 uses default FC emissions per
m² of wafer processed; Tier 2a/2b use gas purchases × (1 − utilization) ×
(1 − abatement DE) per gas per process type, with byproduct CF4 formation
factors. Fabs should use the Tier 2b method with the World Semiconductor
Council / Part 98 subpart I parameters; gases include CF4, C2F6, CHF3, NF3,
SF6 — each converted with its own GWP.

**Pitfalls (all Tier 3):** technology mismatch (using the high-pressure
nitric acid EF for a modern abated plant overstates ~10×); production basis
errors (clinker vs. cement, gross vs. net steel); Tier 1 PFC defaults ignore
actual anode-effect performance and can be badly wrong in either direction.

### Tier 4 — Capacity / benchmark estimation

**When:** no production data (screening, M&A due diligence). Estimate
production = nameplate capacity × sector-typical utilization (e.g., 85–90%
cement in a strong market), then apply Tier 3 EFs; or apply a published
sector intensity benchmark (e.g., GNR/GCCA "Getting the Numbers Right" for
cement ~0.83–0.86 t CO2/t cementitious total incl. fuel; IAI statistics for
aluminum). Label results as order-of-magnitude, data quality 4–5 per the
`ghg-protocol` skill §8, and replace with real production data before formal
reporting.

## Emission factors / parameters quick reference

**Process GWPs, 100-year** (IPCC AR5 2013 w/o feedback; AR6 2021 — verify
current required set):

| Gas | AR5 | AR6 | Main process source |
|---|---|---|---|
| N2O | 265 | 273 | Nitric/adipic acid, caprolactam |
| CF4 (PFC-14) | 6,630 | 7,380 | Aluminum anode effects, semiconductor etch |
| C2F6 (PFC-116) | 11,100 | 12,400 | Aluminum, semiconductors |
| NF3 | 16,100 | 17,400 | Semiconductor/display chamber cleaning |
| SF6 | 23,500 | 25,200 | Magnesium cover gas, semiconductors |
| HFC-23 (CHF3) | 12,400 | 14,600 | HCFC-22 byproduct, semiconductor etch |

**Stoichiometric constants (exact):** CaCO3 → 0.4397 t CO2/t; MgCO3 →
0.5220 t CO2/t; CaO basis 0.785 t CO2/t CaO; MgO basis 1.092 t CO2/t MgO;
C → CO2 ratio 44.01/12.011 = 3.664; urea carbon 0.733 t CO2/t urea.

**Production EFs:** see Tier 3 table (IPCC 2006 v3, 2006 vintage). For US
regulatory alignment use the corresponding 40 CFR Part 98 subpart equations
(H cement, F aluminum, V nitric acid, G ammonia, Q iron & steel, I
semiconductors); EPA GHG Emission Factors Hub does not cover process EFs —
go to Part 98 or IPCC directly. Always verify against the current published
edition before reporting.

## Unit and conversion traps

- **Clinker vs. cement basis.** The ~0.51–0.52 EF is per tonne of **clinker**.
  Cement = clinker + gypsum + SCMs; at a 0.75 clinker-to-cement ratio, applying
  the clinker EF to cement tonnage overstates process CO2 by ~33%. Purchased
  clinker ground on site has no on-site calcination emissions (scope 3 cat 1).
- **N2O vs. NOx.** Nitric acid plants report NOx (NO/NO2) for air-permit
  compliance; NOx is **not** a GHG and its CEMS does not measure N2O. Do not
  convert or substitute one for the other.
- **kg N2O vs. t CO2e.** Nitric acid EFs are in kg N2O per tonne of 100%
  HNO3. Two traps: acid tonnage is often recorded at commercial concentration
  (~55–68%) — convert to 100% acid basis; and forgetting the GWP step (×265
  or ×273) understates by two orders of magnitude.
- **Carbon vs. CO2.** Mass-balance results in tonnes of carbon must be
  multiplied by 3.664 (44.01/12.011). Reporting t C as t CO2 understates 3.7×.
- **Feedstock double counting.** If natural gas feedstock to the reformer is
  also in the site's fuel-purchase total fed to the stationary-combustion
  calculation, that carbon is counted twice. Reconcile total site gas
  purchases = fuel use + feedstock use.
- **HHV/NCV in feedstock EFs.** IPCC energy-basis feedstock factors are NCV;
  US gas purchase data are HHV (`ghg-protocol` skill §7).
- **Anode-effect units.** Slope coefficients are per **AE-minutes per
  cell-day**; some DCS systems log AE frequency (AE/cell-day) × duration
  (min/AE) separately — multiply them, don't use frequency alone.

## Data collection & gap-filling

Collect, in priority order:
1. **Production records**: clinker/lime/steel/NH3/HNO3/Al tonnage by month,
   at defined basis (100% acid, crude steel, saleable clinker).
2. **Raw material and composition data**: raw-meal carbonate content, clinker
   CaO/MgO lab analyses, feedstock carbon content, coke/coal assays — needed
   for Tier 2.
3. **Process control data**: anode-effect logs (AEM), abatement DE test
   reports and uptime logs, CEMS hourly files, semiconductor gas purchase and
   utilization records.
4. **Regulatory filings**: 40 CFR Part 98 subpart reports, EU ETS verified
   plant reports — often the fastest audit-grade source and should reconcile
   with the corporate inventory (mind boundary and GWP-set differences: EU
   ETS excludes N2O at most sites and uses its own GWP vintage).
5. **Sector-tool workbooks**: GCCA/CSI spreadsheet, IAI questionnaire,
   worldsteel data collection — if the plant already files these, reuse them.

Gap-filling: missing months → interpolate on production (process emissions
scale near-linearly with output); missing composition → prior-year plant
average or IPCC default, flagged; no production data at all → Tier 4
capacity estimate, flagged as estimated and scheduled for replacement
(`ghg-protocol` skill §8).

## QA checks

- **Implied intensity**: t CO2 per t product vs. the IPCC default and sector
  benchmark (clinker 0.50–0.54 process-only; BOF steel ~1.2–1.8 total; NH3
  1.6–2.5). Outliers = unit error or method error until proven otherwise.
- **YoY variance vs. production**: process emissions should track production
  volume closely; intensity drifting >±5% YoY without a process change
  (abatement install, raw-mix change) needs explanation.
- **Combustion/process split reconciliation**: combustion + process should
  reconcile to CEMS totals (±5%) where CEMS exists, and site fuel purchases
  should reconcile to combustion activity data + feedstock.
- **Abatement credit audit**: DF × ASUF credit must be backed by stack tests
  (DF) and operating logs (uptime); credit claimed for hours the abatement
  unit was bypassed is an error.
- **Negative or zero process lines** at a facility whose NAICS/sector implies
  calcination or reduction chemistry → completeness gap.
- **GWP set consistency** across N2O/PFC sources and with the rest of the
  inventory (`ghg-protocol` skill §4); base-year recalculation on method or
  GWP change per §6.

## Worked FAQ

**Q1. Our cement plant made 480,000 t of cement at a 0.74 clinker ratio, all
clinker produced on site. Process CO2?**
Clinker = 480,000 × 0.74 = 355,200 t. Tier 3 default: 355,200 × 0.52 t CO2/t
(IPCC 2006, incl. CKD) = **184,704 t CO2** process. Kiln fuel is separate
stationary combustion. If clinker CaO/MgO analyses exist, switch to the Tier 2
formula (EF ≈ CaO × 0.785 + MgO × 1.092, plus measured CKD correction) and
disclose the method change.

**Q2. Nitric acid plant, 35,000 t of 60% acid, high-pressure, no abatement.
N2O and CO2e?**
Convert to 100% basis: 35,000 × 0.60 = 21,000 t HNO3. E = 21,000 × 9 kg/t
(IPCC 2006 Table 3.3, high-pressure, unabated) = 189,000 kg = 189 t N2O.
CO2e: 189 × 273 (AR6) = **51,597 t CO2e** (AR5: 189 × 265 = 50,085 t). Note
the two traps handled: acid concentration and the N2O≠NOx distinction.

**Q3. We installed tertiary N2O abatement mid-year (DF 0.88 per stack test,
online 95% of production after commissioning on 1 July, even production).**
Split the year: H1 unabated, H2 abated. Per 10,000 t/half at 7 kg/t
(medium-pressure): H1 = 70.0 t N2O; H2 = 10,000 × 7 × (1 − 0.88 × 0.95) =
70,000 × 0.164 = 11.48 t N2O. Year = 81.48 t N2O × 273 (AR6) ≈ **22,244 t
CO2e**. Keep the stack-test report and uptime log as evidence; do not apply
the abatement factor to H1.

**Q4. Steel EAF shop: 300,000 t crude steel, charge carbon 2,400 t, electrode
consumption 450 t (98% C), carbon in steel out 0.05%. Process CO2 by carbon
balance?**

```
C_in  = 2,400 + 450 × 0.98        = 2,841.0 t C
C_out = 300,000 × 0.0005          = 150.0 t C
E     = (2,841.0 − 150.0) × 3.664 = 9,860 t CO2
```
Compare: Tier 1 default 300,000 × 0.08 = 24,000 t CO2 — the default assumes
more carbon input; the site balance governs when input data are complete.
Natural gas burners at the EAF are stationary combustion, not in this balance.

**Q5. Is the CO2 we capture and sell to a beverage company deductible?**
Under IPCC/Part 98 logic, transferred CO2 can be subtracted from the source's
process emissions, but the Corporate Standard has no automatic deduction for
CO2 that is later released by the buyer (beverage CO2 is emitted on use).
Common defensible treatment: report gross process emissions and disclose the
transferred quantity; deduct only durable storage. Flag both treatments to
the user and recommend disclosure of whichever is chosen (`ghg-protocol`
skill §9, item 6).

**Q6. Aluminum smelter with no anode-effect data — what can we do?**
Tier 1 defaults (IPCC 2006 Table 4.15): for CWPB, 0.4 kg CF4 and 0.04 kg
C2F6 per t Al. At 150,000 t Al: 60.0 t CF4 and 6.0 t C2F6 → AR6: 60 × 7,380 +
6 × 12,400 = 442,800 + 74,400 = **517,200 t CO2e**, plus anode CO2 150,000 ×
1.6 = 240,000 t CO2. Flag that modern well-run pots emit far less than Tier 1
implies — obtaining AEM data (every modern potline logs it) and moving to the
slope method is the single highest-value data request for this source.

## References

- GHG Protocol Corporate Accounting and Reporting Standard (Revised Edition,
  2004), ch. 4.
- IPCC 2006 Guidelines for National GHG Inventories, vol. 3 (Industrial
  Processes and Product Use): ch. 2 (minerals — cement 2.2, lime 2.3, glass
  2.4, soda ash 2.5), ch. 3 (chemicals — ammonia 3.2, nitric acid 3.3, adipic
  3.4), ch. 4 (metals — iron & steel 4.2, aluminum 4.4), ch. 6
  (electronics); 2019 Refinement updates where issued.
- IPCC AR5 WG1 (2013) Appendix 8.A; AR6 WG1 (2021) ch. 7 supplementary
  tables — GWP values.
- WBCSD Cement Sustainability Initiative, "Cement CO2 and Energy Protocol"
  (v3.1, 2011; maintained by GCCA) and GNR/GCCA "Getting the Numbers Right"
  database — cement sector tool and benchmarks.
- International Aluminium Institute, "Aluminium Sector Greenhouse Gas
  Protocol" (2006) and IAI anode-effect survey reports — PFC slope
  coefficients and sector statistics.
- worldsteel, "CO2 Emissions Data Collection Methodology" — site carbon
  balance for iron & steel.
- 40 CFR Part 98 subparts: F (aluminum), G (ammonia), H (cement), I
  (electronics), Q (iron & steel), S (lime), V (nitric acid), P (hydrogen),
  N (glass) — US regulatory equations and factors.
- GHG Protocol sector calculation tools index (ghgprotocol.org/calculation-
  tools) — check for the current versions of the cement, aluminum, and iron
  & steel tools.
- Cross-cutting conventions: the `ghg-protocol` skill (GWP sets §4, EF
  hierarchy §7, data quality §8, base-year recalculation §6, answering style
  §9).
