# SETxGNN 維護說明

各站共通的維護流程見母 repo（yao-care/txgnn）的 CLAUDE.md；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）；
UsTxGNN 是第一個試做站（做法見 UsTxGNN/CLAUDE.md 同名一節）。本站的規則與程式都在本 repo，頁面文字用瑞典文，依據是Läkemedelsverket 的許可資料。
本站的在地字樣、頁首規則細節、歷史刪改的提交清單集中在 `src/setxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁在免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/setxgnn/regulatory/page_format.py` | 頁首＝快速總覽「Evidensnivå」格的**第一個**等級（主預測）。2026-11-12 實測 442 頁有總覽等級，頁首全部符合（0 頁例外），所以照實寫成程式、不改現有等級；Tw 是整格取最高，本站不同。頁首已是 N/A 的頁（已知用途／沒有保留預測）不依總覽格重算 |
| 撤回預測 | `src/setxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/se_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/setxgnn/regulatory/licenses.py` | 快照存本藥許可證號與事實層；gate 依快照驗市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反（本站沒有程式產生的許可證表，不驗表格列內容） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證與待重審項目；證據包沒有許可證適應症文字時照實回報可比對 0 頁 |
| gate | `scripts/check_seo_docs.py` 最後 4 項 | 紀錄都已套用、許可證＝快照、頁首＝快速總覽等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依新事實直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 466 筆紀錄（261 頁）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁後會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。

2026-11-12 表格列狀態對事實層（母目錄 `check_drug_page.py --row-status`）：99 頁 272 列以 `se-row-20261112-*`（每頁一筆）更正——271 列 Läkemedelsverket 註冊狀態 Godkänd 的許可在表格寫成 indraget／indragen／avregistrerad／återkallat（其中 73 列是核准但目前未販售，仍不是撤回），febuxostat 56645 反向（Avregistrerad 寫成 godkänd）。
事實層先抽 35 列對照證據包原始狀態與 lmv_registreringsstatus.json（2026-11-02），全部一致。只改狀態字：Status 欄改「Godkänd」、適應症欄去掉狀態註記（整格只有狀態字的改「Ej angiven」）。`scripts/apply_drug_reviews.py` 的 display 改成多列表格原句逐列顯示。
