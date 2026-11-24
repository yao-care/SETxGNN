---
layout: default
title: Ethosuximide
parent: Endast modellprediktion (L5)
nav_order: 179
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
description: "Ethosuximide: predikterad ny indikation Nephrogenic syndrome of inappropriate antidiuresis (evidensnivå L5). I Sverige, godkännanden (Läkemedelsverket): 8 (giltiga: 8)"
---

# Ethosuximide
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

## Ethosuximide: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

---

## Sammanfattning

Etosuximid används ursprungligen för att behandla absensepilepsi. Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder denna riktning, så förutsägelsen bygger enbart på modellen.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN-förutsägelsepoäng | 0.9991 |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 8 av 8) |
| Antal godkännanden | 8 (giltiga: 8) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Baserat på allmänt känd farmakologi blockerar etosuximid T-typ kalciumkanaler i thalamiska neuron, vilket förklarar effekten vid absensepilepsi.

Något direkt samband mellan denna mekanism och NSIAD kan inte påvisas. NSIAD orsakas av aktiverande mutationer i vasopressin V2-receptorn (AVPR2) eller, mer sällan, i GNAS. Detta ger konstant ökad återabsorption av vatten i njurarna, oberoende av vasopressin. Ett eventuellt samband skulle kräva att etosuximid påverkar signalering eller vattenhantering i njurens samlingsrör, men inga data stöder det.

Den mycket höga poängen (0,9991) är en beräknad förutsägelse och ska inte tolkas som biologisk eller klinisk bekräftelse. Likheten mellan den ursprungliga och den nya indikationen har inte kunnat bedömas.

---

## Marknadsinformation Sverige

Godkända indikationstexter saknas i datan. Fem av godkännandena visas nedan.

<!-- licenses:begin -->

| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
|------|------|------|------|------|
| 68510 | Etosuximid 2care4 | Oral lösning | 2care4 ApS | Godkänd |
| 58150 | Ethosuximide Orifarm | Kapsel, mjuk | Orifarm Generics A/S | Godkänd |
| 61462 | Etosuximid Ebb | Oral lösning | Ebb Medical AB | Godkänd |
| 6837 | Suxinutin | Oral lösning | Essential Pharma (M) Ltd | Godkänd |
| 64700 | Ethosuximide Strides | Kapsel, mjuk | Strides Nordic ApS | Godkänd |

Tabellen visar 5 av 8 godkännanden i uppgifterna.

Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter).

<!-- licenses:end -->

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumétext): ångestsyndrom, neuros, dystymi, njursjukdom, pyouretär, blodsjukdom, leversjukdom, gallblåsesjukdom, systemisk lupus erythematosus (inklusive pediatrisk form), neutropeni, agranulocytos och akut intermittent porfyri.
- **Läkemedelsinteraktioner**: totalt 92 interaktioner identifierades. Samtliga 20 som visas i datan är av måttlig allvarlighetsgrad. Bland de viktigaste finns:
  - Opioider och cannabinoider: morfin (även liposomal), opium, dronabinol, nabilon (risk för additiv sedering)
  - Etanol, prometazin, klorfeniramin och metoklopramid (additiv effekt på centrala nervsystemet)
  - Aprepitant, kobicistat, deferasirox och fostamatinib
  - Klorokin, meflokin och hydroxiklorokin
  - Folsyra, leukovorin och levoleukovorin
  - Sibutramin

Produktresumétexter med varningar och kontraindikationer har inte kunnat hämtas. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds endast av modellen (evidensnivå L5), utan kliniska prövningar, litteratur eller känd mekanistisk koppling.

<!-- review:begin se-lic-20261124b-ethosuximide-1 -->

> **Granskningsrättelse (2026-11-24)**: Ursprungligen stod det: ”Dessutom saknas giltiga godkännanden i Sverige.” Borttaget: uppgiften att godkännandena är indragna, avregistrerade eller saknar giltig status stämde inte med Läkemedelsverkets uppgifter, där det finns godkännanden med registreringsstatus Godkänd. Endast den felaktiga uppgiften har ändrats. Aktuella antal och status för godkännandena finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-lic-20261124b-ethosuximide-1 -->

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata från DrugBank och analysera ett möjligt samband med AVPR2/GNAS-signalering.
- Hämta och bearbeta produktresumétexter för varningar och kontraindikationer, så att säkerhetsgranskning kan genomföras.
- Göra en systematisk litteratur- och prövningssökning på etosuximid vid NSIAD.
- Genomföra prekliniska studier (till exempel cellmodeller med aktiverande AVPR2-mutation) för att testa om det finns någon biologisk effekt.
- Beakta kontraindikationerna för njur- och blodsjukdom, eftersom NSIAD är en njurrelaterad störning.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-24 | Rättat: godkännandena är inte indragna/ogiltiga | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

