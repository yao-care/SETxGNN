---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

Using **txgnn-pipeline** context confirmed. Now generating the evaluation report based on the Evidence Pack.

---

# Ketoprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) of the propionic acid class, widely used globally for the relief of pain and inflammation, though it holds no registered authorizations in Sweden.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare genetic skeletal disorder — with a score of 99.98%.
However, this prediction is supported by **no clinical trials and no published literature**, placing it at evidence level L5 (model output only), and the mechanistic rationale is critically weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Sweden (NSAID; commonly indicated for pain and inflammation) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ketoprofen in this dataset. Based on established pharmacological knowledge, Ketoprofen is a non-selective COX-1 and COX-2 inhibitor. It reduces the synthesis of prostaglandins, thromboxanes, and prostacyclin, producing analgesic, anti-inflammatory, and antipyretic effects. NSAID-class drugs (including Ketoprofen, naproxen, and diclofenac) are recognized as first-line treatments for inflammatory arthropathies such as spondyloarthropathy.

Acromesomelic dysplasia, Hunter-Thompson type, however, is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the **CDMP1 (GDF5)** gene. This results in impaired BMP/GDF5 signalling during embryonic limb development, producing characteristic severe shortening of the middle and distal limb segments. It is a purely structural, genetically determined morphological disorder — there is no established inflammatory component in its pathophysiology that would serve as a pharmacological target for a COX inhibitor.

**The mechanistic link between Ketoprofen's COX inhibition and this skeletal dysplasia is essentially absent.** No amount of prostaglandin suppression can correct a genetically encoded defect in bone morphogenesis. The TxGNN model's high prediction score most likely reflects non-specific associations between "skeletal disease" nodes in the biomedical knowledge graph rather than a true mechanistic relationship. This prediction should be treated as a probable false positive and should not advance to clinical investigation without compelling new mechanistic evidence.

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
Acromesomelic dysplasia, Hunter-Thompson type is a genetically determined structural disorder of skeletal development (CDMP1/GDF5 pathway) with no meaningful overlap with the COX-inhibition mechanism of Ketoprofen; the absence of any supporting clinical trials or literature, combined with a mechanistically implausible pathway, makes advancement unjustifiable at this stage.

**To proceed, the following is needed:**

- **Mechanistic re-evaluation:** Identify any theoretical link between COX/prostaglandin pathways and CDMP1/GDF5 BMP signalling before any further steps are considered
- **MOA documentation:** Complete Ketoprofen MOA data should be retrieved from DrugBank API to support a full mechanistic assessment
- **Safety data:** Package insert review (TFDA/EMA) required to populate key warnings and contraindications before any S1 safety evaluation can begin
- **Knowledge graph audit:** Investigate why TxGNN assigns rank 68 to this indication — likely a "skeletal disease" cluster artefact that may require graph curation
- **Alternative indication review:** Rank 8 (Spondyloarthropathy) represents a far more mechanistically plausible repurposing target for Ketoprofen and warrants a separate, prioritised evaluation
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

