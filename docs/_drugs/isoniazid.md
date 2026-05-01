---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the `txgnn-pipeline` skill for context. Now generating the report from the Evidence Pack.

---

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a cornerstone anti-tuberculosis antibiotic used for both active and latent TB treatment.
The TxGNN model predicts it may be effective for **conjunctivitis**, with **1 clinical trial** and **20 publications** currently available — however, the evidence relates specifically to **tuberculosis-associated** conjunctivitis rather than conjunctivitis as a broad clinical category.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (active and latent) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Sweden Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on well-established pharmacological knowledge, isoniazid is a frontline antimycobacterial agent whose efficacy against tuberculosis has been demonstrated for decades. It acts by inhibiting mycolic acid biosynthesis in *Mycobacterium tuberculosis* (via InhA inhibition), disrupting the integrity of the bacterial cell wall and ultimately killing the organism.

The mechanistic link to conjunctivitis is plausible — but narrowly so. Isoniazid may benefit two specific ocular subtypes: **primary tuberculous conjunctivitis** (direct infection of conjunctival tissue by *M. tuberculosis*) and **phlyctenular keratoconjunctivitis** (an immune-mediated hypersensitivity reaction to *M. tuberculosis* antigens). Both are recognised, if rare, manifestations of TB in which anti-TB therapy including isoniazid forms the cornerstone of treatment.

Critically, "conjunctivitis" as a diagnostic category also encompasses viral, bacterial (non-TB), allergic, and toxic subtypes — against none of which isoniazid has any known mechanistic benefit. The TxGNN model's high score (99.36%) most likely reflects strong knowledge-graph linkages between tuberculosis nodes and ocular symptom nodes, rather than a broad repurposing opportunity across conjunctivitis of all etiologies. This limits the practical scope of this prediction considerably.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Pragmatic RCT comparing 3HP vs 1HP regimens for latent TB infection (LTBI) prevention; primary endpoint is incidence of systemic drug reactions — conjunctivitis is **not** a treatment target and appears only as a potential adverse event monitor item, not as evidence of therapeutic benefit |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort/Prophylaxis Study | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis in Alaskan Eskimos — the most directly relevant evidence; demonstrates INH reducing TB-associated keratoconjunctivitis incidence |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Clinical Report | Ann Oculistique | Describes local isoniazid application in the treatment of ocular tuberculosis; supports topical/systemic INH use in TB-origin eye disease |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis; treated with standard anti-TB regimen including isoniazid with resolution |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | *M. tuberculosis* presenting as chronic red eye; illustrates TB conjunctivitis as a diagnostic and treatment challenge, managed with anti-TB therapy |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket successfully treated with anti-TB drugs; highlights TB as a rare but ongoing cause of conjunctivitis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case Series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis; 13 in children with primary TB; positive tuberculin test in all; outcome improved with anti-TB treatment |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Report | Can J Ophthalmol | Conjunctival phlyctenulosis as an early warning sign of impending clinical tuberculosis; reinforces TB treatment as the definitive intervention |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clin Pediatrics | Unexpected cause of conjunctivitis in an adolescent; clinical context suggests TB-related etiology managed with anti-infective therapy |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Arch Ophthalmol | Early documentation of primary tuberculosis of the conjunctiva; historical baseline for understanding TB-origin conjunctival disease |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Review of systemic drugs causing ocular side effects; contextualises drug–conjunctiva interactions including conjunctivitis as a drug-induced event — not directly supportive of INH repurposing |

---

## Sweden Market Information

No marketing authorizations for isoniazid were found in the database (0 authorizations, not marketed). Isoniazid is typically dispensed as part of fixed-dose combination anti-TB products or through hospital pharmacy channels, and may be accessible via named-patient or compassionate use pathways when clinically indicated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication "conjunctivitis" is a clinically broad category; all identifiable evidence supports isoniazid only for the rare subtype of **tuberculosis-associated conjunctivitis**, which is already addressed within existing TB treatment guidelines. The single clinical trial does not investigate conjunctivitis as a therapeutic endpoint, and the entire literature base consists of historical case reports and case series — none constituting systematic or controlled evidence of benefit for conjunctivitis in general.

**To proceed, the following is needed:**

- **Narrow the indication scope**: Reframe the target indication from "conjunctivitis" to "tuberculous conjunctivitis / phlyctenular keratoconjunctivitis secondary to TB" to improve scientific validity and regulatory plausibility
- **Mechanism of action data**: Retrieve complete MOA from DrugBank (DG002 data gap) to strengthen mechanistic justification documentation
- **Safety profile**: Obtain full warning and contraindication data from the TFDA package insert (DG001 data gap, currently Blocking severity) before any clinical evaluation proceeds
- **Systematic review**: Commission or identify a systematic review of anti-TB therapy outcomes specifically in phlyctenular keratoconjunctivitis to upgrade evidence from L4 to L3
- **Ophthalmology expert consultation**: Confirm clinical relevance and unmet need with ophthalmology specialists, given that this is an exceedingly rare indication in modern TB-low-prevalence settings
---

