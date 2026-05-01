---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 4
---

# Naproxen
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

# Naproxen: Drug Repurposing Evaluation — Insufficient Data to Generate Prediction

## One-Sentence Summary

Naproxen (DrugBank: DB00788) is a widely recognized analgesic and anti-inflammatory agent with no current Taiwan regulatory registration.
No TxGNN drug repurposing predictions were generated for this candidate, and mechanism of action data was not retrieved from the data pipeline.
A complete repurposing assessment cannot be produced at this time; this report documents the current data status and required remediation steps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Prediction pipeline output not available |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction Is Available

The TxGNN prediction pipeline returned an empty result set for Naproxen. This can occur for several reasons:

1. **Knowledge graph coverage**: Naproxen may not be included in the current version of the TxGNN knowledge graph, or its drug node may be missing required feature embeddings.
2. **Original indication data missing**: The `original_indications` field is empty, which removes the anchor concept used by the model to reason about mechanistic similarity.
3. **MOA data gap**: Without mechanism of action data, the model cannot generate high-confidence predictions based on target pathway overlap.

Until these upstream data gaps are resolved, no prediction-driven repurposing evaluation can be completed.

---

## Taiwan Market Information

Naproxen has no approved drug registrations in Taiwan. No license records were returned from the TFDA query.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction pipeline produced no output for Naproxen, and all three required data layers — original indications, mechanism of action, and TxGNN predictions — are currently missing. There is no evidence base on which to proceed with a repurposing recommendation.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve Taiwan package insert (TFDA 仿單) to obtain approved indications, key warnings, and contraindications — download PDF from TFDA official website and parse
- **[High]** Query DrugBank API for mechanism of action (MOA), pharmacological class, and target data for DB00788
- **[Required]** Re-run the TxGNN prediction pipeline after populating missing drug node features
- **[Required]** Confirm whether Naproxen is included in the current knowledge graph version; if absent, add drug node with appropriate feature embeddings
- **[Optional]** Cross-reference with international registrations (FDA, EMA) to obtain original approved indication text as a fallback data source
---

