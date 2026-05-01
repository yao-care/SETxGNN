---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# BUSULFAN: Drug Repurposing Evaluation Report

## One-Sentence Summary

Busulfan is a well-established alkylating antineoplastic agent historically used for chronic myelogenous leukaemia (CML) and as a conditioning regimen prior to haematopoietic stem cell transplantation (HSCT). The TxGNN model has **not generated any predicted new indications** for this compound. Combined with **no clinical trial evidence**, **no literature evidence**, and **multiple critical data gaps**, this candidate currently lacks sufficient information for repurposing evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (known: CML, HSCT conditioning) |
| Predicted New Indication | — None predicted by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

There is **no TxGNN prediction to evaluate** for Busulfan at this time. The model did not output any candidate new indications for this drug.

From a pharmacological standpoint, Busulfan is a bifunctional alkylating agent that cross-links DNA strands, leading to cytotoxic cell death — particularly in rapidly dividing cells. It was one of the earliest chemotherapy agents used for CML and remains a cornerstone of myeloablative conditioning regimens prior to HSCT. Its mechanism of action is broad and non-selective, which means it could theoretically have activity against various malignancies, but this also limits its specificity and increases toxicity concerns.

The absence of TxGNN predictions may reflect that Busulfan's well-characterised but non-selective mechanism does not present strong graph-based signals for novel disease associations beyond its established uses, or it may be due to insufficient representation of this drug in the knowledge graph. Further investigation into the model's input features would be needed to clarify this.

## Clinical Trial Evidence

Currently no related clinical trials registered for predicted new indications (no new indications were predicted).

## Literature Evidence

Currently no related literature available for predicted new indications (no new indications were predicted).

## Taiwan Market Information

Busulfan currently holds **no valid marketing authorisations** (藥證) in Taiwan. The TFDA query returned zero results.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No authorisations on record |

## Cytotoxicity

Busulfan is a conventional cytotoxic alkylating agent. This section is included per protocol for antineoplastic drugs.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent — alkyl sulfonate class) |
| Myelosuppression Risk | **High** — Busulfan causes profound and prolonged myelosuppression; pancytopenia is expected, particularly when used in myeloablative conditioning doses |
| Emetogenicity Classification | Moderate to High (dose-dependent) |
| Monitoring Items | CBC with differential (mandatory, frequent monitoring), liver function tests (risk of hepatic veno-occlusive disease / sinusoidal obstruction syndrome), renal function, pulmonary function (risk of "busulfan lung" — pulmonary fibrosis), seizure monitoring (CNS toxicity), therapeutic drug monitoring of busulfan levels recommended in HSCT setting |
| Handling Protection | **Yes** — Must follow cytotoxic drug handling regulations (closed-system transfer devices, PPE including double gloving, protective gown, eye protection). Busulfan is classified as a hazardous drug per NIOSH guidelines |

## Safety Considerations

> Detailed package insert safety data (warnings, contraindications, drug interactions) was not retrievable from the TFDA database, as Busulfan is not currently marketed in Taiwan. Please refer to the originator's package insert or international references (e.g., FDA label, EMA SmPC) for comprehensive safety information.

**Key known safety concerns from international references include:**

- **Hepatic veno-occlusive disease (VOD) / Sinusoidal obstruction syndrome (SOS)** — potentially fatal, especially at myeloablative doses
- **Pulmonary toxicity** — "busulfan lung" (interstitial pulmonary fibrosis), may occur months to years after treatment
- **Seizures** — prophylactic anticonvulsants (e.g., phenytoin, levetiracetam) recommended during high-dose therapy
- **Secondary malignancies** — alkylating agents carry a known risk of treatment-related myelodysplastic syndrome / acute myeloid leukaemia
- **Severe myelosuppression** — dose-limiting toxicity; requires blood product support infrastructure
- **Reproductive toxicity** — teratogenic; contraindicated in pregnancy

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any predicted new indications for Busulfan. Additionally, multiple critical data gaps exist — including the absence of MOA data in the evidence pack, no Taiwan marketing authorisation, and no retrievable safety labelling from TFDA. Without a target indication to evaluate, the repurposing pipeline cannot proceed.

**To proceed, the following is needed:**
- Resolution of **DG001** (Blocking): Obtain package insert warnings/contraindications from an alternative regulatory source (e.g., FDA, EMA) since the drug is not marketed in Taiwan
- Resolution of **DG002** (High): Retrieve detailed mechanism of action from DrugBank API to enrich the knowledge graph input
- Investigation into why TxGNN produced no predictions — verify that Busulfan (DB01008) is adequately represented in the knowledge graph and that input features are correctly mapped
- If a specific repurposing hypothesis exists from clinical observation or literature, consider manual evidence collection to bypass the model prediction step
- Reassess after knowledge graph update or model retraining
---

