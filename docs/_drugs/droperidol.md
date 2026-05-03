---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Droperidol
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

以下是根據 Evidence Pack 生成的藥師評估報告：

---

# Droperidol: From Perioperative Antiemesis to Tourette Syndrome

## One-Sentence Summary

Droperidol is a butyrophenone-class neuroleptic used in perioperative and emergency settings as an antiemetic and sedative for acute agitation.
The TxGNN model predicts it may be effective for **Tourette Syndrome**, supported by **0 clinical trials** and **1 indirect publication** (via the related drug Haloperidol) at this time.
Notably, among all 10 predicted indications in this pack, **Headache Disorder** (rank 7) carries significantly stronger evidence — 1 clinical trial and 20 publications — and warrants parallel consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Perioperative antiemesis and sedation for acute agitation (no Taiwan approvals on record) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Droperidol is a butyrophenone-class compound and a potent dopamine D2 receptor antagonist — pharmacologically the same core mechanism as Haloperidol, which holds FDA approval for Tourette syndrome. Although DrugBank MOA data was not retrieved in this analysis, it is well-established that D2 blockade reduces tic severity by suppressing dopaminergic overactivity in the basal ganglia circuit, which is central to Tourette syndrome pathophysiology. The TxGNN knowledge graph most likely captured this drug-class–disease link through shared receptor targets.

The mechanistic extrapolation from Haloperidol to Droperidol is scientifically defensible: both are butyrophenones acting on the same receptor at comparable affinity. The prediction is therefore a class-level inference, not a random association. For a genetic tic disorder where D2 antagonism is the established pharmacological rationale, Droperidol is a structurally and mechanistically coherent candidate.

However, significant practical barriers exist. First, Droperidol is formulated almost exclusively for intravenous and intramuscular administration in acute procedural settings, whereas Tourette syndrome requires long-term oral maintenance therapy — a route-of-administration mismatch that cannot be resolved without new formulation development. Second, the 2001 FDA black box warning for QTc interval prolongation makes chronic daily use highly problematic. These limitations explain the L4 evidence level and Hold recommendation despite the high TxGNN score.

---

## Clinical Trial Evidence

Currently no clinical trials for Droperidol in Tourette Syndrome have been registered on ClinicalTrials.gov or the ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Clinical Study (Indirect) | Current Psychiatric Therapies | Evaluates Haloperidol — a class-related butyrophenone D2 antagonist — in severe behavior disorders; not a direct study of Droperidol in Tourette syndrome. Serves as a class-analogy reference only. |

---

## Safety Considerations

Droperidol carries a **black box warning for QTc interval prolongation and potentially fatal cardiac arrhythmias** (FDA, 2001). This warning was the primary driver behind its reduced clinical utilization over the past two decades and is a critical constraint for any chronic-use repurposing scenario. A 2020 review ([PMID 32839811](https://pubmed.ncbi.nlm.nih.gov/32839811/)) has argued for reintegration of Droperidol into emergency practice under appropriate monitoring, but this does not extend to outpatient chronic administration.

Formal Taiwan package insert warnings and contraindications were not available for this analysis. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic analogy between Droperidol and Haloperidol is pharmacologically sound, but no direct clinical or preclinical evidence supports Droperidol specifically in Tourette syndrome. Combined with the QTc black box warning and the route-of-administration mismatch for chronic use, the current evidence base is insufficient to advance this indication.

**Cross-indication highlight:**
The most actionable finding in this Evidence Pack is **Headache Disorder (rank 7)** — Evidence Level L3, with 1 clinical trial and 20 publications, including endorsements from both the American Headache Society (2015) and the Canadian Headache Society (2015). This indication already carries a **"Proceed with Guardrails"** recommendation and may represent a higher-priority near-term target for further investigation.

**To proceed with Tourette Syndrome exploration, the following is needed:**

- Direct preclinical studies of Droperidol in validated Tourette syndrome animal models
- Route-of-administration feasibility assessment (oral formulation development or depot alternatives)
- Comprehensive cardiac safety profiling, given the QTc black box warning
- DrugBank MOA data retrieval to confirm receptor binding profile (Data Gap DG002)
- Taiwan TFDA package insert review for warnings and contraindications (Data Gap DG001)
- Comparative benchmarking against currently approved Tourette treatments (Haloperidol, pimozide, fluphenazine, aripiprazole)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

