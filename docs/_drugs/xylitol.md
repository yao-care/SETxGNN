---
layout: default
title: Xylitol
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 1
---

# Xylitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The txgnn-pipeline skill is about pipeline management and doesn't override the report-writing instructions. Proceeding directly to generate the report from the Evidence Pack.

---

# Xylitol: From Dental Caries Prevention to Meningococcal Infection

## One-Sentence Summary

Xylitol is a naturally occurring sugar alcohol widely used as a dental health aid and sugar substitute, with documented activity against nasopharyngeal bacterial colonisation (notably *Streptococcus pneumoniae*).
The TxGNN model predicts it may be effective for **Meningococcal Infection**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction — placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal indication registered in Taiwan (TFDA); commonly used for dental caries prevention and sugar substitution |
| Predicted New Indication | Meningococcal Infection |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on the pharmacological literature, xylitol is a five-carbon sugar alcohol that interferes with bacterial adhesion to nasopharyngeal mucosa primarily by disrupting the bacterial **phosphotransferase system (PTS)** — a key metabolic transport pathway in gram-positive and gram-negative bacteria alike. This mechanism is best characterised for *Streptococcus pneumoniae*, where xylitol has been shown in clinical trials to reduce nasopharyngeal carriage and incidence of acute otitis media.

*Neisseria meningitidis*, the causative agent of meningococcal disease, similarly colonises the nasopharynx before invasive spread. The theoretical mechanistic analogy is therefore anatomically and microbiologically plausible: if xylitol can disrupt colonisation of the nasopharynx by one bacterial pathogen via PTS inhibition and anti-adhesion effects, it is conceivable — in principle — that a similar effect could occur with *N. meningitidis*. This is the biological basis that likely drove the TxGNN knowledge-graph model to surface this prediction.

However, it is essential to state clearly: **no in vitro, animal, or clinical studies have directly tested xylitol against *N. meningitidis***. The entire mechanistic argument is drawn from cross-pathogen inference, and the formal MOA entry for this compound is absent from the current evidence pack. The high TxGNN score (99.66%) reflects topological similarity within the disease–drug knowledge graph, not empirical experimental evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Xylitol in meningococcal infection.

---

## Literature Evidence

Currently no related literature available for Xylitol in meningococcal infection.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on model inference without any supporting experimental, clinical, or epidemiological data — classified as evidence level L5. While the mechanistic analogy through nasopharyngeal anti-adhesion is biologically plausible, it remains speculative and untested for *N. meningitidis* specifically. A Hold decision is warranted until foundational evidence is generated.

**To proceed, the following is needed:**

- **In vitro studies**: Minimum inhibitory concentration (MIC) and anti-adhesion assays of xylitol against *N. meningitidis* strains to confirm whether PTS inhibition or adhesion disruption actually occurs
- **MOA clarification**: Retrieve full mechanistic profile from DrugBank (DB11195) and primary literature to confirm whether the PTS-disruption hypothesis extends to gram-negative organisms such as *Neisseria*
- **Safety data**: Obtain TFDA package insert (if applicable) or international equivalents to document contraindications, warnings, and special population restrictions before any exploratory clinical use
- **Dosing considerations**: Xylitol is used across a wide dose range (topical dental to oral systemic). For an anti-infective indication, appropriate systemic concentrations and tolerability at those doses must be established
- **Regulatory pathway assessment**: Since xylitol has zero authorisations in Taiwan and is generally classified as a food ingredient / excipient, a regulatory strategy for reclassification as an investigational drug would be needed before clinical trials can be initiated
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

