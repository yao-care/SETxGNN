---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the `txgnn-pipeline` skill to guide report generation. Now writing the evaluation report based on the Evidence Pack.

---

# Plerixafor: From Stem Cell Mobilization to Myeloid Leukemia

## One-Sentence Summary

Plerixafor (Mozobil) is a CXCR4 receptor antagonist approved internationally for hematopoietic stem cell mobilization prior to autologous transplantation, though it currently holds no marketing authorization in Sweden.

The TxGNN model's top-scoring prediction is **Indolent Plasma Cell Myeloma** (score 99.97%), but that direction carries no clinical evidence (L5). The most actionable prediction — and the focus of this report — is **Myeloid Leukemia** (score 99.02%), where Plerixafor acts as a chemosensitizer by dislodging leukemia stem cells from their protective bone marrow niche.

This direction is supported by **30 clinical trials** and **20 publications**, including multiple completed Phase 1/2 studies that directly tested Plerixafor as a chemosensitizing agent in AML patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hematopoietic stem cell mobilization (international approval; not authorized in Sweden) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L2 |
| Sweden Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Plerixafor is a small-molecule CXCR4 antagonist. Its established mechanism involves blocking the CXCL12–CXCR4 interaction that normally anchors hematopoietic stem cells within the bone marrow microenvironment. By disrupting this axis, Plerixafor mobilizes stem cells into peripheral blood — the pharmacological basis of its approved use in autologous transplant preparation for lymphoma and myeloma patients.

In acute myeloid leukemia, leukemia stem cells (LSCs) exploit the exact same CXCL12–CXCR4 signalling axis to shelter within protective bone marrow niches, effectively hiding from cytotoxic chemotherapy. This stroma-mediated drug resistance is a well-established driver of treatment failure and disease relapse in AML. Blocking CXCR4 with Plerixafor evicts LSCs from their sanctuary and re-exposes them to chemotherapy — a strategy termed "chemosensitization" — which is mechanistically direct and biologically well-founded.

The mechanistic bridge from the approved indication to myeloid leukemia is unusually strong: the same molecule, the same receptor, the same biological axis — applied in a different clinical context. Multiple completed Phase 1/2 trials have tested this hypothesis in AML patients, combining Plerixafor with regimens such as MEC, FLAG-Ida, decitabine, and sorafenib. A 2020 systematic review (Maganti et al., *Leukemia Research*) identified 19+ relevant preclinical and clinical studies supporting this approach.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Plerixafor + decitabine induction in older AML patients (≥60 yrs); largest Phase 1 cohort directly testing CXCR4 priming to sensitize leukemia stem cells to hypomethylating therapy |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | Completed | 113 | AML18 Pilot Trial: feasibility of adding Plerixafor (CXCR4 inhibitor) alongside standard DAE chemotherapy in older AML and high-risk MDS patients |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Completed | 55 | PLERIFLAG regimen (fludarabine + idarubicin + cytarabine + G-CSF + Plerixafor) as second-line induction in relapsed/refractory AML ≤65 yrs |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 + MEC (mitoxantrone, etoposide, cytarabine) in relapsed/refractory AML; foundational chemosensitization concept study |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF chemosensitization in relapsed/refractory AML; evaluates disruption of bone marrow microenvironment |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Completed | 33 | Plerixafor + G-CSF + sorafenib in FLT3-mutant AML; precision medicine approach combining niche disruption with targeted kinase inhibition |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Completed | 36 | Plerixafor + cytarabine/daunorubicin ("7+3") ± G-CSF in newly diagnosed AML; tests first-line chemosensitization |
| [NCT01141543](https://clinicaltrials.gov/study/NCT01141543) | Phase 1/2 | Completed | 12 | Plerixafor in myeloablative conditioning (Flu/Bu/TBI) for AML allografting; demonstrates feasibility of mobilizing residual leukemic stem cells prior to transplant |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Plerixafor + cytarabine + etoposide in pediatric relapsed acute leukemia and MDS; directly validates CXCR4 blockade as chemosensitizer in this population |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | Unknown | 28 | Plerixafor + donor lymphocyte infusion (DLI) for relapsed acute leukemia post-allogeneic HSCT; explores CXCR4 blockade to enhance immunotherapy access |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic Review | *Leukemia Research* | Plerixafor combined with chemo/HCT for acute leukemia: 19+ studies identified; provides the most comprehensive synthesis supporting L2 classification |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 Trial | *Blood* | 52 relapsed/refractory AML patients treated with Plerixafor chemosensitization; established CXCR4 inhibition as a viable clinical strategy in AML |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1/2 Trial | *Annals of Hematology* | PLERIFLAG regimen (FLAG-Ida + Plerixafor) in early relapsed/refractory AML; confirms high-dose IV Plerixafor mobilizes blasts and improves chemotherapy access |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 Trial | *Am J Hematology* | Sorafenib + Plerixafor + G-CSF in 28 relapsed/refractory FLT3-ITD AML patients; dose escalation confirms tolerability of triple stroma-targeted approach |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 Trial | *Haematologica* | Plerixafor + decitabine in 69 newly diagnosed older AML patients; evaluates leukemia stem cell mobilization and hypomethylating agent synergy |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Clinical Study | *BBMT* | Plerixafor in myeloablative conditioning for AML allografting; safety and tolerability confirmed; mobilization of leukemic stem cells into peripheral blood demonstrated |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | *Leukemia* | Most up-to-date comprehensive review of CXCR4 as a therapeutic target in AML; covers oncogenic progression, apoptotic regulation, and chemoresistance mediated by CXCL12–CXCR4 axis |
| [28718760](https://pubmed.ncbi.nlm.nih.gov/28718760/) | 2018 | Clinical Analysis | *Leukemia & Lymphoma* | CD25 expression as biomarker in older AML patients treated with Plerixafor + decitabine; CD25-positive blasts associated with inferior survival — potential patient selection tool |
| [29140182](https://pubmed.ncbi.nlm.nih.gov/29140182/) | 2018 | In Vitro Study | *Hematology* | TGF-β1 and CXCL12 modulate AML cell proliferation and chemotherapy sensitivity in MSC co-culture; provides in vitro mechanistic rationale for CXCR4 blockade |
| [33080779](https://pubmed.ncbi.nlm.nih.gov/33080779/) | 2020 | Review | *Cells* | Hyperleukocytosis and leukostasis in AML: molecular pathophysiology including CXCR4 pathway; contextualizes the biological importance of the target |

---

## Sweden Market Information

Plerixafor is not currently authorized in Sweden. No marketing authorizations were identified in the regulatory database.

> **Note:** Internationally, Plerixafor is marketed as **Mozobil® (Sanofi Genzyme)** and holds FDA approval (2008) and EMA approval for use with G-CSF to enhance mobilization of hematopoietic progenitor cells in patients with non-Hodgkin's lymphoma and multiple myeloma prior to autologous stem cell transplantation. Any use in Sweden — for the approved indication or the proposed myeloid leukemia indication — would require a separate regulatory pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data note:** Formal safety data (package insert warnings, contraindications, and drug interaction records) were not retrievable from Swedish/Taiwanese regulatory sources in this data pack, as Plerixafor holds no local authorization. Internationally available prescribing information (EMA/FDA SmPC/label for Mozobil) should be consulted for adverse event profiles, including injection site reactions, gastrointestinal effects, and haematological parameters requiring monitoring when co-administered with myelosuppressive chemotherapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 1/2 clinical trials have directly tested Plerixafor as a CXCR4-blocking chemosensitizer in AML, with a mechanistic link that is unusually well-defined and biologically direct. The 2020 systematic review by Maganti et al. consolidates 19+ studies, placing this at the L2 evidence tier. The absence of a completed Phase 3 RCT is the primary gap preventing a "Go" recommendation.

**To proceed, the following is needed:**

- **Phase 2/3 efficacy data:** No randomized controlled trial has yet confirmed superiority over standard-of-care in AML; this is the critical missing piece for upgrading to L1 evidence
- **Regulatory pathway assessment:** Plerixafor has no Swedish marketing authorization; a compassionate use, named-patient program, or formal EMA extension application would be required
- **MOA documentation:** Formal mechanism-of-action data from DrugBank or the TFDA package insert should be retrieved and incorporated into the safety dossier
- **Safety profiling for combination regimens:** Adverse event profiles for Plerixafor when combined with AML-specific regimens (decitabine, MEC, FLAG-Ida, sorafenib) need to be compiled from the completed trial publications
- **Patient selection biomarkers:** CD25 expression (PMID 28718760) and CXCR4 surface density may predict response; prospective validation is recommended before broad use
- **Pediatric-specific evaluation:** NCT01319864 tested Plerixafor in pediatric leukemia — a separate safety and dosing assessment is needed if this population is to be included
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

