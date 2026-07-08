# GHG Protocol Calculation Skill Suite

A set of Claude Code skills that make Claude a one-stop methodology assistant
for GHG Protocol corporate greenhouse gas accounting. There is one skill per
footprint source, plus a shared navigator skill (`ghg-protocol`) that holds
cross-cutting rules: organizational/operational boundaries, GWP sets, biogenic
treatment, base-year recalculation, emission factor source hierarchy, and data
quality conventions.

## Coverage

| Skill | Footprint source |
|---|---|
| `ghg-protocol` | Navigator + cross-cutting rules (boundaries, GWPs, EF sources, data quality, base year) |
| `s1-stationary-combustion` | Scope 1 — boilers, furnaces, generators, flares |
| `s1-mobile-combustion` | Scope 1 — owned/controlled vehicles, vessels, aircraft, off-road equipment |
| `s1-fugitive-emissions` | Scope 1 — refrigerants, SF6, fire suppression, CH4 leaks, non-Kyoto gases |
| `s1-process-emissions` | Scope 1 — industrial process CO2/N2O/PFCs (cement, ammonia, aluminum…) |
| `s2-purchased-electricity` | Scope 2 — grid electricity, location- & market-based, eGRID/RECs/PPAs |
| `s2-steam-heat-cooling` | Scope 2 — purchased steam, district heat/cooling, CHP allocation |
| `s3-c01-purchased-goods-services` | Scope 3.1 — procurement, supplier-specific → spend-based (EEIO) |
| `s3-c02-capital-goods` | Scope 3.2 — capex, cradle-to-gate in year of acquisition |
| `s3-c03-fuel-energy-related` | Scope 3.3 — WTT of fuels/electricity, T&D losses |
| `s3-c04-upstream-transportation` | Scope 3.4 — inbound/paid freight & distribution (GLEC) |
| `s3-c05-waste-generated` | Scope 3.5 — landfill, incineration, recycling, wastewater |
| `s3-c06-business-travel` | Scope 3.6 — flights (incl. RF question), rail, rental, hotels |
| `s3-c07-employee-commuting` | Scope 3.7 — commuting, surveys, telework/homeworking |
| `s3-c08-upstream-leased-assets` | Scope 3.8 — assets leased by the reporter |
| `s3-c09-downstream-transportation` | Scope 3.9 — customer-paid transport of sold products |
| `s3-c10-processing-sold-products` | Scope 3.10 — downstream processing of intermediates |
| `s3-c11-use-of-sold-products` | Scope 3.11 — lifetime use-phase of sold products |
| `s3-c12-eol-sold-products` | Scope 3.12 — end-of-life of sold products & packaging |
| `s3-c13-downstream-leased-assets` | Scope 3.13 — lessor-side leased assets |
| `s3-c14-franchises` | Scope 3.14 — franchisee scope 1+2 |
| `s3-c15-investments` | Scope 3.15 — financed emissions (GHG Protocol + PCAF) |

## What each source skill contains

Every skill follows the same structure so answers are consistent:

1. **Boundary & classification** — what belongs to the source, the common
   misclassifications, and how overlaps with neighboring categories resolve.
2. **Method ladder** — the full spectrum of calculation approaches, ordered
   from most data-intensive/most accurate (direct measurement,
   supplier-specific) down to screening-level estimation (proxy intensities,
   spend-based EEIO). Each rung: when to use it, data required, formula,
   emission factor sources, a fully worked numeric example, and pitfalls.
3. **Emission factor quick reference** — representative values, every one
   labeled with source, vintage, and units.
4. **Unit and conversion traps**, **data collection & gap-filling**,
   **QA checks**, and a **worked FAQ**.

## Use and limitations

- Ask calculation or methodology questions naturally; Claude routes to the
  right skill. When a question spans sources or you're unsure of the
  category, the `ghg-protocol` navigator handles routing.
- Emission factors quoted in the skills are labeled reference points
  (EPA GHG EF Hub, DEFRA/DESNZ, IPCC 2006, eGRID, IEA, GLEC, PCAF, etc.).
  Factor publications update annually — for inventory-of-record numbers,
  always pull the current-year value from the named source; the skills tell
  you exactly which table to check.
- The skills implement an answering contract (see `ghg-protocol` §9):
  classify first, recommend a method tier based on data availability and
  materiality, show units at every step, name factor sources, state the GWP
  set, and flag ambiguity instead of resolving it silently.
