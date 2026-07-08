---
name: s2-purchased-electricity
description: >-
  Scope 2 purchased grid electricity accounting under the GHG Protocol Scope 2
  Guidance (2015). Use for questions involving kWh or MWh consumption, utility
  bills/invoices, eGRID subregions and Power Profiler lookups, location-based
  vs market-based methods, dual reporting, RECs, GOs, I-RECs, PPAs (physical
  or virtual/VPPA), green tariffs, supplier-specific emission rates, residual
  mix (AIB / Green-e), renewable energy claims, on-site solar netting, EV
  charging electricity, tenant/landlord electricity splits, and grid emission
  factor selection (eGRID, IEA). For purchased steam, district heating/cooling,
  or CHP allocation use `s2-steam-heat-cooling` instead.
---

# Scope 2 — Purchased Electricity

Scope 2 covers emissions from the generation of purchased electricity consumed
in operations inside the reporting company's organizational boundary
(Corporate Standard, ch. 4). Since the GHG Protocol Scope 2 Guidance (2015),
companies with any operations in markets offering product/supplier choice or
contractual instruments **shall report scope 2 two ways**: a **location-based**
total (grid-average factors) and a **market-based** total (contractual
instruments) — the "dual reporting" requirement (Scope 2 Guidance, ch. 4).
Boundary, GWP-set, base-year, and EF-hierarchy conventions are defined in the
`ghg-protocol` skill; this skill assumes them.

## Boundary & classification

Scope 2 electricity = electricity **purchased or otherwise brought into the
organizational boundary and consumed** in owned/controlled operations. Common
classification calls:

- **Leased space — tenant with operational control** (typical office/retail
  lease where the tenant holds the utility account or controls operations):
  tenant reports the electricity as **scope 2**. Under the lessor's inventory
  the same electricity is scope 3 category 13 (downstream leased assets).
- **Landlord-purchased electricity** (full-service gross lease, landlord holds
  the account): if the tenant has operational control of the space, the
  tenant still reports its consumption as scope 2 — obtain **submetered** data
  where it exists; otherwise **allocate** the building total by leased floor
  area share (or occupied-hours-weighted share) and document the allocation
  basis. Common-area electricity purchased by the landlord for spaces the
  tenant does not control → tenant's scope 3 category 8 (upstream leased
  assets), landlord's scope 2.
- **Leases under financial control / equity share**: classification follows
  the consolidation approach chosen (see `ghg-protocol` §2) and lease type
  (finance vs operating); check boundary approach before assigning scope.
- **EV charging**:
  - Chargers at **company facilities** on company utility accounts → the
    charging electricity is already inside scope 2 (do not double count it as
    fleet fuel; the vehicles' scope 1 is zero for electric miles).
  - **Employee home charging** of company or personal vehicles → scope 3
    category 6 (business travel) or 7 (commuting), unless reimbursed
    electricity for company fleet vehicles is treated as purchased energy the
    company controls — state the treatment; most reporters use category 6/7
    or fleet scope 3.
  - **Public charging** paid per session → scope 3 (cat 6/7 for travel or
    commuting; purchased charging for owned fleet is commonly reported as
    scope 2 if the company purchases the electricity, or scope 3 cat 3 —
    disclose the choice and apply it consistently).
- **Self-generated renewable electricity consumed on-site** (rooftop solar
  behind the meter): **zero scope 2** for the self-consumed MWh (and zero
  scope 1 for non-combustion renewables). **But** if the associated RECs are
  sold or transferred, the company **shall not** claim the renewable
  attribute: the self-consumed MWh must be accounted with the **residual mix**
  (or grid-average where none exists) in the market-based total — no double
  claiming (Scope 2 Guidance, ch. 7). Exported surplus MWh are not the
  reporter's scope 2 at all.
- **Electricity purchased for resale** (utilities, retailers): generation
  emissions of resold power are **scope 3 category 3** for the reseller, not
  scope 2. Only the portion the utility itself consumes is its scope 2.
- **Transmission & distribution (T&D) losses** on purchased electricity →
  **scope 3 category 3** for end consumers (≈5% of delivered kWh in the US,
  eGRID grid gross loss ~4.7–5%; verify current eGRID). Exception: utilities
  reporting T&D losses on power they purchase and resell report those losses
  in scope 2 (see `s3-c03-fuel-energy-related`).

## Dual reporting — the core requirement

Both totals are required wherever any operations sit in markets with
contractual instruments (Scope 2 Guidance, ch. 4, "shall"):

- **Location-based**: reflects the average emissions intensity of the grids
  where consumption occurs. Factor hierarchy: subnational grid-average
  (eGRID subregion for the US), then national (IEA country factors), then
  regional. Contractual purchases are **ignored** — a facility's
  location-based number does not change when it buys RECs.
- **Market-based**: reflects emissions from the electricity the company has
  **purposefully chosen** via contractual instruments, with untracked
  consumption at the residual mix.

**Market-based data hierarchy** (Scope 2 Guidance ch. 6, Table 6.2 — use the
most precise available, in order):

1. **Energy attribute certificates** — RECs (US/Canada), GOs (Europe),
   I-RECs/other tracking systems elsewhere — whether standalone (unbundled)
   or bundled with power.
2. **Contracts** for electricity (e.g., PPAs) in markets where certificates
   do not exist or are not required to substantiate the claim.
3. **Supplier/utility-specific emission rates** (e.g., a green tariff or the
   supplier's disclosed product/fuel-mix rate, net of certificates sold off).
4. **Residual mix** — subnational or national — for consumption not covered
   by 1–3 in markets where instruments exist.
5. **Grid-average (location-based) factors** as the fallback where no
   residual mix is available — with disclosure that untracked claims may be
   double counted.

**Scope 2 Quality Criteria** (Scope 2 Guidance ch. 7.1 — all "shall" for any
instrument used in the market-based total). Contractual instruments must:

1. **Convey the GHG emission rate attribute** of the generation (direct
   emissions of the generator — zero for wind/solar/hydro; note biomass
   certificates can carry a non-zero direct rate).
2. Be the **only instrument** carrying that attribute claim (exclusive
   ownership — the same MWh's attributes cannot be sold twice).
3. Be **tracked and retired/redeemed/canceled** by or on behalf of the
   reporting entity (registry retirement statement is the evidence).
4. Be issued and redeemed **as close as possible to the consumption period**
   ("vintage" — best practice: generation within the reporting year; Green-e
   allows a defined window around the reporting year, roughly the 21 months
   spanning Jul 1 prior year–Mar 31 following year; verify current Green-e
   Standard).
5. Be sourced from the **same market** in which the consumption occurs
   (US/Canada RECs for North American load; AIB-domain GOs for European
   load; you cannot apply a Texas REC to German consumption).
6. For **supplier-specific rates**: the rate must be based on delivered
   electricity, incorporating certificates purchased and **excluding
   certificates sold** (otherwise the supplier double-claims).
7.–8. For consumption **without** instruments in markets where instruments
   exist, apply the **residual mix**; where no residual mix is published,
   grid-average may be used **with disclosure** of the double-counting risk.

**Residual mix sources**: **AIB European Residual Mixes** (published annually,
~May, for the prior year, per country) for Europe; **Green-e Residual Mix
Emissions Rates** (annual, by US region/eGRID grouping) for the US. Most
other markets (much of Asia, Latin America outside instrument markets) have
no residual mix → grid average with disclosure is permitted.

**PPAs**: for both **physical** PPAs and **financial/virtual** PPAs (VPPAs,
contracts-for-differences), the market-based claim rides on the **bundled
certificates**, not the power flow or financial settlement. A VPPA that does
not convey and retire RECs/GOs conveys nothing claimable. Certificates from a
VPPA must still satisfy the market-boundary and vintage criteria.

## Method ladder

| # | Method | Activity data | Emission factor | Use when | Uncertainty |
|---|---|---|---|---|---|
| 1 | Interval / submetered kWh × factor | Metered kWh per meter (AMI, submeters, BMS) | Subregion grid factor + instruments | Metering exists; needed for tenant splits, hourly matching | Lowest |
| 2 | Utility invoice kWh × factor | Billed kWh per account | Subregion grid factor + instruments | The standard method — invoices available | Low |
| 3 | Estimated kWh (floor area × intensity, or spend ÷ tariff) | ft² by building type, or $ spend | Benchmark intensity + grid factor | No invoices (landlord won't share, small sites) | High |
| 4 | Full proxy (headcount / revenue intensity) | FTEs, revenue, prior-year intensity | Prior-year kWh/FTE etc. | Screening, immaterial sites, acquisitions pre-data | Highest |

Disclose any mixing of tiers across the portfolio (`ghg-protocol` §3).

### Method 1 — Interval / submetered data

Same formula as Method 2 but per-meter, enabling exact tenant/landlord
splits, calendar-year cutoffs, and (optionally, as a disclosure) hourly
matching against time-stamped certificates. Reconcile the sum of submeters to
the master utility invoice (expect a small unmetered/loss remainder).

### Method 2 — Utility invoice kWh × grid factor (the standard)

```
Location-based emissions (t CO2e)
  = Σ over facilities [ kWh consumed × EF_grid (kg CO2e/kWh) ] / 1,000
```

**US factor assignment — eGRID subregion**: assign each facility to its eGRID
subregion by service address zip code / plant location using EPA **Power
Profiler** (or the eGRID subregion GIS shapefiles for precision near
boundaries). Use the subregion **total output emission rates** (annual, all
generation) — not the non-baseload rates, which are for avoided-emissions
analysis, not inventories. Include CH4 and N2O (eGRID publishes lb/MWh rates;
eGRID also publishes a combined CO2e rate — prefer it) and state the GWP set
per `ghg-protocol` §4.

- eGRID2022 US-average annual total output rate ≈ **818 lb CO2/MWh** ≈
  **0.371 kg CO2/kWh** (818 × 0.4536 / 1,000). Source: EPA eGRID2022
  (released 2024); approximate — verify the current release.
- **Vintage lag**: eGRID data year trails release by ~2 years (eGRID2022
  released Jan 2024). Convention: use the most recent release available for
  the reporting year and disclose the data-year mismatch; do not restate
  unless a base-year trigger applies (`ghg-protocol` §6).
- **Non-US grids**: IEA Emission Factors database (annual; licensed) country
  factors; national publications where superior (UK DESNZ/DEFRA grid factor,
  Canada NIR provincial factors, Australia NGA factors, Japan METI/MoE).

**Worked example (location-based)** — Atlanta office, calendar-2025 invoices
total 2,400,000 kWh; zip maps to eGRID subregion **SRSO**, illustrative
eGRID2022 total output rate ≈ 852 lb CO2/MWh (verify current eGRID):

```
EF = 852 lb/MWh × 0.4536 kg/lb ÷ 1,000 kWh/MWh = 0.3865 kg CO2/kWh
Emissions = 2,400,000 kWh × 0.3865 kg/kWh = 927,542 kg ≈ 928 t CO2
(+ CH4/N2O via eGRID CO2e rate — typically <1% additional)
```

**Market-based calculation mechanics**:

```
Market-based emissions
  = Σ [ MWh covered by instruments × EF_instrument ]        (usually 0 for renewables)
  + Σ [ MWh on supplier-specific rate × EF_supplier ]
  + Σ [ uncovered MWh × EF_residual_mix ]                   (grid avg if none exists)
```

Instrument-covered MWh can never exceed consumption MWh in the market where
the instruments are applied; excess certificates carry no scope 2 benefit
(they may support separate voluntary claims but do not go below zero).

**Worked dual-reporting example** — Midwest plant (RFCW), 10,000 MWh consumed
in 2025; company purchases and retires 6,000 MWh of wind RECs (same-year
vintage, US market):

```
Location-based:
  EF_RFCW ≈ 1,001 lb CO2/MWh (illustrative eGRID2022; verify)
          = 1,001 × 0.4536 / 1,000 = 0.454 kg CO2/kWh = 0.454 t CO2/MWh
  = 10,000 MWh × 0.454 t/MWh = 4,540 t CO2   ← unchanged by the RECs

Market-based:
  6,000 MWh × 0 t/MWh (wind REC direct rate)            =     0 t
  4,000 MWh × 0.50 t CO2/MWh (illustrative Green-e
      residual mix for the region; verify current year)  = 2,000 t
  Market-based total                                     = 2,000 t CO2
```

Report both totals; neither replaces the other. Note the residual mix rate
typically **exceeds** the grid average (renewable attributes are stripped
out), so partial REC coverage can still leave market-based near — or even
above — location-based.

**Pitfalls**: using non-baseload rates; using state-average instead of
subregion rates; treating a VPPA financial settlement as a claim without REC
retirement; netting on-site solar exports against consumption while also
selling the RECs; applying US-average factor to facilities in low-carbon
subregions (overstates) or coal-heavy ones (understates).

### Method 3 — Estimated kWh (floor area or spend)

```
kWh_est = floor area (ft²) × intensity benchmark (kWh/ft²·yr)     [preferred]
kWh_est = electricity spend ($) ÷ average retail tariff ($/kWh)   [fallback]
Emissions = kWh_est × EF_grid
```

Intensity benchmarks: CBECS 2018 electricity intensities (approximate; verify
current CBECS / ENERGY STAR Portfolio Manager technical reference), e.g.,
office ≈ 15 kWh/ft²·yr, warehouse ≈ 6.5, non-mall retail ≈ 13, lodging ≈ 12,
inpatient healthcare ≈ 29, food service ≈ 44. Tariff fallback: EIA average US
commercial retail price ≈ $0.127/kWh (2023; varies 2× by state — use the
state figure; verify current EIA data).

**Worked example** — 40,000 ft² leased office, landlord provides no data,
NYUP subregion (illustrative ≈ 236 lb CO2/MWh ≈ 0.107 kg/kWh; verify):

```
kWh_est = 40,000 ft² × 15 kWh/ft²·yr = 600,000 kWh
Emissions = 600,000 kWh × 0.107 kg/kWh = 64,200 kg ≈ 64 t CO2
```

Flag as estimated (data-quality rubric, `ghg-protocol` §8). Pitfall: applying
whole-building intensity to a partial-floor tenancy without prorating, or
using a national tariff in a high-price state (halves apparent kWh).

### Method 4 — Full proxy

```
kWh_est = headcount (FTE) × prior-year kWh/FTE      (or revenue × kWh/$)
```

Screening only. Example: new 120-FTE sales office; portfolio office intensity
last year 4,800 kWh/FTE → 576,000 kWh × local grid EF. Replace with invoices
next cycle; flag the value.

## Emission factors quick reference

**eGRID2022 annual total output CO2 rates — representative subregions**
(approximate values for orientation; always pull the current eGRID release):

| Subregion | Area | lb CO2/MWh | kg CO2/kWh |
|---|---|---|---|
| US average | — | ~818 | ~0.371 |
| CAMX | California | ~496 | ~0.225 |
| ERCT | Texas (ERCOT) | ~771 | ~0.350 |
| RFCW | Ohio Valley / Midwest | ~1,001 | ~0.454 |
| MROW | Upper Midwest | ~937 | ~0.425 |
| NYUP | Upstate New York | ~236 | ~0.107 |
| NWPP | Pacific Northwest | ~605 | ~0.274 |

Source: EPA eGRID2022 (2024 release), annual total output emission rates,
CO2 only — add CH4/N2O (or use eGRID CO2e rates). **Verify against the
current eGRID publication before use.**

| Item | Value / note | Source |
|---|---|---|
| Non-US grid factors | Country-level CO2 and CO2e per kWh, annual | IEA Emission Factors (current edition; licensed) — verify vintage vs reporting year |
| US residual mix | Regional lb CO2e/MWh; typically > grid average | Green-e Residual Mix Emissions Rates (annual; verify current) |
| European residual mix | Per-country g CO2/kWh, direct + LCA variants | AIB European Residual Mixes (annual, ~May release; use "direct" for scope 2) |
| T&D grid gross loss (US) | ~4.7–5% of delivered kWh → scope 3 cat 3 | eGRID2022 (verify current) |

## Unit and conversion traps

- **lb/MWh → kg/kWh**: multiply by 0.4536 (kg per lb), divide by 1,000 (kWh
  per MWh). 818 lb/MWh × 0.4536 / 1,000 = 0.371 kg/kWh. Dividing by 2,204.62
  alone gives kg/**MWh** ÷ 1,000 — same result, but do it once, not twice.
- **MWh vs kWh**: 1 MWh = 1,000 kWh. The classic 1,000× error — check that
  invoice units (usually kWh) match the factor denominator.
- **kW vs kWh**: demand (kW) charges on invoices are not energy; never sum
  the demand column.
- **Gross vs net metering**: for on-site solar with net metering, scope 2
  applies to **grid-delivered** kWh (gross imports), not the netted bill
  quantity; self-consumed generation is separate (see Boundary §). Netted
  bills understate both imports and generation — request the interval data.
- **Billing-period vs calendar-year cutoff**: invoices rarely align to Jan 1/
  Dec 31. Prorate the straddling bills by days (kWh × days-in-year/days-in-
  bill) or use interval data; apply the same convention every year.
- **MJ/GJ invoices** (some non-US utilities): 1 GJ = 277.78 kWh.
- **CO2 vs CO2e factors**: eGRID subregion CO2 rates exclude CH4/N2O; label
  which you used and be consistent.

## Data collection & gap-filling

**Primary evidence**: utility invoices or EDI/utility-portal feeds (kWh,
account, service address, billing period); ENERGY STAR Portfolio Manager
exports (metered consumption by property); landlord statements / lease
reconciliations (submetered or allocated kWh); interval/AMI data. For the
market-based total: **REC/GO retirement statements** from the registry
(quantity, vintage, generator, beneficiary), PPA contracts and settlement
attestations, green-tariff confirmations, **supplier fuel-mix disclosures**
(with certificate-adjusted emission rate).

**Gap-filling** (document and apply consistently; flag filled values —
`ghg-protocol` §8):
- **Missing month**: use the same month prior year, adjusted by degree days
  for weather-sensitive loads: `kWh_est = kWh_prior × (DD_cur / DD_prior)`;
  or average of adjacent months for flat loads.
- **Missing site**: like-facility intensity (kWh/ft² of comparable sites).
- **Move-in / move-out**: prorate the transition month by occupancy days;
  include acquired facilities from the acquisition date (`ghg-protocol` §6).
- **Estimated meter reads**: utilities true-up later — take the corrected
  invoice when available.

## QA checks

- **Intensity sanity**: kWh/ft²·yr within building-type range (office ~10–20,
  warehouse ~4–10, data center 10–100+; flag outliers ±50% vs CBECS
  benchmark or prior year).
- **Market vs location logic**: market-based < location-based only if
  instruments or a cleaner supplier rate were applied; market-based >
  location-based is legitimate where residual mix > grid average — verify it
  is that and not an error.
- **REC coverage**: retired instrument MWh ≤ consumption MWh per market;
  vintages within the accepted window; retirement statements name the
  reporting entity (or its agent) as beneficiary.
- **Residual mix applied** to all uncovered MWh in instrument markets — using
  grid average there without disclosure fails Quality Criteria 7–8.
- **Subregion spot checks**: re-run 5–10 addresses through Power Profiler,
  especially near subregion boundaries and for multi-state accounts.
- **Completeness**: account inventory vs facility register; 12 billing
  periods per account; no double count of submeters + master meter.
- Factor metadata recorded (source, year, units) for every EF.

## Worked FAQ

**Q1. Our German office consumed 800 MWh and bought no GOs. What goes in each
total?**
Location-based: 800 MWh × the German grid-average factor (IEA or UBA;
illustrative ≈ 0.38 t CO2/MWh, verify current) ≈ 304 t CO2. Market-based:
Germany is an instrument market, so use the **AIB German residual mix**
(illustrative ≈ 0.55 t CO2/MWh direct, verify current AIB release):
800 × 0.55 ≈ **440 t CO2**. Market-based exceeds location-based because
tracked renewable attributes are removed from the residual mix.

**Q2. We have 10,000 MWh consumption, 6,000 MWh retired wind RECs — both
totals?**
See the worked dual-reporting example above: location-based ≈ 4,540 t CO2
(RFCW illustrative 0.454 t/MWh — RECs change nothing); market-based = 6,000 ×
0 + 4,000 × residual mix (illustrative 0.50 t/MWh) = **2,000 t CO2**. Report
both, cite factor sources and vintages.

**Q3. Our VPPA settled 20,000 MWh but the project registry shows no REC
retirement to us. Can we claim it?**
No. The market-based claim requires the certificates to be conveyed and
retired for your benefit (Quality Criteria 1–3). A financial settlement alone
conveys no attribute. Fix the contract administration (retirement in your
name or to your beneficiary account), then claim the retired vintage-matched
MWh.

**Q4. Rooftop solar generated 1,200 MWh; we consumed 900 MWh on-site,
exported 300 MWh, and sold all the RECs. Scope 2 impact?**
The 900 MWh self-consumed cannot be claimed as renewable (RECs sold). Market-
based: 900 MWh × residual mix. Location-based: convention is that self-
generated self-consumed electricity is not "purchased," so most reporters
apply the grid factor only to grid **imports**; if you include self-consumed
MWh in the market-based total at residual mix (required by the no-double-
claiming rule when RECs are sold), disclose the treatment. The 300 MWh
exported are not your scope 2. At an illustrative residual mix of
0.50 t/MWh: 900 × 0.50 = **450 t CO2** added to market-based.

**Q5. Landlord bills us a fixed rate per ft² with no kWh — what do we do?**
Method 3: estimate kWh from your leased area × CBECS-type intensity (e.g.,
25,000 ft² × 15 kWh/ft² = 375,000 kWh), apply the local subregion factor, and
flag as estimated. In parallel, request a landlord statement or submeter —
this is also the data you need for any future market-based instrument
matching.

**Q6. Which eGRID rate column do we use — total output or non-baseload?**
**Total output** annual rates for inventory accounting. Non-baseload rates
approximate marginal generation and are for estimating avoided emissions from
interventions — using them in an inventory overstates most facilities'
emissions and is a common assurance finding.

## References

- GHG Protocol Corporate Standard (2004, rev.), ch. 4 (operational boundary).
- GHG Protocol **Scope 2 Guidance** (2015): ch. 4 (dual reporting
  requirement), ch. 5 (location-based hierarchy), ch. 6 incl. Table 6.2
  (market-based data hierarchy), ch. 7 (Quality Criteria, residual mix),
  ch. 8 (calculation), ch. 11 (disclosure & recommended renewable-purchase
  features).
- EPA **eGRID** (annual releases; subregion total output rates; Power
  Profiler for zip-to-subregion) and EPA GHG Emission Factors Hub.
- **IEA Emission Factors** database (annual; non-US grid factors).
- **AIB European Residual Mixes** (annual); **Green-e** Residual Mix Emissions
  Rates and Green-e Energy National Standard (vintage windows).
- CBECS (EIA, 2018) / ENERGY STAR Portfolio Manager (intensity benchmarks).
- Cross-cutting conventions: the `ghg-protocol` skill (GWPs §4, base year §6,
  EF hierarchy §7, data quality §8).
