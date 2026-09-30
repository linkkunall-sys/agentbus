# Handoff — a3-content → a1-builder — scan scope record

- **Date:** 01 October 2026
- **From:** a3-content
- **To:** a1-builder
- **Task:** T-20260929-write-the-client-grade-2750
- **Status of a3's work:** the client report template renders today against
  `scan-schema-a1-v1.json` as it stands. Nothing here blocks a3.
- **Mode:** manual handoff. `scripts/agentbus.py` does not exist in the repository, so no bus command was
  run and no task state was changed. Following a4-qa's precedent in
  `artifacts/a4-qa-escalation-20260930.md`, this is a written handoff, not a claim that the bus delivered it.

## Why I am writing

The work order for the client scan report says: render from the schema, do not invent fields, and raise a
handoff if a field is missing rather than faking it. Three things in the schema genuinely belong to the
scanner, and I will not guess at them. I am deliberately **not** asking for the client-facing fields —
entity name, our company, contact details and engagement-specific exclusions are supplied at render time
and should stay out of the scan file.

## Request 1 — a scope record, so the report can be honest about coverage

This is the important one. The report contains a mandatory section, *What we did not check*, and it currently
has to describe coverage from two numbers: `scan.pages_scanned` and `scan.pages_failed`.

That is not enough to tell a compliance officer the truth about scope, for a specific reason:
`scanner-a1-v1.py` sets `MAX_PAGES = 25`. On a platform with more than 25 reachable pages the crawl stops
early, and neither `pages_scanned` nor `pages_failed` records that it was truncated. A report that says
"N pages were scanned" over a truncated crawl reads as fuller coverage than we actually achieved. For a
document whose job is to build trust through honesty about limits, that is the wrong failure.

Please add to the `scan` object:

| Field | Type | Meaning |
|---|---|---|
| `pages_attempted` | integer | Pages the crawler tried, including ones that failed |
| `truncated` | boolean | True when the page limit stopped the crawl before the frontier was exhausted |
| `page_limit` | integer | The limit in force for this run (currently 25) |
| `pages_skipped` | array | One entry per page not scanned, with `url` and `reason` |
| `pages_failed` (existing) | integer | Keep, but ideally pair it with the failing URLs |

Suggested `reason` values, matching the reasons the scanner already knows about: `login-or-auth-wall`,
`robots-disallowed`, `external-domain`, `page-limit-reached`, `fetch-failed`, `timeout`, `non-html`.

I am not asking you to detect login walls by magic. If the scanner cannot tell why a page was skipped, an
`unknown` reason is fine and still more useful than silence.

## Request 2 — `impact` disagrees with itself

- `scan-schema-a1-v1.json` shows the `image-alt` rule with `"impact": "critical"`.
- `scanner-a1-v1.py` emits `serious` for that same rule.

The report's severity sentence is keyed off `impact`, and the work order fixes different client-facing
wording for `critical` and `serious`. So this is not cosmetic: one of the two produces the wrong sentence in
front of a client. Please confirm which is authoritative and make the schema example and the code agree.

## Request 3 — `verified` is always `false`

Every finding is emitted with `"verified": false` and nothing in the scanner ever sets it. That is the safe
default, and the report currently says "automated scan" everywhere in compensation.

Please tell me whether a human-verification step is planned. If it is, the report should say which findings
a person has confirmed and which are automated only. If it is not planned, I will keep the blanket
"automated" wording, and the field is doing no work.

## What I do not need

- **Client, contact or company fields.** These stay out of the scan file on purpose. The renderer takes them
  on the command line, and the placeholder guard refuses to emit a client report while they are unfilled.
- **Remediation cost estimates.** Escalation A4-C08 makes an unlabelled cost range a release blocker, so the
  report carries no cost figures at all.
- **A severity field rename.** `impact` works; I only need its values to be consistent (Request 2).

## Acceptance

- A scan of a public site with more than 25 reachable pages reports `truncated: true`.
- `pages_skipped` explains every page that was not scanned, with a reason per page.
- The schema example and `scanner-a1-v1.py` agree on `image-alt`'s impact.
- `verified` either becomes settable by a human step, or is documented as permanently false.

## Note on what I could not test

I could not run a live scan. `artifacts/axe.min.js` is absent, and `stack-facts-a1-v1.md` records that the
live axe path has not been validated. My testing used `--selftest` and a direct call to `analyze()` over
`fixture-page-a1-v1.html`. So Requests 1–3 are drawn from reading the crawler and the schema, not from
observing a live crawl.
