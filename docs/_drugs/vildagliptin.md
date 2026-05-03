---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

Jag använder `txgnn-pipeline`-skillet för att förstå rapportens sammanhang, och genererar nu rapporten baserat på Evidence Pack. Eftersom `predicted_indications[0]` (classic stiff person syndrome) är L5/Hold utan stödjande evidens, och `predicted_indications[9]` (typ 1-diabetes mellitus) är L2 med 50 kliniska prövningar och 20 publikationer samt rekommendationen "Proceed with Guardrails", väljer jag att fokusera rapporten på den kliniskt meningsfulla toppkandidaten med faktisk evidens — typ 1-diabetes mellitus.

---

# Vildagliptin: Från typ 2-diabetes till typ 1-diabetes mellitus

---

## Sammanfattning

Vildagliptin är en potent och selektiv DPP-4-hämmare (dipeptidylpeptidas-4) som globalt används för behandling av typ 2-diabetes mellitus, men som för närvarande inte är godkänd i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **typ 1-diabetes mellitus**, med **50 kliniska prövningar** och **20 publikationer** som för närvarande stöder denna riktning. Den biologiska kopplingen understöds av vildagliptins dokumenterade effekter på glukagonreglering, β-cellsskydd och – unikt – bevarat hypoglykemimotregleringssvar, vilket är en kritisk säkerhetsfördel vid T1DM.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Typ 2-diabetes mellitus (globalt godkänd, ej registrerad i Sverige) |
| Förutsagd ny indikation | Typ 1-diabetes mellitus |
| TxGNN-förutsägelsepoäng | 99,37% |
| Evidensnivå | L2 – 1 avslutad Fas 2 RCT direkt för T1DM + multipla Fas 3-studier med insulinbehandlade patienter |
| Marknadsstatus i Sverige | Inte godkänd |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Detaljerade verkningsmekanismdata från DrugBank är för tillfället inte tillgängliga i detta underlag. Baserat på den samlade litteraturen i Evidence Pack är vildagliptin en potent och selektiv DPP-4-hämmare som verkar genom att blockera nedbrytningen av inkretinhormoner — framför allt GLP-1 (glukagonliknande peptid 1) och GIP (glukosbeorende insulinotropisk polypeptid). Läkemedlets effekt vid typ 2-diabetes är väl bevisad, och dess mekanism är biologiskt tillämpbar på typ 1-diabetes av flera skäl.

Det mest kliniskt relevanta särdragen vid T1DM är att vildagliptin minskar postprandialt glukagon på ett glukoskänsligt sätt — utan att hämma den livsviktiga glukagonmotregleringen vid hypoglykemi. Detta har direkt demonstrerats hos T1DM-patienter (PMID 22855332) och är mekanistiskt distinkt från DPP-4-hämning vid T2DM. Insulin-behandlade T1DM-patienter är särskilt utsatta för hypoglykemi, varför ett läkemedel som bevarar motreglationssvaret utgör en klinisk fördel framför många andra blodsockersänkande tilläggsbehandlingar.

GLP-1-vägens β-cellsprotektiva effekter — antiapoptos, β-cellsneogenesis och immunmodulering via GLP-1R→cAMP→PDX-1-signalering — ger ytterligare biologisk plausibilitet: DPP-4-hämning kan bromsa den residuala autoimmuna β-cellsdestruktionen och bevara endogen insulinsekretion. Djurstudier (PMID 23523961, PMID 25395211) och en klinisk dubbelblind RCT (PMID 33124663) bekräftar att vildagliptin kan inducera β-cellsnybildning och minska oxidativ β-cellsskada i T1DM-modeller.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) | Fas 2 | Avslutad | 55 | Dubbelblind, placebo-kontrollerad 3-arms RCT: rapamycin ± vildagliptin vid långvarig T1DM (2016–2019). Primärt syfte: återställa endogen insulinproduktion och korrigera glykemisk labilitet. Mest direkt T1DM-evidens för vildagliptin. |
| [NCT00138606](https://clinicaltrials.gov/study/NCT00138606) | Fas 3 | Avslutad | 179 | 28-veckors förlängningsstudie av vildagliptin + insulin vid T2DM. Insulinberoende population överlappar kliniskt med T1DM — ger direkt säkerhets- och effektdata för insulin/vildagliptin-kombination. |
| [NCT05102149](https://clinicaltrials.gov/study/NCT05102149) | Fas 3 | Okänd | 672 | Multicenter, randomiserad, dubbelblind Fas 3-studie av PB-201 med vildagliptin och placebo som kontrollarm (n=672). Stort urval och robust design; status behöver bekräftas. |
| [NCT00821977](https://clinicaltrials.gov/study/NCT00821977) | Fas 2/3 | Avslutad | 338 | Adaptiv parallelgruppsstudie av vildagliptin som monoterapi vid T2DM (2008–2010). Ger långtidssäkerhetsdata tillämpbar på tvärsindikationsriskbedömning. |
| [NCT04916093](https://clinicaltrials.gov/study/NCT04916093) | Fas 4 | Avslutad | 60 | Fas 4 huvud-mot-huvud-jämförelse sitagliptin vs vildagliptin vs metformin som förstahandsval vid T2DM. Ger DPP-4-klassjämförelsedata. |
| [NCT01219400](https://clinicaltrials.gov/study/NCT01219400) | Fas 4 | Avslutad | 28 | Vildagliptins effekt på glukagonmotreglering vid hypoglykemi hos insulinbehandlade T2DM-patienter. Direkt relevant säkerhetsdata för T1DM-kontext: visar bevarat motregleringssvar. |
| [NCT01963130](https://clinicaltrials.gov/study/NCT01963130) | N/A | Avslutad | 97 | Vildagliptin och portavenstryck samt hepatostetaos vid T2DM (n=97). Ger vaskulär och hepatisk säkerhetsinformation. |
| [NCT02145611](https://clinicaltrials.gov/study/NCT02145611) | Fas 4 | Avslutad | 50 | Vildagliptin vs glibenklamid + metformin vid T2DM med hypertoni under 12 veckor. Endotelfunktionstdata med GLP-1-vaskulär mekanismrelevans. |
| [NCT04237493](https://clinicaltrials.gov/study/NCT04237493) | Fas 4 | Avslutad | 687 | Dosreduktion av blodsockersänkande multidrogregimer vid Ramadan-fasta (n=687, 2017). Vildagliptin ingår; ger data om glykemisk hantering vid oregelbunden måltidsrytm — relevant för T1DM-patienter med variabelt ätmönster. |
| [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) *(se ovan)* | Fas 2 | Avslutad | 55 | Se rad 1 — primärstudie för T1DM-indikationen. Resultat publicerade som PMID 33124663. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|--------------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT (dubbelblind) | J Clin Endocrinol Metab | Fas 2 RCT: Rapamycin + vildagliptin vs placebo vid långvarig T1DM. Undersöker om kombinationsbehandlingen återställer β-cellsfunktion. Direkt, prospektiv T1DM-evidens för vildagliptin. |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | Klinisk studie (RCT) | Diabetology Metab Syndr | Adjungerad oral vildagliptin vid T1DM-ungdomar (MiniMed 780G) under Ramadan-fasta. DPP-4-hämning minskade iftar-relaterade glukosexkursioner med låg hypoglykemirisk — direkt T1DM-evidens. |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | Klinisk studie (prospektiv) | Diabetes Obes Metab | Vildagliptin som tillägg vid T1DM-ungdomar med NASH. Förbättrade MMP-14-nivåer, leverstyvhet och subklinisk ateroskleros. Belyser extraglykemiska fördelar vid T1DM. |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | Klinisk farmakologistudie | J Clin Endocrinol Metab | Nyckeldata: vildagliptin minskar glukagon vid hyperglykemi men bevarar motreglation vid hypoglykemi vid T1DM. Kritisk säkerhetsdemonstation för T1DM-indikationen. |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Systematisk översikt | Expert Opin Investig Drugs | DPP-4-hämmare uppvisar immunskyddande effekter på β-celler och renalprotektiva effekter vid T1DM; sammanfattar pleiotropa mekanismer bortom antihyperglykemisk effekt. |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Mekanistisk humanstudie | Front Endocrinol | Insikter i GLP-1- och GIP-mekanismer via vildagliptin: förhöjda inkretinnivåer bibehålls i 24 timmar, med β-cellskänslighetsförbättring. Belyser mekanistisk grund för T1DM-tillämpning. |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Translationell studie | Curr Pharm Biotechnol | Vildagliptin inducerar β-cellsneogenesis och förbättrar lipidprofil i sen fas av T1DM (Fischer-råttor + kliniska observationer). |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Klinisk studie | Horm Metab Res | Tidig klinisk evidens: vildagliptins effekt på glukagonkoncentration vid måltider hos T1DM-patienter. Bevisade glukagonhämmande effekt i T1DM-population. |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Djurstudie | Arch Med Res | Vildagliptin minskar oxidativ stress och β-cellsdestruktion i T1DM-råttmodell. Ger preklinisk mekanistisk grund. |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Djurstudie | Can J Physiol Pharmacol | Vildagliptin/pioglitazon förbättrade overall glykemisk kontroll vid T1DM-råttor. Preklinisk kombinationsdata. |

---

## Marknadsinformation Sverige

Vildagliptin är **inte godkänt av Läkemedelsverket (MPA) i Sverige**. Inga registrerade licenser finns. Läkemedlet marknadsförs under varumärket **Galvus®** och **Eucreas®** (kombination med metformin) i andra EU-länder via EMA-godkännande, men saknar godkännande på den svenska marknaden.

> För fullständig säkerhetsinformation hänvisas till EMA-godkänd produktresumé (SmPC) för Galvus® tillgänglig via [EMA:s läkemedelsdatabas](https://www.ema.europa.eu/).

---

## Säkerhetsaspekter

Inga säkerhetsdata från Läkemedelsverket eller den svenska produktresumén är tillgängliga, då vildagliptin saknar godkännande i Sverige. Inga läkemedelsinteraktionsdata återfanns i Evidence Pack.

> Se EMA-godkänd produktresumé (SmPC) för Galvus® för fullständig information om varningar, kontraindikationer och läkemedelsinteraktioner.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Vildagliptin uppvisar välgrundad biologisk plausibilitet för typ 1-diabetes mellitus, underbyggd av en genomförd dubbelblind Fas 2 RCT (NCT02803892 / PMID 33124663), direkta kliniska humanstudier vid T1DM och ett unikt säkerhetssärdrag — bevarat hypoglykemimotregleringssvar — som är kliniskt avgörande för insulinbehandlade patienter. Evidensläget motiverar L2-klassificering och vidare utredning, men saknar ännu en avslutad Fas 3 RCT med T1DM som primär indikation.

**För att gå vidare krävs:**

- Hämta och granska EMA:s produktresumé (SmPC) för Galvus® för fullständig säkerhetsprofil, kontraindikationer och interaktionsdata
- Bekräfta och fullständigt extrahera resultat från NCT02803892 (PMID 33124663) avseende primära och sekundära effektmått
- Söka och värdera eventuella ytterligare registrerade Fas 2–3 studier med T1DM som primär indikation (utöver de 50 identifierade i Evidence Pack)
- Planera eller identifiera Fas 3 RCT specifikt riktad mot T1DM som primär indikation och inkludering av relevanta endpunkter (HbA1c-sänkning, insulindosreduktion, hypoglykemifrekvens, β-cellsfunktionsmarkörer)
- Genomföra regulatorisk förhandsdialog med EMA/Läkemedelsverket om förutsättningarna för en T1DM-indikationsutvidgning för ett redan EMA-godkänt läkemedel
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

