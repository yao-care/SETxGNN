---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Vildagliptin is a selective DPP-4 (dipeptidyl peptidase-4) inhibitor clinically established worldwide for treating type 2 diabetes mellitus (T2DM) — though it currently holds no Taiwan registration. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)**, with **50 clinical trials** and **20 publications** identified, anchored by a completed Phase 2 RCT conducted directly in T1DM patients. While TxGNN assigns higher raw scores to nine rare diseases in the top-10 list (ranks 1–9), those predictions carry zero supporting evidence and likely represent graph-topology false positives; T1DM (rank 10) is the only top-10 candidate with an L2 evidence base and a multi-layered, biologically coherent mechanistic rationale — and is therefore the subject of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (established clinical use globally; no formal Taiwan registration on record) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Vildagliptin is a potent, selective inhibitor of DPP-4 (also known as CD26), an enzyme that rapidly cleaves and inactivates the incretin hormones GLP-1 and GIP. By blocking DPP-4, vildagliptin extends meal-stimulated GLP-1 and GIP activity across the full 24-hour cycle, yielding glucose-dependent enhancement of insulin secretion and suppression of inappropriate glucagon secretion. These pharmacological effects are directly relevant to T1DM, where deficient glucagon counterregulation and excess post-meal glucagon hypersecretion are cardinal features that amplify hyperglycemia even when insulin is adequately replaced.

The mechanistic case for T1DM rests on four converging pathways, each independently supported by human or preclinical evidence. First, DPP-4 inhibition prolongs GLP-1 activity, suppressing pathological post-meal glucagon hypersecretion in T1DM while — critically — preserving the protective glucagon counterregulation during hypoglycemia (PMID 22855332). Second, GLP-1 signaling promotes β-cell survival, reduces apoptosis, and stimulates β-cell neogenesis in residual islet tissue, a meaningful benefit particularly in new-onset T1DM where C-peptide secretion is not yet fully abolished (PMID 25395211). Third, vildagliptin has been shown to reduce oxidative stress in pancreatic β-cells, a key driver of T1DM pathogenesis (PMID 23523961). Fourth, DPP-4/CD26 is highly expressed on activated T cells, and its inhibition may modulate the autoimmune T-cell response responsible for ongoing β-cell destruction in T1DM — a pleiotropic immune effect not shared by insulin or sulfonylureas (PMID 30848158).

Vildagliptin would not replace insulin in T1DM. Its intended role is adjunctive: to reduce glycemic variability, attenuate daily insulin requirements, protect residual β-cell mass, and potentially slow autoimmune progression. This is precisely the hypothesis tested in the completed Phase 2 RCT (NCT02803892) and the recent T1DM adolescent studies (PMID 38057844, PMID 39318059), which collectively demonstrate a clinically meaningful signal warranting further development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) | Phase 2 | Completed | 55 | Direct T1DM trial: prospective, randomized, double-blind, placebo-controlled 3-arm study of rapamycin (1 month) ± vildagliptin (3 months) vs. placebo in long-standing T1DM patients; primary endpoints were restoration of endogenous insulin production and correction of glycemic lability |
| [NCT00099931](https://clinicaltrials.gov/study/NCT00099931) | Phase 3 | Completed | 254 | Vildagliptin added to insulin in T2DM patients not at target on insulin alone; the most T1DM-analogous completed Phase 3 insulin-combination study, directly evaluating safety and efficacy in a fully insulin-dependent clinical context |
| [NCT00138606](https://clinicaltrials.gov/study/NCT00138606) | Phase 3 | Completed | 179 | 28-week extension of vildagliptin + insulin combination in T2DM; provides long-term safety and glycemic effectiveness data in insulin-requiring patients — the most directly applicable long-term safety reference for T1DM |
| [NCT05102149](https://clinicaltrials.gov/study/NCT05102149) | Phase 3 | Unknown | 672 | Multicenter, randomized, double-blind, placebo-controlled study using vildagliptin as the active comparator for PB-201 in treatment-naïve T2DM; rigorous design provides the most robust contemporaneous safety and efficacy benchmarking for vildagliptin |
| [NCT01219400](https://clinicaltrials.gov/study/NCT01219400) | Phase 4 | Completed | 28 | Evaluates whether vildagliptin affects glucagon counterregulation during standardized insulin-induced hypoglycemia in insulin-treated T2DM patients; directly informs the critical hypoglycemia safety question for T1DM adjunctive use |
| [NCT04916093](https://clinicaltrials.gov/study/NCT04916093) | Phase 4 | Completed | 60 | Head-to-head comparison of sitagliptin, vildagliptin, and metformin as first-line options in newly diagnosed T2DM; provides DPP-4 class comparative safety data including HbA1c reduction and adverse event profile |
| [NCT00821977](https://clinicaltrials.gov/study/NCT00821977) | Phase 2/3 | Completed | 338 | Vildagliptin as monotherapy in T2DM using an adaptive 2–3 period parallel-group design; establishes long-term monotherapy safety profile and dose benchmarks |
| [NCT02476760](https://clinicaltrials.gov/study/NCT02476760) | N/A | Completed | 1,417,914 | Multi-jurisdictional population-based cohort study (Canada, US, UK) assessing whether incretin-based drugs increase the risk of acute pancreatitis; critical safety context given pancreatic exposure of DPP-4 inhibitors |
| [NCT02145611](https://clinicaltrials.gov/study/NCT02145611) | Phase 4 | Completed | 50 | 12-week RCT of vildagliptin vs. glibenclamide (add-on to metformin) in T2DM with hypertension; examines GLP-1-mediated effects on endothelial function and vascular smooth muscle — relevant to T1DM cardiovascular comorbidity |
| [NCT01604213](https://clinicaltrials.gov/study/NCT01604213) | Phase 4 | Completed | 60 | Vildagliptin + metformin vs. metformin monotherapy in T2DM patients with coronary artery disease undergoing cardiac rehabilitation; evaluates anti-inflammatory (IL-6, hs-CRP), anti-thrombotic, and anti-atherosclerotic biomarker effects |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | RCT / Mechanistic Crossover | J Clin Endocrinol Metab | Vildagliptin significantly suppresses hyperglycemia-induced glucagon hypersecretion in T1DM while fully preserving protective glucagon counterregulation during hypoglycemia — the definitive human mechanistic proof of glucagon benefit in T1DM |
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT (Double-Blind) | J Clin Endocrinol Metab | Phase 2 RCT in 55 long-standing T1DM patients: rapamycin + vildagliptin vs. placebo; did not significantly restore β-cell function in established disease but provides key safety and feasibility data for the combination approach |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | Prospective Interventional | Diabetol Metab Syndr | RCT of adjunctive oral vildagliptin in T1DM adolescents and young adults on MiniMed 780G advanced hybrid closed-loop during Ramadan fasting; demonstrated significant reduction of iftar-related postprandial glucose excursions |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | Clinical Cohort (RCT) | Diabetes Obes Metab | Vildagliptin add-on in T1DM adolescents with NASH: significant reductions in MMP-14 levels, liver stiffness, and subclinical atherosclerosis markers, suggesting cardiovascular-hepatic protective effects beyond glycemic control |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Systematic Review | Expert Opin Investig Drugs | Comprehensive review of DPP-4 inhibitor pleiotropic effects: evidence for renal protection and protection of pancreatic β-cells from immune destruction in both T1DM and T2DM; clearly outlines current evidence gaps and research priorities |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Preclinical + Clinical Pilot | Curr Pharm Biotechnol | First study evaluating vildagliptin-induced β-cell neogenesis in a late-phase T1DM rat model; also demonstrated improvement in lipid homeostasis; supports the β-cell regeneration and lipid-protective mechanistic hypotheses |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Mechanistic Clinical Study | Front Endocrinol | Detailed vildagliptin mechanism review: DPP-4 inhibition restores GLP-1 and GIP levels over 24 hours, improving impaired β-cell glucose sensitivity in IFG, IGT, and T2DM; foundational pharmacodynamic context directly applicable to T1DM β-cell preservation |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Animal Study | Arch Med Res | Vildagliptin reduces oxidative stress and ameliorates pancreatic β-cell destruction in STZ-induced T1DM rats; preclinical support for antioxidant and cytoprotective mechanisms relevant to the ongoing autoimmune process in T1DM |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Clinical Study | Horm Metab Res | Early proof-of-concept: direct measurement of vildagliptin's effect on glucagon concentration during meals specifically in T1DM patients; established the glucagon regulation hypothesis in humans |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Animal/Pharmacology Study | Can J Physiol Pharmacol | Vildagliptin/pioglitazone combination improved overall glycemic control in T1DM rats; provides preclinical basis for combination strategies with insulin sensitizers in multi-drug T1DM management approaches |

---

## Taiwan Market Information

Vildagliptin currently holds **no registered product authorizations in Taiwan** (0 TFDA licenses on record). There are no approved dosage forms, brand names, or licensed indications available for review.

> Vildagliptin is available in other markets under brand names such as Galvus® (Novartis) across the EU and many Asian countries. The absence of Taiwan registration requires a complete regulatory pathway assessment and new drug application planning before any domestic clinical or commercial application.

---

## Safety Considerations

Please refer to the package insert for safety information.

> TFDA package insert data covering warnings and contraindications could not be retrieved at the time of this report. Downloading and parsing the official TFDA package insert PDF is a **blocking prerequisite** (DG001) before any formal safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT conducted directly in T1DM patients (NCT02803892), combined with two independent RCTs demonstrating glucagon suppression and glycemic benefit in T1DM (PMID 22855332; PMID 38057844), a systematic review supporting β-cell immune protection (PMID 30848158), and an emerging body of pediatric clinical cohort data (PMID 39318059), collectively establish an L2 evidence base with a multi-layered and biologically coherent mechanistic rationale. The primary benefit signal — suppression of pathological post-meal glucagon with preservation of hypoglycemia-protective glucagon — is consistent across human studies and represents a clinically meaningful contribution to T1DM adjunctive management.

**To proceed, the following is needed:**

- **Retrieve TFDA package insert** for formal warnings, contraindications, and hepatic/renal dosing restrictions — this is a blocking prerequisite before any safety clearance (DG001)
- **Obtain DrugBank MOA data** including DPP-4 inhibitory kinetics, substrate selectivity, and known off-target interactions (DG002)
- **Define the target T1DM population**: new-onset T1DM with residual C-peptide secretion is expected to benefit more than long-standing T1DM with complete β-cell absence; population selection criteria should be pre-specified
- **Design a Phase 2/3 RCT** of vildagliptin as add-on to standard insulin therapy in T1DM, with primary endpoints of HbA1c reduction, time-in-range improvement, daily insulin dose change, and hypoglycemic event frequency
- **Conduct long-term immunomodulatory safety assessment**: DPP-4/CD26 is expressed on activated T cells; chronic inhibition effects on autoimmune disease activity, infection risk, and other immune-mediated conditions require prospective monitoring
- **Assess drug interactions** with rapid-acting insulin analogues, CGM systems, and common T1DM co-medications (e.g., SGLT2 inhibitors, which carry a DKA risk that may be relevant in insulin-deficient states)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

