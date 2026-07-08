---
name: s3-c02-capital-goods
description: >-
  Scope 3 Category 2 (Capital Goods) methodology assistant. Use for capex
  footprints: machinery, equipment, buildings and construction, vehicles, IT
  hardware/servers, and any capitalized purchase. Covers the year-of-acquisition
  rule and why depreciation/amortization spreading is prohibited, embodied
  carbon per m2 or per unit, spend-based capex-by-asset-class EEIO estimates,
  and the boundary with Category 1 (expensed vs capitalized) and Category 8
  (leased assets).
---

# Scope 3 Category 2 — Capital Goods

**Category definition (Scope 3 Standard, ch. 5, Table 5.4):** "Extraction,
production, and transportation of capital goods purchased or acquired by the
reporting company in the reporting year." **Minimum boundary:** all upstream
(cradle-to-gate) emissions of purchased capital goods. Capital goods are
final products with extended life used to manufacture a product, provide a
service, or sell/store/deliver merchandise — plant, machinery, buildings,
facilities, vehicles, IT equipment — treated as fixed assets (PP&E) in
financial accounting.

Governing documents: Corporate Value Chain (Scope 3) Standard (2011), ch. 5;
Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013), Category 2
chapter. Cross-cutting conventions (method ladder, GWPs, EF hierarchy, data
quality) are in the `ghg-protocol` skill.

## Boundary & classification

**In scope (minimum boundary):**
- Full **cradle-to-gate** emissions of every capital good acquired in the
  reporting year: raw materials, component manufacture, assembly,
  construction activity, and upstream transport up to delivery.
- Construction projects: account in the year(s) construction spend occurs or
  on completion/handover — pick one convention and apply it consistently
  (multi-year builds are commonly recognized as capitalized spend is incurred).
- Self-constructed assets: purchased materials and contractor services for
  the build are Category 2 (fuel your own equipment burns on site is scope 1).

**The accounting-treatment rule (Cat 1 vs Cat 2):** classification follows
the reporter's **own financial accounting**. Capitalized on the balance
sheet → Category 2; expensed in the P&L → Category 1 (Scope 3 Calculation
Guidance, Cat. 1/2). Depreciation itself is never an emissions input — it is
only the marker that identifies which purchases are capital goods. Apply your
capitalization threshold consistently and never count a purchase in both
categories.

**Year of acquisition — no depreciation spreading:** the total cradle-to-gate
emissions of capital goods are reported **in full in the year of
acquisition**. The Scope 3 Calculation Guidance (Category 2) explicitly
states companies should **not** depreciate, discount, or amortize the
emissions of capital goods over their useful life. Consequence: Category 2 is
lumpy — a factory-build year will spike it. That is by design; handle it with
disclosure (see QA), not smoothing.

**Out of scope / routed elsewhere:**
- **Operating** the capital good (fuel, electricity) → scopes 1/2.
- **Leased assets you do not purchase** → Category 8 (upstream leased assets)
  for operating leases where the lessor retains the asset. Nuance: finance/
  capital leases that put the asset on *your* balance sheet are commonly
  treated like an acquisition — the asset's embodied emissions then fit the
  Category 2 logic, and its operation falls in scope 1/2 (control) rather
  than Category 8. Under IFRS 16 most leases capitalize a right-of-use asset;
  the GHG Protocol boundary follows control/ownership substance, not just the
  balance-sheet entry — state your treatment and apply it consistently.
- **Purchased land**: no embodied manufacturing emissions (land-use-change
  emissions, if any, are addressed under land-sector guidance, not here).
- Assets acquired through **M&A** → organizational boundary/base-year
  machinery (`ghg-protocol` §6), not Category 2.
- Second-hand assets: the Guidance allows excluding (embodied emissions were
  attributable to the first purchaser) or including with disclosure —
  choose and disclose.

## Method ladder

The Scope 3 Calculation Guidance (Category 2) names the same ladder as
Category 1, applied to capital goods:

| # | Method | Activity data | Emission factor | Typical use |
|---|---|---|---|---|
| 1 | Supplier-specific | Asset-level purchases | Supplier cradle-to-gate PCF / EPD, or allocated supplier scope 1+2 | Major equipment, construction with EPD-backed materials |
| 2 | Average-data | Physical measures (m² built, units, tonnes of machinery) | Embodied-carbon benchmarks per unit | Buildings, fleets, IT hardware |
| 3 | Spend-based | Capex by asset class | EEIO $-intensity (USEEIO/EXIOBASE) by producing industry | Screening, mixed capex programs |

(Hybrid combinations are permitted exactly as in Category 1.)

### Method 1 — Supplier-specific

**When:** the manufacturer publishes a cradle-to-gate PCF/LCA (common for
servers, network gear, some vehicles) or the construction project has a
whole-building LCA (EN 15978 modules A1–A5).

```
Emissions = Σ_assets ( units acquired × cradle-to-gate PCF_asset )

# Building projects (EN 15978):
Embodied = A1–A3 (product) + A4 (transport to site) + A5 (construction process)
```

**Method walk-through (IT refresh):** pull the manufacturer's PCF for the
exact model and configuration acquired; strip use phase and end-of-life so
only manufacturing + delivery remain; multiply by units acquired; book the
total in the year of acquisition. PCFs are configuration-sensitive
(memory/storage count can roughly double a server PCF) — match the
configuration, not just the model family.

**Pitfalls:** PCFs often report *whole-life* totals with a use-phase share —
strip use phase (that's your scope 2) and end-of-life; GWP set and biogenic
conventions differ across manufacturers.

### Method 2 — Average-data (per unit / per m² / per mass)

**When:** you know physical scale but lack product-specific LCAs.

```
Emissions = Σ ( physical quantity × embodied-carbon benchmark )
```

Benchmark sources: RICS/LETI/CRREM embodied-carbon benchmarks for buildings;
ecoinvent datasets for machinery per kg; ICE database (Univ. of Bath) for
construction materials; manufacturer-class averages for IT and vehicles.

**Method walk-through (office construction):** take the building's gross
internal area (m² GIA); select an upfront embodied-carbon benchmark (A1–A5,
kg CO2e/m²) from the current LETI/RICS edition that matches the building type
and structural system; multiply and book in the acquisition/completion year,
stating the module scope and area definition used.

**Pitfalls:** benchmark scope varies (A1–A3 vs A1–A5 vs whole-life) — match
and state modules; structural system (timber vs concrete vs steel) can shift
building benchmarks roughly twofold; per-mass machinery factors are crude —
prefer spend-based if mass is estimated anyway.

### Method 3 — Spend-based (EEIO by asset class)

**When:** screening the whole capex program from the fixed-asset register.

```
Emissions = Σ_class ( capex_class,deflated to factor $-year × EEIO EF_producing industry )
```

Map asset classes to producing commodities: buildings → nonresidential
construction; machinery → machinery manufacturing; vehicles → motor vehicle
manufacturing; IT → computer/electronics manufacturing. Apply the same
inflation, currency, tax-removal, and purchaser-price rules as Category 1
(see the `s3-c01-purchased-goods-services` skill and Unit traps below).

**Method walk-through:** extract reporting-year additions by asset class from
the fixed-asset register; strip land, capitalized labor/interest, and
intangibles; deflate each class to the EEIO factor's dollar-year; multiply by
the current-release factor for the producing industry; sum, documenting
release, dollar-year, and deflator per class.

**Pitfalls:** using total capex including land and capitalized labor/interest
(strip non-goods components); asset register "additions" vs cash capex timing
differences; double counting capitalized internal costs already in scopes 1/2.

### Lumpy-capex disclosure recommendation

Because emissions land entirely in the acquisition year, the Guidance
recommends that companies with cyclically large capital purchases **disclose
the fluctuation** — e.g., note the major project driving a Category 2 spike,
and optionally show a multi-year average as *supplemental* information. The
reported inventory number itself must remain the undepreciated
year-of-acquisition total.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| LETI / RICS embodied-carbon benchmarks | Benchmark tables by building type (upfront, A1–A5) | Buildings, UK-oriented; check applicability | kg CO2e per m² (state GIA/NIA/GEA and module scope) | Periodic editions — verify current |
| Manufacturer PCF libraries (Dell, HPE, Lenovo, Apple, OEM LCAs) | Model-specific PCF documents | IT hardware, vehicles; configuration-specific | kg CO2e per unit, cradle-to-gate (strip use phase/EOL) | Per model release |
| ICE database (Univ. of Bath) | Material embodied-carbon tables | Construction materials | kg CO2e per kg of material | Versioned releases |
| ecoinvent | Machinery/vehicle/material datasets | Global, geography-specific | kg CO2e per kg or unit, cradle-to-gate | Versioned releases — state version |
| EPA Supply Chain GHG Emission Factors (USEEIO-based) | Producing-industry commodity factors | US, spend-based capex screening | kg CO2e per USD of a stated dollar-year, purchaser price | Per USEEIO release — verify current |
| EPDs (EN 15804) | Product-specific declarations | Construction products | Per declared unit, by module | Per publication; check validity |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **Depreciation is not activity data.** Never multiply annual depreciation
  by a factor — that both smooths (prohibited) and double counts across years.
  Use gross additions in the year.
- **Nominal vs. real currency and price basis** for EEIO — same rules as
  Category 1 (deflate to factor dollar-year; purchaser-price basis; strip
  taxes and land).
- **m² definition:** GIA vs NIA vs GEA changes per-m² results ~10–20%; match
  the benchmark's definition.
- **LCA module scope:** A1–A3 vs A1–A5 vs "whole life incl. B/C" — Category 2
  wants cradle-to-gate (+ delivery/installation where available); using
  whole-life PCFs unstripped double counts your future scope 2 and Cat 11-like
  use phase.
- **kg vs t CO2e per m²** — construction benchmarks appear in both.
- **Capitalized software/intangibles:** internally developed software has no
  embodied goods; purchased hardware inside a capitalized project does.
  Split project capex into goods vs labor/intangibles before factoring.

## Data collection & gap-filling

1. **Fixed-asset register extract**: additions in the reporting year by asset
   class, cost, in-service date, and project code. Reconcile to the cash-flow
   statement's capex line (see QA).
2. **Construction-in-progress**: decide (and document) recognition timing —
   spend-as-incurred vs completion — and get project-level spend or
   whole-building LCA data from the design team (EN 15978 assessments are
   increasingly contractually required).
3. **Major-asset refinement**: for the top assets/projects (usually a handful
   dominate), request manufacturer PCFs/EPDs or bills of materials; leave the
   tail spend-based.
4. **Procurement/AP cross-check**: capitalized flags in AP data catch capex
   routed through procurement systems; ensures the Cat 1/Cat 2 split is
   complete and exclusive.
5. **Gap-filling**: missing asset-class detail → apply the blended EEIO factor
   of the known mix; missing project LCAs → per-m² benchmark with the
   structural system stated; flag all proxies per `ghg-protocol` §8.

## QA checks

- **Reconciliation:** Σ capex put through methods ≈ fixed-asset additions ≈
  capex per cash-flow statement, with land/intangibles/capitalized-labor
  exclusions itemized.
- **No Cat 1 overlap:** sample AP lines near the capitalization threshold;
  confirm each landed in exactly one category. No inbound freight for capital
  goods double counted with Cat 4 (reporter-paid delivery of capital goods is
  Cat 4 by the same convention as Cat 1 — disclose).
- **Lumpiness narrative:** year-over-year swing >±30% should trace to named
  projects; include the disclosure note.
- **Share reasonableness:** Category 2 is typically a few percent of scope 3
  for asset-light firms but can rival Category 1 in build-out years for
  utilities, real estate, data-center operators, and heavy industry.
- **Factor-basis consistency:** one dollar-year, one GWP set, module scope
  (A1–A5) stated for building benchmarks, cradle-to-gate only for PCFs.

## Worked FAQ

**Q1. Can we spread our new plant's embodied emissions over its 25-year life?**
No. The Scope 3 Calculation Guidance (Category 2) explicitly prohibits
depreciating/amortizing capital-goods emissions. Report the full
cradle-to-gate total in the acquisition year and add a lumpiness disclosure;
a multi-year average may be shown only as supplemental information.

**Q2. We leased 30 forklifts (operating lease). Category 2?**
No — you didn't acquire them. Their operation under your control is
scope 1 (fuel) / scope 2 (electric); the embodied emissions sit with the
lessor. If instead you finance-lease them onto your balance sheet, treating
the embodied emissions under the Category 2 logic in year one is the
consistent reading — state your treatment.

**Q3. How do we screen a year of machinery capex?**
Spend-based method: take machinery-class additions from the fixed-asset
register, strip non-goods components, deflate to the EEIO factor's
dollar-year, and multiply by the machinery-manufacturing factor from the
current EPA Supply Chain release (purchaser price). Refine the largest assets
with manufacturer PCFs if material.

**Q4. Our building LCA reports an annualized whole-life intensity
(kg CO2e/m²/yr). Usable?**
Not directly — that's a whole-life figure including operational energy (your
future scope 2). Extract the upfront embodied modules (A1–A5) as a total
kg CO2e/m², multiply by GIA, and book it in the acquisition/completion year.

**Q5. We bought a used stamping press. Include it?**
The Guidance permits either excluding second-hand goods (embodied emissions
were accounted at first sale) or including them; excluding with disclosure is
the common choice. Refurbishment materials/work purchased are Category 1/2
per capitalization treatment either way.

**Q6. 1,500 laptops with manufacturer PCFs — Cat 1 or Cat 2?**
If your policy capitalizes them (common above per-unit thresholds or as a
pooled asset), Category 2; if expensed, Category 1. Either way the method is
units × model-specific cradle-to-gate PCF, counted once, in the acquisition
year — never in both categories.

## References

- GHG Protocol Corporate Value Chain (Scope 3) Standard (2011) — ch. 5,
  Table 5.4 (Category 2 definition and minimum boundary).
- Technical Guidance for Calculating Scope 3 Emissions v1.0 (2013) —
  Category 2 chapter (methods; the no-depreciation rule; Cat 1/2 split by
  accounting treatment).
- EPA Supply Chain GHG Emission Factors (USEEIO-based, current release) —
  capex asset-class screening.
- Building embodied carbon: RICS Whole Life Carbon Assessment (2nd ed. 2023),
  LETI Embodied Carbon Primer/benchmarks, ICE database v3 (Univ. of Bath),
  EN 15978 module structure.
- Manufacturer PCF libraries (Dell, HPE, Lenovo, Apple product reports);
  ecoinvent (machinery, vehicles).
- Cross-cutting conventions: the `ghg-protocol` skill.
