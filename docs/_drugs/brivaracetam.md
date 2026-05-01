---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: Drug Repurposing Evaluation — Awaiting Prediction Data

## One-Sentence Summary

Brivaracetam (DB05541) is an antiepileptic drug known to selectively bind synaptic vesicle protein 2A (SV2A), used internationally for partial-onset (focal) seizures. The TxGNN model has **not yet generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps in mechanism of action, safety, and regulatory information. **No repurposing candidates can be evaluated at this time.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack (known internationally: partial-onset seizures) |
| Predicted New Indication | **None** — TxGNN has not returned predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — No prediction or supporting studies available |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Can't This Drug Be Evaluated Yet?

Brivaracetam is a well-characterized antiepileptic drug approved in the US (Briviact®) and the EU for the adjunctive treatment of partial-onset seizures. It is a high-affinity, selective ligand for synaptic vesicle protein 2A (SV2A), a mechanism related to but distinct from its predecessor levetiracetam. However, the current evidence pack lists the mechanism of action as unavailable, and no original indications are recorded from the Taiwan (TFDA) data source.

The most critical gap is that the `predicted_indications` array is empty — the TxGNN model has not generated any repurposing candidates for Brivaracetam. Without a target indication, no mechanistic plausibility analysis, clinical trial search, or literature review can be performed. This may be due to incomplete mapping of Brivaracetam within the TxGNN knowledge graph, or the drug may not yet have been processed through the prediction pipeline.

Additionally, Brivaracetam is not marketed in Taiwan (0 TFDA licenses), which adds a regulatory barrier to any future repurposing effort in this market. Before re-evaluation, both the prediction pipeline and regulatory data need to be populated.

---

## Clinical Trial Evidence

Currently no predicted indication available — clinical trial search not applicable.

---

## Literature Evidence

Currently no predicted indication available — literature search not applicable.

---

## Taiwan Market Information

Brivaracetam currently holds **no TFDA marketing authorizations** and is not available on the Taiwan market.

---

## Safety Considerations

Safety data (warnings, contraindications, and drug interactions) is not available in the current evidence pack. TFDA package insert data could not be retrieved for this drug.

> Please refer to the international package insert (e.g., US Briviact® PI or EMA SmPC) for complete safety information.

---

## Data Gaps Summary

The following critical data gaps were identified and must be resolved before re-evaluation:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter Stage 1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | **High** | Prevents mechanistic relevance analysis | Query DrugBank API for MOA data |
| — | TxGNN Predicted Indications | **Blocking** | No repurposing candidate to evaluate | Run Brivaracetam through TxGNN prediction pipeline |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications exist for Brivaracetam, making it impossible to evaluate any repurposing opportunity. Combined with the absence of a Taiwan marketing authorization and multiple blocking data gaps, this candidate cannot proceed at this time.

**To proceed, the following is needed:**
- **Run Brivaracetam through the TxGNN prediction pipeline** to generate candidate indications (highest priority)
- Resolve DG002: Retrieve detailed mechanism of action data from DrugBank (SV2A binding, pharmacodynamics)
- Resolve DG001: Obtain TFDA package insert safety data, or alternatively source from FDA/EMA if Taiwan registration is not planned
- Assess Taiwan regulatory pathway feasibility, given the drug is currently not marketed (未上市)
- Once a predicted indication is available, re-generate the evidence pack with clinical trial and literature searches targeting that indication
---

