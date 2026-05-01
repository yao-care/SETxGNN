---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 0
---

# Dapagliflozin
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

# DAPAGLIFLOZIN: Evaluation Pending — No TxGNN Prediction Available

## One-Sentence Summary

Dapagliflozin (DrugBank: DB06292) is a sodium-glucose co-transporter 2 (SGLT2) inhibitor widely used internationally for type 2 diabetes mellitus, heart failure, and chronic kidney disease. The TxGNN model has **not yet generated any predicted new indications** for this drug, and it is currently **not marketed in Taiwan** with **zero TFDA authorizations**. This report documents the current data state and identifies the gaps that must be filled before a repurposing evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (known internationally: type 2 diabetes, heart failure, CKD) |
| Predicted New Indication | — (No TxGNN prediction generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction, no supporting studies in pack) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Dapagliflozin is a selective inhibitor of sodium-glucose co-transporter 2 (SGLT2) in the proximal renal tubule. By blocking SGLT2, it reduces renal glucose reabsorption, leading to urinary glucose excretion (glycosuria) and thereby lowering blood glucose levels. Beyond glycaemic control, SGLT2 inhibitors have demonstrated significant cardiovascular and renal protective effects through mechanisms involving natriuresis, osmotic diuresis, reduced preload, and potential anti-inflammatory and anti-fibrotic pathways.

No TxGNN prediction has been generated for Dapagliflozin at this time. The absence of a prediction may stem from insufficient drug-disease relationship data in the knowledge graph, or the drug may not yet have been processed through the prediction pipeline. Notably, Dapagliflozin has already undergone substantial clinical repurposing internationally — from its original diabetes indication to heart failure (DAPA-HF trial) and chronic kidney disease (DAPA-CKD trial) — suggesting that conventional repurposing avenues have already been extensively explored.

Once the TxGNN model generates predictions for this drug, a full mechanistic plausibility analysis should be conducted to evaluate any novel indication candidates beyond the already-established repurposed uses.

## Clinical Trial Evidence

Currently no TxGNN-predicted indications are available, therefore no indication-specific clinical trial search was performed.

## Literature Evidence

Currently no TxGNN-predicted indications are available, therefore no indication-specific literature search was performed.

## Taiwan Market Information

Dapagliflozin currently holds **no TFDA authorizations** and is **not marketed in Taiwan** based on the evidence pack data.

> **Note:** Dapagliflozin is marketed internationally under the brand names **Farxiga** (US) and **Forxiga** (EU/other markets) by AstraZeneca. The absence of Taiwan authorizations in this dataset should be verified against current TFDA records, as the drug is widely available in many Asia-Pacific markets.

## Safety Considerations

Please refer to the package insert for safety information. Key safety data (warnings, contraindications, and drug-drug interactions) were not available in the evidence pack at the time of this report.

> **Known class-level safety signals for SGLT2 inhibitors** (from international labelling, not from this evidence pack):
> - Risk of diabetic ketoacidosis (including euglycaemic DKA)
> - Genital mycotic infections
> - Urinary tract infections
> - Volume depletion / hypotension in susceptible populations
> - Fournier's gangrene (rare)
> - Lower limb amputation risk (class-level signal, primarily canagliflozin)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indication has been generated for Dapagliflozin, and critical data gaps remain (MOA data, TFDA regulatory information, safety profile). Without a predicted new indication, a repurposing evaluation cannot proceed. Furthermore, this drug has already been extensively repurposed through conventional clinical development (diabetes → heart failure → CKD), which may limit the novelty of any model-generated predictions.

**To proceed, the following is needed:**
- **TxGNN prediction generation**: Run Dapagliflozin through the TxGNN prediction pipeline to identify candidate indications
- **MOA data completion**: Query DrugBank API for detailed mechanism of action (remediation identified as DG002)
- **TFDA regulatory verification**: Confirm Taiwan market status against current TFDA database — the drug may have been approved under brand names not captured in this query
- **Safety data collection**: Obtain TFDA package insert warnings and contraindications (remediation identified as DG001, severity: Blocking)
- **Differentiation analysis**: Once predictions are available, assess whether they represent genuinely novel indications beyond the already-established heart failure and CKD uses
---

