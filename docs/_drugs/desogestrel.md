---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: Drug Repurposing Evaluation Report

## One-Sentence Summary

Desogestrel is a third-generation progestogen widely used as an oral contraceptive.
The TxGNN model has **not yet generated predicted new indications** for this drug,
and there are currently **no clinical trials** or **publications** linked to a repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral contraception (progestogen-only) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions or supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Desogestrel is a synthetic progestogen (third-generation) that is metabolized to its active form etonogestrel. It exerts contraceptive effects primarily by inhibiting ovulation through suppression of gonadotropins (LH surge) and by altering cervical mucus consistency.

Since the TxGNN model has not produced any predicted new indications for Desogestrel at this time, no mechanism-based plausibility assessment can be performed. The absence of a prediction may reflect limited connectivity in the knowledge graph or insufficient signal for novel disease associations beyond its established hormonal/contraceptive use.

Further data enrichment — including full MOA annotation from DrugBank and expanded knowledge graph features — would be needed before the model can generate meaningful repurposing candidates for this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered for any repurposing indication.

## Literature Evidence

Currently no related literature available for any repurposing indication.

## Taiwan Market Information

Desogestrel currently holds **no TFDA authorizations** in Taiwan. No product is marketed domestically.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No authorizations found |

> Note: Desogestrel-containing products (e.g., Cerazette®, Mercilon®) are available in other markets (EU, US) but have not been registered with the TFDA.

## Safety Considerations

> Please refer to the package insert for safety information. TFDA package insert warnings, contraindications, and drug–drug interaction data were not available for this drug in Taiwan.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions have been generated for Desogestrel, and the drug is not marketed in Taiwan (0 TFDA authorizations). Without a candidate indication, there is no actionable repurposing hypothesis to evaluate at this time.

**To proceed, the following is needed:**
- **Mechanism of action data (MOA):** Query DrugBank API to obtain full pharmacological target and pathway annotations (Data Gap DG002)
- **TFDA package insert warnings/contraindications:** Download and parse available package insert PDFs to enable safety assessment (Data Gap DG001, Blocking)
- **TxGNN model re-run:** Ensure Desogestrel (DB00304) and its active metabolite etonogestrel (DB00294) are properly represented in the knowledge graph, then re-execute the prediction pipeline
- **Regulatory pathway exploration:** If a prediction emerges, assess whether an import drug application or clinical trial authorization would be required given the drug's current non-marketed status in Taiwan
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

