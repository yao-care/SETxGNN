---
layout: default
title: Lisinopril
parent: Endast modellprediktion (L5)
nav_order: 267
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "lisinopril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
description: "Lisinopril: predikterad ny indikation Pulmonary hypertension owing to lung disease and/or hypoxia (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Lisinopril
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## Lisinopril: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

---

## Sammanfattning

Lisinopril är en ACE-hämmare som ursprungligen användes för att behandla högt blodtryck och hjärtinfarkt. TxGNN-modellen förutsäger att det kan vara effektivt mot **posterolateral hjärtinfarkt**, men för närvarande finns **inga kliniska prövningar** och **ingen publicerad litteratur** som specifikt stöder denna förutsägelse. Förutsägelsen speglar sannolikt den redan godkända indikationen hjärtinfarkt snarare än en ny behandlingsmöjlighet.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN-förutsägelsepoäng | 0.9989 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 17 av 17) |
| Antal godkännanden | 17 (giltiga: 17) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Baserat på känd information är lisinopril en ACE-hämmare. Den hämmar renin-angiotensin-aldosteronsystemet (RAAS), sänker blodtrycket och begränsar ogynnsam ombyggnad av hjärtmuskeln efter en infarkt.

Posterolateral hjärtinfarkt är en anatomisk undertyp av hjärtinfarkt, en sjukdom för vilken lisinopril redan är etablerat. Sambandet är därför mekanistiskt rimligt. Den höga poängen beror sannolikt på att modellen ärver information från den överordnade diagnosen hjärtinfarkt, inte på ny evidens. Det är alltså snarast en ontologidriven förutsägelse och inte en genuin signal om läkemedelsåteranvändning.

Inga studier som specifikt rör denna undertyp har identifierats.

---

## Marknadsinformation Sverige

Samtliga 17 godkännanden är avregistrerade. Godkänd indikationstext finns inte registrerad. De fem första godkännandena visas nedan.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 61807 | Lisinopril Ebb | Tablett | Ej angiven |
| 16929 | Lisinopril STADA | Tablett | Ej angiven |
| 10870 | Zestril | Tablett | Ej angiven |
| 60550 | Lisiliv | Tablett | Ej angiven |
| 16928 | Lisinopril STADA | Tablett | Ej angiven |

---

## Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer har inte kunnat hämtas, så säkerhetsbilden nedan bygger på kunskapsgrafen och interaktionsdatabasen.

- **Kontraindikationer och risktillstånd enligt kunskapsgrafen** (inte hämtade från produkttext): njursjukdom, leversjukdom, angioödem (inklusive ärftligt och ACE-hämmarorsakat), pankreatit, gallblåsesjukdom, systemisk lupus erythematosus, diabetes och diabetesketoacidos, neutropeni och agranulocytos, aortastenos, lågt blodtryck, hyperparathyroidism, leverencefalopati samt kaliumbrist.
- **Läkemedelsinteraktioner**: totalt 308 interaktioner är registrerade. Bland de som visas finns två av allvarlig grad (**kaliumcitrat** och **kaliumbikarbonat**, risk för hyperkalemi). Flera av måttlig grad nämns också, bland andra:
  - kortikosteroider (hydrokortison, dexametason, betametason, triamcinolon, budesonid)
  - diabetesläkemedel (metformin, alogliptin, saxagliptin, kanagliflozin, dapagliflozin, empagliflozin, klorpropamid)
  - acetylsalicylsyra, morfin, bupropion, dronabinol
  - pikosulfat och polyetylenglykol med elektrolyter
- Vid riskbedömning bör särskilt njurfunktion (bland annat vid malign renovaskulär hypertoni och bilateral njurartärstenos) och kaliumnivåer följas.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för posterolateral hjärtinfarkt saknar helt specifika kliniska prövningar och litteratur (L5). Den ligger nära den redan etablerade indikationen hjärtinfarkt och tillför knappast något nytt.

**För att gå vidare krävs:**
- Hämta produktresumé för varningar och kontraindikationer, vilket är ett blockerande datagap för säkerhetsscreeningen.
- Komplettera data om verkningsmekanismen från DrugBank.
- Fastställa om undertyper av hjärtinfarkt behöver bedömas separat eller omfattas av den befintliga indikationen.
- Klargöra marknadsläget, eftersom det för närvarande inte finns något giltigt svenskt godkännande.

**Övriga förutsägelser i listan:** De övriga nio förutsägelserna har likaså låg evidens och bör avvaktas. Där finns två små kliniska studier med lisinopril (PMID 17047621 och 14524095), men båda är sannolikt små och okontrollerade, så kvaliteten är osäker. Den kan motivera en fortsatt forskningsfråga, men inte ett beslut att gå vidare.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

