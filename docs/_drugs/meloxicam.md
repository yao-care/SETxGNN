---
layout: default
title: Meloxicam
parent: Endast modellprediktion (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Meloxicam: predikterad ny indikation Akromesomel dysplasi, Hunter-Thompson-typ (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext finns registrerad i de svenska godkännandena. E…"
monitor_inn: "meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
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

## Meloxikam: Från reumatoid artrit och artros till akromesomel dysplasi av Hunter-Thompson-typ
{: .text-alpha }

---

### Sammanfattning

Meloxikam är ett icke-steroidalt antiinflammatoriskt läkemedel (NSAID) som ursprungligen användes vid ledinflammation och ledsjukdomar, bland annat reumatoid artrit, artros och juvenil idiopatisk artrit. TxGNN-modellen förutsäger att det kan vara effektivt mot **akromesomel dysplasi av Hunter-Thompson-typ** med ett mycket högt modellpoäng, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder förutsägelsen. Förutsägelsen bedöms därför som en ren modellprediktion utan stöd i data.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext finns registrerad i de svenska godkännandena. Enligt kunskapsgrafen: reumatoid artrit, artros, juvenil idiopatisk artrit och spondyloartropati |
| Förutsagd ny indikation | Akromesomel dysplasi, Hunter-Thompson-typ |
| TxGNN-förutsägelsepoäng | 99,9 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 4 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Baserat på känd information är meloxikam ett NSAID som företrädesvis hämmar COX-2 och därmed minskar bildningen av prostaglandiner, som driver inflammation och smärta. Effekten vid ledinflammation är väl belagd.

Akromesomel dysplasi av Hunter-Thompson-typ är en ärftlig skelettsjukdom som orsakas av funktionsförlustmutationer i CDMP1/GDF5. Dessa mutationer påverkar BMP-signalering och broskutveckling. Någon tydlig mekanistisk koppling till meloxikam har inte identifierats: att hämma prostaglandinsyntesen kan inte förväntas korrigera en genetisk defekt i broskbildningen.

Det höga modellpoängen speglar sannolikt att sjukdomen ligger nära andra muskuloskeletala sjukdomar i kunskapsgrafen, snarare än ett verkligt terapeutiskt samband. Förutsägelsen bör därför tolkas med stor försiktighet.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

Alla fyra godkännanden är avregistrerade. Ingen indikationstext finns registrerad.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 48662 | Melox (Medochemie Ltd) | Injektionsvätska, lösning | Ej angiven |
| 23826 | Meloxicam Bluefish (Bluefish Pharmaceuticals AB) | Tablett | Ej angiven |
| 59104 | Meloxicam Ebb (Ebb Medical AB) | Tablett | Ej angiven |
| 23827 | Meloxicam Bluefish (Bluefish Pharmaceuticals AB) | Tablett | Ej angiven |

---

### Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer ingick inte i underlaget. Följande information kommer från kunskapsgrafen och ska inte likställas med märkningstext.

- **Kontraindikationer enligt kunskapsgrafen**: Sjukdomstillstånd där meloxikam anges som kontraindicerat är bland annat:
  - Hjärt- och kärlsjukdomar: högt blodtryck, hjärtsvikt, hjärtinfarkt, stroke, hjärtkärlsjukdom
  - Njursjukdom och nedsatt njurfunktion
  - Mag-tarmsjukdomar: aktivt magsår, gastrit
  - Blodsjukdomar: koagulationsrubbningar, anemi, hemoglobinopati
  - Metabola tillstånd: diabetes mellitus, diabetisk ketoacidos, hyperlipidemi
  - Missbruk eller beroende

- **Läkemedelsinteraktioner**: Totalt 273 interaktioner finns registrerade. Exempel på måttliga interaktioner:
  - Kortikosteroider: hydrokortison, dexametason, betametason, triamcinolon, budesonid
  - Acetylsalicylsyra
  - Antidiabetika: metformin, glimepirid, klorpropamid
  - Mesalazin och balsalazid
  - Aminoglykosider och vankomycin: kanamycin, vankomycin
  - Aprepitant

  Linaklotid har en lindrig interaktion.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar helt stöd i kliniska prövningar och litteratur (evidensnivå L5), och någon rimlig mekanistisk koppling mellan COX-hämning och en genetisk broskdefekt har inte identifierats. Dessutom är alla svenska godkännanden avregistrerade.

**För att gå vidare krävs:**
- Hämta verkningsmekanismen från DrugBank för att kunna analysera mekanistiska samband.
- Hämta produktresumé från Läkemedelsverket för att genomföra en säkerhetsgranskning.
- Utvärdera prekliniska data som kan visa en koppling mellan prostaglandinvägen och GDF5/BMP-signalering.
- Överväg att i stället prioritera de förutsagda indikationer som överlappar med meloxikams befintliga användning, till exempel polyartikulär juvenil idiopatisk artrit eller reumatoid nodulos. Dessa är dock främst förfiningar av befintliga indikationer och inte nya användningsområden.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

