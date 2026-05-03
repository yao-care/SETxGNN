---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: Drug Repurposing Evaluation Report

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic widely used to treat bacterial infections including urinary tract infections, respiratory infections, and gastrointestinal infections. The TxGNN model has **not yet generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps that must be resolved before evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Ciprofloxacin |
| DrugBank ID | DB00537 |
| Original Indication | Not recorded in this evidence pack (known use: bacterial infections) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction or supporting studies available) |
| Taiwan Market Status | ✗ Not marketed (per TFDA query) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, **no TxGNN prediction has been generated** for Ciprofloxacin, so a mechanistic plausibility assessment cannot be performed.

For context, Ciprofloxacin is a second-generation fluoroquinolone antibiotic. It works by inhibiting bacterial DNA gyrase (topoisomerase II) and topoisomerase IV, which are essential enzymes for bacterial DNA replication, transcription, repair, and recombination. This mechanism of action is well-established in antimicrobial pharmacology, but the detailed MOA data was not included in the current evidence pack.

Before any repurposing evaluation can proceed, TxGNN predictions must first be generated for this compound, and the mechanism of action data gap must be filled via DrugBank API query.

## Clinical Trial Evidence

Currently no predicted indication is available; therefore, no clinical trial search has been conducted for a repurposing direction.

## Literature Evidence

Currently no predicted indication is available; therefore, no literature search has been conducted for a repurposing direction.

## Taiwan Market Information

Ciprofloxacin has **0 active authorizations** recorded in the TFDA database per the query conducted on 2026-03-29. No license details are available to display.

> **Note:** Ciprofloxacin is a globally well-established antibiotic (WHO Essential Medicines List). The absence of TFDA records in this evidence pack may reflect a query scope limitation rather than true absence from the Taiwan market. This should be verified.

## Safety Considerations

No safety data (warnings, contraindications, or drug-drug interactions) was retrieved in the current evidence pack. The DDI query returned no results.

> Please refer to the package insert for safety information. Ciprofloxacin is known to carry fluoroquinolone-class warnings including tendon rupture, peripheral neuropathy, CNS effects, and QT prolongation — these should be confirmed via the TFDA package insert.

## Data Gaps Requiring Resolution

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanism-relevance analysis | Query DrugBank API |
| — | TxGNN Predicted Indications | **Blocking** | No repurposing candidate to evaluate | Run TxGNN prediction pipeline for DB00537 |
| — | Original Indication Data | Medium | Cannot establish baseline for comparison | Populate from DrugBank or TFDA records |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is at a very early stage — the TxGNN model has not yet generated any predicted indications for Ciprofloxacin, and critical data fields (MOA, safety warnings, contraindications) remain unfilled. Without a predicted indication, no repurposing evaluation can be meaningfully conducted.

**To proceed, the following is needed:**
1. **Run TxGNN prediction** for Ciprofloxacin (DB00537) to generate candidate new indications
2. **Resolve DG001 (Blocking):** Retrieve and parse TFDA package insert for warnings and contraindications
3. **Resolve DG002:** Query DrugBank API to populate mechanism of action data
4. **Verify Taiwan market status:** Cross-check TFDA database for existing Ciprofloxacin authorizations (the current 0-result may be a query limitation)
5. **Re-generate evidence pack** once the above gaps are filled, then re-evaluate
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

