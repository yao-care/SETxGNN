---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# APIXABAN: Drug Repurposing Evaluation Report

## One-Sentence Summary

Apixaban (DrugBank: DB06605) is a well-known direct oral anticoagulant (Factor Xa inhibitor), marketed globally under the brand name Eliquis. The TxGNN model has **not yet generated any predicted new indications** for this compound, and the evidence pack contains **significant data gaps** in mechanism of action, safety warnings, and regulatory information for Taiwan.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (known globally for atrial fibrillation stroke prevention, VTE treatment/prevention) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies in this pack) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

No TxGNN prediction has been generated for Apixaban at this time, so a mechanistic plausibility assessment cannot be performed.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Apixaban is a selective, reversible inhibitor of coagulation Factor Xa (FXa). By inhibiting FXa, it decreases thrombin generation and thrombus development. It is widely approved internationally for the prevention of stroke and systemic embolism in patients with non-valvular atrial fibrillation, as well as for the treatment and prevention of deep vein thrombosis (DVT) and pulmonary embolism (PE).

Until the TxGNN model generates predicted indications for Apixaban, no drug repurposing assessment can proceed beyond this preliminary data inventory stage.

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication has been identified by TxGNN for evaluation.

## Literature Evidence

Currently no related literature available — no predicted indication has been identified by TxGNN for evaluation.

## Taiwan Market Information

Apixaban currently holds **no TFDA marketing authorizations** in Taiwan (market status: 未上市). No license records were found in the regulatory query conducted on 2026-03-29.

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug-drug interactions) returned as data gaps or not found in the current evidence pack.

## Data Gaps Summary

The following critical data gaps have been identified and must be resolved before any repurposing evaluation can proceed:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

Additionally:
- **Predicted Indications**: The `predicted_indications` array is empty — TxGNN predictions have not been generated or mapped for this compound.
- **Original Indications**: Not populated in the evidence pack despite Apixaban being a well-characterized drug globally.
- **DDI Data**: Query returned `not_found` with zero interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications exist for Apixaban in this evidence pack, making it impossible to evaluate any repurposing opportunity. Furthermore, there are two unresolved data gaps (one at Blocking severity) that prevent even a baseline safety assessment.

**To proceed, the following is needed:**
- **Run TxGNN prediction** for Apixaban (DB06605) to generate candidate new indications
- **Resolve DG001 (Blocking):** Obtain and parse TFDA package insert to extract warnings and contraindications
- **Resolve DG002 (High):** Query DrugBank API for detailed mechanism of action data
- **Populate original indications** from DrugBank or TFDA approved indication text
- **Verify Taiwan market status** — Apixaban (Eliquis) is widely available internationally; confirm whether it truly has no TFDA authorization or if the query needs refinement
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

