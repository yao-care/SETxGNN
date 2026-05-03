---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 5
---

# Guaifenesin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill for context — this is a TxGNN report generation task for the Taiwan (TW) pipeline. Proceeding to generate the report from the Evidence Pack.

---

# Guaifenesin: From Expectorant Use to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is a well-established expectorant and mucolytic agent, widely used to relieve respiratory congestion by reducing mucus viscosity and promoting airway clearance.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease** (encompassing conditions such as chronic rhinitis and sinusitis),
with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant / mucolytic — no Taiwan regulatory authorization on record |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. However, based on established pharmacological knowledge and the supporting repurposing rationale: Guaifenesin acts as a mucolytic agent by increasing the water content of airway mucosal secretions, thereby reducing mucus viscosity and enhancing the efficiency of nasal ciliary clearance — a mechanism long recognized in respiratory therapeutics.

Nasal cavity disease — including chronic rhinitis and sinusitis — shares a core pathological feature: mucus stagnation due to impaired mucociliary clearance. Because Guaifenesin directly addresses this bottleneck by thinning secretions and facilitating drainage, the mechanistic link between the drug's known action and this new indication is biologically plausible and clinically rational.

A completed Phase 2 randomized controlled trial in pediatric chronic rhinitis (NCT01364467) provides the most direct clinical evidence available, with supporting literature documenting guaifenesin use in allergic rhinitis and sinusitis management. Together, these strands of evidence — plus TxGNN's high confidence score of 99.98% — make this among the more grounded predictions in this candidate set.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | 14-day randomized, placebo-controlled, parallel-group pilot trial of oral guaifenesin for chronic rhinitis (CRS) in children aged 7–18; assessed nasal symptom relief via the SN-5 survey compared to nasal airway volume and biophysical properties of nasal secretions. Sample size limits statistical power; a confirmatory large-scale RCT is needed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review / Clinical Commentary | Logopedics, Phoniatrics, Vocology | Decongestants combined with guaifenesin identified as useful for managing allergic nasal symptoms in voice users; discusses mucosal involvement in chronic laryngitis and rhinitis with specific reference to guaifenesin's role in reducing secretion thickness |
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review / Expert Opinion | American Journal of Rhinology | Describes management of chronic sinusitis in adult cystic fibrosis patients; contextualizes mucolytic strategies — including guaifenesin-relevant approaches — in the setting of nasal cavity disease with severe secretion impairment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT directly evaluating oral guaifenesin in pediatric chronic rhinitis provides meaningful clinical support for the nasal cavity disease indication, and the mechanistic rationale — mucolytic action targeting mucus stagnation central to nasal cavity pathology — is well-grounded. This justifies moving forward under close monitoring rather than holding.

**To proceed, the following is needed:**
- **MOA data from DrugBank**: Formal mechanism of action documentation is currently missing (Data Gap DG002); required for mechanistic analysis
- **Taiwan package insert safety information**: Warnings and contraindications are unavailable (Data Gap DG001); must be resolved before clinical safety screening (Stage S1)
- **Larger-scale confirmatory RCT**: The sole supporting trial is a pilot (n=30); a powered Phase 2/3 study in adult and pediatric populations is needed to establish efficacy
- **Adult population data**: Existing evidence is exclusively pediatric (ages 7–18); adult applicability needs dedicated investigation
- **Pharmacovigilance plan**: Define monitoring strategy for relevant special populations (pediatric dosing, elderly, pregnancy)
- **Dosage form and route review**: Confirm that available oral formulations are appropriate for the target nasal cavity disease indication and patient population
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

