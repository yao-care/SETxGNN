---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Rifabutin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using `txgnn-pipeline` to orient context. Now generating the Rifabutin evaluation report from the Evidence Pack.

---

# Rifabutin: From MAC Bacteremia Prevention to HIV Infectious Disease

## One-Sentence Summary

Rifabutin (Mycobutin®) is a semisynthetic rifamycin-class antibiotic established internationally for preventing *Mycobacterium avium* complex (MAC) bacteremia in patients with advanced HIV disease and for treating tuberculosis in HIV/TB co-infected individuals who require concurrent antiretroviral therapy. The TxGNN model predicts it has broad utility in **HIV infectious disease** management — a finding supported by **39 clinical trials** and **20 publications** documenting its deeply integrated role across MAC prophylaxis, HIV/TB co-infection treatment, and ARV drug interaction optimisation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (not registered in Sweden); internationally established for MAC bacteremia prevention in advanced HIV disease |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Rifabutin belongs to the rifamycin antibiotic class. Its mechanism centres on inhibition of mycobacterial DNA-dependent RNA polymerase — specifically binding the β subunit (encoded by *rpoB*) — thereby blocking transcription and exerting potent bactericidal activity against *Mycobacterium avium* complex (MAC) and *Mycobacterium tuberculosis*. Crucially, compared with rifampicin, rifabutin is approximately 3–5 times weaker as a CYP3A4 inducer. This pharmacokinetic advantage is what makes it the preferred rifamycin in HIV patients: rifampicin's powerful enzyme induction causes unacceptable reductions in exposure to protease inhibitors (PIs) and many NNRTIs, effectively undermining antiretroviral therapy.

The TxGNN model's top prediction of "HIV infectious disease" reflects the well-established clinical reality that rifabutin is already a cornerstone drug within HIV patient management — not merely incidentally, but by design. Its role spans two critical domains: (1) primary prophylaxis against disseminated MAC bacteremia in patients with CD4 counts ≤200 cells/mm³, and (2) replacement of rifampicin in tuberculosis treatment regimens for HIV/TB co-infected patients receiving PI-based or NNRTI-based ART. The high TxGNN score therefore signals genuine mechanistic and epidemiological alignment rather than a speculative cross-disease leap.

Multiple completed Phase 3 trials enrolling hundreds to over a thousand participants have confirmed both prophylactic and therapeutic efficacy. Phase 2 trials in South Africa and Vietnam have extended this evidence to real-world HIV/TB co-infection settings. Phase 4 post-marketing data from Japan further confirm ongoing safety surveillance. The absence of Swedish marketing authorisation reflects a regulatory and market access gap, not a deficit in evidence — Mycobutin® holds approvals in the United States, Japan, and EU member states.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1,100 | Clarithromycin alone vs rifabutin alone vs combination for MAC bacteremia prevention in HIV patients with CD4 ≤100 cells/mm³; compared efficacy, survival, toxicity, and quality of life across three arms |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and/or rifabutin for MAC prevention combined with daily vs weekly fluconazole for deep fungal infection prevention; assessed bacterial, mycobacterial, and toxoplasma incidence |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with rifabutin 300 mg, rifabutin 450 mg, or placebo for MAC bacteremia treatment; primary endpoint was ≥2-log CFU reduction maintained at 16 weeks |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Two doses of clarithromycin combined with ethambutol and either rifabutin or clofazimine for disseminated MAC in AIDS patients; evaluated optimal multi-drug treatment regimens |
| [NCT00002343](https://clinicaltrials.gov/study/NCT00002343) | Phase 4 | Completed | 200 | PK/PD optimisation of rifabutin monotherapy vs rifabutin + ethambutol for MAC prophylaxis in AIDS patients with CD4 ≤100 cells/mm³; dose-adjusted based on serum rifabutin levels |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin as rifampicin substitute combined with ART in HIV/TB co-infected patients (South Africa); precisely characterised rifabutin PK with multiple ARV regimens to confirm therapeutic exposure |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin + ART for HIV/TB co-infection (Vietnam); confirmed PK parameters and validated rifabutin as a safe rifampicin alternative across different ART combinations |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | Pharmacokinetics of ARV and anti-TB drugs (including rifabutin) during pregnancy and postpartum in HIV/TB co-infected women; addressed a critical underserved clinical population |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | N/A | Completed | 215 | Intermittent rifabutin-based regimen for HIV-related tuberculosis; determined rates of confirmed treatment failure and relapse with isoniazid/rifamycin-susceptible HIV-TB |
| [NCT01059422](https://clinicaltrials.gov/study/NCT01059422) | Phase 4 | Completed | 10 | Raltegravir + lamivudine/abacavir FDC combined with rifabutin-based first-line TB therapy in ART-naïve HIV/TB co-infected adults; 48-week efficacy and safety data for modern integrase-based regimens |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Systematic Review | Cochrane Database Syst Rev | Rifamycins (including rifabutin) vs isoniazid for TB prevention; comparable efficacy with potentially higher treatment completion rates — supports rifabutin's role in TB prophylaxis in high-risk populations |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort / Phase 2 | J Antimicrobial Chemotherapy | Rifabutin PK and safety in TB/HIV co-infected children on LPV/r-based second-line ART; confirmed subtherapeutic exposures common; severe neutropenia identified as key treatment-limiting toxicity |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrobial Chemotherapy | Safety and efficacy of rifabutin in HIV/TB co-infected children on LPV/r-based ART; established rifabutin as the preferred rifamycin for children on PI-based ART despite limited paediatric data |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | Population PK Analysis | J Antimicrobial Chemotherapy | Pooled DDI modelling between rifabutin and multiple HIV PIs; predicted optimal rifabutin doses (often 150 mg every other day) when co-administered with ritonavir-boosted PIs |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | HIV and TB bidirectional lethal synergy reviewed; rifabutin identified as the key ARV-compatible TB drug, with its weaker CYP3A4 induction permitting concurrent use with PIs and integrase inhibitors |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK Model | Br J Clin Pharmacology | Population PK model characterising the dolutegravir–rifabutin DDI; rifabutin moderately reduces dolutegravir AUC — critical for guiding dosing in HIV/TB co-infected patients on DTG-based regimens |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | PK / Phase 1 | J Antimicrobial Chemotherapy | Short-term safety and PK of rifabutin with LPV/r in young HIV-infected children; established early dosing guidance and confirmed feasibility of rifabutin use in paediatric HIV/TB management |
| [21726477](https://pubmed.ncbi.nlm.nih.gov/21726477/) | 2009 | Review | BMJ Clinical Evidence | HIV/TB co-infection management evidence review; annual TB risk in HIV-positive individuals 5–10× higher than HIV-negative; rifabutin positioned as preferred ARV-compatible TB treatment option |
| [9459473](https://pubmed.ncbi.nlm.nih.gov/9459473/) | 1998 | Observational | JAMA | Observational data from the HIV Outpatient Study (HOPS); clarithromycin + rifabutin combination associated with possible chemoprophylaxis benefit against cryptosporidiosis — suggesting broader opportunistic infection protection |
| [20660678](https://pubmed.ncbi.nlm.nih.gov/20660678/) | 2010 | Crossover PK Study | Antimicrobial Agents Chemother | Three-way crossover study in healthy volunteers establishing that rifabutin 150 mg every other day with darunavir/ritonavir achieves adequate rifabutin exposure; practical dosing strategy for HIV/TB patients on DRV/r |

---

## Sweden Market Information

Rifabutin is currently **not marketed in Sweden** and holds no registered marketing authorisations with the Swedish Medical Products Agency (MPA). The drug is approved in other major jurisdictions — including the United States (Mycobutin®), Japan (post-marketing surveillance programme completed), and multiple EU member states — primarily for prevention of disseminated MAC disease in patients with advanced HIV infection.

Any Swedish clinical use would require exploring import authorisation, compassionate use pathways, or a formal MPA marketing authorisation application. Given existing EMA-level approvals in other EU countries, a mutual recognition or decentralised procedure may offer the most efficient regulatory route.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for rifabutin in HIV infectious disease management is among the strongest encountered in drug repurposing evaluation — multiple completed Phase 3 trials, an established international approval history, and a well-understood pharmacological rationale all converge to support an L1 evidence classification. The primary barriers are regulatory access (no Swedish MPA registration) and formal MOA documentation, not efficacy uncertainty.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate MPA import authorisation or evaluate decentralised EU marketing authorisation application leveraging existing EMA-territory approvals
- **MOA documentation**: Obtain complete DrugBank mechanistic profile (current data gap DG002) to support regulatory submissions
- **Full safety profile**: Retrieve Swedish or EMA SmPC-equivalent package insert to address safety data gaps (DG001); key known risks to document include rifabutin-associated uveitis (dose-dependent, potentiated by CYP3A4 inhibitors) and neutropenia (particularly in paediatric populations)
- **DDI mapping with modern ART**: Prioritise interaction profiling with current first-line regimens — dolutegravir-based (DTG + 2 NRTIs) and TAF-containing combinations — as these are now standard of care but underrepresented in older rifabutin trial data
- **Haematological monitoring protocol**: Establish CBC with differential monitoring schedule, especially for patients on concomitant CYP3A4 inhibitors (macrolides, azoles) where elevated rifabutin plasma levels increase myelosuppression risk
- **Ophthalmologic monitoring plan**: Formalise uveitis surveillance protocol for patients receiving rifabutin with macrolide or azole co-medication
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

