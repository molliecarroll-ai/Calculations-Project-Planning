---
name: s3-c08-upstream-leased-assets
description: >-
  Scope 3 Category 8 (Upstream Leased Assets) methodology assistant. Use for
  questions about leased offices, leased buildings, leased vehicles, and leased
  equipment where the reporter is the lessee and the emissions are not already
  in scope 1 or 2. Covers the operational-control vs. financial/equity boundary
  interaction, lessor-provided data, floor-area intensity (CBECS) estimation,
  and the category 8 vs. scope 1/2 vs. category 13 routing decision.
---

# Scope 3 Category 8 — Upstream Leased Assets

**Definition (Scope 3 Standard, ch. 5, table 5.4):** Emissions from the
operation of assets **leased by the reporting company (as lessee)** in the
reporting year that are **not already included in scope 1 or scope 2**. The
category exists to catch leased-asset emissions that the organizational
boundary choice pushes out of scopes 1/2 — it is a residual category, not a
place to double count.

**Governing documents:** Scope 3 Standard (2011), category 8 + appendix on
leased assets; Technical Guidance for Calculating Scope 3 Emissions (v1.0,
2013), category 8 chapter. Cross-cutting conventions are in the
`ghg-protocol` skill.

## Boundary & classification

**The key insight:** category 8's content is determined by your
**organizational boundary approach** (`ghg-protocol` §2) and lease type,
*before* any calculation:

| Boundary approach | Lease situation | Where emissions go |
|---|---|---|
| Operational control | Any lease the reporter operates (typical office lease, leased vehicle fleet the company runs) | **Scope 1** (fuel) / **Scope 2** (purchased electricity) — **not** category 8 |
| Operational control | Leased asset the reporter does *not* operate (rare as lessee) | Category 8 |
| Financial control / equity share | Finance/capital lease (asset on balance sheet) | Scope 1/2 |
| Financial control / equity share | **Operating lease** (not on balance sheet under the Standard's convention) | **Category 8** |

Consequences:
- Under **operational control** (the most common choice), most leased
  offices, vehicles, and equipment land in scope 1/2, and **category 8 is
  often empty or minimal**. Do not "move" leased-office electricity into
  category 8 to flatter scope 2 — that misstates both.
- Under **financial control or equity share**, energy use of assets held
  under **operating leases** (leased offices you don't financially control,
  short-term equipment rentals, operating-leased vehicles) lands here.
- Note the accounting-standards wrinkle: IFRS 16/ASC 842 moved most operating
  leases onto balance sheets, but GHG Protocol lease classification follows
  the Standard's own guidance (operational vs. financial control over the
  asset), not current financial-statement geography. Document your mapping.

**Common residual contents even under operational control:**
- **Landlord-controlled common areas and central plant** in leased buildings
  where the reporter has no operational control over HVAC/central services
  and doesn't procure the energy (tenant sub-metered spaces are scope 2;
  landlord-run central boiler serving your floor: judgment — many report
  allocated central-plant energy in scope 2 if they consume it; if excluded
  there, capture it here). Decide once, disclose.
- Short-term rentals/equipment where operation is genuinely the lessor's.
- Co-location data centers: usually treated as purchased services (category 1)
  or scope 2 (if the reporter controls its IT load's power contract) — a
  known grey zone; some reporters use category 8. Pick a treatment, disclose,
  and keep it consistent.

**Routing traps:**
- Reporter as **lessor** (you lease assets *to* others) → **category 13**,
  the downstream mirror.
- Rental cars and hotels on business trips → category 6, not category 8
  (business-travel convention).
- Franchise operations → category 14.
- Whatever is excluded from scope 1/2 by the boundary must land here — the
  Standard does not permit leased-asset emissions to vanish between scopes.

**Minimum boundary:** scope 1 and 2 emissions of lessors occurring during the
reporter's operation of leased assets (i.e., the assets' fuel combustion and
purchased electricity). Optional: the assets' life-cycle (embodied)
emissions — normally excluded here (embodied emissions of leased capital
sit with the lessor).

## Method ladder

Scope 3 Calculation Guidance, category 8:

| Tier | Method | Data needed |
|---|---|---|
| 1 | Asset-specific | Metered fuel/energy per leased asset × fuel/grid EFs |
| 2 | Lessor-specific | Lessor-provided energy or emissions allocated to your leased share |
| 3 | Average-data: floor-area intensity | Leased m²/ft² × building-type energy intensity (CBECS, ECON 19) × EFs |
| 4 | Proxy: headcount / asset-count | FTE or asset count × per-unit intensity from measured sites |

### Method 1 — Asset-specific

**When:** you have meters or fuel records for the leased asset (then ask
first whether it actually belongs in scope 1/2 under your boundary!).

```
CO2e = Σ  fuel [units] × fuel EF  +  electricity [kWh] × grid EF
```

Use standard stationary/mobile combustion factors (EPA Hub, DESNZ) and grid
factors (eGRID, IEA) — see `s1-stationary-combustion`, `s2-purchased-electricity`
for factor discipline. **Walk-through:** for an operating-leased warehouse
under an equity-share boundary with no operational control, take metered gas
(current-year EPA Hub or DESNZ fuel factor, matching the fuel's unit and
HHV/NCV basis) plus metered kWh (current-year subregional eGRID or national
grid factor), sum the two lines, and book the total in category 8.

### Method 2 — Lessor-specific

```
CO2e = lessor-reported building emissions × (your leased area ÷ total lettable area)
   or  lessor-allocated kWh/fuel × EFs
```

Ask landlords for tenant sustainability statements (increasingly standard in
green leases). **Pitfalls:** lessor allocations may include common areas
(fine — disclose), use market-based electricity factors (align with your
scope 2 method choice), or a different reporting year (pro-rate).

### Method 3 — Floor-area × intensity (average-data)

**When:** no meter/lessor data; the workhorse for leased offices.

```
CO2e = leased area [ft² or m²] × energy intensity_buildingtype [kWh/ft²/yr]
       × (fuel/electricity split) × respective EFs
```

**Intensity sources:** US — EIA **CBECS** (Commercial Buildings Energy
Consumption Survey; 2018 survey published 2022 — verify current; office
average site energy ≈ **77 kBtu/ft²/yr ≈ 22.6 kWh/ft²/yr**, roughly
55% electricity / 45% fuels for office stock); UK — BEES/CIBSE benchmarks;
EU national equivalents.

**Worked example.** 40,000 ft² operating-leased office, US:

```
Electricity: 40,000 ft² × 12.4 kWh/ft²/yr (CBECS 2018 office electric; verify)
           = 496,000 kWh × 0.38 kgCO2e/kWh (eGRID subregion; verify) = 188.5 tCO2e
Natural gas: 40,000 ft² × 31 kBtu/ft²/yr = 1,240 MMBtu × 53.1 kgCO2e/MMBtu
           (EPA Hub 2024, incl. CH4/N2O; verify) = 65.8 tCO2e
Category 8 ≈ 254 tCO2e
```

**Pitfalls:** CBECS intensities are US-stock averages — climate zone and
building age swing them ±50%; site vs. source energy (use **site** kWh with
combustion/grid EFs — source-energy figures double-count generation losses);
leased *usable* vs. *rentable* area (intensities are per gross floor area).

### Method 4 — Headcount / asset-count proxy

```
CO2e = FTE_unmeasured × (tCO2e/FTE from measured comparable sites)
   or  n_assets × per-asset intensity (e.g., leased forklift-hours × fuel rate)
```

Last-resort gap-fill; flag per `ghg-protocol` §8. Typical measured office
building-energy intensity lands ~0.3–1.0 tCO2e/FTE/yr depending on grid and
climate — derive your own, don't borrow this range for reporting.

## Emission factors quick reference

Category 8 reuses stationary/mobile/electricity factors — no category-native
factor set. Representative anchors (verify current):

| Quantity | Value | Source/vintage |
|---|---|---|
| Office site energy intensity (US avg) | ~77 kBtu/ft²/yr (~22.6 kWh/ft²/yr) | EIA CBECS 2018 |
| Warehouse site energy intensity (US avg) | ~25–30 kBtu/ft²/yr | EIA CBECS 2018 |
| Natural gas | 53.1 kgCO2e/MMBtu (HHV) | EPA Hub 2024, AR5 |
| US grid (national avg, location-based) | ~0.37 kgCO2e/kWh | eGRID 2023 (use subregion) |
| UK grid | ~0.207 kgCO2e/kWh | DESNZ 2024 |
| Average car (leased, if c8) | ~0.17 kgCO2e/vehicle-km | DESNZ 2024 |

## Unit and conversion traps

- **kBtu vs. kWh** (1 kWh = 3.412 kBtu) — CBECS publishes kBtu/ft².
- **ft² vs. m²** (1 m² = 10.764 ft²) in international portfolios.
- **Site vs. source energy**: apply EFs to site energy only.
- **HHV vs. NCV** on gas intensities (US HHV convention — `ghg-protocol` §7).
- **Partial-year leases**: pro-rate intensity-based estimates by lease months.
- **Shared buildings**: allocate lessor data by your floor-area share, not
  headcount share, unless the lessor allocates otherwise.

## Data collection & gap-filling

- **Lease register** (from real estate/finance): asset list, area, lease
  type (operating/finance), term dates — the starting inventory; classify
  each lease against the boundary table above before collecting energy data.
- **Landlord/lessor energy statements**; green-lease data clauses for future
  years.
- **Utility bills or sub-meters** where the reporter pays directly (usually →
  scope 2, but confirms intensities).
- **Gap-fill** unmeasured leases with floor-area intensity; annualize partial
  data; flag estimates distinctly (`ghg-protocol` §8).

## QA checks

- **Double-count sweep**: every leased asset must appear exactly once across
  scope 1, scope 2, and category 8 — reconcile the lease register against the
  scope 1/2 facility list annually.
- **Empty-category justification**: under operational control, "category 8 =
  0 (all leased assets in scope 1/2)" is a legitimate, disclosable outcome —
  say it explicitly rather than leaving the category blank.
- **Intensity sanity**: implied kWh/ft² of estimates should sit within ~2× of
  CBECS/benchmark for the building type.
- **Boundary drift**: lease reclassifications (IFRS 16 adoption, boundary
  approach change) shift emissions between scopes without real change —
  document; boundary-approach change triggers base-year recalculation
  (`ghg-protocol` §6).

## Worked FAQ

**Q1. We lease all 12 of our offices and pay the utilities. Operational
control boundary — what's in category 8?** Likely nothing from those offices:
gas you burn is scope 1, electricity you buy is scope 2. Category 8 would
hold only leased assets you don't operate. Report category 8 as not
applicable/zero with that justification.

**Q2. Equity-share boundary; we hold a 5-year operating lease on a regional
office, landlord bills energy in rent.** Category 8. No meter data →
floor-area method: 15,000 ft² × 22.6 kWh/ft²/yr ≈ 339,000 kWh-equivalent
site energy; split 55/45 electric/gas per CBECS: 186,450 kWh × 0.38
kgCO2e/kWh ≈ 70.9 t; 152,550 kWh × 3.412 = 520.5 MMBtu-equiv… simpler: 465
MMBtu gas × 53.1 = 24.7 t. **≈ 96 tCO2e** (screening; request lessor data).

**Q3. Our leased company-car fleet — category 8?** Under operational control
(you fuel and direct the vehicles): **scope 1**. Under a financial-control
reading where they're operating leases you also operate — still typically
scope 1 by the leased-assets appendix (lessee with operational control).
Category 8 only if you genuinely don't operate them.

**Q4. We sublease two floors to another tenant.** For that sublet space you
are a lessor → **category 13** (downstream leased assets), while the head
lease's retained space follows the normal analysis. Allocate by floor area.

**Q5. Colocation data center rack space?** Grey zone. Common treatments: (a)
scope 2 if you control the equipment's power draw and the colo passes through
metered kWh (many reporters + the Scope 2 Guidance lean here), (b) category 1
purchased services, (c) category 8 leased asset. Choose, disclose, keep
consistent; metered-kWh-based scope 2 gives the best decision usefulness.

## References

- Corporate Value Chain (Scope 3) Standard (2011), ch. 5, table 5.4 (category 8) and appendix A (accounting for leased assets: lessee/lessor, lease-type matrix).
- Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 8 chapter (asset-specific, lessor-specific, average-data methods).
- GHG Protocol FAQ on leased assets / Corporate Standard ch. 4 (boundary interaction).
- EIA CBECS (2018, published 2022) — building energy intensities; UK CIBSE/BEES benchmarks.
- EPA GHG Emission Factors Hub; eGRID; DESNZ conversion factors — the underlying fuel/grid EFs.
- `ghg-protocol` skill — organizational boundaries (§2), EF hierarchy (§7), base-year rules (§6).
