---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a selective inhibitor of influenza virus neuraminidase, indicated for the treatment and prevention of influenza A and B.
The TxGNN model predicts it may be effective for **Pyelonephritis**,
however **no clinical trials** and **no supporting publications** exist for this direction, and the mechanistic rationale is considered implausible — this prediction is likely a false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Influenza A and B (treatment and prophylaxis) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Sweden Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacological information, Zanamivir is a selective inhibitor of influenza virus neuraminidase (NA), a surface glycoprotein essential for releasing newly formed viral particles from infected host cells. By blocking this enzyme, zanamivir prevents viral spread and reduces the duration and severity of influenza A and B infections.

Pyelonephritis is an acute bacterial upper urinary tract infection, most commonly caused by *Escherichia coli* ascending from the lower urinary tract. There is no established mechanistic overlap between influenza virus neuraminidase inhibition and bacterial renal parenchymal infections. The pathogen class (virus vs. bacterium), the molecular drug target (viral surface glycoprotein vs. bacterial cell wall or metabolic enzymes), and the therapeutic strategies are entirely distinct domains.

The high TxGNN score (99.84%) is most likely a false positive. Graph neural networks may detect indirect connections in biological knowledge graphs — for example, shared immune response pathways or inflammation-related nodes that are activated in both viral respiratory infections and bacterial urinary tract infections — but such network proximity does not imply a therapeutic relationship. This prediction should be treated as a model artifact requiring human expert review rather than as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Sweden Market Information

Zanamivir currently holds no marketing authorizations in Sweden (MPA). The drug has not been approved or marketed through the Swedish regulatory pathway at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is classified as L5 — model output only, with zero supporting clinical trials and zero supporting publications. More critically, the mechanistic link between zanamivir (a virus-specific neuraminidase inhibitor) and pyelonephritis (a bacterial kidney infection) is biologically implausible; the TxGNN prediction is assessed as a likely false positive arising from shared immune/inflammatory network nodes in the knowledge graph.

**To proceed, the following is needed:**
- Formal false-positive classification and feedback to the TxGNN model for calibration purposes
- Independent mechanistic review to determine whether any off-target antibacterial activity of zanamivir has ever been reported in preclinical literature
- If any indirect biological plausibility is identified (e.g., influenza-associated secondary bacterial pyelonephritis), targeted preclinical studies would be required before considering further development
- Completion of MOA data gap (DG002) and TFDA package insert retrieval (DG001) to support any future full safety assessment
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

