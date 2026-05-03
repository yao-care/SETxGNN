---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

Skill content noted — this is a Swedish TxGNN deployment (Se). Generating the pharmacist evaluation report now based on the Evidence Pack.

---

# Telmisartan: Från hypertoni till Prinzmetal angina

## Sammanfattning

Telmisartan är en angiotensin II-receptorblockerare (ARB) med dubbel verkningsmekanism — AT1-receptorblockad och partiell PPARγ-agonism — och används globalt för behandling av hypertoni och kardiovaskulär riskreduktion. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Prinzmetal angina** (vasospastisk angina) med en förutsägelsepoäng på **99,98%**. För närvarande finns **inga kliniska prövningar** och **inga publikationer** som direkt stöder denna indikation, vilket placerar evidensen på nivå L5 — enbart modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Hypertoni (globalt etablerad; ej godkänd i Sverige) |
| Förutsagd ny indikation | Prinzmetal angina |
| TxGNN-förutsägelsepoäng | 99,98% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd farmakologisk information är telmisartan en ARB som tillhör klassen AT1-receptorantagonister med den unika tilläggsegenskapen att vara en partiell PPARγ-agonist — vilket gett läkemedlet epitetet "metabosartan". Dess effekt vid hypertoni och sekundärprevention av kardiovaskulära händelser är väldokumenterad i globala registreringar.

Sambandet med Prinzmetal angina är teoretiskt men inte orimligt: vasospastisk angina beror på övergående koronart artärspasm, och angiotensin II kan via AT1-receptorer bidra till vasokonstriktion i koronarkärlen. AT1-blockad skulle teoretiskt kunna motverka detta. Därtill kan PPARγ-aktivering förbättra endotelfunktionen och minska vaskulär reaktivitet — en mekanism som kan vara relevant vid kärlspasm.

Kopplingen är dock rent spekulativ och saknar experimentellt stöd. Det finns varken kliniska studier, djurexperimentella data eller mekanistiska rapporter som specifikt undersökt telmisartans effekt vid Prinzmetal angina. TxGNN:s höga förutsägelsepoäng baseras på topologiska relationer i sjukdoms-läkemedels-grafen och bör tolkas som en hypotesgenererande signal snarare än ett kliniskt bevis.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Telmisartan är för närvarande **inte godkänt** på den svenska marknaden. Inga produktgodkännanden finns registrerade i detta underlag.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Trots en hög TxGNN-förutsägelsepoäng (99,98%) saknas all faktisk evidens för telmisartan vid Prinzmetal angina — varken kliniska prövningar, djurmodelldata eller publicerad litteratur finns tillgänglig för denna indikation. Förutsägelsen är biologiskt möjlig på teorinivå men har ännu inte testats experimentellt.

**För att gå vidare krävs:**
- Systematisk sökning efter prekliniska data: påverkar AT1-blockad och/eller PPARγ-aktivering koronart artärspasm i djurmodeller?
- Litteraturgranskning utvidgad till angränsande ARB-preparat (losartan, valsartan, candesartan) vid vasospastisk angina för att bedöma klasseffekt
- Mekanistisk bedömning: kartlägg överlappande patofysiologiska vägar mellan angiotensin II-signalering och koronart vasospasm
- Komplettering av säkerhetsprofil via produktresumé och DrugBank API (MOA, kontraindikationer, DDI)
- Om preklinisk signal identifieras: proof-of-concept pilotstudie (fas 2) för effekt och säkerhet vid Prinzmetal angina
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

