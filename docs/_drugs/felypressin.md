---
layout: default
title: Felypressin
parent: Endast modellprediktion (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Felypressin: predikterad ny indikation Läkemedelsinducerad osteoporos (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga data"
monitor_inn: "FELYPRESSIN"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "esotropia", "diabetic retinopathy", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "chondroid hamartoma", "non-seminomatous lesion", "tumor of testis and paratestis", "pre-malignant neoplasm"]
---

# Felypressin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

# Felypressin: Från okänd ursprunglig indikation till läkemedelsinducerad osteoporos

---

### Sammanfattning

Felypressin är en syntetisk analog till vasopressin och ingår i en tandvårdsberedning (Citanest Dental Octapressin), men den ursprungliga godkända indikationen framgår inte av de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **läkemedelsinducerad osteoporos**, med ett mycket högt modellpoäng (99,8 %). Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder förutsägelsen, så evidensen är begränsad till själva modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga data |
| Förutsagd ny indikation | Läkemedelsinducerad osteoporos |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 1 (indraget) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Baserat på känd information är felypressin en syntetisk vasopressinanalog som främst verkar som agonist på V1a-receptorn, vilket ger kärlsammandragning. Det används därför typiskt som tillsats i lokalbedövningsmedel för att förlänga effekten.

Ett samband med läkemedelsinducerad osteoporos är hypotetiskt. Vasopressinreceptorer finns i benceller, så en teoretisk koppling kan finnas. Den är dock spekulativ och saknar stöd i kliniska data eller litteratur.

Det höga poängvärdet speglar sannolikt närhet i kunskapsgrafen och inte faktisk biologisk eller klinisk evidens. Förutsägelsen bör därför tolkas med stor försiktighet.

**Övriga förutsägelser i toppen av listan** (alla L5, utan prövningar eller litteratur):

| Rang | Förutsagd indikation | Poäng | Bedömning |
|------|------|------|------|
| 2 | Svår icke-proliferativ diabetesretinopati | 99,6 % | Vasokonstriktion kan snarare försämra näthinnans genomblödning |
| 3 | Esotropi | 99,4 % | Trolig artefakt i kunskapsgrafen |
| 4 | Diabetesretinopati | 99,4 % | Samma resonemang som ovan, risk för skada |
| 5 | Bronkiala adenom/karcinoider hos barn | 99,2 % | Ingen etablerad mekanism |
| 6 | Duktal eller duktulär proliferation | 99,2 % | Ingen identifierbar mekanism |
| 7 | Kondroitt hamartom | 99,2 % | Ingen mekanistisk grund |
| 8 | Icke-seminomatös lesion | 99,2 % | Ingen evidens |
| 9 | Tumör i testikel och paratestikel | 99,2 % | Ingen evidens för antitumöreffekt |
| 10 | Premalign neoplasi | 99,2 % | Ospecifik kategori |

Flera av dessa har identiska poäng, vilket tyder på en generell grafeffekt snarare än läkemedelsspecifik biologi.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10433 | Citanest Dental Octapressin | Injektionsvätska, lösning | Ingen indikationstext tillgänglig (status: indraget) |

Tillverkare: Dentsply DeTrey GmbH. Det finns inga giltiga godkännanden för felypressin i Sverige för närvarande.

---

### Säkerhetsaspekter

Inga säkerhetsdata för varningar, kontraindikationer eller läkemedelsinteraktioner är tillgängliga i de data som sammanställts. Sökningen efter interaktioner gav inga träffar.

Se produktresumén för säkerhetsinformation.

Observera att som vasokonstriktor (V1a-agonist) kan felypressin teoretiskt försämra blodflödet i vävnader. Detta är särskilt relevant för de förutsagda ögonindikationerna (diabetesretinopati).

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellpoäng (L5) utan stöd av kliniska prövningar, litteratur eller en etablerad mekanism. Dessutom saknas giltigt godkännande i Sverige och grundläggande säkerhetsdata.

**För att gå vidare krävs:**
- Hämta och granska produktresumé från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket för närvarande blockerar säkerhetsbedömningen.
- Komplettera verkningsmekanismdata från DrugBank.
- Genomföra en litteratur- och prövningssökning för vasopressinreceptorer och bämetabolism (benmetabolism) samt läkemedelsinducerad osteoporos.
- Utreda prekliniskt om V1a-agonism har en biologiskt rimlig effekt på benvävnad.
- Klargöra administreringsväg, eftersom nuvarande beredning är en lokal injektionsvätska för tandvård.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

