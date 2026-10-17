---
layout: default
title: Atazanavir
parent: Endast modellprediktion (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Atazanavir: predikterad ny indikation Felint förvärvat immunbristsyndrom (kattens AIDS) (evidensnivå L5). Ursprunglig indikation: HIV-infektion och AIDS (enligt kunskapsgrafen"
monitor_inn: "atazanavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Atazanavir
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

# Atazanavir: Från HIV-infektion och AIDS till felint förvärvat immunbristsyndrom

---

### Sammanfattning

Atazanavir är en proteashämmare som ursprungligen användes för att behandla HIV-infektion och AIDS. TxGNN-modellen förutsäger att det kan vara effektivt mot **felint förvärvat immunbristsyndrom (kattens AIDS)**, men för denna förutsägelse finns **inga kliniska prövningar och ingen publicerad litteratur**. Förutsägelsen bygger enbart på modellen och bör tolkas försiktigt.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | HIV-infektion och AIDS (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsägd ny indikation | Felint förvärvat immunbristsyndrom (kattens AIDS) |
| TxGNN-förutsägelsepoäng | 99,98 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Baserat på känd information är atazanavir en proteashämmare mot HIV-1, och dess effekt vid HIV-infektion är väl belagd. Mekanistiskt kan den vara tillämpbar på kattens immunbristvirus.

Felint immunbristvirus (FIV) är ett lentivirus med ett aspartylproteas som är besläktat med HIV-1-proteaset. En proteashämmare som atazanavir kan därför i teorin verka även på FIV. Den höga poängen (0,9998) speglar sannolikt främst att sjukdomen liknar HIV i kunskapsgrafen.

Proteaset hos FIV skiljer sig dock från HIV-1-proteaset i substratspecificitet. Känsligheten för hämmare kan därför inte antas. Detta är en ren förutsägelse utan stöd av studier.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 56659 | Atazanavir STADA | Kapsel, hård | Indikationstext saknas (indragen) |
| 56658 | Atazanavir STADA | Kapsel, hård | Indikationstext saknas (indragen) |

Båda godkännandena har dragits in, och inget giltigt godkännande finns för närvarande.

---

### Säkerhetsaspekter

- **Samband med sjukdomar enligt kunskapsgrafen (inte hämtat från produktresumétext):** Kunskapsgrafen anger kontraindikation eller försiktighet vid bland annat leversvikt, leversjukdom, gallblåsesjukdom, hyperglykemi, diabetes mellitus, diabetesketoacidos, kronisk hepatit B och C, hemofili, hyperbilirubinemi (inklusive Gilberts syndrom), njursten, akut urinsyranefropati, atrioventrikulärt block och laktatacidos.
- **Läkemedelsinteraktioner:** Totalt 277 interaktioner har identifierats. Exempel på allvarliga (Major):
  - Famotidin
  - Ranitidin
  - Rabeprazol
  - Omeprazol
  - Loperamid
  - Triamcinolon
  - Budesonid

  Exempel på måttliga (Moderate):
  - Acarbose
  - Metformin
  - Pioglitazon
  - Hydrokortison
  - Betametason
  - Aprepitant
  - Aluminiumhydroxid
  - Kalciumkarbonat

Se produktresumén för fullständig säkerhetsinformation om varningar och kontraindikationer.

---

### Övriga förutsagda indikationer (kort översikt)

| Förutsagd indikation | Poäng | Evidensnivå | Kommentar |
|------|------|------|------|
| Simian immunbristvirusinfektion | 99,98 % | L4 | En djurstudie på makaker som fått kombinationsbehandling (PMID 20497048). Det är oklart om atazanavir ingick. Begränsat värde för användning hos människa. |
| Neuroutvecklingsstörning med ataxi, avsaknad av tal och minskad vit substans i hjärnbarken | 99,98 % | L5 | Ingen trolig mekanistisk koppling. Sannolikt ett artefaktresultat i kunskapsgrafen. |
| Familjär kombinerad hyperlipidemi (föråldrad term) | 99,82 % | L5 | Motsägelsefull, eftersom proteashämmare oftare ger dyslipidemi. |
| Medfödd HIV-infektion | 99,71 % | L3 | Sju observationsstudier främst om säkerhet och farmakokinetik vid exponering under graviditet. Det rör sig i princip om den ursprungliga HIV-indikationen i en särskild population. |
| AIDS-relaterat komplex | 99,71 % | L3 | Tre observationsstudier och prekliniska studier. Överlappar med den godkända HIV-indikationen. |

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för kattens AIDS bygger enbart på modellen (L5), utan kliniska prövningar eller litteratur. Dessutom saknar atazanavir giltigt godkännande i Sverige.
- Flera av de övriga förutsägelserna rör antingen den ursprungliga HIV-indikationen eller saknar mekanistisk grund.

**För att gå vidare krävs:**
- Data om atazanavirs verkningsmekanism, som saknas i underlaget.
- Produktresumé med varningar och kontraindikationer från Läkemedelsverket, så att säkerhetsgranskning kan göras.
- Laboratoriestudier (in vitro) av atazanavirs hämning av FIV-proteas.
- Ett tydligt beslut om vilken användning som avses, eftersom kattens AIDS är en veterinärmedicinsk sjukdom. Det avgör vilka regelverk och studier som gäller.
- Om medfödd HIV ska utredas vidare: atazanavirspecifika studier av säkerhet och effekt vid graviditet och hos nyfödda.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

