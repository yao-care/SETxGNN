---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: Preliminary Evaluation — Awaiting Predicted Indication Data

## One-Sentence Summary

Axitinib (DB06626) is a selective tyrosine kinase inhibitor known internationally for the treatment of advanced renal cell carcinoma.
The TxGNN model has **not yet generated predicted new indications** for this drug,
and the evidence pack currently contains **no clinical trial or literature evidence** for repurposing candidates. This report serves as a baseline assessment pending completion of the prediction pipeline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current evidence pack (known internationally: advanced renal cell carcinoma) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (Model prediction not yet available) |
| Taiwan Market Status | ❌ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data has not been populated in the evidence pack. Based on publicly available pharmacological knowledge, Axitinib is a second-generation **selective inhibitor of vascular endothelial growth factor receptors (VEGFR-1, VEGFR-2, and VEGFR-3)**. It is a small-molecule tyrosine kinase inhibitor (TKI) that blocks tumour angiogenesis by inhibiting VEGF-mediated endothelial cell proliferation and survival.

Axitinib was originally approved by the US FDA (2012) and the EMA for the treatment of **advanced renal cell carcinoma (RCC)** after failure of one prior systemic therapy. Its anti-angiogenic mechanism has broad theoretical applicability to other solid tumours where VEGF-driven neovascularisation plays a key role.

However, because the TxGNN prediction pipeline has not yet returned candidate indications for Axitinib, no mechanistic bridging analysis between an original and a new indication can be performed at this time. This section should be revisited once `predicted_indications` data becomes available.

---

## Clinical Trial Evidence

Currently no predicted indication has been generated, therefore no indication-specific clinical trial search was performed.

---

## Literature Evidence

Currently no predicted indication has been generated, therefore no indication-specific literature search was performed.

---

## Taiwan Market Information

Axitinib currently holds **no TFDA marketing authorisations** in Taiwan (市場狀態：未上市). No license records are available.

---

## Cytotoxicity

Axitinib is an antineoplastic agent (tyrosine kinase inhibitor targeting VEGFR). The following cytotoxicity profile is based on known pharmacological properties:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low to moderate (anaemia and thrombocytopenia reported; less common than conventional cytotoxics) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Blood pressure (hypertension is a class effect), CBC with differential, thyroid function (hypothyroidism risk), liver function tests (ALT/AST), urinalysis (proteinuria), cardiac function |
| Handling Protection | Oral formulation — standard handling precautions for anticancer agents apply; no special cytotoxic spill procedures typically required for intact oral tablets |

---

## Safety Considerations

Safety data (key warnings, contraindications, drug–drug interactions) are currently **not available** in the evidence pack. TFDA package insert data was queried but detailed warnings and contraindications were not extracted.

> Please refer to the package insert for complete safety information. Key class-effect concerns for VEGFR-TKIs include: hypertension, arterial/venous thromboembolic events, haemorrhage, cardiac failure, gastrointestinal perforation, wound healing complications, reversible posterior leukoencephalopathy syndrome (RPLS), hepatotoxicity, and proteinuria.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline has not yet generated candidate repurposing indications for Axitinib. Additionally, the drug is not currently marketed in Taiwan (no TFDA authorisations), and critical data fields — including MOA, safety warnings, and contraindications — remain unpopulated. There is insufficient information to proceed with any repurposing evaluation at this time.

**To proceed, the following is needed:**
- Complete TxGNN prediction run to populate `predicted_indications` with scored candidate diseases
- Retrieve detailed mechanism of action (MOA) data from DrugBank API (Data Gap DG002)
- Obtain TFDA package insert warnings and contraindications (Data Gap DG001, Blocking severity)
- Perform drug–drug interaction query once the target indication and its standard-of-care regimens are known
- Reassess Taiwan market pathway feasibility (drug is currently not marketed — would require new drug application or special import pathway)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

