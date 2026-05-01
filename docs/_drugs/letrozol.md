---
layout: default
title: Letrozol
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Letrozol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# LETROZOL：藥物再利用評估 — 證據包資料不足，無法完成完整評估

## One-Sentence Summary

LETROZOL 的 Evidence Pack 中，原始適應症、TxGNN 預測適應症及安全性資料均未成功填入。目前資料不足以支撐完整的老藥新用評估，建議在補齊關鍵缺口後再行重新評估。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 未填入（Evidence Pack 欄位為空） |
| Predicted New Indication | 無（`predicted_indications` 陣列為空） |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — 無模型預測輸出 |
| Taiwan Market Status | 未上市（授權數：0） |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

本 Evidence Pack 的 `predicted_indications` 欄位為空陣列，代表 TxGNN 模型尚未針對 LETROZOL 產生任何預測輸出，或預測結果未被成功寫入。沒有目標適應症，無法進行機轉關聯性分析。

從 Query Log 可發現矛盾現象：DrugBank 查詢狀態為 `success`（`result_count: 1`），TFDA 仿單查詢同樣為 `success`（`result_count: 1`），但這兩個成功的來源資料均未被解析並填入 `drug` 或 `safety` 欄位。這強烈指向資料管線（pipeline）的上游存在資料轉換或寫入的問題。

此外，`taiwan_regulatory.market_status` 標示為「未上市」，但 TFDA 仿單查詢竟有 1 筆結果，此一矛盾需在後續步驟中澄清。

---

## Query Log 現況摘要

| # | 來源 | 查詢日期 | 狀態 | 結果數 | 備註 |
|---|------|---------|------|--------|------|
| 1 | TFDA | 2026-03-29 | success | 0 | 核准資料查無結果 |
| 2 | DDI | 2026-03-29 | not_found | 0 | 藥物交互作用無資料 |
| 3 | DrugBank | 2026-03-29 | success | **1** | 資料未填入 drug 欄位 ⚠️ |
| 4 | TFDA 仿單 | 2026-03-29 | success | **1** | 資料未填入 safety 欄位 ⚠️ |

---

## Safety Considerations

請參閱藥品仿單的警語與禁忌事項。（安全性資料未從已成功查詢的 TFDA 仿單中解析填入。）

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence Pack 缺少全部關鍵輸入：原始適應症、TxGNN 預測結果、作用機轉（MOA）及安全性資料均為空值或 Data Gap。在這些欄位補齊之前，無法進行任何老藥新用候選評估。

**To proceed, the following is needed:**

1. **修復資料管線**：DrugBank 查詢（Query #3）和 TFDA 仿單查詢（Query #4）均已成功取得 1 筆資料，但結果未寫入 Evidence Pack；需檢查解析器（parser）的資料轉換邏輯
2. **填入 `drug.original_indications`**：從 DrugBank 資料解析已核准適應症
3. **填入 `drug.original_moa`**：從 DrugBank pharmacology 欄位提取作用機轉
4. **執行 TxGNN 模型**：為 LETROZOL 生成 `predicted_indications` 輸出
5. **解析 TFDA 仿單**：從已成功取得的仿單中，提取 `safety.key_warnings` 與 `safety.contraindications`
6. **澄清台灣市場狀態矛盾**：TFDA 仿單查詢有結果，但 `market_status` 標示「未上市」，需確認是否因藥名拼寫差異（LETROZOL vs. LETROZOLE）導致查詢對象不一致
---

