---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Solid Tumor Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (Taxotere) is a taxane-class cytotoxic chemotherapy agent globally established for treating multiple solid tumors — including breast cancer, non-small cell lung cancer, gastric cancer, and prostate cancer — but not currently registered in Sweden.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **50 clinical trials** and **20 publications** currently supporting this direction — a finding that aligns with its FDA/EMA-approved global indication and reflects the model's ability to correctly identify well-validated drug-disease relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered in Sweden — no approved indication on record |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semi-synthetic taxane derivative that promotes microtubule polymerization and inhibits depolymerization, resulting in stabilization of non-functional microtubule bundles. This leads to G2/M cell cycle arrest and subsequent apoptosis — a mechanism that disproportionately impacts rapidly dividing cells. Breast cancer cells, particularly in aggressive subtypes such as triple-negative (TNBC) and HER2-positive disease, are characterized by high mitotic activity and are therefore mechanistically well-matched to taxane-based therapy. The sequence of gemcitabine followed by docetaxel further exploits this vulnerability through time-dependent synergistic cytotoxicity.

The clinical evidence supporting Docetaxel in breast cancer spans all treatment contexts. In the adjuvant setting, regimens such as TC (docetaxel + cyclophosphamide), TAC (+ doxorubicin), and TCHP (+ carboplatin + trastuzumab + pertuzumab) are established standards of care. In the neoadjuvant setting, AC→Docetaxel combinations consistently achieve high pathological complete response rates. In metastatic disease, both single-agent and combination strategies with capecitabine, trastuzumab, or bevacizumab demonstrate meaningful survival benefits. Multiple Phase 3 RCTs with thousands of enrolled patients have confirmed these findings across diverse populations.

Although detailed mechanistic action data is not available from the current local regulatory database query, Docetaxel belongs to the taxane pharmacological class with an extensively documented mechanism in the scientific literature. The TxGNN score of 99.90% reflects the density and quality of clinical and biological data linking this drug to breast cancer in the model's training knowledge graph — effectively validating an already globally recognized indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Major landmark RCT comparing preoperative AC vs preoperative AC→Docetaxel vs postoperative Docetaxel in Stage II/III operable breast cancer; established the role of adding a taxane to anthracycline regimens |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy (TC×6 or AC→weekly Paclitaxel) with or without trastuzumab in HER2-low, node-positive or high-risk node-negative invasive breast cancer; large-scale validation of Docetaxel-containing adjuvant regimens |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Phase 3 | Completed | 2,611 | AC→Docetaxel vs AC→Docetaxel+Capecitabine for high-risk breast cancer; evaluated whether adding capecitabine to a Docetaxel backbone improves overall survival |
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Weekly Docetaxel vs CMF as adjuvant treatment in women aged ≥65 or ineligible for anthracyclines; core evidence for Docetaxel use in elderly patients and anthracycline-contraindicated populations |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | TCHP (Docetaxel+Carboplatin+Trastuzumab+Pertuzumab) with vs without estrogen deprivation for HR+/HER2+ locally advanced breast cancer; assessed impact of combined endocrine suppression on pCR rates |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FEC→Docetaxel vs FEC→Paclitaxel as adjuvant chemotherapy for axillary lymph node-positive breast cancer; direct taxane comparison in an adjuvant setting |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC vs TCX (Docetaxel+Cyclophosphamide+Capecitabine) as adjuvant treatment for high-risk HER2-negative breast cancer; prospective evaluation of capecitabine substitution for anthracyclines |
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | Phase 3 | Completed | 300 | Mitoxantrone vs FEC as first-line chemotherapy for metastatic breast cancer with unfavorable prognosis; historical comparative baseline for evaluating taxane-era regimen superiority |
| [NCT03252431](https://clinicaltrials.gov/study/NCT03252431) | Phase 3 | Completed | 393 | F-627 vs Pegfilgrastim (Neulasta) in Stage I–III breast cancer receiving myelotoxic Docetaxel-containing chemotherapy; informs G-CSF prophylaxis protocols for taxane regimens |
| [NCT04066335](https://clinicaltrials.gov/study/NCT04066335) | Observational | Unknown | 1,498 | Real-world post-marketing safety evaluation of Nanoxel M (nanoparticle Docetaxel formulation) across multiple cancer indications including breast cancer; large-scale safety surveillance data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT Series | J Clin Oncol | ABC trials (USOR 06-090, NSABP B-46-I/USOR 07132, NSABP B-49): compared TC×6 vs TaxAC regimens in early breast cancer; demonstrated that TC may not be inferior to anthracycline+taxane combinations in select populations |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Systematic Review | The Oncologist | Comprehensive 10-year review of Docetaxel and Paclitaxel clinical experience in metastatic, neoadjuvant, and adjuvant breast cancer; seminal comparative synthesis of the taxane class in breast cancer |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Phase IIb RCT | J Clin Oncol | Dose-dense Doxorubicin+Docetaxel ± Tamoxifen as preoperative therapy for operable breast cancer; evaluated pathological response as surrogate endpoint for survival benefit |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Prospective Cohort | Breast Cancer | Docetaxel+Cyclophosphamide+Trastuzumab (HER-TC) as neoadjuvant chemotherapy for HER2+ breast cancer; assessed pCR rates stratified by hormone receptor status as a prognostic marker |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective Cohort | Anti-Cancer Drugs | Association between adjuvant Docetaxel-based chemotherapy and breast cancer-related lymphedema in Stage II/III patients; key safety signal relevant to long-term post-treatment quality of life monitoring |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 1/2 | Cancer | Capecitabine+Docetaxel+Epirubicin (TEX) as first-line treatment for locally advanced/metastatic breast carcinoma; evaluated activity and safety of a triple-agent taxane-containing regimen |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase 2 (Interim Analysis) | Breast Cancer | CEF→Docetaxel neoadjuvant chemotherapy multicenter trial (JBCRG); interim analysis in 79 patients showing clinical response rates and tolerability of sequential anthracycline-taxane neoadjuvant approach |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 1/2 | Oncology | Docetaxel+Vinorelbine combination for metastatic breast cancer; early data establishing projected median survival and response rates in untreated and previously treated patients |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 Dose-Finding | Tumori | Docetaxel+Gemcitabine weekly schedule for anthracycline-pretreated metastatic breast cancer; explored tolerability-optimized scheduling as an alternative to standard 3-weekly regimens |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Seminal early review of Docetaxel's preclinical and clinical antineoplastic profiles; foundational reference establishing the pharmacological rationale for breast cancer activity |

---

## Sweden Market Information

Docetaxel is **not currently registered in Sweden**. No marketing authorizations are on record in the available regulatory database (0 licenses, market status: not marketed).

> **Note for context:** Docetaxel (Taxotere and generics) holds valid marketing authorization in multiple major markets — including the United States (FDA), European Union (EMA centralized procedure), Japan, and others — for breast cancer, non-small cell lung cancer, gastric cancer, prostate cancer, and head and neck cancer. The absence of a Swedish registration reflects a market entry gap rather than a deficiency in the global evidence base.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent; semi-synthetic derivative of 10-deacetylbaccatin III) |
| Myelosuppression Risk | High — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia occurs in up to 12–15% of patients without G-CSF prophylaxis; G-CSF primary prophylaxis (e.g., pegfilgrastim) is recommended for regimens with >20% febrile neutropenia risk |
| Emetogenicity Classification | Low to moderate (lower than anthracyclines; standard 5-HT₃ antagonist + dexamethasone antiemetic premedication recommended) |
| Monitoring Items | CBC with differential (before each cycle); ALT/AST/ALP/total bilirubin (hepatic function assessment mandatory — dose adjustment or withholding required for hepatic impairment); weight and peripheral edema assessment each cycle (fluid retention syndrome); fluid intake/output monitoring in high-dose or prolonged courses |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed-system transfer devices, nitrile gloves, protective gown, eye protection); polysorbate 80-containing formulations require corticosteroid premedication (typically Dexamethasone 8 mg orally twice daily for 3 days starting the day before infusion) to reduce severity of hypersensitivity reactions and fluid retention |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel's efficacy in female breast carcinoma is supported by multiple completed Phase 3 RCTs with combined enrollment exceeding 10,000 patients across adjuvant, neoadjuvant, and metastatic settings — meeting Level 1 evidence criteria — and the drug holds existing FDA/EMA marketing authorization for this indication globally. The primary barrier to Swedish market use is regulatory registration, not clinical evidence.

**To proceed, the following is needed:**

- Retrieval and review of the full prescribing information (package insert) from TFDA and/or EMA sources, including black box warnings, contraindications, and drug-drug interactions (currently classified as data gaps DG001/DG002)
- Formal pharmacist safety review covering cytotoxic handling protocols per Swedish occupational health regulations
- Assessment of existing EMA centralized marketing authorization (Taxotere/generic docetaxel) for direct reference in a Swedish MPA submission or mutual recognition procedure
- Establishment of a local pharmacovigilance and Risk Management Plan (RMP) aligned with EMA requirements
- Alignment of G-CSF prophylaxis, premedication protocols, and hepatic dose-adjustment criteria with current Swedish oncology guidelines (e.g., SWEDCAN/regional cancer center protocols)
- Consideration of health technology assessment (HTA) by TLV (Tandvårds- och läkemedelsförmånsverket) for potential reimbursement inclusion in the Swedish benefits scheme
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

