---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

Använder **txgnn-pipeline**-skillet för att säkerställa korrekt rapportformat för TxGNN Se-projektet, och genererar nu rapporten baserad på Evidence Pack.

---

# Prasugrel: Från akut koronarsyndrom till pulmonell hypertension

## Sammanfattning

Prasugrel är en P2Y12-receptorantagonist (thienopyridin) som internationellt är godkänd för att förebygga trombotiska komplikationer vid akuta koronarsyndrom (ACS) och perkutan koronarintervention (PCI) – läkemedlet är dock **inte registrerat i Sverige**. TxGNN-modellen förutsäger att det kan vara verksamt mot **pulmonell hypertension**, med trombocytaktivering som teoretisk mekanistisk länk till sjukdomspatogenesen. Evidensunderlaget är emellertid mycket svagt – de identifierade kliniska prövningarna och publikationerna saknar direkt relevans för denna indikation, vilket placerar förutsägelsen på **evidensnivå L5**.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat i Sverige; internationellt godkänt för akut koronarsyndrom (ACS) och PCI |
| Förutsagd ny indikation | Pulmonell hypertension |
| TxGNN-förutsägelsepoäng | 99,88% (modellrang 316) |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Prasugrel är en prodrug som efter hepatisk metabolism bildar en aktiv metabolit som irreversibelt blockerar ADP-receptorn P2Y12 på trombocytytan. Detta förhindrar ADP-medierad trombocytaggregation och ger en starkare och mer förutsägbar antitrombotisk effekt än äldre thienopyridiner som klopidogrel.

Vid pulmonell arteriell hypertension (PAH) är trombocytaktivering en känd komponent i sjukdomspatogenesen: aktiverade trombocyter frisätter tromboxan A₂, serotonin och PDGF, vilka driver pulmonell vasokonstriktion och progressiv kärlremodellering. Teoretiskt sett kan P2Y12-hämning minska detta trombocytmedierade bidrag till sjukdomsprogression.

Trots den mekanistiska teorin är standardbehandling för PAH idag baserad på endotelinreceptorantagonister (ERA), PDE5-hämmare och prostacyklinpreparat – antitrombotisk behandling ingår inte i etablerade riktlinjer. Inget kliniskt prövningsprogram undersöker prasugrel specifikt vid PAH, och risk-nyttaförhållandet är helt okänt i denna patientgrupp.

---

## Kliniska prövningar

Sökningen identifierade 2 prövningar, men båda bedöms som **icke relevanta (grad C)** – de berör varken prasugrel eller pulmonell hypertension:

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|--------|-----------|--------------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Avslutad | 500 | Tvärsnittsstudie av NOAC-behandling hos äldre patienter med icke-valvulär förmaksflimmer i Spanien – ingen koppling till prasugrel eller pulmonell hypertension |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Avslutad | 300 | Retrospektiv multicenter-studie av cancerrelaterad venös tromboembolism; utvärderar andelen patienter som inte uppfyller CARAVAGGIO-inklusionskriterier – ingen koppling till prasugrel eller pulmonell hypertension |

---

## Litteraturbevis

Sökningen identifierade 2 publikationer med begränsad direkt relevans:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Registerstudie (observationell) | Kardiologiia | ACTIVE-registret analyserar bakgrundsbehandling med kardiovaskulära läkemedel och dess inverkan på COVID-19-dödlighet hos 5 808 patienter – prasugrel eller PAH berörs inte direkt |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Kohortstudie | Current Medical Research and Opinion | Faktorer kopplade till klopidogrelanvändning och följsamhet hos ACS-patienter efter PCI; nämner prasugrel som jämförelsepreparat – inte relevant för PAH-indikationen |

---

## Marknadsinformation Sverige

Prasugrel är **inte registrerat i Sverige** och har inga beviljade godkännanden i den svenska läkemedelsdatabasen. Inga produktuppgifter finns att redovisa.

---

## Säkerhetsaspekter

Inga detaljerade varningsdata, kontraindikationer eller läkemedelsinteraktioner är tillgängliga i detta evidence pack för den svenska marknaden.

> Se produktresumén (SmPC) för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots att TxGNN genererar ett högt förutsägelsepoäng (99,88%) för pulmonell hypertension saknas all direkt klinisk evidens – de identifierade prövningarna och publikationerna är inte relevanta för denna kombination. Resultatet är en hypotesgenerande signal (L5) och utgör inte underlag för kliniska beslut.

**För att gå vidare krävs:**
- Riktad litteratursökning av prekliniska studier om P2Y12-hämning i experimentella PAH-modeller
- Kontakt med PAH-specialister för bedömning av om antitrombotisk behandling kan ha kompletterande roll
- Genomgång av prasugrels fullständiga SmPC (EU-godkänd version) för säkerhetsprofil och kontraindikationer
- Beakta att **migrän med PFO (rang 2, L4-evidens)** har ett starkare mekanistiskt och empiriskt underlag och bör prioriteras som nästa utvärderingssteg
- Klargöra registreringsväg i Sverige (centraliserat EMA-förfarande) om klinisk prövning planeras
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

