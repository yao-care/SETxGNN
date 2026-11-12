---
layout: default
title: Zanamivir
parent: Endast modellprediktion (L5)
nav_order: 456
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
description: "Zanamivir: predikterad ny indikation Pyelonephritis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Zanamivir
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

## Zanamivir: Pyelonephritis
{: .text-alpha }

---

### Sammanfattning

Zanamivir är en neuraminidashämmare som ursprungligen användes för att behandla **influensa**. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Pyelonephritis |
| TxGNN-förutsägelsepoäng | 0.9984 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Baserat på allmänt känd information hämmar zanamivir neuraminidas (sialidas) hos influensavirus, vilket hindrar nya viruspartiklar från att frigöras från infekterade celler.

Pyelonefrit är oftast en bakteriell njurinfektion, vanligen orsakad av *E. coli*. Något etablerat mekanistiskt samband med influensa finns inte. Ett spekulativt resonemang är att hämning av bakteriella eller humana sialidaser skulle kunna påverka bakteriers vidhäftning eller avlägsnandet av sialinsyra från värdvävnad. Inga data har dock lämnats som stöder detta.

Den mycket höga modellpoängen ska därför tolkas med stor försiktighet. Den är en ren modellförutsägelse utan stöd från studier.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 14997 | Relenza (GlaxoSmithKline AB) | Inhalationspulver, avdelad dos | Indikationstext saknas |

<!-- review:begin se-row-20261112-zanamivir-1 -->

> **Granskningsrättelse (2026-11-12)**: Ursprungligen stod det: ”14997 / Relenza (GlaxoSmithKline AB) – indraget / Inhalationspulver, avdelad dos / Indikationstext saknas” Enligt Läkemedelsverkets registreringsstatus (2026-11-02) har 14997 status Godkänd; tabellen angav det som indraget. Endast statusuppgiften i tabellen har ändrats. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-row-20261112-zanamivir-1 -->

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (modellbaserade samband, inte hämtade från produktresumétext): epilepsi, kroniskt obstruktiv lungsjukdom (KOL), svår tidigt debuterande KOL, bronkialsjukdom och delirium.
- **Läkemedelsinteraktioner**: 8 interaktioner identifierades.
  - Insulin humant (inhalation, snabbverkande): **måttlig** nivå.
  - Övriga (klaritromycin, loratadin, montelukast, ketotifen, fexofenadin, ibuprofen, diklofenak): nivå **okänd**.

Se produktresumén för fullständig information om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen är endast modellbaserad (L5). Det saknas kliniska prövningar och relevant litteratur, och inget plausibelt mekanistiskt samband med pyelonefrit har identifierats.

<!-- review:begin se-lic-20261106-zanamivir-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Det saknas kliniska prövningar och relevant litteratur, och inget plausibelt mekanistiskt samband med pyelonefrit har identifierats. Dessutom är det enda svenska godkännandet indraget.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 1, varav giltiga: 1; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-zanamivir-1 -->

**För att gå vidare krävs:**
- Hämta produktresumé och säkerhetsinformation (varningar, kontraindikationer) från Läkemedelsverket.
- Komplettera data om verkningsmekanism.
- Prekliniska studier som undersöker om sialidashämning påverkar uropatogener eller värdvävnad vid pyelonefrit.
- Systematisk litteratursökning som riktar sig specifikt mot pyelonefrit.
- Bedöma administreringsväg (inhalation) i förhållande till en systemisk njurinfektion.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Dessutom är det enda svenska godkännandet indraget” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-12 | Tabell: 1 godkännande (14997) är godkänd, inte indragna | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

