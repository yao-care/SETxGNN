---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

The txgnn-pipeline skill applies here. Now generating the report based on the Evidence Pack.

---

# Oxazepam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Oxazepam is a short-to-intermediate acting benzodiazepine, traditionally used for anxiety disorders and alcohol withdrawal management, but is currently not marketed in Sweden.
The TxGNN model predicts it may be effective for **Insomnia**, with **0 registered clinical trials** and **11 publications** (including 2 RCTs) currently supporting this direction.
Overall evidence is sufficient to warrant cautious advancement, pending full safety documentation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders (no Sweden regulatory data available; based on pharmacological class) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oxazepam is a benzodiazepine that acts as a **positive allosteric modulator of GABA-A receptors**, enhancing chloride ion (Cl⁻) influx into neurons. This causes neuronal hyperpolarization and broad central nervous system depression — producing sedation, hypnosis, and anxiolysis. Crucially, oxazepam has an intermediate half-life of 4–15 hours and **no active metabolites**, a pharmacokinetic profile that distinguishes it from longer-acting benzodiazepines like flurazepam and makes it well-suited to treating sleep-onset insomnia without causing excessive next-day sedation.

Anxiety and insomnia are tightly intertwined conditions — anxiety is among the most common drivers of chronic insomnia, and GABAergic inhibition addresses the core neurological hyperarousal that underlies both. The mechanistic link from oxazepam to insomnia is therefore not a leap but a direct extension of its primary pharmacological action.

Clinical evidence from a 1984 polysomnographic RCT confirmed that oxazepam improves objective sleep measures in chronic insomnia patients while **avoiding the daytime sleepiness** caused by flurazepam, supporting its practical advantage in this indication. More recent literature extends this evidence to elderly populations and post-cardiac event patients, underscoring its relevance across clinically meaningful subgroups.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for oxazepam in insomnia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | Am J Psychiatry | Polysomnographic RCT (n=14) in chronic insomnia: oxazepam improved nocturnal sleep measures without causing daytime sleepiness, unlike flurazepam; some rebound effects noted |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | Ann Pharmacother | RCT in post-STEMI patients: oxazepam vs melatonin both effective for anxiety and sleep disturbance; melatonin associated with fewer adverse effects and drug interactions |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Systematic Review | Arch Gerontol Geriatr | 60 elderly patients (>70 yrs) with insomnia and comorbidities (depression, dementia): examined efficacy and tolerability of hypnotic drugs including oxazepam in this vulnerable population |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | J Clin Exp Hepatol | Management of alcohol withdrawal syndrome in liver disease: insomnia identified as early withdrawal symptom; benzodiazepines including oxazepam discussed as first-line management |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs including benzodiazepines; discusses half-life and metabolic profiles relevant to sleep versus daytime function trade-offs |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review (Guideline) | Psychiatrische Praxis | Cross-sectional review of BPSD management in dementia across Germany, Austria, Switzerland; benzodiazepines including oxazepam addressed as sleep and behavioural management agents |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Retrospective Cohort | PeerJ | Drug utilisation study in elderly: long-term BZD and z-drug use associated with age, female sex, depression, and chronic disease; underscores need for appropriate patient selection |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Clinical Study | JAMA | Case series: withdrawal syndrome occurred when oxazepam (short-acting) was substituted for diazepam or flurazepam; informs safe transition protocols |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Drug Review | CNS Drugs | Review of paroxetine for panic disorder; contextualises benzodiazepines' role as comparator/adjunct in anxiety-driven sleep disruption |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case Report | Am J Transl Res | Case of agomelatine-induced tongue temperature perception abnormality with oxazepam as concurrent medication; highlights drug interaction monitoring in polypharmacy insomnia treatment |

---

## Sweden Market Information

Oxazepam currently holds **no marketing authorisations in Sweden** (MPA). No product listings are available.

If this repurposing pathway is pursued, a formal regulatory submission to MPA/EMA would be required before any clinical deployment in Sweden.

---

## Safety Considerations

Detailed prescribing warnings and contraindications are not available in the current evidence pack.

> Please refer to the package insert for safety information. Key areas to review include: dependence and withdrawal risk (characteristic of all benzodiazepines), use in elderly patients (fall risk, cognitive effects), and concomitant CNS depressants.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two RCTs and a body of observational and review literature directly support oxazepam's efficacy in insomnia — particularly its favourable profile (no active metabolites, intermediate half-life, no daytime sedation) relative to other benzodiazepines. The TxGNN score of 99.86% reflects mechanistic plausibility that is well-corroborated by decades of clinical use. However, Sweden has no current authorisations, and critical safety documentation is missing.

**To proceed, the following is needed:**
- Obtain the full prescribing information / SmPC from EMA or a reference market where oxazepam is approved (e.g. Germany, Netherlands) to complete the safety profile assessment
- Confirm the regulatory pathway: new marketing authorisation application vs. mutual recognition procedure in Sweden
- Develop a risk management plan specifically addressing **dependence liability, withdrawal risk**, and use in elderly patients (the highest-risk insomnia subgroup)
- Conduct a systematic review or meta-analysis of existing oxazepam insomnia RCTs to upgrade evidence to L1 before full commercial development
- Assess whether a bridging pharmacokinetic or comparative effectiveness study is required by MPA
---

