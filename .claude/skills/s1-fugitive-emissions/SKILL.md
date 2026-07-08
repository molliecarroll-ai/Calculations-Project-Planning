---
name: s1-fugitive-emissions
description: >-
  Scope 1 fugitive emissions methodology: refrigerants and refrigerant leakage
  (HFCs, R-410A, R-134a, R-404A, R-407C, R-32), AC and chiller top-ups, vehicle
  air conditioning, SF6 in electrical switchgear, fire suppression agents
  (HFC-227ea, FK-5-1-12), methane leaks from gas distribution and
  landfill/wastewater at own facilities. Use for the material-balance and
  screening (leak-rate) methods, GWP of refrigerant blends, and the treatment
  of non-Kyoto refrigerants (CFCs, HCFCs like R-22, HFOs like R-1234yf) as
  memo items. Also use for questions about refrigerant purchase records,
  service logs, nameplate charge, and EPA Section 608 / EU F-Gas records.
---

# Scope 1 — Fugitive Emissions

Fugitive emissions are intentional or unintentional releases of GHGs from
owned or controlled sources that are not combustion: refrigerant leakage from
refrigeration/AC equipment, SF6 losses from electrical equipment, fire
suppression agent releases, and CH4 leaks (equipment seals, gas piping,
landfill/wastewater at own facilities). Gases covered are chiefly HFCs, PFCs,
SF6, and CH4. Governing documents: GHG Protocol Corporate Standard ch. 4
(scope 1 definition); GHG Protocol "Calculating HFC and PFC Emissions from the
Manufacturing, Installation, Operation and Disposal of Refrigeration and
Air-conditioning Equipment" calculation tool (v1.0, 2005 — "the HFC tool");
EPA Center for Corporate Climate Leadership, "GHG Inventory Guidance: Direct
Fugitive Emissions from Refrigeration, Air Conditioning, Fire Suppression, and
Industrial Gases" (2014, updated); IPCC 2006 GL vol. 3 ch. 7 (ODS substitutes)
and ch. 8 (SF6). Cross-cutting conventions (GWP sets, boundary approach, EF
hierarchy, answering style) are defined in the `ghg-protocol` skill — follow
them; this skill does not restate them.

## Boundary & classification

Confirm classification before calculating (per the `ghg-protocol` skill §2
and §9):

- **Owned/operated equipment vs. landlord HVAC.** Refrigeration/AC equipment
  the reporter owns or operates (operational-control test) → scope 1. In a
  leased building where the **landlord** owns and services the central HVAC
  plant, refrigerant losses are the landlord's scope 1; for the tenant they
  fall in scope 3 category 8 (upstream leased assets) — and are frequently
  immaterial and excluded with justification. The answer flips with the
  boundary approach: under operational control, a tenant who operates and
  services its own dedicated units reports them in scope 1 even if the
  landlord holds title. State which boundary approach applies before answering.
- **Vehicle air conditioning** (mobile AC) belongs **here**, not in mobile
  combustion. The mobile combustion tools cover fuel CO2/CH4/N2O only;
  refrigerant losses from vehicle AC systems (typically R-134a legacy,
  R-1234yf in newer fleets) are scope 1 fugitive for owned/controlled vehicles.
- **Refrigerants in leased assets**: leased vehicles or equipment the reporter
  operates → scope 1 under operational/financial control (consistent with the
  treatment of their fuel); assets leased out to others → scope 3 category 13.
- **Non-Kyoto gases.** CFCs and HCFCs (e.g., R-22, R-11) are Montreal Protocol
  gases and HFOs (e.g., R-1234yf, R-1234ze) are short-lived non-Kyoto gases:
  all are reported **outside the scopes as an optional memo item**, never
  added to scope 1 totals (Corporate Standard ch. 4; `ghg-protocol` skill §4).
  Still quantify them — R-22 has a GWP of 1,760 (AR5) and remaining installed
  bases are large.
- **Fire suppression systems** using HFCs (HFC-227ea/FM-200, HFC-125,
  HFC-236fa) or PFCs → scope 1 fugitive (annual leakage plus any discharge
  events, including accidental discharges and testing). CO2 flooding systems:
  discharged CO2 is scope 1. FK-5-1-12 (Novec 1230) has GWP < 1 (memo/de
  minimis). Inert-gas systems (IG-541 etc.) have no GHG content.
- **Electrical switchgear SF6** (and NF3 or SF6 in other electrical/electronic
  equipment) → scope 1 for owned/operated gas-insulated switchgear, circuit
  breakers, and transformers. Material mainly for utilities and large
  industrial substations, but any owned HV/MV gear counts.
- **CH4 from wastewater treatment or landfills at own facilities** → scope 1
  (often labeled fugitive; some inventories classify as process — pick one and
  be consistent). Third-party-managed waste from your operations → scope 3
  category 5.
- **Natural gas distribution leaks**: for gas utilities/pipeline operators,
  CH4 leaks from owned mains, services, and compressor stations are a core
  scope 1 fugitive source (40 CFR Part 98 subpart W methods). For ordinary
  reporters, leaks downstream of their meter in their own piping are
  technically scope 1 but usually de minimis; upstream production/transmission
  leaks are scope 3 category 3.

## Method ladder

| Tier | Method | Data basis | Use when |
|---|---|---|---|
| 1 | Material balance (full sales-based lifecycle) | Refrigerant inventory counts, purchase/sale records, nameplate capacity changes | Complete stock records exist; large refrigerant users |
| 2 | Simplified material balance | Purchase records split by purpose (top-up vs. new charge) + disposal records | Service purchases known but no cylinder inventory tracking |
| 3 | Screening / emission-factor | Equipment register (type, count, nameplate charge) × default leak rates | No purchase or service data; screening or immaterial fleets |
| 4 | Spend or purchase-record proxy | Refrigerant invoices ($ or undifferentiated kg) | Only invoices exist; last resort, flag data quality 4–5 |

Always compute per refrigerant, in kg of refrigerant, then convert to CO2e
with the blend-weighted GWP (see blend subsection). Never average across
refrigerant types before applying GWPs.

### Tier 1 — Material balance (sales-based lifecycle method)

**When:** the reporter tracks refrigerant containers held on site, purchases,
returns, and equipment additions/retirements. This is the GHG Protocol HFC
tool "Sales-Based Method" and mirrors EPA's mass-balance approach; it captures
installation, service, and disposal losses in one equation.

**Data required:** beginning and ending inventory of refrigerant in storage
(cylinders, not in equipment); all acquisitions (purchases, refrigerant
provided by contractors, returns after off-site recycling); all disbursements
(sales, returns to supplier, refrigerant sent off-site for recycling or
destruction); total full-charge (nameplate) capacity of the equipment fleet at
start and end of year.

```
E_kg = (I_begin − I_end)                 # storage inventory decrease
     + (A − D)                           # acquisitions − disbursements
     − (C_end − C_begin)                 # net increase in fleet nameplate capacity

E_CO2e = E_kg × GWP_refrigerant / 1,000   # tonnes CO2e, GWP per gas or blend-weighted
```

Terms: I = refrigerant in storage (kg); A = acquisitions (kg); D =
disbursements off-site (kg); C = sum of equipment nameplate charges (kg). The
capacity term removes refrigerant that went into (or came out of) equipment
rather than the atmosphere.

**Sign conventions that trip people up:** inventory decrease and net
acquisitions both add to emissions. Fleet **growth** makes the capacity term
subtract (that refrigerant went into equipment, not the air); fleet
**shrinkage** from retirements makes it negative, adding the retired charge
into the balance — recovered gas then nets back out through I_end or D.
Convert the resulting kg, per refrigerant, with the mass-weighted blend GWP
from the declared AR set.

**Pitfalls:** omitting the capacity term (overstates emissions in growth
years, produces negative results in retirement years); counting refrigerant
inside equipment as "inventory" (inventory = storage only); missing
contractor-supplied refrigerant that never appears in your purchase ledger;
retired equipment whose recovered charge went off-site must show up in D or
the balance breaks.

### Tier 2 — Simplified material balance

**When:** purchases can be split by purpose but cylinder inventories are not
tracked. Assumes storage inventory is steady state, so **refrigerant purchased
to service existing equipment ≈ refrigerant emitted** (every kg topped up
replaced a kg that leaked or will leak before the next service).

```
E_kg = P_new × k_install                       # losses charging new equipment
     + P_service                               # all top-up/service purchases
     + C_retired × (1 − f_recovered)           # charge lost at disposal

k_install: installation loss fraction, default 0.2–3% by equipment type
           (IPCC 2006 GL vol.3 ch.7 Table 7.9 — verify current edition)
f_recovered: fraction of retired-unit charge actually recovered (from
           technician recovery records; if unknown, EPA guidance defaults
           by equipment type, often 0–85% — verify)
```

**Walk-through** — a service-only year (no installs or retirements) reduces
to E_kg = P_service per refrigerant; convert with the blend GWP. The whole
method turns on the purpose split of purchases — see pitfalls.

**Pitfalls:** purchases that charged **new** equipment must be excluded from
the top-up term (only the installation-loss fraction of those kg is emitted);
multi-year service cycles make single-year purchases lumpy — average over the
service interval or the year-to-year series will swing wildly; steady-state
assumption fails during fleet expansion or refrigerant transitions.

### Tier 3 — Screening / emission-factor method

**When:** only an equipment register exists (type, count, nameplate charge).
Multiply installed charge by default annual leak rates by equipment type.

```
E_kg = Σ_equipment_type [ N × charge_kg × LR_operating ]
       (+ N_new × charge × k_install  + N_retired × charge × (1 − f_recovered), if applicable)
```

Default operating leak rates — **GHG Protocol HFC tool defaults, adopted from
IPCC 2006 GL vol. 3 ch. 7 Table 7.9 (2006 vintage). These ranges define the
screening method; verify against the current GHG Protocol tool and IPCC 2019
Refinement before use; site-specific rates always take precedence:**

| Equipment type | Typical charge | Installation loss | Operating leak rate (%/yr of charge) | Refrigerant remaining at disposal |
|---|---|---|---|---|
| Domestic/residential-style refrigeration | 0.05–0.5 kg | 0.2–1% | 0.1–0.5% | 80% (of charge) |
| Stand-alone commercial units | 0.2–6 kg | 0.5–3% | 1–15% | 80% |
| Medium & large commercial refrigeration (supermarket racks) | 50–2,000 kg | 0.5–3% | 10–35% | 100% (less recovery) |
| Industrial refrigeration (incl. cold storage, food processing) | 10–10,000 kg | 0.5–3% | 7–25% | 100% (less recovery) |
| Chillers (comfort cooling) | 10–2,000 kg | 0.2–1% | 2–15% | 100% (less recovery) |
| Residential & commercial comfort AC / heat pumps | 0.5–100 kg | 0.2–1% | 1–10% | 80% |
| Mobile (vehicle) AC | 0.5–1.5 kg | 0.2–0.5% | 10–20% | 50% |

Pick a point within the range based on equipment age, climate, and maintenance
regime; document the choice. Midpoint is a defensible default for screening.

**Walk-through**: per refrigerant, E_kg = installed charge × the selected,
documented leak rate; convert with the blend GWP from the declared AR set.
For high-leak categories (e.g., supermarket racks) the selected rate is the
dominant uncertainty — disclose it.

**SF6 in switchgear** (same tier structure): nameplate SF6 capacity × annual
leak rate. Defaults: sealed-pressure MV switchgear ≈ 0.1–0.5%/yr
(manufacturer-certified, often ≤0.1%); closed-pressure HV equipment ≈
0.5–2.6%/yr (IPCC 2006 GL vol. 3 ch. 8 regional defaults; EPA SF6 Emission
Reduction Partnership reports utility fleet averages ~1% or below — verify
current data). Utilities with top-up logs should use the mass-balance method
instead (Tier 1 dominates for this source; 40 CFR Part 98 subpart DD
prescribes it for large users).

**Fire suppression**: installed agent base × default annual release rate ≈ 2%
±1%/yr (IPCC 2006 GL vol. 3 ch. 7.4 default for fire protection — verify),
**plus** actual kg of any recorded discharge events.

**Pitfalls:** applying leak rates to purchases instead of installed charge;
using this tier *and* adding purchase-based emissions (double counting — pick
one method per equipment population); forgetting that the ranges are wide —
disclose the selected rate.

### Tier 4 — Spend or purchase-record proxy

**When:** only supplier invoices exist, with no purpose split and no equipment
register. Convert invoice $ to kg using unit prices (or take invoiced kg
directly) and treat total purchases as emissions — i.e., the Tier 2 equation
with everything assigned to the service term. This overstates emissions in
years with new installations and understates disposal losses. Flag as data
quality 4–5 per the `ghg-protocol` skill §8 and prioritize replacing it with
an equipment register (Tier 3) or purpose-coded purchases (Tier 2).

### Blend decomposition and GWPs

Blended refrigerants are decomposed into constituents by **mass fraction**,
and the blend GWP is the mass-weighted average of constituent GWPs
(`ghg-protocol` skill §4). Compositions per ASHRAE Standard 34 designations:

```
GWP_blend = Σ_i (mass_fraction_i × GWP_i)

R-410A = 50% HFC-32 / 50% HFC-125
  AR5: 0.50 × 677  + 0.50 × 3,170 = 1,923.5 ≈ 1,924
  AR6: 0.50 × 771  + 0.50 × 3,740 = 2,255.5 ≈ 2,256

R-404A = 44% HFC-125 / 52% HFC-143a / 4% HFC-134a
  AR5: 0.44 × 3,170 + 0.52 × 4,800 + 0.04 × 1,300 = 3,942.8 ≈ 3,943
  AR6: 0.44 × 3,740 + 0.52 × 5,810 + 0.04 × 1,530 = 4,728.0 ≈ 4,728

R-407C = 23% HFC-32 / 25% HFC-125 / 52% HFC-134a
  AR5: 0.23 × 677 + 0.25 × 3,170 + 0.52 × 1,300 = 1,624.2 ≈ 1,624
  AR6: 0.23 × 771 + 0.25 × 3,740 + 0.52 × 1,530 = 1,907.9 ≈ 1,908
```

Blends containing non-Kyoto constituents (e.g., R-448A/R-449A contain HFOs;
legacy blends contain HCFCs) are split: the Kyoto-gas mass goes in scope 1,
the non-Kyoto mass to the memo item.

## Emission factor sources

For fugitive sources the "factors" are GWPs (fixed per IPCC assessment-report
edition) and method-defining default parameters — not annually revised
emission factors:

- **GWPs**: IPCC AR5 WG1 (2013) Appendix 8.A; AR6 WG1 (2021) ch. 7
  supplementary tables; republished in the EPA Hub GWP table (Part 98
  Table A-1-aligned). Static per AR edition — use the declared set.
- **Blend compositions**: ASHRAE Standard 34 (mass fractions).
- **Default leak/loss rates**: GHG Protocol HFC tool, adopting IPCC 2006 GL
  vol. 3 ch. 7 Table 7.9 (2006 vintage; check the 2019 Refinement). SF6:
  IPCC 2006 ch. 8, EPA SF6 Partnership statistics, Part 98 subpart DD.
  Fire suppression: IPCC 2006 ch. 7.4.

**100-year GWPs of common refrigerants and agents** (IPCC AR5 2013 without
climate-carbon feedback; AR6 2021. Retained because fixed per AR edition;
verify your disclosure program's required set):

| Substance | AR5 GWP-100 | AR6 GWP-100 | Notes |
|---|---|---|---|
| HFC-134a (R-134a) | 1,300 | 1,530 | Legacy vehicle AC, chillers |
| HFC-32 (R-32) | 677 | 771 | Newer AC; R-410A constituent |
| HFC-125 | 3,170 | 3,740 | Blend constituent |
| HFC-143a | 4,800 | 5,810 | R-404A constituent |
| HFC-227ea | 3,350 | 3,600 | Fire suppression (FM-200) |
| HFC-23 | 12,400 | 14,600 | Byproduct; ultra-low-temp refrigeration |
| R-410A (blend) | 1,924 | 2,256 | Mass-weighted, computed above |
| R-404A (blend) | 3,943 | 4,728 | Mass-weighted, computed above |
| R-407C (blend) | 1,624 | 1,908 | Mass-weighted, computed above |
| SF6 | 23,500 | 25,200 | Switchgear |
| CH4 (fossil) | 28 | 29.8 | Gas leaks |
| R-22 (HCFC-22) | 1,760 | 1,960 | **Non-Kyoto — memo item only** |
| R-1234yf (HFO) | <1 | ~0.5 | **Non-Kyoto — memo item only** |
| FK-5-1-12 (Novec 1230) | <1 | <1 | Fire suppression; effectively nil |

Default leak/loss-rate ranges live in the Tier 3 section above; all carry
wide ranges — state the value chosen and verify the current publication.

This skill intentionally quotes no factor values. When a quantitative answer
is needed, pull the current-year value from the named source. (The GWPs and
default parameter ranges above are retained: they are fixed by the named
publication edition and define the methods.)

## Unit and conversion traps

- **lbs vs. kg cylinders.** US refrigerant cylinders are labeled in pounds
  (25 lb, 30 lb jugs); most EFs and reporting are metric. 1 lb = 0.4536 kg.
  A 30 lb cylinder is 13.6 kg — treating it as 30 kg overstates by 2.2×.
- **Charge vs. top-up.** Nameplate (full) charge is what the equipment holds;
  top-up is what was added. Leak-rate methods apply the % to the **charge**,
  never to purchases; mass-balance methods use purchases, never charge × rate.
- **% leak rate applied to the wrong base.** 10% of an 800 kg installed charge
  ≠ 10% of 40 kg of purchases. Applying default rates to purchase volumes is a
  frequent, large understatement.
- **Double counting purchase + leak-rate methods.** For any single equipment
  population use one tier. Adding "top-up purchases" to "charge × leak rate"
  counts the same leak twice.
- **Blend GWP shortcuts.** Using the GWP of the dominant constituent (e.g.,
  HFC-125 for R-410A) instead of the mass-weighted blend GWP misstates by up
  to ~65%.
- **Cylinder heels.** "Empty" returned cylinders retain 5–10% heel; if
  disbursements are recorded at nominal full weight the balance overstates
  returns and understates emissions. Use actual weights where available.
- **GWP set consistency.** Do not mix AR5 blend GWPs with AR6 single-gas
  values in one inventory (`ghg-protocol` skill §4).

## Data collection & gap-filling

Collect, in priority order:
1. **Service records / work orders** (HVAC contractor tickets showing kg added
   per event, per unit, per refrigerant) — the backbone of Tiers 1–2.
2. **Refrigerant purchase invoices** with refrigerant type and kg (or cylinder
   count × size), coded by purpose (new charge vs. service) where possible.
3. **Equipment register** with equipment type, refrigerant type, nameplate
   charge, install date, location — required for Tier 3 and for the capacity
   term in Tier 1.
4. **Regulatory F-gas records**: EU F-Gas Regulation (517/2014, recast
   2024/573) leak-check logs for systems ≥5 t CO2e; US EPA Section 608
   (40 CFR Part 82 subpart F) leak-inspection and appliance records for
   systems ≥50 lb charge; these are audit-grade leak evidence that often
   already contains kg-added data.
5. **SF6**: utility gas cards / top-up logs per breaker; nameplate ratings.
6. **Fire suppression**: system inspection certificates (agent weight checks),
   discharge incident reports.

Gap-filling: with only equipment counts, assign typical charges from the Tier
3 table (or manufacturer literature for the specific models) and default leak
rates — document both assumptions. Missing sites: apply a per-site or
per-floor-area intensity from comparable audited sites, flagged as estimated
per the `ghg-protocol` skill §8. Partial-year service data: annualize only if
service is roughly continuous; do not annualize a single large top-up event.

## QA checks

- **Implied leak rate**: total emissions ÷ total installed charge, per
  refrigerant and per site. Compare against the Tier 3 default range for the
  equipment mix; a comfort-cooling office fleet implying 40%/yr, or a
  supermarket implying 1%/yr, needs investigation.
- **Negative mass-balance result** means the capacity or inventory terms are
  wrong (e.g., new-equipment charge not purchased through your ledger because
  it arrived pre-charged, or retirements not reflected) — never report a
  negative; fix the terms. Pre-charged equipment contributes no purchase but
  increases capacity, driving the balance negative unless handled (exclude
  the pre-charged capacity from ΔC or add a matching notional acquisition).
- **Top-up without matching equipment**: purchases of a refrigerant absent
  from the equipment register indicate an incomplete register or contractor
  mis-invoicing.
- **YoY variance**: fugitive emissions are lumpy (service cycles, discharge
  events); investigate swings >±50% but expect volatility — consider
  disclosing multi-year averages as context, while reporting the actual year.
- **Recovery reasonableness**: recovered kg at disposal cannot exceed
  nameplate charge; recovery rates >95% claimed without weigh tickets are
  suspect.
- **Memo-item completeness**: if the register shows R-22 units but the memo
  item is zero, the inventory is incomplete, not clean.

## FAQ

**Q1. We bought 300 lb of R-410A this year, all for topping up rooftop units.
What are our emissions?**
Simplified material balance (Tier 2): top-up purchases ≈ emissions. Convert
pounds to kg first (1 lb = 0.4536 kg — US cylinders are labeled in lb), then
multiply the kg by the R-410A mass-weighted blend GWP from the inventory's
declared AR set (blend table above) and state the set used. Confirm none of
the purchases charged **new** equipment — those kilograms belong in the
installation-loss term, not the top-up term.

**Q2. What's the GWP of R-407C, and how do I show my work?**
Decompose by mass: 23% HFC-32, 25% HFC-125, 52% HFC-134a. AR5: 0.23×677 +
0.25×3,170 + 0.52×1,300 = 155.7 + 792.5 + 676.0 = **1,624**. AR6: 0.23×771 +
0.25×3,740 + 0.52×1,530 = 177.3 + 935.0 + 795.6 = **1,908**. Cite ASHRAE 34
for the composition and the IPCC AR edition for the constituent GWPs.

**Q3. Full mass balance: we started the year with 80 kg of R-134a in
cylinders and ended with 55 kg; bought 150 kg; sent 25 kg off-site for
reclamation; decommissioned a chiller with a 60 kg nameplate charge (fleet
capacity fell by 60 kg). How does the balance work?**

```
C_end − C_begin = −60 kg  (fleet shrank)
E = (80 − 55) + (150 − 25) − (−60)
  = 25 + 125 + 60
  = 210 kg R-134a  → convert with the HFC-134a GWP from the declared AR set
```
Note how the equation treats the retired chiller: its 60 kg charge left the
fleet, and any of it that was actually **recovered** must already appear in
I_end (recovered into your cylinders) or D (sent off-site) — where it
correctly nets out. Whatever was not recovered is booked as emissions, which
is the right answer. Verify with recovery weigh tickets that I_end and D
reflect the recovered gas; if recovery happened but was never recorded, the
210 kg overstates emissions and the records, not the formula, need fixing.

**Q4. Our landlord runs the building chillers; we have server-room CRAC units
we maintain under our own contract. What goes where?**
Under operational control: the CRAC units are your scope 1 (you direct their
operation and servicing); the landlord's central plant is your scope 3
category 8 (or excluded with justification if immaterial). Under equity share
in a building you don't own, neither is scope 1. State the boundary approach
in the answer (`ghg-protocol` skill §2).

**Q5. We found 12 R-22 packaged units on the register. Scope 1?**
No. R-22 is an HCFC (Montreal Protocol, non-Kyoto). Estimate losses the same
way — typical charge × a documented point in the comfort-AC default leak-rate
range, converted with the R-22 GWP — but report the result as a **memo item
outside the scopes**, never in scope 1 totals. Also flag the phase-out
compliance angle (no new R-22 supply in the US since 2020) — an operational
risk note, not a scope 1 line.

**Q6. A 68 kg HFC-227ea fire-suppression system discharged accidentally in
March. How is it reported?**
The full discharged mass is scope 1 in the reporting year: discharged kg ×
the HFC-227ea GWP from the declared AR set. Add the routine ~2%/yr default
leakage on the remaining installed base. Disclose the event if it materially
drives YoY variance.

## References

- GHG Protocol Corporate Accounting and Reporting Standard (Revised Edition,
  2004), ch. 4 (scope 1 definition, direct GHG emissions).
- GHG Protocol calculation tool: "Calculating HFC and PFC Emissions from the
  Manufacturing, Installation, Operation and Disposal of Refrigeration and
  Air-Conditioning Equipment" (v1.0, 2005) — sales-based, lifecycle-stage, and
  screening methods; default parameter tables.
- EPA Center for Corporate Climate Leadership, "GHG Inventory Guidance:
  Direct Fugitive Emissions from Refrigeration, Air Conditioning, Fire
  Suppression, and Industrial Gases" (2014; check for updates) — material
  balance, simplified material balance, screening method.
- 40 CFR Part 98: subpart DD (SF6 electrical equipment), subpart W (petroleum
  and natural gas systems CH4), subpart OO (fluorinated GHG suppliers).
- IPCC 2006 Guidelines for National GHG Inventories, vol. 3 (IPPU), ch. 7
  (ODS substitutes; Table 7.9 charge/leak defaults) and ch. 8 (SF6/PFCs from
  other product uses); 2019 Refinement where updated.
- IPCC AR5 WG1 (2013) Appendix 8.A and AR6 WG1 (2021) ch. 7 supplementary
  tables — GWP values.
- ASHRAE Standard 34 — refrigerant designations and blend compositions.
- EU F-Gas Regulation (EU) 2024/573 (recast of 517/2014); US EPA Section 608
  regulations (40 CFR Part 82 subpart F) — leak-check recordkeeping.
- EPA GHG Emission Factors Hub (updated ~annually) — GWP tables and blend
  GWPs consistent with Part 98 Table A-1.
- Cross-cutting conventions: the `ghg-protocol` skill (GWP sets §4, EF
  hierarchy §7, data quality §8, answering style §9).
