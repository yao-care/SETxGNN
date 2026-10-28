---
layout: default
title: Empagliflozin
parent: Endast modellprediktion (L5)
nav_order: 160
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
description: "Empagliflozin: predikterad ny indikation Fokalt stelbensyndrom (focal stiff limb syndrome) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Empagliflozin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

## Empagliflozin: Fokalt stelbensyndrom (focal stiff limb syndrome)
{: .text-alpha }

---

### Sammanfattning

Empagliflozin ursprungligen användes för att behandla **typ 2-diabetes mellitus**. TxGNN-modellen (djupinlärning) förutsäger att läkemedlet kan vara effektivt mot **fokalt stelbensyndrom** (focal stiff limb syndrome), med en förutsägelsepoäng på 0,9906. Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder förutsägelsen, vilket innebär att den enbart bygger på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Fokalt stelbensyndrom (focal stiff limb syndrome) |
| TxGNN-förutsägelsepoäng | 0.9906 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 6 av 6) |
| Antal godkännanden | 6 (giltiga: 6) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Baserat på allmän farmakologisk kunskap är empagliflozin en SGLT2-hämmare, som sänker blodsockret genom att minska återupptaget av glukos i njurarna. Effekten vid typ 2-diabetes är väl belagd.

Fokalt stelbensyndrom hör till spektrumet av stelbenssyndrom (stiff-person-spektrumet). Det är en sällsynt autoimmun, neurologisk sjukdom som ofta har samband med anti-GAD65-antikroppar och nedsatt GABA-hämning. Det finns ingen känd väg som kopplar SGLT2-hämning till denna mekanism.

Ett möjligt skäl till den höga poängen är att anti-GAD-autoimmunitet ofta förekommer tillsammans med diabetes, framför allt typ 1. Poängen kommer från TxGNN-modellen (djupinlärning) och kan spegla likheter som modellen har lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Detta är en spekulation och stöds inte av underlaget. Samma poäng ges för klassiskt stelmanssyndrom (0,9906), vilket tyder på att de två förutsägelserna delar samma mönster i modellen och inte är oberoende signaler.

Andra förutsagda indikationer i modellen är klassiskt stelbensyndrom och opsismodysplasi. Inte heller för dessa finns studier eller litteratur. För opsismodysplasi (orsakad av INPPL1-/SHIP2-mutationer) finns ett löst samband via insulinsignalering, men empagliflozin verkar via njurens glukosåterupptag och påverkar inte den signalvägen.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 67533 | Empagliflozin Labiana | Filmdragerad tablett | Indikationstext saknas (indraget) |
| 67534 | Empagliflozin Labiana | Filmdragerad tablett | Indikationstext saknas (indraget) |
| 66345 | Empagliflozin Devatis | Filmdragerad tablett | Indikationstext saknas (indraget) |
| 65282 | Hynica | Filmdragerad tablett | Indikationstext saknas (indraget) |
| 66346 | Empagliflozin Devatis | Filmdragerad tablett | Indikationstext saknas (indraget) |

Totalt finns 6 godkännanden, alla indragna. Det sjätte (65281, Hynica, Adalvo Limited) visas inte i tabellen eftersom högst 5 listas.

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner:** Totalt har 100 interaktioner identifierats. De flesta av de som visas är av måttlig grad. Exempel:

- **Måttlig:** fenylefrin, acebutolol, acetazolamid, formoterol, pseudoefedrin, nifedipin, adrenalin, etinylestradiol, hydrokortison, salbutamol, etanol, fosamprenavir, fosinopril, fosfenytoin, furosemid, gemifloxacin
- **Lindrig:** hydrokortison (topikalt), alclometason (topikalt)

Se produktresumén för information om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellpoäng (L5). Det saknas kliniska prövningar och litteratur, och ingen rimlig mekanistisk koppling mellan SGLT2-hämning och fokalt stelbensyndrom har kunnat identifieras. Dessutom är samtliga svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata (MOA) från DrugBank för att kunna analysera ett eventuellt mekanistiskt samband.
- Hämta varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA) för en fullständig säkerhetsbedömning.
- Genomföra en systematisk litteratur- och prövningssökning samt prekliniska studier som kan ge stöd för en koppling till stelbenssyndrom.
- Utreda om förutsägelsen speglar ett verkligt samband eller enbart likheter som TxGNN-modellen har lärt sig mellan relaterade sjukdomar.
- Klargöra marknadsstatus, eftersom inget godkännande för närvarande är giltigt i Sverige.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

