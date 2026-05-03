---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Diazepam
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

Använder **txgnn-pipeline** för kontextuell förankring av rapporten, sedan skriver jag rapporten enligt promptspecifikationen v5.

---

# Diazepam: Från ångestlindring till insomni

## Sammanfattning

Diazepam är ett klassiskt bensodiazepin med lång klinisk historia, primärt använt för ångestlindring, kramplösning och muskelrelaxation. TxGNN-modellen förutsäger med en prediktionspoäng på nära **100 %** (global rank 8) att diazepam kan vara effektivt mot **insomni**, understött av **24 identifierade kliniska prövningar** och **18 publikationer** i evidensbasen. Det finns ett direkt mekanistiskt samband via GABA-A-receptoraktivering, och ett historiskt randomiserat dubbelblindförsök bekräftar klinisk effekt specifikt för sömnstörningar.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej registrerat i Sverige – ingen MPA-indikationstext tillgänglig |
| Förutsagd ny indikation | Insomni |
| TxGNN-förutsägelsepoäng | 100,0 % |
| Evidensnivå | L1 |
| Marknadsstatus i Sverige | Inte registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Gå vidare med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Diazepam är en positiv allosterisk modulator (PAM) av GABA-A-receptorn – den viktigaste hämmande jonkanalreceptorn i centrala nervsystemet. Vid bindning till bensodiazepinbindningsstället förstärker diazepam GABA:s förmåga att öppna kloridjonkanalen, vilket leder till hyperpolarisering av neuronen och dämpning av elektrisk aktivitet i hjärnan. Detta ger upphov till de kliniskt välkända effekterna: ångestdämpning, sedation, muskelrelaxation och kramplindring.

Kopplingen till insomni är direkt och biologiskt välgrundad: GABA-A-aktivering sänker sömnlatens (tid till insomnande), ökar total sömntid och reducerar uppvakningar under natten – effekter som direkt adresserar insomnikärnkriterierna. Det historiska randomiserade dubbelblindförsöket (PMID 6113175) som jämförde diazepam mot lormetazepam hos 100 insomniapatienter bekräftar klinisk verkan, och diazepam används fortfarande rutinmässigt som positiv referenskontroll i prekliniska insomniamodeller världen över.

Diazepams farmakologiska profil medför dock specifika begränsningar. Den långa halveringstiden (20–100 timmar för modersubstansen, 36–200 timmar för aktiv metabolit nordiazepam) ger risk för morgonresidualsedation och kognitiv kumulativ påverkan. REM-sömn och djupsömn (N3) supprimeras, och risken för toleransutveckling, beroende och rebound-insomni vid utsättning är väldokumenterad. Moderna kliniska riktlinjer rekommenderar därför KBT-I och nyare sömnmedel (orexinantagonister, melatonin) som förstahandsval framför bensodiazepiner.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Fas 3 | Aktiv, ej rekryterande | 260 | Randomiserad longitudinell studie av blindad nedtrappning av hypnotika (inkl. diazepam) kombinerat med KBT-I; utvärderar relativ effektivitet jämfört med öppen nedtrappning för att uppnå utsättning hos insomniapatienter |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Fas 2 | Avslutad | 74 | Utvärderar hur nedtrappningshastighet och personlighetsegenskaper påverkar framgångsrik utsättning av bensodiazepinhypnotika vid sömnstörning; diazepam är det primärt studerade läkemedlet |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Avslutad | 188 | Ny mekanism för att hjälpa äldre vuxna att sluta med sömnmedicin; kombinerar hypnotikanedtrappning med KBT-I och insomnifokuserade kognitiva och beteendestrategier |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Avslutad | 128 | Randomiserad kontrollerad studie som jämför psykologiskt stöd mot Acceptance and Commitment Therapy (ACT) som tillägg till nedtrappningsprogram för BZD-beroende insomniapatienter |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | Avslutad | 114 | Psykosocial intervention PASSE-65+ för äldre BZD-användare (inklusive insomni- och ångestiondikationer); utvärderar gradvis dosminskning med psykosocialt stöd |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Fas 4 | Avslutad | 17 | Placebokontrollerad multicenterstudie av ramelteon som tillägg vid dosminskning av BZD/non-BZD-hypnotika vid kronisk insomni; diazepam ingår i nedtrappningsgruppen |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Fas 1 | Avslutad | 12 | Enkeldos randomiserad crossover-studie av GABA-modulatorn AZD7325 hos friska frivilliga; diazepam (Valium) används som farmakodynamisk referenssubstans för kalibrering av biomarkörmätningar |
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | N/A | Okänd | 74 | Direkt jämförelse av klonazepam mot intermittent oral diazepam för återfallsprofylax av feberkramper hos barn; bidrar med metodologisk referens för bensodiazepinjämförande studiedesign |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Dubbelblind 7-dagarsstudie (n=100): diazepam 5 mg vs. lormetazepam 1 mg för sömnstörningar; lormetazepam var signifikant överlägset (p<0,05) för insomningstid och sömnlängd – bekräftar diazepams hypnotiska verkan men pekar på relativ svaghet jämfört med kortverkande BZD |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Översikt | Bioorganic Chemistry | Syntetisk klinisk genomgång av GABA-A-modulatorer; diazepam definieras explicit som referens-PAM vid epilepsi, ångest och **insomni**, med notering om biverkningsprofil (sedation, minnesproblem, beroendeutveckling) |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Djurstudie | Nature Neuroscience | Långtidsbehandling med diazepam försämrar dendritisk ryggradsstabilitet via mitokondriellt 18 kDa TSPO och orsakar kognitiv nedsättning hos möss – viktig säkerhetssignal om neurotoxicitet vid kronisk insomnibehandling |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Kohortstudie | Cell & Mol Biol Lett | Kroniskt BZD-bruk (diazepam och zolpidem) för insomni och ångest associerat med förhöjd risk för bröstcancer via GABA-A-receptorer på tumörceller; indikerar behov av långtidssäkerhetsövervakning |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Systematisk översikt | Front Pharmacology | Meta-analys (8 databaser) av Suanzaoren-formuleringar för insomni; diazepam används som aktivt jämförelseläkemedel i inkluderade RCT och ger referensram för hypnotisk effektstorlek |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Djurstudie | China J Chin Materia Medica | Diazepam 2 mg/kg som positiv kontroll i CUMS-inducerad depression- och insomnimodell hos möss; bekräftar dosrespons och standardiserad modellvaliditet |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Djurstudie | J Pharm Biomed Analysis | Diazepam som positiv kontroll i PCPA-råttmodell; metabolomisk profil av sedativa/hypnotiska effekter inklusive neurotransmittorförändringar vid insomni |
| [34983880](https://pubmed.ncbi.nlm.nih.gov/34983880/) | 2021 | Djurstudie | Experimental Neurobiology | Validering av tyroxin-inducerad insomniamodell (face-, construct- och predictive validity); diazepam används för prediktiv validering och stärker modellens representativitet för läkemedelsutvärdering |
| [32240473](https://pubmed.ncbi.nlm.nih.gov/32240473/) | 2020 | Djurstudie | Chin J Integrative Medicine | Sedativa och hypnotiska effekter av Polygala tenuifolia hos äldre insomniråttor; diazepam ingår som kontrollgrupp för sömnparametermätning (sömntid, insomningstid) |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Gå vidare med försiktighet**

**Motivering:**
- Diazepam har ett direkt och väletablerat mekanistiskt samband med sömnindukton via GABA-A-aktivering, och evidensbasen inkluderar ett historiskt RCT specifikt för insomni. Moderna kliniska prövningar fokuserar dock uteslutande på utsättningsstrategier – inte terapeutisk nytta – vilket avspeglar att nuvarande riktlinjer aktivt avråder från ny insättning av bensodiazepiner vid insomni till förmån för KBT-I och nyare sömnmedel.

**För att gå vidare krävs:**
- Formell registrering hos Läkemedelsverket (MPA) – 0 godkännanden identifierade i Sverige
- Insamling av fullständig säkerhetsdata (kontraindikationer, varningar och interaktionsprofil) från godkänd SmPC
- Systematisk bedömning av läkemedelsinteraktioner, särskilt med CNS-dämpande medel, alkohol och opioider
- Klinisk risk-nyttaanalys för insomniindikationen: jämförelse mot KBT-I (förstahandsval), melatonin och orexinantagonister (lemborexant, suvorexant)
- Avgränsning av indikation till kortvarig användning (< 2–4 veckor) med hänsyn till beroenderisk, rebound-insomni och kognitiv påverkan vid långtidsbruk
- Utformning av en risk-minimeringsplan (i likhet med REMS-upplägg) om registrering för insomni aktualiseras, givet substansens beroendeframkallande potential
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

