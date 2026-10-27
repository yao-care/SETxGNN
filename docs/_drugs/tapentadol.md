---
layout: default
title: Tapentadol
parent: Endast modellprediktion (L5)
nav_order: 411
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tapentadol: predikterad ny indikation Migränsjukdom (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Ej angiven i de sammanställda data (indikationstexten saknas för alla…"
monitor_inn: "tapentadol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to"]
---

# Tapentadol
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

## Tapentadol: Från smärta (indikationstext saknas i registret) till migränsjukdom
{: .text-alpha }

---

## Sammanfattning

Tapentadol är ett opioid smärtstillande läkemedel som i Sverige har marknadsförts bland annat som Palexia, Palexia Depot och Tapimio Depot. Någon godkänd indikationstext finns inte i de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **migränsjukdom**, men det finns **inga kliniska prövningar** och **inga publikationer som direkt stöder** denna riktning. Den förutsägelsen bygger enbart på en modellberäkning.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i de sammanställda data (indikationstexten saknas för alla godkännanden) |
| Förutsagd ny indikation | Migränsjukdom (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 20 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda data. Utifrån allmänt känd information är tapentadol en agonist på my-opioidreceptorn och hämmar samtidigt återupptaget av noradrenalin. Båda mekanismerna påverkar centrala smärtbanor, och det är sannolikt det som ligger bakom modellens höga poäng.

Sambandet mellan den ursprungliga användningen (smärtlindring) och migrän är att båda involverar smärtsignalering i nervsystemet. Därför kan en modell som bygger på kunskapsgrafer koppla ihop dem. Poängen är mycket hög, men den visar främst likhet i grafen och inte faktisk klinisk nytta.

Det finns dessutom starka kliniska skäl till försiktighet. Opioider rekommenderas generellt inte vid migrän, eftersom de ger risk för läkemedelsöveranvändningshuvudvärk, förvärrad kronisk migrän och beroende. Mekanismen går därför inte att bekräfta som tillämpbar utifrån de data som finns.

Modellen förutsäger också närliggande tillstånd, bland annat migrän med hjärnstamsaura (99,6 %) och genetisk benägenhet för migrän (99,1 %). Dessa förutsägelser speglar sannolikt likheter mellan sjukdomsbeteckningar i modellen snarare än oberoende signaler för tapentadol.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

För migränsjukdom (huvudförutsägelsen) finns ingen relaterad litteratur tillgänglig för närvarande. Följande två publikationer hittades för den närliggande termen "genetisk benägenhet för migrän", men de är indirekta och utvärderar inte tapentadol vid migrän:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Översikt | Expert Opinion on Pharmacotherapy | Diskuterar NSAID och paracetamol som icke-opioida alternativ vid akut smärta, mot bakgrund av opioidkrisen. |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Kohortstudie | Drug, Healthcare and Patient Safety | Opioider rekommenderas inte rutinmässigt vid migrän på grund av risk för läkemedelsöveranvändningshuvudvärk och beroende. Studien beskriver samtidig användning av opioider med triptaner eller serotonerga antidepressiva (risk för serotonergt syndrom). |

---

## Marknadsinformation Sverige

Alla 20 godkännanden är indragna. Indikationstext saknas i registret. De fem första visas här:

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 61813 | Tapentadol Depot STADA | Depottablett | Ej angiven |
| 61815 | Tapentadol Depot STADA | Depottablett | Ej angiven |
| 65224 | Tapentadol Depot Zentiva | Depottablett | Ej angiven |
| 42621 | Palexia | Filmdragerad tablett | Ej angiven |
| 65225 | Tapentadol Depot Zentiva | Depottablett | Ej angiven |

Övriga godkännanden gäller bland annat Tapimio Depot (Neuraxpharm), Palexia Depot (Grünenthal) och Tapentadol Consilient Health.

---

## Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 120 interaktioner har identifierats. Exempel på de allvarligaste (nivå Major):
  - Morfin
  - Bupropion
  - Lorcaserin
  - Dietylpropion
  - Fentermin
  - Dolasetron
  - Palonosetron
- Interaktioner av medelsvår grad (Moderate) omfattar bland annat naloxon, atropin, hyoscyamin, glykopyrronium, dronabinol, nabilon och eluxadolin.
- Litteraturen (PMID 29760569) lyfter risken för serotonergt syndrom när opioider kombineras med triptaner eller serotonerga antidepressiva. Det är särskilt relevant vid migränbehandling.
- Läkemedelsöveranvändningshuvudvärk och beroende är kända risker med opioider vid migrän.

För varningar och kontraindikationer, se produktresumén.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen är enbart modellbaserad (L5) utan kliniska prövningar eller direkt litteratur. Opioider rekommenderas dessutom generellt inte vid migrän, och alla svenska godkännanden är indragna.

**För att gå vidare krävs:**
- Verkningsmekanismdata för tapentadol (hämtas från DrugBank).
- Varningar och kontraindikationer från produktresumén (hämtas från Läkemedelsverkets webbplats).
- Prekliniska studier och kontrollerade kliniska prövningar av tapentadol vid migrän.
- En bedömning av risken för läkemedelsöveranvändningshuvudvärk och serotonergt syndrom, samt jämförelse med etablerade migränbehandlingar.
- Klargörande av varför alla godkännanden är indragna och om en återlansering är aktuell.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

