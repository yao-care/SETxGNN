---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: Repurposing Assessment — Insufficient Data to Proceed

## One-Sentence Summary

Lorazepam (DB00186) is a well-known benzodiazepine commonly used for anxiety disorders and sedation.
However, **no TxGNN-predicted new indications** are present in this Evidence Pack, and key data items — including mechanism of action, package insert warnings, and approved indications — are either missing or unresolved.
This report reflects the current data status and outlines what must be collected before a repurposing evaluation can be completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | None — TxGNN prediction output is absent |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — prediction output not yet available) |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indication is present in this Evidence Pack (`predicted_indications` is empty), so a mechanistic rationale for a specific new use cannot be constructed at this stage.

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, lorazepam belongs to the benzodiazepine class, acting at GABA-A receptors to produce anxiolytic, sedative, anticonvulsant, and muscle-relaxant effects. Its established clinical roles include anxiety disorders, acute seizure management, procedural sedation, and alcohol withdrawal — but none of these original indications have been formally recorded in the submitted Evidence Pack.

Once the TxGNN prediction pipeline produces a candidate indication and the MOA data gap (DG002) is resolved via DrugBank, this section should be updated to articulate the mechanistic bridge between lorazepam's known neurological activity and the proposed new indication.

---

## Taiwan Market Information

No marketing authorizations for lorazepam are registered in the Taiwan regulatory database queried on 2026-03-29. No product table can be generated.

> Note: The absence of Taiwan registrations is unexpected for a widely used benzodiazepine. It is recommended to verify the query spelling and scope, and to check whether lorazepam is regulated under a controlled substance registry separate from the standard drug license database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The TFDA package insert query returned a successful result (query log ID 4), but the content has not been parsed into structured fields. Resolving data gap DG001 (TFDA 仿單警語/禁忌) is classified as **Blocking** for safety pre-screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction output is absent, and two critical data gaps — MOA (High severity) and TFDA package insert warnings (Blocking severity) — remain unresolved, making it impossible to conduct even a preliminary repurposing safety screen.

**To proceed, the following is needed:**

- **\[Blocking\] Resolve DG001** — Download and parse the TFDA package insert PDF to extract warnings, contraindications, and special population precautions; this unlocks the S1 safety pre-screening step
- **\[High\] Resolve DG002** — Query DrugBank API for lorazepam's mechanism of action (DB00186) to enable mechanistic bridge analysis
- **\[Required\] Re-run TxGNN prediction pipeline** — Confirm that lorazepam (DB00186) was included in the prediction run and retrieve the `predicted_indications` output; if the model returned no candidates, document the reason (e.g., below threshold, excluded node)
- **\[Recommended\] Verify Taiwan market status** — Confirm whether lorazepam is absent from Taiwan drug licenses due to a query issue or whether it is genuinely not marketed domestically, possibly registered under a controlled substance framework
- **\[Recommended\] Populate original indications** — Record the established clinical uses (anxiety, seizure, sedation) in the `original_indications` field to enable proper indication-to-indication comparability analysis once a prediction target is available
---

