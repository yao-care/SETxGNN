---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

Using the `txgnn-pipeline` skill to guide report generation. Now I'll generate the full evaluation report based on the Evidence Pack, focusing on the highest-evidence predicted indication: **Ankylosing Spondylitis** (L1 evidence, multiple RCTs, "Proceed with Guardrails").

---

# Flurbiprofen: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a phenylalkanoic acid non-steroidal anti-inflammatory drug (NSAID) with established clinical use in inflammatory rheumatic conditions including rheumatoid arthritis and osteoarthritis, though it currently holds no regulatory approval in Sweden.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis (AS)**, with a prediction score of **99.97%** (TxGNN global rank 124).
This direction is supported by **0 registered clinical trials** but **20 published studies**, of which at least 7 are randomised controlled trials that directly evaluated flurbiprofen in active AS patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No current regulatory approval in Sweden; published literature identifies use in rheumatoid arthritis, osteoarthritis, and allied rheumatic conditions |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Sweden Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN ranking:** TxGNN's highest-scoring predictions for flurbiprofen (ranks 1–7 in this list) point to rare skeletal dysplasias such as acromesomelic dysplasia and brachydactyly syndromes — genetic, structural conditions with no inflammatory pathology and no supporting evidence. These high scores likely reflect network topology artefacts (shared skeletal/musculoskeletal nodes) rather than genuine therapeutic signal. **Ankylosing spondylitis** is the only prediction in this Evidence Pack with actual clinical evidence (L1) and a direct mechanistic rationale, and is therefore the focus of this report.

---

## Why is This Prediction Reasonable?

Flurbiprofen is a potent dual COX-1/COX-2 inhibitor belonging to the phenylalkanoic acid class. It works by competing with arachidonic acid at the cyclo-oxygenase binding site, thereby suppressing prostaglandin synthesis — particularly PGE2 — and reducing inflammation, pain, and fever. Detailed DrugBank MOA data was unavailable for this Evidence Pack; the above description is derived from published clinical literature (PMID 391529, PMID 2670397). In preclinical models, flurbiprofen has been shown to be approximately 200 times more potent than aspirin and at least as potent as indomethacin as an anti-inflammatory agent.

Ankylosing spondylitis is a chronic seronegative spondyloarthropathy primarily affecting the axial skeleton and sacroiliac joints. Its core pathological driver is persistent PGE2-mediated inflammation leading to progressive enthesitis, syndesmophyte formation, and spinal fusion. HLA-B27 positivity is a major genetic risk factor, but the downstream inflammation is largely prostaglandin-dependent, making COX inhibition a mechanistically rational and well-validated approach. NSAIDs are the universally recognised first-line pharmacological therapy for AS across all major international guidelines (ASAS, ACR/EULAR).

The TxGNN prediction is strongly corroborated by decades of clinical research. Multiple double-blind randomised trials conducted between 1974 and 1986 directly evaluated flurbiprofen at 150–300 mg/day in active AS, consistently demonstrating efficacy equivalent to comparators such as indomethacin, phenylbutazone, and naproxen. A pooled safety analysis spanning nine Phase 3 trials involving 1,677 patients confirms a manageable safety profile across AS, OA, and RA populations. These studies predate mandatory ClinicalTrials.gov registration but represent robust Phase 3-level evidence in the modern sense.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP.

> **Context:** Clinical evidence for flurbiprofen in ankylosing spondylitis derives from trials conducted in the 1970s–1980s, prior to mandatory trial registration. Seven randomised controlled trials and a pooled Phase 3 safety analysis are documented in the published literature (see Literature Evidence below). No contemporary registration-era trials have been identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT | Am J Medicine | Double-blind RCT, 90 patients, 26 weeks: flurbiprofen 200 mg/day (3×/day) equally effective as phenylbutazone 300 mg/day in controlling AS pain and symptoms; some patients controlled at 150 mg/day |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT | Am J Medicine | Double-blind RCT, 57 patients, 26 weeks: flurbiprofen 200 mg/day (4×/day) as effective as indomethacin in controlling pain and associated AS symptoms; adequate control also achieved at 100 mg/day (2×/day) |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT | Br Med J | Double-blind crossover, 35 patients, 4 weeks: flurbiprofen 150 mg/day showed therapeutic efficacy approaching phenylbutazone 300 mg/day; well tolerated; authors conclude it may be a valuable alternative in AS |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT | NZ Med J | Double-blind crossover, 30 patients, 4 weeks: flurbiprofen 200 mg/day and naproxen 750 mg/day both highly effective in relieving AS pain and stiffness; no significant difference in efficacy between the two |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT | Curr Med Res Opin | Parallel double-blind RCT, 26 patients, 6 weeks: flurbiprofen 150–200 mg/day and indomethacin 75–100 mg/day equally effective in relieving AS joint pain and tenderness; no withdrawals due to lack of efficacy in either arm |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT | South Med J | Parallel double-blind RCT, 26 patients, 6 weeks: flurbiprofen equally effective as indomethacin across all efficacy endpoints for active AS |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT | Eur J Clin Pharmacol | Double-blind parallel RCT, 27 patients, 6 weeks: flurbiprofen 150–200 mg/day equally effective as phenylbutazone 300–400 mg/day in relieving AS joint pain and tenderness |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT | Ann Rheum Dis | Double-blind crossover comparison of indomethacin, flurbiprofen, and placebo in AS patients |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Safety Cohort | Am J Medicine | Pooled analysis of 9 Phase 3 trials (1,677 patients with AS, OA, or RA; 941 on flurbiprofen): no clinically significant drug-related effects on kidney or liver function across all age groups and disease categories |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Comprehensive pharmacology and clinical review: flurbiprofen 150–300 mg/day comparable in efficacy to indomethacin 75–150 mg/day and therapeutic aspirin doses in rheumatic diseases including AS; generally fewer side effects than aspirin |

---

## Sweden Market Information

Flurbiprofen currently holds no approved product authorisations in Sweden (MPA). No licences are available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The full TFDA package insert for flurbiprofen was identified in the query log but its content was not parsed into this Evidence Pack. As an NSAID, standard class-level risks — including gastrointestinal toxicity, cardiovascular events, renal function impairment, and interactions with anticoagulants — should be reviewed before clinical use. A proton pump inhibitor co-prescription strategy may be warranted for long-term AS treatment (see PMID [22350497](https://pubmed.ncbi.nlm.nih.gov/22350497/)).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Seven randomised controlled trials — including two 26-week Phase 3 studies enrolling 57 and 90 patients respectively — consistently demonstrate flurbiprofen's efficacy in active ankylosing spondylitis, with a safety profile comparable to indomethacin and phenylbutazone. The mechanism (COX inhibition → reduced PGE2 → suppressed axial inflammation) is the same validated pathway underpinning first-line NSAID therapy for AS, making this a mechanistically and clinically credible repurposing candidate.

**To proceed, the following is needed:**
- **Formal MOA documentation:** Retrieve complete mechanism of action data from DrugBank API (currently Data Gap DG002)
- **Package insert review:** Parse TFDA package insert content to extract contraindications and key warnings, including NSAID-class cardiovascular and GI risk warnings (currently Data Gap DG001)
- **DDI assessment:** Drug interaction data returned empty; a systematic DDI search (particularly for anticoagulants, antihypertensives, and corticosteroids commonly co-prescribed in AS) is required before any clinical decision
- **Contemporary trial search:** Conduct a broader ClinicalTrials.gov and EU CTR search using MeSH terms for the full spondyloarthropathy spectrum (axial SpA, nr-axSpA) to identify any post-2000 flurbiprofen trials that may have been missed
- **Regulatory pathway assessment:** Evaluate whether a Swedish MPA dossier, compassionate use programme, or academic prescribing pathway is appropriate given the absence of current market authorisation
- **Long-term safety protocol:** Given that AS is a lifelong condition, a risk management plan addressing chronic NSAID use (GI protection, cardiovascular monitoring, renal function checks) should be defined before initiation
---

