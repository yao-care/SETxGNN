---
layout: default
title: Digoxin
parent: Endast modellprediktion (L5)
nav_order: 141
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
description: "Digoxin: predikterad ny indikation Prinzmetal angina (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Digoxin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **5** st
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

## Digoxin: Prinzmetal angina
{: .text-alpha }

---

### Sammanfattning

Digoxin är en hjärtglykosid som ursprungligen används vid behandling av förmaksflimmer och digitalisförgiftning. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Prinzmetal angina** (kärlkrampsangina), men prediktionen bygger enbart på en grafbaserad modell. Det finns **inga kliniska prövningar** och endast **1 publikation** (en allmän översikt utan direkt koppling till digoxin vid denna sjukdom).

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Prinzmetal angina |
| TxGNN-förutsägelsepoäng | 0.9981 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 3 av 3) |
| Antal godkännanden | 3 (giltiga: 3) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Digoxin är allmänt känt som en hämmare av Na⁺/K⁺-ATPas med positivt inotrop och vagotont verkan, och används för frekvenskontroll vid förmaksflimmer.

Prinzmetal angina orsakas av kramp i kranskärlen och behandlas normalt med kalciumkanalblockerare och nitrater. Något trovärdigt mekanistiskt samband mellan digoxin och denna sjukdom har inte kunnat fastställas. Digoxin kan teoretiskt öka hjärtmuskelns syrebehov och har kopplats till kärlsammandragning, så nytta är osannolik och risk för skada kan inte uteslutas.

Den höga poängen (0,9981) ska därför ses som en ren grafbaserad förutsägelse och inte som tecken på verklig effekt. Sambandet till de ursprungliga indikationerna är att båda är hjärtsjukdomar, men det räcker inte som stöd.

<!-- review:begin se-lic-20261106-digoxin-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Alla tre godkännanden (Evolan Pharma AB) är indragna, och för närvarande finns inget giltigt godkännande i Sverige.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 3, varav giltiga: 3; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-digoxin-1 -->

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Översikt | Acta physiologica et pharmacologica Bulgarica | Allmän översikt om kronofarmakologi och dygnsrytmer vid blodtrycksbehandling. Ger inget direkt stöd för digoxin vid Prinzmetal angina. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 9004 | Digoxin Evolan | Tablett | Ej angiven (indraget) |
| 9003 | Digoxin Evolan | Tablett | Ej angiven (indraget) |
| 8811 | Digoxin Evolan | Injektionsvätska, lösning | Ej angiven (indraget) |

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): njursjukdom, kaliumbrist, hyperkalcemi, nefrokalcinos, störd fosformetabolism, hjärtinfarkt, kranskärlstrombos, hemoglobinopati, cor pulmonale, Wolff-Parkinson-White syndrom, sjuka sinusknutan-syndrom, kammarflimmer, hypertrofisk kardiomyopati, AV-block, myxödem, hypotyreos, myokardit, konstriktiv perikardit och restriktiv kardiomyopati.
- **Läkemedelsinteraktioner**: Totalt 100 interaktioner identifierades. Bland de som visas finns flera av måttlig grad, bland annat:
  - Kortikosteroider (hydrokortison, dexametason, betametason, triamcinolon)
  - Amfotericin B (inklusive lipidkomplex)
  - Tetracyklin och doxycyklin
  - Rabeprazol
  - Metformin och akarbos
  - Adrenalin
  - Acetylsalicylsyra
  - Bupropion
  - Kolekalciferol och kalciumfosfat

  Interaktioner av lägre grad omfattar bland annat atropin, hyoscyamin, glykopyrronium och albiglutid.

Se produktresumén för fullständig säkerhetsinformation, eftersom varningar och kontraindikationer från godkänd produktinformation saknas i underlaget.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Prediktionen saknar både kliniska prövningar och relevant litteratur, och det finns inget trovärdigt mekanistiskt samband. Dessutom finns risk för skada vid kranskärlskramp.

<!-- review:begin se-lic-20261106-digoxin-2 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Dessutom finns risk för skada vid kranskärlskramp, och alla svenska godkännanden är indragna.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 3, varav giltiga: 3; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-digoxin-2 -->

**För att gå vidare krävs:**
- Hämta och analysera produktresumé för varningar och kontraindikationer (blockerande dataglapp).
- Hämta verkningsmekanism från DrugBank.
- Genomföra riktad litteraturgenomgång om digoxin vid vasospastisk angina, inklusive säkerhetsaspekter.
- Prekliniska eller mekanistiska studier som visar eventuell nytta innan kliniska studier övervägs.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Alla tre godkännanden (Evolan Pharma AB) är indragna, och för närvarande finns inget giltigt godkännande i Sverige” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-06 | Borttaget: ”och alla svenska godkännanden är indragna” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

