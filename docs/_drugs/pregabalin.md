---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill as context — this is a TxGNN Se (Sweden) project pharmacist report. I'll now generate the evaluation report per the v5 prompt format.

---

# Pregabalin: From Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is a gabapentinoid anticonvulsant and analgesic, established in clinical practice for neuropathic pain, partial-onset seizures, and fibromyalgia.
The TxGNN model predicts it may be effective for **Tendinitis**,
with **0 clinical trials** and **6 publications** currently supporting this direction — though none directly evaluate pregabalin as a tendinitis treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuropathic pain, partial-onset seizures, fibromyalgia (established uses; no Swedish regulatory records retrieved) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Sweden Market Status | No records found |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pregabalin is a gabapentinoid that binds to the α2-δ subunit of voltage-gated calcium channels in the central nervous system, reducing presynaptic calcium influx and the release of excitatory neurotransmitters (glutamate, substance P, norepinephrine). This mechanism underlies its efficacy in neuropathic pain and epilepsy. However, detailed MOA data was not retrieved from DrugBank in this evidence pack, so the mechanistic analysis below draws on established pharmacological knowledge and contextual literature signals.

Tendinitis is primarily a local inflammatory condition driven by prostaglandins, cytokines, and mechanical tissue stress at the tendon level. Pregabalin's core mechanism — calcium channel modulation reducing central sensitization — has only partial overlap with this pathophysiology. A theoretical neuropathic overlap exists in chronic tendinopathy, where central sensitization contributes to persistent pain even after the acute inflammatory phase resolves. In that narrow subpopulation, pregabalin's analgesic mechanism could be relevant.

The retrieved literature does not support pregabalin as a direct tendinitis treatment. The two highest-tier publications are perioperative RCTs after rotator cuff repair surgery — a different clinical context. The TxGNN prediction likely reflects graph-level proximity through shared "musculoskeletal pain" and "nociception" nodes rather than a direct biological link to tendinitis. Evidence is preclinical or indirect at best, placing this at L4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT (perioperative) | Arthroscopy | Perioperative oral pregabalin produced postoperative pain scores equivalent to interscalene brachial plexus block after arthroscopic rotator cuff repair; opioid-sparing effect observed |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT (postoperative) | J Orthop Sci | Retrospective cohort evaluating pregabalin's analgesic and opioid-sparing effect after arthroscopic rotator cuff repair; results conflicting with limited evidence for this regimen |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case Report | Pain Practice | Posterior femoral cutaneous nerve neuropathy secondary to hamstring tendonitis from long-distance running; neuropathic pain management (including pregabalin-class drugs) discussed |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case Series / Review | Praxis | Fluoroquinolone-associated disability including tendinopathy reviewed; neurological and redox-system damage pathway highlighted; pregabalin mentioned in neurological symptom management context |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Animal Study | Adv Pharmacol Pharm Sci | Cissus quadrangularis assessed for vincristine-induced peripheral neuropathy in rats; plant reported to treat injured tendons; pregabalin used as pharmacological reference |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial Commentary | Arthroscopy | Piriformis syndrome with sciatic nerve compression at piriformis tendon discussed; multimodal analgesic context, no direct pregabalin-for-tendinitis data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.71%), the mechanistic overlap between pregabalin's calcium channel modulation and the primary inflammatory pathophysiology of tendinitis is indirect at best. All six retrieved publications address perioperative or neuropathic-overlap pain scenarios — none constitute a therapeutic study in tendinitis. With no registered clinical trials and only indirect preclinical signals (L4), the evidence base does not support moving forward at this stage.

**To proceed, the following is needed:**
- Retrieve DrugBank MOA data (DG002) to complete mechanistic link analysis
- Retrieve Swedish MPA / TFDA package insert safety data (DG001) for warnings and contraindications
- Conduct a targeted literature review specifically on chronic tendinopathy with neuropathic pain features to test the central-sensitization hypothesis
- If mechanistic rationale is confirmed, design a prospective pilot study in patients with chronic tendinopathy meeting neuropathic pain screening criteria (e.g., PainDETECT ≥ 19)
- Consider that pregabalin is a controlled substance in many jurisdictions (abuse potential); regulatory implications for any new indication must be assessed upfront
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

