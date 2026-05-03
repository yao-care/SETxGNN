---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# DASATINIB: Drug Repurposing Evaluation Report

## One-Sentence Summary

Dasatinib is a multi-targeted tyrosine kinase inhibitor, widely known internationally for treating chronic myeloid leukaemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukaemia (Ph+ ALL). The TxGNN model has **not yet generated predicted new indications** for this drug, and critical data gaps remain in the evidence pack. The current evidence is **insufficient to support a repurposing recommendation** at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | DASATINIB |
| DrugBank ID | DB01254 |
| Original Indication | Not recorded in evidence pack (internationally approved for CML and Ph+ ALL) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | **L5** (No prediction or supporting studies in pack) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations (TFDA) | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

### Known Mechanism of Action

Currently, detailed mechanism of action data is not available in the evidence pack (listed as a Data Gap). Based on publicly known information, Dasatinib is a second-generation BCR-ABL tyrosine kinase inhibitor that also inhibits SRC family kinases (SRC, LCK, YES, FYN), c-KIT, EPHA2, and PDGFRβ. Its broad kinase inhibition profile is the basis for its established efficacy in haematological malignancies driven by the BCR-ABL fusion protein.

### Repurposing Potential

Due to its multi-kinase inhibition profile — particularly SRC family kinases and PDGFRβ — Dasatinib has been investigated internationally in numerous solid tumours (e.g., prostate cancer, breast cancer, NSCLC) and non-oncological conditions (e.g., pulmonary arterial hypertension, systemic sclerosis). However, the TxGNN model has not yet produced a specific predicted indication for this drug in the current evidence pack. **No mechanistic bridging analysis can be performed until a target indication is identified.**

### Current Status

The absence of a TxGNN prediction, combined with the drug not being marketed in Taiwan (0 TFDA licenses), means that this candidate cannot advance through the repurposing evaluation pipeline at this time.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is available; therefore, no indication-specific clinical trial search was performed.

> Currently no related clinical trials registered for a predicted new indication.

---

## Literature Evidence

No TxGNN-predicted indication is available; therefore, no indication-specific literature search was performed.

> Currently no related literature available for a predicted new indication.

---

## Taiwan Market Information

Dasatinib is **not currently marketed in Taiwan**. No TFDA drug licenses were found.

> No authorization records available from TFDA.

---

## Cytotoxicity

Dasatinib is an antineoplastic agent (targeted tyrosine kinase inhibitor). Based on general pharmacological knowledge:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Multi-kinase inhibitor: BCR-ABL / SRC family / c-KIT / PDGFRβ) |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and anaemia are common (reported in >30% of patients internationally) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during first 2 months, then monthly), liver function (ALT/AST, bilirubin), renal function, electrolytes, chest X-ray (risk of pleural effusion) |
| Handling Protection | Oral tablet — standard handling procedures; no special cytotoxic handling required for intact oral dosage forms |

> ⚠️ Note: The above information is based on general pharmacological knowledge. Please refer to the package insert warnings and precautions for authoritative details.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Key safety data (warnings, contraindications, drug interactions) were not available in the evidence pack. The following are well-known safety concerns from international labelling for reference only:
>
> - **Pleural effusion**: Occurs in approximately 20–35% of patients; requires monitoring and dose adjustment
> - **QT prolongation**: ECG monitoring recommended
> - **Pulmonary arterial hypertension (PAH)**: Rare but serious; requires vigilance
> - **Haemorrhage**: Risk of severe bleeding events, including CNS haemorrhage
> - **CYP3A4 interactions**: Dasatinib is a CYP3A4 substrate; strong inhibitors/inducers should be used with caution; avoid concomitant use with H2-blockers and PPIs (reduced absorption)

---

## Data Gaps Summary

The following critical data gaps were identified in this evidence pack:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Impacts mechanism-association analysis | Query DrugBank API |

Additionally:
- **No TxGNN predicted indications** — The model has not yet generated repurposing candidates for this drug
- **No Taiwan market data** — Drug is not marketed in Taiwan (0 licenses)
- **No DDI data** — Drug interaction query returned no results

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dasatinib has a pharmacologically rich multi-kinase inhibition profile that makes it an inherently interesting repurposing candidate. However, the evidence pack contains no TxGNN-predicted new indications, the drug is not marketed in Taiwan, and critical safety data (TFDA package insert) is missing. There is insufficient information to evaluate any repurposing direction at this time.

**To proceed, the following is needed:**
1. **Run TxGNN prediction** for Dasatinib to generate candidate new indications with confidence scores
2. **Resolve DG001 (Blocking)**: Obtain TFDA package insert warnings and contraindications — required before S1 safety assessment can begin
3. **Resolve DG002 (High)**: Retrieve detailed MOA data from DrugBank API to enable mechanism bridging analysis
4. **Confirm Taiwan regulatory pathway**: Since Dasatinib is not currently marketed in Taiwan, evaluate whether an import drug licence or special access pathway would be required
5. **Once a predicted indication is available**: Conduct targeted clinical trial (ClinicalTrials.gov) and literature (PubMed) searches to assess evidence level
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

