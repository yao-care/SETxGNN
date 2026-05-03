---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

Används **txgnn-pipeline** som bekräftar detta är ett Se (Sverige) TxGNN-projekt. Genererar nu rapporten med fokus på den indikation med starkast evidens — **inflammatorisk spondylopati** (rang 9, L1-evidens med 19 kliniska prövningar och 20 publikationer), i stället för rang 1 (acromesomelic dysplasia, L5, nollbevis).

---

# Celecoxib: Från artrit till inflammatorisk spondylopati

## Sammanfattning

Celecoxib är en selektiv COX-2-hämmare (cyklooxygenas-2-hämmare) som tillhör NSAID-klassen och används globalt för behandling av artritsjukdomar såsom osteoartrit, reumatoid artrit och ankyloserande spondylit, men är för närvarande inte godkänt på den svenska marknaden. TxGNN-modellen förutsäger att det kan vara effektivt mot **inflammatorisk spondylopati** (axial spondylartrit/ankyloserande spondylit), med **19 kliniska prövningar** och **20 publikationer** som stöder denna riktning. Sammantaget är evidensläget robust — ett unikt fynd från 2025 tyder dessutom på att celecoxib är det **enda NSAID** som kan hämma radiografisk skelettskadeprogression vid spondylartrit.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej tillgänglig (ingen registrering i Sverige) |
| Förutsagd ny indikation | Inflammatorisk spondylopati |
| TxGNN-förutsägelsepoäng | 99,80 % |
| Evidensnivå | L1 |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Gå vidare |

---

## Varför är denna förutsägelse rimlig?

Celecoxib hämmar selektivt enzymet COX-2, vilket minskar syntesen av prostaglandin E2 (PGE2). Vid inflammatorisk spondylopati — inklusive ankyloserande spondylit (AS) och axial spondylartrit (axSpA) — är COX-2-medierat PGE2 en central drivkraft för den kroniska ryggradsinflammationen, ledsmärtan och morgonstelheteten. Hämning av denna signalväg ger direkt symptomlindring och reducerad inflammation i sakroiliakalleden och kotpelaren.

Sambandet mellan artrit (etablerad indikation) och inflammatorisk spondylopati är biologiskt välgrundat: båda tillstånden delar autoimmun-medierad ledinflammation med aktivering av TNF, IL-1β, IL-6 och COX-2-signalvägen. Inflammatorisk spondylopati kan ses som en axial variant av inflammatorisk artrit och delas mekanistiskt med reumatoid artrit vad gäller prostaglandindriven synovit, vilket motiverar tillämpning av samma terapeutiska mekanism.

En anmärkningsvärd observation från 2025 (Choi et al., *BMB Reports*) är att celecoxib verkar vara det **enda NSAID som hämmar radiografisk progression** vid spondylartrit — en effekt som sannolikt inte enbart beror på COX-2-hämning utan kan involvera reglering av Wnt/BMP-signalvägen och hämning av osteoproliferation. Detta ger celecoxib en potentiellt sjukdomsmodifierande profil som skiljer det från övriga NSAIDs i denna indikation.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Fas 3 | Avslutad | 458 | 12-veckors RCT som jämför celecoxib 200 mg QD, 200 mg BID och diklofenak vid AS; direkt evidens för symtomlindringseffekt och säkerhet |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Fas 3 | Avslutad | 240 | 6-veckors randomiserad dubbelblind studie av celecoxib vs diklofenak SR hos kinesiska AS-patienter, med 6-veckors öppen förlängning på celecoxib 400 mg |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Fas 4 | Avslutad | 330 | 12-veckors randomiserad dubbelblind studie av celecoxib 200 mg och 400 mg vs diklofenak vid AS; bekräftande fas 4-studie av tidigare 6-veckors resultat |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Fas 4 | Avslutad | 156 | CONSUL-studien: utvärderar om tillägg av celecoxib till golimumab (anti-TNF) påverkar strukturell skelettskadeprogression i kotpelaren under 2 år vid AS |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Fas 4 | Avslutad | 150 | Multicenter öppen randomiserad studie (54 veckor): etanercept och celecoxib ensamt/kombinerat vid aktiv AS; primärt utfall MRI SPARCC-poäng i sakroiliakalleden |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Fas 2 | Avslutad | 42 | N-av-1-studier som individualiserar val av selektiv COX-2-hämmare vs icke-selektiv COX-hämmare vid axial spondylartrit; inkluderar proteomisk analys av prediktiva biomarkörer |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Fas 4 | Avslutad | 12 | Pilotsstudie av NSAIDs effekt på inflammatoriska lesioner vid axSpA baserat på MRI-fynd; utvärderar benmärgsödem i sakroiliakalleden |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Avslutad | 547 | Postmarketing-studie av etoricoxib (Arcoxia) och celecoxib (Celebrex) i klinisk praxis i Frankrike; användningsmönster och säkerhetsuppföljning |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Fas 2 | Okänd | 300 | Registerstudie av adalimumab + NSAIDs vs adalimumab enbart vid AS; utvärderar kombinationsterapins säkerhet och effekt |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Fas 4 | Avslutad | 9 | 6-veckors randomiserad dubbelblind pilotstudie av 4 olika NSAIDs vid axial spondylartrit; jämför smärtreduktion från baslinjen vid vecka 4 respektive vecka 6 |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematisk översikt/Meta-analys | BMB Reports | Celecoxib är det enda NSAID som hämmar radiografisk progression vid spondylartrit; effekten är sannolikt delvis COX-2-oberoende |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Paraplyöversikt | Drugs | Systematisk syntes av evidens (systematiska översikter och meta-analyser) om celecoxibs säkerhet vid kroniska muskuloskeletala sjukdomar |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Jämförande säkerhetsstudie | Scandinavian Journal of Rheumatology | Nationell kohortstudie: celecoxib och icke-selektiva NSAIDs har jämförbar kardiovaskulär och gastrointestinal blödningsrisk vid AS |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT (CONSUL) | Annals of the Rheumatic Diseases | Celecoxib tillagt golimumab minskade inte signifikant radiografisk spinal progression vid r-axSpA under 2 år jämfört med golimumab enbart |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimod kombinerat med celecoxib visade signifikant effekt och godtagbar säkerhet vid aktiv axSpA i randomiserad dubbelblind placebokontrollerad studie |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT (jämförande) | Clinical Rheumatology | Imrecoxib och celecoxib reducerade sakroiliakal inflammation vid axSpA via reglering av benmetabolism (OPG, RANKL) och angiogenes (VEGF) |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Celecoxib 200 mg BID i 12 veckor minskade BASDAI/ASDAS och BAS-METIS vid axSpA; DKK-1-nivåer korrelerade med bilddiagnostiska poäng |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | The Journal of Rheumatology | Celecoxib visade statistiskt signifikant förbättring av BASDAI, nocturnal pain och global bedömning vid AS; god tolerabilitet |
| [40153331](https://pubmed.ncbi.nlm.nih.gov/40153331/) | 2025 | Klinisk riktlinje | Clinical and Experimental Rheumatology | Evidens- och expertbaserade rekommendationer för NSAID-användning vid psoriasisartrit; understryker celecoxibs plats i inflammatorisk spondyloartropati |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Översikt | Drugs | Celecoxib indicerat i EU för OA, RA och AS; genomgång av ett decenniums klinisk erfarenhet av effekt och gastrointestinal säkerhetsprofil |

---

## Säkerhetsaspekter

> Säkerhetsdata (viktiga varningar, kontraindikationer och läkemedelsinteraktioner) är inte tillgängliga i detta evidenspaket. Se celecoxibs produktresumé (SmPC) och Läkemedelsverkets resurser för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Gå vidare**

**Motivering:**
Celecoxib uppvisar L1-evidens för inflammatorisk spondylopati med tre avslutade fas 3/4-prövningar som direkt utvärderar läkemedlet mot aktiva komparatorer, och ett unikt 2025-fynd om att celecoxib är det enda NSAID med dokumenterad hämning av radiografisk skelettskadeprogression vid spondylartrit ger ytterligare klinisk motivation för registrering på den svenska marknaden.

**För att gå vidare krävs:**
- **Regulatorisk väg:** Ansökan till Läkemedelsverket baserat på befintlig EMA-dokumentation (celecoxib är godkänt i EU för OA, RA och AS via centraliserat förfarande)
- **Säkerhetsprofil:** Fullständig genomgång av SmPC — särskilt kardiovaskulära risker (COX-2-selektiva hämmare är kontraindicerade vid etablerad hjärt-kärlsjukdom), gastrointestinal tolerabilitet och njurpåverkan
- **Läkemedelsinteraktioner:** Kartläggning av interaktioner med biologiska läkemedel (TNF-hämmare, IL-17-hämmare) och metotrexat som används parallellt vid axSpA
- **Patientpopulationsanalys:** Identifiering av svenska AS/axSpA-patienter som kan gynnas, med beaktande av kardiovaskulär riskstratifiering
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

