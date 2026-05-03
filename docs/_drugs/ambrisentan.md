---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Ambrisentan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

Baserat på Evidence Pack genererar jag nu rapporten enligt promtformatet v5.

---

# Ambrisentan: Från pulmonell arteriell hypertension till pulmonell arteriovenoös missbildning

## Sammanfattning

Ambrisentan är en selektiv ETA-receptorantagonist som ursprungligen godkändes för behandling av pulmonell arteriell hypertension (PAH). TxGNN-modellen förutsäger att det kan vara effektivt mot **pulmonell arteriovenoös missbildning (PAVM)**, med **0 kliniska prövningar** och **1 publikation** som för närvarande stöder denna riktning. Denna rapport är en flerindikatorbedömning av tio förutsagda indikationer, varav PAH associerad med HIV-infektion uppvisar den starkaste evidensen (L1, en avslutad fas 3-RCT), följt av PAH vid bindvävssjukdom och medfödd hjärtsjukdom (båda L2).

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Pulmonell arteriell hypertension (idiopatisk/ärftlig) |
| Förutsagd ny indikation | Pulmonell arteriovenoös missbildning (PAVM) |
| TxGNN-förutsägelsepoäng | 99,41% |
| Evidensnivå | L4 (mekanistisk koppling; inga kliniska prövningar) |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är Ambrisentan en selektiv endotelinreceptorantagonist (ETA) som blockerar endotelin-1-medierad (ET-1) vasokonstriktion och kärlremodellering i lungkärlen. Dess effekt vid idiopatisk och ärftlig PAH har bevisats i pivotala kliniska prövningar (bl.a. ARIES-1 och ARIES-2).

Pulmonell arteriovenoös missbildning (PAVM) är en strukturell kärlanomalitet i lungorna som i de flesta fall förekommer i samband med hereditär hemorragisk telangiektasi (HHT) – ett autosomalt dominant ärftligt tillstånd med mutationer i ALK1-, ENG- och BMPR2-generna som påverkar TGF-β/BMP-signalvägen. En undergrupp av HHT-patienter utvecklar PAH som en allvarlig komplikation, och det är i detta överlappande kliniska scenario som kopplingen till Ambrisentan uppkommer. ET-1 kan vara uppregulerat hos HHT-patienter, vilket ger ett visst biokemiskt stöd för ETA-antagonism.

Den mekanistiska kopplingen är dock i grunden **indirekt**: PAVM är en anatomisk arteriovenös shuntmissbildning snarare än en primärt vasokonstriktiv sjukdom. Ambrisentans ETA-blockad saknar direkt effekt på de strukturella shuntarna, och modellens höga förutsägelsepoäng reflekterar sannolikt det nätverksmässiga sambandet via PAH-komorbiditet (HHT→PAH→ERA-terapi) snarare än ett primärt terapeutiskt mål mot PAVM.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande för pulmonell arteriovenoös missbildning.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|-----------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Fallrapport | World Journal of Clinical Cases | Fallrapport om HHT-patient med komorbid PAH; genetisk familjeanalys identifierar sjukdomsmutationer. Illustrerar den kliniska överlappningen HHT–PAH men utvärderar inte Ambrisentan specifikt vid PAVM |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- PAVM-indikationen grundar sig på en indirekt mekanistisk koppling via HHT-PAH-komorbiditet, utan stöd från kliniska prövningar (L4-evidens). Ambrisentan saknar dessutom marknadsgodkännande i Sverige och fullständiga säkerhetsdata finns inte tillgängliga för bedömning.

**För att gå vidare krävs:**
- **Säkerhetsdata:** Hämta och analysera produktresumé (SmPC/TFDA-jäkort) för att koda varningar, kontraindikationer och kliniskt relevanta läkemedelsinteraktioner
- **Verkningsmekanismdata (MOA):** Bekräfta via DrugBank API (DB06403)
- **PAVM-specifik utredning:** Kartlägg om pågående HHT- eller PAH-studier inkluderar PAVM-subpopulationer med ET-1-uppregulering
- **Prioritering av starkare indikationskandidater i detta flerindikatorspaket:**

| Rang | Indikation | Evidensnivå | Beslut |
|------|-----------|-------------|--------|
| 5 | PAH vid HIV-infektion | **L1** – fas 3 RCT (NCT00709956, n=64, avslutad) | Gå vidare med försiktighet |
| 4 | PAH vid bindvävssjukdom | **L2** – fas 4 + fas 2 avslutade (inkl. SSc-PAH) | Gå vidare med försiktighet |
| 2 | PAH vid medfödd hjärtsjukdom | **L2** – fas 3b öppen studie (NCT01808313, n=134, avslutad) | Gå vidare med försiktighet |
| 1 | Pulmonell arteriovenoös missbildning | L4 – mekanistisk koppling | **Avvakta** |
| 3, 6–10 | Övriga (hemolytisk anemi, schistosomiasis, tandrelaterade, hårsyndrom, Dandy-Walker) | L5 – modellförutsägelse | **Avvakta** |
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

