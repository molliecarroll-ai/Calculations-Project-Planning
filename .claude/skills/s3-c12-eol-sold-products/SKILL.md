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

**Worked example — packaged beverage producer.** Sold in the US market:
20,000 t PET bottles, 5,000 t aluminum cans, 8,000 t corrugated secondary
packaging. US disposal mix (EPA Facts & Figures, 2018 data — verify
current): PET ~29% recycled / ~17% combusted / ~54% landfilled; aluminum
cans ~50% recycled / ~12% combusted / ~38% landfilled; corrugated ~90%+
recycled / remainder split.

Illustrative EFs (DEFRA 2024 waste-disposal factors, kgCO2e/t — verify
current edition; DEFRA's landfill factors embed UK gas-capture rates,
US landfills differ — disclose if applying to US mix):
PET landfill ≈ 9 (inert, near-zero decay); PET incineration ≈ 2,290 stoich.
fossil CO2 if counting combustion at the EfW plant (note: DEFRA's own EfW
convention allocates combustion CO2 to the energy generated and reports
~21 kgCO2e/t "combustion" for the waste generator — state which convention
you follow; the conservative product-footprint treatment counts the fossil
CO2); recycling ≈ 21 (collection only, cut-off); aluminum landfill ≈ 9
(inert), recycling ≈ 21; corrugated landfill ≈ 1,000 (biogenic CH4,
material-specific — verify), recycling ≈ 21, incineration (biogenic CO2
outside scopes; CH4/N2O small).

Using the conservative EfW convention for plastics:

```text
PET:  20,000 × (0.54×0.009 + 0.17×2.29 + 0.29×0.021) = 20,000 × 0.400 = 8,006 tCO2e
Alu:   5,000 × (0.38×0.009 + 0.12×0.021 + 0.50×0.021) = 5,000 × 0.0164 =    82 tCO2e
Corr:  8,000 × (0.05×1.00  + 0.03×0.021 + 0.92×0.021) = 8,000 × 0.0700 =   560 tCO2e
C12 ≈ 8,650 tCO2e   (+ biogenic CO2 memo from corrugated combustion/decay)
```

**Pitfalls:** (a) mixing the DEFRA "generator" convention (EfW CO2 allocated
to energy user, ~21 kg/t) with stoichiometric fossil-CO2 EfW factors —
results differ ~100×, pick one and disclose; (b) applying UK
landfill-gas-capture-adjusted factors to markets with low capture;
(c) forgetting packaging mass entirely; (d) treating "recycled" share with a
zero factor *and* crediting avoided virgin material (double benefit).

### 2. Average-data (mixed waste) method

**When:** screening or immaterial category. Total sold mass × one mixed-MSW
factor:

```text
C12 = total mass of products + packaging sold (t) × mixed-MSW disposal EF (tCO2e/t)
```

E.g., DEFRA 2024 "municipal waste to landfill" ≈ 446 kgCO2e/t (verify).
A 100,000 t sales mass → `100,000 × 0.446 = 44,600 tCO2e` upper-bound-style
screen. Pitfall: wildly wrong material mix (inert-heavy products overstated,
food/paper-heavy understated) — use only to decide whether tier 1 effort is
warranted.

## Emission factors / parameters quick reference

Representative values; **verify against the named current edition** and
record source/year/units. All kgCO2e per metric tonne of material.

| Material | Landfill | Incineration/EfW | Recycling (cut-off) | Compost | Source + vintage |
|---|---|---|---|---|---|
| Mixed MSW | ~446 | see convention note | ~21 | — | DEFRA 2024 waste factors |
| Food waste | ~630 | ~21 (DEFRA conv.) | — | ~9–10 | DEFRA 2024 |
| Paper & board | ~1,000 (CH4-driven) | biogenic CO2 (memo) + minor CH4/N2O | ~21 | — | DEFRA 2024 (verify exact) |
| Plastics (avg) | ~9 (inert) | ~2,300–3,100 fossil CO2 stoich. (PET 2,290; HDPE ~3,140) or ~21 under DEFRA generator convention | ~21 | — | Stoichiometry / DEFRA 2024 — state convention |
| Glass | ~9 (inert) | — | ~21 | — | DEFRA 2024 |
| Metals (steel/alu) | ~9 (inert) | — | ~21 | — | DEFRA 2024 |
| Textiles (synthetic) | low decay | fossil CO2 by fiber | ~21 | — | DEFRA 2024 / stoichiometry |
| Wood | ~800–830 (CH4) | biogenic CO2 (memo) | ~21 | — | DEFRA 2024 (verify) |

**Disposal-mix reference points (verify current):** US MSW overall (EPA
Facts & Figures, 2018 data): ~50% landfill, ~12% combustion w/ energy
recovery, ~24% recycled, ~9% composted. EU varies widely by member state
(Eurostat: DE/NL/SE near-zero landfill, high EfW+recycling; some member
states >50% landfill) — never apply a single "EU average" to
country-concentrated sales without disclosure.

## Unit and conversion traps

- **Sold-in-year, full EOL fate:** like category 11, account the eventual EOL of *this year's* sales cohort now — not the tonnage of your products discarded by consumers this year.
- **Product mass vs. packaging mass:** both are in scope; BOM mass excludes packaging — add packaging specs separately. Watch net vs. gross shipping mass and per-unit vs. per-case packaging.
- **Percent conventions:** disposal mixes published as % of *generation* vs. % of *discards after recycling* — EPA reports both; mixing bases misallocates 20–30 points.
- **Biogenic split:** landfill CH4 in-scope; biogenic decomposition/combustion CO2 outside the scopes as memo (`ghg-protocol` skill §5). Do not zero-out paper landfill because "it's biogenic" — the CH4 is the point.
- **EfW conventions:** stoichiometric fossil CO2 at the plant vs. DEFRA's allocate-to-energy-user convention (~21 kg/t) differ by orders of magnitude for plastics. State the convention; be consistent YoY.
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

**Q1. We sell 3,000 t of food products (plus 400 t plastic film, 600 t
board packaging) in the UK. Estimate C12.**
Note: food *consumed* is not waste; assume 15% household food waste share
(WRAP data — verify): 450 t food waste. UK mix (DEFRA/WRAP, verify): food →
~40% landfill-equivalent residual, 60% collected organics; film → residual
(mostly EfW in UK); board → 80% recycled.
Food: `450 × (0.40×0.63 + 0.60×0.010) ≈ 116 t`.
Film (DEFRA generator convention): `400 × 0.021 ≈ 8 t` (or `400 × ~2.5 =
1,000 t` counting stoichiometric fossil CO2 — convention choice, disclose).
Board: `600 × (0.80×0.021 + 0.20×1.00) ≈ 130 t`.
Total ≈ **254 tCO2e** (generator convention) — plus biogenic memo.

**Q2. Are avoided emissions from our recyclable packaging a credit here?**
No. Category 12 reports gross treatment emissions; avoided-burden credits
are not netted into scope 3 totals. You may discuss avoided emissions
separately outside the inventory, clearly labeled.

**Q3. Our electronics contain 2,000 t mixed WEEE sold into the EU. Approach?**
Use Eurostat WEEE collection/treatment rates (~45–55% formally collected —
verify current): formally treated share → recycling/collection factors
(~21 kg/t) plus specific treatment of hazardous fractions; uncollected share
→ mixed-MSW fate of the destination market. `2,000 × (0.5×0.021 + 0.5×0.30)
≈ 321 tCO2e` illustrative; refine with WEEE-scheme data. Refrigerant in the
WEEE goes to category 11's lifetime-release term, not here.

**Q4. Does compostable packaging zero out our C12 for that mass?**
No. Composting has a small factor (~9–10 kgCO2e/t, DEFRA 2024 — verify) and
only for the share that actually reaches composting; certified-compostable
material landfilled still generates CH4. Weight by the real market's organics
capture rate.

**Q5. We sell industrial pumps (steel-dominated, 25-yr life). Is C12
material?**
Rarely: metals are inert in landfill and mostly recycled — `1,000 t ×
(0.85×0.021 + 0.15×0.009) ≈ 19 tCO2e` per 1,000 t sold. Screen, report the
small number or justify exclusion with the screen documented.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5, Table 5.4 (category 12 minimum boundary; packaging inclusion).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 12 chapter (waste-type-specific method; reuse of category 5 methodology; disposal-mix assumptions; recycling allocation discussion).
- Data sources: US EPA *Advancing Sustainable Materials Management: Facts and Figures* (latest data year — verify); Eurostat waste and packaging-waste statistics (annual); UK DESNZ/DEFRA GHG conversion factors, waste tables (annual); EPA WARM model; IPCC 2006 Guidelines vol. 5 (SWDS first-order decay, incineration).
- Cross-cutting rules: the `ghg-protocol` skill (§4 GWPs, §5 biogenic, §7 EF hierarchy, §8 data quality).
