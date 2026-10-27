---
layout: default
title: Urofollitropin
parent: Endast modellprediktion (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Urofollitropin: predikterad ny indikation Migränsjukdom (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext registrerad i godkännandedata (använd produktre…"
monitor_inn: "UROFOLLITROPIN"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "His bundle tachycardia", "restless legs syndrome", "obsolete neurogenic bladder (disease)", "multifocal atrial tachycardia (disease)", "postural orthostatic tachycardia syndrome", "migraine with or without aura, susceptibility to", "Raynaud disease"]
---

# Urofollitropin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

## Urofollitropin: Från (ingen ursprunglig indikation angiven) till migränsjukdom
{: .text-alpha }

---

## Sammanfattning

Urofollitropin är ett urinframställt follikelstimulerande hormon (FSH, ett gonadotropin) som används vid ägglossningsinduktion och assisterad befruktning. I de data som sammanställts för denna rapport finns dock ingen godkänd indikationstext registrerad. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **migränsjukdom**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder förutsägelsen. Den är därför enbart en modellbaserad hypotes.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext registrerad i godkännandedata (använd produktresumén) |
| Förutsagd ny indikation | Migränsjukdom (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,85 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 6 (samtliga avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är urofollitropin ett gonadotropin med FSH-aktivitet. Dess effekt vid ägglossningsinduktion och assisterad befruktning är känd, men något mekanistiskt samband med migrän är inte belagt i underlaget.

Det enda tänkbara sambandet är indirekt och spekulativt: hormonella svängningar, framför allt i östrogennivåer, är kända för att påverka migrän. FSH-behandling förändrar östrogennivåerna, men det betyder inte att läkemedlet skulle lindra migrän. Det kan lika gärna vara en riskfaktor.

Poängen från TxGNN bygger på grafbaserade samband i en kunskapsgraf och utgör inte klinisk evidens. Närliggande förutsägelser, som migrän med hjärnstamsaura och genetisk migränbenägenhet, speglar sannolikt samma signal och är inte oberoende stöd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Samtliga sex godkännanden är avregistrerade och ingen produkt är för närvarande marknadsförd med giltigt godkännande. Samtliga tillhör IBSA Farmaceutici Italia S.r.l.

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 22944 | Fostimon | Pulver och vätska till injektionsvätska, lösning | Avregistrerad |
| 46427 | Fostimon Set | Pulver och vätska till injektionsvätska, lösning | Avregistrerad |
| 47701 | Fostimon Set | Pulver och vätska till injektionsvätska, lösning | Avregistrerad |
| 46428 | Fostimon Set | Pulver och vätska till injektionsvätska, lösning | Avregistrerad |
| 22943 | Fostimon | Pulver och vätska till injektionsvätska, lösning | Avregistrerad |

Ytterligare ett godkännande (47702, Fostimon Set) finns också registrerat och är avregistrerat. Ingen godkänd indikationstext finns tillgänglig i data.

---

## Säkerhetsaspekter

- **Läkemedelsinteraktioner**: En interaktion av måttlig allvarlighetsgrad är registrerad, med **ganirelix** (källa: DDInter). Ganirelix är en GnRH-antagonist som används i fertilitetsbehandling, så kombinationen är relevant i den kliniska miljö där urofollitropin används.

Varnings- och kontraindikationsdata saknas i de data som sammanställts. Se produktresumén för övrig säkerhetsinformation.

---

## Övriga förutsägelser med högst poäng

Samtliga övriga förutsägelser bland de tio högst rankade saknar också kliniska prövningar och litteratur (evidensnivå L5). Ingen av dem har ett mekanistiskt stöd i underlaget.

| Rang | Sjukdom | TxGNN-poäng | Bedömning |
|------|---------|------|-----------|
| 2 | Migrän med hjärnstamsaura | 99,81 % | Undertyp av migrän, sannolikt samma signal som rang 1 |
| 3 | Cauda equina-syndrom | 99,78 % | Ingen rimlig mekanism, sannolikt grafartefakt |
| 4 | His bundle-takykardi | 99,69 % | Inget känt samband med FSH |
| 5 | Restless legs syndrome | 99,69 % | Dopamin- och järnrelaterad patofysiologi, inget FSH-samband |
| 6 | Neurogen blåsa (föråldrad term) | 99,64 % | Föråldrad term i ontologin, lågt värde som mål |
| 7 | Multifokal förmakstakykardi | 99,54 % | Inget känt samband |
| 8 | Posturalt ortostatiskt takykardisyndrom (POTS) | 99,52 % | Svag, spekulativ hormonell koppling |
| 9 | Migrän med eller utan aura, benägenhet | 99,52 % | Dubblerar sannolikt migränsignalen |
| 10 | Raynauds sjukdom | 99,50 % | Inget FSH-förmedlat samband känt |

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen om migrän bygger enbart på en grafbaserad modellpoäng utan kliniska prövningar, litteratur eller etablerad verkningsmekanism. Dessutom saknas giltiga godkännanden i Sverige och säkerhetsdata för läkemedlet är ofullständiga.

**För att gå vidare krävs:**
- Verkningsmekanismdata för läkemedlet (till exempel via DrugBank).
- Varningar och kontraindikationer från produktresumén (Läkemedelsverket), vilket är ett blockerande dataglapp för säkerhetsbedömning.
- Litteraturgenomgång av sambandet mellan FSH/östrogenfluktuationer och migrän, inklusive om hormonbehandling snarare ökar migränrisken.
- Prekliniska eller mekanistiska studier som stödjer en terapeutisk hypotes, innan kliniska studier övervägs.
- Bedömning av om en ny produkt skulle behöva godkännas på nytt, eftersom alla nuvarande godkännanden är avregistrerade.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

