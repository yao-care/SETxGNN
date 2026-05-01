---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

Using `txgnn-pipeline` to confirm context for this Evidence Pack — this is an SeTxGNN (Sweden) drug repurposing evaluation. Now generating the report.

**Expert judgment note:** The Evidence Pack's top-scored predictions (ranks 1–5) are all L5/Hold with no evidence and explicit mechanistic flags as TxGNN graph diffusion artifacts. The most clinically actionable prediction — with direct ofloxacin evidence and the strongest recommendation — is **rank 8: Septicemic Plague** ("Proceed with Guardrails"). This is selected as the primary subject of this report.

---

# Ofloxacin: From Bacterial Infections to Septicemic Plague

## One-Sentence Summary

Ofloxacin is a broad-spectrum fluoroquinolone antibiotic with established bactericidal activity against a wide range of gram-positive and gram-negative organisms.
The TxGNN model predicts it may be effective for **Septicemic Plague** (*Yersinia pestis*), with **20 publications** supporting this direction — including direct in vitro susceptibility data and animal model studies confirming ofloxacin's anti-*Y. pestis* activity, the same mechanistic basis used by the FDA to approve related fluoroquinolones for plague treatment under the Animal Efficacy Rule.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (fluoroquinolone antibiotic class) |
| Predicted New Indication | Septicemic Plague (*Yersinia pestis*) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ofloxacin is a second-generation fluoroquinolone antibiotic that works by inhibiting two essential bacterial enzymes: DNA gyrase (topoisomerase II) and topoisomerase IV. These enzymes are required for DNA replication, transcription, repair, and chromosomal segregation. By forming a stable drug–enzyme–DNA ternary complex, ofloxacin induces irreversible double-strand DNA breaks, producing a rapid bactericidal effect across a broad spectrum of pathogens. Notably, levofloxacin — the active L-isomer of the racemic ofloxacin — is essentially half the ofloxacin molecule, meaning the two drugs share an identical pharmacophore and mechanism.

*Yersinia pestis*, the bacterium responsible for bubonic, septicemic, and pneumonic plague, encodes GyrA/GyrB (DNA gyrase) and ParC/ParE (topoisomerase IV) subunits that are naturally susceptible to fluoroquinolones. The mechanistic link is direct and experimentally confirmed: ofloxacin achieves a MIC of approximately 0.08 mg/L against *Y. pestis* (PMID 16127904), and ranked among the most active antibiotics tested in a panel of 78 clinical *Y. pestis* strains — second only to ciprofloxacin (PMID 8540736). In vivo, ofloxacin provided both prophylactic and therapeutic protection in murine plague models (PMID 16127904; PMID 8203841).

This prediction aligns with existing regulatory precedent. Because human plague clinical trials are ethically and practically impossible — the disease is too rare and too lethal — the FDA approved ciprofloxacin and levofloxacin for plague under the Animal Efficacy Rule (21 CFR 314.600), based on exactly the same mechanistic rationale and animal model evidence class that exists for ofloxacin. The TxGNN model, in this case, is capturing a genuine and well-grounded pharmacological relationship, not an artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. This is expected for plague: human efficacy trials are not feasible given the disease's rarity and the lethality of deliberate exposure. Regulatory approval for fluoroquinolones in this indication is specifically granted via the FDA Animal Efficacy Rule, which explicitly bypasses the Phase 2/3 human trial requirement. Any future submission for ofloxacin would follow the same pathway.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Regulatory Review | *Clin Infect Dis* | FDA Animal Efficacy Rule approvals for pneumonic plague; establishes the regulatory framework directly applicable to ofloxacin |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal Model (NHP) | *Clin Infect Dis* | Ciprofloxacin and levofloxacin ≥90% effective in African green monkey plague model; confirms fluoroquinolone class efficacy at human-equivalent PK exposures |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal Model (NHP) | *PLoS Negl Trop Dis* | Levofloxacin (ofloxacin's active isomer) cures experimental pneumonic plague in non-human primates — strongest class-level proxy evidence |
| [37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/) | 2023 | Review | *Am J Trop Med Hyg* | Global plague epidemiology 2010–2019: 4,547 cases across 6 countries, 17% mortality; treatment landscape including fluoroquinolones |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal Model (In vivo) | *Antibiotiki i khimioterapiia* | **Direct ofloxacin data**: MIC 0.08 mg/L against *Y. pestis*; prophylactic and therapeutic efficacy demonstrated in albino mice infected with both antigen-complete and antigen-defective strains |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | *Antimicrob Agents Chemother* | Ofloxacin active against 78 *Y. pestis* clinical strains; activity ranked behind ciprofloxacin, ahead of traditionally used agents (streptomycin, tetracycline, chloramphenicol) |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal Model (In vivo) | *Antimicrob Agents Chemother* | Ofloxacin efficacious in vivo in a standardised mouse model of systemic *Y. pestis* infection alongside ceftriaxone and gentamicin |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal Model | *Antibiotiki i khimioterapiia* | Ofloxacin used as reference fluoroquinolone in combined emergency plague prophylaxis experiments (antibiotic + vaccine); confirms its role as a class comparator |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal Model (In vivo) | *Antimicrob Agents Chemother* | Fluoroquinolone class evaluated head-to-head with streptomycin for murine pneumonic plague; establishes class efficacy benchmark |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal Model (Comparative) | *Antibiotiki i khimioterapiia* | Levofloxacin and moxifloxacin ED₅₀ 5.5–14 mg/kg against FI⁺ and FI⁻ *Y. pestis* strains in mice; phenotype-independent efficacy supports class robustness |

---

## Sweden Market Information

Ofloxacin is not currently registered with the Swedish Medical Products Agency (MPA). There are no marketing authorizations on record. Any use in Sweden would require either a new marketing authorization application or a compassionate use / emergency preparedness pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level alert:** Fluoroquinolones carry established class-wide risks including QT prolongation, tendinopathy/tendon rupture (risk elevated with concomitant corticosteroids), peripheral neuropathy, and CNS effects (seizures, psychosis). These should be factored into any benefit–risk assessment.
>
> **Reverse safety signal (from Evidence Pack):** The TxGNN rank 2 prediction for *hyperamylasemia* should be treated as a contraindication signal, not a treatment opportunity. Fluoroquinolones — including ofloxacin — are a documented drug-induced cause of pancreatitis. Administering ofloxacin to patients with elevated amylase is potentially harmful.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ofloxacin demonstrates direct in vitro and in vivo efficacy against *Yersinia pestis* through the same mechanism (DNA gyrase inhibition) that underpins FDA-approved fluoroquinolone plague treatments. The evidence level (L3) meets the standard historically applied to plague drug approvals, where human clinical trials are not ethically possible and the Animal Efficacy Rule governs regulatory decision-making.

**To proceed, the following is needed:**

- **PK/PD benchmarking:** Confirm that ofloxacin's AUC/MIC ratio against *Y. pestis* at standard clinical doses achieves the bactericidal threshold established for approved comparators (ciprofloxacin 400 mg IV q12h; levofloxacin 500 mg IV q24h)
- **Resistance profile documentation:** Screen for quinolone cross-resistance; PMID 21574421 confirms nalidixic acid-resistant (Nal^r) *Y. pestis* mutants are cross-resistant to levofloxacin and moxifloxacin — the same risk likely applies to ofloxacin
- **Regulatory pathway mapping:** Assess feasibility of MPA/EMA authorization under Sweden's national biodefense or emergency preparedness provisions, aligned with the FDA Animal Efficacy Rule precedent
- **MOA formal documentation:** Resolve current DrugBank data gap by querying the API for complete mechanism-of-action characterisation
- **Package insert retrieval:** Obtain Sweden/EU package insert to complete key warnings, contraindications, and drug interaction profiling

---

### Additional Predictions Overview

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|-----------|-------------|---------------|---------------|-------|
| 6 | Monoclonal Gammopathy (infection prophylaxis in myeloma) | 99.82% | L3 | Research Question | Levofloxacin Phase 3 RCT (TEAMM, PMID 31668592) shows class-level efficacy; 20 publications; ofloxacin-specific data lacking |
| 10 | Punctate Epithelial Keratoconjunctivitis | 99.57% | L4 | Research Question | Ofloxacin 0.3% eye drops already used for bacterial ocular infections; existing literature indirect only |
| 1–5, 7, 9 | Haematological conditions (polyclonal hyperviscosity, congenital analbuminemia, etc.) | ≥99.72% | L5 | Hold | No mechanistic link; no evidence; likely TxGNN graph diffusion artefacts from adjacent haematological disease nodes |
| 2 | Hyperamylasemia | 99.91% | L5 | **Contraindication** | Fluoroquinolones are known pancreatitis inducers — ofloxacin may worsen this condition |
---

