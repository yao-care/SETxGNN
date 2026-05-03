---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **8** st
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

Nu genererar jag rapporten baserat på Evidence Pack JSON.

---

# Simvastatin: Från primär hyperkolesterolemi till familjär hyperkolesterolemi

## Sammanfattning

Simvastatin är en HMG-CoA-reduktashämmare som kliniskt används för att sänka LDL-kolesterol och behandla primär hyperkolesterolemi och blandad dyslipidemi. TxGNN-modellen förutsäger att det kan vara effektivt mot **familjär hyperkolesterolemi (FH)** – en ärftlig sjukdom orsakad av genetiska defekter i LDL-receptorfunktionen som leder till kraftigt förhöjda LDL-nivåer och tidig kranskärlssjukdom. Förutsägelsen stöds av **19 kliniska prövningar** (varav flertalet fas 3) och **18 publikationer**, inkluderande tre Cochrane-systematiska översikter och ledande kardiologiska riktlinjer från ACC/AHA 2026.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige (inga godkännanden tillgängliga) |
| Förutsagd ny indikation | Familjär hyperkolesterolemi |
| TxGNN-förutsägelsepoäng | 99,63% |
| Evidensnivå | L1 (≥2 avslutade fas 3 RCT med direkt simvastatin-evidens) |
| Marknadsstatus i Sverige | Ej godkänd/registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Simvastatin hämmar HMG-CoA-reduktas, det hastighetsbegränsande enzymet i kolesterolbiosyntesen i levern. När den endogena kolesterolproduktionen minskar kompenserar levercellerna genom att uppregulera LDL-receptoruttrycket på cellytan, vilket ökar clearance av LDL-partiklar från blodbanan och sänker det cirkulerande LDL-kolesterolet med 30–50%.

Familjär hyperkolesterolemi orsakas av autosomal dominant nedärvda mutationer i generna för LDL-receptorn (LDLR), apolipoprotein B (APOB) eller PCSK9, samtliga resulterar i defekt LDL-metabolism och kraftigt förhöjt LDL sedan födseln. Simvastatin motverkar direkt denna patofysiologi: genom att kompensatoriskt öka LDL-receptortätheten kan läkemedlet delvis kringgå den genetiska defekten och öka hepatisk LDL-uptake. Mekanismkopplingen är direkt och tillhör statinernas biologiska kärnmålpunkt.

Denna förutsägelse representerar snarare en formell evidensdokumentation av en välkänd klinisk tillämpning än en spekulativ ompositionering. Statiner – däribland simvastatin – är globalt förstahandsbehandling vid FH och rekommenderas i samtliga ledande riktlinjer (ACC/AHA, AACE/ACE, EAS). TxGNN-modellens höga poäng (99,63%) speglar den starka sjukdoms-läkemedelskopplingen i kunskapsgrafen och bekräftas av ett synnerligen robust kliniskt evidensläge.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fas 3 | Avslutad | 50 | Effekt och säkerhet för ezetimib ko-administrerat med atorvastatin eller **simvastatin** vid homozygoust FH; primärt mål LDL-C-sänkning |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fas 3 | Avslutad | 44 | Långtidssäkerhet (24 månader) för ezetimib tillagt atorvastatin eller **simvastatin** vid homozygoust FH; öppen förlängningsstudie |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fas 3 | Avslutad | 720 | ENHANCE-studien: ezetimib + **hösdos simvastatin** vs **simvastatin ensamt** vid heterozygoust FH; utvärderade karotis-intima media-tjocklek som surrogatmått för aterosklerosprogression |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fas 3 | Avslutad | 248 | Randomiserad dubbelblind studie; ezetimib i kombination med **simvastatin** hos ungdomar (10–17 år) med heterozygoust FH |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Fas 3 | Avslutad | 486 | Alirocumab (PCSK9-hämmare) vid heterozygoust FH med otillräcklig LDL-sänkning trots statin-behandling; bekräftar statin som obligatorisk bakgrundsbehandling |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Fas 3 | Avslutad | 2 341 | Stor långtidsstudie (ODYSSEY LONG TERM); alirocumab vid hög kardiovaskulär risk, statin som standardbehandling i bakgrunden |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Fas 3 | Avslutad | 986 | Öppen förlängningsstudie för alirocumab vid HeFH; långtidssäkerhet och effekt med statin som bakgrundsbehandling |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fas 3 | Avslutad | 249 | Alirocumab vid HeFH; parallellgruppsdesign, statin-bakgrundsbehandling |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Fas 3 | Avslutad | 216 | Multicenter-RCT; alirocumab tillagt stabil daglig statindos vid HeFH eller hög kardiovaskulär risk |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fas 3b | Avslutad | 442 | Öppen randomiserad parallellgruppsstudie; njureffekter av rosuvastatin och **simvastatin** vid Fredrickson typ IIa/IIb dyslipidemi inkl. heterozygoust FH |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Klinisk praxisriktlinje | *Circulation* | 2026 ACC/AHA-riktlinje för dyslipidemivård; ersätter 2018 års riktlinje och bekräftar statiner som hörnsten i FH-behandling |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Klinisk praxisriktlinje | *Journal of the American College of Cardiology* | Parallell publikation av 2026 ACC/AHA dyslipidemiriktlinje |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane systematisk översikt | *The Cochrane Database of Systematic Reviews* | Statiner för barn med familjär hyperkolesterolemi; stöder tidig statinbehandling och visar säker lipidprofil |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Cochrane systematisk översikt | *The Cochrane Database of Systematic Reviews* | Cochrane-uppdatering; statiner inklusive simvastatin vid pediatrisk FH – effekt och säkerhetsprofil bekräftad |
| [25054950](https://pubmed.ncbi.nlm.nih.gov/25054950/) | 2014 | Cochrane systematisk översikt | *The Cochrane Database of Systematic Reviews* | Tidig Cochrane-genomgång av statiner vid barn-FH; underlag för internationella behandlingsrekommendationer |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | *New England Journal of Medicine* | ENHANCE-studien; simvastatin ± ezetimib vid FH – ezetimib sänkte LDL ytterligare men påverkade inte aterosklerosprogression (karotis-IMT) signifikant |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Klinisk praxisriktlinje | *Endocrine Practice* | AACE/ACE-riktlinjer för dyslipidemivård; statiner rekommenderas vid FH och högriskpatienter |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Nytta-riskanalys | *Expert Opinion on Drug Safety* | Nytta-riskbedömning av simvastatin specifikt vid familjär hyperkolesterolemi; stöder långtidsbehandling med god tolerabilitetsprofil |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Klinisk kohort | *Journal of Clinical Medicine* | Cellulär immunitet hos barn med FH under simvastatin-behandling (10 mg, ≥26 veckor); ingen kliniskt relevant immunpåverkan påvisades |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Nytta-riskanalys | *Drug Safety* | Tidigt och inflytelserikt underlag för simvastatin vid FH; sammanfattar kardiovaskulär riskreduktion och säkerhetsprofil vid långtidsanvändning |

---

## Säkerhetsaspekter

Detaljerade svenska säkerhetsdata (varningar, kontraindikationer, läkemedelsinteraktioner) saknas i det inlämnade evidensunderlaget.

> Se produktresumén för säkerhetsinformation.

**Klinisk notering:** Simvastatin är ett känt CYP3A4-substrat. Samtiida administrering med starka CYP3A4-hämmare (t.ex. itrakonazol, ketokonazol, HIV-proteashämmare) kan ge kraftigt ökade plasmanivåer av simvastatin med risk för myopati och rabdomyolys. Dosjustering eller byte till ett statin med lägre interaktionsrisk (t.ex. rosuvastatin, pravastatin) bör övervägas i sådana situationer.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Simvastatin uppnår evidensnivå L1 för familjär hyperkolesterolemi, med ett flertal avslutade fas 3-studier som direkt involverar simvastatin som antingen primär intervention eller obligatorisk bakgrundsbehandling. Mekanismkopplingen är direkt och biologiskt välmotiverad. Begränsningarna utgörs av avsaknad av svenska regulatoriska godkännanden och att fullständiga säkerhetsdata (varningar, kontraindikationer) ännu inte dokumenterats i evidensunderlaget.

**För att gå vidare krävs:**
- Inläsning av produktresumé (SmPC) för simvastatin från Läkemedelsverket eller EMA för att komplettera varningar, kontraindikationer och interaktionsdata
- Verifiering av marknadsstatus i Sverige – simvastatin förekommer i generisk form och ingår i Inegy® (simvastatin/ezetimib); registreringsstatus behöver bekräftas via Läkemedelsverkets produktdatabas
- Bedömning av relevanta dosregimer för FH (heterozygoust vs homozygoust) och populationsspecifika överväganden (pediatrisk användning, graviditet)
- Utvärdering av samspel med moderna FH-behandlingar (PCSK9-hämmare, inclisiran) för att fastställa simvastatin rollenin det aktuella behandlingslandskapet
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

