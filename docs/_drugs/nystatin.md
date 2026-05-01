---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Nystatin
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

---

# Nystatin: From Candidiasis to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal antibiotic first introduced in the 1950s, primarily used for the topical treatment of Candida infections.
The TxGNN model predicts it may be effective for **vulvovaginitis** — inflammation of the vulva and vagina most commonly caused by *Candida albicans* —
with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record; known use: fungal infections / candidiasis |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Market Status | ✗ Not Marketed (0 approvals) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on established pharmacology, nystatin is a polyene macrolide antifungal that selectively binds to ergosterol in the fungal cell membrane. This binding creates transmembrane pores, increases membrane permeability, and causes leakage of intracellular contents — resulting in fungicidal activity. Because ergosterol is found in fungal membranes but not mammalian cell membranes, nystatin's selectivity is high, making it well-tolerated when applied topically.

*Candida albicans* is responsible for 85–90% of vulvovaginitis cases of infectious origin, making it the primary pathogen in this condition. Nystatin vaginal tablets have been used as a first-line topical treatment since the 1950s — the TxGNN model's top prediction therefore reflects a well-established mechanistic fit rather than a speculative leap. What makes this prediction clinically significant today is the rising prevalence of fluconazole-resistant *Candida* species, where azole therapy fails and nystatin re-emerges as a critical alternative. A 2024 review (PMID 39771534) identifies nystatin alongside boric acid and newer antifungals as key options in this drug-resistant context.

A 2018 rat-model study (PMID 30359236) further demonstrated that nystatin not only eliminates the pathogen but also enhances the vaginal mucosal immune response and protects vaginal epithelial ultrastructure during *C. albicans* infection — suggesting immunomodulatory benefits beyond direct antifungal action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Systematic Review | BMJ Clinical Evidence | VVC is the second most common cause of vaginitis; *C. albicans* accounts for 85–90% of cases; reviews comparative antifungal efficacy including nystatin |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Systematic Review | BMJ Clinical Evidence | Updated evidence on VVC epidemiology and treatment options; confirms nystatin as active comparator |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Systematic Review | BMJ Clinical Evidence | VVC treatment evidence review; comparative data across antifungal classes |
| [16620487](https://pubmed.ncbi.nlm.nih.gov/16620487/) | 2005 | Systematic Review | Clinical Evidence | Evidence-based overview of vulvovaginal candidiasis; nystatin vs. azole efficacy discussed |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Systematic Review | Journal of Women's Health | Recurrent VVC management; non-albicans *Candida* increasingly resistant to azoles; nystatin identified as alternative |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Clinical Review | Pharmaceutics | Fluconazole-resistant VVC management; nystatin identified as key alternative alongside boric acid, oteseconazole, and ibrexafungerp |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical Study | BMC Microbiology | Nystatin enhances vaginal mucosal immune response against *C. albicans* and protects vaginal epithelial ultrastructure in rat VVC model |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Observational Study | Mycoses | In vitro susceptibility testing of 287 *Candida* isolates from complicated VVC; nystatin MICs correlated with clinical treatment outcomes |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Clinical Study | Ceska Gynekologie | Evaluation of combined vaginal nifuratel + nystatin therapy for mixed vulvovaginal infections; treatment outcomes assessed |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Clinical Review | Obstetrics and Gynecology Clinics of North America | Historical overview of topical antifungals; nystatin introduced 1950s for VVC treatment; role in context of azole era discussed |

---

## Market Authorizations

No approved product registrations found. Nystatin is not currently marketed and has no recorded authorizations on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nystatin has a well-established mechanistic and clinical basis for treating *Candida*-driven vulvovaginitis, supported by multiple tier-1 systematic reviews and over six decades of clinical use. The TxGNN prediction confirms this indication alignment rather than proposing a speculative new use, and the drug's renewed relevance in fluconazole-resistant cases adds contemporary clinical value.

**To proceed, the following is needed:**
- Retrieve the full package insert (仿單/SmPC) to document contraindications, dosage guidance, and labeled warnings
- Query the DrugBank API to populate MOA data and complete the mechanistic documentation
- Confirm the intended market and identify the appropriate regulatory filing pathway, given zero existing local approvals
- Define the target patient population — specifically whether to position nystatin as a first-line option or as an alternative reserved for fluconazole-resistant or recurrent VVC cases
- Identify a suitable vaginal dosage form (pessary, tablet, cream) and assess manufacturing or importation feasibility for market introduction
---

