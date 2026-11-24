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
| 許可證 | `scripts/sync_license_tables.py`（程式表前後有 `<!-- licenses:begin/end -->`，2026-11-24 起）、`snapshots/se_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/setxgnn/regulatory/licenses.py` | 快照存本藥許可證號、事實層、程式表列；gate 依快照驗程式區塊、市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反 |
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

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 68 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Någon detaljerad verkningsmekanismdata finns för närvarande inte tillgänglig.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `se-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（svenska）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：57 頁寫入紀錄（美國仿單 53、ChEMBL 4），8 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 4 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 2 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）2 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Ursprunglig indikation: Inte angiven i de lokala uppgifterna」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：Läkemedelsverket 許可。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abacavir「Ursprunglig indikation: Inte angiven i de lokala uppgifterna」→「I Sverige, godkännanden (Läkemedelsverket): 5 (giltiga: 4)」；2026-11-19 改了 384 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site SETxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式維護（2026-11-24）

用戶 2026-11-24 決定（各站同日；本站做 A＋B）：每週許可證排程只改得到概覽表狀態列／張數列，AI 寫在「Marknadsinformation Sverige」的自由格式許可證表
（號碼格「(indraget)」、indikation 欄全是「Ingen indikationstext registrerad」；11-12 以 99 筆 `se-row-20261112-*` 人工更正 272 列）與正文張數句會跟著 Läkemedelsverket 資料過期、讓 checker 擋整頁；改成程式產生、每週自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py` 依證據包 tfda.records（＋`config/license_own_extra.json` 的人工補收號碼，febuxostat 的 Feburo 55201／55202；該檔另記 form、registreringsstatus、holder）產生
  「| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |」，欄位照 Läkemedelsverket 原文（Status＝Registreringsstatus 原文：Godkänd、Registrerad、Avregistrerad、Tillfälligt återkallad；核准但未販售仍是 Godkänd）。
  選列照換表當時報告原表依序列出的號碼與列數（`config/license_table_pins.json`，447 頁；正文常寫「De fem första」「Tillverkare: …」「Båda godkännandena …」，換成別的列會對不上；febuxostat 的 n 改 3 列出 Feburo），
  其餘依程式排序（有效在前、單方在前、號碼）；原本沒有表的頁 min(5, 總數) 列。總數多於列數時表下「Tabellen visar N av M godkännanden i uppgifterna.」（partial 頁「… av minst M …; listan kan vara ofullständig.」），再一行來源句；沒有紀錄時一句 NONE_LINE。
  持有人名稱照 Läkemedelsverket 原文（第一輪曾把公司型態「KG」寫成「Kommanditgesellschaft」，第二輪母目錄 checker P5 加公司名 KG 豁免（295dd578）後改回原文，10 頁）。
  快照另存 rows／total／partial_rows；gate 第 18 項（licenses.py → sync_license_tables.block_problems）整塊比對、擋市場段落裡程式區塊以外的表。`config/license_own_extra.json` 的號碼也算進快照 own。
  接上：`scripts/license_adapter.py` 的 `sync_tables`（每週排程，--bundles 全站比對、只寫有變的）與 `PAGE_NOTE`、`apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾（不給 --ws 時沿用現有快照的 facts）、`sync_notes_to_docs.py`（carry_block）。
- B. 正文張數改寫：`scripts/rewrite_license_counts.py`＋`src/setxgnn/regulatory/count_prose.py`（移植 Kr／My／DE，瑞典文句型：「N giltiga godkännanden (av M)」「N av M godkännanden är giltiga」「Av M … är N giltiga och C avregistrerade」
  「Totalt finns N godkännanden, varav V är giltiga」「alla N godkännanden」、två～tolv）；有保留、相對數（ytterligare／övriga／fler／till）、劑型或單方／複方子集、廠商、點名許可證號、講表上筆數的句子、partial 頁不動；
  0／1、båda、en／ett 的改動（單複數與形容詞變化）、「alla／samtliga … giltiga」而事實不符、同句有試驗／交互作用等字樣而數字不符的不改、列待查。不寫查核框；gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 套用（資料 data-20261123-163507）：程式表 454 頁（447 頁 AI 表換掉、7 頁補在標題下；公開頁有市場段落的全部有程式表，5 個公開頁與 26 個 noindex 頁沒有市場段落、不加）；緊接舊表只講表上筆數的說明句拿掉 12 句（由程式說明句取代）。
  錨在舊表列上的 99 筆 `se-row-20261112-*` 標 superseded。正文張數程式改寫 0 句（現行正文張數都跟事實層一致）。
  正文單方說法依證據包成分欄不成立的 8 句以 `se-lic-20261124-*` 更正（articaine、imipenem 全部是複方；bendroflumethiazide、bupivacaine、cyanocobalamin、dexamethasone、dipyridamole、thiamine 有複方），更正文字不寫張數。
  紀錄說明句裡寫死的「Antal godkännanden enligt uppgifterna: N, varav giltiga: V」（site.FIGURES，365 筆，其中 5 筆已跟現行事實不符）改成指向概覽表與程式表，同 id 重發、前版存 history；site.FIGURES 也改成不寫數字。
  另寫的寬偵測（同句有許可字樣與數字或全稱／否定狀態字樣、跟事實層不符）全量掃 110 句→57 句，剩下多是「en／ett」冠詞誤中與講表上 5 筆（仍＝程式表列數）；真正跟事實相反的 12 句（famciclovir、gemcitabine、hydroxyzine 的待辦或決策條目寫「全部撤回／沒有有效許可」、sulbactam、partial 頁 8 句）列進待查清單，沒改。
  checker 全量前後都是 0；gate exit 0；改到的 458 頁 last_modified_at 改 2026-11-24。
- 母目錄 `.claude/license_labels/SETxGNN.json` 目前只有 valid 寫法，程式表會寫的 Avregistrerad、Tillfälligt återkallad（cancelled）、Registrerad（valid）還沒有（要在母目錄加）。

## 許可證狀態錯句逐句更正（2026-11-24 第二輪）

用戶 2026-11-24 第二輪決定：第一輪列進待查的舊錯句逐句寫查核紀錄、劑型說法全站掃。
- 待查清單 12 句（famciclovir、gemcitabine、hydroxyzine、sulbactam、tacrolimus、xylometazoline 寫許可已撤回或沒有有效許可；glycine、sertraline、budesonide、ebastine、ethanol×2 是 partial 頁寫死「20 張有效」而收到的紀錄有 Avregistrerad）逐句對照證據包後全部更正，待查項目標 resolved（附 record_ids）。
- 照「找到一個錯就查同類」另寫寬偵測（indragen／indragna／dragits in／återkallad／upphävd／saknas giltig／inga aktiva／inte längre giltig／tidigare godkända…，跟事實層有效張數比）全量掃公開頁，第一輪的寬偵測漏了大量「Dessutom saknas giltiga godkännanden i Sverige」「Klargöra varför godkännandena dragits in」寫法（11 月 AI 重產時照證據包錯誤狀態寫的）：
  合計 78 句以 `se-lic-20261124b-*` 更正（69 頁：決策理由裡的錯誤子句刪掉、待辦條目只拿掉錯的前提、整條建立在錯誤前提上的 4 條（3 條待辦、1 條決策理由）刪除、把現行許可寫成「tidigare」的 9 句拿掉時間詞），更正文字不寫張數；
  更正文字本身錯的 2 筆同 id 重發（`se-lic-20261106-pioglitazone-1`「目前沒有有效上市產品」、`se-lic-20261106-prilocaine-3`「bland de tidigare godkännandena」，前版存 history）。
  複掃剩下的都成立（全部有效的「alla N giltiga」、有實際 Avregistrerad 的句子、別國撤市、試驗撤回）；partial 頁收到的 20 張全部有效、正文寫「20 giltiga」的 9 句跟概覽表「minst 20」一致，不改。
- 劑型說法（「Beredningsformen är …」「Samtliga produkter är …」「endast oral tablett」等 58 句）逐句對照證據包全部品項的劑型（partial 頁另對 data/raw 的 Läkemedelsverket 全量清單）：只有 isoleucine「alla … infusionsvätskor」漏了證據包裡的腹膜透析液，併在上面的紀錄更正；其餘成立、不改。
- 紀錄說明的張數樣板（site.FIGURES）第一輪已改成不寫數字，確認現行紀錄沒有寫死張數的說明。
- checker 全量前後都是 0；gate exit 0。
- 同日母 repo checker 把上面這些 sv 否定／撤回前提句型加進 M3（`sv_neg_x`，另成一組）：用 ebdef401 前的頁面反向驗證，78 句裡抓到 71 句（漏的 7 句是 partial 頁寫死「20 giltiga」等張數句，不屬否定句型；同 id 重發的 prilocaine 也抓得到），另抓到第二輪寬偵測漏掉的 2 句「Dessutom saknas aktiva godkännanden i Sverige」（propofol、ramipril），以 `se-lic-20261124c-*` 更正；改後 checker 全量 0、gate exit 0。
