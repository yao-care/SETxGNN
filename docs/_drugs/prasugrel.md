---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

---

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a potent antiplatelet drug belonging to the thienopyridine class, globally established for reducing thrombotic cardiovascular events in patients with acute coronary syndrome (ACS) undergoing percutaneous coronary intervention (PCI).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of 99.88%.
However, evidence retrieval found **no directly relevant clinical trials or published literature** for this indication — the prediction currently stands at the model-only level (L5) and is assessed as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Coronary Syndrome / Percutaneous Coronary Intervention (ACS/PCI) *(based on known global approval; no Taiwan license data available)* |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the current evidence dataset. Based on established pharmacological knowledge, prasugrel belongs to the thienopyridine drug class and acts as an irreversible P2Y12 ADP receptor antagonist. After oral administration, it is converted by hepatic CYP enzymes into an active thiol metabolite that covalently binds to platelet P2Y12 receptors, suppressing ADP-induced platelet aggregation more potently and consistently than clopidogrel. Its approved clinical role is in preventing stent thrombosis and reducing major adverse cardiovascular events in ACS/PCI patients.

In pulmonary arterial hypertension (PAH), activated platelets contribute to disease pathology by releasing vasoactive mediators — primarily serotonin (5-HT) and thromboxane A2 (TXA2) — which promote pulmonary vasoconstriction and drive vascular smooth muscle remodeling. P2Y12 inhibition theoretically suppresses platelet activation and downstream release of these harmful mediators, providing a plausible, if indirect, mechanistic basis for TxGNN's prediction.

That said, this rationale is entirely theoretical and has never been clinically tested. Both clinical trials and literature entries retrieved during evidence collection turned out to be false-positive database matches with no actual relevance to prasugrel or pulmonary hypertension. This prediction should be treated as a hypothesis worth future exploration, not actionable clinical evidence at this stage.

---

## Clinical Trial Evidence

> ⚠️ **No directly relevant trials were identified.** The two trials returned by the search pipeline were confirmed irrelevant upon expert review (both Grade C — false-positive database matches unrelated to either Prasugrel or Pulmonary Hypertension).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational cross-sectional study of NOAC management in elderly non-valvular atrial fibrillation patients in Spain — **not related to Prasugrel or Pulmonary Hypertension** |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective multicenter study assessing treatment eligibility criteria in cancer-associated venous thromboembolism — **not related to Prasugrel or Pulmonary Hypertension** |

---

## Literature Evidence

> ⚠️ **No directly relevant literature was identified.** The two publications retrieved do not address Prasugrel in the context of Pulmonary Hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Retrospective / Observational | Kardiologiia | ACTIVE registry analysis of cardiovascular background therapy and COVID-19 mortality risk — addresses general CV drug classes; **not specific to Prasugrel or Pulmonary Hypertension** |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Real-world Observational | Curr Med Res Opin | Factors associated with clopidogrel/prasugrel use and adherence after PCI in ACS — addresses prasugrel in its **original ACS indication only**, not Pulmonary Hypertension |

---

## Taiwan Market Information

Prasugrel is **not approved** in Taiwan. No product authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Bleeding risk (clinically important):** As a potent, irreversible P2Y12 inhibitor, prasugrel carries a well-documented risk of serious and potentially fatal bleeding in its approved indication. Any exploratory use in pulmonary hypertension patients — who frequently receive concurrent anticoagulation (e.g., warfarin, riociguat combinations) — would require careful individual risk-benefit evaluation. Detailed Taiwan TFDA label data including specific warnings and contraindications were not captured in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.88%), no clinical or preclinical studies support prasugrel use in pulmonary hypertension; all retrieved evidence was confirmed as false-positive pipeline matches, leaving the platelet-mediated PAH mechanism as an unverified biological hypothesis.

**To proceed, the following is needed:**
- Preclinical validation in animal or ex vivo PAH models to test whether P2Y12 inhibition reduces 5-HT/TXA2-driven pulmonary vasoconstriction and vascular remodeling
- Translational studies measuring platelet activation biomarkers (P-selectin, TXA2 metabolites) in PAH patient cohorts to confirm mechanistic relevance
- Safety and drug interaction assessment for prasugrel in PH patients with concurrent anticoagulant use
- Formal MOA documentation via DrugBank API to establish a complete pharmacological rationale

---

> **Note on other predicted indications:** Among the 10 TxGNN-predicted indications in this evidence pack, **migraine disorder in patients with patent foramen ovale (PFO)** (Rank 2, evidence level L4) represents the most evidence-supported repurposing direction. A retrospective review directly studying thienopyridines — including prasugrel — in PFO-associated migraine (PMID [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/)) and a P2Y12 class pilot trial with ticagrelor (PMID [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/)) together provide a mechanistically coherent, class-level indirect evidence base. This direction is recommended for a dedicated Research Question assessment as a separate report.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

