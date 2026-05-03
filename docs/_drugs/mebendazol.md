---
layout: default
title: Mebendazol
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 0
---

# Mebendazol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# MEBENDAZOL: Evaluation Hold — Critical Data Gaps Prevent Full Assessment

## One-Sentence Summary

MEBENDAZOL (mebendazole) is a well-established antiparasitic agent whose original indications and repurposing data could not be retrieved for this assessment.
The TxGNN pipeline returned **no predicted indications** for this compound, and two critical data gaps — TFDA package insert warnings (Blocking severity) and mechanism of action (High severity) — remain unresolved.
A full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data pack |
| Predicted New Indication | No prediction returned |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions; model output absent) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The query log records a successful TFDA package insert retrieval (result\_count: 1) and a successful DrugBank lookup (result\_count: 1), yet neither safety warnings nor mechanism of action were populated in the Evidence Pack. This suggests a downstream extraction or mapping failure in the pipeline, rather than a true absence of source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications were returned, and both blocking and high-severity data gaps remain open; without a predicted target indication, mechanism plausibility, or safety baseline, no repurposing case can be constructed or evaluated.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve TFDA package insert warnings and contraindications: download the insert PDF from the TFDA website and re-run extraction
- **[DG002 — High]** Populate mechanism of action from the DrugBank API — the query returned 1 result; verify why MOA was not carried through to the Evidence Pack
- **Pipeline diagnostic:** Confirm that the DrugBank result (result\_count: 1) and TFDA insert result (result\_count: 1) are being correctly parsed and mapped into `drug.original_moa` and `safety.key_warnings` respectively
- **Spelling verification:** Confirm that the INN query string `MEBENDAZOL` (without trailing *e*) matches the canonical WHO INN `MEBENDAZOLE` in all upstream database lookups, to rule out a name-mismatch causing the TxGNN pipeline to return zero predictions
- **Re-run TxGNN:** Once the drug identity and MOA fields are correctly populated, re-run the prediction pipeline to obtain ranked predicted indications
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

