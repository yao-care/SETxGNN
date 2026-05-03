---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Ritonavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Ritonavir is a well-established HIV protease inhibitor, globally approved as part of combination antiretroviral therapy (cART) for HIV-1 infection, though it currently holds no registrations in the Taiwan drug database.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **12 publications** supporting this direction—all derived from preclinical animal models and in vitro studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (globally established; not registered in current market database) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (Preclinical: Animal & In Vitro Studies) |
| Sweden Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory database. Based on established pharmacological knowledge, Ritonavir is an HIV protease inhibitor originally developed to treat HIV-1 infection. It acts by competitively binding to the viral protease active site, blocking cleavage of the Gag-Pol polyprotein precursor and thereby preventing viral particle maturation into infectious virions.

The mechanistic link to SIV infection is biologically coherent. SIV and HIV belong to the same genus (*Lentivirus*) of primate retroviruses, and their protease structures are highly conserved. The substrate-binding groove of SIV protease differs only minimally from that of HIV-1, and multiple in vitro studies have directly confirmed that Ritonavir inhibits SIVmac239 at nanomolar concentrations (IC₅₀ ≈ 13 nM) comparable to its activity against HIV-1 (IC₅₀ ≈ 25 nM). This cross-reactivity is a direct consequence of shared protease architecture rather than an indirect inference.

That said, a critical context applies: SIV infection is primarily a disease of non-human primates and a research tool for modeling HIV/AIDS. It does not represent a direct human clinical indication in the conventional sense. The high TxGNN score likely reflects the drug's mechanistic overlap and the abundance of SIV/ART co-occurrence signals in the knowledge graph, rather than an actionable human repurposing opportunity. Occupational exposure risk in primate research facilities represents the only narrow human-facing scenario.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ritonavir in Simian Immunodeficiency Virus Infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In Vitro | Antimicrob Agents Chemother | Direct comparison of SIVmac239 and HIV-1 susceptibility to protease inhibitors; Ritonavir inhibited SIV at IC₅₀ of 13 nM vs 25 nM for HIV-1, confirming cross-reactivity |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro | Antiviral Ther | Evaluated 16 approved antiretrovirals (including Ritonavir) against HIV-2, SIVmac251, SIVb670, and SHIV strains; informed guidance for treatment and post-exposure prophylaxis |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study (NHP) | J Virol | Quadruple ART including Ritonavir in SIVmac251-infected cynomolgus macaques; characterized rapid viral decay kinetics analogous to HIV-1 mathematical models |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Study (NHP) | PLoS Pathog | Highly intensified ART (including Ritonavir-based regimen) in SIVmac251-infected rhesus macaques achieved sustained viremia suppression and measurable reduction of the viral reservoir |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Study (NHP) | PLoS One | cART + HDAC inhibitor (SAHA) in SIV-infected Chinese-origin rhesus macaques; established a reliable NHP model for studying viral reservoirs on suppressive ART |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal Study | Microbes Infect | Constructed a novel SHIV carrying the HIV-1-derived protease gene to enable in vivo testing of protease inhibitors; viral growth fully blocked by protease inhibitors in vitro and attenuated in rhesus macaques |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal Study (NHP) | J Virol Methods | Oral HAART (AZT + 3TC + Lopinavir/Ritonavir) in SHIV89.6P-infected macaques; assessed CD8 subset kinetics following treatment |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Study (NHP) | mBio | Demonstrated that lentiviral brain reservoirs persist in microglia despite effective ART across multiple NHP and human models; relevant to CNS sanctuary site understanding |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Mechanistic | J Virol | HIV-1 Vif protein is cleaved by viral protease; establishes mechanistic role of protease in processing accessory proteins, relevant to understanding PI activity scope |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In Vitro | Antiviral Chem Chemother | K-12 fluoroquinolone showed activity against ritonavir-resistant HIV strains and SIV; Ritonavir used as resistance benchmark, confirming SIV as a valid test system |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is primarily a disease of non-human primates and serves as a research surrogate for HIV/AIDS; it does not constitute a conventional human clinical indication. While in vitro evidence confirms Ritonavir inhibits SIV protease at nanomolar concentrations comparable to HIV-1, all 12 supporting publications are preclinical (animal models and in vitro assays), with no registered human clinical trials. The mechanistic basis is sound, but the translational pathway to a human indication is not established.

**To proceed, the following is needed:**
- Clarify the clinical question: Is the goal (a) validating Ritonavir as a preclinical tool in SIV models, or (b) evaluating occupational post-exposure prophylaxis for primate researchers?
- If (b), conduct a systematic review of occupational SIV exposure cases and existing PEP protocols
- Obtain formal mechanism of action documentation (DrugBank API) to complete the regulatory safety profile
- Retrieve Taiwan package insert (TFDA PDF) to populate key warnings, contraindications, and DDI data before any S1 safety assessment can proceed
- Consider whether a higher-value repurposing target exists, given Ritonavir's well-known role as a CYP3A4 inhibitor used as a pharmacokinetic booster (e.g., in Paxlovid), which may represent a more clinically actionable direction
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

