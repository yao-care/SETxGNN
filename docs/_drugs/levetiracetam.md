---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

Jag använder `txgnn-pipeline`-skillet för kontext. Nu genererar jag rapporten baserat på Evidence Pack-data.

---

# Levetiracetam: Från epilepsi (partiella anfall) till visuell epilepsi

## Sammanfattning

Levetiracetam är ett etablerat andra generationens antiepileptikum som globalt är godkänt för behandling av partiella anfall, myoklona kramper vid juvenil myoklonisk epilepsi och primärt generaliserade tonisk-kloniska anfall. TxGNN-modellen förutsäger med **99,98 %** säkerhet att levetiracetam kan vara effektivt mot **visuell epilepsi** – en reflexepilepsiform utlöst av visuella stimuli – och placerar detta som den högst rankade nya indikationen (global rang 98). Evidensbasen inkluderar **9 kliniska prövningar** och **20 publikationer** som stöder användningen av levetiracetam vid besläktade epilepsitillstånd.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Epilepsi – partiella anfall (adjungerad och monoterapibehandling; internationellt godkänt, ej registrerat i Sverige per aktuell data) |
| Förutsagd ny indikation | Visuell epilepsi (visual epilepsy) |
| TxGNN-förutsägelsepoäng | 99,98 % (rang 98 globalt) |
| Evidensnivå | L3 – Systematiska översikter och observationsstudier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanism-data saknas i det aktuella evidenspaketet. Baserat på tillgänglig litteratur inom evidensgranskningen är levetiracetam ett antiepileptikum som binder till synaptiskt vesikelprotein SV2A (synaptic vesicle protein 2A) och hämmar L-typ kalciumkanaler, vilket modulerar neurotransmittorfrisättningen och därigenom dämpar abnorm neuronal urladdning (PMID 34903423; PMID 35848684). Denna mekanism skiljer sig fundamentalt från klassiska antiepileptika som verkar via natriumkanaler eller GABA-systemet, och förklarar läkemedlets breda antiepileptiska profil.

Visuell epilepsi är en reflexepilepsiform där anfall utlöses av visuella stimuli såsom flimrande ljus eller kontrastrika mönster. Tillståndet delar kärnmekanismer med andra anfallstyper – abnorm kortikal hyperexcitabilitet och okontrollerad neuronal urladdning – och SV2A-modulering kan förväntas dämpa denna hyperexcitabilitet oavsett utlösande stimulus. Levetiracetams dokumenterade effekt mot myoklona anfall och fotosensitiva epilepsier (t.ex. Jeavons syndrom, sunflower syndrome) stärker ytterligare kopplingen till visuellt utlösta anfallstyper.

I litteraturen finns dessutom fallrapporter och konsensusbaserade expertpanelsrekommendationer som specifikt nämner levetiracetam som ett behandlingsalternativ vid eyelid myoclonia-epilepsi och fotosensitiva generaliserade epilepsier, vilka patofysiologiskt överlappar med visuell epilepsi (PMID 37326215; PMID 16302877).

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|----------------|-----|--------|-----------|--------------|
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Fas 4 | Okänd | 40 | Utvärderar levetiracetam som lovande alternativ till fenobarbital vid neonatala anfall med signifikant bättre biverkningsprofil |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Avslutad | 31 | Öppen studie av LEV vid profylaktisk behandling av migrän med/utan aura (visuella störningar); utvärderar säkerhet och effektivitet |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Fas 2 | Avbruten | 1 | Testade om LEV kan minska hippokampal hyperaktivitet vid psykos med visuell scenprocesseringsuppgift via fMRI; avbruten tidigt |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Fas 3 | Ännu ej påbörjad | 580 | Randomiserad, dubbelblind, placebokontrollerad studie av profylaktisk LEV för att förbättra funktionellt utfall vid intracerebral blödning i akutfasen |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Fas 4 | Avslutad | 111 | LICEO-studien: prospektiv observationsstudie av nya AEDs (inkl. LEV) som förstahandsval kombinationsterapi vid fokal epilepsi i klinisk vardag |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Fas 2 | Avslutad | 87 | Randomiserad, dubbelblind, placebokontrollerad studie av kognitiva effekter av LEV (20–60 mg/kg/dag) som adjungerad terapi vid refraktära partiella anfall hos barn 4–16 år |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Fas 2 | Avslutad | 62 | Undersöker om LEV reducerar hippokampal hyperaktivitet vid psykotiska tillstånd med fMRI; inkluderar visuell scenprocesseringsuppgift som engagerar anteriora hippokampus |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Fas 3 | Ännu ej påbörjad | 1 649 | MAST-studien: definierar bästa praxis för AED-användning efter traumatisk hjärnskada; inkluderar jämförelse fenytoin vs. LEV för kortvarig anfallsprofylax |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Fas 1/2 | Pågående (inbjudan) | 24 | Genterapi (AVASPA) för Canavan-sjukdom med kongenital vit substanssjukdom; LEV ingår som del av anfallshantering i studieprotokollet |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | *Pediatrics* | Randomiserad kontrollerad studie jämför LEV vs. fenobarbital vid neonatala anfall; LEV visar god effekt med fördelaktig säkerhetsprofil |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | *Seizure* | Öppen RCT: fenytoin vs. LEV vid akuta symtomatiska anfall hos barn med akut encefalitsyndrom; direkt jämförelse av effekt och säkerhet |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | Fas 3 RCT | *The Lancet Neurology* | PEACH-studien: dubbelblind, placebokontrollerad Fas 3; profylaktisk LEV vid intracerebral blödning minskade inte signifikant akuta anfallsförekomsten |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematisk översikt | *Neurocritical Care* | Meta-analys av LEV för anfallsprofylax vid ICH, TBI och neurointensivvård; effekt, dosering och biverkningar granskas systematiskt |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematisk översikt | *Journal of Neurology* | Nätverks-meta-analys av anfallsmediciner vid idiopatisk generaliserad epilepsi; utvärderar LEV som monoterapi och tilläggsbehandling |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematisk översikt | *Epilepsy & Behavior* | Meta-analys av LEV för myoklona anfall vid idiopatisk generaliserad epilepsi (inkl. JME); jämför effekt och säkerhet med övriga ASM |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Översikt | *CNS Drugs* | Bred genomgång av levetiracetam i epilepsibehandling; globalt godkänt för partiella anfall, myoklona anfall vid JME samt primärt generaliserade tonisk-kloniska anfall |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Klinisk riktlinje | *Neurocritical Care* | NCS klinisk praxisriktlinje för anfallsprofylax hos vuxna med måttlig–svår TBI; evidensbaserad genomgång av LEVs plats i behandlingen |
| [37326215](https://pubmed.ncbi.nlm.nih.gov/37326215/) | 2023 | Konsensus | *Epilepsia* | Internationell expertpanel för hantering av eyelid myoclonia-epilepsi (inkl. fotosensitiva former); LEV nämns som behandlingsalternativ |
| [16302877](https://pubmed.ncbi.nlm.nih.gov/16302877/) | 2005 | Översikt | *Epilepsia* | Fotosensitivitet vid idiopatisk generaliserad epilepsi; beskriver patofysiologi och antiepileptisk behandling vid visuellt utlösta anfall – direkt relevant för visuell epilepsi |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Levetiracetams SV2A-medierade mekanism är teoretiskt och kliniskt motiverat tillämpbar på visuell epilepsi, och den breda evidensbasen för besläktade fotosensitiva och reflexepilepsier är lovande. Avvakta-rekommendationen grundar sig i frånvaron av registrering i Sverige, kompletta svenska/europeiska säkerhetsdata samt att det saknas dedikerade kontrollerade studier specifikt för visuell epilepsi som enskild indikation.

**För att gå vidare krävs:**
- Granska och sammanställa studier som specifikt undersöker levetiracetam vid fotosensitiv epilepsi och reflexepilepsier (Jeavons syndrom, sunflower syndrome, reading epilepsy)
- Inhämta fullständig produktresumédata (SmPC) för varningar, kontraindikationer och läkemedelsinteraktioner från Läkemedelsverket (MPA) eller EMA
- Verifiera aktuell regulatorisk status i Sverige – notera att levetiracetam (Keppra®) är EMA-godkänt och troligen tillgängligt via generika; datafältet "ej registrerat" behöver verifieras mot aktuell Läkemedelsdatabas
- Komplettera verkningsmekanism (MOA)-data via DrugBank API (DG002)
- Överväga prospektiv fallserie eller retrospektiv kohortstudie som specifikt inkluderar patienter med visuell epilepsi behandlade med levetiracetam
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

