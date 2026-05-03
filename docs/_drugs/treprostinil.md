---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

The txgnn-pipeline skill confirms this is within the TxGNN ecosystem. Now I have everything I need — let me generate the full evaluation report.

---

# Treprostinil: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Treprostinil is a synthetic prostacyclin analogue with established global approval for pulmonary arterial hypertension (PAH), acting as a potent pulmonary vasodilator and antiproliferative agent in pulmonary vessel walls.
The TxGNN model assigns a prediction score of **99.70%** for **Pulmonary Arteriovenous Malformation (PAVM)** as the top-ranked new indication, yet this specific indication is supported by **0 clinical trials** and **0 publications** — and mechanistic analysis raises a direct concern that vasodilation may worsen the characteristic right-to-left shunting seen in PAVM.
Notably, other PAH subtypes appearing in the same prediction set — particularly PAH associated with connective tissue disease (L2 evidence, direct treprostinil clinical data) and PAH associated with congenital heart disease (L3 evidence) — represent substantially more credible repurposing targets warranting separate evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) — not registered in Sweden; established global approval |
| Predicted New Indication | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Sweden Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data source. Based on established clinical and pharmacological knowledge, treprostinil is a tricyclic benzindene prostacyclin analogue that acts primarily through IP (prostacyclin) receptor agonism. This drives pulmonary and systemic vasodilation, inhibits platelet aggregation, and suppresses smooth muscle cell proliferation within pulmonary vessel walls. These effects underpin its proven efficacy in idiopathic PAH, where increased pulmonary vascular resistance is the core pathology.

Pulmonary arteriovenous malformation (PAVM) is, however, a structurally distinct disease: abnormal direct connections between pulmonary arteries and veins bypass the pulmonary capillary bed, creating persistent right-to-left intrapulmonary shunts. The disease mechanism is anatomical — not vasoconstrictive — and first-line management is interventional (transcatheter coil or vascular plug embolotherapy), not pharmacological vasodilation. Applying a vasodilator such as treprostinil in PAVM lacks physiological rationale, and systemic vasodilation could theoretically increase shunt fraction, worsening hypoxemia and paradoxical embolism risk rather than improving them.

The TxGNN high score (99.70%, model internal rank #906) most likely reflects the close proximity of the PAVM and PAH disease nodes within the underlying biological knowledge graph — both conditions involve abnormal pulmonary vasculature. This is a characteristic graph-propagation artifact, not a mechanistically verified therapeutic link. For PAVM specifically, this prediction should be treated as a model false positive. The more clinically credible repurposing signals from this same dataset — PAH associated with connective tissue disease (rank #4, L2 evidence, direct subcutaneous treprostinil clinical studies from 2002–2024) and PAH associated with congenital heart disease (rank #2, L3 evidence) — merit prioritized independent evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Pulmonary Arteriovenous Malformation.

---

## Literature Evidence

Currently no related literature available for Pulmonary Arteriovenous Malformation.

---

## Sweden Market Information

Treprostinil has no authorized products in Sweden. Zero marketing authorizations are on record, and the drug is not available under any brand name in the Swedish market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's highest-ranked prediction for treprostinil — pulmonary arteriovenous malformation — achieves a high score due to disease-node proximity in the knowledge graph, but is mechanistically contraindicated: PAVM is a structural shunt disorder where prostacyclin-mediated vasodilation may actively worsen right-to-left shunting and hypoxemia, and there is no clinical trial or published literature evidence to suggest otherwise.

**To proceed or redirect, the following is needed:**

- **For PAVM specifically:** Preclinical studies examining the hemodynamic effect of IP receptor agonism in PAVM animal models or patient subgroups with co-existing pulmonary hypertension — currently absent. Without this, no clinical advancement is justified.
- **Higher-priority alternatives within this Evidence Pack:** The following predictions from the same dataset should each receive a dedicated evaluation report, as they carry substantially stronger mechanistic and clinical support:
  - **PAH associated with connective tissue disease** (rank #4, L2 evidence): Direct subcutaneous treprostinil trials in CTD-PAH exist from 2002 onward (PMID 11897647, 15302727); 2024 meta-analysis confirms efficacy. Decision likely: *Proceed with Guardrails*.
  - **PAH associated with congenital heart disease** (rank #2, L3 evidence): Observational data and a terminated Phase 2 treprostinil trial in neonates; prostacyclin analogues used in CHD-PAH adults. Decision likely: *Proceed with Guardrails* with monitoring for shunt risk.
  - **PAH associated with HIV infection** (rank #3, L3 evidence): Mechanistically plausible (HIV-mediated prostacyclin synthase suppression); a terminated Phase 4 trial exists; DDI risk with antiretrovirals requires evaluation. Decision: *Research Question*.
- **Regulatory pathway for Sweden:** With zero Swedish authorizations, any advancement requires a formal European/Swedish MPA registration strategy in parallel with clinical evidence generation.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

