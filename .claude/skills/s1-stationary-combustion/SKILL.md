---
name: s1-stationary-combustion
description: >-
  Scope 1 stationary combustion methodology. Use for questions about natural
  gas, boilers, furnaces, ovens, kilns, dryers, water heaters, diesel/gasoline
  emergency generators, on-site CHP, flares, fuel oil, propane/LPG, coal, or
  biomass/wood/biogas burned in fixed equipment. Also routes here: fuel
  combustion emission factors (EPA Hub Table 1, Part 98 Table C-1, DEFRA fuel
  tables, IPCC 2006 Vol. 2 defaults), HHV vs NCV conversion, therms/MMBtu/GJ
  unit math, and estimating fuel use from spend or floor area.
---

# Scope 1 — Stationary Combustion

Stationary combustion is the intentional oxidation of fuel in fixed equipment
(boilers, furnaces, heaters, incinerators, engines, turbines, flares) owned or
controlled by the reporting company. It produces CO2, CH4, and N2O; CO2
dominates (typically >99% of CO2e for gas and oil). Governing documents:
GHG Protocol Corporate Standard (2004) ch. 4 & 6; GHG Protocol cross-sector
tool *"GHG emissions from stationary combustion"* (worksheet tool, latest
version); IPCC 2006 GL Vol. 2 (Energy), ch. 1–2; in the US, 40 CFR Part 98
Subpart C defines the tier methods and default factors that the EPA GHG
Emission Factors Hub republishes. Cross-cutting conventions (GWP set choice,
biogenic reporting, EF hierarchy, base year) live in the `ghg-protocol` skill.

## Boundary & classification

**In scope 1 (stationary):** all fuel burned in fixed equipment at facilities
inside the organizational boundary — boilers, furnaces, process heaters, kilns,
dryers, thermal oxidizers, stationary engines and turbines (including
emergency/backup generators), on-site incinerators, flares, and owned/operated
CHP plants.

Common misclassifications and the corrections:

| Situation | Wrong treatment | Correct treatment |
|---|---|---|
| Wood, biogas, biomethane, biogenic waste burned on site | CO2 added to scope 1 | Biogenic CO2 reported **outside the scopes** as a separate line; CH4 and N2O from the same combustion **stay in scope 1** (see `ghg-protocol` §5) |
| Biofuel blend in a generator (e.g., B20) | Whole volume at the fossil EF | Split: fossil share → scope 1 CO2; bio share → biogenic CO2 line; CH4/N2O on the whole quantity |
| Emergency/backup generators | Omitted as "immaterial by default" | In scope 1; usually small but must be screened — request runtime hours or fuel deliveries; document if excluded as de minimis |
| Flares (landfill gas, process gas) | Omitted or treated as fugitive | Combustion source → stationary combustion. Fossil flare gas → scope 1 CO2; landfill/digester gas CO2 is biogenic, but CH4 slip from incomplete combustion is scope 1 |
| CHP the company **owns/operates** | Only the electricity share counted | 100% of fuel combustion is scope 1; if heat/power is sold to others, emissions may be allocated for reporting to buyers, but the reporter's scope 1 is the full combustion (see `s2-steam-heat-cooling` for the allocation math on the buyer side) |
| Steam/heat **purchased** from a third-party plant | Scope 1 | Scope 2 → route to `s2-steam-heat-cooling` |
| Leased building where the reporter (lessee) controls operations and pays the gas bill | Scope 3 cat. 8 | Under **operational control** (and usually financial control): scope 1 for the lessee. Under equity share or if the lessor operates the systems: lessee reports under scope 3 category 8 → `s3-c08-upstream-leased-assets`. Landlord mirror-image: cat. 13 vs scope 1 |
| Company vehicles fueled from an on-site tank | Stationary (because the tank is fixed) | Classification follows the **combustion equipment**, not the tank: road vehicles → `s1-mobile-combustion`; a stationary engine fed from the same tank stays here. Allocate tank throughput between the two |
| Natural gas leaks, venting | Stationary combustion | Uncombusted releases are fugitive → `s1-fugitive-emissions` |
| Upstream production/transport of the fuel (well-to-tank) | Added to scope 1 | Scope 3 category 3 → `s3-c03-fuel-energy-related` |

## Method ladder

| # | Method | Data needed | Part 98 analogue | Typical use |
|---|---|---|---|---|
| 1 | CEMS / direct stack measurement | Continuous CO2 (or O2/flow-derived) monitoring | Tier 4 | Large regulated units (power, cement) |
| 2 | Fuel quantity × measured carbon content / measured HHV | Metered fuel + lab analyses | Tier 3 (carbon), Tier 2 (measured HHV × default EF) | Coal, process gas, variable-quality fuels |
| 3 | Fuel quantity × published fuel EF | Metered/invoiced fuel quantity | Tier 1 | **The standard method** for nearly all corporate reporters |
| 4 | Estimation: spend ÷ price, floor-area intensity, prior-year extrapolation | Spend, ft², partial-year data | — | Gap-filling, screening, small leased sites |

### Method 1 — CEMS / direct measurement

**When:** the unit already has a certified continuous emissions monitoring
system (typically because a regulator requires it — US Part 75/Part 98 Tier 4,
EU ETS). Rarely installed voluntarily.

**Data:** hourly CO2 concentration and stack gas flow, QA'd per the applicable
monitoring plan; fuel data still needed for CH4/N2O (CEMS measures CO2 only).

```
CO2 (t) = Σ_hours [ CO2 concentration × stack flow × unit conversions ]   (per monitoring plan)
CH4, N2O  = fuel heat input (MMBtu or TJ) × gas-specific EF               (Tier 1 style, below)
```

**Pitfalls:** biogenic and fossil CO2 arrive commingled in the stack — for
mixed fuels (e.g., coal + biomass co-firing) split using fuel records or ASTM
D6866 biogenic carbon testing. Do not double count: if a unit is covered by
CEMS, exclude its fuel from the Method 3 calculation.

### Method 2 — Measured carbon content / measured heat content (mass balance)

**When:** fuel quality varies enough that defaults misstate emissions —
coal, petroleum coke, refinery/process gas, waste-derived fuels. This is the
Part 98 **Tier 3** approach (Tier 2 = measured HHV × default per-MMBtu EF).

**Data:** metered fuel quantity per period; lab analyses of carbon content
(mass %) and, for Tier 2, HHV; sampling frequency per Part 98 §98.34 or
supplier certificates of analysis.

```
CO2 (kg) = fuel mass (kg) × carbon fraction (kg C/kg fuel) × 44/12 × oxidation factor
```

Oxidation factor: 1.00 by default (IPCC 2006 GL Vol. 2 ch. 1 and Part 98 both
assume complete oxidation unless measured otherwise).

**Worked example** — 1,000 metric tons of bituminous coal, measured average
carbon content 68.0% (as received):

```
CO2 = 1,000,000 kg × 0.680 × (44/12)
    = 1,000,000 × 0.680 × 3.6667
    = 2,493,333 kg  ≈ 2,493 t CO2
```

CH4/N2O still come from energy-basis defaults: with measured HHV
28.5 GJ/t → 28,500 GJ = 28.5 TJ; IPCC 2006 Vol. 2 Table 2.2 (energy
industries, NCV basis — convert first, see unit traps): CH4 1 kg/TJ, N2O
1.5 kg/TJ → ~28.5 kg CH4 and ~42.8 kg N2O ≈ 0.80 + 11.3 = 12.1 t CO2e
(AR5: CH4 28, N2O 265) — ~0.5% of the CO2. Round-trip check: 2,493 t CO2 /
1,000 t coal = 2.49 t/t, inside the plausible 2.2–2.7 range for bituminous.

**Pitfalls:** carbon content basis (as-received vs dry vs dry-ash-free) must
match the mass basis of the fuel quantity; moisture mismatches shift results
5–15%. Weighted-average the lab results by tonnage, not a simple mean.

### Method 3 — Fuel quantity × published EF (the standard method)

**When:** you have invoiced or metered fuel quantities. This covers >90% of
corporate stationary combustion reporting.

**Data:** fuel quantity by fuel type per site per period, from utility
invoices (natural gas), delivery tickets/tank fill logs (oil, propane, coal),
or meters.

**EF sources (in `ghg-protocol` §7 hierarchy order):**
- **US:** EPA GHG Emission Factors Hub, Table 1 "Stationary Combustion"
  (republishes 40 CFR Part 98 Tables C-1 heat contents/CO2 and C-2 CH4/N2O).
  All energy-basis factors are **HHV**.
- **UK:** DESNZ/DEFRA GHG Conversion Factors, "Fuels" tab (annual; gives
  kg CO2e per kWh gross-CV and net-CV, per liter, per tonne, with CO2/CH4/N2O
  broken out).
- **Rest of world / default:** IPCC 2006 GL Vol. 2, Tables 1.4 (NCVs), 2.2–2.5
  (EFs, **NCV basis**, kg per TJ).
- The GHG Protocol stationary combustion tool bundles IPCC defaults with a
  built-in calculator.

**Two factor bases — pick per your activity data:**

*Energy basis* (gas billed in therms, MMBtu, kWh, GJ):

```
E_gas (kg) = energy (MMBtu, HHV) × EF_gas (kg or g / MMBtu)
CO2e (kg)  = CO2 + CH4 (kg) × GWP_CH4 + N2O (kg) × GWP_N2O
```

**Worked example** — US office, 12,000 therms of natural gas for the year
(EPA Hub 2025 / Part 98 Table C-1 & C-2; AR5 GWPs: CH4 28, N2O 265):

```
Energy   = 12,000 therms × 0.1 MMBtu/therm            = 1,200 MMBtu (HHV)
CO2      = 1,200 MMBtu × 53.06 kg CO2/MMBtu           = 63,672 kg
CH4      = 1,200 MMBtu × 1.0 g/MMBtu = 1,200 g        → 1.20 kg × 28  =  33.6 kg CO2e
N2O      = 1,200 MMBtu × 0.10 g/MMBtu = 120 g         → 0.12 kg × 265 =  31.8 kg CO2e
Total    = 63,672 + 33.6 + 31.8 = 63,737 kg ≈ 63.7 t CO2e
```

*Volume/mass basis* (fuel bought in gallons, liters, tonnes):

```
E_CO2 (kg) = volume (gal) × EF (kg CO2/gal)
```

**Worked example** — 3,500 US gallons of diesel (distillate No. 2) in backup
generators (EPA Hub 2025):

```
CO2      = 3,500 gal × 10.21 kg CO2/gal               = 35,735 kg
Energy   = 3,500 gal × 0.138 MMBtu/gal                = 483 MMBtu (HHV)
CH4      = 483 × 3.0 g/MMBtu  = 1,449 g → 1.449 kg × 28  =  40.6 kg CO2e
N2O      = 483 × 0.60 g/MMBtu =   290 g → 0.290 kg × 265 =  76.8 kg CO2e
Total    = 35,735 + 40.6 + 76.8 ≈ 35,852 kg ≈ 35.9 t CO2e
```

**Worked example, UK/DEFRA style** — 250,000 kWh of natural gas (UK bills in
kWh, gross CV). DEFRA 2024 natural gas ≈ 0.1829 kg CO2e/kWh (gross CV,
CO2+CH4+N2O bundled; verify current-year table):

```
250,000 kWh × 0.1829 kg CO2e/kWh = 45,725 kg ≈ 45.7 t CO2e
```

**Worked example, IPCC default** — 100,000 m³ of natural gas, non-US/UK site,
measured NCV 37.0 MJ/m³ (IPCC 2006 Vol. 2 Table 2.4, NCV basis: CO2
56,100 kg/TJ; CH4 5 kg/TJ, N2O 0.1 kg/TJ for commercial/institutional):

```
Energy = 100,000 m³ × 37.0 MJ/m³ = 3,700,000 MJ = 3.70 TJ (NCV)
CO2    = 3.70 × 56,100 = 207,570 kg
CH4    = 3.70 × 5   = 18.5 kg × 28  = 518 kg CO2e
N2O    = 3.70 × 0.1 = 0.37 kg × 265 =  98 kg CO2e
Total  ≈ 208.2 t CO2e
```

**Pitfalls:**
- Applying an HHV-basis factor (EPA) to NCV-quantified energy or vice versa —
  ~10% error for gas (see unit traps).
- Natural gas invoices in m³ or ccf without the billed energy: use the
  utility's stated calorific value, not a generic one, where available.
- Blended/biogenic fuels at the fossil factor (split them).
- Double counting deliveries vs consumption for tank fuels: deliveries ≈
  consumption only over a full year with similar start/end tank levels;
  otherwise adjust for inventory change.

### Method 4 — Estimation (spend, intensity benchmarks, extrapolation)

**When:** invoices unavailable (small leased sites, missing months,
screening). High uncertainty — flag as estimated (`ghg-protocol` §8).

**(a) Spend ÷ unit price → quantity, then Method 3:**

```
Quantity = spend ($) ÷ average unit price ($/unit, same region & period)
```

Example: $8,000 annual gas spend, average commercial rate $1.10/therm (EIA
state-level commercial price for the year) → 7,273 therms → 727.3 MMBtu ×
53.06 = **38.6 t CO2** (+ CH4/N2O as above). Never apply a combustion EF to
dollars directly; convert to physical units first (a spend-based EEIO factor
is a different, life-cycle boundary — see `ghg-protocol` §3 tier 5).

**(b) Floor-area energy intensity:** US commercial → EIA **CBECS 2018**
(Table E7 and related give natural gas intensity by building type; offices are
on the order of 30–40 kBtu/ft²·yr of gas — pull the actual figure for the
building type and census region). Manufacturing → EIA MECS. UK → CIBSE/DEC
benchmarks.

Example: 20,000 ft² office, no gas data; CBECS office gas intensity taken as
33 kBtu/ft²·yr → 660 MMBtu × 53.06 = **35.0 t CO2** (label: estimated,
CBECS 2018 intensity).

**(c) Missing-month extrapolation:** use same-month prior year (for
weather-driven heating loads) or daily-average of adjacent months for
non-seasonal loads; degree-day normalization if HDD data are handy. Document
which months are filled.

**Pitfalls:** intensity benchmarks embed climate and vintage assumptions;
don't apply US CBECS to non-US buildings. Prior-year rollover must be flagged
and replaced when actuals arrive.

## Emission factors quick reference

All values below: verify against the **current-year** publication before use —
EPA updates the Hub roughly annually (Part 98 CO2 factors are stable; CH4/N2O
and heat contents occasionally revise), DEFRA/DESNZ republishes every June.

| Fuel | Factor | Units | Source & vintage |
|---|---|---|---|
| Natural gas | 53.06 | kg CO2/MMBtu (HHV) | EPA Hub 2025 / Part 98 Table C-1 |
| Natural gas | 1.0 / 0.10 | g CH4 / g N2O per MMBtu | EPA Hub 2025 / Part 98 Table C-2 |
| Natural gas heat content | 1.026 | MMBtu per 1,000 scf (HHV) | EPA Hub 2025 |
| Natural gas (UK) | ≈0.1829 | kg CO2e/kWh (gross CV) | DEFRA/DESNZ 2024 |
| Natural gas (IPCC) | 56,100 | kg CO2/TJ (NCV) | IPCC 2006 Vol. 2 Table 2.2 |
| Distillate fuel oil No. 2 (diesel) | 10.21 / 73.96 | kg CO2/gal · kg CO2/MMBtu (HHV) | EPA Hub 2025 |
| Residual fuel oil No. 6 | 11.27 / 75.10 | kg CO2/gal · kg CO2/MMBtu | EPA Hub 2025 |
| Kerosene | 10.15 | kg CO2/gal | EPA Hub 2025 |
| Propane | 5.72 / 62.87 | kg CO2/gal · kg CO2/MMBtu | EPA Hub 2025 |
| LPG (UK) | ≈1.56 | kg CO2e/liter | DEFRA/DESNZ 2024 |
| Gas oil (UK) | ≈2.76 | kg CO2e/liter | DEFRA/DESNZ 2024 |
| Petroleum products, generic | 3.0 / 0.60 | g CH4 / g N2O per MMBtu | EPA Hub 2025 / Table C-2 |
| Bituminous coal | 93.28 | kg CO2/MMBtu (HHV) | EPA Hub 2025 |
| Sub-bituminous coal | 97.17 | kg CO2/MMBtu (HHV) | EPA Hub 2025 |
| Coal (any) | 11 / 1.6 | g CH4 / g N2O per MMBtu | EPA Hub 2025 / Table C-2 |
| Wood & wood residuals | 93.80 (biogenic) | kg CO2/MMBtu (HHV) | EPA Hub 2025 |
| Wood | 7.2 / 3.6 | g CH4 / g N2O per MMBtu (in scope 1) | EPA Hub 2025 |
| Landfill gas / biogas | 52.07 (biogenic); 3.2 / 0.63 | kg CO2/MMBtu; g CH4 / g N2O per MMBtu | EPA Hub 2025 |
| Diesel/gas oil (IPCC) | 74,100 | kg CO2/TJ (NCV) | IPCC 2006 Vol. 2 Table 2.2 |

DEFRA fuel factors are **kg CO2e** (CO2+CH4+N2O pre-bundled, current-year
UK-official GWPs) — do not add separate CH4/N2O on top; EPA/IPCC factors are
per-gas — you must add CH4/N2O and choose the GWP set yourself.

## Unit and conversion traps

- **HHV/GCV vs NCV/LHV.** US (EPA, Part 98) factors and US fuel billing are
  **HHV/gross**; IPCC and IEA are **NCV/net**. NCV ≈ GCV × 0.90 for natural
  gas (~10% gap, latent heat of water vapor) and ≈ GCV × 0.95 for coal and oil
  (~5%) — IPCC 2006 Vol. 2 ch. 1 convention. Applying a kg/TJ-NCV factor to
  HHV energy overstates gas CO2 ~10%. Per-MMBtu factor pairs differ too:
  53.06 kg/MMBtu-HHV ≈ 56.1 t/TJ-NCV for gas — same physics, different basis.
- **Therms and decatherms.** 1 therm = 0.1 MMBtu = 105.5 MJ; 1 Dth (dekatherm)
  = 10 therms = 1 MMBtu. 1 MMBtu = 1.05506 GJ. 1 kWh = 3,412 Btu = 3.6 MJ.
- **ccf/Mcf vs energy.** 1 Mcf (1,000 scf) gas ≈ 1.026 MMBtu HHV (EPA default;
  use the utility's CV when stated). "MCF" (thousand) vs "MMCF" (million):
  a 1,000× blunder that QA must catch.
- **US vs imperial gallons.** 1 US gal = 3.78541 L; 1 imperial gal = 4.54609 L
  = 1.2009 US gal. UK fuel records in liters, US factors per US gallon.
- **LPG mass vs volume.** Propane ≈ 0.493 kg/L (≈1.87 kg per US gal) at
  ambient; tank fills quoted in gallons, kg, or % of tank — confirm which.
  A "gallon" of propane is liquid volume, not vapor.
- **Gas volume reference conditions.** Nm³ (0 °C), Sm³ (15 °C), scf (60 °F)
  differ by several %; UK bills apply a volume correction factor (typically
  1.02264) before converting m³ → kWh via the local CV. Use the billed kWh
  when present instead of re-deriving.
- **Short tons vs metric tons vs long tons** for coal: 1 short ton = 0.9072 t.

## Data collection & gap-filling

Request per facility:
- **Natural gas:** 12 months of utility invoices or a consumption export
  (therms/kWh/m³ + billed CV); meter numbers to map to facilities.
- **Oil/propane/coal:** delivery tickets or supplier annual statements, tank
  fill logs, start/end tank inventory levels (dip readings) for the year.
- **Generators:** fuel purchase records or runtime hours × nameplate
  consumption (gal/hr) as fallback.
- **Flares/CHP:** fuel metering, gas composition analyses, operating logs.
- **Leased space:** landlord energy statements or lease-area allocation of
  building gas (allocate by leased ft² share if sub-metering is absent —
  document the allocation basis). If the landlord operates the systems and
  the boundary approach puts it out of scope 1, route to `s3-c08`.

Gap-filling (per `ghg-protocol` §8): pro-rata annualization of partial-year
data, same-month prior year for heating fuels, like-facility intensity
(MMBtu/ft²) for sites with no data at all. Flag every filled value.

## QA checks

- **Year-over-year variance:** flag site-level changes >±15% without a known
  driver (weather, occupancy, equipment change); check HDD-normalized gas use.
- **Intensity sanity:** gas MMBtu/ft² vs CBECS-type benchmarks for the
  building type; boiler fuel vs production output for industrial sites.
- **Unit-error red flags:** results off by ~1,000× (kg vs t, Mcf vs MMcf,
  MJ vs GJ), ~10× (therms vs MMBtu/Dth), ~25× (m³ read as therms, since
  1 m³ ≈ 0.354 therms — a factor near 3, while ccf vs Mcf is 10×; any
  "suspiciously round" multiple warrants a unit audit), ~1.2× (imperial vs
  US gallons), ~1.1× (HHV/NCV).
- **Completeness vs facility list:** reconcile reporting sites against the
  real-estate/asset register; every site with a gas meter, tank, generator, or
  kitchen should appear or have a documented zero/de-minimis.
- **Per-gas share check:** CH4+N2O should be ≲1% of CO2e for gas/oil; if
  higher, a gram/kilogram slip is likely.
- **Biogenic line check:** wood/biogas CO2 must appear in the biogenic memo
  line, not scope 1; scope 1 should still contain their CH4/N2O.

## Worked FAQ

**Q1. Our US HQ used 48,500 therms of natural gas. Scope 1 emissions?**
48,500 therms = 4,850 MMBtu. CO2 = 4,850 × 53.06 = 257,341 kg. CH4 = 4,850 ×
1.0 g = 4.85 kg × 28 = 135.8 kg CO2e. N2O = 4,850 × 0.10 g = 0.485 kg × 265 =
128.5 kg CO2e. **Total ≈ 257.6 t CO2e** (EPA Hub 2025 factors, AR5 GWPs;
verify current-year Hub).

**Q2. A landlord-operated leased office where we pay pro-rated gas — scope 1?**
Depends on your consolidation approach and who has operational control of the
combustion equipment. If the landlord operates the boiler, most companies
using operational control report the allocated gas under **scope 3 category
8** (upstream leased assets), calculated the same way (allocated therms × EF).
If you operate the heating system under your lease, it is scope 1. State the
treatment in your inventory design; see `ghg-protocol` §2 and `s3-c08`.

**Q3. Backup generator burned 600 gal of B20 biodiesel blend. How to book it?**
Split by volume: fossil diesel 480 gal × 10.21 kg CO2/gal = 4,901 kg scope 1
CO2; biodiesel 120 gal × 9.45 kg CO2/gal (EPA Hub 2025, biodiesel 100%) =
1,134 kg **biogenic CO2, outside the scopes**. CH4/N2O on total energy:
600 gal × 0.138 MMBtu/gal ≈ 82.8 MMBtu (diesel HHV as proxy) × (3.0 g CH4 +
0.60 g N2O)/MMBtu → 0.248 kg CH4 (7.0 kg CO2e) + 0.0497 kg N2O (13.2 kg CO2e).
**Scope 1 ≈ 4.92 t CO2e; biogenic ≈ 1.13 t CO2.**

**Q4. UK site burned 30,000 liters of gas oil in a boiler. Emissions?**
DEFRA/DESNZ 2024 gas oil ≈ 2.76 kg CO2e/L (bundled CO2+CH4+N2O; verify
current table): 30,000 × 2.76 = 82,800 kg ≈ **82.8 t CO2e**. Do not add
separate CH4/N2O — the DEFRA CO2e factor already includes them. If you need
per-gas reporting, use DEFRA's CO2/CH4/N2O column breakout instead.

**Q5. We co-fire 5,000 t wood chips (HHV 9.0 MMBtu/t as received) with coal.
Where does the wood go?**
Energy = 45,000 MMBtu. Biogenic CO2 = 45,000 × 93.80 kg/MMBtu = 4,221 t →
**outside-of-scopes biogenic line**. Scope 1 keeps CH4 = 45,000 × 7.2 g =
324 kg × 28 = 9.07 t CO2e and N2O = 45,000 × 3.6 g = 162 kg × 265 = 42.9 t
CO2e → **≈52.0 t CO2e in scope 1** from the wood, plus the coal computed
normally. (EPA Hub 2025; AR5.)

**Q6. Only 9 months of gas invoices exist for a site (Jan–Sep, 21,000 therms).
Annualize how?**
Gas heating is seasonal — do not simple-average. Use same-months prior year to
estimate the Oct–Dec share (e.g., if Oct–Dec was 38% of the prior year's
total, estimate full year = 21,000 ÷ 0.62 ≈ 33,900 therms), or HDD-weight the
missing months. Flag the 12,900-therm estimate as gap-filled and replace when
invoices arrive (`ghg-protocol` §8).

## References

- GHG Protocol Corporate Standard (rev. 2004), ch. 4 (operational boundaries),
  ch. 6 (identifying and calculating emissions).
- GHG Protocol cross-sector tool: *GHG emissions from stationary combustion*
  (calculation worksheet + guidance PDF), ghgprotocol.org/calculation-tools.
- IPCC 2006 Guidelines, Vol. 2 (Energy): ch. 1 (introduction, NCV/GCV
  conventions, Table 1.4 default NCVs), ch. 2 (stationary combustion,
  Tables 2.2–2.5 default EFs, kg/TJ NCV).
- US EPA GHG Emission Factors Hub (annual; Table 1 stationary combustion) —
  epa.gov/climateleadership/ghg-emission-factors-hub.
- 40 CFR Part 98 Subpart C (Tier 1–4 methods; Tables C-1, C-2).
- UK DESNZ/DEFRA Greenhouse Gas Reporting: Conversion Factors (annual, June),
  "Fuels" tab and methodology paper.
- EIA CBECS 2018 (commercial building energy intensities); EIA MECS
  (manufacturing); EIA fuel price series for spend-based estimation.
- Cross-cutting conventions: the `ghg-protocol` skill (§4 GWPs, §5 biogenic,
  §7 EF hierarchy, §8 data quality).
