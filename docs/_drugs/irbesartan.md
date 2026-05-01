---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using **txgnn-pipeline** context confirmed. Now generating the Irbesartan evaluation report based on the Evidence Pack.

---

# Irbesartan: From Diabetic Nephropathy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), clinically established for hypertension and diabetic nephropathy in patients with type 2 diabetes and proteinuria.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction confidence of 99.31%.
However, **no clinical trials and no publications** directly support this specific repurposing direction at this time; the current evidence is mechanistic in nature only (Level L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Diabetic nephropathy (Type 2 diabetes with proteinuria) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (Mechanistic rationale only; no clinical or preclinical studies retrieved) |
| Sweden Market Status | Not Marketed (0 authorizations on record) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data from DrugBank is not yet available for this report. Based on established pharmacological knowledge and information within this Evidence Pack, Irbesartan belongs to the angiotensin II type 1 (AT1) receptor antagonist class (ARB). By selectively blocking the AT1 receptor, it prevents angiotensin II from driving vasoconstriction, aldosterone secretion, and pro-fibrotic signalling — directly reducing blood pressure and intraglomerular hypertension, and suppressing TGF-β–mediated renal fibrosis.

Malignant hypertensive renal disease is a severe hypertensive emergency characterised by rapid-onset blood pressure elevation causing fibrinoid necrosis of renal arterioles and thrombotic microangiopathy. The core driver of this process is intense, pathological overactivation of the renin–angiotensin–aldosterone system (RAAS). Since irbesartan directly antagonises the primary RAAS effector — angiotensin II at the AT1 receptor — the mechanistic rationale for benefit in this condition is highly coherent.

The strongest supporting argument is the adjacent-indication principle: irbesartan is already approved for **diabetic nephropathy**, a condition where RAAS-mediated glomerular hyperperfusion, elevated intraglomerular pressure, and fibrosis are the central pathological mechanisms — exactly the same pathways implicated in malignant hypertensive renal injury. The TxGNN model's very high confidence score (99.31%, rank 1 of all predictions) is consistent with this mechanistic overlap, making this a scientifically plausible repurposing hypothesis worthy of structured investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Irbesartan in malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available directly linking Irbesartan to malignant hypertensive renal disease.

---

## Sweden Market Information

Irbesartan is currently not marketed in Sweden. No product authorizations are on record in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Safety data (TFDA package insert warnings, contraindications, and drug–drug interactions) could not be retrieved in this pipeline run. Before any clinical decision is made, the following known class-level risks must be evaluated:
> - ARBs are **contraindicated in bilateral renal artery stenosis** and in pregnancy.
> - In malignant hypertension specifically, rapid blood pressure reduction carries a risk of acute kidney injury due to sudden loss of pressure-dependent glomerular perfusion — the safety profile in this acute-severe context requires careful assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic rationale linking irbesartan's AT1 antagonism to malignant hypertensive renal disease is compelling and logically coherent, there are currently no clinical trials, published studies, or preclinical data directly supporting this repurposing application. Safety data could not be retrieved, and known class-level risks (acute kidney injury, bilateral RAS contraindication) are clinically significant in this patient population.

**To proceed, the following is needed:**

- **MOA data**: Retrieve formal mechanism of action record from DrugBank (DB01029) to complete the mechanistic dossier
- **Safety review**: Download and parse the full package insert (TFDA/EMA/FDA) to extract warnings, contraindications, and special population restrictions before any clinical evaluation
- **Class-level evidence review**: Conduct a systematic PubMed search for ARB class drugs (losartan, valsartan, candesartan) in malignant hypertension and hypertensive emergency with renal involvement — class-level evidence may support an informed extrapolation to irbesartan
- **Regulatory precedent check**: Verify whether irbesartan or any ARB has an approved or guideline-recommended role in hypertensive nephropathy crises (e.g., JNC 8, ESH/ESC hypertension guidelines, KDIGO)
- **Risk–benefit framing**: Evaluate whether the target population (malignant HTN with acute renal injury) represents a setting where ARBs are likely safe vs. contraindicated, given the acute nature of the disease
- **If evidence supports proceeding**: Design a prospective observational or pragmatic RCT protocol comparing ARB-based vs. standard regimens in patients presenting with malignant hypertensive renal disease
---

