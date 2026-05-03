---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Filgrastim
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

Använder **txgnn-pipeline** för att förstå projektstrukturen, sedan genererar jag rapporten enligt systemprompten (v5) med korrekt svenska sektionsrubriker och format.

---

# Filgrastim: Från neutropeni till primär trombocytfrisättningsstörning

## Sammanfattning

Filgrastim är en rekombinant granulocytkolonistimulerande faktor (G-CSF) som primärt används för att behandla neutropeni och mobilisera hematopoetiska stamceller inför transplantation. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **primär trombocytfrisättningsstörning** med en förutsägelsepoäng på 99,998 %. Bevisbasen omfattar **14 kliniska prövningar** och **1 publikation**, men samtliga utgör indirekt stöd via HSCT-kontext – ingen prövning har direkt utvärderat Filgrastim som behandling mot denna specifika diagnos.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej tillgänglig (inga svenska godkännanden registrerade) |
| Förutsagd ny indikation | Primär trombocytfrisättningsstörning |
| TxGNN-förutsägelsepoäng | 99,998 % |
| Evidensnivå | L4 – Mekanistiska studier / indirekt klinisk evidens |
| Marknadsstatus i Sverige | Ej på marknaden |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är Filgrastim en rekombinant G-CSF (granulocytkolonistimulerande faktor) som primärt stimulerar produktion och mognad av neutrofila granulocyter via G-CSF-receptorn (CSF3R), och används kliniskt för att mobilisera hematopoetiska stamceller inför transplantation.

Sambandet med primär trombocytfrisättningsstörning är av indirekt karaktär: G-CSF-receptorn uttrycks i låg utsträckning även på megakaryocyter – de celler som ger upphov till trombocyter. Teoretiskt sett kan G-CSF-signalering via JAK-STAT-vägen ha en viss modulerande effekt på megakaryocytdifferentiering. Vidare kan HSCT-protokoll – där Filgrastim används som stamcellsmobiliserande medel – i princip åtgärda den bakomliggande hematopoetiska stamcellsdefekten vid vissa kongenitala former av primär trombocytfrisättningsstörning.

Det är viktigt att betona att Filgrastim i sig inte riktar sig direkt mot trombocyternas frisättningsmekanismer. Effekten är att betrakta som en möjlig indirekt konsekvens av HSCT-mobilisering snarare än en direkt farmakologisk verkan på sjukdomsprocessen. Modellens förutsägelse baseras sannolikt på delade biologiska noder i kunskapsgrafen kopplade till hematopoies och trombocytproduktion.

---

## Kliniska prövningar

> **Notera:** Samtliga prövningar nedan genomfördes i HSCT- eller supportiv-vård-kontext. Ingen prövning har primärt utvärderat Filgrastim som behandling mot primär trombocytfrisättningsstörning.

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fas 2 | Avbruten | 200 | HSCT från icke-besläktad givare vid hematologiska maligniteter; Filgrastim som stamcellsmobiliserare. Avbröts utan att nå primärt endpoint. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fas 2 | Avslutad | 60 | Allogen/syngeneisk PBSC-transplantation vid pediatriska sarkom. Filgrastim användes för mobilisering; ingen effekt på trombocytfrisättning studerades. |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Fas 2 | Avbruten | 16 | Navelsträngsblodstransplantation kombinerat med NK-celler vid myeloisk leukemi; Filgrastim stödde hematopoetisk återhämtning. Avbröts vid lågt deltagarantal. |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fas 2 | Avslutad | 19 | Reducerad-intensitet HSCT vid GATA2-mutationer. Utforskade hematopoetisk rekonstruktion vid högriskblodsjukdom; ej riktad mot trombocytfrisättningsstörning. |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fas 2 | Avslutad | 64 | Randomiserad jämförelse av CD34⁺-selekterad vs. icke-selekterad autolog SCT vid mantelcellslymfom och diffust storcelligt B-cellslymfom. Primärt endpoint: 3-årsöverlevnad. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fas 1/2 | Rekryterar | 260 | Explorerar lägsta effektiva dos av post-transplantationscyklofosfamid för GvHD-profylax kombinerat med sirolimus och MMF. Filgrastim är stödläkemedel, ej primär intervention. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fas 2 | Rekryterar | 358 | Plattformsprotokoll för GvHD-profylax vid missmatchad icke-besläktad givare PBSCT. Jämför läkemedelskombinationer för att förhindra GvHD. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fas 3 | Rekryterar | 156 | Randomiserad kontrollerad studie av AHSCT jämfört med bästa tillgängliga terapi vid behandlingsresistent relapserande multipel skleros. 72 månaders uppföljning planerad. |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fas 2 | Avslutad | 9 | Pilotstudie av intensifierad lymfodepletion följt av autolog HSCT vid svår systemisk lupus erythematosus. Litet urval; Filgrastim för stamcellsmobilisering. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fas 1/2 | Avslutad | 147 | Icke-myeloablativ allogen HSCT med busulfan, fludarabin och helkroppsbestrålning vid hematologiska maligniteter. Utforskade graft-versus-tumor-effekten post-transplantation. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|--------------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Kohort/Översikt | Frontiers in Immunology | G-CSF-mobilisering av perifera blodstamceller hos friska givare orsakar preferentiell mobilisering av lymfocytsubgrupper. Belyser immunologiska aspekter av G-CSF-behandling och deras relevans för post-transplantationskomplikationer, men stöder inte direkt effekt vid trombocytfrisättningsstörning. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Samtliga 14 identifierade prövningar genomfördes i HSCT- eller supportiv-vård-kontext, och Filgrastim utvärderades aldrig som primär intervention mot primär trombocytfrisättningsstörning; den mekanistiska länken via G-CSF-receptorns svaga uttryck på megakaryocyter saknar klinisk bekräftelse, vilket sammantaget ger evidensnivå L4.

**För att gå vidare krävs:**
- Dedikerade mekanistiska studier av G-CSF:s direkta effekt på megakaryocyters frisättningsfunktion (in vitro/in vivo)
- Identifiering av patientunderpopulationer med primär trombocytfrisättningsstörning där HSCT-baserad strategi är kliniskt aktuell
- Komplettering av säkerhetsdata (varningar, kontraindikationer, läkemedelsinteraktioner) via produktresumé och DrugBank API
- Klargörande av Filgrastims faktiska godkännandestatus i Sverige – inga licensuppgifter kunde verifieras i detta evidenspaket
- Riktad litteratursökning om G-CSF och megakaryocytfunktion för att avgöra om befintlig preklinisk evidens motiverar en dedikerad klinisk prövning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

