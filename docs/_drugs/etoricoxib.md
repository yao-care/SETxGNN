---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Etoricoxib: From Arthritis & Musculoskeletal Pain to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor approved in multiple countries for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, and acute pain, but not currently approved in Taiwan.
The TxGNN model predicts it may be effective for **Migraine Disorder**, yielding a mechanistic plausibility score of **99.90%**.
However, this specific prediction is currently supported by **zero clinical trials and no direct literature** — though closely related predictions for broader headache disorders (ranks #9 and #10) do show supporting case evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TFDA approval on record; globally used for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, and acute pain |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Taiwan (TFDA) Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Etoricoxib is a highly selective COX-2 inhibitor. Its primary mechanism involves blocking cyclooxygenase-2, thereby suppressing the production of prostaglandin E₂ (PGE₂) — a key mediator of neurogenic inflammation and peripheral/central pain sensitization. In migraine pathophysiology, PGE₂ plays a documented role in activating and sensitizing the trigeminovascular system, which drives the characteristic throbbing pain of migraine attacks. This mechanistic overlap gives the TxGNN knowledge graph a biologically plausible reason to connect Etoricoxib with migraine disorder.

The prediction gains indirect support from two closely related indications predicted by the same model. For **headache disorder** (rank #9, Evidence Level L4), published case reports and case series document that Etoricoxib — like indomethacin — can effectively treat indomethacin-responsive headache syndromes including idiopathic stabbing headache, primary cough headache, and paroxysmal hemicranias. For **trigeminal autonomic cephalalgia** (rank #10, Evidence Level L4), a case series shows Etoricoxib and celecoxib can substitute for indomethacin in patients who cannot tolerate the latter. These findings suggest a class effect among selective COX-2 inhibitors across the broader family of primary headache disorders.

That said, migraine disorder as a standalone indication currently has no dedicated clinical trial and no direct pharmacological literature for Etoricoxib. The 99.90% TxGNN score reflects knowledge graph proximity and mechanistic plausibility, not confirmed clinical efficacy. Bridging this gap would require purpose-designed proof-of-concept studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Etoricoxib in migraine disorder.

---

## Literature Evidence

Currently no related literature available for Etoricoxib in migraine disorder.

---

## Taiwan (TFDA) Market Information

Etoricoxib is not currently approved by the Taiwan Food and Drug Administration (TFDA). No domestic product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Additional safety signal from evidence pack**: A case report ([PMID 21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/)) describes a 75-year-old patient who developed life-threatening hyperkalemia and acute kidney dysfunction after receiving Etoricoxib 90 mg daily for 3 days, while concurrently taking telmisartan (an ARB) and a low-sodium/high-potassium diet. This highlights the importance of monitoring renal function and serum electrolytes in elderly patients or those on renin-angiotensin-aldosterone system (RAAS)-blocking agents.
>
> **Mechanistic safety concern for pulmonary hypertension**: COX-2 inhibition suppresses prostacyclin (PGI₂), an endogenous pulmonary vasodilator. Patients with pre-existing pulmonary hypertension should be considered a contraindicated or high-caution population for Etoricoxib.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for migraine disorder carries strong mechanistic plausibility supported by Etoricoxib's COX-2 inhibitory mechanism, but the complete absence of dedicated clinical trials or direct literature means this cannot progress beyond hypothesis generation at this stage (Evidence Level L5).

**To proceed, the following is needed:**

- **Confirm MOA documentation**: Obtain formal DrugBank or SmPC mechanistic data, as MOA is currently flagged as a data gap
- **Review indomethacin-responsive headache evidence**: Cross-reference case evidence from rank #9 (headache disorder) and rank #10 (trigeminal autonomic cephalalgia) to determine if migraine subpopulations — particularly those with COX-responsive features — overlap sufficiently to justify a repurposing protocol
- **Design a proof-of-concept study**: A small Phase 2 pilot or pragmatic observational study comparing Etoricoxib against existing migraine prophylaxis options would be the minimum threshold to advance beyond L5
- **Cardiovascular and renal risk assessment**: As a COX-2 selective inhibitor, Etoricoxib carries a known cardiovascular thrombotic signal (increased MI/stroke risk) and renal function risks. A migraine population is typically younger, but comorbidity screening is required before any study design
- **TFDA regulatory pathway review**: Since Etoricoxib has no current Taiwan approval, any clinical repurposing study would require an IND filing and engagement with TFDA
---

