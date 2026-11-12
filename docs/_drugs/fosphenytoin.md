---
layout: default
title: Fosphenytoin
parent: Endast modellprediktion (L5)
nav_order: 209
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "fosphenytoin"
predicted_indications: ["conjunctivitis", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "manic bipolar affective disorder", "myositis fibrosa", "idiopathic granulomatous myositis", "fibromyalgia"]
description: "Fosphenytoin: predikterad ny indikation Conjunctivitis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Fosphenytoin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

## Fosphenytoin: Conjunctivitis
{: .text-alpha }

---

## Sammanfattning

Fosfenytoin är en prodrug till fenytoin och har ursprungligen använts för att behandla epilepsi och status epilepticus. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **manisk bipolär sjukdom**, men underlaget är mycket begränsat: **inga kliniska prövningar** och **1 publikation** (en liten, ej verifierad explorativ rapport från 2003) stöder för närvarande denna riktning.

Den saknar dock helt stöd i evidens och mekanistiskt resonemang. Denna rapport fokuserar på manisk bipolär sjukdom, eftersom det är den enda förutsagda indikationen med någon form av publicerat underlag.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Conjunctivitis |
| TxGNN-förutsägelsepoäng | 0.9936 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 3 av 3) |
| Antal godkännanden | 3 (giltiga: 3) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på känd information är fosfenytoin en prodrug till fenytoin, en natriumkanalblockerare med antikonvulsiv effekt. Dess effekt vid epilepsi är väl belagd, och mekanistiskt kan den vara tillämpbar på mani genom dämpning av neuronal överretbarhet.

Flera antikonvulsiva läkemedel med natriumkanalaktivitet, till exempel karbamazepin, valproat och lamotrigin, är väletablerade vid bipolär mani. Det ger ett resonemang på läkemedelsklassnivå för att fosfenytoin skulle kunna ha en effekt.

Underlaget är dock indirekt och preliminärt. Fenytoin är i sig inte en etablerad stämningsstabiliserare, och den enda publikationen är en liten explorativ rapport vars fulltext inte har granskats.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Explorativ klinisk rapport (design ej verifierad) | The Journal of Clinical Psychiatry | Studien testade hypotesen att högdos fenytoin intravenöst kan ha akut antimanisk effekt. Fosfenytoin användes eftersom det ger få hjärt- och lokala venbiverkningar. Resultat framgår inte av det tillgängliga sammandraget. |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 14441 | Pro-Epanutin (Pfizer AB) | Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning | Uppgift saknas |
| 63732 | Pro-Epanutin (Orifarm AB) | Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning | Uppgift saknas |
| 58390 | Pro-Epanutin (Orifarm AB) | Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning | Uppgift saknas |

<!-- review:begin se-row-20261112-fosphenytoin-1 -->

> **Granskningsrättelse (2026-11-12)**: Ursprungligen stod det: ”14441 / Pro-Epanutin (Pfizer AB) / Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning / Uppgift saknas (indraget); 63732 / Pro-Epanutin (Orifarm AB) / Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning / Uppgift saknas (indraget); 58390 / Pro-Epanutin (Orifarm AB) / Koncentrat till infusionsvätska, lösning/injektionsvätska, lösning / Uppgift saknas (indraget)” Enligt Läkemedelsverkets registreringsstatus (2026-11-02) har 14441, 63732, 58390 status Godkänd; tabellen angav dem som indraget. Endast statusuppgiften i tabellen har ändrats. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-row-20261112-fosphenytoin-1 -->

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (hämtade från relationer i TxGNN:s kunskapsgraf, inte från produktresumétext): långt QT-syndrom (även ärftligt), torsades de pointes, plötsligt hjärtstopp, hjärtledningsrubbning, atrioventrikulärt block, Adams-Stokes syndrom, njursjukdom, leversjukdom, gallblåsesjukdom, trombocytopeni, leukopeni, pancytopeni, agranulocytos, neutropeni (inklusive medfödda former), systemisk lupus erythematosus, lågt blodtryck, missbruk/beroende, hyperfosfatemi samt sjukdom i lymfsystemet.
- **Läkemedelsinteraktioner**: Totalt 306 interaktioner identifierades. Bland de som visas finns:
  - **Allvarliga (Major):** cimetidin, eliglustat
  - **Måttliga (Moderate):** bland annat famotidin, ranitidin, doxycyklin, hydrokortison, betametason, klaritromycin, aprepitant, dronabinol samt flera diabetesläkemedel (akarbos, alogliptin, kanagliflozin, klorpropamid, albiglutid, dulaglutid) och D-vitaminer (kolekalciferol, kalcifediol, kalcitriol)
  - **Lindriga (Minor):** acetylsalicylsyra

Se produktresumén för fullständig säkerhetsinformation, eftersom varningar och kontraindikationer från godkänd produktinformation inte fanns tillgängliga.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den enda stödjande publikationen är en liten explorativ rapport från 2003 utan verifierad design eller resultat, och inga kliniska prövningar finns. Säkerhetsunderlaget från produktinformationen saknas.

<!-- review:begin se-lic-20261106-fosphenytoin-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Samtliga svenska godkännanden är dessutom indragna, och säkerhetsunderlaget från produktinformationen saknas.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 3, varav giltiga: 3; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-fosphenytoin-1 -->

**För att gå vidare krävs:**
- Granskning av fulltexten till PMID 12716241 för att bedöma studiedesign, storlek och resultat
- Systematisk litteratursökning efter ytterligare studier av fenytoin/fosfenytoin vid mani
- Hämtning och genomgång av produktresumé med varningar och kontraindikationer (blockerande dataluckor)
- Hämtning av verkningsmekanismdata från DrugBank
- Utvärdering av administreringsväg, eftersom fosfenytoin ges intravenöst eller intramuskulärt och därför är mindre lämpat för långtidsbehandling
- Bedömning av läkemedlets nuvarande tillgänglighet i Sverige

<!-- review:begin se-lic-20261106-fosphenytoin-2 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Bedömning av läkemedlets nuvarande tillgänglighet i Sverige, då inget godkännande är giltigt” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 3, varav giltiga: 3; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-fosphenytoin-2 -->

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”amtliga svenska godkännanden är dessutom indragna, och s” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-06 | Borttaget: ”då inget godkännande är giltigt” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-12 | Tabell: 3 godkännanden (14441, 63732, 58390) är godkända, inte indragna | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

