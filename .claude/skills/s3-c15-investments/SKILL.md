---
name: s3-c15-investments
description: >-
  Scope 3 Category 15 — Investments, i.e., financed emissions. Use for
  questions about PCAF, equity investments, corporate bonds, business loans,
  project finance, mortgages, commercial real estate lending, motor vehicle
  loans, sovereign debt, attribution factors, EVIC, PCAF data quality scores
  (1-5), and financial-institution inventories generally. Covers the GHG
  Protocol category 15 base rules plus the PCAF Global GHG Accounting and
  Reporting Standard as the operational elaboration by asset class. Typically
  THE dominant category for banks, asset managers, insurers, and other FIs.
---

# Scope 3 Category 15 — Investments (Financed Emissions)

**Definition (Scope 3 Standard, ch. 5, category 15):** emissions from the
operation of **investments** (including equity and debt investments and
project finance) in the reporting year, **not already included in scope 1
or scope 2**. Category 15 is where the organizational-boundary residue
lands: whatever ownership interest your consolidation approach excludes
from scopes 1/2 (see the `ghg-protocol` skill §2) is accounted here in
proportion to your share.

Governing documents, in order of application:
- **Scope 3 Standard (2011)**, ch. 5 and Table 5.4 (definition, minimum boundary, the four investment types), plus the category 15 discussion of the equity-share attribution logic.
- **Scope 3 Calculation Guidance (2013), category 15 chapter** — investment-specific and average-data methods.
- **PCAF Global GHG Accounting and Reporting Standard for the Financial Industry** (Part A: Financed Emissions, 2nd ed., Dec 2022; conceived as a GHG Protocol-built detailed elaboration of category 15) — the operational rulebook financial institutions actually implement: per-asset-class attribution formulas, data-quality scoring, disclosure rules. Where the Scope 3 Standard is silent on FI specifics, PCAF governs. PCAF also publishes Part B (Facilitated Emissions, capital markets, 2023) and Part C (Insurance-Associated Emissions, 2022) — adjacent to, and reported separately from, category 15 financed emissions.
- Cross-cutting conventions (GWP set, data quality philosophy, base year): the `ghg-protocol` skill.

**Financial-industry note.** For banks, asset managers, pension funds, and
insurers, category 15 is typically **THE dominant category — commonly
95–99.9% of the total inventory**, hundreds to thousands of times scope 1+2.
Regulatory and voluntary regimes (CSRD/ESRS E1, SBTi FI target-setting,
CDP FS module, NZBA) all effectively require PCAF-conformant financed
emissions. Treat data quality scoring and attribution discipline as the
core of the exercise.

## Boundary & classification

### The four GHG Protocol investment types

The Scope 3 Standard's minimum boundary covers four categories of financial
investment (scope 1 and 2 emissions of investees, proportional to
investment; investees' material scope 3 where relevant — and required under
PCAF's phase-in for fossil-sector exposures):

1. **Equity investments** in companies **not consolidated** into scopes 1/2 — under an equity-share or financial-control approach, entities with <~50%/no control; under operational control, *any* equity stake without operational control (including some >50% stakes). Required, proportional to equity share.
2. **Debt investments with known use of proceeds** (project bonds, ring-fenced lending) — required: emissions of the funded project, proportional.
3. **Project finance** (as sponsor or debt provider) — required, proportional; plus a "should" for accounting **total projected lifetime emissions** of newly financed fossil/long-lived projects in the year of financial close, reported separately from the scope 3 total.
4. **Managed investments and client services** (AUM, advisory) and **debt without known use of proceeds** (general corporate loans, bonds) — **optional** under the 2011 Standard, but **required by PCAF** for the asset classes it covers. Modern practice: follow PCAF; the "optional" label is superseded for any FI claiming PCAF conformance.

**Out of scope / routed elsewhere:**
- Consolidated subsidiaries/JVs → scopes 1/2 per your boundary approach; never both there and in 15.
- Your own corporate operations (offices, data centers) → scopes 1/2 and categories 1–14 like any company.
- **Facilitated** capital-markets activity (underwriting, syndication sold down) → PCAF Part B, reported separately, weighted differently — not category 15 financed emissions.
- Insurance underwriting portfolios → PCAF Part C (insurance-associated emissions), separate metric.
- Derivatives, short positions, and cash: excluded under current PCAF (no attribution method); monitor PCAF updates.
- Sovereign bonds: covered by PCAF's sovereign-debt method (below) — include when material.

### The universal attribution equation

```text
Financed emissions_i = Attribution factor_i × Investee (or asset) emissions_i
C15 = Σ_i Financed emissions_i
```

The attribution factor is **your financing ÷ the total capitalization of
the financed entity/asset**, with the denominator defined per asset class
(next section). Emissions are the investee's scope 1 + scope 2 (and
scope 3 per PCAF's sector phase-in — required since 2021 for oil & gas and
mining exposures, with later phase-ins by sector; verify the current PCAF
timetable), for the **reporting year**, follow-the-money at a fixed
measurement date (typically fiscal year-end outstanding amounts; PCAF
permits year-end or average — disclose which).

## Method ladder

For category 15 the "method ladder" runs along two axes: the **asset-class
attribution formula** (fixed by PCAF) and the **emissions-data tier** (PCAF
data quality scores 1–5). The Scope 3 Calculation Guidance's
investment-specific vs. average-data methods map onto scores 1–3 vs. 4–5.

**Attribution denominators by PCAF asset class:**

| PCAF asset class | Attribution factor | Emissions basis |
|---|---|---|
| Listed equity & corporate bonds | Outstanding amount ÷ **EVIC** | Investee S1+S2 (+S3 phased) |
| Business loans & unlisted equity | Outstanding ÷ (total equity + debt) [book values; EVIC if borrower is listed] | Borrower S1+S2 (+S3 phased) |
| Project finance | Outstanding ÷ (total project equity + debt) | Project S1+S2 |
| Commercial real estate | Outstanding ÷ property value at origination | Property (building energy) emissions |
| Mortgages | Outstanding ÷ property value at origination | Property emissions |
| Motor vehicle loans | Outstanding ÷ total vehicle value at origination | Vehicle operating emissions |
| Sovereign debt | Exposure ÷ (PPP-adjusted GDP) | Country production emissions (incl./excl. LULUCF reported separately) |

**PCAF data quality scores (1 = best, 5 = worst), generic shape:**

| Score | Emissions data basis |
|---|---|
| 1 | Verified reported emissions of the investee/asset |
| 2 | Unverified reported emissions |
| 3 | Physical-activity-based estimate (energy/production data × EFs) |
| 4 | Economic-activity-based estimate (revenue × sector-average intensity, e.g., EEIO) |
| 5 | Asset-class/sector average per $ of asset or revenue proxied from sector splits |

Report the **exposure-weighted average score per asset class** — a required
PCAF disclosure and the main comparability signal.

### 1. Listed equity and corporate bonds

**Attribution:**

```text
Attribution_i = outstanding amount_i ÷ EVIC_i

EVIC = Enterprise Value Including Cash
     = market capitalization (ordinary + preferred shares)
     + total debt (book value) + minority interest
     (cash NOT deducted — that is the difference from classic enterprise value)
```

**Method walk-through.** Symbolic, per instrument:

```text
1. Outstanding amount at the measurement date   ← portfolio ledger
2. EVIC components (market cap, total debt, minority interest)
       ← issuer financials / data vendors (Bloomberg, FactSet),
         fiscal-year-aligned with the emissions year
3. Investee S1+S2   ← CDP response or assured report (score 1);
                      unverified report (score 2)
4. Financed emissions = (outstanding ÷ EVIC) × investee S1+S2
5. C15 contribution = Σ instruments; record the DQ score per record
```

**When investee data is unavailable** — the score-4 EEIO fallback:

```text
Financed emissions = attribution × investee revenue ($)
                     × sector-average emission intensity (tCO2e/$ revenue)
```

Intensity sources: EXIOBASE, USEEIO (verify version), commercial ESG-data
sector intensities, PCAF's own emission-factor database (access via PCAF
membership; regionalized sector factors). A score-5 variant estimates even
revenue from outstanding-amount × sector asset-turnover ratios.

**Pitfalls:** EVIC vs. enterprise value (deducting cash inflates
attribution — can push Σ attribution over 100% of the issuer); negative or
near-zero book equity does not affect EVIC (market-based) but breaks the
business-loan denominator (below); mixing the emissions fiscal year with a
different EVIC date (see traps).

### 2. Business loans and unlisted equity

**Attribution:**

```text
Attribution = outstanding loan or equity stake
              ÷ (total company equity + total debt)      [balance-sheet book values]
# If the borrower is listed: use EVIC as denominator instead.
```

Outstanding = drawn amounts only (undrawn commitments excluded under PCAF).

**Method walk-through.** Attribution = drawn outstanding ÷ (borrower book
equity + total debt), both from the borrower's financial statements for the
same fiscal year as the emissions. Where the borrower reports no emissions,
estimate from primary production data × a sector production intensity
(e.g., GCCA GNR for cement, worldsteel for steel — current year) plus an S2
estimate from energy data → score 3 (physical-activity-based). Multiply and
sum across the book.

**Pitfalls:** negative equity → denominator can go ≤ 0 or attribution > 100%;
PCAF guidance: cap attribution at 100% and disclose. Revolvers: drawn
balance at measurement date. Client's total debt should be *total* debt,
not just debt to you.

### 3. Project finance

```text
Attribution = outstanding (equity + debt) provided by you
              ÷ total project value (total equity + debt of the project)
Financed emissions = attribution × annual project emissions
```

Plus (GHG Protocol "should" / PCAF separate line): in the year of financial
close for new projects, report **total projected lifetime emissions**
separately — e.g., a financed gas plant's 25-year output — not summed into
the annual C15 total.

**Input provenance.** Total project value and your outstanding come from
the financing documents; annual project emissions from project-specific
activity data — metered fuel, or generation × a plant-specific
(heat-rate-derived) intensity — score 2–3 by data source. At financial
close of a new long-lived project, also disclose attribution × projected
lifetime emissions as the separate line described above, never summed into
the annual C15 total.

### 4. Commercial real estate and mortgages

```text
Attribution = outstanding loan ÷ property value at origination
Financed emissions = attribution × property emissions
Property emissions = floor area × energy intensity (by type/region) × EFs
                     (score 3–4) or actual metered energy (score 1–2)
```

**Input provenance.** Loan outstanding and origination value from loan
systems — the LTV-share attribution is fixed at the origination value.
Property emissions from actual metered energy × EFs (score 1–2) or from
floor area × building-type/EPC-label intensity (RECS/CBECS in the US, EPC
registries in the EU/UK — score 3–4). Per loan: LTV share × property
emissions; sum across the book, tracking the score mix.

**Pitfalls:** PCAF fixes the property value **at origination** (updating
the denominator to current values while outstanding amortizes would
manufacture attribution drift); where origination value is unavailable,
PCAF permits latest-available with disclosure. Energy intensities: RECS/
CBECS (US), EPC databases (EU/UK) — score by granularity.

### 5. Motor vehicle loans

```text
Attribution = outstanding ÷ vehicle value at origination
Financed emissions = attribution × (annual km × fuel consumption × fuel EF)
```

**Input provenance.** Outstanding and vehicle value from origination
records; annual km and fuel consumption from national transport statistics
(score 4) or telematics/odometer data (better); fuel EF from the market's
factor source, current edition.

### 6. Sovereign debt

```text
Attribution = your exposure ÷ PPP-adjusted GDP of the country
Financed emissions = attribution × country production emissions
```

Country emissions from UNFCCC inventories/EDGAR (production basis;
LULUCF included and excluded reported as separate lines per PCAF 2nd ed.).
PPP-adjusted GDP from IMF WEO/World Bank, matched to the emissions year.

### 7. Managed investments / AUM (optional under 2011 Standard)

Funds and mandates: look through to holdings and apply the underlying
asset-class methods; where look-through is impossible, fund-average
intensity estimates (score 5). Disclose AUM coverage %. Multi-asset
portfolios: sum per-asset-class results; never average intensities across
asset classes with different denominators.

### Reporting metrics (what to publish alongside the tCO2e total)

PCAF-conformant disclosure pairs the absolute number with context metrics —
compute them from the same record-level data, never as independent
estimates:

```text
Absolute financed emissions (tCO2e)          = Σ attribution_i × emissions_i
Economic emissions intensity (tCO2e/$M)      = absolute ÷ $M outstanding (per asset class)
Physical emissions intensity                  = Σ attributed emissions ÷ Σ attributed output
                                                (e.g., tCO2e/MWh for a power book)
WACI (tCO2e/$M revenue)                       = Σ_i [ portfolio weight_i
                                                × (investee S1+S2 ÷ investee revenue_i) ]
Weighted data quality score (per asset class) = Σ_i (outstanding_i × score_i) ÷ Σ outstanding
Coverage (%)                                  = covered outstanding ÷ total outstanding
```

Note WACI (a TCFD metric) uses **portfolio weights, not attribution
factors** — it is not a financed-emissions measure and must not be summed
with or substituted for the absolute total. Label each metric distinctly.

## Emission factor and parameter sources

Record source, edition/vintage, and units for every input per the
`ghg-protocol` skill §7.

**Denominator/financial data:**

| Parameter | Source | Notes |
|---|---|---|
| EVIC components | Issuer financials; index/data vendors (Bloomberg, FactSet) | Fiscal-year-end aligned with emissions year; EVIC floors per EU PAB/CTB rules exist for negative values |
| Book equity + debt (private) | Borrower financial statements | Same fiscal year as emissions |
| Property value at origination | Loan origination records | Fixed; do not revalue |
| PPP-adjusted GDP | IMF WEO / World Bank (annual) | Match emissions year |

**PCAF data quality scores — detailed shape for two key asset classes**
(paraphrased from PCAF 2nd ed. score tables; consult the standard's exact
tables per asset class before assigning scores):

*Listed equity & corporate bonds / business loans:*

| Score | Basis |
|---|---|
| 1 | Reported emissions, third-party verified; audited energy data × EFs |
| 2 | Reported emissions, unverified |
| 3 | Company primary physical-activity data (energy, production) × EFs |
| 4 | Company revenue × sector-average revenue intensity (EEIO/sector data) |
| 5 | Outstanding amount × sector-average emissions per $ of assets/revenue, with revenue itself estimated from asset-turnover ratios |

*Mortgages / commercial real estate:*

| Score | Basis |
|---|---|
| 1 | Actual metered building energy × supplier-specific/actual EFs |
| 2 | Actual metered building energy × average grid/fuel EFs |
| 3 | Estimated energy from floor area × building-type/EPC-label intensity |
| 4 | Estimated energy from number of buildings × building-type averages |
| 5 | Estimated energy from country-average building stock data only |

**Emissions/intensity data:**

| Data | Source + vintage | Typical DQ score |
|---|---|---|
| Investee reported S1+S2 | CDP responses (annual), annual/sustainability reports, ESG vendors | 1 (verified) / 2 (unverified) |
| Sector production intensities (t/t product, t/MWh) | GCCA GNR (cement), worldsteel, IEA (power) — latest year | 3 |
| Sector revenue intensities (tCO2e/$M) | EXIOBASE (v3.x), USEEIO (v2.x), PCAF EF database (member access) — verify versions | 4–5 |
| Building intensities | RECS / CBECS (EIA, current survey cycles); EU EPC registries | 3–4 |
| Vehicle use statistics | National transport statistics (e.g., US FHWA annual VMT series — current year) | 4 |
| Country inventories | UNFCCC CRF submissions; EDGAR (annual) | 2–3 |
| Grid factors for investee S2 estimates | eGRID (biennial data releases); IEA (latest) | — |

This skill intentionally quotes no factor values. When a quantitative
answer is needed, pull the current-year value from the named source.

## Unit and conversion traps

- **EVIC ≠ enterprise value:** cash is **not** deducted in EVIC. Using classic EV shrinks the denominator and inflates attribution; portfolio-wide this typically overstates financed emissions by several percent and can push single-issuer attribution sums past 100%.
- **Vintage alignment (attribution-factor mismatch):** numerator (your year-end outstanding), denominator (issuer EVIC / balance sheet), and investee emissions should reference the **same or nearest fiscal year**. A 2023 emissions figure over a 2026 EVIC after a stock rally silently deflates results — a market-price artifact, not decarbonization. PCAF acknowledges market-driven EVIC volatility; disclose the data vintages and consider explaining YoY movements via a decomposition (see QA).
- **Drawn vs. committed:** PCAF attributes **outstanding (drawn)** amounts; committed-but-undrawn facilities are excluded from financed emissions (they appear in some target-setting frameworks — keep the metrics distinct).
- **tCO2e vs. tCO2e/$M lent (economic intensity) vs. physical intensity (tCO2e/MWh):** PCAF requires absolute financed emissions; intensities are supplementary — never sum intensities.
- **Currency and FX:** numerator and denominator in one currency at one FX date.
- **Double counting inside C15:** holding both the equity and the debt of one issuer is fine — EVIC-based attribution is designed so equity + debt holders together ≤ 100%. But do not count a loan **and** its securitized form, or a fund holding **and** its look-through constituents.
- **Percent vs. basis points:** a 0.5% attribution entered as 0.5 (i.e., 50%) is the classic 100× error — enforce decimal-fraction convention in models.
- **LULUCF split** for sovereigns: incl./excl. reported separately, not blended.

## Data collection & gap-filling

- **Portfolio extract at measurement date:** instrument-level outstanding amounts, asset-class tags, issuer identifiers (LEI/ISIN) — the backbone; garbage identifiers are the #1 practical failure.
- **Investee disclosures:** CDP (largest structured source), annual/sustainability reports, transition plans; ESG data vendors (MSCI, S&P Trucost, ISS, Bloomberg) resell reported + estimated figures — record whether each vendor number is *reported* (score 1–2) or *vendor-estimated* (score 4–5); do not launder vendor estimates into score 2.
- **PCAF emission-factor database** for sector/region average factors (member access; updated periodically — verify vintage).
- **Borrower engagement:** for private-book materiality (large corporate/CRE), collect financials + energy data through relationship managers at origination/annual review; add ESG data covenants to documentation.
- **Gap-filling hierarchy (mirrors the DQ scores):** reported → physical-activity estimate → revenue × sector intensity (EEIO, score 4) → sector-average per $ outstanding (score 5). Flag every estimated record; recompute the weighted DQ score after each fill.
- **Coverage disclosure:** % of AUM/lending covered by asset class; excluded asset classes named with reasons (PCAF requirement).

## QA checks

- **Dominance sanity:** for an FI, C15 should dwarf scopes 1+2 (often >99% of total). If C15 is comparable to operational emissions, coverage or unit errors are almost certain.
- **Attribution bounds:** every attribution factor in [0, 1]; issuer-level Σ (your instruments ÷ EVIC) sensible; flag denominators ≤ 0 (negative equity) and apply the documented cap-and-disclose rule.
- **Reconciliation:** Σ instrument outstanding in the calculation = portfolio ledger at the measurement date, per asset class.
- **Weighted DQ score** per asset class computed, disclosed, and tracked YoY — improving score with stable emissions is the expected maturity path.
- **YoY decomposition:** attribute changes to (a) portfolio size/mix, (b) EVIC/denominator market moves, (c) investee emissions changes, (d) data-quality/method changes — disclose (d) explicitly; base-year recalculation per the `ghg-protocol` skill §6 policy.
- **Vintage audit:** emissions year vs. financial-data year per record; mismatches > 2 years flagged.
- **No consolidation overlap:** entities in scopes 1/2 absent from C15 and vice versa (list-level check against the org-boundary register).
- **Scope 3 phase-in compliance:** investee scope 3 included for the sectors PCAF currently requires (energy/mining onward — verify current schedule) and reported as a separate line from investee S1+S2.

## Worked FAQ

**Q1. We hold a small stake in a listed utility that reports assured
S1+S2. Financed emissions?**
Attribution = position value ÷ the utility's EVIC (fiscal-year-aligned
components from issuer financials or data vendors), × the reported assured
S1+S2 → DQ score 1. Expect the result to dwarf your operational footprint —
a single utility position routinely exceeds a mid-size bank's entire
scopes 1+2; that is normal for C15.

**Q2. Private borrower, facility partly drawn, no emissions data. Method?**
Attribution on the drawn amount only ÷ (borrower book equity + total debt),
same fiscal year; the undrawn commitment is excluded under PCAF. With no
reported or physical-activity data, fall back to score 4: borrower revenue
× a region-matched sector revenue intensity (EXIOBASE / USEEIO / PCAF EF
database — record the version). Flag the record as estimated and fold it
into the exposure-weighted DQ score.

**Q3. Our equity stake is 60% but we use operational control and don't
operate the company. Scope 1 or C15?**
C15. Under operational control, a non-operated 60% stake is excluded from
scopes 1/2, so it lands in category 15 at 60% attribution of the investee's
S1+S2 (GHG Protocol logic; for PCAF unlisted equity, attribution = your
equity ÷ (borrower total equity + debt) — the share-of-capital view; state
which convention and be consistent). This is the classic oil-and-gas
non-operated-JV pattern.

**Q4. Our financed emissions dropped 18% but we sold nothing and investees'
emissions were flat. How?**
Almost certainly EVIC inflation — equity markets rose, denominators grew,
attribution shrank. Report the number per PCAF but decompose the change in
the narrative; consider also disclosing an intensity metric and DQ scores so
readers see no real-economy decarbonization occurred.

**Q5. Mortgage book on EPC-based estimates — how does it improve?**
Per loan, attribution = outstanding ÷ property value at origination
(fixed); property emissions from EPC-label or floor-area intensity
estimates score 3–4. Moving to actual metered energy (utility-data
partnerships) moves the book toward score 1–2 and typically shifts the
estimate materially — disclose it as a method change and track the
exposure-weighted score YoY.

**Q6. Do we include our investees' scope 3?**
Per the Scope 3 Standard: where significant ("should"). Per PCAF 2nd ed.:
**required on a sector phase-in** — oil, gas, and mining from 2021 reporting,
additional sectors on the published schedule (verify current PCAF
requirements). Report investee scope 3 as a separate line from investee
S1+S2, because inter-company double counting within it is unavoidable.

**Q7. We underwrote a $500M bond issuance but hold none of it. Category 15?**
No — that is **facilitated** emissions, PCAF Part B: reported separately
from financed emissions, with a 33% weighting factor applied to the
facilitated amount under the 2023 standard (verify current). Only retained
positions enter category 15.

## References

- Corporate Value Chain (Scope 3) Accounting and Reporting Standard (WRI/WBCSD, 2011): ch. 5, Table 5.4 (category 15 minimum boundary; four investment types; project-finance lifetime-emissions "should").
- Technical Guidance for Calculating Scope 3 Emissions, v1.0 (WRI/WBCSD, 2013): Category 15 chapter (investment-specific and average-data methods).
- **PCAF, The Global GHG Accounting and Reporting Standard for the Financial Industry** — Part A: Financed Emissions, 2nd edition (Dec 2022): asset-class methods (ch. 5), attribution rules, data-quality score tables per asset class, disclosure requirements. Part B: Facilitated Emissions (2023). Part C: Insurance-Associated Emissions (2022). Verify current editions and sector scope 3 phase-in schedule at carbonaccountingfinancials.com.
- Data sources: CDP; PCAF emission-factor database; EXIOBASE/USEEIO (versioned); UNFCCC/EDGAR (sovereign); IMF WEO (PPP GDP); RECS/CBECS/EPC (property); eGRID/IEA (grids). Record vintage for every factor.
- Cross-cutting rules: the `ghg-protocol` skill (§2 organizational boundary → C15 residue, §4 GWPs, §6 base year, §7 EF hierarchy, §8 data quality, §9 answering contract).
