---
layout: default
title: Mannitol
parent: Endast modellprediktion (L5)
nav_order: 274
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
description: "Mannitol: predikterad ny indikation Nephrogenic syndrome of inappropriate antidiuresis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Mannitol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **9** st
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

## Mannitol: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

---

## Sammanfattning

Mannitol är ett osmotiskt verkande läkemedel som i de data som sammanställts för denna rapport är kopplat till bland annat hjärnödem, förhöjt intrakraniellt tryck, förhöjt ögontryck, hjärtsvikt och cystisk fibros. TxGNN-modellen förutsäger att det kan vara effektivt mot **nefrogent syndrom med olämplig antidiures** (poäng 0,9997), men det finns **inga kliniska prövningar** och endast **1 publikation**, en allmän översikt utan mannitolspecifika data. Förutsägelsen bygger därmed enbart på modellen, och flera mekanistiska överväganden talar snarare emot en nytta.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN-förutsägelsepoäng | 0.9997 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 4 av 4) |
| Antal godkännanden | 4 (giltiga: 4) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är mannitol ett osmotiskt diuretikum. Dess effekt vid hjärnödem och förhöjt intrakraniellt tryck bygger på att det drar vatten från vävnaden till blodbanan, och mekanistiskt skulle det kunna påverka vätskebalansen även vid nefrogent syndrom med olämplig antidiures.

Sambandet är dock svagt. Sjukdomen orsakas av en aktiverande förändring i vasopressin V2-receptorn, vilket ger för mycket vattenåterupptag i njurarna och låga natriumnivåer. Mannitol korrigerar inte denna grunddefekt. Osmotiska vattenförskjutningar skulle dessutom i teorin kunna förvärra hyponatremin. Den höga poängen bör därför tolkas som en ren modellförutsägelse och inte som ett belägg för effekt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Översikt | European Journal of Internal Medicine | Beskriver vanliga fallgropar vid utredning av hyponatremi. Innehåller inga mannitolspecifika data för detta tillstånd. |

---

## Marknadsinformation Sverige

Samtliga fyra godkännanden är återkallade, och ingen produkt med mannitol har för närvarande giltigt godkännande i de data som sammanställts. Indikationstext saknas för alla fyra.

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 22708 | Aridol | Inhalationspulver, hård kapsel | Godkänd |
| 18054 | Mannitol Baxter Viaflo | Infusionsvätska, lösning | Godkänd |
| 9205 | Mannitol Fresenius Kabi | Infusionsvätska, lösning | Godkänd |
| 57202 | Corhum | Lösning för kardioplegi/organförvaring | Godkänd |

---

## Säkerhetsaspekter

Produktresumé med varningar och kontraindikationer saknas i de data som sammanställts. Se produktresumén för säkerhetsinformation.

Följande information kommer från kunskapsgrafen och inte från produkttext:

- **Tillstånd kopplade till kontraindikation i kunskapsgrafen**: leversvikt, leversjukdom, leverkoma och hepatisk encefalopati, anuri, nedsatt njurfunktion, lungödem, intrakraniell blödning, porfyri, trombocytopeni, neutropeni, agranulocytos, anemi, sömnapné och substansberoende, bland andra. Detta ska bekräftas mot produktresumén.
- **Läkemedelsinteraktioner** (100 identifierade; ett urval):
  - **Allvarlig**: amikacin.
  - **Måttlig**: litium inte listad, men bland annat lamivudin, formoterol, salbutamol, arformoterol, amifostin, bensazepril, kaptopril, karbamazepin, cisatrakurium, citalopram, dapagliflozin, kanagliflozin, desvenlafaxin, bisakodyl, pikosulfat, polyetylenglykol med elektrolyter, jotalaminsyra och diatrizoat.
  - **Lindrig**: doxycyklin.

Vid den aktuella förutsagda indikationen är särskilt nedsatt njurfunktion, lungödem och risken för förvärrad hyponatremi relevanta.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar kliniska prövningar och mekanistiskt stöd. Den enda publikationen är en allmän översikt, och mannitols osmotiska effekt kan i stället förvärra hyponatremi.

**För att gå vidare krävs:**
- Hämta och analysera produktresumé för varningar och kontraindikationer.
- Komplettera data om verkningsmekanism (t.ex. från DrugBank).
- Genomföra en riktad litteraturgenomgång om mannitol vid nefrogent syndrom med olämplig antidiures, samt prekliniska data som kan stödja en mekanism.
- Bedöma om andra förutsagda indikationer, som akut pulmonell hjärtsjukdom (där litteraturen snarare pekar på risk för lungödem), har bättre underlag. Ingen av dem har i nuläget kliniska prövningar.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

