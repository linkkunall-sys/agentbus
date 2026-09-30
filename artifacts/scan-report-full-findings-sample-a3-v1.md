# Full findings — all 10

Scanner a1-v1 · 1 page(s) scanned · 0 page(s) failed · companion to the one-page scan report.

Findings are ordered worst first. Effort is our estimate (small / medium / large).

| # | Severity | What it is | Where | Who it affects | How to fix | Effort | For developers |
|---|---|---|---|---|---|---|---|
| F-001 | serious | Blind investors are told nothing about this image | fixture://page · element img | Blind and low-vision people using screen readers | Add concise alt text, or alt="" if purely decorative. | small | WCAG 1.1.1 (A) |
| F-002 | serious | Investors using screen readers cannot tell what this field is for | fixture://page · element input | People using screen readers or voice control | Associate a visible <label> with this field. | small | WCAG 1.3.1, 4.1.2 (A) |
| F-003 | serious | A button announces no purpose | fixture://page · element button | Screen-reader users | Give the button visible text or an accessible name. | small | WCAG 4.1.2 (A) |
| F-004 | serious | A link announces no destination | fixture://page · element a | Screen-reader users | Provide link text or meaningful alternative text for its image. | small | WCAG 2.4.4 (A) |
| F-005 | serious | Embedded content is announced with no name | fixture://page · element iframe | Screen-reader users | Add a concise title to the iframe. | small | WCAG 4.1.2 (A) |
| F-007 | serious | The page does not declare its language | fixture://page · element html | Screen-reader users | Set the correct lang attribute on the html element. | small | WCAG 3.1.1 (A) |
| F-009 | serious | A menu control cannot be operated from the keyboard | fixture://page · element div | Keyboard-only users | Use a native button and support keyboard activation. | small | WCAG 2.1.1 (A) |
| F-010 | serious | Text is hard to distinguish from its background | fixture://page · element .low-contrast | People with low vision or reading in bright conditions | Increase text/background contrast to at least 4.5 to 1. | small | WCAG 1.4.3 (AA) |
| F-006 | moderate | Table data has no headings, so relationships are unclear | fixture://page · element table | Screen-reader users reading tabular data | Mark header cells with <th> and appropriate scope. | small | WCAG 1.3.1 (A) |
| F-008 | moderate | The page outline skips a level | fixture://page · element heading | People navigating by headings | Use heading levels in a logical sequence. | small | WCAG 1.3.1 (A) |
