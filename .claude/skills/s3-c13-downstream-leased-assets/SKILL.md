---
name: s3-c13-downstream-leased-assets
description: >-
  Scope 3 Category 13 — Downstream Leased Assets. Use for questions from the
  lessor's perspective: leased-out assets, landlord emissions, REITs and
  commercial property owners, tenant energy in landlord inventories, leased
  vehicle/equipment fleets, and lease-type (finance vs. operating) plus
  boundary-approach classification. Covers the asset-specific method (tenant
  submeter or utility data) and the average-data method (floor area ×
  CBECS/benchmark intensity), and the category 13 vs. category 11 overlap for
  leased products.
---

# Scope 3 Category 13 — Downstream Leased Assets

**Definition (Scope 3 Standard, ch. 5, category 13):** emissions from the
operation of assets that are **owned by the reporting company (acting as
lessor) and leased to other entities** in the reporting year, and that are
**not already included in scope 1 or scope 2**. The mirror image of
category 8 (upstream leased assets, lessee perspective). Core constituency:
REITs and commercial landlords, vehicle/equipment leasing companies,
equipment manufacturers with leasing arms.

Governing documents:
- Scope 3 Standard (2011), ch. 5, Table 5.4; **Appendix A (Accounting for Leased Assets)** — the decisive text for lease classification.
- Scope 3 Calculation Guidance (2013), **category 13 chapter** (asset-specific and average-data methods; lessor decision tree).
- Cross-cutting conventions: the `ghg-protocol` skill (boundary approaches §2, EF hierarchy §7, data quality §8).

## Boundary & classification

**The classification question comes first** (Scope 3 Standard, Appendix A):
whether a leased-out asset's operating emissions sit in your scope 1/2 or
category 13 depends on the **lease type** and your **consolidation
approach**:

| Lease type | Lessor's treatment |
|---|---|
| **Finance/capital lease** | Lessee holds ownership-like control → lessee's scope 1/2; lessor reports the asset's operation in **category 13** |
| **Operating lease** | Depends on lessor's boundary approach: under **operational control**, a landlord who does not operate tenant spaces (no operational control over tenant energy use) → **category 13**; where the lessor retains operational control (e.g., landlord-operated central plant, common areas, landlord-procured whole-building energy it controls) → those emissions are the lessor's **scope 1/2**, and only the remainder is category 13. Under equity share/financial control, owned leased-out assets generally land in scope 1/2. |

Practical REIT pattern (operational-control boundary): common-area and
landlord-operated central-plant energy → scopes 1/2; **tenant-space energy
(tenant-procured or tenant-controlled)** → category 13. Document the
building-by-building split; assurance providers ask for the lease-structure
rationale (triple-net vs. gross lease) per asset.

**In scope (minimum boundary):** scope 1 and 2 emissions of lessees during
operation of the leased assets (fuel combusted in/at the asset, electricity
consumed by the asset) not counted in the lessor's scopes 1/2. Optionally,
lessees' relevant scope 3-type life-cycle emissions.

**Out of scope / routed elsewhere:**
- Assets the reporter **leases in** (reporter = lessee) → category 8 or scopes 1/2.
- Assets **sold** to customers → category 11; assets both leased and later sold — account for the leased period in 13 and, if sold used, remaining lifetime per your category 11 policy (disclose).
- **Franchise** arrangements → category 14, even where property is leased to franchisees as part of the franchise package (put it in one category, disclose — the Guidance suggests franchises with leases may be reported in 13 or 14; convention: 14).
- Embodied/construction emissions of buildings you develop → categories 1/2 (capital goods for own account) at construction, not 13.
- **Category 13 vs. category 11 overlap for leased products:** equipment leased to customers (e.g., leased copiers, cars on operating lease) is category 13 during the lease. To avoid double counting, do not also run those units through category 11 as if sold. If a lessor prefers, the Standard permits accounting for lifetime use of leased products analogously to category 11 — pick one treatment per product line and disclose.

## Method ladder

| Tier | Method (Calc. Guidance, cat. 13) | Data basis | Typical use |
|---|---|---|---|
| 1 | **Asset-specific method** | Actual fuel/energy per leased asset: tenant submeters, tenant utility bills, whole-building meters net of landlord share, vehicle telematics/fuel cards | Managed portfolios; green-lease data clauses |
| 2 | **Average-data method** | Floor area (or asset count) × building-type energy intensity × EF | No tenant data; screening; residual gap-fill |

### 1. Asset-specific method

**When:** you can obtain per-asset energy — tenant-submetered electricity
and fuel, tenant utility-bill data (green lease clauses, ENERGY STAR
Portfolio Manager tenant sharing), or, for vehicles/equipment, fuel-card and
telematics data.

```text
C13 = Σ_assets [ Σ_fuels (fuel qty × fuel EF) + electricity (kWh) × grid EF ]
      − any portion already in lessor scope 1/2
```

**EF sources:** fuel EFs from EPA Hub / DESNZ; grid factors by asset
location (eGRID subregion, national factors) — location-based default;
market-based optionally in parallel (see `s2-purchased-electricity`).

**Method walk-through — tenant-space energy (office landlord).** Symbolic,
per asset:

```text
1. Tenant-procured electricity (kWh) and fuel (MMBtu, therms)
      ← tenant utility bills / submeters (green-lease clauses, ENERGY STAR
        Portfolio Manager tenant sharing), or whole-building data minus the
        landlord-metered share
2. Grid EF by asset location   ← eGRID subregion (US) / national factor,
        current year
3. Fuel EF                     ← EPA Hub / DESNZ, current edition (HHV-match)
4. Building C13 = Σ_fuels (qty × EF) + kWh × grid EF
5. Portfolio C13 = Σ_buildings − anything already in lessor scope 1/2
```

For vehicle/equipment lessors: fuel-card or telematics fuel per covered
unit × the fuel EF; extrapolate uncovered units at the covered-fleet
per-unit average, flagged as estimated — annual lease-period basis (see
traps).

**Pitfalls:** double counting whole-building utility data already in the
lessor's scope 2 (net out the landlord-procured share); tenant data with
mismatched periods (calendar-align or pro-rate); vacancies (vacant-space
energy the landlord controls is scope 1/2, not 13).

### 2. Average-data method

**When:** no tenant data. Floor area × building-type intensity:

```text
C13 = Σ_buildings [ leased floor area (ft² or m²)
                    × energy intensity_(building type) (kWh/ft²·yr by fuel)
                    × EF_fuel ]
```

**Intensity sources:** US — **CBECS** (Commercial Buildings Energy
Consumption Survey, 2018 survey, EIA — verify for newer cycles) by building
type and fuel; residential — RECS; UK/EU — CIBSE benchmarks, national EPC
data; or Portfolio Manager peer medians.

**Application note.** Take the current CBECS (or CIBSE/EPC) intensity for
the building type fuel by fuel — electricity in kWh/ft²·yr against the
location's grid factor, gas in kBtu or MMBtu/ft²·yr against the gas EF —
over the leased floor area, then sum. Prefer subregional grid factors, and
reconcile the area basis (CBECS intensities are whole-building) before
multiplying.

**Pitfalls:** wrong building type (retail vs. office intensities differ
~2×); gross vs. net rentable vs. tenant-occupied area; applying whole-building
intensities to tenant-space-only area (CBECS intensities are whole-building —
subtract the landlord scope 1/2 share or disclose the overlap treatment);
national-average intensity for extreme climates.

## Emission factor and parameter sources

Record source, edition/vintage, and units for every input per the
`ghg-protocol` skill §7.

| Source | Governing table / dataset | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| EIA CBECS | Building-type energy-intensity tables, by fuel (office, retail, warehouse, food service, lodging, etc.) | US commercial buildings | kWh/ft²·yr (electricity); kBtu/ft²·yr (total/gas); whole-building basis | Survey cycles (multi-year; verify the current cycle) |
| EIA RECS | Residential energy-intensity tables | US residential | per household / per ft² | Survey cycles |
| CIBSE benchmarks; national EPC registries | UK/EU building benchmarks | UK/EU buildings | kWh/m²·yr | Periodic |
| ENERGY STAR Portfolio Manager | Peer-median intensities | US/Canada portfolios | site/source EUI | Continuous |
| EPA eGRID | Subregion output emission rates | US grid, subregional and national | per MWh (convert to kWh) | Biennial data releases |
| EPA GHG EF Hub / UK DESNZ conversion factors | Fuel combustion tables (natural gas, gasoline, diesel) | Fuels | per MMBtu / gallon (EPA, HHV); per litre / kWh (DESNZ) | Annual |

This skill intentionally quotes no factor values. When a quantitative
answer is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **Annual, lease-period accounting — not lifetime.** Unlike category 11, category 13 covers emissions from operating the leased assets **during the reporting year**. A car on a 3-year lease contributes one year of driving per inventory year, not a lifetime block. If you instead elect the lifetime (category 11-style) treatment for leased products, say so and never mix conventions within a product line.
- **ft² vs. m²** (× 10.764) and **kBtu vs. kWh** (1 kWh = 3.412 kBtu) — CBECS mixes kWh (electricity) and kBtu/therm (gas).
- **Whole-building vs. tenant-space intensity**, gross vs. net lettable area, and occupancy adjustments.
- **Scope 2 / category 13 seam:** landlord-purchased energy resold or passed through to tenants — decide once (commonly: landlord-procured = lessor scope 2; tenant-procured = category 13), apply portfolio-wide, disclose.
- **Partial-year leases and acquisitions/disposals:** pro-rate by months under lease.
- **HHV/NCV** on gas factors as usual (`ghg-protocol` skill §7).

## Data collection & gap-filling

- **Lease abstracts:** lease type (finance/operating), utility responsibility (triple-net vs. gross), floor areas — the classification dataset.
- **Green lease clauses / tenant data programs:** contractual energy-data sharing; ENERGY STAR Portfolio Manager tenant sharing; automated utility-data services. Target the largest assets first.
- **Whole-building data** from utilities (aggregate/whole-building tariff data programs) minus landlord-metered share is often easier than tenant-by-tenant collection.
- **Gap-filling:** covered-asset intensity extrapolated to similar uncovered assets (per ft², per vehicle) beats generic CBECS; label filled values per the `ghg-protocol` skill §8. Report the % of floor area on actual vs. estimated data — a standard REIT disclosure metric (and what GRESB asks).

## QA checks

- **Classification audit:** every owned asset appears exactly once across scope 1/2, category 13, or (if franchised) category 14 — reconcile the fixed-asset register against the inventory.
- **No scope 2 double count:** landlord-procured energy not repeated in 13.
- **Intensity sanity:** implied kWh/ft² of asset-specific data vs. CBECS/benchmark range for the building type; outliers investigated.
- **Coverage metric:** % of leased area (or fleet) on actual data, tracked YoY; method-mix changes disclosed.
- **11/13 sweep:** no unit both "sold" (11) and "leased" (13) in the same year; consistent treatment at lease-end sales.
- **YoY consistency:** same benchmark source/vintage policy; portfolio changes (acquisitions/disposals) pro-rated, base year handled per the `ghg-protocol` skill §6.

## Worked FAQ

**Q1. We're a triple-net retail REIT, operational-control boundary, no
tenant data. First-pass C13?**
Average-data method: tenant-controlled floor area × the current CBECS
retail intensity, fuel by fuel, × location-appropriate EFs (subregional
grid factors where assets are geocoded; gas EF from the current EPA Hub).
Mind the building-type match (retail vs. office intensities differ
materially) and the whole-building area basis. Then start green-lease data
collection on the largest assets — % of area on actual data is the
maturity metric.

**Q2. Landlord buys all building energy and re-bills tenants. Scope 2
or C13?**
If you procure and control the supply, the standard treatment is lessor
**scope 2** for the whole building (you hold operational control of energy
supply); category 13 then excludes it. The alternative (tenant-share carved
into 13) is defensible where tenants control usage — choose one convention,
apply portfolio-wide, disclose. Never both.

**Q3. Equipment maker leasing 4,000 diesel generators (avg 900 operating
h/yr, 15 L/h). C13?**
`4,000 × 900 h × 15 L/h × 2.72 kgCO2e/L = 146,880 t ≈ 147,000 tCO2e/yr`.
Annual basis while leased; if a unit is later sold used, shift to your
category 11 policy for the remaining life and disclose.

**Q4. Our JV owns a leased-out mall; we hold 30% equity, no control,
financial-control boundary. Where does it go?**
Not category 13 — you are not the (consolidated) lessor. The equity stake
is **category 15** (investments): 30% × the JV's scope 1/2 (see
`s3-c15-investments`).

**Q5. Finance-leased trucks to customers — customers say it's their
scope 1. Both counting it?**
Yes, correctly: lessee scope 1 (they control and combust the fuel); lessor
category 13. Inter-company double counting across different inventories is
by design; it is only an error within one inventory.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5, Table 5.4 (category 13); **Appendix A — Accounting for Leased Assets** (lease-type × boundary-approach matrix).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 13 chapter (asset-specific and average-data methods).
- Data sources: EIA CBECS 2018 (and successors) building intensities; EIA RECS (residential); eGRID (subregional grid factors); EPA GHG Emission Factors Hub (annual); CIBSE/EPC benchmarks (UK/EU). Verify current editions.
- Cross-cutting rules: the `ghg-protocol` skill (§2 boundaries, §7 EF hierarchy, §8 data quality/gap-filling).
