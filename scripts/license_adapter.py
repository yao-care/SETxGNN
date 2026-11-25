"""SE（Läkemedelsverket）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv（依 ATC 主群組逐組匯出，; 分隔、UTF-16，免金鑰；
參數沿用站上 process_fda_data.py）。欄位：MT-nummer（＝證據包 license_id）、Registreringsstatus（Godkänd／Avregistrerad…）；
2026-11-25 起另存品名、規格、劑型、ATC、Verksamt ämne（成分原文）、持有人、H/V、核准日、平行輸入（RAW_FILE 每筆的 name…parallel_import）。
寫回 status＝Registreringsstatus 原文；reviewer 依文字判定（avregistr、återkall 算註銷）。新檔沒有的 MT-nummer 保留原狀態。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/lmv_registreringsstatus.json"
URL = "https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv"
ATC_GROUPS = list("ABCDGHJLMNPRSV")
PARAMS = {"narcClass": 0, "open": 0, "prescript": 0, "prodClass": 0, "registrationDateType": 0, "sale": 0, "status": 0, "vetHum": 0}


def _decode(b):
    for enc in ("utf-16", "utf-8-sig", "latin-1"):
        try:
            t = b.decode(enc)
            if "\x00" not in t[:200]:
                return t
        except (UnicodeDecodeError, ValueError):
            continue
    raise RuntimeError("無法解碼匯出檔")


def fetch():
    out = []
    for atc in ATC_GROUPS:
        for attempt in range(4):
            try:
                r = requests.get(URL, params={**PARAMS, "atcCode": atc}, timeout=180,
                                 headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
                r.raise_for_status()
                if "text/html" in r.headers.get("Content-Type", ""):
                    raise RuntimeError(f"ATC {atc} 回傳 HTML")
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(10 * (attempt + 1))
        rows = csv.DictReader(io.StringIO(_decode(r.content)), delimiter=";")
        if "MT-nummer" not in (rows.fieldnames or []) or "Registreringsstatus" not in (rows.fieldnames or []):
            raise RuntimeError(f"ATC {atc} 欄位改變：{rows.fieldnames}")
        for x in rows:
            k = (x.get("MT-nummer") or "").strip()
            if k:
                g = lambda c: (x.get(c) or "").strip()  # noqa: E731
                # 2026-11-25（用戶決定「adapter 存成分」）：除了號碼與狀態，另存收集器比對與補收要用的欄位（原文，不改寫），
                # 讓 Release 帶著現行清單的成分；scripts/add_current_licences.py 依這些欄位補收新許可。
                out.append({"mt": k, "status": g("Registreringsstatus"), "atc": atc,
                            "name": g("Namn"), "strength": g("Styrka"), "form": g("Form"), "atc_code": g("ATC-kod"),
                            "ingredients": g("Verksamt ämne"), "ingredients_simple": g("Verksamt ämne (förenklat)"),
                            "holder": g("Innehavare"), "hv": g("H/V"), "approval_date": g("Godkännandedatum"),
                            "parallel_import": g("Parallellimport")})
    return out


def validate(new, old):
    p = []
    if len(new) < 8000:
        p.append(f"只解析出 {len(new)} 筆，疑似匯出格式改變")
    if sum(1 for r in new if not r["status"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 Registreringsstatus")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["mt"]: r["status"] for r in new if r["status"]}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True


# 2026-11-24（用戶決定「程式產生許可證表」）：每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）在概覽表同步之後，
# 依證據包把「Marknadsinformation Sverige」的程式許可證表重排（scripts/sync_license_tables.py --bundles；所有頁比對、只寫有變的）。
# PAGE_NOTE：排程 3b 自我檢查允許的非表格行（程式區塊標記、Tabellen visar 句、來源句、沒有任何紀錄時的一句）。
def _slt(site_dir):
    import importlib.util
    from pathlib import Path
    s = importlib.util.spec_from_file_location("sync_license_tables", Path(site_dir) / "scripts" / "sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def sync_tables(site_dir, bundles):
    """回傳 [(頁, 欄位, 前值, 後值)]；所有有證據包的頁都比對（只寫內容有變的），不只 bundles 列出的藥"""
    import difflib
    from pathlib import Path
    m = _slt(site_dir)
    drugs = Path(site_dir) / "docs" / "_drugs"
    before = {p.name: p.read_text(encoding="utf-8") for p in drugs.glob("*.md")}
    out = []
    for name in m.run(from_bundles=True):
        new = (drugs / name).read_text(encoding="utf-8")
        for l in difflib.unified_diff(before[name].split("\n"), new.split("\n"), lineterm="", n=0):
            if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].startswith("|"):
                out.append((name[:-3], "Godkännandetabell (programgenererad)", l[1:] if l[0] == "-" else "", l[1:] if l[0] == "+" else ""))
    return out


try:
    import importlib.util as _ilu
    from pathlib import Path as _P
    _s = _ilu.spec_from_file_location("_slt_note", _P(__file__).resolve().parent / "sync_license_tables.py")
    _m = _ilu.module_from_spec(_s)
    _s.loader.exec_module(_m)
    PAGE_NOTE = _m.PAGE_NOTE
except Exception:  # 站上的 license_adapter 被母目錄當模組載入時，路徑一定在 scripts/ 下；這裡只防萬一
    PAGE_NOTE = r"^<!-- licenses:(begin|end) -->$"
