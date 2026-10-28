---
layout: default
title: Isoflurane
parent: Endast modellprediktion (L5)
nav_order: 235
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Isoflurane: predikterad ny indikation Prinzmetal angina (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext registrerad i godkännandedata (isofluran är ett…"
monitor_inn: "isoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
---

# Isoflurane
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

## Isofluran: Från generell anestesi till Prinzmetal angina
{: .text-alpha }

---

## Sammanfattning

Isofluran är ett inhalationsanestetikum som används för generell anestesi. Indikationstexten saknas dock i de godkännandedata som sammanställts för rapporten. TxGNN-modellen (djupinlärning) förutsäger att isofluran kan vara effektivt mot **Prinzmetal angina** (poäng 0,9967), men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder förutsägelsen. Den vilar alltså enbart på en modellberäkning (evidensnivå L5).

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext registrerad i godkännandedata (isofluran är ett inhalationsanestetikum) |
| Förutsagd ny indikation | Prinzmetal angina |
| TxGNN-förutsägelsepoäng | 0,9967 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är isofluran ett flyktigt (inhalerbart) narkosmedel. Dess effekt vid generell anestesi är väletablerad, och mekanistiskt skulle det kunna vara tillämpbart på Prinzmetal angina via dess effekter på kärlens glatta muskulatur.

Prinzmetal angina orsakas av spasmer i hjärtats kranskärl. Flyktiga anestetika vidgar blodkärl, och det är den enda tänkbara kopplingen till sjukdomen. Det är dock en spekulation som de tillgängliga uppgifterna inte stöder.

Det finns också skäl som talar emot nytta. Isofluran har diskuterats i samband med så kallat *coronary steal*, där blodflödet kan omfördelas bort från områden med nedsatt blodtillförsel. Dessutom är en generell inhalationsnarkos svår att förena med behandling av en kronisk, återkommande kärlsjukdom. Förutsägelsen bör därför ses som en hypotes och inte som ett belagt behandlingsspår.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare | Status |
|---------|------|------|------|------|
| 61474 | Sedaconda | Inhalationsånga, vätska | Sedana Medical AB | Indraget |
| 12337 | Isofluran Baxter | Inhalationsånga, vätska | Baxter Medical AB | Indraget |

Inget av godkännandena är för närvarande giltigt, och ingen godkänd indikationstext finns registrerad.

---

## Säkerhetsaspekter

**Kontraindikationer enligt kunskapsgrafen** (härledda från TxGNN:s kunskapsgraf, inte från produktresumé):
- Leversjukdom
- Gallblåsesjukdom
- Hypotoni (lågt blodtryck)
- Malign hypertermi vid anestesi, inklusive ansträngningsutlöst malign hypertermi
- Duchennes muskeldystrofi, Beckers muskeldystrofi och muskeldystrofi i allmänhet

**Läkemedelsinteraktioner** (38 interaktioner identifierade, de viktigaste nedan):
- **Adrenalin (epinefrin)**: allvarlig (Major) interaktion
- **Morfin**: måttlig (Moderate) interaktion
- **Opium**: måttlig (Moderate) interaktion

Övriga identifierade interaktioner, till exempel med atropin, hydrokortison och omeprazol, har ännu inte graderats. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för Prinzmetal angina bygger enbart på en modellpoäng, utan stöd från studier eller publikationer, och coronary steal talar mot nytta.
- Isoflurans godkännanden i Sverige är dessutom alla indragna, och de säkerhetsuppgifter som finns tyder på försiktighet vid hjärt-kärlpåverkan (till exempel hypotoni).

**För att gå vidare krävs:**
- Preklinisk eller mekanistisk evidens för att isofluran lindrar kranskärlsspasm utan att orsaka coronary steal
- Fullständig verkningsmekanism och säkerhetsinformation från produktresumé
- En genomförbar administreringsväg och ett användningsscenario för en kronisk sjukdom

**Notering om andra förutsagda indikationer:** Bland de övriga förutsägelserna har **migränsjukdom** mest stöd (evidensnivå L4). Det består av prekliniska studier som visar att inhalationsanestetika hämmar kortikal spridande depression, samt två fallrapporter om behandling av status migrainosus med generell anestesi. Även där saknas kliniska prövningar. Ett möjligt nästa steg vore en preklinisk studie av dosberoende hämning av kortikal spridande depression, följd av en pilotstudie vid refraktär status migrainosus under övervakade former.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

