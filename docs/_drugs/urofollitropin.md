---
layout: default
title: Urofollitropin
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Urofollitropin
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Urofollitropin: From Infertility Treatment to Migraine Disorder

## One-Sentence Summary

Urofollitropin is a purified follicle-stimulating hormone (FSH) preparation used in fertility medicine to stimulate ovarian follicle development in women undergoing assisted reproduction (e.g., IVF/ICSI) and to treat anovulatory infertility.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a prediction score of **99.85%**, however there are currently **0 clinical trials** and **0 relevant publications** supporting this direction.
Mechanistic review of all retrieved evidence strongly suggests these predictions reflect knowledge graph structural artefacts rather than genuine biological repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian stimulation / Infertility treatment (not registered in Taiwan; approved for ART in other markets) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Urofollitropin is a purified preparation of FSH extracted from the urine of postmenopausal women. It acts by binding to FSH receptors (FSHR) on ovarian granulosa cells, triggering follicular recruitment, growth, and maturation. Its established therapeutic role is in assisted reproductive technology and anovulatory infertility. Detailed mechanism of action data is not currently available in the database, but FSH's gonadotropin signaling is well-characterized in the reproductive literature.

The theoretical basis for the migraine prediction rests on one anatomical observation: FSH receptors have been detected in the hypothalamus and select brainstem nuclei — regions that overlap with the trigeminovascular pain network implicated in migraine pathophysiology. In principle, FSH signaling at these sites could theoretically modulate pain processing. However, no direct mechanistic study, animal model, or clinical investigation has ever explored this pathway. The connection between FSH and headache disorders remains entirely speculative.

The high TxGNN scores across all 10 predicted indications (migraine disorder, brainstem aura migraine, His bundle tachycardia, POTS, restless legs syndrome, Raynaud disease, and others) are most likely explained by knowledge graph topology: as a neuroendocrine signaling molecule, FSH is densely connected to hypothalamic–pituitary–neurological nodes in the graph, causing non-specific score inflation across neurological and autonomic disease categories. This interpretation is confirmed by a targeted literature review: the 20 publications retrieved for the adjacent indication "migraine with or without aura, susceptibility to" (rank 9) were all found to concern **epilepsy-migraine genetic comorbidity** (SCN1A, MTHFR polymorphisms, neuroinflammation cascades) — none mention FSH or Urofollitropin. These papers were introduced via a knowledge graph migraine↔epilepsy comorbidity node and represent confirmed false positives.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **⚠️ False Positive Alert:** 20 publications were retrieved by the pipeline for the adjacent prediction "migraine with or without aura, susceptibility to" (rank 9). Manual review confirmed that **all 20 papers** concern epilepsy and migraine genetic overlap research — topics including SCN1A polymorphisms, MTHFR variants, EEG patterns, neuroinflammation, and pediatric epilepsy models. **None of these papers discuss FSH, Urofollitropin, or gonadotropin signaling.** They were imported via a knowledge graph comorbidity edge and do not constitute supporting evidence for this repurposing hypothesis.

---

## Taiwan Market Information

Urofollitropin has **no approved products in Taiwan** as of the data cutoff (2026-05-01). The drug has not received marketing authorization from the Taiwan Food and Drug Administration (TFDA) under any brand name or dosage form. No license data is available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (TFDA package insert warnings, contraindications, drug interactions) could not be retrieved during this evaluation cycle. This constitutes a blocking data gap that prevents formal safety screening. The TFDA package insert PDF should be obtained and parsed before any further development activity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Urofollitropin are classified at L5 (model prediction only), supported by zero clinical trials and zero relevant publications across every disease category. Mechanistic review identified knowledge graph structural inflation — not genuine biological rationale — as the likely driver of high prediction scores. The top prediction of migraine disorder has no preclinical, translational, or clinical support whatsoever.

**To proceed, the following is needed:**

- **Resolve MOA data gap**: Retrieve Urofollitropin mechanism of action from DrugBank API to enable proper mechanistic plausibility assessment
- **Resolve safety data gap**: Download and parse the TFDA package insert PDF to enable S1-level safety screening (currently blocking)
- **Preclinical evidence search**: Before any further investment, conduct a targeted search on FSHR expression in trigeminal ganglia and hypothalamic pain circuits — animal model data would be the minimum bar to upgrade from L5
- **KG node audit**: Flag FSH/FSHR as a high-degree hub node in the TxGNN knowledge graph; predictions for neuroendocrine hormones with broad CNS receptor distribution should receive automatic plausibility filtering before ranking
- **Consider deprioritization**: With all 10 candidates at L5 and no mechanistic bridging evidence, Urofollitropin should be deprioritized relative to repurposing candidates with at least L3-level evidence in the current pipeline
---

