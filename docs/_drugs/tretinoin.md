---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

Med `txgnn-pipeline`-skillet laddat som vägledning, genererar jag nu rapporten baserat på Evidence Pack-data. Tretinoin (ATRA) är ett välkänt retinoid – jag använder etablerad farmakologi för att fylla luckor där `original_indications` och `original_moa` saknas i JSON:en.

---

# Tretinoin: Från akne och akut promyelocytisk leukemi till reumatoid nodulos

## Sammanfattning

Tretinoin (all-trans-retinsyra, ATRA) är ett retinoid som traditionellt används för behandling av akne vulgaris (topikalt) och akut promyelocytisk leukemi (systemiskt). TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **reumatoid nodulos**, men det finns för närvarande **inga kliniska prövningar** och **inga relevanta publikationer** som stödjer denna specifika indikation. Förutsägelsen baseras uteslutande på kunskapsgrafens strukturella samband och saknar empirisk evidensgrund.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Akne vulgaris (topikalt); akut promyelocytisk leukemi (systemiskt) – inga svenska godkännanden tillgängliga |
| Förutsagd ny indikation | Reumatoid nodulos (rheumatoid nodulosis) |
| TxGNN-förutsägelsepoäng | 99,84% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det inlämnade underlaget. Baserat på känd farmakologi är Tretinoin en potent agonist för retinsyrareceptorerna RARα, RARβ och RARγ, vilka reglerar genuttryck kopplat till celldifferentiering, immunmodulering och inflammation. Tretinoin är en del av retinoidklassen (vitamin A-derivat) vars effekt vid akne (normalisering av follikulär keratinisering och talgproduktion) och vid APL (induktion av leukemisk blastdifferentiering via RARα-PML-fusionsproteinbrytning) är väldokumenterad.

Den teoretiska kopplingen till reumatoid nodulos bygger på att RARα/β/γ-aktivering kan dämpa NF-κB-signalering och gynna M2-makrofagpolarisering – mekanismer som i teorin motverkar granulombildning, vilket är det centrala patologiska draget vid reumatoid nodulos. Dessutom har ATRA visat immunsuppressiva egenskaper genom reglering av Th17/Treg-balansen, vilket är relevant vid autoimmuna tillstånd.

Det bör dock understrykas att detta samband är rent spekulativt. Det saknas helt preklinisk eller klinisk forskning specifikt inriktad på Tretinoin vid reumatoid nodulos, och avståndet från de etablerade indikationerna till detta reumatologiska tillstånd är mekanistiskt sett betydande.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Tretinoin är inte godkänt i Sverige. Inga godkännanden är registrerade hos Läkemedelsverket (MPA). Produkten saknar marknadsstatus i det svenska systemet.

---

## Cytotoxicitet

Tretinoin uppfyller kriterierna för antineoplastisk klassificering: läkemedlet används systemiskt vid akut promyelocytisk leukemi (APL), en cancerdiagnos, och ingår i etablerade cytotoxiska behandlingsprotokoll. Bedömningen nedan avser systemisk användning.

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Differentieringsmedel (målriktad terapi) – RARα-agonist som inducerar terminal differentiering av leukemiska blastar via nedbrytning av PML-RARα-fusionsproteinet |
| Myelosuppressionsrisk | Medel – Differentieringssyndrom (tidigare kallat ATRA-syndrom) kan utlösas under APL-behandling med feber, andningspåverkan och organsvikt; direkt benmärgssuppression är lägre än vid konventionell cytostatikabehandling |
| Emetogenicitetsklassificering | Låg–Medel |
| Övervakningspunkter | Fullständigt blodstatus med differentialräkning, levervärden (ALAT, ASAT, ALP), kreatinin, koagulationsprover (PK/INR, fibrinogen); klinisk övervakning för tecken på differentieringssyndrom (feber, dyspné, pleuravätska, viktökning) |
| Hanteringsskydd | Systemisk Tretinoin (mjuka kapslar) hanteras enligt rutiner för antineoplastiska läkemedel vid beredning och administrering; topikal beredning kräver inga speciella cytotoxiska skyddsåtgärder |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> **Notering:** Fullständig säkerhetsdata (varningar, kontraindikationer, läkemedelsinteraktioner) för det svenska godkännandet saknas i detta underlag. Detta är en identifierad dataklass av blockerande karaktär (DG001) som måste åtgärdas innan en formell säkerhetsbedömning kan genomföras.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots ett högt TxGNN-förutsägelsepoäng på 99,84% är evidensnivån för Tretinoin vid reumatoid nodulos klassificerad som L5 – det finns inga kliniska prövningar och inga direkta publikationer som stödjer denna indikation, och den mekanistiska länken är rent spekulativ utan stöd av prekliniska data.

**För att gå vidare krävs:**
- Systematisk litteratursökning om ATRA:s effekt på granulombildning, makrofagpolarisering och NF-κB-signalering vid reumatoida tillstånd
- Identifiering av in vitro- eller djurmodellstudier för reumatoid nodulos
- Farmakologisk bedömning av lämplig administreringsväg (topikalt vs. systemiskt) vid reumatoid nodulos
- Inhämtande av fullständig produktresumé för säkerhetsbedömning (åtgärda DG001: TFDA/EMA-varningar och kontraindikationer)
- Komplettering av verkningsmekanismdata via DrugBank API (åtgärda DG002)
- Kontakt med reumatologisk expertis för klinisk bedömning av hypotesens relevans
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

