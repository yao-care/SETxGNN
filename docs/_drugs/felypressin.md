---
layout: default
title: Felypressin
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Felypressin
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

The txgnn-pipeline skill covers infrastructure and deployment — not report writing. The system prompt already defines the full report format. I'll proceed to generate the report directly from the Evidence Pack.

---

# Felypressin: From Dental Vasoconstrictor to Drug-Induced Osteoporosis

## One-Sentence Summary

Felypressin is a synthetic vasopressin analogue used as a vasoconstrictor, most commonly combined with local anaesthetics (e.g., prilocaine) for dental procedures as an adrenaline-free alternative.
The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**,
but currently **no clinical trials** and **no publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vasoconstrictor for dental local anaesthesia (no formal regulatory authorisation on record) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, felypressin is a synthetic analogue of arginine vasopressin (AVP) that acts selectively on V1a receptors to produce vasoconstriction. It is used as an adrenaline-free vasoconstrictor in dental local anaesthesia (most commonly combined with prilocaine), and is preferred in patients for whom epinephrine is contraindicated, such as those with certain cardiovascular conditions.

The mechanistic rationale connecting felypressin to drug-induced osteoporosis is indirect and speculative. Vasopressin receptors — specifically AVPR1A — are known to be expressed on osteoblasts and osteoclasts, suggesting that vasopressin signalling may play a modulatory role in bone metabolism. However, drug-induced osteoporosis is predominantly driven by glucocorticoid/corticosteroid pathways, which do not directly intersect with felypressin's V1a-mediated vasoconstrictor mechanism. No pharmacological bridge between the two has been established in the literature.

The high TxGNN prediction score (99.80%) most likely reflects topological proximity in the knowledge graph between vasopressin-class drugs and bone disease nodes, rather than a direct or clinically meaningful pharmacological connection. With zero supporting clinical trials and zero publications specific to this drug–disease pair, this prediction should be treated as a hypothesis-generating signal only, not as actionable evidence.

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
Despite a high TxGNN model score, the predicted link between felypressin and drug-induced osteoporosis rests entirely on knowledge-graph topology with no clinical or preclinical experimental evidence, and the mechanistic chain is too indirect to justify further investment at this stage.

**To proceed, the following is needed:**
- Preclinical studies (in vitro / in vivo) examining whether felypressin modulates bone turnover markers via AVPR1A signalling in osteoblasts or osteoclasts
- Mechanism of action data retrieved from DrugBank API (data gap DG002)
- Full safety profile from the package insert — TFDA/EMA/FDA (data gap DG001)
- Clarification of the clinical question: is felypressin being evaluated as a *treatment* for drug-induced osteoporosis, or is drug-induced osteoporosis a potential *side effect* of felypressin itself that warrants pharmacovigilance?
- Review of whether the TxGNN score reflects a genuine drug–disease biological signal or is an artefact of vasopressin receptor ubiquity in the knowledge graph
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

