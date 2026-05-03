---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

Using `txgnn-pipeline` to orient the report context. Now generating the Swedish evaluation report based on the Evidence Pack.

---

# Alprazolam: Från ångestsyndrom till insomnia

## Sammanfattning

Alprazolam är ett bensodiazepinpreparat som internationellt används för behandling av ångestsyndrom och paniksyndrom, men som för närvarande saknar godkänt marknadstillstånd i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **insomnia (sömnlöshet)** med en förutsägelsepoäng på **99,81 %**. Stödet för denna riktning inkluderar **7 kliniska prövningar** och **18 publikationer**, vilket placerar evidensen på nivå **L2**.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige; internationellt: ångestsyndrom och paniksyndrom |
| Förutsagd ny indikation | Insomnia (sömnlöshet) |
| TxGNN-förutsägelsepoäng | 99,81 % |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Ej godkänt |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Detaljerade verkningsmekanismdata från DrugBank saknas för närvarande. Baserat på känd farmakologi är alprazolam en positiv allosterisk modulator av GABA-A-receptorer, vilket förstärker den hämmande neurotransmissionen i centrala nervsystemet. Denna mekanism minskar sömnlatensen och ökar andelen tidig djupsömn (slow-wave sleep) — effekter som är direkt relevanta för behandling av insomnia.

Sambandet mellan alprazolams ursprungliga indikation (ångestsyndrom) och insomnia är väl belagt i klinisk litteratur. Ångest och sömnlöshet samförekommer i hög utsträckning, och sömnstörningar ingår som centrala symtom vid både generaliserat ångestsyndrom och paniksyndrom. Alprazolams sedativa egenskaper har historiskt lett till klinisk användning vid insomnia, framför allt när sömnstörningen samexisterar med ångest.

Det bör dock noteras att alprazolam hämmar REM-sömnen och att toleransutveckling samt rebound-insomnia vid utsättning är välkända kliniska risker. Dessa begränsningar innebär att läkemedlet konkurrerar med — och sannolikt underordnar sig — etablerade sömnmedel som Z-preparat (zolpidem, zopiklon) och kognitiv beteendeterapi för insomnia (KBT-i). Potentialen som förstahandsval vid primär insomnia bedöms som begränsad.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Fas 4 | Avslutad | 418 | Öppen multicenterstudie (8 veckor) som jämförde tillägg av alprazolam (Niravam) till SSRI/SNRI med enbart SSRI/SNRI-behandling vid GAD eller paniksyndrom; primärt utfallsmått var tid till ångestsymtomlindring |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Fas 2 | Avslutad | 220 | Dubbelblind, placebokontrollerad RCT; utvärderade AVP-923 (dextromethorfan/kinidin) mot agitation vid Alzheimers sjukdom; sömnrelaterade sekundära utfall och bensodiazepinreferensarm ingick |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | Observationell | Okänd | 1 400 | Prospektiv kohortstudie i Taiwan; undersökte användningsmönster, risk-nyttaprofil samt kliniska och ekonomiska utfall för hypnotika inklusive bensodiazepiner vid sömnstörningar hos äldre |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | Observationell | Avslutad | 170 | Digital självhjälpsintervention för att underlätta utsättning av bensodiazepiner (inkl. Xanax/alprazolam) hos veteraner med sömnstörningar; fokus på att minska användning snarare än att utvärdera sömneffekt |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Jämförande RCT | Cureus | Direkt jämförelse av alprazolam mot melatonin vid sömnstörningar hos hemodialyspatienter med njursvikt i slutstadiet; utvärderade subjektiv sömnkvalitet, trötthet och dagtidsfunktion |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (sammansatt) | Medicine | Alprazolam i kontrollarmen jämfördes med kombinationsbehandling (moxibustion + öronakupunktur + alprazolam) vid kranskärlssjukdom och insomnia (n=116); experimentgruppen visade förbättrad neurotransmittorprofil |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Djurstudie | Aging | Upprepad alprazolam-administrering orsakade mitokondriell dysfunktion i hippocampus hos möss och försämrad minneskonsolidering — viktig säkerhetssignal för långtidsanvändning vid insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Metaanalys | Acta Pharmaceutica | Systematisk genomgång av lugnande läkemedel (inkl. bensodiazepiner) vid kroniska sjukdomar hos äldre; utvärderade effektstorlek, biverkningsprofil och optimal dos |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Tvärsnittstudie | Medicine | Kartläggning av insomnia bland COVID-19-överlevare (dec 2022–feb 2023); identifierade förekomst och riskfaktorer för ihållande sömnstörningar efter infektion |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiologisk studie | Value in Health Regional Issues | Tioårig prediktion av bensodiazepinbruk (inkl. alprazolam) i Kroatien; visar ökande trend och ekonomisk börda av långtidsbruk kopplat till insomnia och ångest |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Kohortstudie (verkliga världen) | China J Chin Mater Med | Verklighetsstudie av insomniapatienter (n=1 067) vid 20 kinesiska sjukhus; kartlade samsjukligheter och läkemedelsanvändningsmönster inklusive bensodiazepiner |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Kohortstudie | JHEP Reports | Utsättning av hypnotika minskade fall och frakturer hos levercirrospatienter; understryker riskprofilen för bensodiazepiner (inkl. alprazolam) i sköra patientgrupper |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observationsstudie | Sleep Medicine | Analys av receptmönster för sömnmedel i stor managed care-population; noterade ökad användning av bensodiazepiner (inkl. alprazolam) som hypnotikum trots tillgång till dedikerade sömnmedel |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Översiktsartikel | Expert Opin Drug Metab Toxicol | Farmakokinetisk genomgång av anxiolytika inklusive bensodiazepiner; relevant för förståelse av absorptions- och eliminationsprofil vid sömnindikation |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Alprazolams verkningsmekanism via GABA-A-receptorer ger biologisk plausibilitet för sömnindikationen, och befintlig litteratur inkluderar ett direkt jämförande RCT mot melatonin vid insomnia. Evidensnivån är L2, men de tillgängliga prövningarna är heterogena i design och populations­relevans, och de kliniska riskerna med toleransutveckling, beroende och rebound-insomnia är välkända begränsningar.

**För att gå vidare krävs:**
- Inhämtning av fullständig produktresumé (SmPC) och säkerhetsprofil inklusive kontraindikationer och läkemedelsinteraktioner
- Jämförande effekt- och säkerhetsanalys mot godkända sömnmedel (Z-preparat, doxepin, melatonin) för att fastställa alprazolams plats i terapin
- Definition av målpopulation — exempelvis insomnia med komorbid ångest kontra primär insomnia utan ångestkomponent
- Riskstratifiering avseende beroendepotential och berättigande inför eventuellt ansökningsunderlag eller klinisk prövningsdesign
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

