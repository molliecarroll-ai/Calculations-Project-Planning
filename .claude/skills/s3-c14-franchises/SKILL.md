---
name: s3-c14-franchises
description: >-
  Scope 3 Category 14 — Franchises. Use for questions from the franchisor's
  perspective about franchisee emissions: franchise operations, franchised
  restaurants/hotels/retail locations, collecting franchisee scope 1 and 2
  data, floor-area × intensity estimation for franchise networks, and how
  franchisees themselves report. Covers the franchisee-specific and
  average-data methods and the category 14 vs. scope 1/2 vs. category 13
  classification of franchise arrangements.
---

# Scope 3 Category 14 — Franchises

**Definition (Scope 3 Standard, ch. 5, category 14):** emissions from the
operation of **franchises not included in the franchisor's scope 1 or
scope 2** — i.e., the **scope 1 and scope 2 emissions of franchisees**
(entities operating under a license to sell or distribute the reporting
company's goods or services in return for payments such as royalties).
This category applies to **franchisors only**. Core constituency: quick-service
restaurant brands, hotel brands, convenience/retail franchise systems,
service franchises, some fuel-retail brand networks.

Governing documents:
- Scope 3 Standard (2011), ch. 5, Table 5.4 (category 14 minimum boundary).
- Scope 3 Calculation Guidance (2013), **category 14 chapter** (franchisee-specific and average-data methods).
- Cross-cutting conventions: the `ghg-protocol` skill (boundaries §2, EF hierarchy §7, data quality §8).

## Boundary & classification

**In scope (minimum boundary):** franchisees' **scope 1 emissions** (gas
combustion in kitchens/heating, franchisee-operated vehicles, refrigerant
leakage from their equipment) and **scope 2 emissions** (their purchased
electricity/heat/cooling), for all franchised locations operating in the
reporting year. Optional: franchisees' upstream scope 3-type emissions
(their food purchases, waste) — usually the franchisor already captures the
supply chain it controls (company-mandated distribution) in its own
categories 1/4; do not double count.

**Out of scope / routed elsewhere:**
- **Company-owned/operated locations** → franchisor's scopes 1/2 (by boundary approach). A mixed system (e.g., 90% franchised QSR brand) must split the location list cleanly.
- **Franchisor-operated services** to franchisees (distribution fleets, corporate offices) → scopes 1/2 and upstream categories.
- Property the franchisor owns and leases to franchisees: emissions could be argued into **category 13**; the Guidance's convention is to keep franchise operations **in category 14** (report leased-to-franchisee assets in 14, note the treatment) — one category, disclosed, never both.
- Products sold **to** franchisees for resale (food, packaging): upstream burden → franchisor categories 1/4; consumer use/EOL of those goods → categories 11/12 per their own rules. Category 14 is strictly the franchisees' operational (S1+S2) footprint.
- **Franchisee's own inventory:** the franchisee reports its operations as its own scope 1/2, and franchisor-related items separately per the standard's guidance (e.g., goods purchased from the franchisor in category 1; franchise fees do not create a scope 3 category for the franchisor's corporate emissions beyond normal purchased-services treatment). Do not confuse the two perspectives — this skill is the franchisor's.

**Overlap resolution:** master-franchise and sub-franchise tiers — count each
operating location once; if a location is counted by the master franchisee's
program data, do not re-add it from the brand location list.

## Method ladder

| Tier | Method (Calc. Guidance, cat. 14) | Data basis | Typical use |
|---|---|---|---|
| 1 | **Franchisee-specific method** | Franchisees' actual fuel/energy (or reported S1+S2) per location | Data-mature systems; large franchisees; sustainability-program participants |
| 2 | **Average-data method** | Locations or floor area × energy intensity per franchise type × EF | Long-tail locations; standard first pass |
| 3 | Revenue proxy (screening) | System sales × intensity per $ (derived or EEIO) | Screening only |

Hybrid is the norm: specific data for participating franchisees + average
data for the rest — disclose the split (`ghg-protocol` skill §3).

### 1. Franchisee-specific method

**When:** franchisees supply utility/fuel data (data clauses in franchise
agreements, brand sustainability portals, shared utility-data platforms) or
their own computed scope 1/2.

```text
C14 = Σ_locations [ Σ_fuels (fuel qty × fuel EF)
                    + electricity (kWh) × grid EF (location)
                    + refrigerant losses × GWP ]
```

**Method walk-through.** Symbolic:

```text
1. Covered locations: kWh and therms per location   ← franchisee-supplied
   utility data (agreement data clauses, brand sustainability portal,
   utility-data aggregators), pro-rated to the reporting year
2. Grid EF per location   ← eGRID subregion where geocoded / national factor
3. Gas EF                 ← EPA Hub current edition (per therm, HHV)
4. Covered C14 = Σ_locations (kWh × grid EF + therms × gas EF
                 + refrigerant losses × GWP)
5. Uncovered tail: extrapolate covered per-location averages stratified by
   store format × climate zone, flagged as estimated
6. System C14 = covered + extrapolated; disclose the coverage split
```

**Pitfalls:** self-selected reporters are often the larger/newer (or
greener) stores — stratify the extrapolation by store format and climate,
not one global mean; billing periods pro-rated to the reporting year;
franchisee-reported "scope 2" market-based figures mixed with your
location-based inventory (collect kWh, compute EFs yourself).

### 2. Average-data method

**When:** no franchisee data. Floor area (preferred) or location count ×
building-type intensity:

```text
C14 = Σ_types [ total franchised floor area_type (ft²)
                × energy intensity_type (kWh or kBtu/ft²·yr, by fuel)
                × EF_fuel ]
   or  Σ_types [ location count × average energy per location_type × EF ]
```

**Intensity sources:** CBECS 2018 food service / retail / lodging
intensities (EIA — verify current cycle); brand engineering data (design
energy models per store format are often better than CBECS); hotel sector
benchmarks (CHSB — Cornell Hotel Sustainability Benchmarking).

**Application note.** Take total franchised floor area by format from the
location master list, multiply by the current CBECS/CHSB intensity (or
brand engineering design-energy models — often better than generic
benchmarks) fuel by fuel, then by the location-appropriate EFs (subregional
grid factors where geocoded; gas EF from the current EPA Hub).

**Pitfalls:** store-format mix (a drive-thru QSR ≠ food court kiosk);
climate weighting for heating/cooling-dominated formats; counting
partial-year openings/closures at full-year weight (pro-rate by operating
months); missing franchisee vehicles and refrigerants (CBECS covers building
energy only — add fleet/refrigerant estimates for formats where material,
e.g., delivery-heavy brands).

### 3. Revenue proxy (screening only)

`system sales ($) × kgCO2e/$` from either an internally derived intensity
(covered locations' emissions ÷ their sales) or EEIO restaurant/accommodation
sector factors (USEEIO — verify version). Use to size the category before
investing in data programs; score 5 on data quality; do not carry into a
mature inventory.

## Emission factor and parameter sources

Record source, edition/vintage, and units for every input per the
`ghg-protocol` skill §7.

| Source | Governing table / dataset | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| EIA CBECS | Food-service, retail, and lodging intensity tables, by fuel (food service is the highest-intensity commercial type) | US commercial buildings | kBtu/ft²·yr (total/gas); kWh/ft²·yr (electricity); whole-building basis | Survey cycles (verify the current cycle) |
| Cornell Hotel Sustainability Benchmarking (CHSB) | Hotel energy/carbon benchmarks | Global lodging, by segment and climate | per room / per ft² | Annual |
| EPA eGRID | Subregion output emission rates | US grid | per MWh (convert to kWh) | Biennial data releases |
| EPA GHG EF Hub | Natural gas (therm/MMBtu, HHV) and vehicle-fuel tables | US fuels | per therm / MMBtu / gallon | Annual |
| IPCC 2006 GL vol. 3 ch. 7; EPA GreenChill | Commercial-refrigeration leak-rate defaults | Refrigerant losses | % of charge per yr | Static / periodic |
| IPCC assessment report (declared AR set) | GWP tables (blend-weighted for commercial blends) | Refrigerants | 100-yr GWP | Per assessment cycle |
| USEEIO | Restaurant/accommodation sector intensities | Revenue-proxy screening | per $ revenue | Versioned |

This skill intentionally quotes no factor values. When a quantitative
answer is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **Annual operating emissions** for locations franchised during the reporting year — pro-rate openings, closures, transfers (company-owned ↔ franchised conversions switch a location between scope 1/2 and category 14 mid-year: split by months, never double count).
- **Floor area basis:** kitchen + dining vs. total building; leased pad sites; ft² vs. m² (× 10.764); kBtu vs. kWh (÷ 3.412).
- **Location count vs. system data:** brand marketing "units" counts can include licensed shelf-space or ghost kitchens with very different intensities — reconcile to the franchise disclosure document location list.
- **Therms/MMBtu/HHV:** US gas billing in therms (1 therm = 0.1 MMBtu HHV); EPA factors HHV (`ghg-protocol` skill §7).
- **Refrigerants:** kg of charge × GWP of the actual refrigerant (R-404A-heavy commercial refrigeration is high-GWP, AR5 ≈ 3,943 — blend-weight per `s1-fugitive-emissions`); one AR set inventory-wide (`ghg-protocol` skill §4).

## Data collection & gap-filling

- **Franchise agreement data clauses:** the structural fix — new/renewing agreements should require annual utility-data sharing; many brands run a sustainability portal or use automated utility-data aggregators with franchisee consent.
- **Location master list** (from franchise operations/FDD): format, floor area, geography, open/close dates — the denominator for everything.
- **Brand-standard equipment specs:** mandated kitchen/refrigeration packages let engineering estimate per-format energy and refrigerant charge better than generic benchmarks.
- **Gap-filling:** stratify covered-location actuals by format × climate zone and extrapolate within strata; fall back to CBECS/CHSB only for strata with zero coverage. Flag actual vs. estimated per the `ghg-protocol` skill §8 and report the coverage %.
- Track **coverage KPI YoY** (% of locations / % of system floor area on actual data) — the standard maturity metric for this category.

## QA checks

- **Location reconciliation:** company-owned + franchised = total system; each location in exactly one of scope 1/2 or category 14; conversions pro-rated.
- **Per-location sanity:** implied tCO2e/location within format benchmarks (a US QSR typically ~100–250 tCO2e/yr S1+S2; a full-service hotel far more); outliers audited for unit errors.
- **Extrapolation-bias check:** covered-location average vs. system-wide format/climate mix; adjust stratification if covered sample skews.
- **Completeness:** franchisee vehicles and refrigerants included or their exclusion disclosed for formats where material.
- **YoY method consistency:** same intensity sources and stratification; coverage-driven changes (more actual data) disclosed as method improvement, base year per the `ghg-protocol` skill §6.
- **No double counting** with category 1 (goods sold to franchisees), category 13 (franchisee-leased property kept in 14), category 11 (fuel sold at franchised fuel retail — decide 11 vs. 14 boundary for fuel throughput and disclose; convention: sold fuel → 11, station operations → 14).

## Worked FAQ

**Q1. 5,000-location QSR system, zero franchisee data. First-pass C14?**
Average format 2,800 ft², food-service intensities (CBECS 2018 — verify):
electricity `5,000 × 2,800 × 45 kWh/ft² × 0.37 = 233,100 t`; gas `5,000 ×
2,800 × 0.10 MMBtu/ft² × 53.4 = 74,760 t`; refrigerant `5,000 × 120 kg
charge × 15% × 3,943 (R-404A, AR5) /1000 = 354,870 t`... note refrigerant
rivals energy for refrigeration-heavy formats — verify charge/leak with
engineering. Order-of-magnitude C14 ≈ **660,000 tCO2e**; prioritize a data
program.

**Q2. We own 20% of locations and franchise 80%. Split?**
Owned/operated 20% → scopes 1/2 (operational control). Franchised 80% →
category 14. A location converting to franchise on July 1 → 6 months in
scopes 1/2, 6 months in category 14.

**Q3. Do franchisees' food purchases belong in our C14?**
Optional, not minimum boundary. If you already account the brand supply
chain you mandate (your distributors' sales to franchisees) in your
categories 1/4, adding franchisee purchases to 14 double counts inside your
own inventory — include franchisee upstream only for spend outside your
captured supply chain, and disclose.

**Q4. A fuel-brand franchisor: is franchisees' fuel throughput C14?**
No — fuel *sold to consumers* is category 11 (use of sold products) if you
are in the fuel's value chain as producer/supplier; the stations' own
operations (shop electricity, canopy lighting) are category 14. If you only
license the brand and never own the fuel, the fuel is not your sold product —
document the contractual structure and state the treatment.

**Q5. I'm the franchisee. Where does the franchisor appear in my
inventory?**
Your restaurant is your scope 1/2. Goods bought from/through the franchisor
→ your category 1; royalty/marketing fees → purchased services in category 1
(spend-based); property leased from the franchisor that you operate → your
scope 1/2 (operational control) or category 8 per lease type. Category 14
never appears in a franchisee's inventory.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5, Table 5.4 (category 14 minimum boundary; franchisor/franchisee perspectives).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 14 chapter (franchisee-specific and average-data methods).
- Data sources: EIA CBECS 2018 (food service, retail, lodging intensities); Cornell Hotel Sustainability Benchmarking (CHSB, annual); eGRID; EPA GHG Emission Factors Hub (annual); IPCC 2006 GL vol. 3 ch. 7 (refrigeration leak defaults). Verify current editions.
- Cross-cutting rules: the `ghg-protocol` skill (§2 boundaries, §3 hybrid-method disclosure, §7 EF hierarchy, §8 data quality).
