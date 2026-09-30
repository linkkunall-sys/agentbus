# Claims audit — a4-qa — v1

- **Checked on:** 2026-09-30 (UTC)
- **Task:** T-20260929-verify-every-claim-in-7fd5
- **Release recommendation:** **HOLD the existing pitch. Apply the corrections, remove unverified assertions, then re-audit the actual files.**

## Summary

Of the **10 supplied claims**: **3 confirmed · 2 corrected · 3 unverifiable · 2 misleading**. These are mutually exclusive verdicts on the original claims, not counts of individual facts inside a compound claim.

Critical findings:

- **The audit and remediation dates are stale.** SEBI's 31 July 2026 circular extends **both** to **31 October 2026**, not just remediation. Other provisions remain unchanged. See claim 6 and primary evidence P5.
- **Do not market an unqualified “IAAP-only” requirement as settled current law.** The July 2025 text expressly names IAAP-certified professionals; the December 2025 clarification uses “certified accessibility professionals.” The difference is verified; its legal effect on exclusivity is not. See claim 3.
- **The remediation cost range is [EXP], attributed to a vendor, not an official benchmark, a validated per-entity cost, or our price.** See claim 8.
- The February penalty letter was obtained, but the claimed aggregate count was not independently established. The repeat-offender amount/count/date combination lacks a retrieved primary order. See claims 4–5.
- The judgment was located on the Supreme Court's own host, but the available primary-PDF extraction stops before the holding. A reproduction and SEBI's account support the claim, but do not satisfy this task's direct-primary verification requirement. See claim 7.

### Scope limitation — do not call this a complete pitch audit

At the start of this session, `git ls-files` and a filesystem inventory showed **only `README.md`**, containing `# agentbus`. At that point there was no `MASTER_PROMPT.md`, a4 packet, `artifacts/`, pitch material, video script/captions, templates, CSCRF answers, a2 target list, scanner, or `scripts/agentbus.py`. This session adds only the three a4-qa reports; the project inputs remain missing.

Accordingly:

- The `claim` column quotes the **work order's §2.2 wording**, not unseen pitch sentences.
- `appears_in` records the work order locator and the reported destinations. Exact repository filenames, line numbers, video timestamps, and all other claims must be supplied before the “every claim” task can be completed.
- Cross-file numeric drift, existing `[EST]` labels, correction propagation, company security/privacy statements, and credentials **have not been inspected**.
- Nothing in this report authorizes a client send or represents that missing client-facing files have been fixed.
- The supplied agentbus claim command was attempted and failed because the script does not exist. No task was successfully claimed, marked done, or handed off in agentbus. The escalation and content handoff are recorded manually in `artifacts/a4-qa-escalation-20260930.md`.

## Verdict rules and labels

- **confirmed:** the original proposition is supported by personally inspected primary evidence within the stated scope.
- **corrected:** an incorrect or stale detail has a source-backed replacement.
- **unverifiable:** required evidence for the original assertion was not obtained/inspectable. This is **not** a finding that the assertion is false. A supported subset or attributed replacement does not make the original claim pass.
- **misleading:** wording omits provenance, qualifications, or uncertainty that changes what a buyer would reasonably understand.

`[EST]` is reserved, under the work order, for propositions supported by official or peer-reviewed sources. `[EXP]` marks vendor estimates or other secondary assertions. **An `[EXP]` label is not permission to publish an unverified enforcement count.** Labels next to original quotations below are audit annotations, outside the quoted text.

## Required claims table

| claim | appears_in | verdict | primary_source | corrected_text | checked_on | notes |
| --- | --- | --- | --- | --- | --- | --- |
| **1.** “SEBI circular dated 31 July 2025 mandating digital accessibility” | Work order §2.2, row 1. Reported: one-pager, video, templates. Actual files/locations unavailable. | confirmed | P1: SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/111, header p.1, ¶¶2–3 pp.2–3, ¶7 p.5. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf) | SEBI issued Circular No. SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/111 on 31 July 2025, mandating digital accessibility compliance for the digital platforms of SEBI-regulated entities under the RPwD Act, 2016 and corresponding rules. | 2026-09-30 | Scope is SEBI registered/recognised intermediaries and SEBI-regulated market infrastructure institutions, as defined in ¶2—not every financial firm, every fintech, or every listed business by inference. The PDF's `aug-2025` upload directory is not its issue date. |
| **2.** “Standards are WCAG 2.1, IS 17802:2021, GIGW 3.0” | Work order §2.2, row 2. Reported: all material. Actual files/locations unavailable. | corrected | P1, Annexure I, B “Scope,” points 1–4, pp.7–8; C §6.1 p.10. P4, Annexure B, p.4, supplies the AA reporting criterion. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/dec-2025/1765194149704.pdf) | SEBI's circular references WCAG 2.1 or the latest version, the accessibility guidelines in the latest version of GIGW, IS 17802, and the RPwD Act, 2016 and corresponding rules. Its December 2025 readiness-report format asks whether each platform meets a minimum AA level under the latest WCAG guidelines. | 2026-09-30 | The circular does not freeze WCAG at 2.1, specify `IS 17802:2021`, or name `GIGW 3.0` in its standards list. Do not present those fixed versions as a verbatim list from the circular. If separately naming the IS parts/years or the currently published GIGW version, obtain and cite the relevant official standards/notification as a separate claim. WCAG-only scanning is not proof of all the circular's requirements. |
| **3.** “Audits must be by IAAP-certified professionals” | Work order §2.2, row 3. Reported: video, one-pager. Actual files/locations unavailable. | misleading | P1, ¶5 milestone table p.4 and Annexure I C §§5.1, 5.4 pp.9–10; P3, Annexure A Table A row 2 and Table C2; P4, ¶3(a), ¶3(d) pp.1–2. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/sep-2025/1758794128066.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/dec-2025/1765194149704.pdf) | SEBI's 31 July 2025 circular expressly specifies IAAP-certified accessibility professionals, including for annual audits. Its 8 December 2025 clarification requires periodic accessibility audits through certified accessibility professionals. An automated scan is preliminary triage, not a substitute for the required professional audit and usability testing. | 2026-09-30 | IAAP wording in the original circular is confirmed. The later text does not name IAAP in ¶3(d), and ¶3(a) replaces the December auditor-appointment milestone with readiness reporting. **Neither IAAP exclusivity nor its removal is established by this wording comparison.** Obtain a written SEBI clarification on accepted auditor credentials before claiming exclusivity as a sales differentiator. No credentials or sign-off authority of our team have been verified. |
| **4.** [EXP — aggregate count only; not cleared] “Penalties of ₹10,000 on 155 establishments (Feb 2025)” | Work order §2.2, row 4. Reported: video, one-pager. Actual files/locations unavailable. | unverifiable | P6: CCPD letter digitally signed 17 February 2025, cases CCPD/15519/1101/2024 and CCPD/15530/1101/2024, ¶¶4–6 and Appendix-A. The amount/month are supported; the stated aggregate is not established. [1](https://cdnbbsr.s3waas.gov.in/s39fb7b048c96d44a0337f049e0a61ff06/uploads/2025/02/20250217228190441.pdf) | In a letter dated 17 February 2025, the Chief Commissioner for Persons with Disabilities directed a ₹10,000 penalty on each non-compliant respondent listed in Appendix-A for failure to comply with mandatory accessibility standards and the Court's directions. | 2026-09-30 | The letter does not state the alleged aggregate total. Appendix-A mixes ministries/departments with case-specific respondents and contains repeated establishments/case entries, including Pocket FM. A numbered row or case is not necessarily a unique establishment. **Settlement:** an official aggregate, or a complete respondent-level reconciliation with a stated counting unit and duplicate handling. The replacement preserves only the verified subset; the original count remains unverified. “Imposed/directed” does not establish collection, finality, or that a present-day scanner error would trigger the same penalty. These are CCPD proceedings, not a SEBI penalty schedule. |
| **5.** [EXP — unverified secondary assertion; not cleared] “Penalties of ₹50,000 on 96 repeat offenders (Jul 2025)” | Work order §2.2, row 5. Reported: video, one-pager. Actual files/locations unavailable. | unverifiable | **Required primary order not retrieved.** Seek the subsequent CCPD enforcement order and complete respondent annexure in the above suo-motu cases, or a DEPwD/CCPD official statement explicitly giving amount, unique count, and order date. Official June/July final/interim-order indexes were inspected but did not supply it. P6 is background, not evidence for this later assertion. | SEBI requires covered regulated entities to comply with digital accessibility requirements under the RPwD Act, 2016 and corresponding rules. | 2026-09-30 | Delete the entire historical amount/count/date assertion pending primary evidence. The replacement is a separate verified compliance statement, **not a softened verification of the original**. The vendor repeats a July claim, while the law-firm lead describes proceedings on 20 June 2025. Neither establishes the primary order's date or an independently reconciled count. A July press-publication date must not be substituted for an order date. No inference that the reported repeat-offender population matches the February appendix is cleared. |
| **6.** “Deadlines: audits 30 Apr 2026, remediation 31 Jul 2026, annual report 30 Apr 2027” | Work order §2.2, row 6. Reported: video. Actual script/captions/timestamps unavailable. | corrected | P2: 29 August 2025, ¶3 Table 1 rows 4–6, p.2; P3: 25 September 2025, Annexure A Table A rows 3–5 and annual footnote, p.3; **P5: 31 July 2026, ¶¶3–4, p.1**, superseding the audit/remediation dates. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1756462899734.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/sep-2025/1758794128066.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/jul-2026/1785493077212.pdf) | As checked on 30 September 2026, SEBI has extended both the digital-platform accessibility audit and remediation deadline to 31 October 2026. Annual compliance reporting remains due within 30 days of each financial year-end, effective 30 April 2027, through the reporting authority applicable to the regulated entity. | 2026-09-30 | The quoted April/July dates were genuine intermediate dates, not the current deadlines. P5 explicitly extends **both** activities and leaves other provisions unchanged. Do not state that all earlier milestones were extended. P4 separately replaces the auditor-appointment milestone with readiness reporting by 31 March 2026. Reporting is category-specific; not every RE reports directly to SEBI. Recheck circulars before any send. |
| **7.** “Supreme Court recognised digital access under Article 21, April 2025” | Work order §2.2, row 7. Reported: video. Actual script/captions/timestamps unavailable. | unverifiable | P7: Supreme Court judgment in Pragya Prasun & Ors. v. Union of India & Ors., WP(C) 289/2024, with Amar Jain, WP(C) 49/2025. **Relevant holding ¶17 and dated closing page were not directly inspectable through the primary-PDF retriever.** P1, Annexure I A p.7, verifies SEBI's own account of the 30 April 2025 judgment. [1](https://api.sci.gov.in/supremecourt/2024/17879/17879_2024_13_1501_61229_Judgement_30-Apr-2025.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf) | SEBI's 31 July 2025 circular cites the Supreme Court's judgment dated 30 April 2025 in the Pragya Prasun and Amar Jain matters, reporting that the right to digital access is an intrinsic component of the right to life and personal liberty. | 2026-09-30 | The official judgment's accessible opening establishes that it concerns disability barriers in digital KYC and invokes Article 21. A full reproduction exposes the expected holding at ¶17, but is not the required direct primary-host inspection; its webpage metadata also gives a conflicting date. **Settlement:** retrieve/read ¶17 and the signed/dated closing page of the court-hosted original (an uploaded relevant excerpt is sufficient). This is an evidence-access limitation, not a finding that the proposition is false. The replacement is expressly attributed to the verified SEBI document; do not label the original as directly judgment-verified. |
| **8.** [EXP — vendor estimate] “Remediation costs ₹2,00,000–₹8,00,000 per entity” | Work order §2.2, row 8. Reported: one-pager, video. Actual files/locations unavailable. | misleading | **No official or independently validated per-entity cost benchmark obtained.** V1, BarrierBreak's own readiness guide, FAQ “Who bears the cost of accessibility audits and remediation?” → “Remediation and platform improvements,” establishes vendor provenance only. [1](https://www.barrierbreak.com/sebi-digital-accessibility-readiness-guide/) | [EXP] BarrierBreak, an accessibility vendor, publishes an illustrative remediation range of ₹2,00,000–₹8,00,000 in its SEBI readiness guide. This is a vendor estimate, not a SEBI benchmark, an independently validated per-entity cost, or our quoted price. A scoped assessment is required before quoting a project. | 2026-09-30 | The guide says these expenses “commonly range” across code changes, screen-reader compatibility, UI redesign and PDF remediation. It supplies no inspected methodology, representative sample, or universal “per entity” definition for that range. Vendor provenance is confirmed; empirical cost validity is not. **Every retained occurrence must carry [EXP] plus attribution**, including captions, thumbnails, templates and spoken script; no propagation could be performed on missing files. Do not launder the guide's other pricing or enforcement numbers into [EST]. |
| **9.** “The mandate is annual and recurring” | Work order §2.2, row 9. Reported: one-pager, video. Actual files/locations unavailable. | confirmed | P1, ¶6 p.5 and Annexure I C §5.4 p.10; P2 ¶3 Table 1 row 6 p.2; P3 Annexure A Table A row 5/footnote p.3; P4 ¶3(d) p.2; P5 ¶4 p.1. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1756462899734.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/sep-2025/1758794128066.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/dec-2025/1765194149704.pdf) [1](https://www.sebi.gov.in/sebi_data/attachdocs/jul-2026/1785493077212.pdf) | SEBI's framework requires annual accessibility audits and annual compliance reporting, alongside continuing accessibility responsibilities. It is not a one-off exercise. | 2026-09-30 | Confirmed for recurring regulatory obligations, **not** for recurring purchases from us. The circular does not mandate a monthly scanner subscription, a particular vendor, guaranteed renewal, or a revenue amount. Reporting frequency and professional audit/usability coverage must not be conflated with automated scan frequency. |
| **10.** “CSCRF issued 20 August 2024” | Work order §2.2, row 10. Reported: CSCRF answers. Actual answers/locations unavailable. | confirmed | P8: SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113, issue-date/number header p.1 and subject p.2. [1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2024/1724326790365.pdf) | SEBI issued the Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities on 20 August 2024, through Circular No. SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113. | 2026-09-30 | This verifies issuance and identifier only. It does **not** verify our controls, applicability to a particular firm/vendor, current implementation deadlines, compliance, certification, security, or privacy promises. The original circular records earlier cybersecurity frameworks and uses a graded RE approach; do not call CSCRF the first SEBI cybersecurity requirement. Missing answers and implementation evidence are a separate release blocker. |

## Primary-document evidence — quotations and locators

Quotations below are excerpts from personally inspected retrieved text, with line breaks normalized; some excerpts end before the source sentence ends. They are not quotations from blog summaries. Extraction/encoding anomalies are not silently corrected or treated as independently verified print errors. Where extraction or access limits apply, those limits are stated. Full PDF binaries were not archived or hashed; direct sandbox downloads failed at TLS, while the page-retrieval tool returned document text.

### P1 — SEBI digital accessibility circular, 31 July 2025

[1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1754651443956.pdf)

Header, p.1: `SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/111` and `31.07.2025`.

¶3, pp.2–3:

> In order to facilitate such accessibility, it is mandated that all Digital Platforms of REs shall be compliant with the provisions of the Rights of Persons with Disabilities Act, 2016 (“RPwD Act, 2016”) and corresponding rules

¶7, p.5:

> The provisions of this circular shall be applicable to all REs with effect from the date of this circular.

Annexure I, B, pp.7–8:

> 1. Web Content Accessibility Guidelines (“WCAG”) 2.1 or latest version.
>
> 2. Accessibility guidelines as described in the latest version of Guidelines for Indian Government Websites (“GIGW”).
>
> 3. IS 17802: Indian Standards on Accessibility Requirements for Information and Communication Technology (“ICT”) Products and Services.

Point 4 additionally references the RPwD Act and corresponding rules. The three standards alone are not the complete list.

¶5, milestone table, p.4:

> Appointment of IAAP certified accessibility professionals as Auditor.

Annexure I, C §5.1, pp.9–10:

> The said accessibility audit shall include usability testing by persons with disabilities.

Annexure I, C §5.4, p.10:

> All REs shall conduct annual accessibility audits of their digital platforms including websites, mobile apps, portals through IAAP certified accessibility professionals

¶6, p.5:

> The compliance reporting for this circular shall be done on annual basis within 30 days from the end of each financial year

Annexure I, A, p.7:

> The Hon’ble Supreme Court, in its judgment dated April 30, 2025, in the matter of Pragya Prasun & Ors. Vs. Union of India and Ors. [WP(C)/289/2024] and Amar Jain vs. Union of India & Ors. [WP(C)/49/2025] pertaining to Digital Accessibility for persons with disabilities, has inter alia held that the right to Digital Access is an intrinsic component of right to life and personal liberty.

This last quotation is **SEBI's account**, not a substitute for inspection of the judgment's holding.

### P2 — SEBI extension/reporting-authority circular, 29 August 2025

[1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2025/1756462899734.pdf)

No. `SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/121`, ¶3 Table 1, p.2:

- Row 4, audit, “New Date”: `April 30, 2026`.
- Row 5, remediation, “New Date”: `July 31, 2026`.
- Row 6, annual reporting, “New Date”: `April 30, 2027`.

**Retrieved-text inconsistency:** row 5's old “Current Date” cell reads `Jan 31, 2025` in the extracted text even though the underlying circular was issued in July 2025. Verify that cell visually before diagnosing a print error; do not silently treat it as an authoritative old deadline. The operative new date is corroborated in P3 and later replaced by P5.

¶4 Table 2 maps stock brokers/DPs to exchanges/depositories, IAs/RAs to BSE Ltd., and MIIs/other REs to SEBI. Do not generalize direct-to-SEBI submission to all buyers.

### P3 — SEBI compliance guidelines, 25 September 2025

[1](https://www.sebi.gov.in/sebi_data/attachdocs/sep-2025/1758794128066.pdf)

No. `SEBI/HO/ITD-1/ITD_VIAP/P/CIR/2025/131`, Annexure A, Part A, Table A, p.3:

> Annually give compliance to conducting annual accessibility audits of all the digital platforms and submit final report of such audit to SEBI

Row 5 gives `April 30, 2027`. Its footnote states:

> Annual compliance is to be submitted within 30 days of each Financial Year, effective April 30, 2027

The annexure states that these submission guidelines apply to REs required to submit directly to SEBI. Broader reporting-authority mappings are in P2 and P4. Table C2, p.6, asks for the professional's certification details, including `IAAP ID/Certificate No.`

### P4 — SEBI clarification, 8 December 2025

[1](https://www.sebi.gov.in/sebi_data/attachdocs/dec-2025/1765194149704.pdf)

No. `HO/13/19/13(2)2025-ITD-1_VIAP/I/187/2025`.

¶3(a), pp.1–2:

> Instead of meeting the compliance requirement for appointment of accessibility auditor by December 14, 2025, REs shall submit a status of their readiness and compliance to the accessibility requirements for each of their digital platforms latest by March 31, 2026

¶3(d), p.2:

> All REs shall conduct periodic accessibility audits of their digital platforms including websites, mobile apps and portals through certified accessibility professionals

Annexure B, p.4, reporting field:

> Is minimum level of accessibility at AA level as per latest WCAG guidelines (Yes / No)

The professional-audit sentence does not say IAAP. It also does not explicitly say that the original IAAP requirement is removed. That ambiguity must not be resolved through a vendor's self-assessment or sales copy.

### P5 — SEBI extension, 31 July 2026 — decisive current deadline evidence

[1](https://www.sebi.gov.in/sebi_data/attachdocs/jul-2026/1785493077212.pdf)

No. `HO/(411)2026-ITD-5_DIV2/I/17922/2026`.

¶3, p.1:

> Based on the representations received and examination of the status of compliance of REs, the extension is granted for "Conduct of Accessibility Audit for the digital platforms and Remediation of findings from the audit" by October 31,2026.

¶4, p.1:

> All other provisions of the aforementioned circulars shall remain unchanged and shall be complied by REs.

A current-date search of SEBI's public circular listings and digital-accessibility notices did not surface a later change during this session. This is a bounded search, not a guarantee that no later instrument exists; recheck before sending material.

### P6 — CCPD February enforcement letter

[1](https://ccpd.nic.in/letter-dated-17-feb-2025-imposing-fine-on-establishments-which-have-not-complied-with-filing-access-audit-report-or-the-letter-of-engagement-of-access-auditor/) provides the official link to [1](https://cdnbbsr.s3waas.gov.in/s39fb7b048c96d44a0337f049e0a61ff06/uploads/2025/02/20250217228190441.pdf).

Cases `CCPD/15519/1101/2024` and `CCPD/15530/1101/2024`; digital signature dated `17-02-2025`.

¶4:

> In view of the above, this Court has now decided to impose a penalty of ₹10,000/- each on all respondent establishments which have not complied with the mandatory accessibility standards, and this Court’s direction. A list of all such respondents is enclosed at Appendix-A.

¶6:

> after 28th February, 2025, a fresh review will be undertaken

The letter warns of higher fines for continuing non-compliance. It does not supply the alleged aggregate total, the later repeat-offender order, or evidence that all directed fines were paid. Appendix-A's duplicate entries prevent treating its row count as a verified unique-establishment count without reconciliation.

### P7 — Supreme Court judgment: relevant text access incomplete

Court-hosted original located: [1](https://api.sci.gov.in/supremecourt/2024/17879/17879_2024_13_1501_61229_Judgement_30-Apr-2025.pdf).

The opening names both writ petitions and the judgment author, R. Mahadevan, J. ¶3 states that the petitions seek accessible alternatives for digital KYC for persons with disabilities and refer to Article 21. **Those are the petitions' subject/prayers, not proof of the Court's final holding.**

The primary-PDF retriever exposes only the first 30 pages; its final returned chunk is still in respondent submissions (§9.5). It does not expose the relevant ¶17 or the closing date/signature page. Direct local downloads also failed at TLS.

A reproduction of the judgment was inspected as a **lead only**, not accepted as the primary settlement: [4](https://www.latestlaws.com/latest-caselaw/2025/april/2025-latest-caselaw-485-sc/). Its ¶17 contains the expected digital-access/right-to-life wording. Its webpage metadata says 29 April while the court-PDF link names 30 April; this reinforces the need to inspect the original closing page. P1 independently confirms **SEBI's account** of a 30 April judgment. Obtain the relevant court-original pages to clear claim 7.

### P8 — SEBI CSCRF, issuance only

[1](https://www.sebi.gov.in/sebi_data/attachdocs/aug-2024/1724326790365.pdf)

Header, p.1:

> August 20, 2024
>
> SEBI/HO/ ITD-1/ITD_CSC_EXT/P/CIR/2024/113

Subject, p.2:

> Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities (REs)

The initial pages and issuance metadata were inspected. **The complete framework, later amendments, and our implementation were not audited.** Confirmation of the issuance claim must not be reused as a security sign-off.

## Vendor provenance and unresolved research trails

### V1 — cost estimate is [EXP]

BarrierBreak's own guide: [1](https://www.barrierbreak.com/sebi-digital-accessibility-readiness-guide/), FAQ “Who bears the cost of accessibility audits and remediation?” → “Remediation and platform improvements.”

[EXP — vendor statement; not an independent benchmark] The inspected text says:

> Expenses for application code updates, screen-reader compatibility improvements, user interface redesigns, and accessible PDF remediation commonly range from Rs. 2,00,000 to Rs. 8,00,000.

This is sufficient to establish **who published the estimate**, not its empirical validity or a universal per-entity price. The guide also retained pre-extension dates in its timeline section when inspected. Its pricing paragraph must not confer authority on its regulatory summaries.

### Penalty-count trails — leads are not settlements

- The vendor's enforcement summary was found at [1](https://www.barrierbreak.com/sebi-circular-july-31-2025-mandatory-digital-accessibility-for-financial-sector-entities/). Its claimed aggregate counts remain secondary assertions [EXP], not cleared facts.
- The law-firm lead [3](https://www.azbpartners.com/bank/bridging-the-digital-divide-indias-evolving-accessibility-framework/) links the February letter and a newspaper report; it describes later proceedings on 20 June 2025. The law-firm text and linked press report are not substitutes for the later primary order.
- Official indexes inspected: [1](https://ccpd.nic.in/june-2025-orders/), [1](https://ccpd.nic.in/june-2025-interimorders/), [1](https://ccpd.nic.in/july-2025-orders/), [1](https://ccpd.nic.in/july-2025-interimorders/). The sought later enforcement order was not retrieved from these listings. Do **not** turn “not found in this search” into “does not exist.”

## Drift, labels, omissions, and release actions

| Check | Result this session | Required next action |
| --- | --- | --- |
| Compare every copy of a number/date | Blocked: only the work order's claim list was available. No assertion of zero drift is made. | Supply one-pager, script/captions, video text overlays, templates and CSCRF answers; build exact file/line or timestamp locators for every occurrence. |
| Find the remaining claims | Blocked: pitch and earlier artifacts absent. README has no substantive pitch claims. | Enumerate every material factual assertion, numerical result and security promise before task completion. |
| Existing [EST] labels | Not inspected; no existing material was supplied. | Require a primary/peer-reviewed citation for each [EST]; downgrade secondary estimates to [EXP], and remove unverifiable assertions rather than merely relabeling them. |
| Cost label propagation | Correct replacement prepared, **not applied to absent files**. | a3-content must use the claim 8 wording and [EXP] label at every retained occurrence, then submit v2 files for re-verification. |
| Deadline propagation | Current primary-source correction prepared. | Replace both audit and remediation dates in every occurrence; retain a checked-on date and category-specific reporting qualifications. |
| Auditor exclusivity | Text difference confirmed; legal resolution outstanding. | h1-human to obtain authoritative clarification before retaining an exclusive-qualification sales claim. Do not claim we have credentials that have not been inspected. |
| Omissions about testing | P1 expressly requires usability testing by persons with disabilities. | Do not sell an automated public-page scan as a complete statutory audit, a certificate, or proof that entire investor journeys are accessible. |
| Recurring-revenue thesis | Annual legal obligation confirmed; willingness to buy/renew not established. | Validate the actual buyer and scope. Do not equate annual compliance with mandatory monthly SaaS spending. |
| ₹0 delivery plan | No actual plan/credentials/compatible test operator supplied. | Reuse existing compatible resources if available. If qualified human audit or required screen-reader testing cannot be arranged without spending, hold the promise and escalate any proposed expenditure to h1-human. No purchase is authorized here. |
| CSCRF security/privacy promises | Cannot inspect missing answers or implementation. | Hold any such send until each answer is mapped to implemented controls, data flows, retention, access controls and other supporting evidence. Do not infer company compliance from P8. |

## Completion status

**Source-level first pass on the ten supplied claims: recorded. Full Task 1 acceptance: not met.** Exact file locations, discovery of remaining claims, cross-file comparisons, label/correction propagation, and final content re-verification are outstanding. The unverified claims also require the evidence specified in their notes before the original assertions can be approved.

**Manual handoff to a3-content:** apply paste-ready corrections only to actual supplied files, publish v2 with a change manifest, and return the changed files plus all claim occurrences for a4 verification. Do not mark the current draft approved or the task done based on this document.
