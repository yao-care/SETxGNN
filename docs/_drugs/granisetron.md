---
layout: default
title: Granisetron
parent: Endast modellprediktion (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Granisetron: predikterad ny indikation Manisk bipolär sjukdom (engelska: manic bipolar affective disorder) (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga godkännandedata"
monitor_inn: "granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetron: Från illamående och kräkningar vid cytostatikabehandling till manisk bipolär sjukdom
{: .text-alpha }

---

## Sammanfattning

Granisetron är en 5-HT3-receptorantagonist. De registrerade svenska godkännandena saknar indikationstext i de data som sammanställts för denna rapport. Läkemedlet är vanligen använt mot illamående och kräkningar, men det kan inte bekräftas av dessa data.
TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **manisk bipolär sjukdom**, men det finns **0 kliniska prövningar** och **0 publikationer** som stöder denna riktning. Förutsägelsen bygger enbart på en modellberäkning.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga godkännandedata |
| Förutsagd ny indikation | Manisk bipolär sjukdom (engelska: manic bipolar affective disorder) |
| TxGNN-förutsägelsepoäng | 0,9962 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 6 av 6) |
| Antal godkännanden | 6 (giltiga: 6) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Granisetron är dock känt som en selektiv 5-HT3-receptorantagonist, och blockad av dessa receptorer kan i teorin påverka dopamin- och serotoninsignalering som är viktig för stämning och psykos.

Sambandet med den ursprungliga indikationen är ännu inte utrett. Den ursprungliga indikationen saknas i godkännandedata, och likheten mellan indikationerna är därför inte bedömd.

Den höga poängen (0,9962) är en beräkning från modellen och inte ett kliniskt resultat. Mekanismen är en hypotes och bör inte tolkas som belagd effekt.

**Övriga förutsägelser från modellen** (alla på evidensnivå L5, utan kliniska prövningar eller litteratur):

| Rang | Sjukdom | Poäng | Mekanistisk rimlighet |
|------|------|------|------|
| 9 | Kallurtikaria | 0,9910 | Svagt, indirekt stöd via mastcellsmodulering |
| 10 | Konjunktivit | 0,9910 | Ingen direkt mekanism; troligen nätverksassociation |

---

## Marknadsinformation Sverige

Samtliga sex godkännanden är avregistrerade. Ingen indikationstext finns tillgänglig.

| Godkännandenummer | Produktnamn | Beredningsform | Tillverkare |
|---------|------|------|-----------|
| 23574 | Granisetron STADA | Filmdragerad tablett | STADA Arzneimittel AG |
| 66545 | Granisym | Filmdragerad tablett | STADA Arzneimittel AG |
| 23575 | Granisetron STADA | Filmdragerad tablett | STADA Arzneimittel AG |
| 66544 | Granisym | Filmdragerad tablett | STADA Arzneimittel AG |
| 26690 | Granisetron Fresenius Kabi | Injektionsvätska, lösning | Fresenius Kabi AB |

Ytterligare ett godkännande (25505, Granisetron Hameln, koncentrat till injektions-/infusionsvätska, lösning) finns också och är avregistrerat.

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgraf (inte produkttext)**: Kunskapsgrafen kopplar granisetron till följande tillstånd: långt QT-syndrom, familjärt långt QT-syndrom, kaliumbrist, plötsligt hjärtstopp och retledningsrubbning i hjärtat. Dessa är grafbaserade kopplingar och ersätter inte produktresumén.
- **Läkemedelsinteraktioner**: Totalt 461 interaktioner har identifierats. Exempel på interaktioner av allvarlig grad (Major):
  - Fentanyl, alfentanil och tramadol
  - Dextrometorfan
  - Almotriptan och sumatriptan
  - Amiodaron, amisulprid och amitriptylin
  - Anagrelid

  Måttliga interaktioner (Moderate) finns bland annat med abirateron, famotidin, formoterol, adenosin, salbutamol, alfuzosin, propofol samt kodein och dihydrokodein.

  Många av de allvarliga interaktionerna rör läkemedel som påverkar QT-intervallet eller serotoninsystemet. Detta är i linje med kunskapsgrafens varningar för hjärtrytmrubbningar.

Se i övrigt produktresumén för fullständig säkerhetsinformation, eftersom varningar och kontraindikationer från godkännandetexten saknas.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för manisk bipolär sjukdom bygger enbart på en modellberäkning (evidensnivå L5), utan kliniska prövningar eller publikationer. Läkemedlet är marknadsfört i Sverige med 6 giltiga godkännanden av 6, men viktiga data om varningar och kontraindikationer saknas.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för att komplettera varningar, kontraindikationer och godkänd indikation.
- Hämta verkningsmekanismdata från DrugBank.
- Göra en systematisk litteratur- och prövningssökning för granisetron vid bipolär sjukdom och manisk sjukdom, inklusive studier av andra 5-HT3-antagonister.
- Bedöma hjärtsäkerhet (QT-förlängning) och interaktionsrisker med vanliga läkemedel vid bipolär sjukdom, särskilt antipsykotika och antidepressiva.
- Utreda vilken beredningsform och administreringsväg som skulle behövas för den nya indikationen, samt om någon produkt kan återinföras på marknaden.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

