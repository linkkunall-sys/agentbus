#!/usr/bin/env python3
"""Render a client-grade one-page accessibility scan report.

Input   : a scan JSON produced by artifacts/scanner-a1-v1.py
          (schema: artifacts/scan-schema-a1-v1.json, scanner a1-v1)
Output  : a one-page Markdown report and a one-page print-ready HTML report.

Design rules enforced here, taken from the a3 work order:

  * No invented scan fields. Every fact read from the scan JSON is read from a
    field that exists in scan-schema-a1-v1.json. Nothing is inferred into a
    field the schema does not define.
  * Client-facing context the schema does not carry (entity name, contact
    block, exclusions) must be supplied on the command line. It is never
    guessed. Requested from a1-builder via the a3->a1 handoff.
  * The severity language table is used verbatim.
  * Acronyms are expanded on first use.
  * The "What we did not check" section is mandatory and cannot be suppressed.
  * The renderer refuses to write a client report whose contact block is still
    a placeholder. Use --allow-placeholders only for internal samples.

Exit codes: 0 ok · 2 bad input · 3 placeholder contact block refused.
"""

import argparse
import datetime
import html as htmllib
import json
import re
import sys

# --- House severity language. Verbatim from the a3 work order section 2.4. ---
SEVERITY_SENTENCE = {
    "critical": "An investor using a screen reader cannot complete this task at all.",
    "serious": "They can complete it, but only with difficulty and workarounds.",
    "moderate": "It works, but it is frustrating and slow for some users.",
    "minor": "It causes an annoyance, not a failure.",
}
SEVERITY_FEELING = {
    "critical": "Compliance and reputational exposure today",
    "serious": "Will be found in an audit",
    "moderate": "Worth fixing in the next release",
    "minor": "Low priority, still listed",
}
SEVERITY_ORDER = {"critical": 0, "serious": 1, "moderate": 2, "minor": 3}

# --- Acronyms, expanded on first use. The work order names these explicitly. ---
ACRONYMS = {
    "WCAG": "Web Content Accessibility Guidelines",
    "PDF/UA": "PDF Universal Accessibility",
    "IAAP": "International Association of Accessibility Professionals",
    "RPwD": "Rights of Persons with Disabilities",
}

# --- Human, consequence-led headings for known rules. The schema carries a rule
# --- id, not a heading. This map is a3 editorial work, not scan data. Rules with
# --- no entry here render a flagged placeholder for a human to word, never an
# --- auto-invented claim.
RULE_HEADINGS = {
    "image-alt": "Blind investors are told nothing about this image",
    "label": "Investors using screen readers cannot tell what this field is for",
    "button-name": "A button announces no purpose",
    "frame-title": "Embedded content is announced with no name",
    "td-headers": "Table data has no headings, so relationships are unclear",
    "link-name": "A link announces no destination",
    "html-has-lang": "The page does not declare its language",
    "heading-order": "The page outline skips a level",
    "keyboard": "A menu control cannot be operated from the keyboard",
    "color-contrast": "Text is hard to distinguish from its background",
}

# --- Effort vocabulary is fixed by the work order: small / medium / large. ---
EFFORT_LABEL = {"small": "small", "medium": "medium", "large": "large"}

BUDGETS = {
    "what_we_checked": 60,
    "three_fixes": 220,
    "what_we_did_not_check": 70,
    "what_happens_next": 50,
}

# --- Page geometry for the one-page check. Must match the CSS in render_html. ---
MM = 2.834645  # mm -> pt
PAGE_W_MM, PAGE_H_MM = 210.0, 297.0      # A4
MARGIN_MM = 12.0
REM_PT = 9.6                             # html { font-size: 9.6pt }
LINE = 1.34                              # body line-height
COL_FRACTIONS = [0.045, 0.20, 0.17, 0.15, 0.23, 0.06, 0.145]


def estimate_layout(md):
    """Estimate rendered height in mm from real Helvetica font metrics.

    This is a measurement model, not a print render: it assumes the browser uses
    Helvetica/Arial metrics at the point sizes declared in the report CSS and
    lays the table out with the column fractions above. It is accurate enough to
    catch a report that will spill onto a second page, and it is clearly a
    better guide than counting words. It does not replace one print check by a
    human before the first client send.

    Requires reportlab (dev-time only). Returns (height_mm, usable_mm) or None.
    """
    try:
        from reportlab.pdfbase.pdfmetrics import stringWidth  # type: ignore
    except ImportError:
        return None

    usable_w = (PAGE_W_MM - 2 * MARGIN_MM) * MM
    usable_h = (PAGE_H_MM - 2 * MARGIN_MM) * MM

    def wrapped(text, size, width):
        words_left = text.split()
        if not words_left:
            return 1
        lines, cur = 1, ""
        for word in words_left:
            trial = (cur + " " + word).strip()
            if stringWidth(trial, "Helvetica", size) <= width:
                cur = trial
            else:
                lines += 1
                cur = word
        return lines

    height = 0.0
    in_table = False
    header_done = False
    for ln in md.splitlines():
        s = ln.strip()
        if not s or s == "---":
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if not in_table:
                in_table = True
                height += 9.5 * 1.15  # header row
                continue
            size = 0.74 * REM_PT
            row_lines = 1
            for cell, frac in zip(cells, COL_FRACTIONS):
                row_lines = max(row_lines, wrapped(cell, size, frac * usable_w))
            height += row_lines * size * LINE + 2 * 0.24 * REM_PT + 0.75
        elif s.startswith("## "):
            in_table = False
            height += 1 * REM_PT + 0.3 * REM_PT + 0.16 * REM_PT + 0.75 + LINE * 0.82 * REM_PT
        elif s.startswith("# "):
            height += 1.5 * REM_PT * 1.2 + 0.35 * REM_PT
        elif re.match(r"^\d+\.\s\*\*", s):
            height += wrapped(s, REM_PT, usable_w) * REM_PT * LINE + 0.28 * REM_PT
        elif s.startswith("- "):
            height += wrapped(s[2:], REM_PT, usable_w) * REM_PT * LINE + 0.3 * REM_PT
        else:
            height += wrapped(s, REM_PT, usable_w) * REM_PT * LINE + 0.45 * REM_PT
    return height / MM, usable_h / MM



def plural(n, singular, many=None):
    """'1 page' / '2 pages' — client-facing copy should not read '1 page(s)'."""
    return f"{n} {singular if n == 1 else (many or singular + 's')}"


def words(text):
    """Count words in a fragment, ignoring Markdown table pipes and bullets."""
    plain = re.sub(r"[|*_`#>\[\]()]", " ", text)
    return len([w for w in plain.split() if re.search(r"[A-Za-z0-9]", w)])


def expand_acronyms(text):
    """Expand each acronym on its first use in the document."""
    for short, long_form in ACRONYMS.items():
        pattern = re.compile(r"(?<![\w/])" + re.escape(short) + r"(?![\w])")
        if pattern.search(text):
            text = pattern.sub(f"{long_form} ({short})", text, count=1)
    return text


def load_scan(path):
    with open(path, encoding="utf8") as fh:
        data = json.load(fh)
    for key in ("scan", "summary", "findings"):
        if key not in data:
            raise ValueError(f"scan JSON is missing the top-level key '{key}'")
    return data


def severity(impact):
    return impact if impact in SEVERITY_SENTENCE else "moderate"


def finding_heading(f):
    rule = f.get("rule", "")
    if rule in RULE_HEADINGS:
        return RULE_HEADINGS[rule], True
    return f"{{{{HEADING NEEDED for rule '{rule}'}}}}", False


def consequence(f):
    """One finding = heading + ~40 words of consequence. Leads with the human
    consequence, never with the rule reference."""
    sev = severity(f.get("impact"))
    parts = [SEVERITY_SENTENCE[sev]]
    what = (f.get("what_happens") or "").strip()
    who = (f.get("who_is_affected") or "").strip()
    if what:
        parts.append(what if what.endswith(".") else what + ".")
    if who:
        parts.append(f"Affects: {who}.")
    return " ".join(parts)


def what_it_would_take(f):
    effort = EFFORT_LABEL.get((f.get("effort") or "").strip().lower(), "to be assessed")
    fix = (f.get("how_to_fix") or "").strip()
    if fix and not fix.endswith("."):
        fix += "."
    return f"Effort: {effort}. {fix}".strip()


def ref_for_devs(f, internal):
    refs = ", ".join(f.get("wcag") or [])
    level = f.get("level") or ""
    rule = f.get("rule") or ""
    bits = []
    if refs:
        bits.append(f"WCAG {refs}" + (f" ({level})" if level else ""))
    if internal and rule:
        bits.append(f"rule {rule}")
    return " · ".join(bits) if bits else "—"


def finding_where(f):
    page = f.get("page") or ""
    sel = f.get("selector") or ""
    page = re.sub(r"^https?://", "", page).rstrip("/")
    where = page if page else "—"
    if sel:
        # Plain ASCII separator: the arrow glyph is missing from common PDF base
        # fonts and renders as a blank box, which would be an accessibility defect
        # in an accessibility report.
        where += f" · element {sel}"
    return where


def context_exclusions(behind_login, out_of_scope):
    """Build the mandatory 'what we did not check' text.

    The default statement is grounded in artifacts/stack-facts-a1-v1.md, which
    states the scanner does not submit forms or use login credentials. Anything
    the operator adds is used verbatim; nothing is inferred about pages we have
    not been told about."""
    lines = [
        "Pages behind a login were not checked, because the scanner submits no forms "
        "and uses no credentials.",
    ]
    if behind_login:
        lines.append("Not reachable in this scan: " + "; ".join(dict.fromkeys(behind_login)) + ".")
    if out_of_scope:
        lines.append("Out of scope by agreement: " + "; ".join(dict.fromkeys(out_of_scope)) + ".")
    lines.append(
        "This is an automated scan of publicly accessible pages. It finds a subset of issues "
        "and does not replace testing with a person using a screen reader."
    )
    return " ".join(lines)


def render_full_findings(scan, path, internal):
    """Write every finding, uncut, as the companion file the one-pager refers to.

    The one-page report caps its table to keep to a single page; this file is
    where the uncut list lives, so nothing is ever dropped silently."""
    rows = ["| # | Severity | What it is | Where | Who it affects | How to fix | Effort | For developers |",
            "|---|---|---|---|---|---|---|---|"]
    findings = sorted(scan["findings"],
                      key=lambda f: (SEVERITY_ORDER[severity(f.get("impact"))], f.get("id", "")))
    for f in findings:
        heading, _ = finding_heading(f)
        rows.append("| {id} | {sev} | {what} | {where} | {who} | {fix} | {effort} | {ref} |".format(
            id=f.get("id", "—"),
            sev=severity(f.get("impact")),
            what=heading,
            where=finding_where(f),
            who=f.get("who_is_affected") or "—",
            fix=f.get("how_to_fix") or "—",
            effort=f.get("effort") or "—",
            ref=ref_for_devs(f, internal),
        ))
    s = scan["scan"]
    header = (f"# Full findings — all {len(findings)}\n\n"
              f"Scanner {s.get('scanner_version','—')} · {s.get('pages_scanned',0)} page(s) scanned · "
              f"{s.get('pages_failed',0)} page(s) failed · companion to the one-page scan report.\n\n"
              "Findings are ordered worst first. Effort is our estimate (small / medium / large).\n")
    with open(path, "w", encoding="utf8") as fh:
        fh.write(header + "\n" + "\n".join(rows) + "\n")
    return path


def render_markdown(scan, args, internal):
    s, summ, findings = scan["scan"], scan["summary"], scan["findings"]
    entity = args.entity
    platform = args.platform or s.get("url", "")
    date = args.date
    out = []
    # Header, three lines: entity · platform and date · who we are. No logo theatre.
    out.append(f"# Accessibility scan report — {entity}")
    out.append("")
    out.append(f"Platform scanned: {platform} · Scan date: {date}")
    out.append("")
    who_we_are = args.company if not args.prepared_by else f"{args.prepared_by}, {args.company}"
    out.append(f"Prepared by {who_we_are} · {args.contact_email}")
    out.append("")

    # What we checked
    pages = sorted({re.sub(r"^https?://", "", (f.get("page") or "")).rstrip("/")
                    for f in findings if f.get("page")})
    if not pages and s.get("url"):
        pages = [re.sub(r"^https?://", "", s["url"]).rstrip("/")]
    shown, extra = pages[:5], max(0, len(pages) - 5)
    included = ", ".join(shown) if shown else "the platform's public entry page"
    if extra:
        included += f", and {extra} further page(s)"
    total = summ.get("total_findings", 0)
    scanned_n, failed_n = s.get("pages_scanned", 0), s.get("pages_failed", 0)
    failed_note = "" if not failed_n else f" {plural(failed_n, 'page')} could not be scanned."
    checked = (f"{plural(scanned_n, 'publicly accessible page was', 'publicly accessible pages were')} "
               f"scanned with scanner {s.get('scanner_version','—')}, including {included}."
               f"{failed_note} "
               f"{plural(total, 'finding was', 'findings were')} recorded.")
    if internal:
        checked += " [RES]"
    out.append("## What we checked")
    out.append("")
    out.append(checked)
    out.append("")

    # The three things to fix first
    top_ids = summ.get("top_three") or []
    by_id = {f.get("id"): f for f in findings}
    top = [by_id[i] for i in top_ids if i in by_id]
    if not top:
        top = sorted(findings, key=lambda f: SEVERITY_ORDER[severity(f.get("impact"))])[:3]
    out.append("## The three things to fix first")
    out.append("")
    if not top:
        out.append("No findings were recorded. That is a result, not a clearance: automated "
                   "scanning covers a subset of the Accessibility Guidelines, and manual and "
                   "screen-reader testing is still required.")
        out.append("")
    for n, f in enumerate(top, 1):
        heading, ok = finding_heading(f)
        line = f"{n}. **{heading}**" if ok else f"{n}. **{heading}**"
        out.append(line)
        body = f"{consequence(f)} {what_it_would_take(f)}"
        if internal:
            body += f" [RES on the finding, EXP on the effort estimate]"
        out.append(body)
        out.append("")

    # Full findings
    out.append("## Full findings")
    out.append("")
    if not findings:
        out.append("No findings were recorded in this scan.")
        out.append("")
    else:
        out.append("| # | What it is | Where | Who it affects | How to fix | Effort | For developers |")
        out.append("|---|---|---|---|---|---|---|")
        ranked = sorted(findings, key=lambda f: (SEVERITY_ORDER[severity(f.get("impact"))], f.get("id", "")))
        cap = args.max_table_rows
        for f in ranked[:cap]:
            heading, _ = finding_heading(f)
            out.append("| {id} | {what} | {where} | {who} | {fix} | {effort} | {ref} |".format(
                id=f.get("id", "—"),
                what=heading,
                where=finding_where(f),
                who=f.get("who_is_affected") or "—",
                fix=f.get("how_to_fix") or "—",
                effort=f.get("effort") or "—",
                ref=ref_for_devs(f, internal),
            ))
        out.append("")
        if len(ranked) > cap:
            # One page is the hard constraint; the middle section is what gets cut,
            # never the two closing sections. Nothing is dropped silently.
            out.append(f"The table lists the {cap} highest-severity findings. "
                       f"All {len(ranked)} findings, including the remaining "
                       f"{len(ranked) - cap}, are listed in full in the companion findings file "
                       f"supplied with this report.")
            out.append("")

    # Mandatory section. Never suppressed.
    out.append("## What we did not check")
    out.append("")
    note = context_exclusions(args.behind_login, args.out_of_scope)
    if internal:
        note += " [RES: scanner does not submit forms or use credentials — stack-facts-a1-v1.md]"
    out.append(note)
    out.append("")

    # What happens next
    out.append("## What happens next")
    out.append("")
    out.append("We can fix these findings, re-scan to confirm each one is closed, and set up "
               "monitoring so new pages are checked as they ship. The annual accessibility audit "
               "the regulator expects then falls out of the same cycle. Reply to this email and "
               "we will scope the first batch.")
    out.append("")

    # Contact, exactly four lines
    out.append("## Contact")
    out.append("")
    out.append(args.contact_name)
    out.append(args.contact_email)
    out.append(args.contact_phone)
    out.append(f"{args.prepared_by} · {date}")
    out.append("")

    if internal:
        out.append("---")
        out.append("")
        out.append("## Internal only — do not send")
        out.append("")
        out.append("Claim labels, checked by a4-qa before release:")
        out.append("")
        out.append("- **[RES]** every finding, count, page and severity is read directly from the "
                   "scan JSON produced by scanner a1-v1. Reproduce with the command in the template.")
        out.append("- **[RES]** 'pages behind a login were not checked' follows from the scanner's "
                   "own documented behaviour in stack-facts-a1-v1.md: it submits no forms and uses "
                   "no credentials.")
        out.append("- **[RES]** 'finds a subset of issues and does not replace testing with a person' "
                   "repeats the scanner's own output text ('automated results require human "
                   "confirmation') and does not assert a detection percentage.")
        out.append("- **[EST]** 'the annual accessibility audit the regulator expects' rests on the "
                   "audited SEBI annual-schedule position in claims-audit-a4-v1.md, claim 6. "
                   "This report deliberately carries no deadline date, no penalty figure and no "
                   "fixed standards version, because those must use a4-qa's audited wording.")
        out.append("- **[EXP]** every effort estimate (small / medium / large) is our professional "
                   "judgement, not a benchmark.")
        out.append("- No cost figures appear anywhere in this report, by design. Pricing is quoted "
                   "after the scan, never before (see escalation A4-C08: an unlabelled cost range "
                   "is a release blocker).")
        out.append("")

    md = "\n".join(out)
    return expand_acronyms(md)


def render_html(md, args, internal):
    """Minimal, print-ready one-page HTML. No logo, no decoration."""
    esc = htmllib.escape
    lines = md.splitlines()
    body = []
    in_table = False
    for ln in lines:
        if ln.startswith("# "):
            body.append(f"<h1>{esc(ln[2:])}</h1>")
        elif ln.startswith("## "):
            if in_table:
                body.append("</tbody></table>")
                in_table = False
            body.append(f"<h2>{esc(ln[3:])}</h2>")
        elif ln.startswith("|"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if not in_table:
                body.append('<table><thead>')
                body.append("<tr>" + "".join(f"<th>{esc(c)}</th>" for c in cells) + "</tr>")
                body.append("</thead><tbody>")
                in_table = True
            else:
                body.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in cells) + "</tr>")
        elif ln.strip() == "---":
            pass
        elif ln.strip() == "":
            continue
        elif re.match(r"^\d+\.\s", ln.strip()):
            body.append(f"<p class='finding'>{esc(ln.strip())}</p>")
        elif ln.strip().startswith("- "):
            body.append(f"<p class='bullet'>{esc(ln.strip()[2:])}</p>")
        else:
            body.append(f"<p>{esc(ln)}</p>")
    if in_table:
        body.append("</tbody></table>")

    banner = ""
    if args.allow_placeholders:
        banner = ("<div class='sample'>SAMPLE RENDER — not a client report. "
                  "Contact details are placeholders and the scan is a fixture page.</div>")

    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<title>Accessibility scan report — {esc(args.entity)}</title>
<style>
  @page {{ size: A4; margin: 12mm; }}
  html {{ font-size: 9.6pt; }}
  body {{ font-family: "Helvetica Neue", Arial, sans-serif; color: #16181d; line-height: 1.34; margin: 0; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 .35rem; letter-spacing: -.01em; }}
  h2 {{ font-size: .82rem; text-transform: uppercase; letter-spacing: .07em;
        margin: 1rem 0 .3rem; color: #4a5160; border-bottom: 1px solid #dfe2e8; padding-bottom: .16rem; }}
  p {{ margin: 0 0 .45rem; }}
  p.finding {{ margin: 0 0 .5rem; }}
  p.bullet {{ margin: 0 0 .3rem; }}
  table {{ width: 100%; border-collapse: collapse; margin: .3rem 0 .5rem; }}
  th, td {{ text-align: left; vertical-align: top; padding: .24rem .34rem;
            border-bottom: 1px solid #e6e9ee; font-size: .74rem; }}
  th {{ background: #f4f6f9; font-weight: 600; }}
  .sample {{ background: #fff4e0; border: 1px solid #e8b866; padding: .4rem .5rem;
             margin-bottom: .6rem; font-weight: 600; font-size: .8rem; }}
  section, .page {{ page-break-inside: avoid; }}
</style>
</head>
<body>
{banner}
{"".join(body)}
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Render a one-page client scan report from a1-v1 scan JSON.")
    ap.add_argument("--scan", required=True, help="path to scan JSON from artifacts/scanner-a1-v1.py")
    ap.add_argument("--entity", required=True, help="client entity name as it should appear on the report")
    ap.add_argument("--platform", default="", help="platform URL scanned (defaults to scan.url)")
    ap.add_argument("--date", default=datetime.date.today().strftime("%d %B %Y"),
                    help="report date, DD Month YYYY (default: today)")
    ap.add_argument("--prepared-by", default="{{FOUNDER_NAME}}")
    ap.add_argument("--company", default="{{COMPANY_NAME}}",
                    help="our company name as it appears in the header's 'who we are' line")
    ap.add_argument("--contact-name", default="{{FOUNDER_NAME}}")
    ap.add_argument("--contact-email", default="{{FOUNDER_EMAIL}}")
    ap.add_argument("--contact-phone", default="{{FOUNDER_PHONE}}")
    ap.add_argument("--behind-login", action="append", default=[],
                    help="repeatable: name a login-gated area that was not checked")
    ap.add_argument("--out-of-scope", action="append", default=[],
                    help="repeatable: name something explicitly out of scope")
    ap.add_argument("--internal", action="store_true",
                    help="append the internal claim-label block for a4-qa")
    ap.add_argument("--out", default="", help="Markdown output path")
    ap.add_argument("--html", default="", help="HTML output path")
    ap.add_argument("--full-findings", default="",
                    help="write every finding, uncut, as the companion file the report refers to")
    ap.add_argument("--no-fit", action="store_true",
                    help="do not auto-fit the findings table to one page; use --max-table-rows as given")
    ap.add_argument("--allow-placeholders", action="store_true",
                    help="write an internal sample even though the contact block is a placeholder")
    ap.add_argument("--check", action="store_true", help="print section word budgets and exit")
    ap.add_argument("--check-layout", action="store_true",
                    help="estimate rendered height in mm from font metrics (needs reportlab)")
    ap.add_argument("--max-table-rows", type=int, default=12,
                    help="cap rows in the full findings table so the report keeps to one page "
                         "(default 12; the report states how many findings were moved)")
    args = ap.parse_args()

    # Refuse to emit a client report with an unfilled contact block. This is the
    # guard for the work order rule that the client report carries real details.
    placeholder = re.compile(r"\{\{.*?\}\}")
    contact_text = " ".join([args.contact_name, args.contact_email, args.contact_phone,
                             args.prepared_by, args.company])
    if placeholder.search(contact_text) and not args.allow_placeholders:
        print("REFUSED: the contact block still contains a placeholder "
              f"({placeholder.search(contact_text).group(0)}).\n"
              "Fill --contact-name/--contact-email/--contact-phone/--prepared-by, or pass "
              "--allow-placeholders for an internal sample only.", file=sys.stderr)
        return 3

    try:
        scan = load_scan(args.scan)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"REFUSED: could not read the scan JSON: {exc}", file=sys.stderr)
        return 2

    # Auto-fit the findings table to one page. The work order is explicit that one
    # page wins and the middle section is what gets cut, never the closing two.
    # Nothing is dropped silently: whatever is cut is named in the report and
    # written in full to --full-findings.
    if not args.no_fit:
        ceiling = min(args.max_table_rows, len(scan["findings"]))
        chosen, note = ceiling, None
        for cap in range(ceiling, -1, -1):
            args.max_table_rows = cap
            candidate = render_markdown(scan, args, args.internal)
            est = estimate_layout(candidate)
            if est is None:
                note = ("Auto-fit skipped: reportlab is not installed, so the one-page fit is "
                        "UNVERIFIED. Run: python3 -m pip install reportlab")
                chosen = ceiling
                break
            height_mm, usable_mm = est
            if height_mm <= 0.96 * usable_mm:
                chosen = cap
                break
            chosen = cap
        else:
            note = ("Auto-fit reached 0 table rows and the report still does not fit one page. "
                    "Shorten the 'three things to fix first' section before sending.")
        args.max_table_rows = chosen
        if note:
            print(f"WARNING: {note}", file=sys.stderr)

    md = render_markdown(scan, args, args.internal)

    if args.check:
        sections = {
            "what_we_checked": md.split("## What we checked")[1].split("##")[0],
            "three_fixes": md.split("## The three things to fix first")[1].split("## Full findings")[0],
            "what_we_did_not_check": md.split("## What we did not check")[1].split("##")[0],
            "what_happens_next": md.split("## What happens next")[1].split("##")[0] if not args.internal
                                 else md.split("## What happens next")[1].split("---")[0],
        }
        for key, budget in BUDGETS.items():
            n = words(sections[key])
            flag = "OK" if n <= budget else "OVER"
            print(f"{flag:4} {key:24} {n:4} words (budget {budget})")

    if args.check_layout:
        est = estimate_layout(md)
        if est is None:
            print("LAYOUT CHECK SKIPPED: reportlab not installed "
                  "(python3 -m pip install reportlab).", file=sys.stderr)
        else:
            height_mm, usable_mm = est
            pct = 100 * height_mm / usable_mm
            verdict = "FITS" if height_mm <= usable_mm else "OVERFLOWS"
            print(f"{verdict} one A4 page (estimated): {height_mm:.0f}mm of {usable_mm:.0f}mm "
                  f"usable ({pct:.0f}%), from Helvetica font metrics. "
                  f"This is an estimate; confirm with one print before the first client send.")

    if args.out:
        with open(args.out, "w", encoding="utf8") as fh:
            fh.write(md + "\n")
        print(f"wrote {args.out}")
    if args.full_findings:
        render_full_findings(scan, args.full_findings, args.internal)
        print(f"wrote {args.full_findings}")
    if args.html:
        with open(args.html, "w", encoding="utf8") as fh:
            fh.write(render_html(md, args, args.internal))
        print(f"wrote {args.html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
