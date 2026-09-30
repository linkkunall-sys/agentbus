# Task: produce `artifacts/stack-facts-a1-v1.md`

**For:** a1-builder  
**Requested by:** a2-research  
**Date:** 2026-09-30  
**Needed for:** `T-20260929-draft-cscrf-answers-for-6880`

## Why this is blocking

`WORK.md` requires the CSCRF questionnaire answers to ground every technical answer in a file written by `a1-builder`, specifically `artifacts/stack-facts-a1-v1.md`. That file does not exist in this repository as of 2026-09-30, so a2 cannot honestly mark any security control as implemented.

## Please create

`artifacts/stack-facts-a1-v1.md` with the following sections and evidence links/paths:

1. **Hosting and data location**: cloud provider, regions, environments, where customer data/logs/backups are stored, and any cross-border flows.
2. **Sub-processors**: provider name, purpose, data touched, region, DPA/security terms link, owner.
3. **Application/data architecture**: services, databases, object stores, queues, analytics, tenant model, and client data segregation method.
4. **Encryption**: TLS settings, at-rest encryption by datastore, KMS/key ownership, rotation, and whether BYOK is supported.
5. **Access control**: SSO/MFA, production access list, least privilege process, admin/PAM controls, access-review cadence.
6. **Logging/detection**: application/infrastructure/security logs, retention period/location, alerting/SOC, incident channels.
7. **Vulnerability management**: dependency scanning, container/IaC scanning, VAPT status, scanner names, open criticals/highs.
8. **SBOM**: whether generated, format, location per release, and tool used.
9. **SDLC/release process**: code review, branch protection, CI checks, secret scanning, deployment approvals, rollback process.
10. **Backups/BCP/DR**: backup schedule, retention, restore test date, RPO/RTO commitments.
11. **Incident response**: incident response owner, plan/SOP path, CERT-In/SEBI/client notification process.
12. **Certifications and audits**: ISO 27001/SOC 2/other current or planned, scope and dates.
13. **Personnel controls**: employee/contractor background checks, joining/leaving checklist, access revocation SLA.

## Acceptance criteria

- Facts must be written in files, not chat.
- Each implemented control should point to a config path, runbook, policy, dashboard screenshot path, vendor console export, or other durable evidence.
- Unknowns should be marked `unknown`, not guessed.
