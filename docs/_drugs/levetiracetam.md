---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: Evaluation Report — Insufficient TxGNN Output for Repurposing Assessment

## One-Sentence Summary

Levetiracetam (DrugBank: DB01202) is a well-established antiepileptic agent widely used for seizure management.
The current Evidence Pack contains **no TxGNN predicted indications**, rendering a standard drug repurposing evaluation impossible at this stage.
Until the data pipeline is completed and predictions are generated, this candidate must be placed on **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory database (data gap) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — No predictions or supporting studies available in this pack |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction Can Be Assessed

The `predicted_indications` array in this Evidence Pack is empty. This means one of the following occurred in the data pipeline:

1. **Model output not yet generated** — The TxGNN model has not yet run or returned results for DB01202.
2. **Mapping failure** — Disease mapping from TxGNN output to ICD/MeSH codes may have failed upstream.
3. **Intentional exclusion** — The candidate may have been filtered out prior to evidence collection.

Additionally, two blocking or high-severity data gaps exist:

| Gap ID | Item | Severity | Impact |
|--------|------|----------|--------|
| DG001 | Taiwan FDA package insert (warnings/contraindications) | Blocking | Cannot complete S1 safety assessment |
| DG002 | Mechanism of Action (MOA) | High | Cannot perform mechanistic relevance analysis |

Without predicted indications, there is no repurposing hypothesis to evaluate, and the rest of the standard report sections (clinical trial evidence, literature evidence, mechanism reasoning) cannot be meaningfully populated.

---

## Taiwan Market Information

Levetiracetam currently has **no approved product licenses** in the Taiwan regulatory database. No dosage forms or approved indications are on record.

> Note: This contrasts with the drug's global regulatory status — Levetiracetam is approved in many jurisdictions (FDA, EMA, etc.) for epilepsy. The absence of Taiwan records may reflect a query scope limitation or an actual market gap that warrants separate investigation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Drug-drug interaction data was queried on 2026-03-29 and returned no results (`not_found`). Taiwan FDA package insert data was queried but warnings and contraindications were not parsed into the Evidence Pack (DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack lacks the minimum required data to support a drug repurposing evaluation — specifically, no TxGNN predicted indications are present and both MOA and safety data are flagged as gaps. Proceeding without these would produce an assessment without any scientific basis.

**To proceed, the following is needed:**
- Re-run the TxGNN pipeline for DB01202 and confirm `predicted_indications` is populated with at least one scored candidate
- Retrieve MOA data via DrugBank API (remediation for DG002)
- Download and parse the Taiwan FDA package insert PDF to extract warnings and contraindications (remediation for DG001)
- Verify whether the absence of Taiwan market authorization is accurate or a query scope issue
- Resubmit the completed Evidence Pack for a full evaluation
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

