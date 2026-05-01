---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

The txgnn-pipeline skill is loaded. Now let me analyse the Evidence Pack and generate the evaluation report.

**Key observations from the data:**
- Nitrofurantoin (DB00698): known UTI antibiotic; MOA data gap
- Top predicted indication: Rheumatoid Arthritis — **KG false positive** (shared "interstitial lung fibrosis" node, not a therapeutic link)
- Zero clinical trials; 12 publications — all showing harm or indirect association, not treatment benefit
- Not marketed in Sweden (0 authorizations)
- All safety fields are data gaps
- Not antineoplastic → Cytotoxicity section omitted
- Evidence Level: L5 (model prediction only; no supportive repurposing evidence)

---

# NITROFURANTOIN: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran antibiotic used globally for the treatment and prophylaxis of urinary tract infections (UTIs).
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **12 publications** currently associated with this direction.
However, critical analysis reveals this is almost certainly a **knowledge graph false positive** — all retrieved literature documents nitrofurantoin as a cause of lung toxicity in RA patients, not as a therapeutic agent for RA itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urinary tract infection (UTI) — treatment and prophylaxis |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nitrofurantoin is not available in this dataset. Based on established pharmacology, nitrofurantoin is a nitrofuran antibiotic whose bactericidal activity is thought to derive from inhibition of multiple bacterial enzyme systems involved in carbohydrate metabolism and DNA repair. It has no known immunomodulatory, anti-inflammatory, or disease-modifying mechanism relevant to autoimmune disease.

The predicted link between nitrofurantoin and Rheumatoid Arthritis appears to be a **knowledge graph (KG) false positive**. Both nitrofurantoin and RA independently converge on the clinical entity "interstitial lung fibrosis" — nitrofurantoin as a well-documented drug-induced pulmonary toxicity (a **side effect**), and RA as a systemic disease complication. In the TxGNN knowledge graph, this shared node misleads the model into inferring a therapeutic relationship that does not exist in biology. The high TxGNN score (99.89%) reflects structural proximity in the graph, not pharmacological plausibility.

The 12 retrieved publications reinforce this interpretation: they describe antibiotic use as a risk trigger for RA flares, nitrofurantoin as a cause of irreversible pulmonary fibrosis in RA patients already on methotrexate, and general reviews of drug-induced lung toxicity. Critically, **no publication supports a therapeutic role for nitrofurantoin in RA**. The evidence pattern is consistent with potential harm rather than benefit in this patient population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | RCT/Screening | Acta Medica Scandinavica | Nitrofurantoin short-term therapy for bacteriuria in middle-aged women with 1-year follow-up — establishes drug's UTI context, no RA link |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled case series | Scientific Reports | Antibiotic use associated with RA flare timing in UK CPRD cohort (n = 31,992 RA patients); suggests infections and antibiotics influence RA activity — not a treatment signal |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Observational | Chest | Poor prognosis in RA patients hospitalised for diffuse interstitial lung fibrosis; establishes the RA–pulmonary fibrosis comorbidity underpinning the KG false positive |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | 94-year-old RA patient on long-term methotrexate developed **irreversible pulmonary fibrosis** after nitrofurantoin was added for recurrent UTI — direct evidence of harm in RA population |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis review; nitrofurantoin listed among causative agents; RA cited as a predisposing systemic disease — confirms the shared ILD node mechanism |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease patterns; nitrofurantoin cited among antibiotics implicated in pulmonary infiltrates and fibrosis |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Drug-induced autoimmune hepatitis workup; nitrofurantoin listed as drug to exclude; RA and thyroiditis mentioned as co-occurring autoimmune conditions |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonia with CD4 alveolitis in RA patient; contextualises drug-induced lung toxicity as a recurring hazard in RA pharmacotherapy |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | Historical synopsis of alveolitis and pulmonary fibrosis; background context only |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis; nitrofurantoin mentioned among drugs known to cause sialadenitis — peripheral relevance only |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every piece of retrieved evidence confirms that the TxGNN prediction for nitrofurantoin in rheumatoid arthritis is a knowledge graph artefact — both entities are linked to interstitial lung fibrosis through entirely different pathways (drug toxicity vs. disease complication), and there is no biological mechanism, clinical trial, or therapeutic literature supporting repurposing. Proceeding would carry patient safety risk given documented pulmonary toxicity in RA patients on concurrent immunosuppressants.

**To proceed, the following would be needed:**

- Identification of a plausible biological mechanism (e.g., microbiome-mediated immunomodulation, NF-κB pathway interaction) linking nitrofurantoin to RA pathogenesis
- At least one preclinical study (in vitro or in vivo animal model) demonstrating anti-inflammatory or disease-modifying activity in RA-relevant systems
- MOA data from DrugBank to assess whether any molecular targets overlap with RA disease biology
- KG graph audit to correct the false positive edge between nitrofurantoin and RA via the shared ILD node, preventing recurrence in future prediction cycles
---

