---
name: ghg-protocol
description: >-
  Cross-cutting GHG Protocol corporate accounting reference and router. Use for
  any question about organizational/operational boundaries, scope definitions,
  GWP sets and CO2e conversion, biogenic emissions, base year recalculation,
  emission factor source selection, data quality scoring, uncertainty, or which
  footprint-source skill to use. Also use when a question spans multiple
  emission sources or you're unsure which category an activity belongs to.
---

# GHG Protocol — Corporate Accounting Navigator

This is the shared foundation for the footprint-source skill suite. Every
source-specific skill (listed in §1) assumes the conventions defined here.
When answering methodology questions: **cite the governing document and
chapter**, state assumptions explicitly, and never present an estimate as
more certain than its method tier warrants.

## 0. Governing documents

| Document | Governs | Cite as |
|---|---|---|
| GHG Protocol Corporate Accounting and Reporting Standard (Revised Edition, 2004; amended 2013 for Scope 2 alignment) | Scopes 1 & 2 requirements, boundaries, base year, reporting principles | Corporate Standard, ch. N |
| GHG Protocol Scope 2 Guidance (2015) | Location-based and market-based scope 2 accounting; contractual instrument Quality Criteria | Scope 2 Guidance, ch. N |
| Corporate Value Chain (Scope 3) Accounting and Reporting Standard (2011) | Scope 3 requirements: which of the 15 categories apply, boundary rules | Scope 3 Standard, ch. N |
| Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013) | Category-by-category calculation methods (the method ladders) | Scope 3 Calculation Guidance, category N |
| GHG Protocol calculation tools (cross-sector: stationary combustion, mobile combustion, HFC/refrigeration, purchased electricity; plus sector tools) | Default formulas and emission factors | Named tool + version |
| IPCC Guidelines for National GHG Inventories (2006; 2019 Refinement) | Underlying combustion/process emission factor science, tier definitions | IPCC 2006 GL, vol./ch. |
| GHG Protocol Land Sector and Removals Guidance (2022, final draft → 2024) | Biogenic CO2, land-based removals and storage | LSRG, ch. N |

Requirements language: the standards distinguish **"shall"** (required for
conformance), **"should"** (recommended), and **"may"** (permissible option).
Preserve that distinction when answering — do not upgrade a "should" to a
requirement.

## 1. Skill index — route by footprint source

**Scope 1 (direct):**
- `s1-stationary-combustion` — boilers, furnaces, turbines, heaters, generators, flares
- `s1-mobile-combustion` — owned/controlled vehicles, vessels, aircraft, off-road equipment
- `s1-fugitive-emissions` — refrigerants/HFCs, SF6, fire suppression, CH4 leaks, non-Kyoto gases
- `s1-process-emissions` — chemical/physical process CO2, N2O, PFCs etc. (cement, ammonia, aluminum…)

**Scope 2 (purchased energy):**
- `s2-purchased-electricity` — grid electricity; location-based & market-based; eGRID/RECs/PPAs
- `s2-steam-heat-cooling` — purchased steam, district heating/cooling, CHP allocation

**Scope 3 (value chain), by category number:**
- `s3-c01-purchased-goods-services` · `s3-c02-capital-goods` · `s3-c03-fuel-energy-related`
- `s3-c04-upstream-transportation` · `s3-c05-waste-generated` · `s3-c06-business-travel`
- `s3-c07-employee-commuting` (incl. telework) · `s3-c08-upstream-leased-assets`
- `s3-c09-downstream-transportation` · `s3-c10-processing-sold-products`
- `s3-c11-use-of-sold-products` · `s3-c12-eol-sold-products`
- `s3-c13-downstream-leased-assets` · `s3-c14-franchises` · `s3-c15-investments`

Common routing traps:
- **Leased asset the reporter operates** → scope 1/2 under operational control, not category 8/13. Check the boundary approach first (§2).
- **Electricity T&D losses** → category 3, not scope 2 (except for utilities reporting T&D losses on purchased power they resell, which is scope 2… see `s3-c03`).
- **Company vehicles vs. employee vehicles** → scope 1 vs. category 6/7 by ownership/control, not by who is driving.
- **Outsourced activities** (contract manufacturing, 3PL warehousing) → scope 3 of the reporter; never "deduct" them.
- **Waste hauled by third party from own operations** → category 5; own landfill/incinerator → scope 1.
- **Combustion of biomass** → biogenic CO2 reported outside the scopes; CH4/N2O from the same combustion stay in scope (§5).

## 2. Boundaries

**Organizational boundary** (Corporate Standard ch. 3) — pick one consolidation
approach and apply it to every source:
- **Equity share**: account for emissions per % economic ownership.
- **Financial control**: 100% of emissions from operations you can direct financial/operating policies of (usually = financial consolidation).
- **Operational control**: 100% of emissions from operations where you hold operating authority (most common choice; aligns with permits/authority to implement operating policies).

Consequences: a 50/50 JV is 50% under equity share, 100% or 0% under control
approaches. Whatever is excluded from scope 1/2 by the boundary choice
(e.g., equity investments under operational control) lands in **scope 3
category 15**, not nowhere.

**Operational boundary** (ch. 4): scope 1 = direct from owned/controlled
sources; scope 2 = purchased electricity/steam/heat/cooling consumed; scope 3
= all other value chain (15 categories, upstream 1–8, downstream 9–15).
Scope 1 and 2 are required; under the Scope 3 Standard all 15 categories must
be screened, and non-negligible ones accounted or exclusion justified.

## 3. The method ladder (universal pattern)

Every source skill presents methods from most to least data-intensive. The
generic ladder:

| Tier | Generic name | Data basis | Typical uncertainty |
|---|---|---|---|
| 1 | Direct measurement | CEMS, metered gas, measured mass balance | Lowest |
| 2 | Activity-data × source-specific EF | Fuel/energy/mass quantities + supplier or site-specific factors | Low |
| 3 | Activity-data × average EF | Quantities + published average factors (EPA, DEFRA, IPCC defaults, eGRID) | Moderate |
| 4 | Proxy / intensity extrapolation | Floor area, headcount, production units, partial-year extrapolation | High |
| 5 | Spend-based (EEIO) | $ spend × economy-wide $-intensity factors (USEEIO, EXIOBASE) | Highest |

Rules of use:
- **Materiality-proportionate effort**: use higher tiers for large sources; spend/proxy tiers are acceptable for screening and immaterial sources (Scope 3 Calculation Guidance, "Introduction").
- **Screening then refinement** is the sanctioned workflow: estimate all categories cheaply, then invest data collection where the tonnage is.
- **Never mix silently**: when a category combines tiers (e.g., supplier-specific for top suppliers + spend-based for the tail = "hybrid method"), disclose the split.
- Moving up the ladder between years can change results absent any real-world change — disclose method changes; base-year recalculation is triggered only per §6.

## 4. GWPs and CO2e

- Seven Kyoto-basket gas groups: CO2, CH4, N2O, HFCs, PFCs, SF6, NF3. CO2e = Σ (mass_gas × GWP_gas), using **100-year GWPs from a single, named IPCC assessment report** across the whole inventory.
- Current best practice (and CDP/SEC/CSRD alignment): **AR5 without climate-carbon feedback** or **AR6**. Key values: CH4 fossil — AR4: 25, AR5: 28, AR6: 29.8; N2O — AR4: 298, AR5: 265, AR6: 273; SF6 — AR5: 23,500, AR6: 25,200; HFC-134a — AR5: 1,300, AR6: 1,530.
- **Do not mix AR editions across sources or years.** Switching AR set = recalculate base year (§6).
- **Non-Kyoto gases with climate impact** (e.g., HFOs like R-1234yf, CFCs/HCFCs — the latter regulated under Montreal Protocol) are reported **outside the scopes** as an optional memo item, not added to scope totals. Blended refrigerants (R-410A etc.) → decompose into constituents and GWP-weight (see `s1-fugitive-emissions`).

## 5. Biogenic emissions

- CO2 from combustion/decomposition of biomass (biofuel share, wood, biogas, biogenic waste fraction): report as a **separate line item outside the scopes** ("biogenic CO2"), never netted against fossil totals.
- CH4 and N2O from biomass combustion **remain inside** the relevant scope, converted with standard GWPs.
- Land-sector removals/storage: only claimable per Land Sector and Removals Guidance rules (traceability, permanence monitoring, reversal accounting). Do not net removals against gross emissions in the main scopes.

## 6. Base year and recalculation

(Corporate Standard ch. 5) Recalculate the base year when, per your published
**significance threshold** (commonly 5% of total inventory):
- structural changes: M&A, divestitures, outsourcing/insourcing of activities that existed in the base year;
- methodology/EF/GWP-set changes or error discoveries;
- **not** for organic growth/decline (new plants built, output changes).
Acquired operations that did not exist in the base year → no recalculation;
current + future years only. Facilities acquired mid-year: include from
acquisition date (control approaches).

## 7. Emission factor source hierarchy

Preference order when a source skill says "published average EF":
1. **Supplier/site-specific measured** factors (with documentation).
2. **National, current-year regulatory/statistical**: US EPA GHG Emission Factors Hub (updated ~annually; based on 40 CFR Part 98 and eGRID), UK DESNZ/DEFRA conversion factors (annual), national inventory factors elsewhere.
3. **International defaults**: IPCC 2006 GL / 2019 Refinement (fuel & process), IEA electricity factors (non-US grids), IMO/GLEC (transport).
4. **LCA databases** for cradle-to-gate product factors: ecoinvent, GaBi/Sphera, Agribalyse; sector programs (worldsteel, PlasticsEurope, PCF/EPD data).
5. **EEIO** for spend: USEEIO (US), EXIOBASE (global, MRIO), DEFRA table 13 (legacy).

Match the factor's **boundary** (combustion-only vs. life-cycle/WTW), **units**
(HHV vs. LHV/GCV vs. NCV — US factors typically HHV, IPCC/IEA typically NCV;
converting wrongly shifts results ~5–10% for gas), **geography**, and
**vintage** to the activity data. Record source, year, and units for every
factor — that metadata is what an assurance provider asks for first.

## 8. Data quality, uncertainty, and assurance readiness

- Score data per the Scope 3 Calculation Guidance five-dimension rubric: technological, temporal, geographical representativeness; completeness; reliability (1 = best, 5 = worst per dimension).
- Uncertainty: parameter (EF and activity data ranges — propagate with error propagation or Monte Carlo), scenario (method choices), model. Qualitative disclosure is acceptable; quantified ranges are better for material sources.
- Keep an **evidence trail per data point**: source document, extraction date, unit conversions applied, EF citation, GWP set. Estimation and gap-filling steps (extrapolation window, proxy basis) must be documented and consistently applied.
- Gap-filling conventions: pro-rata temporal extrapolation (annualize partial data), like-facility intensity proxies (per ft², per FTE, per unit output), prior-year rollover flagged for replacement. Always flag filled values distinctly from actuals.

## 9. Answering-style contract for all skills in this suite

1. Identify the footprint source and confirm scope/category classification before calculating anything.
2. Present the applicable method ladder and recommend a tier based on stated data availability and materiality.
3. Show the formula, then a worked computation with explicit units at each step.
4. Name the EF source (publication, year, table) — never emit a bare number as if universal.
5. State the GWP set used.
6. Flag ambiguities (boundary questions, factor vintage, HHV/NCV) rather than resolving them silently. Where the Protocol allows multiple treatments, say so and show both.
7. If a question falls outside GHG Protocol corporate accounting (e.g., product footprints → Product Standard, ISO 14067; offsets/claims → separate guidance), say which framework governs instead.
