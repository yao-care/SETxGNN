---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: Drug Repurposing Evaluation Report

## One-Sentence Summary

Ambrisentan is an endothelin receptor antagonist (selective ETA antagonist) approved internationally for the treatment of **pulmonary arterial hypertension (PAH)**. The TxGNN model has **not yet generated predicted new indications** for this drug, and the evidence pack currently contains significant data gaps that must be resolved before a meaningful repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Ambrisentan |
| DrugBank ID | DB06403 |
| Original Indication | Not recorded in current evidence pack (known internationally: Pulmonary Arterial Hypertension) |
| Predicted New Indication | — (No predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions or supporting studies in this pack) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses (TFDA) | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. Based on publicly known pharmacological information, Ambrisentan is a **selective endothelin type-A (ETA) receptor antagonist**. It blocks the binding of endothelin-1 (ET-1) to ETA receptors on pulmonary artery smooth muscle cells, resulting in vasodilation and reduced pulmonary vascular resistance. It is approved in many countries (e.g., US as Letairis®, EU as Volibris®) for the treatment of pulmonary arterial hypertension (PAH, WHO Group I).

Because the TxGNN model has **not yet produced any predicted indications** for Ambrisentan in this evidence pack, no mechanistic plausibility assessment for a new indication can be performed at this time. Once predictions are generated, the endothelin pathway's involvement in fibrosis, cardiovascular remodelling, and other vascular diseases could provide biologically plausible rationales for repurposing.

---

## Clinical Trial Evidence

No predicted indications are available in this evidence pack; therefore, no indication-specific clinical trial search was performed.

> Currently no related clinical trials registered for a new predicted indication.

---

## Literature Evidence

No predicted indications are available in this evidence pack; therefore, no indication-specific literature search was performed.

> Currently no related literature available for a new predicted indication.

---

## Taiwan Market Information

Ambrisentan currently holds **no TFDA licenses** and is **not marketed in Taiwan**.

> No authorization records found in the TFDA database.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.
>
> **Note for reference (based on international labelling):** Ambrisentan carries a **boxed warning for embryo-fetal toxicity** (Category X) and is contraindicated in pregnancy. It is also associated with peripheral oedema, decreased haemoglobin/haematocrit, and potential hepatotoxicity. A Risk Evaluation and Mitigation Strategy (REMS) programme applies in some jurisdictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Ambrisentan contains critical data gaps and, most importantly, **no TxGNN-predicted new indications**. Without a target indication, no repurposing evaluation pathway can be initiated. Additionally, Ambrisentan is not marketed in Taiwan, which adds regulatory complexity to any future repurposing effort.

**To proceed, the following is needed:**

1. **TxGNN Prediction Run** — Execute the TxGNN model for Ambrisentan (DB06403) to generate candidate new indications with prediction scores
2. **MOA Data** — Retrieve detailed mechanism of action from DrugBank API (resolves data gap DG002)
3. **TFDA Package Insert / Safety Data** — Obtain and parse the package insert for key warnings and contraindications (resolves data gap DG001), or source from international regulatory databases (FDA, EMA) given the drug is not marketed in Taiwan
4. **Drug-Drug Interaction Data** — Query additional DDI databases (e.g., DrugBank interactions endpoint) to populate the safety profile
5. **Regulatory Pathway Assessment** — Evaluate whether an import drug license or clinical trial application would be required in Taiwan given the current non-marketed status

---

*Report generated: 2026-04-03 | Evidence Pack version: v4 | Candidate ID: TW-DB06403-multi*

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
---

