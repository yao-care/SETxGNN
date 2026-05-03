---
layout: default
title: Dexibuprofen
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Dexibuprofen
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

# Dexibuprofen: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dexibuprofen is the pharmacologically active S(+)-enantiomer of ibuprofen, a well-established non-steroidal anti-inflammatory drug (NSAID) used for pain, inflammation, and fever. The TxGNN model has **not yet generated a predicted new indication** for this compound. With **no clinical trials**, **no supporting literature**, and **no Taiwan market authorization**, this candidate currently lacks sufficient data for further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Taiwan authorization on file) |
| Predicted New Indication | None — TxGNN has not produced a prediction for this drug |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Model prediction not available; no actual studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, dexibuprofen is the S(+)-enantiomer of racemic ibuprofen and belongs to the propionic acid class of NSAIDs. It exerts its effects primarily through inhibition of cyclooxygenase (COX-1 and COX-2) enzymes, thereby reducing the synthesis of prostaglandins involved in inflammation, pain, and fever. Compared to racemic ibuprofen, dexibuprofen offers similar efficacy at roughly half the dose, with a potentially improved gastrointestinal tolerability profile.

However, the TxGNN model has not returned any predicted new indications for dexibuprofen at this time. This may be due to insufficient representation of the drug within the knowledge graph, or the model may not have identified a disease association that meets its confidence threshold. Without a prediction target, no mechanism-to-disease bridging analysis can be performed.

Given the absence of both a TxGNN prediction and Taiwan regulatory data, this candidate cannot proceed through the standard repurposing evaluation pipeline at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to evaluate).

---

## Literature Evidence

Currently no related literature available (no predicted indication to evaluate).

---

## Taiwan Market Information

Dexibuprofen has **no approved marketing authorizations** in Taiwan. The TFDA query returned zero results.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: TFDA package insert warnings, contraindications, and drug-drug interaction data were all unavailable for dexibuprofen in Taiwan. As an NSAID, general class-level safety concerns include:
> - **Cardiovascular risk**: Increased risk of serious cardiovascular thrombotic events, myocardial infarction, and stroke with prolonged use
> - **Gastrointestinal risk**: Increased risk of serious GI adverse events including bleeding, ulceration, and perforation
> - **Renal risk**: May cause fluid retention, oedema, and renal impairment
> - **Hypersensitivity**: Contraindicated in patients with known NSAID hypersensitivity or aspirin triad (asthma, rhinitis, nasal polyps)
>
> These are general NSAID class warnings and should be confirmed against the product-specific package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has not generated a predicted new indication for dexibuprofen, and the drug is not currently marketed in Taiwan. Without a target indication, evidence gathering and safety evaluation cannot proceed meaningfully.

**To proceed, the following is needed:**
- **TxGNN prediction output**: Re-run or verify the TxGNN model to determine if dexibuprofen has any viable repurposing candidates above the confidence threshold
- **Mechanism of action data (MOA)**: Retrieve detailed pharmacological target and pathway information from DrugBank (Data Gap DG002)
- **TFDA package insert warnings/contraindications**: Obtain and parse the relevant safety data if and when a Taiwan authorization exists (Data Gap DG001, Blocking severity)
- **Taiwan market pathway assessment**: Evaluate whether dexibuprofen could be introduced via a new drug application or if an existing racemic ibuprofen authorization could serve as a reference
- **Knowledge graph enrichment**: Ensure dexibuprofen's drug-target-disease relationships are adequately represented in the TxGNN knowledge graph before re-prediction
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

