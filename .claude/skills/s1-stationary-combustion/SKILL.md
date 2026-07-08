---
name: s1-stationary-combustion
description: >-
  Scope 1 stationary combustion methodology. Use for questions about natural
  gas, boilers, furnaces, ovens, kilns, dryers, water heaters, diesel/gasoline
  emergency generators, on-site CHP, flares, fuel oil, propane/LPG, coal, or
  biomass/wood/biogas burned in fixed equipment. Also routes here: fuel
  combustion emission factor sources (EPA Hub Table 1, Part 98 Table C-1,
  DEFRA fuel tables, IPCC 2006 Vol. 2 defaults), HHV vs NCV conversion,
  therms/MMBtu/GJ unit math, and estimating fuel use from spend or floor area.
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

**Method walk-through** — variable-quality solid fuel (e.g., coal):

```
M_fuel   = fuel mass burned (kg), from weighbridge/delivery records,
           adjusted for start/end inventory change
CF       = carbon fraction (kg C/kg fuel), tonnage-weighted average of the
           lab analyses, on the same moisture basis as M_fuel
CO2 (kg) = M_fuel × CF × (44/12) × oxidation factor

CH4/N2O:  Q_fuel (TJ, NCV) = M_fuel × measured heating value (basis-converted)
          CH4, N2O (kg)    = Q_fuel × EF_gas (IPCC 2006 Vol. 2 Table 2.2,
                             kg/TJ, NCV basis — convert first; see unit traps)
          CO2e             = CH4 × GWP_CH4 + N2O × GWP_N2O
                             (GWPs per the inventory's declared AR set)
```

CH4+N2O typically contribute well under 1% of CO2e for coal; a much larger
share signals a unit slip. Round-trip check: CO2 per tonne of fuel should land
in a plausible range for the fuel rank (roughly 2.2–2.7 t CO2/t for bituminous
coal).

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

**Method walk-through** (energy basis — gas billed in therms, MMBtu, kWh, GJ;
US/EPA style):

```
Q_fuel (MMBtu, HHV) = billed therms × 0.1   (or billed MMBtu/Dth directly)
CO2 (kg)  = Q_fuel × EF_CO2          — EPA Hub Table 1, kg CO2/MMBtu (HHV),
                                       current year
CH4 (kg)  = Q_fuel × EF_CH4 ÷ 1,000  — EPA Hub Table 1 / Part 98 Table C-2,
                                       g CH4/MMBtu
N2O (kg)  = Q_fuel × EF_N2O ÷ 1,000  — same source, g N2O/MMBtu
CO2e (kg) = CO2 + CH4 × GWP_CH4 + N2O × GWP_N2O
            — GWPs per the inventory's declared AR set (`ghg-protocol` §4)
```

*Volume/mass basis* (fuel bought in gallons, liters, tonnes): identical
structure with V_fuel × EF_CO2 (kg CO2/gal from EPA Hub Table 1), plus CH4/N2O
computed on the fuel's energy content (V_fuel × default heat content →
MMBtu × the per-MMBtu gas factors).

*Regional variants:* DEFRA/DESNZ factors arrive as **kg CO2e** per kWh (gross
or net CV), per liter, or per tonne with CH4/N2O pre-bundled at current
UK-official GWPs — apply directly to the billed quantity and do **not** add
separate CH4/N2O (use DEFRA's per-gas breakout columns when per-gas reporting
is required). IPCC 2006 defaults are kg per TJ on an **NCV** basis — convert
the activity data's basis first (see unit traps).

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
Quantity = spend ($) ÷ average unit price ($/unit, same region & period —
           e.g., EIA state-level commercial gas price for the year)
→ then Method 3 on the derived quantity
```

Never apply a combustion EF to dollars directly; convert to physical units
first (a spend-based EEIO factor is a different, life-cycle boundary — see
`ghg-protocol` §3 tier 5).

**(b) Floor-area energy intensity:** US commercial → EIA **CBECS 2018**
(Table E7 and related give natural gas intensity by building type; offices are
on the order of 30–40 kBtu/ft²·yr of gas — pull the actual figure for the
building type and census region). Manufacturing → EIA MECS. UK → CIBSE/DEC
benchmarks. Derive MMBtu = floor area × intensity, then feed Method 3; label
the result as estimated and cite the benchmark used (e.g., "CBECS 2018 office
gas intensity").

**(c) Missing-month extrapolation:** use same-month prior year (for
weather-driven heating loads) or daily-average of adjacent months for
non-seasonal loads; degree-day normalization if HDD data are handy. Document
which months are filled.

**Pitfalls:** intensity benchmarks embed climate and vintage assumptions;
don't apply US CBECS to non-US buildings. Prior-year rollover must be flagged
and replaced when actuals arrive.

## Emission factor sources

| Source | Governing table(s) | Coverage | Basis / units convention | Update cadence |
|---|---|---|---|---|
| EPA GHG Emission Factors Hub | Table 1 (Stationary Combustion), republishing 40 CFR Part 98 Tables C-1 (heat contents, CO2) and C-2 (CH4/N2O) | US fuels: natural gas, fuel oils, propane/LPG, coal, wood/biomass, landfill gas/biogas; CO2 per MMBtu and per gal/scf/ton; CH4/N2O per MMBtu; default heat contents | **HHV** basis; per-gas factors — you add CH4/N2O and choose the GWP set | Annual (Part 98 CO2 factors are stable; CH4/N2O and heat contents occasionally revise) |
| 40 CFR Part 98 Subpart C | Tables C-1, C-2 | Regulatory source behind the Hub; also defines the Tier 1–4 methods | HHV; per-gas | Amended by rulemaking (infrequent) |
| UK DESNZ/DEFRA GHG Conversion Factors | "Fuels" tab | UK fuels: kg CO2e per kWh (gross and net CV), per liter, per tonne, with CO2/CH4/N2O breakout columns | **CO2e pre-bundled** at current UK-official GWPs — do not add CH4/N2O on top | Annual (June) |
| IPCC 2006 GL Vol. 2 (Energy) | Table 1.4 (default NCVs); Tables 2.2–2.5 (EFs by sector) | Default factors for the rest of the world, all fuels, kg per TJ | **NCV** basis; per-gas | Static (2006); check the 2019 Refinement |
| GHG Protocol stationary combustion tool | Worksheet + guidance | Bundles the IPCC defaults with a built-in calculator | Per the bundled IPCC defaults | Check the current tool version at ghgprotocol.org |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **HHV/GCV vs NCV/LHV.** US (EPA, Part 98) factors and US fuel billing are
  **HHV/gross**; IPCC and IEA are **NCV/net**. NCV ≈ GCV × 0.90 for natural
  gas (~10% gap, latent heat of water vapor) and ≈ GCV × 0.95 for coal and oil
  (~5%) — IPCC 2006 Vol. 2 ch. 1 convention. Applying a kg/TJ-NCV factor to
  HHV energy overstates gas CO2 ~10%. The same fuel's per-MMBtu-HHV and
  per-TJ-NCV factors are different numbers describing the same physics —
  never mix bases.
- **Therms and decatherms.** 1 therm = 0.1 MMBtu = 105.5 MJ; 1 Dth (dekatherm)
  = 10 therms = 1 MMBtu. 1 MMBtu = 1.05506 GJ. 1 kWh = 3,412 Btu = 3.6 MJ.
- **ccf/Mcf vs energy.** 1 Mcf (1,000 scf) gas ≈ 1.026 MMBtu HHV (EPA default
  heat content; use the utility's CV when stated). "MCF" (thousand) vs "MMCF"
  (million): a 1,000× blunder that QA must catch.
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

## FAQ

**Q1. Our US HQ used 48,500 therms of natural gas. How do we compute scope 1?**
Method 3, energy basis: convert therms → MMBtu (× 0.1), apply the current-year
EPA Hub Table 1 natural gas CO2 factor (kg CO2/MMBtu, HHV), add CH4 and N2O
from the same table's g/MMBtu factors, and convert those with the inventory's
declared GWP set. Expect CH4+N2O to add well under 1% of the CO2e. Cite the
Hub publication year and GWP set in the disclosure.

**Q2. A landlord-operated leased office where we pay pro-rated gas — scope 1?**
Depends on your consolidation approach and who has operational control of the
combustion equipment. If the landlord operates the boiler, most companies
using operational control report the allocated gas under **scope 3 category
8** (upstream leased assets), calculated the same way (allocated therms × EF).
If you operate the heating system under your lease, it is scope 1. State the
treatment in your inventory design; see `ghg-protocol` §2 and `s3-c08`.

**Q3. Backup generator burned 600 gal of B20 biodiesel blend. How to book it?**
Split by volume: the 80% fossil-diesel share × the Hub Table 1 diesel CO2
factor → scope 1 CO2; the 20% biodiesel share × the Hub biodiesel (B100) CO2
factor → **biogenic CO2, outside the scopes**. CH4/N2O are computed on the
**whole** 600 gal via its energy content (gallons × heat content → MMBtu ×
the per-MMBtu CH4/N2O factors) and stay in scope 1. The classic errors:
burning the whole volume at the fossil factor, or dropping CH4/N2O on the bio
share.

**Q4. UK site burned 30,000 liters of gas oil in a boiler. Which factor?**
The current-year DEFRA/DESNZ "Fuels" tab, gas oil row, kg CO2e per liter —
applied directly to the liters. Do not add separate CH4/N2O — the DEFRA CO2e
factor already includes them. If you need per-gas reporting, use DEFRA's
CO2/CH4/N2O column breakout instead of the bundled CO2e column.

**Q5. We co-fire wood chips with coal. Where does the wood go?**
Compute the wood's energy (tonnage × HHV as received), apply the Hub Table 1
wood/biomass CO2 factor, and report that CO2 on the **outside-of-scopes
biogenic line**. The wood's CH4 and N2O (per-MMBtu factors × the declared
GWPs) **stay in scope 1**, alongside the coal computed normally. Two QA
failures to watch for: no biogenic line despite biomass fuel, or wood CO2
sitting inside scope 1.

**Q6. Only 9 months of gas invoices exist for a site (Jan–Sep, 21,000 therms).
Annualize how?**
Gas heating is seasonal — do not simple-average. Use same-months prior year to
estimate the Oct–Dec share (e.g., if Oct–Dec was 38% of the prior year's
total, estimate full year = 21,000 ÷ 0.62 ≈ 33,900 therms), or HDD-weight the
missing months. Flag the estimated portion as gap-filled and replace when
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
