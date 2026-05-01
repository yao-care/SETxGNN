---
layout: default
title: Metronidazol
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Metronidazol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Metronidazole: Drug Repurposing Pre-Screening Report

## One-Sentence Summary

Metronidazole (INN: METRONIDAZOL) is a well-established antimicrobial agent widely used for anaerobic bacterial and protozoal infections.
This Evidence Pack contains **no TxGNN-predicted indications**, no clinical trial evidence, and no literature evidence — the pipeline did not return a repurposing candidate for evaluation.
The current data state is insufficient to produce a full repurposing assessment; a **Hold** decision is recommended until the data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication recorded in Sweden |
| Predicted New Indication | Not available — predicted_indications list is empty |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Could Be Generated

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological knowledge, Metronidazole belongs to the nitroimidazole class; its activity against anaerobes and protozoa has been extensively proven clinically. However, because the TxGNN model returned an **empty predicted_indications array**, there is no model-generated repurposing candidate to evaluate, and no mechanistic bridge to a new indication can be assessed at this stage.

The most probable cause is a **drug identity resolution failure**: the query used the spelling `METRONIDAZOL` (INN without the final "e"), which may not have matched the node label used in the TxGNN knowledge graph. The DrugBank query did return one result (query_log id 3), but the resolved data was not populated into the drug fields, suggesting a downstream mapping error.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack returned zero predicted indications and zero approved authorizations in Sweden, leaving no repurposing candidate to assess. The pipeline cannot be evaluated until the data gaps below are resolved.

**To proceed, the following is needed:**

- **Re-run TxGNN query** using the correct node identifier — try `Metronidazole` (with final "e"), DrugBank ID `DB00916`, and MeSH concept `D008795` to ensure graph node matching
- **Populate MOA data from DrugBank** — the DrugBank query succeeded (result_count: 1) but the data was not written into `drug.original_moa`; extract pharmacodynamics, mechanism, and categories from that record
- **Retrieve package insert warnings** — TFDA/MPA package insert query succeeded (result_count: 1) but `safety.key_warnings` and `safety.contraindications` remain empty; parse the PDF to fill these fields
- **Confirm Sweden registration status** — Metronidazole products (e.g., Flagyl) are marketed in many European countries; verify whether any MPA (Swedish Medical Products Agency) authorizations exist under alternative spellings or brand names
- **Re-run DDI query** using the resolved DrugBank ID to capture known interactions (warfarin, lithium, alcohol, disulfiram, etc.)
---

