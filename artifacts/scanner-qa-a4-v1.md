# Scanner QA — a4-qa — v1

- **Checked on:** 2026-09-30 (UTC)
- **Task:** T-20260929-qa-test-the-scanner-8fd0
- **Execution status:** **BLOCKED — no live-site test performed**
- **Verdict:** **DO NOT SHIP a client-facing scanner report yet.**

This is a blocker report, **not** a completed three-platform QA study. It contains no invented sites, findings, classifications, screen-reader announcements, false-positive results, or bug reproductions.

## Why execution is blocked

At session start, `git ls-files` and a filesystem inventory showed only `README.md`, whose complete content was `# agentbus`. There was no master prompt, a4 packet, task store, a2 target list, a1 scanner implementation/output, or report schema. The task's dependency on a1-builder Task 1 therefore **cannot be checked**; a1's completion must not be assumed either way.

The workspace is **Linux**. The required NVDA-on-Windows or VoiceOver-on-macOS test environment was not available. No compatible external operator's evidence was supplied. DOM inspection, an accessibility-tree snapshot, a Linux screen reader, or another automated checker would not substitute for the screen-reader protocol specified in the work order.

| Blocker | Evidence this session | Unblock requirement | Requested owner |
| --- | --- | --- | --- |
| Scanner and builder dependency unavailable | No implementation, executable, scanner version, task state or raw output in the checkout. | Supply the a1 Task 1 handoff, scanner version/commit, run instructions, output schema and representative generated report. | a1-builder / h1-human |
| Target selection unavailable | No a2 target list or size classifications in the checkout. | Supply the actual target list with public URLs and a defensible large/mid/small classification. Do not invent that three convenient sites came from a2's list. | a2-research |
| Mandatory manual screen-reader environment unavailable | OS check returned Linux; no Windows/NVDA or macOS/VoiceOver session or transcript was supplied. | Arrange an existing compatible device and operator, or provide a way for a4 to observe/re-verify the specified tests. Record OS, browser and screen-reader versions. Any proposed spending requires h1-human approval. | h1-human / a4-qa |
| Coordination/rules unavailable | `MASTER_PROMPT.md`, a4 packet and `scripts/agentbus.py` absent. The Task 1 claim attempt failed with file-not-found. | Restore the rules, packet and coordination script/task state. No successful agentbus QA claim, completion or handoff is asserted. | h1-human |

No platform scans were attempted. Retrieval of public regulatory documents for the separate claims audit was **research**, not scanner QA.

## Coverage and classification counts

| Metric | Observed result |
| --- | --- |
| Platforms tested | **0** of the required 3 |
| Large / mid / small platforms | **0 / 0 / 0**; not selected |
| Public platform pages scanned | **0** |
| Sampled scanner findings, N | **0**, below the required minimum of 20 |
| True positives, TP | **0 observed classifications** |
| False positives, FP | **0 observed classifications** |
| Unverifiable sampled findings, U | **0 observed classifications** — no findings were sampled; this does not mean that all findings were verifiable |
| Keyboard-only tests | **Not performed** |
| NVDA / VoiceOver tests | **Not performed** |
| Independent contrast measurements | **Not performed** |
| Finding-specific HTML inspections | **Not performed** |
| Client/private data collected | **None** |
| Behind-login scanning | **None** |

### False-positive rate

The work order's metric is:

```text
false-positive rate = false positives ÷ sample size = FP ÷ N
```

**This session:** `N = 0`; no FP classification was observed. `0 ÷ 0` is **undefined**. **False-positive rate: N/A — not measured.** It is not zero percent, and no numerical accuracy claim is cleared.

For the executed rerun, report `TP + FP + U = N`, include all sampled findings in the denominator, and publish U separately. An unverified finding is not a true positive. A low measured FP proportion with unresolved U is not proof that the report is credible. If the measured rate exceeds approximately 20%, recommend delaying the first send as directed by the work order.

## Sampled-finding evidence table

**There are no sampled finding rows.** Adding twenty placeholders and calling them “unverifiable” would falsely imply that a scanner run and sampling had occurred. No `verified: true` finding is created by this report.

The executed v2 must populate this table with at least twenty **actual scanner-reported** findings. This is a schema for the rerun, not observations:

| sample_id | platform / size | page and element selector | scanner finding ID / rule / assertion | classification | independent evidence used | limitations / evidence reference |
| --- | --- | --- | --- | --- | --- | --- |

Allowed classifications: **true positive · false positive · unverifiable**. Evidence must identify the precise rendered element and state what the human test actually established, rather than merely repeating the scanner's explanation.

## Report-quality judgment

No generated scanner report was supplied. Numeric quality scores would therefore be invented.

For the rerun, use a 1–5 scale, where 5 is strongest, for each requested criterion:

| Criterion | Score now | Reason / evaluation needed |
| --- | --- | --- |
| Plausibility of findings | **N/A — not evaluated** | Need actual rules, pages, elements, assertions and independent manual classifications. Check hidden/decorative elements, dynamic states, accessible names and duplicate component occurrences rather than assuming an automated flag is a confirmed barrier. |
| Clarity of fix advice | **N/A — not evaluated** | Need the delivered report. Advice must explain the affected user task, applicable criterion, a specific fix and a reproducible retest. A generic recommendation is not enough. |
| Whether anything would embarrass us if challenged (challenge-safety score) | **N/A — not evaluated** | Need the report's exact wording and evidence. Unsupported confirmations, claimed screen-reader announcements, unexplained numbers, incorrect legal deadlines or claims of certified/full compliance would be release blockers. No actual such report overstatement has been observed here because the report is absent. |

**Would a compliance head accept this as the requested QA evidence? No.** The required study has not been executed. This is not a finding that the unavailable scanner is defective; it is a finding that its credibility has not been demonstrated.

## Worst-false-positive bug reports

**None can honestly be published yet.** No observed false positives, pages or elements exist in this session's QA data. Do not invent two or three bugs to fill the acceptance checklist.

For each of the two or three worst **observed** false positives in the executed rerun, record:

1. Public page URL, test timestamp, scanner version and exact finding/rule ID.
2. Stable element selector, relevant HTML excerpt and rendered state, including viewport/theme and any public interaction needed to reproduce it.
3. Scanner assertion, steps to reproduce, expected result and independently observed result.
4. Keyboard keystrokes/outcome, actual NVDA or VoiceOver announcement and versions, or measured foreground/background colour pair and contrast calculation, as applicable.
5. Why the assertion is wrong, user/report impact, proposed fix and a regression test against the same element/state.

These are reporting requirements, **not observed bugs**.

## Exact rerun gates and protocol

1. **Read the restored rules and packet first.** Verify a1's delivered scanner and record its version. Review the a2 list and choose one large, one mid and one small platform from it; record the actual size basis and source.
2. **Scan public pages only, politely.** Check public-site restrictions, predeclare a small page scope and low sequential request rate, and stop on denial, rate limiting or an access restriction. No credentials, logins, KYC submissions, private dashboards or client data. Do not evade restrictions. Log URLs, timestamps, skipped pages and reasons.
3. **Keep the scanner's raw output and the exact rendered report.** Preserve finding IDs, rules, selectors, page/state, versions and report counts so a reviewer can reproduce both the finding and the document shown to the buyer. Avoid collecting unrelated personal information.
4. **Take at least twenty findings across all three platforms and several pages.** Predeclare and log the selection method; spread the sample across rules and pages rather than cherry-picking only easy successes or suspected errors. A proposed balanced allocation is 7 large / 7 mid / 6 small. It is a sampling plan, not an executed result. Disclose repeated components and whether the unit is a reported occurrence or a distinct issue. If the scoped run produces fewer findings, say so and keep acceptance open; do not manufacture a sample.
5. **Hand-verify each finding without relying on the scanner.** Record keyboard-only operation with Tab, Shift-Tab, Enter, Space and arrows; record what NVDA on Windows or VoiceOver on macOS actually announces; independently measure the specific colour pair for contrast assertions; and inspect the actual element's HTML. For a modality that is genuinely inapplicable, record N/A with a reason. For a missing required observation, classify the assertion as unverifiable rather than substituting automated output.
6. **Classify every sample and keep evidence.** Only a4 may set `verified: true`, and only for personally confirmed true positives. Independent evidence must be tied to the precise assertion and page state. Explain both false positives and unverifiables.
7. **Calculate and publish FP ÷ N.** Show TP, FP, U and N. Score the three report-quality criteria, publish specific observed bug reports, and issue a plain ship/fix-first/do-not-ship verdict. No compliance certificate, population-wide accuracy or complete-platform coverage claim may be inferred from a twenty-finding sample.
8. **Hold release until these gates are met.** A report on a few public pages is a scoped diagnostic, not verification of private investor journeys, mobile apps, PDFs or all SEBI obligations. Use the claims audit's corrected legal wording; do not assert a professional audit or security/privacy posture that has not been evidenced.

## Verdict and acceptance

**DO NOT SEND THIS TO A CLIENT YET.** The scanner implementation, target list and generated report were not supplied, and the required manual screen-reader environment was unavailable. Consequently there is no defensible sample, false-positive measurement, report-quality score or bug reproduction. Delay the first scanner-backed send until the required three-platform study and manual checks are actually performed; do not conceal the missing evidence with a clean-looking percentage or unearned `verified: true` flags. No spending or credential claim is authorized to unblock the work.

| Acceptance criterion | Status |
| --- | --- |
| 3 platforms, large/mid/small from a2 list | **Not met — blocked** |
| At least 20 sampled scanner findings | **Not met — no run** |
| Every finding classified with independent evidence | **Not met — no sample** |
| Measured false-positive rate with sample size | **Not met — rate undefined at N = 0** |
| Two or three reproducible worst-FP bug reports | **Not met — no observed FP** |
| Plain release verdict | **Met — do not ship yet** |
| No private data or behind-login scanning | **Met — no scans performed** |

**Task 2 is not done.** The blocker escalation is recorded in `artifacts/a4-qa-escalation-20260930.md`. A completed, evidenced rerun should be published as v2; this v1 must not be represented as a passed QA study.
