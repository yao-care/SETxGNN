---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# DIGOXIN: Drug Repurposing Candidate — Awaiting Prediction Data

## One-Sentence Summary

Digoxin (DrugBank: DB00390) is a well-known cardiac glycoside historically used for heart failure and atrial fibrillation. Currently, the TxGNN model has **no predicted new indications** for this drug, and critical data gaps in mechanism of action and safety information must be resolved before evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | DIGOXIN |
| DrugBank ID | [DB00390](https://go.drugbank.com/drugs/DB00390) |
| Original Indication | Not available in current dataset (no TFDA licenses found) |
| Predicted New Indication | **None** — No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No model predictions, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for Digoxin. Without a predicted indication, a mechanistic plausibility assessment cannot be performed.

> Detailed mechanism of action (MOA) data is not available in this Evidence Pack. Digoxin is widely recognized as a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump, leading to increased intracellular calcium and enhanced cardiac contractility. Its conventional indications include heart failure with reduced ejection fraction and rate control in atrial fibrillation/flutter. However, this MOA data was not supplied through the current pipeline and represents a **High-severity data gap (DG002)**.

Until the TxGNN model produces candidate indications and the MOA data gap is resolved, no mechanistic bridging analysis can be conducted.

## Clinical Trial Evidence

Currently no predicted indication exists, therefore no related clinical trials can be assessed.

## Literature Evidence

Currently no predicted indication exists, therefore no related literature can be assessed.

## Taiwan Market Information

No TFDA marketing authorizations were found for Digoxin. The drug is listed as **not marketed (未上市)** in Taiwan based on the TFDA query conducted on 2026-03-29.

> **Note:** Digoxin is widely available in many global markets. The absence from the TFDA database may warrant re-verification or consideration of alternative brand name searches.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> **Note:** The TFDA package insert query (2026-03-29) returned 1 result, but warnings and contraindications were not extracted into this Evidence Pack. This constitutes a **Blocking-severity data gap (DG001)** that must be resolved before safety evaluation can proceed.

## Data Gaps Summary

The following unresolved data gaps are blocking this evaluation:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | **High** | Affects mechanistic relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications are available for Digoxin, and two critical data gaps (safety information and MOA) remain unresolved. Without a target indication and baseline safety profile, this candidate cannot advance through the evaluation pipeline.

**To proceed, the following is needed:**
- Run TxGNN prediction pipeline for Digoxin (DB00390) to generate candidate new indications
- Resolve **DG001**: Extract warnings and contraindications from the TFDA package insert PDF
- Resolve **DG002**: Query DrugBank API for detailed mechanism of action data
- Re-verify Taiwan market status — Digoxin is globally well-established; the zero-license finding may indicate a search limitation (e.g., brand name variants not queried)
- Once predictions and safety data are available, re-generate this Evidence Pack and re-evaluate
---

