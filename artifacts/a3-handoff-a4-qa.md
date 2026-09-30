# Handoff — a3-content → a4-qa — verification of the scan report and outreach pack

- **Date:** 01 October 2026
- **From:** a3-content
- **To:** a4-qa
- **Tasks:** T-20260929-write-the-client-grade-2750 (high) · T-20260929-produce-the-free-scan-67a8 (normal)
- **Decision requested:** verify the claims below before anything reaches a client. **No client send is
  authorised by this document.**

## Mode — manual, and why

`scripts/agentbus.py` does not exist in this repository, so the `claim`, `note`, `done` and `handoff`
commands in the work order could not be run. No task state was changed and no bus delivery is asserted.
This follows the precedent set in `artifacts/a4-qa-escalation-20260930.md`. The bus still needs restoring by
h1-human.

**One correction to the work order's suggested handoff text.** The command in section 5 of my work order asks
me to state that the template is "tested against a live scan report". That is not true and I have not
claimed it. The template was tested against a real scan — but of a1-builder's **fixture page**, not a live
site. A live scan was impossible: `artifacts/axe.min.js` is absent and `stack-facts-a1-v1.md` records the
live axe path as unvalidated.

## Artifacts for verification

| Artifact | What it is |
|---|---|
| `artifacts/scan-report-template-a3-v1.md` | The template, its binding contract, rules and budgets |
| `artifacts/scan-report-template-a3-v1.html` | Generated one-page report, banner-marked as a sample render |
| `artifacts/scan-report-sample-a3-v1.md` | The rendered sample, Markdown |
| `artifacts/scan-report-full-findings-sample-a3-v1.md` | All 10 findings, uncut |
| `artifacts/scan-fixture-output-a3-v1.json` | The real scan the sample renders from |
| `scripts/render-scan-report.py` | The renderer |
| `artifacts/outreach-pack-a3-v2.md` | Email, WhatsApp, follow-up, pricing answer, checklist, tracker spec |
| `artifacts/a3-handoff-a1-schema-fields.md` | Field request to a1-builder |

## Please verify on Task 1

1. **Every claim label is correct.** The `--internal` block asserts five labels: two [RES] on scanner-derived
   facts, one [RES] on the scanner's own output wording, one [EST] on the annual-audit sentence, one [EXP] on
   effort estimates. Check each against its cited basis, and check that the [EST] genuinely rests on the
   audited annual-schedule position in claim 6 and not on anything stronger.
2. **No banned claim has leaked into the client-facing text.** The report must contain no deadline date, no
   penalty figure, no enforcement count, no fixed standards version, and no credential claim. I believe it
   contains none; this is exactly the kind of thing the author cannot spot.
3. **The "What we did not check" section is present and truthful.** It is mandatory and the renderer cannot
   omit it. Check that its default sentence about login-gated pages is fairly derived from
   `stack-facts-a1-v1.md`.
4. **The unsourced statistic was dropped.** The work order's worked example ends "for roughly one in fifty
   they cannot use it at all". No packet file sources that figure, so it is not in the template. Confirm this
   is the right call, or supply the citation.
5. **The one-page claim is only an estimate.** It comes from a font-metrics model, not a print render. Treat
   it as unverified and see the open items below.

## Please verify on Task 2

1. **Every claim in the email traces to the approved list** in section 8 of the pack, and the banned list is
   absent. The pack's approved wording is drawn from your own audit; check I have not paraphrased it into
   something stronger.
2. **The deadline sentence is the weak point.** It is accurate as at the audited date and must be rechecked
   before any send, and again for any send on or after 01 November 2026. Please confirm the exact wording you
   want used, since this is the one claim in the pack that decays with time.
3. **Scope wording.** The email says "SEBI-regulated entities", not "financial firms" or "fintechs". Confirm
   that matches your scope note on claim 1.
4. **The follow-up gate.** The pack states the day-6 follow-up may only be sent if the scan was actually run.
   Check that no other sentence in the pack implies a scan already exists for a target.
5. **Word counts.** The email body is 138 words and the WhatsApp version is 56 words in three sentences,
   both measured. Confirm they are inside the limits you are holding us to.

## Open items I could not close

1. **No print verification of the one page.** No browser, Chromium or PDF engine could be installed in the
   writing environment — PyPI was reachable, the Chromium CDN and the Debian mirrors were not. I tried
   WeasyPrint (missing Pango/Cairo), Playwright (browser download blocked) and xhtml2pdf (ignores `@page`
   margins and point sizes, so its page count is meaningless). The fit is therefore a font-metrics estimate,
   reported honestly as such in the template. **Someone must print it once before the first client send.**
2. **No live scan has ever been run**, by me or by a1. Nothing in either deliverable asserts otherwise.
3. **`artifacts/outreach-templates-a3-v1.md` was never supplied.** The work order asked me to roll it into the
   outreach pack. I could not improve a file I do not have, so the pack is a fresh draft built from the work
   order's content spec and must be diffed against h1-human's existing messaging.
4. **`MASTER_PROMPT.md` was never supplied.** If it constrains tone or claim handling beyond the work order,
   both deliverables may need adjustment.
5. **Entity, company and contact details are placeholders**, consistent with the unfilled one-pager. The
   renderer refuses to emit a client report while they are unfilled, so this is a hard gate, not a note.
   Neither artifact can go to a client until h1-human fills them.

## Blocker

`scripts/agentbus.py` is missing, so no task transition could be recorded. This is the same blocker a4-qa
escalated on 30 September 2026 and it remains open.
