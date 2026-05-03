---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

Using the `txgnn-pipeline` skill context confirmed — this is a TW-series TxGNN drug repurposing report. Generating now based on the Evidence Pack.

---

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sunitinib (Sutent®) is a multi-targeted receptor tyrosine kinase inhibitor (TKI) approved globally for advanced renal cell carcinoma (RCC), imatinib-resistant gastrointestinal stromal tumor (GIST), and pancreatic neuroendocrine tumors (pNET), though it is currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **2 directly relevant completed Phase 2 clinical trials** and **9 publications** currently supporting this direction.
The mechanistic basis is strong — liposarcoma is driven by PDGFR-α/β and VEGFR signaling, both of which are core targets of sunitinib.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced/metastatic renal cell carcinoma; GIST (FDA-approved globally; not registered in Taiwan) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sunitinib simultaneously inhibits multiple receptor tyrosine kinases — including VEGFR-1/2/3, PDGFR-α/β, KIT, FLT3, RET, and CSF1R. Its antitumor effect is delivered through two complementary mechanisms: blocking tumor angiogenesis (via VEGFR) and suppressing direct tumor cell proliferation signals (via PDGFR and KIT). This broad-spectrum kinase inhibition is what gives sunitinib potential across multiple cancer types.

Liposarcoma, the most common adult soft tissue sarcoma, is highly dependent on PDGFR-α/β and VEGFR-driven signaling for tumor growth and neovascularization. Well-differentiated and dedifferentiated liposarcomas frequently harbor MDM2/CDK4 amplification and show elevated VEGF expression, while myxoid liposarcomas carry FUS-DDIT3 translocations that maintain active PDGFR-driven proliferative loops. Sunitinib's dual VEGFR/PDGFR blockade provides a direct on-target rationale for activity in these subtypes.

Clinical precedent exists as well. Multiple Phase 2 trials have specifically enrolled non-GIST soft tissue sarcoma patients — explicitly including liposarcoma subgroups — and tested sunitinib in this population. A single-institution Phase 2 study (Mahmood et al., 2011) directly focused on leiomyosarcoma, liposarcoma, and malignant fibrous histiocytoma. While objective response rates are modest, durable stable disease and partial responses have been documented, including one case report of long-lasting clinical benefit in heavily pre-treated metastatic liposarcoma (Porzio et al., 2013).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Sunitinib continuous daily dosing in metastatic/locally advanced non-GIST sarcomas; explicitly covers liposarcoma subtype; primary endpoint is antitumor activity and safety |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Sunitinib malate in unresectable or metastatic soft tissue sarcoma (leiomyosarcoma, liposarcoma, fibrosarcoma, MFH) at Moffitt Cancer Center; assesses promising dose and response |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | Regorafenib (SARC024) in multiple sarcoma subtypes; sunitinib prior failure cited as rationale for studying SMOKIs in sarcoma — provides indirect supportive context for the sarcoma TKI class |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 Clinical Trial | Int J Cancer | Sunitinib in relapsed/refractory STS with focus on leiomyosarcoma, liposarcoma, and MFH; reports safety, efficacy, and clinical activity of multi-targeted TKI in these common subtypes |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Comprehensive review of genetic, epigenetic, and transcriptomic alterations in liposarcoma; identifies VEGFR/PDGFR pathway as actionable targets relevant to sunitinib's mechanism |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | Emerging therapies for adult STS; discusses histology-specific TKI use including sunitinib and pazopanib in second-line and beyond settings |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven treatment strategy in STS; summarizes evidence for TKI activity (including sunitinib) across sarcoma subtypes, distinguishing subtype-specific response patterns |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Subtype-stratified medical treatment of adult STS; covers both cytotoxic and targeted agents; contextualizes sunitinib alongside other TKIs |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case Report | Anticancer Res | Long-lasting clinical benefit documented in a heavily pre-treated patient with metastatic liposarcoma receiving sunitinib; supports direct disease-specific efficacy |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Genomic Study | Oncotarget | NGS profiling of extraskeletal myxoid chondrosarcoma; evaluates actionable mutations and molecular predictors of sunitinib benefit in translocation-associated sarcomas |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study Protocol | BMC Cancer | REGOSARC trial protocol for regorafenib in advanced STS; explicitly cites sunitinib's established activity in STS as part of the scientific rationale |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Clinicopathologic Analysis | Am J Surg Pathol | Characterization of myxoid inflammatory myofibroblastic sarcoma; provides updated molecular landscape and targetable alteration context within the broader sarcoma field |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multi-targeted receptor tyrosine kinase inhibitor (TKI); not conventional cytotoxic |
| Myelosuppression Risk | Moderate — neutropenia (Grade 3/4 reported in ~10–12% of patients) and thrombocytopenia are well-established class effects; dose modification frequently required |
| Emetogenicity Classification | Low to moderate (oral agent; nausea reported but high-grade emesis uncommon) |
| Monitoring Items | CBC with differential (every cycle), liver function (AST/ALT/bilirubin), renal function (creatinine), thyroid function (TSH), blood pressure, cardiac function (LVEF/echocardiogram at baseline and periodically), electrolytes |
| Handling Protection | Standard oral cytotoxic precautions apply; follow institutional cytotoxic handling guidelines for preparation and disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Taiwan package insert data (TFDA) was not retrieved during evidence collection. Detailed contraindications and warnings for the Taiwan-specific label remain unverified. This is a **blocking data gap** that must be resolved before clinical recommendation is finalized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two directly relevant completed Phase 2 trials enrolled soft tissue sarcoma patients explicitly including liposarcoma and tested sunitinib with Grade A relevance; a published Phase 2 study (Mahmood et al., 2011) further documents clinical activity in liposarcoma specifically, and the PDGFR-α/β dual-inhibition mechanism provides strong biological plausibility. However, no Phase 3 RCT exists for this indication and subtype-specific response data remain limited, warranting guardrails.

**To proceed, the following is needed:**

- **Taiwan package insert (TFDA)** — resolve the blocking data gap on contraindications and key warnings before S1 safety screening
- **Mechanism of action data** from DrugBank — to formally document MOA linkage for regulatory and clinical review files
- **Histological subtype stratification** — response to sunitinib appears to vary across liposarcoma subtypes (well-differentiated/dedifferentiated vs. myxoid/round cell); subtype-specific patient selection criteria should be defined
- **Drug-drug interaction assessment** — currently no DDI data is available; critical for polypharmacy patients
- **Formal pharmacokinetic evaluation** in the target Taiwanese patient population, especially for any renal/hepatic impairment adjustments
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

