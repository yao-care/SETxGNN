---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dienogest is a synthetic progestogen identified in DrugBank (DB09123), commonly used internationally for the treatment of endometriosis. The TxGNN model has **not yet generated predicted new indications** for this compound, and there are **no clinical trial or literature evidence entries** in the current evidence pack. This report documents the baseline status and identifies critical data gaps that must be resolved before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack |
| Predicted New Indication | None (TxGNN prediction not yet available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions or supporting studies available) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Dienogest is a fourth-generation selective progestogen with anti-androgenic activity. It is widely used outside of Taiwan — particularly in Europe and Japan — for the treatment of endometriosis, where it suppresses estradiol-driven endometrial tissue growth.

However, because the TxGNN model has not yet produced any predicted indications for Dienogest, a mechanistic plausibility analysis cannot be performed at this time. The absence of predictions may be related to incomplete input data (e.g., missing MOA mapping in the knowledge graph) or the drug not meeting the model's threshold criteria for repurposing candidates.

Before any repurposing assessment can proceed, the foundational data gaps — particularly the mechanism of action and the original indication mapping — must be resolved to enable the TxGNN model to generate meaningful predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the evidence pack.

---

## Literature Evidence

Currently no related literature available in the evidence pack.

---

## Taiwan Market Information

Dienogest currently holds **no marketing authorizations** in Taiwan (TFDA). There are no registered licenses or approved products containing Dienogest as an active ingredient in the Taiwan market.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not yet available in the evidence pack for Dienogest.

---

## Data Gaps Requiring Resolution

The following critical data gaps were identified and must be addressed before this candidate can advance:

| Gap ID | Item | Severity | Impact | Recommended Remediation |
|--------|------|----------|--------|------------------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanism-relevance analysis | Query DrugBank API for MOA data |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no TxGNN-predicted indications for Dienogest at this time, and critical baseline data (MOA, original indication mapping, safety profile) remains unresolved. The candidate cannot be evaluated for repurposing potential until foundational data is in place.

**To proceed, the following is needed:**
- Resolve **DG002**: Obtain detailed mechanism of action data from DrugBank API to enable knowledge graph integration
- Resolve **DG001**: Obtain TFDA package insert warnings and contraindications (or equivalent international regulatory data, given the drug is not marketed in Taiwan)
- Re-run TxGNN prediction pipeline once MOA and indication data are properly mapped into the knowledge graph
- If Dienogest remains unmarketable in Taiwan, assess whether international regulatory data (EMA, PMDA) can serve as a proxy for safety evaluation
- Consider whether the Taiwan-unmarketable status affects the strategic value of pursuing this candidate for drug repurposing in the Taiwan context
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

