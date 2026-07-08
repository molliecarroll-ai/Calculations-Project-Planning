---
name: s3-c01-purchased-goods-services
description: >-
  Scope 3 Category 1 (Purchased Goods and Services) methodology assistant. Use
  for procurement footprints, supplier emissions allocation, spend-based EEIO
  calculations (USEEIO, EXIOBASE), cradle-to-gate product factors (ecoinvent,
  DEFRA material factors), supplier-specific PCFs, and the hybrid method. Also
  use for questions about mapping AP/spend data to NAICS/UNSPSC, CDP supply
  chain data, and avoiding double counting between purchased goods, capital
  goods, and inbound freight.
---

# Scope 3 Category 1 — Purchased Goods and Services

**Category definition (Scope 3 Standard, ch. 5, Table 5.4):** "Extraction,
production, and transportation of goods and services purchased or acquired by
the reporting company in the reporting year, not otherwise included in
Categories 2–8." **Minimum boundary:** all upstream (cradle-to-gate) emissions
of purchased goods and services.

Governing documents: Corporate Value Chain (Scope 3) Accounting and Reporting
Standard (2011), ch. 5 and Appendix; Technical Guidance for Calculating
Scope 3 Emissions (v1.0, 2013), Category 1 chapter. Cross-cutting conventions
(method-ladder rules, GWP sets, EF hierarchy, data quality scoring, answering
style) are defined in the `ghg-protocol` skill — apply them here without
restatement.

## Boundary & classification

**In scope (minimum boundary):**
- Cradle-to-gate emissions of **all** purchased or acquired products (goods
  and services): raw material extraction, agriculture, intermediate
  manufacturing, upstream transport between suppliers, and the tier-1
  supplier's own scope 1 and 2 emissions attributable to the product.
- Both production-related procurement (materials, components, contract
  manufacturing) and non-production procurement (IT services, consulting,
  cleaning, software, marketing, insurance).
- Goods acquired free of charge or via barter still count if acquired.

**Out of scope / routed elsewhere:**
- **Capital goods → Category 2.** The dividing line is the reporter's own
  financial accounting treatment: if the purchase is **capitalized** on the
  balance sheet (fixed asset, PP&E), it is Category 2; if expensed, Category 1
  (Scope 3 Calculation Guidance, Cat. 1/Cat. 2). Follow your accounting
  policy consistently and disclose it. Never count a purchase in both.
- **Fuels and energy purchased → Category 3** (their upstream/WTT emissions)
  and scopes 1/2 (their combustion/generation). Do not put fuel or electricity
  purchases through Category 1 EEIO factors.
- **Inbound transportation and distribution paid for by the reporting
  company → Category 4.** In principle, freight arranged and paid by the
  *supplier* and embedded in the product price belongs to Category 1
  (it is part of the good's cradle-to-gate footprint, and EEIO purchaser-price
  factors already include margins on trade and transport). The **practical
  convention** many programs adopt is: freight the reporter procures directly
  (own freight contracts, 3PL invoices) → Category 4; everything embedded in
  the goods price → stays in Category 1 via the product/spend factor.
  Whichever split you use, **disclose it and apply it consistently** so
  nothing is counted twice or dropped.
- Emissions from **using** purchased goods in your own operations (e.g.,
  burning purchased fuel, operating purchased equipment) → scopes 1/2.
- Purchases by franchisees, investees, or leased-asset operators outside your
  organizational boundary → Categories 14, 15, 13 respectively.

**Overlap resolution rules:**
1. Sort every AP line into exactly one of: Cat 1, Cat 2 (capitalized),
   Cat 3 (fuels/energy), Cat 4 (reporter-paid freight), Cat 5–8, or
   scope 1/2 pass-through. A category-coded chart-of-accounts mapping is the
   control that prevents double counting.
2. If a supplier gives you a cradle-to-*grave* PCF, strip downstream stages —
   Category 1 takes cradle-to-gate only.
3. Intra-company transfers within the organizational boundary are not
   purchases — exclude them (they'd double count your own scopes 1/2).

## Method ladder

The Scope 3 Calculation Guidance (Category 1) names four methods, most to
least data-intensive:

| # | Method | Activity data | Emission factor | Typical use |
|---|---|---|---|---|
| 1 | Supplier-specific | Quantities purchased per supplier/product | Supplier-provided cradle-to-gate PCF, or allocated supplier scope 1+2 (+ upstream) | Top suppliers, engaged supply chains |
| 2 | Hybrid | Mix: supplier scope 1+2 allocation + secondary data for missing upstream stages | Combination | Suppliers reporting corporate but not product data |
| 3 | Average-data | Physical quantities (kg, units, m², liters) | Published cradle-to-gate factors per unit (ecoinvent, DEFRA materials, EPDs, sector averages) | Material-intensive purchases with mass data |
| 4 | Spend-based | Procurement spend by commodity | EEIO $-intensity factors (USEEIO, EXIOBASE) | Screening, long-tail spend, services |

Standard workflow per the `ghg-protocol` skill §3: spend-based screening of
100% of procurement first, then refine the largest contributors up the ladder.
Disclose the tier mix — a Category 1 total is almost always hybrid in practice.

### Method 1 — Supplier-specific

**When:** supplier provides a product carbon footprint (PCF, ideally
ISO 14067 / GHG Protocol Product Standard conformant, cradle-to-gate), or
corporate scope 1+2 (+ relevant scope 3) data you can allocate.

**Formulas:**

```
Emissions = Σ_products ( quantity_purchased × PCF_cradle-to-gate )

# Allocation from supplier corporate data (physical allocation preferred):
Allocated emissions = supplier (scope 1 + scope 2 [+ material upstream scope 3])
                      × ( reporter purchases from supplier ÷ supplier total production )

# where the ratio is in physical units (units, kg) if available,
# else economic: reporter spend with supplier ÷ supplier total revenue
```

**Method walk-through (revenue allocation):**
1. Obtain the supplier's reported scope 1 and scope 2 (and, if available,
   Category-1-relevant upstream scope 3) for the period matching your
   purchases, plus total revenue or production volume and the GWP set used.
2. Allocation share = your spend with the supplier ÷ supplier total revenue
   (prefer physical units purchased ÷ units produced when available).
3. Allocated emissions = supplier (scope 1 + scope 2) × allocation share.

Note this covers only the supplier's scope 1+2 (their "gate-to-gate") — the
supplier's own upstream (their Category 1, etc.) is missing. Either request
the supplier's relevant upstream scope 3, or top it up with secondary data
(→ hybrid method). State the GWP set the supplier used and harmonize.

**Pitfalls:** revenue allocation distorts when the supplier sells
heterogeneous products at different margins/intensities (prefer physical
allocation, Scope 3 Standard ch. 8); un-verified supplier data (score it per
the data-quality rubric); PCFs with inconsistent boundaries (biogenic
treatment, GWP set, cutoff rules); currency/period mismatch between your
purchases and the supplier's reporting year.

### Method 2 — Hybrid

**When:** supplier gives scope 1+2 allocation or partial PCF, but upstream
stages (their materials, inbound transport) are unquantified.

```
Emissions = allocated supplier scope 1+2
          + Σ ( material inputs × cradle-to-gate material EFs )     # secondary
          + Σ ( upstream transport t-km × mode EF )                 # secondary
          [+ waste in supplier ops × waste EFs]
```

**Method walk-through:** take the supplier's allocated scope 1+2 (per Method 1);
add the bill-of-materials masses for your units multiplied by current
cradle-to-gate material factors (ecoinvent or sector-association sources,
version and geography documented per line); add known inbound transport legs
at current mode factors. Ask the supplier exactly what its allocation already
includes before topping up.

**Pitfalls:** double counting when the supplier's allocation already includes
some upstream (ask exactly what's in it); gap between BOM mass and purchased
mass (yield loss/scrap belongs in the footprint).

### Method 3 — Average-data (physical)

**When:** you know physical quantities purchased (mass, units, area) but have
no supplier data. The workhorse for materials-heavy procurement.

```
Emissions = Σ_i ( mass_i or units_i × cradle-to-gate EF_i )
```

EF sources: ecoinvent (specify version, dataset, geography, system model —
e.g., cutoff vs. APOS), DEFRA/DESNZ "material use" factors (annual UK tables),
EPDs, sector-association averages (worldsteel, PlasticsEurope, International
Aluminium Institute).

**Method walk-through:** pull purchased masses by material from procurement
quantity data; for each material select the current-year cradle-to-gate
factor whose geography and production route match your supply; multiply and
sum, documenting source, version, and dataset per line.

**Pitfalls:** picking a global-average factor when your supply is regionally
specific (primary aluminum varies severalfold between hydro-based and
coal-grid smelting); using a *recycled-content* factor without evidence of
recycled content; DEFRA material factors are primary-production based and
UK-oriented — check applicability; factor boundary (some "material" factors
exclude fabrication into the purchased form).

### Method 4 — Spend-based (EEIO)

**When:** only financial data exists — screening, services, and the long
spend tail.

```
Emissions = Σ_c ( spend_c,adjusted × EEIO EF_c )

spend_adjusted = nominal spend ÷ inflation index (factor ref year → spend year)
              [× FX conversion to factor currency, same year]
```

EF sources:
- **USEEIO / EPA Supply Chain GHG Emission Factors for US Industries and
  Commodities** (kg CO2e per USD of a stated dollar-year, **purchaser price**,
  by NAICS-aligned commodity; "with margins" factors include trade/transport
  margins — verify the current release on EPA's page).
- **EXIOBASE** (multi-regional IO, 44 countries + 5 RoW regions, ~200
  products; EUR basis; use for non-US spend or import-adjusted intensities).
- DEFRA table 13 indirect factors are legacy (discontinued) — do not use for
  new work.

**Adjustments required:**
1. **Inflation-adjust** spend to the factor's dollar-year using a producer
   price or GDP deflator index (recent-year spend against older-dollar
   factors overstates emissions if unadjusted).
2. **Currency-convert** at the factor year's average rate when spend is
   non-USD against USEEIO (or prefer EXIOBASE for that geography).
3. **Deduplicate**: strip taxes (VAT/sales tax), intra-company transfers,
   capital purchases (→ Cat 2), fuels/energy (→ Cat 3/scopes 1–2),
   reporter-paid freight (→ Cat 4), and pure financial flows (debt service,
   dividends) before applying factors.
4. **Price basis**: match purchaser-price factors to what you actually paid;
   producer-price factors need margin handling (see Unit traps).

**Method walk-through:** extract spend by NAICS-mapped commodity from the AP
cube; deflate each line to the factor's dollar-year with a PPI/deflator
index; currency-convert if needed at the factor-year average rate; multiply
by the current-release USEEIO purchaser-price factor for that commodity; sum
and record the release, dollar-year, and index used.

**Pitfalls:** EEIO factors are economy-average — they cannot reflect supplier
improvements (a supplier decarbonizing shows zero change under spend-based);
miscoded commodities (mapping "software licenses" to "computer manufacturing"
can be several-fold off); negative spend lines (credits/rebates) need
netting, not factor application; discounts mean spend understates physical
flow.

## Emission factor sources

| Source | Governing table | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| EPA Supply Chain GHG Emission Factors (USEEIO-based) | Commodity factor file, current release | US economy, NAICS-aligned commodities (spend-based) | kg CO2e per USD of a stated dollar-year; purchaser price; with/without-margins variants | Updated with USEEIO releases — verify current |
| EXIOBASE 3 | MRIO product intensities | 44 countries + 5 RoW regions, ~200 products | kg CO2e per EUR, basic prices | Periodic releases |
| ecoinvent | Material/process datasets | Global; geography- and system-model-specific (cutoff vs. APOS) | kg CO2e per kg or unit, cradle-to-gate | Versioned releases — state version |
| DEFRA/DESNZ UK GHG Conversion Factors | "Material use" tables | UK-oriented, primary-production basis | kg CO2e per tonne | Annual |
| Sector associations (worldsteel, IAI, PlasticsEurope, GCCA) | Sector LCI/average reports | Global/regional material averages | kg CO2e per tonne of material | Multi-year updates |
| EPDs / supplier PCFs (PACT, Catena-X) | Program-specific declarations | Product-specific, cradle-to-gate | Per declared unit | Per publication; check validity window |

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **Nominal vs. real dollars:** EEIO factors are denominated in a specific
  base-year currency. Always deflate/inflate spend to that year; skipping this
  typically inflates emissions by cumulative inflation since the factor year.
- **Purchaser vs. producer price basis:** USEEIO publishes both. Purchaser
  price (what you paid, incl. wholesale/retail/transport margins) matches AP
  data; producer-price factors applied to purchaser-price spend overstate by
  spreading margins wrongly. State the basis.
- **kg vs. tonne:** factor tables mix kg CO2e/kg, kg CO2e/$, and t CO2e/t.
  A 1,000× error from kg/t confusion is the single most common Category 1 bug.
- **Boundary of "cradle-to-gate":** confirm whether a PCF/factor includes
  packaging, inbound transport to the supplier's gate, and biogenic carbon
  treatment; harmonize before summing.
- **GWP set:** supplier PCFs may use AR4/AR5/AR6 — restate to your inventory's
  set where gas-level detail allows; otherwise disclose the mix
  (`ghg-protocol` §4).
- **VAT/sales tax:** remove from spend before EEIO; IO tables are basic/
  purchaser prices excluding deductible taxes conventions — mixing bases
  skews results.

## Data collection & gap-filling

1. **Extract the full AP/spend cube** for the reporting year: supplier, GL
   account, cost center, amount, currency, date. Target 100% of P&L cost of
   goods + opex procurement (reconcile totals to the P&L — see QA).
2. **Categorize to a commodity taxonomy**: map GL accounts/UNSPSC/internal
   procurement categories to NAICS (for USEEIO) or EXIOBASE products. Keep the
   mapping table under version control; it drives everything.
3. **Segment by materiality**: rank suppliers/categories by spend and by
   screened emissions (they differ — carbon-intense commodities rise). Refine
   the **top N suppliers** (commonly those covering 60–80% of screened
   Category 1 emissions) with supplier-specific or average-data methods; leave
   the tail spend-based.
4. **Supplier engagement**: CDP Supply Chain is the dominant channel for
   corporate-level supplier data; PACT/Catena-X PCF exchange for
   product-level. Request: scope 1, scope 2 (both methods), revenue or
   production volume, allocation basis, GWP set, verification status.
5. **Gap-filling**: missing months → pro-rata extrapolation; unmapped spend →
   apply a conservative weighted-average factor and flag; supplier
   non-response → fall back down the ladder, never to zero. Flag all filled
   values distinctly (`ghg-protocol` §8).

## QA checks

- **Category share reasonableness:** Category 1 is typically the largest
  scope 3 category — often 40%+ of a full corporate footprint for
  manufacturers/retailers, and frequently >70% of scope 3 for services firms.
  A small Category 1 with big procurement is a red flag (coverage gap or
  unit error).
- **Spend coverage completeness:** Σ(spend put through methods) vs. P&L total
  operating costs + COGS, minus payroll, depreciation (→ Cat 2 logic), taxes,
  and financial items. Explain every excluded dollar.
- **Double-count scans:** no supplier/GL line appears in both Cat 1 and Cat 2
  (check capitalization flags); freight suppliers don't appear in both Cat 1
  and Cat 4; fuel/energy vendors excluded (→ Cat 3, scopes 1–2).
- **Factor-basis consistency:** one dollar-year per EEIO run; one GWP set;
  purchaser-price basis throughout; documented factor citations per line.
- **Intensity sanity:** implied kg CO2e/$ of total Category 1 should fall
  within the plausible range of the underlying commodity mix — pure services
  at the low end, heavy-materials procurement an order of magnitude or more
  higher.
- **Year-over-year deltas** decomposed into volume, mix, method, and factor
  effects before publication.

## Worked FAQ

**Q1. We spent €4.2M on packaging in 2025. How do we screen it?**
Spend-based method: convert to USD at the factor-year average rate, deflate
to the USEEIO factor's dollar-year, map the spend to the packaging commodity
(e.g., paperboard container manufacturing), and multiply by the
current-release EPA Supply Chain purchaser-price factor. Screening tier only —
refine with tonnages (average-data method) if material.

**Q2. Supplier reports scope 1+2 and revenue; we know our spend with them.
What's our allocation, and is it complete?**
Allocated emissions = supplier (scope 1 + scope 2) × (your spend ÷ supplier
revenue), preferring physical allocation when unit data exists. Not
complete — it omits the supplier's own upstream. Either obtain their
Cat-1-relevant scope 3 or top up with the hybrid method; disclose the
boundary either way.

**Q3. We bought 250 t of PET resin. How do we estimate it?**
Average-data method: mass × the current cradle-to-gate PET factor
(ecoinvent/PlasticsEurope, matching grade and geography). If your resin is
rPET, use a recycled-content factor only with supplier evidence, and note the
allocation method it embeds.

**Q4. Our supplier paid the ocean freight and billed it in the unit price.
Category 1 or 4?**
In principle Category 1 (it's inside the good's cradle-to-gate price and the
purchaser-price EEIO factor already includes transport margins). Category 4
covers freight *you* purchase. If you separately model supplier-paid inbound
freight in Cat 4 (a common practical convention when lanes are known),
disclose that and ensure the Cat 1 method doesn't also include it.

**Q5. A supplier decarbonized 30% but our spend-based number didn't move. Why?**
EEIO factors are economy averages — they respond to your spend, not supplier
performance. Move that supplier to Method 1 (supplier-specific) to capture
the reduction; disclose the method change.

**Q6. Should software SaaS subscriptions be in Category 1?**
Yes — purchased services are in the minimum boundary. Use spend-based with
the data-processing/software-publishing commodity factor from the current
EPA Supply Chain release, or the vendor's customer-allocated footprint if
published (several hyperscalers provide these).

## References

- GHG Protocol Corporate Value Chain (Scope 3) Accounting and Reporting
  Standard (WRI/WBCSD, 2011) — ch. 5 (boundary, Table 5.4), ch. 7 (data),
  ch. 8 (allocation).
- Technical Guidance for Calculating Scope 3 Emissions v1.0 (2013) —
  Category 1 chapter (method definitions, decision tree, formulas).
- EPA Supply Chain GHG Emission Factors for US Industries and Commodities
  (USEEIO-based; verify current release and dollar-year).
- EXIOBASE 3 (MRIO database) — for non-US spend.
- ecoinvent (current version; note system model), DEFRA/DESNZ UK Government
  GHG Conversion Factors (annual; "material use" tables), sector averages
  (worldsteel, IAI, PlasticsEurope), EPD programs.
- CDP Supply Chain program; PACT Pathfinder Framework (PCF exchange).
- Cross-cutting conventions: the `ghg-protocol` skill.
