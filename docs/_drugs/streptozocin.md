---
layout: default
title: Streptozocin
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

Using `txgnn-pipeline` to guide the drug repurposing report generation. Now producing the evaluation report based on the Evidence Pack.

---

# Streptozocin: From Pancreatic Islet Cell Carcinoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Streptozocin is a DNA alkylating agent in the nitrosourea class, internationally used for metastatic pancreatic islet cell carcinoma (Zanosar®), though it is not registered in Taiwan.
The TxGNN model assigns it the top predicted indication of **Relapsing-Remitting Multiple Sclerosis (RRMS)** with a score of **99.97%**,
yet the evidence base consists of **0 clinical trials** and **1 animal-model publication** — and critically, that publication uses streptozocin to *induce* diabetes in rats rather than to treat RRMS, making this a likely **knowledge-graph false positive** that should not advance to clinical evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pancreatic islet cell carcinoma (metastatic) — not registered in Taiwan |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**Short answer: it is not.** This is almost certainly a knowledge-graph false positive, and the mechanistic rationale does not hold up under scrutiny.

Streptozocin (STZ) is a naturally occurring nitrosourea antibiotic that acts as a DNA alkylating agent. It selectively destroys pancreatic beta cells by exploiting the GLUT2 glucose transporter to enter cells, after which it causes DNA strand breaks, inhibits PARP, and depletes NAD⁺. This selective beta-cell toxicity is the basis for its clinical use in insulin-secreting neuroendocrine tumors — and also makes it the standard laboratory tool for *inducing* type 1 diabetes in rodent models. This dual identity as both a cancer drug and a disease-induction agent is the likely root cause of the erroneous prediction.

Relapsing-remitting multiple sclerosis is an autoimmune demyelinating disease driven by T-cell and B-cell dysregulation of the central nervous system. There is no known connection between DNA alkylation and RRMS pathophysiology. The TxGNN knowledge graph appears to have generated a spurious association through the following path: **STZ → (induces) diabetic rat model → FTY720/fingolimod treatment → RRMS**. The only retrieved publication (PMID 28162947) is a study examining whether fingolimod improves erectile dysfunction in STZ-induced diabetic rats. In this paper, streptozocin is the disease-causing tool; fingolimod (an approved RRMS drug) is the actual therapeutic intervention. The model appears to have conflated the roles of these two agents.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, streptozocin belongs to the nitrosourea class of conventional cytotoxic agents. Its established antitumor activity in neuroendocrine tumors has no mechanistic bridge to RRMS, and no clinical or preclinical data supports this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for streptozocin in relapsing-remitting multiple sclerosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28162947](https://pubmed.ncbi.nlm.nih.gov/28162947/) | 2017 | Animal Study | J Sex Med | **⚠ False positive indicator.** STZ is used to *induce* type 1 diabetes in rats (disease model); fingolimod (FTY720) — an approved RRMS drug — is the therapeutic agent studied. Streptozocin plays no therapeutic role in this publication. |

---

## Taiwan Market Information

Streptozocin is not registered in Taiwan. No authorization records are available from TFDA databases (queried 2026-03-29, result count = 0).

---

## Cytotoxicity

Streptozocin is an antineoplastic nitrosourea antibiotic. The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrosourea class (DNA alkylating agent) |
| Myelosuppression Risk | **Low** — streptozocin is notably non-myelosuppressive compared to chloroethylnitrosoureas; dose-limiting toxicity is nephrotoxicity, not bone marrow suppression |
| Emetogenicity Classification | **High** — severe nausea and vomiting are common and expected; aggressive anti-emetic prophylaxis is required |
| Monitoring Items | Renal function (serum creatinine, BUN, urinalysis — recommended weekly during treatment); liver function tests; fasting blood glucose; CBC |
| Handling Protection | Required — streptozocin is on the NIOSH hazardous drug list; cytotoxic handling protocols (closed-system transfer, PPE, dedicated disposal) must be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert data was retrieved (query_log ID 4, status: success) but detailed warning and contraindication content was not populated in this evidence pack. Before any clinical consideration, the package insert must be reviewed for nephrotoxicity protocols, hepatotoxicity warnings, and reproductive hazard classifications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (RRMS, rank 1) is a knowledge-graph false positive — the only supporting literature uses streptozocin as a disease-induction agent in a rodent model, not as a treatment for multiple sclerosis. There is no plausible mechanistic basis and zero clinical evidence for this indication. Advancing this prediction would misallocate research resources.

**Context on other predictions in this evidence pack:**

| Rank | Disease | Evidence Level | Historical Verdict |
|------|---------|---------------|-------------------|
| 2 | Small cell lung carcinoma | L2 | Directly refuted: multiple Phase II trials (1978–1984) confirmed STZ is **inactive** as a single agent in SCLC |
| 7 | Lymphosarcoma | L3 | Limited early Phase I/II activity observed (1974); obsolete — modern NHL regimens are far superior |
| 1–10 (remainder) | Various rare tumors, HBOC | L5 | Pure model predictions; no clinical or preclinical support |

**To improve model quality and avoid similar false positives, the following is recommended:**

- **Knowledge graph audit:** Verify that streptozocin's role in publications (treatment agent vs. research tool for disease induction) is correctly tagged in the TxGNN knowledge graph; false positive predictions of this type suggest node-role conflation
- **MOA data retrieval:** Obtain streptozocin's mechanism of action from DrugBank API (data gap DG002) to enable proper mechanistic filtering
- **TFDA package insert parsing:** Extract full warnings and contraindications from the retrieved PDF (data gap DG001) before any regulatory pathway assessment
- **Known-indication recall validation:** Confirm TxGNN correctly identifies pancreatic islet cell carcinoma and carcinoid tumors as positive predictions for streptozocin, as a model quality benchmark
---

