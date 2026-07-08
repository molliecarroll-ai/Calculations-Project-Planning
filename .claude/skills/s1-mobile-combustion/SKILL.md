---
name: s1-mobile-combustion
description: >-
  Scope 1 mobile combustion methodology. Use for questions about company cars,
  vans, trucks, fleet fuel (gasoline/petrol, diesel, CNG, LNG, LPG/autogas),
  fuel cards, corporate aircraft and jet fuel, owned vessels, forklifts and
  off-road equipment, biofuel blends (E10, E85, B20), fleet EVs and hybrids,
  distance-based vs fuel-based method selection and emission factor sources
  (EPA Hub mobile tables, DEFRA vehicle tables), and fuel economy
  (mpg, L/100km) conversions.
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

**Method walk-through** — US fleet on a biofuel blend (fuel volume +
telematics distance):

```
V_fossil     = V_fuel × (1 − blend share, by volume)    # E10 → × 0.90
CO2 (kg)     = V_fossil × EF_CO2(fossil fuel)           # EPA Hub Table 2,
                                                          kg/gal, current year
V_bio        = V_fuel × blend share
CO2_bio (kg) = V_bio × EF_CO2(biofuel: E100/B100 row)   # Hub Table 2
                                                          → biogenic memo line
CH4 (kg)     = miles × EF_CH4(vehicle type, model year) ÷ 1,000  # Hub Table 3
N2O (kg)     = miles × EF_N2O(vehicle type, model year) ÷ 1,000  # Hub Table 3
Scope 1 CO2e = CO2 + CH4 × GWP_CH4 + N2O × GWP_N2O
               # GWPs per the inventory's declared AR set
```

Look up the exact model-year row in Hub Table 3 — older vehicles run several
times higher on CH4/N2O than recent model years. For a modern road fleet the
CH4/N2O contribution is well under 1% of CO2e.

**Pitfalls:** fuel card exports mix personal-use fuel and non-fleet purchases
— filter by vehicle/card; "gasoline" at US pumps is almost always E10 — using
the fossil gasoline factor on the full volume overstates fossil CO2 ~3%; bulk
tank deliveries need inventory adjustment (see the stationary skill); don't
apply DEFRA per-liter CO2e factors *and* EPA per-mile CH4/N2O — double
counting.

### Method 2 — Distance × fuel economy → derived fuel

**When:** reliable odometer/telematics distance but no fuel records (e.g.,
drivers fuel personally and expense it).

**Data:** annual distance per vehicle or class; fuel economy — actual fleet
mpg (best), manufacturer/EPA-rated adjusted for real-world (rated values
flatter reality by ~10–20%), or class averages.

```
Fuel (gal) = miles ÷ fuel economy (mi/gal)
Fuel (L)   = km × (L/100 km) ÷ 100
→ then Method 1: CO2 from the Hub Table 2 per-gallon factor;
  CH4/N2O per mile from Hub Table 3 using the same distance
```

**Pitfalls:** using rated (window-sticker/NEDC/WLTP) economy without a
real-world uplift understates fuel; mixing km with mpg (1 mi = 1.60934 km;
mpg = 235.215 ÷ (L/100 km)); imperial mpg ≠ US mpg (×1.201).

### Method 3 — Distance × distance-based EF by vehicle type

**When:** distance is the only activity data, or you report UK-style. This is
also how EPA CH4/N2O is always done (see Method 1).

**Data:** km or miles by vehicle type/size/fuel.

**EF sources:** DEFRA "Passenger vehicles" and "Delivery vehicles" tabs
(kg CO2e/km by vehicle type, size, and fuel, all gases bundled; the
fleet-average per-km factors shift with UK fleet composition every year —
always use the current-year workbook). US: EPA Hub Tables 3/5 for CH4/N2O
only — EPA publishes no per-mile CO2 factor for scope 1; derive CO2 via fuel
economy (Method 2).

```
CO2e (kg) = Σ_vehicle_class [ distance (km) × EF(class, size, fuel) ]
            # DEFRA current-year tab, kg CO2e/km, bundled gases
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
Volume = spend ÷ volume-weighted average pump price
         (same country, fuel, and period)
→ then Method 1 (treat US pump gasoline as E10 and split the blend)
```

Price sources: EIA weekly retail gasoline/diesel prices (US annual averages),
DESNZ/AA UK pump prices, national statistics elsewhere.

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
8,000 mi/yr average car (higher for company cars, ~15–20k km). Derive fuel via
class-average economy, then apply Method 1 factors. Uncertainty easily ±40% —
replace with real data for material fleets.

### Special cases

- **Biofuel blends:** split by volume share (E10 = 10% ethanol, E85 ≈ 70–85%,
  B20 = 20% biodiesel, HVO = 100% biogenic CO2). Fossil share × the fossil
  fuel factor → scope 1 CO2; bio share × the biofuel CO2 factor (EPA Hub
  Table 2 carries ethanol E100 and biodiesel B100 rows) → biogenic memo line.
  CH4/N2O on the whole quantity. DEFRA "average biofuel blend" factors
  already net out the biogenic CO2 and give the biogenic amount separately.
- **CNG/LNG:** CNG CO2 factors are per scf (EPA Hub Table 2); convert GGE if
  the fuel system reports gasoline-gallon-equivalents (1 GGE ≈ 125.7 scf —
  verify the program's definition). LNG is per liquid US gallon (Hub Table 2).
- **EV/hybrid:** battery-EV → no scope 1; charging → scope 2 (kWh from
  charge-point network exports or reimbursements). Non-plug-in hybrids: plain
  gasoline vehicles here (use their actual fuel). PHEV: fuel here, kWh scope
  2; if the utility/charging split is unknown, use the fleet telematics
  electric-mode share or the EPA utility factor for that model.
- **Refrigerants in mobile A/C and TRUs:** leakage → `s1-fugitive-emissions`;
  only the fuel is accounted here.

## Emission factor sources

| Source | Governing table(s) | Coverage | Basis / units convention | Update cadence |
|---|---|---|---|---|
| EPA GHG Emission Factors Hub | Table 2 (Mobile Combustion CO2) | CO2 for gasoline, diesel, ethanol (biogenic), biodiesel (biogenic), LPG, CNG, LNG, jet fuel, aviation gasoline, marine residual fuel | Fuel-volume basis (kg CO2 per US gal; CNG per scf); per-gas — add CH4/N2O and pick the GWP set yourself | Annual |
| EPA GHG Emission Factors Hub | Table 3 (on-road CH4/N2O); Table 5 (alternative-fuel vehicles) | CH4 and N2O by vehicle type and model year (after-treatment technology dependent) | Distance basis (g/mile); model-year rows extend each year | Annual |
| EPA GHG Emission Factors Hub | Table 4 (non-road CH4/N2O) | Forklifts, construction/agricultural equipment, locomotives, marine, aircraft | Fuel basis (g/gal by fuel and equipment type) | Annual |
| 40 CFR Part 98 | Table C-1 | Fuel heat contents/densities behind Hub Table 2 | HHV; per-gas | Amended by rulemaking |
| UK DESNZ/DEFRA GHG Conversion Factors | "Fuels" tab | Per-liter kg CO2e for mineral and average-biofuel-blend road fuels, with separate biogenic ("outside of scopes") lines | **CO2e pre-bundled** (CO2+CH4+N2O) — do not add per-gas factors on top | Annual (June) |
| UK DESNZ/DEFRA GHG Conversion Factors | "Passenger vehicles", "Delivery vehicles" tabs | kg CO2e/km by vehicle type, size, and fuel (UK fleet-average); WTT companions on separate tabs | Distance basis; CO2e pre-bundled; fleet-average values move year to year | Annual (June) |
| IPCC 2006 GL Vol. 2 ch. 3 | Tables 3.2.1–3.2.2 (road); 3.3–3.6 (off-road, rail, water, air) | Default factors for the rest of the world | Energy basis (kg per TJ, **NCV**); per-gas | Static (2006); check the 2019 Refinement |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

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
  kg; the EPA LPG factor is per liquid US gallon.
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

## FAQ

**Q1. Fleet bought 22,000 gal of diesel, of which 6,000 gal was B20 in summer
months. How is it booked?**
Split the B20 gallons 80/20 by volume, then total the fossil diesel
(straight diesel + the 80% share) and apply the current-year Hub Table 2
diesel CO2 factor → scope 1. The 20% biodiesel share × the Hub Table 2 B100
factor → biogenic CO2, outside the scopes. CH4/N2O come per mile from Hub
Table 3 using fleet distance — if distance is unknown, derive it from fuel ÷
class mpg and label the assumption.

**Q2. Corporate jet uplifted 20,000 gal Jet A. How is it treated?**
Scope 1 if the aircraft is owned/operated; a chartered aircraft is scope 3
cat. 6, and WTT of the fuel is cat. 3. CO2 = gallons uplifted × the Hub
Table 2 Jet A factor; CH4/N2O per gallon from Hub Table 4 (aircraft row) add
well under 1% of the total.

**Q3. Our UK company cars drove 300,000 km but we only know 60% are diesel,
40% petrol.**
Method 3: apportion the distance by the fuel split and apply the current-year
DEFRA "Passenger vehicles" average diesel-car and average petrol-car per-km
CO2e factors to each share (bundled gases — add nothing on top). Verify the
workbook year, since fleet-average per-km factors move annually. Record the
WTT per-km companion (→ cat. 3) separately.

**Q4. Warehouse runs 8 propane forklifts, 2,400 gal LPG/yr.**
Off-road mobile combustion, scope 1 — even though the forklifts never leave
the site. CO2 = gallons × the Hub Table 2 LPG factor; CH4/N2O per gallon from
Hub Table 4 (LPG non-road row), a small addition. Confirm whether the
"gallons" are liquid volume (they should be — see the LPG unit trap).

**Q5. We leased 10 EVs and 5 PHEVs. What goes where?**
EVs: no scope 1; charging kWh → scope 2 (`s2-purchased-electricity`),
including reimbursed home charging if within your boundary policy. PHEVs:
gasoline purchases → scope 1 here (Method 1); charging kWh → scope 2. If the
gasoline/electric split is unknown, telematics electric-mode share is the
best allocator. Vehicle manufacturing/leasing overheads → scope 3 (cat. 2/8).

**Q6. Only fuel spend exists: $54,400 diesel across US depots.**
Method 4: divide by the EIA annual average retail diesel price for the year
and region, then apply the Hub Table 2 diesel factor to the derived gallons;
flag as spend-derived. Note US pump diesel may contain up to 5% biodiesel
(B5) without labeling — a small conservatism; refine with fuel-card volume
data next cycle.

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
