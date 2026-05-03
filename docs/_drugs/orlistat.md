---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor originally used for weight management in obesity.
The TxGNN model predicts it may be effective for **Hypervitaminosis**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this direction, making it a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obesity (weight management) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Orlistat is a potent and selective inhibitor of pancreatic and gastric lipases. By covalently binding to the active serine residue of these enzymes, it prevents the hydrolysis of dietary triglycerides, reducing fat absorption in the gastrointestinal tract by approximately 30%. This mechanism is well-established in obesity treatment, where reducing caloric intake from fat is the primary goal.

The theoretical mechanistic link to hypervitaminosis lies in a known side effect of orlistat: reduced intestinal absorption of fat-soluble vitamins A, D, E, and K. Because these vitamins are co-absorbed with dietary fat, blocking fat absorption simultaneously limits fat-soluble vitamin uptake. In theory, this mechanism could partially attenuate newly ingested fat-soluble vitamins in conditions of excess accumulation.

However, this prediction carries significant limitations. First, orlistat can only block new intake — it cannot mobilise or eliminate vitamins already accumulated in body tissues, making it ineffective for clearing established toxicity. Second, it has no effect whatsoever on water-soluble vitamin excess (e.g., Vitamin B6 or B12 toxicity). Third, and most critically, this vitamin-reducing effect is catalogued as an **adverse reaction** of orlistat, not a therapeutic mechanism. The high TxGNN score (0.994) likely reflects the model capturing the fat-absorption pathway overlap, but this does not translate to clinical utility for treating hypervitaminosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Orlistat currently has **no marketing authorizations** in Taiwan. No approved products are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5) with no clinical trials, no supporting literature, and a mechanistic rationale that is physiologically questionable — the proposed mechanism is in fact a listed adverse effect of the drug rather than a therapeutic action, and is structurally incapable of addressing most forms of hypervitaminosis.

**To proceed, the following is needed:**
- Clarify the specific subtype of hypervitaminosis being targeted (fat-soluble vs. water-soluble), as orlistat is mechanistically irrelevant to the latter
- Conduct a formal preclinical study to test whether orlistat meaningfully reduces fat-soluble vitamin levels in a controlled hypervitaminosis model (e.g., Vitamin A or D toxicity model)
- Obtain mechanism of action (MOA) documentation from DrugBank to refine pathway analysis
- Retrieve TFDA package insert warnings and contraindications to complete baseline safety assessment before any further development stage evaluation
- Consider whether the TxGNN prediction reflects a genuine therapeutic signal or a spurious correlation via the fat-absorption pathway — an expert pharmacological review is recommended before investing further resources
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

