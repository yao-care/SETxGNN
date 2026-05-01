---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

Now I have the necessary context. Let me generate the evaluation report based on the Evidence Pack, following the Drug Repurposing Evaluation Report Prompt (v5) format. The top predicted indication is **rheumatoid nodulosis** (rank 1), with no supporting evidence — and osteoarthritis (rank 7) carries the strongest mechanistic literature.

---

# TRETINOIN: From Acute Promyelocytic Leukemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (all-trans retinoic acid, ATRA) is a vitamin A derivative with internationally established clinical use in acute promyelocytic leukemia (APL) and acne vulgaris, though it carries no registered indications in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Nodulosis**, yet **no clinical trials** and **no supporting literature** exist for this specific direction — placing the prediction at the lowest evidence tier (L5).
Without any experimental validation, this signal is currently insufficient to support clinical development planning.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally used for acute promyelocytic leukemia and acne vulgaris |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the pipeline (DrugBank API query pending). Based on established pharmacological knowledge, Tretinoin is an endogenous retinoid that binds nuclear retinoic acid receptors (RAR-α, RAR-β, RAR-γ), acting as a transcriptional regulator of genes governing cellular differentiation, proliferation, and immune homeostasis. Its most clinically significant systemic role is inducing terminal differentiation of malignant promyelocytes in APL via degradation of the PML-RARα fusion protein; topically, it normalises follicular keratinocyte turnover in acne.

The immunomodulatory pathway is where TxGNN likely infers a connection to rheumatoid nodulosis. Retinoic acid is known to promote CD4⁺ regulatory T cells (Tregs) while suppressing pro-inflammatory Th17 differentiation, shifting the immune balance away from autoimmune-driven tissue damage. Rheumatoid nodulosis is a rare subtype of rheumatoid arthritis characterised by recurrent subcutaneous rheumatoid nodule formation (macrophage-driven granuloma) in a Th1/Th17-predominant inflammatory milieu, often with surprisingly mild articular disease.

However, this mechanistic inference remains entirely theoretical. The pathophysiology of rheumatoid nodulosis — granuloma formation anchored by activated macrophages and complement deposition — is distinct from classical RA synovitis, and systemic Th17 suppression may not address the local granuloma microenvironment. There are currently no preclinical animal models, in vitro studies, or clinical trial registrations testing this hypothesis. The TxGNN score should be interpreted as a computational signal only, requiring independent experimental validation before any further investment is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Tretinoin has no registered products in Taiwan. No authorizations on record.

---

## Cytotoxicity

Tretinoin (ATRA) is classified as an antineoplastic differentiating agent for APL treatment and meets the criteria for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Differentiating agent (Retinoid class) — not a conventional cytotoxic; acts via nuclear receptor transcriptional regulation, not DNA damage |
| Myelosuppression Risk | Low for tretinoin monotherapy; the primary haematological concern is **ATRA Differentiation Syndrome** (fever, respiratory distress, fluid retention, pleuropericardial effusion) rather than myelosuppression per se |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), serum triglycerides and cholesterol, signs of differentiation syndrome (SpO₂, chest X-ray), pregnancy status |
| Handling Protection | Standard chemotherapy precautions apply; highly teratogenic (Pregnancy Category X) — strict dual contraception and pregnancy avoidance protocols are mandatory for all patients of childbearing potential |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.84%), rheumatoid nodulosis is an evidence-empty indication for tretinoin — no preclinical studies, no clinical trials, and no supporting publications exist. The mechanistic link via Th17/Treg modulation is biologically plausible but unvalidated, and the unique granuloma-driven pathology of rheumatoid nodulosis makes extrapolation from general immunomodulatory data unreliable.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept**: In vitro macrophage polarisation and granuloma formation models, or murine models of rheumatoid nodule development, to test tretinoin's effect on the granuloma microenvironment
- **MOA data retrieval**: Complete the DrugBank API query (DG002) to formally document tretinoin's immunomodulatory targets and confirm overlap with rheumatoid nodulosis pathways
- **Safety data**: Obtain and parse the TFDA package insert PDF (DG001) to enable S1 safety pre-assessment; pay particular attention to teratogenicity management and differentiation syndrome risk in non-APL populations
- **Adjacent indication reassessment**: Consider prioritising **osteoarthritis** (TxGNN rank 7, L4 evidence, 20 publications including GWAS and mechanistic studies on the ALDH1A2/retinoic acid axis) as a stronger near-term research candidate; mechanistic literature there may also illuminate whether local vs. systemic RA concentration determines pro- or anti-inflammatory outcomes
- **Indication-specific feasibility review**: Given that rheumatoid nodulosis is a rare RA subtype with no disease-modifying treatment registrations, confirm target patient population size and clinical trial feasibility before any programme commitment
---

