---
layout: default
title: Apixaban
parent: Endast modellprediktion (L5)
nav_order: 37
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "APIXABAN"
predicted_indications: ["migraine disorder"]
description: "Apixaban: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Apixaban
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

## Apixaban: Migrän (migraine disorder)
{: .text-alpha }

---

### Sammanfattning

Apixaban är en direkt faktor Xa-hämmare (blodförtunnande läkemedel) som finns som filmdragerad tablett. TxGNN-modellen förutsäger att det kan vara effektivt mot **migrän (migraine disorder)**, men evidensen är mycket svag: ingen studie stöder att apixaban lindrar migrän. Den enda kliniska prövningen i underlaget gäller stroke-prevention vid öppetstående foramen ovale, och de två fallrapporterna om apixaban beskriver migrän med aura som förvärrades eller inte försvann under behandling. Evidensnivån är **L5**.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 0.9902 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: minst 18) |
| Antal godkännanden | minst 20 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

Det finns ingen detaljerad uppgift om verkningsmekanism i de data som sammanställts för denna rapport. Apixaban hämmar koagulationsfaktor Xa och minskar därmed trombbildning. Något direkt mekanistiskt samband med migrän är inte fastställt.

En möjlig indirekt koppling är att migrän med aura har samband med paradoxal embolism via öppetstående foramen ovale (PFO) och med proteotrombotiska tillstånd såsom antifosfolipidantikroppar. I sådana undergrupper skulle antitrombotisk behandling kunna minska migränbördan. Det är dock en hypotes om en särskild undergrupp, inte en generell antimigränmekanism.

De tillgängliga fallrapporterna pekar i olika riktningar eller mot förvärring under apixaban. Det antyder att eventuell nytta inte är en klasseffekt för faktor Xa-hämmare. Den höga modellpoängen bör därför tolkas med stor försiktighet.

---

### Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fas 3 | Avslutad | 664 | Jämför förslutning av PFO eller antikoagulantia med trombocythämmare för att förebygga återfall av stroke. Migrän är varken huvudsyfte eller effektmått, och det framgår inte att apixaban var den antikoagulant som studerades. Kan inte räknas som evidens för migrän. |

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospektiv studie (75 patienter) | Lupus | Antitrombotisk behandling vid svårbehandlad migrän med antifosfolipidantikroppar. Det går inte att bekräfta att apixaban ingick. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Fallrapport | Headache | Kvinna med migrän med aura som var symtomfri i 12 år på warfarin. Symtomen återkom inom 3 veckor efter byte till apixaban och försvann igen när warfarin återinsattes. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Fallrapport med litteraturgenomgång | The Neurologist | Migrän med aura som förvärrades efter start av apixaban. Litteraturen om direkta orala antikoagulantia vid migrän är knapphändig och motsägelsefull. |

---

### Marknadsinformation Sverige

Apixaban har minst 20 registrerade godkännanden i Sverige (listan kan vara ofullständig), varav 18 giltiga och 2 avregistrerade. Nedan visas ett urval av de huvudsakliga godkännandena. Indikationstext finns inte registrerad i de lokala uppgifterna.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 64399 | Apixaban Cipla | Filmdragerad tablett | Uppgift saknas |
| 65249 | Apixaban Viatris Pharma | Filmdragerad tablett | Uppgift saknas |
| 60455 | Apixaban Viatris | Filmdragerad tablett | Uppgift saknas |
| 63832 | Apixaban Zentiva | Filmdragerad tablett | Uppgift saknas |
| 63542 | Apixaban Teva GmbH | Filmdragerad tablett | Uppgift saknas |

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Sammanlagt 100 interaktioner är registrerade. Bland de viktigaste med allvarlig (Major) nivå finns acetylsalicylsyra, kobicistat, deferasirox, ibritumomab tiuxetan och tositumomab. Flera interaktioner av måttlig nivå finns också, bland annat med klaritromycin, deksametason, aprepitant, mikonazol och klotrimazol.

Se i övrigt produktresumén för varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Ingen studie visar nytta av apixaban vid migrän, och de två fallrapporterna om apixaban beskriver förvärrad eller kvarstående migrän med aura. Evidensnivån är L5 trots den höga modellpoängen.

**För att gå vidare krävs:**
- Kontrollerade studier som direkt undersöker apixaban vid migrän, helst i definierade undergrupper (PFO, antifosfolipidantikroppar).
- Klarhet i verkningsmekanism och varför effekten verkar skilja sig mellan warfarin och faktor Xa-hämmare.
- Genomgång av produktresumén för säkerhetsinformation, eftersom varningar och kontraindikationer saknas i de sammanställda data.

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

