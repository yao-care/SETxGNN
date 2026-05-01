---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 4
---

# Acitretin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Acitretin: Drug Repurposing Evaluation Report

## One-Sentence Summary

Acitretin is a second-generation systemic retinoid, known internationally for the treatment of severe psoriasis and other keratinization disorders. No TxGNN predicted indications are currently available for this drug, and **no clinical trial or literature evidence** has been compiled in this evidence pack. The evaluation is currently on hold pending additional data.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Acitretin |
| DrugBank ID | [DB00459](https://go.drugbank.com/drugs/DB00459) |
| Original Indication | Not recorded in this evidence pack (known use: severe psoriasis) |
| Predicted New Indication | None available — TxGNN predictions not yet generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or studies available) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, no TxGNN prediction has been generated for Acitretin. Therefore, a mechanistic plausibility assessment cannot be performed at this time.

For context, Acitretin is the active metabolite of etretinate and belongs to the retinoid class. Retinoids modulate gene expression by binding to nuclear retinoic acid receptors (RARs and RXRs), influencing cell proliferation, differentiation, and apoptosis. It is primarily used for the treatment of severe psoriasis (including erythrodermic and pustular forms) and other disorders of keratinization. The detailed mechanism of action (MOA) data was not available in the current evidence pack (Data Gap DG002).

Once TxGNN predictions are generated, the known retinoid receptor-mediated mechanism and its broad effects on cell differentiation and immune modulation could provide a basis for evaluating repurposing candidates across dermatological, oncological, or immunological indications.

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack.

> No predicted indications have been generated, so clinical trial mapping has not been performed.

## Literature Evidence

Currently no related literature available in this evidence pack.

> Literature evidence collection is pending the generation of TxGNN predicted indications.

## Taiwan Market Information

Acitretin is currently **not marketed in Taiwan**. No TFDA licenses were found.

| Item | Content |
|------|------|
| Market Status | Not marketed (未上市) |
| Total Licenses | 0 |
| Available Dosage Forms | None |

> Note: Acitretin is marketed in many other countries (e.g., under the brand names Soriatane® and Neotigason®) for severe psoriasis.

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) was not available in the current evidence pack. The following is based on the well-known safety profile of Acitretin from international labelling:

> **Please refer to the package insert for complete safety information.**
>
> Key internationally recognised safety concerns for Acitretin include:
> - **Teratogenicity**: Acitretin is highly teratogenic. Women of childbearing potential must use effective contraception and avoid pregnancy during treatment and for **at least 3 years** after discontinuation.
> - **Hepatotoxicity**: Liver function tests should be monitored regularly.
> - **Hyperlipidaemia**: May elevate triglycerides and cholesterol levels.
> - **Mucocutaneous side effects**: Dry skin, cheilitis, and hair loss are common.
>
> *These are reference notes from international labelling and do not replace the local package insert.*

## Data Gaps Identified

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot enter S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indications have been generated for Acitretin, and critical data gaps remain unresolved (MOA data, TFDA safety labelling). Additionally, Acitretin is not currently marketed in Taiwan, which presents additional regulatory barriers to any repurposing initiative. The evaluation cannot proceed until predictions and baseline safety data are available.

**To proceed, the following is needed:**
- Generate TxGNN predictions for Acitretin (DB00459) to identify candidate new indications
- Resolve **DG001** (Blocking): Obtain and parse TFDA package insert for warnings and contraindications
- Resolve **DG002** (High): Retrieve detailed MOA data from DrugBank API
- Once predictions are available, perform clinical trial and literature evidence searches
- Assess Taiwan market entry feasibility given the current "not marketed" status
---

