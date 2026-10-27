---
layout: default
title: Sorbitol
parent: Endast modellprediktion (L5)
nav_order: 398
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Sorbitol: predikterad ny indikation Exercise-induced malignant hyperthermia (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga godkännandedata"
monitor_inn: "SORBITOL"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
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

## Sorbitol: Från rektal användning (indikation ej angiven) till exercise-induced malignant hyperthermia
{: .text-alpha }

---

### Sammanfattning

Sorbitol är en sockeralkohol som används som osmotiskt verkande medel och laxermedel, och finns i rektallösningar som tidigare var godkända i Sverige. Någon ursprunglig indikation är inte angiven i godkännandedata. TxGNN-modellen förutsäger att sorbitol kan vara effektivt mot **exercise-induced malignant hyperthermia**, men förutsägelsen är endast beräkningsbaserad: det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder den.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga godkännandedata |
| Förutsägen ny indikation | Exercise-induced malignant hyperthermia |
| TxGNN-förutsägelsepoäng | 99,4 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 3 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är sorbitol en sockeralkohol med osmotisk effekt, som används som laxermedel och hjälpämne. Någon etablerad mekanistisk koppling till den nya indikationen har inte kunnat visas.

Malign hypertermi orsakas av störd kalciumfrisättning via ryanodinreceptorn (RYR1) i skelettmuskulaturen. Sorbitol har ingen känd effekt på denna process. Gällande standardbehandling, dantrolen, verkar som RyR1-antagonist och har en helt annan mekanism.

Ett samband skulle i så fall vara spekulativt, till exempel en hypotetisk osmotisk effekt eller vätskeförskjutning, och det har inte påvisats. Den höga poängen (0,994) ska därför tolkas som en beräkningsmässig signal och inte som tecken på klinisk nytta.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 10793 | Resulax | Rektallösning | Indragen |
| 65612 | Dokusatnatrium/Sorbitol Evolan | Rektallösning | Indragen |
| 6514 | Klyx | Rektallösning | Indragen |

Ingen godkänd indikationstext finns registrerad för dessa godkännanden.

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgraf** (inte hämtade från produkttext): aktiv magsårssjukdom.
- **Läkemedelsinteraktioner** (2 identifierade):
  - **Tolevamer**: allvarlig (Major) interaktion
  - **Lamivudin**: måttlig (Moderate) interaktion

Se produktresumén för fullständig säkerhetsinformation om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellpoäng utan stöd från kliniska prövningar eller litteratur, och det saknas en rimlig mekanistisk koppling. Dessutom är samtliga svenska godkännanden indragna.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata för sorbitol från DrugBank.
- Hämta varningar och kontraindikationer från produktresumén hos Läkemedelsverket.
- Göra en systematisk litteratursökning och en prekliniskt inriktad mekanistisk bedömning av en eventuell koppling till RYR1-relaterad kalciumreglering.
- Bedöma administrationsvägens kompatibilitet, eftersom tillgängliga produkter är rektallösningar och den nya indikationen sannolikt kräver en annan administrationsform.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

