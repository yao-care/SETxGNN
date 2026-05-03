---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# ALPRAZOLAM: Drug Repurposing Evaluation Report

## One-Sentence Summary

Alprazolam is a well-known benzodiazepine widely used for anxiety and panic disorders globally. The TxGNN model has **not generated any predicted new indications** for this drug at this time. Combined with the fact that this drug currently has **no marketing authorisation in Taiwan** and significant data gaps remain, there is insufficient basis for a repurposing recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Alprazolam |
| DrugBank ID | DB00404 |
| Original Indication | Not listed in evidence pack (known use: anxiety and panic disorders) |
| Predicted New Indication | — None predicted by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No prediction, no supporting studies) |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is There No Prediction?

Alprazolam is a triazolobenzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor. It enhances the inhibitory effect of gamma-aminobutyric acid (GABA) in the central nervous system, producing anxiolytic, sedative, and muscle-relaxant effects. It is one of the most widely prescribed benzodiazepines worldwide for generalised anxiety disorder and panic disorder.

Despite its well-characterised pharmacology, the TxGNN model did not generate any repurposing predictions for Alprazolam. This may be due to several factors: (1) the drug's mechanism is already broadly applied across its therapeutic class, (2) the knowledge graph may lack sufficient novel connectivity to suggest unexplored indications, or (3) known safety concerns with benzodiazepines (dependence, withdrawal, cognitive impairment) may limit the model's confidence in new therapeutic applications.

Additionally, the evidence pack indicates that detailed mechanism of action data was not retrieved from DrugBank (flagged as a high-severity data gap, DG002), which may have further limited the model's ability to infer cross-indication links.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indications exist; therefore, no targeted clinical trial search was performed for repurposing candidates.

---

## Literature Evidence

Currently no TxGNN-predicted indications exist; therefore, no targeted literature search was performed for repurposing candidates.

---

## Taiwan Market Information

Alprazolam currently holds **no marketing authorisation (許可證)** in Taiwan. The TFDA query returned zero results.

> **Note:** Although Alprazolam is widely available in many countries (e.g., as Xanax®), it does not appear in the TFDA licence database based on the query performed on 2026-03-29. This may warrant verification, as Alprazolam-containing products may be registered under different trade names or formulations.

---

## Safety Considerations

Safety data (warnings, contraindications, and drug-drug interactions) were not available in the evidence pack. However, based on the well-known pharmacological profile of benzodiazepines, clinicians should be aware of:

- **Dependence and withdrawal risk**: Alprazolam has significant potential for physical dependence, particularly with prolonged use. Abrupt discontinuation can cause seizures and life-threatening withdrawal.
- **CNS depression**: Risk of respiratory depression, especially when combined with opioids, alcohol, or other CNS depressants.
- **Cognitive and psychomotor impairment**: May affect driving ability and increase fall risk in elderly patients.
- **Controlled substance status**: Alprazolam is classified as a Schedule IV controlled substance internationally.

> ⚠️ Please refer to the package insert for complete safety information. The evidence pack flagged missing TFDA package insert warnings (DG001, Blocking severity) as a critical data gap.

---

## Data Gaps Summary

The following critical data gaps were identified and should be resolved before any further evaluation:

| Gap ID | Item | Severity | Impact | Recommended Remediation |
|--------|------|----------|--------|------------------------|
| DG001 | TFDA Package Insert Warnings/Contraindications | **Blocking** | Cannot proceed with S1 safety screening | Download and parse package insert PDF from TFDA website |
| DG002 | Mechanism of Action (MOA) | High | Affects mechanism-relevance analysis | Query DrugBank API |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has not identified any repurposing candidates for Alprazolam. Additionally, the drug has no current marketing authorisation in Taiwan, and multiple blocking-level data gaps remain unresolved. There is no actionable basis for a drug repurposing investigation at this time.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): Obtain TFDA package insert warnings and contraindications — required before any safety evaluation can begin
- Resolve **DG002** (High): Retrieve detailed MOA data from DrugBank to enable mechanism-based inference
- Verify Taiwan market status: Confirm whether Alprazolam is truly unregistered in Taiwan or if it exists under alternative trade names
- Re-run TxGNN prediction after data gaps are filled to determine if new indication predictions emerge
- If no predictions emerge after data enrichment, this candidate should be **deprioritised** in the repurposing pipeline
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

