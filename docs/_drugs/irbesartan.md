---
layout: default
title: Irbesartan
parent: Endast modellprediktion (L5)
nav_order: 234
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Irbesartan: predikterad ny indikation Malign hypertensiv njursjukdom (evidensnivå L5). Ursprunglig indikation: Hypertoni, högt blodtryck och diabetesnefropati"
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Irbesartan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

# Irbesartan: Från hypertoni och diabetesnefropati till malign hypertensiv njursjukdom

---

## Sammanfattning

Irbesartan är en angiotensin II-receptorblockerare (AT1) som ursprungligen används mot högt blodtryck och diabetesnefropati. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **malign hypertensiv njursjukdom**, men underlaget består enbart av en modellförutsägelse: **0 kliniska prövningar** och **0 publikationer** för just denna indikation. Förutsägelsen är dessutom i hög grad en omformulering av de befintliga indikationerna och inte en ny återanvändningssignal.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Hypertoni, högt blodtryck och diabetesnefropati (enligt kunskapsgrafen; godkännandetexter i den svenska registerdatan saknas) |
| Förutsagd ny indikation | Malign hypertensiv njursjukdom |
| TxGNN-förutsägelsepoäng | 99,3 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 15 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Någon detaljerad verkningsmekanismdata finns för närvarande inte tillgänglig. Baserat på känd information är irbesartan en AT1-receptorblockerare. Dess effekt vid hypertoni och diabetesnefropati är väl belagd, och mekanistiskt kan blockad av renin-angiotensinsystemet vara tillämpbar även vid hypertensiv njurskada.

Sambandet mellan den ursprungliga och den nya indikationen är nära. Malign hypertensiv njursjukdom är en allvarlig njurskada orsakad av mycket högt blodtryck, och renin-angiotensinsystemet spelar en central roll. Den höga poängen (0,993) beror sannolikt på att modellen följer kopplingar via hypertoninoder i kunskapsgrafen.

Det finns dock viktiga förbehåll. Malign hypertoni är ett akut tillstånd där ARB-läkemedel normalt inte är förstahandsbehandling. Förutsägelsen tillför därför litet nytt jämfört med de befintliga indikationerna.

**Andra förutsägelser i modellen:**
- **Malign renovaskulär hypertoni** (poäng 99,3 %, L5): Mekanismen är rimlig, men ARB kan försämra njurfunktionen akut vid dubbelsidig njurartärstenos eller stenos i en solitär njure, vilket är en betydande säkerhetsrisk. Inga studier finns.
- **Pulmonell hypertension med oklar multifaktoriell mekanism** (poäng 99,3 %, L5): Angiotensin II bidrar till kärlombyggnad i prekliniska modeller, men kopplingen är obevisad och sjukdomsgruppen är heterogen.
- **Pulmonell hypertension orsakad av lungsjukdom och/eller hypoxi** (poäng 99,3 %, L4): Se litteraturavsnittet nedan. Detta är den förutsägelse som har mest underlag, men underlaget är indirekt och prekliniskt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Den primära förutsägelsen (malign hypertensiv njursjukdom) saknar litteratur. Tabellen nedan gäller den fjärde förutsägelsen, pulmonell hypertension orsakad av lungsjukdom och/eller hypoxi. Endast studier där irbesartan eller AT1-blockad faktiskt studerats är medtagna.

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Översikt | Inflammopharmacology | Beskriver breda (pleiotropa) effekter av AT1-blockerare vid hypoxi orsakad av hjärtischemi. |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preklinisk (in vitro) | PLoS One | Irbesartan skyddade hjärtmuskelceller under hypoxisk stress. |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preklinisk (djur) | Sleep & Breathing | Irbesartan minskade sömnapné-inducerad apoptos i hjärtat och ökade Sirtuin 1. |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preklinisk (djur) | Am J Physiol Heart Circ Physiol | Irbesartan hämmade kranskärlens nybildning stimulerad av kronisk intermittent hypoxi hos nyfödda råttor. |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preklinisk (djur) | Biomed Pharmacother | Irbesartan lindrade lungartärförändringar i en råttmodell av kronisk höjdsjuka via kolesterolmetabolism. |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preklinisk (djur, typ ej klassificerad) | Eur Rev Med Pharmacol Sci | Irbesartan förbättrade oxidativ stress vid höghöjdsrelaterad pulmonell hypertension hos råttor via påverkan på tarmfloran. |
| [30525078](https://pubmed.ncbi.nlm.nih.gov/30525078/) | 2018 | Preklinisk (djur) | Regenerative Therapy | ARB-förbehandling upphävde den gynnsamma effekten av stamcellsark efter hjärtinfarkt; endast perifert relevant. |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preklinisk (djur) | Renal Failure | Irbesartan minskade ciklosporinorsakad njurtoxicitet; endast perifert relevant. |

Övriga hämtade artiklar (växtextrakt vid diabetesnjursjukdom samt en fallrapport om roxadustat) rör inte irbesartan och har uteslutits.

---

## Marknadsinformation Sverige

Samtliga 15 godkännanden är avregistrerade och inget gällande godkännande finns. Indikationstext saknas i registerdatan. De fem första godkännandena:

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 26629 | Irbesartan Sandoz | Filmdragerad tablett | – |
| 26352 | Irbesartan Actavis | Filmdragerad tablett | – |
| 26351 | Irbesartan Actavis | Filmdragerad tablett | – |
| 42423 | Irbesartan STADA | Filmdragerad tablett | – |
| 42424 | Irbesartan STADA | Filmdragerad tablett | – |

Bland de övriga avregistrerade godkännandena finns både enkomponentsprodukter (Accord, STADA) och kombinationer med hydroklortiazid (STADA, Actavis).

---

## Säkerhetsaspekter

**Kontraindikationer enligt kunskapsgrafen** (hämtade från kopplingar mellan läkemedel och sjukdom, inte från produktresumétext):
- Angioödem, inklusive läkemedelsutlöst och ärftligt angioödem
- Pankreatit
- Systemisk lupus erytematosus
- Muskelsjukdomar, myopati och rabdomyolys
- Diabetes mellitus och diabetisk ketoacidos
- Lågt blodtryck (hypotension)
- Anuri och förträngning eller förslutning av njurartär
- Gikt och hyperurikemi
- Hyperkalcemi, nefrokalcinos och rubbad fosformetabolism
- Hyperparatyreoidism
- Leverkoma och leverencefalopati
- Neonatal gulsot
- Kaliumbrist och familjär periodisk förlamning

Dessa uppgifter bör tolkas försiktigt, eftersom en del sannolikt avser hydroklortiazid i kombinationspreparaten snarare än irbesartan i sig.

**Läkemedelsinteraktioner:** Totalt 100 interaktioner identifierades. De viktigaste (allvarlig nivå):
- **Kaliumcitrat** (allvarlig) – risk för hyperkalemi
- **Kaliumbikarbonat** (allvarlig) – risk för hyperkalemi

Måttliga interaktioner förekommer bland annat med kortikosteroider (hydrokortison, dexametason, betametason, budesonid, triamcinolon), acetylsalicylsyra, SGLT2-hämmare (kanagliflozin, dapagliflozin, empagliflozin), insuliner (aspart, degludec), morfin, bupropion, aprepitant, dronabinol samt vissa laxermedel och tarmrengöringsmedel.

Se produktresumén för fullständig information om varningar och försiktighetsåtgärder.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen om malign hypertensiv njursjukdom stöds av ingen klinisk prövning eller publikation (L5) och är i huvudsak en omformulering av irbesartans befintliga indikationer. Dessutom är ARB inte förstahandsbehandling vid akut malign hypertoni.
- Den mest underbyggda riktningen är pulmonell hypertension orsakad av hypoxi (L4), men den bygger enbart på indirekta, prekliniska data.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket för varningar, kontraindikationer och godkända indikationer (saknas i nuvarande underlag).
- Komplettera verkningsmekanismdata från DrugBank.
- Genomföra en litteratur- och prövningssökning specifikt för malign hypertensiv njursjukdom för att bedöma om någon ny signal finns.
- Utföra prekliniska studier med lungkärlsspecifika mått för hypoxirelaterad pulmonell hypertension, följt av en säkerhets- och genomförbarhetsbedömning (med särskild uppmärksamhet på hypotension, njurfunktion och kaliumnivåer).
- Notera att alla svenska godkännanden är avregistrerade, vilket påverkar möjligheten till praktisk användning och måste utredas.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

