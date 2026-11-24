#!/usr/bin/env python3
"""「Marknadsinformation Sverige」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定「程式產生許可證表」；全程不用 AI）。

為什麼：這張表原本是報告（AI）寫的自由格式表（多數是「| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |」，
indikation 欄全是「Ingen indikationstext registrerad」之類；少數另有 Status／Tillverkare／Innehavare 欄、或在號碼格寫「(indraget)」）。
Läkemedelsverket 的資料每週變，AI 表不會跟著改，跟事實矛盾時 checker 擋整頁（2026-11-12 就以 se-row-20261112-* 人工更正 272 列）。
改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables 掛鉤，--bundles）依同一套規則重排，gate 依快照驗內容。
範本：DETxGNN（快照存列、gate 整塊比對）、HkTxGNN（照原表選列，正文才對得上）的同名檔。

表格（文字照 Läkemedelsverket 原文，不翻譯；本站就是瑞典文）：
  | Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
  證據包 tfda.records＋config/license_own_extra.json（證據包漏收、人工對照確屬本藥的號碼；事實層也併進去）（Läkemedelsverket 匯出：MT-nummer、Läkemedelsnamn、Läkemedelsform、Innehavare、Registreringsstatus）；
  狀態欄＝Registreringsstatus 原文（Godkänd、Registrerad、Avregistrerad、Tillfälligt återkallad…；核准但未販售仍是 Godkänd）。
選列與順序：換表當時報告原表依序列出的號碼（config/license_table_pins.json 的 ids）在前——正文常寫「De fem första visas nedan」
  「Tillverkare: …」「De tre återstående är …」「Båda godkännandena …」，換成別的列會對不上；其餘依程式排序：有效（Godkänd／Registrerad）
  在前、單一成分在前（成分欄以「; 」分隔的個數）、再依號碼。列數＝原表列數（pins 的 n，最多 20）；原本沒有表的頁 min(5, 總數)。
表下：總數多於列數時一句 SHOW（證據包只收了一部分紀錄的 partial 頁寫「minst」並註明可能不完整），再一行來源句 SOURCE；
  證據包沒有任何紀錄時整個區塊只有 NONE_LINE。區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（前後空行），
  讓查核紀錄、正文張數改寫（scripts/rewrite_license_counts.py）與 gate 分得出哪些字是程式寫的。
放在哪：段落裡原有的第一張表換成程式區塊；段落裡沒有表時放在標題下；沒有市場段落的頁不加。表以外的文字不動
  （--migrate 只在第一次換表時用：緊接舊表下一行、只講「表上列了幾筆」的句子拿掉，由 SHOW 取代；查核紀錄的文字不動）。
資料來源：預設讀快照 snapshots/se_licenses.json.gz 的 rows／total／partial（scripts/build_license_snapshot.py 用 rows_of 算）；
  --bundles 改讀 data/bundles（每週排程在建新快照前用）。gate（scripts/check_seo_docs.py 第 18 項）檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程 license_adapter.sync_tables；
  scripts/sync_notes_to_docs.py 整頁重寫時用 carry_block 移植舊頁的程式區塊。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [--migrate] [--init-pins] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "se_licenses.json.gz"
PINS_FILE = ROOT / "config" / "license_table_pins.json"
SECS = ("Marknadsinformation Sverige",)
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = ["| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |", "|------|------|------|------|------|"]
SHOW = "Tabellen visar {n} av {m} godkännanden i uppgifterna."
SHOW_PARTIAL = "Tabellen visar {n} av minst {m} godkännanden; uppgifterna innehåller bara en del av godkännandena, så listan kan vara ofullständig."
SOURCE = "Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter)."
NONE_LINE = "I Läkemedelsverkets uppgifter som sammanställts för den här rapporten finns inget godkännande för den här substansen."
MAX_ROWS = 20
VALID_ST = ("godkänd", "registrerad")
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
PAGE_NOTE = (r"^(" + "|".join(re.escape(x) for x in (BEGIN, END, SOURCE, NONE_LINE)) + r"|Tabellen visar \d+ av \d+ godkännanden i uppgifterna\."
             r"|Tabellen visar \d+ av minst \d+ godkännanden; uppgifterna innehåller bara en del av godkännandena, så listan kan vara ofullständig\.)$")
SHOW_RX = re.compile(r"^Tabellen visar \d+ av (minst )?\d+ godkännanden")
# --migrate：緊接舊表的下一行裡只講「表上列了幾筆」的句子（數字或「första」跟顯示字樣同句、沒有狀態／成分／劑型等事實字樣）
_NUMW = r"(?:\d+|en|ett|två|tre|fyra|fem|sex|sju|åtta|nio|tio|elva|tolv|tjugo)"
CAPTION_RX = [
    re.compile(r"^(?:Listan|Tabellen)(?: ovan)? visar (?:de |endast )?(?:" + _NUMW + r" )?(?:första|av)\b[^.;]*\.$", re.I),
    re.compile(r"^Visar " + _NUMW + r" av (?:totalt )?" + _NUMW + r" (?:registrerade )?godkännanden\.$", re.I),
    re.compile(r"^Fler godkännanden finns i de lokala (?:data|uppgifterna)(?: än de(?: " + _NUMW + r")? som visas här|; här visas de " + _NUMW + r" första)\.$", re.I),
]
CAPTION_FACT = re.compile(r"giltig|avregistr|indrag|återkall|enkomponent|enkelsubstans|kombination|tablett|kapsel|injektion|lösning|"
                          r"kräm|salva|tillverk|innehav|marknadsför", re.I)


def cell(x, cap=90):
    s = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return (s if len(s) <= cap else s[:cap - 1].rstrip() + "…") or "–"


def holder(x):
    """innehavare：照 Läkemedelsverket 原文（2026-11-24 第二輪：公司名裡的 KG 照原文，checker P5 已豁免 GmbH／Ges.m.b.H. … KG）"""
    return cell(x, 70)


def is_valid(r):
    return str(r.get("status") or "").strip().lower() in VALID_ST


def is_combo(r):
    return len([x for x in str(r.get("ingredients") or "").split(";") if x.strip()]) > 1


def uniq(recs):
    seen = {}
    for r in recs or []:
        k = str(r.get("license_id") or "").strip()
        if k and k not in seen:
            seen[k] = r
    return list(seen.values())


def _idkey(k):
    return (0, int(k), k) if k.isdigit() else (1, 0, k)


_PINS = None


def pins():
    global _PINS
    if _PINS is None:
        _PINS = json.loads(PINS_FILE.read_text(encoding="utf-8")).get("pins", {}) if PINS_FILE.exists() else {}
    return _PINS


def pins_for(stem):
    p = pins()
    return p.get(stem) or p.get(stem.replace("-", "_")) or p.get(stem.replace("_", "-")) or {}


EXTRA_FILE = ROOT / "config" / "license_own_extra.json"


def extra_records(stem):
    """config/license_own_extra.json（證據包漏收、人工對照確屬本藥的許可證，事實層也併進去）轉成證據包紀錄的欄位"""
    if not EXTRA_FILE.exists():
        return []
    pg = json.loads(EXTRA_FILE.read_text(encoding="utf-8")).get("pages", {})
    m = pg.get(stem) or pg.get(stem.replace("-", "_")) or pg.get(stem.replace("_", "-")) or {}
    return [{"license_id": k, "brand_name_zh": v.get("product"), "dosage_form": v.get("form"), "license_holder": v.get("holder"),
             "ingredients": v.get("ingredients"), "status": v.get("registreringsstatus") or ("Godkänd" if v.get("status") == "valid" else "")}
            for k, v in m.items()]


def rows_of(tf, pin=None, extra=()):
    """證據包 tfda（＋extra_records）→ (要顯示的表格列, 總數, partial)。pin＝{"ids": [...], "n": N}（config/license_table_pins.json）。"""
    pin = pin or {}
    recs = uniq(list(tf.get("records") or []) + list(extra or []))
    recs.sort(key=lambda r: (not is_valid(r), is_combo(r), _idkey(str(r["license_id"]).strip())))
    rank = {k: i for i, k in enumerate(pin.get("ids") or [])}
    recs.sort(key=lambda r: rank.get(str(r["license_id"]).strip(), len(rank)))  # 穩定排序：沒選的保持程式排序
    rows = [f"| {str(r['license_id']).strip()} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'), 80)} | {cell(r.get('dosage_form'), 80)} | "
            f"{holder(r.get('license_holder') or r.get('manufacturer'))} | {cell(r.get('status'), 40)} |" for r in recs]
    total = len(rows)
    partial = int(tf.get("total_matches") or 0) > total
    n = min(MAX_ROWS, total, int(pin.get("n") or 5))
    return rows[:n], total, partial


def program_block(rows, total, partial=False):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows + [""]
    if partial:
        out += [SHOW_PARTIAL.format(n=len(rows), m=total), ""]
    elif total > len(rows):
        out += [SHOW.format(n=len(rows), m=total), ""]
    return out + [SOURCE]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def bounds(lines):
    """第一個市場段落（## 或 ### Marknadsinformation Sverige）的 (標題行, 段落結尾)；沒有回 (None, None)"""
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) in SECS:
            lv = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{lv}}} ", lines[k])), len(lines))
            return i, j
    return None, None


def first_table(lines, a, b):
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return x, y + 1


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def strip_captions(line, protect=()):
    """--migrate 用：回傳 (拿掉只講表上筆數的句子後的行, 拿掉的句子)；行內其他句子不動"""
    parts = re.split(r"(?<=[.!?])\s+", line.strip())
    keep, gone = [], []
    for s in parts:
        if any(r.match(s) for r in CAPTION_RX) and not CAPTION_FACT.search(s) and not any(p and s in p for p in protect):
            gone.append(s)
        else:
            keep.append(s)
    return " ".join(keep), gone


def process(text, rows, total, partial=False, migrate=False, protect=()):
    """回傳 (新內容, 拿掉的說明句)。沒有市場段落時原樣。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, total, partial))
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk)), []
    h, b = bounds(lines)
    if h is None:
        return text, []
    x, y = first_table(lines, h + 1, b)
    gone = []
    if x is None:
        return "\n".join(_splice(lines, h + 1, h + 1, blk)), []
    if migrate:
        k = y
        while k < b and not lines[k].strip():
            k += 1
        if k < b and not lines[k].startswith(("<!--", ">", "|", "#", "-", "*")) and lines[k].strip() != "---":
            new, gone = strip_captions(lines[k], protect)
            if gone:
                lines = lines[:k] + ([new] if new else []) + lines[k + 1:]
    return "\n".join(_splice(lines, x, y, blk)), gone


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁（之後 apply_drug_reviews.py 結尾會依快照補上）。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = new_text.replace("\r\n", "\n").split("\n")
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk))
    h, b = bounds(lines)
    if h is None:
        return new_text
    x, y = first_table(lines, h + 1, b)
    if x is None:
        return "\n".join(_splice(lines, h + 1, h + 1, blk))
    return "\n".join(_splice(lines, x, y, blk))


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def bundle_for(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def _protect():
    p = ROOT / "docs/_data/drug_reviews.json"
    out = {}
    if p.exists():
        for r in json.loads(p.read_text(encoding="utf-8")).get("records", []):
            out.setdefault(r["file"], []).extend([r.get("replacement") or "", r.get("anchor") or "", r.get("claim") or ""])
    return out


def run(from_bundles=False, check=False, only=None, migrate=False, report=None):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。report（list）收 --migrate 拿掉的說明句 (頁, 句子)。"""
    snap = {} if from_bundles else _snapshot()
    prot = _protect() if migrate else {}
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = bundle_for(p.stem)
            if b is None:
                continue
            rows, total, partial = rows_of(b.get("tfda") or {}, pins_for(p.stem), extra_records(p.stem))
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, total, partial = e["rows"], e["total"], e.get("partial_rows", False)
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new, gone = process(t0, rows, total, partial, migrate, prot.get(p.name, ()))
        if report is not None:
            report += [(p.stem, s) for s in gone]
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def block_problems(sec_lines, entry):
    """gate 用：段落裡的程式區塊＝快照重算的結果、段落裡沒有程式區塊以外的表（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in sec_lines, END in sec_lines
    if has_b != has_e or sec_lines.count(BEGIN) > 1:
        return ["程式許可證區塊標記不成對或不只一組"]
    if "rows" not in entry:
        return []
    if not has_b:
        return ["市場段落沒有程式許可證表（跑 python3 scripts/sync_license_tables.py）"]
    i, j = sec_lines.index(BEGIN), sec_lines.index(END)
    errs = []
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["total"], entry.get("partial_rows", False)) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        errs.append(f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）")
    outside = [x for k, x in enumerate(sec_lines) if x.startswith("|") and not (i < k < j)]
    if outside:
        errs.append(f"市場段落有程式區塊以外的表格：{outside[0][:40]}")
    return errs


def init_pins():
    """第一次換表前：記下各頁報告原表依序列出的號碼與列數（之後的選列依這份；換表後不要再跑）"""
    sys.path.insert(0, str(ROOT / "src"))
    from setxgnn.regulatory import licenses as L
    out, missing = {}, []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        if is_redirect(t):
            continue
        lines = t.split("\n")
        if BEGIN in lines:
            continue
        h, b = bounds(lines)
        if h is None:
            continue
        x, y = first_table(lines, h + 1, b)
        if x is None:
            continue
        ids = [L._id_token(ln.strip().strip("|").split("|")[0]) for ln in lines[x + 2:y]]
        ids = [i for i in ids if i]
        bd = bundle_for(p.stem)
        have = {str(r.get("license_id") or "").strip() for r in ((bd or {}).get("tfda") or {}).get("records") or []}
        missing += [(p.stem, i) for i in ids if i not in have]
        out[p.stem] = {"ids": ids, "n": max(1, min(MAX_ROWS, y - x - 2))}
    PINS_FILE.parent.mkdir(exist_ok=True)
    PINS_FILE.write_text(json.dumps({"_doc": "換表當時（2026-11-24）報告原表依序列出的 Läkemedelsverket 號碼（ids）與列數（n）；"
                                             "scripts/sync_license_tables.py 的選列依這份（原表選的列在前，其餘依程式排序）",
                                     "pins": out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out, missing


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--init-pins" in a:
        o, miss = init_pins()
        print(f"原表選列：{len(o)} 頁；證據包沒有的號碼 {len(miss)} 個 {miss[:10]}")
        sys.exit(0)
    only = {x for x in a if not x.startswith("--")} or None
    rep = []
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only, migrate="--migrate" in a, report=rep)
    for s, x in rep:
        print(f"  拿掉說明句 {s}：{x}")
    print(f"程式許可證表：{'待改' if '--check' in a else '改'} {len(ch)} 頁" + (f"；拿掉說明句 {len(rep)} 句" if "--migrate" in a else ""))
    if "--check" in a:
        sys.exit(1 if ch else 0)
