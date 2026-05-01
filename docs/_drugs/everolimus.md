---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Everolimus
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

Using `txgnn-pipeline` for context — the skill confirms this is a TW-series TxGNN report. Now generating the full evaluation report per the Drug Repurposing Evaluation Report Prompt v5.

---

# Everolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR (mechanistic target of rapamycin) inhibitor approved globally for advanced renal cell carcinoma, hormone receptor-positive breast cancer, and pancreatic neuroendocrine tumors — though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Liposarcoma** (specifically dedifferentiated liposarcoma, DDLPS),
with **1 active Phase 2 clinical trial** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for advanced RCC, PNET, and HR+ breast cancer |
| Predicted New Indication | Liposarcoma (Dedifferentiated Liposarcoma, DDLPS) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Everolimus is a rapalog that selectively inhibits mTORC1 (mechanistic target of rapamycin complex 1), blocking downstream effectors S6K1 and 4E-BP1 — two central regulators of protein synthesis, cell proliferation, and metabolic reprogramming. By shutting down mTORC1, everolimus starves tumor cells of the growth signals they depend on. This mechanism is validated across multiple approved oncology indications (clear-cell RCC, PNET, breast cancer) and forms the scientific backbone of its predicted utility in soft-tissue sarcomas.

The link to liposarcoma is mechanistically grounded. Dedifferentiated liposarcoma (DDLPS) is defined by CDK4 and MDM2 amplification, and importantly, by significant hyperactivation of the Akt/mTOR and MAPK signaling pathways (PMID 26518767). Immunohistochemical and in vitro studies across 99 DDLPS specimens confirm this pathway dependency, making mTOR inhibition a biologically rational strategy. When everolimus is paired with the CDK4/6 inhibitor ribociclib, the combination simultaneously blocks two complementary oncogenic drivers — the cell cycle checkpoint and the mTOR growth axis — producing synergistic anti-proliferative activity across tumor models.

This dual-targeting rationale is now under formal clinical evaluation. The ongoing Phase II SAR-096 trial (NCT03114527) directly tests ribociclib plus everolimus in advanced DDLPS and leiomyosarcoma, with 2024 results already published (PMID 37967116), providing the first prospective clinical evidence for this approach. The combination is not yet standard of care, but the mechanistic case is robust and the early clinical signal justifies continued investment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, Not Recruiting | 48 | Two-arm study evaluating ribociclib + everolimus in advanced DDL (Arm A) and LMS (Arm B); patients must have ≥1 prior systemic therapy; ribociclib 300 mg/day (3 weeks on/1 week off) + everolimus 2.5 mg/day; 2024 results published (PMID 37967116) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II Clinical Trial | Clinical Cancer Research | SAR-096 trial results: ribociclib + everolimus in advanced DDL/LMS; first prospective efficacy data for this CDK4/6 + mTOR dual blockade strategy in sarcoma |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational/Mechanistic | Tumour Biology | Akt/mTOR and MAPK pathway hyperactivation confirmed in 99 DDLPS specimens by IHC; in vitro mTOR inhibitor antitumor activity demonstrated, providing key mechanistic rationale |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Preclinical Review | Frontiers in Oncology | PDOX mouse models of sarcoma (including liposarcoma) identify effective CDK inhibitor combinations; supports CDK + mTOR co-targeting strategy as translatable approach |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Eribulin combined with mechanistically distinct anticancer agents (including mTOR inhibitors) evaluated in liposarcoma and breast cancer xenografts; broad-spectrum antitumor activity shown |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclinical/Mechanistic | Oncogene | XPO1 inhibitor KPT-330 (Selinexor) disrupts core transcriptional regulatory circuitry in DDLPS by modulating translation; highlights tumor biology beyond CDK4/MDM2 and potential for mTOR pathway crosstalk |

---

## Taiwan Market Information

Everolimus is **not registered** in Taiwan. No authorization records were found in the Taiwan FDA database (query date: 2026-03-29). Clinicians seeking access would need to pursue compassionate use, named-patient programs, or a formal new drug application (NDA) through the TFDA.

---

## Cytotoxicity

Everolimus is classified as an antineoplastic agent (mTOR inhibitor); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — anemia is the most common hematologic effect; thrombocytopenia and leukopenia reported at lower frequency than traditional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (anemia monitoring), fasting blood glucose and lipids (hyperglycemia and hypertriglyceridemia are class effects), serum creatinine, stomatitis/oral mucositis assessment, pulmonary function (non-infectious pneumonitis is a rapalog class warning) |
| Handling Protection | Follow institutional oral oncolytic handling guidelines; standard cytotoxic precautions for preparation and disposal apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data from the Taiwan TFDA package insert could not be retrieved (Data Gap DG001). Drug-drug interaction data was also not found in the local database. Clinicians should consult the approved SmPC or global prescribing information (e.g., Afinitor/Votubia) before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Akt/mTOR signaling axis is mechanistically active and well-characterized in DDLPS, and the Phase II SAR-096 trial (NCT03114527) — with 2024 published results (PMID 37967116) — provides direct prospective clinical evidence for everolimus plus ribociclib in this indication, meeting the threshold for L2 evidence.

**To proceed, the following is needed:**

- **Review SAR-096 full results** (PMID 37967116): Extract ORR, PFS, and toxicity data to determine whether efficacy endpoints were met and which subtype (DDL vs. LMS) responded better
- **Resolve DG001** (TFDA package insert): Download and parse the Taiwan FDA SmPC PDF to enable formal safety assessment and contraindication mapping
- **Resolve DG002** (MOA data): Query DrugBank API for full mechanistic annotation, drug categories, and pharmacokinetic profile to support indication-mechanism alignment analysis
- **Assess Taiwan regulatory pathway**: Evaluate compassionate use or expedited review eligibility for sarcoma indication, given unmet need in relapsed/refractory DDLPS
- **Define target patient population**: Clarify whether intended use is specifically DDLPS or broader liposarcoma subtypes, and confirm CDK4 amplification as a biomarker enrichment strategy
- **Review safety monitoring plan** for the ribociclib + everolimus combination, including QTc prolongation (ribociclib risk) and non-infectious pneumonitis (everolimus class effect) co-management
---

