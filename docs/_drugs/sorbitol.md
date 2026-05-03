---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The `txgnn-pipeline` skill confirms this is within the TxGNN drug repurposing system. The report generation is governed by the system prompt instructions. Proceeding to generate the evaluation report from the Evidence Pack.

---

# SORBITOL: From Osmotic Agent to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is an osmotic sugar alcohol widely used as a laxative and pharmaceutical excipient, with no formal original indications registered in this dataset.
The TxGNN model predicts it may be effective for **Exercise-Induced Malignant Hyperthermia (ExMH)**,
however **no clinical trials** and **no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication data available |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, Sorbitol is an osmotic sugar alcohol primarily acting on intestinal water osmosis and extracellular fluid tonicity regulation — it draws water into the intestinal lumen and modulates extracellular osmotic pressure.

Exercise-Induced Malignant Hyperthermia (ExMH) is a rare, life-threatening condition driven by mutations in *RYR1* or *CACNA1S* genes, which cause uncontrolled Ca²⁺ release from the skeletal muscle sarcoplasmic reticulum (SR). This triggers a cascade of severe hypermetabolism, hyperthermia, and rhabdomyolysis. There is no established pharmacological connection between sorbitol's osmotic mechanism and this RYR1/CACNA1S-mediated pathway.

While hyperosmotic solutions can theoretically modulate intracellular calcium signaling, this effect has never been experimentally demonstrated at the skeletal muscle SR Ca²⁺ channel level, and its direction and magnitude remain entirely unknown. The high TxGNN score (0.9940) most likely reflects **sparse node bias** in the knowledge graph: ExMH is an ultra-rare indication with heavily imbalanced positive/negative training samples, making the model prone to over-predicting osmotic agents for such diseases. This prediction should be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting sorbitol's use in exercise-induced malignant hyperthermia, and the mechanistic rationale is highly speculative. The high TxGNN score is most likely an artifact of sparse node bias in the knowledge graph rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Preclinical studies investigating sorbitol's effect on skeletal muscle Ca²⁺ channel activity (RYR1/CACNA1S pathway)
- Mechanism of action data from DrugBank to enable a pharmacological plausibility assessment
- Evidence of any osmotic agent effects in hyperthermia or skeletal myopathy models
- Review of TxGNN model calibration for ultra-rare diseases to quantify and correct sparse node bias before further action
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

