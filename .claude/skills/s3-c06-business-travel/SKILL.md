---
name: s3-c06-business-travel
description: >-
  Scope 3 Category 6 (Business Travel) methodology assistant. Use for questions
  about flights and air travel emissions, radiative forcing multipliers, cabin
  class and distance-band factors, rail, taxi and rideshare, rental cars,
  personal-car mileage reimbursement, hotel stays, and travel agency (TMC)
  booking data. Covers distance-based, fuel-based, and spend-based methods,
  emission factor source selection (DEFRA/DESNZ, EPA Hub), and great-circle
  distance uplift conventions.
---

# Scope 3 Category 6 — Business Travel

**Definition (Scope 3 Standard, ch. 5, table 5.4):** Emissions from the
transportation of employees for business-related activities in vehicles **not
owned or operated** by the reporting company — aircraft, trains, buses,
taxis/rideshare, rental cars, and employees' own cars used on business —
during the reporting year.

**Governing documents:** Scope 3 Standard (2011), category 6; Technical
Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 6 chapter.
Cross-cutting conventions (GWP set, EF hierarchy, method-ladder rules,
answering style) are in the `ghg-protocol` skill.

## Boundary & classification

**In scope (minimum boundary):** scope 1 and 2 emissions of the transport
carriers (i.e., the fuel burn and electricity of the planes, trains, and
vehicles), allocated to the reporter's travelers:
- Commercial **air travel** (typically the dominant line, often >70–90% of the
  category for professional-services firms).
- **Rail**, intercity bus/coach.
- **Taxi and rideshare** journeys.
- **Rental cars** on business.
- **Employee-owned cars used for business** — the mileage-reimbursement
  population. This belongs in category 6 (business use), not category 7.

**Optional additions (disclose if included):**
- **Hotel stays** on business trips (the Guidance names them an optional part
  of category 6; widely included; DEFRA publishes per-room-night country
  factors).
- Well-to-tank (WTT) fuel-cycle emissions of travel fuels — if included,
  say so; note that upstream fuel emissions of your value-chain transport are
  not automatically category 3 (category 3 covers fuels the *reporter* buys).

**Out of scope / routing:**
- **Company-owned or -leased aircraft and vehicles** operated by the reporter
  → **scope 1** (fuel) / scope 2 (EV charging at own sites), not category 6.
- **Employee commuting** home↔work → category 7 (see `s3-c07-employee-commuting`).
  A trip from home directly to a client site is judgment territory: common
  practice books it as business travel when it replaces or exceeds the normal
  commute; document the rule.
- Travel by **non-employees** (candidates, contractors, board members):
  the Standard keys category 6 to employees; grey-zone travelers may be
  included optionally or under category 1 (purchased services) — pick one
  treatment and disclose.
- Employee air miles paid personally and not reimbursed: out.

### Aviation specifics: RF, distance bands, cabin class, GCD uplift

- **Radiative forcing (RF) / non-CO2 effects.** Aviation's contrails, NOx, and
  water vapor add warming beyond CO2. The GHG Protocol does not require an
  RF multiplier; it is an **optional** adjustment. Common practice: apply
  DEFRA's "with RF" air factors (multiplier ≈ **1.9** on the CO2 component,
  DESNZ methodology) or report without RF. **Whichever you choose, disclose
  it and keep it consistent across years** — a silent switch moves air
  emissions by nearly a factor of two. Some frameworks (e.g., UK SECR
  guidance) expect with-RF.
- **Distance bands** (DEFRA convention): domestic (within UK, used generically
  for short domestic hops), short-haul international (<~3,700 km), long-haul
  international (≥~3,700 km). Per-pkm factors differ because
  takeoff/landing fuel is amortized over different distances — domestic per-km
  factors are the *highest*.
- **Cabin class**: premium cabins occupy more floor area per seat, so
  per-pkm factors scale up by class — premium economy modestly above economy,
  business roughly 2–4× economy, first the highest (DEFRA derives the class
  ratios from seat-area allocation; pull current ratios from the DEFRA
  methodology paper). A business-class-heavy travel program can double its
  air footprint versus an all-economy assumption.
- **Great-circle distance (GCD) + uplift**: distances computed from
  origin-destination (O-D) airport pairs via GCD understate actual track flown
  (routing, holding, stacking). Apply an uplift of **~8–9%** (DEFRA
  methodology uses 8%; ICAO-based approaches similar) unless your factor set's
  methodology already embeds it — DEFRA's published per-pkm factors assume you
  apply the uplift to GCD yourself. Check and document.

## Method ladder

Scope 3 Calculation Guidance, category 6, names three methods:

| Tier | Method | Data needed | Typical use |
|---|---|---|---|
| 1 | Fuel-based | Litres/kg of fuel consumed by carriers, allocated to your travelers | Rare (charters, dedicated shuttles) |
| 2 | Distance-based | passenger-km (or vehicle-km) by mode/class × mode factor | The standard method; TMC booking data |
| 3 | Spend-based | Travel spend by mode × EEIO or $-based factor | Screening; expense-only visibility |

Hybrid is normal: distance-based for TMC-booked air/rail + spend- or
distance-based for out-of-channel ground travel. Disclose the split
(`ghg-protocol` §3).

### Method 1 — Fuel-based

**When:** chartered aircraft/vessels or a supplier reports actual fuel for
your trips.

```
CO2e = Σ  fuel [litres] × fuel EF [kgCO2e/litre] / 1000        (whole vehicle)
allocate to reporter: × (your passengers ÷ total passengers)    if shared
```

Fuel EFs come from the standard fuel-combustion tables (EPA GHG Emission
Factors Hub; DEFRA/DESNZ "Fuels" tab — per litre or per kg, updated
annually). **Pitfall:** a charter your company exclusively pays for but
does not operate is still category 6 (whole-flight fuel, no per-passenger
division); an *owned/operated* aircraft is scope 1.

### Method 2 — Distance-based (the standard)

```
CO2e_air  = Σ_legs  GCD [km] × (1 + uplift 0.08) × pax × EF_band,class [kgCO2e/pkm] / 1000
CO2e_rail = passenger-km × EF_rail / 1000
CO2e_car  = vehicle-km × EF_vehicle-km / 1000          (rental / reimbursed mileage)
CO2e_taxi = passenger-km × EF_taxi-pkm / 1000
CO2e_hotel = room-nights × EF_country [kgCO2e/night] / 1000
```

**Data:** TMC/agency booking exports (O-D airport pairs per leg, cabin class,
traveler count), rail booking data, rental-car contracts (km or fuel),
expense-system mileage claims (already in vehicle-distance units).

**EF sources:** DESNZ/DEFRA "Business travel — air / land / sea" and "Hotel
stay" tables (annual, kgCO2e/pkm with and without RF); US EPA GHG Emission
Factors Hub travel factors (per passenger-mile, no RF variant published);
national rail operators' disclosures for supplier-specific rail.

**Method walk-through — an air itinerary.**

1. Extract leg-level records from the TMC export: origin and destination
   airport per leg, cabin class, traveler count, ticket status.
2. Compute great-circle distance per leg from the O-D airport pair; apply
   the ~8% uplift: distance = GCD × 1.08 (skip if the distance engine
   already uplifts).
3. Convert to passenger-km: pkm = distance × travelers on the leg (each leg
   of a round trip counted separately; each traveler counted separately).
4. Select the factor: current-year DEFRA/DESNZ "Business travel — air"
   table, keyed by haul band (from leg distance) and cabin class, using the
   with-RF or without-RF variant per your disclosed convention.
5. CO2e = Σ_legs pkm × EF / 1000; label the RF basis on the result.

Mileage-reimbursement claims plug into the car line directly: claimed
distance is already vehicle-km (convert miles × 1.609 first) × a current-year
average-car factor (DEFRA "Business travel — land"; EPA Hub for US fleets for
geographic fit). Do not divide by occupancy.

**Pitfalls:** counting a round trip once; per-mile factors applied to km;
applying air pkm factors to *flights* rather than *passengers* (3 colleagues
on one flight = 3 × pkm); connecting itineraries — compute per leg, not
end-to-end O-D (a one-stop routing flies farther and may cross band
thresholds); missing class of service defaults — default to "average
passenger" or economy and disclose.

### Method 3 — Spend-based

```
CO2e = Σ_modes  spend [$] × EEIO factor_mode [kgCO2e/$] / 1000
```

Sources: USEEIO (air transportation, transit/ground, accommodation sectors),
EXIOBASE. **Pitfalls:** airfare prices vary ~5× for the same seat, so
spend-based air is very noisy; premium fares inflate spend-based estimates in
the same direction as their real emissions but not proportionally; currency
and inflation-year adjustment of the factor is mandatory. Use for screening
and the untracked tail only.

### TMC / agency data ingestion notes

- Request a **leg-level** extract: origin, destination, cabin class,
  ticket/refund status, traveler count, travel date. Exclude refunded/unused
  tickets; include exchanges once.
- Many TMCs deliver pre-computed CO2e — reconcile their methodology (RF
  on/off, uplift, factor vintage, GWP set) before mixing with your own
  numbers; recompute from O-D pairs if opaque.
- Capture **out-of-channel leakage**: compare TMC air spend to expense-system
  air spend; estimate untracked bookings spend-based or by ratio uplift, and
  disclose the gap-fill.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| UK DESNZ/DEFRA GHG Conversion Factors | "Business travel — air" | Air by haul band (domestic, short-haul intl, long-haul intl) and cabin class; with-RF and without-RF variants | kgCO2e per passenger-km | Annual |
| UK DESNZ/DEFRA GHG Conversion Factors | "Business travel — land" / "— sea" | Rail (national, underground, international), coach, taxi, ferries; cars by size/fuel incl. EVs | pkm for shared modes; vehicle-km for cars/taxis (check per row) | Annual |
| UK DESNZ/DEFRA GHG Conversion Factors | "Hotel stay" | Per-room-night factors by country of stay | kgCO2e per room-night | Annual |
| US EPA GHG Emission Factors Hub | Business travel tables | Air (short/medium/long haul), rail, vehicles; CO2, CH4, N2O published separately; no RF variant | per passenger-mile / vehicle-mile — convert units and GWP-weight gases per your inventory's GWP set | Annual |
| USEEIO / EXIOBASE | Air transportation, ground transit, accommodation sectors | Spend-based screening factors | kgCO2e per currency unit (inflation- and currency-adjust) | Model releases |
| National rail operators' disclosures | Operator sustainability reports | Supplier-specific rail | per passenger-km | Varies |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **passenger-km vs. vehicle-km**: air/rail/taxi factors are per *passenger*-km;
  car and rental factors are per *vehicle*-km. Mileage claims and rental odometer
  data are vehicle-km — never divide by an occupancy assumption; conversely
  never multiply air pkm by aircraft occupancy.
- **Miles vs. km**: US data arrives in miles (×1.609); EPA factors are
  per mile, DEFRA per km.
- **Round trip vs. one-way**: booking data is usually leg-level (safe);
  survey or itinerary summaries may be trip-level — confirm and double.
- **Short/long-haul thresholds** differ by factor set (DEFRA ~3,700 km;
  EPA short <300 mi, medium 300–2,300 mi, long >2,300 mi) — bucket with the
  thresholds of the factor set you use.
- **GCD uplift**: apply 8–9% once; don't double-apply if your distance
  engine already uplifts.
- **RF on/off**: label every air number; never sum with-RF and without-RF
  figures.
- Hotel factors are per **room**-night, not per guest-night — shared rooms
  count once.

## Data collection & gap-filling

- **TMC/agency exports** — primary air/rail source (leg-level O-D + class).
- **Expense system mining**: mileage-reimbursement claims (distance directly),
  taxi/rideshare spend (→ spend-based or ÷ $/km to distance), rental-car
  receipts — prefer **fuel purchases on rentals** (fuel-based) over rental-day
  proxies; else rental-days × avg km/day (document ~60–120 km/day assumption).
- **Rideshare providers** offer corporate-account CO2e or distance reports.
- **Hotel nights** from TMC hotel bookings + expense-claimed nights; by
  country of stay.
- **Gap-filling**: out-of-channel bookings via spend ratio; missing cabin
  class → economy or "average passenger" (disclose direction of bias);
  missing O-D → average trip distance by route type from the known population.
- Keep the evidence trail per `ghg-protocol` §8: extract dates, factor
  vintages, RF choice, uplift.

## QA checks

- **Per-FTE reasonableness**: business travel varies widely by industry —
  desk-based ~0.1–0.5 tCO2e/FTE/yr; consulting/sales-heavy 1–4+; >6 warrants
  a look for double-counted round trips or RF/no-RF mixing.
- **Air share**: air typically ≥70% of category 6 for flying organizations;
  a ground-dominated result usually signals missing TMC air data.
- **RF consistency across years**: confirm the same RF convention every year;
  a ~1.9× jump/drop in air emissions with flat travel volume is the classic
  symptom of a silent RF switch.
- **Class-mix check**: average kgCO2e/pkm across the air file should sit
  between economy and business factors consistent with your travel policy.
- **Refunds/exchanges**: emissions per ticket count should be stable YoY;
  spikes often mean unused tickets weren't excluded.

## Worked FAQ

**Q1. We have annual passenger-km totals by haul band and class from our
TMC — how do we turn them into emissions?**
Apply the current-year DEFRA/DESNZ "Business travel — air" factor for each
band × class combination, summing across bands. Compute with-RF and
without-RF totals in parallel from the two factor variants, report per your
disclosed RF convention, and label the basis on every air figure. If class
is missing, default to economy or "average passenger" and disclose the
default and its direction of bias.

**Q2. Should we apply the 1.9 RF multiplier?** Optional under the GHG
Protocol; not required, not prohibited. Decide once, apply to all air travel,
disclose, and hold constant across years (changing it later = document as a
methodology change; recalc base year if significant per `ghg-protocol` §6).
If reporting under UK SECR or to buyers who expect RF, include it.

**Q3. An employee drove her own car to client sites; we reimbursed
mileage. Where does it go and how is it calculated?** Category 6,
distance-based. Mileage claims are already vehicle-distance: convert miles
to km (× 1.609) if needed, apply a current-year average-car (or fuel/size-
specific, if known) factor from DEFRA "Business travel — land" — or the EPA
Hub passenger-car factor for US fleets for geographic fit — with no
occupancy division. Her daily commute stays in category 7.

**Q4. Our TMC covers 80% of air spend; expense data shows more booked
directly.** Compute the TMC population distance-based; gap-fill the
out-of-channel spend with a spend-based estimate (current USEEIO air-
transportation factor, currency- and inflation-adjusted). Report the
category as a hybrid, disclose the method split and the gap-fill share, and
flag the tail for TMC consolidation next year.

**Q5. How do we account for hotel stays?** Optional but widely included:
room-nights × the per-room-night factor for the **country of stay** from the
current DEFRA "Hotel stay" tab. Collect nights by country from TMC hotel
bookings plus expense claims; count shared rooms once. Country mix matters —
a small share of nights in high-factor-grid countries can dominate the hotel
line, so do not apply a single home-country factor to a global program.

**Q6. The CEO flies on the company-owned jet — category 6?** No. Owned (or
operated-leased) aircraft fuel is **scope 1**. Chartered flights on
third-party-operated aircraft are category 6, fuel-based if the operator
reports fuel, else distance-based with a charter/business-aviation factor.

## References

- Corporate Value Chain (Scope 3) Standard (2011), ch. 5, table 5.4 (category 6).
- Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 6 chapter (fuel-based, distance-based, spend-based methods).
- UK DESNZ/DEFRA GHG Conversion Factors (annual): "Business travel — air", "Business travel — land", "Hotel stay" tabs + methodology paper (RF multiplier, 8% GCD uplift, cabin-class ratios).
- US EPA GHG Emission Factors Hub (annual): business travel factors per passenger-mile.
- ICAO Carbon Emissions Calculator methodology (fuel-per-route basis, no RF).
- `ghg-protocol` skill — GWP sets, EF hierarchy, hybrid-method disclosure.
