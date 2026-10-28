---
layout: default
title: Warfarin
parent: Endast modellprediktion (L5)
nav_order: 453
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
monitor_inn: "warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Warfarin: predikterad ny indikation Heparinkofaktor 2-brist (heparin cofactor 2 deficiency) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Warfarin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

## Warfarin: Heparinkofaktor 2-brist (heparin cofactor 2 deficiency)
{: .text-alpha }

---

### Sammanfattning

Warfarin är ett blodförtunnande läkemedel (vitamin K-antagonist) som ursprungligen används vid lungemboli, trombossjukdom och intrakraniell emboli. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt vid **heparinkofaktor 2-brist** (högsta rankade förutsägelse), men det finns **inga kliniska prövningar** och endast **3 fallrapporter** som stöder just denna riktning. Den bäst belagda förutsägelsen är i stället **trombofili** (1 fas 3-prövning och 19 publikationer), vilket i hög grad är en förlängning av läkemedlets befintliga indikation.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Heparinkofaktor 2-brist (heparin cofactor 2 deficiency) |
| TxGNN-förutsägelsepoäng | 0.9987 |
| Evidensnivå | L5 (endast fallrapporter) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Baserat på allmänt känd information hämmar warfarin de vitamin K-beroende koagulationsfaktorerna II, VII, IX och X samt protein C och S. Därmed minskar det kroppens förmåga att bilda trombin och blodproppar.

Heparinkofaktor 2-brist är en ärftlig trombofili, alltså en medfödd benägenhet att bilda blodproppar. Långtidsbehandling med antikoagulantia för att förebygga nya proppar är därför mekanistiskt rimlig. Sambandet till warfarins ursprungliga indikationer (lungemboli och trombossjukdom) är mycket nära: det handlar snarare om samma användning i en särskild patientgrupp än om en helt ny användning.

Observera att flera andra förutsägelser har mycket svagare stöd. Reumatoid artrit, fibrocystisk bröstsjukdom och benign mammär dysplasi framstår som sannolikt falskt positiva signaler (se nedan).

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för heparinkofaktor 2-brist för närvarande.

För den närliggande förutsägelsen **trombofili** finns en prövning:

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Fas 3 | Okänd | 300 | Randomiserad studie om D-dimer-styrd förlängning av sekundärprofylax efter oprovocerad djup ventrombos. Gäller behandlingstidens längd, inte warfarin mot kontroll. |

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Fallrapport | Kyobu geka | Trombos i höger kammare hos en 14-årig flicka med ärftlig heparinkofaktor II-brist. Propp avlägsnades kirurgiskt. |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Fallrapport | Nihon Kyobu Shikkan Gakkai zasshi | Kvinna med medfödd antitrombinbrist och upprepade proppar, behandlad med warfarin i 7 år. Byte till heparin efter inläggning. |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Fallrapport (familj) | Journal of UOEH | Familj med multipel trombos där känd ärftlig trombofili uteslutits. Warfarin startades hos ett barn som ändå fick ny propp. |

Litteraturen består av tre små japanska fallrapporter från 1990–2001 utan kontrollerade data. Därmed kan inte effekt eller dosering styrkas.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 6897 | Waran (Orifarm Healthcare A/S) | Tablett | Indikationstext saknas; indraget |
| 42966 | Warfarin Orion (Orion Corporation) | Tablett | Indikationstext saknas; indraget |

Detta bör verifieras.

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): bl.a. leversvikt och leversjukdom, nedsatt njurfunktion, blodkoagulationssjukdom, kronisk hjärtsvikt, hypertoni, hypotyreos, nefrotiskt syndrom, kolestas, anemi, hyperlipidemi, psykossjukdomar, substansberoende och kronisk diarrésjukdom.
- **Läkemedelsinteraktioner**: totalt 865 registrerade interaktioner. Bland de som redovisats finns två med **allvarlig (Major)** nivå: **acetylsalicylsyra** och **metronidazol**. Flera **måttliga** interaktioner finns, t.ex. med ranitidin, rabeprazol, doxycyklin, metformin, amoxicillin, bupropion, aprepitant, mesalazin samt kortikosteroider (hydrokortison, dexametason, betametason, triamcinolon, budesonid).
- **Övrigt**: i litteraturen beskrivs warfarininducerad hudnekros, en sällsynt men allvarlig komplikation som kopplas till protein C-brist. Läkemedlet interagerar dessutom med många läkemedel genom CYP2C9 (t.ex. leflunomid och danazol).

Se produktresumén för fullständiga varningar och kontraindikationer, eftersom dessa inte fanns tillgängliga i underlaget.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen om heparinkofaktor 2-brist stöds endast av tre små fallrapporter (L4) och är i praktiken en förlängning av warfarins befintliga indikation, inte en ny användning. Förutsägelserna för reumatoid artrit, fibrocystisk bröstsjukdom och benign mammär dysplasi bedöms som sannolikt falskt positiva, eftersom de bygger på läkemedelsinteraktioner och inte på terapeutisk effekt.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket för närvarande blockerar säkerhetsgranskningen.
- Hämta verkningsmekanismdata från DrugBank.
- Verifiera marknadsstatus, eftersom båda godkännandena är indragna.
- Sammanställa kontrollerade data eller kohortstudier för warfarin vid ärftlig trombofili, särskilt jämfört med direktverkande orala antikoagulantia (DOAK), som enligt en ISTH-kommunikation från 2024 allt oftare används i stället.
- Bedöma om trombofili (L1-förutsägelsen, NCT00895505) är ett mer meningsfullt spår att utreda vidare, trots att prövningens status är okänd.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

