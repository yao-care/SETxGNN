---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

The txgnn-pipeline skill covers technical pipeline operations and isn't specific to report writing here. The main system prompt provides the complete report format. I'll now generate the evaluation report.

---

# Tobramycin: From Gram-negative Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Tobramycin is a broad-spectrum aminoglycoside antibiotic with well-established bactericidal activity against Gram-negative organisms — particularly *Pseudomonas aeruginosa* — used in serious bacterial infections including pulmonary infections in cystic fibrosis and necrotizing otitis externa.
The TxGNN model predicts it may be effective for **Exposure Keratitis** (score: 99.93%), with **2 clinical trials** and **7 publications** identified in the surrounding evidence — though none directly evaluate tobramycin as a treatment for this specific condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-negative bacterial infections (*Pseudomonas aeruginosa* and related organisms) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Sweden Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, tobramycin is an aminoglycoside antibiotic whose bactericidal activity derives from irreversible binding to the bacterial 30S ribosomal subunit, inhibiting protein synthesis. It is particularly effective against aerobic Gram-negative bacteria and demonstrates concentration-dependent killing — properties that underpin its clinical use against *Pseudomonas aeruginosa* across multiple infection sites.

The mechanistic connection to exposure keratitis is indirect but biologically plausible. Exposure keratitis occurs when incomplete eyelid closure leaves the corneal epithelium chronically unprotected; this barrier disruption substantially raises the risk of secondary bacterial superinfection, with Gram-negative pathogens among the chief culprits. In this context, topical tobramycin acts not as a treatment for the underlying exposure itself, but as prophylactic or adjunctive antibacterial coverage — a role well-supported by its ophthalmic formulation's activity spectrum.

One critical caution arises from the literature: PMID 2707046 demonstrates, in a rabbit corneal epithelial cell model, that tobramycin — alongside other aminoglycosides — exhibits direct cytotoxicity to corneal epithelial cells. Since the cornea in exposure keratitis is already compromised, prolonged topical aminoglycoside use could potentially worsen epithelial damage rather than promote healing. This safety signal means the therapeutic window for tobramycin in this setting requires careful evaluation.

---

## Clinical Trial Evidence

Neither of the 2 identified trials directly evaluates tobramycin in exposure keratitis (both received Grade C relevance):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Evaluates platelet-rich fibrin (PRF) membrane for four ophthalmic conditions (macular hole, pterygium, corneal ulcer, glaucoma trabeculectomy); no tobramycin component |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic herpetic (HSV) keratitis; viral etiology — tobramycin has no antiviral activity |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case Report | Oxford Medical Case Reports | MDR *Shewanella algae* bacterial keratitis in a vegetative patient unable to close his eyes — directly illustrates the secondary bacterial keratitis risk in prolonged corneal exposure |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case Report | Ophthalmology | First reported contact lens-related *Bacillus cereus* keratitis and ulcer from contaminated lens case; highlights Gram-positive bacterial pathogen diversity in corneal infections |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case Report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy; illustrates the need for antibacterial prophylaxis after any corneal barrier disruption |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In Vitro Study | Current Eye Research | **Key safety signal**: tobramycin (alongside neomycin, gentamicin, amikacin) demonstrated cytotoxicity to rabbit corneal epithelial cells in culture; exposure duration and concentration both matter |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | MIC Study | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect of antibiotic eyedrops (including tobramycin) against isolates from the Japanese National Surveillance of Infectious Keratitis — provides in vitro activity benchmarks |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case Report | Eye Science | Paracentral corneal dellen in Graves ophthalmopathy — example of corneal exposure from incomplete eyelid closure, illustrating the clinical context tobramycin might address |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospective Case Series | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis treatment outcomes (60 cases); limited direct applicability to human exposure keratitis |

---

## Safety Considerations

Please refer to the package insert for complete safety information. Based on evidence identified within this review:

- **Corneal epithelial toxicity**: In vitro data (PMID 2707046) confirms aminoglycoside-class toxicity to corneal epithelial cells, including tobramycin. This is a specific and clinically meaningful concern for topical use on an already-compromised corneal surface in exposure keratitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for tobramycin as adjunctive antibacterial prophylaxis in exposure keratitis is biologically plausible, but the evidence base is entirely indirect (L4: in vitro data and case reports of secondary bacterial keratitis). Critically, tobramycin's own corneal epithelial cytotoxicity — demonstrated in vitro — raises the possibility that the drug could worsen an already-fragile corneal surface, creating a risk-benefit balance that has not been formally evaluated in this indication.

**To proceed, the following is needed:**
- Prospective clinical data specifically evaluating antibacterial prophylaxis strategies in exposure keratitis, with tobramycin as a study arm
- Head-to-head safety comparison of topical tobramycin vs. fluoroquinolone alternatives (e.g., ciprofloxacin, moxifloxacin) on compromised corneal epithelium
- Complete MOA and safety data retrieved from DrugBank and TFDA/MPA package insert (currently flagged as data gaps DG001 and DG002)
- Ophthalmic formulation regulatory status confirmed for the target market before any clinical pathway is designed
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

