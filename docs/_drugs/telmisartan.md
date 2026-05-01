---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

Now I have the context I need. Let me generate the evaluation report based on the Evidence Pack.

---

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 receptor blocker (ARB) with an additional partial PPARγ agonist action, widely used internationally for hypertension and cardiovascular risk reduction — though no Taiwan approval record exists in this dataset.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina caused by coronary artery spasm),
with **no clinical trials** and **no publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not on record in Taiwan (ARB class; known international use: hypertension) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, telmisartan belongs to the ARB (angiotensin II type 1 receptor blocker) class and uniquely acts as a partial PPARγ agonist — earning it the informal label "metabosartan." Its blood pressure-lowering efficacy and cardiovascular event reduction have been established in large Phase 3/4 trials.

Prinzmetal angina (variant angina) is caused by transient coronary artery spasm. Theoretically, AT1 receptor blockade could relieve angiotensin II–induced coronary vasospasm, while PPARγ activation provides antioxidative and endothelial-protective effects on the coronary vasculature. These mechanistic links are pharmacologically coherent.

However, no preclinical study has used a coronary spasm model with telmisartan, and no clinical research has ever enrolled Prinzmetal angina patients. The high TxGNN score (99.98%, rank 73) is most likely driven by graph topology — telmisartan's cardiovascular nodes in the knowledge graph sit close to coronary artery disease nodes — rather than true therapeutic relevance. This prediction should be treated as a hypothesis-generation signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no preclinical or clinical evidence of any kind supporting telmisartan specifically for Prinzmetal angina. At evidence level L5, this is purely a model-generated hypothesis whose high score is most likely an artifact of knowledge graph proximity rather than biological plausibility.

**To proceed, the following is needed:**
- Preclinical investigation using a validated coronary artery spasm model (e.g., ergonovine or methacholine challenge in animal models)
- Confirmation of mechanistic link between AT1R blockade / PPARγ activation and vasospastic angina pathophysiology
- Retrieval of MOA data from DrugBank (DG002 remediation)
- Taiwan package insert and safety data (DG001 remediation) to enable S1 safety pre-screening
- Literature search broadened to ARB class effects on coronary vasomotor tone

---

> **Note on the full prediction landscape:** While Prinzmetal angina is ranked #1 by TxGNN score, the strongest empirical evidence in this Evidence Pack belongs to **intracerebral hemorrhage** (rank #9, Evidence Level L1), supported by the completed TRIDENT Phase 3 trial (NCT02699645, n=1,671) and multiple animal model studies. If prioritizing evidence-based repurposing candidates, **intracerebral hemorrhage** and **cerebral artery occlusion** (rank #4, L3) represent substantially higher-confidence targets for further evaluation.
---

