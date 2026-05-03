---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Travoprost
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

The txgnn-pipeline skill is for model training and deployment work — not directly applicable here. The task is to generate an evaluation report per the **Drug Repurposing Evaluation Report Prompt (v5)** system instructions. Proceeding with report generation now.

---

# Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a synthetic prostaglandin F2α (PGF2α) analogue and FP receptor agonist, internationally established as an ophthalmic solution for open-angle glaucoma and ocular hypertension, though it carries no current Taiwan regulatory registration.
The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**, with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (no Taiwan registration) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacological information, travoprost is a PGF2α analogue that acts as an FP receptor agonist. Its primary clinical use in glaucoma relies on enhanced uveoscleral aqueous outflow to reduce intraocular pressure. As a prostaglandin, travoprost also exerts vasodilatory activity on vascular smooth muscle — an effect clinically observed as conjunctival hyperemia and directly measured in at least one trial (NCT00308945), which quantified its impact on retinal vascular diameter and choroidal blood flow.

Visceral calciphylaxis is a rare, life-threatening condition defined by calcification and thrombotic occlusion of small blood vessels in visceral organs, leading to progressive tissue ischemia and necrosis. The theoretical mechanistic link proposed by TxGNN rests on the idea that prostaglandin-mediated vasodilation might improve local ischemia resulting from microvascular occlusion. However, calciphylaxis is fundamentally a disease of pathological vascular calcification — a structural and metabolic problem — and there is no established mechanism by which FP receptor agonism dissolves calcium deposits, reduces calcification load, or reverses established thrombotic occlusion.

The TxGNN model's near-perfect prediction score most likely reflects knowledge graph proximity between prostaglandin/vascular biology nodes and calcification/ischemic vascular disease nodes — an indirect, graph-inference-driven association rather than a direct mechanistic pathway. In the absence of any supporting clinical or preclinical evidence, this prediction must be classified as purely hypothesis-generating and does not warrant clinical exploration at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at Evidence Level L5 — supported solely by the TxGNN knowledge graph model with zero clinical trials, zero publications, and no established mechanistic pathway linking travoprost to visceral calciphylaxis. Travoprost is additionally not registered in Taiwan, and core safety data (warnings, contraindications, DDI) could not be retrieved, precluding even a basic safety screening (Decision Stage S0).

**To proceed, the following is needed:**
- Detailed mechanism of action data (FP receptor biology in the context of vascular calcification and ischemia)
- Preclinical studies (in vitro or animal model) evaluating prostaglandin F2α effects on vascular calcification or calciphylaxis pathology
- Route of administration feasibility assessment (ophthalmic topical → systemic exposure is extremely limited; a new delivery route would be required for visceral disease)
- Taiwan TFDA package insert review to extract warnings and contraindications
- Drug-drug interaction database query to complete safety screening
- Consideration of whether any prostaglandin E-series analogues (which have more established peripheral vascular evidence) might be a more plausible class for this hypothesis
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

