"""SE（Läkemedelsverket）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv（依 ATC 主群組逐組匯出，; 分隔、UTF-16，免金鑰；
參數沿用站上 process_fda_data.py）。欄位：MT-nummer（＝證據包 license_id）、Registreringsstatus（Godkänd／Avregistrerad…）。
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
                out.append({"mt": k, "status": (x.get("Registreringsstatus") or "").strip(), "atc": atc})
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
