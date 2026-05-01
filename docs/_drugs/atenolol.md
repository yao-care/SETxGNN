---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# ATENOLOL: Drug Repurposing Evaluation Report

## One-Sentence Summary

Atenolol is a well-known selective beta-1 adrenergic receptor blocker, widely used internationally for hypertension, angina pectoris, and cardiac arrhythmias. The TxGNN model has **not generated any predicted new indications** for this drug at this time. Combined with the absence of Taiwan market authorization and multiple critical data gaps, this candidate currently **lacks sufficient basis for repurposing evaluation**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (known internationally: hypertension, angina, arrhythmias) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

**No TxGNN prediction was generated for Atenolol.** Without a predicted new indication, a mechanistic plausibility assessment cannot be performed.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Atenolol is a cardioselective (beta-1 selective) adrenergic antagonist. It reduces heart rate, cardiac output, and blood pressure by blocking beta-1 receptors in the heart. It is one of the most widely prescribed antihypertensives globally and has a long track record of clinical use.

Despite this well-characterized pharmacological profile, the TxGNN model did not identify any novel indication candidates for Atenolol. This may reflect that: (1) the drug's therapeutic space is already well-explored, (2) its mechanism does not strongly overlap with unmet-need disease networks in the knowledge graph, or (3) additional data inputs are needed before predictions can be generated.

## Clinical Trial Evidence

Currently no predicted indication to evaluate — no related clinical trials to report.

## Literature Evidence

Currently no predicted indication to evaluate — no related literature to report.

## Taiwan Market Information

Atenolol currently holds **no valid marketing authorizations** in Taiwan (TFDA). No product licenses were found in the regulatory database query (queried 2026-03-29).

## Safety Considerations

> Please refer to the package insert for safety information.
>
> All safety fields — including key warnings, contraindications, and drug–drug interactions — returned as data gaps in this evidence pack. The TFDA package insert query returned 1 result but the structured safety data was not extracted. The DDI query returned no results.

## Data Gaps Summary

The following critical data gaps were identified and must be resolved before any repurposing assessment can proceed:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not produce any predicted new indications for Atenolol, and the drug is not currently marketed in Taiwan. Multiple blocking-level data gaps remain unresolved. There is no actionable repurposing hypothesis to evaluate at this time.

**To proceed, the following is needed:**
- **Resolve DG001 (Blocking):** Extract structured safety data (warnings, contraindications) from the TFDA package insert PDF
- **Resolve DG002 (High):** Retrieve detailed mechanism of action from DrugBank API to populate the MOA field
- **Re-run TxGNN prediction** after upstream data gaps are filled to determine whether new indication candidates emerge
- **Verify original indication data:** The evidence pack contains no original indications — confirm whether this is a data extraction issue or reflects actual regulatory status
- **Assess Taiwan market relevance:** Given Atenolol is not marketed in Taiwan, evaluate whether pursuing a Taiwan-specific repurposing pathway is strategically appropriate, or whether the analysis should be redirected to jurisdictions where the drug is already approved
---

