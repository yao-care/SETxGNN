---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Nu genererar jag rapporten baserat på Evidence Pack-data. Modafinil är ett vakenhetsfrämjande läkemedel (inte antineoplastiskt), varför cytotoxicitetssektionen utelämnas. Marknadsinformation utelämnas eftersom det inte finns några svenska registreringar att tabellisera.

---

# Modafinil: Från excessiv dagtidsömnighet till insomni

## Sammanfattning

Modafinil är ett vakenhetsfrämjande läkemedel, FDA-godkänt för behandling av excessiv dagtidsömnighet vid narkolepsi, obstruktiv sömnapné och skiftarbetsstörning, men inte registrerat i Sverige. TxGNN-modellen förutsäger med en poäng på **99,85%** att läkemedlet kan vara effektivt mot **insomni** — en paradoxal prediktion, eftersom modafinils verkningsmekanism primärt motverkar sömn snarare än underlättar den. Förutsägelsen stöds av **1 direkt klinisk prövning** med modafinil mot primär insomni och **19 publikationer**, men den sammantagna evidensbasen bedöms som **L4** med rekommendationen att avvakta.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Excessiv dagtidsömnighet vid narkolepsi, obstruktiv sömnapné och skiftarbetsstörning (FDA-godkänt; ej registrerat i Sverige) |
| Förutsagd ny indikation | Insomni |
| TxGNN-förutsägelsepoäng | 99,85% |
| Evidensnivå | L4 – Prekliniska studier / mekanismstudier |
| Marknadsstatus i Sverige | Inte på marknaden |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande saknas detaljerad verkningsmekanismdata i den strukturerade datakällan. Baserat på tillgänglig information är modafinil ett vakenhetsstimulerande läkemedel som hämmar dopaminåterupptag och aktiverar orexin/hypokretin-signalvägar. Dessa mekanismer ökar vakenhet och minskar excessiv sömnighet — vilket är läkemedlets etablerade terapeutiska profil vid narkolepsi och liknande tillstånd.

Sambandet mellan den ursprungliga indikationen och insomni är i grunden paradoxalt: modafinils primära verkan motverkar insomni-behandlingens mål att underlätta insomning och bibehålla sömn. TxGNN-modellens extremt höga poäng (99,85%) bedöms med stor sannolikhet spegla en falsk positiv signal. Modafinil är tätt kopplat till sömnsjukdoms-noder i kunskapsgrafen (narkolepsi, OSA, skiftarbetsstörning), och insomni delar samma nod-kluster — vilket leder till att modellen felaktigt identifierar en koppling.

Det enda mekanistiskt rimliga scenariot är att modafinil, genom att förstärka vakenhet under dagen, indirekt kan återupprätta en normal dygnsrytm och därigenom förbättra nattlig sömnkvalitet i utvalda patientgrupper — exempelvis vid skiftarbetsrelaterad insomni eller cancerrelaterade sömnrubbningar. Denna indirekta effekt är dock högt kontextberoende och kan inte generaliseras till primär insomni.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fas 4 | Avslutad | 40 | Undersöker om modafinil, ensamt eller i kombination med KBT-I, förbättrar dagtidsfunktion och minskar svårighetsgraden av primär insomni — den enda direkt relevanta prövningen med modafinil |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Fas 2 | Avslutad | 138 | Fyraarmad RCT av KBT-I och armodafinil för insomni och trötthet hos bröstcancerpatienter efter kemoterapi; armodafinil är R-enantiomeren av modafinil |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Fas 2 | Avslutad | 226 | Randomiserad prövning av KBT med eller utan armodafinil för insomni och trötthet hos cancerövervivare; primärt utfallsmått är sömnstörning |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Fas 2 | Avslutad | 70 | Pilotprövning av beteendeterapi (BBT-I/KBT-I) med eller utan armodafinil 150 mg/dag för insomni hos bröstcancerpatienter inför cancerbehandling |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Avslutad | 39 | Utvärderar armodafinil, KBT-I eller kombinationen för sömnkontinuitet hos patienter med sömnrelaterad andningsstörning och komorbid insomni |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Fas 2 | Avslutad | 830 | RECOVER-SLEEP: Plattformsprotokoll för utvärdering av interventioner vid sömnrubbningar efter SARS-CoV-2-infektion (Long COVID); interventionsspecifika detaljer i separata bilagor |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Fas 2 | Aktiv, ej rekryterande | 361 | RECOVER-SLEEP: Pågående parallell plattformsstudie för sömnrubbningar vid Long COVID |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Fas 4 | Avslutad | 18 | Randomiserad placebokontrollerad 8-veckorsprövning av modafinil för dygnsrytmstörning och kognitiv dysfunktion vid stabil bipolär sjukdom; resultat ej direkt överförbara till primär insomni |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fas 4 | Avslutad (terminerad) | 2 | Utforskar om dagtidsbehandling med modafinil kan förstärka sömntryck och förbättra nattlig sömn hos äldre vuxna med sömnstörningar; terminerades tidigt pga. rekryteringssvårigheter |
| [NCT00582491](https://clinicaltrials.gov/study/NCT00582491) | N/A | Avslutad | 44 | Inpatient-studie av modafinils effekter på sömn, sömnighet, uppmärksamhet och inlärning hos individer med kokainnberoende; sömnmätning är sekundärt utfallsmått |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidensbaserad översikt | Drugs | Genomgång av modafinils godkända och experimentella indikationer baserat på RCT; primärt dokumenterat vid EDS och trötthet, inte primär insomni |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematisk översikt + metaanalys | PLoS One | Metaanalys av modafinil för trötthet och EDS vid neurologiska sjukdomar; påvisar effekt vid EDS men inkonsistenta resultat — sömnstörning ej primärt utfallsmått |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematisk översikt | Parkinsonism & Related Disorders | Systematisk översikt av farmakologiska interventioner för dagtidsömnighet och sömnstörningar vid Parkinsons sjukdom; modafinil ingår som behandlingsalternativ |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | EBM-granskning | Movement Disorders | MDS Task Force EBM-uppdatering om behandling av icke-motoriska symtom vid Parkinsons, inklusive sömnstörningar och dagtidsömnighet |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Översiktsartikel | Expert Opinion on Pharmacotherapy | Aktuell genomgång av farmakologiska och icke-farmakologiska behandlingsstrategier för sömnrubbningar vid Parkinsons sjukdom |
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | RCT | Neurology | Randomiserad placebokontrollerad dubbelblindprövning av modafinil för trötthet vid multipel skleros; utfall fokuserat på trötthet, inte sömnproblem |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | J Head Trauma Rehabilitation | Randomiserad prövning av modafinil för trötthet och EDS vid kronisk traumatisk hjärnskada; sömnstörning utvärderades som sekundärt utfall |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Översiktsartikel | Drugs | Översikt av skiftarbetsstörning (SWSD): sjukdomsbörda, komorbiditeter och behandlingsstrategier inklusive modafinil — relevant kontextinformation |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Läkemedelsprofil | Drug Design, Development and Therapy | Profil av pitolisant vid narkolepsi med jämförelse mot modafinil; ger kontextuell förståelse av modafinils roll i sömnsjukdomsbehandling |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Fallserie | Am J Hospice & Palliative Care | Modafinil minskar trötthet vid Charcot-Marie-Tooth typ 1A; fallserie, lägsta evidensnivå — illustrerar off-label bredd men ej direkt relevant för insomni |

---

## Säkerhetsaspekter

> Se produktresumén för säkerhetsinformation. Modafinil är inte registrerat i Sverige och inga svenska godkännandehandlingar finns tillgängliga. Säkerhetsdata från läkemedelsmyndighetens ursprungliga godkännandehandlingar bör inhämtas direkt.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
TxGNN-modellens förutsägelsepoäng på 99,85% bedöms med stor sannolikhet vara en falsk positiv signal orsakad av modafinils täta koppling till sömnsjukdoms-noder i kunskapsgrafen — insomni delar samma nod-kluster som narkolepsi och OSA utan att det föreligger ett genuint terapeutiskt samband. Modafinils vakenhetsstimulerande verkningsmekanism är i grunden motsatt behandlingsmålet vid primär insomni, och befintliga kliniska data är otillräckliga och huvudsakligen indirekta (armodafinil, cancerpopulationer, EDS-fokus).

**För att gå vidare krävs:**
- Inhämtning av fullständig säkerhetsinformation (varningar, kontraindikationer) från originalproduktresumén för att möjliggöra S1-säkerhetsbedömning
- Detaljerad MOA-data från DrugBank API för att kvantifiera den mekanistiska konflikten formellt
- Fulltextgranskning av NCT00124384 (modafinil vid primär insomni, n=40) för att bedöma faktiska kliniska utfall
- Avgränsning av om en specifik delpopulation — exempelvis insomni sekundär till dygnsrytmstörning vid skiftarbete — kan motivera fortsatt utvärdering
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

