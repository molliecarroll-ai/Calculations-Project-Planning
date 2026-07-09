#!/usr/bin/env python3
"""Build the tracker tabs workbook for the Calculations Roadmap Gantt.

Produces an .xlsx that is uploaded to Google Drive (converted to a Google
Sheet). Each tab is designed to be copied into the existing "Calculations
Roadmap Gannt" sheet via right-click tab -> Copy to -> Existing spreadsheet.

Content source: README.md in this repo (plan of record).
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
PHASE_FILL = PatternFill("solid", fgColor="D9E2F3")
HARD_FILL = PatternFill("solid", fgColor="FCE4D6")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
PHASE_FONT = Font(bold=True, size=11)
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

STATUS_LIST = '"Not started,In progress,On track,At risk,Blocked,Done"'
CP_STATUS_LIST = '"Upcoming,Held - on track,Held - actions needed,Missed"'
STAGE_LIST = '"Intake,Requirements,Build,Test & validate,Ship & enable,Post-ship,Done"'


def sheet(wb, title, headers, widths):
    ws = wb.create_sheet(title)
    for i, (h, w) in enumerate(zip(headers, widths), 1):
        c = ws.cell(row=1, column=i, value=h)
        c.fill, c.font, c.alignment = HEADER_FILL, HEADER_FONT, WRAP
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"
    return ws


def fill_rows(ws, rows, start=2):
    for r, row in enumerate(rows, start):
        for c, val in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.alignment, cell.border = WRAP, THIN
    return start + len(rows)


def add_dropdown(ws, col_letter, formula, last_row):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}2:{col_letter}{last_row}")


wb = Workbook()
wb.remove(wb.active)

# ---------------------------------------------------------------- READ ME
ws = sheet(wb, "READ ME", ["Calculations Roadmap - Plan, Checkpoints & Tracker"], [110])
readme = [
    "PURPOSE: Working tabs for the calcs & automations practice area. Companion to the 'Gannt' tab; plan of record lives in the Calculations-Project-Planning repo README.",
    "",
    "HOW TO GET THESE TABS INTO THE GANNT SHEET: open this file, right-click each tab -> 'Copy to' -> 'Existing spreadsheet' -> pick 'Calculations Roadmap Gannt'. (Drive API access used to create this file cannot edit the existing sheet directly.)",
    "",
    "TABS:",
    "  Step-by-Step Plan - every step from now to end of year, grouped by phase, with owner, who to engage, target date, and a status dropdown.",
    "  Checkpoints - the 7 project checkpoints (aligned to the biweekly Thursday sync). Each lists what to verify and what to decide.",
    "  Stakeholders - who on the broader Persefoni team to engage, for what, and when.",
    "  Progress Tracker - one row per roadmap item; the tab to update at every biweekly sync (stage, %, status, blockers, last updated).",
    "",
    "WORKING RHYTHM: update the Progress Tracker + relevant step statuses at the biweekly Mollie/Evan/Erin sync; walk the Checkpoints tab when a checkpoint date is reached; post a monthly snapshot to #cspa-calculations-and-automations.",
    "",
    "HARD DATES (highlighted orange throughout): Simplified electricity - Aug 31, 2026. In-platform gap filling (Liberty Mutual) - Dec 31, 2026.",
]
fill_rows(ws, [[t] for t in readme])

# ------------------------------------------------------- Step-by-Step Plan
ws = sheet(
    wb, "Step-by-Step Plan",
    ["Step", "What & exit criteria", "Owner (DRI)", "Engage", "Target", "Checkpoint", "Status"],
    [7, 58, 14, 30, 14, 11, 13],
)
P1 = [
    ["1.1", "Hold gap-filling requirements session: reconcile AI-built-tool learnings vs original PRD; split calcs vs advanced workstreams. Exit: agreed scope split.", "Mollie", "Suhayl, Tai, Evan, Erin", "Jul 7", "CP1", "Done"],
    ["1.2", "Ship spend-based waste: final front-end test + QA sign-off. Exit: live in prod, CS notified.", "Evan", "Vinh/Huyen (dev); Erin (pre-ship platform pass)", "Mid-Jul", "CP1", "In progress"],
    ["1.3", "Update gap-filling PRD (calcs workstream) from session outcomes. Exit: approved by Evan (feasibility) and Erin (customer fit).", "Mollie", "Suhayl, Tai", "Jul 23", "CP1", "In progress"],
    ["1.4", "Complete eGRID pipeline work (Snowflake/DevOps) and ship. Exit: subregion auto-assignment live.", "Evan", "Vinh", "End Jul-Aug", "CP2", "In progress"],
    ["1.5", "Finalize simplified electricity product guidance. Exit: guidance signed off, no open product questions.", "Mollie", "Product team, Evan, Erin", "Mid-Jul", "CP1", "In progress"],
    ["1.6", "Simplified electricity final dev + testing. Exit: QA sign-off from Evan.", "Evan", "Vinh, Huyen", "Aug 20", "CP2", "In progress"],
    ["1.7", "SHIP SIMPLIFIED ELECTRICITY - HARD DATE. Exit: live; Erin usability pass done; CS enablement note posted.", "Evan", "Erin", "Aug 31", "CP3", "Not started"],
    ["1.8", "Draft refrigerants / non-Kyoto requirements. Exit: PRD draft ready for review (passes requirements gate).", "Mollie", "Erin (methodology), Evan (feasibility)", "End Aug", "CP2", "Not started"],
    ["1.9", "Cat 11 scoping: collect AGCO + Tenneco methodology & sample data; join Daimler discussions; untangle region-varying efficiency values. Exit: data in hand, open methodology questions listed.", "Mollie", "Ben, Caroline, AGCO/Tenneco account teams, Evan", "Jul-Aug", "CP3", "In progress"],
    ["1.10", "August code freeze (platform outages): no new code starts; use the month for requirements, testing, validation.", "All", "-", "Aug", "-", "Not started"],
]
P2 = [
    ["2.1", "DEFRA telework go/no-go: Evan's PRD re-review complete AND window open between electricity ship and gap-filling start. Queue it if window closed.", "Evan", "Mollie", "Sep 3", "CP3", "Not started"],
    ["2.2", "DEFRA build + test (only if 2.1 = go).", "Evan", "Vinh/Huyen; Erin (platform review)", "Sep", "CP4", "Not started"],
    ["2.3", "Start gap-filling build. Exit: eng kicked off against approved PRD.", "Evan", "Vinh, Huyen", "~Sep 1", "CP3", "Not started"],
    ["2.4", "Gap-filling build with biweekly methodology validation against Liberty Mutual's actual use case.", "Evan", "Erin (validation), Mollie (PRD arbiter), Liberty Mutual account team", "Sep-Nov", "CP4-5", "Not started"],
    ["2.5", "Simplified combustion window decision: reconcile 2 vs 3 month estimate; confirm eng can carry it with light support only (else it slides).", "Evan", "Mollie", "Sep 3", "CP3", "Not started"],
    ["2.6", "Refrigerants start decision: requirements gate passed + light-support slot free (else Dec/Q1).", "Mollie", "Evan, Erin", "Oct 1", "CP4", "Not started"],
    ["2.7", "Gap-filling health check vs Liberty Mutual date. If at risk: pause everything else, both leads converge.", "Mollie", "Evan, Erin", "Oct 1", "CP4", "Not started"],
    ["2.8", "Draft Cat 11 PRD from validated three-account methodology (Daimler, AGCO, Tenneco).", "Mollie", "Erin, Evan, Ben, Caroline", "Oct", "CP5", "Not started"],
    ["2.9", "Cat 11 build decision: score against prioritization rubric; slot for Dec/Q1 if it ranks.", "Mollie", "Evan, Erin, eng", "Nov 12", "CP5", "Not started"],
]
P3 = [
    ["3.1", "GAP FILLING FINAL VALIDATION & DELIVERY TO LIBERTY MUTUAL - HARD DATE (end of year). Target internal done: Dec 17.", "Evan", "Erin, Liberty Mutual account team", "Dec 17 / Dec 31", "CP6-7", "Not started"],
    ["3.2", "CS enablement & docs for all 2026-shipped calcs (electricity, eGRID, spend waste, + fall ships).", "Erin", "Broader CS team, Mollie", "Dec", "CP7", "Not started"],
    ["3.3", "Re-score full backlog with rubric; publish 2027 H1 roadmap.", "Mollie", "Evan, Erin, product/eng leadership", "Dec 17", "CP7", "Not started"],
    ["3.4", "Start Cat 11 build if greenlit at CP5.", "Evan", "Vinh, Huyen", "Dec/Q1 2027", "-", "Not started"],
]
row = 2
for label, steps in [
    ("PHASE 1 - SHIP THE IN-FLIGHT WORK (Jul-Aug 2026)", P1),
    ("PHASE 2 - THE COMMITTED BUILDS (Sep-Nov 2026)", P2),
    ("PHASE 3 - DELIVER & RESET (Dec 2026 +)", P3),
]:
    cell = ws.cell(row=row, column=1, value=label)
    cell.font = PHASE_FONT
    for c in range(1, 8):
        ws.cell(row=row, column=c).fill = PHASE_FILL
    row = fill_rows(ws, steps, row + 1)
for r in (9, 26):  # hard-date rows: 1.7 and 3.1
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = HARD_FILL
add_dropdown(ws, "G", STATUS_LIST, row)

# ------------------------------------------------------------- Checkpoints
ws = sheet(
    wb, "Checkpoints",
    ["Checkpoint", "Date (biweekly Thu sync)", "What we verify", "Decisions to make", "Who's in the room", "Status", "Outcome / actions"],
    [11, 13, 48, 40, 28, 18, 30],
)
cps = [
    ["CP1", "Jul 23", "Spend-based waste shipped; gap-filling PRD updated & approved; eGRID ETA confirmed; electricity product guidance closed.", "Any scope changes to gap filling out of the Jul 7 session.", "Mollie, Evan, Erin", "Upcoming", ""],
    ["CP2", "Aug 20", "Electricity on track for Aug 31 (QA status); eGRID shipped; refrigerants PRD draft reviewed.", "Escalate electricity if at risk (hard date). Preliminary DEFRA go/no-go.", "Mollie, Evan, Erin (+Vinh if pipeline work open)", "Upcoming", ""],
    ["CP3", "Sep 3", "ELECTRICITY SHIPPED (hard-date verification); gap-filling code started; Cat 11 data collected.", "DEFRA final go/no-go. Combustion window decision (2 vs 3 mo reconciled).", "Mollie, Evan, Erin", "Upcoming", ""],
    ["CP4", "Oct 1", "Gap filling on track vs Liberty Mutual date; DEFRA done or queued; combustion progress if running.", "Refrigerants start decision. If gap filling at risk: pause everything else.", "Mollie, Evan, Erin", "Upcoming", ""],
    ["CP5", "Nov 12", "Gap filling entering test/validate; Cat 11 PRD drafted and scored.", "Cat 11 build decision (Dec/Q1 slot).", "Mollie, Evan, Erin + eng as needed", "Upcoming", ""],
    ["CP6", "Dec 10", "Gap-filling final validation plan; Liberty Mutual delivery logistics; CS enablement drafted.", "Confirm delivery date with Liberty Mutual account team.", "Mollie, Evan, Erin, LM account team", "Upcoming", ""],
    ["CP7", "Dec 17", "GAP FILLING DELIVERED (hard-date verification); 2026 retro; 2027 H1 roadmap published.", "2027 H1 commitments.", "Mollie, Evan, Erin, product/eng leadership", "Upcoming", ""],
]
last = fill_rows(ws, cps) - 1
for r in (4, 8):  # CP3, CP7 hard-date verifications
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = HARD_FILL
add_dropdown(ws, "F", CP_STATUS_LIST, last)

# ------------------------------------------------------------ Stakeholders
ws = sheet(
    wb, "Stakeholders",
    ["Name / group", "Role", "Why engaged (expertise)", "Engage for", "When"],
    [22, 26, 38, 44, 22],
)
stakeholders = [
    ["Mollie Carroll", "PM / requirements owner (CS)", "Methodologies, technical requirements", "All PRDs, prioritization, checkpoint facilitation, cross-team coordination", "Always"],
    ["Evan Kutter", "Calc support lead; directs eng", "Calculations engineering, testing, QA", "Build DRI on every major item; QA sign-off; directs Vinh & Huyen", "Always (~0.8 FTE plannable)"],
    ["Erin Dickinson", "Calc support lead", "Customer needs, platform use, methodologies", "Intake scoring (demand + CS time saved), methodology review, pre-ship usability pass", "Every item (~6 hrs/wk)"],
    ["Vinh", "Engineer (directed by Evan)", "Snowflake / DevOps pipeline; platform dev", "eGRID pipeline; electricity + gap-filling builds", "Per Evan's direction"],
    ["Huyen", "Engineer (directed by Evan)", "Platform dev", "Electricity, gap-filling, and fall builds", "Per Evan's direction"],
    ["Suhayl", "Gap-filling SME", "AI-built gap-filling tool learnings", "Requirements sessions; PRD review", "Jul (session held Jul 7) + as needed"],
    ["Tai Le", "Gap-filling SME", "Gap-filling requirements", "Requirements sessions; PRD review", "Jul + as needed"],
    ["Ben", "Daimler account", "Cat 11 customer context", "Daimler methodology/sample data; customer discussions", "Jul-Oct (Cat 11 scoping)"],
    ["Caroline Bartlett", "Daimler account", "Cat 11 customer context", "Daimler methodology/sample data; customer discussions", "Jul-Oct (Cat 11 scoping)"],
    ["AGCO & Tenneco account teams", "Account teams", "Cat 11 demand at their accounts", "Methodology + sample data (region-variable fuel use; weight apportioning)", "Jul-Aug"],
    ["Liberty Mutual account team", "Account team", "Gap-filling committed customer", "Use-case validation during build; delivery coordination", "Sep-Dec"],
    ["Product team (contact TBD)", "Product", "Product guidance & roadmap alignment", "Simplified electricity guidance (Jul); quarterly re-prioritization", "Jul; quarterly"],
    ["Broader CS team", "#cspa-calculations-and-automations", "Frontline customer workarounds", "Intake of new items (channel template); enablement on shipped calcs", "Ongoing; monthly snapshot"],
]
fill_rows(ws, stakeholders)

# -------------------------------------------------------- Progress Tracker
ws = sheet(
    wb, "Progress Tracker",
    ["Item", "Pipeline stage", "DRI", "% complete", "Priority score", "Hard date", "Next checkpoint", "Status", "Blockers / notes", "Last updated"],
    [26, 16, 18, 11, 12, 12, 12, 13, 42, 12],
)
items = [
    ["Spend-based waste", "Test & validate", "Evan", "85%", 2.95, "", "CP1 Jul 23", "On track", "Front end in dev/test; ships mid-Jul", "2026-07-08"],
    ["eGRID subregion assignment", "Build", "Evan", "70%", 3.20, "", "CP1 Jul 23", "On track", "Snowflake/DevOps pipeline pieces with Vinh", "2026-07-08"],
    ["Simplified electricity", "Build", "Evan", "60%", 4.35, "Aug 31, 2026", "CP2 Aug 20", "On track", "Needs product guidance closed; final dev + testing", "2026-07-08"],
    ["Simplified combustion", "Build (eng-led)", "Evan (light touch)", "50%", 3.15, "", "CP3 Sep 3", "Not started", "Reconcile 2 vs 3 month estimate; runs only if light-support", "2026-07-08"],
    ["Refrigerants / non-Kyoto", "Requirements", "Mollie (PRD) / Evan (build)", "25%", 2.80, "", "CP4 Oct 1", "Not started", "PRD to draft by end Aug; fails requirements gate until then", "2026-07-08"],
    ["DEFRA telework", "Requirements", "Evan", "20%", 2.55, "", "CP3 Sep 3", "In progress", "PRD re-review underway; go/no-go depends on Sep window", "2026-07-08"],
    ["In-platform gap filling", "Requirements", "Evan (build) / Mollie (PRD)", "0%", 4.35, "Dec 31, 2026", "CP1 Jul 23", "On track", "PRD update from Jul 7 session; code start ~Sep 1", "2026-07-08"],
    ["Category 11", "Intake / scoping", "Mollie", "0%", 2.85, "", "CP5 Nov 12", "In progress", "Collecting AGCO/Tenneco data; Daimler efficiency-value oddities open", "2026-07-08"],
]
last = fill_rows(ws, items) - 1
for r in (4, 9):  # hard-date items: electricity, gap filling
    for c in range(1, 11):
        ws.cell(row=r, column=c).fill = HARD_FILL
add_dropdown(ws, "B", STAGE_LIST, last)
add_dropdown(ws, "H", STATUS_LIST, last)

out = sys.argv[1] if len(sys.argv) > 1 else "tracker_tabs.xlsx"
wb.save(out)
print(f"wrote {out}")
