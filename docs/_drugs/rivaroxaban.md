---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using `txgnn-pipeline` skill for context, then generating the evaluation report from the Evidence Pack.

---

# Rivaroxaban: From Anticoagulation to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct oral anticoagulant (Factor Xa inhibitor) used globally for prevention and treatment of venous thromboembolism (VTE) and stroke prevention in non-valvular atrial fibrillation, though it currently holds no MPA authorization in Sweden.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **4 publications** currently supporting this direction — placing the evidence at level **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No MPA authorization on record; Rivaroxaban is globally established as a Factor Xa inhibitor for VTE prevention/treatment and stroke prevention in non-valvular atrial fibrillation |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Rivaroxaban is a direct Factor Xa inhibitor — it selectively blocks the active site of Factor Xa, thereby preventing the conversion of prothrombin to thrombin and suppressing clot formation. Its proven efficacy in thromboembolic conditions is well-established in global clinical practice, though it has not been registered in Sweden to date.

Rheumatoid arthritis (RA) is driven by chronic systemic inflammation, which creates a persistent hypercoagulable state: RA patients exhibit elevated thrombin generation, increased Factor Xa activity, and a significantly higher incidence of VTE compared to the general population. This is the core biological bridge that the TxGNN knowledge graph appears to have captured — Rivaroxaban already treats the *consequence* (thrombosis) of the inflammatory state that RA generates, and the model may be inferring a more direct anti-inflammatory role.

A speculative secondary mechanism involves PAR-2 (protease-activated receptor 2): Factor Xa can activate PAR-2 on synovial fibroblasts, potentially modulating pro-inflammatory signalling cascades within the joint. However, this pathway lacks direct preclinical or clinical validation in RA, and must be considered highly theoretical. The available literature does not study Rivaroxaban *as a treatment for RA itself* — it reflects use of Rivaroxaban in RA patients for comorbid anticoagulation. As a result, this prediction is most likely a knowledge graph artefact of the RA–hypercoagulability–anticoagulant association, rather than a genuine therapeutic repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Lab/Clinical Study | La Revue de medecine interne | Thrombin generation assay (TGA) used to evaluate hypercoagulable states in autoimmune diseases including antiphospholipid syndrome; supports biological plausibility that coagulation dysregulation is clinically relevant in autoimmune conditions — indirect mechanistic background only |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Comprehensive review of VTE diagnosis and treatment (DVT incidence 88–112 per 100,000 person-years); general anticoagulation background with no RA-specific content |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Observational/Adherence Study | PloS one | Compares medication adherence to rivaroxaban vs apixaban in non-valvular AF; not specific to RA; demonstrates real-world rivaroxaban utilisation patterns |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | 88-year-old RA patient on oral steroids experiencing multiple thromboembolic events (lower limb + cerebral) despite anticoagulation for AF; illustrates the RA–thromboembolism comorbidity intersection but does not represent repurposing of Rivaroxaban for RA treatment |

---

## Sweden Market Information

Rivaroxaban has not received MPA authorization in Sweden. No product licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Rivaroxaban in rheumatoid arthritis stands at L5 — the prediction is driven entirely by the TxGNN model with no disease-specific clinical trials and no literature directly studying Rivaroxaban as a therapeutic agent for RA. The available publications reflect comorbid anticoagulation use in RA patients, not a repurposing signal.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro or animal model studies demonstrating anti-inflammatory effects of Factor Xa inhibition or PAR-2 modulation specifically in RA-relevant models (e.g., CIA mouse model, synovial fibroblast assays)
- **Mechanistic data**: Formal investigation of whether PAR-2–mediated signalling by Factor Xa has measurable impact on synovitis or joint destruction
- **MOA documentation**: Retrieve complete Rivaroxaban MOA from DrugBank (Data Gap DG002)
- **Safety baseline**: Download and parse the package insert for key warnings and contraindications (Data Gap DG001) before any feasibility assessment can proceed

---

> **Note on Multi-Indication Evaluation (TW-DB06228-multi):**
> This report covers the top-ranked TxGNN prediction (Rheumatoid Arthritis, rank 1). Among the four predicted indications, the **HIV Infectious Disease** indication (rank 3, score 99.17%) carries materially stronger clinical evidence — evidence level **L3** — with 1 completed Phase 2 PK/safety trial ([NCT00786422](https://clinicaltrials.gov/study/NCT00786422), n=25) and 8 publications covering DOAC safety in HIV patients on antiretroviral therapy. That indication's core repurposing framing is "safe anticoagulation strategy for HIV patients with comorbid thrombosis," not treatment of HIV itself, and warrants a separate dedicated report. The **Gout** (rank 2) and **Brachydactyly-Syndactyly Syndrome** (rank 4) predictions are both L5 with no mechanistic basis and are recommended as Hold without further review.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

