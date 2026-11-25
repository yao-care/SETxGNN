---
layout: default
title: Articaine
parent: Endast modellprediktion (L5)
nav_order: 41
evidence_level: L5
indication_count: 4
monitor_inn: "articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
last_modified_at: 2026-11-25
description: "Articaine: predikterad ny indikation Gikt (gout) (evidensnivå L5). I Sverige, godkännanden (Läkemedelsverket): 6 (giltiga: 6)"
---

# Articaine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

## Artikain: lokalanestetikum av amidtyp (natriumkanalblockerare) → Gikt (gout)
{: .text-alpha }

---

### Sammanfattning

Artikain är ett lokalanestetikum av amidtyp som ges som injektionsvätska, lösning, och som främst används vid tandvård. TxGNN-modellen förutsäger att det kan vara effektivt mot **gikt (gout)**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som direkt studerar detta samband. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Gikt (gout) |
| TxGNN-förutsägelsepoäng | 0,9958 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 6 av 6) |
| Antal godkännanden | 6 (giltiga: 6) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Artikain är känt som ett lokalanestetikum av amidtyp som blockerar spänningsstyrda natriumkanaler och därmed hämmar nervledning.

Någon känd koppling mellan denna mekanism och urinsyrametabolism eller den inflammation som kännetecknar gikt har inte identifierats. Natriumkanalblockad angriper inte de processer som ligger bakom giktattacker, till exempel utfällning av urinsyrakristaller och den efterföljande inflammatoriska reaktionen.

Den höga poängen (0,9958) är därför en beräkningsmässig förutsägelse utan stöd av mekanistiska eller kliniska data. Förutsägelsen bör tolkas med stor försiktighet.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

Enligt de lokala registren gäller samtliga godkännanden för artikain kombinationsprodukter med adrenalin, alla som injektionsvätska, lösning. Indikationstext finns inte registrerad för någon av dem.

<!-- review:begin se-lic-20261124-articaine-1 -->

> **Granskningsrättelse (2026-11-24)**: Ursprungligen stod det: ”Enligt de lokala registren finns fyra godkännanden för enkomponentsprodukter av artikain, alla som injektionsvätska, lösning.” Enligt Läkemedelsverkets uppgifter innehåller samtliga godkännanden för artikain (Septocaine, Septocaine forte, Nordanest) både artikainhydroklorid och adrenalintartrat; texten angav dem som enkomponentsprodukter. Uppgiften om enkomponents- och kombinationsprodukter följer de verksamma ämnena i Läkemedelsverkets uppgifter; antal godkännanden och status finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel (verksamma ämnen, registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-lic-20261124-articaine-1 -->

<!-- licenses:begin -->

| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
|------|------|------|------|------|
| 14251 | Septocaine forte | Injektionsvätska, lösning | SEPTODONT | Godkänd |
| 67433 | Nordanest | Injektionsvätska, lösning | Laboratorios Inibsa S.A. | Godkänd |
| 67432 | Nordanest | Injektionsvätska, lösning | Laboratorios Inibsa S.A. | Godkänd |
| 14380 | Septocaine | Injektionsvätska, lösning | SEPTODONT | Godkänd |

Tabellen visar 4 av 6 godkännanden i uppgifterna.

Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter).

<!-- licenses:end -->

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Tio interaktioner finns registrerade. Den allvarligaste är med nitrit (nitrous acid), klassad som **större (Major)**. Flera interaktioner av **måttlig** grad gäller andra lokalanestetika, bland annat bensokain, lidokain, oxibuprokain, cinkokain och tetrakain, samt liposomalt morfin. Interaktionen med hyaluronidas är **mindre**.

Produktresumén bör konsulteras för fullständig information om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen om gikt saknar stöd i både kliniska prövningar och litteratur, och det finns ingen rimlig mekanistisk koppling mellan natriumkanalblockad och giktens patogenes. Evidensnivån är L5.

**För att gå vidare krävs:**
- Dokumenterad verkningsmekanism och en mekanistisk hypotes för hur artikain skulle kunna påverka gikt
- Prekliniska studier som direkt undersöker effekt vid gikt eller urinsyrarelaterad inflammation
- Genomgång av produktresumén för varningar och kontraindikationer
- Bedömning av om administreringsväg och beredningsform (injektion) är lämpliga för indikationen

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-24 | Artikain: godkännandena gäller kombinationsprodukter med adrenalin, inte enkomponentsprodukter | Rättad | [Läkemedelsverket – export av godkända läkemedel (verksamma ämnen, registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

