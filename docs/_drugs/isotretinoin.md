---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

---

# Isotretinoin: From Severe Acne to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is a synthetic retinoid (vitamin A derivative) best known for treating severe nodular acne unresponsive to conventional therapy. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, yet **no clinical trials or publications** currently support this specific direction. The prediction rests entirely on computational modelling, and substantial pre-clinical and clinical evidence must be generated before any repurposing attempt can be seriously considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe nodular acne (primary known use; no formal licence record available in this dataset) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, isotretinoin is a synthetic 13-*cis*-retinoic acid that acts as a retinoic acid receptor (RAR) agonist. This RAR signalling pathway has a documented — though incompletely characterised — crosstalk with the renin-angiotensin system (RAS): all-trans retinoic acid (ATRA) has been shown in basic research to suppress angiotensinogen (*AGT*) gene expression and down-regulate renin receptor activity. Theoretically, this could reduce renin-dependent blood pressure elevation. Separately, *in vitro* studies demonstrate that ATRA inhibits vascular smooth muscle cell proliferation, which may slow the progressive renovascular remodelling that defines malignant renovascular hypertension.

Malignant renovascular hypertension is a rare, life-threatening condition driven by renal artery stenosis and runaway renin secretion leading to end-organ damage. If isotretinoin's RAR-mediated RAS suppression were to translate into a meaningful clinical effect, it could theoretically complement existing antihypertensive regimens. The TxGNN model likely captures these pathway-level associations, which explains the high computational score.

That said, this mechanistic link is entirely inferential — derived from basic science and structurally related retinoid research, not from any study in patients with malignant renovascular hypertension. Additionally, isotretinoin is known to elevate serum triglycerides and adversely affect lipid metabolism. In patients with already compromised cardiovascular and renal function, this side-effect profile introduces meaningful risks that have never been formally evaluated in this population.

> A closely related prediction, **Malignant Hypertensive Renal Disease** (TxGNN rank 2468, identical score 99.01%), shares the same mechanistic logic — isotretinoin's anti-fibrotic potential via RAR/RXR-mediated suppression of TGF-β-driven renal tubular epithelial–mesenchymal transition (EMT). Both predictions appear to reflect the same underlying network signal across two adjacent disease nodes, reinforcing the biological hypothesis while also confirming the absence of clinical evidence for either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Sweden Market Information

Isotretinoin currently holds no marketing authorisation on record. No licence data is available for this compound in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN computational score (99.01%), there is zero supporting clinical or published evidence for isotretinoin in malignant renovascular hypertension. The mechanistic rationale — RAR-mediated RAS suppression and anti-proliferative effects on vascular smooth muscle — is biologically plausible but entirely speculative, and isotretinoin's known triglyceride-raising and teratogenic risks pose uncharacterised dangers in a hypertensive, renally compromised population.

**To proceed, the following is needed:**

- **MOA confirmation:** Retrieve full mechanism of action and DrugBank category data to formally verify RAR/RAS pathway involvement
- **Safety profile completion:** Obtain the full package insert (warnings, contraindications, drug interactions) — currently a blocking data gap — before any safety evaluation can begin
- **Targeted literature review:** Commission a systematic search on retinoids and the renin-angiotensin system in hypertension and renal disease to surface indirect supportive evidence
- **Pre-clinical validation:** Conduct animal model studies in malignant renovascular hypertension to establish proof-of-concept before human study design
- **Cardiovascular/renal risk assessment:** Formally evaluate isotretinoin-induced hypertriglyceridaemia and any nephrotoxic signals in the intended patient population
- **Regulatory mapping:** Confirm whether any jurisdiction has approved isotretinoin for any cardiovascular or renal indication, which could reduce the regulatory pathway burden
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

