---
layout: default
title: Linezolid
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 0
---

# Linezolid
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **0** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

# Linezolid: Drug Repurposing Evaluation — Awaiting Prediction Data

## One-Sentence Summary

Linezolid (DB00601) is an oxazolidinone-class antibiotic used for serious gram-positive bacterial infections, including MRSA and VRE.
This Evidence Pack returned **no TxGNN predicted indications**, and two critical data gaps — mechanism of action and safety warnings — are unresolved.
**A complete repurposing evaluation cannot be conducted at this time; the decision is Hold.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No prediction returned |
| TxGNN Prediction Score | — |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Taiwan Market Information

Linezolid currently holds **zero authorizations** in Taiwan and is **not marketed**. No license records were found in the TFDA database.

> A successful TFDA package insert query was logged (2026-03-29), but the retrieved content has not yet been parsed into structured fields. Pending manual review of that document may unlock safety and indication data.

---

## Safety Considerations

Please refer to the package insert for safety information. The following data remain unresolved:

- **Key Warnings**: Not yet extracted from TFDA package insert
- **Contraindications**: Not yet extracted from TFDA package insert
- **Drug Interactions**: No records found in the DDI database

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no predicted indications for Linezolid, making it impossible to evaluate any repurposing hypothesis. Two upstream data gaps — a Blocking-severity gap in TFDA safety information and a High-severity gap in mechanism of action — further prevent risk assessment even if a prediction were available.

**To proceed, the following is needed:**

- **[Blocking]** Parse the TFDA package insert PDF already retrieved (2026-03-29) to extract key warnings and contraindications
- **[High]** Query DrugBank API for Linezolid (DB00601) mechanism of action (MOA)
- **[Required]** Re-run TxGNN prediction pipeline for DB00601 to generate indication candidates
- **[Supplementary]** Expand DDI database search or consult an alternative interaction source (e.g., Lexicomp, Micromedex)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

