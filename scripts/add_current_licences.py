"""依原收集規則補收 Läkemedelsverket 現行清單有、證據包沒收的本藥許可（2026-11-25 第六輪，用戶決定；全程不用 AI）。

問題：證據包的許可是 collectors/sefda.py 收的：證據包的 DrugBank ID（tfda.drugbank_ids）→ data/processed/drug_mapping.csv
（2026-03 清單 data/raw/se_fda_drugs.json 的有效品項，由 scripts/run_kg_prediction.py 的 map_fda_drugs_to_drugbank 逐品項對照）
裡同一個 ID 的 MT 號 → se_fda_drugs.json 的那一列；撤銷狀態（config/fields.yaml withdrawn_statuses：Indragen、Avregistrerad、
Tillfälligt indragen，子字串比對）不收；最多存 20 筆（單方在前），total_matches 是全部筆數。2026-03 之後才出現的 MT 號
（或 2026-03 時沒有成分欄、所以沒進 drug_mapping 的號）不在 drug_mapping，永遠收不進來。

收集規則（逐包判定）：證據包收集的時間不同，用的 drug_mapping 也不同——2026-10-12 rescue_mapping 補救之前收的照
drug_mapping.csv.bak_20261012，之後收的照現行 drug_mapping.csv。第一次跑時照兩份對照在 se_fda_drugs.json 重算原收集器，
張數正好等於 total_matches、證據包現有紀錄都在裡面的那份就是它的規則（兩份都對用現行），記在 tfda.collection_rule；
當時算進 total_matches、因 20 筆上限沒存的號回填到 tfda.records_not_stored（防重複計數）。重算不出的整包不補（停損）。

新許可的對照（照原 pipeline，不放寬）：現行清單（license_adapter.fetch() 存的 data/raw/lmv_registreringsstatus.json）裡不在
drug_mapping、狀態不是撤銷、有成分（Verksamt ämne）的品項，照 run_kg_prediction.py 同一支 map_fda_drugs_to_drugbank 對 DrugBank ID
＝bak 規則；現行規則另對失敗的成分跑母目錄 .claude/rescue_mapping.py 的 rescue_ingredient（站上複本 scripts/rescue_mapping_20261012.py；2026-11-25 驗證：這兩步對 2026-03 清單
重跑，跟 drug_mapping.csv.bak_20261012、drug_mapping.csv 逐列相同）。對到證據包 drugbank_ids、證據包還沒有的（records、
records_not_stored、config/license_own_extra.json）就補：records 未滿 20 筆存進 records（單方在前），滿了只記號碼在
records_not_stored，兩者都算進 total_matches；每筆記 source（清單與下載日、規則）、added（補收日）。只加不刪、可重複執行。

不補的：bak 規則的證據包，用現行對照才會多對到的 2026-03 舊號（rescue 之後沒重收的既有差異，不是新許可）。

用法（repo 根目錄）：python3 scripts/add_current_licences.py [--download] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑。
"""
import csv
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as A  # noqa: E402

BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data" / A.RAW_FILE
BASE_LIST = ROOT / "data/raw/se_fda_drugs.json"
CUR = "drug_mapping.csv"
BAK = "drug_mapping.csv.bak_20261012"
MAPS = {CUR: ROOT / "data/processed/drug_mapping.csv", BAK: ROOT / "data/processed" / BAK}
EXTRA = ROOT / "config/license_own_extra.json"
CAP = 20
MIN_CUR = 20000
WD = ("indragen", "avregistrerad", "tillfälligt indragen")  # config/fields.yaml withdrawn_statuses（sefda._is_withdrawn：子字串）
csv.field_size_limit(10**9)


def withdrawn(st):
    s = str(st or "").strip().lower()
    return any(w in s for w in WD)


def load_map(p):
    lic, ids_all = {}, set()
    with open(p, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            lid = str(row.get("license_id") or "").strip()
            ids_all.add(lid)
            db = str(row.get("drugbank_id") or "").strip().upper()
            if not db or str(row.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            if lid:
                lic.setdefault(db, set()).add(lid)
    return {"lic": lic, "ids": ids_all}


def rescue_ns():
    """2026-10-12 rescue_mapping 的 rescue_ingredient（站上複本 scripts/rescue_mapping_20261012.py＝母目錄 .claude/rescue_mapping.py）；vocab 改讀本站 data/external"""
    for p in (ROOT / "scripts/rescue_mapping_20261012.py", ROOT.parent / "txgnn/.claude/rescue_mapping.py"):
        if p.exists():
            src = p.read_text(encoding="utf-8")
            break
    else:
        raise SystemExit("找不到 rescue_mapping.py，判斷不了現行對照，不補收")
    src = re.sub(r"^import sys as _sys, pathlib as _pl;.*$", "", src, count=1, flags=re.M)
    src = src.replace('BASE / "ESTxGNN/data/external/drugbank_vocab.csv"', f'Path({str(ROOT / "data/external/drugbank_vocab.csv")!r})')
    ns = {"__name__": "rescue_mapping"}
    exec(compile(src, "rescue_mapping", "exec"), ns)  # noqa: S102 — 本專案自己的檔
    return ns


def new_mapping(cands):
    """新品項 → {rule: {MT: set(DrugBank ID)}}，照 run_kg_prediction.py（＋rescue）原 pipeline"""
    import pandas as pd
    from setxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
    df = pd.DataFrame([{"Godkännandenummer": c["mt"], "Läkemedelsnamn": c.get("name", ""), "Aktiv substans": c.get("ingredients", "")}
                       for c in cands])
    fm = {"license_id": "Godkännandenummer", "brand_name": "Läkemedelsnamn", "ingredients": "Aktiv substans"}
    m = map_fda_drugs_to_drugbank(df, field_mapping=fm) if len(df) else pd.DataFrame()
    ns = rescue_ns()
    out = {CUR: {}, BAK: {}}
    for r in m.to_dict("records") if len(m) else []:
        lid = str(r.get("license_id") or "").strip()
        db = str(r.get("drugbank_id") or "").strip().upper()
        ok = str(r.get("mapping_success")).strip().lower() in ("true", "1")
        if ok and db:
            out[BAK].setdefault(lid, set()).add(db)
            out[CUR].setdefault(lid, set()).add(db)
            continue
        for name, _rule in ns["rescue_ingredient"](str(r.get("normalized_ingredient") or r.get("original_ingredient") or "")):
            out[CUR].setdefault(lid, set()).add(ns["vocab"][name].upper())
    return out


def ncomp(ing):
    return len([x for x in str(ing or "").split(";") if x.strip()])


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    today = datetime.date.today().isoformat()
    if "--download" in argv:
        cur = A.fetch()
        p = A.validate(cur, None)
        if p:
            raise SystemExit("現行清單有問題，不補收：" + "；".join(p))
        RAW.write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    else:
        try:
            cur = json.loads(RAW.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到現行清單 {RAW}：{e}")
    if len(cur) < MIN_CUR:
        raise SystemExit(f"現行清單只有 {len(cur)} 筆，疑似下載或格式有問題，不補收")
    ldate = datetime.date.fromtimestamp(RAW.stat().st_mtime).isoformat()
    curd = {str(r.get("mt") or "").strip(): r for r in cur if r.get("mt")}
    try:
        maps = {k: load_map(p) for k, p in MAPS.items() if p.exists()}
        base = json.loads(BASE_LIST.read_text(encoding="utf-8"))
        extra = json.loads(EXTRA.read_text(encoding="utf-8")).get("pages", {}) if EXTRA.exists() else {}
    except Exception as e:
        raise SystemExit(f"讀不到對照資料：{e}")
    if CUR not in maps:
        raise SystemExit("沒有 data/processed/drug_mapping.csv，不補收")
    by_lic = {}
    for r in base:
        lid = str(r.get("Godkännandenummer") or "").strip()
        if lid:
            by_lic.setdefault(lid, []).append(r)
    # 新品項：不在 drug_mapping（2026-03 有效品項）、不是撤銷狀態、有成分
    dm = maps[CUR]["ids"]
    cands = [c for c in curd.values() if c["mt"] not in dm and not withdrawn(c.get("status")) and str(c.get("ingredients") or "").strip()]
    nm = new_mapping(cands)
    by_db = {rule: {} for rule in maps}
    for rule in maps:
        for lid, dbs in nm[rule].items():
            for db in dbs:
                by_db[rule].setdefault(db, set()).add(lid)
    rows, nb, nrec, nfill, gaps, nrule = [], 0, 0, 0, [], 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        t = b.get("tfda") or {}
        if not t:
            continue
        ids = {str(x).upper() for x in t.get("drugbank_ids") or []}
        if not ids:
            continue
        recs = list(t.get("records") or [])
        not_stored = [str(x) for x in t.get("records_not_stored") or []]
        have = {str(r.get("license_id") or "") for r in recs} | set(not_stored)
        have |= set((extra.get(page) or {}).keys())
        total = int(t.get("total_matches") or len(recs))
        rule = t.get("collection_rule")
        changed = False
        if not rule:  # 第一次：重算原收集器，找出收集規則、回填當時沒存的號碼
            plain = {str(r.get("license_id")) for r in recs}
            for rn in (CUR, BAK):
                if rn not in maps:
                    continue
                act = [r for db in ids for lid in maps[rn]["lic"].get(db, ()) for r in by_lic.get(lid, []) if not withdrawn(r.get("Status"))]
                m = [str(r["Godkännandenummer"]) for r in act]
                if act and len(m) == total and plain <= set(m):
                    rule = rn
                    hid = sorted(set(m) - plain, key=lambda x: int(x) if x.isdigit() else 0)
                    if hid:
                        not_stored = hid
                        have |= set(hid)
                        nfill += 1
                        rows.append(f"{page}\t-\t({len(hid)} 張當時算進總數、沒存)\tbackfill_not_stored\t{rn}\t")
                    break
            if not rule:
                gaps.append(page)
                rows.append(f"{page}\t-\t(兩份對照都重算不出 total_matches {total})\tskipped_rule\t\t")
                continue
            nrule += 1
            changed = True
        if total - len(recs) - len(not_stored) != 0:
            gaps.append(page)
            rows.append(f"{page}\t-\t(total_matches {total} 跟已知號碼 {len(recs) + len(not_stored)} 不符)\tskipped_gap\t\t")
            continue
        want = {lid for db in ids for lid in by_db[rule].get(db, ())} - have
        src = (f"Läkemedelsverket exportmedprodcsv ({ldate}); matched by the original collector rule ({rule}"
               f"{'' if rule == CUR else ', pre-2026-10-12 mapping used when this bundle was collected'})")
        added = []
        for lid in sorted(want, key=lambda x: (ncomp(curd[x].get("ingredients")) > 1, int(x) if x.isdigit() else 0)):
            r = curd[lid]
            rec = {"license_id": lid, "brand_name_zh": r.get("name", ""), "brand_name_en": r.get("ingredients", ""),
                   "ingredients": r.get("ingredients", ""), "indication": "", "dosage_form": r.get("form", ""),
                   "manufacturer": r.get("holder", ""), "license_holder": r.get("holder", ""),
                   "approval_date": r.get("approval_date", ""), "expiry_date": "", "status": r.get("status", ""),
                   "source": src, "added": today}
            total += 1
            if len(recs) < CAP:
                recs.append(rec)
                where = "records"
            else:
                not_stored.append(lid)
                where = "not_stored"
            added.append(lid)
            rows.append(f"{page}\t{lid}\t{r.get('name', '')}\t{where}\t{r.get('ingredients', '')}\t{r.get('status', '')}")
        if not added and not changed:
            continue
        nb += bool(added)
        nrec += len(added)
        t2 = dict(t, records=recs, total_matches=total, found=bool(recs), collection_rule=rule)
        if not_stored:
            t2["records_not_stored"] = not_stored
        if not dry:
            b["tfda"] = t2
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tproduct\twhere\tingredients\tstatus\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"新品項候選 {len(cands)} 筆（對到 DrugBank：現行規則 {len(nm[CUR])}、bak 規則 {len(nm[BAK])}）")
    if nrule:
        print(f"記下收集規則：{nrule} 個證據包（回填 records_not_stored {nfill} 個）")
    if gaps:
        print(f"⚠ 判斷不了收集規則或總數對不上、這次不補的證據包 {len(gaps)} 個：{', '.join(gaps[:20])}")
    print(f"{'（試跑）' if dry else ''}依原收集規則補收：{nb} 個證據包、{nrec} 筆（現行清單 {len(curd)} 筆，{ldate}）")


if __name__ == "__main__":
    main(sys.argv[1:])
