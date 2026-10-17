---
layout: default
title: Deferiprone
parent: Endast modellprediktion (L5)
nav_order: 130
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Deferiprone: predikterad ny indikation Hepatisk porfyri (evidensnivå L5). Ursprunglig indikation: Ingen godkänd indikationstext finns i de svenska godkännandena. Enlig…"
monitor_inn: "deferiprone"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "hepatoportal sclerosis", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "pyruvate kinase deficiency of red cells", "pyropoikilocytosis, hereditary"]
---

# Deferiprone
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **9** st
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

# Deferipron: Från hemosideros och beta-talassemi till hepatisk porfyri

---

### Sammanfattning

Deferipron är en oral järnkelator som ursprungligen används vid järnöverskott (hemosideros) och beta-talassemi. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **hepatisk porfyri**, men stödet är begränsat: inga kliniska prövningar finns registrerade och **2 prekliniska publikationer** (djurmodeller) pekar i denna riktning.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen godkänd indikationstext finns i de svenska godkännandena. Enligt kunskapsgrafen: hemosideros, beta-talassemi och relaterade hemoglobinopatier |
| Förutsagd ny indikation | Hepatisk porfyri |
| TxGNN-förutsägelsepoäng | 99,2 % |
| Evidensnivå | L4 (endast prekliniska studier) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 5 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

Detaljerad data om verkningsmekanismen finns för närvarande inte tillgänglig i det sammanställda underlaget. Baserat på känd information är deferipron en oral järnkelator som binder fritt (labilt) järn. Dess effekt vid transfusionsrelaterat järnöverskott vid talassemi är väl etablerad.

Vid porfyri, särskilt porphyria cutanea tarda, förvärrar ökat leverjärn och järnberoende oxidativ stress ansamlingen av uroporfyrin. Standardbehandlingen aflåtning (flebotomi) verkar sannolikt genom att minska leverjärnet. En järnkelator kan därför i teorin ge liknande effekt utan blodtappning.

Två prekliniska studier stöder resonemanget. En studie från 2020 visade att järnkelering förbättrade hemolytisk anemi och ljuskänslighet i en modell av kongenital erytropoetisk porfyri. En studie från 2007 på möss (modell för porphyria cutanea tarda) jämförde deferipron med järnfattig kost. Resultaten kommer dock från djurmodeller, och det saknas data från människa.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preklinisk (djurmodell) | Blood | Järnkelering förbättrade hemolytisk anemi och hudens ljuskänslighet i en modell av kongenital erytropoetisk porfyri |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Preklinisk (musmodell) | Hepatology | Jämförde deferipron med järnfattig kost för att minska leverjärn och uroporfyrinansamling hos Hfe-/--möss (modell för porphyria cutanea tarda) |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 55997 | Deferiprone DOC | Filmdragerad tablett | Ej angiven (indraget) |
| 50975 | Deferipron Evolan | Filmdragerad tablett | Ej angiven (indraget) |
| 64937 | Deferipron Ebb | Filmdragerad tablett | Ej angiven (indraget) |
| 55996 | Deferiprone DOC | Filmdragerad tablett | Ej angiven (indraget) |
| 50974 | Deferipron Evolan | Filmdragerad tablett | Ej angiven (indraget) |

Samtliga fem godkännanden är indragna, och inget läkemedel med deferipron har för närvarande giltigt godkännande i Sverige.

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Totalt 246 interaktioner är registrerade. De som visas i underlaget är av måttlig allvarlighetsgrad och gäller främst preparat som kan binda deferipron eller järn i tarmen och minska upptaget:
  - Kalciumsalter (fosfat, acetat, karbonat, citrat, glukonat, laktat m.fl.)
  - Magnesiumsalter (oxid, karbonat, klorid, citrat, glukonat, hydroxid, sulfat)
  - Aluminiumhydroxid, magaldrat, attapulgit och kaolin
  - Sukralfat
  - Järn

Övrig säkerhetsinformation (varningar och kontraindikationer) saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation. I bedömningen av förutsagda indikationer har agranulocytos lyfts som en känd allvarlig risk som kräver noggrann blodövervakning.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensen för hepatisk porfyri är begränsad till två prekliniska djurstudier utan kliniska prövningar, och läkemedlet saknar för närvarande giltigt godkännande i Sverige. Dessutom saknas varnings- och kontraindikationsdata, vilket hindrar en fullständig säkerhetsbedömning.

**För att gå vidare krävs:**
- Hämta och granska produktresumén (varningar och kontraindikationer) från Läkemedelsverket
- Hämta data om verkningsmekanismen från DrugBank
- Utvärdera säkerhetsprofilen, särskilt risken för agranulocytos och behovet av blodövervakning
- Genomföra eller identifiera kliniska studier (t.ex. fall- eller pilotstudier) på människor med porphyria cutanea tarda eller andra porfyrier
- Klargöra läkemedlets regulatoriska status, eftersom alla godkännanden är indragna
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

