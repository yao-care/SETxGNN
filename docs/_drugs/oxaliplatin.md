---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using `txgnn-pipeline` to confirm report generation context. Now composing the full evaluation report based on the Evidence Pack.

---

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum-based chemotherapy agent, globally established as a standard backbone treatment for colorectal cancer (FOLFOX/XELOX regimens), though it currently holds no registered product authorization in Taiwan.
The TxGNN model predicts it may be effective for **Malignant Pleural Mesothelioma (MPM)**,
with **6 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally established for colorectal cancer |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oxaliplatin is a third-generation cisplatin analogue carrying a 1,2-diaminocyclohexane (DACH) carrier ligand. Its mechanism of action centres on the formation of bulky 1,2-intrastrand Pt-DNA adducts that physically block DNA polymerase and impair nucleotide excision repair (NER), ultimately triggering apoptotic cell death. This adduct geometry is structurally distinct from cisplatin, allowing oxaliplatin to retain activity against some cisplatin-resistant tumours — an important consideration in MPM, where cisplatin intolerance is common.

Malignant pleural mesothelioma arises from mesothelial cells lining the pleura and is broadly sensitive to platinum compounds; the current first-line standard (pemetrexed + cisplatin ± nivolumab/ipilimumab) relies on platinum's DNA-damaging backbone for efficacy. Oxaliplatin's distinct adduct profile makes it a mechanistically rational substitution, and synergistic activity has been demonstrated in clinical trials when paired with antifolates (raltitrexed) or nucleoside analogues (gemcitabine), as each combination partner attacks a complementary DNA-repair pathway, amplifying cytotoxicity.

Beyond direct cytotoxicity, 2019 translational data (PMID 31455014) showed that oxaliplatin alters immune checkpoint expression on MPM cells, raising its potential as an immunomodulatory partner for checkpoint inhibitors. Taken together, the mechanistic rationale, Phase 2 trial evidence across multiple combination regimens, and emerging immunotherapy synergy data position oxaliplatin as a clinically defensible second-line option — or a first-line alternative platinum backbone for patients who cannot tolerate cisplatin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Directly tested oxaliplatin + gemcitabine as first- or second-line chemotherapy in pleural or peritoneal mesothelioma; the most pivotal trial for this indication |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + oxaliplatin (Eloxatin) in previously treated MPM patients; up to 6 cycles with CT reassessment every 8 weeks |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1,000 | International prospective registry of PIPAC/PITAC (pressurised aerosol intraperitoneal/intrathoracic chemotherapy) for malignant pleural and peritoneal diseases; oxaliplatin is among the most commonly used PIPAC agents |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Cadonilimab (anti-PD-1/CTLA-4 bispecific) + oxaliplatin-containing chemotherapy for locally advanced gastroesophageal cancer; supports oxaliplatin's role as a chemotherapy backbone in combination with immunotherapy |
| [NCT07532902](https://clinicaltrials.gov/study/NCT07532902) | Phase 1 | Recruiting | 60 | BMS-986504 + standard-of-care therapy in MTAP-deleted solid tumours (basket trial); oxaliplatin serves as the SOC chemotherapy backbone |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | NX-1607 (CBL-B inhibitor) dose escalation in advanced malignancies; first-in-human safety study with oxaliplatin as potential combination agent |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 Open-Label | J Clin Oncol | Raltitrexed 3 mg/m² + oxaliplatin 130 mg/m² in 70 MPM patients (55 chemo-naive, 15 pretreated); established combination activity particularly in first-line setting |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 Multicenter | Clin Lung Cancer | 25 MPM patients received gemcitabine 1,000 mg/m² + oxaliplatin 80 mg/m² on days 1 & 8 of a 21-day cycle for up to 6 cycles; multicenter efficacy and tolerability data |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase 2 Single-Arm | Tumori | Pilot study of oxaliplatin + raltitrexed in inoperable MPM; building on Phase 1 data showing activity and reporting preliminary response outcomes |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase 2 Single-Arm | J Occup Med Toxicol | Gemcitabine ± oxaliplatin in pemetrexed-pretreated MPM patients; efficacy and safety evidence specifically in the second-line, pemetrexed-refractory population |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 | Lung Cancer | Vinorelbine 30 mg/m² (days 1 & 8) + oxaliplatin 130 mg/m² (day 1) as first-line in untreated MPM; evaluated a novel non-antifolate combination |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 Single-Arm | Lung Cancer | Raltitrexed + oxaliplatin as second-line MPM: no objective responses in 14 patients (28.6% disease stabilisation only); key negative result constraining second-line use in this specific combination |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Phase 2 Series | Eur J Cancer | Institut Gustave Roussy 9-year experience across 7 consecutive trials in 163 mesothelioma patients; summarises early raltitrexed-oxaliplatin rationale and chemo-immunotherapy data |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review / Translational | Int J Mol Sci | Oxaliplatin modulates immune checkpoint expression on MPM cells in vitro; supports rational design of oxaliplatin + immune checkpoint inhibitor combination schedules |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | Comprehensive review of MPM chemotherapy; newer platinum-containing combinations including oxaliplatin-based regimens show higher response rates than conventional single agents |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Emerging role of antifolates in MPM; compares raltitrexed/oxaliplatin vs. pemetrexed/cisplatin efficacy signals; positioned oxaliplatin combinations as a promising pre-pemetrexed era treatment |

---

## Taiwan Market Information

Oxaliplatin currently has **no registered product authorizations in Taiwan**. A TFDA database query (2026-03-29) returned zero records. No dosage form, indication, or license data is available from the Taiwan regulatory system.

> If clinical use or research procurement is planned, import via special approval (專案進口) or compassionate use pathways would be required.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum compound (3rd-generation cisplatin analogue, DACH-platinum) |
| Myelosuppression Risk | Low to Moderate — neutropenia and thrombocytopenia occur but are generally less severe than cisplatin; cumulative peripheral sensory neuropathy is the primary dose-limiting toxicity |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential (each cycle), renal function (creatinine clearance before each cycle), liver function tests, and serial peripheral neuropathy assessment (cold-triggered acute neuropathy and cumulative sensory neuropathy grading) |
| Handling Protection | Must follow cytotoxic drug handling regulations; avoid skin and mucosal contact; cold avoidance precautions for patients post-infusion |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan FDA package insert data (warnings, contraindications) was not retrievable in this evidence pack (data gap DG001). DDI screening also returned no records. A full safety review should be completed before clinical or research use, drawing from the EMA/FDA-approved SmPC/label and institutional cytotoxic drug handling protocols.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials have directly evaluated oxaliplatin in MPM — including completed studies of oxaliplatin + gemcitabine and raltitrexed + oxaliplatin — establishing proof of clinical activity, particularly in first-line and cisplatin-intolerant settings; however, a notable Phase 2 negative result for the second-line raltitrexed + oxaliplatin combination (PMID 15893013) underscores the importance of treatment-line and combination partner selection before broader adoption.

**To proceed, the following is needed:**

- **Safety data retrieval**: Download and parse the TFDA package insert PDF (or EMA/FDA SmPC) to complete S1 safety screening — warnings, contraindications, and DDI profile are currently unresolved data gaps
- **Positioning clarity**: Formally define the target patient population (first-line cisplatin-ineligible vs. second-line pemetrexed-refractory) and preferred combination partner (gemcitabine preferred over raltitrexed in second-line based on available evidence)
- **Histological subtype stratification**: Epithelioid MPM (~60–70% of cases) shows the best platinum sensitivity; any prospective study should stratify by subtype and exclude pure sarcomatoid cases (evidence level L4, Hold recommendation)
- **Immunotherapy combination assessment**: Evaluate oxaliplatin as an immunomodulatory backbone in combination with nivolumab/ipilimumab, building on the 2019 translational checkpoint expression data
- **Taiwan access pathway**: Initiate special import (專案進口) application or expanded access protocol, as oxaliplatin has no current TFDA authorization
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

