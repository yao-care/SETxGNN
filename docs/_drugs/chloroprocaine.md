---
layout: default
title: Chloroprocaine
parent: Endast modellprediktion (L5)
nav_order: 93
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Chloroprocaine: predikterad ny indikation Cauda equina-syndrom (evidensnivå L5). Ursprunglig indikation: Uppgift saknas (godkännandetexterna är tomma)"
monitor_inn: "chloroprocaine"
predicted_indications: ["cauda equina syndrome"]
---

# Chloroprocaine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

# Kloroprokain: Från lokalanestesi till cauda equina-syndrom

---

## Sammanfattning

Kloroprokain är ett lokalanestetikum av estertyp som i Sverige har marknadsförts under namnet Ampres (injektionsvätska, lösning). Något godkänt användningsområde finns inte angivet i de data som sammanställts för rapporten.
TxGNN-modellen förutsäger **cauda equina-syndrom** med mycket hög poäng (99,0 %). Underlaget består av **0 kliniska prövningar** och **4 publikationer**. Den förutsägelsen bedöms sannolikt spegla en **biverkningskoppling** (neurotoxicitet vid spinal- och epiduralbedövning) och inte en möjlig behandlingseffekt.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Uppgift saknas (godkännandetexterna är tomma) |
| Förutsagd ny indikation | Cauda equina-syndrom |
| TxGNN-förutsägelsepoäng | 99,0 % |
| Evidensnivå | L4 (endast mekanism- och översiktsdata, inga studier som stöder behandlingseffekt) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Kloroprokain är ett lokalanestetikum av estertyp som blockerar spänningsstyrda natriumkanaler och därmed hindrar nervimpulser. Detaljerade mekanismdata finns inte tillgängliga i underlaget, men denna verkningsmekanism är väl känd för läkemedelsklassen.

Kopplingen till cauda equina-syndrom är sannolikt **inte terapeutisk**. Litteraturen beskriver syndromet som en komplikation efter spinal- och epiduralbedövning med lokalanestetika, däribland kloroprokain. Den föreslagna förklaringen är neurotoxicitet vid höga lokala koncentrationer eller ojämn fördelning, till exempel vid kontinuerliga spinalkatetrar. Den höga poängen speglar därför troligen denna association i kunskapsgrafen.

Det finns ingen rimlig mekanism enligt vilken natriumkanalblockad skulle behandla cauda equina-syndrom. Tillståndet orsakas oftast av mekanisk kompression och kräver vanligen kirurgisk dekompression.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta anaesthesiologica Scandinavica | Jämförelse av kloroprokain och lidokain (med fentanyl) för selektiv spinalanestesi vid dagkirurgisk transuretral prostataresektion. Studien gäller anestesi, inte behandling av cauda equina-syndrom. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Översikt | Acta anaesthesiologica Scandinavica | Översikt av kloroprokain vid spinalanestesi som alternativ till lidokain (transienta neurologiska symtom). Neurologiska följdtillstånd har beskrivits efter intratekal injektion av stora doser konserveringsmedelshaltigt preparat. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Översikt | Drug safety | Översikt av komplikationer vid regional anestesi (misslyckad blockad, nervskada, toxicitet hos lokalanestetika) och hur de kan förebyggas. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Fallrapport | Regional anesthesia | Två fall av cauda equina-syndrom efter spinal-epiduralanestesi. Tidigare rapporter har satt lidokain, kloroprokain och prokain i samband med syndromet. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 58182 (indragen) | Ampres | Injektionsvätska, lösning | Uppgift saknas |
| 58183 (indragen) | Ampres | Injektionsvätska, lösning | Uppgift saknas |

Tillverkare: B. Braun Melsungen AG.

---

## Säkerhetsaspekter

- **Möjliga kontraindikationer enligt kunskapsgrafen** (relationer i en kunskapsgraf, inte produkttext): njursjukdom, leversjukdom, gallblåsesjukdom, myasthenia gravis (inklusive vuxendebuterande form), sjukdom i neuromuskulära synapsen, butyrylkolinesterasbrist, hjärt-kärlsjukdom och hjärtsjukdom. Dessa uppgifter bör verifieras mot produktresumén.
- **Läkemedelsinteraktioner** (12 registrerade):
  - **Allvarlig:** nitrit (”nitrous acid”).
  - **Måttliga:** sulfasalazin samt andra lokalanestetika (lidokain topikalt och oftalmiskt, bensokain, kokain nasalt och topikalt, tetrakain topikalt och oftalmiskt, oxibuprokain, cinkokain).
  - **Lindrig:** hyaluronidas.
- Viktiga varningar och kontraindikationer från produktresumén saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga TxGNN-poängen verkar bero på att cauda equina-syndrom är en känd komplikation av neuraxial anestesi och inte på någon behandlingseffekt. Det finns inga kliniska prövningar, och inga publikationer visar nytta för patienter med syndromet.
- Båda svenska godkännandena är dessutom indragna.

**För att gå vidare krävs:**
- Ett mekanistiskt resonemang för varför kloroprokain skulle kunna behandla cauda equina-syndrom (för närvarande saknas det).
- Verkningsmekanismdata (kan hämtas från DrugBank).
- Varningar och kontraindikationer från produktresumén (Läkemedelsverket), som är en förutsättning för säkerhetsbedömning.
- Prekliniska eller kliniska data som visar behandlingsnytta, om kandidaten ska utvärderas vidare.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

