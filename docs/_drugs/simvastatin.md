---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Using `txgnn-pipeline` skill noted; this is a report generation task within that pipeline. Now generating the report from the Evidence Pack.

---

# Simvastatin: From Hyperlipidemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor belonging to the statin class, widely used globally for the treatment of hyperlipidemia and cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**,
with **19 clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperlipidemia / Dyslipidemia (global approvals; no TFDA registration on record) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Taiwan (TFDA) Market Status | ✗ Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Simvastatin works by competitively inhibiting HMG-CoA reductase — the enzyme catalyzing the rate-limiting step in hepatic cholesterol biosynthesis. By blocking this pathway, the drug reduces endogenous cholesterol production and simultaneously triggers compensatory upregulation of LDL receptors on hepatocyte surfaces, dramatically increasing clearance of LDL-C from the bloodstream. This dual mechanism directly addresses the core pathophysiology of familial hypercholesterolemia, where mutations in *LDLR*, *APOB*, or *PCSK9* impair normal LDL receptor function and allow LDL-C to accumulate in circulation from birth.

Familial hypercholesterolemia is characterized by lifelong markedly elevated LDL-C, accelerating atherosclerosis and reducing life expectancy by 15–30 years if untreated. Because FH patients retain at least partially functional LDL receptors (in the heterozygous form), statins can upregulate the remaining receptor pool and achieve meaningful LDL-C reductions of 30–55% depending on dose. In homozygous FH, where receptor function is severely diminished, simvastatin is typically used in combination with ezetimibe or PCSK9 inhibitors to achieve clinically meaningful lowering.

The evidence base is exceptionally strong. The landmark ENHANCE trial (NCT00552097, n=720) directly compared high-dose simvastatin monotherapy against simvastatin plus ezetimibe in heterozygous FH patients, generating pivotal data on both LDL-C lowering and carotid intima-media thickness progression. Multiple Phase 3 RCTs in both adult and pediatric FH populations — spanning heterozygous and homozygous subtypes — confirm consistent efficacy. Most compellingly, the 2026 ACC/AHA Guideline on the Management of Dyslipidemia formally endorses statins, including simvastatin, as core first-line therapy for FH, placing this candidate at the highest available evidence tier (L1).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE Trial: high-dose simvastatin alone vs simvastatin + ezetimibe in heterozygous FH; primary endpoint was carotid IMT progression — the landmark direct simvastatin-in-FH RCT |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg co-administered with atorvastatin or simvastatin in homozygous FH; evaluated efficacy and safety of the combination over 12 weeks |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label extension of ezetimibe add-on to atorvastatin or simvastatin in homozygous FH; assessed long-term safety and tolerability of the regimen |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2341 | Long-term alirocumab safety study in high-CV-risk FH patients; simvastatin permitted as background therapy, contributing large-scale long-term statin safety data |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab vs placebo in heterozygous FH inadequately controlled on lipid-modifying therapy; simvastatin as permitted background treatment, confirming statin standard-of-care status |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Open-label extension assessing long-term alirocumab efficacy and safety in HeFH; provides extended follow-up of outcomes with statin background therapy including simvastatin |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab (REGN727) in HeFH patients on lipid-modifying therapy including simvastatin; multinational Phase 3 RCT confirming statin inadequacy in high-risk FH and need for add-on therapy |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | 6-week head-to-head comparison of rosuvastatin vs simvastatin in Fredrickson Type IIa & IIb dyslipidemia including HeFH; assessed renal safety profile of both statins |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe co-administered with simvastatin in adolescents aged 10–17 years with heterozygous FH; multicenter Phase 3 RCT evaluating pediatric efficacy and safety |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam HCl in pediatric HeFH patients (ages 10–17) on stable statin monotherapy including simvastatin; evaluated add-on bile acid sequestrant lipid-lowering effect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Clinical Practice Guideline | Circulation | 2026 ACC/AHA Dyslipidemia Guideline (replaces 2018 guideline): statins including simvastatin remain core first-line therapy for FH; most current authoritative recommendation |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane Systematic Review | Cochrane Database Syst Rev | Statins in children with FH (2019 update): comprehensive meta-analysis confirming LDL-C lowering efficacy and acceptable safety of statin therapy including simvastatin in pediatric FH patients |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | Primary ENHANCE trial publication: simvastatin + ezetimibe vs simvastatin alone in HeFH — ezetimibe added incremental LDL-C reduction; no significant difference in carotid IMT progression |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | RCT | J Am Coll Cardiol | Long-term ezetimibe/simvastatin coadministration in adolescents with HeFH: effective and sustained LDL-C reduction with acceptable safety profile across 48 weeks |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Study | J Am Coll Cardiol | Statins in heterozygous FH: quantified statin-induced reduction in coronary artery disease events and all-cause mortality, providing real-world effectiveness evidence |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | RCT | Int Angiology | Long-term ezetimibe/simvastatin therapy in heterozygous FH: greater LDL-C reduction and regression of carotid IMT compared to simvastatin alone over extended follow-up |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Safety | Comprehensive benefit-risk assessment of simvastatin specifically in FH: supports long-term use; life expectancy in untreated FH reduced 15–30 years, reversed with adequate statin therapy |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Practice Guideline | Endocr Pract | AACE/ACE 2017 Dyslipidemia Management Guidelines: endorses statin therapy as first-line treatment for FH; provides risk stratification framework for LDL-C targets |
| [2405804](https://pubmed.ncbi.nlm.nih.gov/2405804/) | 1990 | Multicenter RCT | Arch Intern Med | Simvastatin vs cholestyramine in familial and nonfamilial hypercholesterolemia (n=251): simvastatin 20–40 mg/day reduced LDL-C by 32–40%, establishing foundational efficacy data in FH |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Cochrane Systematic Review | Cochrane Database Syst Rev | Statins in children with FH (2017 Cochrane Review): systematic review supporting statin use in pediatric FH population, including simvastatin, with favorable short-to-medium term safety profile |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan (TFDA) package insert data and DrugBank contraindication/warning fields were not available in this evidence pack. Retrieval from the TFDA official website is recommended before clinical implementation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — anchored by the ENHANCE trial (n=720) and confirmed across adult, pediatric, heterozygous, and homozygous FH subpopulations — along with endorsement in the 2026 ACC/AHA Dyslipidemia Guideline and two Cochrane systematic reviews, establish simvastatin as a standard-of-care agent for familial hypercholesterolemia at Evidence Level L1. The prediction is not truly a novel repurposing; rather, it reflects TxGNN accurately identifying an established indication that lacks formal TFDA regulatory registration in Taiwan.

**To proceed, the following is needed:**
- **TFDA package insert retrieval**: Download and parse the official insert PDF to obtain Taiwan-specific warnings, contraindications, dosing, and precautions (currently blocking safety evaluation)
- **Drug-drug interaction (DDI) assessment**: Re-query DDI database; simvastatin has known clinically significant interactions (e.g., with CYP3A4 inhibitors, fibrates, niacin) that must be documented
- **Taiwan regulatory pathway review**: Since TFDA registration is absent (0 licenses), confirm whether a formal regulatory filing is required for clinical use in Taiwan, or whether off-label prescribing protocols apply
- **MOA documentation**: Obtain complete DrugBank mechanism-of-action record for regulatory submission completeness
---

