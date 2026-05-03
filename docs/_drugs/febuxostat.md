---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 3
---

# Febuxostat
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the evaluation report based on the Evidence Pack.

---

# Febuxostat: From Hyperuricemia (Gout) to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a selective xanthine oxidoreductase (XOR) inhibitor, globally established for treating chronic hyperuricemia in gout patients.
The TxGNN model predicts it may be effective for **Renal Hypouricemia** — specifically in preventing exercise-induced acute kidney injury (EIAKI) in patients with hereditary renal urate transport defects —
with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic hyperuricemia associated with gout (no Taiwan regulatory data on file) |
| Predicted New Indication | Hypouricemia, renal (prevention of exercise-induced AKI) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, febuxostat is a **non-purine selective inhibitor of xanthine oxidoreductase (XOR)** — the terminal enzyme in purine catabolism that converts hypoxanthine → xanthine → uric acid. By blocking XOR, febuxostat reduces uric acid production at the source, which is the same mechanism responsible for its efficacy in gout-related hyperuricemia.

In **renal hypouricemia (RHUC)**, loss-of-function mutations in urate transporters (URAT1 / ABCG2) cause the kidneys to over-excrete uric acid, producing abnormally low serum urate. The paradox is that during intense anaerobic exercise, rapid purine breakdown generates a large transient flux of hypoxanthine and xanthine through the XOR pathway. This oxidative burst in the renal tubules — not the baseline low uric acid itself — is thought to trigger EIAKI. The repurposing logic therefore targets the **complication, not the primary diagnosis**: febuxostat suppresses peak XOR activity during exercise, reducing oxidative substrate load and free-radical injury to tubular cells.

This mechanism is biologically plausible and is directly analogous to the reported benefit of allopurinol (another XOR inhibitor) in the same setting. At least one published case explicitly proposes febuxostat as a prophylactic agent in RHUC-related EIAKI, citing its superior XOR selectivity and more predictable pharmacokinetics compared to allopurinol. The mechanistic link is indirect (febuxostat was designed to lower uric acid, not protect kidneys), but the biological rationale is sound.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study at Shanghai Xu-hui Central Hospital examining whether tight uric acid control reduces kidney stone recurrence and preserves renal function in hyperuricemia patients with nephrolithiasis |

> ⚠️ **Caveat:** This trial's status is listed as Unknown and its registry title displays only the sponsoring institution. It is unclear whether febuxostat was the primary comparator, and no results data are available. Direct review of the ClinicalTrials.gov record is recommended before citing this trial as direct evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Hypothesis / Case Report | Internal Medicine (Tokyo) | A 16-year-old football player with familial RHUC (compound heterozygous URAT1 mutations) and recurrent EIAKI: standard hydration prophylaxis failed; febuxostat proposed as a preventive strategy by reducing XOR-mediated oxidative stress during anaerobic exercise |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrative Review | Clinical Rheumatology | Comprehensive update on hypouricemia for rheumatologists covering etiology, diagnosis, and management; addresses RHUC pathophysiology and its exercise-related complications including EIAKI |

---

## Taiwan Market Information

Febuxostat has **no registered authorizations in Taiwan** and has not been submitted for Taiwan FDA (TFDA) review based on available data.

> For reference: febuxostat is approved in major markets under brand names Uloric® (US, FDA 2009), Adenuric® (EU, EMA 2008), and Feburic® (Japan). A formal TFDA New Drug Application would be required prior to any local clinical development or commercialization.

---

## Safety Considerations

Safety data (local package insert warnings, contraindications, and drug interaction records) was not retrievable from the Taiwan regulatory database for this Evidence Pack.

Please refer to the package insert for safety information.

> **Note for reviewers:** This data gap is classified as **Blocking** for the S1 safety screening stage. Before any development decision can progress, the following globally known safety signals must be formally reviewed and documented:
> - **Cardiovascular mortality** (FDA Boxed Warning, 2019): CARES trial demonstrated higher cardiovascular death rates vs. allopurinol; use is restricted in patients with established CV disease
> - **Critical drug interactions**: Co-administration with azathioprine, mercaptopurine, or theophylline is contraindicated or requires major dose adjustment due to XOR-mediated accumulation
> - **Gout flare on initiation**: Transient flare risk in gout patients; standard prophylaxis protocols apply

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting febuxostat for renal hypouricemia is currently limited to a single Phase 4 trial with unknown status and two narrative-level publications — insufficient to support a development commitment. More critically, Taiwan package insert safety data (a Blocking data gap) has not been resolved, precluding formal S1 safety evaluation.

**To proceed, the following is needed:**

- **Resolve Blocking data gap**: Retrieve and parse the Taiwan TFDA package insert (or equivalent reference labeling) to complete S1 safety screening, especially cardiovascular risk and contraindication assessment
- **Confirm trial relevance**: Contact investigators or review full NCT04398251 record to verify whether febuxostat was the primary intervention and whether results are available
- **Obtain MOA documentation**: Query DrugBank API (DB04854) to formally document the mechanism of action for regulatory and scientific review purposes
- **Assess indication scope**: Determine whether the target population (RHUC-related EIAKI) constitutes a rare/orphan disease designation opportunity, which may affect the development pathway and regulatory strategy
- **Consider related predictions**: TxGNN also predicts benefit in HPRT partial deficiency (Kelley-Seegmiller syndrome, score 99.98%) and Lesch-Nyhan syndrome (score 99.68%) — both involve XOR-driven hyperuricemia from impaired purine salvage; these may be bundled into a single purine metabolism disorder program if evidence supports it
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

