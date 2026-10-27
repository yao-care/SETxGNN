---
layout: default
title: Cyanocobalamin
parent: Endast modellprediktion (L5)
nav_order: 115
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Cyanocobalamin: predikterad ny indikation Biotinmetabol sjukdom (biotin metabolic disease) (evidensnivå L5). Ursprunglig indikation: Ingen godkänd indikationstext finns registrerad i godkännandedata.…"
monitor_inn: "cyanocobalamin"
predicted_indications: ["biotin metabolic disease"]
---

# Cyanocobalamin
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

## Cyanokobalamin: Från vitamin B12-brist till biotinmetabol sjukdom
{: .text-alpha }

---

### Sammanfattning

Cyanokobalamin är en syntetisk form av vitamin B12 och har använts vid vitaminbristtillstånd, framför allt B12-brist, perniciös anemi och andra bristanemier. TxGNN-modellen förutsäger att det kan vara effektivt mot **biotinmetabol sjukdom**, men förutsägelsen bygger enbart på modellen: **inga kliniska prövningar** och **1 publikation** (en allmän översikt om biotekniskt framställda vitaminer, som inte direkt stöder indikationen) har hittats.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen godkänd indikationstext finns registrerad i godkännandedata. Enligt kunskapsgrafen: vitaminbristtillstånd, B12-brist, perniciös anemi, folatbristanemi, järnbristanemi |
| Förutsagd ny indikation | Biotinmetabol sjukdom (biotin metabolic disease) |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast återkallade godkännanden |
| Antal godkännanden | 13 (samtliga återkallade, inga giltiga) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för rapporten. Baserat på allmänt känd information fungerar cyanokobalamin (vitamin B12) som kofaktor för två enzym: metioninsyntas och metylmalonyl-CoA-mutas. Dess effekt vid B12-brist och perniciös anemi är väletablerad.

Biotin är i sin tur kofaktor för karboxylaser, till exempel propionyl-CoA-karboxylas, som matar in i samma metylmalonyl-CoA-väg. De två vitaminerna delar alltså metaboliska vägar kring propionat och nedbrytning av grenade aminosyror. Det kan förklara varför grafmodellen kopplar ihop dem.

Det finns dock ingen direkt evidens för att cyanokobalamin korrigerar defekterna vid biotinmetabola sjukdomar som biotinidasbrist eller holokarboxylassyntetasbrist. Standardbehandlingen är biotintillskott, och B12 skulle inte ersätta den. Saknad mekanismdata försvagar dessutom bedömningen. Förutsägelsen bör därför ses som en hypotes, inte som en terapeutisk rekommendation.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Översikt | Journal of Chemical Technology and Biotechnology | Allmän översikt om biotekniska processer för tillverkning av vitaminer och relaterade biokemikalier. Behandlar inte behandling av biotinmetabol sjukdom med cyanokobalamin. |

---

### Marknadsinformation Sverige

Samtliga 13 godkännanden är återkallade. Ingen indikationstext finns registrerad. Nedan visas de fem första.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 53633 | Novavita | Filmdragerad tablett | Ej angiven |
| 64641 | Betolvan | Filmdragerad tablett | Ej angiven |
| 9992 | Betolvex | Filmdragerad tablett | Ej angiven |
| 14650 | Betolvidon | Tablett | Ej angiven |
| 67584 | Cyanocobalamin Farmacia | Filmdragerad tablett | Ej angiven |

Övriga godkännanden omfattar bland annat TrioBe, Bevitrio, Beviplex Comp samt injektions- och infusionspreparat (Soluvit, Cernevit, Viant).

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner:** 313 interaktioner är registrerade. De som visas i underlaget är i huvudsak av lägre betydelse:

- **Mindre (Minor):** syrahämmare som famotidin, ranitidin, cimetidin, nizatidin samt protonpumpshämmare (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), samt kaliumklorid. Dessa kan minska upptaget av B12 från kosten.
- **Okänd nivå:** metformin, glimepirid, rosiglitazon, acarbose, doxycyklin, mesalazin, morfin och sukralfat.

Varningar och kontraindikationer från produktresumé saknas i underlaget. Se produktresumén för säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga modellpoängen (99,6 %) bygger enbart på en grafbaserad förutsägelse. Det saknas kliniska prövningar och relevant litteratur, och standardbehandlingen (biotin) gör att B12 knappast tillför något.
- Alla svenska godkännanden är återkallade, och viktig säkerhets- och mekanismdata saknas.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket för närvarande blockerar säkerhetsgranskningen.
- Komplettera verkningsmekanismen från DrugBank.
- Genomföra en riktad litteraturgenomgång om samband mellan B12 och biotinmetabola sjukdomar (biotinidasbrist, holokarboxylassyntetasbrist).
- Bedöma administreringsvägens kompatibilitet och om det finns något kliniskt behov utöver biotinbehandling.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

