---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 7
---

# Valsartan
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the Valsartan evaluation report based on the Evidence Pack.

---

# Valsartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Valsartan is an angiotensin II type 1 receptor blocker (ARB) with established global approvals for hypertension and heart failure, though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **0 clinical trials** and **1 preclinical publication** currently supporting this direction.
The prediction score is extremely high (99.97%), reflecting strong graph-embedding alignment with RAAS-driven disease nodes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, heart failure (global approvals; not registered in Taiwan) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the Taiwan regulatory database for this drug. Based on established pharmacological knowledge, Valsartan selectively blocks the angiotensin II type 1 (AT1) receptor, thereby inhibiting the vasoconstrictive and aldosterone-releasing effects of angiotensin II — the downstream effector of the renin-angiotensin-aldosterone system (RAAS). Its efficacy in systemic hypertension and heart failure is globally proven across major regulatory agencies (FDA, EMA).

Malignant renovascular hypertension is defined by severe RAAS overactivation combined with fibrinoid necrosis of the afferent glomerular arterioles, leading to rapid-onset end-organ damage. Because Valsartan directly blocks AT1, it can theoretically attenuate angiotensin II-induced vasospasm and glomerular capillary hypertension — the two key pathological drivers in this condition. The mechanistic fit is therefore highly plausible and well-grounded in the drug's core pharmacology.

A 2001 animal study published in *Circulation* demonstrated that AT1 receptor blockade can prevent lethal malignant hypertension even in the absence of systemic blood pressure reduction, implicating kidney inflammation as an independent therapeutic target. While this evidence is preclinical and not specific to Valsartan as a branded compound, it directly validates the AT1 antagonism pathway. Escalation to prospective clinical investigation is the logical next step.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Animal/Preclinical | *Circulation* | AT1 receptor blockade prevents lethal malignant hypertension in an animal model independent of blood pressure reduction; kidney inflammation identified as a key mechanistic target |

---

## Taiwan Market Information

Valsartan is currently not registered or marketed in Taiwan. No authorized products appear in the TFDA database. The drug's safety and efficacy profile must therefore be referenced from international regulatory dossiers (FDA, EMA) and published literature.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert warnings and contraindications were not retrievable in this data cycle — see Data Gap DG001.)

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The mechanistic case for Valsartan in malignant renovascular hypertension is scientifically compelling — RAAS overactivation is the central pathological driver, and AT1 antagonism is Valsartan's direct mechanism — but supporting clinical evidence is currently limited to a single 2001 preclinical study. No registered clinical trials exist for this specific indication, leaving the evidence at L4 (preclinical only).

**To proceed, the following is needed:**

- **Prospective clinical data**: A dedicated observational study or controlled trial evaluating ARBs (ideally Valsartan specifically) in malignant renovascular hypertension patients
- **MOA documentation**: Retrieve formal DrugBank MOA record to close Data Gap DG002 and support mechanistic narrative
- **Safety profile**: Obtain TFDA package insert or reference EMA/FDA SmPC to close Data Gap DG001 before any clinical translation discussion
- **Market pathway assessment**: Since Valsartan is not marketed in Taiwan, evaluate whether a named-patient or off-label use pathway applies for research purposes
- **Consideration of Rank 6 indication**: *Chronic pulmonary heart disease* (L3, Proceed with Guardrails) has substantially richer clinical trial and literature evidence via the Sacubitril/Valsartan (LCZ696) data set; this may represent a higher-priority near-term repurposing candidate for parallel evaluation
---

