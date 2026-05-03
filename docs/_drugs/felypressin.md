---
layout: default
title: Felypressin
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

Jag använder `txgnn-pipeline`-skillet för att säkerställa korrekt hantering av TxGNN-rapportgenerering, och producerar nu rapporten baserat på Evidence Pack.

---

# Felypressin: Från vasokonstriktor i lokalbedövning till läkemedelsinducerad osteoporos

## Sammanfattning

Felypressin (DB00093) är ett syntetiskt vasopressin-analogt peptid med selektiv affinitet för vasopressin V1-receptorn (V1R), kliniskt använt som vasokonstriktor i dentala lokalbedövningsmedel. TxGNN-modellen förutsäger att det kan vara effektivt mot **läkemedelsinducerad osteoporos**, men det stöds för närvarande av **0 kliniska prövningar** och **0 publikationer** specifika för denna kombination. Hela evidensunderlaget bygger uteslutande på modellförutsägelse utan experimentell bekräftelse.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige |
| Förutsagd ny indikation | Läkemedelsinducerad osteoporos (drug-induced osteoporosis) |
| TxGNN-förutsägelsepoäng | 99,80% |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Ej på marknaden |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Felypressin är ett syntetiskt nonapeptid strukturellt besläktat med vasopressin (ADH), med selektiv bindning till vasopressin V1-receptorn (V1R). Dess etablerade kliniska roll är som vasokonstriktor i kombinerade tandläkarbedövningsmedel – den används för att minska blödning och förlänga anestesins verkningstid lokalt. Till skillnad från epinefrin har felypressin i princip inga direkta hjärt-kärlbiverkningar vid rekommenderade doser.

Den mekanistiska kopplingen till läkemedelsinducerad osteoporos är svag och indirekt. Det finns spridda rapporter i litteraturen om att vasopressin V1R-signalering kan ha inflytande på benmetabolismen via modulering av RANKL/OPG-axeln, som styr balansen mellan osteoklast- och osteoblastaktivitet. Felypressins höga V1R-selektivitet gör en sådan effektväg teoretiskt möjlig.

Det saknas dock helt direkta studier som kopplar felypressin till benmetabolism eller osteoporospatofysiologi. Den mekanistiska relationen bedöms som svag, förutsägelsen är datadriven och baseras på grafnätverksstruktur i TxGNN-modellen snarare än på kausal biologisk evidens. Utan stödjande prekliniska eller kliniska data kan en behandlingsrelevans inte fastställas.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Felypressin har inga registrerade läkemedelsgodkännanden i Sverige. Produkten är ej på marknaden.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån är L5 – förutsägelsen bygger enbart på TxGNN-modellens grafnätverksanalys utan stöd från kliniska prövningar, publikationer eller prekliniska studier som direkt involverar felypressin och läkemedelsinducerad osteoporos. Det mekanistiska sambandet via V1R/RANKL är spekulativt och saknar experimentell förankring.

**För att gå vidare krävs:**
- Inhämtning av fullständig MOA-data från DrugBank API (nuvarande datakvalitet: Data Gap)
- Granskning av produktresumén för säkerhetsprofil, varningar och kontraindikationer
- Identifiering av prekliniska studier som undersöker V1R-aktivering och effekter på benmetabolism och osteoklastaktivitet
- Utvärdering av om systemisk exponering för felypressin (utöver lokal/dental användning) är farmakologiskt och säkerhetsmässigt möjlig
- Regulatorisk bedömning för eventuell klinisk prövningsansökan i Sverige
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

