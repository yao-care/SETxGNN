---
layout: default
title: Docusate
parent: Endast modellprediktion (L5)
nav_order: 147
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
description: "Docusate: predikterad ny indikation Plummer-Vinson syndrome (evidensnivå L5). I Sverige, godkännanden (Läkemedelsverket): 2 (giltiga: 2)"
---

# Docusate
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

## Docusate: Plummer-Vinson syndrome
{: .text-alpha }

---

## Sammanfattning

TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Plummer-Vinsons syndrom**, men **inga kliniska prövningar och ingen litteratur** stöder denna riktning.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Plummer-Vinson syndrome |
| TxGNN-förutsägelsepoäng | 0.9918 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Dokusat är i allmänhet känt som ett anjoniskt ytaktivt ämne som verkar som avföringsmjukgörande. Det påverkar varken järnupptag, blodbildning eller slemhinnebildning i matstrupen.

Plummer-Vinsons syndrom kännetecknas av järnbristanemi, sväljsvårigheter och membran i matstrupen. De anemirelaterade indikationerna härrör troligen från kombinationspreparat med järn, där dokusat lindrar järnorsakad förstoppning.

Det finns därför ingen etablerad mekanistisk koppling.

---

## Marknadsinformation Sverige

<!-- licenses:begin -->

| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
|------|------|------|------|------|
| 6514 | Klyx | Rektallösning | Ferring Läkemedel AB | Godkänd |
| 65612 | Dokusatnatrium/Sorbitol Evolan | Rektallösning | Evolan Pharma AB | Godkänd |

Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter).

<!-- licenses:end -->

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): magsår, kaliumbrist, sicklecellanemi, ärftlig persistens av fetalt hemoglobin, primär hyperoxaluri, ärftlig hemokromatos, hemosideros, järnmetabolismrubbning, Wilsons sjukdom, ulcerös kolit, inflammatorisk tarmsjukdom, hemolytisk anemi, appendicit, kronisk atrofisk gastrit, Lebers hereditära optikusneuropati och gastroenterit.
- **Läkemedelsinteraktioner** (4 identifierade):
  - Laktulos – måttlig
  - Mineralolja – måttlig
  - Fenolftalein – måttlig
  - Linaklotid – lindrig

Se produktresumén för fullständig information om varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellens poäng (evidensnivå L5). Inga kliniska prövningar eller publikationer finns, ingen mekanistisk koppling är etablerad. Dokusat har ingen känd effekt på järnbrist eller membran i matstrupen.

<!-- review:begin se-lic-20261106-docusate-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Inga kliniska prövningar eller publikationer finns, ingen mekanistisk koppling är etablerad, och båda svenska godkännandena är indragna.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Aktuella antal och status för godkännandena finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-docusate-1 -->

**För att gå vidare krävs:**
- Detaljerad verkningsmekanism från DrugBank.
- Produktresumé med varningar och kontraindikationer från Läkemedelsverket.
- Litteratur- eller prekliniska data som kan motivera en biologisk koppling mellan dokusat och Plummer-Vinsons syndrom.
- Bedömning av beredningsform och administreringsväg, eftersom de godkända produkterna är rektallösningar.
- Överväg att behandla förutsägelsen som en grafartefakt och prioritera andra kandidater.

<!-- review:begin se-lic-20261124b-docusate-1 -->

> **Granskningsrättelse (2026-11-24)**: Ursprungligen stod det: ”Bedömning av beredningsform och administreringsväg, eftersom de tidigare godkända produkterna är rektallösningar.” Texten beskrev godkännandena eller produkterna som tidigare (inte längre gällande), men enligt Läkemedelsverkets uppgifter har de registreringsstatus Godkänd. Endast den felaktiga tidsangivelsen har ändrats; förslaget i övrigt är oförändrat. Aktuella antal och status för godkännandena finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-lic-20261124b-docusate-1 -->

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”och båda svenska godkännandena är indragna” | Rättad (reviderad 2026-11-24; tidigare version sparad i posten) | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-12 | Tabell: 2 godkännanden (6514, 65612) är godkända, inte indragna | Ersatt av den programgenererade licenstabellen (tidigare: Rättad) | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |
| 2026-11-24 | Rättat: godkännandena beskrevs som tidigare | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

