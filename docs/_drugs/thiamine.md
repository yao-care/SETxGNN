---
layout: default
title: Thiamine
parent: Endast modellprediktion (L5)
nav_order: 422
evidence_level: L5
indication_count: 3
monitor_inn: "thiamine"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "primary hereditary glaucoma", "open-angle glaucoma"]
last_modified_at: 2026-11-24
description: "Thiamine: predikterad ny indikation Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidensnivå L5). I Sverige, godkännanden (Läkemedelsverket): 13 (giltiga: 13)"
---

# Thiamine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

## Thiamine: Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

---

## Sammanfattning

Tiamin (vitamin B1) är marknadsfört i Sverige som injektions- och infusionsvätska. De sammanställda uppgifterna innehåller ingen godkänd indikationstext för preparaten. TxGNN-modellen förutsäger att tiamin kan vara effektivt mot **resistens mot tyroideahormon orsakad av mutation i tyroideahormonreceptor beta**, med en mycket hög modellpoäng. Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder förutsägelsen, så den är endast en datorbaserad modellutsaga.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN-förutsägelsepoäng | 0.9943 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 13 av 13) |
| Antal godkännanden | 13 (giltiga: 13) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Tiamin är allmänt känt som en kofaktor i kolhydrat- och energimetabolismen, bland annat för pyruvatdehydrogenas, transketolas och alfa-ketoglutaratdehydrogenas.

Något tydligt mekanistiskt samband med den förutsagda sjukdomen har inte kunnat fastställas. Resistens mot tyroideahormon är en monogen receptorsjukdom, där en mutation i tyroideahormonreceptor beta försämrar kroppens svar på hormonet. Tiamin har ingen känd direkt påverkan på denna signalväg, och en vitaminkofaktor förväntas knappast korrigera ett receptordefekt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Godkännandena gäller främst enkomponentsprodukter men även kombinationsprodukter med andra vitaminer (Zubatmin, Viant); inga är avregistrerade eller ej marknadsförda. Nedan visas fem av dem.

<!-- review:begin se-lic-20261124-thiamine-1 -->

> **Granskningsrättelse (2026-11-24)**: Ursprungligen stod det: ”Totalt 13 giltiga godkännanden för enkomponentsprodukter, inga avregistrerade eller ej marknadsförda.” Enligt Läkemedelsverkets uppgifter är Zubatmin och Viant kombinationsprodukter där tiaminhydroklorid ingår tillsammans med andra vitaminer; texten angav alla godkännanden som enkomponentsprodukter. Uppgiften om enkomponents- och kombinationsprodukter följer de verksamma ämnena i Läkemedelsverkets uppgifter; antal godkännanden och status finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel (verksamma ämnen, registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-lic-20261124-thiamine-1 -->

<!-- licenses:begin -->

| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
|------|------|------|------|------|
| 57646 | Thiamine Sterop | Injektionsvätska, lösning | Laboratoires Sterop NV | Godkänd |
| 65471 | Bevione | Injektionsvätska, lösning | Orifarm Healthcare A/S | Godkänd |
| 64052 | Thiatum | Injektionsvätska, lösning | Life Medical ApS | Godkänd |
| 65508 | Thiamine Kabi | Injektions-/infusionsvätska, lösning | Fresenius Kabi AB | Godkänd |
| 56261 | Viant | Pulver till infusionsvätska, lösning | B. Braun Melsungen AG | Godkänd |

Tabellen visar 5 av 13 godkännanden i uppgifterna.

Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter).

<!-- licenses:end -->

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar helt stöd i kliniska prövningar och litteratur, och något tydligt mekanistiskt samband finns inte. Evidensnivån är därför L5.
- Modellen förutsäger även två glaukomindikationer (primärt ärftligt glaukom och öppenvinkelglaukom). Dessa har likaså svagt stöd: för öppenvinkelglaukom finns endast observationsstudier om näringsintag och tiaminnivåer i blodet, och ingen studie har prövat tiamin som behandling.

**För att gå vidare krävs:**
- Ett dokumenterat mekanistiskt samband mellan tiamin och tyroideahormonreceptor beta-signalering, till exempel genom prekliniska studier.
- Verkningsmekanismen för tiamin från DrugBank, så att den mekanistiska analysen kan fördjupas.
- Säkerhetsuppgifter (varningar och kontraindikationer) från produktresumén på Läkemedelsverkets webbplats.
- Kliniska eller prekliniska studier som direkt undersöker tiamin vid den förutsagda sjukdomen innan vidare utvärdering.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-24 | Tiamin: Zubatmin och Viant är kombinationsprodukter med andra vitaminer | Rättad | [Läkemedelsverket – export av godkända läkemedel (verksamma ämnen, registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

