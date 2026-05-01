---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# DARUNAVIR: Drug Repurposing Evaluation — Insufficient Prediction Data

## One-Sentence Summary

Darunavir (DrugBank: DB01264) is a well-known HIV-1 protease inhibitor widely used for the treatment of HIV/AIDS.
The TxGNN model has **not yet generated any predicted new indications** for this drug,
and the evidence pack currently contains **significant data gaps** in mechanism of action, safety, and regulatory information for Taiwan.

## Quick Overview

| Item | Content |
|------|------|
| Drug (INN) | Darunavir |
| DrugBank ID | DB01264 |
| Original Indication | Not documented in evidence pack (known globally: HIV-1 infection) |
| Predicted New Indication | — None predicted |
| TxGNN Prediction Score | — Not available |
| Evidence Level | N/A — No prediction generated |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Incomplete?

Darunavir is a second-generation HIV-1 protease inhibitor (brand name Prezista®, manufactured by Janssen). It works by selectively inhibiting the cleavage of HIV-encoded Gag-Pol polyproteins in infected cells, thereby preventing the formation of mature virus particles. It is typically co-administered with a pharmacokinetic booster (ritonavir or cobicistat) and is approved in numerous countries for the treatment of HIV-1 infection in adults and paediatric patients.

However, the current evidence pack has the following critical gaps that prevent a meaningful drug repurposing evaluation:

1. **No predicted indications**: The `predicted_indications` array is empty. Without a TxGNN prediction, no target disease can be evaluated.
2. **Mechanism of action not documented**: The MOA field is marked as a data gap, which impairs any mechanistic plausibility analysis.
3. **No Taiwan regulatory data**: Darunavir is not marketed in Taiwan per this evidence pack (0 authorizations), meaning there is no local package insert or safety data to draw from.

Until the TxGNN model produces at least one predicted indication and the data gaps are remediated, no repurposing assessment can proceed.

## Clinical Trial Evidence

Currently no predicted indication has been generated — clinical trial search not applicable.

## Literature Evidence

Currently no predicted indication has been generated — literature search not applicable.

## Taiwan Market Information

Darunavir currently holds **no marketing authorizations** in Taiwan. No license records are available.

## Safety Considerations

> Please refer to the package insert for safety information. All safety fields (warnings, contraindications, drug-drug interactions) are currently unavailable in this evidence pack.

**Identified Data Gaps:**

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | Blocking | Cannot proceed to S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Impairs mechanism–indication relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications exist for Darunavir at this time. Combined with missing MOA data, absent Taiwan regulatory information, and empty safety profiles, there is insufficient evidence to evaluate any repurposing opportunity. The evaluation cannot advance beyond the data collection phase.

**To proceed, the following is needed:**
- **Run TxGNN prediction** for Darunavir to generate candidate new indications
- **Remediate DG002**: Retrieve detailed mechanism of action data from DrugBank API
- **Remediate DG001**: Obtain TFDA package insert warnings and contraindications (or equivalent international label data, given Darunavir is not marketed in Taiwan)
- **Obtain safety data**: Drug-drug interaction profiles are critical given Darunavir's known extensive CYP3A4 interactions and requirement for pharmacokinetic boosting
- **Clarify regulatory pathway**: Since Darunavir is not marketed in Taiwan, determine whether an international reference (e.g., FDA, EMA) label should be used as the safety reference
---

