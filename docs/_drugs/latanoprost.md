---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Ocular Hypertension / Open-Angle Glaucoma — No Repurposing Prediction Available

## One-Sentence Summary

Latanoprost is a prostaglandin F2α analogue widely used as an ophthalmic solution to reduce intraocular pressure in open-angle glaucoma and ocular hypertension.
The current Evidence Pack contains **no TxGNN-generated repurposing predictions** for this compound, and critical regulatory and safety data are absent from the Taiwan MPA database, making a full repurposing evaluation impossible at this stage.
Without predicted indications, clinical trial evidence, or literature linkage to a new disease target, this candidate cannot advance through the standard evaluation pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ocular hypertension; open-angle glaucoma (ophthalmic use) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Sweden Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan MPA package insert data was queried (2026-03-29) with one record located, but warning/contraindication fields were not successfully extracted into this Evidence Pack. Drug interaction data returned no results. Both items require manual resolution before any safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Latanoprost (DB00654) is critically incomplete — the TxGNN model returned zero predicted indications, and both Taiwan MPA safety data and mechanism of action data are missing, making it impossible to conduct even a preliminary repurposing feasibility assessment.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for DB00654 to generate candidate repurposing indications; verify that the knowledge graph node for Latanoprost is correctly linked and that the prediction run did not silently fail
- **Extract MOA from DrugBank API** (DG002 — High severity): Latanoprost is a prostaglandin F2α receptor agonist; mechanistic data is essential for evaluating cross-indication plausibility
- **Parse Taiwan TFDA package insert PDF** (DG001 — Blocking severity): Retrieve warnings, contraindications, and special population guidance to enable S1 safety screening
- **Verify drug interaction data source**: DDI query returned no results; confirm whether this reflects a true absence of known interactions or a query failure
- **Confirm Sweden/EU marketing status** via EMA records: Taiwan MPA shows zero authorizations; independent EU-market verification may yield different regulatory standing for Xalatan or generic equivalents
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

