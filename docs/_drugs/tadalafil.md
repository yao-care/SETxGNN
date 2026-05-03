---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Tadalafil: From Erectile Dysfunction to Ambras Syndrome Hypertrichosis

## One-Sentence Summary

Tadalafil is a selective phosphodiesterase type 5 (PDE5) inhibitor approved globally for erectile dysfunction, pulmonary arterial hypertension, and benign prostatic hyperplasia, though no Taiwan TFDA registration was found in this dataset.
The TxGNN model ranks **Ambras type hypertrichosis universalis congenita** as its top new indication with a prediction score of **99.98%**,
however **no clinical trials and no supporting literature** exist for this direction, placing evidence entirely at **Level L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile Dysfunction / Pulmonary Arterial Hypertension (globally approved; Taiwan TFDA registration not found in dataset) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (0 registrations found) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, tadalafil is a selective inhibitor of phosphodiesterase type 5 (PDE5), the enzyme that degrades cyclic guanosine monophosphate (cGMP). By inhibiting PDE5, tadalafil raises intracellular cGMP levels, inducing smooth muscle relaxation and vasodilation — the basis for its approved efficacy in erectile dysfunction, pulmonary arterial hypertension (PAH), and benign prostatic hyperplasia.

Ambras type hypertrichosis universalis congenita is an extremely rare genetic disorder caused by mutations in the **TRPS1 gene** (chromosome 8q), resulting in dense hair growth across the entire body from birth. This is a structural genetic defect that lies entirely outside the PDE5/cGMP signaling pathway. While PDE5 inhibition can theoretically alter blood flow in hair follicle microenvironments, it cannot correct the underlying gene-level defect driving Ambras syndrome. The mechanistic rationale for this TxGNN prediction is therefore extremely weak, and the model's high confidence score likely reflects graph topology proximity rather than biological plausibility.

It is worth highlighting that among all eight predicted indications in this pack, **kyphoscoliotic heart disease (rank 7)** stands out as the most mechanistically coherent candidate: spinal deformity causes restrictive lung disease, which secondarily drives pulmonary arterial hypertension — a condition directly and mechanistically addressable by tadalafil's approved PAH indication (Adcirca®). This prediction deserves separate evaluation priority even though it ranks lower in the TxGNN output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Taiwan FDA records returned **0 approved registrations** for tadalafil at the time of data collection (March 2026). This is an anomalous finding: tadalafil (Cialis®, Adcirca®) holds regulatory approval in the United States, European Union, Japan, and many other jurisdictions. This result likely reflects a query limitation or a registration filed under a brand name rather than the INN. **Direct verification with the Taiwan Food and Drug Administration is strongly recommended before drawing any market access conclusions.**

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Safety Signal Identified:** Among all eight predicted indications analyzed in this pack, one piece of retrieved literature — [PMID 17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) (Dinn & Wall, *Cephalalgia*, 2006) — is an **adverse event case report** describing tadalafil-associated migraine aura, not a therapeutic application. The mechanism is consistent with known pharmacology: PDE5 inhibition elevates cGMP, promotes cerebrovascular dilation, and may trigger cortical spreading depression (CSD) — the established neurophysiological basis of migraine aura. This finding indicates the predicted indication "migraine with brainstem aura" (rank 8) should be treated as a **contraindication signal**, not a repurposing opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication (Ambras type hypertrichosis universalis congenita) is a rare monogenic disorder with no mechanistic link to PDE5 inhibition and zero supporting clinical or preclinical evidence. All eight predicted indications are rated L5 with Hold recommendations, with the single exception of kyphoscoliotic heart disease (rank 7, L4), which has a mechanistically sound but currently unsubstantiated case. Additionally, the only retrieved literature across all indications is an adverse event report, not a treatment signal.

**To proceed, the following is needed:**

- **Resolve Taiwan registration data gap**: Query TFDA by brand name (Cialis®, Adcirca®) and verify market status; the 0-license result is inconsistent with tadalafil's global regulatory standing
- **Retrieve MOA and safety data** (Data Gaps DG001 & DG002): Download TFDA package insert PDF for contraindications and warnings; query DrugBank API for complete mechanistic profile
- **Prioritize kyphoscoliotic heart disease (rank 7) for a dedicated evidence search**: Conduct a focused PubMed/ClinicalTrials search combining tadalafil, PAH, and restrictive lung/kyphoscoliosis; this is the only predicted indication with a biologically credible path forward
- **Do not pursue hair-disorder indications (ranks 1–3, 5–6)** without preclinical evidence: the entire hypertrichosis/trichomegaly/hair-shaft cluster lacks mechanistic grounding and should be deprioritized until cGMP-hair follicle axis studies emerge
- **Flag rank 8 (migraine with brainstem aura) as a safety exclusion**: Tadalafil should be avoided in patients with migraine with aura history; document this as a prescribing caution in any future clinical planning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

