---
layout: default
title: Ketamine
parent: Endast modellprediktion (L5)
nav_order: 243
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Ketamine: predikterad ny indikation Huvudvärkssjukdom (headache disorder) (evidensnivå L5). Ursprunglig indikation: Ej angiven (godkännandena saknar indikationstext)"
monitor_inn: "ketamine"
predicted_indications: ["headache disorder"]
---

# Ketamine
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

## Ketamin: Från ej angiven ursprunglig indikation till huvudvärkssjukdom (headache disorder)
{: .text-alpha }

---

## Sammanfattning

Ketamin (Ketamin Abcur, Ketalar) har fyra svenska godkännanden i form av injektionsvätska, men i de data som sammanställts för rapporten finns ingen godkänd indikationstext, så den ursprungliga användningen kan inte anges därifrån. TxGNN-modellen förutsäger att ketamin kan vara effektivt mot **huvudvärkssjukdom** (poäng 99,3 %), med **9 kliniska prövningar** och **18 publikationer** som för närvarande hör till denna riktning. Endast en fas 3-studie (THINK) är avslutad, och den andra fas 3-studien (KetHead) rekryterar fortfarande. Evidensen är därför lovande men inte avgörande.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven (godkännandena saknar indikationstext) |
| Förutsagd ny indikation | Huvudvärkssjukdom (headache disorder) |
| TxGNN-förutsägelsepoäng | 99,3 % |
| Evidensnivå | L2 (se motivering nedan) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 4 (alla indragna, 0 giltiga) |
| Rekommenderat beslut | Fortsätt med försiktighet |

**Om evidensnivån:** Nivå L1 kräver minst två avslutade fas 3-RCT. Här är bara en fas 3-studie avslutad (THINK, NCT03081416). KetHead (NCT05306899) pågår fortfarande och saknar resultat. Nivån blir därför **L2** enligt reglerna, även om enskilda källor anger L1.

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på allmän farmakologi är ketamin en NMDA-receptorantagonist. Resonemanget nedan bygger alltså på allmän kunskap, inte på data i underlaget.

Glutamatsignalering och central sensitisering anses bidra till smärta vid migrän, klusterhuvudvärk och kronisk huvudvärk. Blockad av NMDA-receptorer kan dämpa kortikal spridande depression (en våg av nervcellsaktivitet som ligger bakom migränaura) och smärtöverföring i trigeminovaskulära banor. Ketamins effekter på nedåtgående smärthämning och på stämningsläge kan dessutom vara till nytta vid kronisk huvudvärk med samtidig depression.

Den höga modellpoängen stämmer med denna mekanism. Evidensen är dock blandad: den omfattar akut migrän på akutmottagning, kronisk migrän, spänningshuvudvärk och klusterhuvudvärk. Dos, administrationssätt (intravenöst, intranasalt, oralt) och jämförelsebehandling varierar mycket mellan studierna.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Fas 3 | Avslutad | 80 | THINK-studien: intranasalt ketamin i låg dos jämfört med standardbehandling vid primär huvudvärk på akutmottagning (randomiserad, enkelblind, placebokontrollerad). Resultat bör granskas per huvudvärkstyp och jämförelsepreparat. |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Fas 3 | Rekryterar | 56 | KetHead: multicenter-RCT med högdos intravenöst ketamin (1 mg/kg/h i sex timmar) mot placebo vid kronisk daglig huvudvärk. Inga resultat ännu. |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Fas 4 | Avslutad | 54 | Check-studien: lågdos ketamin jämfört med proklorperazin (Compazine) mot huvudvärk på akutmottagning, dubbelblind och randomiserad. |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Fas 4 | Avslutad | 93 | Engångsinfusion av ketamin i kombination med magnesiumsulfat vid refraktär kronisk klusterhuvudvärk. Kombinationen gör det svårt att särskilja ketamins egen effekt. |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | Ej angiven | Avslutad | 34 | Randomiserad, placebokontrollerad studie av ketamin i låg dos mot akut migränliknande huvudvärk på akutmottagning. Litet underlag. |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Fas 4 | Okänd | 60 | Ketamin i låg dos jämfört med ketorolak vid spänningshuvudvärk. Okänd status, så resultatens tillförlitlighet är osäker. |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Fas 1/2 | Avslutad | 23 | Pilotstudie av ketamin som nässpray vid kronisk klusterhuvudvärk. Visar genomförbarhet och en tidig signal, men är liten. |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Fas 4 | Avslutad | 5 | Oralt ketamin + aspirin jämfört med rimegepant (Nurtec) vid akut huvudvärk. Alltför få deltagare för att bedöma effekt. |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | Ej angiven | Avslutad | 300 | PACE-studien: observationsstudie av topikala NSAID mot smärta. Sambandet med ketamin och huvudvärk är oklart. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Systematisk översikt | Journal of Dental Anesthesia and Pain Medicine | Utvärderar ketamin vid migrän och andra primära huvudvärkssjukdomar mot placebo och aktiva jämförelsepreparat (midazolam, metoklopramid/difenhydramin, proklorperazin/difenhydramin). |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Systematisk översikt och metaanalys | Journal of Neurology | Förebyggande behandling vid refraktär kronisk klusterhuvudvärk, ett svårbehandlat tillstånd där många terapier prövats. |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospektiv kohortstudie | Frontiers in Neurology | Bedömer effekt, effektduration och säkerhet för infusioner av lidokain och ketamin vid huvudvärk hos inneliggande patienter. Tidigare stöd har bestått av små fallserier. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Riktlinje | Headache | Uppdaterad riktlinje från American Headache Society om parenteral akutbehandling av migrän på akutmottagning. |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Översikt | Drugs | Läkemedelsbehandling av klusterhuvudvärk, både vid akuta attacker och som förebyggande behandling. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Översikt | Expert Review of Neurotherapeutics | Nämner ketamin som möjligt tilläggs- eller monoterapialternativ vid trigeminusneuralgi. |
| [39037675](https://pubmed.ncbi.nlm.nih.gov/39037675/) | 2024 | Översikt | CNS Drugs | Beskriver det växande intresset för psykoaktiva substanser som huvudvärksläkemedel. Formella studier har först nyligen börjat. |
| [32189074](https://pubmed.ncbi.nlm.nih.gov/32189074/) | 2020 | Översikt | Current Neurology and Neuroscience Reports | Behandlingsalternativ vid huvudvärk hos vuxna på akutmottagning och slutenvård. |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Översikt | Current Neurology and Neuroscience Reports | Akutbehandling av huvudvärk hos barn och ungdomar på akutmottagning och slutenvård. |
| [37806714](https://pubmed.ncbi.nlm.nih.gov/37806714/) | 2023 | Översikt | Progress in Brain Research | Samband mellan migrän och behandlingsresistent depression, två tillstånd som ofta förekommer samtidigt. |

Flera av de översikter som listas ovan berör ketamin bara i förbigående. De stöder därför riktningen mer indirekt än de kontrollerade studierna.

---

## Marknadsinformation Sverige

Alla fyra godkännanden är indragna, och inget giltigt godkännande finns för närvarande.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 51974 | Ketamin Abcur (Abcur AB) | Injektionsvätska, lösning | Ej angiven |
| 51973 | Ketamin Abcur (Abcur AB) | Injektionsvätska, lösning | Ej angiven |
| 8710 | Ketalar (Pfizer AB) | Injektionsvätska, lösning | Ej angiven |
| 8711 | Ketalar (Pfizer AB) | Injektionsvätska, lösning | Ej angiven |

---

## Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer ingick inte i de sammanställda data. Säkerhetsgranskningen kan därför inte slutföras innan den har hämtats från Läkemedelsverket.

**Möjliga kontraindikationer enligt kunskapsgrafen** (härledda från samband mellan läkemedel och sjukdom i en kunskapsgraf, inte från produkttext):
- Hjärt- och kärlsjukdomar: högt blodtryck, stroke och andra cerebrovaskulära sjukdomar, hjärninfarkt, hjärtinfarkt, kranskärlssjukdom, myokardischemi
- Förhöjt tryck: intrakraniell hypertension (förhöjt tryck i skallen), pseudotumor cerebri, okulär hypertension (förhöjt ögontryck)
- Skiftande medvetandetillstånd och beroende: delirium, missbruk och beroende
- Övrigt: andningssvikt, tyreotoxikos, hypertyreos, Graves sjukdom, hemoglobinopati

**Läkemedelsinteraktioner:** 111 interaktioner har identifierats. De viktigaste av måttlig svårighetsgrad är:
- Opioider och närliggande: morfin (även liposomalt), opium, difenoxylat
- Cannabinoider: dronabinol, nabilon
- Stimulerande eller blodtryckshöjande: sibutramin, fentermin, efedrin, fenfluramin, isometepten, adrenalin (topikalt)
- Magtarmmedel: metoklopramid

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Modellpoängen är mycket hög och det finns flera randomiserade studier, men bara en fas 3-studie är avslutad (THINK) och resultaten är blandade mellan huvudvärkstyper, doser och administrationssätt.
- Säkerhetsunderlaget är ofullständigt (ingen produktresumé) och inga giltiga svenska godkännanden finns. Kunskapsgrafen anger dessutom flera möjliga kardiovaskulära och intrakraniella kontraindikationer.

**För att gå vidare krävs:**
- Resultat från THINK-studien och från KetHead (förväntas slutföras 2027), analyserade per huvudvärkstyp.
- Hämta och granska produktresumé med varningar och kontraindikationer, särskilt för patienter med hjärt-kärlsjukdom, förhöjt tryck och beroendehistorik.
- Komplettera data om verkningsmekanism (saknas i underlaget) och om vilket administrationssätt som är lämpligast för huvudvärk.
- Klargöra regulatorisk väg i Sverige, eftersom alla nuvarande godkännanden är indragna.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

