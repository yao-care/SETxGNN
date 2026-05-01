---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Ramipril
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

The `txgnn-pipeline` skill confirms this is a TxGNN drug repurposing report task. Now I'll generate the full evaluation report following the v5 prompt specification.

---

# Ramipril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Ramipril is a well-established ACE inhibitor (angiotensin-converting enzyme inhibitor) widely used for hypertension, heart failure, and long-term cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (Group 3 PH)**,
with **0 clinical trials** and **20 publications** currently retrieved — though none of the publications directly evaluate ramipril for this specific indication; all are general hypoxia biology reviews.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / cardiovascular risk reduction (no Taiwan registration on file) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 — Background mechanism studies only; no direct clinical trials |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack (Data Gap DG002). Based on established pharmacological knowledge, ramipril is an ACE inhibitor that blocks the enzyme responsible for converting angiotensin I into angiotensin II (Ang II). By suppressing Ang II, ramipril reduces systemic vasoconstriction, lowers aldosterone-driven fluid retention, and limits vascular remodeling — effects that form the foundation of its use in hypertension, systolic heart failure, post-myocardial infarction protection, and CKD progression (REIN trial, HOPE trial).

The mechanistic bridge to Group 3 pulmonary hypertension lies in the renin-angiotensin system (RAS). Chronic hypoxia activates the RAS, promoting pulmonary vasoconstriction and vascular smooth muscle remodeling. Theoretically, ACE inhibition could attenuate these pathological changes by reducing Ang II signaling in the pulmonary vasculature — an attractive hypothesis for a class of drugs with a long safety track record.

However, this hypothesis carries important clinical caveats. The role of ACE inhibitors in Group 3 PH has not been established in clinical practice. Unlike pulmonary arterial hypertension (Group 1), Group 3 PH management primarily targets the underlying lung disease. Systemic vasodilation from ramipril could worsen ventilation-perfusion (V/Q) mismatch and impair oxygenation in patients already compromised by lung disease — a safety concern that distinguishes this from standard hypertension use. None of the 20 retrieved publications address ramipril in this context; the evidence base is entirely indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **Important caveat**: All publications below are general hypoxia biology reviews. None directly evaluate ramipril for pulmonary hypertension owing to lung disease and/or hypoxia. Their relevance to this repurposing hypothesis is indirect background context only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Reviews the four core mechanisms of hypoxemia (hypoventilation, V/Q mismatch, shunt, low inspired O₂) — provides essential pathophysiological framework for Group 3 PH |
| [9446167](https://pubmed.ncbi.nlm.nih.gov/9446167/) | 1997 | Review | Revue Medicale de Liege | Describes hepatopulmonary syndrome as a model of pulmonary vascular dysregulation driven by systemic disease; relevant to hypoxia-PH linkage |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Overviews hypoxia-mediated biology including HIF-1α signaling, angiogenesis, and pH homeostasis; background for RAS-hypoxia interaction |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Examines HIF pathway's role in innate immunity and inflammatory hypoxia; contextualizes inflammation in hypoxic vascular disease |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Discusses strategies to therapeutically modify tumor hypoxia; methodology relevant to hypoxia intervention concepts |
| [28219680](https://pubmed.ncbi.nlm.nih.gov/28219680/) | 2017 | Review | Experimental Cell Research | Reviews HIF-mediated transcriptional repression under hypoxia; mechanistic context for oxygen-sensing pathways |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Examines hypoxia's dual role in neurodegeneration vs. neuroprotection, including altitude and pulmonary disease contexts |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Reviews clinical and molecular mechanisms of cognitive impairment under acute and chronic hypoxia |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Revista Medica del IMSS | Discusses hypobaric hypoxia at altitude and physiological/genetic adaptation; most recent publication in the set |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Review | Journal of Applied Physiology | Translational overview of hypoxia research priorities; editorial commentary |

---

## Taiwan Market Information

Ramipril has no registered products with the Taiwan Food and Drug Administration (TFDA). No authorizations are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: TFDA package insert data (warning labels and contraindications) could not be retrieved (Data Gap DG001, severity: Blocking). This gap must be resolved before any clinical translation work proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.93%), no clinical trials and no direct pharmacological studies support ramipril in Group 3 pulmonary hypertension. The mechanistic hypothesis is biologically plausible but clinically unvalidated, and systemic ACE inhibition carries a real risk of worsening hypoxia in this patient population by aggravating V/Q mismatch.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001 (Blocking)**: Retrieve and review the TFDA package insert to screen for contraindications relevant to hypoxic lung disease patients (e.g., bilateral renal artery stenosis, pregnancy, hypotension risk)
- **Resolve Data Gap DG002 (High)**: Confirm ramipril's full MOA from DrugBank to substantiate or refute the RAS-hypoxia mechanistic link
- **Targeted literature search**: Search specifically for ACEI class evidence in Group 3 PH (e.g., "ACE inhibitor AND hypoxic pulmonary hypertension" or "ramipril AND pulmonary vascular remodeling")
- **Preclinical signal check**: Identify whether any animal model data demonstrates ACE inhibition reduces hypoxic pulmonary vasoconstriction without compromising gas exchange
- **Safety signal review**: Consult pulmonary hypertension clinical guidelines (ESC/ERS 2022) for any existing recommendations or warnings regarding ACEI use in Group 3 PH
- **Compare with rank-10 indication**: The cerebral artery occlusion prediction (rank 10, Evidence Level L3, decision stage S2) has stronger direct evidence for ramipril and may represent a higher-priority repurposing candidate for near-term evaluation
---

