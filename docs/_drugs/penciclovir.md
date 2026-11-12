---
layout: default
title: Penciclovir
parent: Endast modellprediktion (L5)
nav_order: 342
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "penciclovir"
predicted_indications: ["fascioliasis"]
description: "Penciclovir: predikterad ny indikation Fascioliasis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Penciclovir
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

## Penciclovir: Fascioliasis
{: .text-alpha }

---

### Sammanfattning

Penciclovir är ett antiviralt läkemedel som ursprungligen används mot herpes labialis (munherpes). TxGNN-modellen förutsäger att det kan vara effektivt mot **fascioliasis** (leverikterinfektion), men förutsägelsen bygger enbart på modellens beräkning: det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder den, och någon biologisk förklaring har inte kunnat identifieras.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Fascioliasis |
| TxGNN-förutsägelsepoäng | 0.9906 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Utifrån allmänt känd information är penciclovir en guanosinanalog. Den aktiveras av ett virusspecifikt enzym, tymidinkinas, och omvandlas till penciclovirtrifosfat som hämmar virusets DNA-polymeras. Därför verkar läkemedlet selektivt i virusinfekterade celler.

Fascioliasis orsakas av leverikterna *Fasciola hepatica* och *F. gigantica*, alltså parasiter och inte virus. De saknar ett motsvarande viralt tymidinkinas och DNA-polymeras som penciclovir kan verka på. Något rimligt mekanistiskt samband mellan läkemedlet och sjukdomen har därför inte kunnat identifieras.

Den höga poängen (0,9906) kommer från TxGNN-modellen (djupinlärning) och kan spegla likheter som modellen har lärt sig mellan relaterade sjukdomar, inte biologiska belägg. Den bör därför tolkas med stor försiktighet.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 48482 | Vectatone (Perrigo Sverige AB) | Kräm | Indikationstext saknas (indraget) |
| 12824 | Vectavir (Perrigo Sverige AB) | Kräm | Indikationstext saknas (indraget) |

---

### Säkerhetsaspekter

Se produktresumén för säkerhetsinformation. Inga varningar, kontraindikationer eller läkemedelsinteraktioner har kunnat hämtas för detta läkemedel i de data som sammanställts. Eftersom de godkända produkterna är indragna finns ingen aktuell svensk produktresumé att utgå från.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds endast av modellen (L5), utan kliniska prövningar eller litteratur, och verkningsmekanismen (virusspecifikt enzym) saknar angivbar koppling till en parasitsjukdom. Krämformen är sannolikt olämplig för en systemisk leverinfektion.

<!-- review:begin se-lic-20261106-penciclovir-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Dessutom är båda svenska godkännandena indragna, och krämformen är sannolikt olämplig för en systemisk leverinfektion.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 2, varav giltiga: 2; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-penciclovir-1 -->

**För att gå vidare krävs:**
- Ett biologiskt resonemang för hur penciclovir skulle kunna påverka *Fasciola*, till exempel genom prekliniska studier (in vitro-test mot parasiten).
- Kompletterande data om verkningsmekanism, varningar och kontraindikationer från DrugBank och Läkemedelsverkets produktresumé.
- Utvärdering av om en lämplig beredningsform och administreringsväg finns för en leverinfektion.
- Jämförelse med etablerad behandling av fascioliasis (till exempel triklabendazol) för att bedöma om ett kliniskt behov finns.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Dessutom är båda svenska godkännandena indragna, och k” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

