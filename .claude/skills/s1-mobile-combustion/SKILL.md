---
name: s1-mobile-combustion
description: >-
  Scope 1 mobile combustion methodology. Use for questions about company cars,
  vans, trucks, fleet fuel (gasoline/petrol, diesel, CNG, LNG, LPG/autogas),
  fuel cards, corporate aircraft and jet fuel, owned vessels, forklifts and
  off-road equipment, biofuel blends (E10, E85, B20), fleet EVs and hybrids,
  distance-based vs fuel-based vehicle emission factors (EPA g/mile CH4-N2O,
  DEFRA kg CO2e/km), and fuel economy (mpg, L/100km) conversions.
---

# Scope 1 — Mobile Combustion

Mobile combustion is fuel burned in transportation devices owned or controlled
by the reporting company: on-road vehicles (cars, vans, trucks, buses),
off-road and non-road equipment (forklifts, agricultural and construction
machinery), locomotives, marine vessels, and aircraft. Gases: CO2 (fuel-carbon
driven, >97% of CO2e for road fleets), plus CH4 and N2O (combustion- and
after-treatment-technology driven). Governing documents: GHG Protocol
Corporate Standard (2004) ch. 4 & 6; GHG Protocol cross-sector tool
*"Calculating CO2 emissions from mobile sources"*; IPCC 2006 GL Vol. 2
(Energy) ch. 3 (Mobile Combustion); US EPA GHG Emission Factors Hub Tables
2–5; UK DESNZ/DEFRA conversion factors ("Fuels", "Passenger vehicles",
"Delivery vehicles" tabs). Cross-cutting conventions live in the
`ghg-protocol` skill.

## Boundary & classification

**In scope 1 (mobile):** combustion in vehicles/equipment inside the
organizational boundary — owned vehicles and, under the control approaches,
**leased vehicles the company operates** (typical for fleet leases where the
company directs use and buys the fuel).

Routing table — get this right before calculating:

| Situation | Belongs in | Notes |
|---|---|---|
| Company-owned or company-leased-and-operated vehicles | **Scope 1 here** | Under operational/financial control, an operating- or finance-leased fleet vehicle the company fuels and dispatches is scope 1. Under equity share/finance-lease nuances see Corporate Standard ch. 4 & `ghg-protocol` §2; leased vehicles excluded from scope 1 land in `s3-c08` |
| Employee-owned cars on business trips (mileage reimbursement, "grey fleet") | Scope 3 cat. 6 → `s3-c06-business-travel` | Ownership/control decides, not who pays for fuel |
| Employee commuting | Scope 3 cat. 7 → `s3-c07-employee-commuting` | |
| Third-party logistics (3PL), common carriers, contracted freight | Scope 3 cat. 4 (paid by reporter, upstream) or cat. 9 (downstream) → `s3-c04` / `s3-c09` | Never scope 1, even for dedicated contracted trucks the reporter does not operate |
| Rental cars for business travel | Scope 3 cat. 6 (short-term rental) | Long-term leases operated by the company → scope 1 under control approaches |
| Off-road equipment: forklifts, yard tractors, excavators, gensets on wheels | **Scope 1 here** (mobile) | Use EPA Hub Table 4 non-road factors / DEFRA fuels; a trailer-mounted generator parked long-term is functionally stationary — either classification is defensible; be consistent |
| Refrigerated transport (reefer/TRU diesel) | **Scope 1 here** for the TRU fuel combustion | Refrigerant leakage from the same unit → `s1-fugitive-emissions`. DEFRA "refrigerated" freight factors already bundle TRU fuel — don't double count |
| Fleet EV charging electricity | Scope 2 → `s2-purchased-electricity` | Zero scope 1 tailpipe. Home-charged company EVs paid by the company: still scope 2 if within boundary control, commonly estimated from reimbursement kWh |
| Plug-in hybrids (PHEV) | Split | Liquid fuel → scope 1 here; charging kWh → scope 2 |
| Biofuel share of blends (E10, B20, HVO, SAF) | Biogenic CO2 **outside the scopes**; CH4/N2O stay in scope 1 | `ghg-protocol` §5 |
| Well-to-tank (upstream fuel production & delivery) | Scope 3 cat. 3 → `s3-c03-fuel-energy-related` | DEFRA publishes separate WTT tables — never add WTT factors to scope 1 |
| Lubricants, urea/DEF (AdBlue) | Minor; urea CO2 is technically scope 1 process-type CO2 | Usually de minimis; document if excluded |

## Method ladder

| # | Method | Data needed | Typical use |
|---|---|---|---|
| 1 | Fuel quantity by fuel type × fuel EF | Fuel card exports, bulk purchase records, on-site tank logs | **Preferred** — CO2 is fuel-based by nature |
| 2 | Distance × vehicle fuel economy → derived fuel → fuel EF | Odometer/telematics km + fleet fuel-economy data | Fuel data absent, distance solid |
| 3 | Distance × distance-based EF by vehicle type | Distance only | DEFRA per-km factors; EPA per-mile CH4/N2O always uses this |
| 4 | Fuel spend ÷ average price → liters/gallons | Fuel spend from GL/expense system | Gap-filling |
| 5 | Vehicle count × average annual mileage assumption | Fleet register only | Screening; last resort |

**Structural note on CH4/N2O:** in the **US EPA methodology**, CO2 is
fuel-based (kg/gal) but CH4/N2O for on-road vehicles are **distance- and
vehicle-technology-based** (g/mile by vehicle type and model year, EPA Hub
Table 3, alternative-fuel vehicles Table 5; non-road is g/gal, Table 4) —
because they depend on catalyst/after-treatment, not fuel carbon. In the
**DEFRA methodology**, everything is bundled into a single kg CO2e per liter
or per km factor. Don't mix: with EPA factors you need both fuel and distance
(or accept the small error of estimating distance from fuel); with DEFRA you
need only one basis.

### Method 1 — Fuel quantity × fuel EF (preferred)

**When:** fuel card exports, bulk fuel purchase records, or fleet fuel
accounting exist. Always prefer this for CO2 — it is exact w.r.t. carbon.

**Data:** annual liters/gallons by fuel type (and by vehicle class + model
year if using EPA CH4/N2O); blend composition (E10 vs E0, B20 share).

**EF sources:** EPA GHG Emission Factors Hub Table 2 (mobile CO2, kg/gal;
mirrors Part 98 Table C-1 densities/HHVs), Tables 3–5 (CH4/N2O); DEFRA
"Fuels" tab (kg CO2e/liter, blends pre-split with a separate "outside of
scopes" biogenic line); IPCC 2006 Vol. 2 ch. 3 Tables 3.2.1–3.2.2 (kg/TJ NCV)
for defaults elsewhere.

```
CO2 (kg)   = fuel volume × EF_CO2 (kg/gal or kg/L)                 [split blends first]
CH4 (kg)   = miles × EF_CH4 (g/mile) ÷ 1,000        (EPA, on-road)
N2O (kg)   = miles × EF_N2O (g/mile) ÷ 1,000        (EPA, on-road)
CO2e       = CO2 + CH4×GWP_CH4 + N2O×GWP_N2O
```

**Worked example** — US sales fleet: 40,000 US gal of E10 gasoline purchased;
telematics shows 900,000 miles; cars are gasoline passenger cars, recent
model years. EPA Hub 2025, AR5 GWPs (CH4 28, N2O 265):

```
Fossil gasoline share = 40,000 × 0.90 = 36,000 gal
CO2 (fossil)  = 36,000 gal × 8.78 kg CO2/gal        = 316,080 kg
Ethanol share = 40,000 × 0.10 = 4,000 gal
CO2 (biogenic)= 4,000 gal × 5.75 kg CO2/gal         = 23,000 kg  → outside of scopes
CH4  = 900,000 mi × ~0.005 g/mi = 4,500 g → 4.5 kg × 28  = 126 kg CO2e
N2O  = 900,000 mi × ~0.002 g/mi = 1,800 g → 1.8 kg × 265 = 477 kg CO2e
Scope 1 total ≈ 316,080 + 126 + 477 = 316,683 kg ≈ 316.7 t CO2e
Biogenic CO2  ≈ 23.0 t
```

(The ~0.005/~0.002 g/mi are illustrative of recent-model-year gasoline
passenger cars — look up the exact model-year row in EPA Hub Table 3; older
vehicles run several times higher.)

**Pitfalls:** fuel card exports mix personal-use fuel and non-fleet purchases
— filter by vehicle/card; "gasoline" at US pumps is almost always E10 — using
8.78 on the full volume overstates fossil CO2 ~3%; bulk tank deliveries need
inventory adjustment (see the stationary skill); don't apply DEFRA per-liter
CO2e factors *and* EPA per-mile CH4/N2O — double counting.

### Method 2 — Distance × fuel economy → derived fuel

**When:** reliable odometer/telematics distance but no fuel records (e.g.,
drivers fuel personally and expense it).

**Data:** annual distance per vehicle or class; fuel economy — actual fleet
mpg (best), manufacturer/EPA-rated adjusted for real-world (rated values
flatter reality by ~10–20%), or class averages.

```
Fuel (gal) = miles ÷ fuel economy (mi/gal)
Fuel (L)   = km × (L/100 km) ÷ 100
→ then Method 1 formulas
```

**Worked example** — 12 diesel delivery vans, telematics total 480,000 miles,
observed fleet average 16.0 mpg:

```
Fuel  = 480,000 ÷ 16.0 = 30,000 gal diesel
CO2   = 30,000 × 10.21 kg/gal                       = 306,300 kg
CH4/N2O: light-duty diesel trucks, per-mile (EPA Hub Table 3, model-year row);
  at ~0.001 g CH4/mi and ~0.0015 g N2O/mi (illustrative recent MY):
  CH4 0.48 kg × 28 ≈ 13 kg; N2O 0.72 kg × 265 ≈ 191 kg CO2e
Total ≈ 306,300 + 13 + 191 ≈ 306.5 t CO2e
```

**Pitfalls:** using rated (window-sticker/NEDC/WLTP) economy without a
real-world uplift understates fuel; mixing km with mpg (1 mi = 1.60934 km;
mpg = 235.215 ÷ (L/100 km)); imperial mpg ≠ US mpg (×1.201).

### Method 3 — Distance × distance-based EF by vehicle type

**When:** distance is the only activity data, or you report UK-style. This is
also how EPA CH4/N2O is always done (see Method 1).

**Data:** km or miles by vehicle type/size/fuel.

**EF sources:** DEFRA "Passenger vehicles" and "Delivery vehicles" tabs
(kg CO2e/km, all gases bundled — e.g., DEFRA 2024: average diesel car
≈0.170 kg CO2e/km, average petrol car ≈0.164 kg CO2e/km, average diesel van
(≤3.5 t) ≈0.24 kg CO2e/km, artic HGV average laden ≈0.86 kg CO2e/km — verify
the current-year workbook; factors shift with fleet-average composition every
year). US: EPA Hub Tables 3/5 for CH4/N2O only — EPA publishes no per-mile
CO2 factor for scope 1; derive CO2 via fuel economy (Method 2).

```
CO2e (kg) = distance (km) × EF (kg CO2e/km)        [DEFRA-style, bundled]
```

**Worked example** — UK-operated fleet: 120,000 km on average diesel cars
(company cars, fuel unknown quantity). DEFRA 2024 average diesel car
≈0.170 kg CO2e/km:

```
120,000 km × 0.170 kg CO2e/km = 20,400 kg ≈ 20.4 t CO2e (scope 1)
```

DEFRA also lists a WTT per-km companion factor (→ scope 3 cat. 3) and a
biogenic share line — keep them out of scope 1.

**Pitfalls:** "average car" factors assume UK fleet mix — poor fit for a
fleet of large SUVs or US vehicles; DEFRA per-km factors are for the vehicle,
not per passenger (per-passenger-km factors on the "Business travel" tab are
for scope 3 cat. 6, not here).

### Method 4 — Fuel spend ÷ average price

**When:** only financial data (GL fuel accounts, expense categories) exist.

```
Volume = spend ÷ average pump price (same country, fuel, and period)
→ then Method 1
```

Price sources: EIA weekly retail gasoline/diesel prices (US annual averages),
DESNZ/AA UK pump prices, national statistics elsewhere.

**Worked example** — $30,000 of gasoline spend, US, annual average retail
price $3.40/gal:

```
Volume = 30,000 ÷ 3.40 = 8,824 gal (treat as E10 → fossil 7,941 gal)
CO2    = 7,941 × 8.78 = 69,725 kg ≈ 69.7 t (+ biogenic 882 gal × 5.75 ≈ 5.1 t)
```

**Pitfalls:** spend includes taxes, car washes, snacks on fuel cards; prices
vary ±20% within a year — use the volume-weighted period average; convert
currency at period rates. Flag as estimated.

### Method 5 — Vehicle count × average annual mileage

**When:** screening only; you know the fleet register and nothing else.

```
Distance = vehicles × average annual km (national statistic for the class)
→ then Method 3 (or Method 2 → 1)
```

US reference: FHWA average ~11,500 mi/yr per light-duty vehicle; UK: ~7,000–
8,000 mi/yr average car (higher for company cars, ~15–20k km). **Worked
example** — 15 gasoline pickups, assume 15,000 mi/yr each, 17 mpg class
average: 225,000 mi ÷ 17 = 13,235 gal × 8.78 = 116,204 kg ≈ **116.2 t CO2**
(+ CH4/N2O per mile). Uncertainty easily ±40% — replace with real data for
material fleets.

### Special cases

- **Biofuel blends:** split by volume share (E10 = 10% ethanol, E85 ≈ 70–85%,
  B20 = 20% biodiesel, HVO = 100% biogenic CO2). Fossil share → scope 1 CO2;
  bio share × the bio-fuel CO2 factor (ethanol 5.75, biodiesel 9.45 kg
  CO2/gal, EPA Hub 2025) → biogenic memo line. CH4/N2O on the whole quantity.
  DEFRA "average biofuel blend" factors already net out the biogenic CO2 and
  give the biogenic amount separately.
- **CNG/LNG:** CNG 0.05444 kg CO2/scf (EPA Hub 2025); convert GGE if the fuel
  system reports gasoline-gallon-equivalents (1 GGE ≈ 125.7 scf, verify the
  program's definition). LNG 4.50 kg CO2/gal (EPA Hub 2025).
- **EV/hybrid:** battery-EV → no scope 1; charging → scope 2 (kWh from
  charge-point network exports or reimbursements). Non-plug-in hybrids: plain
  gasoline vehicles here (use their actual fuel). PHEV: fuel here, kWh scope
  2; if the utility/charging split is unknown, use the fleet telematics
  electric-mode share or the EPA utility factor for that model.
- **Refrigerants in mobile A/C and TRUs:** leakage → `s1-fugitive-emissions`;
  only the fuel is accounted here.

## Emission factors quick reference

Verify against the current-year publication — EPA Hub updates ~annually
(model-year rows extend each year); DEFRA republishes every June and its
fleet-average per-km factors move year to year.

| Item | Factor | Units | Source & vintage |
|---|---|---|---|
| Motor gasoline (CO2) | 8.78 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Diesel (CO2) | 10.21 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Ethanol E100 (biogenic CO2) | 5.75 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Biodiesel B100 (biogenic CO2) | 9.45 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| LPG/propane (CO2) | 5.72 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| CNG (CO2) | 0.05444 | kg CO2/scf | EPA Hub 2025, Table 2 |
| LNG (CO2) | 4.50 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Jet fuel / Jet A (CO2) | 9.75 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Aviation gasoline (CO2) | 8.31 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Residual fuel oil, marine (CO2) | 11.27 | kg CO2/US gal | EPA Hub 2025, Table 2 |
| Gasoline passenger car CH4/N2O | by model year, order 0.002–0.02 CH4 / 0.001–0.01 N2O | g/mile | EPA Hub 2025, Table 3 — look up the model-year row |
| Diesel heavy-duty CH4/N2O | model-year dependent (post-2007 after-treatment raises N2O) | g/mile | EPA Hub 2025, Table 3 |
| Non-road (forklifts, construction, aircraft, marine) CH4/N2O | per gallon by fuel/equipment | g/gal | EPA Hub 2025, Table 4 |
| Diesel, 100% mineral (UK) | ≈2.66 | kg CO2e/liter (CO2+CH4+N2O bundled) | DEFRA/DESNZ 2024, Fuels |
| Diesel, average biofuel blend (UK) | ≈2.51 | kg CO2e/liter | DEFRA/DESNZ 2024 |
| Petrol, 100% mineral (UK) | ≈2.34 | kg CO2e/liter | DEFRA/DESNZ 2024 |
| Petrol, average biofuel blend (UK) | ≈2.16 | kg CO2e/liter | DEFRA/DESNZ 2024 |
| Average diesel car (UK) | ≈0.170 | kg CO2e/km | DEFRA/DESNZ 2024, Passenger vehicles |
| Average petrol car (UK) | ≈0.164 | kg CO2e/km | DEFRA/DESNZ 2024 |
| Average diesel van ≤3.5 t (UK) | ≈0.24 | kg CO2e/km | DEFRA/DESNZ 2024, Delivery vehicles |
| Motor gasoline (IPCC) | 69,300 | kg CO2/TJ (NCV) | IPCC 2006 Vol. 2 Table 3.2.1 |
| Diesel/gas oil (IPCC) | 74,100 | kg CO2/TJ (NCV) | IPCC 2006 Vol. 2 Table 3.2.1 |

DEFRA per-liter and per-km factors bundle CH4/N2O into CO2e (do not add
more); EPA factors are per-gas (you add CH4/N2O and pick the GWP set —
state it per `ghg-protocol` §4).

## Unit and conversion traps

- **US vs imperial gallons:** 1 US gal = 3.78541 L; 1 imperial gal =
  4.54609 L. Applying EPA kg/US-gal factors to imperial-gallon (or liter)
  volumes without converting is a 20% (or 3.8×) error.
- **Miles vs km:** 1 mi = 1.60934 km. mpg(US) = 235.215 ÷ (L/100 km);
  mpg(imperial) = 1.201 × mpg(US).
- **HHV vs NCV:** EPA per-gallon CO2 factors are volume-based (no CV basis
  needed), but energy-basis work (IPCC kg/TJ) is NCV — gasoline/diesel NCV ≈
  GCV × 0.95 (~5%); see the stationary skill's trap list for the full rules.
- **LPG mass vs volume:** autogas sold per liter (≈0.51 kg/L propane) or per
  kg; EPA's 5.72 kg CO2/gal is per liquid US gallon.
- **CNG units:** scf vs Nm³ vs kg vs GGE/DGE — confirm the dispenser unit;
  1 kg CNG ≈ 48–52 scf depending on composition.
- **E10 nominal vs actual:** blend share is a volume %, not energy % —
  splitting by volume is the standard convention (EPA/DEFRA both).
- **Distance double counting:** telematics "engine-on" distance vs billed
  reimbursement miles can overlap for the same vehicles — pick one source
  per vehicle.

## Data collection & gap-filling

Request:
- **Fuel card exports** (WEX, Comdata, Shell/BP fleet cards): liters/gallons
  by fuel grade, vehicle/card ID, date — the single best dataset.
- **Bulk fuel purchases** and on-site tank logs for depots (with start/end
  inventory); allocation between mobile and stationary users of the tank.
- **Telematics/AVL exports** (odometer, distance, idle hours) for Methods
  2–3 and for the EPA CH4/N2O distance basis.
- **Fleet register:** vehicle count, class, fuel type, model year (needed for
  EPA Table 3 rows), lease vs owned status.
- **Aviation/marine:** fuel uplift records from FBOs/bunkering, flight logs.
- **EV charging:** charge-point network kWh exports, reimbursement records.

Gap-filling: missing months → daily-average of adjacent months (road fleets
are less seasonal than heating; adjust for known seasonality e.g. agricultural
equipment); vehicles missing from fuel data but present in the register →
Method 5 with class averages, flagged. Keep the fuel-liters ↔ distance
cross-check wherever both exist: implied economy should sit near the class
norm.

## QA checks

- **Implied fuel economy:** total distance ÷ total fuel per class; flag cars
  outside ~15–60 mpg (4–16 L/100 km), heavy trucks outside ~4–9 mpg.
- **Year-over-year variance:** >±15% per class without fleet-size or activity
  change → investigate.
- **Unit red flags:** off by ~1,000× (kg vs t, mL vs L), ~3.8× (liters at a
  per-gallon factor), ~1.2× (imperial vs US gallons; imperial vs US mpg),
  ~1.6× (miles/km swap). A per-vehicle result above ~25 t CO2e/yr for a
  passenger car or below ~1 t for a full-time vehicle is suspect.
- **CH4/N2O share:** should be ≲1–2% of fleet CO2e (modern road vehicles);
  more suggests a g/kg slip or wrong table row.
- **Completeness:** reconcile against the fleet register and insurance
  schedule; every registered vehicle needs fuel data, an estimate, or a
  documented disposal date. Check biogenic line exists if any E10/B20/HVO
  was consumed.
- **Boundary check:** no 3PL, grey-fleet, or rental fuel in scope 1 totals.

## Worked FAQ

**Q1. Fleet bought 22,000 gal of diesel (B20 in summer months: 6,000 of the
22,000 gal). Scope 1?**
Fossil diesel = 16,000 + 6,000 × 0.80 = 20,800 gal × 10.21 = 212,368 kg.
Biogenic = 6,000 × 0.20 = 1,200 gal × 9.45 = 11,340 kg biogenic CO2 (outside
scopes). CH4/N2O per mile from EPA Hub Table 3 using fleet distance (if
distance unknown, derive from fuel ÷ class mpg and label the assumption).
**Scope 1 ≈ 212.4 t CO2 + small CH4/N2O; biogenic ≈ 11.3 t.** (EPA Hub 2025.)

**Q2. Corporate jet uplifted 20,000 gal Jet A. Emissions?**
CO2 = 20,000 × 9.75 = 195,000 kg = **195 t CO2** (EPA Hub 2025 Table 2).
CH4/N2O per gallon from Hub Table 4 (aircraft row) add well under 1%. All
scope 1 if the aircraft is owned/operated; a chartered aircraft is scope 3
cat. 6. WTT of the fuel → cat. 3.

**Q3. Our UK company cars drove 300,000 km but we only know 60% are diesel,
40% petrol.**
Diesel: 180,000 km × ≈0.170 = 30,600 kg. Petrol: 120,000 km × ≈0.164 =
19,680 kg. **Total ≈ 50.3 t CO2e** (DEFRA 2024 average-car per-km factors,
bundled gases; verify current-year workbook). Record the WTT companion
(→ cat. 3) separately.

**Q4. Warehouse runs 8 propane forklifts, 2,400 gal LPG/yr.**
Off-road mobile, scope 1: CO2 = 2,400 × 5.72 = 13,728 kg ≈ **13.7 t**. CH4/N2O
per gallon from EPA Hub Table 4 (LPG non-road row) — order tens of kg CO2e.
The forklifts' fuel is mobile combustion even though they never leave the
site.

**Q5. We leased 10 EVs and 5 PHEVs. What goes where?**
EVs: no scope 1; charging kWh → scope 2 (`s2-purchased-electricity`),
including reimbursed home charging if within your boundary policy. PHEVs:
gasoline purchases → scope 1 here (Method 1); charging kWh → scope 2. If the
gasoline/electric split is unknown, telematics electric-mode share is the
best allocator. Vehicle manufacturing/leasing overheads → scope 3 (cat. 2/8).

**Q6. Only fuel spend exists: $54,400 diesel across US depots.**
At the EIA annual average retail diesel price (say $3.85/gal for the year —
use the actual figure): 54,400 ÷ 3.85 = 14,130 gal × 10.21 = 144,270 kg ≈
**144.3 t CO2**, flagged as spend-derived (Method 4). Note US pump diesel may
contain up to 5% biodiesel (B5) without labeling — a ≤1–5% conservatism;
refine with fuel-card volume data next cycle.

## References

- GHG Protocol Corporate Standard (rev. 2004), ch. 4 (leased assets,
  boundaries), ch. 6.
- GHG Protocol cross-sector tool: *Calculating CO2 emissions from mobile
  sources* (worksheet + guidance), ghgprotocol.org/calculation-tools.
- IPCC 2006 Guidelines, Vol. 2 (Energy), ch. 3 (Mobile Combustion), Tables
  3.2.1–3.2.2 (road), 3.3–3.6 (off-road, rail, water, air).
- US EPA GHG Emission Factors Hub (annual): Table 2 (mobile CO2), Table 3
  (on-road CH4/N2O g/mile by vehicle type & model year), Table 4 (non-road
  g/gal), Table 5 (alternative-fuel vehicles).
- 40 CFR Part 98 Table C-1 (fuel heat contents/densities behind Table 2).
- UK DESNZ/DEFRA GHG Conversion Factors (annual): Fuels, Passenger vehicles,
  Delivery vehicles, WTT tabs; methodology paper for fleet-average
  derivations.
- EIA retail fuel price series; FHWA VM-1 (average annual mileage).
- Cross-cutting conventions: the `ghg-protocol` skill (§2 boundaries, §4
  GWPs, §5 biogenic, §7 EF hierarchy).
