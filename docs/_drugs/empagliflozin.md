---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the `txgnn-pipeline` skill for context, and applying the Drug Repurposing Evaluation Report v5 format to the provided Evidence Pack. Note: Empagliflozin is not antineoplastic, so the Cytotoxicity section is omitted. Sweden Market Information section is also omitted as there are zero registered products.

---

# Empagliflozin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is a sodium-glucose cotransporter-2 (SGLT2) inhibitor, primarily used globally for type 2 diabetes mellitus, heart failure, and chronic kidney disease — however, no registered products were found in this dataset.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**,
with **0 clinical trials** and **0 publications** currently supporting this direction, making this an entirely model-driven prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no registered products found in dataset) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, empagliflozin is an SGLT2 inhibitor that reduces renal glucose reabsorption, leading to glucosuria, osmotic diuresis, and downstream cardiorenal protective effects. Its proven therapeutic benefits cover metabolic and cardiovascular-renal axes.

Focal stiff limb syndrome is a localized variant of stiff person syndrome (SPS), whose core pathology is the loss of inhibitory GABAergic neurotransmission in the spinal cord and brainstem, driven by autoantibodies against GAD65 (glutamic acid decarboxylase 65). This autoimmune neurological mechanism has no direct intersection with SGLT2 inhibition's known pharmacodynamic pathways.

A highly indirect mechanistic bridge has been proposed: SGLT2 inhibitors are known to suppress NF-κB signaling and NLRP3 inflammasome activation, thereby reducing pro-inflammatory cytokines such as IL-6 and TNF-α. In theory, this could provide a modest supplementary anti-inflammatory effect relevant to autoimmune neuroinflammation. However, no published evidence currently supports that this mechanism influences GAD65 antibody titers or clinical SPS symptoms. Furthermore, SGLT2 is predominantly expressed in renal proximal tubules with negligible central nervous system expression, making direct CNS action pharmacologically implausible. The high TxGNN score (0.99) most likely reflects the topological proximity of "metabolic disease – autoimmunity – nervous system" nodes in the knowledge graph, rather than a direct biological correspondence.

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
There is no clinical trial or published literature supporting the use of empagliflozin in focal stiff limb syndrome or any stiff person syndrome spectrum disorder, and the proposed mechanistic link is highly speculative and indirect — the TxGNN prediction is most likely an artifact of knowledge graph topology rather than actionable biological plausibility.

**To proceed, the following is needed:**
- Retrieve full mechanism of action (MOA) data from DrugBank to formally assess any indirect anti-inflammatory or neuroimmune pathways
- Obtain safety data (key warnings, contraindications, drug interactions) from the TFDA package insert or MPA/EMA product labeling
- Conduct a targeted literature review to determine whether any SGLT2 inhibitor class effect has been observed in CNS autoimmune conditions
- Commission preclinical feasibility assessment (in vitro GABAergic neuron models or SPS animal models) before any clinical hypothesis can be formulated
- Reassess TxGNN prediction in the context of alternative disease rankings — classic stiff person syndrome (rank 2) and opsismodysplasia (rank 3) share identical or near-identical scores, suggesting the model may not be discriminating meaningfully between these targets
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

