---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

The txgnn-pipeline skill confirms this is a standard TxGNN repurposing report task. Now generating the full report from the Evidence Pack.

---

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib (Iressa®) is a first-generation EGFR tyrosine kinase inhibitor, clinically established for the treatment of EGFR-mutation-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**,
with **no clinical trials** and **no published literature** currently supporting this direction.
At an L5 evidence level, this prediction rests entirely on computational modeling and carries insufficient support for clinical progression at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-small cell lung cancer (EGFR-mutation positive) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on contextual information within the accompanying literature, Gefitinib is a selective inhibitor of the EGFR (epidermal growth factor receptor) tyrosine kinase domain. It competitively blocks the ATP-binding site of EGFR and suppresses downstream signaling cascades — including RAS/MAPK and PI3K/AKT — that govern cell proliferation, survival, and angiogenesis. It was the first EGFR TKI approved globally for NSCLC patients harboring sensitizing mutations in exons 19 and 21.

Gingival fibromatosis is a rare condition involving diffuse, benign overgrowth of gingival connective tissue driven by excessive fibroblast proliferation and collagen deposition. Because EGFR signaling participates in fibroblast activation in general, there is a theoretical basis for the idea that EGFR inhibition might slow this overgrowth. This is the probable mechanistic pathway the TxGNN knowledge graph is exploiting to generate this prediction.

However, the primary etiological drivers of gingival fibromatosis are either germline mutations (SOS1, RASA1) or drug-induced overgrowth caused by phenytoin, cyclosporin, or nifedipine — none of which involves EGFR as a central or rate-limiting pathway. The mechanistic link is therefore indirect at best. The very high prediction score (99.89%) most likely reflects a network proximity artifact in the knowledge graph rather than a direct biological connection, and should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (EGFR-targeted therapy for NSCLC).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — First-generation EGFR tyrosine kinase inhibitor (4-anilinoquinazoline class) |
| Myelosuppression Risk | Low — EGFR TKIs are not associated with significant bone marrow suppression; this is distinct from conventional cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST/bilirubin), pulmonary symptoms (interstitial lung disease/pneumonitis — reported in post-marketing data), QTc interval (hERG channel blockade and QT prolongation documented), skin reactions (acneiform rash, paronychia, xerosis — occurring in >50% of patients) |
| Handling Protection | Standard cytotoxic drug handling precautions apply per institutional guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, observational study, or published literature directly linking gefitinib to gingival fibromatosis, and the mechanistic rationale is weak — EGFR is not a primary driver of this condition. A TxGNN score of 99.89% alone, at L5 evidence, is insufficient to justify further development investment.

**To proceed, the following is needed:**
- Preclinical experiments (in vitro fibroblast proliferation assays, and ideally an in vivo gingival fibromatosis model) evaluating the effect of EGFR inhibition
- Mechanistic evidence confirming that EGFR pathway activity is upregulated and functionally relevant in gingival fibromatosis tissue
- Formal MOA documentation retrieved from DrugBank API (to address DG002)
- TFDA package insert safety data — warnings and contraindications (to address DG001)
- Review of known EGFR inhibitor dermatological and mucosal toxicity profiles to assess whether gefitinib's known side effects (acneiform rash, mucosal changes) could confound or worsen gingival tissue in this patient population
---

