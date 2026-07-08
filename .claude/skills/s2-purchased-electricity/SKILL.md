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
  factor source selection (eGRID, IEA). For purchased steam, district
  heating/cooling, or CHP allocation use `s2-steam-heat-cooling` instead.
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
  **scope 3 category 3** for end consumers (a few percent of delivered kWh in
  the US; eGRID publishes the grid gross loss rate — pull the current
  release). Exception: utilities reporting T&D losses on power they purchase
  and resell report those losses in scope 2 (see `s3-c03-fuel-energy-related`).

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
analysis, not inventories. Include CH4 and N2O (eGRID publishes per-gas
lb/MWh rates and a combined CO2e rate — prefer the CO2e rate) and state the
GWP set per `ghg-protocol` §4.

- **Location-based factor source**: EPA eGRID, total output emission rate
  for the assigned subregion, lb/MWh, updated annually with a ~2-year
  data-vintage lag. Convention: use the most recent release available for
  the reporting year and disclose the data-year mismatch; do not restate
  unless a base-year trigger applies (`ghg-protocol` §6).
- **Non-US grids**: IEA Emission Factors database (annual; licensed) country
  factors; national publications where superior (UK DESNZ/DEFRA grid factor,
  Canada NIR provincial factors, Australia NGA factors, Japan METI/MoE).

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

**Dual-reporting walk-through** (symbolic) — a facility consumes `C` MWh in
the reporting year and retires `R` MWh of same-market, vintage-eligible wind
RECs, with `R ≤ C`:

```
Location-based:
  E_LB = C × EF_grid
    EF_grid: subregion total output rate, current eGRID release (Power
    Profiler assignment); convert lb/MWh → t/MWh (× 0.4536 / 1,000)
    ← unchanged by the RECs

Market-based:
  E_MB = R × EF_instrument + (C − R) × EF_RM
    EF_instrument: generator direct rate conveyed by the certificate
      (zero for wind/solar/hydro; may be non-zero for biomass)
    EF_RM: residual mix for the consumption market — Green-e (US) or AIB
      (Europe), current release; grid average with disclosure if none exists
```

Report both totals; neither replaces the other. Note the residual mix rate
typically **exceeds** the grid average (renewable attributes are stripped
out), so partial REC coverage can still leave market-based near — or even
above — location-based.

**Pitfalls**: using non-baseload rates; using state-average instead of
subregion rates; treating a VPPA financial settlement as a claim without REC
retirement; netting on-site solar exports against consumption while also
selling the RECs; applying a US-average factor to facilities in low-carbon
subregions (overstates) or coal-heavy ones (understates).

### Method 3 — Estimated kWh (floor area or spend)

```
kWh_est = floor area (ft²) × intensity benchmark (kWh/ft²·yr)     [preferred]
kWh_est = electricity spend ($) ÷ average retail tariff ($/kWh)   [fallback]
Emissions = kWh_est × EF_grid
```

Intensity benchmarks: CBECS electricity intensities by building type (pull
the current CBECS tables or the ENERGY STAR Portfolio Manager technical
reference; offices commonly run ~10–20 kWh/ft²·yr — see QA sanity ranges).
Tariff fallback: EIA average retail commercial price for the facility's
**state** (current year) — state prices vary ~2×, so never use the national
figure when the state is known.

Walk-through (symbolic): `A` = leased area (ft², prorated to the tenancy),
`I` = benchmark intensity for the building type → `kWh_est = A × I`,
`E = kWh_est × EF_grid` (subregion factor as in Method 2). Flag as estimated
(data-quality rubric, `ghg-protocol` §8). Pitfall: applying whole-building
intensity to a partial-floor tenancy without prorating, or using a national
tariff in a high-price state (halves apparent kWh).

### Method 4 — Full proxy

```
kWh_est = headcount (FTE) × prior-year kWh/FTE      (or revenue × kWh/$)
```

Screening only. Derive the intensity from the portfolio's own prior-year
data for comparable sites, apply the local grid factor, replace with
invoices next cycle, and flag the value.

## Emission factor sources

| Source | Governing table / series | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| EPA eGRID | Subregion **total output** emission rates (CO2, CH4, N2O, and combined CO2e); Power Profiler for zip-to-subregion | US, by eGRID subregion | lb/MWh | Annual release; ~2-year data-vintage lag |
| IEA Emission Factors | Country grid factors, CO2 and CO2e | Non-US national grids | per kWh | Annual; licensed; verify vintage vs reporting year |
| Green-e Residual Mix Emissions Rates | US regional residual mix (typically above grid average) | US, by region/eGRID grouping | lb CO2e/MWh | Annual |
| AIB European Residual Mixes | Per-country residual mix, direct + LCA variants — use "direct" for scope 2 | Europe (AIB domain) | g CO2/kWh | Annual, ~May release for prior year |
| Supplier fuel-mix disclosures | Product/supplier emission rate, certificate-adjusted | Contracted supply | per supplier disclosure | Annual |
| National publications | UK DESNZ/DEFRA grid factor; Canada NIR provincial; Australia NGA; Japan METI/MoE | Respective countries | per national convention | Annual |

eGRID also publishes the US **grid gross loss** rate used for scope 3
category 3 T&D losses (see `s3-c03-fuel-energy-related`).

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **lb/MWh → kg/kWh**: multiply by 0.4536 (kg per lb), divide by 1,000 (kWh
  per MWh) — i.e., kg/kWh = lb/MWh × 0.0004536. Dividing by 2,204.62 alone
  gives kg/**MWh** ÷ 1,000 — same result, but do it once, not twice.
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

**Q1. Our German office consumed electricity and bought no GOs. What goes in
each total?**
Location-based: consumption × the German grid-average factor (IEA country
factor, or a superior national publication), current vintage. Market-based:
Germany is an instrument market, so untracked consumption takes the **AIB
German residual mix** (direct variant, current release) — not the grid
average. Expect market-based to exceed location-based, because tracked
renewable attributes are stripped out of the residual mix; that outcome is
correct, not an error.

**Q2. We have consumption in one US market and retired wind RECs covering
part of it — how do the two totals work?**
Follow the dual-reporting walk-through above. Location-based: full
consumption × the subregion total output rate (current eGRID) — the RECs
change nothing. Market-based: REC-covered MWh at the certificate's conveyed
direct rate (zero for wind) plus the uncovered remainder at the current
Green-e residual mix for the region. Before crediting the RECs, confirm the
Quality Criteria: same market as the load, vintage within the accepted
window, retirement statement naming the reporting entity as beneficiary.
Report both totals with factor sources and vintages.

**Q3. Our VPPA settled 20,000 MWh but the project registry shows no REC
retirement to us. Can we claim it?**
No. The market-based claim requires the certificates to be conveyed and
retired for your benefit (Quality Criteria 1–3). A financial settlement alone
conveys no attribute. Fix the contract administration (retirement in your
name or to your beneficiary account), then claim the retired vintage-matched
MWh.

**Q4. Rooftop solar generated more than we consumed on-site; we exported the
surplus and sold all the RECs. Scope 2 impact?**
The self-consumed MWh cannot be claimed as renewable (RECs sold). Market-
based: self-consumed MWh × residual mix. Location-based: convention is that
self-generated self-consumed electricity is not "purchased," so most
reporters apply the grid factor only to grid **imports**; if you include
self-consumed MWh in the market-based total at residual mix (required by the
no-double-claiming rule when RECs are sold), disclose the treatment. The
exported MWh are not your scope 2.

**Q5. Landlord bills us a fixed rate per ft² with no kWh — what do we do?**
Method 3: estimate kWh from your leased area × a CBECS-type intensity for
the building type (prorated to your tenancy), apply the local subregion
factor, and flag as estimated. In parallel, request a landlord statement or
submeter — this is also the data you need for any future market-based
instrument matching.

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
- CBECS (EIA) / ENERGY STAR Portfolio Manager (intensity benchmarks).
- Cross-cutting conventions: the `ghg-protocol` skill (GWPs §4, base year §6,
  EF hierarchy §7, data quality §8).
