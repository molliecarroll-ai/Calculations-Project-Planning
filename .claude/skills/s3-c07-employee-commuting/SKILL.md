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
  are material, using the **DEFRA homeworking factor** (first published in the
  2020 conversion-factor set; ~0.33 kgCO2e per FTE working-hour in the 2024
  vintage — verify current) or a bottom-up kWh model: (heating share + equipment
  kWh per FTE-day) × home-energy EFs. Disclose inclusion either way; a company
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

**Extrapolation:**

```
CO2e = Σ_modes [ (Σ_respondents_m  d_oneway × 2 × days/yr) × EF_m / 1000 ] × (total FTE ÷ respondent FTE)
```

Extrapolate per site or region, not globally, when mode splits differ.
Non-response is assumed to mirror respondents — state this assumption; if
respondents skew (e.g., cyclists over-respond to green surveys), reweight or
flag.

**Worked example.** Site with 1,000 FTE; 400 respond. Respondent totals
(annualized, one-way distance × 2 × on-site days):

```
Car (avg 1.1 occupancy):  2,900,000 vehicle-km
Bus:                        310,000 passenger-km
Rail/metro:                 640,000 passenger-km
Cycle/walk:                 180,000 km (EF = 0)

Car:  2,900,000 vkm × 0.168 kgCO2e/vkm (DESNZ 2024 average car; verify) = 487.2 tCO2e
Bus:    310,000 pkm × 0.102 kgCO2e/pkm (DESNZ 2024 local bus; verify)   =  31.6 tCO2e
Rail:   640,000 pkm × 0.035 kgCO2e/pkm (DESNZ 2024 national rail)       =  22.4 tCO2e
Respondent subtotal = 541.2 tCO2e
Extrapolate: 541.2 × (1,000 ÷ 400) = 1,353 tCO2e
Per-FTE check: 1.35 tCO2e/FTE — plausible for a car-heavy suburban site.
```

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
one-way travel time; NHTS for distances, ~mean one-way commute ≈ 19–20 km);
UK — Census travel-to-work + National Travel Survey; EU national travel
surveys. **Working days**: ~250 weekdays − leave/holiday/sick ≈ **220–230
days/yr** full-time on-site; multiply by average on-site fraction for hybrid
policies (e.g., 3 days/week policy → ×0.6). Document every parameter.

**Worked example.** 500-FTE US office, no survey. Assume (ACS/NHTS-informed;
verify locally): 76% drive alone, 9% carpool (occ 2.2), 5% transit, 10%
remote-heavy/walk. One-way 19 km; 225 potential days × 60% on-site (hybrid) =
135 days.

```
Drive-alone: 500×0.76=380 × 19×2×135 = 1,949,400 vkm × 0.335 kgCO2e/vmi→per-km:
  use EPA passenger-car ≈ 0.21 kgCO2e/km (EPA Hub 2024, gasoline car; verify)
  = 409.4 tCO2e
Carpool: 45 × 19×2×135 = 230,850 vkm ÷ 2.2 occ… (carpool: count vehicle-km once:
  45 pax ÷ 2.2 = 20.5 vehicles × 5,130 km = 105,165 vkm × 0.21 = 22.1 tCO2e)
Transit: 25 × 19×2×135 = 128,250 pkm × 0.10 (bus mix; verify) = 12.8 tCO2e
Total ≈ 444 tCO2e  → 0.89 tCO2e/FTE (plausible US suburban)
```

### Telework add-on

```
CO2e = remote FTE-days × hours/day × homeworking EF [kgCO2e/FTE-hour] / 1000
  or  = remote FTE-days × homeworking EF [kgCO2e/FTE-day] / 1000
```

DESNZ 2024 homeworking factor ≈ **0.33 kgCO2e/FTE-hour** (office equipment +
share of home heating; UK grid/gas mix; first vintage 2020; verify current
and geographic fit — for non-UK, build bottom-up: equipment ~0.15 kWh/h ×
local grid EF + heating increment in heating season). **Worked example:**
1,000 FTE × 2 remote days/week × 46 weeks = 92,000 FTE-days × 8 h × 0.33
kgCO2e/h = 242,880 kgCO2e ≈ **243 tCO2e**. **Pitfall:** applying the UK
factor to mild/electric-heat geographies without adjustment; double counting
the heating term for employees who would heat the home anyway — DEFRA's
method already takes an incremental view; state your basis.

## Emission factors quick reference

Representative values — label, verify current vintage before use.

| Mode | EF | Units | Source/vintage |
|---|---|---|---|
| Average car (unknown fuel) | ~0.17 | kgCO2e/vehicle-km | DESNZ 2024 |
| US gasoline passenger car | ~0.34 (~0.21/km) | kgCO2e/vehicle-mile | EPA Hub 2024 |
| Motorcycle (average) | ~0.11 | kgCO2e/vehicle-km | DESNZ 2024 |
| Local bus | ~0.10 | kgCO2e/passenger-km | DESNZ 2024 |
| National rail (UK) | ~0.035 | kgCO2e/passenger-km | DESNZ 2024 |
| London Underground | ~0.028 | kgCO2e/passenger-km | DESNZ 2024 |
| US transit bus | ~0.06–0.07/pkm | kgCO2e/passenger-km | EPA Hub 2024 (per passenger-mile ~0.10) |
| Battery EV car (UK grid) | ~0.05 | kgCO2e/vehicle-km | DESNZ 2024 (scope 3 of employee; grid-dependent) |
| Homeworking | ~0.33 (≈0.30–0.34 across vintages) | kgCO2e/FTE-hour | DESNZ 2020–2024 |

Note on employee EVs: the employee's home charging is still category 7 for
the reporter (it is the employee's purchased electricity, not the reporter's
scope 2); use a per-km EV factor built on the local grid mix.

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

**Q1. Quick screen: 2,500 employees, no survey.** Average-data: assume 18 km
one-way, 75% car / 25% low-carbon mix, 210 on-site days (hybrid-adjusted),
car 0.17 kgCO2e/vkm: 2,500 × 0.75 × 18 × 2 × 210 × 0.17 / 1000 ≈ **2,410
tCO2e** (plus a small transit term ≈ 2,500×0.25×18×2×210×0.06/1000 ≈ 284
tCO2e) → ~**2,700 tCO2e**, ~1.1 tCO2e/FTE — in range. Screening grade;
survey if material.

**Q2. We moved to 3 days/week in office. How do we adjust last year's
survey-based figure?** Scale commuting days: prior on-site fraction (say
100%) → 0.6, so commuting term × 0.6; add telework term for the 2
days/week: FTE × 2 × 46 wks × 8 h × 0.33 kgCO2e/h. Disclose as an activity
change (no base-year recalc — real-world change, `ghg-protocol` §6).

**Q3. Is telework mandatory to report?** No — optional under the Scope 3
Standard/Guidance. But if remote days are a large share of working time,
omitting it while claiming commuting reductions is misleading; include it or
justify exclusion. Cite the DEFRA homeworking factor and vintage when used.

**Q4. An employee carpools with 2 colleagues, 30 km one-way, 140 on-site
days.** One vehicle: 30 × 2 × 140 = 8,400 vkm × 0.17 = 1,428 kgCO2e total ≈
**0.48 tCO2e per person** (÷3). Booking 3 × full vehicle-km would triple-count.

**Q5. Our company runs its own employee shuttle buses.** The shuttles' diesel
is **scope 1** (owned/operated), not category 7. Employees' travel from home
to the shuttle stop in their own cars remains category 7. A contracted
third-party shuttle would instead sit in category 7.

**Q6. Survey response was 12% — can we still use it?** Use with caution:
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
