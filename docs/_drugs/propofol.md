---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the report based on the Evidence Pack.

---

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a short-acting intravenous anesthetic widely used for the induction and maintenance of general anesthesia and procedural sedation.
The TxGNN model predicts it may be effective for **Migraine Disorder** at sub-anesthetic doses,
with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anesthesia and intravenous sedation (established clinical use; no Taiwan authorization on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed in Taiwan |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Propofol (2,6-diisopropylphenol) is a potent positive allosteric modulator of GABA-A receptors. By enhancing inhibitory neuronal signaling, it reduces overall cortical excitability. Critically for migraine, it suppresses **cortical spreading depression (CSD)** — the electrophysiological wave thought to underlie migraine aura and to trigger the subsequent headache phase. This mechanism has been validated in an animal model (PMID 22390898), providing a plausible biological bridge from anesthetic to antimigraine use.

Beyond CSD suppression, propofol carries a secondary antiemetic profile: it inhibits dopamine D2 receptors and modulates 5-HT3 signaling, offering relief for the nausea and vomiting that frequently accompany migraine attacks. Propofol may additionally dampen nociceptive transmission in the trigeminal vascular system, the pathway responsible for the throbbing, vascular-type pain of migraine. These three converging mechanisms — CSD inhibition, antiemesis, and trigeminal pain modulation — provide a coherent pharmacological rationale for its use in migraine, distinct from its anesthetic role.

The concept of using sub-anesthetic ("low-dose") propofol for refractory migraine has been in clinical practice since at least 2000 (PMID 10759925) and is now included in discussions of second-line emergency department (ED) therapies by the American Headache Society (PMID 41321235, 2026 guideline update). The strongest controlled data come from pediatric ED settings, but adult ED evidence is accumulating through RCTs and systematic reviews.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Prospective RCT of sub-anesthetic propofol for abortive treatment of pediatric migraine in the ED; provides the primary controlled evidence base |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Evaluated efficacy, safe dosing limits, and duration of effect of low-dose propofol infusion as an abortive agent in pediatric migraine |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Adult ED trial of low-dose propofol for severe refractory migraine; terminated early (n=12); provides a safety signal but not conclusive efficacy data |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Unknown | 130 | Compared postoperative headache rates with propofol vs. sevoflurane maintenance, indirectly informing propofol's protective effect on migraine; status unverified |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | NA | Completed | 315 | Electroacupuncture analgesia in CABG surgery; propofol may appear in the control/anesthesia arm, but primary intervention is not propofol — low relevance to migraine indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Clinical Guideline | Headache | 2025 American Headache Society update on parenteral pharmacotherapies for acute migraine in the ED; propofol included in evidence assessment |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Academic Emergency Medicine | Systematic review evaluating the safety and efficacy of propofol for acute migraine treatment in the ED; concludes propofol is a viable option based on available limited evidence |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management; evaluates combination strategies |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | The Journal of Emergency Medicine | Prospective randomized controlled trial of low-dose propofol for pediatric migraine in the ED; assessed efficacy and length-of-stay impact |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | Evaluated sumatriptan/propofol combination vs. sumatriptan alone for acute migraine management in the ED |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Systematic Review & Network Analysis | Headache | Network meta-analysis comparing parenteral agents for reducing relapse after severe acute migraine; propofol included as comparator |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Current Pain and Headache Reports | Overview of IV migraine management in children and adolescents in the pediatric ED; reviews propofol among intravenous agents |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Review | Headache | Three-part series on rescue therapy for acute migraine; part 2 covers propofol among other agents (neuroleptics, antihistamines, nitrous oxide) |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Review | Expert Review of Neurotherapeutics | Detailed drug profile of propofol for management of refractory/super-refractory migraine headaches at sub-anesthetic doses |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Case Series | Headache | Foundational early report on propofol's unique effectiveness for refractory migraine in an outpatient headache center setting |

---

## Taiwan Market Information

Propofol currently holds no product authorizations in Taiwan. No approved indications, dosage forms, or license records are available.

> Note: Propofol is a widely available intravenous anesthetic internationally. The absence of Taiwan registration may reflect a data gap or the drug being procured through hospital-specific import channels rather than a commercial license. Verification with the TFDA drug license database is recommended.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interactions) was not retrievable from the Taiwan regulatory source at the time of this evaluation.

> Please refer to the originator package insert and current TFDA drug monograph for full safety information, particularly regarding:
> - **Cardiorespiratory depression**: Propofol causes dose-dependent hypotension and apnea; sub-anesthetic use for migraine must be performed with resuscitation equipment available and appropriate monitoring.
> - **Propofol Infusion Syndrome (PRIS)**: A rare but potentially fatal complication associated with high doses over prolonged infusion; not a concern at low single doses used for migraine.
> - **Lipid vehicle**: Propofol is formulated in a soy/egg lecithin emulsion — caution in patients with relevant allergies.
> - **Controlled setting requirement**: Due to sedation risk, sub-anesthetic propofol for migraine must be administered in a monitored clinical environment (ED or equivalent), not in ambulatory/outpatient settings without monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 controlled trial (NCT01604785, n=74) and multiple RCTs in the literature support the use of sub-anesthetic propofol for acute migraine, primarily in emergency department settings. The mechanistic rationale (CSD suppression via GABA-A enhancement) is well-grounded and independently validated in animal models, and the 2025/2026 American Headache Society guideline update includes propofol in its evidence review, reflecting growing clinical acceptance.

**To proceed, the following is needed:**

- **Taiwan regulatory pathway clarification**: Confirm whether propofol has any hospital formulary or import approval in Taiwan before clinical repurposing protocols are designed.
- **Adult outpatient data**: Current controlled evidence is heavily weighted toward the pediatric ED population; prospective adult trials with standardized endpoints are needed to generalize findings.
- **Formal MOA documentation**: A structured DrugBank/literature review of propofol's complete mechanism of action should be attached to the dossier to support regulatory submissions.
- **Safety monitoring protocol**: A site-specific protocol defining minimum monitoring requirements (vitals, oxygen saturation, IV access, recovery period) for sub-anesthetic propofol migraine treatment must be developed before any clinical implementation.
- **Dosing standardization**: The optimal sub-anesthetic dose range (typically reported as 10–40 mg IV bolus, repeated as needed) and maximum total dose for migraine should be explicitly defined in any institutional protocol.
- **TFDA package insert review**: Retrieve and parse the TFDA-registered product monograph (if any) or international reference product SPC to document contraindications formally.
---

