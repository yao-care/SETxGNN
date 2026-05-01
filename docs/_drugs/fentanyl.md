---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 2
---

# Fentanyl
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

The `txgnn-pipeline` skill confirms this is a standard TxGNN report generation task. Now let me analyze the Evidence Pack carefully and produce the report.

**Key observations from the data:**
- Fentanyl has **no Taiwan registrations** (0 licenses)
- Top prediction (NSIAD) has **0 trials + 0 literature** → L5
- The `repurposing_rationale` explicitly flags a **mechanistic worsening effect** (opioids stimulate ADH → aggravates NSIAD)
- All safety fields are `[Data Gap]`
- Fentanyl is NOT antineoplastic → no Cytotoxicity section

---

# Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid, used worldwide for severe pain management and anesthesia induction, but not currently registered in Taiwan.
The TxGNN model assigns **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)** as its top predicted new indication with a score of **99.46%**,
yet there are currently **0 clinical trials** and **0 publications** supporting this direction—and mechanistic analysis raises serious concerns that fentanyl may actually **worsen** the target condition rather than treat it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain management / Anesthesia (not registered in Taiwan; globally established use) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, fentanyl is a potent synthetic **μ-opioid receptor (μOR) full agonist**—one of the most widely used agents for severe acute pain and perioperative anesthesia worldwide. Its analgesic effect is mediated through binding to μOR in the central and peripheral nervous system, inhibiting ascending pain signal transmission.

**A critical mechanistic conflict exists with NSIAD.** Nephrogenic Syndrome of Inappropriate Antidiuresis is caused by gain-of-function mutations in the *AVPR2* gene, resulting in constitutive activation of the vasopressin V2 receptor (V2R) independent of ADH levels. This drives inappropriate water reabsorption, leading to dilutional hyponatremia. The therapeutic goal in NSIAD is to **reduce** V2R activity. However, opioid drugs—including fentanyl—are well-documented to **stimulate endogenous ADH (antidiuretic hormone) secretion**. This would further amplify signaling through an already over-activated V2R pathway, directly worsening the core pathology rather than resolving it. The mechanistic direction is diametrically opposed to the treatment goal.

The TxGNN model's high prediction score (99.46%) most likely reflects structural or topological feature similarity between fentanyl and NSIAD-related nodes within the knowledge graph (e.g., shared downstream signaling proteins or electrolyte-related pathways), rather than a true causal therapeutic relationship. This is a known limitation of graph neural network-based repurposing models: high scores reflect graph proximity, not mechanistic plausibility. This prediction warrants **expert pharmacological and clinical review before any further action**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Fentanyl is not currently registered or marketed in Taiwan. No product authorizations are on record in the regulatory database queried as of this evidence pack's data cutoff (2026-05-01).

> **Note:** Fentanyl is approved and widely used in many other jurisdictions (EU, US, Japan, etc.) for acute and chronic severe pain, cancer pain, and anesthesia. Its absence from Taiwan's registry does not reflect a lack of global clinical use.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug interactions) was not retrievable from the Taiwan regulatory database for this evidence pack, as fentanyl carries no Taiwan market authorization.

Please refer to the originating manufacturer's package insert and relevant national regulatory sources for complete safety information. Based on the drug's well-established pharmacological profile, the following are broadly recognized safety concerns that any clinical team should be aware of:

- **Respiratory depression**: The most serious risk with fentanyl; can be fatal, particularly in opioid-naive patients or with concurrent CNS depressants
- **Opioid dependence and abuse potential**: Fentanyl is a Schedule I/II controlled substance in most jurisdictions with high misuse and diversion risk
- **Hyponatremia risk**: Of direct relevance to NSIAD—opioid-induced ADH stimulation can cause or worsen hyponatremia, which is the primary morbidity in NSIAD patients

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate presents a compounding set of concerns: zero supporting clinical or literature evidence (L5), a mechanistic pathway that is **directionally opposed** to the therapeutic goal of NSIAD, and an unfavorable safety profile in the context of the target disease (opioid-induced ADH secretion aggravates NSIAD's core pathology). Advancing this candidate is not justified under current evidence.

**To proceed, the following would be needed:**

- **Mechanistic de-risking**: Independent pharmacological review to determine whether any indirect mechanism (e.g., via non-ADH opioid pathways, alternative receptor subtypes) could plausibly confer benefit in NSIAD—this review should explicitly address the ADH-worsening concern
- **Regulatory safety data**: Retrieval of the full package insert from a market where fentanyl is approved (e.g., Taiwan TFDA equivalents, EMA SmPC, or FDA prescribing information) to complete the S1 safety assessment
- **Preclinical evidence**: In vitro or animal model studies demonstrating any effect on V2R signaling or sodium homeostasis before any clinical hypothesis can be formed
- **Knowledge graph audit**: Review of the TxGNN graph topology around fentanyl and NSIAD nodes to understand the source of the high score and whether it reflects a true biological relationship or a graph artefact

> For reference, the second-ranked TxGNN prediction—**Tourette syndrome** (score: 99.05%)—also carries zero supporting evidence (L5, Hold), and its mechanistic rationale similarly conflicts with established opioid pharmacology. The overall repurposing signal for fentanyl in this evidence pack is considered unreliable without further mechanistic validation.
---

