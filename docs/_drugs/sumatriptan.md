---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

# Sumatriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a selective serotonin (5-HT1B/1D) receptor agonist and the prototypical triptan, established worldwide as first-line acute treatment for migraine attacks. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly called basilar migraine), with **0 registered clinical trials** and **18 publications** currently relevant to this direction — though most evidence addresses migraine with aura broadly rather than this specific subtype. Given a historical (and mechanistically contested) contraindication, direct clinical validation for this subtype is still lacking.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine treatment (established global clinical use; no local registered licenses found) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Market Status | Not marketed (0 local licenses) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sumatriptan acts as a potent, selective agonist at 5-HT1B and 5-HT1D serotonin receptors, producing two complementary anti-migraine effects: it constricts dilated cranial blood vessels (particularly in the dura mater) and suppresses trigeminal nerve endings from releasing pain mediators such as CGRP and substance P. This dual vascular-neuronal mechanism underlies its proven efficacy in acute migraine and is the pharmacological basis of the entire triptan drug class.

Migraine with Brainstem Aura (MBA) — formerly termed basilar-type migraine — is a migraine subtype in which aura symptoms clearly originate from the brainstem (e.g., diplopia, dysarthria, tinnitus, ataxia, decreased consciousness) or affect both visual fields simultaneously. Critically, MBA shares the same trigeminovascular pathway as other migraine subtypes, which is precisely where sumatriptan exerts its effect. The TxGNN model correctly identified this mechanistic overlap. Historically, however, sumatriptan was listed as contraindicated in this subtype due to theoretical concerns that basilar artery vasoconstriction could precipitate brainstem ischaemia.

Modern neurophysiology has substantially revised the understanding of MBA: the primary pathophysiological mechanism is now thought to be cortical spreading depression (CSD) propagating into brainstem structures, rather than primary vascular constriction. This shift makes the historical contraindication increasingly difficult to justify on mechanistic grounds — yet no prospective clinical trial has formally tested sumatriptan safety and efficacy specifically in MBA. In short, the biological rationale for repurposing is sound, but the safety question has never been directly answered in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sumatriptan specifically in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Early sumatriptan administration significantly prevented PACAP38-provoked migraine attacks; supports early intervention strategy |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Meta-analysis | Neurology | Sumatriptan is significantly less effective in migraine with aura than without aura — the most directly relevant finding to the brainstem aura subtype |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing sumatriptan vs. ginger powder in acute migraine without aura; both showed comparable efficacy |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Practice Guideline | Headache | American Headache Society updated evidence assessment confirms sumatriptan as a Level A (established) acute migraine therapy |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of sumatriptan 200 mg oral in acute migraine with aura; demonstrated meaningful efficacy in the aura subtype |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Clinical Study | Neurology | Subcutaneous sumatriptan and the migraine aura — early direct investigation of triptan use in aura-associated attacks |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanistic Study | JAMA Neurology | PET imaging showed sumatriptan binds central 5-HT1B receptors during migraine attacks, supporting a central (not purely vascular) mechanism of action |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Critical Review | Cephalalgia | Comprehensive review of all published sumatriptan trials; detailed analysis of dual vascular/neuronal mechanism and clinical efficacy across migraine subtypes |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review | Expert Review of Neurotherapeutics | Needle-free subcutaneous sumatriptan remains effective even in patients with established central sensitisation — relevant to severe or refractory migraine subtypes |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus as a complication of migraine with or without aura; highlights treatment gaps and the functional burden, providing context for refractory migraine management |

---

## Safety Considerations

Please refer to the package insert for full safety information.

> ⚠️ **Critical note for this repurposing context:** Current prescribing information for sumatriptan and other triptans typically lists hemiplegic migraine and basilar-type migraine (migraine with brainstem aura) as contraindications, based on the theoretical risk of basilar artery vasospasm causing brainstem ischaemia. Any clinical application to MBA must formally address whether this contraindication remains valid under modern mechanistic understanding, and must include prospective safety monitoring. This contraindication review is a prerequisite before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for sumatriptan in migraine with brainstem aura is biologically plausible under the modern CSD model, and the TxGNN prediction score is very high (99.74%). However, no clinical trials have directly tested sumatriptan in this specific subtype, current prescribing labels carry an explicit contraindication for this population, and available literature addresses migraine with aura broadly rather than MBA specifically. The evidence is insufficient and the safety question unresolved — this should be treated as a research question rather than a ready repurposing candidate.

**To proceed, the following is needed:**

- **Contraindication re-evaluation:** Systematic review of whether the basilar/brainstem aura contraindication is still supported by current evidence — this is the single most important blocker
- **MOA data retrieval:** Obtain full DrugBank mechanism-of-action data to complete the mechanistic dossier
- **Safety data:** Download and parse the full prescribing information (package insert / SmPC) to populate key warnings and contraindications
- **Prospective case series or observational study:** Collect real-world safety data in MBA patients who have received sumatriptan (some may have been treated off-label)
- **Phase 2 pilot trial design:** If contraindication review supports feasibility, design a small Phase 2 trial with enhanced safety monitoring (neuroimaging, brainstem perfusion assessment) as the minimum clinical evidence threshold
- **Drug interaction screening:** Complete DDI assessment before any clinical application
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

