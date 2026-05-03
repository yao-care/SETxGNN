---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

Using `txgnn-pipeline` skill noted. Now I'll analyze the Evidence Pack and generate the report per the v5 template.

---

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant granulocyte colony-stimulating factor (G-CSF) internationally established for treating and preventing neutropenia — most commonly in patients receiving myelosuppressive chemotherapy or undergoing hematopoietic stem cell transplantation (HSCT).
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **14 clinical trials** identified and **1 publication** currently available; however, none of the trials directly target this platelet disorder, placing the evidence at a preclinical/mechanistic level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered products in Sweden |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, filgrastim is a recombinant human G-CSF that binds to the G-CSF receptor (CD114), stimulating the proliferation, differentiation, and functional activation of neutrophil precursors in the bone marrow. Its principal clinical use internationally is to shorten severe neutropenia following myelosuppressive chemotherapy, and to mobilize hematopoietic progenitor cells into peripheral blood for collection and transplantation.

The proposed mechanistic link to primary release disorder of platelets is grounded in the observation that CD114 (G-CSF receptor) is also expressed on megakaryocytes — the bone marrow cells responsible for producing platelets. In principle, G-CSF signaling through megakaryocytic CD114 could influence the biogenesis and regulated exocytosis of platelet alpha-granules and dense-granules, the structures whose deficient secretion defines primary release disorders. This is a biologically plausible hypothesis worth exploring at the preclinical level.

However, the mechanism remains speculative. All 14 clinical trials identified in the evidence search use filgrastim exclusively as a supportive agent within HSCT or oncology protocols — not as a targeted intervention for platelet release disorders. The TxGNN prediction most likely reflects the proximity of relevant disease nodes in the knowledge graph rather than a validated pharmacological relationship. Independent preclinical confirmation is required before clinical translation can be considered.

---

## Clinical Trial Evidence

> ⚠️ **Important caveat:** None of the following trials directly investigate filgrastim as a treatment for primary release disorder of platelets. In every case, filgrastim appears as a supportive agent for stem cell mobilization or post-transplant neutrophil recovery.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT (peripheral blood or cord blood) for hematological malignancies; filgrastim used for donor stem cell mobilization and post-transplant neutrophil support |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplantation for high-risk pediatric sarcomas; filgrastim used for PBSC mobilization; evaluated safety and antitumour immune effect |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ cell selection vs. no selection in ASCT for advanced mantle cell or DLBCL; filgrastim for stem cell mobilization; primary endpoint: 3-year overall survival |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT feasibility study for GATA2 mutation patients; filgrastim used as standard transplant support for engraftment |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Randomised controlled trial of AHSCT vs. best available therapy for treatment-resistant relapsing multiple sclerosis; filgrastim for PBSC mobilization; 72-month follow-up planned |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding study for post-transplant cyclophosphamide + sirolimus + MMF as GvHD prophylaxis after reduced-intensity PBSC transplantation; filgrastim as supportive drug for mobilization |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing PTCy-based GvHD prophylaxis regimens in mismatched unrelated donor PBSC transplant; filgrastim as standard mobilization support |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant combined with NK cells and aldesleukin for myeloid leukemia; filgrastim included for post-transplant haematopoietic recovery |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion followed by autologous HSCT for severe systemic lupus erythematosus; filgrastim used for stem cell mobilization prior to immune reset |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT using busulfan, fludarabine, and total-body irradiation for hematological malignancies; filgrastim as standard PBSC mobilization and donor lymphocyte infusion support |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Observational/Cohort | Frontiers in Immunology | G-CSF mobilization in healthy allogeneic donors preferentially mobilises specific lymphocyte subsets; graft depletion strategies investigated to reduce post-transplant immune-mediated complications without compromising antileukaemic activity |

---

## Sweden Market Information

Filgrastim currently has no registered product authorizations in Sweden. No approved indication text is available from the Swedish registry (total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The overall evidence level is L4 (mechanistic/preclinical reasoning only). All 14 identified clinical trials enrol filgrastim as a supportive agent in HSCT and oncology settings — none are designed to test filgrastim as a direct therapy for primary release disorder of platelets. The proposed megakaryocytic CD114 mechanism is biologically plausible but wholly unvalidated, and the drug has no registered products in Sweden, leaving both the benefit and safety profile for this indication entirely uncharacterised.

**To proceed, the following is needed:**

- **Preclinical mechanistic studies**: In vitro and in vivo experiments examining G-CSF effects on megakaryocyte granule biogenesis (alpha-granule and dense-granule formation) and stimulus-coupled secretion
- **Case series or observational data**: Systematic search for any published reports of G-CSF use in patients with platelet secretion defects or storage pool disorders
- **MOA documentation**: Formal retrieval of filgrastim's mechanism of action from DrugBank or SmPC to confirm or rule out megakaryocyte-specific activity
- **Safety profile establishment**: Full review of the EMA/MHRA Summary of Product Characteristics (SmPC) for relevant warnings, contraindications, and drug interactions before any clinical hypothesis can be formed
- **Clarification of therapeutic target**: Determine whether the proposed benefit would come from filgrastim directly modulating platelet secretion, or indirectly via megakaryocyte expansion — as these require different trial designs and endpoints
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

