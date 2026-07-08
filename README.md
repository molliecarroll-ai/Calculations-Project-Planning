# Calculations Practice Area — Long-Term Implementation Plan

**Owner:** Mollie Carroll (project manager, calcs & automations practice area)
**Team:** Two calculations support leads (Evan, Erin) + product/engineering partners
**Source of record for items:** #cspa-calculations-and-automations · [Calculations Roadmap Gantt](https://docs.google.com/spreadsheets/d/1DOq0RLQGeCX5QxQsmL6d7h9nm0Jgpr4Mzivv7ie6AKk/edit?gid=0#gid=0)
**Last updated:** 2026-07-08

## Purpose

Prioritize Persefoni platform calculation improvements so that we (1) use engineering time efficiently, (2) respond to real customer needs, and (3) maximize time saved for the customer solutions team by replacing manual/Excel workarounds with in-platform capability.

---

## 1. Current Item Inventory (as of June 25 roadmap sync)

| # | Item | % Complete | Est. Duration | Target Window | Status / Notes |
|---|------|-----------|---------------|---------------|----------------|
| 1 | Spend-based waste | 85% | ~1 mo | July 2026 | Front end in dev/test; ships within weeks |
| 2 | eGRID subregion assignment | 70% | ~1.5 mo | Jul–Aug 2026 | Snowflake/DevOps pipeline pieces remain (Evan confirming with Vinh); can run concurrently with simplified electricity |
| 3 | Simplified electricity | 60% | ~4 mo total | End of July, Aug at latest | **Top priority.** Core components built; remaining: product guidance, final dev, testing |
| 4 | Simplified combustion | 50% | 2–3 mo ⚠️ | Sep–Nov 2026 | ⚠️ Sync said 2 months, Gantt says 3 — reconcile at next sync |
| 5 | Expanded refrigerant list / non-Kyoto reporting | 25% | ~2 mo | Oct–Nov 2026 | Builds on biogenic work, simpler (no activity/energy data, no density conversions). **Requirements not yet written** |
| 6 | DEFRA telework | 20% | ~1 mo | September 2026 | Evan re-reviewing PRD; sequenced after simplified electricity |
| 7 | In-platform gap filling | 0% | ~5 mo | Sep–Nov 2026 (code start ~Sep due to August outages) | **Hard commitment: Liberty Mutual end-of-year inventory.** Needs requirements session (Suhayl & Tai, set for Jul 7) to reconcile AI-built-tool learnings vs. original PRD and split calcs vs. advanced workstreams |
| 8 | Category 11 build | Unscoped | TBD | TBD (flagged on Gantt) | Demand at 3 accounts: Daimler (needs real platform build; odd region-varying efficiency values in sample data), AGCO (region-variable fuel-use assumptions), Tenneco (weight-apportioning for catalytic converters). Methodology/sample data collection in progress |

---

## 2. Prioritization Criteria (proposed, for internal discussion)

Score each candidate item 1–5 on six criteria. Weighted total drives rank order; discussion can override with a documented reason.

| Criterion | Weight | What it measures | Scoring guide (1 → 5) |
|-----------|--------|------------------|----------------------|
| **Customer commitment / deadline pressure** | 25% | Contractual or promised dates (e.g., Liberty Mutual EOY inventory) | No commitments → hard dated commitment at risk |
| **Breadth of customer demand** | 20% | How many accounts need it, and pipeline/renewal exposure | 1 account, nice-to-have → 3+ accounts or renewal-blocking (e.g., Cat 11 surfaced at 3 accounts in one week) |
| **CS time saved / workaround cost** | 20% | Hours/month CS spends on manual or Excel workarounds this would eliminate | Rare, quick workaround → recurring, error-prone, multi-hour workaround every inventory cycle |
| **Effort & readiness (inverse)** | 15% | Remaining engineering effort and how close it is to done | Large build, 0% started → small remaining effort, mostly done (rewards finishing in-flight work) |
| **Strategic / methodology leverage** | 10% | Reuses or unlocks other calc work (e.g., refrigerants building on biogenic) | One-off → foundation for multiple future calcs |
| **Accuracy & compliance risk** | 10% | Does the current gap create audit/assurance or data-quality exposure? | Cosmetic → material misstatement risk |

**Gates (pass/fail, independent of score):**

- **Requirements gate:** an item cannot enter the build queue without an approved PRD *and* validated sample/customer data. (This is what's currently blocking refrigerants and Cat 11, and what the Jul 7 session resolves for gap filling.)
- **Capacity gate:** an item cannot go active without a named DRI from the calc support team who has WIP headroom (see §3).

**Standing tie-breakers:** finish in-flight work before starting new work; prefer items that de-risk a dated customer commitment.

---

## 3. Capacity & Working Model (two calc support leads)

**Actual capacity (confirmed Jul 2026):** Evan is 100% dedicated to this work, but ~20% of that is reactive support → **~0.8 FTE of plannable roadmap capacity**. Erin is ~15% dedicated → **~6 hours/week**. Combined ≈ 0.95 FTE, heavily concentrated in one person. The model below is built around that asymmetry:

**Skills map (confirmed Jul 2026):**

| Person | Expertise | Standing role on every item |
|--------|-----------|------------------------------|
| Evan | Calculations engineering, testing, QA | Build DRI: owns dev collaboration, testing, and QA sign-off |
| Erin | Customer needs, platform use, methodologies | Voice of customer + methodology reviewer: validates that the item solves the real customer problem and works in actual platform workflows |
| Mollie | Methodologies, technical requirements | Requirements owner + PM: drafts/owns PRDs, runs prioritization, sequences the roadmap |

- **Evan is the primary DRI for major builds.** WIP limit: **1 active build-support item + 1 item in requirements/definition** at a time — never more. His schedule is planned at 80%, never 100%; the reactive load is real and permanent.
- **Erin's 15% is aimed at what only she covers:** customer-needs validation and platform-use review. Concretely: she scores the *breadth of demand* and *CS time saved* criteria at intake, sanity-checks methodology choices against how customers actually use the platform, and does the pre-ship usability pass. Testing/QA stays with Evan (his strength) — Erin should not spend her 6 hrs/week there, and she should not DRI a full build.
- **Mollie closes the requirements gate.** Since PRDs are the standing bottleneck (refrigerants, Cat 11, gap filling), requirements drafting is Mollie's lane, with Erin contributing methodology/customer input in bounded sessions and Evan reviewing for build feasibility.
- **Pairing is a scarce resource.** A pairing day consumes most of Erin's weekly allocation, so pair only in **scheduled, bounded sessions**: requirements workshops (gap filling, Cat 11), methodology sign-offs, and go/no-go reviews before ship. Day-to-day build support is solo (Evan) by default.
- **Continuity risk:** Evan is a single point of failure for the whole practice area. Mitigations: Erin reviews everything (so context is never single-homed), and every item must leave behind a written PRD + methodology note + test evidence — no tribal-knowledge ships.
- **Team-wide concurrency:** effectively **one major build at a time** on the support side, with a second item allowed only if its support burden is light (eng-heavy items where CS involvement is review/testing only).
- **Pipeline stages:** Intake → Scoping/Requirements → Build support → Test/validate → Ship & enable (docs, KB, CS training) → Post-ship check (did it actually reduce CS workaround time?).

---

## 4. Phased Long-Term Plan

### Phase 1 — Ship the in-flight work (July–August 2026)
- **Ship:** spend-based waste (July), eGRID subregion assignment (Jul–Aug), simplified electricity (end of July, Aug at latest — top priority).
- **Requirements:** hold the Jul 7 gap-filling session (Suhayl & Tai); update the PRD and split calcs vs. advanced workstreams. Draft refrigerant/non-Kyoto requirements so it can start on time in October.
- **Cat 11 scoping track (parallel, low intensity):** collect AGCO and Tenneco methodology/sample data; untangle Daimler's region-varying efficiency values; Mollie joins Daimler discussions with Ben & Caroline.
- **Constraint:** August outages — plan no new code starts in August; use the time for requirements, testing, and validation.

### Phase 2 — The committed builds (September–November 2026)

With ~0.8 FTE of plannable support capacity (Evan) + Erin's review hours, the four fall items must be **stack-ranked, not run in parallel**: **gap filling > DEFRA telework > simplified combustion > refrigerants.**

- **In-platform gap filling** (code start ~Sep) — Evan's active build through EOY (dev collaboration, testing, QA); protected top priority because of the Liberty Mutual commitment. Erin validates the methodology and the workflow against Liberty Mutual's actual use case; Mollie owns the updated PRD out of the Jul 7 session.
- **DEFRA telework** (~1 mo) — Evan runs it as his active build in the window between simplified-electricity ship and gap-filling code start (early Sep); if that window closes, it queues behind gap filling rather than running alongside it.
- **Simplified combustion** (Sep–Nov per Gantt) — proceeds in its window **only if engineering can carry it with light support involvement** (Erin methodology/platform review; Evan spot-check QA only). If it needs real support bandwidth, it slides. Reconcile the 2 vs. 3 month estimate first.
- **Refrigerants / non-Kyoto** (Oct–Nov) — starts only if the requirements gate passed in Phase 1 *and* combustion isn't already consuming the light-support slot; otherwise moves to Dec/Q1.
- Mid-phase checkpoint (early Oct): if gap filling is slipping against the Liberty Mutual date, everything else pauses and both leads converge on it — the dated commitment wins.

### Phase 3 — Category 11 and the next cycle (December 2026 →)
- **Category 11 build decision by November:** with methodology validated across Daimler/AGCO/Tenneco data, write the PRD in October, score it against the criteria in §2, and target a December/Q1 build start if it ranks (three-account demand suggests it will).
- **Run the first full re-prioritization cycle:** score all remaining + new intake items with the §2 rubric; publish the 2027 H1 roadmap.

### Ongoing operating cadence
| Cadence | What happens |
|---------|--------------|
| **Biweekly** — Mollie/Evan/Erin roadmap sync (existing) | Standing agenda: pipeline review by stage, blockers, score any new intake items, update % complete |
| **Monthly** | Update the Gantt sheet and post a status snapshot to #cspa-calculations-and-automations |
| **Quarterly** | Re-score the full backlog with product/engineering; confirm eng capacity; publish next-quarter commitments |
| **Continuous intake** | New candidate items get posted to the Slack channel with a short template: *what's the calc gap, which accounts, current workaround & CS hours, any deadline.* Scored at the next biweekly sync — nothing jumps the queue without a score |

---

## 5. Open Questions (for internal discussion)

1. ~~**Capacity reality**~~ — **Answered (Jul 2026):** Evan 100% dedicated with ~20% reactive (≈0.8 FTE plannable); Erin ~15% (≈6 hrs/wk). §3 and Phase 2 updated accordingly.
2. ~~**Skills split**~~ — **Answered (Jul 2026):** Evan = calc engineering/testing/QA; Erin = customer needs/platform use/methodologies; Mollie = methodologies/technical requirements. Skills map added to §3. Residual risk: no one besides Evan covers engineering/QA — written test evidence per item is the mitigation.
3. **Other dated commitments:** Liberty Mutual EOY is the only hard date captured. Are there other contractual or promised dates (Daimler? renewals tied to Cat 11?) that should raise an item's commitment score?
4. **Workaround cost data:** Do we have (or can we start tracking) CS hours spent per calc-area workaround? That evidence makes the 20% "CS time saved" criterion objective instead of anecdotal, and it's the best story for justifying eng investment.
5. **Engineering capacity:** Who commits eng bandwidth on the product side (Vinh's team?), and how many concurrent builds can they actually support? The plan assumes ~2 concurrent.
6. **Tooling:** Keep the Gantt sheet as the source of truth, or move item tracking to Jira/Confluence with the sheet as the executive view?
7. **Estimate discrepancy:** Simplified combustion — 2 months (sync notes) vs. 3 months (Gantt). Which is right?
