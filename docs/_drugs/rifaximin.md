---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using `txgnn-pipeline` skill to orient to the report context. The skill confirms this is a TxGNN multi-country repurposing pipeline (TW prefix). Now generating the evaluation report based on the Evidence Pack.

---

# RIFAXIMIN: From Gastrointestinal Bacterial Infections to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a minimally-absorbed oral antibiotic used for gastrointestinal bacterial conditions such as traveler's diarrhea and hepatic encephalopathy.
The TxGNN model predicts it may be effective for **Oral Candidiasis** with a score of **99.75%**,
but **no clinical trials** have been registered and the only available observational study actually suggests rifaximin may *increase* the risk of *Candida* infections rather than treat them.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Taiwan regulatory data (TFDA has no approved license) |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the queried data sources. Based on established pharmacological knowledge, rifaximin is a non-absorbable, gut-restricted antibiotic derived from the rifamycin class. It works by inhibiting bacterial RNA polymerase, suppressing bacterial transcription locally within the gastrointestinal tract. Its validated clinical uses include reducing recurrence of hepatic encephalopathy, treating traveler's diarrhea caused by *Escherichia coli*, and managing IBS with diarrhea (IBS-D) — all bacterial targets.

The predicted indication — oral candidiasis — is caused by *Candida* species, which are fungi. Rifaximin has no antifungal mechanism. In fact, the antimicrobial suppression of normal gut bacteria (which competitively inhibit fungal colonization) is a well-known driver of antibiotic-associated candidiasis: eliminating bacterial competitors can promote *Candida* overgrowth. This is the opposite direction of treatment.

The sole piece of literature retrieved (PMID 34180023, *Annals of Hematology*, 2021) directly confirms this risk: rifaximin prophylaxis in allogeneic hematopoietic stem cell transplant recipients was associated with an **increased** incidence of micafungin-resistant *Candida* spp. infections. The TxGNN high score almost certainly reflects graph topology proximity among oral disease nodes rather than any genuine pharmacological mechanism linking rifaximin to treating candidiasis. All six predicted indications share the same L5 rating and Hold decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Observational / Case series | *Annals of Hematology* | Rifaximin use in allogeneic HSCT recipients **favoured** micafungin-resistant *Candida* spp. infections — the drug appears to promote rather than treat candidiasis by disrupting competitive bacterial flora in the gut. |

---

## Taiwan Market Information

Rifaximin is currently **not marketed in Taiwan**. The TFDA query returned zero approved licenses, and no approved indication text is on record. The drug is not available through any authorised channel in this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA package insert warnings and contraindications were not retrievable from structured data; a manual download of the TFDA PDF is required to complete the safety profile.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six TxGNN-predicted indications for rifaximin are rated L5 (model prediction only) with a uniform Hold recommendation. The top-ranked prediction — oral candidiasis — is mechanistically implausible: rifaximin is an antibacterial with no antifungal activity, and the only literature found suggests it may actively *worsen* Candida infection risk. The prediction most likely reflects graph topology artifacts, not genuine repurposing opportunity.

**To proceed, the following is needed:**

- **MOA data gap**: Retrieve full mechanism of action from DrugBank API to enable rigorous mechanistic screening of all predictions
- **Safety data gap**: Download and parse the TFDA package insert PDF to obtain warnings, contraindications, and drug interaction data (currently blocking S1 safety assessment)
- **Redirect model inquiry**: Re-evaluate TxGNN predictions against biologically plausible indications where rifaximin's antibacterial/microbiome-modulating mechanism is relevant — e.g., spontaneous bacterial peritonitis (SBP) prophylaxis, minimal hepatic encephalopathy, or small intestinal bacterial overgrowth (SIBO)
- **Do not advance oral candidiasis**: The existing evidence is directionally contrary to a therapeutic benefit; this indication should be deprioritized unless a novel mechanistic hypothesis (e.g., gut-oral microbiome axis) can be articulated with preclinical support
---

