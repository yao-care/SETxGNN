---
layout: default
title: Treosulfan
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 1
---

# Treosulfan
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

Using `txgnn-pipeline` for context. Now generating the evaluation report based on the Evidence Pack.

---

# Treosulfan: From Myeloablative Conditioning to Diabetic Cataract

## One-Sentence Summary

Treosulfan is a bifunctional alkylating agent internationally approved as a myeloablative conditioning regimen prior to allogeneic haematopoietic stem cell transplantation (HSCT) in patients with haematological malignancies.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, with a prediction score of 99.01%; however, **no clinical trials or supporting publications** have been identified for this indication.
Evidence rests entirely on computational model prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myeloablative conditioning prior to allogeneic HSCT (haematological malignancies; based on international approvals — not registered in this market) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Treosulfan is a bifunctional alkylating agent whose primary cytotoxic and immunosuppressive effects are achieved through DNA cross-linking. It has been approved internationally (EMA-approved as Trecondi® since 2019) as a conditioning agent that intentionally ablates the recipient's bone marrow, enabling engraftment of donor stem cells. Its established clinical role is in haematological oncology, not ophthalmology.

Diabetic cataract develops through a distinct set of pathophysiological pathways: chronic hyperglycaemia drives excess polyol accumulation via the aldose reductase pathway, generates oxidative stress, and promotes non-enzymatic glycation of lens crystallins — all of which progressively cloud the lens. There is no well-characterised direct pharmacological link between alkylating DNA damage and these lens-specific metabolic processes.

The TxGNN model may be capturing indirect biological network connections — for example, shared protein interaction nodes, pathway co-membership, or transcriptomic similarity between alkylating agent responses and lens epithelial cell biology under diabetic stress. However, without mechanistic feasibility data or preclinical evidence, this prediction cannot be corroborated. The large gap between treosulfan's extreme systemic toxicity profile and an ophthalmic indication further complicates any straightforward repurposing path.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Treosulfan meets the criteria for antineoplastic classification: it is a bifunctional alkylating agent used in haematological cancer treatment and belongs to the same mechanistic family as busulfan.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Bifunctional alkylating agent (same class as busulfan) |
| Myelosuppression Risk | **Very High** — myeloablation is the intended therapeutic endpoint; profound pancytopenia (neutropenia, thrombocytopenia, anaemia) is expected and is managed within the HSCT programme framework |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential (daily during conditioning period), liver function tests (ALT, AST, bilirubin — sinusoidal obstruction syndrome risk), renal function (creatinine, eGFR), pulmonary function assessment |
| Handling Protection | Full cytotoxic handling measures required — closed-system drug transfer devices (CSTD), appropriate PPE, per institutional chemotherapy handling and disposal protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based entirely on TxGNN computational modelling (L5 evidence), with zero supporting clinical trials or publications identified. Beyond the absence of evidence, there is a fundamental mismatch between treosulfan's extreme myelotoxic profile — where the drug's therapeutic action *is* bone marrow destruction — and the requirements of an ophthalmic indication such as diabetic cataract, where patient safety would demand a completely different dosing paradigm and route of administration.

**To proceed, the following is needed:**
- **Mechanistic feasibility analysis**: identify specific biological pathways linking treosulfan's alkylating activity to lens epithelial cell survival, polyol metabolism, or oxidative stress in a diabetic context
- **Preclinical evidence**: in vitro lens epithelial cell studies or diabetic animal model experiments examining treosulfan's effect on cataractogenesis
- **TxGNN interpretability audit**: review which knowledge graph features (shared protein targets, pathway nodes, gene expression signatures) are driving this prediction, to assess biological plausibility
- **Route and dose reformulation assessment**: systemic myeloablative doses are incompatible with ophthalmic use; any repurposing would require a topical or intravitreal route with an entirely different pharmacokinetic profile and safety characterisation
- **MOA documentation**: retrieve full DrugBank mechanism of action data to enable proper mechanistic-link analysis
---

