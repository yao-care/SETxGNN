---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **5** st
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

Nu genererar jag rapporten baserat på Evidence Pack. Propofol är ett etablerat anestetikum (ej antineoplastiskt), så cytotoxicitetsavsnittet utelämnas. Säkerhetsdata saknas helt ([Data Gap]), och inga svenska godkännanden finns registrerade.

---

# Propofol: Från allmän anestesi till migrän

## Sammanfattning

Propofol är ett intravenöst anestetikum som sedan decennier används för induktion och underhåll av generell anestesi samt för sedering vid intensivvård och procedurella ingrepp. TxGNN-modellen förutsäger att propofol i sub-anestetiska doser kan vara effektivt vid akut behandling av **migrän**, med **5 kliniska prövningar** och **20 publikationer** som för närvarande stöder denna riktning. Den starkaste evidensen utgörs av en avslutad fas 2/3-studie på pediatrisk akutmottagning, kompletterad av flera randomiserade kontrollerade studier och en systematisk översikt hos vuxna.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Induktion och underhåll av generell anestesi; sedering vid intensivvård och procedurer |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,69% |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Propofol (2,6-diisopropylphenol) verkar primärt genom positiv allosterisk modulering av GABA-A-receptorer, vilket förstärker inhibitorisk neurotransmission i centrala nervsystemet. Vid sub-hypnotiska doser (10–40 mg IV bolus) uppnås inte full anestesi, men CNS-dämpningen är tillräcklig för att påverka smärtprocessering och central nervaktivitet. Propofol har därutöver en svag blockerande effekt på natriumkanaler, vilket ytterligare kan minska neuronal urladdning.

Den mekanistiska kopplingen till migrän är biologiskt välgrundad. Migrän involverar hyperaktivering av det trigeminovaskulära systemet med central sensitisering som ett centralt patofysiologiskt drag – GABA-erga läkemedel kan dämpa denna sensitisering och bryta anfallet. I djurmodeller har propofol-hemisuccinat visats undertrycka kortikal spridande depolarisation (cortical spreading depression, CSD), som betraktas som den elektrofysiologiska korrelaten till migränaura och möjlig utlösare av migränsmärta.

Den kliniska observationen som lade grunden för detta forskningsområde var att patienter med migrän upplevde anfallsfrihet i samband med propofol-anestesi. Denna iakttagelse ledde till systematisk utforskning av sub-anestetisk dosering som abortivbehandling vid svårbehandlad och refraktär migrän, framför allt i akutmottagningssetting där standardbehandlingar inte gett tillräcklig effekt.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Fas 2/3 | Avslutad | 74 | Enda direkta fas 2/3-prövning; sub-anestetisk propofol som abortivbehandling av pediatrisk migrän på akutmottagning. Tillräcklig statistisk styrka; utgör det starkaste direkta kliniska evidensunderlaget. |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | — | Avslutad | 40 | Utvärderar effekt och säkerhet av lågdos propofol-infusion som abortivbehandling vid pediatrisk migrän. Bekräftar dosintervall och tolerabilitet i pediatrisk population. |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | — | Avbruten | 12 | Lågdos propofol för svår refraktär migrän hos vuxna på akutmottagning. Avbröts tidigt (n=12); riktningen stöder användningen men data är otillräckliga som primär evidens. Avbrottsorsak bör utredas. |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | — | Okänd | 130 | Jämförde propofol mot sevofluran som underhållsanestesi avseende postoperativ huvudvärk. Ger indirekt information om propofols skyddande effekt vid huvudvärk; lägre relevans för re-purposing. |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | — | Avslutad | 315 | Elektroakupunkturstudie vid hjärtkirurgi; propofol används enbart som anestesimedel. Minimal relevans för återanvändningsbedömning av propofol mot migrän. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Klinisk riktlinje | Headache | AHS 2025 uppdaterade riktlinjer för parenteral farmakoterapi vid akut migrän på akutmottagning; evidensvärdering inkluderar propofol. |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematisk översikt | Academic Emergency Medicine | Systematisk genomgång av propofols säkerhet och effekt vid akut migrän på akutmottagning; sammanfattar hela det befintliga evidensunderlaget. |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | Dubbelblind RCT jämför propofol + granisetron mot propofol + metoklopramid vid symtomkontroll av akut migrän. |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT utvärderar sumatriptan/propofol-kombination mot sumatriptan/placebo vid akut migrän på akutmottagning. |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | Journal of Emergency Medicine | Prospektiv RCT av lågdos propofol för pediatrisk migrän; utvärderar effekt och biverkningsprofil samt potentiellt förkortad vårdtid. |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | Pilot-RCT | Emergency Medicine Australasia | Pilot-RCT jämför propofol i sedationsdos mot standardbehandling vid initial migrän på akutmottagning. |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Översikt | Current Pain and Headache Reports | Genomgång av intravenös migränbehandling hos barn och ungdomar; diskuterar propofol bland övriga parenterala alternativ. |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Översikt | Expert Review of Neurotherapeutics | Fullständig läkemedelsprofil för propofol vid superrefraktär migrän; beskriver sub-anestetisk dosregim och patientpopulation. |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Fallserie | Headache | Tidig observationsstudie som rapporterade unik effekt av intravenöst propofol vid refraktär migrän på poliklinisk headache-mottagning; lade grunden för vidare forskning. |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Översikt | Headache | Genomgång av räddningsbehandlingar vid akut migrän inklusive propofol, lidokain och nitrous oxide; kontextualiserar propofols plats bland alternativa terapier. |

---

## Marknadsinformation Sverige

Inga registrerade läkemedelsgodkännanden för propofol finns i de tillgängliga regulatoriska data för Sverige. Propofol används dock som välbeprövat anestetikum inom sjukvården globalt och är föremål för godkännanden i ett flertal andra länder.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
Evidensunderlaget klassificeras som L2 baserat på en avslutad fas 2/3-prövning (NCT01604785, n=74) med stöd från flera RCT, en systematisk översikt och uppdaterade kliniska riktlinjer från American Headache Society. Den mekanistiska kopplingen via GABA-A-modulering och dämpning av trigeminovaskulär aktivering är biologiskt välmotiverad, och kliniska observationer av propofols anfallsbrytande effekt sträcker sig tillbaka till tidigt 2000-tal.

**För att gå vidare krävs:**
- Inhämtning av fullständig säkerhetsinformation: produktresumé, varningar och kontraindikationer för propofol (klassificeras som Blocking data gap)
- Kartläggning av läkemedelsinteraktioner med vanliga migränläkemedel (triptaner, NSAID, antiemetika, betablockerare)
- Utredning av avbrottsorsaken för NCT02492295 (säkerhetsproblem eller rekryteringssvårigheter)
- Regulatorisk strategi för off-label-användning alternativt formell indikationsutvidgning i Sverige
- Klarläggning av administrationskrav: intravenös tillgång och klinisk övervakning begränsar användningen till akutmottagning och slutenvård, vilket påverkar tillgängligheten som migränbehandling
- Större väldesignade RCT hos vuxna för att fastställa optimal dosering, effektduration och jämförbarhet mot befintliga standardterapier
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

