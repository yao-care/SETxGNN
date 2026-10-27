---
layout: default
title: Pilocarpine
parent: Endast modellprediktion (L5)
nav_order: 350
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Pilocarpine: predikterad ny indikation Primärt ärftligt glaukom (evidensnivå L5). Ursprunglig indikation: Öppenvinkelglaukom, okulär hypertension (enligt kunskapsgrafen"
---

# Pilocarpine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

## Pilokarpin: Från öppenvinkelglaukom och okulär hypertension till primärt ärftligt glaukom
{: .text-alpha }

---

### Sammanfattning

Pilokarpin är ett muskarint läkemedel som ursprungligen användes för att behandla öppenvinkelglaukom och okulär hypertension (förhöjt ögontryck). TxGNN-modellen förutsäger att det kan vara effektivt mot **primärt ärftligt glaukom**, men för närvarande finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder denna riktning. Förutsägelsen bygger enbart på modellen, och den ligger mycket nära den ursprungliga indikationen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Öppenvinkelglaukom, okulär hypertension (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Primärt ärftligt glaukom |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 6 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

Pilokarpin är en muskarin (M3) agonist. Det drar ihop ciliarmuskeln och ökar avflödet av kammarvatten via trabekelverket, vilket sänker ögontrycket. Det är grunden för den etablerade användningen vid öppenvinkelglaukom och okulär hypertension. Någon detaljerad verkningsmekanismdata från kuraterade källor finns inte i underlaget, så beskrivningen ovan bygger på allmänt känd farmakologi.

Den förutsagda indikationen, primärt ärftligt glaukom, är sannolikt nästan identisk med den ursprungliga indikationen. Den höga poängen (0,998) speglar därför troligen att diagnosen ligger nära befintliga glaukomdiagnoser i kunskapsgrafen, snarare än en ny mekanism.

Mekanismen kan vara tillämpbar, men inte säkert. Ärftliga former (till exempel MYOC- eller CYP1B1-relaterade) kan innebära felbildning av kammarvinkeln. Vid kongenitalt eller utvecklingsrelaterat glaukom kan behandling med mios (pupillsammandragande medel) som förbättrar avflödet vara mindre effektiv. Sambandet är alltså rimligt men obekräftat.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10171 | Pilokarpin Karo Pharma | Ögondroppar, lösning i endosbehållare | Ingen indikationstext angiven |
| 10170 | Pilokarpin Karo Pharma | Ögondroppar, lösning i endosbehållare | Ingen indikationstext angiven |
| 13407 | Salagen | Filmdragerad tablett | Ingen indikationstext angiven |
| 11964 | Fotil forte | Ögondroppar, lösning i endosbehållare | Ingen indikationstext angiven |
| 11655 | Fotil | Ögondroppar, lösning | Ingen indikationstext angiven |

Ytterligare ett indraget godkännande (Fotil forte, ögondroppar, lösning, nr 11763) finns, vilket ger totalt 6 godkännanden. Samtliga är indragna.

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumétext): Följande tillstånd är kopplade till pilokarpin som kontraindikationer:
  - Ögon: trångvinkelglaukom (vinkelslutsglaukom), keratit, keratokonjunktivit, irit, iridocyklit, uveit, näthinneavlossning
  - Luftvägar: astma, kroniskt obstruktiv lungsjukdom (KOL), andra bronkiella sjukdomar
  - Lever och gallvägar: leversvikt, gallsten (kolelitiasis, kolecystolitiasis, koledokolitiasis), kolecystit, gallvägssjukdom, obstruktiv gulsot
  - Njurar: njursten (nefrolitiasis), akut urátnefropati
- **Läkemedelsinteraktioner**: Totalt 102 interaktioner är registrerade. De viktigaste är av måttlig grad och gäller andra antikolinerga läkemedel, eftersom effekterna motverkar varandra:
  - Atropin (även ögonpreparat), hyoscyamin, skopolamin (även ögonpreparat)
  - Glykopyrronium (även topikalt), klidinium, dicyklomin
  - Mepenzolat, metskopolamin, propantelin, trospium
  - Interaktioner med okänd grad är registrerade för bland annat pantoprazol, omeprazol, lansoprazol, klotrimazol, morfin, metformin och adrenalin.

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds enbart av modellen (L5), utan kliniska prövningar eller litteratur. Den ligger dessutom mycket nära den ursprungliga indikationen och tillför därför sannolikt inget nytt. Alla svenska godkännanden är indragna.

**För att gå vidare krävs:**
- Hämta produktresumétext (varningar, kontraindikationer och godkända indikationer) från Läkemedelsverket, eftersom säkerhetsgranskningen annars inte kan genomföras.
- Komplettera verkningsmekanismen från kuraterade källor, till exempel DrugBank.
- Klargöra om primärt ärftligt glaukom skiljer sig från öppenvinkelglaukom på ett kliniskt meningsfullt sätt, särskilt med avseende på kammarvinkelns utveckling.
- Söka litteratur och kliniska prövningar för pilokarpin vid ärftliga och kongenitala glaukomformer.
- Bedöma administreringsväg och tillgänglighet, eftersom inga godkända ögonpreparat för närvarande är marknadsförda i Sverige.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

