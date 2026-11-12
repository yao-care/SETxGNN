"""本站查核機制的在地設定（SETxGNN，瑞典文；2026-11-12 建）。

程式（page_format、licenses、withdrawn、scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py）的核心流程比照 TwTxGNN／UsTxGNN，本站的字樣、規則細節、提交清單集中在這裡。
"""
import re

SITE = "SETxGNN"
CODE = "se"

# ---- 頁首等級（page_format）----
OVERVIEW_LEVEL_LABELS = ["Evidensnivå"]
HEADER_LABEL = "Evidensnivå"
# 2026-11-12 實測：442 頁有總覽等級，頁首全部＝總覽格第一個等級（主預測），0 頁例外 → first（不照 Tw 整格取最高）
HEADER_RULE = "first"
HEADER_KEEP_NA = True
HEADER_EXCEPTIONS: dict = {}
WITHDRAWN_RE = re.compile(r"^\s*(\*\*)?(Återkallad|Återkallat|Återkallade)\b", re.I)
DESC_LEVEL_WORD = r"evidensnivå"
DESC_LEVEL_DEFAULT = "evidensnivå"
NA_DESC = "endast kända användningar"

# ---- 許可證（licenses）----
MARKET_SECTIONS = ["Marknadsinformation Sverige"]  # ## 或 ### 標題

# ---- 查核框與查核紀錄表（apply_drug_reviews）----
DISCLAIMER_RE = re.compile(r"^## Ansvarsfriskrivning\b", re.M)
LOG_HEAD = "## Granskningslogg"
LOG_COLS = "| Granskningsdatum | Punkt | Åtgärd | Källa |"
LABEL = {"correct": "Granskningsrättelse", "annotate": "Granskningsanmärkning", "rereview": "Väntar på omprövning",
         "rereview_result": "Omprövningsresultat"}
ACTION = {"correct": "Rättad", "annotate": "Anmärkning tillagd", "rereview": "Markerad för omprövning",
          "section": "Avsnitt med källor tillagt", "rereview_result": "Omprövning klar",
          "header_level": "Evidensnivån i sidhuvudet räknades om enligt snabböversikten",
          "description_level": "Sidbeskrivningens evidensnivå följer sidhuvudet"}
VERDICT = {"maintain": "Oförändrad", "downgrade": "Nedgraderad", "upgrade": "Uppgraderad", "withdraw": "Återkallad"}
BOX_HEAD = "> **{label} ({date})**: "
ORIG_STATED = "Ursprungligen stod det: ”{claim}”"
SPACE, FULL_STOP, SENT_END = " ", ".", ".!?)”"
PAREN = " ({})"
JOIN, LIST_SEP, ITEM_SEP = " / ", "; ", ", "
SOURCE_WORD = "Källa: "
DECISION = "Beslutsrekommendation: "
TABLE_UPDATED = "{labels} på sidan har uppdaterats enligt omprövningen; de ursprungliga värdena finns i granskningsloggen nedan."
LEVEL_SAME = "evidensnivå {o} oförändrad"
LEVEL_CHANGE = "evidensnivå {o} → {n}"
ACT_REREVIEWED = "Markerad för omprövning → omprövad (se omprövningsresultatet)"
ACT_HEADER = "Evidensnivån i sidhuvudet räknades om enligt snabböversikten ({o} → {n})"
ACT_HEADER_WD = "Huvudprediktionen återkallades vid omprövning; evidensnivån i sidhuvudet räknades om ({o} → {n})"
ACT_NA_LIST = ", listas nu under ”{title}”"
ACT_RESULT = "Omprövning: {verdict}, {change}"
ACT_TABLE = "; {label}: ”{a}” → ”{b}”"
ACT_DESC = "Sidbeskrivningen: ”evidensnivå {o}” ändrades till ”{n}” (följer sidhuvudets nivå; övrig text oförändrad, originalet sparat i posten)"
ACT_REVISED = " (reviderad {d}; tidigare version sparad i posten)"
ST_SUPERSEDED = "Ersatt av den programgenererade licenstabellen (tidigare: {act})"
ST_REGEN = "Finns inte längre efter att rapporten genererades om ({d}: {note}; tidigare: {act})"
ST_PROGRAM = "Finns inte längre efter en programrättelse ({d}: {note}; tidigare: {act})"
ST_WITHDRAWN = "Granskningen återkallad ({d}: {note}; tidigare: {act})"
INTRO = ("Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. "
         "Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.")
INTRO_HEADER = ("Nedan finns granskningsloggen för den här sidan; evidensnivån i sidhuvudet följer snabböversikten. "
                "Modellens prediktioner, översiktstabellen och slutsatserna har inte skrivits om.")
INTRO_RERE = ("Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller "
              "endast grundläggande faktauppgifter och modellens prediktionstext har inte skrivits om; evidensnivåer och beslut har ändrats "
              "endast genom ett omprövningsresultat (nedgradering, uppgradering eller återkallelse), med de ursprungliga värdena nedan.")

# ---- 刪改轉紀錄（reviews_from_edits）----
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs）：938ac17f 刪「只剩註銷許可」、4e2faf00 移除台灣 TFDA 翻譯殘留、
# a7e1e463 第二批掃描刪矛盾子句。排程狀態格、排除表、AI 重產、i18n、description、空行修正不算。
COMMITS = ["938ac17f", "4e2faf00", "a7e1e463"]
# 期間內改寫整段報告文字的提交（AI 重產、排除表、英文殘留改瑞典文）：之前的刪改可能因此已不在頁面上
REGEN_COMMITS = ["0668db3c", "050f185a", "294fac7d", "20dc2b6f", "a5bcac6c", "59de49cd", "070c4c86", "636505f9", "5e95160f"]
SOURCES = [{"title": "Läkemedelsverket – export av godkända läkemedel", "url": "https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv"},
           {"title": "Läkemedelsverket", "url": "https://www.lakemedelsverket.se/"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-ZÅÄÖ0-9(*"”\[])|\n')
CLASS_EXTRA: dict = {}
NOTES = {
    "tw": "Borttaget: kvarlämnad malltext om Taiwans läkemedelsmyndighet (TFDA), som inte gäller den här svenska sidan.",
    "cancel": "Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data ({date}).",
    "count": "Borttaget: antalet eller statusen för godkännandena stämde inte med Läkemedelsverkets data ({date}).",
    "generic": "Borttaget: uppgiften stämde inte med Läkemedelsverkets godkännandedata ({date}).",
}
FIGURES = " Antal godkännanden enligt uppgifterna: {total}, varav giltiga: {valid}; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige."
SUMMARY = "Borttaget: ”{text}”"
STRIP_CHARS = " ,;.\n-"
REGEN_NOTE = "rapporten genererades om i november 2026 och innehåller inte längre uppgiften"

# ---- 原適應症交叉驗證（check_original_indications）----
ORIGINAL_LABELS = ["Ursprunglig indikation"]
ORIGINAL_NONE_RE = re.compile(r"^\s*(inte angiven|ej angiven|ingen|uppgift saknas|saknas|n/a)", re.I)
PHRASE_SPLIT = re.compile(r"[;,/()]+|\boch\b|\beller\b", re.I)
PHRASE_MIN = 4
