---
layout: default
title: Cefadroxil
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# Cefadroxil
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

# CEFADROXIL: Drug Repurposing Evaluation Report

## One-Sentence Summary

Cefadroxil is a first-generation cephalosporin antibiotic commonly used for bacterial infections of the skin, urinary tract, and upper respiratory tract. The TxGNN model has **not generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps including mechanism of action and regulatory safety information.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (known: bacterial infections including UTI, pharyngitis, skin infections) |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for cefadroxil, so there is no new indication to evaluate for mechanistic plausibility.

Cefadroxil (DrugBank ID: DB01140) is a first-generation cephalosporin, a class of β-lactam antibiotics that work by inhibiting bacterial cell wall synthesis through binding to penicillin-binding proteins (PBPs). Detailed mechanism of action data was not available in the evidence pack (flagged as Data Gap DG002), though the drug's pharmacology is well-characterized in the literature.

Without a predicted indication from the TxGNN model, no mechanism-to-disease bridging analysis can be performed at this time. This candidate should be revisited once the prediction pipeline has been run and validated predictions are available.

## Clinical Trial Evidence

Currently no predicted indication available — clinical trial search not applicable.

## Literature Evidence

Currently no predicted indication available — literature search not applicable.

## Taiwan Market Information

Cefadroxil has **no active marketing authorizations** in Taiwan (TFDA). No licenses were found in the regulatory query conducted on 2026-03-29.

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: Key warnings, contraindications, and drug interaction data were all unavailable in this evidence pack (Data Gaps DG001). The TFDA package insert query returned 1 result but parsed safety fields remain empty. It is recommended to retrieve and parse the full package insert PDF from the TFDA website to complete the safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications exist for cefadroxil at this time, and the drug is not currently marketed in Taiwan. Without a target indication, there is no actionable repurposing hypothesis to evaluate.

**To proceed, the following is needed:**
- Run the TxGNN prediction pipeline for cefadroxil (DB01140) and generate candidate indications
- Fill Data Gap DG002: Retrieve detailed mechanism of action from DrugBank API
- Fill Data Gap DG001 (Blocking): Download and parse the TFDA package insert PDF for safety warnings and contraindications
- Reassess market access feasibility given the drug's current unlicensed status in Taiwan
- Once predictions are available, collect clinical trial and literature evidence for the top-ranked indication(s)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

