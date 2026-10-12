# Signal — evidence review, refutation log and buildable backlog

**Agent:** a5 · **Version:** v1 · **Date compiled:** 2026-10-12 (all "checked on" dates = 2026-10-12 unless stated)
**Product under review:** *Signal* — an internship / early-career job-signal tracker for students (stores filters; monitors LinkedIn, Internshala, Unstop and company career pages; verifies a listing is still live at source; extracts a structured summary; alerts the student; optionally prefills applications with explicit consent).
**Markets in scope:** India **and** the United States. Every finding below is tagged with the setting it was measured in. Cross-country generalisation is treated as unproven throughout.
**Companion artifact:** `artifacts/signal-evidence-table-a5-v1.csv` (same evidence table, machine-readable, 51 rows).

## How to read the labels

| Label | Meaning |
|---|---|
| `[PEER]` | Peer-reviewed journal or reviewed conference proceedings |
| `[PREPRINT]` | arXiv/SSRN/working paper, not peer-reviewed |
| `[GOV]` | Government, official statistics, or primary law |
| `[VENDOR]` | Company-published research; the publisher usually sells a related product |
| `[DOCS]` | Product/API documentation or a site's own access policy file |
| `[SECONDARY]` | Law-firm note, reproduction, or summary used because the primary source could not be opened |
| `[UNVERIFIED]` | Could not open the source itself; metadata only, or blocked |
| causal / correlational / self-reported | Stated per claim |

Rules applied: every page cited below was opened in this session — nothing is cited from memory — and the handful of sources whose primary text could not be reached carry `[SECONDARY]` or `[UNVERIFIED]` and are listed again in §10.3. Numbers are quoted exactly as published, with the sample and year, and each is marked causal, correlational or self-reported. Where a sub-question has no supporting evidence, it says **NO EVIDENCE FOUND** and lists the queries tried.

---

## Verdict on the five anchor claims (read this first)

| Anchor | As briefed | Verdict after review |
|---|---|---|
| **A** Ghost jobs ~21% (Ng 2024) and 55% / 1.63× (SSRN 5987416) | "≈1 in 5 postings are fake" | **Overstated and mis-unitised.** Ng's 21% is computed over Glassdoor *interview reviews* (56,559 flagged of ~269,347), not postings; a keyword baseline on the same corpus gives 1.3–1.6%. SSRN 5987416 computes 55% on **160 of its 414** postings, 89.6% US, 56.8% software. CRS (Apr 2025) states there are **no official statistics**. **Keep the problem, drop the number.** |
| **B** Search intensity declines within a spell (Faberman & Kudlyak 2019) | "Users burn out, so nudge them" | **True in the source, but the inversion matters more:** longer-duration seekers search *more* intensely throughout. A 2025 Swedish study (2.4m activity reports) finds within-spell effort essentially **flat**. Decay is setting-specific; the robust driver of discouragement is falling callbacks, not time. |
| **C** Breadth wins: +44% interviews (Belot/Kircher/Muller 2019); internships +14% callbacks (Nunley 2016) | Two solid causal results | **Partly confirmed, with a sharp caveat.** The 44% is real and in the paper — but it is significant at the **10% level only**, on ~300 Edinburgh job seekers, and the authors show you would need **3,794 subjects per arm** to detect the implied job-finding effect. The same team's larger UK scale-up (EJ, accepted 2025) reports +20–40% on pre-registered stable-job/earnings outcomes. Nunley's +14% stands. |
| **D** Agents ~55–60% web task success (WebVoyager 2024; Mind2Web 2023), safety measured separately (ST-WebAgentBench) | Plan on ~57% | **Wrong as written.** Mind2Web is an *offline dataset on static snapshots* and reports **2.0% task success** for GPT-4 (36.2/30.1/26.4% step success). On 300 tasks over 136 **live** sites, most frontier agents hit **~30%** (best: Operator 61.3%). A naive search-and-click agent scores 51% on WebVoyager but 22% on the live set. **Plan on ≈30%.** And ST-WebAgentBench shows Completion-under-Policy is **under two-thirds** of nominal completion. |
| **E** Freshness as budgeted scheduling (Cho & Garcia-Molina 2003); official OJA pipelines dedup across portals (Eurostat/Cedefop) | Correct framing | **Confirmed — and it contains a trap.** Cho & Garcia-Molina's own results show the intuitive *proportional* policy ("poll volatile boards more") is the **worst** (freshness 0.12 vs 0.57 uniform vs 0.62 optimal; age 400 days vs 5.6 vs 4.3). Eurostat/Cedefop's three-stage dedup (physical → semantic → logical) is a directly copyable design. |

---

## 1. Evidence table

51 rows, one per source. Full machine-readable version with extra columns (`evidence_type`, `setting`, `verification`) in `artifacts/signal-evidence-table-a5-v1.csv`.

### A — Ghost listings and staleness

| # | Citation + link | Method & sample | Headline estimate | Design strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| A01 | `[PREPRINT]` Ng, H. (2024). *Why Is It So Hard to Find a Job Now? Enter Ghost Jobs.* arXiv:2410.21771, 29 Oct 2024. [link](https://arxiv.org/abs/2410.21771) | BERT classifier over ~269,347 English Glassdoor **interview reviews**; 56,559 flagged. Unit = a review, not a posting. US. Observational. | "Up to 21%"; keyword baseline on the same corpus 1.3–1.6%. By sector: Publishing 34.4%, Internet & Web 30.1%, Software Dev 29.8%, Commercial Printing 12.2%. No CIs in abstract. | Weak–moderate: self-selected reviewers; 13× spread between methods on identical data | No | Never show "21% of listings are fake" in product; measure Signal's own dead-listing rate instead. |
| A02 | `[GOV]` Congressional Research Service (2025). *Ghost Job Postings*, IF12977, 25 Apr 2025. [link](https://www.congress.gov/crs_external_products/IF/HTML/IF12977.web.html) | Official review of US vacancy data and the vendor literature. | **No official statistics exist.** JOLTS counts an opening only if a specific position exists, work could start within 30 days, and the employer is actively recruiting outside workers. CRS flags that vendor surveys have opaque methods and the vendors sell verification tools. | Strong as a statement about data availability | n/a | The only defensible claim Signal can make is per-listing and timestamped: "checked at 09:14 IST against the employer's Greenhouse board." |
| A03 | `[PREPRINT]` Santhosh & Jennifer (2025). SSRN 5987416, posted 30 Dec 2025, 12 pp., zero references. [link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5987416) | N=414 postings, Jun–Oct 2025, volunteer applicant panel; **only 160 classifiable**; 89.6% US users; 45.7% LinkedIn-sourced; 56.8% software engineering. Self-reported. | 55.0% of classified postings (88/160) problematic; confidential employer 77.5% vs named 47.5% = **1.63×, p<0.05**. | Very weak: convenience sample, 62% unclassified, no pre-registration | No | The *confidential-employer* flag is cheap and testable; the 55% is not quotable and does not transfer to Indian internships. |
| A04 | `[VENDOR]` Greenhouse (2024). *2024 State of Job Hunting report*, 10 Dec 2024. [link](https://www.greenhouse.com/blog/greenhouse-2024-state-of-job-hunting-report) | Survey of 2,500 workers (US/UK/Germany) + undisclosed internal classification of postings on the Greenhouse platform. Self-reported + proprietary. | **18–22%** of jobs posted on Greenhouse classified as ghost jobs in any quarter; 3 in 5 candidates suspect a ghost job; 61% ghosted post-interview; **15% of candidates oppose any AI involvement in hiring**; 28% want more clarity on AI use. | Weak: classifier and denominator undisclosed | Same order as Ng by a different, undisclosed method — convergence ≠ replication | Consent and disclosure are features: a sixth of candidates reject AI in hiring outright. |
| A05 | `[VENDOR]` ResumeBuilder.com (2024). *3 in 10 Companies Currently Have Fake Job Postings Listed*, upd. 18 Jun 2024. [link](https://www.resumebuilder.com/3-in-10-companies-currently-have-fake-job-posting-listed/) | Pollfish online panel, launched 22 May 2024; 1,641 hiring managers screened, 649 completed; screener required admitting a fake posting. Self-reported. | 40% of companies posted a fake listing in the past year; 79% of those have one active; kept active ~1 month (31%), 3 months (19%), ≥1 year (9%); posted on company site 72%, LinkedIn 70%, Indeed 49%. | Very weak: self-selection plus a leading screener | No | Use only as a prior on **where** stale postings live (career sites and LinkedIn), never on how many. |
| A06 | `[VENDOR]` Clarify Capital (2022). *Job Seekers Beware of Ghost Jobs*, fielded 31 Aug–1 Sep 2022. [link](https://clarifycapital.com/job-seekers-beware-of-ghost-jobs-survey) | 1,045 hiring managers, two-day online fielding. Self-reported. | 68% had a posting active >30 days; 1 in 10 >6 months; 50% keep postings open because they are "always open to new people"; 40% do not expect to fill active posts for 2–3 months. | Very weak; conflates slow hiring with no hiring | No | Age alone is not deadness. Any "stale" label must be backed by a source check, not a date. |
| A07 | `[VENDOR, sceptic]` LinkUp (2023). *The Absurd Myth of 'Ghost Jobs'*. [link](https://www.linkup.com/insights/blog/the-absurd-myth-of-ghost-jobs) | Census of postings indexed **directly from company career sites**: 5–7m US / 10–11m global per month; 2.14m unique jobs removed in March 2023. Observational. | Average closed duration **45.6 days** (12-month US time-to-fill 46 days). Of jobs removed in Mar 2023: 58% were up <30 days, 35% 1–6 months, **7% >6 months** (up from 4% in May 2022). Explicitly: board data is polluted by syndication, pay-to-post and expired listings. | Moderate for duration; cannot observe intent | Directionally consistent with vacancy-duration statistics | Make ATS/career-site feeds the ground truth and treat aggregator copies as derived. A 30-day-old posting is normal. |
| A08 | `[PEER-EDITED LAW]` Grimm, D. J. (2025). *Ghost Jobs*, 125 Colum. L. Rev. F. 183 (13 Nov 2025), pp. 183–204. [link](https://www.columbialawreview.org/wp-content/uploads/2025/11/November-2025-Forum-Grimm.pdf) | Doctrinal analysis of FTC Act §5 applied to ghost jobs. Legal argument, not measurement. | Argues ghost jobs are actionable as unfair/deceptive practices; reports (citing CNBC/Revelio Labs) that hires per ten listings fell from **8 to 4 between 2019 and 2024**; notes a résumé-coaching vendor claiming 1.7m "potential ghost jobs" on LinkedIn. | Strong as legal analysis; cited prevalence is vendor-grade | n/a | Deception law is arriving. Signal's own labels must be literally true, timestamped and sourced — they are marketing claims with regulatory exposure. |
| A09 | `[PEER]` Albrecht, Decreuse & Vroman (2023). *Directed Search with Phantom Vacancies*, International Economic Review 64(2): 837–869. [link](https://onlinelibrary.wiley.com/doi/abs/10.1111/iere.12615) · WP PDF [link](https://faculty.georgetown.edu/vromans/PhantomsMarch2017Final.pdf) | Directed-search model: filled ads persist as "phantoms"; calibrated to US data 2000–2008 using the Craigslist listing-age distribution. Theory + calibration (not causal). | In the working-paper calibration: **~70% of applications go to listings <48h old**; applicants per listing falls **more than 5×** between day 1 and day 2; phantoms account for ~28% of unemployment and ~85% of friction-driven unemployment. | Strong theory; calibration is model-dependent | Builds on Chéron & Decreuse (2017, REStud) | Freshness is already the dominant signal students use. Signal's edge is the **accuracy** of the freshness claim, not the idea. |
| A10 | `[WORKING PAPER]` Fradkin, Bhole & Horton. *Competition Avoidance vs Herding in Job Search.* [link](https://andreyfradkin.com/assets/jobs_authors.pdf) | Three randomised field experiments on Jobs on Facebook, Mar–Aug 2019, millions of job seekers; 21–25% US; median user 31–33; mostly non-degree roles. **Causal.** | Showing prior-applicant counts raised applications to vacancies with <5 prior applicants by **3.8%** (range 0.9–6.4%) and reduced them to crowded ones. **Removing vacancy age cut clicks 3% and applications 1.8%.** | Strong internal validity; platform-specific | Partially replicates and qualifies Gee (2019) | Posting age is an input students actively use. Show both age and last-verified time; hiding age suppresses engagement. |
| A11 | `[PEER]` Gee, L. K. (2019). *The More You Know*, Management Science 65(5): 2077–2094 (IZA DP 10372). [link](https://www.iza.org/publications/dp/10372/the-more-you-know-information-effects-on-job-application-rates-in-a-large-field-experiment) | ~2.3m LinkedIn job seekers, March 2012, ~100,000 postings; member-level randomisation. **Causal.** | Showing the number of prior applicants raised the probability of finishing an application by **3.5%**; larger effect for women. | Strong; 2012 platform context | Extended (and partly contradicted on direction of reallocation) by A10 | Metadata labels move behaviour by single-digit percentages. Do not budget for big behaviour change from badges. |

### B — Search behaviour, decay and attention

| # | Citation + link | Method & sample | Headline estimate | Design strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| B01 | `[PEER]` Faberman & Kudlyak (2019). *The Intensity of Job Search and Search Duration*, AEJ: Macro 11(3): 327–357, DOI 10.1257/mac.20170315. [link](https://www.aeaweb.org/articles?id=10.1257/mac.20170315) · WP [link](https://www.frbsf.org/wp-content/uploads/sites/4/wp2016-13.pdf) | SnagAJob (US hourly/low-wage) application microdata over one year. WP reports **10.11m job-seeker-week observations, 17.26m applications to 1.41m vacancies by 4.77m job seekers**. Correlational (panel with fixed effects). | Within a spell, applications/week **decline** (~2.3 in week 1 → ~1.2 by week 4). Longer-duration seekers send **more** applications throughout; they are older, male, nonemployed, in weak local markets. Replication package DOI 10.3886/E116417V1. | Strong measurement; low-wage segment; not causal | Qualified by B02, contradicted in part by B03 | Design for within-spell decay — but never treat long-duration users as low-effort. They are the power users. |
| B02 | `[WORKING PAPER]` Lalive, Osikominu, Pesaresi, Zuchuat & Zweimüller (2025). *Duration Dependence in Finding a Job*, ROCKWOOL Berlin DP 15/25 (earlier IZA DP 16602). [link](https://www.rfberlin.com/wp-content/uploads/2025/04/25015.pdf) | 58,000 digitised monthly search diaries; **600,000 applications by 15,000 Swiss job seekers**; each application linked to interview and offer. Descriptive + structural. | Applications fall from **11/month in month 1 to just under 10 in months 12–15**; interviews per application fall; **offers per interview rise**. IZA version: 55% of the job-finding decline is true duration dependence, 45% dynamic selection. | Strong (linked application→outcome data) | Same direction as B01 on applications | The thing that decays first is *response*, not effort. Evidence-of-response features beat volume features. |
| B03 | `[PREPRINT]` Cederlöf & Roman (2025). *Duration Dependence and Job Search over the Spell*, arXiv:2511.03377, 5 Nov 2025. [link](https://arxiv.org/html/2511.03377v1) | 2.4m monthly job-seeker activity reports (Sweden); time-and-spell fixed effects. Correlational with strong design. | Raw effort **rises** with duration, but within-spell effort is **flat** and falls sharply only just before re-employment; **86–90%** of the callback decline is dynamic selection, 10–14% true duration dependence. | Strong design; different institution | Directly contradicts the strong reading of decay | "Effort decays" is not a universal law. Measure decay in Signal's own cohort before building anti-decay mechanics. |
| B04 | `[PEER]` Liu, Huang & Wang (2014). *Effectiveness of Job Search Interventions: A Meta-Analytic Review*, Psychological Bulletin 140(4): 1009–1041. [link](https://www.academia.edu/26462337/Effectiveness_of_Job_Search_Interventions_A_Meta_Analytic_Review) | Meta-analysis of 47 experimental / quasi-experimental interventions. | Odds of employment **2.67×** higher for participants; short-term unemployed OR 3.54 vs long-term OR 1.72; effective **only** when skill-building *and* motivation components were both present. | Moderate–strong; heterogeneous, pre-2014 | Meta-analytic by construction | Pure information (alerts) is the component that historically does **not** move employment on its own. |
| B05 | `[PEER]` Altmann, Falk, Jäger & Zimmermann (2018). *Learning about job search*, J. Public Economics 164: 33–49. [link](https://ideas.repec.org/a/eee/pubeco/v164y2018icp33-49.html) | Large brochure RCT with newly unemployed in Germany; administrative outcomes. **Causal.** | Average effects positive but **mostly insignificant**; for job seekers at high risk of long-term unemployment, employment and earnings rose **~4%** over the following year. | Strong | Consistent with B04 on targeting | Target guidance at the at-risk tail. Broadcast advice has ≈0 average effect. |
| B06 | `[WORKING PAPER]` Ben Dhia, Crépon, Mbih, Paul-Delvaux, Picard & Pons (2022). *Can a Website Bring Unemployment Down?* NBER WP 29914. [link](https://www.nber.org/papers/w29914) | Encouragement-design RCT, **212,277** French job seekers; 18 months of administrative follow-up; 47,327 survey responses (22.3%). **Causal.** | **No effect** on search time, search scope, wellbeing, or any employment outcome. "Precise nulls" owing to scale. Modest shifts in search methods only. | Very strong | Null replicates across outcomes | A job-search-advice website does not reduce unemployment. Sell avoided waste and saved time; do not promise outcomes. |
| B07 | `[WORKING PAPER]` Kelley, Ksoll & Magruder (2023 version). *How do Online Job Portals affect Employment and Job Search? Evidence from India.* [link](https://www.povertyactionlab.org/sites/default/files/research-paper/WP3740_Online-Job-Portals-in-India_Magruder-et-al_Aug2023.pdf) | RCT Apr 2015–Sep 2016, vocational-training graduates in India; platform Job Shikari (SMS); arms: uploaded to portal vs uploaded + ~16 extra SMS. **Causal.** | Portal access **reduced employment by 9.2pp (−30% vs control)**, persisting 12 months; the extra-information arm attenuated this to **−4.8pp (−16%)**; reservation wages +2.2% (treatment) and **−5.3%** (priority). | Strong; dated platform; low-skill trades | Not replicated in India | **The single most important India finding:** alerts that raise expectations without calibrating them can lower employment. Ship base rates with every alert. |
| B08 | `[WORKING PAPER — abstract only, UNVERIFIED beyond abstract]` Hensvik, Le Barbanchon & Rathelot (2021). *Do algorithmic job recommendations improve search and matching?* [link](https://www.semanticscholar.org/paper/Do-algorithmic-job-recommendations-improve-search-a-Hensvik-Barbanchon/27538a761eb3b8e22b6052c6e54f32f75a76f18e) | Two-sided randomised experiment on Sweden's largest job board; collaborative filtering. **Causal (per abstract).** | Clicks/applications on recommended vacancies **+10–16%**; **no** average effect on total search intensity, job finding or earnings. | Strong design per abstract; preliminary 2020 results | Consistent with B06 | Recommenders reallocate attention without creating matches. Optimise for avoided waste, not CTR. |
| B09 | `[PEER]` Okoshi et al. (2015/2016). *Towards attention-aware adaptive notification on smart phones* (Attelia), Pervasive and Mobile Computing. [link](https://www.sciencedirect.com/science/article/abs/pii/S1574119215001881) · companion PDF [link](https://www.julian-ramos.com/papers/Okoshi2015.pdf) | In-the-wild study, **30 participants, 16 days**, breakpoint-timed vs randomly timed notifications; plus a controlled lab study. | **28% lower frustration** for interruption-sensitive users; response time **13% faster**; lab study **46% lower cognitive load** for the sensitive cluster. A later Yahoo! JAPAN deployment with **>680,000 users** reported **49.7% faster** responses. | Moderate (small n, subjective measures) | Large-scale industrial follow-up | Alert **timing** is a bigger lever on tolerance than alert content. Make delivery windows user-set and quiet-hours-aware. |
| B10 | `[PEER]` Pielot et al. (2017). *Predicting Opportune Moments to Engage Mobile Phone Users*, ACM IMWUT/UbiComp. [link](https://pielot.org/pubs/Pielot2017-UbiComp-Engagement.pdf) | Field study, **337 participants, ~4 weeks**; 120m phone-use events; 78,930 prompts; 30,689 responses; 3,367 voluntary engagements. | Classifier-timed engagement lifted conversion precision from **0.043 → 0.071 (+66.6% relative)** without silencing users. | Moderate–strong | Consistent with B09 | Budget for ~5–7% engagement on proactive nudges. Design alert caps around that reality. |

### C — Breadth, matching and skills

| # | Citation + link | Method & sample | Headline estimate | Design strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| C01 | `[PEER]` Belot, Kircher & Muller (2019). *Providing Advice to Jobseekers at Low Cost*, Review of Economic Studies 86(4): 1411–1447, doi 10.1093/restud/rdy059. [link](https://academic.oup.com/restud/article/86/4/1411/5115940) | ~300 unemployed job seekers in **Edinburgh, UK**, invited to 12 weekly supervised search sessions; treatment interface suggested alternative occupations with high skill transferability. **Causal.** | Occupational breadth **+0.2 SD** (≈ the broadening that occurs naturally over 3 months); **total interviews +44%, significant at the 10% level only**; driven entirely by initially narrow searchers; baseline 0.61 interviews/week → 0.89. Authors: detecting the implied job-finding effect would need **3,794 per arm**. | Moderate: randomised but small; headline is p<0.10; out-of-lab interviews self-reported | Scale-up in C02 | Build breadth suggestions; promise "more interviews **for narrow searchers**", never "+44% interviews". |
| C02 | `[AUTHOR PAGE — UNVERIFIED]` Belot, Kircher & Muller (accepted 2025), Economic Journal — UK long-term unemployed scale-up. [link](https://philippkircher.com/publications/providing-advice-job-seekers-low-cost-experimental-study-online-advice/) | Randomised field experiment, **~1,500** long-term unemployed UK job seekers; advice embedded in a provider's search engine. Pre-registered primary outcomes. | Effects on "finding a stable job" and a cumulative-earnings threshold **positive and large: 20–40% after 9 months**. | Potentially strong; full paper not opened | Scale-up of C01 | The breadth mechanism survived a pre-registered scale-up on exactly the stuck-searcher population. Rank it above freshness-only features. |
| C03 | `[PEER]` Nunley, Pugh, Romero & Seals (2016). *College major, internship experience, and employment opportunities*, Labour Economics 38: 37–46, doi 10.1016/j.labeco.2015.11.002. [link](https://ideas.repec.org/a/eee/labeco/v38y2016icp37-46.html) | Résumé audit of business-related openings in the **US**; randomised internship experience and major on fictitious résumés. **Causal (for callbacks).** | Internship experience raises the interview rate by **14%**; **no** detectable benefit from a business degree; signalling favoured as the mechanism. | Strong for callbacks; silent on hires | Consistent with the wider audit literature | Internship experience is the strongest controllable callback lever for students — foreground it in profile completeness, above GPA or coursework. |
| C04 | `[PEER]` Crépon, Duflo, Gurgand, Rathelot & Zamora (2013). *Do Labor Market Policies Have Displacement Effects?* QJE 128(2): 531–580. [author summary link](https://cepr.org/voxeu/columns/job-placement-and-displacement-evidence-randomised-experiment) | Two-level clustered RCT; **~30,000** young educated job seekers; 235 French communities; 2007–2010. **Causal.** | Treated **+2.5pp** long-term employment at 8 months; **untreated peers in treated areas −2.1pp**; net effect small and insignificant; gains gone by 12 months; in the tightest markets controls were **7.7pp worse off**. | Strong (designed for displacement) | Landmark | Helping one student apply first can take the slot from another. Never market Signal as creating opportunity; measure match quality. |
| C05 | `[PREPRINT]` Skill-LLM (arXiv:2410.12052, Oct 2024) comparative results on the SkillSpan benchmark. [link](https://arxiv.org/html/2410.12052v1) | Span-F1 on SkillSpan (English job ads), exact-span matching. | JobSpanBERT **58.9**, ESCOXLM-R **62.6**, NNOSE **64.2**, fine-tuned LLaMA-3-8B **64.8**; **GPT-4 few-shot only 27.8**. | Moderate (public benchmark; harsh metric) | Benchmark reused across papers | Skill extraction tops out ≈65 F1. Show extracted fields **with the source snippet** as "from the posting", never as verified requirements. |
| C06 | `[PEER]` Nguyen et al. (2024). *Rethinking Skill Extraction in the Job Market Domain using LLMs*, NLP4HR @ EACL 2024. [link](https://aclanthology.org/2024.nlp4hr-1.3.pdf) | Six skill-extraction datasets (SkillSpan, Green, Fijo, Kompetencer, Gnehm, Sayfullina); LLM prompting vs supervised. | Supervised average **64.4 F1**; LLM prompting far lower; **17–22%** of errors involve conjoined skills ("Python and SQL"); **8%** of errors trace to wrong gold annotations. | Moderate–strong (multi-dataset error taxonomy) | Multi-dataset by construction | Errors cluster in bullet-list requirement text. Parse lists conservatively; keep the raw snippet visible for every extracted field. |

### D — Agents, extraction and trust

| # | Citation + link | Method & sample | Headline estimate | Design strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| D01 | `[PEER]` He et al. (2024). *WebVoyager*, ACL 2024, arXiv:2401.13919. [link](https://arxiv.org/abs/2401.13919) | 643 tasks over **15 real websites**; GPT-4V multimodal agent; automatic evaluator validated against humans. | **59.1%** task success; auto-evaluation agrees with humans **85.3%**. | Moderate: live sites, curated and known task set | Re-tested by D03 | 59% is the optimistic ceiling on familiar sites — not a planning number. |
| D02 | `[PEER]` Deng et al. (2023). *Mind2Web*, NeurIPS 2023 D&B, arXiv:2306.06070. [link](https://arxiv.org/abs/2306.06070) | **2,350 demonstrations, 137 websites, 31 domains**, avg 10.59 actions/task. Evaluation **replays static snapshots**, not live sites. | Paper publishes **no live task-success rate**. MindAct w/ GPT-4: step success **36.2 / 30.1 / 26.4%** (cross-task / -website / -domain), **task success 2.0%** on all three; best fine-tuned model **5.2%** (cross-task). | Strong as a dataset; weak as evidence about live agents | n/a | **Anchor D's citation is wrong.** Mind2Web's own task-success numbers are single digits. Figures read from the UK AI Safety Institute `inspect_evals` reproduction of the paper's table `[SECONDARY]` ([link](https://ukgovernmentbeis.github.io/inspect_evals/evals/mind2web/index.html)). |
| D03 | `[PEER]` Xue et al. (2025). *An Illusion of Progress? Assessing the Current State of Web Agents*, COLM 2025, arXiv:2504.01382 (Online-Mind2Web). [link](https://arxiv.org/html/2504.01382v4) | **300 tasks across 136 live websites**, human evaluation; WebJudge auto-evaluator (85.7% human agreement). | Most frontier agents **~30%**; Operator **61.3%**, Claude Computer Use 3.7 **56.3%**, SeeAct **30.7%**. A naive Google-search-and-click agent scores **51% on WebVoyager but 22% here**. Easy→medium drop **−31.6pp**. | Strong (human-evaluated, live, adversarial to benchmark inflation) | Direct re-test of D01 | **Plan Signal's agent for ≈30% unaided success on unseen sites.** Every agent path needs a deterministic fallback and a human-visible failure state. |
| D04 | `[PEER]` Levy et al. *ST-WebAgentBench*, arXiv:2410.06703 (v7, ICLR 2026). [link](https://arxiv.org/abs/2410.06703) | **222 tasks**, each paired with organisational safety/trust policies across six orthogonal dimensions including **user consent**. | Introduces **Completion under Policy (CuP)** and **Risk Ratio**; across three SOTA agents, average CuP is **less than two-thirds** of nominal completion. | Strong for policy-violation measurement; synthetic enterprise apps | New metric | Roughly a third of apparently successful agent runs break a stated policy. Consent gates and read-only defaults are mandatory, not optional. |
| D05 | `[PEER]` Debenedetti et al. (2024). *AgentDojo*, NeurIPS 2024 D&B. [link](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) | **97 realistic tasks, 629 security test cases**, four tool suites, 10 models, 95% CIs reported. | Best agents solve **<66%** with no attack. GPT-4o: benign utility **69.0%**, utility under attack **50.1%**, targeted attack success **47.7%**. A **tool-filter** defence cuts ASR to **~7.5%**; all defences cost **15–20%** utility under attack; injections late in a tool response reach **~70%** ASR. | Strong, with CIs | Widely reused | Job-posting text is attacker-controlled input. Never let one agent read a posting and submit a form in the same unsupervised step; use read-only tools for parsing. |
| D06 | `[PEER]` Xiong et al. (2024). *Can LLMs Express Their Uncertainty?* ICLR 2024, arXiv:2306.13063. [link](https://arxiv.org/pdf/2306.13063) | Confidence-elicitation benchmark across 5 LLMs and 8 datasets; calibration and failure prediction. | Verbalized confidence is **systematically overconfident**, clustering at 80–100% in multiples of 5; average **ECE > 0.377** for GPT-3/3.5/Vicuna; calibration improves with capability. | Strong (multi-model) | Confirmed in later surveys | Never surface a model's self-reported confidence as a freshness or extraction score. Calibrate against observed outcomes. |
| D07 | `[PEER]` *Evidence of a social evaluation penalty for using AI*, PNAS 122(19), 8 May 2025. [link](https://www.pnas.org/doi/10.1073/pnas.2426766122) | **Four preregistered experiments, N = 4,439**, including an incentive-compatible hiring task. **Causal.** | People who use AI **anticipate and receive** worse evaluations of competence, diligence and motivation; managers who do not use AI act on this **in hiring decisions**. | Strong (preregistered, incentive-compatible) | Converges with Schilke & Reimann (2025), *Organizational Behavior and Human Decision Processes* 188:104405 `[UNVERIFIED — abstract seen only via citing works]` | Automated submission risks the student's **reputation with the employer**, not just their privacy. Default to assist-and-review and let the student control disclosure. |

### E — Freshness, dedup, identity and feed access

| # | Citation + link | Method & sample | Headline estimate | Design strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| E01 | `[PEER]` Cho & Garcia-Molina (2003). *Effective page refresh policies for web crawlers*, ACM TODS 28(4): 390–426. [link](http://oak.cs.ucla.edu/~cho/papers/cho-tods03.pdf) · [ACM DL](https://dl.acm.org/doi/pdf/10.1145/958942.958945) | Formal freshness/age metrics; empirical validation on **270 websites tracked over 4 months**; weighted (importance-based) freshness defined in §6.1. | Uniform policy: freshness **0.57**, age **5.6 days**. Optimal: **0.62 / 4.3 days**. **Proportional: 0.12 / 400 days — the worst.** Fixed-order checking beats random order (0.63 vs ~0.48 at r=1). | Strong; still the standard reference | Textbook-level | Do **not** poll volatile boards proportionally more. Use importance-weighted, near-uniform, fixed-order scheduling. |
| E02 | `[GOV]` Eurostat / Cedefop Web Intelligence Hub — OJA data methodology. [link](https://cros.ec.europa.eu/wih/oja) | Official production pipeline for EU-wide online job advertisement statistics: landscaping → ingestion (scraping / crawling / API) → pre-processing → information extraction. | **Three-stage dedup is mandatory:** physical (same URL/ID), semantic (fuzzy match on description + location; portal metadata/reference IDs to kill aggregator copies), logical (match on structured fields after extraction, then **merge**). Duplicates are flagged and merged, not deleted. | Strong as a documented production standard; no published precision/recall | Used by Eurostat and Cedefop (Skills-OVATE), 28 countries | Copy the three-stage design. Store a **merge graph** with per-source first-seen/last-seen rather than one "best" record. |
| E03 | `[PEER]` Zhao, Chen & Mason (2021). *A Framework for Duplicate Detection from Online Job Postings*, WI-IAT '21. [link](https://dl.acm.org/doi/pdf/10.1145/3486622.3493928) | ~**9.3m** Australian job postings (Mar 2015–May 2019); expert-labelled gold set of **1,498 pairs** (38% duplicates); 24 method combinations. | Best method (Overlap + skip-gram) **F1 0.9686, AUC 0.9952**, beating the Apollo baseline. Cites Textkernel's estimate that duplicates are **50–80%** of postings crawled from boards. | Strong on the gold set; same-title/location blocking limits generality | Beats a published baseline | Cheap n-gram overlap reaches ~0.97 F1. Spend no model budget on dedup; spend it on liveness. |
| E04 | `[DOCS]` Greenhouse Job Board API. [link](https://docs.greenhouse.io/job-board.html) | Public JSON endpoint per employer board token; reads need no auth. | Exposes `id`, `internal_job_id`, `requisition_id`, `title`, `updated_at`, `first_published`, `application_deadline`, `absolute_url`, plus **`include_ai_disclaimer`, `ai_disclaimer`, `ai_opt_out_request_url`**. Application POST requires Basic Auth with a board key. | n/a | n/a | One feed gives created + updated + requisition identity **and the employer's own AI-screening disclosure**. Make ATS feeds the trusted core. |
| E05 | `[DOCS]` Lever Postings API. [link](https://github.com/lever/postings-api) | Public JSON per site name (global + EU instances). | Documented fields: `id`, `text`, `categories`, `country`, description fields, `hostedUrl`, `applyUrl`, `workplaceType`, `salaryRange`. **No created/updated timestamp is documented.** Application POSTs are rate-limited (429). Lever states published postings "may be scraped by third parties". | n/a | n/a | Lever gives identity but not age. For Lever boards, derive first-seen/last-seen yourself and label freshness as **observed by Signal**, not published. |
| E06 | `[DOCS/GOV]` USAJOBS Search API. [link](https://developer.usajobs.gov/api-reference/get-api-search) | Keyed public API over currently open US federal announcements. | Response exposes `MatchedObjectId` (control number), `PositionID`, **`PositionStartDate`, `PositionEndDate`, `PublicationStartDate`, `ApplicationCloseDate`**. | n/a | n/a | The only source here that publishes an explicit close date — use it as the **test fixture** for Signal's liveness logic. |
| E07 | `[DOCS]` Internshala `robots.txt` (retrieved 2026-10-12). [link](https://internshala.com/robots.txt) | Site access policy. | For `User-Agent: *` — **Disallow** `/internship/details/`, `/job/details/`, `/internship/search/`, `/job/search/`, `/external-jobs/*`, `/student*`, `/api/`. A named block (GPTBot, ClaudeBot, Anthropic-AI, PerplexityBot, Google-Extended, Amazonbot…) is disallowed site-wide except `/about_us`, `/blog/`, `/competitions/`. | n/a | n/a | **Crawling Internshala listings is out of bounds.** Internshala coverage requires a partnership/API, or the source gets dropped from the pilot. |
| E08 | `[DOCS]` Unstop `robots.txt` (retrieved 2026-10-12). [link](https://unstop.com/robots.txt) | Site access policy. | For `User-Agent: *` — **Allow** `/internship/`, `/job/`, `/competitions/`, `/api/public/*`; **Disallow** `/api/*`, `/u/*`, `/p/*`, `/pf/*`, `/directory/user/*`. Most AI crawlers explicitly allowed; CCBot/Bytespider/Diffbot blocked; Bingbot crawl-delay 1. | n/a | n/a | Unstop listing paths are crawlable under robots.txt (ToS still needs counsel). Make Unstop the **India anchor source** for the pilot. |
| E09 | `[UNVERIFIED — blocked]` LinkedIn `robots.txt`. [link](https://www.linkedin.com/robots.txt) | Fetch attempted from this sandbox 2026-10-12. | **HTTP 403** — the access-policy file itself could not be retrieved programmatically. | n/a | n/a | If you cannot even read the robots file, you do not have permission to automate the site. LinkedIn = human-only deep links. |

### F — Legal and regulatory

| # | Citation + link | Method & sample | Headline | Strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| F01 | `[GOV/PRIMARY]` *Van Buren v. United States*, 593 U.S. 374 (2021), No. 19-783, decided 3 Jun 2021. [link](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf) | US Supreme Court statutory interpretation of CFAA §1030(a)(2), (e)(6). | "Exceeds authorized access" covers obtaining information from areas of a computer that are off-limits; liability turns on a **gates-up-or-down** inquiry, not on purpose or policy violation. | Binding precedent | n/a | Breaking a usage policy is not automatically a federal crime — but that is a criminal-law point only, not permission. |
| F02 | `[SECONDARY — primary opinions not opened]` *hiQ Labs v. LinkedIn*, 31 F.4th 1180 (9th Cir. 18 Apr 2022); N.D. Cal. SJ 4 Nov 2022; consent judgment 8 Dec 2022. [Privacy World](https://www.privacyworld.blog/2022/04/hiq-labs-v-linkedin/) · [Polsinelli](https://www.polsinelli.com/publications/data-scraping-update-linkedin-v-hiq-answers-some-questions-but-leaves-many-more-open) | Law-firm analyses of the appellate and district rulings. | Scraping **public** profiles likely is not CFAA "without authorization". **But** the district court held hiQ **breached LinkedIn's User Agreement**, and the Dec 2022 consent judgment entered **$500,000** against hiQ with a permanent injunction and data deletion (per secondary sources). | Strong on CFAA; the contract outcome is the operative risk | Reinforced by F03 | "Not a CFAA crime" ≠ "allowed". The party that won the CFAA point still paid and wound down. **Do not scrape LinkedIn.** |
| F03 | `[SECONDARY — opinion not opened]` *Meta Platforms v. Bright Data*, No. 3:23-cv-00077-EMC (N.D. Cal. 23 Jan 2024). [FBM analysis](https://www.fbm.com/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/) | Summary judgment on breach of contract. | Terms govern "your use" as a **logged-in user**; logged-off scraping of public pages by a non-user did not breach the contract; only tortious interference survived. | District court; persuasive, not binding | Consistent with F02's logic | Logged-out collection of public pages is the defensible posture: never log in, never create accounts, never bypass CAPTCHAs or rate limits. |
| F04 | `[GOV/PRIMARY]` O. Reg. 476/24, *Rules and Exemptions re Job Postings*, under the Employment Standards Act, 2000 — consolidation period from **1 Jan 2026** (e-Laws currency 7 Oct 2026). [link](https://www.ontario.ca/laws/regulation/240476) | Full regulation text read. | In force **1 Jan 2026**. Part III.1 **does not apply** to employers with **<25 employees** on the posting date. Defines "artificial intelligence" broadly (a machine-based system that infers from inputs to generate predictions, content, recommendations or decisions) and "publicly advertised job posting" (with four carve-outs). Compensation disclosure exempt above **$200,000**; posted ranges capped at **$50,000**; interviewed applicants must be told within **45 days** whether a hiring decision was made. | Primary law | n/a | A regulator now requires employers to state whether a posting is for an **existing vacancy** and whether **AI screens** applicants. Surface the employer's own statement; do not invent a ghost score. **Note:** those two duties sit in ESA ss. 8.1–8.6, which e-Laws did not render for us — **lawyer to verify the statutory text**. |
| F05 | `[GOV/PRIMARY]` Digital Personal Data Protection Rules, 2025, G.S.R. 846(E), Gazette of India, 13–14 Nov 2025 (MeitY). [link](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) | Official gazette text (bilingual) read for commencement and notice rules. | Rule 1: rules **1, 2 and 17–21** in force on publication; **rule 4** (consent managers) **one year** after publication; **rules 3, 5–16, 22, 23** **eighteen months** after publication (≈13 May 2027). Rule 3 requires notice that is independently understandable, with an **itemised description of the personal data** and the specific purposes, plus a link to withdraw consent as easily as it was given. | Primary law | n/a | Signal's Indian student profiles have a hard deadline: itemised notice, easy withdrawal, no bundled consent, by mid-2027. Build it now, not in 2027. |

### G/H — Context and method

| # | Citation + link | Method & sample | Headline | Strength | Replicated? | Product consequence |
|---|---|---|---|---|---|---|
| G01 | `[INDUSTRY SURVEY]` NACE (2025). *2025 Internship & Co-op Report.* [article](https://www.naceweb.org/talent-acquisition/internships/intern-offer-and-conversion-rates-fall-acceptances-rise) · [exec summary PDF](https://www.naceweb.org/docs/default-source/default-document-library/2025/publication/executive-summary/2025-nace-internship-and-coop-report-executive-summary.pdf?sfvrsn=4e8d957c_3) | **247 organisations** (208 NACE members = 24.8% of eligible), fielded 16 Oct 2024 – 2 Jan 2025; employer-reported. | Full-time offer rate to the 2024 intern class **62%** (five-year low); overall conversion just under **51%**; in-person **71.9% offer / 58.5% conversion** vs hybrid **56.2% / 46.0%**. | Moderate: self-selected employer members | Annual series | Internships are the highest-yield funnel for students; weight internship/co-op listings above generic entry-level postings. **US only.** |
| G02 | `[GOV]` PIB, Government of India (17 Mar 2025). *PM Internship Scheme, Round 2 of pilot phase.* [link](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2111914) | Official description of the PMIS pilot. | Round 1 drew **>600,000 applications**; Round 2 offered **100,000+ internships across 730+ districts**; each applicant may apply to **up to 3** internships; stipend ₹5,000/month for 12 months plus a ₹6,000 grant; target one crore internships over five years. | Primary for scheme design; no outcome data | n/a | A first-party, high-trust India source with explicit application caps — integrate before touching any private Indian board. |
| H01 | `[PEER]` Murphy, Allen, Stevens & Weatherhead (2005). *A Meta-analysis of Hypothetical Bias in Stated Preference Valuation*, Env. & Resource Economics 30(3): 313–325. [link](https://ideas.repec.org/a/kap/enreec/v30y2005i3p313-325.html) | Meta-analysis of 28 stated-preference studies using the same elicitation mechanism for hypothetical and real values; **83 observations**. | Median ratio of hypothetical to actual WTP **1.35**, with severe positive skew; choice-based elicitation reduces bias; student subjects may themselves be a source of bias. | Strong for the method question | Meta-analytic | Discount any survey-based pricing answer from students, then confirm with a real-money paywall (see Experiment 3). |

---

## 2. Refutation log

For each anchor claim: the strongest evidence **against** it, what survives, and — where nothing contradicts it — the exact queries run so the gap is auditable.

### Anchor A — "~21% of postings are ghost jobs (Ng 2024); 55% / 1.63× (SSRN 5987416)"

**Strongest refutations**
1. **Unit error (fatal to the headline).** Ng's classifier runs on Glassdoor *interview reviews*, not postings (A01). A job seeker who was interviewed and wrote a review is not a random posting.
2. **Method sensitivity of 13×.** On the same corpus, a keyword approach yields **1.3–1.6%** vs the model's 21% (A01). A result that moves by an order of magnitude with method choice cannot carry a product claim.
3. **The official position is "unknown".** CRS, April 2025: there are **no official statistics**; the vendor surveys have opaque methodology and the vendors sell verification tools (A02).
4. **A duration-based counter-measurement.** LinkUp, from career-site census data: average closed duration **45.6 days**, **58%** of removed jobs had been up <30 days and only **7%** >6 months (A07). Most long-lived postings are slow hiring, not fake hiring.
5. **The second source is too weak to cite.** SSRN 5987416 computes 55% over **160 of 414** postings, 89.6% US, 56.8% software engineering, zero references (A03).
6. **Vendor numbers disagree with each other** in ways that reveal the construct is not fixed: 18–22% of *postings per quarter* (A04) vs 40% of *companies in a year* (A05) vs 68% of *managers with a posting >30 days* (A06). These are three different quantities presented as one phenomenon.

**What survives:** stale and never-filled postings are real, common enough that students encounter them, and the cost of verification is low. The **confidential-employer** correlate (1.63×, A03) is a cheap feature hypothesis. The Ontario "existing vacancy" disclosure (F04) gives a legally-mandated, employer-authored signal in at least one jurisdiction.

### Anchor B — "Search intensity declines within a spell (Faberman & Kudlyak 2019)"

**Strongest refutations**
1. **Cederlöf & Roman (2025)**, 2.4m Swedish activity reports: within-spell effort is **flat**; raw increases are dynamic selection; **86–90%** of the callback decline is composition, not behaviour (B03).
2. **Faberman & Kudlyak's own second finding inverts the product reading:** longer-duration seekers search **more** intensely throughout (B01). "Long-unemployed = disengaged" is the opposite of what the paper says.
3. **Lalive et al. (2025)** show the decline in applications is modest (**11 → just under 10 per month over 12–15 months**) while *offers per interview rise* with duration (B02). The binding constraint is employer response, not student effort.

**What survives:** effort is not constant over a spell, and the first weeks are the highest-intensity period (2.3 → 1.2 applications/week in the first month, B01). Onboarding and the first fortnight carry disproportionate product weight.

### Anchor C — "Breadth wins: +44% interviews; internships +14% callbacks"

**Strongest refutations**
1. **Significance and power.** The +44% is significant **at the 10% level only**, on ~300 participants; the authors themselves compute that detecting the implied job-finding effect needs **3,794 per arm** (C01). The interview effect is real; the employment effect is undemonstrated in that study.
2. **Heterogeneity reverses for some users.** Initially broad searchers became *narrower* under treatment, with no interview gain (C01).
3. **Digital-only delivery has failed at scale.** Bob Emploi: **212,277** participants, **precise nulls** on every employment outcome (B06). Swedish algorithmic recommendations: +10–16% clicks on recommended vacancies, **no** effect on job finding or earnings (B08).
4. **Congestion.** Crépon et al.: treated +2.5pp, untreated peers in the same labour market **−2.1pp**, net ≈ 0 (C04). Breadth help can redistribute rather than create.
5. **The naturally-occurring counterfactual.** The treatment effect on breadth equals roughly what happens anyway after ~3 months of searching (C01) — so part of the value is acceleration, not addition.

**What survives:** the mechanism is still the best-supported *positive* lever in this review, and the same team's pre-registered UK scale-up reports **+20–40%** on stable-job and earnings outcomes at 9 months (C02). Nunley's **+14%** internship callback effect (C03) is a clean résumé-audit result and is directly actionable for students.

### Anchor D — "Agents reach ~55–60% success on real web tasks"

**Strongest refutations**
1. **The Mind2Web citation does not support the claim.** It is an offline dataset on static snapshots; GPT-4 task success is **2.0%** (D02).
2. **Live-web evaluation collapses the number.** Online-Mind2Web, 300 tasks / 136 live sites, human-graded: most frontier agents **~30%** (D03).
3. **Benchmark inflation is demonstrated, not alleged.** A naive Google-search-and-click agent scores **51% on WebVoyager** and **22%** on the live set (D03).
4. **Success is measured without safety.** CuP is **under two-thirds** of nominal completion across three SOTA agents (D04).
5. **Adversarial input is the normal case for Signal.** AgentDojo: GPT-4o targeted attack success **47.7%** with a generic injection; defences cost **15–20%** utility (D05).

**What survives:** WebVoyager's **59.1%** on 15 known sites (D01) is a fair estimate for a *small, curated, instrumented* site list — which is exactly Signal's intended posture ("prefer a smaller trusted list over a bigger unchecked one"). Tool filtering drops attack success to ~7.5% (D05), so a read-only verification tool is both safer and cheaper.

### Anchor E — "Freshness is budgeted scheduling; official pipelines dedup across portals"

**Strongest refutation**
1. **The intuitive policy is the worst one.** Cho & Garcia-Molina's own measurements: proportional refresh gives freshness **0.12** and age **400 days** vs uniform **0.57 / 5.6 days** and optimal **0.62 / 4.3 days** (E01). A naive "crawl volatile sources more often" scheduler would be worse than crawling everything at the same rate.
2. **Dedup is not a solved sub-problem in the wild.** Textkernel's estimate that **50–80%** of board-crawled postings are duplicates (cited in E03) means identity resolution dominates cost before freshness even starts.

**What survives:** everything else. Importance-weighted freshness (§6.1 of E01), fixed-order checking, and Eurostat/Cedefop's three-stage dedup with merge (E02) are directly implementable, and n-gram overlap reaches **F1 0.9686** on an expert-labelled job-posting gold set (E03).

### Where refutation searches came up empty

Nothing contradicting these was found; queries are listed so the gap is auditable (all run 2026-10-12, see §10 for the full trail):
- **Evidence that automated "verify live at source" improves student outcomes.** Queries: `job alert freshness verification experiment outcomes`, `"verified live" job listing experiment application outcomes`, `willingness to pay job search tool students subscription experiment price premium alerts evidence`. → **NO EVIDENCE FOUND.**
- **Evidence that students' trust in a job-alert product depends on disclosure of automated submission.** Closest available evidence is the general AI-disclosure penalty (D07) and candidate attitudes (A04: 15% oppose any AI in hiring). → **NO DIRECT EVIDENCE FOUND.**

---

## 3. Mechanism map

Both sides of the market, with the evidence tag for each arrow. `→` = causal/empirical support, `⇢` = modelled or inferred.

### 3.1 Applicant side

```
                     ┌────────────────────────────────────────────┐
                     │  Student attention is the scarce resource  │
                     └────────────────────────────────────────────┘
                                        │
   listing age shown ──(A10: removing age → −3% clicks, −1.8% applications)──┐
   applicant count shown ─(A10: +3.8% to low-competition; A11: +3.5% finish)─┤
                                                                             ▼
                              ┌───────────────────────────────────────────────────┐
     phantom/stale listings ──┤  Directed search toward *young* listings           │
     (A09: ~70% of apps to    │  (A09 calibration; A10 experimental confirmation)  │
      listings <48h old)      └───────────────────────────────────────────────────┘
                                        │                         │
                 wasted application      │                         │  crowding on fresh listings
                 (no reply possible)     ▼                         ▼  (queue falls >5× day1→day2, A09)
                              ┌─────────────────────┐    ┌──────────────────────────────┐
                              │ Falling callbacks    │    │ Congestion externality       │
                              │ (B02: interviews/app │    │ (C04: −2.1pp for untreated   │
                              │  fall with duration) │    │  peers in treated markets)   │
                              └─────────────────────┘    └──────────────────────────────┘
                                        │
                                        ▼
                     ┌────────────────────────────────────────────┐
                     │ Discouragement → fewer applications         │
                     │ (B02: 11 → <10/month; B01: 2.3 → 1.2/week   │
                     │  in month 1) …BUT B03 finds within-spell    │
                     │  effort flat — setting-dependent            │
                     └────────────────────────────────────────────┘
                                        │
                 ┌──────────────────────┴───────────────────────┐
                 ▼                                              ▼
   ┌──────────────────────────────┐              ┌────────────────────────────────────┐
   │ Narrow search persists        │              │ Expectation inflation              │
   │ (C01: breadth advice lifts    │              │ (B07 India: portal access → −9.2pp │
   │  interviews +44% p<0.10 for   │              │  employment, reservation wage +2.2%│
   │  narrow searchers)            │              │  — alerts raised expectations)     │
   └──────────────────────────────┘              └────────────────────────────────────┘
```

**Spillover / signalling loop (applicant side):**
internship experience → **+14% interview rate** (C03) → more callbacks → sustained effort (B02 logic) → more internships. Signal can only enter this loop at the *application targeting* step; it cannot manufacture the signal itself.

### 3.2 Employer side

```
 Marginal cost of one more posting ≈ 0 ──────────────────────────────────┐
 (A08 quotes Ng on this as the driver)                                   │
                                                                         ▼
 ┌────────────────────────────────────────────────────────────────────────────────┐
 │ Employer incentives to leave a requisition open                                 │
 │  • "always open to new people" — 50% of managers (A06, self-reported)            │
 │  • pipeline/résumé banking — 59% cite collecting résumés for later (A05)         │
 │  • appear open to talent 67% / appear to be growing 66% (A05, self-reported)     │
 │  • slow genuine hiring: average time-to-fill ≈ 46 days (A07, observed)           │
 │  • syndication: boards keep copies after the employer removes the original (A07) │
 │  • ATS auto-refresh/reposting behaviour (⇢ inferred; see §11 NO EVIDENCE FOUND)  │
 └────────────────────────────────────────────────────────────────────────────────┘
          │                                   │                              │
          ▼                                   ▼                              ▼
  Phantom stock grows            Application volume per req rises     Recruiter workload rises
  (A09: ~28% of unemployment     (A04: recruiter workload +26% in     → more candidate ghosting
   attributable in calibration)   one quarter, vendor-reported)        (A04: 61% ghosted post-interview)
          │                                                                   │
          └──────────────────────────┬────────────────────────────────────────┘
                                     ▼
             ┌─────────────────────────────────────────────────────────┐
             │ Regulatory response (the new variable)                   │
             │  • Ontario, in force 1 Jan 2026: must state whether the  │
             │    posting is for an existing vacancy and whether AI     │
             │    screens applicants (F04; statute text lawyer-verify)  │
             │  • FTC §5 deception theory (A02, A08)                    │
             │  • Greenhouse already emits ai_disclaimer fields (E04)   │
             └─────────────────────────────────────────────────────────┘
```

**The two sides meet at identity.** A single requisition appears as: ATS record (`requisition_id`, E04) → employer career page → aggregator copies (50–80% duplicate rate, E03) → social posts. Freshness claims are only meaningful **per node**, which is why Eurostat/Cedefop merge rather than collapse (E02) and why Signal must store a merge graph with per-source first-seen / last-seen.

**Where Signal can actually intervene (ranked by mechanism strength):**
1. Kill the *wasted application* arrow — verification at source, cheap, measurable in-product.
2. Dampen the *expectation inflation* arrow — base rates shipped with alerts (B07 is the warning).
3. Nudge the *narrow search* arrow — occupation/role adjacency suggestions (C01/C02).
4. Do **not** push the *crowding* arrow — more speed into fresh listings is zero-sum (C04, A09).

---

## 4. Idea backlog (26 buildable ideas)

Effort: **S** ≤ 1 week of one engineer · **M** 2–4 weeks · **L** > 1 month or needs a partnership.
⚠️ = platform-blockable or ToS-risky. Ranked within each block by evidence strength × decision value.

### Block 1 — Liveness and identity (the core promise)

| # | Name | Anchor / mechanism | Trigger + data required | Effort | Impact pathway | Failure mode + guardrail | Cheap falsification test |
|---|---|---|---|---|---|---|---|
| 1 | **ATS-first trusted source list** | E04, E05, A07 — career-site data is the clean layer | Curated list of ~300 employers hiring interns in US+India; Greenhouse/Lever board tokens; nightly pull | M | Removes syndication noise at the root; every record has a first-party origin | Coverage looks thin next to aggregators → guardrail: publish the source list in-product and state coverage honestly | Pull 300 boards for 2 weeks; measure what share of student-saved listings they cover. <40% ⇒ the thesis fails |
| 2 | **Last-verified stamp + named source on every card** | A02 (only defensible claim is per-listing), A10 (age is used) | Verification event log: `source`, `checked_at`, `http_status`, `evidence` | S | Turns a vague "live" badge into an auditable claim; the only legally safe phrasing | Users read "verified" as "you will get a reply" → guardrail: wording is "seen live at 09:14 IST on employer's Greenhouse board" | Show 50 students two cards (badge vs timestamp+source); ask what it guarantees. If >30% say "they will reply", rewrite |
| 3 | **Verify-on-open** | E01 (freshness is budgeted), A09 (phantoms) | On click, synchronous re-check of the source URL before the student reads the posting | S | Catches the posting that died between crawl and click — the moment of maximum user pain | Latency; source rate limits → guardrail: 1.5s timeout, cached fallback, per-domain concurrency cap | Log pre-click vs post-click status for 2 weeks. If <2% flip, this is theatre — drop it |
| 4 | **Importance-weighted, fixed-order refresh scheduler** | E01 (proportional = worst: 0.12 vs 0.62) | Per-listing weight (student saves × recency × source reliability); fixed traversal order | M | Maximises weighted freshness per request budget; the single highest-leverage infra decision | Engineers "optimise" it into proportional polling → guardrail: policy chosen in config, regression test asserts non-proportional | Simulate a week of history under proportional vs weighted-uniform; compare weighted freshness. Replicates E01's ordering or the model is wrong |
| 5 | **Merge graph with per-source first-seen/last-seen** | E02 (physical→semantic→logical dedup, then *merge*) | Canonical posting node + edges to every source copy with its own timestamps | M | Lets Signal say "live on the career site, gone from the board" — the distinction that matters | Over-merging hides a real second opening → guardrail: never merge across different `requisition_id` | Hand-label 200 clusters; measure merge precision. <0.95 precision ⇒ loosen the rule |
| 6 | **Cheap dedup (n-gram overlap + title/location blocking)** | E03 (F1 0.9686, no LLM needed) | Title + location blocking, skip-gram overlap, threshold tuned on a local gold set | S | Removes the 50–80% duplicate load before any expensive step | Indian postings have noisier titles/locations → guardrail: build a 500-pair India gold set before shipping | Label 500 India pairs; if F1 <0.90, add a location-normalisation step before spending on models |
| 7 | **Dead-application counter ("we saved you N")** | A02, A07 — measurement beats prevalence claims | Verification log + student's application log | S | Converts the product's core value into a number the student can see and the team can optimise | Encourages inflating the counter → guardrail: counter only increments on a *confirmed* 404/closed state with evidence stored | If the median student's counter is <1/week after a month, the pain is too rare to monetise |
| 8 | **Confidential-employer flag** | A03 (77.5% vs 47.5%, 1.63×, p<0.05, weak sample) | Employer-name field present/absent at parse time | S | One-line heuristic for the strongest single correlate reported anywhere | Treated as a fraud label → guardrail: phrase as "employer not named", never "likely fake" | Track outcomes on 500 flagged vs unflagged applications; if reply rates do not differ, remove the flag |
| 9 | **Surface the employer's own vacancy / AI disclosure** | F04 (Ontario, in force 1 Jan 2026), E04 (`ai_disclaimer`, `ai_opt_out_request_url`) | Greenhouse board fields; regex for statutory phrasings on career pages | M | Shows a *first-party* statement instead of Signal's guess — legally safe and genuinely informative | Absence read as a negative signal → guardrail: show "not stated" neutrally; never infer | Count how many of 300 boards expose a disclosure field. If <5% in India, scope the feature to North America |
| 10 | **Closing-date capture** | E06 (`ApplicationCloseDate`), E04 (`application_deadline`) | Feed fields where present; explicit "no deadline published" otherwise | S | Deadlines beat freshness heuristics whenever they exist | Inventing deadlines from posting age → guardrail: only published dates are rendered | Measure field availability across sources; if <10% publish one, deprioritise the UI |
| 11 | **Requisition identity / repost badge** | E04 (`requisition_id`, `internal_job_id`), A05 (reposting behaviour) | Store req IDs over time; detect new posting with a seen req ID | M | "Third posting of this requisition since June" is a far stronger staleness signal than age | Normal multi-location reqs look like reposts → guardrail: only flag same req + same location | Over 8 weeks, check whether repost-flagged listings have lower reply rates in Signal's own funnel |
| 12 | **Per-source health dashboard + SLA kill switch** | A07 (board pollution), E01 | Per-source dead-on-open rate, dedup rate, parse failure rate | S | Operationalises "prefer a smaller trusted list over a bigger unchecked one" | Sunk-cost attachment to bad sources → guardrail: automatic demotion at >15% dead-on-open for 2 weeks | Run for a month; if no source ever crosses the threshold, the thresholds are wrong |

### Block 2 — Attention, expectations and search behaviour

| # | Name | Anchor / mechanism | Trigger + data required | Effort | Impact pathway | Failure mode + guardrail | Cheap falsification test |
|---|---|---|---|---|---|---|---|
| 13 | **Alert budget with delivery windows** | B09 (28% less frustration, 13% faster at breakpoints), B10 (~5–7% engagement) | User-set daily cap, quiet hours, digest vs instant toggle | S | Protects the scarce resource (attention) and reduces churn, the main failure mode of alert products | Caps hide the one job that mattered → guardrail: "urgent" class (deadline <48h) bypasses the cap, max 1/day | A/B digest vs instant (Experiment 2). If mute rates are equal, cadence is not the lever |
| 14 | **Base-rate card inside every alert** | B07 (India: expectation inflation → −9.2pp employment) | Signal's own funnel stats by role family and region | M | Directly counteracts the only documented *harm* from a job portal in India | Discouraging students into inaction → guardrail: pair the base rate with the next concrete action | Randomise base-rate card on/off; measure applications and 4-week retention. Harm ⇒ revert immediately |
| 15 | **Week-1 intensity onboarding** | B01 (2.3 → 1.2 applications/week within month 1) | Signup cohort date; application events | S | Front-loads help when effort is naturally highest, instead of fighting decay later | Pressure-selling to anxious students → guardrail: no streaks, no loss-framing, no daily goals | Compare week-1 vs week-4 application rates in Signal's own cohort. If flat (B03 pattern), skip anti-decay work entirely |
| 16 | **Callback/outcome tracker** | B02 (offers-per-interview *rise*; response is the binding constraint) | Student-logged outcomes + email-forward parsing (opt-in) | M | Gives a student evidence of response, which is what actually decays | Becomes a chore → guardrail: one-tap logging from the alert thread; never required | If <20% of students log any outcome in 3 weeks, the data layer is not viable; fall back to a monthly survey |
| 17 | **Breadth index on saved filters** | C01 (effect concentrated in narrow searchers) | Saved-filter occupation/role codes; simple dispersion measure | S | Identifies the exact subgroup for whom breadth advice worked | A crude taxonomy mislabels students → guardrail: show the index and let the student correct it | Check whether the index predicts reply rates in Signal's funnel; no gradient ⇒ the taxonomy is noise |
| 18 | **Adjacent-role suggestions, narrow searchers only** | C01 (+44%, p<0.10), C02 (+20–40% in scale-up) | Role adjacency from observed co-application patterns (not a licensed taxonomy at pilot scale) | M | The strongest positive mechanism in the review, targeted at the subgroup it worked for | Broad searchers get *narrower* when nudged (C01) → guardrail: suppress for students already above the breadth median | Offer suggestions to half the narrow-searcher segment; measure accepted suggestions and 30-day interviews |
| 19 | **Internship-experience profile prompt** | C03 (+14% interview rate from internship experience) | Profile completeness state | S | Pushes the single strongest controllable callback signal for students | Turns into résumé-writing scope creep → guardrail: prompt only; no generated content | Measure callback rate for students with vs without an internship listed (observational, caveated) in Signal's funnel |
| 20 | **Deadline-first ordering (not freshness-first)** | A09/A10 (everyone already races to fresh), C04 (crowding is zero-sum) | Published deadlines (idea 10) + verification recency | S | Differentiates on *actionability* rather than adding to the day-1 stampede | Few sources publish deadlines → guardrail: fall back to verified-recency ordering | If deadline coverage <10% (test in idea 10), this ranks below freshness and should wait |

### Block 3 — Extraction, agents and consent

| # | Name | Anchor / mechanism | Trigger + data required | Effort | Impact pathway | Failure mode + guardrail | Cheap falsification test |
|---|---|---|---|---|---|---|---|
| 21 | **Deterministic-first extraction ladder** | E04 (structured ATS JSON), C05 (LLM span-F1 ≈ 65) | Order: ATS JSON → schema.org `JobPosting` JSON-LD → DOM rules → LLM last | M | Most fields never need a model; accuracy and cost both improve | "LLM for everything" default → guardrail: log which rung produced each field; alert if LLM share rises | Measure field-level accuracy by rung on 200 postings. If the LLM rung is not clearly worse, the ladder is unnecessary |
| 22 | **Evidence snippet for every extracted field** | C06 (errors cluster in bullet lists; 8% of gold labels themselves wrong) | Character offsets stored with each extraction | S | Makes extraction errors visible and correctable instead of authoritative | Clutter → guardrail: snippet on hover/expand only | Ask 10 students to spot errors with and without snippets; if detection does not improve, drop it |
| 23 | **Read-only verification tool with tool isolation** | D05 (tool filter cuts ASR 47.7% → ~7.5%), D04 (CuP < ⅔) | Separate service: fetch + parse only; no form, auth, or write capability | M | Removes the entire prompt-injection → unwanted-action path by construction | Pressure to "just let it click apply" → guardrail: write capability does not exist in that binary | Red-team 50 postings with injected instructions; any state-changing action ⇒ architecture failure |
| 24 | **Assist-and-review prefill (never auto-submit)** | D04 (consent dimension), D07 (social penalty for AI use, N=4,439) | Field mapping + a review screen with per-field provenance; explicit per-application consent | L | Captures the time saving without the reputational and policy risk of automation | Silent defaults creeping toward auto-submit → guardrail: consent is per application, expires in 24h, and is logged | Experiment 1 variant: measure completion time and whether students edit prefilled fields. No edits ⇒ they are not reviewing; stop the feature |
| 25 | **Calibrated low-confidence queue** | D06 (verbalized confidence overconfident; ECE > 0.377) | Outcome-calibrated reliability score (not model self-report); human review queue | M | Keeps the "live" label trustworthy at the margin, where it is most likely wrong | Using model confidence as the score → guardrail: score must be fit on observed verification outcomes | Compare model self-confidence vs fitted score against ground truth on 300 checks; keep whichever calibrates |
| 26 | **India source pack: Unstop + PMIS + employer career pages** ⚠️ | E07 (Internshala disallows listing paths), E08 (Unstop allows), G02 (PMIS) | Unstop `/internship/`, `/job/` paths under robots; PMIS portal; curated India employer boards | M | Gives genuine India coverage without touching a source that forbids it | Someone adds Internshala "just for the pilot" → guardrail: an allowlist in code, with the robots snapshot stored next to it | Measure India coverage of student-saved listings from this pack alone; <30% ⇒ go partnership-first |

**Platform-blockable / ToS-risky flags.** ⚠️ Idea 26 only, and only for the Internshala exclusion it encodes. Note for the whole backlog: **no idea in this list fetches LinkedIn.** LinkedIn appears in the brief as a monitored source, but its `robots.txt` returned **HTTP 403** to this sandbox (E09) and the hiQ litigation ended with a $500,000 judgment and a permanent injunction against the scraper on contract grounds (F02). The only LinkedIn-compatible pattern is a **human-initiated deep link out** plus optional user-pasted URLs.

---

## 5. Do-not-build list

| # | Do not build | Why (evidence) | What to do instead |
|---|---|---|---|
| 1 | **Automated LinkedIn monitoring, scraping, or logged-in access** | `robots.txt` not even retrievable (403, E09); hiQ won on CFAA but lost on contract — $500k consent judgment, permanent injunction, company wound down (F02); Meta v. Bright Data turned on logged-out status and exact ToS wording (F03) | Deep-link out to LinkedIn; let the student paste a URL for a one-off check they initiated |
| 2 | **Crawling Internshala listing/search/detail pages** | Internshala's own `robots.txt` disallows `/internship/details/`, `/job/details/`, `/internship/search/`, `/job/search/`, `/external-jobs/*` for all agents, and blocks named AI crawlers site-wide (E07) | Pursue an API/partnership; until then show Internshala as "not covered" rather than covering it badly |
| 3 | **A "ghost job probability" score on individual listings** | No defensible base rate exists (A02); estimates swing 1.3%→21% by method on identical data (A01); vendor figures measure different quantities (A04/A05/A06); a wrong accusation is a defamation and FTC-style deception risk running the *other* way (A08) | Report observable facts only: last verified, requisition reposts, whether the employer named itself, and the employer's own vacancy statement (F04) |
| 4 | **Auto-submitting applications (even with blanket consent)** | ~⅓ of nominally successful agent runs violate a stated policy (CuP < ⅔, D04); live-web success ≈30% (D03); prompt injection from posting text reaches 47.7% targeted ASR against a strong model (D05); AI-assisted candidates are judged less competent and it changes hiring decisions (D07, N=4,439) | Assist-and-review prefill with per-application consent (idea 24) |
| 5 | **Mass-apply / "apply to 100 jobs" volume features** | Volume is zero-sum under congestion (C04: untreated peers −2.1pp, −7.7pp in tight markets); recommenders raise clicks 10–16% with no effect on job finding (B08); Bob Emploi's precise nulls at n=212,277 (B06) | Optimise avoided waste and match quality; cap applications per day by default |
| 6 | **Proportional "crawl the volatile sources more often" scheduling** | It is the worst policy in the foundational measurement: freshness 0.12 and age 400 days vs 0.62/4.3 optimal (E01) | Importance-weighted, near-uniform, fixed-order scheduling (idea 4) |
| 7 | **LLM-generated cover letters / answers at volume** | AI use carries a measured social-evaluation penalty in hiring tasks (D07); employers report AI-driven application floods and rising deception suspicion (A04) — volume generation puts the student on the wrong side of that filter | Snippet library from the student's own past answers, with an explicit "written by you" default |
| 8 | **Market-wide freshness claims ("we track 10M live jobs")** | No official prevalence statistics exist (A02); dead-listing rates are source-specific and unmeasured at that scale; FTC §5 deception theory is being argued for exactly this kind of claim (A08) | Publish the source list, the per-source dead-on-open rate, and the check interval (idea 12) |

---

## 6. Three experiment designs runnable with ~200 student users

Shared rules: block-randomise on **market (India / US)** and **year of study**; pre-register hypothesis, primary metric, exclusions and stop rule in `tasks/` before launch (commit hash = the pre-registration timestamp); analyse intention-to-treat; report effect sizes with 95% CIs, never bare p-values. Power calculations below use α = 0.05 two-sided, 80% power (z = 1.96 + 0.84 = 2.80).

### Experiment 1 — Does a verified-live label change what students apply to?

| | |
|---|---|
| **Hypothesis** | Showing "seen live at *HH:MM* on *source*" (vs showing posting age only) reduces the share of applications sent to listings that are already dead, without reducing total applications. |
| **Why this and not a badge test** | A10 shows posting-age information is already used and that removing it cuts applications 1.8%; the open question is whether *verification* adds anything beyond *age*. A02 says no market-wide prevalence claim is available, so Signal must measure its own. |
| **Unit of randomisation** | **Listing impression, randomised within student** (crossover). Students are the clusters; each student sees a mix. |
| **Allocation** | 1:1 at impression level, seeded per student so a given listing keeps its arm for that student; 3 weeks; expected ~40 eligible impressions per student ⇒ ~8,000 impressions. |
| **Primary metric** | Application-start rate per impression (binary). |
| **MDE + power rationale** | Baseline 12%; assumed ICC 0.10 with cluster size 40 ⇒ design effect 1 + 39(0.10) = 4.9; effective n ≈ 1,633 (≈816/arm). SE(diff) = √(2·0.12·0.88/816) = 0.0161 ⇒ **MDE ≈ 4.5pp** (12% → 7.5% or 16.5%). This detects only large effects — which is appropriate, because the decision is binary: is verification worth its latency and infrastructure cost at all? |
| **Secondary (the outcome that matters)** | Wasted-application rate per student = applications that were dead at submission or within 7 days. Student-level, n = 100/arm ⇒ MDE = 2.80·√(2/100) = **0.40 SD**. |
| **Guardrail** | Total applications per student must not fall by more than 15% (pre-specified non-inferiority margin); plus median added latency < 1.5s at p95. |
| **Pre-registered stop rule** | Fixed horizon: 3 weeks or 8,000 impressions, whichever first. **One** interim at day 10, **on the guardrail only** — halt if the applications drop exceeds 15% with p < 0.005. No interim look at the primary; no extension of the sample after unblinding. |

### Experiment 2 — Alert cadence: instant alerts vs a scheduled digest

| | |
|---|---|
| **Hypothesis** | A digest delivered in a student-chosen window produces at least as much engagement as instant alerts, with materially lower mute/unsubscribe rates. |
| **Why** | B09 (28% lower frustration, 13% faster response at breakpoints; 49.7% faster at scale) and B10 (realistic engagement ≈ 5–7%) say timing dominates content. Churn — not click-through — is the failure mode of alert products. |
| **Unit of randomisation** | **Student** (contamination between arms is impossible; cadence is a property of the account). |
| **Allocation** | 1:1, blocked by market and year; 4 weeks; n = 200 (100/arm). |
| **Primary metric** | Number of listings opened from alerts per student over 28 days (count; negative-binomial model). |
| **MDE + power rationale** | n = 100/arm ⇒ MDE = 0.40 SD. With an assumed mean of 9 opens and SD 8, **MDE ≈ 3.2 opens (~35% relative)**. State plainly in the pre-registration: this trial can only kill or keep a cadence, it cannot estimate a small difference. |
| **Secondary** | Applications started; time-to-first-open; 28-day retention of the alert channel (binary; note n = 200 gives only ~20pp MDE on a 55% baseline — reported as descriptive). |
| **Guardrail** | Mute/unsubscribe rate ≤ 15% per arm; zero alerts delivered inside declared quiet hours (hard constraint, monitored as a defect not a metric). |
| **Pre-registered stop rule** | Stop an arm at the day-14 interim if its mute rate exceeds 25% (pre-specified harm threshold); otherwise run the full 4 weeks. Primary analysed once, at the end. |

### Experiment 3 — Willingness to pay (revealed, with real money)

| | |
|---|---|
| **Hypothesis** | At least 20% of students who completed a 3-week trial will pay the low price point, and demand is materially price-sensitive between the two points. |
| **Why revealed and not survey** | H01: median hypothetical-to-actual WTP ratio **1.35** with severe positive skew, and the meta-analysis specifically flags **student subjects** as a possible source of bias. A stated-preference answer from 200 students is close to worthless on its own. |
| **Design** | Two stages. **(a)** At day 18, every student answers one incentive-free closed question ("would you pay ₹X / $Y per month?") — recorded only to estimate Signal's own hypothetical-bias factor. **(b)** At day 21 the paywall appears with a **randomly assigned real price**, charged for real, cancellable any time, refundable on request within 14 days. |
| **Unit of randomisation** | **Student**, assigned at trial start (so price is fixed before any usage effects), blocked by market: India cells ₹149 vs ₹399/month; US cells $3 vs $8/month. |
| **Allocation** | 1:1 within market; n = 200 ⇒ 100 per price cell (50 per market-cell). |
| **Primary metric** | Paid conversion rate at the assigned price (binary, revealed preference). |
| **MDE + power rationale** | Comparing 25% vs 10%: SE = √(0.25·0.75/100 + 0.10·0.90/100) = 0.053 ⇒ z = 0.15/0.053 = 2.85, **power ≈ 81%**. So the design detects a **15pp** gap between price points, i.e. a roughly 2.5× difference in conversion — enough to choose a price, not enough to estimate elasticity. Market-level cells (n = 50) are descriptive only and must be reported as such. |
| **Secondary** | Hypothetical-vs-revealed ratio per market (Signal's own calibration factor, to compare against H01's 1.35); 60-day retained-payer rate. |
| **Guardrail** | Refund-on-request within 14 days, no questions asked; "regret rate" (refunds + immediate cancellations) tracked per cell; no dark patterns in the cancel flow (manually reviewed before launch). |
| **Pre-registered stop rule** | Fixed n = 200 or 6 weeks, whichever first. Halt the paywall entirely if the regret rate exceeds 10% in either cell at the day-21 interim. No price changes mid-experiment; any new price requires a new pre-registration. |

**Three things these experiments deliberately do not test:** employment outcomes (B06 shows even n = 212,277 with administrative data was needed to produce precise nulls — 200 students cannot speak to employment), interview counts as a primary (C01 needed 3,794 per arm for the implied job-finding effect), and agent autonomy (not safe to randomise until the read-only architecture in idea 23 passes a red-team).

---

## 7. User research protocol (10 participants)

### 7.1 Screening

Screener survey (5 questions, ~90 seconds), run over campus channels in both markets. **Include** if: currently a student or ≤ 12 months from graduation; applied to ≥ 3 internships/early-career roles in the last 60 days; uses at least two sources (e.g. a campus portal plus LinkedIn or Unstop); has a smartphone with notifications enabled. **Exclude** if: works in recruiting or HR tech; has used an auto-apply bot as their primary channel (separate, much smaller, segment — interview later, do not mix); is a personal contact of the team.

### 7.2 Sampling plan (10 participants)

| Slot | Market | Profile | Rationale |
|---|---|---|---|
| 1–2 | India | Tier-1 city engineering student, actively applying | Core volume segment; heaviest Unstop/Internshala users |
| 3–4 | India | Tier-2/3 city student, non-CS major | Tests whether a curated ATS-first source list has enough coverage (idea 1's failure mode) |
| 5 | India | Final-year student who applied to PMIS (G02) | Government-portal expectations and the 3-application cap |
| 6–7 | US | Undergraduate at a non-target school, 2+ months searching | Matches the narrow-searcher segment from C01 |
| 8 | US | Student with a prior internship (C03 signal present) | Different baseline callback experience |
| 9 | Either | Student who stopped applying in the last month | Discouragement path (B02) — the person a retention feature must serve |
| 10 | Either | Student who has used an AI tool to write or submit applications | Direct probe of the D07 reputational-penalty question |

Sessions: 45 minutes, remote, recorded with consent, incentive paid in local currency (₹800 / $15), transcripts stored pseudonymously, deleted after 180 days. Two researchers; one interviews, one codes. Stop recruiting at 10 unless two new codes appear in the last two sessions (then extend to 12).

### 7.3 Semi-structured guide (10 questions)

Warm-up: "Walk me through the last internship you applied to — screen by screen."

1. When you look at a listing, how do you decide whether it is **still real**? What do you look at first?
2. You see a posting labelled "posted 3 days ago" and another labelled "we checked this listing 20 minutes ago on the company's own careers page." What is the difference to you — and what would make you doubt the second one?
3. Tell me about a time you applied to something and later realised the role was gone or had never been open. What happened, and what did it cost you?
4. If a tool told you a listing was "likely a ghost job", how would you react? What would you need to see before you believed it? *(Probe: would a wrong accusation bother you?)*
5. How many job alerts in a day is too many? What is the difference between an alert that helps and one that makes you mute the app? *(Probe for timing, batching, quiet hours — B09/B10.)*
6. Describe the last time you muted or deleted a job-alert product. What was the final straw?
7. If an app offered to **fill in** an application form for you, where exactly would you want to be asked before anything was sent? *(Probe for per-application vs blanket consent — D04.)*
8. Suppose the employer could tell that an AI helped you apply. Does that change anything for you? *(Probe the reputational concern directly — D07.)*
9. Someone suggests roles you did not search for, because students with your profile got interviews there. Useful or irrelevant? When would it feel like the tool had given up on what you actually want? *(C01's narrow/broad heterogeneity.)*
10. If this tool cost money, what would need to be true for you to pay for it — and what would you expect it to stop doing for free? *(Then: "what have you actually paid for in your job search so far?" — anchor on revealed behaviour, per H01.)*

Close: "What is the one thing about applying to internships you would pay someone to make go away?"

**Analysis:** code against the five anchor mechanisms (staleness, attention, breadth, automation trust, identity/freshness) plus an open bucket; report disagreements between India and US slots separately — do not pool, and do not generalise across markets (standing constraint).

---

## 8. Data and feasibility notes

### 8.1 What each source actually exposes

| Source | Creation timestamp | Update timestamp | Removal / close signal | Repost or requisition ID | Vacancy / AI disclosure | Access status (checked 2026-10-12) |
|---|---|---|---|---|---|---|
| **Greenhouse Job Board API** (E04) | `first_published` | `updated_at` | Listing disappears from the board; `application_deadline` when set | `requisition_id`, `internal_job_id`, `id` | **Yes** — `include_ai_disclaimer`, `ai_disclaimer`, `ai_opt_out_request_url` | Public JSON, no auth for reads; auth only to POST applications |
| **Lever Postings API** (E05) | **Not documented** | **Not documented** | Posting disappears from the feed | `id` (posting ID) only | No | Public JSON; application POST rate-limited (429s); Lever states published postings may be scraped by third parties |
| **USAJOBS Search API** (E06) | `PublicationStartDate`, `PositionStartDate` | — | **`ApplicationCloseDate`, `PositionEndDate`** (explicit) | `PositionID`, `MatchedObjectId` (control number) | n/a (federal process disclosed elsewhere) | API key required; US federal only |
| **Employer career pages (generic)** | Sometimes in JSON-LD `JobPosting.datePosted` | Rarely | Page 404 / removed from index | Sometimes in URL | Increasingly, where law requires (F04) | Logged-out public fetch; per-site robots to be checked and snapshotted |
| **Unstop** (E08) | Not inspected | Not inspected | Not inspected | Not inspected | Not inspected | `robots.txt` **allows** `/internship/`, `/job/`, `/competitions/`, `/api/public/*` for generic agents |
| **Internshala** (E07) | — | — | — | — | — | `robots.txt` **disallows** listing, detail and search paths for all agents ⇒ **excluded** |
| **LinkedIn** (E09) | — | — | — | — | — | `robots.txt` returned **HTTP 403** to this sandbox ⇒ **human-initiated deep links only** |
| **PMIS (pminternship.mca.gov.in)** (G02) | Not inspected | Not inspected | Round-based deadlines announced via PIB | n/a | Government scheme | First-party government portal; terms not yet reviewed — **check before integration** |
| **Eurostat/Cedefop WIH OJA** (E02) | Publication date extracted by the pipeline | n/a | n/a | Portal reference IDs used for dedup | n/a | Methodology is public and copyable; the microdata is not a live feed for a consumer product |

**Gaps to state plainly to the product team:** no source in this review publishes a *removal* event; removal is always inferred from absence. Only USAJOBS publishes a close date as a first-class field. Only Greenhouse publishes both a creation and an update timestamp plus a requisition ID — which is why ideas 1, 9, 10 and 11 are scoped to ATS-backed boards first.

### 8.2 Licence and terms posture

- **Robots-first, logged-out-always.** Collect only what a logged-out visitor can see; snapshot each source's `robots.txt` alongside the allowlist entry and re-check weekly; honour `Crawl-delay` (e.g. Bingbot 1s on Unstop, E08).
- **Terms of service are the live risk, not the CFAA.** hiQ won the CFAA point and still ended with a $500,000 judgment and a permanent injunction on contract grounds (F02); Bright Data prevailed because it was **logged out** and not a party to the terms (F03). Translation: never create accounts, never log in, never bypass CAPTCHAs or rate limits, and keep a documented record of the logged-out posture.
- **ATS feeds have their own terms.** Lever's docs explicitly contemplate third-party scraping of published postings (E05); Greenhouse's reads are unauthenticated (E04). Both still need a written review per employer board, because the employer — not the ATS — usually owns the posting.
- **Student data.** India: DPDP Rules commencement is staged to ~13 May 2027 for the substantive obligations, with itemised notice and easy withdrawal (F05). EU/UK students on campus: GDPR applies to profile data; no GDPR text was opened in this session, so **treat the GDPR analysis as not yet done** rather than assumed.

### 8.3 Cost per verified listing — feed-based vs agent-based `[EST]`

Arithmetic, not a quote. Assumptions stated so they can be overridden.

**Feed-based (ATS boards):** 300 employer boards × 24 checks/day = 7,200 HTTP GETs/day. Assume 50 postings per board ⇒ 15,000 postings covered, each re-verified 24×/day = 360,000 listing-verifications/day from 7,200 requests. At a generous $0.00002 per request-equivalent in compute and bandwidth, that is **≈ $0.0004 per 1,000 listing-verifications**, i.e. effectively free; the real cost is engineering time and the per-board onboarding.

**Agent-based (browser agent on an arbitrary career page):** 30–90 seconds of a browser session plus model tokens. Assume $0.01–0.05 per attempt all-in. At the live-web success rate for unseen sites of **≈30%** (D03), the cost per *successful* verification is **$0.03–0.17**, plus a human fallback for the ~70% that fail. At 15,000 listings re-verified even once a day, that is **$450–2,550/day** — three to four orders of magnitude more than the feed path.

**Conclusion that follows from the arithmetic:** agents are not a verification layer, they are a **coverage-expansion** tool of last resort — used for one-off checks of sources with no feed, under a read-only architecture (idea 23), with results cached and a human queue for failures (idea 25). Any plan that puts an agent in the steady-state verification loop is both ~1,000× more expensive and three times less reliable than the feed path.

---

## 9. Legal, policy and ethics pass

**Status note:** this is an engineering-grade reading of primary sources where they could be opened, and of law-firm analyses where they could not. Items marked **LAWYER** must be confirmed by counsel before launch. Nothing here is legal advice.

### 9.1 United States — computer access and contract

| Instrument | What it actually holds | What it means for Signal |
|---|---|---|
| **CFAA after *Van Buren*** (F01, primary opinion read) | "Exceeds authorized access" = obtaining information from areas of a computer that are off-limits to you; a **gates-up-or-down** inquiry. Purpose and policy violations are outside the clause. | Reading a public, logged-out job posting is not a CFAA problem. Creating accounts to see more, or using credentials you are not entitled to, puts you back inside the statute. |
| **hiQ v. LinkedIn** (F02, `[SECONDARY]`) | 9th Cir. (Apr 2022): scraping public profiles likely is **not** CFAA "without authorization". N.D. Cal. (Nov 2022): hiQ nevertheless **breached the User Agreement**. Dec 2022 consent judgment: **$500,000**, permanent injunction, data deletion. | **The limit of the CFAA win is the whole lesson.** Contract, trespass-to-chattels and misappropriation theories survived and ended the company. Signal must not scrape LinkedIn under any configuration. |
| **Meta v. Bright Data** (F03, `[SECONDARY]`) | Terms govern "your use" as a logged-in user; a logged-out non-user did not breach them by collecting public pages. Only tortious interference survived. | The defensible posture is precisely: logged out, no account, no CAPTCHA bypass, public pages only, honour robots and rate limits. **LAWYER:** confirm this reading against each target site's current terms, since the outcome turned on specific wording. |
| **FTC Act §5** (A02, A08) | CRS notes §5 reaches deceptive advertising; the Feb 2025 FTC Joint Labor Task Force named deceptive job advertising; Grimm argues ghost jobs are actionable deception. | Cuts **both ways**. It supports Signal's mission framing, and it governs Signal's own claims: a "verified live" badge that is wrong, or a "ghost job" label that is unfounded, is itself a potential deception/defamation exposure. Hence do-not-build #3 and #8. |

### 9.2 Canada — Ontario (the first regulator to act on this directly)

- **O. Reg. 476/24** under the Employment Standards Act, 2000, **in force 1 January 2026** (F04, primary text read; e-Laws currency 7 Oct 2026). Verified from the regulation itself: Part III.1 does **not** apply to employers with **fewer than 25 employees** on the posting date; "artificial intelligence" is defined broadly (any machine-based system inferring outputs from inputs); "publicly advertised job posting" excludes general recruitment campaigns, help-wanted signs, internal-only postings, and out-of-Ontario work; compensation disclosure is excused above **$200,000**; a posted range may not exceed **$50,000**; interviewed applicants must be told within **45 days** whether a hiring decision was made.
- **LAWYER / verification gap:** the two duties most relevant to Signal — the statement of whether the posting is for an **existing vacancy**, and the disclosure of **AI used to screen, assess or select** — sit in ESA ss. 8.1–8.6, and the e-Laws statute page did not render for this review. Multiple law-firm summaries describe both duties as effective 1 Jan 2026 (`[SECONDARY]`), and the regulation's own cross-references to ss. 8.1, 8.2(2), 8.2(3) and 8.6 are consistent with that. **Confirm the statutory text before quoting the duty in product copy.**
- **Product consequence:** in Ontario, the "is this a real vacancy?" question becomes an employer-authored field rather than an inference. Signal should ingest and display that statement (idea 9) — and Greenhouse already exposes an AI-disclosure field that maps onto the second duty (E04).

### 9.3 India — DPDP

- **DPDP Rules, 2025** notified 13–14 Nov 2025, G.S.R. 846(E) (F05, gazette text read). Commencement is staged **in the rules themselves**: rules 1, 2 and 17–21 on publication; **rule 4 (consent managers) at 12 months**; **rules 3, 5–16, 22, 23 at 18 months** (≈13 May 2027). Rule 3 requires a notice that is understandable **independently of any other information**, with an **itemised description of the personal data** and the specific purposes, plus a link enabling withdrawal of consent **as easily as it was given**.
- **Product consequence:** Signal stores student profiles, filters, résumés and (if prefill ships) application content — all personal data of, frequently, young adults. Build the itemised notice, granular purposes, and one-tap withdrawal **now**; retrofitting consent architecture in 2027 is more expensive than building it in 2026. **LAWYER:** children's-data rules (verifiable parental consent) if any users are under 18; significant-data-fiduciary thresholds; cross-border transfer rules for US-hosted infrastructure.

### 9.4 EU/UK — GDPR

**Not assessed in this review.** No GDPR primary text or guidance was opened in this session, so there is no finding to report. If any student user is in the EU/UK (likely for international internship search), a separate pass is required covering: lawful basis for profile processing, automated-decision-making rules if Signal ranks or filters opportunities, data-minimisation for scraped employer contact details, and retention. **Flagged as an open LAWYER item, not as a cleared one.**

### 9.5 Platform terms — operating rules that fall out of the above

1. Logged-out only; no account creation; no credential sharing; no CAPTCHA or rate-limit circumvention (F01, F02, F03).
2. `robots.txt` is a hard gate, snapshotted at onboarding and re-checked weekly; a source that disallows its listing paths is excluded, full stop (E07 — Internshala).
3. A source whose access policy cannot even be retrieved is treated as a prohibition, not an absence (E09 — LinkedIn, HTTP 403).
4. Per-source request budgets honour published `Crawl-delay` (E08 — Bingbot 1s on Unstop) and self-impose conservative concurrency.
5. Agent traffic is identified honestly in the user-agent string, with a contact URL.

### 9.6 Ethics — the three decisions that matter most

- **Accusation asymmetry.** Labelling a real employer's real posting "ghost" harms a third party who is not Signal's user and cannot respond. The evidence base cannot support individual-listing accusations (A01, A02). **Report observations, not verdicts.**
- **Disclosure vs reputational harm to the student.** AI assistance carries a measured social-evaluation penalty that changes hiring decisions (D07, N = 4,439, preregistered), and 15% of candidates oppose any AI in hiring (A04). The student — not Signal — decides what is disclosed and what is automated. Per-application consent, 24-hour expiry, full audit log (idea 24).
- **Congestion and fairness.** Speed advantages in a congested market are partly zero-sum (C04: −2.1pp for untreated peers; −7.7pp in the tightest markets). Signal should not advertise "apply first, beat other candidates"; it should sell *not wasting effort*. This is both the honest framing and the one supported by evidence.

---

## 10. Search trail

**Date of all searches and retrievals: 2026-10-12.** Tooling: Arena web-search tool (general web index) and direct URL retrieval (`fetch_page`). Databases and repositories reached: arXiv, SSRN, RePEc/IDEAS, EconPapers, AEAweb, NBER, ACL Anthology, ACM Digital Library, NeurIPS Proceedings, Wiley Online Library, Oxford Academic (REStud), Semantic Scholar, congress.gov (CRS), supremecourt.gov, ontario.ca e-Laws, meity.gov.in (Gazette of India), pib.gov.in, cros.ec.europa.eu (Eurostat WIH), naceweb.org, columbialawreview.org, GitHub, vendor documentation sites, and `robots.txt` endpoints.

### 10.1 Queries run (verbatim, this session)

```
Mind2Web MindAct GPT-4 results "task success rate" element accuracy step success cross-domain test split
Cedefop Eurostat Web Intelligence Hub online job advertisements methodology deduplication ESCO classification
Ontario Employment Standards Act publicly advertised job postings January 1 2026 "existing vacancy" artificial intelligence disclosure O. Reg. 476/24
Meta Platforms v Bright Data 2024 ruling scraping breach of contract logged out public data
Liu Huang Wang 2014 meta-analysis job search interventions employment odds "Journal of Applied Psychology" effect
Kelley Ksoll Magruder "How Do Online Job Portals Affect Employment and Job Search" India Babajob randomized results
"Can a Website Bring Unemployment Down" Bob Emploi randomized evaluation France results Crépon Pons
Belot Kircher Muller online advice jobseekers "44%" increase interviews narrow search unemployed
Kelley Ksoll Magruder "Job Shikari" American Economic Journal Applied Economics 2024 online job portals India published
mobile notification field study attention "opportune moments" breakpoint response time reduced disruption CHI UbiComp evaluation
job advertisement deduplication benchmark dataset near-duplicate detection online job ads evaluation precision recall research
Gee 2019 Management Science "The More You Know" LinkedIn field experiment number of applicants information job application rates 3.5%
Crépon Duflo Gurgand Rathelot Zamora 2013 Quarterly Journal of Economics job placement assistance displacement effects randomized experiment France
Altmann Falk Jäger Zimmermann 2018 "Learning about job search" information brochure unemployed Journal of Public Economics results
"algorithmic job recommendations" Sweden randomised field experiment job seekers clicks applications 10-16% no effect job finding
Digital Personal Data Protection Rules 2025 notified India date phased implementation consent manager MeitY official gazette
skill extraction job postings ESCO benchmark F1 evaluation "SkillSpan" OR "Kompetencer" OR "TechSkillNER" state of the art 2023 2024 error analysis
AgentDojo benchmark prompt injection attack success rate utility under attack NeurIPS 2024 AI agents
survey job seekers comfort AI agent auto-apply on their behalf percentage 2025 consent autofill applications research
hiQ Labs v LinkedIn Ninth Circuit April 2022 opinion CFAA "without authorization" public profiles; November 2022 final judgment breach of contract settlement
Faberman Kudlyak "intensity of job search" Snagajob data sample number of job seekers applications 2019 AEJ macro working paper
hiQ Labs LinkedIn final judgment December 2022 stipulated consent judgment hiQ admitted breach permanent injunction
Schilke Reimann 2025 AI disclosure reduces trust "Journal of Experimental Social Psychology" OR PNAS Nexus transparency penalty
NACE 2025 internship conversion rate offer rate full-time hires from internship program survey percentage
Greenhouse "Real Jobs" verified job badge 2025 ghost job verification how it works
experiment "posting age" OR "job age" displayed job seekers application behavior field experiment evidence stale listings
Albrecht Decreuse Vroman "phantom vacancies" directed search listing age journal calibration US data
PM Internship Scheme India 2025 portal number of internship opportunities applications official PIB
Switzerland search diaries 15,000 job seekers 600,000 applications duration dependence applications decline 25% discouragement paper authors 2025
hypothetical bias meta-analysis stated versus real willingness to pay ratio List Gallet 2001 Murphy 2005 median ratio
measurement study expired job postings still listed aggregator stale dead listings percentage research crawl
willingness to pay job search tool students subscription experiment price premium alerts evidence
```

Earlier in the same session (wording recorded in the session log as a paraphrase, not preserved verbatim — flagged as such rather than reconstructed): searches for **Ng 2024 / arXiv 2410.21771 ghost jobs**, **Nunley et al. 2016 internship callbacks Labour Economics**, **SSRN 5987416**, **"Online-Mind2Web" "An Illusion of Progress"**, and **Cho & Garcia-Molina TODS 2003 refresh policies**.

### 10.2 Documents retrieved directly (`fetch_page`)

arxiv.org/abs/2410.21771 · arxiv.org/abs/2306.06070 · arxiv.org/html/2306.06070v3 · arxiv.org/abs/2410.06703 · arxiv.org/html/2504.01382v4 · arxiv.org/html/2410.12052v1 · arxiv.org/html/2511.03377v1 · arxiv.org/pdf/2306.13063 · aeaweb.org (mac.20170315) · frbsf.org wp2016-13.pdf · ideas.repec.org (REStud 86-4; Labour Economics 38; J Public Economics 164; Env. & Resource Economics 30-3) · academic.oup.com/restud/article/86/4/1411/5115940 · papers.ssrn.com (5987416) · nber.org/papers/w29914 · povertyactionlab.org (WP3740) · semanticscholar.org (Hensvik et al.) · philippkircher.com · academia.edu (Liu et al. 2014) · aclanthology.org/2024.nlp4hr-1.3.pdf · dl.acm.org/doi/pdf/10.1145/3486622.3493928 · proceedings.neurips.cc (AgentDojo) · oak.cs.ucla.edu/~cho/papers/cho-tods03.pdf · onlinelibrary.wiley.com/doi/abs/10.1111/iere.12615 · faculty.georgetown.edu/vromans/PhantomsMarch2017Final.pdf · andreyfradkin.com/assets/jobs_authors.pdf · pielot.org/pubs/Pielot2017-UbiComp-Engagement.pdf · julian-ramos.com/papers/Okoshi2015.pdf · pnas.org/doi/10.1073/pnas.2426766122 · congress.gov (IF12977) · supremecourt.gov/opinions/20pdf/19-783_k53l.pdf · ontario.ca/laws/regulation/240476 · ontario.ca/laws/statute/00e41 *(returned no content)* · meity.gov.in Gazette PDF (DPDP Rules 2025) · pib.gov.in (PRID 2111914) · columbialawreview.org (Grimm 2025) · cros.ec.europa.eu/wih/oja · docs.greenhouse.io/job-board.html · github.com/lever/postings-api (+ README) · developer.usajobs.gov/api-reference/get-api-search · greenhouse.com/blog/greenhouse-2024-state-of-job-hunting-report · resumebuilder.com (fake postings survey) · clarifycapital.com (ghost jobs survey) · linkup.com (absurd myth of ghost jobs) · naceweb.org (internship conversion) · internshala.com/robots.txt · unstop.com/robots.txt · linkedin.com/robots.txt *(HTTP 403)* · cedefop.europa.eu/en/data-insights/online-job-advertisements-methodology *(404)* · greenhouse.com/real-jobs *(404)* · greenhouse.com/blog/ai-in-hiring-report-2025 *(404)*

### 10.3 Retrieval failures, recorded

| Target | Result | Consequence |
|---|---|---|
| `academic.oup.com/restud/article/86/4/1411/...` (first attempt, earlier in session) | Returned navigation chrome only (paywall) | Re-attempted later at the redirected URL and the article sections were returned; the "44%" figure is quoted from that successful retrieval |
| `linkedin.com/robots.txt` | **HTTP 403** | LinkedIn treated as human-only (E09, do-not-build #1) |
| `ontario.ca/laws/statute/00e41` | Page returned no body content | ESA ss. 8.1–8.6 text unverified → LAWYER item (§9.2) |
| `cedefop.europa.eu/.../online-job-advertisements-methodology` | 404 | Methodology sourced instead from the Eurostat CROS WIH page (E02) |
| `greenhouse.com/real-jobs`, `greenhouse.com/blog/ai-in-hiring-report-2025` | 404 | Greenhouse's 2025 "AI in Hiring" statistics (22% of candidates using bots, 91% of recruiters spotting deception) are **not cited** anywhere in this review, because only third-party restatements were reachable |
| Schilke & Reimann (2025), OBHDP 188:104405 | Article itself not opened; seen only in citing works | Cited as `[UNVERIFIED]` corroboration for D07, never as a standalone finding |

---

## 11. Themed sub-questions

### 11.1 Ghost listings and staleness

**How common are postings that cannot be filled?** Unknown, and the honest answer is that nobody knows: CRS states there are **no official statistics** (A02). The credible *bounds* on the question come from duration data, not surveys: of US jobs removed from company career sites in March 2023, **58% had been up under 30 days** and **7% over six months**, with an average closed duration of **45.6 days** against a 46-day average time-to-fill (A07). The headline prevalence numbers (21%, A01; 18–22%, A04; 40% of companies, A05) measure three different things by three undisclosed or non-comparable methods.

**Which observable features correlate with a posting being problematic?** Only one quantified correlate was found: **confidential/unnamed employer, 77.5% vs 47.5% (1.63×, p<0.05)** — on a 160-posting, US-and-software-dominated convenience sample (A03). Treat as a hypothesis, not a feature spec.

**Does showing posting age change what students apply to?** **Yes — causally.** Removing vacancy age from a job board cut clicks **3%** and applications **1.8%**; showing prior-applicant counts moved applications **+3.8%** toward vacancies with fewer than five prior applicants (A10, three randomised experiments, millions of users). Theory and calibration agree that search concentrates violently on new listings: **~70% of applications to listings under 48 hours old**, with the queue per listing falling **more than 5×** from day 1 to day 2 (A09).

**How often do saved/bookmarked listings go dead, and how fast?** **NO EVIDENCE FOUND.** Queries attempted: `measurement study expired job postings still listed aggregator stale dead listings percentage research crawl`; `experiment "posting age" OR "job age" displayed job seekers application behavior field experiment evidence stale listings`; plus the ghost-job searches listed in §10.1. What surfaced was vendor commentary on job-board "pollution" (a LinkUp blog post that was not opened and is therefore not cited) and an unsourced Reddit analysis of "5 million listings" — neither is usable under the standing rules. **This is a measurable gap Signal should close with its own instrumentation (idea 7), not fill with a citation.**

**Do reposts resurface at the top of date-sorted results?** **NO EVIDENCE FOUND.** Queries attempted: as above, plus `job advertisement deduplication benchmark dataset near-duplicate detection online job ads evaluation precision recall research`. The mechanism is plausible (ATS feeds carry `requisition_id` and `updated_at`, E04) and is directly testable in Signal's own data, but no study measuring it was located.

**Is there India-specific evidence on ghost listings?** **NO EVIDENCE FOUND.** Every prevalence source located is US-centric (A01, A03, A04, A05, A06) or US/UK/Germany (A04). Do not transfer any of these rates to Internshala, Unstop or Indian career pages.

### 11.2 Search behaviour and decay

**Does effort decay within a search spell?** Contested, and the contest is the finding. Yes in US low-wage online application data (**2.3 → 1.2 applications/week in month 1**, B01) and in Swiss search diaries (**11 → just under 10 per month over 12–15 months**, B02). **No** in Swedish activity reports, where within-spell effort is flat and **86–90%** of the apparent callback decline is composition (B03). For a product: measure it in your own cohort before building for it.

**Who are the heavy users?** Counter-intuitively, the long-duration seekers — they search **more** intensely throughout, and are older, male, nonemployed and in weaker local markets (B01). Any "re-engage the lapsed user" feature built on the opposite assumption is aimed at the wrong people.

**What actually declines?** Employer response. Interviews per application fall with duration while **offers per interview rise** (B02). The implication for Signal is that evidence-of-response features (idea 16) address the real decay, and volume features do not.

**Do information interventions work?** Weakly and only when targeted. Meta-analysis: OR **2.67** overall, but **3.54** short-term vs **1.72** long-term unemployed, and only when skill *and* motivation components were both present (B04). Brochures: null on average, **+4%** employment and earnings for the at-risk tail (B05). Full web platforms: **precise nulls** at n = 212,277 (B06). Recommenders: **+10–16%** clicks, nothing downstream (B08).

**Does more information ever hurt?** **Yes, in India.** Being told you were added to a job portal **reduced employment by 9.2pp (−30%)** for 12 months, via raised reservation wages; sending substantially more information about the actual jobs on offer cut the damage to **−4.8pp** and *lowered* reservation wages 5.3% (B07). This is the strongest India-specific result in the review and it argues for shipping calibrated base rates with alerts (idea 14).

**What alert cadence is tolerable?** No study of job alerts specifically was found; the transferable HCI evidence says timing beats content: breakpoint-timed notifications produced **28% less frustration** and **13% faster** responses (n = 30 in the wild), with a 680,000-user deployment reporting **49.7% faster** responses (B09), and realistic voluntary engagement with proactive content is around **4–7%** (B10).

### 11.3 Breadth, matching and skills

**Does broadening search help?** For narrow searchers, yes: **+0.2 SD** breadth and **+44% interviews** — at **p<0.10**, n ≈ 300, Edinburgh (C01). The same team's pre-registered UK scale-up with ~1,500 long-term unemployed reports **+20–40%** on stable-job and earnings outcomes at 9 months (C02, author page; full paper not opened).

**Who should not be broadened?** Initially broad searchers became *narrower* under the same treatment with no interview gain (C01). Targeting is not an optimisation here; it is a correctness requirement.

**What do students actually control?** Internship experience: **+14% interview rate** in a US résumé audit, with **no** measurable benefit from the business degree itself (C03). Signalling, not human capital, is the favoured explanation — which means the product job is making an existing signal legible, not manufacturing one.

**Does helping some students hurt others?** Yes, measurably: **−2.1pp** for untreated peers in treated areas, and **−7.7pp** in the most competitive local markets (C04).

**How reliable is automated skill/requirement extraction?** Span-F1 tops out around **64.8** on the standard SkillSpan benchmark, with **GPT-4 few-shot at 27.8** (C05); across six datasets, supervised systems average **64.4 F1**, errors concentrate in conjoined skills (**17–22%**), and **8%** of "errors" are wrong gold labels (C06). Extraction is an assistive summary, never a filter criterion the student cannot see through (idea 22).

**Is there a validated occupation-adjacency resource for Indian early-career roles?** **NO EVIDENCE FOUND.** Queries attempted: the SkillSpan/ESCO query in §10.1 and the Cedefop/ESCO methodology query. ESCO and O\*NET are European and US instruments respectively; no evaluation of either on Indian internship titles was located. Build adjacency from Signal's own co-application data (idea 18) and treat imported taxonomies as unvalidated here.

### 11.4 Agents, extraction and trust

**What success rate should Signal plan for?** **≈30%** for an agent on unseen live sites (D03), not 55–60%. On a small curated set of known sites, ~59% is defensible (D01). The gap between those two numbers *is* the argument for the curated source list (idea 1).

**Is the benchmark literature itself reliable?** Only with care. A naive search-and-click agent scores **51% on WebVoyager** but **22%** on the live, human-graded set (D03) — i.e. one popular benchmark can be substantially gamed. And the Mind2Web citation in the brief does not support the claim made from it at all (D02).

**What happens to safety when agents succeed?** Completion under Policy averages **under two-thirds** of nominal completion across three SOTA agents (D04): roughly a third of "successes" break a stated rule. Under adversarial input, GPT-4o shows **47.7%** targeted attack success, while a **tool-filter** architecture cuts that to **~7.5%** at a 15–20% utility cost (D05).

**Can model self-confidence gate the "live" label?** No. Verbalized confidence is systematically overconfident, clusters at 80–100%, and shows average **ECE > 0.377** for several models (D06). Calibrate on observed outcomes instead (idea 25).

**How will students feel about automated submission?** The closest evidence is general but strong: four preregistered experiments (**N = 4,439**) find people who use AI are judged **less competent, less diligent and less motivated**, and that this changes hiring decisions (D07); 15% of candidates oppose **any** AI involvement in hiring (A04). Corroborating work on disclosure penalties exists (Schilke & Reimann 2025, OBHDP 188:104405) but was **not opened** — `[UNVERIFIED]`.

**Is there direct evidence on students' trust in automated job-application agents?** **NO EVIDENCE FOUND.** Queries attempted: `survey job seekers comfort AI agent auto-apply on their behalf percentage 2025 consent autofill applications research`; `Schilke Reimann 2025 AI disclosure reduces trust ...`. Only vendor blogs and tool-marketing content surfaced. This is exactly what the user-research protocol's questions 7–8 are for (§7.3).

### 11.5 Freshness, dedup and identity

**What refresh policy maximises freshness under a fixed budget?** Importance-weighted and near-uniform, checked in **fixed order**. The measured ordering is unambiguous: proportional **0.12** freshness / 400 days age; uniform **0.57** / 5.6 days; optimal **0.62** / 4.3 days; fixed-order beats random-order **0.63 vs ~0.48** at r=1 (E01, validated on 270 sites over 4 months).

**How do official statistical pipelines handle the same identity problem?** Three stages, then **merge**: physical (same URL/ID), semantic (fuzzy match on description + location; portal reference IDs to strip aggregator copies), logical (structured-field match after extraction) — Eurostat/Cedefop WIH (E02). Duplicates are flagged and merged, not silently dropped, which preserves per-source provenance. Known error sources are documented by the producers themselves: dedup, merging, spam filtering, date detection, language detection.

**How hard is dedup technically?** Not hard: **F1 0.9686 / AUC 0.9952** from n-gram overlap with title+location blocking on a 1,498-pair expert gold set, beating a published baseline (E03). The scale of the problem is the issue, not the algorithm — duplicates are estimated at **50–80%** of board-crawled postings (Textkernel, cited in E03).

**Which sources expose the timestamps Signal needs?** Greenhouse: `first_published`, `updated_at`, `requisition_id`, `application_deadline`, plus AI-disclosure fields (E04). USAJOBS: `PublicationStartDate`, `ApplicationCloseDate`, `PositionEndDate` (E06). Lever: **no documented timestamps at all** (E05). Nobody publishes a removal event — removal is always inferred from absence.

**Can Signal monitor the three named consumer sources?** Partially: **Unstop yes** (robots allows `/internship/`, `/job/`), **Internshala no** (robots disallows listing, detail and search paths for all agents), **LinkedIn no** (robots itself returned HTTP 403) (E07, E08, E09). Company career pages — the fourth named source — are the strongest leg and should carry the product.

---

## 12. Executive brief (one page)

**Bottom line.** The product thesis survives the evidence, but three of the five anchor claims must be restated before they appear in a deck, a pitch, or product copy. The defensible version of Signal is *a small, honest, verified source list with per-listing provenance*, not *a market-wide ghost-job detector with an autonomous apply agent*.

### Five decisions the evidence supports

1. **Build ATS/career-site-first, with a published source list.** Career-site data is the clean layer (A07); Greenhouse alone yields created + updated + requisition identity + the employer's own AI disclosure (E04); board copies carry a 50–80% duplicate load (E03). Smaller and trusted beats bigger and unchecked.
2. **Make every freshness claim per-listing, timestamped and sourced.** There is no official prevalence statistic to lean on (A02), estimates swing 1.3%→21% by method (A01), and deception law is converging on exactly this kind of claim (A08, F04).
3. **Schedule refreshes with importance weights in fixed order — never proportionally.** Proportional is the worst policy in the foundational measurement: 0.12 vs 0.62 freshness, 400 vs 4.3 days age (E01).
4. **Keep agents read-only, consent-gated and out of the steady-state loop.** Live-web success ≈30% (D03), Completion-under-Policy under two-thirds (D04), targeted prompt-injection success 47.7% against a strong model with tool filtering cutting it to ~7.5% (D05), and agent verification costs roughly 1,000× the feed path `[EST]` (§8.3).
5. **Ship base rates with alerts, especially in India.** The only causal evidence of a job portal *harming* users is Indian: −9.2pp employment from expectation inflation, halved by sending real information about the jobs on offer (B07).

### Two things the evidence overturns

1. **"Agents already succeed on 55–60% of real web tasks."** Mind2Web is an offline dataset on static snapshots whose published task success is **2.0%** (D02); on 300 live sites with human grading, most frontier agents reach **~30%** (D03). Re-plan the agent roadmap around 30%, and treat the 59.1% WebVoyager figure as applying only to a small, known site list (D01).
2. **"About one in five postings is a ghost job."** Ng's 21% is computed over Glassdoor *interview reviews*, not postings, and a keyword baseline on the same data gives 1.3–1.6% (A01); the 55%/1.63× preprint rests on 160 classifiable postings from a US software-heavy convenience sample (A03); the official position is that no statistics exist (A02). Keep the user pain; delete the number from every artefact.

*Honourable mention, half-overturned:* "breadth wins, +44% interviews" is real but **p<0.10 on ~300 people**, and the authors themselves show the job-finding effect would need 3,794 per arm (C01). It is a promising mechanism with a strong scale-up (C02), not a settled fact.

### Three things to test first

1. **Experiment 1 — does verification beat age?** Within-student, listing-level randomisation of "seen live at *HH:MM* on *source*" vs age only; primary = application-start rate (MDE ≈ 4.5pp); secondary = wasted-application rate. If verification adds nothing over the age label students already use (A10), the core differentiator is not worth its latency.
2. **Experiment 3 — will students actually pay?** Real-money paywall at two randomised price points after a 3-week trial (MDE ≈ 15pp between cells), with the hypothetical question asked first so Signal can estimate its own hypothetical-bias factor against the published median of 1.35 (H01). Nothing in this review establishes willingness to pay for job-search tooling — it is the single biggest unknown.
3. **Source-coverage probe before anything else (two weeks, no users).** Pull ~300 ATS boards plus Unstop and PMIS; measure what share of listings that 20 students actually saved last month is covered, and the per-source dead-on-open rate. If coverage is under ~40% (idea 1's falsification threshold), the honest-and-small strategy fails on relevance and the company needs partnerships before product.

---

### Provenance and limits of this review

- 51 sources, consulted on 2026-10-12. Every link was retrieved in this session except those explicitly marked `[UNVERIFIED]` (LinkedIn robots.txt, Hensvik et al. full text, Belot et al. 2025 full text, Schilke & Reimann 2025), those marked `[SECONDARY]` (Mind2Web results table, hiQ and Bright Data court opinions), and the retrieval failures logged in §10.3.
- Mix (from the CSV's `evidence_type` column): 21 peer-reviewed journal/conference papers + 1 peer-edited law review; 10 preprints, working papers or author-page summaries; 4 vendor publications; 1 industry-association survey; 6 government or primary-law documents; 5 product-documentation / access-policy files; 2 law-firm secondary analyses; 1 blocked source recorded as a negative result.
- Geographic coverage is honest about its own gap: of the behavioural causal evidence, **one** study is Indian (B07). US, UK, France, Germany, Sweden and Switzerland supply the rest. **No finding in this document should be assumed to transfer to Indian students without local measurement.**
- Not done, and flagged rather than hidden: GDPR analysis (§9.4), the ESA statutory text behind Ontario's vacancy/AI duties (§9.2), Indian platform terms of service, and any measurement of how quickly saved listings die (§11.1).
