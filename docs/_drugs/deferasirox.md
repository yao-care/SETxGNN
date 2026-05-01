---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 5
---

# Deferasirox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Deferasirox: Drug Repurposing Evaluation Report

## One-Sentence Summary

Deferasirox is an oral iron chelator primarily used for the treatment of chronic iron overload caused by repeated blood transfusions (transfusional hemosiderosis). The TxGNN model **did not generate any predicted new indications** for this drug, and there are **significant data gaps** in mechanism of action, safety, and regulatory information that prevent further evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name | Deferasirox |
| DrugBank ID | DB01609 |
| Original Indication | Chronic iron overload (transfusion-dependent) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No prediction, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

### No Prediction Was Generated

The TxGNN model did not produce any predicted new indications for Deferasirox in this evaluation cycle. This may be due to one or more of the following factors:

1. **Insufficient knowledge graph connectivity** — Deferasirox's primary role as an iron chelator may result in limited edges connecting it to disease nodes beyond its established indications in the TxGNN knowledge graph.
2. **Narrow pharmacological profile** — Iron chelation is a highly specific mechanism. Unlike multi-target kinase inhibitors or immunomodulators, chelators typically have fewer plausible off-target therapeutic effects, which may limit the model's ability to identify repurposing candidates.

### Background on Deferasirox

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological knowledge, Deferasirox is a tridentate iron chelator that selectively binds ferric iron (Fe³⁺) with high affinity, forming a soluble complex that is excreted primarily through the faeces. It is marketed globally under the brand names **Exjade** (dispersible tablet) and **Jadenu** (film-coated tablet) for the treatment of chronic iron overload in patients receiving long-term blood transfusions, such as those with thalassemia major, sickle cell disease, or myelodysplastic syndromes.

Despite the absence of a TxGNN prediction, it is worth noting that iron chelation has been investigated in other contexts (e.g., neuroprotection, antimicrobial activity, anti-proliferative effects in certain cancers). Future iterations of the model with enriched data may yield candidate indications.

---

## Clinical Trial Evidence

No TxGNN-predicted indication was generated; therefore, no targeted clinical trial search was performed for a new indication.

> Currently no related clinical trials registered for a repurposed indication.

---

## Literature Evidence

No TxGNN-predicted indication was generated; therefore, no targeted literature search was performed for a new indication.

> Currently no related literature available for a repurposed indication.

---

## Taiwan Market Information

Deferasirox currently holds **no active marketing authorizations** (藥證) in Taiwan.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| — | — | — | — |

> No TFDA licenses found. Deferasirox is not currently marketed in Taiwan (未上市).

---

## Safety Considerations

> Please refer to the package insert for safety information.

Safety data (key warnings, contraindications, and drug–drug interactions) were not available in this Evidence Pack. Key safety considerations known from global labelling include:

- **Renal toxicity**: Deferasirox can cause acute renal failure; serum creatinine monitoring is essential.
- **Hepatotoxicity**: Hepatic failure, including fatal cases, has been reported.
- **GI haemorrhage**: Upper GI ulceration and haemorrhage have been observed, particularly in elderly patients.
- **Cytopenias**: Agranulocytosis, neutropenia, and thrombocytopenia have been reported.

*Note: The above is based on general pharmacological knowledge and global labelling. A formal safety evaluation requires TFDA-approved package insert data, which is identified as a blocking data gap (DG001).*

---

## Data Gaps

The following critical data gaps were identified and must be resolved before any repurposing evaluation can proceed:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanism–indication relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any predicted new indications for Deferasirox. Combined with the absence of Taiwan market authorization and multiple blocking data gaps (safety labelling, MOA), there is currently no actionable repurposing signal to evaluate.

**To proceed, the following is needed:**
- Obtain TxGNN prediction results — verify whether Deferasirox was included in the prediction input and re-run if necessary with updated knowledge graph data
- Resolve **DG001** (Blocking): Acquire TFDA package insert or equivalent regulatory safety data
- Resolve **DG002** (High): Retrieve detailed MOA from DrugBank API to enable future mechanism–disease linkage analysis
- Monitor emerging research on iron chelation in oncology, neurodegeneration, and infectious disease for potential manual candidate identification
---

