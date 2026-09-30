# Outreach pack — free accessibility scan (a3, v2)

- **Owner:** a3-content
- **Task:** T-20260929-produce-the-free-scan-67a8
- **Written:** 01 October 2026
- **Goal:** sending an email takes under two minutes per target
- **Verified by:** a4-qa before anything is sent

**Read this first — one caveat.** The work order asks for this pack to be rolled into
`artifacts/outreach-templates-a3-v1.md`. That file was never committed to the repository and was not
supplied, so nothing could be improved in place. This is a fresh draft built from the work order's content
spec, and it must be diffed against h1-human's existing templates before use. If h1-human's v1 already
carries approved wording, keep that wording and merge only what is new here.

---

## 1. The two-minute send

1. Open the target list, take the next row with no `sent_date`.
2. Copy the email in section 2. Replace the three bracketed fields. Check the per-target notes.
3. Run the five-line checklist in section 6.
4. Send, then fill in `sent_date` and `followup_due` (= sent date + 6 days) in the tracking CSV.

## 2. The email

**Subject:** A free accessibility scan of [ENTITY]'s investor platform

> Dear [NAME],
>
> We are offering [ENTITY] a free accessibility scan of its publicly reachable investor pages. There is no
> cost and no meeting needed to receive it.
>
> You get a one-page report: the three things to fix first, which pages are affected, who each problem
> affects, and what the fix takes. It is written for a reader with no technical background, and it names
> what we did not check as clearly as what we did.
>
> SEBI's circular of 31 July 2025 requires digital accessibility compliance for SEBI-regulated entities. As
> checked on 30 September 2026, SEBI has extended both the audit and the remediation deadline to
> 31 October 2026.
>
> We scan only pages that are publicly reachable. We do not log in, submit forms, or touch customer data.
>
> May I send the scan?
>
> [YOUR NAME]
> [COMPANY] · [EMAIL] · [PHONE]
> [DATE]

**Word count of the body: 138** (limit 150), counting the greeting and signature. Recount if you change
anything.

### What to change per target

| Field | Where it comes from | Check before sending |
|---|---|---|
| `[ENTITY]` | `entity_name` column of the target list | Use the exact registered name. "Aditya Birla Sun Life AMC Limited", not "ABSAMC". |
| `[NAME]` | `contact_name` column | If the row names a role rather than a person, write "Dear Sir or Madam" rather than guessing a title. |
| `[YOUR NAME]`, `[COMPANY]`, `[EMAIL]`, `[PHONE]`, `[DATE]` | Your own details | These are still placeholders. Do not send while they are unfilled. |

### Per-target judgement, from the target list's own columns

- **`category`** tells you which journey to mention if you ever add a line — AMCs and brokers have an
  investor login, RTAs and KYC agencies mostly have public portals. The template above stays generic on
  purpose, so you do not have to write per-category copy.
- **`est_size`** matters for timing, not wording. There are 28 `large` and 21 `mid` targets, and 25 at
  priority 1. Work priority 1 first.
- **`notes`** sometimes warns you off a contact route. Read it. One row already says "use role email only".

## 3. WhatsApp / LinkedIn version

Three sentences, no attachments, no links that look like tracking.

> Hello [NAME], I am offering [ENTITY] a free accessibility scan of its public investor pages, delivered as
> a one-page report within 48 hours and at no cost. SEBI's July 2025 circular covers SEBI-regulated
> entities, and as checked on 30 September 2026 the audit and remediation deadline is 31 October 2026. May
> I send it to you?

**Word count: 56, three sentences.** Do not attach the report, the one-pager or a PDF on first contact.

## 4. The follow-up (day 6)

**Rule: send this only if the scan was actually run.** The follow-up refers to a real report. If no scan was
run, this email does not exist and the target is closed as "no follow-up".

**Subject:** Your accessibility scan — shall I send it?

> Dear [NAME],
>
> Following up on my note of [DATE]. The scan is done and the report is ready to send — one page, the three
> things to fix first, and a clear note on what we did not check.
>
> Would you like me to send it? If accessibility is not a priority for [ENTITY] this year, tell me and I
> will close the file.
>
> [YOUR NAME]

One follow-up only. There is no third email. A target that has not replied after the follow-up is marked
`closed - no response` in the tracking CSV.

## 5. The "what does it cost" answer

Say this, and nothing more:

> The scan costs nothing, and so does the report. If you want us to do the remediation work — fix the
> findings, re-scan to confirm each one is closed, and set up monitoring — we quote after the scan, once we
> know what is actually involved. We do not quote before we have looked.

**Never quote a price before the scan.** The work order is explicit that pricing follows the scan, never
precedes it. This also keeps the pack clear of escalation A4-C08, where publishing an unlabelled cost range
is a release blocker.

## 6. The sending checklist

Five lines. Run through them before every send.

1. **Entity name and contact name match the target list exactly**, and you have read that row's `notes`.
2. **Every claim in the email is on the approved list in section 8** — nothing new, nothing stronger.
3. **No attachment** on first contact, and the placeholder fields are filled with real details.
4. **The deadline sentence is still true on today's date.** Recheck it; it is the only time-sensitive claim.
5. **The scan for this target has actually been run** before the day-6 follow-up goes out.

## 7. Tracking table spec

The work order names six columns: entity · contact · sent date · follow-up due · reply · next action.

`artifacts/target-list-a2-v1.csv` already holds 50 rows and 13 columns, so do not build a second file.
Add these six columns to a working copy of it and you have the tracker:

| New column | Value | Notes |
|---|---|---|
| `sent_date` | DD Month YYYY, or blank | Blank means not yet contacted |
| `followup_due` | sent date + 6 days | Set it when you set `sent_date` |
| `reply` | `none` / `replied` / `no` / `scan sent` / `closed` | Keep to these five values so the column stays countable |
| `next_action` | one short phrase | "send scan", "day-6 follow-up", "book call", "close" |
| `scan_run_on` | DD Month YYYY, or blank | This is the gate for the follow-up email |
| `outcome` | blank until closed | `scan sent` / `quoted` / `won` / `lost` / `no response` |

Keep the existing `priority`, `entity_name`, `category`, `contact_role`, `contact_name`, `contact_email`
and `est_size` columns — they drive the sequencing in section 2.

## 8. Approved claims, and what is banned

Every claim in the pack must trace to a primary source. These are the only claims cleared for use, all
through `artifacts/claims-audit-a4-v1.md` and `artifacts/a4-qa-escalation-20260930.md`.

| Use this | Source | Do not say |
|---|---|---|
| "SEBI's circular of 31 July 2025 requires digital accessibility compliance for SEBI-regulated entities." | Circular SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/111, ¶¶2–3 | Do not widen it to "every financial firm", "every fintech" or "all listed companies". Scope is SEBI-registered and recognised entities. |
| "As checked on 30 September 2026, SEBI has extended both the audit and remediation deadline to 31 October 2026." | The 31 July 2026 circular, ¶¶3–4 | Do not say only remediation moved, and do not quote the old dates. |
| "Requires compliance with accessibility standards referenced by SEBI." | Circular, Annexure I, B, points 1–4 | Do not present WCAG 2.1, IS 17802:2021 and GIGW 3.0 as a verbatim frozen list from the circular. The circular refers to WCAG 2.1 or the latest version and the latest GIGW. |
| Nothing about penalties. | — | **Banned:** any penalty amount, any count of enforcement actions, any aggregate figure, any court holding. A4-C04, A4-C05 and A4-C07 all remain unresolved. |
| Nothing about credentials. | — | **Banned:** claiming or implying IAAP or other certification for our company or team, or that SEBI requires an exclusively IAAP-certified auditor. A4-C03 is unresolved. |
| Nothing about a target's platform. | — | **Banned:** asserting that a named entity's site has defects before we have scanned it. We have scanned nobody yet. |

## 9. Verification status

What a4-qa must check, and what I could not verify myself:

1. **The deadline sentence is time-sensitive.** It was accurate as at the audited date. It must be re-checked
   immediately before the first send, and again for any send on or after 01 November 2026.
2. **No target has been scanned.** Nothing in this pack claims otherwise, and no scan result is quoted. The
   day-6 follow-up is gated on a real scan for precisely this reason.
3. **The remediation claim in section 5 is a capability statement,** not a proven one. The scanner has never
   been validated against a live site (`scanner-qa-a4-v1.md`: no live test performed). If the remediation
   offer is made, the capability needs to exist.
4. **This pack was written without h1-human's v1 templates,** so a diff against the existing messaging is
   outstanding.
5. **Placeholders remain.** `[YOUR NAME]`, `[COMPANY]`, `[EMAIL]`, `[PHONE]` are unfilled, exactly as in the
   one-pager.
