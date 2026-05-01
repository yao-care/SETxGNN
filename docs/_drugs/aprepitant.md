---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# APREPITANT: Drug Repurposing Evaluation — Awaiting Prediction Data

## One-Sentence Summary

Aprepitant (DrugBank: DB00673) is a neurokinin-1 (NK1) receptor antagonist, widely known internationally for prevention of chemotherapy-induced and postoperative nausea and vomiting. Currently, the TxGNN model has **no predicted new indications** on file, and critical data gaps (MOA details, regulatory label information) remain unresolved. **No clinical trial or literature evidence** has been compiled for a repurposing direction at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug (INN) | Aprepitant |
| DrugBank ID | DB00673 |
| Original Indication | Not available in evidence pack (known internationally as anti-emetic for CINV) |
| Predicted New Indication | **None** — TxGNN prediction not yet available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No model prediction or supporting studies on file) |
| Taiwan Market Status | ❌ Not marketed |
| Number of TFDA Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Aprepitant is a selective neurokinin-1 (NK1) receptor antagonist. It works by blocking the binding of substance P to the NK1 receptor in the central nervous system, thereby inhibiting the emetic reflex. It is marketed internationally (e.g., as Emend® by Merck) for prevention of acute and delayed chemotherapy-induced nausea and vomiting (CINV) as well as postoperative nausea and vomiting (PONV).

Since no TxGNN-predicted new indication is available, a mechanistic plausibility assessment cannot be performed at this stage. The NK1 receptor pathway is implicated in pain signaling, inflammation, and mood regulation beyond emesis, which could theoretically open repurposing avenues — but this remains speculative without a formal model prediction.

To enable a meaningful evaluation, the TxGNN prediction pipeline must first be run for Aprepitant to generate candidate indications with associated scores.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search has been conducted.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search has been conducted.

---

## Taiwan Market Information

Aprepitant currently holds **no TFDA licenses** and is **not marketed in Taiwan**. No authorization records are available.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug–drug interaction data were not available in the current evidence pack.

---

## Data Gaps Requiring Resolution

The following critical gaps were identified and must be addressed before this evaluation can proceed:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Affects mechanism–indication relevance analysis | Query DrugBank API |

Additionally:
- **Predicted indications** are completely absent — the TxGNN model must be run for DB00673.
- **Original indication text** is missing from the evidence pack and should be populated from DrugBank or TFDA sources.
- **Drug–drug interaction (DDI)** query returned no results; consider querying alternative sources (e.g., DrugBank interaction API, Lexicomp).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indication exists for Aprepitant at this time, and multiple blocking data gaps (TFDA label information, MOA) prevent even a preliminary safety assessment. The evaluation cannot proceed until foundational data is in place.

**To proceed, the following is needed:**
1. **Run the TxGNN prediction model** for Aprepitant (DB00673) to generate candidate repurposing indications with scores
2. **Resolve DG001 (Blocking):** Obtain and parse the TFDA package insert for warnings and contraindications
3. **Resolve DG002 (High):** Query DrugBank API for detailed mechanism of action data
4. **Populate original indication** from authoritative sources (DrugBank, TFDA, or international labels)
5. **Re-query DDI sources** using alternative databases if TFDA yields no results
6. Once predicted indications are available, conduct targeted **clinical trial** (ClinicalTrials.gov) and **literature** (PubMed) searches for the top-ranked candidates
---

