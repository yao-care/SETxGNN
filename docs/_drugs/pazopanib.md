---
layout: default
title: Pazopanib
parent: Endast modellprediktion (L5)
nav_order: 340
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "pazopanib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
description: "Pazopanib: predikterad ny indikation Liposarcoma (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Pazopanib
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

## Pazopanib: Liposarcoma
{: .text-alpha }

---

## Sammanfattning

Pazopanib är en tyrosinkinashämmare som ursprungligen används mot avancerad njurcellscancer och mjukdelssarkom. TxGNN-modellen (djupinlärning) förutsäger att läkemedlet kan vara effektivt mot **liposarkom**, med en mycket hög förutsägelsepoäng (0,9959). Poängen kommer från TxGNN-modellen och kan spegla likheter som modellen lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Den här förutsägelsen stöds dock av **0 kliniska prövningar** och **0 publikationer** i de data som sammanställts för rapporten, så den vilar enbart på modellen.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsägd ny indikation | Liposarcoma |
| TxGNN-förutsägelsepoäng | 0.9959 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 10 av 10) |
| Antal godkännanden | 10 (giltiga: 10) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på känd information är pazopanib en hämmare av tyrosinkinaserna VEGFR, PDGFR och c-KIT. Effekten vid njurcellscancer och mjukdelssarkom är väl dokumenterad, och mekanistiskt kan den vara tillämpbar på den förutsagda indikationen.

Njurcellscancer med Xp11.2/TFE3-fusion är en egen molekylär undertyp av njurcellscancer. Hämning av nybildning av blodkärn (angiogenes) används vid njurcellscancer i stort, och sådana läkemedel används även vid denna undertyp. Sambandet till pazopanibs ursprungliga indikation är alltså närliggande.

Samtidigt finns ingen prövning eller publikation för just denna undertyp. Kopplingen bygger enbart på TxGNN-förutsägelsen och på att njurcellscancer som grupp är en rimlig målgrupp. Den höga poängen bör därför inte läsas som självständig evidens.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Alla 10 godkännanden är giltiga. Nedan visas fem av dem.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 61540 | Pazopanib STADA | Filmdragerad tablett | Ingen indikationstext registrerad |
| 65260 | Pazopanib Glenmark | Filmdragerad tablett | Ingen indikationstext registrerad |
| 66227 | Pazopanib Newbury | Filmdragerad tablett | Ingen indikationstext registrerad |
| 65259 | Pazopanib Glenmark | Filmdragerad tablett | Ingen indikationstext registrerad |
| 61539 | Pazopanib STADA | Filmdragerad tablett | Ingen indikationstext registrerad |

---

## Cytotoxicitet

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Målriktad terapi (tyrosinkinashämmare) |
| Myelosuppressionsrisk | Se produktresumén för varningar och försiktighetsåtgärder |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Hanteringsskydd | Se produktresumén för varningar och försiktighetsåtgärder |

---

## Säkerhetsaspekter

Varningar och kontraindikationer från produktresumén saknas i de sammanställda uppgifterna.

**Kontraindikationer från kunskapsgrafen** (kommer från TxGNN:s kunskapsgraf och är inte etikettext): Följande tillstånd kopplas till läkemedlet.
- Hjärt- och kärlsjukdom: högt blodtryck, långt QT-syndrom (även ärftligt), torsades de pointes, hjärtinfarkt och kranskärlstrombos
- Lever: leversvikt, läkemedelsorsakad leverskada, hyperbilirubinemi (inklusive ärftlig form och Gilberts syndrom)
- Mage-tarm: diarrésjukdom, aktivt magsår, pankreatit
- Hjärna: intracerebral blödning
- Ämnesomsättning och elektrolyter: hypotyreos (inklusive myxödem och medfödd form), kaliumbrist, hyperkalcemi, nefrokalcinos, störd fosforomsättning
- Blod och njurar: hemoglobinopati, proteinuri

**Läkemedelsinteraktioner:** Totalt 519 interaktioner är identifierade. Bland de viktigaste:
- **Allvarliga (Major):** syrahämmande läkemedel som famotidin, ranitidin, cimetidin, omeprazol, esomeprazol, rabeprazol och dexlansoprazol, samt klaritromycin och dolasetron
- **Måttliga (Moderate):** bland annat pioglitazon, loperamid, aprepitant, dexametason, budesonid, bisakodyl, magnesiumoxid, polyetylenglykol, saxagliptin och eliglustat

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för njurcellscancer med Xp11.2/TFE3-fusion har högsta möjliga modellpoäng men ingen studie eller publikation bakom sig (evidensnivå L5).
- Samtidigt är läkemedlet marknadsfört i Sverige med 10 giltiga godkännanden av 10, och säkerhetsdata från produktresumén saknas, vilket är ett blockerande dataglapp.

**För att gå vidare krävs:**
- Hämta och läs produktresumén (varningar och kontraindikationer) från Läkemedelsverket.
- Hämta verkningsmekanismdata från DrugBank.
- Göra en systematisk litteratur- och prövningssökning specifikt för njurcellscancer med Xp11.2/TFE3-fusion, för att se om det finns evidens utanför de sammanställda data.
- Bekräfta att de 10 giltiga svenska godkännandena innebär att läkemedlet är tillgängligt.

**Observation om andra förutsagda indikationer:** Flera andra förutsägelser från samma modell har betydligt mer stöd och kan vara värda att prioritera framför den ovan.
- **Liposarkom** (evidensnivå L2): flera avslutade fas 2-prövningar, bland annat NCT01506596 och NCT01692496. Rekommendationen är att gå vidare med skyddsåtgärder.
- **Dermatofibrosarcoma protuberans** (L2): en fas 2-studie publicerad (PMID 32956651). Den tidiga fas 2a-prövningen NCT01059656 avbröts i förtid.
- **Fibroblastiska tumörer** (L2): bland annat fas 2-prövningen NCT02066285 vid solitär fibrös tumör.
- **Oklassificerad njurcellscancer** (L3): retrospektiva serier och en enarmad fas 2-studie.

För dessa gäller samma krav på komplettering av säkerhetsdata.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

