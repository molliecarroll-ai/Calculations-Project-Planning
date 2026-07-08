---
name: s3-c10-processing-sold-products
description: >-
  Scope 3 Category 10 — Processing of Sold Products. Use for questions about
  intermediate products sold to third parties, downstream processing emissions,
  tier-1 customer manufacturing of the reporter's outputs, allocation of a
  customer's scope 1/2 to a purchased input, or whether category 10 applies at
  all (final vs. intermediate products, unknown end uses). Covers the
  site-specific and average-data methods, allocation rules, and the
  estimation-vs-justified-exclusion decision when downstream pathways are
  unknown or highly varied.
---

# Scope 3 Category 10 — Processing of Sold Products

**Definition (Scope 3 Standard, ch. 5, category 10):** emissions from the
processing of **intermediate products** sold in the reporting year by
**downstream companies** (e.g., manufacturers) subsequent to sale by the
reporting company and prior to use by the end consumer. Intermediate products
are products that require further processing, transformation, or inclusion in
another product before use. Emissions in scope are the **scope 1 and scope 2
emissions of downstream value chain partners** that occur during processing.

Governing documents:
- Scope 3 Standard (2011), ch. 5 (category descriptions, minimum boundaries, Table 5.4).
- Scope 3 Calculation Guidance (2013), **category 10 chapter** — the method ladder below.
- Cross-cutting conventions (GWP set, EF hierarchy, data quality, base year): see the `ghg-protocol` skill. Do not re-derive those here.

Category 10 only exists for companies that sell intermediate products:
chemicals, resins, steel, aluminum, glass, semiconductors, pulp, yarns and
fabrics, agricultural commodities, refinery feedstocks sold for further
conversion, components and subassemblies. A company selling only finished
consumer products has **no category 10** (its downstream story is categories
9, 11, 12).

## Boundary & classification

**In scope (minimum boundary):** scope 1 and scope 2 emissions of the
downstream entities that process the sold intermediate product — from the
point of sale through all processing steps **until the final product is
produced** (i.e., until no further transformation occurs before use). Where
there are multiple processing tiers (resin → film converter → packaging
printer), the minimum boundary in principle covers the full chain to the
final product; in practice most reporters model the dominant first-tier
processing step and disclose the truncation.

**Out of scope / routed elsewhere:**
- Transport of the sold product from the reporter to the customer → **category 9** (downstream transportation and distribution), not category 10.
- Emissions from the **use** of the final product → **category 11**; from its disposal → **category 12**. Do not fold use-phase energy into category 10.
- Upstream (cradle-to-gate) emissions of the intermediate product itself → already in the reporter's scopes 1/2 and upstream categories; category 10 begins **after the sale**.
- Processing in facilities the reporter owns or controls (tolling at own plants) → scope 1/2, not category 10.
- The customer's purchased-goods emissions other than processing your product (their other inputs) → allocated out; only the share of their scope 1/2 attributable to processing **your** product counts.

**Overlap resolution:**
- **Category 10 vs. category 11 for fuels/feedstocks:** products sold as fuels are category 11 (combustion during use). Products sold as **feedstocks** that are chemically transformed (naphtha to a cracker) are category 10 for the processing energy; carbon embodied in the product that is later released downstream is picked up in the eventual final product's own accounting — state your treatment.
- **Double counting with the customer's inventory** is expected and permitted: your category 10 = their scope 1/2. Scope 3 allows this by design (Scope 3 Standard, ch. 5); never "net" it out.

**Unknown or highly varied end uses.** The Calculation Guidance explicitly
recognizes that sellers of commodity intermediates (e.g., steel coil,
bulk polymers sold via distributors) may not know the eventual products or
processing pathways. Permitted treatments, in order of preference:
1. **Estimate** downstream processing emissions using representative
   pathways and sales-mix assumptions, disclosing the assumptions (e.g.,
   "60% of resin sold to injection molders, 40% to film extrusion, per
   trade-association end-use statistics").
2. **Justify exclusion** of category 10 where emissions cannot be
   reasonably estimated, and disclose the exclusion with justification in
   the inventory report. Exclusion is a disclosure decision, not a default —
   screen first (a spend/tonnage screen using average processing intensities
   is usually feasible).

## Method ladder

| Tier | Method (Calc. Guidance, cat. 10) | Data basis | Typical use |
|---|---|---|---|
| 1 | **Site-specific method** | Customer (processor) scope 1/2 data allocated to your product | Concentrated customer base; large B2B contracts |
| 2 | **Average-data method** | Tonnes of intermediate sold × average processing emissions per tonne (by process type) | Commodity sales, many customers, distributor channels |

There is no spend-based tier defined for this category in the Guidance;
for screening, a sector-average processing intensity applied to sold tonnage
is the low-effort floor.

### 1. Site-specific method

**When:** a small number of customers process most of your sold volume and
will share facility energy or emissions data (or already report CDP data you
can allocate).

**Data required:** customer facility scope 1 + 2 emissions (or fuel and
electricity quantities to compute them); an allocation basis — preferably
**physical** (tonnes of your product processed ÷ total tonnes processed at
the facility), else economic (revenue share). Follow the Scope 3 Standard
ch. 8 allocation hierarchy: physical over economic.

```text
C10_emissions = Σ_customers [ (customer facility S1 + S2 emissions, tCO2e)
                              × allocation_share_of_your_product ]

allocation_share = mass of your intermediate processed at facility (t)
                   ÷ total mass of all inputs processed at facility (t)
```

**EF/parameter sources:** if the customer gives energy, not emissions:
fuel EFs from EPA Hub / DEFRA / IPCC and grid factors per location (see the
`ghg-protocol` skill §7). State whether their scope 2 is location- or
market-based; location-based is the safer default for consistency.

**Worked example.** You sell 12,000 t of aluminum sheet to a customer whose
stamping plant reports 38,000 t CO2e scope 1 + 2 (verified, location-based)
and processes 95,000 t of total metal input per year.

```text
allocation_share = 12,000 t ÷ 95,000 t = 0.1263
C10 = 38,000 tCO2e × 0.1263 = 4,800 tCO2e
```

**Pitfalls:** (a) customers report company-wide, not facility, emissions —
company-wide totals need a second allocation step (facility share of
production) and degrade data quality; (b) allocation by revenue silently
diverges from mass allocation when your product is a high-value minor input;
(c) reporting-year mismatch between the customer's fiscal year and yours —
disclose; (d) counting the customer's full scope 1/2 without allocating out
their other inputs (overstates).

### 2. Average-data method

**When:** many customers, distributor sales, or unknown specific processors —
the normal case for commodity intermediates.

**Data required:** mass (or units) of each intermediate product sold in the
reporting year, by product type and, ideally, by destination market;
an average **processing emission factor** per unit for the downstream
process(es), from LCA databases or industry associations.

```text
C10_emissions = Σ_products [ mass sold (t) × share to pathway_i
                             × processing EF_pathway_i (tCO2e/t processed) ]
```

**EF/parameter sources:** ecoinvent and Sphera/GaBi process datasets (use the
**processing/conversion step only**, not cradle-to-gate of the input);
industry association LCAs (PlasticsEurope conversion-process eco-profiles,
worldsteel downstream fabrication data); academic/LCI literature. Match
geography (grid mix of the processing country dominates electricity-driven
processes).

**Worked example.** A polymer producer sells 50,000 t of PP resin;
end-use statistics say 55% injection molding, 30% film extrusion, 15%
unknown (treated as injection molding, disclosed). Representative conversion
factors (illustrative values on the order of published European conversion
LCIs — verify against current ecoinvent/PlasticsEurope datasets before use):
injection molding ≈ 0.55 tCO2e/t processed; film extrusion ≈ 0.35 tCO2e/t.

```text
Injection (incl. unknown): 50,000 t × 0.70 × 0.55 tCO2e/t = 19,250 tCO2e
Film extrusion:            50,000 t × 0.30 × 0.35 tCO2e/t =  5,250 tCO2e
C10 total = 24,500 tCO2e
```

**Pitfalls:** (a) using a cradle-to-gate factor for the *final* product
minus your product's factor — subtraction of mismatched LCA boundaries is
error-prone; prefer direct conversion-step factors; (b) only modeling one
processing tier when several occur before the final product — disclose the
truncation; (c) double counting mass when a product is sold partly to
processors and partly as final goods — split the sales ledger first.

## Emission factors / parameters quick reference

Representative downstream-processing intensities (all **verify against the
named current source before use**; values shift with grid decarbonization):

| Processing step | Typical intensity | Units | Source + vintage |
|---|---|---|---|
| Plastics injection molding (EU grid) | ~0.4–0.7 | tCO2e / t polymer processed | ecoinvent v3.x "injection moulding" (check current version year) |
| Plastics film extrusion (EU) | ~0.25–0.45 | tCO2e / t | ecoinvent v3.x "extrusion, plastic film" |
| Blow molding | ~0.5–0.9 | tCO2e / t | ecoinvent v3.x |
| Steel cold rolling / stamping | ~0.2–0.4 | tCO2e / t steel | worldsteel LCI (2023 data release; verify) |
| Aluminum sheet forming | ~0.3–0.5 | tCO2e / t | International Aluminium Institute LCI (verify vintage) |
| Textile cut-and-sew (garment assembly) | ~0.3–0.8 | tCO2e / t fabric | LCA literature; highly grid-dependent |
| Semiconductor packaging/assembly | site-specific; no reliable generic | — | request customer data |

Electricity-dominant processes: scale the factor to the processing country's
grid (see `s2-purchased-electricity` and the `ghg-protocol` skill §7 for grid
factor sources — eGRID, IEA, national factors).

## Unit and conversion traps

- **Sold in the reporting year**, not processed in the reporting year: the boundary is products *sold* this year; downstream processing may physically occur next year. Account for all future processing of this year's sales now (consistent with categories 11/12 lifetime logic).
- **Mass basis drift:** sales ledgers in kg, lb, units, or linear meters vs. EFs in tCO2e/t — normalize to metric tonnes; watch net vs. gross (with packaging) mass.
- **Processing-step vs. cradle-to-gate factors:** an ecoinvent "product at converter" dataset includes the input polymer's upstream burden; you need the *conversion step only*. Check the dataset system boundary.
- **Yield/scrap:** 1 t sold ≠ 1 t in final product. If the EF is per tonne of *output*, divide by yield; if per tonne of *input processed*, apply to sold mass directly. State which.
- **Grid vintage:** conversion EFs embed a grid factor from the dataset's reference year; a 2015-vintage EU dataset overstates today's electricity emissions.

## Data collection & gap-filling

- **Sales ledger by SKU/customer/market** is the activity-data backbone: extract tonnes sold per product family and channel.
- **Customer processing data requests:** piggyback on CDP Supply Chain (in reverse — you are their supplier; ask top customers by volume for facility energy per tonne processed) or add a data clause to commercial agreements. Prioritize by tonnage: top ~10 customers often cover >50% of volume.
- **End-use split:** trade associations (PlasticsEurope, worldsteel, CRU, ICIS) publish end-use market statistics; distributor sales can be apportioned by the market-level split. Disclose the source and year.
- **Gap-filling:** unknown pathway share → assign to the highest-intensity plausible pathway (conservative) or the sales-weighted average (representative) — pick one convention, disclose, keep it stable YoY. Flag estimated shares distinctly from customer-confirmed data per the `ghg-protocol` skill §8.
- If estimation is genuinely infeasible (e.g., commodity traded on exchanges with unknowable destinations), document the screening attempt and record a **justified exclusion** in the inventory report.

## QA checks

- **Applicability check:** every product line classified final vs. intermediate; category 10 total = 0 only if no intermediates are sold (or exclusion is documented).
- **Mass balance:** Σ tonnes assigned to pathways = tonnes sold as intermediates (no orphan or double-counted volume).
- **No category 9/11/12 leakage:** transport, use-phase, and EOL emissions excluded from the category 10 total.
- **Magnitude sanity:** category 10 per tonne sold should be within the range of the process intensities used; a result exceeding the *most* intensive pathway's factor × total tonnage signals a unit error.
- **YoY consistency:** same pathway-split source and same EF vintage policy; method-tier changes (average → site-specific) disclosed, and base year recalculated only per the `ghg-protocol` skill §6.
- **Allocation audit trail:** for site-specific data, retain the customer's total, the allocation basis, and the share calculation.

## Worked FAQ

**Q1. We sell steel coil to service centers who slit it and sell to
fabricators. How many tiers must we include?**
The minimum boundary runs to the final product, but the Guidance accepts
representative estimation. Model slitting (trivial, ~0.02–0.05 tCO2e/t) plus
one representative fabrication step (~0.2–0.4 tCO2e/t, worldsteel LCI —
verify current). For 200,000 t sold: `200,000 t × (0.03 + 0.30) tCO2e/t =
66,000 tCO2e`. Disclose the two-tier truncation and pathway assumptions.

**Q2. Our customer gave us their whole-company footprint (120,000 tCO2e
S1+S2), not facility data. Can we use it?**
Yes, with two allocations. If the plant processing your input represents 25%
of their production tonnage, and your input is 15% of that plant's input
mass: `120,000 × 0.25 × 0.15 = 4,500 tCO2e`. Score it lower on the data
quality rubric (`ghg-protocol` skill §8) than facility-level data and note
both allocation steps.

**Q3. We sell 30,000 t of glass containers to beverage fillers. Is filling
"processing"?**
Yes — filling, capping, and labeling are processing of an intermediate
product (an empty container is not usable by the end consumer). Filling is
low-intensity (order 0.02–0.06 tCO2e/t of container throughput, dominated by
line electricity — derive from a customer's line data or beverage-sector
LCIs; verify). `30,000 t × 0.04 tCO2e/t = 1,200 tCO2e`. Often immaterial —
a screening estimate plus disclosure may suffice.

**Q4. Half our resin goes through distributors and we cannot trace it. Can
we exclude that half?**
Not by default. Apply the market-level end-use split to the distributor
volume (estimation with disclosed assumptions is the Guidance's preferred
treatment). Exclusion is justifiable only if no reasonable estimation basis
exists — rare for commodities with published end-use statistics.

**Q5. Our category 10 equals our customer's scope 1. Isn't that double
counting?**
It is double counting *between two different companies' inventories*, which
the Scope 3 Standard permits by design — each company's scope 3 overlaps
with others' scopes 1/2. It would only be an error if the same emissions
appeared twice within *your* inventory (e.g., also in category 11).

**Q6. We sell both an intermediate (bulk chemical) and a finished consumer
formulation of it. How do we split?**
Split the sales ledger: bulk chemical tonnage → category 10 (processing by
formulators); finished formulation → categories 9/11/12 as applicable, no
category 10. Never apply category 10 factors to finished-product volume.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5 (category 10 definition and minimum boundary, Table 5.4); ch. 8 (allocation).
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 10 chapter (site-specific and average-data methods; treatment of unknown end uses).
- Cross-cutting conventions: the `ghg-protocol` skill (GWP set §4, EF hierarchy §7, data quality §8, answering-style contract §9).
- Process datasets: ecoinvent (current version), Sphera MLC/GaBi, PlasticsEurope Eco-profiles, worldsteel LCI, International Aluminium Institute LCI — always record version and reference year; verify factors are current at time of use.
