"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN、DETxGNN 同名檔，規則是本站瑞典文句型）。

正文裡「N giltiga godkännanden (av M)」「N av M godkännanden är giltiga」「Av M registrerade godkännanden är N giltiga och C avregistrerade」
「Totalt finns N godkännanden, varav V är giltiga」「Alla N godkännanden är giltiga」這類 Läkemedelsverket 許可張數敘述，由程式依許可證快照
（snapshots/se_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 Läkemedelsverket 許可張數」的地方，其餘一律不動：
  - 句子要有許可字樣（godkännande、licens、försäljningstillstånd；單獨的「tillstånd」常是「疾病／狀況」，不算），
    且沒有試驗、文獻、病人、交互作用、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor／claim 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（minst、ofullständig、urval、ungefär…）、講證據包或查詢、相對數（ytterligare、övriga、andra、fler、till）、
    劑型或單方／複方子集（enkomponent、kombination、tablett、injektion…）、其他國家、廠商子集、講表格顯示筆數
    （visa(s/r)、listan、tabellen、nedan、ovan、första、listade…，reason＝display；數字等於程式表列數 facts["shown"] 也算對）；事實層 partial 或總數 0 的頁整頁不動。
角色：「X av Y」的 X 看後面的狀態字（giltig→有效；avregistrerad／indragen／återkallad→註銷），Y＝總數；
「Av M … är N giltiga (och C avregistrerade)」M＝總數；「varav V är giltiga och C avregistrerat」；「N giltiga …」有效；
「N avregistrerade …」註銷（「ett avregistrerat」這種 en／ett 接狀態字也認，但不改）；點名許可證號（4～6 位數）的句子不動；「N (registrerade) godkännanden」總數（後面接「är giltiga」算有效、「är indragna／avregistrerade」算註銷，
前面是 alla／samtliga 時算總數）；其餘數字不動。數字可寫成阿拉伯數字或 två～tolv；「båda」與「en／ett」不改（單複數、
形容詞變化要跟著改），跨過 1 的改動同理，列 grammar。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列為 ambiguous。
不改、列出（要改請寫查核紀錄）：同句有試驗／交互作用等其他字樣（mixed）、原數字 0（zero-premise）、新數字 0（zero-result）、1／båda 跟其他數之間的改動（grammar）、
句子說「alla／samtliga／båda … giltiga」或「inga … avregistrerade」而事實不符（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÅÄÖ*\[(>-])")
WORDS = {"två": 2, "tre": 3, "fyra": 4, "fem": 5, "sex": 6, "sju": 7, "åtta": 8, "nio": 9, "tio": 10, "elva": 11, "tolv": 12,
         "båda": 2, "bägge": 2}
W_OUT = {v: k for k, v in WORDS.items() if k not in ("båda", "bägge")}
ONE = r"(?:en|ett)"
NUM = re.compile(r"(?<![\w.,/-])(\d{1,4}|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r"|" + ONE +
                 r"(?=\s+(?:(?:(?:giltigt|registrerat|avregistrerat|svenskt|indraget)\s+)?(?:läkemedels|marknads)?godkännande\b|"
                 r"(?:är\s+)?(?:avregistrerat|indraget|återkallat|giltigt)\b)))(?![\w%-])", re.I)
LICENSE = re.compile(r"godkännand|\blicens(?:er|erna|en)?\b|försäljningstillstånd", re.I)
NOT_LICENSE = re.compile(r"prövning|studie|publikation|artikel|patient|deltagare|interaktion|PMID|NCT|\bmg\b|\bml\b|%|\bår\b|månad|vecka|"
                         r"\bdos|indikation(?:er|erna)\b|fas \d|\b(?:19|20)\d\d\b|tillstånden\b", re.I)
HEDGED = re.compile(r"\bminst\b|åtminstone|ofullständig|delvis|urval|ungefär|omkring|cirka|\bca\b|troligen|möjligen|"
                    r"evidenspaket|evidence pack|sökning|sökningen|hämtade|"
                    r"ytterligare|övriga|\bandra\b|\bfler\b|\btill\b|återstående|resterande|bland annat|däribland|utöver|"
                    r"enkomponent|enkelsubstans|enskild substans|enda aktiva|enbart|kombination|"
                    r"tablett|kapsel|injektion|infusion|lösning|pulver|spray|droppar|kräm|salva|gel\b|plåster|suppositori|inhalation|beredning|"
                    r"\bFDA\b|\bUSA\b|\bEMA\b|centralt|Danmark|Norge|Finland|tillverk|innehav|från [A-Z]", re.I)
DISPLAY = re.compile(r"\bvisa[rs]?\b|\blistan\b|\btabellen\b|\bnedan\b|\bovan\b|\bförsta\b|\blistade?\b|följande|\bredovisas\b", re.I)
CANC = r"(?:avregistrer\w*|indrag\w*|återkall\w*|upphäv\w*|upphör\w*|ogiltig\w*)"
VALID = r"(?:giltig\w*|gällande|i kraft)"
ADJ = r"(?:(?:registrerade?|registrerat|svenska|svenskt|lokala|nuvarande|befintliga|aktuella)\s+)*"
NOUN = r"(?:läkemedels|marknads)?godkännande(?:n|na|t)?|licens(?:er|erna|en)?|försäljningstillstånd(?:et|en)?"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _val(tok):
    t = tok.lower()
    if t.isdigit():
        return int(t)
    if t in WORDS:
        return WORDS[t]
    return 1


def _fmt(tok, v):
    if tok.isdigit() or v not in W_OUT:
        return str(v)
    w = W_OUT[v]
    return w.capitalize() if tok[:1].isupper() else w


def _role(s, a, b):
    left, right = s[max(0, a - 50):a], s[b:b + 80]
    # 「X av Y」的 Y＝總數（前面是數字、「giltiga godkännanden」，或句首／括號的「Av」接名詞）；其他「av N」不動
    if re.search(r"\bav\s+(?:de\s+|totalt\s+)?$", left, re.I):
        pre = re.sub(r"\bav\s+(?:de\s+|totalt\s+)?$", "", left, flags=re.I)
        if re.search(r"(\d+|" + "|".join(WORDS) + r")\s*$", pre, re.I) or \
                re.search(r"(giltiga|avregistrerade)\s+(?:" + ADJ + r"(?:" + NOUN + r")\s*)?\(?$", pre, re.I):
            return "total"
        if re.search(r"(?:^|[(;,:]\s*|\.\s+)$", pre) and re.match(r"\s+" + ADJ + r"(?:" + NOUN + r")\b", right, re.I):
            return "total"  # 「Av 20 registrerade godkännanden är 16 giltiga」
        return None
    # 「X av Y …」的 X：看後面的狀態字
    m = re.match(r"\s+av\s+(?:de\s+|totalt\s+)?\S+\s+" + ADJ + r"(?:(?:" + NOUN + r")\s*)?(?:\([^)]*\)\s*)?(?:(?:är|var|förblir|fortfarande|nu)\s+){0,2}(" + VALID + "|" + CANC + ")", right, re.I)
    if m:
        return "cancelled" if re.match(CANC, m.group(1), re.I) else "valid"
    if re.match(r"\s+av\s+", right):
        if re.search(r"giltiga\s+(?:" + NOUN + r")\s*\(?$|giltiga\s*\(?$", left, re.I):
            return "valid"  # 「alla fyra giltiga godkännanden (4 av 4)」
        return None
    # 「varav 12 är giltiga och 1 är avregistrerat」「är 16 giltiga och 4 avregistrerade」
    if re.match(r"\s+(?:är\s+|var\s+)?" + VALID, right, re.I) and re.search(r"\b(varav|är|och)\s+$", left, re.I):
        return "valid"
    if re.match(r"\s+(?:är\s+|var\s+)?" + CANC, right, re.I) and re.search(r"\b(varav|är|och)\s+$", left, re.I):
        return "cancelled"
    if re.match(r"\s+(?:" + ADJ + r")giltig[at]?\s+(?:" + ADJ + r")(?:" + NOUN + r")\b", right, re.I):
        return "valid"
    if re.match(r"\s+" + CANC + r"\s+(?:" + ADJ + r")(?:" + NOUN + r")\b", right, re.I):
        return "cancelled"
    m = re.match(r"\s+" + ADJ + r"(?:" + NOUN + r")\b([^.;,:]{0,40})", right, re.I)
    if m:
        tail = m.group(1)
        allq = re.search(r"\b(alla|samtliga|totalt)\s*$", left, re.I)
        if re.search(r"\b(är|var|har)\s+(?:\w+\s+)?" + CANC, tail, re.I) and not allq:
            return "cancelled"
        if re.search(r"\b(är|var)\s+(?:\w+\s+)?giltiga", tail, re.I) and not allq:
            return "valid"
        return "total"
    return None


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(alla|samtliga|båda|bägge|det enda|den enda)\b[^.;]{0,60}" + VALID, lo) and (f.get("valid") != f.get("total")):
        return False
    if re.search(r"\b(inga|inget|ingen)\b[^.;]{0,40}" + CANC, lo) and f.get("cancelled"):
        return False
    if re.search(r"\b(inga|inget|ingen)\b[^.;]{0,50}\bgiltig", lo) and f.get("valid"):
        return False
    if re.search(r"\b(alla|samtliga|båda|bägge)\b[^.;]{0,60}" + CANC, lo) and (f.get("cancelled") != f.get("total")):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] for m, r in found)
    if NOT_LICENSE.search(sent):  # 同句另有試驗、交互作用等字樣：不改；數字跟事實對不上時列出（不要默默略過許可證張數）
        return sent, ("mixed" if bad else "mixed-ok")
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    if re.search(r"(?<![\w.,])\d{4,6}(?![\w.,])", sent):  # 點名許可證號（例「två giltiga (Feburo, 55201 och 55202)」）：講的是那幾張
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] and _val(m.group(1)) != f.get("shown") for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, role in found:
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if (old == 1) != (v == 1) or m.group(1).lower() in ("båda", "bägge", "en", "ett"):
            return sent, "grammar"
        subs.append((m, role, old, v))
    if not _premise_ok(sent, f):
        return sent, "premise"
    if not subs:
        return sent, None
    out, pos = [], 0
    for m, _, _, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(_fmt(m.group(1), v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
