---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 0
---

# Bortezomib
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

# BORTEZOMIB: Drug Repurposing Evaluation — Awaiting TxGNN Predictions

## One-Sentence Summary

Bortezomib is a proteasome inhibitor widely used internationally for the treatment of multiple myeloma and mantle cell lymphoma. The TxGNN model has **not yet generated predicted new indications** for this drug. Currently, there are **no clinical trials** or **publications** linked to a repurposed indication within this evidence pack, and **critical data gaps** remain to be resolved before evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma, mantle cell lymphoma (per international labelling; no Taiwan licence on record) |
| Predicted New Indication | — *(No TxGNN prediction available)* |
| TxGNN Prediction Score | — |
| Evidence Level | **L5** (Model prediction pending; no supporting studies in pack) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, no TxGNN-predicted indication has been generated for bortezomib, so a mechanistic plausibility assessment cannot be performed at this time.

For background, bortezomib is a first-in-class reversible inhibitor of the 26S proteasome's chymotrypsin-like activity. By blocking proteasomal degradation, it causes accumulation of pro-apoptotic proteins, inhibits NF-κB signalling, disrupts cell-cycle regulation, and induces endoplasmic reticulum stress — mechanisms that are particularly lethal to malignant plasma cells. It is marketed globally (e.g., Velcade®) for multiple myeloma and mantle cell lymphoma.

Once TxGNN predictions become available, the mechanistic bridge between bortezomib's proteasome inhibition and any new candidate indication should be evaluated. The MOA data in this evidence pack is currently flagged as a **High-severity data gap (DG002)** and should be formally populated from DrugBank before proceeding.

## Cytotoxicity

Bortezomib is an antineoplastic agent (proteasome inhibitor class). The following cytotoxicity profile applies:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Proteasome inhibitor) |
| Myelosuppression Risk | **High** — thrombocytopenia is very common (cyclical nadir ~Day 11, recovery by Day 21); neutropenia is common |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelet count (before each dose), hepatic function (AST/ALT/bilirubin), renal function, blood glucose, peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations; use personal protective equipment during reconstitution and administration |

## Safety Considerations

> Please refer to the package insert for safety information.
>
> *Note: Key warnings (DG001, Blocking severity) and contraindications are flagged as data gaps. The TFDA package insert was located (query log #4) but has not yet been parsed into structured fields. This must be resolved before any Stage 1 safety screening can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indication has been generated for bortezomib, so there is no candidate repurposing hypothesis to evaluate. Additionally, two critical data gaps — the TFDA package insert warnings/contraindications (Blocking) and the mechanism of action details (High) — remain unresolved.

**To proceed, the following is needed:**
- **TxGNN prediction run**: Execute or re-run the TxGNN model for bortezomib (DB00188) to generate candidate indications with confidence scores
- **Resolve DG001 (Blocking)**: Parse the TFDA package insert PDF to extract structured warnings, contraindications, and precautions
- **Resolve DG002 (High)**: Query DrugBank API for complete MOA, target, and pharmacodynamic data
- **Taiwan market verification**: Confirm whether bortezomib biosimilars or branded products (e.g., Velcade®) hold any active TFDA licences, as the drug is widely used in Taiwan hospitals despite the evidence pack showing 0 licences
- **Clinical evidence enrichment**: Once a predicted indication is identified, search ClinicalTrials.gov and PubMed for supporting trials and literature
---

