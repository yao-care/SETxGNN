---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

The txgnn-pipeline skill confirms this is a Swedish TxGNN deployment report. Now I'll generate the evaluation report following the v5 format.

---

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

Ibuprofen is a well-established non-steroidal anti-inflammatory drug (NSAID), widely used for pain relief, fever reduction, and inflammatory conditions globally.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare inherited skeletal dysplasia caused by CDMP1/GDF5 mutations.
Currently, **no clinical trials** and **no publications** support this direction — this remains a model-only prediction at the lowest evidence level (L5), with a recommendation to **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in this market |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known pharmacology, Ibuprofen is a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, thereby dampening pain, fever, and inflammatory responses. Its safety and efficacy in these established indications are extensively documented over decades of clinical use.

Acromesomelic dysplasia, Hunter-Thompson type is a rare autosomal recessive disorder caused by loss-of-function mutations in CDMP1/GDF5, a bone morphogenetic protein (BMP) family member critical for limb cartilage and joint formation. The disease manifests as disproportionately short forearms and lower legs, with structural skeletal defects determined during embryonic development. This is fundamentally a fixed genetic structural lesion — not an inflammatory or prostaglandin-mediated process.

The mechanistic bridge from COX inhibition to GDF5 pathway rescue is extremely thin. While prostaglandins can theoretically modulate chondrocyte differentiation in vitro, there is no experimental or clinical evidence that Ibuprofen influences CDMP1/GDF5 signaling in a therapeutically meaningful way. The TxGNN prediction at rank 786 most likely reflects network-level co-association patterns between shared gene neighbors rather than a direct pharmacological rationale. This gap is consistent across all seven predicted indications in this pack, all of which involve rare congenital skeletal or developmental disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Sweden Market Information

Ibuprofen has no registered marketing authorizations in this market. No license data is available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven TxGNN-predicted indications for Ibuprofen are rare congenital skeletal or multi-system developmental syndromes (acromesomelic dysplasia, brachyolmia, brachydactyly-syndactyly syndrome, myosclerosis, pseudoachondroplasia, and others) with zero supporting clinical trials, zero supporting publications, and no plausible mechanistic link to COX inhibition. These diseases arise from fixed structural genetic defects established before or at birth, where anti-inflammatory intervention has no established therapeutic role. The predictions are network-model artifacts rather than biologically grounded hypotheses.

**To proceed, the following is needed:**

- **Mechanistic rationale**: In vitro or in vivo evidence that COX inhibition or prostaglandin reduction modulates the relevant pathways (GDF5/BMP signaling, TRPV4, COMP, TRIP11, FAM20A, COL6A, HOXD/BMP morphogenesis)
- **Preclinical data**: Animal model studies for at least the top-ranked indication (myosclerosis has relatively the highest mechanistic plausibility among the seven, as NSAIDs have limited anti-inflammatory effects in fibrotic disease)
- **Safety profile**: Package insert warnings, contraindications, and drug interaction data must be retrieved before any clinical evaluation stage can open
- **Regulatory status**: Ibuprofen registration data for the Sweden market should be confirmed, as this is a globally marketed OTC/Rx drug and the absence of authorizations in this database may reflect a data gap rather than true non-availability
- **TxGNN model audit**: Given that all top-7 predictions cluster around rare genetic skeletal dysplasias — an atypical pattern for a broad-spectrum NSAID — a review of whether Ibuprofen's graph representation in the knowledge graph accurately reflects its known indication space is warranted
---

