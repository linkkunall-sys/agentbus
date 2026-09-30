# Client scan report — template and rules (a3, v1)

- **Owner:** a3-content
- **Task:** T-20260929-write-the-client-grade-2750
- **Written:** 01 October 2026
- **Renders from:** `artifacts/scan-schema-a1-v1.json` (scanner a1-v1)
- **Renderer:** `scripts/render-scan-report.py`
- **Tested against:** `artifacts/scan-fixture-output-a3-v1.json` — a real scan, produced by a1-builder's own analyzer from a1's fixture page

This is the report that *is* the free 48-hour scan. It is written for a compliance officer with eight minutes
and no technical background. One page. Read once, name the three fixes, act.

---

## 1. The one-page rule

One page is a hard limit. The work order says what to sacrifice when it is tight: **cut the middle, never the
last two sections.**

In practice that means the full findings table is the first thing to shrink; *What we did not check* and
*What happens next* are never cut. The renderer enforces this rather than trusting the author:

- It auto-fits the findings table to one page, dropping rows from the bottom of the severity ranking.
- Whatever it drops is stated in the report ("The table lists the 6 highest-severity findings...") and
  written out in full in the companion findings file. **Nothing disappears silently.**
- If the report still does not fit after the table is empty, it warns you to shorten the top-three section.

## 2. What this template binds to, and what it refuses to invent

The work order is explicit: render from the schema, do not invent fields. Here is the complete binding.

| Report slot | Read from (schema field) |
|---|---|
| Platform scanned | `scan.url` |
| Scan date shown in the header | supplied on the command line, `--date` |
| Pages scanned | `scan.pages_scanned` |
| Pages that could not be scanned | `scan.pages_failed` |
| Scanner version | `scan.scanner_version` |
| Total findings recorded | `summary.total_findings` |
| Which three get top billing | `summary.top_three` (ids, resolved against `findings[].id`) |
| Severity of a finding | `findings[].impact` |
| Consequence text | `findings[].what_happens` |
| Who it affects | `findings[].who_is_affected` |
| How to fix | `findings[].how_to_fix` |
| Effort | `findings[].effort` |
| Where it is | `findings[].page` + `findings[].selector` |
| Page list in *What we checked* | distinct `findings[].page` |
| Rule reference for developers | `findings[].wcag` + `findings[].level` |

### Fields the report needs that the schema does not have

These are **not** faked and **not** written into the scan JSON. They are supplied at render time, and the
ones that belong in the scan are requested from a1-builder in
`artifacts/a3-handoff-a1-schema-fields.md`:

| Needed by the report | Why it cannot come from the schema | How it is supplied today |
|---|---|---|
| Entity name | Not in the scan | `--entity` |
| Who we are (our company) | Not in the scan | `--company` |
| Contact name, email, phone | Not in the scan | `--contact-name`, `--contact-email`, `--contact-phone` |
| Pages deliberately excluded | The scanner cannot know our engagement scope | `--out-of-scope` (repeatable) |
| Named login-gated areas | The scanner cannot know what is behind a login | `--behind-login` (repeatable) |
| A human heading per finding | The schema carries a rule id, not a sentence | a 10-rule heading map inside the renderer, plus a loud placeholder for any rule not in the map |

Two wording choices in the schema need a decision from a1-builder, both raised in the handoff:

1. **`impact` vs severity wording.** `scan-schema-a1-v1.json` shows `image-alt` with `impact: "critical"`,
   while `scanner-a1-v1.py` emits `serious` for the same rule. The schema example and the code disagree.
2. **`verified` is always `false`.** Every emitted finding is unverified. The template must never imply a
   human has confirmed a finding, so it says "automated scan" wherever the distinction matters.

## 3. The seven sections, in order

| # | Section | Budget | Status in v1 |
|---|---|---|---|
| 1 | Header — entity · platform and date · who we are | 3 lines | Enforced, exactly 3 lines |
| 2 | What we checked | 60 words | Enforced by the word-budget check |
| 3 | The three things to fix first | 220 words | Enforced by the word-budget check |
| 4 | Full findings | table | Auto-fitted to one page; companion file carries all |
| 5 | What we did not check | 70 words | Mandatory — the renderer cannot omit it |
| 6 | What happens next | 50 words | Enforced; one clear ask, no pressure |
| 7 | Contact | 4 lines | Enforced; refuses to render placeholders |

Rules that apply throughout:

- **Every acronym is expanded on first use.** The renderer does this automatically for WCAG, PDF/UA, IAAP
  and RPwD. WCAG is spelled out as Web Content Accessibility Guidelines (WCAG) at first use.
- **Lead with the human consequence.** The rule reference sits in a narrow "For developers" column, never
  in the opening sentence.
- **No fear-mongering, no overclaiming.** The report describes what is broken. It makes no prediction about
  penalties, audits or enforcement.

## 4. Severity language — use these words, exactly

Severity comes from `findings[].impact`. The sentence is chosen by severity and is fixed.

| Technical severity | The report says | What the reader should feel |
|---|---|---|
| critical | "An investor using a screen reader cannot complete this task at all." | Compliance and reputational exposure today |
| serious | "They can complete it, but only with difficulty and workarounds." | Will be found in an audit |
| moderate | "It works, but it is frustrating and slow for some users." | Worth fixing in the next release |
| minor | "It causes an annoyance, not a failure." | Low priority, still worth listing |

The severity sentence is followed by the finding's own `what_happens` and `who_is_affected`, keeping the
whole consequence block to roughly 40 words. "Effort: small / medium / large" then closes it.

## 5. Guards built into the renderer

These exist because the failure modes are real, not hypothetical.

1. **The placeholder guard.** If the contact block still contains `{{...}}`, the renderer refuses to write
   the report and exits with code 3. `--allow-placeholders` overrides it for internal samples only. This is
   what stops a report going out with an unfilled contact footer.
2. **The missing-scan guard.** A scan file that cannot be read, or that is missing `scan`, `summary` or
   `findings`, exits with code 2 rather than rendering a half-empty report.
3. **The one-page check.** `--check-layout` estimates the rendered height in millimetres from real
   Helvetica font metrics and prints FITS or OVERFLOWS.
4. **The word-budget check.** `--check` prints each section's word count against its budget.
5. **No cost figures, ever.** Pricing is quoted after the scan, never before. This also keeps the report
   clear of escalation A4-C08, where an unlabelled cost range is a release blocker.

## 6. The internal version and claim labels

`--internal` appends a clearly separated block headed *Internal only — do not send*. It carries the
[EST] / [RES] / [EXP] labels that a4-qa checks before anything goes out. Nothing in that block is written
for the client.

The labels currently asserted:

| Label | Applied to | Basis |
|---|---|---|
| [RES] | Every finding, count, page and severity | Read directly from the scan JSON |
| [RES] | "Pages behind a login were not checked" | The scanner's documented behaviour: it submits no forms, uses no credentials (`stack-facts-a1-v1.md`) |
| [RES] | "Finds a subset of issues and does not replace testing with a person" | The scanner's own output text, "automated results require human confirmation"; no detection percentage is claimed |
| [EST] | "The annual accessibility audit the regulator expects" | The audited annual-schedule position, `claims-audit-a4-v1.md` claim 6 |
| [EXP] | Every effort estimate | Our professional judgement, not a benchmark |

**Deliberately absent from the report:** any deadline date, any penalty figure, and any fixed standards
version. Those must use a4-qa's audited wording and nothing else.

## 7. Tested against a real scan

The template was rendered against `artifacts/scan-fixture-output-a3-v1.json` — 10 findings from a1-builder's
analyzer run over a1's own fixture page. Reproduce it exactly:

```sh
python3 scripts/render-scan-report.py \
  --scan artifacts/scan-fixture-output-a3-v1.json \
  --entity "SAMPLE - a1-builder fixture page (not a client)" \
  --platform "fixture://page" --date "30 September 2026" \
  --allow-placeholders --behind-login "account, portfolio and transaction pages" \
  --out artifacts/scan-report-sample-a3-v1.md \
  --html artifacts/scan-report-template-a3-v1.html \
  --full-findings artifacts/scan-report-full-findings-sample-a3-v1.md \
  --check --check-layout
```

Observed result on that run: all four word budgets pass, the table auto-fitted to 6 rows, and the estimated
height was 260mm of 273mm usable (95%) — FITS.

For a real client, drop `--allow-placeholders` and pass real details:

```sh
python3 scripts/render-scan-report.py \
  --scan findings.json --entity "Example AMC Limited" \
  --company "<our company>" --prepared-by "<your name>" \
  --contact-name "<your name>" --contact-email "<you>@<company>.in" --contact-phone "+91 ..." \
  --behind-login "account, portfolio and transaction pages" \
  --out report.md --html report.html --full-findings full-findings.md \
  --check --check-layout --internal
```

## 8. Worked example of one finding

The work order's worked example is the quality bar. Here is the same finding as the template actually
renders it, from the fixture run:

> **1. Blind investors are told nothing about this image**
> They can complete it, but only with difficulty and workarounds. A screen reader cannot describe this
> image, so its information may be lost. Affects: Blind and low-vision people using screen readers.
> Effort: small. Add concise alt text, or `alt=""` if purely decorative.

Two notes on matching the brief's example:

- **The heading and structure match**, and the consequence leads, with a plain fix and a stated effort.
- **One deliberate difference.** The brief's example ends "for roughly one in fifty they cannot use it at
  all". That statistic has no source in any packet file, so it is **not** reproduced. Under the work order's
  own rule, numbers carry their source and every `[EST]` needs an official or peer-reviewed citation.
  Supply the citation and the sentence can be restored.

## 9. What is not verified

Stated plainly, because a4-qa needs to know where to look:

1. **The one-page fit is an estimate, not a print render.** It comes from Helvetica font metrics, not from
   a browser or PDF engine. No browser, Chromium or PDF engine could be installed in the writing
   environment (PyPI was reachable, the Chromium and Debian package mirrors were not). **Confirm the fit
   with one print before the first client send.** This is the one acceptance criterion not fully closed.
2. **The template has never rendered a live-site scan.** It has rendered a real scan of a1's fixture page.
   No live site has been scanned, because no `artifacts/axe.min.js` bundle is present and `stack-facts-a1-v1.md`
   records that the axe path has not been validated. The report must not be sent to a target until a real
   scan of that target has been run.
3. **The `--check-layout` model assumes Helvetica/Arial metrics** at the point sizes in the report CSS, with
   the table's column fractions. A different font stack changes the estimate.
4. **The 10-rule heading map is a3 editorial work.** A rule outside the map renders
   `{{HEADING NEEDED for rule '...'}}` rather than an invented sentence. Real scans surface axe rules the
   map does not cover; those need human wording.

## 10. Decisions flagged for h1-human and a4-qa

1. **Cutting the findings table to fit one page.** The work order wants every finding listed *and* one page.
   Where those conflict, one page wins and the table is trimmed, with the full list in the companion file.
   If you would rather always print the complete table and accept two pages for large scans, say so — it is
   one flag, `--no-fit`.
2. **Dropping the "one in fifty" statistic** until it has a citation, per the note in section 8.
3. **No regulatory date or penalty figure anywhere.** The closing section refers to the annual audit the
   regulator expects, without naming a date. If a date belongs in the client report at all, use the audited
   wording from `claims-audit-a4-v1.md` claim 6 and re-check it before every send.
4. **Entity and contact details are placeholders.** The one-pager's placeholders are still unfilled by
   h1-human, and the renderer refuses to produce a client report with them unfilled.
5. **The scanner's unverified flag.** Every finding is emitted with `verified: false`. If a finding has been
   confirmed by a human, the report should one day say so; the schema has the field but nothing sets it.
