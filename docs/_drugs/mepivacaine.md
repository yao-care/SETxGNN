---
layout: default
title: Mepivacaine
parent: Endast modellprediktion (L5)
nav_order: 278
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "mepivacaine"
predicted_indications: ["gastroduodenitis", "peptic ulcer disease"]
description: "Mepivacaine: predikterad ny indikation Gastroduodenitis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Mepivacaine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## Mepivacaine: Gastroduodenitis
{: .text-alpha }

---

### Sammanfattning

Mepivakain är ett amidlokalanestetikum som i Sverige har marknadsförts som injektionsvätska (bland annat under namnen Carbocain och Scandonest). Det finns ingen registrerad indikationstext i de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **gastroduodenit**, men det finns **inga kliniska prövningar** och **ingen relevant litteratur** som stöder denna riktning. Förutsägelsen bygger enbart på modellberäkning.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Gastroduodenitis |
| TxGNN-förutsägelsepoäng | 0.9949 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 7 av 7) |
| Antal godkännanden | 7 (giltiga: 7) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Det som är allmänt känt är att mepivakain är ett amidlokalanestetikum som blockerar spänningsberoende natriumkanaler och därmed hämmar nervsignaler.

Ett samband med inflammation i magsäck och tolvfingertarm är i nuläget spekulativt. En tänkbar hypotes är minskad signalering från sensoriska nervändar i mag-tarmkanalen eller lokala antiinflammatoriska effekter, men inga data i underlaget styrker detta. Den höga poängen (0,9949) är en ren datorberäknad förutsägelse.

Den enda hittade publikationen (PMID 6890367) handlar om säkerhetsfarmakologi för ett annat läkemedel, lofexidin, och är inte relevant för mepivakain eller magsår.

---

### Marknadsinformation Sverige

Alla sju godkännanden är indragna. Ingen indikationstext finns registrerad.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 5969 | Carbocain | Injektionsvätska, lösning | – |
| 5970 | Carbocain | Injektionsvätska, lösning | – |
| 14381 | Scandonest | Injektionsvätska, lösning | – |
| 6751 | Carbocain dental | Injektionsvätska, lösning | – |
| 5972 | Carbocain adrenalin | Injektionsvätska, lösning | – |

---

### Säkerhetsaspekter

- **Möjliga kontraindikationer enligt kunskapsgraf (ej från produktresumé):** njursjukdom, leversjukdom, gallblåsesjukdom, myasthenia gravis (inklusive vuxendebuterande form), sjukdom i neuromuskulära synapsen, butyrylkolinesterasbrist, hjärt-kärlsjukdom och hjärtsjukdom. Dessa kommer från samband i kunskapsgrafen och inte från läkemedlets produkttext.
- **Läkemedelsinteraktioner:** 11 interaktioner identifierade.
  - Måttliga: liposomalt morfin, lidokain (topikalt och oftalmiskt), bensokain (topikalt), kokain (topikalt och nasalt), tetrakain (oftalmiskt och topikalt), oxibuprokain (oftalmiskt), cinkokain (topikalt).
  - Lindrig: hyaluronidas.
  - De flesta måttliga interaktionerna gäller andra lokalanestetika, där risken är additiv systemtoxicitet.

För varningar och kontraindikationer enligt godkänd text, se produktresumén. Dessa uppgifter saknas i underlaget.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds enbart av en modellberäkning (evidensnivå L5), utan kliniska prövningar eller relevant litteratur. Dessutom är samtliga svenska godkännanden indragna och mekanistiskt samband saknas.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata (t.ex. via DrugBank) och analysera ett eventuellt mekanistiskt samband med gastroduodenit.
- Hämta och granska produktresumé med varningar och kontraindikationer från Läkemedelsverket (MPA), eftersom säkerhetsgranskningen inte kan genomföras utan dessa.
- Genomföra systematisk litteratursökning efter prekliniska och kliniska data om mepivakain vid gastroduodenit.
- Utreda administreringsväg, eftersom mepivakain finns som injektionsvätska och en möjlig väg för magtarmindikation inte är klarlagd.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

