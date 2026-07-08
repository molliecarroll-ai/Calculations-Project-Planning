---
name: s3-c03-fuel-energy-related
description: >-
  Scope 3 Category 3 (Fuel- and Energy-Related Activities) methodology
  assistant. Use for well-to-tank (WTT) / upstream fuel emissions, upstream
  emissions of purchased electricity (fuel-cycle), transmission and
  distribution (T&D) losses, and generation of purchased power resold by
  utilities. Covers DEFRA WTT tables, eGRID grid gross loss, IEA loss rates,
  and the lifecycle-minus-combustion factor arithmetic that avoids double
  counting with scopes 1 and 2.
---

# Scope 3 Category 3 — Fuel- and Energy-Related Activities (not in scope 1 or 2)

**Category definition (Scope 3 Standard, ch. 5, Table 5.4):** "Extraction,
production, and transportation of fuels and energy purchased or acquired by
the reporting company in the reporting year, not already accounted for in
scope 1 or scope 2." **Minimum boundary**, four activities:

- **(a) Upstream emissions of purchased fuels** — cradle-to-tank ("well-to-
  tank", WTT) emissions of fuels the reporter combusts (whose combustion is
  scope 1).
- **(b) Upstream emissions of purchased electricity/steam/heat/cooling** —
  WTT emissions of fuels consumed in generating the energy the reporter
  consumes (whose generation emissions are scope 2).
- **(c) Transmission & distribution (T&D) losses** — generation (combustion)
  emissions of the electricity/steam/heat/cooling lost in T&D between
  generator and the reporter's meter.
- **(d) Generation of purchased electricity that is sold to end users** —
  applies to utilities and power marketers: generation emissions of power
  they purchase and resell (reported here to avoid scope 2 for energy they
  don't consume).

Governing documents: Scope 3 Standard (2011), ch. 5; Technical Guidance for
Calculating Scope 3 Emissions (v1.0, 2013), Category 3 chapter. Cross-cutting
conventions are in the `ghg-protocol` skill.

## Boundary & classification

**In scope:** the upstream life-cycle stages of energy the reporter already
counts downstream: extraction, processing/refining, and transport of fuels;
WTT of generation fuels; the combustion emissions embodied in line losses.

**Out of scope / routed elsewhere — the no-double-counting rules:**
- **Combustion of fuels you purchased** → scope 1. Category 3(a) is only the
  upstream slice. Never apply a life-cycle (WTW) factor in scope 1 and then
  add Category 3 — see the factor arithmetic below.
- **Generation emissions of electricity you consume** → scope 2. Category 3
  adds only (b) WTT of generation fuels and (c) losses.
- Under the GHG Protocol, **T&D losses are Category 3, not scope 2**, for end
  consumers (this differs from some national schemes). Exception: a utility
  that purchases power, loses some in its own T&D system while delivering the
  rest to customers, reports the losses' generation emissions as its own
  **scope 2** (energy "consumed" by its network); end-use customers report
  their share of losses in Category 3(c). Do not report the same losses in
  both places.
- Fuels/electricity **purchased and resold without consumption** (activity d)
  are Category 3 for the reseller, never scope 2.
- Upstream emissions of fuels burned by **suppliers, carriers, leased assets,
  franchisees** are embedded in Categories 1, 4/9, 8/13, 14 respectively —
  Category 3 covers only energy *the reporter itself* purchases.
- **Market-based scope 2 users:** for consistency, Category 3(b)/(c) may be
  computed on a market-basis where supplier-specific fuel-mix data exists;
  in practice most reporters compute Category 3 on the location-based grid
  mix and disclose. State your basis.

**Factor arithmetic (the core identity):**

```
life-cycle (well-to-wheel/WTW) EF = combustion (tank-to-wheel) EF + WTT EF
=> WTT EF = life-cycle EF − combustion EF

Scope 1  uses combustion EF only.
Cat 3(a) uses WTT EF only.
Using a WTW factor in scope 1, or WTW in Cat 3, double counts.
```

## Method ladder

The Scope 3 Calculation Guidance (Category 3) offers two methods per
activity:

| # | Method | Activity data | Emission factor | Typical use |
|---|---|---|---|---|
| 1 | Supplier-specific | Fuel/energy quantities by supplier | Supplier-provided upstream/WTT factors (e.g., refinery- or field-specific), utility-specific loss rates | Large fuel buyers, utility data available |
| 2 | Average-data | Fuel/energy quantities | Published average WTT and loss factors (DEFRA/DESNZ WTT tables, eGRID GGL, IEA losses, GREET) | Default for nearly everyone |

Energy quantities are the same activity data already collected for scopes 1
and 2 — Category 3 is largely a re-multiplication exercise, which is why it
should never be omitted for "lack of data".

### Activity (a) — Upstream (WTT) emissions of purchased fuels

```
Emissions = Σ_fuels ( fuel quantity × WTT EF_fuel )
```

The **DEFRA/DESNZ UK Government GHG Conversion Factors "WTT — fuels" tables**
(annual) are the workhorse source: WTT factors per liter, kWh, tonne, for
every common fuel, maintained yearly. US alternative: derive WTT from
Argonne **GREET** life-cycle model minus EPA combustion factors.

**Worked example:** Fleet purchases 500,000 L diesel (average biofuel blend).

```
WTT: 500,000 L × 0.61 kg CO2e/L = 305,000 kg = 305 t CO2e
# DEFRA 2024 WTT table, diesel (average biofuel blend) ≈ 0.61 kg CO2e/L — verify current year
# (scope 1 combustion, separately: 500,000 L × ~2.51 kg CO2e/L ≈ 1,255 t CO2e)
```

WTT is typically **20–30% of combustion** for conventional fossil fuels —
a useful sanity ratio.

**Pitfalls:** applying WTT to fuels consumed by third parties (belongs in
Cats 1/4/etc.); biofuel blends — DEFRA WTT blend factors already reflect
blend shares including biofuel cultivation/processing (which can make biofuel
WTT *higher* than fossil WTT even though combustion CO2 is biogenic); HHV/NCV
mismatch when converting energy-basis factors (`ghg-protocol` §7).

### Activity (b) — Upstream (WTT) emissions of purchased electricity

```
Emissions = electricity consumed (kWh) × WTT-of-generation EF (kg CO2e/kWh)
```

Fuel-cycle factor = upstream emissions of the fuels burned to generate the
grid mix, per delivered kWh. DEFRA publishes "WTT — UK electricity"
(generation component) annually; for other grids use IEA life-cycle
extensions or national sources; absent anything better, approximate as
grid combustion EF × an upstream uplift for the generation mix (documented
assumption, ~10–25% for fossil-heavy grids).

### Activity (c) — T&D losses

```
Emissions = electricity consumed (kWh) × grid combustion EF (kg CO2e/kWh)
            × loss factor

# Loss factor conventions — state which you use:
#   losses-as-share-of-delivered:  L/(1−L)  applied to metered consumption
#   published "T&D loss EF" (DEFRA): already per kWh consumed — multiply directly
```

Loss rates: **eGRID Grid Gross Loss (GGL)** for the US, ~4.5–5% (eGRID 2022:
national GGL ≈ 4.8% — verify current eGRID release); **IEA** country loss
rates elsewhere (world average ~8%; EU mostly 4–7%; some grids, e.g. India,
15%+ — verify IEA World Energy Balances current edition). DEFRA publishes a
combined UK "T&D — UK electricity" factor (~0.018 kg CO2e/kWh consumed,
2024 — verify) plus a small "WTT of T&D" factor for the upstream slice of the
lost electricity.

**Worked example — one facility, all three activities (a)+(b)+(c):**
US facility, reporting year: 1,200,000 kWh grid electricity; 3,500 MMBtu
natural gas; 20,000 L diesel for backup generators.

```
(a) Fuel WTT
  Gas:    3,500 MMBtu × 293.07 kWh/MMBtu = 1,025,745 kWh(HHV)
          × 0.034 kg CO2e/kWh WTT            =  34,875 kg  # DEFRA 2024 WTT nat gas (gross CV) ≈ 0.034 — verify; US-specific: GREET
  Diesel: 20,000 L × 0.61 kg CO2e/L WTT      =  12,200 kg  # DEFRA 2024 WTT — verify

(b) Electricity upstream (fuel-cycle)
  1,200,000 kWh × 0.055 kg CO2e/kWh          =  66,000 kg  # illustrative fuel-cycle factor ≈ 15% of a 0.37 kg/kWh grid; use published value — verify

(c) T&D losses
  1,200,000 kWh × 0.373 kg CO2e/kWh × 0.048/(1−0.048)
                                             =  22,566 kg  # eGRID 2022 US-avg output EF ≈ 0.373 kg CO2e/kWh and GGL ≈ 4.8% — use subregion values; verify

Category 3 total ≈ 34,875 + 12,200 + 66,000 + 22,566 = 135,641 kg ≈ 136 t CO2e
```

Use the facility's **eGRID subregion** factor and GGL, not the national
average, in real work.

### Activity (d) — Generation of purchased electricity sold to end users

Utilities/retailers only:

```
Emissions = electricity purchased for resale (kWh) × generation EF of the
            purchased power (supplier-specific if known, else grid average)
```

**Worked example:** A retail electricity provider buys 2.0 TWh on the
wholesale market and resells it. Grid-average generation EF 0.35 kg CO2e/kWh
(illustrative — use the relevant market factor, verify).

```
2,000,000,000 kWh × 0.35 kg CO2e/kWh = 700,000 t CO2e (Category 3d)
```

The end customers of that power report the same generation emissions as
*their* scope 2 — that is expected and is not double counting within any one
inventory.

## Emission factors quick reference

Representative values — verify against the current publication year.

| Item | Factor | Source & vintage |
|---|---|---|
| Diesel WTT (avg biofuel blend) | ~0.61 kg CO2e/L | DEFRA/DESNZ 2024 WTT fuels — verify current year |
| Petrol WTT (avg biofuel blend) | ~0.59 kg CO2e/L | DEFRA 2024 WTT fuels — verify |
| Natural gas WTT | ~0.034 kg CO2e/kWh (gross CV) | DEFRA 2024 WTT fuels — verify; US supply chains differ (methane leakage) — consider GREET |
| Jet kerosene WTT | ~0.52 kg CO2e/L | DEFRA 2024 WTT fuels — verify |
| LPG WTT | ~0.19 kg CO2e/L | DEFRA 2024 WTT fuels — verify |
| UK electricity, generation (scope 2 ref) | ~0.207 kg CO2e/kWh | DEFRA 2024 — verify |
| UK electricity, WTT of generation (Cat 3b) | ~0.053 kg CO2e/kWh | DEFRA 2024 "WTT — UK electricity" — verify |
| UK electricity, T&D losses (Cat 3c) | ~0.018 kg CO2e/kWh consumed | DEFRA 2024 "T&D — UK electricity" — verify |
| US grid output EF (national) | ~0.37 kg CO2e/kWh | EPA eGRID 2022 (2024 release) — use subregion; verify |
| US grid gross loss (GGL) | ~4.8% | eGRID 2022 — verify current |
| Country T&D loss rates | EU ~4–7%; world avg ~8%; India ~15%+ | IEA World Energy Balances (current ed.) — verify |

## Unit and conversion traps

- **WTT vs WTW double counting** — the defining trap. Audit that scope 1 uses
  combustion-only factors and Category 3 uses WTT-only; if a source gives
  only life-cycle factors, subtract combustion explicitly and show the
  arithmetic.
- **HHV/GCV vs LHV/NCV:** DEFRA energy-basis factors are gross CV; IPCC/IEA
  are net CV; US MMBtu convention is HHV. Natural gas GCV≈1.108×NCV —
  mismatching shifts results ~10%.
- **Loss-factor algebra:** L as a share of *generation* vs of *delivered*
  electricity differ by the factor 1/(1−L). eGRID GGL is defined relative to
  delivered sales — apply consumption × L/(1−L) × generation EF, or use a
  pre-built per-kWh-consumed loss factor (DEFRA style) directly. Don't do
  both.
- **Generation vs consumption EF basis:** some published grid factors already
  include losses ("consumption-based") — using one of those in scope 2 *and*
  adding Cat 3(c) double counts. Check the factor's stated basis.
- **kWh vs MWh vs MMBtu vs GJ:** 1 MMBtu = 293.07 kWh; 1 GJ = 277.78 kWh.
- **Market vs location basis:** keep Category 3(b)/(c) basis consistent with
  the scope 2 method it accompanies, or disclose the difference.

## Data collection & gap-filling

1. **Reuse scope 1/2 activity data** — fuel purchase registers, utility
   invoices, meter data. Category 3 requires no new metering; it requires the
   same quantities re-multiplied by upstream factors. Build it as a derived
   calculation from the scope 1/2 dataset so the numbers can never diverge.
2. **Supplier-specific upgrades:** large gas/diesel buyers can request
   supplier upstream intensities (increasingly available under methane
   programs, e.g., certified gas); utilities can supply company-specific loss
   rates and fuel-mix data.
3. **Grid mapping:** map every meter to its eGRID subregion / national grid;
   pull the matching GGL or IEA loss rate. Keep the mapping with the scope 2
   workpapers.
4. **Gap-filling:** missing loss rate → IEA country value or world average,
   flagged; missing WTT factor for an exotic fuel → nearest DEFRA analog or
   GREET pathway, documented; missing months → same pro-rata extrapolation
   used in scopes 1/2 (`ghg-protocol` §8).

## QA checks

- **Ratio tests:** Cat 3(a) ≈ 20–30% of scope 1 stationary+mobile fossil
  emissions; Cat 3(c) ≈ scope 2 (location-based) × loss rate (≈5% US);
  Cat 3(b) ≈ 10–25% of scope 2 for fossil-heavy grids. Large deviations mean
  a factor-basis error.
- **Completeness:** every scope 1 fuel line and every scope 2 meter has a
  Category 3 counterpart (a reconciliation join, not a judgment call).
- **Double-count scan:** no WTW factors in scope 1/2; no consumption-basis
  grid factor combined with a separate loss line; utility reporters check
  losses aren't in both scope 2 and Cat 3.
- **Factor vintage alignment:** WTT tables, grid EFs, and loss rates from
  publication years matching the reporting year (or nearest available,
  disclosed).
- **GWP set** consistent with the rest of the inventory (`ghg-protocol` §4).

## Worked FAQ

**Q1. Scope 1 diesel is 1,255 t CO2e from 500,000 L. What's Category 3(a)?**
500,000 L × 0.61 kg CO2e/L (DEFRA 2024 WTT, diesel avg blend — verify) =
**305 t CO2e**. Sanity: 305/1,255 ≈ 24%, inside the expected 20–30% band.

**Q2. Scope 2 (location-based) is 4,100 t CO2e from 11.0 GWh in eGRID
subregion with EF 0.373 kg CO2e/kWh. T&D losses?**
11,000,000 kWh × 0.373 × 0.048/(1−0.048) = **207 t CO2e** (eGRID 2022 GGL
≈ 4.8% — verify subregion value). Roughly 5% of scope 2, as expected.

**Q3. We buy 100% renewable power via RECs. Is Category 3 zero?**
Not automatically. On the location basis, 3(b)/(c) follow the physical grid.
On a market basis you may reflect the contractual mix (wind/solar have small
but nonzero fuel-cycle emissions and losses still occur physically); the
common practice is location-based Category 3 with disclosure. State your
basis; don't silently zero it.

**Q4. Our German site used 2.4 GWh. Cat 3(c) with IEA data?**
2,400,000 kWh × ~0.35 kg CO2e/kWh (German grid, ~2023, illustrative — verify
UBA/IEA current) × ~0.055/(1−0.055) (IEA German loss rate ~5–6% — verify) ≈
**49 t CO2e**.

**Q5. Can I just apply DEFRA's WTW freight factor to my own trucks and skip
Category 3?**
No. Your own trucks' combustion is scope 1 (combustion factor) and their fuel
WTT is Category 3(a) (WTT factor) — two lines, two scopes. WTW factors are
for third-party transport in Categories 4/6/9.

**Q6. We're a gas utility: we buy and resell 50 million therms to customers.
Where does that go?**
Combustion by your customers is their scope 1 (and Category 11 for you as
sold-product use if you report it there per the Standard's fuel-sale
treatment); the *upstream* emissions of gas you resell are your Category 3(d)
analog for fuels (extraction/processing/transport of purchased fuels sold on).
Your own network compressor fuel and fugitives remain scope 1.

## References

- GHG Protocol Corporate Value Chain (Scope 3) Standard (2011) — ch. 5,
  Table 5.4 (Category 3 definition; the four activities; scope 1/2 exclusion).
- Technical Guidance for Calculating Scope 3 Emissions v1.0 (2013) —
  Category 3 chapter (methods and formulas per activity).
- DEFRA/DESNZ UK Government GHG Conversion Factors (annual): "WTT — fuels",
  "WTT — UK electricity", "T&D — UK electricity" tables.
- EPA eGRID (subregion output EFs and Grid Gross Loss, current release);
  EPA GHG Emission Factors Hub (packaging of the above).
- IEA World Energy Balances / Emission Factors (country T&D losses, grid
  factors); Argonne GREET model (US fuel-cycle pathways).
- Cross-cutting conventions: the `ghg-protocol` skill.
