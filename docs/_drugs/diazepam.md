---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# DIAZEPAM: Drug Repurposing Evaluation Report

## One-Sentence Summary

Diazepam is a well-known benzodiazepine widely used globally for anxiety disorders, seizure management, muscle spasms, and alcohol withdrawal.
The TxGNN model has **not generated any predicted new indications** for this drug at this time,
and **no clinical trial or literature evidence** has been collected in this evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (globally known for anxiety, seizures, muscle spasms, sedation) |
| Predicted New Indication | None predicted |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No model prediction or supporting studies available |
| Sweden Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on widely known pharmacological information, Diazepam (DrugBank ID: DB00829) is a long-acting benzodiazepine that enhances the effect of the neurotransmitter gamma-aminobutyric acid (GABA) at the GABA-A receptor, resulting in sedative, anxiolytic, anticonvulsant, and muscle relaxant properties. It is one of the most commonly prescribed benzodiazepines worldwide.

However, the TxGNN model has not generated any predicted new indications for Diazepam in this evaluation cycle. Without a predicted indication, no mechanism-based rationale for repurposing can be assessed at this stage.

The absence of a prediction does not necessarily mean Diazepam lacks repurposing potential — it may reflect data limitations in the knowledge graph input, or that Diazepam's known indication coverage is already extensive. A future re-run with an updated knowledge graph may yield different results.

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack.

## Literature Evidence

Currently no related literature available in this evidence pack.

## Sweden Market Information

Diazepam currently has **no marketing authorizations** recorded in Sweden within this dataset. No license details are available.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack. Given that Diazepam is a controlled benzodiazepine with well-documented risks (respiratory depression, dependence, withdrawal syndrome, interactions with CNS depressants and opioids), clinicians should consult the full prescribing information before any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No new indication has been predicted by the TxGNN model for Diazepam, and no supporting clinical or literature evidence has been collected. Without a target indication, there is no actionable repurposing candidate to evaluate at this time.

**To proceed, the following is needed:**
- Re-run TxGNN prediction with an updated knowledge graph to determine if new indications emerge for Diazepam
- Obtain detailed mechanism of action (MOA) data from DrugBank API to resolve data gap DG002
- Retrieve package insert warnings and contraindications from the regulatory authority to resolve data gap DG001
- Clarify Sweden market status — Diazepam is widely available globally; the absence of Swedish authorizations may reflect a data collection issue rather than true market absence
- If a predicted indication is generated in a future cycle, collect relevant clinical trial and literature evidence to support evaluation
---

