---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# BIMATOPROST: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bimatoprost is a synthetic prostaglandin analogue, widely known internationally for the treatment of open-angle glaucoma, ocular hypertension, and hypotrichosis of the eyelashes. The TxGNN model has **not generated any predicted new indications** for this drug at this time. Combined with the absence of Taiwan (TFDA) market authorization, the current evidence base is insufficient to support a repurposing candidate assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in evidence pack (known internationally: glaucoma / ocular hypertension, eyelash hypotrichosis) |
| Predicted New Indication | **None** — No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions, no supporting studies) |
| Taiwan Market Status | ❌ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**No TxGNN prediction has been generated for Bimatoprost**, so there is no repurposing hypothesis to evaluate at this time.

For context, Bimatoprost is a synthetic prostamide — a structural analogue of prostaglandin F2α. It lowers intraocular pressure (IOP) by increasing aqueous humour outflow through both the trabecular meshwork and uveoscleral pathways. Internationally, it is marketed as **Lumigan®** (ophthalmic solution for glaucoma) and **Latisse®** (for eyelash growth). Detailed mechanism of action data was not available in the evidence pack (flagged as a data gap), but the prostamide receptor pathway is well-characterized in the published literature.

Without a predicted indication from the TxGNN model, no mechanistic bridge to a new therapeutic area can be assessed. This drug may be revisited if future model runs produce candidate indications, or if the underlying knowledge graph is updated with additional Bimatoprost-related edges.

---

## Clinical Trial Evidence

No predicted indication exists; therefore, no targeted clinical trial search was performed.

---

## Literature Evidence

No predicted indication exists; therefore, no targeted literature search was performed.

---

## Taiwan Market Information

Bimatoprost currently holds **no TFDA marketing authorizations** in Taiwan. No license records were returned from the TFDA query (queried 2026-03-29).

> **Note:** Bimatoprost is approved and widely marketed in other jurisdictions (US FDA, EMA) under the brand names Lumigan® and Latisse®. The absence of a Taiwan license represents a regulatory gap that would need to be addressed independently of any repurposing effort.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Key warnings, contraindications, and drug–drug interaction data were not available in the evidence pack. No DDI records were found in the queried databases. For international reference, the US FDA label for Lumigan® lists adverse effects including conjunctival hyperaemia, eye pruritus, iris pigmentation changes, and periorbital skin darkening.

---

## Data Gaps Identified

The following critical data gaps were flagged during evidence collection:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing prediction exists for Bimatoprost, and the drug is not marketed in Taiwan. There is no candidate indication to evaluate, and critical safety data gaps (TFDA warnings/contraindications) remain unresolved. Without a prediction and without local regulatory data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- **TxGNN model re-run** with an updated knowledge graph to determine whether any new indications are predicted for Bimatoprost
- **Resolution of DG001** — Obtain TFDA package insert data (warnings, contraindications) if/when the drug enters the Taiwan market, or reference international labels
- **Resolution of DG002** — Query DrugBank API for complete mechanism of action data to support future mechanistic bridging analysis
- **Regulatory pathway assessment** — If a repurposing indication is later identified, evaluate whether an import drug license or clinical trial application would be required in Taiwan
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

