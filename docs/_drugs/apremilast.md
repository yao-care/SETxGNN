---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 0
---

# Apremilast
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

# Apremilast: Drug Repurposing Evaluation Report

## One-Sentence Summary

Apremilast (DrugBank: DB05676) is a phosphodiesterase 4 (PDE4) inhibitor known internationally for treating psoriasis and psoriatic arthritis. The TxGNN model has **not yet generated predicted new indications** for this drug, and critical data gaps remain in mechanism of action details and regulatory safety information for Taiwan.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Apremilast |
| DrugBank ID | DB05676 |
| Original Indication | Not recorded in current dataset |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (Model prediction not yet available) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Apremilast is a selective phosphodiesterase 4 (PDE4) inhibitor that works by increasing intracellular cyclic AMP (cAMP) levels, which in turn modulates inflammatory mediators. It is approved in many countries (marketed as Otezla®) for plaque psoriasis, psoriatic arthritis, and oral ulcers associated with Behçet's disease.

However, the TxGNN model has not yet produced any predicted new indications for Apremilast. This may be due to incomplete knowledge graph integration or the drug not yet being fully mapped within the TxGNN prediction pipeline. Until the model generates candidate indications, no mechanism-based repurposing rationale can be evaluated.

## Clinical Trial Evidence

Currently no TxGNN-predicted indications are available, therefore no targeted clinical trial search has been conducted.

## Literature Evidence

Currently no TxGNN-predicted indications are available, therefore no targeted literature search has been conducted.

## Taiwan Market Information

Apremilast currently holds **no TFDA authorizations** and is **not marketed in Taiwan**. No license records were found in the TFDA database (queried 2026-03-29).

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the current dataset.

## Data Gaps Requiring Resolution

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot proceed to S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanism–indication relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications are currently available for Apremilast, and critical data gaps (TFDA safety information, MOA details) remain unresolved. The drug is also not marketed in Taiwan, which adds regulatory complexity to any repurposing effort. Evaluation cannot proceed until the prediction pipeline generates candidate indications.

**To proceed, the following is needed:**
- Run the TxGNN prediction model for Apremilast (DB05676) to generate candidate new indications
- Resolve DG001: Obtain TFDA package insert warnings and contraindications (Blocking)
- Resolve DG002: Retrieve detailed mechanism of action data from DrugBank API
- Investigate international regulatory filings (FDA, EMA) for approved indications to populate the original indication field
- Assess Taiwan market entry feasibility if a promising repurposing candidate is identified
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

