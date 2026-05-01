---
layout: default
title: Bivalirudin
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
---

# Bivalirudin
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

# Bivalirudin: Evaluation Report — No Predicted Indication Available

## One-Sentence Summary

Bivalirudin (DrugBank: DB00006) is a synthetic peptide known internationally as a direct thrombin inhibitor used as an anticoagulant during percutaneous coronary interventions. However, the current Evidence Pack contains **no TxGNN-predicted new indications**, and the drug is **not marketed in Taiwan** with **zero active licenses**, making a full repurposing evaluation not possible at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no Taiwan license data) |
| Predicted New Indication | **None** — TxGNN prediction results not yet available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No prediction, no supporting studies in pack) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**No TxGNN prediction is available for evaluation.**

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on publicly known information, Bivalirudin is a synthetic 20-amino-acid peptide that acts as a **direct thrombin inhibitor**. It reversibly binds to both the catalytic active site and the anion-binding exosite of thrombin, thereby inhibiting the coagulation cascade. Internationally, it is primarily used as an anticoagulant during **percutaneous coronary intervention (PCI)** and in patients with heparin-induced thrombocytopenia (HIT).

Since the `predicted_indications` array is empty, there is no new indication to assess for mechanistic plausibility. The TxGNN model has not yet generated a repurposing candidate for this drug, or the results have not been integrated into this Evidence Pack. A meaningful mechanistic bridging analysis cannot be performed until a predicted indication is provided.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search was performed for a repurposed indication.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search was performed for a repurposed indication.

---

## Taiwan Market Information

Bivalirudin currently holds **no active marketing authorizations** in Taiwan (TFDA). No license records were returned from the TFDA query conducted on 2026-03-29.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| — | — | — | No Taiwan licenses on record |

---

## Safety Considerations

> Please refer to the package insert for safety information.

All safety fields (key warnings, contraindications, and drug-drug interactions) returned as data gaps or not found in the current Evidence Pack. Since Bivalirudin is not marketed in Taiwan, no local package insert data is available from TFDA.

For international reference, prescribers should be aware that Bivalirudin, as a direct thrombin inhibitor, carries inherent **bleeding risk** as its primary safety concern. Full safety profiling should be sourced from international drug references (e.g., DrugBank, FDA label, EMA SmPC) before any repurposing consideration.

---

## Data Gaps Requiring Resolution

The following critical data gaps were identified in this Evidence Pack:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Affects mechanism-association analysis | Query DrugBank API |

Additionally, the most critical gap is the absence of any **TxGNN predicted indications**, without which no repurposing evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted new indications for Bivalirudin, and the drug is not marketed in Taiwan (zero licenses). There is insufficient data to evaluate any drug repurposing opportunity at this time. Additionally, two data gaps (one Blocking-severity) remain unresolved.

**To proceed, the following is needed:**
- **TxGNN prediction results** — Run or re-run the TxGNN model for Bivalirudin (DB00006) and populate the `predicted_indications` array
- **Mechanism of Action data** — Query DrugBank API to obtain structured MOA information (DG002)
- **TFDA package insert** — If Bivalirudin gains Taiwan market entry, download and parse package insert PDF for warnings and contraindications (DG001)
- **Taiwan regulatory pathway assessment** — Evaluate whether an import drug license or clinical trial application is warranted if a viable indication is predicted
---

