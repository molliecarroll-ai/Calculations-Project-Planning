---
name: s3-c09-downstream-transportation
description: >-
  Scope 3 Category 9 (Downstream Transportation and Distribution) methodology
  assistant. Use for questions about downstream freight, customer-paid or
  customer-arranged shipping of sold products, retail and distribution-center
  storage of sold products, the category 4 vs. category 9 payment-boundary
  rule, tonne-km freight calculations, GLEC-aligned mode factors, and
  end-customer transport to point of use.
---

# Scope 3 Category 9 — Downstream Transportation and Distribution

**Definition (Scope 3 Standard, ch. 5, table 5.4):** Emissions from
transportation and distribution of **sold products** in the reporting year,
in vehicles and facilities **not owned or controlled by the reporting
company** and **not paid for by the reporting company** — i.e., transport
and storage paid by customers or other downstream parties, between the point
of sale (or reporter's gate) and the end consumer. Includes downstream retail
and storage.

**Governing documents:** Scope 3 Standard (2011), category 9; Technical
Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 9 chapter
(which explicitly mirrors the category 4 methods). Cross-cutting conventions
are in the `ghg-protocol` skill.

## Boundary & classification

**The payment-boundary rule (the c4/c9 hinge).** The Scope 3 Standard sorts
product transport by **who pays/procures it**, not by direction of goods
flow:
- Transport the **reporter pays for** — inbound *and outbound* — → **category
  4** (upstream transportation and distribution). Yes: reporter-paid outbound
  shipping of sold products is category 4 by definition, because purchased
  transport services are an upstream purchase.
- Transport **paid/arranged by customers or downstream parties** (customer
  collects ex-works, retailer runs its own distribution, distributor pays
  freight) → **category 9**.

Apply the rule shipment-population by Incoterms/freight terms: ex-works/FCA
sales where the buyer books the carrier → c9; DAP/DDP/prepaid-freight sales →
c4. A company selling everything delivered-duty-paid may legitimately have a
near-zero category 9 (transport) and a big category 4 — state this rather
than splitting arbitrarily.

**In scope (minimum boundary):**
- Third-party, downstream-paid **freight**: road, rail, sea, air, barge,
  parcel — from reporter's gate through to the end consumer, across however
  many downstream echelons (distributor → retailer → consumer) as can be
  reasonably modeled.
- **Storage and distribution centers** holding sold products downstream
  (customer/3PL-paid warehousing): facility scope 1 + 2 allocated to the
  reporter's product throughput.
- **Retail**: retail stores' scope 1 + 2 allocated to the reporter's products
  (shelf/floor-space or throughput allocation) — required within the minimum
  boundary where products are sold via retail not paid by the reporter.
- **Optional:** end-consumer travel to the point of purchase (explicitly
  optional in the Guidance; most reporters exclude — disclose either way).
- Refrigerant leakage from downstream cold-chain transport/storage where
  material (cold-chain products) — part of facilities'/vehicles' scope 1.

**Out of scope / routing:**
- Reporter-paid transport of any kind → category 4.
- Reporter-**owned/operated** trucks, DCs, retail stores → scope 1/2.
- Transport of sold *intermediate* products to the customer's processing →
  still c9 if customer-paid (processing itself → category 10).
- Emissions of using sold products (fuel burned by a sold vehicle) →
  category 11; end-of-life → category 12.
- Franchised retail stores → category 14 (if franchisor); leased-out DCs →
  category 13.

**Double-counting note:** your category 9 is your customer's category 4 —
that overlap between different companies' inventories is by design and is
not an error.

## Method ladder

Methods mirror category 4 (the Guidance says so explicitly): fuel-based,
distance-based, and spend-based for transport, plus a site/average method for
storage and retail. The extra difficulty vs. c4: the activity data belongs to
**other parties**, so expect modeled distances and customer-supplied data.

| Tier | Method | Data needed | Typical use |
|---|---|---|---|
| 1 | Fuel-based | Fuel used by downstream carriers/DCs allocated to your goods | Rare; dedicated customer fleets sharing data |
| 2 | Distance-based | mass × distance per shipment/echelon × mode EF (tonne-km) | The standard where shipment lanes are known/modelable |
| 3 | Spend-based | Downstream parties' transport spend on your products × EEIO | Screening; customer-reported spend |
| + | Storage & retail | Facility energy × your throughput share; or tonnes × per-tonne storage factor | Wherever downstream warehousing/retail is material |

### Method 1 — Fuel-based

**When:** a downstream partner (retailer's fleet, customer's dedicated haul)
shares fuel data attributable to your products.

```
CO2e = Σ fuel [litres] × fuel EF [kgCO2e/litre]
       × allocation share (your tonnes or tonne-km ÷ total carried) / 1000
```

Fuel EFs come from the standard fuel tables (DESNZ "Fuels" tab; EPA Hub —
per litre/gallon, updated annually). **Pitfall:** allocating shared vehicles
by shipment count instead of mass or tonne-km biases against dense products.

### Method 2 — Distance-based (tonne-km; the standard)

```
CO2e = Σ_legs  mass [tonnes] × distance [km] × EF_mode [kgCO2e/tonne-km] / 1000
```

Build the downstream network model: sold volumes by customer/region, typical
lane distances (gate → customer DC → retail → consumer as far as included),
mode by lane. Where actual customer lanes are unknown, model representative
lanes (e.g., national average gate-to-retail distance) and disclose the
modeling basis.

**EF sources:** GLEC Framework (v3; the ISO 14083-aligned freight
methodology — preferred for freight; WTW by default, label if using TTW),
DESNZ 2024 "Freighting goods" tables (kgCO2e/tonne-km by vehicle class and
load assumptions), EPA Hub freight factors (per ton-mile).

**Method walk-through.**

1. From the sales ledger, split sold tonnes by Incoterms: customer-paid
   legs stay in this category; reporter-paid legs go to c4.
2. Build lanes per downstream leg: tonnes (gross, including packaging) ×
   distance. First-echelon distances come from ship-to addresses; lower
   echelons from national-average haul lengths, disclosed as modeled.
3. Assign a mode per lane and sum tonne-km by mode.
4. Apply current-year mode factors — GLEC v3 defaults (WTW) or DESNZ
   "Freighting goods" (TTW, with a separate WTT tab) by vehicle class and
   load assumption; EPA Hub per short-ton-mile for US data — one WTW/TTW
   basis for the whole category, labeled.
5. CO2e = Σ_lanes tonne-km × EF_mode / 1000; record each lane's data-quality
   tier.

**Pitfalls:** using vehicle-km factors with tonne payloads (an HGV
vehicle-km factor is roughly an order of magnitude above its per-tonne-km
counterpart at typical loads); empty running and load factor — DEFRA
"average laden" factors embed UK-average utilization and empty-return
assumptions, so don't apply a separate empty-running uplift on top;
double-counting the leg the reporter paid for (that one is c4).

**Multi-echelon modeling discipline.** When goods pass through several
downstream stages, build the model as a table of (echelon, share of sold
tonnes, mode, distance) and let unknown lower echelons default to national
averages. Example structure for a consumer-goods seller (ex-works):

```
Echelon                     Tonnes basis        Mode       Distance source
gate → customer DC          100% of sold t      road       ship-to addresses
customer DC → retail store  retail-channel t    road       national avg (e.g., 60–100 km)
retail → consumer           optional            car        excluded (disclosed)
export leg                  export t            sea/air    port-pair distances
```

Sum tonne-km per row, apply mode EFs, and record each row's data-quality tier
separately — the first echelon is usually tier 2 (real addresses), the lower
ones tier 3–4 (modeled). Disclose the blend per `ghg-protocol` §3.

### Method 3 — Spend-based

```
CO2e = downstream transport spend on your products [$] × EEIO freight factor [kgCO2e/$] / 1000
```

Usable when customers disclose freight spend, or by estimating freight cost
as a % of downstream revenue on your products (industry logistics-cost
benchmarks ~4–8% of sales for consumer goods — document). Screening only.

### Storage, distribution centers, and retail

```
CO2e_storage = Σ_facilities  facility (S1+S2) emissions × (your throughput or space share)
   or         tonnes sold × storage intensity [kgCO2e/t] (per-pallet-week × dwell time)
CO2e_retail  = retail store (S1+S2) × allocation (shelf-space share, or sales share)
   or         tonnes/units sold × retail intensity benchmark
```

Where retailer data is unavailable, an average-data route: retail energy
intensity (CBECS "mercantile" building type, current release) × estimated
shelf-space-ft²-years attributable to your products × grid/fuel EFs —
coarse; disclose. For warehousing, derive a per-pallet-week or per-tonne-week
intensity from GLEC logistics-site guidance or 3PL data (chilled/frozen runs
several times ambient); label as estimate. Storage and retail are usually a
minor add-on to transport for ambient goods — cold chain is the exception.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| GLEC Framework v3 (ISO 14083-aligned) | Default freight factors by mode | Road, rail, sea (container/bulk), air, inland waterway, transshipment; logistics-site guidance | kgCO2e per tonne-km, WTW by default | Framework revisions; factors updated periodically |
| UK DESNZ/DEFRA GHG Conversion Factors | "Freighting goods" + "WTT — delivery vehicles" | Road by vehicle class and laden assumption (incl. refrigerated variants), rail, sea, air (with/without RF) | kgCO2e per tonne-km, TTW with separate WTT tab | Annual |
| US EPA GHG Emission Factors Hub | Product transport tables | US road, rail, air, waterborne freight | per short-ton-mile (1 ton-mile = 1.460 t-km); CO2/CH4/N2O separate | Annual |
| EIA CBECS | Mercantile / warehouse building types | Retail and storage energy intensities for average-data allocation | kBtu/ft²/yr site energy | Multi-year survey cycle |
| DESNZ / EPA Hub fuel tables | Fuels | Fuel-based method (diesel, marine fuels) | per litre / gallon | Annual |

Per tonne-km, air freight sits far above road, and road far above rail and
sea — mode mix dominates everything else in this category.

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **tonne-km vs. ton-mile**: 1 ton-mile (US short ton) = 1.460 tonne-km;
  EPA factors are per short-ton-mile.
- **Vehicle-km vs. tonne-km factors** — never interchange (see Method 2).
- **WTW vs. TTW**: GLEC/ISO 14083 report well-to-wheel; DEFRA splits TTW +
  WTT. Pick one basis for the whole category and label it.
- **Chargeable vs. actual weight** (parcel/air): carriers bill dimensional
  weight; emissions want actual mass.
- **One leg or many**: model each downstream echelon separately; don't apply
  gate-to-consumer straight-line distance to a multi-stop network.
- **Gross vs. net product mass**: include packaging mass in the shipped
  tonnes (it travels too).
- **RF on air freight**: same optional-multiplier discipline as category 6 —
  disclose and hold consistent.

## Data collection & gap-filling

- **Sales/ERP data**: sold tonnes by customer, region, and Incoterms — the
  c4/c9 split starts here.
- **Customer logistics surveys**: lane distances, modes, DC dwell for top
  customers (mirror of the supplier surveys used in c4).
- **Retailer sustainability programs** (e.g., major-retailer supplier
  scorecards) sometimes publish per-supplier downstream logistics estimates —
  reconcile methodology before adopting.
- **3PL/carrier reports** where downstream parties share them.
- **Gap-filling**: model representative lanes from customer ship-to
  addresses; national average haul lengths (e.g., US average truck shipment
  distances from FAF/CFS data) for the unknown tail; flag all modeled legs
  (`ghg-protocol` §8).

## QA checks

- **c4/c9 reconciliation**: total product transport (c4 + c9 + scope 1
  fleet) should cover ~100% of sold tonnes' movement; overlaps = paid-leg
  double counting.
- **Implied intensity**: category total ÷ sold tonnes ÷ average distance
  should land near the mode-mix-weighted EF; an implied 1+ kgCO2e/t-km means
  a vehicle-km factor slipped in.
- **Mode-mix sanity**: air share of t-km above a few percent should be
  deliberate and documented.
- **Ex-works share stability**: YoY movement in the c4/c9 split should track
  real Incoterms changes, not data noise.
- **Retail/storage share**: for ambient goods, storage+retail is usually a
  minor add-on to transport; if it dominates, check the allocation basis.

## Worked FAQ

**Q1. We pay outbound freight to our distributors (DAP); they pay onward
freight to retailers. Split?** Your paid leg (gate→distributor) → **category
4**. Distributor-paid onward legs (distributor→retail→consumer) → **category
9**. Compute both with the same tonne-km method; never book the paid leg in
both.

**Q2. Product sold ex-works and customers truck it — what is the
calculation?** Tonne-km distance-based: sold tonnes × average haul distance
(from ship-to addresses or a national-average assumption, disclosed) × the
current-year road-freight factor for the representative vehicle class and
laden assumption (DESNZ "Freighting goods" TTW, adding the WTT tab for WTW;
or GLEC WTW defaults). Label the WTW/TTW basis on the result.

**Q3. A customer air-freights our product instead of sea — does it matter?**
Substantially: per tonne-km, air freight is far above sea, so a single
customer's mode switch on a long lane can be visible at category level.
Compute the lane's tonne-km with the air factor (RF treatment disclosed and
consistent with your category 6 convention), and capture top customers'
actual modes specifically rather than assuming a default mode mix.

**Q4. Our products sell through 2,000 retail stores we don't own or pay.**
Minimum boundary includes retail scope 1+2 allocated to your products. Coarse
route: estimate shelf space ft² × store-years occupied by your SKUs × retail
energy intensity (CBECS mercantile, verify) × grid/fuel EFs; or obtain
retailer-allocated figures. Disclose the allocation basis — sales-share vs.
space-share can differ materially.

**Q5. Do we include consumers driving to the store to buy our product?**
Optional (Scope 3 Calculation Guidance, category 9). Most reporters exclude;
if the business model makes it material (e.g., destination retail), you may
include a modeled estimate (trips × distance × car EF ÷ basket allocation) —
disclose either way.

**Q6. We use a 3PL for outbound distribution that we pay for — c9 because
it's outbound?** No — **category 4**. Payment/procurement, not direction,
decides. The 3PL's warehousing you pay for is likewise c4 (or scope 1/2 if
you operate the site).

**Q7. Cold chain: customers distribute our frozen product — anything beyond
the truck fuel?** Yes, two additions: refrigeration-unit fuel/energy — use
the refrigerated-HGV variants in the DESNZ "Freighting goods" table (they
run materially above ambient per t-km) rather than an ad hoc uplift — and
**refrigerant leakage** from reefer units and cold stores (scope 1 of the
downstream party, in your c9 allocation). For frozen goods, cold-store dwell
(tonnes × weeks × a frozen-store intensity derived from 3PL or GLEC
logistics-site data) can rival the transport term — model it explicitly.

## References

- Corporate Value Chain (Scope 3) Standard (2011), ch. 5, table 5.4 (categories 4 and 9 definitions; payment boundary).
- Technical Guidance for Calculating Scope 3 Emissions (v1.0, 2013), category 9 chapter (methods mirror category 4: fuel-based, distance-based, spend-based; storage/retail allocation).
- GLEC Framework v3 / ISO 14083:2023 — freight and logistics-site emission accounting, default factors (WTW).
- UK DESNZ/DEFRA GHG Conversion Factors (annual): "Freighting goods" and "WTT — delivery vehicles" tabs.
- US EPA GHG Emission Factors Hub (annual): product transport factors per short-ton-mile; EIA CBECS for retail/warehouse intensities; FHWA FAF / Census CFS for US haul-length statistics.
- `ghg-protocol` skill — EF hierarchy, hybrid-method disclosure, data-quality scoring.
