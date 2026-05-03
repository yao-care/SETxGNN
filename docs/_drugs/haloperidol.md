---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Schizophrenia / Psychosis to Manic Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic and potent D2/D3 dopamine receptor antagonist, historically established for the treatment of schizophrenia and acute psychosis.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **9 clinical trials** and **20 publications** currently supporting this direction.
This is the only actionable signal among the 10 predicted indications evaluated: haloperidol has served as the standard active comparator in multiple Phase 3 RCTs for acute mania, producing an exceptionally strong L1 evidence base — though it is not currently registered locally.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia and acute psychotic disorders |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Sweden Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Haloperidol is a butyrophenone-class antipsychotic with extremely high affinity for dopamine D2 receptors (Ki ≈ 0.7 nM). Its core mechanism — potent D2/D3 receptor antagonism — rapidly suppresses dopaminergic overactivity throughout the mesolimbic and mesocortical circuits. This was originally harnessed to control psychotic symptoms in schizophrenia, where excess dopamine signalling underlies hallucinations and disorganised thinking.

The mechanistic bridge to bipolar mania is well-established: the dopamine dysregulation hypothesis of mania posits that acute manic episodes are driven by pathological hyperdopaminergia in reward and arousal circuits — precisely the same target pathways blocked by haloperidol. This pharmacological overlap explains decades of clinical use for manic episode management. Its efficacy is so well-accepted that multiple Phase 3 RCTs selected haloperidol as the standard active comparator arm when validating newer atypical antipsychotics (risperidone, olanzapine, aripiprazole) for acute mania.

Among the 10 TxGNN-predicted indications reviewed in this report, manic bipolar affective disorder is ranked 10th by raw TxGNN score (99.83%) but stands alone at Evidence Level L1 with a "Proceed with Guardrails" recommendation. The remaining nine predictions (ranks 1–9) are all L5/Hold with no supporting clinical evidence, several carrying mechanistic rationales that are explicitly counter-therapeutic for haloperidol. The clinically prioritised finding is therefore clear: formal consideration of local indication expansion for manic bipolar affective disorder is warranted.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs placebo vs **haloperidol** in acute Bipolar I mania over 12 weeks; haloperidol as direct active comparator, providing primary efficacy and safety data |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and **haloperidol**-controlled double-blind trial of olanzapine in manic or mixed episodes of Bipolar I disorder; haloperidol arm delivers direct comparative efficacy data |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs placebo vs **haloperidol** as add-on to mood stabilisers in bipolar manic phase; haloperidol as active comparator for combination therapy |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs placebo for acute Bipolar I mania over 12 weeks; large trial with haloperidol as indirect reference comparator |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic adherence programme for chronic psychotic disorders in Tanzania; haloperidol-relevant but very small sample limits generalisability |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate + amisulpride vs valproate + **haloperidol** (5–15 mg/day) for Bipolar I manic episodes over 3 months; evaluates combination safety and efficacy |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A (Observational) | Recruiting | 200 | Maternal psychiatric course and infant development in pregnant individuals with severe mental illness taking antipsychotics; not an efficacy trial — safety monitoring context only |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs conventional antipsychotics in acute mania in Sweden; terminated early — sample too small (n=11) for meaningful conclusions |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient supplement as adjunctive treatment in bipolar disorder; not directly haloperidol-related |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review + Network Meta-analysis | Molecular Psychiatry | Comprehensive NMA of pharmacological treatments for acute bipolar mania across multiple RCTs; provides comparative efficacy, acceptability, tolerability, and safety rankings including haloperidol |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Comparative Analysis | BMJ Mental Health | Comparison of antipsychotic dose equivalents between acute mania and schizophrenia; directly relevant to haloperidol dosing optimisation in manic episodes |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review | Acta Psychiatrica Scandinavica | Evidence-based review of treatment options for bipolar mania; discusses choice of antipsychotics including haloperidol with clinical management guidance |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Evidence-based Review | CNS Neuroscience & Therapeutics | Treatment of refractory bipolar mania; explicitly recommends adding haloperidol to lithium, valproate, or carbamazepine in partial responders |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Olanzapine vs placebo vs **haloperidol** in Japanese Bipolar I patients with manic/mixed episode; provides direct haloperidol efficacy data in an Asian population |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | Journal of Clinical Psychopharmacology | Antipsychotic-induced extrapyramidal side effects (EPS) in bipolar disorder vs schizophrenia; documents haloperidol's higher EPS burden vs atypical agents — a key safety guardrail |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review + Meta-analysis | Human Psychopharmacology | Pharmacological treatment of acute agitation in psychotic and bipolar disorder; supports haloperidol for rapid agitation control in manic episodes |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | Journal of Clinical Psychiatry | Double-blind controlled trial comparing clonazepam vs **haloperidol** in acute mania; early foundational direct evidence for haloperidol's anti-manic efficacy |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Review | BMJ Clinical Evidence | Comprehensive overview of bipolar disorder management; documents the established clinical role of antipsychotics including haloperidol in manic episodes |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | HTA / Systematic Review | Health Technology Assessment | Rapid systematic review and health economic evaluation of newer drugs for bipolar mania; used haloperidol as the reference standard comparator — confirming its benchmark status |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Haloperidol's potent D2/D3 dopamine receptor antagonism directly targets the core pathophysiology of acute mania, and its efficacy is substantiated by at least three completed Phase 3 RCTs in which it served as the active comparator (NCT00253162, n=439; NCT00129220, n=224; NCT00253149, n=158) — satisfying the L1 threshold. While not currently registered locally, the global evidence base is mature and the mechanistic rationale is unambiguous. The primary guardrails relate to the known safety profile of first-generation antipsychotics rather than any uncertainty about efficacy.

**To proceed, the following is needed:**
- Obtain and review the complete local package insert to document contraindications, key warnings, and special population considerations (pregnancy, elderly, QTc prolongation)
- Retrieve formal mechanism of action documentation from DrugBank (MOA data currently unavailable — remediation via DrugBank API query)
- Develop a safety monitoring plan that explicitly addresses the elevated extrapyramidal side effect (EPS) and tardive dyskinesia risk associated with haloperidol, particularly for maintenance use in bipolar patients
- Confirm available formulation routes (oral tablet/liquid, short-acting injectable, long-acting decanoate) and their suitability for acute vs maintenance management of manic bipolar disorder
- Initiate regulatory pathway review for local indication expansion application
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

