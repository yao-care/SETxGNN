---
layout: default
title: Rivastigmine
parent: Endast modellprediktion (L5)
nav_order: 384
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "rivastigmine"
predicted_indications: ["glaucoma"]
description: "Rivastigmine: predikterad ny indikation Glaucoma (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Rivastigmine
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

## Rivastigmine: Glaucoma
{: .text-alpha }

---

## Sammanfattning

Rivastigmin är en kolinesterashämmare som ursprungligen används vid Alzheimers sjukdom och närliggande neurodegenerativa tillstånd. TxGNN-modellen förutsäger att det kan vara effektivt mot **glaukom**, med en mycket hög modellpoäng. Det finns **inga kliniska prövningar** och **3 publikationer** (varav en prekliniskt djurstudie på kanin), så evidensen är än så länge mycket begränsad.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Glaucoma |
| TxGNN-förutsägelsepoäng | 0.9927 |
| Evidensnivå | L5 (endast prekliniska studier och mekanismstudier) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 18 av 18) |
| Antal godkännanden | 18 (giltiga: 18) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Rivastigmin hämmar enzymerna acetylkolinesteras och butyrylkolinesteras. Det gör att signalsubstansen acetylkolin bryts ner långsammare och att den kolinerga aktiviteten ökar. Observera att uppgifter om verkningsmekanism saknas i de data som sammanställts för rapporten. Beskrivningen här bygger därför på läkemedlets allmänt kända farmakologi.

Vid glaukom är det förhöjda ögontrycket den viktigaste behandlingsbara riskfaktorn. Kolinerga läkemedel som pilokarpin och fysostigmin sänker trycket genom att öka kontraktionen i ciliarmuskeln och förbättra avflödet av kammarvatten via trabekelverket. Rivastigmin verkar på samma övergripande sätt genom att öka kolinerg aktivitet i ögats vävnad.

Det finns stöd för resonemanget i en studie från 2000, där lokalt applicerat rivastigmin sänkte ögontrycket hos kaniner med normalt tryck. En översikt från 2024 om kolinerga ämnen och ögontryck stöder klassresonemanget. Den höga modellpoängen stämmer med mekanismen men är en beräkning och inget bevis för effekt hos människa.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preklinisk djurstudie (kanin) | Journal of Ocular Pharmacology and Therapeutics | Lokalt rivastigmin, en selektiv kolinesterashämmare, sänkte ögontrycket hos kaniner med normalt tryck. |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Översikt | Frontiers in Molecular Biosciences | Går igenom kolinerga ämnen för sänkning av ögontryck. Godkända M3-agonister har systemiska kolinerga biverkningar som begränsar användningen. |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Översikt (patentlitteratur) | Expert Opinion on Therapeutic Patents | Beskriver acetylkolinesterashämmare och reaktivatorer. Mild hämning har terapeutisk relevans vid bland annat Alzheimers sjukdom, myasthenia gravis och glaukom. |

---

## Marknadsinformation Sverige

De fem första visas nedan. Indikationstext saknas i registret.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 62230 | Rivastigmin Abacus Medicine | Depotplåster | Uppgift saknas |
| 58673 | Rivastor | Depotplåster | Uppgift saknas |
| 48948 | Rigmin | Depotplåster | Uppgift saknas |
| 61635 | Rivastigmin STADA Arzneimittel | Depotplåster | Uppgift saknas |
| 46274 | Rivastor | Depotplåster | Uppgift saknas |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): epilepsi, sjukdom i basala ganglierna, fokal handdystoni, blefarospasm, kroniskt obstruktiv lungsjukdom (KOL), astma (inklusive allergisk och intrinsic astma), diarrésjukdom, plötsligt hjärtstopp, hjärtats retledningssjukdom, anorexia nervosa, aktivt magsår, urinvägsobstruktion, sjuk sinusknutesyndrom, parkinsonism/Parkinsons sjukdom samt AV-block.
- **Läkemedelsinteraktioner**: 170 kända interaktioner. Den enda av allvarlig grad bland de redovisade är **bupropion** (Major). Måttliga interaktioner förekommer bland annat med antikolinerga medel (atropin, hyoscyamin, glykopyrronium, dicyklomin, trospium), H2-blockerare (famotidin, ranitidin, cimetidin), loperamid, metronidazol, klaritromycin, levofloxacin samt 5-HT3-antagonister (dolasetron, palonosetron).
- **Förväntade kolinerga effekter vid ögonanvändning**: mag-tarmbesvär, långsam hjärtfrekvens, irritation på ögats yta och pupillsammandragning.

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensen består av en djurstudie på kanin och två översikter, utan humandata. Den höga modellpoängen är enbart en beräkning.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket för varningar och kontraindikationer samt verkningsmekanism från DrugBank.
- Preklinisk bekräftelse av effekt på ögontryck i fler modeller, inklusive modeller med förhöjt tryck.
- Utveckling och säkerhetsprövning av en lokal ögonberedning (tolerans, systemisk exponering, påverkan på hjärtfrekvens).
- Jämförelse med befintlig glaukombehandling för att bedöma det kliniska mervärdet.
- Därefter en tidig klinisk prövning (fas 1/2) på ögontryck hos människa.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

