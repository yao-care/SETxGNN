---
layout: default
title: Bosutinib
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 0
---

# Bosutinib
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

Now I have all the context I need. The Evidence Pack's `predicted_indications` is empty, but the project's FHIR data shows a TxGNN prediction for "blast phase chronic myelogenous leukemia, BCR-ABL1 positive" with a score of 0.5. Let me generate the report.

---

# BOSUTINIB: From Chronic Myeloid Leukaemia to Blast Phase CML, BCR-ABL1 Positive

## One-Sentence Summary

Bosutinib is a BCR-ABL tyrosine kinase inhibitor originally developed for the treatment of Philadelphia chromosome-positive chronic myeloid leukaemia (Ph+ CML) in the chronic phase. The TxGNN model predicts it may also be effective for **Blast Phase Chronic Myelogenous Leukaemia, BCR-ABL1 Positive**, though with a moderate prediction score of **50%**. Currently there are **no clinical trials** or **publications** included in the evidence pack to directly support this specific repurposing direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ph+ Chronic Myeloid Leukaemia (chronic phase) |
| Predicted New Indication | Blast Phase Chronic Myelogenous Leukaemia, BCR-ABL1 Positive |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 (Model prediction only, no clinical studies in pack) |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bosutinib is a dual Src/ABL tyrosine kinase inhibitor that blocks the constitutively active BCR-ABL1 fusion oncoprotein — the hallmark driver of chronic myeloid leukaemia. By inhibiting BCR-ABL1 kinase activity, bosutinib suppresses the proliferative signalling cascade that sustains the leukaemic clone. Globally, it is approved (as Bosulif®, Pfizer) for adult patients with newly diagnosed or resistant/intolerant Ph+ CML in the chronic phase.

Blast phase CML represents the terminal transformation of the disease, characterised by rapid expansion of immature blast cells and acquisition of additional genetic aberrations. Because the BCR-ABL1 fusion protein remains the central oncogenic driver even in blast crisis, a BCR-ABL1-directed inhibitor like bosutinib retains mechanistic plausibility. Indeed, other second- and third-generation TKIs (dasatinib, ponatinib) have demonstrated activity in blast phase CML, supporting the biological rationale.

However, blast phase CML is substantially more resistant to TKI monotherapy than chronic phase disease, due to clonal evolution, additional mutations (e.g. T315I for some TKIs), and activation of BCR-ABL1-independent survival pathways. The moderate TxGNN score of 50% may reflect this complexity. Detailed mechanism of action data was not available in the evidence pack; the above is based on the known pharmacological profile of bosutinib as a Src/ABL kinase inhibitor.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| Currently no related clinical trials registered in the evidence pack | — | — | — | — |

> **Note:** While the evidence pack contains no clinical trial data, bosutinib has been studied in blast phase CML in registration trials (e.g. the Phase 1/2 Study 200, NCT00261846) and has received FDA approval for Ph+ CML including accelerated phase. Additional targeted searches of ClinicalTrials.gov are recommended.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| Currently no related literature available in the evidence pack | — | — | — | — |

> **Note:** Published data on bosutinib in advanced-phase CML exist in the medical literature (e.g. Cortes et al., Blood 2011; Gambacorti-Passerini et al., Am J Hematol 2015). A systematic literature search is recommended to supplement this evidence pack.

## Sweden Market Information

Bosutinib is currently **not marketed in Sweden** and holds **0 authorizations** from the Swedish MPA in this evidence pack.

> **Note:** Bosutinib is authorised in the EU under the brand name Bosulif® (EMA centralised procedure). The absence of Swedish-specific license records may reflect data collection scope rather than true unavailability. Verification with the Swedish MPA / EMA EPAR database is recommended.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL / Src tyrosine kinase inhibitor) |
| Myelosuppression Risk | Moderate to High — thrombocytopenia, neutropenia, and anaemia are common (reported in >20% of patients in clinical trials) |
| Emetogenicity Classification | Low to Moderate (nausea and diarrhoea are among the most frequent adverse events) |
| Monitoring Items | CBC with differential (weekly during first month, then monthly); liver function tests (ALT, AST, bilirubin — hepatotoxicity risk); renal function (creatinine, eGFR); electrolytes; lipase (pancreatitis risk) |
| Handling Protection | Standard oral targeted-therapy handling; no special cytotoxic spill precautions required beyond institutional policies for oral anticancer agents |

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Key safety signals known from the global label (Bosulif® SmPC/USPI) include:
> - **Hepatotoxicity**: ALT/AST elevations reported; liver function monitoring required
> - **Gastrointestinal toxicity**: Diarrhoea (very common, may be severe), nausea, vomiting
> - **Myelosuppression**: Thrombocytopenia, neutropenia, anaemia
> - **Fluid retention**: Including pleural effusion, pericardial effusion, and peripheral oedema
> - **Renal toxicity**: Decline in eGFR observed; renal function monitoring recommended
>
> *The above is based on the globally known safety profile. The evidence pack did not contain TFDA/MPA-specific labelling data.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is moderate (50%), and the evidence pack currently contains no clinical trials, literature, or regulatory authorization data to support advancing this candidate. While the mechanistic rationale (BCR-ABL1 inhibition in blast phase CML) is sound and published literature outside this pack does exist, the evidence pack itself is at Level L5 with multiple critical data gaps.

**To proceed, the following is needed:**
- Supplement the TxGNN prediction with a **systematic literature search** for bosutinib in blast phase / accelerated phase CML (PubMed, Cochrane)
- Query **ClinicalTrials.gov** for completed and ongoing trials of bosutinib in advanced-phase CML
- Obtain **detailed MOA data** from DrugBank API to close data gap DG002
- Retrieve **Swedish MPA / EMA authorization records** for Bosulif® to clarify regulatory status in Sweden
- Obtain **package insert warnings and contraindications** (FASS.se or EMA SmPC) to close data gap DG001
- Re-evaluate the candidate once the evidence pack is supplemented; reclassification to **Proceed with Guardrails** is plausible if published Phase 2/3 data in blast phase CML are confirmed
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

