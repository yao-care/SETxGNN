---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 1
---

# Estriol
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

Using `txgnn-pipeline` skill noted — this is a TxGNN Se/Tw multi-country report. Now generating the report from the Evidence Pack.

---

# Estriol: From Menopausal Hormone Therapy to Amenorrhea

## One-Sentence Summary

Estriol (E3) is a weak, naturally occurring estrogen with established pharmacological use in menopausal hormone therapy for symptoms of estrogen deficiency including genitourinary atrophy and vasomotor symptoms.
The TxGNN model predicts it may be effective for **Amenorrhea** — particularly functional hypothalamic amenorrhea (FHA) and premature ovarian insufficiency (POI) —
with **3 clinical trials** retrieved and **13 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in this regulatory database |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L2 |
| Sweden Market Status | ✗ Not marketed (0 authorizations found) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, estriol (E3) is the weakest of the three major human endogenous estrogens — alongside estradiol (E2) and estrone (E1). It binds estrogen receptors ERα and ERβ in the hypothalamus and anterior pituitary, where it participates in feedback regulation of the GnRH–LH–FSH reproductive axis.

Functional hypothalamic amenorrhea (FHA) arises from suppressed pulsatile GnRH secretion, typically triggered by psychosocial stress, excessive exercise, or low energy availability. This suppression cascades into reduced LH and FSH release, causing ovarian hypoestrogenia and cessation of menstruation. In this context, estriol is mechanistically positioned to restore hypothalamic–pituitary feedback and partially reactivate the reproductive axis. PMID 22137494 directly demonstrated that estriol administration modulates LH secretion in FHA patients, providing clinical proof of concept for this precise mechanism.

Compared with estradiol (E2), estriol's lower intrinsic estrogenic potency is an advantage in the amenorrhea setting: it provides sufficient hypothalamic receptor stimulation to modulate GnRH feedback while substantially reducing the risk of endometrial hyperplasia and breast tissue proliferation that would concern clinicians treating young women with FHA or premature ovarian insufficiency (POI). A 2023 review (PMID 37371858) corroborates this, describing low-dose estrogens as neuroendocrine modulators capable of triggering positive feedback mechanisms in the hypothalamic–pituitary unit in FHA patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn | 0 | Investigated photobiomodulation for vulvovaginal atrophy in postmenopausal women, whose menopause was defined as 12 months of amenorrhea. Study was withdrawn before enrolling any participants — provides no usable efficacy evidence. |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1,570 | Estetrol (E4) 15 or 20 mg vs. placebo for vasomotor symptoms in postmenopausal women (E4Comfort Study I). Large, completed RCT establishing estrogen-replacement benefit in hypoestrogenic states; indirect evidence for the estrogen–hypothalamic axis, though the study drug is estetrol (E4), not estriol (E3). |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1,015 | Estetrol (E4) 15 or 20 mg vs. placebo for vasomotor symptoms in postmenopausal women (E4Comfort Study II). Companion trial to NCT04209543; same mechanistic context applies. |

> **Important caveat:** NCT04209543 and NCT04090957 investigate **estetrol (E4)**, a structurally distinct estrogen from estriol (E3), for vasomotor symptoms rather than amenorrhea. They provide contextual evidence on estrogen-replacement in hypoestrogenic conditions but are **not** direct evidence for estriol in amenorrhea. No completed trial of estriol specifically targeting FHA or POI-related amenorrhea was identified in this search.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Clinical Study | Fertility and Sterility | **Most directly relevant.** Estriol administration modulates LH secretion in women with functional hypothalamic amenorrhea (FHA) — direct clinical evidence linking estriol to the GnRH–LH axis disruption that defines this indication. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Low-dose estrogens as neuroendocrine modulators in FHA; reviews evidence that low-dose estrogens can restore positive GnRH feedback — supports mechanistic rationale for using weak estrogens (including E3) in FHA management. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Clinical Trial | Medicinski Pregled | Effects of estro-progestagen therapy on lipid and hormonal profiles in women with premature primary ovarian failure (hypergonadotropic amenorrhea); supports estrogen replacement as standard management for POI-related amenorrhea. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case Report | Lancet | Endocrinological findings in two patients with premature ovarian failure — early clinical description of the hormonal profile (hypergonadotropic hypoestrogenia) that characterises a major subset of amenorrhea. |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Clinical Trial | J Obstet Gynaecol Br Commonw | Clinical trial of pituitary and urinary FSH plus chorionic gonadotrophin in idiopathic secondary amenorrhea — historical controlled study on hormonal intervention in secondary amenorrhea; establishes the gonadotrophin-amenorrhea therapeutic axis. |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | Clinical Obstetrics and Gynecology | Neoplasia and hormonal contraception — background review on long-term estrogen safety relevant to risk assessment for prolonged estriol use in amenorrhea treatment. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Review | British Journal of Psychiatry | Anorexia nervosa — clinically relevant as anorexia nervosa is a prototypical cause of FHA through hypothalamic GnRH suppression; contextualises the psychosomatic pathway to amenorrhea. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observational | Chinese J Modern Developments Trad Med | Observations on gonadal function changes in women with amenorrhea and oligomenorrhea — observational hormonal data from a distinct patient population, broadening the clinical picture of amenorrhea pathophysiology. |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Cohort | Am J Obstet Gynecol | Prolonged gynecologic and endocrine effects following medroxyprogesterone acetate administration during pregnancy — historical cohort providing context on progestogen-induced secondary amenorrhea and hormonal recovery. |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Study | J Clin Endocrinol Metab | Mechanism of action of anti-ovulatory compounds — foundational mechanistic study on how estrogens modulate the hypothalamic–pituitary reproductive axis, underpinning the pharmacological basis of this repurposing hypothesis. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
PMID 22137494 provides direct clinical evidence that estriol modulates LH secretion in functional hypothalamic amenorrhea, and the pharmacological mechanism (hypothalamic–pituitary ERα/ERβ feedback modulation) is well-grounded in endocrinology. However, no dedicated Phase 2/3 RCT of estriol specifically targeting amenorrhea was identified — the two completed Phase 3 trials in this pack involve estetrol (a different estrogen) for vasomotor symptoms, providing only indirect contextual support. The evidence is promising but insufficient on its own for regulatory progression.

**To proceed, the following is needed:**
- Full MOA data from DrugBank (data gap DG002) to formalise the mechanistic rationale in regulatory dossiers
- Sweden/Taiwan package insert safety data including contraindications and key warnings (data gap DG001) — essential for S1 safety screening
- At least one dedicated clinical trial of estriol (E3) in FHA or POI-related amenorrhea, or a systematic review pooling existing estriol studies
- Drug–drug interaction profile for estriol (DDI query returned no results — requires manual review of reference sources)
- Verification of Sweden market status against the Swedish Medical Products Agency (MPA) database, as estriol products (e.g., Ovestin) are known to exist in European markets but returned 0 hits in the current query
- Dose-optimisation data: the optimal estriol dose for hypothalamic feedback modulation in amenorrhea may differ substantially from doses used in menopausal indications
---

