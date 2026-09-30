# Accessibility scan report — SAMPLE - a1-builder fixture page (not a client)

Platform scanned: fixture://page · Scan date: 30 September 2026

Prepared by {{FOUNDER_NAME}}, {{COMPANY_NAME}} · {{FOUNDER_EMAIL}}

## What we checked

1 publicly accessible page was scanned with scanner a1-v1, including fixture://page. 10 findings were recorded.

## The three things to fix first

1. **Blind investors are told nothing about this image**
They can complete it, but only with difficulty and workarounds. A screen reader cannot describe this image, so its information may be lost. Affects: Blind and low-vision people using screen readers. Effort: small. Add concise alt text, or alt="" if purely decorative.

2. **Investors using screen readers cannot tell what this field is for**
They can complete it, but only with difficulty and workarounds. The purpose of this field is not announced, making it difficult to know what to enter. Affects: People using screen readers or voice control. Effort: small. Associate a visible <label> with this field.

3. **A button announces no purpose**
They can complete it, but only with difficulty and workarounds. Assistive technology cannot tell the person what this button does. Affects: Screen-reader users. Effort: small. Give the button visible text or an accessible name.

## Full findings

| # | What it is | Where | Who it affects | How to fix | Effort | For developers |
|---|---|---|---|---|---|---|
| F-001 | Blind investors are told nothing about this image | fixture://page · element img | Blind and low-vision people using screen readers | Add concise alt text, or alt="" if purely decorative. | small | Web Content Accessibility Guidelines (WCAG) 1.1.1 (A) |
| F-002 | Investors using screen readers cannot tell what this field is for | fixture://page · element input | People using screen readers or voice control | Associate a visible <label> with this field. | small | WCAG 1.3.1, 4.1.2 (A) |
| F-003 | A button announces no purpose | fixture://page · element button | Screen-reader users | Give the button visible text or an accessible name. | small | WCAG 4.1.2 (A) |
| F-004 | A link announces no destination | fixture://page · element a | Screen-reader users | Provide link text or meaningful alternative text for its image. | small | WCAG 2.4.4 (A) |
| F-005 | Embedded content is announced with no name | fixture://page · element iframe | Screen-reader users | Add a concise title to the iframe. | small | WCAG 4.1.2 (A) |
| F-007 | The page does not declare its language | fixture://page · element html | Screen-reader users | Set the correct lang attribute on the html element. | small | WCAG 3.1.1 (A) |

The table lists the 6 highest-severity findings. All 10 findings, including the remaining 4, are listed in full in the companion findings file supplied with this report.

## What we did not check

Pages behind a login were not checked, because the scanner submits no forms and uses no credentials. Not reachable in this scan: account, portfolio and transaction pages. This is an automated scan of publicly accessible pages. It finds a subset of issues and does not replace testing with a person using a screen reader.

## What happens next

We can fix these findings, re-scan to confirm each one is closed, and set up monitoring so new pages are checked as they ship. The annual accessibility audit the regulator expects then falls out of the same cycle. Reply to this email and we will scope the first batch.

## Contact

{{FOUNDER_NAME}}
{{FOUNDER_EMAIL}}
{{FOUNDER_PHONE}}
{{FOUNDER_NAME}} · 30 September 2026

