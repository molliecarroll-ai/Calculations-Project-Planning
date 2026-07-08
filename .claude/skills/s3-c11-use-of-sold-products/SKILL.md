---
name: s3-c11-use-of-sold-products
description: >-
  Scope 3 Category 11 — Use of Sold Products. Use for questions about product
  use phase, lifetime emissions of products sold in the reporting year,
  fuel-consuming products (vehicles, engines, boilers), energy-using products
  (appliances, electronics, equipment), sold fuels and feedstocks, and
  GHG-containing products (refrigerant charge, aerosols). Covers direct vs.
  indirect use-phase boundaries, the units-sold × lifetime × energy × EF
  formula family, lifetime and use-profile assumption governance, and grid
  decarbonization refinements. Typically the dominant category for OEMs,
  appliance/electronics makers, and energy companies.
---

# Scope 3 Category 11 — Use of Sold Products

**Definition (Scope 3 Standard, ch. 5, category 11):** emissions from the use
of goods and services **sold by the reporting company in the reporting
year**, over their **expected total lifetime**. The category covers the
scope 1 and scope 2 emissions of end users (consumers and business
customers) that occur during use of the sold products.

Governing documents:
- Scope 3 Standard (2011), ch. 5 (definition, minimum boundary — Table 5.4; direct vs. indirect use-phase).
- Scope 3 Calculation Guidance (2013), **category 11 chapter** — formulas for fuels, energy-using products, GHG-containing products, and indirect use-phase.
- Cross-cutting conventions (GWP set, EF source hierarchy, data quality, base year recalculation): the `ghg-protocol` skill. This skill does not restate them.

**Why this category dominates.** For automotive OEMs, engine and equipment
makers, appliance and electronics manufacturers, and oil & gas / fuel
retailers, category 11 is routinely **60–95% of the total corporate
inventory** — a single year's vehicle sales carry a decade-plus of driving;
a barrel sold is a barrel burned. Treat assumptions here (lifetime, use
intensity, grid factors) as the highest-stakes parameters in the whole
inventory.

## Boundary & classification

### Direct use-phase emissions — required minimum boundary

The minimum boundary is the **direct use-phase emissions of sold products
over their expected lifetime**. The Calculation Guidance defines three
product classes, each with its own formula family:

1. **Products that directly consume energy (fuels or electricity) during
   use** — vehicles, engines, aircraft, boilers, furnaces, appliances,
   electronics, lighting, data-center hardware, pumps, motors.
   → lifetime energy/fuel consumption × emission factor.
2. **Fuels and feedstocks sold** — gasoline, diesel, natural gas, LPG, coal,
   crude-derived products sold for combustion.
   → quantity sold × **combustion** emission factor (combustion only; the
   upstream production of the fuel is the buyer's category 3 problem, and
   your scopes 1/2 and upstream categories already carry your production).
3. **GHGs and products containing GHGs emitted during use** — refrigerants
   and pre-charged HVAC/refrigeration equipment, aerosols, fire suppression,
   SF6-containing switchgear, N2O canisters, fertilizers (N2O from applied
   N is commonly treated here when sold to end users; disclose treatment).
   → GHG contained per unit × fraction released over lifetime (in-use
   leakage + end-of-life release) × GWP.

If a sold product fits several classes (a gas boiler consumes fuel; a heat
pump consumes electricity *and* contains refrigerant), account for **each
mechanism** and sum.

### Indirect use-phase emissions — optional

Products that **indirectly** cause use-phase emissions: apparel (washing,
drying, ironing), food (refrigeration, cooking), soaps and detergents
(heated water), cookware. Accounting is **optional** under the Standard but
recommended ("should") when indirect use-phase emissions are significant —
e.g., detergent and apparel companies commonly include them because the
heated-water/laundry emissions dwarf everything else. If included, use
**use-profile scenarios** (e.g., washes per garment lifetime × machine
energy per wash × % warm vs. cold) and disclose the profile source.

### Out of scope / routed elsewhere

- Downstream **processing** of sold intermediates → category 10. An engine sold to an OEM for installation: the OEM's assembly energy is your category 10; the vehicle's driving fuel is your category 11 (as a component maker you account the use of your component's function — see FAQ Q5).
- Product **end-of-life** → category 12 (but EOL *release of contained GHGs* is conventionally counted in category 11's lifetime-release fraction per the Guidance's GHG-containing-product formula; do not also count the same release in category 12 — disclose where you put it).
- Products **leased to customers** (reporter = lessor, retains ownership) → category 13; do not double count the same asset in 11 and 13. Products **sold** outright → category 11.
- Electricity sold by a utility that it *generated* → scope 1 (generation), not category 11; electricity *purchased and resold* → scope 3 category 3 for T&D losses and the buyer's consumption treatment per the utility annexes. Fuels retailed without transformation → category 11 combustion.
- Use of products by the reporter itself (demo fleets, own use) → scopes 1/2.

### Sold-in-year over full lifetime — the central convention

Category 11 is **not** the annual emissions of the installed base. It is a
**forward-looking lifetime total for the reporting year's sales cohort**:

```text
C11(year Y) = Σ over products sold in Y of (expected lifetime emissions)
```

A car sold in 2026 contributes its entire ~15 years / ~200,000 km of driving
to the 2026 inventory, discounted by nothing. Next year's inventory covers
next year's cohort. Consequences: (a) sales growth alone grows category 11;
(b) no "true-up" of prior cohorts is required when reality diverges from the
lifetime assumption — but assumption *changes* are method changes (disclose;
base-year recalculation per the `ghg-protocol` skill §6).

## Method ladder

The Guidance's methods are organized by product class rather than a strict
data-intensity ladder; within each, better data = product-family-specific
measured consumption; worse data = generic/typical-product assumptions.

| Tier | Method | Product class | Data basis |
|---|---|---|---|
| 1 | Direct use-phase: **fuels/energy-using products, measured profiles** | Vehicles, appliances, equipment | Units sold by model × model-specific lifetime energy/fuel (test-cycle or telemetry) × EF |
| 2 | Direct use-phase: **sold fuels** | Fuel/energy sellers | Quantity of fuel sold × combustion EF (near-zero model risk) |
| 3 | Direct use-phase: **GHG-containing products** | Refrigerants, charged equipment, SF6 gear | Charge per unit × lifetime release fraction × GWP |
| 4 | Direct use-phase: **generic/average product assumptions** | Any | Units sold × typical-product energy profile (regulatory defaults, sector averages) |
| 5 | **Indirect use-phase scenarios** (optional) | Apparel, food, detergents | Units sold × use-profile scenario × EF |

### 1. Energy-using and fuel-consuming products (measured/model-specific)

**When:** you know units sold by model/market and have per-model consumption
data (regulatory test values, ENERGY STAR specs, engineering measurements,
telematics).

**Core formula family:**

```text
# Electricity-using product
C11 = Σ_models [ units sold × annual energy use (kWh/yr)
                 × expected lifetime (yr)
                 × grid EF (kgCO2e/kWh) ] / 1,000   → tCO2e

# Fuel-consuming product (distance-based)
C11 = Σ_models [ units sold × lifetime distance (km)
                 × fuel consumption (L/100 km) / 100
                 × fuel EF (kgCO2e/L) ] / 1,000     → tCO2e

# Fuel-consuming product (operating-hours-based: gensets, mowers, marine)
C11 = Σ_models [ units sold × lifetime operating hours (h)
                 × fuel rate (L/h) × fuel EF (kgCO2e/L) ] / 1,000
```

Sum by model × market (grid factors and driving patterns differ), then
aggregate.

**Method walk-through — fuel-consuming product (vehicles, the canonical
case).** Symbolic, per model × market:

```text
1. N  = units sold, by model and market   ← sales/ERP shipment data,
        reconciled to revenue
2. D  = lifetime activity (km), per market ← disclosed assumption (national
        transport/scrappage statistics, fleet data, OEM disclosures;
        published OEM assumptions run roughly 150,000–240,000 km by market —
        label yours)
3. FC = real-world fuel consumption (L/100 km) ← regulatory test-cycle value
        (WLTP / EPA label) plus a disclosed real-world uplift (ICCT gap
        studies)
4. EF = combustion factor (kgCO2e/L, incl. CH4/N2O) ← the market's fuel EF
        source, current edition (EPA GHG EF Hub, DESNZ)
5. Per-unit lifetime emissions = D × FC / 100 × EF
6. C11 = Σ_(model, market) N × per-unit / 1,000   → tCO2e
```

**Method walk-through — electricity-using product (appliances,
electronics).** Same skeleton with an energy term:

```text
Per-unit lifetime energy = annual energy use (kWh/yr; sales-weighted label
                           values: ENERGY STAR / DOE / EU energy label)
                           × expected lifetime (yr; service/warranty data,
                           disclosed)
Per-unit emissions       = lifetime kWh × grid EF of the sales market
                           (eGRID subregion / IEA / national source,
                           current year)
C11                      = Σ_models units sold × per-unit / 1,000
```

For BEVs and heat pumps, measure lifetime energy at the wall (charging
losses included) and apply the sales market's grid factor — see the grid
trajectory note below.

**Pitfalls:** test-cycle vs. real-world consumption (NEDC/WLTP/EPA label
values understate real driving by ~5–40% depending on cycle — disclose which
basis and any uplift); ignoring standby/idle energy for electronics;
single-market grid factor applied to global sales; charging losses omitted
for EVs; duty-cycle assumptions for commercial equipment taken from
marketing rather than field data.

### 2. Sold fuels and feedstocks

**When:** you sell fuels (producer, refiner, retailer, utility gas sales).
The highest-certainty method in scope 3 — quantity sold is metered and
combustion chemistry is fixed.

```text
C11 = Σ_fuels [ quantity sold (units) × combustion EF (kgCO2e/unit) ] / 1,000  → tCO2e
```

Use **combustion-only** EFs (not well-to-wheel): the upstream portion is
your own scopes 1/2 and categories 1–4. Assume 100% of sold fuel is
combusted unless you can document non-combustion uses (e.g., naphtha sold as
chemical feedstock → category 10 processing treatment; disclose the split
and the fate of embodied carbon).

**Input provenance.** Quantity sold per fuel is metered from sales/billing
ledgers; the combustion-only EF (CO2 plus CH4/N2O, in the inventory's
declared GWP set) comes from the market's factor source — EPA GHG EF Hub,
DESNZ, or IPCC defaults, current edition — matched to the quantity's basis
(volume, mass, or energy; HHV vs. NCV).

**Pitfalls:** biofuel blend shares — the biogenic CO2 fraction (e.g., 10%
ethanol in E10) is reported outside the scopes, not in the category 11 total
(fossil CO2 + all CH4/N2O stay in; see `ghg-protocol` skill §5); volume
temperature correction for large volumes; double counting fuel sold to your
own franchisees/lessees also captured in categories 13/14 (pick one home).

### 3. GHG-containing products

**When:** you sell refrigerants, pre-charged equipment (AC, heat pumps,
refrigeration cases, vehicle AC), SF6 switchgear, aerosols, fire
suppression, or fertilizer.

```text
C11 = Σ_products [ units sold × GHG charge per unit (kg)
                   × total lifetime release fraction (in-use leaks + EOL release, %)
                   × GWP_gas ] / 1,000   → tCO2e
```

Lifetime release fraction = (annual leak rate × lifetime years) + EOL
release fraction (1 − recovery efficiency), capped at 100%. IPCC 2006 GL
vol. 3 ch. 7 and EPA Vintaging Model provide default leak and recovery
rates by equipment type.

**Input provenance.** Charge per unit from bills of materials and type
approvals; annual leak rate, lifetime, and EOL recovery efficiency from
IPCC 2006 GL vol. 3 ch. 7 defaults or the EPA Vintaging Model
(equipment-type-specific); GWP from the inventory's declared IPCC AR set,
blend-weighted for refrigerant blends.

Note: a heat pump also consumes electricity — add the energy-using-product
formula for the same units and sum both mechanisms.

**Pitfalls:** blends must be GWP-weighted by constituent (see
`s1-fugitive-emissions`); double counting EOL release in category 12;
non-Kyoto refrigerants (R-1234yf, HCFCs) go outside the scopes as memo
items (`ghg-protocol` skill §4).

### 4. Generic/average product assumptions

**When:** no model-level data — use typical-product profiles: regulatory
minimum-efficiency assumptions, sector-average energy-use profiles, or
competitor label data for comparable products.
Same formulas as method 1 with average inputs; score data quality lower and
prioritize replacing assumptions for the highest-volume SKUs.

### 5. Indirect use-phase scenarios (optional)

```text
C11_indirect = units sold × uses per lifetime × energy per use (kWh or L)
               × EF, summed over scenario segments (e.g., wash temperature mix)
```

**Input provenance.** Units sold from sales systems; the use profile (uses
per lifetime, energy per use, scenario mix such as wash-temperature or
line-dry shares) from published consumer-habits surveys (e.g.,
detergent-industry studies); grid EF market-weighted from the usual grid
sources. Disclose the profile source and that inclusion is optional — keep
the choice stable YoY.

### Grid-decarbonization trajectory (optional refinement)

The base method applies the **current** grid factor to all lifetime years.
An optional refinement (increasingly common for EVs and heat pumps) applies
a declining grid-factor trajectory (e.g., IEA STEPS/APS scenarios or
national NDC-consistent projections) year by year over the product's life:

```text
Per-unit emissions = Σ_{t=1..L} annual energy (kWh) × grid EF(year_of_sale + t)
```

This is a scenario choice: disclose the trajectory source, apply it
consistently across products and years, and do not mix current-factor and
trajectory methods silently. Static current-year factors remain the
conservative, most-auditable default.

## Emission factors / parameters quick reference

All values below are for orientation — **verify against the named source's
current edition before use**, and record source/year/units per the
`ghg-protocol` skill §7.

**Fuel combustion EFs (fossil CO2; add CH4/N2O ≈ +0.3–1%):**

| Fuel | EF | Units | Source + vintage |
|---|---|---|---|
| Motor gasoline | 8.78 (≈2.32/L) | kgCO2/gal | EPA GHG EF Hub, 2025 ed. |
| Diesel | 10.21 (≈2.70/L) | kgCO2/gal | EPA GHG EF Hub, 2025 ed. |
| Natural gas | 53.06 | kgCO2/MMBtu (HHV) | EPA Hub 2025; IPCC NCV basis differs — see traps |
| LPG/propane | 5.72 (≈1.51/L) | kgCO2/gal | EPA Hub 2025 |
| Jet fuel (Jet A) | 9.75 | kgCO2/gal | EPA Hub 2025 |
| Marine HFO | 3.114 | tCO2/t fuel | IMO 4th GHG Study (2020) |

**Grid electricity (location-based, generation + T&D as published):**

| Grid | EF | Units | Source + vintage |
|---|---|---|---|
| US national average | ~0.37 | kgCO2e/kWh | eGRID 2023 data (pub. 2025) — use subregion where possible |
| UK | ~0.207 | kgCO2e/kWh | DESNZ 2024 conversion factors |
| EU-27 average | ~0.21–0.25 | kgCO2e/kWh | EEA/IEA latest year |
| China | ~0.55–0.60 | kgCO2e/kWh | IEA emission factors (latest) |
| World average | ~0.44 | kgCO2e/kWh | IEA (latest) |

**Lifetime / use-intensity typicals (label as assumptions, cite basis):**

| Product | Lifetime | Use intensity | Basis |
|---|---|---|---|
| Passenger car | 12–18 yr / 150,000–240,000 km by market | 10,000–19,000 km/yr | National transport statistics; OEM disclosures; disclose market weighting |
| Heavy truck | ~1,000,000+ km | 60,000–120,000 km/yr | Fleet data |
| Refrigerator | 12–15 yr | 300–500 kWh/yr | DOE/ENERGY STAR label data |
| Washing machine | 10–12 yr | ~180–300 cycles/yr | ENERGY STAR; habit surveys |
| Room AC / heat pump | 10–15 yr | climate-zone dependent | DOE test procedures; charge + leak per IPCC 2006 GL v3 ch.7 |
| Laptop | 4–6 yr | 30–60 kWh/yr | ENERGY STAR TEC values |
| Gas boiler (residential) | 15–20 yr | 10,000–20,000 kWh_fuel/yr | National heating statistics |

**Refrigerant GWPs (100-yr):** R-134a — AR5 1,300 / AR6 1,530; R-410A —
AR5 ≈1,924 / AR6 ≈2,256 (blend-weighted); SF6 — AR5 23,500 / AR6 25,200.
One AR set inventory-wide (`ghg-protocol` skill §4).

## Unit and conversion traps

- **Sold-in-year × full lifetime, not installed-base annual.** The #1 category 11 error. Do not compute "our products in the field emitted X this year" — compute "products we sold this year will emit X over their lives." The two differ by roughly a factor of the product lifetime when sales are steady.
- **Lifetime years vs. annual energy:** forgetting to multiply annual kWh by lifetime years (or multiplying twice) shifts results by 10–20×. Make the formula show both terms explicitly.
- **L/100 km vs. km/L vs. mpg:** `L/100 km = 235.215 / mpg(US)`. A 30 mpg car = 7.84 L/100 km. Mixing these inverts the intensity.
- **Test-cycle vs. real-world:** WLTP/EPA-label values understate real consumption; NEDC worse. Disclose the basis and any real-world uplift (ICCT publishes gap estimates).
- **HHV vs. NCV** for sold gas/fuels: EPA factors are HHV-basis, IPCC/IEA NCV — pairing a HHV factor with NCV-quantified energy misstates ~5–10% for gas (`ghg-protocol` skill §7).
- **Combustion-only vs. well-to-wheel EFs:** category 11 uses combustion-only; a WTW factor double counts your own upstream.
- **EV charging losses:** wall-to-battery losses ~10–15% — lifetime energy should be measured at the wall (grid draw), not battery throughput.
- **kgCO2e vs. tCO2e:** the /1,000 step; cohort totals in Mt for large OEMs — sanity-check magnitude (a million vehicles ≈ tens of Mt).
- **Market mix:** grid factors and lifetimes vary by sales market; a global-average shortcut on a China-heavy sales mix materially understates (or overstates for a Nordic mix).

## Data collection & gap-filling

- **Sales/shipment data by SKU and market** from ERP — the backbone. Reconcile units sold to revenue as a completeness check.
- **Product energy specs:** ENERGY STAR certified-product databases, DOE test data, EU energy labels/ecodesign declarations, WLTP/EPA fuel-economy certification values, ErP technical files. Sales-weight across the actual SKU mix — never the "flagship efficient model."
- **Real-world telemetry** (vehicle telematics, connected appliances) upgrades test-cycle assumptions; document the sample and period.
- **Lifetime assumptions:** warranty/service records, national scrappage statistics, industry studies. Governance rule: sales-weighted, documented source, reviewed on a set cycle, changed only with disclosure — lifetime is the single most result-moving assumption in the inventory.
- **Gap-filling:** SKUs without specs → map to the nearest specified model or regulatory minimum-efficiency assumption (conservative), flagged per the `ghg-protocol` skill §8. Missing market split → allocate by revenue share, flagged.
- **Refrigerant/charge data:** bills of materials and type approvals give charge sizes; leak/recovery defaults from IPCC 2006 GL vol. 3 ch. 7 or the EPA Vintaging Model.

## QA checks

- **Dominance sanity:** for OEMs, appliance/electronics makers, and fuel sellers, category 11 should usually be the largest category — often >70% of total scope 1+2+3. If it is not, first suspect a lifetime term dropped or an installed-base (annual) computation.
- **Per-unit sanity:** lifetime tCO2e per unit against benchmarks — ICE car ~25–50 t; refrigerator ~1–2 t; laptop ~0.05–0.15 t (use-phase only); 1 L gasoline ≈ 2.3 kg. Outliers → unit audit.
- **Lifetime-assumption consistency YoY:** same lifetimes/use intensities as last year unless a disclosed method change; a silent change is the classic way a category 11 number moves 20% with no real-world cause.
- **Cohort completeness:** Σ units in the calculation = units sold per the ledger, every market, including fleet/B2B channels.
- **Double-counting sweeps:** sold vs. leased units (11 vs. 13); component vs. final-product accounting if you sell both into the same vehicles (11 vs. 10); GHG-release EOL fraction (11 vs. 12); fuel sold to franchisees (11 vs. 14).
- **Biogenic split:** biofuel-blend biogenic CO2 outside the scopes, disclosed, not netted.
- **Trajectory discipline:** if a grid-decarbonization trajectory is used, one named scenario source, applied to all electric products, disclosed.

## Worked FAQ

**Q1. We sold 120,000 diesel vans (lifetime 250,000 km, real-world
9.5 L/100 km). Category 11?**
`250,000 × 9.5/100 = 23,750 L/van; × 2.72 kgCO2e/L (EPA Hub 2025 + CH4/N2O,
verify) = 64.6 tCO2e/van; × 120,000 = 7,752,000 tCO2e ≈ 7.75 Mt.` Disclose
lifetime-km source and the real-world basis.

**Q2. Our TVs: 800,000 units, 110 kWh/yr label value, 7-yr lifetime, sold
55% EU / 45% US.**
EU: `800,000×0.55 × 110 × 7 × 0.23 kgCO2e/kWh = 77,924 t` (EEA latest — verify).
US: `800,000×0.45 × 110 × 7 × 0.37 = 102,564 t` (eGRID 2023 US avg).
Total ≈ **180,500 tCO2e**. Label values may understate real viewing hours —
note the data-quality limitation.

**Q3. We're a natural gas utility selling 30 million MMBtu to end users.**
Sold fuel: `30e6 MMBtu × 53.06 kgCO2/MMBtu = 1.592e9 kg ≈ 1,592,000 tCO2e`
(EPA Hub 2025, HHV — verify), plus CH4/N2O (+~0.1%). Gas you combusted in
own operations is scope 1, not category 11; T&D losses/leaks are scope 1
(fugitives) for your pipeline.

**Q4. Do we report the installed base's emissions each year until products
retire?**
No. Each reporting year accounts the **full lifetime** emissions of that
year's sales cohort, once. No annual true-up of past cohorts; a change in
lifetime assumptions applies prospectively (and to the base year only per
recalculation policy, `ghg-protocol` skill §6).

**Q5. We make fuel injectors sold to OEMs. Is the car's lifetime fuel our
category 11?**
The Guidance permits **either** accounting the use-phase of the final
product your component enters (proportional treatment is common: some
component makers account the full vehicle fuel, others allocate by the
component's contribution) **or**, since an injector consumes no energy
itself, treating direct use-phase as negligible and disclosing. Best
practice for powertrain-critical components: estimate the enabled final
product's use-phase (units × vehicle lifetime fuel), disclose the approach —
and never claim category 11 = 0 silently. OEM assembly energy is your
category 10 either way.

**Q6. Heat pumps: 60,000 units, 1.1 kg R-32 charge (GWP AR5 677), 3%/yr leak
× 15 yr + 30% EOL release of remainder; 3,500 kWh/yr electricity × 15 yr,
EU grid 0.23 kgCO2e/kWh.**
Refrigerant: release = 45% + 0.30×55% = 61.5%;
`60,000 × 1.1 × 0.615 × 677 / 1,000 = 27,480 tCO2e`.
Energy: `60,000 × 3,500 × 15 × 0.23 / 1,000 = 724,500 tCO2e`.
Total ≈ **752,000 tCO2e** — energy dominates; both mechanisms required.
Optional refinement: declining EU grid trajectory would cut the energy term
materially; disclose scenario if used.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5 and Table 5.4 (category 11 minimum boundary; direct vs. indirect use-phase); ch. 6 (reporting-year sales convention).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 11 chapter (formulas for direct use-phase — fuels, energy-using products, GHG-containing products; indirect use-phase scenarios).
- EF and parameter sources: EPA GHG Emission Factors Hub (annual); eGRID (biennial data releases); UK DESNZ conversion factors (annual); IEA emission factors; IPCC 2006 Guidelines vol. 3 ch. 7 (refrigerant leak/recovery defaults); ENERGY STAR / DOE / EU energy-label databases; ICCT real-world fuel-consumption gap studies. Verify all values against current editions.
- Cross-cutting rules: the `ghg-protocol` skill (§4 GWPs, §5 biogenic, §6 base year, §7 EF hierarchy, §8 data quality, §9 answering contract).
