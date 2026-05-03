---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The skill confirms this is standard TxGNN pipeline output. Now generating the evaluation report from the Evidence Pack:

---

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for the treatment of HIV-1 infection in humans.
The TxGNN model predicts it may have potential for **Feline Acquired Immunodeficiency Syndrome (FIV)**,
currently supported by **no directly relevant clinical trials** and **1 in vitro biochemical/structural study**—placing this firmly at the early-research stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral therapy) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Efavirenz is an NNRTI that binds to an allosteric (non-active-site) pocket on HIV-1 reverse transcriptase (RT), blocking the enzyme's conformational dynamics and halting viral RNA-to-DNA conversion. This mechanism is the cornerstone of its established efficacy in human HIV-1 treatment regimens such as Atripla. Currently, detailed pharmacological mechanism of action data from the evidence pack is unavailable; the above description is derived from contextual information within the Evidence Pack itself.

Feline Immunodeficiency Virus (FIV) is a lentivirus that, like HIV-1, depends on its own reverse transcriptase for replication. The structural homology between FIV RT and HIV-1 RT provides the theoretical basis for the TxGNN model's prediction. On paper, a drug that disables HIV-1 RT might also interfere with FIV RT via the same pocket.

However, the NNRTI binding pocket in FIV RT differs substantially from HIV-1 RT at several key amino acid residues. A 2023 study (PMID 38031646) directly compared the activity of first- and second-generation NNRTIs—including efavirenz—against both HIV and FIV reverse transcriptases using biochemical and structural methods. The findings confirm that these structural differences significantly reduce efavirenz's potency against FIV RT. The mechanistic link is therefore a **weak analogical inference**, not a direct mechanistic equivalence, and structural re-engineering of NNRTI scaffolds would likely be required before meaningful FIV activity could be achieved.

---

## Clinical Trial Evidence

> ⚠️ **Important caveat:** Both trials retrieved for this indication are graded **C (not relevant)**. NCT01263015 and NCT00951015 both study **dolutegravir** (an integrase inhibitor) versus Atripla in **human HIV-1** infection—they have no bearing on efavirenz's use for feline AIDS. They are listed below for transparency but **do not constitute supporting evidence** for this repurposing direction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla in ART-naïve HIV-1 adults over 96 weeks — **not relevant to FIV indication** |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection for dolutegravir in ART-naïve HIV-1 subjects — **not relevant to FIV indication** |

**Net result: No relevant clinical trials for efavirenz in feline acquired immunodeficiency syndrome have been identified.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Biochemical / Structural Study | Journal of Veterinary Science | Compared NNRTIs—including nevirapine, efavirenz, and rilpivirine—against both FIV and HIV reverse transcriptases; structural divergence in the NNRTI binding pocket explains substantially reduced potency of conventional NNRTIs against FIV RT |

---

## Sweden Market Information

No marketing authorizations for efavirenz were found in available Swedish regulatory records. The drug is not currently marketed in Sweden.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Analyst note:** Safety data (key warnings, contraindications, drug interactions) were not retrievable from the current data sources. A notable concern flagged in the mechanistic rationale is that efavirenz carries well-documented CNS side effects (neuropsychiatric symptoms, neurotoxicity) in humans. Species-specific tolerability in cats is unknown and would need to be characterised before any preclinical work proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically coherent in principle—both HIV-1 and FIV rely on reverse transcriptase—but the sole available study demonstrates that structural differences in the FIV RT binding pocket substantially limit efavirenz's activity. With no relevant clinical trials and only one in vitro/structural comparison study (L4 evidence), the current evidence base is insufficient to justify advancing toward even a formal preclinical development programme without further foundational work.

**To proceed, the following is needed:**

- **In vitro activity data:** EC₅₀ and selectivity index of efavirenz against FIV in feline cell lines
- **Structural optimisation pathway:** Assessment of whether second-generation NNRTIs (e.g., rilpivirine) or novel scaffolds can overcome the FIV RT binding pocket differences identified in PMID 38031646
- **Pharmacokinetic/pharmacodynamic profile in cats:** Species-specific metabolism, bioavailability, and tolerability data
- **Safety characterisation:** Efavirenz's CNS toxicity profile in humans raises a flag; feline CNS tolerability must be evaluated before in vivo studies
- **Full MOA documentation:** Retrieve efavirenz's complete DrugBank pharmacology entry to support mechanistic linking analysis
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

