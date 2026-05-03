---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: Evaluation Report — Insufficient Data for Full Repurposing Analysis

## One-Sentence Summary

Miglustat (DB00419) is a small-molecule iminosugar with no original indication data available in this Evidence Pack.
The TxGNN model returned **no predicted indications** for this candidate, and critical data fields — including mechanism of action, approved indications, and safety warnings — are absent.
This report reflects the current data state; a full repurposing evaluation **cannot be completed** until blocking data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data available |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and no prediction returned) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why a Full Prediction Analysis Is Not Possible

The Evidence Pack for Miglustat contains two compounding problems that prevent a standard repurposing evaluation:

**No TxGNN predictions were returned.** The `predicted_indications` array is empty, meaning the model either did not produce a ranked candidate list for this drug, or the output was not successfully captured in this Evidence Pack version. Without a predicted indication, the core premise of the report — explaining *why* a new indication is mechanistically plausible — cannot be constructed.

**Mechanism of action (MOA) data is missing.** The `original_moa` field is flagged as a high-severity data gap (DG002). Even if predicted indications were available, assessing mechanistic plausibility would require understanding how Miglustat exerts its pharmacological effect. Without MOA data, any reasoning about applicability to a new indication would be speculative.

**Original indication is unconfirmed in this dataset.** The `original_indications` array is empty and no TFDA product licenses exist. While Miglustat has known approved uses in other jurisdictions (Gaucher disease, Niemann-Pick disease type C), this Evidence Pack does not contain verified indication data and those entries should not be assumed.

---

## Taiwan Market Information

Miglustat is currently **not marketed in Taiwan**. No TFDA product licenses were found in the regulatory query conducted on 2026-03-29 (query result: 0 records). There are no dosage forms, approved indications, or authorization numbers to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields — key warnings, contraindications, and drug-drug interactions — returned no data in this Evidence Pack. DDI query status: not found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing two blocking-to-high severity data inputs (TFDA package insert safety data and MOA), and the TxGNN prediction engine returned no candidate indications. There is no actionable repurposing signal to evaluate at this time.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve TFDA package insert PDF and extract warnings and contraindications, to enable S1 safety screening
- **[High — DG002]** Query DrugBank API to populate the MOA field; Miglustat's substrate reduction mechanism is central to any mechanistic plausibility argument
- **[Critical]** Investigate why `predicted_indications` is empty — determine whether TxGNN failed to score this drug, returned results that were not captured, or correctly identified no repurposing candidates above threshold
- **[Follow-up]** Once MOA and indication data are restored, re-run the TxGNN pipeline and regenerate the Evidence Pack with a populated `predicted_indications` array before proceeding to full evaluation
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

