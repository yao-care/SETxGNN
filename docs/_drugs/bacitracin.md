---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# BACITRACIN: Drug Repurposing Evaluation Report

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic historically used for the prevention and treatment of bacterial infections, primarily via topical application. The TxGNN model has **no predicted new indications** for this drug at this time. The evidence pack currently contains significant data gaps, and the drug is **not marketed in Taiwan**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in evidence pack (known use: topical bacterial infections) |
| Predicted New Indication | None predicted |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only, no candidate indication identified |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Bacitracin is a cyclic polypeptide antibiotic produced by *Bacillus subtilis* and *Bacillus licheniformis*. It primarily acts by interfering with bacterial cell wall synthesis through inhibition of the dephosphorylation of C₅₅-isoprenyl pyrophosphate, a lipid carrier involved in peptidoglycan biosynthesis. It is most commonly used topically to prevent and treat minor skin infections.

Since the TxGNN model has not generated any predicted new indications for Bacitracin, there is no mechanistic rationale to evaluate at this time. The absence of predictions may reflect the drug's narrow pharmacological profile (primarily antimicrobial), limited systemic use due to nephrotoxicity concerns, or insufficient representation in the knowledge graph used by TxGNN.

Without a candidate indication, no further biological plausibility assessment can be performed.

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication was identified by TxGNN.

## Literature Evidence

Currently no related literature available — no predicted indication was identified by TxGNN.

## Taiwan Market Information

Bacitracin currently holds **no active marketing authorizations** in Taiwan. The TFDA query (2026-03-29) returned zero results.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No authorizations found |

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No new indications have been predicted by TxGNN for Bacitracin, and the drug is not currently marketed in Taiwan. There is insufficient data to proceed with any repurposing evaluation at this stage.

**To proceed, the following is needed:**
- TxGNN model re-run or knowledge graph update to determine if any new indications can be predicted
- Mechanism of action (MOA) data retrieval from DrugBank API (Data Gap DG002)
- TFDA package insert warnings and contraindications (Data Gap DG001)
- Assessment of whether Bacitracin's limited systemic applicability (due to nephrotoxicity) fundamentally constrains repurposing potential
- If a topical-only repurposing strategy is considered, identification of dermatological or wound-care indications beyond current antimicrobial use
---

