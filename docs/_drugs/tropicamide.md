---
layout: default
title: Tropicamide
parent: Endast modellprediktion (L5)
nav_order: 441
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tropicamide: predikterad ny indikation Cauda equina-syndrom (evidensnivå L5). Ursprunglig indikation: Cykloplegi (enligt kunskapsgrafen"
monitor_inn: "tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
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

## Tropikamid: Från cykloplegi till cauda equina-syndrom
{: .text-alpha }

---

### Sammanfattning

Tropikamid är ett kortverkande antimuskarint läkemedel som ursprungligen användes för **cykloplegi** (pupillvidgning och lamning av ackommodationen vid ögonundersökning). TxGNN-modellen förutsäger att det kan vara effektivt mot **cauda equina-syndrom**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder detta. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Cykloplegi (enligt kunskapsgrafen; godkännandenas indikationstexter är tomma) |
| Förutsagd ny indikation | Cauda equina-syndrom |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 4 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för rapporten. Tropikamid är dock känt som en muskarinreceptorantagonist, och farmakologidata visar bindning till muskarinreceptorerna M2, M3, M4 och M5. Dess effekt vid cykloplegi och mydriasis är väl etablerad.

Sambandet mellan den ursprungliga och den nya indikationen är svagt. Cauda equina-syndrom är en neurologisk akutsjukdom där nerverötterna i ryggmärgskanalens nedre del är komprimerade. Blås-, tarm- och känselstörningarna beror på själva nervkompressionen, och ett antimuskarint läkemedel påverkar inte den. I bästa fall skulle det kunna lindra symtom som överaktiv blåsmuskel.

Den höga poängen (0,995) är sannolikt en följd av grafbaserade samband, till exempel gemensamma kopplingar till neurogen blåsdysfunktion, och inte av kliniskt stöd. Tropikamid ges dessutom som ögondroppar med mycket låg systemisk exponering, vilket försvagar resonemanget ytterligare.

**Övriga förutsagda indikationer** (alla med evidensnivå L5, utan studier eller litteratur):

| Förutsagd indikation | Poäng | Kommentar |
|------|------|------|
| Neurogen blåsa (föråldrad term i ontologin) | 99,1 % | Antimuskarina läkemedel som oxybutynin och tolterodin är redan etablerad behandling. Termen bör uppdateras, till exempel till neurogen detrusoröveraktivitet, före vidare bedömning. |
| Irritabel tarm (IBS) | 99,1 % | Antimuskarina och spasmolytiska läkemedel används redan mot IBS-smärta. Tropikamid saknar dokumenterad användning i mag-tarmkanalen. |

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

Samtliga fyra godkännanden är indragna. Ingen indikationstext finns registrerad.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10013 | Tropikamid Bausch & Lomb | Ögondroppar, lösning i endosbehållare | – |
| 7540 | Mydriacyl | Ögondroppar, lösning | – |
| 23485 | Mydriasert | Ögonlamell | – |
| 51088 | Mydrane | Injektionsvätska, lösning | – |

---

### Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer har inte kunnat sammanställas. Se produktresumén för säkerhetsinformation.

**Kontraindikationer enligt kunskapsgrafen** (kommer från grafens samband, inte från produkttext):
- Högt blodtryck (hypertoni)
- Glaukom: öppenvinkelglaukom, trångvinkelglaukom och okulär hypertension
- Diabetes mellitus och diabetesketoacidos
- Plötsligt hjärtstopp och hjärtats retledningssjukdomar
- Hypertyreos, Graves sjukdom och tyreotoxikos
- Hjärtmuskelischemi och kranskärlssjukdom

**Läkemedelsinteraktioner:** 10 möjliga interaktioner har identifierats, men allvarlighetsgraden är inte angiven för någon av dem. De berörda läkemedlen är atropin, kaliumklorid, vankomycin, simvastatin, prednisolon, famotidin, warfarin, lidokain, flukonazol och brimonidin. Atropin är ett annat antimuskarint läkemedel, så additiva antikolinerga effekter är särskilt värda att uppmärksamma.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds av varken kliniska prövningar eller litteratur (L5). Mekanismen är svag för cauda equina-syndrom, och tropikamid har knappt någon systemisk exponering som ögonläkemedel. Dessutom är alla svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta produktresumé med varningar och kontraindikationer, vilket för närvarande blockerar säkerhetsbedömningen.
- Komplettera verkningsmekanismen från DrugBank.
- Göra en systematisk litteratur- och prövningssökning för cauda equina-syndrom.
- Utvärdera om en annan förutsagd indikation (till exempel neurogen detrusoröveraktivitet efter uppdaterad term) är mer rimlig, med hänsyn till att godkända antimuskarina alternativ redan finns.
- Bedöma administrationsväg och möjlig systemisk exponering för den nya indikationen.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

