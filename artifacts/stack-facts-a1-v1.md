# Scanner stack facts (a1-v1)

- Runs on the operator's laptop/VPS; no hosted service or database is used.
- For live scans, Python fetches public page HTML and Playwright/Chromium loads the same-origin pages. Requests identify as `AccessibilityAuditBot/0.1 (+contact: accessibility@example.org)`.
- The scanner does not submit forms or provide login/session credentials. It writes findings JSON and a Markdown summary only to the paths selected by the operator.
- Data transmitted: ordinary HTTP(S) requests to the target origin, with the stated user agent. No findings are sent to the scanner author.
- Data retained: local output files and ordinary target/web-server logs. Operator controls deletion and retention.
- Axe's browser bundle must be locally available at `artifacts/axe.min.js`; it is not fetched at runtime. The execution environment could not retrieve the upstream bundle, so the live axe path has not been validated here.
- Dependency/install: `python3 -m pip install playwright && python3 -m playwright install chromium`. Python standard library otherwise. No dependency licence audit was run; no pip-licenses output is claimed.
