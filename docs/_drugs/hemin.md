---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Hemin
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

以下是根據 Evidence Pack 產生的完整報告：

---

# HEMIN: From Acute Hepatic Porphyria to Thrombocytopenic Purpura

## One-Sentence Summary

HEMIN 是一種靜脈注射用鐵-卟啉化合物，於國際上確立用於治療急性肝卟啉症（Acute Hepatic Porphyria, AHP）的急性發作，透過補充外源性血紅素抑制肝臟 ALAS1 過度活化。TxGNN 模型預測其可能對 **Thrombocytopenic Purpura（血小板減少性紫癜）** 有效，然而目前 **0 項臨床試驗** 及 **0 篇文獻** 支持此方向，預測僅基於計算模型推斷（證據等級 L5）。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Hepatic Porphyria（急性肝卟啉症，國際已核准適應症；Taiwan 無登錄紀錄） |
| Predicted New Indication | Thrombocytopenic Purpura（血小板減少性紫癜） |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

目前 Evidence Pack 中缺乏詳細的作用機轉資料。根據已知資訊，HEMIN 為含鐵卟啉化合物，其主要藥理作用為補充外源性血紅素，從而透過負回饋機制抑制肝臟 ALAS1（delta-aminolevulinic acid synthase 1）的過度表現——這正是 AHP 急性發作的病理核心。此外，HEMIN 亦可誘導血紅素加氧酶-1（Heme Oxygenase-1, HO-1）的表現，HO-1 具有強效抗炎及免疫調節活性，為其次要但重要的機轉。

血小板減少性紫癜（ITP）的核心病理為自體免疫介導的血小板破壞。理論上，HO-1 的誘導可能抑制 ITP 中的抗血小板自體免疫反應，為 TxGNN 預測提供了一定的生物學概念基礎。圖神經網路可能透過知識圖譜中「血液疾病 → 免疫調節 → HEMIN/HO-1」的節點關聯推導出此預測。

然而，此預測存在**關鍵機制矛盾**：HEMIN 本身亦已知具有抑制血小板聚集及損害血小板功能的效果。對於本已以血小板數量不足為核心問題的 ITP 患者，HEMIN 的抗血小板特性可能加劇疾病，而非改善。此機制層面的自相矛盾，加上完全缺乏臨床試驗與文獻佐證，使此預測的可行性存疑，不建議立即進入開發流程。

---

## Clinical Trial Evidence

目前無相關臨床試驗登錄紀錄。

---

## Literature Evidence

目前無相關文獻可供參考。

---

## Safety Considerations

請參閱仿單之警語與注意事項以取得完整安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
此預測完全基於圖神經網路計算推斷（L5 等級），無任何臨床試驗或文獻支持 HEMIN 用於血小板減少性紫癜；且 HEMIN 已知的抗血小板特性在機制層面與 ITP 治療需求形成直接矛盾，存在潛在安全性疑慮。

**To proceed, the following is needed:**
- 補充 HEMIN 的完整作用機轉資料（MOA，目前為 Data Gap，需查詢 DrugBank API）
- 取得 Taiwan TFDA 仿單 PDF 以完成安全性初評（目前為 Blocking 等級資料缺口）
- 進行臨床前研究，釐清 HO-1 誘導對 ITP 動物模型中自體免疫反應及血小板數量的淨效應，以化解機制矛盾
- 若資源有限，建議優先評估 **Rank #2 適應症（Hemophilia）**：已有動物實驗文獻（PMID 19890094）支持 HO-1 誘導可降低 FVIII 替代療法的免疫反應，機制相對清楚且無同等矛盾，為更具開發潛力的切入點
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

