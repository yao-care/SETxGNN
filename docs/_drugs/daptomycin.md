---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: Drug Repurposing Evaluation Report

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic known internationally for treating serious Gram-positive infections, including complicated skin and skin structure infections (cSSSI) and *Staphylococcus aureus* bacteraemia. The TxGNN model has **not generated any predicted new indications** for this drug at this time, and the evidence pack contains significant data gaps that preclude a meaningful repurposing assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Daptomycin |
| DrugBank ID | [DB00080](https://go.drugbank.com/drugs/DB00080) |
| Original Indication | Not recorded in this evidence pack (known internationally: cSSSI, *S. aureus* bacteraemia) |
| Predicted New Indication | — None predicted — |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | **Hold** |

---

## Why Is There No Prediction?

Daptomycin (marketed internationally as **Cubicin**) is a cyclic lipopeptide antibiotic that works by inserting into bacterial cell membranes in a calcium-dependent manner, causing rapid depolarisation and loss of membrane potential. This leads to inhibition of protein, DNA, and RNA synthesis and ultimately bacterial cell death. It is active exclusively against Gram-positive organisms.

The TxGNN model did not generate any repurposing candidates for Daptomycin. This may be due to one or more of the following reasons:

1. **Narrow mechanistic profile**: Daptomycin's mechanism of action targets bacterial cell membranes specifically, which limits theoretical applicability to non-infectious disease indications.
2. **Knowledge graph coverage**: The drug may have insufficient representation in the underlying knowledge graph, limiting the model's ability to identify novel disease–drug associations.
3. **Data gaps**: The evidence pack notes that detailed mechanism of action data (MOA) was not retrieved from DrugBank for this candidate, which may have impacted the prediction pipeline.

---

## Clinical Trial Evidence

No predicted indications were generated, therefore no targeted clinical trial search was performed for repurposing candidates.

---

## Literature Evidence

No predicted indications were generated, therefore no targeted literature search was performed for repurposing candidates.

---

## Taiwan Market Information

Daptomycin is **not marketed in Taiwan**. No TFDA (Taiwan Food and Drug Administration) authorizations were found.

> Note: Daptomycin is marketed in many other countries (US, EU, Japan, etc.) under the brand name **Cubicin** / **Cubicin RF** (Merck). The absence from the Taiwan market means no local label, package insert, or post-market safety data is available from TFDA.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug–drug interactions) was available from Taiwan regulatory sources, as the drug is not marketed locally.

> Please refer to the international package insert (e.g., US FDA-approved Cubicin label) for comprehensive safety information. Key internationally recognised safety concerns for Daptomycin include:
> - **Eosinophilic pneumonia**: Daptomycin is inactivated by pulmonary surfactant and must not be used for pneumonia; eosinophilic pneumonia has been reported.
> - **Myopathy / Rhabdomyolysis**: CPK levels should be monitored; discontinue if CPK >1000 U/L with symptoms or >2000 U/L without symptoms.
> - **Peripheral neuropathy**: Monitor for signs and symptoms.
> - **HMG-CoA reductase inhibitor interaction**: Consider temporarily suspending statins during Daptomycin therapy due to additive myopathy risk.

---

## Data Gaps Identified

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings / Contraindications | **Blocking** | Cannot enter S1 safety preliminary assessment | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanism–indication relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not produce any predicted new indications for Daptomycin. Combined with its absence from the Taiwan market (0 authorizations) and multiple blocking data gaps, there is no actionable repurposing hypothesis to evaluate at this time.

**To proceed, the following is needed:**
- Re-run the TxGNN prediction pipeline after resolving knowledge graph coverage for Daptomycin (DB00080)
- Retrieve and populate the mechanism of action data from DrugBank API (DG002)
- If Daptomycin enters the Taiwan market in the future, obtain TFDA package insert for local safety assessment (DG001)
- Consider whether the drug's narrow antibacterial mechanism realistically supports non-infectious disease repurposing; if not, deprioritise this candidate
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

