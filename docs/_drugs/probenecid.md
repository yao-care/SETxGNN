---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 3
---

# Probenecid
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Probenecid: From Gout / Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Probenecid is a well-established uricosuric agent used to treat gout and chronic hyperuricemia by blocking renal tubular uric acid reabsorption.
The TxGNN model assigns a high prediction score (99.73%) to **Renal Hypouricemia** as a potential new indication, supported by **0 clinical trials** and **20 publications**.
However, a critical mechanistic paradox exists: Probenecid promotes uric acid excretion, which would **aggravate** rather than treat renal hypouricemia — the literature consistently records its role as a **diagnostic probe**, not a therapeutic agent, in this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricemia (no Taiwan authorization on record; based on established pharmacological use) |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Probenecid is a uricosuric agent that inhibits URAT1 (SLC22A12) and OAT4 transporters in the proximal renal tubule, thereby blocking uric acid reabsorption and increasing urinary uric acid excretion. This is the pharmacological basis for its use in lowering serum urate in gout and chronic hyperuricemia. Formal mechanism of action data was not retrieved in this Evidence Pack and is recorded as a data gap, but the drug's transport-inhibitor profile is well-characterised in the referenced literature.

The TxGNN model's high score for renal hypouricemia reflects genuine **biological pathway proximity** — both Probenecid's mechanism and the pathophysiology of renal hypouricemia centre on the URAT1/OAT urate transport system. Renal hypouricemia is caused by loss-of-function mutations in SLC22A12 (URAT1) or GLUT9, resulting in insufficient uric acid reabsorption and chronically low serum urate. The model has correctly identified that this drug and this disease are tightly connected within the same molecular network.

However, this connection represents a **mechanistic contradiction**, not a therapeutic opportunity. Probenecid acts in the same direction as the disease defect — further reducing tubular uric acid reabsorption — which would deepen hypouricemia rather than correct it. What the literature does document (PMID 854144, 8341392, 3813739) is Probenecid's role as a **pharmacological diagnostic probe**: the attenuated or paradoxical uric acid clearance response to Probenecid in hypouricemic patients has been used to distinguish defective-reabsorption subtypes from secretion-enhanced subtypes. The TxGNN score should therefore be interpreted as reflecting co-involvement in the URAT1/OAT pathway, not therapeutic efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia aetiology and classification for rheumatologists; defines serum urate < 2 mg/dL; discusses renal vs. extrarenal causes including URAT1 mutations |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Molecular Genetics and Metabolism | Comprehensive review of hereditary renal hypouricemia; SLC22A12 loss-of-function mutations as primary cause; phenotypic variability and URAT1-independent subtypes discussed |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Clinical case series | Journal of the American Society of Nephrology | SLC22A12 gene sequencing in 32 Japanese patients with idiopathic renal hypouricemia; correlated genetic subtype with urate clearance and clinical phenotype |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review | American Journal of Kidney Diseases | Exercise-induced acute renal failure in renal hypouricemia; case report plus literature review; first systematic discussion of ARF prevention strategies |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report + functional study | Nephron | Familial hypouricemia with markedly elevated uric acid clearance; **attenuated response to both probenecid and pyrazinamide** confirmed a proximal tubular high-capacity reabsorption defect — probenecid used explicitly as diagnostic probe |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report + functional study | Nephron | Novel subtype with drug-insensitive secretion plus defective reabsorption; **no response to probenecid or pyrazinamide**; inosine paradoxically increased urate clearance beyond creatinine clearance |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Clinical study | Archives of Internal Medicine | Diabetic renal hypouricemia in 7 patients; increased pyrazinamide-suppressible urate clearance; **maximal uricosuric response to probenecid** used to characterise tubular transport abnormality in diabetic kidney |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Enhanced tubular secretion subtype with urolithiasis; **probenecid and benzbromarone both markedly increased urate clearance**, confirming secretion-dominant mechanism; urine alkalization successful for stone treatment |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Case report | American Journal of Kidney Diseases | Cholangiocarcinoma with severe persistent hypouricemia (uric acid 1.16–1.40 mg/dL); fractional urate clearance only minimally suppressed by pyrazinamide; **probenecid test used to characterise renal urate handling** |
| [7933674](https://pubmed.ncbi.nlm.nih.gov/7933674/) | 1994 | Case report | Nihon Jinzo Gakkai | 20-year-old with hypouricemia and idiopathic hypercalciuria; urate minimally increased after probenecid but decreased after benzbromarone — incomplete combined pre- and post-secretory reabsorption defect confirmed |

---

## Taiwan Market Information

Probenecid currently holds **no regulatory authorizations in Taiwan**. There are no approved products, licensed dosage forms, or recorded indications in the Taiwan market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model correctly identifies that Probenecid and renal hypouricemia share the URAT1/OAT urate transport pathway, but the two are connected in opposing directions — Probenecid inhibits the reabsorption that is already deficient in this disease, meaning therapeutic use would deepen the patient's hypouricemia and risk worsening exercise-induced acute renal failure, a known complication of this condition. The existing literature confirms Probenecid's role in this disease is diagnostic (probing tubular transport subtype), not therapeutic.

**To proceed, the following is needed:**

- **Clarify the research question**: Is the goal to evaluate Probenecid as a diagnostic probe (scientifically valid, already documented in multiple case reports) or as a therapeutic candidate (mechanistically contraindicated)? These require entirely different development paths.
- **Retrieve full MOA data** from DrugBank (currently a data gap) to formally document the URAT1/OAT4 inhibition mechanism.
- **Retrieve Taiwan package insert warnings and contraindications** (currently a blocking data gap) before any safety assessment can proceed.
- **Consider alternative repurposing targets**: Rank 2 (Lesch-Nyhan syndrome) and Rank 3 (HPRT partial deficiency / Kelley-Seegmiller syndrome) both involve *excess* uric acid production, where Probenecid's uricosuric action is directionally appropriate — though the evidence base for rank 2–3 is also limited and would require a separate targeted literature review.
---

