---
name: s3-c12-eol-sold-products
description: >-
  Scope 3 Category 12 — End-of-Life Treatment of Sold Products. Use for
  questions about end of life, product disposal, packaging disposal, what
  happens to sold products and their packaging when consumers discard them:
  landfill, incineration/energy-from-waste, recycling, composting by material.
  Covers the waste-type-specific method (mirroring category 5 factor logic),
  disposal-mix assumptions by market (EPA Facts and Figures, Eurostat),
  recycling allocation, and packaging mass modeling.
---

# Scope 3 Category 12 — End-of-Life Treatment of Sold Products

**Definition (Scope 3 Standard, ch. 5, category 12):** emissions from the
**waste disposal and treatment of products sold by the reporting company in
the reporting year, at the end of their life**. Includes the total expected
end-of-life (EOL) emissions of all products sold in the reporting year —
same sold-in-year, full-fate convention as category 11 — and covers both the
**products themselves and their packaging**.

Governing documents:
- Scope 3 Standard (2011), ch. 5 (definition, minimum boundary, Table 5.4).
- Scope 3 Calculation Guidance (2013), **category 12 chapter** — which explicitly reuses the category 5 (waste) methodology applied to sold products.
- Cross-cutting conventions (GWP set, biogenic CO2, EF hierarchy, data quality): the `ghg-protocol` skill.

The methodology deliberately **mirrors category 5** (waste generated in
operations): mass of material × treatment pathway × treatment-specific
emission factor. What changes is whose waste it is (your customers'), when
it arises (years after sale), and that you must **assume** the disposal mix
because you do not control it.

## Boundary & classification

**In scope (minimum boundary):** scope 1 and scope 2 emissions of waste
management companies that occur during disposal/treatment of sold products
and their packaging: landfill (CH4 from anaerobic decomposition of
degradable materials), incineration / energy-from-waste (fossil CO2 from
plastics and synthetic materials, N2O), treatment steps of recycling and
composting as allocated (below). Packaging that departs with the product
(primary, secondary, and shipped tertiary packaging) is part of the sold
product for this category.

**Out of scope / routed elsewhere:**
- Waste generated in **your own operations** (manufacturing scrap, returned goods you discard) → category 5.
- **Use-phase** emissions → category 11; EOL **release of contained GHGs** (refrigerant venting at scrappage) is conventionally captured in the category 11 GHG-containing-product lifetime-release fraction — put it in exactly one place and disclose which (see `s3-c11-use-of-sold-products`).
- Transport of discarded products to treatment: collection transport is minor and typically embedded in treatment EFs (e.g., DEFRA factors); disclose if separately modeled.
- **Intermediate products:** the EOL of the *final* products your intermediates end up in is, strictly, downstream of category 10 processing; the Guidance expects sellers of intermediates to estimate EOL of the eventual final products where feasible, with disclosed assumptions, or treat mass-conservatively as the intermediate material itself.
- Biogenic CO2 from decomposition/combustion of biomass-based materials (paper decay CO2 share, wood incineration CO2) → outside the scopes, memo item; landfill **CH4** from those same materials stays **in** (`ghg-protocol` skill §5).

**Recycling allocation (state your convention).** The Guidance leaves
recycling allocation open; the dominant convention (aligned with the
recycled-content / cut-off approach) is:
- Category 12 carries the emissions of collection/sorting and **preparation for recycling attributable to the discarded product**, or — simpler and most common with DEFRA-style factors — a small "recycling" factor covering collection only.
- The **avoided virgin-material burden is NOT credited** — no negative numbers in category 12. Recycled-material benefits show up in the *next* buyer's category 1 (lower recycled-content factor).
- Do not count the recycler's reprocessing energy in your category 12 *and* let the recyclate buyer count it in their category 1 under recycled-content — pick the cut-off convention and disclose.

## Method ladder

| Tier | Method (Calc. Guidance, cat. 12) | Data basis | Typical use |
|---|---|---|---|
| 1 | **Waste-type-specific method** | Product/packaging mass by material × market disposal mix × treatment EF per material-pathway | Standard method; almost always feasible from BOM data |
| 2 | Average product/waste method | Total sold mass × average mixed-waste EF | Screening only; single mixed-MSW factor |

(Take-back-program measured data — actual collected tonnage and treatment —
upgrades the disposal-mix assumption to tier-1-quality inputs for the
covered share.)

### 1. Waste-type-specific method

**When:** always preferred. Requires only bill-of-materials and packaging
specs plus published waste statistics.

**Data required:** (a) mass of sold products + packaging by **material**
(plastic by resin if possible, paper/board, glass, steel, aluminum, food,
textiles, wood, mixed electronics); (b) **disposal mix** per material per
sales market (% landfill / incineration / recycling / compost); (c)
treatment EF per material × pathway.

```text
C12 = Σ_materials Σ_pathways [ mass sold (t) × pathway share_(material, market) (%)
                               × EF_(material, pathway) (tCO2e/t) ]
```

**Disposal-mix sources (disclose source + year):** US — EPA *Advancing
Sustainable Materials Management: Facts and Figures* (latest data year 2018,
with periodic updates — verify); EU — **Eurostat** waste statistics
(env_wasmun, packaging waste env_waspac, annual); national agencies
elsewhere (e.g., UK DEFRA statistics, Japan MOE). Where no data: use the
nearest comparable market and disclose.

**EF sources:** UK DESNZ/DEFRA conversion factors "Waste disposal" tables
(annual — most practical, material × pathway grid); EPA WARM model (US,
includes/excludes offsets — use with care, strip out avoided-emission
credits for GHG Protocol reporting); IPCC 2006 GL vol. 5 (first-order decay
landfill CH4, incineration) for first-principles work.

**Method walk-through — packaged goods.** Symbolic:

```text
1. m_(material) = mass sold per material   ← BOM × units sold, plus packaging
                  specifications (EPR filings are an audit-ready mass source)
2. share_(material, pathway, market)       ← EPA Facts & Figures (US) /
                  Eurostat (EU) / national statistics, year-stamped,
                  weighted by sales-market mix
3. EF_(material, pathway)                  ← DEFRA waste-disposal tables
                  (current edition), WARM, or IPCC — state the EfW convention
4. C12 = Σ_materials Σ_pathways m × share × EF
   (landfill CH4 in scope; biogenic CO2 reported as a memo item)
```

**The energy-from-waste convention choice (state it).** For fossil-carbon
materials (plastics, synthetic textiles) two defensible conventions exist:
count the stoichiometric fossil CO2 released at the EfW plant against the
discarded product, or follow DEFRA's generator convention, which allocates
combustion CO2 to the energy user and leaves the waste generator only a
small collection-level factor. For plastics the two differ by orders of
magnitude — pick one, apply it consistently YoY, and disclose. Note also
that landfill factors embed a gas-capture assumption (DEFRA's reflect UK
capture rates); applying them to low-capture markets requires disclosure.

**Pitfalls:** (a) mixing the DEFRA generator convention with stoichiometric
fossil-CO2 EfW factors — results differ by orders of magnitude for
plastics, pick one and disclose; (b) applying UK
landfill-gas-capture-adjusted factors to markets with low capture;
(c) forgetting packaging mass entirely; (d) treating "recycled" share with a
zero factor *and* crediting avoided virgin material (double benefit).

### 2. Average-data (mixed waste) method

**When:** screening or immaterial category. Total sold mass × one mixed-MSW
factor:

```text
C12 = total mass of products + packaging sold (t) × mixed-MSW disposal EF (tCO2e/t)
```

Use the mixed-MSW landfill factor from the current DEFRA waste tables as an
upper-bound-style screen. Pitfall: the implied material mix can be wildly
wrong (inert-heavy products overstated, food/paper-heavy understated) — use
only to decide whether tier 1 effort is warranted.

## Emission factor and parameter sources

Record source, edition/vintage, and units for every input per the
`ghg-protocol` skill §7.

| Source | Governing table / dataset | Coverage | Units convention | Cadence |
|---|---|---|---|---|
| UK DESNZ/DEFRA conversion factors | "Waste disposal" tables | Material × pathway EFs (landfill, EfW under the generator convention, recycling/collection, composting) | kgCO2e per metric tonne | Annual |
| EPA WARM model | Material-pathway factors | US materials; embeds avoided-emission credits — strip them for GHG Protocol reporting | per US short ton | Periodic versions |
| IPCC 2006 GL vol. 5 | First-order-decay landfill CH4; incineration | First-principles modeling; stoichiometric fossil CO2 for plastics EfW | per Gg / per tonne | Static |
| EPA *Advancing Sustainable Materials Management: Facts and Figures* | Generation and management (recycled/combusted/landfilled/composted) by material | US disposal mixes | % shares, short-ton basis | Periodic data years |
| Eurostat waste statistics (env_wasmun; env_waspac) | Municipal and packaging-waste treatment | EU member-state disposal mixes | % shares, metric tonnes | Annual |
| WRAP; national agencies (UK DEFRA statistics, Japan MOE) | Market-specific mixes; household food-waste shares | UK and other markets | % shares | Periodic |

Disposal mixes vary enormously by market (some EU member states landfill
almost nothing; others most of their MSW) — never apply a single regional
average to country-concentrated sales without disclosure.

This skill intentionally quotes no factor values. When a quantitative
answer is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **Sold-in-year, full EOL fate:** like category 11, account the eventual EOL of *this year's* sales cohort now — not the tonnage of your products discarded by consumers this year.
- **Product mass vs. packaging mass:** both are in scope; BOM mass excludes packaging — add packaging specs separately. Watch net vs. gross shipping mass and per-unit vs. per-case packaging.
- **Percent conventions:** disposal mixes published as % of *generation* vs. % of *discards after recycling* — EPA reports both; mixing bases misallocates 20–30 points.
- **Biogenic split:** landfill CH4 in-scope; biogenic decomposition/combustion CO2 outside the scopes as memo (`ghg-protocol` skill §5). Do not zero-out paper landfill because "it's biogenic" — the CH4 is the point.
- **EfW conventions:** stoichiometric fossil CO2 at the plant vs. DEFRA's allocate-to-energy-user convention differ by orders of magnitude for plastics. State the convention; be consistent YoY.
- **Landfill gas capture:** factors embed a capture assumption (UK ~ high capture; many markets ~0%) — geographic mismatch materially biases CH4-heavy materials.
- **kg vs. t and short ton vs. tonne:** EPA data in US short tons (0.907 t); DEFRA per metric tonne.

## Data collection & gap-filling

- **Bill of materials by SKU** × units sold = product material masses; packaging specifications (often held by packaging engineering or EPR compliance teams — EPR filings are an excellent, audit-ready mass source).
- **Sales by market** to weight disposal mixes: country-level splits from Eurostat/EPA/national statistics, year-stamped.
- **Take-back and EPR program data:** actual collected tonnage and verified treatment routes replace assumed mixes for the covered share; blend with assumptions for the remainder and disclose the split.
- **Gap-filling:** unknown material composition → nearest analog SKU or conservative material assignment (assign ambiguous plastics to the highest-EF pathway mix); unknown market split → revenue-share allocation, flagged per the `ghg-protocol` skill §8.
- Durable goods: disposal mix should reflect the **expected mix at EOL** (a decade out); the standard convention uses current-year statistics — an optional scenario refinement (e.g., legislated landfill phase-outs) may be applied with disclosure, mirroring the category 11 grid-trajectory logic.

## QA checks

- **Mass balance:** Σ material masses across pathways = total sold product + packaging mass; pathway shares per material sum to 100%.
- **Materiality shape:** for most manufacturers category 12 is small relative to categories 1 and 11 — a category 12 rivaling category 1 usually means an EfW-convention or short-ton error, unless products are food/paper-heavy.
- **Convention consistency:** one recycling allocation convention, one EfW convention, disclosed, stable YoY.
- **Biogenic memo present** when paper/wood/food mass is material.
- **No 11/12 double count** of contained-GHG EOL release (refrigerants counted once).
- **Disposal-mix vintage:** source year recorded; refreshed on a set cycle; changes disclosed.

## Worked FAQ

**Q1. We sell food products with plastic film and board packaging in the
UK. How do we structure C12?**
Three material streams, each mass × mix × factor. Food: only the *wasted*
share is waste — apply a household food-waste share from WRAP (a sourced
statistic, not a guess), then the UK organics-vs-residual split. Film: a
residual stream (mostly EfW in the UK) — the EfW convention choice drives
this term by orders of magnitude, so state it. Board: mostly recycled
(collection-level factor), with the landfilled remainder carrying biogenic
CH4 in scope. Factors from the current DEFRA waste tables; biogenic CO2 as
a memo item.

**Q2. Are avoided emissions from our recyclable packaging a credit here?**
No. Category 12 reports gross treatment emissions; avoided-burden credits
are not netted into scope 3 totals. You may discuss avoided emissions
separately outside the inventory, clearly labeled.

**Q3. Our electronics ship as mixed WEEE into the EU. Approach?**
Split the sold mass into formally collected vs. uncollected using Eurostat
WEEE collection/treatment rates (current year). Formally treated share →
recycling/collection factors plus specific treatment of hazardous
fractions; uncollected share → the destination market's mixed-MSW fate.
Refine with WEEE-scheme data where available. Refrigerant in the WEEE goes
to category 11's lifetime-release term, not here.

**Q4. Does compostable packaging zero out our C12 for that mass?**
No. Composting carries a small but nonzero factor (DEFRA waste tables), and
only for the share that actually reaches composting; certified-compostable
material landfilled still generates CH4. Weight by the real market's
organics-capture rate.

**Q5. We sell industrial pumps (steel-dominated, 25-yr life). Is C12
material?**
Rarely: metals are inert in landfill and predominantly recycled, so the
waste-type-specific method returns a very small figure per tonne sold. Run
the screen with current DEFRA metal factors and the market's metals
recycling rate, then report the small number or document a justified
exclusion with the screen on file.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5, Table 5.4 (category 12 minimum boundary; packaging inclusion).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 12 chapter (waste-type-specific method; reuse of category 5 methodology; disposal-mix assumptions; recycling allocation discussion).
- Data sources: US EPA *Advancing Sustainable Materials Management: Facts and Figures* (latest data year — verify); Eurostat waste and packaging-waste statistics (annual); UK DESNZ/DEFRA GHG conversion factors, waste tables (annual); EPA WARM model; IPCC 2006 Guidelines vol. 5 (SWDS first-order decay, incineration).
- Cross-cutting rules: the `ghg-protocol` skill (§4 GWPs, §5 biogenic, §7 EF hierarchy, §8 data quality).
