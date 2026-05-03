---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

Using the `txgnn-pipeline` skill as context, I'll now generate the report based on the Evidence Pack. The top predicted indication (rank 1) has L5 evidence only, while rank 7 (liver sarcoma) has the richest evidence — but per the report format instructions, the report focuses on `predicted_indications[0]`.

---

# Fluorouracil (5-FU): From Antineoplastic Chemotherapy to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a classic pyrimidine antimetabolite, widely used in chemotherapy regimens for solid tumors including colorectal, gastric, and head-and-neck cancers.
The TxGNN model predicts it may be effective for **Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina** (top-ranked prediction, score 99.75%),
however **0 clinical trials** and **0 publications** specifically support this direction — the evidence is model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan authorization record available |
| Predicted New Indication | Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no clinical or preclinical studies) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, Fluorouracil (5-FU) is a fluorinated pyrimidine antimetabolite. It is converted intracellularly to active metabolites — primarily fluorodeoxyuridine monophosphate (FdUMP) — which irreversibly inhibit thymidylate synthase (TS), blocking de novo synthesis of thymidine and thereby disrupting DNA replication in rapidly dividing cells.

Botryoid-type embryonal rhabdomyosarcoma of the vagina is an extremely rare pediatric/adolescent tumor arising from embryonal muscle precursor cells. As a rapidly proliferating malignancy, it is theoretically susceptible to TS inhibitors that target DNA synthesis. The mechanistic reasoning is biologically plausible at a general level.

However, the critical limitation is that rhabdomyosarcoma is a **myogenic (muscle-derived) malignancy**, whereas 5-FU's established clinical activity is almost exclusively in **epithelial cancers (carcinomas)**. The current standard of care for rhabdomyosarcoma is the VAC regimen (vincristine, actinomycin-D, cyclophosphamide), which does not include 5-FU. This TxGNN prediction most likely reflects a graph-based association learned from shared disease network topology, not a direct mechanistic or clinical link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Fluorouracil is a conventional cytotoxic antineoplastic agent belonging to the fluoropyrimidine class. The following cytotoxicity profile applies based on the drug class:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class |
| Myelosuppression Risk | Moderate to High (leukopenia, neutropenia, thrombocytopenia, and anemia are common dose-limiting toxicities) |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Complete blood count (CBC) with differential, liver function tests (LFTs), renal function, serum electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) recommended |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Taiwan TFDA package insert data was not retrievable in this Evidence Pack (Data Gap DG001). Safety review cannot be completed until the package insert is obtained and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on the TxGNN graph neural network model (L5 — no supporting clinical trials or literature). Fluorouracil has no established mechanism of action against myogenic sarcoma lineages, and the botryoid vaginal subtype is an ultra-rare pediatric tumor with essentially no published data on fluoropyrimidine use. Proceeding without preclinical validation would not be justified.

**To proceed, the following is needed:**
- Preclinical in vitro studies testing 5-FU cytotoxicity against rhabdomyosarcoma cell lines (e.g., RD, Rh30)
- Mechanistic evidence linking TS inhibition to myogenic tumor biology
- Review of historical pediatric oncology cooperative group data (COG, IRS) for any prior 5-FU exposure in rhabdomyosarcoma patients
- Taiwan TFDA package insert retrieval for complete warnings and contraindications (Data Gap DG001)
- DrugBank MOA data query to formally document mechanism of action (Data Gap DG002)
- Consider pivoting the report focus to **Liver Sarcoma** (rank 7, Evidence Level L3: 6 clinical trials + 20 publications), which carries substantially more evidence and a stronger mechanistic rationale via hepatic arterial infusion and FOLFIRINOX-based regimens
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

