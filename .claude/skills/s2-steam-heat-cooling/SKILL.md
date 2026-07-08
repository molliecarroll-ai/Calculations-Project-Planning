---
name: s2-steam-heat-cooling
description: >-
  Scope 2 accounting for purchased steam, heat, and cooling under the GHG
  Protocol Scope 2 Guidance (2015). Use for questions involving district
  heating or district energy, purchased steam (klb, MMBtu, GJ), hot water,
  chilled water and district cooling (ton-hours, COP), CHP/cogeneration
  emission allocation (efficiency method, energy content method, work
  potential method), supplier-specific steam emission factors, the EPA Hub
  steam/heat default factor, and boiler-efficiency-based estimation. For grid
  electricity, RECs/PPAs, and eGRID questions use `s2-purchased-electricity`.
---

# Scope 2 — Purchased Steam, Heat, and Cooling

Scope 2 covers emissions from the generation of purchased steam, heating, and
cooling consumed in owned/controlled operations (Corporate Standard, ch. 4).
The Scope 2 Guidance (2015) applies to these energy carriers exactly as to
electricity — including **dual reporting** where contractual instruments or
supplier-specific rates exist (in practice: a supplier-specific district
energy factor is the market-based figure; certificate markets for heat are
rare, so the two totals usually coincide or differ only via supplier data).
Cross-cutting conventions (GWP set, EF hierarchy, base year, data quality)
are defined in the `ghg-protocol` skill.

## Boundary & classification

Scope 2 here = thermal energy **purchased from a third party and consumed**
inside the organizational boundary: utility district steam loops, campus
district heating/hot water, purchased chilled water, steam piped over the
fence from a neighboring plant or CHP.

- **Own boilers/chillers burning purchased fuel** → the fuel is **scope 1**
  (see `s1-stationary-combustion`), not this skill — even if the equipment
  serves the same loads. Electricity driving your own chillers → scope 2
  electricity, not purchased cooling.
- **Leased space — tenant with operational control**: steam/heat/cooling
  purchased for the tenant's space is the tenant's **scope 2**; get
  submetered (condensate meter, BTU meter, ton-hour meter) quantities where
  available, otherwise allocate the building purchase by floor-area share
  (heating/cooling loads scale roughly with area within one building) and
  document the basis. Landlord-purchased thermal energy for common areas the
  tenant does not control → tenant scope 3 category 8; landlord scope 2.
  Under the landlord's inventory, tenant-space energy it purchases is scope 3
  category 13 if tenants hold operational control. Check the consolidation
  approach first (`ghg-protocol` §2).
- **Self-generated heat consumed on-site** (own CHP or boilers): scope 1 via
  fuel. **Heat/steam sold** to others: generation emissions remain the
  generator's scope 1; the GHG Protocol permits reporting emissions
  attributable to exported energy as an information item, allocated per the
  CHP guidance below — the purchaser reports them as scope 2.
- **Steam purchased for resale** (district energy retailers): resold energy's
  generation emissions → the reseller's **scope 3 category 3** (same
  treatment as electricity for resale); only self-consumed energy is its
  scope 2.
- **Distribution losses** in the district network on purchased thermal energy
  → **scope 3 category 3** for the end consumer (district steam loops
  commonly lose 5–15%; supplier can advise). If the supplier's factor is
  expressed per unit **delivered**, losses are already inside the scope 2
  factor — ask which basis the factor uses to avoid double counting.
- **EV charging, electricity questions** → `s2-purchased-electricity`.

## Method ladder

| # | Method | Activity data | Emission factor | Use when | Uncertainty |
|---|---|---|---|---|---|
| 1 | Metered quantity × supplier-specific EF | MMBtu/GJ/klb/ton-hours from invoices or BTU meters | Supplier-calculated (fuel mix, plant efficiency, CHP allocation) | Supplier provides a factor — always ask first | Lowest |
| 2 | Metered quantity × default EF | Same metered quantities | EPA Hub steam/heat factor (or fuel factor ÷ assumed boiler efficiency) | Supplier factor unavailable | Moderate |
| 3 | Estimated consumption × EF | Floor area × thermal intensity benchmark | Default or supplier EF | No invoices/meters (gross leases) | High |
| 4 | Spend-based | $ spend ÷ unit price | Default EF | Screening, immaterial sites | Highest |

### Method 1 — Metered quantity × supplier-specific factor

Request from the district energy provider: annual emission factor (kg
CO2e/MMBtu or /GJ delivered), the fuel mix behind it, whether it is
CHP-allocated (and by which method — efficiency method preferred), and
whether it is per unit generated or delivered.

```
Inputs:  Q = purchased quantity (MMBtu; convert klb/GJ/ton-hours first —
             see Unit traps), from invoices or BTU meters
         EF_supplier = supplier's annual factor (kg CO2e/MMBtu; confirm
             CO2 vs CO2e, generated vs delivered basis, allocation method)
Result:  Emissions (t CO2e) = Q × EF_supplier / 1,000
```

Pitfalls: supplier factor in CO2 vs CO2e (ask); per-generated factors applied
to delivered quantities (understates); klb invoices converted with the wrong
enthalpy (see Unit traps).

### Method 2 — Metered quantity × default factor

Default factors assume a fuel and a boiler efficiency. Default source: the
US EPA GHG Emission Factors Hub **"Steam and Heat"** row — CO2 (kg/MMBtu)
plus CH4 and N2O (g/MMBtu), updated annually; pull the current edition. Its
basis: the natural gas HHV combustion factor (EPA Hub / 40 CFR 98 Table C-1)
divided by an assumed **80% boiler efficiency**. If the district system
burns other fuels (coal, oil, biomass), build your own:

```
EF_steam (kg CO2/MMBtu delivered heat)
  = EF_fuel (kg CO2/MMBtu fuel, HHV) ÷ boiler efficiency
Emissions = quantity (MMBtu) × EF_steam / 1,000     [t CO2]
```

**Method walk-through** (symbolic) — purchased steam `Q` MMBtu, no supplier
data, gas district plant assumed:

```
Inputs:  EF_CO2 (kg/MMBtu), EF_CH4, EF_N2O (g/MMBtu)
             — EPA Hub "Steam and Heat" row, current edition
         GWP_CH4, GWP_N2O — GWP set per `ghg-protocol` §4
CO2:   Q × EF_CO2 / 1,000                          [t CO2]
CH4:   Q × EF_CH4 / 1,000 (kg) × GWP_CH4 / 1,000   [t CO2e]
N2O:   Q × EF_N2O / 1,000 (kg) × GWP_N2O / 1,000   [t CO2e]
Total = sum; state the Hub edition and GWP set used
```

Pitfalls: applying the natural-gas-basis Hub factor to a coal-fired district
system (substantially understates); applying fuel factors without the
efficiency divisor (understates by the efficiency shortfall — ~20–25% at the
default 80% assumption); LHV/NCV fuel factors against HHV US quantities
(`ghg-protocol` §7).

**Chilled water** — if the supplier provides no factor, convert thermal
cooling to the driving energy:

```
Electric chillers:
  kWh_electric = ton-hours × 3.517 kWh_th/ton-hour ÷ COP
  Emissions    = kWh_electric × EF_grid (kg CO2e/kWh, current release —
                 see `s2-purchased-electricity`)
  (COP ≈ 4–6 for large electric centrifugal chillers; ask the supplier)

Absorption chillers (heat-driven):
  MMBtu_heat = ton-hours × 0.012 MMBtu/ton-hour ÷ COP_th
  (COP_th ≈ 0.7 single-effect, ≈ 1.2 double-effect), then apply the steam EF
```

Pitfall: applying the grid factor directly to thermal ton-hour-derived kWh
without dividing by COP (overstates by roughly the COP, i.e., ~4–6×).

### Method 3 — Floor-area estimation

```
MMBtu_est = floor area (ft²) × thermal intensity (kBtu/ft²·yr) / 1,000
Emissions = MMBtu_est × EF (supplier-specific or Hub default, as above)
```

Benchmarks: CBECS district-heat/space-heating intensities by building type
and climate zone (verify the current CBECS / Portfolio Manager technical
reference) — offices on district heat in cold climates commonly
~30–50 kBtu/ft²·yr (sanity range). Flag as estimated; prorate for
partial-floor tenancies and partial-year occupancy.

### Method 4 — Spend-based

```
MMBtu_est = steam spend ($) ÷ unit price ($/MMBtu)
Emissions = MMBtu_est × EF (as in Method 2)
```

Use the supplier's actual tariff schedule for the unit price — district
steam prices vary severalfold by city, so a generic national price badly
distorts the estimate. Screening quality only.

## CHP allocation

When the thermal energy comes from a combined heat and power plant, total
plant emissions must be **allocated between the co-products** so the steam
purchaser and the electricity purchasers don't double count. Governing
document: GHG Protocol **"Allocation of GHG Emissions from a Combined Heat
and Power (CHP) Plant"** guidance (companion tool to the Corporate Standard).
Three methods:

1. **Efficiency method (recommended)** — allocates in proportion to the fuel
   each output would have required in separate production. With the
   guidance's default reference efficiencies — **e_P = 35%** for electricity
   generation and **e_H = 80%** for heat generation:

```
E_heat  = E_total × (H / e_H) / (H / e_H + P / e_P)
E_power = E_total − E_heat
  where H = useful heat output, P = electricity output (same energy units),
  E_total = total plant GHG emissions
```

2. **Energy content method** — allocate by useful energy output shares
   (H vs P directly). Simple, but treats heat and electricity as equally
   valuable; tends to over-allocate to heat.
3. **Work potential method** — allocate by exergy (work potential) of each
   stream; steam's work potential depends on its pressure/temperature.
   Appropriate where heat is used for mechanical work.

State which method the supplier used; use the efficiency method with default
efficiencies when allocating yourself, and disclose the assumed efficiencies.

**CHP allocation walk-through** (efficiency method, symbolic):

```
Inputs:  E_total = total plant GHG emissions (t CO2e/yr, from supplier or
                   public reporting)
         H = useful heat/steam delivered (MMBtu)
         P = electricity output, converted to the same units
             (MWh × 3.412 MMBtu/MWh)
         e_H = 0.80, e_P = 0.35   (GHG Protocol CHP guidance defaults —
                                    method-defining parameters)
Steps:
  F_H = H / e_H          fuel-equivalent of separate heat production
  F_P = P / e_P          fuel-equivalent of separate power production
  heat share = F_H / (F_H + F_P)
  E_heat  = E_total × heat share;   EF_steam = E_heat / H    [t CO2e/MMBtu]
  E_power = E_total − E_heat;       EF_elec  = E_power / P   [t CO2e/MWh]
A customer buying Q MMBtu of this steam reports Q × EF_steam in scope 2.
```

Note: an efficiency-method allocation for gas-fired CHP typically yields a
steam factor **below** the EPA Hub boiler-basis default — cogeneration
credit is real; applying the boiler default to CHP steam typically
overstates.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| EPA GHG Emission Factors Hub | "Steam and Heat" row (CO2, CH4, N2O); natural-gas basis at an assumed 80% boiler efficiency | US purchased steam/heat default | kg CO2/MMBtu; g CH4, N2O/MMBtu (HHV) | Annual |
| EPA Hub / 40 CFR Part 98 Table C-1 | Fuel combustion factors — build EF_fuel ÷ efficiency for non-gas systems | US fuels, HHV basis | kg/MMBtu | Annual (Hub); Part 98 as amended |
| Supplier disclosure | District energy provider's annual factor letter (fuel mix, CHP allocation method, generated vs delivered basis) | Contracted supply | kg CO2e/MMBtu, /GJ, or /ton-hour | Request annually |
| GHG Protocol CHP allocation guidance | Default reference efficiencies (35% power / 80% heat) — method parameters, not factors | CHP allocation | — | Static guidance |
| UK DESNZ conversion factors | "Heat and steam" factor | UK district heat | kg CO2e/kWh | Annual |
| IPCC 2006 GL / national fuel factors | Fuel factors ÷ plant efficiency for non-US systems | Non-US | NCV basis — convert (`ghg-protocol` §7) | Per publication |
| Grid factors (electric chilled-water conversion) | see `s2-purchased-electricity` | — | kg CO2e/kWh | Annual |

Record source, year, and units for every factor used (`ghg-protocol` §7).

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **klb (Mlb) steam → energy**: energy content depends on delivery pressure/
  temperature and condensate return. ENERGY STAR Portfolio Manager
  convention: **1 klb district steam ≈ 1.194 MMBtu**; ask the supplier for
  the actual enthalpy basis before defaulting.
- **MMBtu vs GJ**: 1 MMBtu = 1.05506 GJ; 1 GJ = 0.9478 MMBtu. Mixed-unit
  portfolios (US MMBtu, EU GJ) must be converted before summing.
- **MMBtu vs MBtu vs kBtu**: MMBtu = 10^6 Btu; "MBtu" is ambiguous (10^3 in
  Roman-numeral convention, often misused for 10^6) — resolve from context
  and magnitude before converting.
- **Ton-hours → thermal kWh**: 1 ton refrigeration = 12,000 Btu/h, so
  **1 ton-hour = 12,000 Btu = 0.012 MMBtu = 3.517 kWh thermal**. Thermal kWh
  are not electric kWh — divide by COP before applying a grid factor.
- **lb/MMBtu vs kg/MMBtu** factors: ÷ 2.2046 (or × 0.4536) — mixing them
  shifts results 2.2×.
- **Gross vs net metering**: some steam accounts credit returned condensate
  or meter make-up water instead of steam; confirm the billed quantity is
  delivered energy, not a proxy needing conversion.
- **HHV vs LHV/NCV**: US quantities and EPA factors are HHV; IPCC/IEA fuel
  factors are NCV — converting wrongly shifts gas-based results ~10%
  (`ghg-protocol` §7).
- **Billing-period vs calendar-year cutoff**: steam bills are strongly
  seasonal — day-count proration of straddling winter bills matters more
  than for electricity; apply a consistent convention.

## Data collection & gap-filling

**Primary evidence**: district energy invoices (klb, MMBtu, GJ, or ton-hours
per billing period), BTU-meter or condensate-meter readouts, ENERGY STAR
Portfolio Manager exports (district steam / hot water / chilled water
meters), landlord statements with thermal allocations, the supplier's annual
emission factor letter and fuel-mix disclosure (for CHP: allocation method
and reference efficiencies used).

**Gap-filling** (document, apply consistently, flag filled values —
`ghg-protocol` §8):
- **Missing month**: same month prior year scaled by **heating degree days**
  (steam/heat) or **cooling degree days** (chilled water):
  `Q_est = Q_prior × (DD_cur / DD_prior)`. Straight adjacent-month averaging
  is inappropriate for seasonal thermal loads.
- **Missing site**: like-facility intensity (kBtu/ft² by building type and
  climate zone).
- **Move-in/move-out**: prorate by occupancy days within the billing month;
  acquisitions from acquisition date (`ghg-protocol` §6).
- **Supplier factor lag**: suppliers often publish the factor months after
  year-end — use prior-year factor as placeholder, true-up on receipt, and
  note the substitution.

## QA checks

- **Thermal intensity sanity**: kBtu/ft²·yr of purchased heat within climate-
  appropriate range (roughly 20–80 for offices; hospitals and labs higher);
  chilled water roughly 1–5 ton-hours/ft²·yr for offices in cooling climates.
  Flag ±50% vs benchmark or prior year.
- **Seasonality**: steam consumption should peak in winter months, chilled
  water in summer — a flat profile suggests estimated reads or unit errors.
- **CHP factor reasonableness**: an efficiency-method gas-CHP steam factor
  should land below the EPA Hub boiler-basis default; well above it implies
  coal fuel, energy-content allocation, or an error.
- **Unit audit**: confirm klb→MMBtu enthalpy, ton-hour→kWh_th, and COP
  application on a sample of invoices each cycle.
- **No double counting**: fuel for own boilers not also counted as purchased
  heat; supplier factor basis (generated vs delivered) consistent with any
  scope 3 category 3 loss line.
- Factor metadata (source, year, units, CO2 vs CO2e, allocation method)
  recorded for every EF.

## Worked FAQ

**Q1. We buy Con Ed-type district steam billed in klb. How do we account for
it with no supplier factor?**
Two steps: convert klb to energy (Portfolio Manager convention ≈ 1.194
MMBtu/klb — but ask the supplier for the actual enthalpy basis), then apply
the EPA Hub "Steam and Heat" defaults (current edition, CO2 + CH4 + N2O with
your stated GWP set) per the Method 2 walk-through. Better: request the
utility's published steam factor — large district systems typically publish
one, it reflects the actual CHP fleet, and it moves you to Method 1.

**Q2. Our supplier's CHP plant discloses total emissions, steam output, and
power output; we bought part of the steam. Our scope 2?**
Allocate with the efficiency method and the guidance defaults (e_H = 0.80,
e_P = 0.35): convert power output to the same energy units, compute the
fuel-equivalents H/e_H and P/e_P, take the heat share, derive EF_steam =
allocated heat emissions ÷ delivered steam, and multiply by your purchased
quantity (full walk-through in the CHP section). Disclose the method and
efficiencies used.

**Q3. District cooling invoice shows ton-hours; supplier says electric
chillers with a stated COP. Emissions?**
Convert down the chain: ton-hours × 3.517 → thermal kWh; ÷ the supplier's
COP → electric kWh; × the current subregion grid factor (eGRID/IEA — see
`s2-purchased-electricity`). If the supplier publishes its own kg
CO2e/ton-hour factor, prefer it (Method 1).

**Q4. Do purchased steam and heat get dual-reported like electricity?**
Yes in principle — the Scope 2 Guidance covers all purchased energy. In
practice there is rarely a certificate market or residual mix for heat, so
the market-based figure equals either the **supplier-specific factor** (if
disclosed — that is your "contractual" information) or the same default used
for location-based. Report one number and note the equivalence, or two if a
supplier factor exists.

**Q5. Our landlord's gross lease includes steam heat with no meter — what
now?**
Method 3: estimate MMBtu from your leased area × a CBECS-type district-heat
intensity for the building type and climate zone, apply the Method 2 default
(or a supplier factor if the building's provider publishes one), and flag as
estimated. Ask the landlord for the building's steam total and your area
share to move to Method 1/2 next year.

**Q6. We own the CHP and sell steam to a neighbor — what do we report?**
All fuel combustion is your **scope 1** (see `s1-stationary-combustion`); do
not deduct exported steam from scope 1. You may separately disclose the
emissions attributable to exported steam (allocated by the efficiency
method) as an information item; the neighbor reports that allocation as its
scope 2. Provide them the factor and method so the two inventories align.

## References

- GHG Protocol Corporate Standard (2004, rev.), ch. 4.
- GHG Protocol **Scope 2 Guidance** (2015) — applies to steam, heat, and
  cooling; ch. 6 (contractual data incl. supplier rates), ch. 7 (Quality
  Criteria), ch. 8 (calculation).
- GHG Protocol, **"Allocation of GHG Emissions from a Combined Heat and Power
  (CHP) Plant"** — efficiency, energy content, and work potential methods;
  default reference efficiencies.
- US **EPA GHG Emission Factors Hub** (annual) — steam and heat factors;
  40 CFR Part 98 fuel factors.
- **IPCC 2006 Guidelines** / national factors for non-US fuel bases; UK DESNZ
  heat-and-steam factor (annual).
- CBECS (EIA) / ENERGY STAR Portfolio Manager technical reference
  (thermal conversions incl. steam klb→MMBtu; intensity benchmarks).
- Grid factors for chilled-water conversion: `s2-purchased-electricity`.
- Cross-cutting conventions: the `ghg-protocol` skill (GWPs §4, base year §6,
  EF hierarchy §7, data quality §8).
