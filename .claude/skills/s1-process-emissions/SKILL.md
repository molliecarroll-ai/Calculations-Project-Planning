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
  (N2O catalytic destruction, HFC-23 abatement). Points to IPCC 2006 Vol. 3
  (IPPU) default tables and sector tools (WBCSD-CSI/GCCA cement, IAI aluminum,
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
             (stoichiometric; CaO/MgO fractions from site raw-meal or clinker
             analysis; correct for non-carbonate Ca/Mg sources such as slag
             or fly ash)
CKD_correction: CO2 from calcined cement-kiln dust leaving the kiln system,
             typically +1.5–2% (IPCC 2006 default correction factor if
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
(stoichiometric; that carbon is accounted for on urea use — downstream or
scope 3; disclose the treatment)
```

**Iron & steel — site carbon balance** (worldsteel method; IPCC Tier 2):

```
E_CO2 = [Σ C_inputs − Σ C_outputs] × (44.01/12.011)
C_inputs:  coke, coal, natural gas (reductant share), electrodes, charged
           scrap/DRI/hot metal carbon, limestone/dolomite flux carbon
C_outputs: carbon in crude steel (~0.1–1%), slag, sold coke-oven/blast-furnace
           gas, tar and other sold byproducts
```

**Walk-through (cement, clinker method):** take saleable **clinker** tonnage
(never cement tonnage), compute EF_clinker stoichiometrically from the
lab-measured CaO/MgO fractions attributable to carbonate raw materials, and
apply the CKD correction (measured, or the IPCC default factor, labeled).
Kiln fuel is calculated separately as stationary combustion. **Pitfalls:**
using cement instead of clinker tonnage (see traps below); ignoring
non-carbonate CaO in alternative raw materials (overstates); skipping CKD
(understates 1–2%).

**Walk-through (ammonia):** gross CO2 from the feedstock carbon balance (or,
lacking carbon data, production × the IPCC 2006 Table 3.1 default per t NH3
for the plant's feedstock and process technology — verify current edition);
subtract CO2 stored in urea (Urea_t × 0.733, stoichiometric) and disclose
where the urea carbon is accounted.

### Tier 3 — Production × IPCC Tier 1 default EF

**When:** only product tonnage is known. **Data:** annual production per
product.

```
E = Production_t × EF_default   (per gas; convert N2O/PFCs to CO2e with the
                                 inventory's GWP set — `ghg-protocol` skill §4)
```

Tier 1 defaults are **not quoted here** — pull them from the governing IPCC
table (all IPCC 2006 GL vol. 3, 2006 vintage; check the 2019 Refinement and
current national factors before use):

| Product / process | Tier 1 default lives in | What it provides |
|---|---|---|
| Cement clinker | IPCC 2006 v3 ch. 2.2 | t CO2/t clinker, including a default CKD uplift |
| Lime (high-calcium vs. dolomitic) | IPCC 2006 v3 Table 2.4 | t CO2/t lime by lime type |
| Glass | IPCC 2006 v3 ch. 2.4 | t CO2/t glass, scaled by (1 − cullet ratio) |
| Soda ash (natural/trona production; consumption/use) | IPCC 2006 v3 ch. 2.5 | t CO2/t produced or consumed — production and use factors differ |
| Ammonia | IPCC 2006 v3 Table 3.1 | t CO2/t NH3 by feedstock and process technology |
| Nitric acid N2O | IPCC 2006 v3 Table 3.3 | kg N2O/t 100% HNO3 by plant pressure/technology and abatement status — roughly an order of magnitude spread between plant types, so the row choice matters |
| Iron & steel (BOF, EAF, pig iron) | IPCC 2006 v3 Table 4.1 | t CO2/t product by route — BOF and EAF differ by more than an order of magnitude |
| Aluminum anode CO2 (prebake CWPB, Søderberg) | IPCC 2006 v3 Table 4.10 | t CO2/t Al by cell technology |
| Aluminum PFC Tier 1 | IPCC 2006 v3 Table 4.15 | kg CF4 and kg C2F6 per t Al by cell technology |

**Aluminum PFC Tier 2 — slope method** (preferred whenever anode-effect
process data exist):

```
CF4_kg/t Al  = S_CF4(technology) × AEM      # AEM = anode-effect minutes per cell-day
C2F6_kg/t Al = CF4 × F_C2F6/CF4(technology)
```

Slope coefficients S and byproduct ratios F per cell technology (CWPB, SWPB,
VSS, HSS): IPCC 2006 v3 Table 4.16 / IAI Aluminium Sector GHG Protocol (2006
vintage — verify; plant-specific measured slopes take precedence).

**Walk-through (aluminum smelter):** production × slope(technology) × measured
AEM gives CF4; C2F6 follows via the byproduct ratio; convert each gas with its
own GWP from the declared set; report anode CO2 (production × the Table 4.10
default, or an anode carbon balance) separately from the PFCs.

**Nitric acid with abatement** (IPCC 2006 eq. 3.6):

```
E_N2O = P_HNO3 × EF × (1 − DF × ASUF)
DF = destruction factor (measured; NSCR ~0.80–0.90+, catalytic tertiary units
     often >0.90 — use plant-specific test data)
ASUF = abatement system utilization factor (uptime fraction)
```

**Walk-through (nitric acid):** convert acid tonnage to a 100% HNO3 basis,
select the Table 3.3 EF row matching the plant's pressure/technology and
abatement status, then apply (1 − DF × ASUF) using the plant's stack-test DF
and abatement uptime — and only for the production that occurred while the
abatement system was commissioned and online. Convert with the inventory's
N2O GWP.

**Semiconductors:** IPCC 2006 v3 ch. 6 Tier 1 uses default FC emissions per
m² of wafer processed; Tier 2a/2b use gas purchases × (1 − utilization) ×
(1 − abatement DE) per gas per process type, with byproduct CF4 formation
factors. Fabs should use the Tier 2b method with the World Semiconductor
Council / Part 98 subpart I parameters; gases include CF4, C2F6, CHF3, NF3,
SF6 — each converted with its own GWP.

**Pitfalls (all Tier 3):** technology mismatch (using the unabated
high-pressure nitric acid row for a modern abated plant overstates ~10×);
production basis errors (clinker vs. cement, gross vs. net steel); Tier 1 PFC
defaults ignore actual anode-effect performance and can be badly wrong in
either direction.

### Tier 4 — Capacity / benchmark estimation

**When:** no production data (screening, M&A due diligence). Estimate
production = nameplate capacity × sector-typical utilization (e.g., 85–90%
cement in a strong market), then apply Tier 3 EFs; or apply a published
sector intensity benchmark (GCCA GNR "Getting the Numbers Right" database for
cement, IAI statistics for aluminum — pull current values). Label results as
order-of-magnitude, data quality 4–5 per the `ghg-protocol` skill §8, and
replace with real production data before formal reporting.

## Emission factor sources

**Process GWPs, 100-year** (IPCC AR5 2013 w/o feedback; AR6 2021. Retained
here because they are fixed by the named AR edition — verify the current
required set):

| Gas | AR5 | AR6 | Main process source |
|---|---|---|---|
| N2O | 265 | 273 | Nitric/adipic acid, caprolactam |
| CF4 (PFC-14) | 6,630 | 7,380 | Aluminum anode effects, semiconductor etch |
| C2F6 (PFC-116) | 11,100 | 12,400 | Aluminum, semiconductors |
| NF3 | 16,100 | 17,400 | Semiconductor/display chamber cleaning |
| SF6 | 23,500 | 25,200 | Magnesium cover gas, semiconductors |
| HFC-23 (CHF3) | 12,400 | 14,600 | HCFC-22 byproduct, semiconductor etch |

**Stoichiometric constants (exact, retained):** CaCO3 → 0.4397 t CO2/t;
MgCO3 → 0.5220 t CO2/t; CaO basis 0.785 t CO2/t CaO; MgO basis 1.092 t CO2/t
MgO; C → CO2 ratio 44.01/12.011 = 3.664; urea carbon 0.733 t CO2/t urea.

**Production EF sources:**

| Source | Governing table(s)/section(s) | Coverage | Update cadence |
|---|---|---|---|
| IPCC 2006 GL vol. 3 (IPPU) | ch. 2.2–2.5 (minerals), Tables 3.1/3.3 (chemicals), 4.1/4.10/4.15/4.16 (metals), ch. 6 (electronics) | Tier 1 defaults and Tier 2 parameters for all major process sources | Static (2006); 2019 Refinement updates where issued |
| 40 CFR Part 98 sector subparts | H (cement), F (aluminum), V (nitric acid), G (ammonia), Q (iron & steel), I (electronics), S (lime), P (hydrogen), N (glass) | US regulatory equations and factors — the EPA GHG Emission Factors Hub does **not** cover process EFs; go to Part 98 or IPCC directly | Amended by rulemaking |
| Sector tools | GCCA/WBCSD-CSI cement protocol; IAI Aluminium Sector GHG Protocol; worldsteel CO2 methodology | Sector-standard Tier 2 methods, parameters, and benchmarks | Check current tool versions |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source. (The GWPs and
stoichiometric constants above are retained deliberately: GWPs are fixed per
AR edition and the constants are exact chemistry.)

## Unit and conversion traps

- **Clinker vs. cement basis.** The clinker EF is per tonne of **clinker**.
  Cement = clinker + gypsum + SCMs; at a 0.75 clinker-to-cement ratio, applying
  the clinker EF to cement tonnage overstates process CO2 by ~33%. Purchased
  clinker ground on site has no on-site calcination emissions (scope 3 cat 1).
- **N2O vs. NOx.** Nitric acid plants report NOx (NO/NO2) for air-permit
  compliance; NOx is **not** a GHG and its CEMS does not measure N2O. Do not
  convert or substitute one for the other.
- **kg N2O vs. t CO2e.** Nitric acid EFs are in kg N2O per tonne of 100%
  HNO3. Two traps: acid tonnage is often recorded at commercial concentration
  (~55–68%) — convert to 100% acid basis; and forgetting the N2O GWP step
  understates by two orders of magnitude.
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

## FAQ

**Q1. Our cement plant made 480,000 t of cement at a 0.74 clinker ratio, all
clinker produced on site. How is process CO2 computed?**
Convert to clinker first — cement tonnage is never the calculation basis:
clinker = cement × clinker ratio. Then either Tier 3 (clinker × the IPCC 2006
ch. 2.2 default, which includes a CKD uplift) or, better, Tier 2 if clinker
CaO/MgO analyses exist (EF = CaO × 0.785 + MgO × 1.092, stoichiometric, plus
measured CKD) — and disclose the method change when upgrading. Kiln fuel is
separate stationary combustion.

**Q2. Nitric acid plant, 35,000 t of 60% acid, high-pressure, no abatement.
How is N2O computed?**
Two traps first: convert to a 100% acid basis (tonnage × concentration), and
never substitute NOx CEMS data for N2O. Then apply the IPCC 2006 Table 3.3
row for an unabated high-pressure plant — the highest-EF row; using a lower
row misstates severely because the table spans an order of magnitude — and
convert the kg N2O with the inventory's N2O GWP.

**Q3. We installed tertiary N2O abatement mid-year (DF 0.88 per stack test,
online 95% of production after commissioning on 1 July).**
Split the year at commissioning: pre-commissioning production carries the
unabated Table 3.3 EF; post-commissioning production carries EF ×
(1 − DF × ASUF) with the stack-test DF and the logged uptime. Keep the
stack-test report and uptime log as evidence. The classic error is applying
the abatement factor to the whole year, including the unabated half.

**Q4. Steel EAF shop — how does the site carbon balance work?**

```
C_in  = charge carbon + electrode consumption × electrode carbon fraction
        (+ any natural-gas reductant, flux carbon, DRI/hot-metal carbon)
C_out = crude steel tonnage × steel carbon content
        (+ carbon in slag and sold byproducts)
E_CO2 = (C_in − C_out) × 3.664
```
The site balance governs when input data are complete; the IPCC Table 4.1
EAF default assumes a generic carbon input and can diverge substantially from
a well-documented balance. Natural gas burners at the EAF are stationary
combustion, not part of this balance.

**Q5. Is the CO2 we capture and sell to a beverage company deductible?**
Under IPCC/Part 98 logic, transferred CO2 can be subtracted from the source's
process emissions, but the Corporate Standard has no automatic deduction for
CO2 that is later released by the buyer (beverage CO2 is emitted on use).
Common defensible treatment: report gross process emissions and disclose the
transferred quantity; deduct only durable storage. Flag both treatments to
the user and recommend disclosure of whichever is chosen (`ghg-protocol`
skill §9, item 6).

**Q6. Aluminum smelter with no anode-effect data — what can we do?**
Fall back to the IPCC 2006 Table 4.15 Tier 1 PFC defaults for the cell
technology, converting CF4 and C2F6 each with its own GWP from the declared
set, plus anode CO2 from Table 4.10. Flag that modern well-run pots emit far
less PFC than Tier 1 implies — obtaining AEM data (every modern potline logs
it) and moving to the Tier 2 slope method is the single highest-value data
request for this source.

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
