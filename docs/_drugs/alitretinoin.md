---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: Drug Repurposing Evaluation Report

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a retinoid known internationally for the treatment of Kaposi's sarcoma (topical) and chronic hand eczema (oral). The TxGNN model has **not yet generated predicted new indications** for this drug, and the evidence pack contains significant data gaps in mechanism of action and safety information, making a full repurposing evaluation not yet feasible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Taiwan market authorization) |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no predictions or supporting studies available) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not produced any predicted new indications for Alitretinoin, so a mechanistic plausibility assessment cannot be conducted at this time.

Alitretinoin (9-cis-retinoic acid) is a pan-retinoic acid receptor agonist that binds both RAR and RXR nuclear receptors, regulating cell differentiation, proliferation, and apoptosis. Internationally, it is approved as a topical gel (Panretin®) for cutaneous Kaposi's sarcoma lesions and as an oral capsule (Toctino®) for severe chronic hand eczema unresponsive to potent topical corticosteroids. However, detailed mechanism of action data was not available in this evidence pack (marked as a high-severity data gap).

Once MOA data is retrieved from DrugBank and TxGNN predictions are generated, a full mechanistic plausibility analysis linking the original and predicted indications can be performed.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indications are available, therefore no indication-specific clinical trial evidence has been collected.

---

## Literature Evidence

Currently no TxGNN-predicted indications are available, therefore no indication-specific literature evidence has been collected.

---

## Taiwan Market Information

Alitretinoin currently holds **no marketing authorizations** (藥證) in Taiwan. No products are marketed domestically.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Key safety data — including warnings, contraindications, and drug–drug interactions — were not available in this evidence pack. The TFDA package insert query returned no results, and the DDI query returned no interactions. These represent blocking and high-severity data gaps that must be resolved before any safety assessment can proceed.

---

## Data Gaps Summary

The following critical data gaps were identified and must be addressed before this candidate can advance:

| ID | Item | Severity | Impact | Remediation |
|----|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API |
| — | TxGNN Predicted Indications | **Blocking** | No repurposing candidates to evaluate | Run TxGNN prediction pipeline for DB00523 |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Alitretinoin has no TxGNN-predicted indications, is not marketed in Taiwan, and critical data gaps exist in both safety and mechanism of action information. There is insufficient data to evaluate any drug repurposing opportunity at this time.

**To proceed, the following is needed:**
- Run the TxGNN prediction pipeline for Alitretinoin (DB00523) to generate candidate new indications
- Retrieve detailed mechanism of action data from DrugBank API (DG002)
- Obtain TFDA package insert warnings and contraindications, or source equivalent international safety data (e.g., FDA/EMA labelling) (DG001)
- Re-query drug–drug interaction databases once the drug is contextualized against a specific predicted indication
- Re-evaluate once all blocking data gaps are resolved and at least one predicted indication is available
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

