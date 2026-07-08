---
name: s3-c07-employee-commuting
description: >-
  Scope 3 Category 7 (Employee Commuting) methodology assistant. Use for
  questions about commuting emissions, employee commute surveys, mode split and
  distance assumptions, telework / work from home / homeworking emissions and
  the DEFRA homeworking factor, public transit factors, working-days
  assumptions, and headcount-based average-data estimation. Also use for
  company shuttles, park-and-ride, and hybrid-work-pattern adjustments.
---

# Scope 3 Category 7 — Employee Commuting

**Definition (Scope 3 Standard, ch. 5, table 5.4):** Emissions from the
transportation of employees between their homes and their worksites in
vehicles **not owned or operated** by the reporting company, during the
reporting year. Teleworking (employees working remotely) is a named
**optional** addition.

**Governing documents:** Scope 3 Standard (2011), category 7; Technical
Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 7 chapter.
Cross-cutting conventions (GWP set, EF hierarchy, method rules, answering
style) live in the `ghg-protocol` skill.

## Boundary & classification

**In scope (minimum boundary):**
- Home↔work travel in employee-owned cars and motorcycles.
- Public transit commuting: bus, subway/metro, commuter rail, tram, ferry.
- Carpools/vanpools in non-company vehicles; rideshare commutes.
- Walking/cycling: zero direct emissions (include at 0; e-bike charging is
  de minimis — may be noted).

**Optional but recommended when material:**
- **Teleworking / homeworking**: incremental home energy (heating/cooling and
  office equipment) attributable to working from home. The Guidance predates
  mass hybrid work; post-2020 practice is to include it when remote FTE-days
  are material, using the **DEFRA homeworking factor** (per FTE working-hour,
  published annually in the conversion-factor set since 2020) or a bottom-up
  kWh model: (heating share + equipment kWh per FTE-day) × home-energy EFs.
  Disclose inclusion either way; a company
  that halves commuting via remote work but omits homeworking overstates the
  reduction.

**Out of scope / routing:**
- **Company-operated shuttles, buses, paratransit** → the vehicle fuel is
  **scope 1** if owned/operated by the reporter (scope 2 for electric charged
  on site); a *contracted* third-party shuttle service is category 7 (or
  optionally reported as purchased services — pick one, disclose).
- **Company cars used for commuting** → scope 1 (fuel card / owned vehicle),
  not category 7.
- Business travel, including home→client-site trips booked as business →
  category 6.
- Contractors' commuting: outside the employee boundary; optional to include
  for material on-site contractor populations (disclose).

## Method ladder

Scope 3 Calculation Guidance, category 7, names three methods; telework is an
add-on term under any of them:

| Tier | Method | Data needed | Typical use |
|---|---|---|---|
| 1 | Fuel-based | Fuel used for commuting (rare; fuel-card data on private cars) | Almost never |
| 2 | Distance-based (survey × extrapolation) | Employee survey: mode, one-way distance, days/week on-site; extrapolated to workforce | The standard for material c7 |
| 3 | Average-data | Headcount by site/country × national commuting statistics (avg distance, mode shares, working days) | No survey; screening |
| + | Telework add-on | Remote FTE-days × homeworking factor | Wherever remote work is material |

### Core formula (all distance-based variants)

```
CO2e = Σ_modes Σ_employees  one-way distance [km] × 2 × commuting days/yr × EF_mode [kgCO2e/pkm or /vkm] / 1000
```

- ×2 converts one-way to daily round trip.
- Car EFs are per **vehicle**-km: divide by carpool occupancy only when the
  survey establishes shared rides (single-occupancy default = 1).
- Transit EFs are per **passenger**-km: use directly.

### Method 2 — Employee survey × extrapolation (the standard)

**When:** commuting is material (large workforce, car-dependent geography).

**Survey design:** ask, per respondent — primary mode (and secondary for
multimodal), one-way distance (or home postcode → compute), days per week
on-site (hybrid patterns!), weeks worked, carpool occupancy, vehicle
fuel/size if car. Run annually or biennially; a statistically adequate sample
per site/region — as a rule of thumb aim for a margin of error ≤ ±10% at 95%
confidence (n ≈ 96 for large populations, more for stratification by site).
Avoid seasonal bias (a January survey overstates driving in snow markets);
ask about a "typical week" or survey mid-season.

**Minimum viable question set** (keep it under ~8 questions; response rate
falls with length):

1. Which site do you normally work at? (extrapolation stratum)
2. In a typical week, how many days are you on-site? (0–5+)
3. What is your usual **one-way** distance home→work? (or home postcode)
4. Primary mode for most of that distance? (drive alone / carpool / motorcycle /
   bus / rail-metro / cycle / walk / other)
5. If carpool: how many people usually share the vehicle (including you)?
6. If car: fuel type (petrol/gasoline, diesel, hybrid, plug-in hybrid, EV)?
7. Secondary mode, if your trip is multimodal (e.g., drive to station + rail)?
8. Weeks worked at this pattern this year (captures leave/part-year hires)?

**Extrapolation:**

```
CO2e = Σ_modes [ (Σ_respondents_m  d_oneway × 2 × days/yr) × EF_m / 1000 ] × (total FTE ÷ respondent FTE)
```

Extrapolate per site or region, not globally, when mode splits differ.
Non-response is assumed to mirror respondents — state this assumption; if
respondents skew (e.g., cyclists over-respond to green surveys), reweight or
flag.

**Method walk-through.**

1. Annualize each respondent: one-way distance × 2 × on-site days/yr,
   binned by mode (and by fuel type for cars, if asked).
2. Aggregate to mode totals in the correct unit basis — vehicle-km for
   cars/motorcycles (pooled riders collapsed into vehicles by reported
   occupancy), passenger-km for transit, zero for cycle/walk.
3. Apply current-year mode factors: DEFRA "Business travel — land" (car by
   size/fuel, local bus, rail, underground) or EPA Hub commuting factors for
   US populations; CO2e = Σ_modes activity × EF_mode / 1000.
4. Extrapolate the respondent subtotal to the stratum:
   × (total FTE ÷ respondent FTE), per site or region.
5. Sanity-check the implied tCO2e/FTE against the QA ranges below.

**Pitfalls:** respondents reporting round-trip distance when asked one-way
(pilot the question); hybrid workers answering pre-pandemic habits; applying
the site's mode split to a different geography; forgetting to remove leave
weeks.

### Method 3 — Average-data (headcount × national statistics)

**When:** no survey; small sites; screening.

```
CO2e = Σ_sites  headcount × Σ_modes [ share_m × avg one-way distance_m [km] × 2 × working days/yr × EF_m ] / 1000
```

**Statistics sources:** US — Census ACS commuting tables (mode share, mean
one-way travel time; NHTS for mean one-way distances); UK — Census
travel-to-work + National Travel Survey; EU national travel surveys.
**Working days**: ~250 weekdays − leave/holiday/sick ≈ **220–230 days/yr**
full-time on-site; multiply by average on-site fraction for hybrid policies
(e.g., 3 days/week policy → ×0.6). Document every parameter.

**Method walk-through.**

1. For each site, take headcount from HR and pull the geography's mode
   shares and mean one-way distance from the national statistics above.
2. Set annual commuting days: net working days × on-site fraction from the
   hybrid policy (or badge data).
3. Per mode: people_m = headcount × share_m; activity_m = people_m ×
   one-way distance × 2 × days. Convert carpool passengers to vehicles
   (÷ occupancy) before applying a vehicle-km car factor; leave transit in
   passenger-km.
4. Apply current-year mode factors (EPA Hub for US, DEFRA land tables for
   UK/EU) and sum; check the implied tCO2e/FTE against the QA ranges.

### Telework add-on

```
CO2e = remote FTE-days × hours/day × homeworking EF [kgCO2e/FTE-hour] / 1000
  or  = remote FTE-days × homeworking EF [kgCO2e/FTE-day] / 1000
```

The DEFRA/DESNZ homeworking factor (per FTE-hour; office equipment + a
share of home heating; built on UK grid/gas mix; published annually since
2020) is the standard published option — check geographic fit; for non-UK
populations, build bottom-up: equipment load [kWh/h] × hours × local grid EF
+ a heating increment in the heating season. **Walk-through:** remote
FTE-days = FTE × remote days/week × weeks worked; multiply by hours/day and
the current-year per-hour factor. **Pitfall:** applying the UK factor to
mild/electric-heat geographies without adjustment; double counting the
heating term for employees who would heat the home anyway — DEFRA's method
already takes an incremental view; state your basis.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| UK DESNZ/DEFRA GHG Conversion Factors | "Business travel — land" | Cars by size/fuel (incl. hybrid, PHEV, BEV), motorcycles, local bus, coach, national rail, underground, tram, taxi | kgCO2e per vehicle-km (cars/motorcycles) or passenger-km (transit) — check per row | Annual |
| UK DESNZ/DEFRA GHG Conversion Factors | "Homeworking" tab (2020 onward) | Incremental home-office energy (equipment + heating share), UK grid/gas basis | kgCO2e per FTE working-**hour** | Annual |
| US EPA GHG Emission Factors Hub | Commuting/travel tables | Passenger cars by fuel, transit bus, commuter rail; CO2, CH4, N2O published separately | per vehicle-mile / passenger-mile — convert units and GWP-weight per your inventory's GWP set | Annual |
| National transit operators / agencies | Sustainability disclosures | Supplier-specific transit intensities | per passenger-km | Varies |

Note on employee EVs: the employee's home charging is still category 7 for
the reporter (it is the employee's purchased electricity, not the reporter's
scope 2); use a per-km EV factor built on the local grid mix.

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **One-way vs. round trip**: the classic ×2 error, both directions — survey
  wording must pin this down.
- **Vehicle-km vs. passenger-km**: car factors per vehicle-km (divide pooled
  riders into vehicles); transit per passenger-km.
- **Working days**: 260 weekdays is wrong (ignores leave); 220–230 net
  on-site-eligible days is standard, then × on-site fraction for hybrid.
  Part-timers: use actual days, or FTE-weight.
- **FTE vs. headcount**: extrapolate on FTE for commuting *days*, headcount
  for *people-based* mode shares; be consistent — 2,000 headcount at 0.8
  average FTE commute ~20% fewer days than assumed.
- **Miles vs. km** in mixed US/UK datasets.
- Homeworking factor is per FTE-**hour** in DEFRA — multiply by hours/day
  before applying to days.

## Data collection & gap-filling

- **Commute survey** (annual or biennial; reuse of prior-year results is
  acceptable for up to ~2 years if workforce location and policy are stable —
  flag reuse and refresh after office moves or hybrid-policy changes).
- **HR data**: headcount/FTE by site and country (extrapolation denominator);
  remote-work policy and badge/occupancy data for on-site day rates.
- **Badge/occupancy systems**: actual on-site days beat policy assumptions.
- **Parking permits / transit-subsidy enrollment**: mode-split cross-checks.
- **Home + office postcodes**: compute distances directly (privacy: aggregate
  before storing) instead of self-reported distance.
- **Gap-fill** non-surveyed sites with the mode split of a like site in the
  same geography, national statistics otherwise; flag per `ghg-protocol` §8.

## QA checks

- **Per-FTE reasonableness**: ~**0.5–2 tCO2e/FTE/yr** for car-commuting
  markets; ~0.1–0.5 in transit-dense cities; >3 suggests round-trip double
  counting or a per-mile/per-km mix-up; <0.05 with a car-heavy workforce
  suggests missing extrapolation.
- **Survey response rate**: flag results below ~20–30% response or n<
  ~100/site; report response rate alongside the estimate.
- **Mode-split sanity** vs. national statistics for the geography (a 90%
  transit share in suburban Texas is a data error).
- **Hybrid consistency**: on-site days used in c7 should reconcile with
  telework FTE-days used in the homeworking add-on (they must sum to ~total
  working days).
- YoY movement should track headcount and policy changes, not survey noise —
  large swings after a survey refresh: disclose as method/data update.

## Worked FAQ

**Q1. Quick screen with no survey — what is the recipe?** Average-data:
headcount × national mode shares (ACS/NTS for the geography) × mean one-way
distance (NHTS/NTS) × 2 × hybrid-adjusted on-site days × current-year mode
factors, summed over modes. Document each parameter and its statistical
source, check the implied tCO2e/FTE against the QA ranges, and treat the
result as screening grade — survey if the category is material.

**Q2. We moved to 3 days/week in office. How do we adjust last year's
survey-based figure?** Scale commuting days: prior on-site fraction (say
100%) → 0.6, so commuting term × 0.6; add a telework term for the 2
days/week: FTE × 2 days × weeks worked × hours/day × the current homeworking
factor. Disclose as an activity change (no base-year recalc — real-world
change, `ghg-protocol` §6).

**Q3. Is telework mandatory to report?** No — optional under the Scope 3
Standard/Guidance. But if remote days are a large share of working time,
omitting it while claiming commuting reductions is misleading; include it or
justify exclusion. Cite the DEFRA homeworking factor and vintage when used.

**Q4. How is a 3-person carpool counted?** As one vehicle: annual vehicle-km
= one-way distance × 2 × on-site days for the shared vehicle, × the car
factor, then attributed across the three riders (÷ occupancy) if reporting
per person. Booking each rider at full vehicle-km would triple-count — this
is why the survey asks for carpool occupancy.

**Q5. Our company runs its own employee shuttle buses.** The shuttles' diesel
is **scope 1** (owned/operated), not category 7. Employees' travel from home
to the shuttle stop in their own cars remains category 7. A contracted
third-party shuttle would instead sit in category 7.

**Q6. How do we handle a multimodal commuter (drive to station, then
rail)?** Compute each segment with its own distance and its own mode factor
— car segment in vehicle-km, rail segment in passenger-km. Collapsing the
whole trip to "rail" materially understates (the car leg is far more
intensive per km); collapsing to "car" materially overstates. This is why
the survey asks for a secondary mode and per-segment distances.

**Q7. Survey response was 12% — can we still use it?** Use with caution:
extrapolate but flag the response rate, compare mode split against national
statistics for the geography, and consider blending with average-data. Plan
incentives to lift response next cycle; assurance providers routinely
question sub-20% commute surveys.

## References

- Corporate Value Chain (Scope 3) Standard (2011), ch. 5, table 5.4 (category 7; telework optional).
- Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 7 chapter (fuel-based, distance-based, average-data methods).
- UK DESNZ/DEFRA GHG Conversion Factors (annual): "Business travel — land" (modal factors), "Homeworking" tab (2020 onward) + methodology paper.
- US EPA GHG Emission Factors Hub (annual): commuting factors per vehicle-mile / passenger-mile.
- US Census ACS "Commuting Characteristics"; FHWA National Household Travel Survey (NHTS); UK National Travel Survey — mode shares and distances.
- EcoAct/Lloyds/Bulb "Homeworking emissions whitepaper" (2020) — basis of the DEFRA homeworking approach.
- `ghg-protocol` skill — GWP sets, EF hierarchy, gap-filling and data-quality rules.
