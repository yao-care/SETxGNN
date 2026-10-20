---
layout: default
title: Methionine
parent: Endast modellprediktion (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methionine: predikterad ny indikation Akne (evidensnivå L5). Ursprunglig indikation: Ej angiven i godkännandedata (produkterna är infusionslösningar och e…"
monitor_inn: "methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
---

# Methionine
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

# Metionin: Från ej angiven ursprunglig indikation till akne

---

## Sammanfattning

Metionin är en essentiell aminosyra. I Sverige ingår den i infusionslösningar för näringstillförsel, men de godkännandedata som sammanställts för rapporten anger ingen ursprunglig indikationstext. TxGNN-modellen förutsäger att metionin kan vara effektivt mot **akne**, med mycket hög modellpoäng (99,9996 %). Evidensen är dock svag: **inga kliniska prövningar** och **2 publikationer** finns, och de ger bara indirekt stöd. Det ena är en fallrapport och det andra en kohortstudie.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i godkännandedata (produkterna är infusionslösningar och en peritonealdialysvätska) |
| Förutsagd ny indikation | Akne |
| TxGNN-förutsägelsepoäng | 99,9996 % |
| Evidensnivå | L4 (endast indirekt evidens; ingen studie har testat metionin mot akne) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 20 (alla avregistrerade, 0 giltiga) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Metionin är en svavelhaltig aminosyra som används som näringskomponent i parenterala aminosyralösningar. Mekanistiskt kan den vara tillämpbar på akne via ämnesomsättningen av en-kolföreningar och homocystein, men detta är inte styrkt.

Litteraturen ger bara ett indirekt samband. En studie visade förhöjda homocysteinnivåer i plasma hos patienter som behandlades med isotretinoin mot cystisk akne. Homocystein är en metabolit i metioninomsättningen. Den andra artikeln är en fallrapport om en MTHFR-mutation hos ett nyfött barn, bland annat med neonatal akne, och säger inget om metionin som behandling.

Riktningen på en eventuell effekt är oklar. Tillskott av metionin kan höja homocysteinnivåerna, och det kan vara skadligt snarare än till nytta. Förutsägelsen bör därför ses som en hypotes och inte som ett belagt behandlingsalternativ.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Kohortstudie | International Journal of Dermatology | Förhöjda plasmanivåer av homocystein hos patienter som behandlades med isotretinoin mot cystisk akne. Studien ger indirekt koppling till metioninomsättningen men testar inte metionin som behandling. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Fallrapport | BMJ Case Reports | Nyfödd pojke med ny MTHFR-mutation, encefalopati, hårförlust, marfanoida drag och neonatal akne. Visar ett samband med en-kolmetabolism men ingen behandlingseffekt. |

---

## Marknadsinformation Sverige

Alla 20 godkännanden är avregistrerade. Indikationstext finns inte angiven för något av dem. Nedan visas fem av godkännandena.

| Godkännandenummer | Produktnamn | Beredningsform |
|---------|------|------|
| 12526 | Glavamin | Infusionsvätska, lösning |
| 18399 | StructoKabiven Elektrolytfri | Infusionsvätska, emulsion |
| 10096 | Vamin 18 g N/l elektrolytfri | Infusionsvätska, lösning |
| 10095 | Vamin 14 g N/l elektrolytfri | Infusionsvätska, lösning |
| 12423 | Nutrineal PD4 1,1 % Aminosyror | Peritonealdialysvätska |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgraf (inte produkttext):** Modellens kunskapsgraf kopplar metionin till bland annat följande sjukdomar:
  - njursjukdom, kronisk njursvikt och njursvikt i slutstadiet
  - högt blodtryck, hjärtsjukdom och hjärt-kärlsjukdom
  - diabetes och diabetesketoacidos
  - fenylketonuri och rubbningar i fenylalaninmetabolismen
  - hyperkalcemi, sarkoidos och nefrokalcinos
  - hyperlipidemi och njursten
  - digitalisförgiftning och kammarflimmer

  Dessa uppgifter kommer från en kunskapsgraf och inte från godkänd produktinformation. De bör bekräftas mot produktresumén.

- **Läkemedelsinteraktioner** (5 identifierade):

| Interagerande läkemedel | Nivå |
|------|------|
| Aktivt kol | Måttlig |
| Efedrin | Lindrig |
| Pseudoefedrin | Lindrig |
| Meximletin | Lindrig |
| Flekainid | Lindrig |

- **Homocystein:** Metionin är en föregångare till homocystein. Förhöjda homocysteinnivåer är förknippade med kärlsjukdom, och det talar för försiktighet vid tillskott.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen har mycket hög modellpoäng, men det finns inga kliniska prövningar och den litteratur som hittats är bara indirekt. Dessutom kan metionin höja homocystein, så effektens riktning är oklar och kan vara negativ.
- Samtliga svenska godkännanden är avregistrerade och saknar angiven indikationstext.

**För att gå vidare krävs:**
- Data om verkningsmekanismen, till exempel från DrugBank, för att kunna bedöma sambandet med akne.
- Säkerhetsinformation från produktresuméer hos Läkemedelsverket (MPA), eftersom varningar och kontraindikationer saknas i de sammanställda data.
- Prekliniska eller kliniska studier som direkt testar metionin vid akne, inklusive effekten på homocystein.
- Klargörande av administrationsväg och beredningsform, eftersom befintliga produkter är infusionslösningar och inte lämpar sig för aknebehandling.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

