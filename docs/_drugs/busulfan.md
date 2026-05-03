---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Busulfan
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

Jag använder `txgnn-pipeline`-skillet för att säkerställa korrekt rapportformat, och skriver nu rapporten baserat på Evidence Pack-data.

---

# Busulfan: Från kronisk myeloisk leukemi till myelodysplastiskt syndrom

## Sammanfattning

Busulfan är ett bifunktionellt alkyleringsmedel som historiskt använts för behandling av kronisk myeloisk leukemi (KML) och som idag är välestablerat som konditioneringsmedel inför allogen hematopoetisk stamcellstransplantation (allo-HSCT) vid hematologiska sjukdomar. TxGNN-modellen förutsäger att busulfan kan vara effektivt vid **myelodysplastiskt syndrom (MDS)**, med **10 kliniska prövningar** och **20 publikationer** som stöder denna riktning. Evidensnivån bedöms som **L1**, vilket är den starkaste kategorin, med stöd från multipla randomiserade fas 3-prövningar.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej registrerat i Sverige; känd klinisk användning som konditioneringsmedel inför allo-HSCT vid leukemi |
| Förutsagd ny indikation | Myelodysplastiskt syndrom (myelodysplastic syndrome) |
| TxGNN-förutsägelsepoäng | 99,62% |
| Evidensnivå | L1 – Stöds av multipla fas 3-RCT |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Gå vidare med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Busulfan är ett bifunktionellt alkyleringsmedel som utövar sin verkan genom att bilda korsbindningar mellan DNA-strängar i hematopoetiska progenitorceller, vilket leder till hämning av DNA-replikation och apoptos. Läkemedlet har en utpräglad selektivitet för benmärgsceller och har till följd av detta använts i decennier som konditioneringsmedel inför allogen stamcellstransplantation. Även om en detaljerad verkningsmekanism inte är dokumenterad i det aktuella datapaketet, är busulfans myeloablativa effektprofil välkänd i klinisk och vetenskaplig litteratur.

Myelodysplastiskt syndrom (MDS) är en grupp klonala sjukdomar i de hematopoetiska stamcellerna, karakteriserade av dysplastisk benmärgsmorfologi, progressiva cytopenier och en signifikant risk för transformation till akut myeloisk leukemi (AML). Allogen HSCT är den enda potentiellt kurativa behandlingen för patienter med intermediär- och högrisk-MDS. Det finns ett direkt mekanistiskt samband: busulfans benmärgsablativa effekt eliminerar det MDS-sjuka klonala hematopoetiska systemet och skapar utrymme för donatorns friska stamceller att ta fäste och återupprätta normal blodbildning.

Kombinationsregimen busulfan + fludarabin (Bu/Flu) har bekräftats som en etablerad standardregim inför allo-HSCT vid MDS i randomiserade fas 3-prövningar, däribland MC-FludT.14/L-studien publicerad i *The Lancet Haematology* (2020). Det breda kliniska evidensunderlaget — med publikationer i ledande hematologitidskrifter, pågående randomiserade fas 2-studier med upp till 220 deltagare, och ett internationellt konsensusstöd — gör denna förutsägelse till en av de mest välgrundade i hela TxGNN-analysen.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Fas 2 | Rekryterar | 220 | Randomiserad jämförelse av benadamustine vs ruxolitinib kombinerat med fludarabin+busulfan som konditionering vid haploidentisk SCT för R/R MDS; direkt och aktuell evidens för busulfan vid MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fas 2 | Aktiv, ej rekryterande | 116 | Venetoclax + tidssekventiellt busulfan + cladribin + fludarabin inför allo-SCT vid AML och MDS; busulfan är kärnkomponent i regimen |
| [NCT05027945](https://clinicaltrials.gov/study/NCT05027945) | Fas 2 | Rekryterar | 54 | Allogen HSCT för VEXAS-syndrom (inkluderar MDS-komponent); busulfan som potentiellt konditioneringsalternativ i pågående studie |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | N/A | Avslutad | 30 | Haploidentisk allogen HSCT med reducerad intensitetskonditionering; busulfan i konditioneringsregimen vid MDS och relaterade blodsjukdomar |
| [NCT01252784](https://clinicaltrials.gov/study/NCT01252784) | N/A | Okänd | 20 | RIC allo-HCT följt av profylaktisk doneskalerande donorlymfocytinfusion vid högrisk MDS; busulfan som konditioneringskomponent |
| [NCT00916045](https://clinicaltrials.gov/study/NCT00916045) | Fas 2 | Avbruten (rekryteringssvårigheter) | 40 | Navelsträngsblodstransplantation vid högrisk hematologiska maligniteter inkl. MDS, med myeloablativ eller RIC-konditionering |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Fas 2 | Aktiv, ej rekryterande | 204 | Tidssekventiellt busulfan + post-transplant cyklofosfamid vid allo-SCT för blodcancer; busulfan som kärnläkemedel i stor pågående studie |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Fas 2 | Avslutad | 35 | Fludarabin + busulfan + alemtuzumab som reducerad toxicitetsregim inför allogen HSCT vid stamcellsdefekter, benmärgssvikt och MDS/leukemi hos barn |
| [NCT02221310](https://clinicaltrials.gov/study/NCT02221310) | Fas 2 | Avslutad | 25 | Gemtuzumab ozogamicin + busulfan + cyklofosfamid + allo-SCT vid högrisk AML och MDS; busulfan integrerad i konditioneringsregimen |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Fas 2 | Avslutad | 13 | Högdos busulfan + cyklofosfamid + allogen BMT vid leukemi, MDS, multipelt myelom och lymfom; inkluderar patienter som inte tolererar helkroppsbestrålning |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Jämförande RCT-uppföljning | American Journal of Hematology | Slutanalys fas 3-studie (n=476): treosulfan icke-inferior jämfört med reducerat intensitetsbusulfan (Bu-RIC) som referensstandard vid äldre AML/MDS inför allo-HCT |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Fas 3 RCT | The Lancet Haematology | MC-FludT.14/L: treosulfan+fludarabin jämfört med busulfan+fludarabin (etablerad jämförelseregim) vid äldre och komorbida AML/MDS-patienter inför allo-HSCT |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Fas 3 RCT | The Lancet Haematology | G-CSF+decitabin+busulfan-cyklofosfamid minskar recidivfrekvensen signifikant jämfört med busulfan-cyklofosfamid enbart vid MDS-RAEB och sekundär AML inför allo-HSCT |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Samtida översikt | American Journal of Hematology | Aktuell genomgång av allo-HCT vid MDS och myelofibros; busulfan-baserade regimer bekräftas som klinisk standard, med betoning på genomikprofilering och individualisering |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematisk översikt och meta-analys | Frontiers in Oncology | Långtidsutfall treosulfan vs busulfan-baserade konditioneringsregimer vid MDS/AML inför allo-HCT; busulfan fungerar som referensstandard i meta-analysen |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Fas 3 RCT | Journal of Clinical Oncology | BMT CTN 0901: myeloablativ konditionering (inkl. busulfan-regimer) vs reducerad intensitetskonditionering vid AML/MDS i randomiserad fas 3-design |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Retrospektiv kohortstudie | Transplantation and Cellular Therapy | Propensity score-matchad analys treosulfan vs busulfan-konditionering vid allo-HCT för MDS (n=138); busulfan som aktiv jämförelsearm |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospektiv kohort | Transplantation and Cellular Therapy | Myeloablativ busulfan+fludarabin kombinerat med in vivo T-cellsdeletion är säker och effektiv konditionering vid AML och MDS; stöder utvidgad åldersindikation |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Propensity score-matchad analys | Bone Marrow Transplantation | Nationellt japanskt registerdata (2006–2018): Flu/Bu4 vs Bu4/Cy myeloablativ konditionering vid MDS; Flu/Bu4 visade gynnsamt säkerhetsprofil |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Propensity score-matchad analys | Transplantation and Cellular Therapy | MAC Flu/Bu4 vs RIC Flu/Bu2 konditionering vid MDS; dosintensitetens kliniska relevans kvantifieras i nationellt registerdata |

---

## Marknadsinformation Sverige

Busulfan saknar för närvarande godkännanden hos Läkemedelsverket och är inte registrerat på den svenska marknaden. Inga produktresumér, godkännanden eller licensuppgifter finns att hämta från den svenska regulatoriska databasen. Klinisk användning i Sverige kräver licensansökan.

---

## Cytotoxicitet

Busulfan klassificeras som ett antineoplastiskt alkyleringsmedel (ATC-kod: L01AB01) och uppfyller kriterierna för cytotoxicitetsavsnittet.

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Konventionell cytotoxisk – bifunktionellt alkyleringsmedel (DNA-korsbindning) |
| Myelosuppressionsrisk | Hög – busulfan är ett avsiktligt myeloablativt medel; djupgående och varaktig benmärgssuppression är det terapeutiska målet inför HSCT |
| Emetogenicitetsklassificering | Hög – höga doser alkyleringsmedel kräver antiemetisk profylax (5-HT₃-antagonist + dexametason, överväg NK1-antagonist) |
| Övervakningspunkter | Fullständigt blodstatus dagligen under konditioneringsfas; leverfunktion (ASAT, ALAT, bilirubin, ALP) för detektion av venocklusiv leversjukdom (VOD/SOS); njurfunktion (kreatinin, beräknat GFR); busulfanplasmakoncentrationer för AUC-baserad dosindividualisering (TDM); EEG och neurologisk status (kramprisk – profylaktisk antiepileptisk behandling rekommenderas) |
| Hanteringsskydd | Ja – busulfan är klassificerat som farligt läkemedel (NIOSH kategori 1; IARC grupp 1 – bevisat cancerframkallande för människa); hantering kräver certifierat säkerhetsskåp (BSC klass II B), dubbelhandskar, stänkskyddad skyddsrock och slutet läkemedelssystem (CSTD) vid beredning och administrering |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation. Fullständiga varningsuppgifter, kontraindikationer och interaktionsdata är inte tillgängliga i det aktuella datapaketet och måste inhämtas från tillverkarens dokumentation eller EMA/MHRA inför klinisk användning.

---

## Slutsats och nästa steg

**Beslut: Gå vidare med försiktighet**

**Motivering:**
Busulfan uppvisar stark L1-evidens som konditioneringsmedel inför allo-HSCT vid MDS, bekräftat av multipla randomiserade fas 3-studier och ett brett internationellt prövningsprogram. Den mekanistiska länken är tydlig och väldokumenterad. Läkemedlet är dock ej registrerat i Sverige och säkerhetsdokumentationen har identifierade dataluckor som måste åtgärdas.

**För att gå vidare krävs:**
- Inhämtning av fullständig produktresumé och säkerhetsdokumentation (kontraindikationer, boxed warnings) via EMA, MHRA eller originaltillverkare
- Ansökan om licensiering/nationellt tillstånd hos Läkemedelsverket för användning i HSCT-konditioneringsprotokoll
- Fastställande av TDM-protokoll för AUC-baserad busulfandosindividualisering (mål-AUC 900–1350 μmol·min/L beroende på konditioneringsintensitet)
- Multicentrumsamarbete med etablerade HSCT-enheter (Karolinska, Sahlgrenska, Akademiska) med erfarenhet av busulfan-baserade MDS-konditioneringsregimer
- Komplettering av läkemedelsinteraktionsdata (DDI) givet busulfans metabolism via CYP3A4 och GST-enzymer
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

