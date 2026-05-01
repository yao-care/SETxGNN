---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to orient context, and now proceeding to generate the evaluation report from the Evidence Pack.

---

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a synthetic progestogen, the active ingredient of the subdermal contraceptive implant (Implanon/Nexplanon), primarily used for long-term reversible contraception.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **1 clinical trial** and **1 relevant publication** currently retrieved in support.
However, this prediction carries a critical structural flaw: amenorrhea is a well-documented **side effect** of etonogestrel rather than a condition it treats — the causal relationship is reversed, and the prediction score likely reflects co-occurrence in the knowledge graph rather than genuine therapeutic potential.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception (subdermal implant) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, etonogestrel is 3-ketodesogestrel — the active metabolite of desogestrel — a potent synthetic progestogen that suppresses ovulation by inhibiting the hypothalamic-pituitary-ovarian (HPO) axis, preventing LH surge and follicular maturation. This is the mechanism underlying its contraceptive efficacy as a subdermal implant lasting up to 3–5 years.

The high TxGNN score (99.84%) almost certainly reflects the strong **co-occurrence** of etonogestrel and amenorrhea in biomedical literature and knowledge graphs, not a therapeutic relationship. Etonogestrel implants are known to induce amenorrhea in approximately 20–30% of users, making it one of the most frequently documented implant-related bleeding changes. The knowledge graph edge is real — but its direction is "drug **causes** amenorrhea," not "drug **treats** amenorrhea."

Pathological amenorrhea typically requires restoration of the menstrual cycle (e.g., treating hypothalamic dysfunction, correcting hormonal deficiencies). Etonogestrel's mechanism — sustained HPO axis suppression — would **deepen** amenorrhea, not reverse it. This represents a **causal directionality reversal**, a known failure mode in graph-based repurposing models where side effects are misclassified as indications. Without correcting for this directional bias in the knowledge graph, the prediction is not clinically actionable as a repurposing candidate for amenorrhea treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Extended contraceptive use (year 4–5) of the etonogestrel implant; primary endpoint was contraceptive efficacy (Pearl Index). Amenorrhea was captured only as a **secondary bleeding-pattern endpoint**, not as a treatment target. Trial design does not support an "amenorrhea treatment" indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Implanon (etonogestrel) vs Norplant (levonorgestrel) over 2–4 years in 200 women: zero pregnancies in both groups. Bleeding patterns including amenorrhea were documented per 90-day reference period as **side effect outcomes**, not therapeutic endpoints. |

> **Note:** A second retrieved article (PMID [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/)) describes an RCT of BIO101 (an unrelated compound) for COVID-19 pneumonia and has no connection to etonogestrel or amenorrhea. It has been excluded.

---

## Taiwan Market Information

Etonogestrel is **not currently marketed in Taiwan**. The TFDA database returned zero authorization records (查詢日期：2026-03-29). No product licenses, dosage forms, or approved indication texts are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> TFDA package insert was located (query returned 1 result on 2026-03-29) but warnings and contraindications data were not parsed into this Evidence Pack. Full package insert review is required before any clinical decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for etonogestrel in amenorrhea is assessed as a **causal direction reversal artifact** — the knowledge graph captures etonogestrel as an inducer of amenorrhea (HPO axis suppression), not as a treatment for it. The single supporting trial (NCT04626596) was designed to assess contraceptive efficacy, and the only relevant literature documents amenorrhea as a side effect outcome. There is no mechanistic or clinical basis to pursue this repurposing direction without first resolving this directional ambiguity.

**To proceed, the following is needed:**

- **Resolve causal directionality:** Confirm whether the TxGNN knowledge graph distinguishes "drug → causes disease" from "drug → treats disease" edges; if not, this entire class of HPO-suppression predictions requires systematic review
- **MOA data:** Obtain etonogestrel pharmacology from DrugBank API to formally document the HPO axis suppression mechanism
- **Safety review:** Parse TFDA package insert (already located) to extract contraindications and key warnings
- **Reframe indication scope:** If progesterone-induced amenorrhea has intentional clinical use (e.g., endometriosis, heavy menstrual bleeding, hormone therapy), reframe the repurposing hypothesis under those indications with dedicated evidence collection — the current "amenorrhea (disease)" framing is directionally inappropriate
---

