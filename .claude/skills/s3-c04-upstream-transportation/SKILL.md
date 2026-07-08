---
name: s3-c04-upstream-transportation
description: >-
  Scope 3 Category 4 (Upstream Transportation and Distribution) methodology
  assistant. Use for freight and logistics footprints: inbound transport,
  reporter-paid outbound shipping, 3PL trucking, air/ocean/rail freight,
  tonne-km distance-based calculations per the GLEC Framework and DEFRA
  freight tables, fuel-based carrier calculations, EPA SmartWay data,
  refrigerated transport uplifts, and third-party warehousing/distribution
  centers. Also covers the Category 4 vs Category 9 who-pays split.
---

# Scope 3 Category 4 — Upstream Transportation and Distribution

**Category definition (Scope 3 Standard, ch. 5, Table 5.4):**
"Transportation and distribution of products purchased by the reporting
company in the reporting year between a company's tier 1 suppliers and its
own operations (in vehicles and facilities not owned or controlled by the
reporting company); [and] transportation and distribution services purchased
by the reporting company in the reporting year, including inbound logistics,
outbound logistics (e.g., of sold products), and transportation and
distribution between a company's own facilities (in vehicles and facilities
not owned or operated by the reporting company)." **Minimum boundary:** the
scope 1 and scope 2 emissions of transportation and distribution providers
occurring during use of vehicles and facilities (e.g., from energy use);
optionally, the life-cycle emissions associated with manufacturing vehicles
and infrastructure.

Governing documents: Scope 3 Standard (2011), ch. 5; Technical Guidance for
Calculating Scope 3 Emissions (v1.0, 2013), Category 4 chapter; GLEC
Framework (Smart Freight Centre; v3.x, aligned with ISO 14083:2023) as the
sector methodology. Cross-cutting conventions live in the `ghg-protocol`
skill.

## Boundary & classification

**In scope:**
- **Inbound logistics**: transport of purchased goods from tier-1 suppliers
  to the reporter's operations — by convention including legs the reporter
  pays for; supplier-paid inbound embedded in product price is in principle
  Category 1 (see resolution rules).
- **Outbound logistics the reporter purchases**: delivery of sold products
  where the *reporter* buys the freight service (very common — a seller
  paying a parcel carrier reports that in Category 4, not 9).
- **Inter-facility transfers** by third-party carriers between the reporter's
  own sites.
- **Third-party warehousing, distribution centers, transshipment sites, and
  retail/distribution services purchased** (3PL storage energy use).

**Out of scope / routed elsewhere:**
- **Category 9 (downstream T&D)**: transport and distribution of sold
  products **paid for by the customer or other downstream parties** — the
  who-pays test is the operative split between 4 and 9. A given lane is never
  in both.
- **Own or leased-and-operated vehicles/warehouses** → scope 1/2 (mobile
  combustion, facility energy), not Category 4.
- Freight embedded in supplier prices → Category 1 in principle; if you model
  known supplier-paid inbound lanes in Category 4 instead (a common practical
  convention when you have lane visibility), disclose it and ensure the
  Category 1 method doesn't also capture it (purchaser-price EEIO factors
  include transport margins).
- Employee travel → Categories 6/7; transport of waste → commonly included
  in Category 5 with the waste treatment (either 4 or 5 is defensible —
  disclose).
- Fuel WTT of *your own* vehicles → Category 3. For third-party carriers,
  the **minimum boundary is the carriers' scope 1+2 (tank-to-wheel + facility
  energy)**; GLEC/ISO 14083 practice and DEFRA WTW factors include the fuel
  WTT as well. Including WTT in Category 4 is widespread, and is best
  practice — state whether your factors are TTW or WTW and keep one basis.

## Method ladder

The Scope 3 Calculation Guidance (Category 4) names three methods:

| # | Method | Activity data | Emission factor | Typical use |
|---|---|---|---|---|
| 1 | Fuel-based | Fuel consumed by carriers on your behalf (or carrier scope 1+2 allocated) | Fuel combustion (+WTT) EFs | Dedicated fleets, engaged carriers |
| 2 | Distance-based | Shipment mass × distance × mode | Mode/vehicle-class EFs per tonne-km (GLEC, DEFRA, SmartWay) | Default when shipment data exists |
| 3 | Spend-based | Freight/logistics spend by mode | EEIO $-intensity | Screening, tail spend, parcel where mass unknown |

### Method 1 — Fuel-based

**When:** carriers report fuel used for your shipments (dedicated routes,
contract fleets), or you allocate a carrier's total fuel by your share of
its activity.

```
Emissions = Σ_fuels ( fuel consumed on reporter's behalf × EF_fuel )

# Allocation when only carrier totals exist:
Reporter share = carrier total fuel × ( reporter t-km ÷ carrier total t-km )
```

**Worked example:** A dedicated trucking contract consumed 180,000 L diesel
for your freight.

```
TTW: 180,000 L × 2.51 kg CO2e/L = 451,800 kg = 452 t CO2e   # DEFRA 2024 diesel (avg blend) combustion — verify
WTT: 180,000 L × 0.61 kg CO2e/L = 109,800 kg = 110 t CO2e   # DEFRA 2024 WTT — verify
WTW total                        = 562 t CO2e  (state WTW basis)
```

**Pitfalls:** allocating by shipments instead of t-km biases against dense
freight; refrigeration fuel/refrigerant leakage from reefer units is often a
separate fuel line — ask for it; empty repositioning fuel belongs in the
allocation base.

### Method 2 — Distance-based (the workhorse)

```
Emissions = Σ_legs ( mass (t) × distance (km) × EF_mode,vehicle (kg CO2e/t-km) )
```

- **Mass**: actual shipment weight (chargeable/volumetric weight is a billing
  construct — use physical mass; for volumetric goods GLEC allows
  volume-based intensity).
- **Distance**: actual routed distance by mode; else great-circle ×
  mode-specific detour ("distance adjustment") factors per GLEC (e.g., sea
  routes via port-pair tables, road ~ great-circle × 1.2 or network
  distance).
- **EF**: GLEC Framework default intensities, DEFRA/DESNZ freighting-goods
  tables (annual), EPA SmartWay carrier-specific g/ton-mile data (US),
  carrier-published intensities (ISO 14083 statements increasingly available).

**Load factor and backhaul:** default factors embed average utilization
*including empty running* (DEFRA "average laden" HGV factors assume ~UK
average loading and empty-run share; GLEC defaults similarly). Only adjust
when you have real utilization data:

```
EF_adjusted ≈ EF_vehicle-km ÷ (payload capacity × load factor × (1 − empty-run share))
```

Never apply a full-truck assumption to LTL parcel freight — you'd understate
several-fold.

**Multimodal worked example:** 2,400 t of components: Shanghai→Rotterdam by
container ship (19,500 km sea route), then Rotterdam→Frankfurt by HGV
(580 km road).

```
Sea:  2,400 t × 19,500 km × 0.016 kg CO2e/t-km = 748,800 kg  # container ship avg, DEFRA 2024 / GLEC v3 defaults, TTW ≈0.013–0.016; WTW slightly higher — verify
Road: 2,400 t ×    580 km × 0.13  kg CO2e/t-km = 180,960 kg  # all-HGV avg laden, WTW (DEFRA 2024 ≈0.105 TTW + ≈0.026 WTT) — verify
Total = 929,760 kg ≈ 930 t CO2e
```

Note the ratio: the 580 km road leg emits ~24% as much as the 19,500 km sea
leg — mode choice dominates freight footprints.

**Refrigerated transport:** apply the reefer uplift — DEFRA publishes
refrigerated HGV/van factors ~**12–20% above ambient** for road (2024
tables — verify) ; refrigerated container shipping uplifts can be larger
(reefer power). Don't forget refrigerant leakage if using carrier fuel data.

**Warehousing / transshipment (logistics sites):**

```
Energy-based:  site kWh & fuel allocated to reporter's throughput × grid/fuel EFs
Volume-based:  m³ stored × days × site intensity (kg CO2e/m³·day)  # GLEC logistics-site defaults
Throughput:    tonnes handled × kg CO2e/t handled (transshipment default)
```

GLEC/ISO 14083 provide default logistics-site intensities by site type
(ambient vs temperature-controlled warehouse, transshipment terminal) — pull
current values from the GLEC default-data annex; temperature-controlled sites
run several times ambient intensity.

**Pitfalls:** tonne-km built from *average* rather than actual shipment
masses; double counting the road leg already inside an intermodal factor;
using short-haul air factors for long-haul lanes (short-haul intensity is
~2–3× long-haul); radiative forcing on air freight (DEFRA publishes with- and
without-RF factors — with-RF roughly ~1.9× on CO2e; state your choice).

### Method 3 — Spend-based

```
Emissions = Σ_modes ( freight spend, deflated to factor $-year × EEIO EF_mode )
```

**Worked example:** $2.0M (2025 USD) on truck freight; EPA Supply Chain
Factors v1.3, truck transportation ≈ 0.8 kg CO2e/2022 USD (purchaser price —
illustrative; verify). Deflator 2025→2022 = 1.09 (illustrative).

```
2,000,000 ÷ 1.09 × 0.8 kg/$ = 1,468,000 kg ≈ 1,468 t CO2e
```

**Pitfalls:** freight rates swing with fuel surcharges and market cycles
while physical flows don't — spend-based Category 4 is volatile and
non-steerable; parcel/express spend maps poorly to trucking factors (courier
commodity differs); deduplicate freight already embedded in Category 1 goods
prices.

## Emission factors quick reference

Representative WTW magnitudes per tonne-km — the mode hierarchy (air ≫ road ≫
rail ≈ sea) matters more than decimals. Verify all against current DEFRA/GLEC
publications.

| Mode | ~kg CO2e/tonne-km (WTW) | Source & vintage |
|---|---|---|
| Air freight, long-haul intl (no RF) | ~0.6–0.8 | DEFRA 2024 freighting goods — verify; with RF ≈ ×1.9 |
| Air freight, short-haul (no RF) | ~1.5–2.5 | DEFRA 2024 — verify |
| Van/LGV (parcel-scale road) | ~0.5–0.7 | DEFRA 2024 — verify |
| HGV, all types, average laden | ~0.11–0.13 | DEFRA 2024 (TTW ≈0.105 + WTT ≈0.026) — verify |
| HGV, articulated >33t, avg laden | ~0.08–0.10 | DEFRA 2024 — verify |
| Refrigerated HGV | ambient × ~1.12–1.20 | DEFRA 2024 refrigerated tables — verify |
| Rail freight | ~0.03 | DEFRA 2024 / GLEC v3 — verify |
| Inland waterway/barge | ~0.03–0.05 | GLEC v3 defaults — verify |
| Container ship (deep sea) | ~0.015–0.02 | DEFRA 2024 / GLEC v3 (size-class dependent) — verify |
| Bulk carrier (dry bulk) | ~0.004–0.01 | GLEC v3 / IMO — verify |
| Truck transportation (spend) | ~0.7–0.9 kg CO2e/2022 USD | EPA Supply Chain Factors v1.3 — verify |
| Air transportation (spend) | ~0.9–1.2 kg CO2e/2022 USD | EPA SEF v1.3 — verify |

Rule of thumb: air ≈ 30–50× sea, ≈ 5–8× road per tonne-km; a single air-vs-sea
mode decision usually outweighs every factor-precision question.

## Unit and conversion traps

- **tonne-km vs ton-mile:** US factors (SmartWay) run in g CO2e per short
  ton-mile. 1 tonne-km = 0.685 short ton-miles; 1 g/ton-mile = 1.459 g/t-km.
  Mixing them silently misstates by ~46%.
- **TTW vs WTW basis:** the minimum boundary is carriers' scope 1+2 (≈TTW),
  but DEFRA/GLEC practice is WTW. Pick one basis, label every factor, and
  never sum TTW and WTW lines.
- **kg vs tonnes of shipment mass** (1,000× errors) and **chargeable vs
  actual weight** (volumetric billing weight overstates mass for light goods).
- **Great-circle vs routed distance:** apply GLEC distance-adjustment
  conventions; sea distances come from port-pair tables, not straight lines.
- **Radiative forcing on air:** with-RF vs without-RF is roughly a factor
  ~1.9 on air CO2e (DEFRA) — disclose the choice and keep it consistent with
  Category 6.
- **Intermodal double counts:** a "door-to-door intermodal" carrier factor
  already includes drayage — don't add separate road legs on top.

## Data collection & gap-filling

1. **Transport management system (TMS) / freight-audit-and-pay extract**:
   shipment-level origin, destination, mass, mode, carrier, cost. This is the
   distance-based method's raw material; freight-audit data is usually the
   cleanest single source.
2. **Carrier engagement:** request ISO 14083 / GLEC-conformant emissions
   statements (large ocean, air, and parcel carriers publish shipment-level
   or intensity data; EPA SmartWay for US trucking carrier-specific
   g/ton-mile). Carrier-reported beats defaults on the ladder.
3. **3PL/warehouse providers:** annual energy allocated by your share of
   throughput, pallet-positions, or m³·days; else GLEC site defaults.
4. **Spend cube for the tail:** freight GL accounts + parcel/courier spend not
   in the TMS → spend-based; reconcile total freight spend to the P&L.
5. **Supplier-paid inbound:** if modeling it here, derive lanes from purchase
   orders (supplier location → receiving site, PO weights); disclose the
   convention (see Boundary).
6. **Gap-filling:** missing mass → category-average density × volume, or
   average shipment mass by lane, flagged; missing distance → geocoded
   great-circle × mode adjustment; missing mode → conservative default
   (road for continental, air only with evidence). Flag fills per
   `ghg-protocol` §8.

## QA checks

- **Share reasonableness:** Category 4 is commonly ~5–15% of scope 3 for
  manufacturers/retailers; air-freight-heavy businesses (fashion, pharma,
  electronics) run far higher. An implied network intensity outside
  ~0.01–0.6 kg CO2e/t-km should trace to mode mix or an error.
- **Coverage vs P&L:** freight + logistics spend put through methods
  reconciles to freight expense lines; TMS shipment count vs goods-receipt
  count catches missing flows.
- **Double-count scans:** no lane in both Cat 4 and Cat 9 (who-pays test
  applied shipment-population-wide); no supplier-paid freight in both Cat 1
  and Cat 4; own-fleet fuel not in both scope 1 and Cat 4; warehouse energy
  not in both scope 2 (leased-and-operated) and Cat 4.
- **Basis consistency:** single TTW-or-WTW basis; single RF convention for
  air; single unit system (t-km) after conversion; GWP set per inventory.
- **Mode-mix sanity:** tonnage by mode vs emissions by mode — air should be a
  tiny mass share with an outsized emissions share; if not, factors are
  crossed.

## Worked FAQ

**Q1. 15 t of goods air-freighted Hong Kong→Los Angeles (11,650 km).**
15 t × 11,650 km × 0.65 kg CO2e/t-km (long-haul intl air, no RF, DEFRA
2024 — verify) = **113.6 t CO2e** (≈216 t with RF at ~1.9×). Note the same
mass by container ship (~0.016) would be ~2.8 t CO2e — 40× less.

**Q2. Customer picks up goods from our dock and pays a carrier. Cat 4 or 9?**
Category 9 for you (downstream party pays). If you had paid that same carrier,
it would be your Category 4. Apply the who-pays test across the whole
shipment population, not lane by lane ad hoc.

**Q3. 3PL warehouse stores our goods: our share is 5,000 pallet-positions,
provider allocates us 220,000 kWh electricity + 8,000 L propane forklift fuel.**
Electricity: 220,000 kWh × 0.373 kg CO2e/kWh (eGRID 2022 US avg — use
subregion, verify) = 82.1 t. Propane: 8,000 L × 1.54 kg CO2e/L (EPA Hub
2024 — verify) = 12.3 t. **≈94 t CO2e in Category 4** (energy-based site
method).

**Q4. Our LTL shipments: 3,800 shipments, avg 450 kg, avg 720 km by road.**
3,800 × 0.45 t × 720 km = 1,231,200 t-km × 0.13 kg CO2e/t-km (all-HGV avg
laden WTW, DEFRA 2024 — verify) = **160 t CO2e**. Don't use an articulated-
full-load factor for LTL; average-laden all-HGV or a parcel-network factor is
appropriate.

**Q5. Refrigerated distribution of 900 t over avg 350 km (chilled).**
900 t × 350 km = 315,000 t-km × (0.13 × 1.15 uplift) ≈ 0.15 kg CO2e/t-km
(DEFRA 2024 refrigerated HGV — verify exact factor rather than applying an
uplift when the published refrigerated factor exists) = **47 t CO2e**.

**Q6. Our carrier gave us a SmartWay figure: 78 g CO2e/ton-mile for our
lanes, 2.1M ton-miles. Convert and compute.**
78 g/ton-mile × 1.459 = 113.8 g CO2e/t-km; 2.1M ton-miles ÷ 0.685 = 3.066M
t-km. Either path: 2,100,000 × 78 g = **163.8 t CO2e** (SmartWay data is
carrier-specific TTW+ conventions — check its basis before mixing with WTW
lines).

## References

- GHG Protocol Corporate Value Chain (Scope 3) Standard (2011) — ch. 5,
  Table 5.4 (Category 4 definition and minimum boundary; Cat 9 mirror).
- Technical Guidance for Calculating Scope 3 Emissions v1.0 (2013) —
  Category 4 chapter (fuel-based, distance-based, spend-based methods;
  allocation guidance).
- GLEC Framework (Smart Freight Centre, current v3.x) and ISO 14083:2023 —
  freight-sector method, default intensities, distance conventions,
  logistics-site defaults.
- DEFRA/DESNZ UK Government GHG Conversion Factors (annual) — freighting
  goods, WTT, refrigerated tables.
- EPA SmartWay (carrier-specific US truck/rail/barge data); EPA Supply Chain
  GHG Emission Factors (spend-based); IMO GHG studies (shipping).
- Cross-cutting conventions: the `ghg-protocol` skill.
