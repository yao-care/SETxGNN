---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Mupirocin: Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Mupirocin (DB00410) is a drug currently without registered approvals in Taiwan, and the TxGNN model returned **no predicted new indications** for this candidate in the current pipeline run. Due to missing mechanism of action data, absent original indication records, and no TxGNN output, a complete repurposing evaluation cannot be completed at this stage — a **Hold** decision is recommended until data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction stage not reached) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No prediction is available to evaluate at this time.

Currently, detailed mechanism of action data is not available (Data Gap DG002), and the TxGNN pipeline returned an empty `predicted_indications` array for Mupirocin. Without a scored disease target, it is not possible to assess mechanistic plausibility or biological rationale for any new indication.

Additionally, the original indication field is empty in the current Evidence Pack, which prevents establishing a disease-space relationship between Mupirocin's approved use and any candidate repurposing target.

To proceed to this section, the following must first be resolved: (1) retrieve MOA from DrugBank API, and (2) re-run TxGNN with a valid input graph node for DB00410.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — TxGNN returned no predicted indications, so no disease target is available to query against.

---

## Literature Evidence

Currently no related literature available — no predicted indication target is present to anchor a literature search.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, and drug-drug interactions) returned no data in the current Evidence Pack. The TFDA package insert query (Query Log ID 4) was recorded as successful with 1 result, but the structured data was not parsed into the Evidence Pack. The raw insert content should be extracted and loaded before safety evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Mupirocin (DB00410) is missing the two inputs required for a repurposing evaluation — TxGNN produced no scored indication predictions, and mechanism of action data is absent — making it impossible to assess either biological plausibility or clinical evidence strength.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Extract and parse TFDA package insert (already retrieved, not yet structured) to obtain approved indications, key warnings, and contraindications
- **[DG002 — High]** Query DrugBank API for Mupirocin's mechanism of action (pharmacodynamics, drug class, targets)
- **[Pipeline]** Investigate why TxGNN returned an empty `predicted_indications` array — verify that DB00410 / Mupirocin is present as a node in the knowledge graph and re-run prediction
- **[Regulatory]** Confirm whether Taiwan non-registration reflects a regulatory gap (drug exists but not filed) or a data absence — cross-check with MPA/EMA registrations to determine if a bridging registration pathway is relevant
- Once the above are resolved, re-generate the Evidence Pack and re-run this evaluation
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

