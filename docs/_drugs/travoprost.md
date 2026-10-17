---
layout: default
title: Travoprost
parent: Endast modellprediktion (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Travoprost: predikterad ny indikation Visceral kalcifylaxi (evidensnivå L5). Ursprunglig indikation: Öppenvinkelglaukom och okulär hypertension"
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
---

# Travoprost
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

# Travoprost: Från öppenvinkelglaukom och okulär hypertension till visceral kalcifylaxi

---

## Sammanfattning

Travoprost är en prostaglandin F2-alfa-analog som ursprungligen används som ögondroppar för att sänka det intraokulära trycket vid **öppenvinkelglaukom** och **okulär hypertension**.
TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **visceral kalcifylaxi**, men det finns **inga kliniska prövningar** och **ingen litteratur** som stöder just denna indikation. Förutsägelsen bygger enbart på modellen (evidensnivå L5).

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Öppenvinkelglaukom och okulär hypertension (enligt kunskapsgrafen; godkännandetexterna i det svenska registret är tomma) |
| Förutsagd ny indikation | Visceral kalcifylaxi |
| TxGNN-förutsägelsepoäng | 99,99 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 10 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Travoprost är en prostaglandin F2-alfa-analog (FP-receptoragonist). Dess effekt vid glaukom är väl belagd: den sänker ögontrycket genom ökat avflöde av kammarvatten.

Något tydligt mekanistiskt samband mellan detta och visceral kalcifylaxi har inte kunnat påvisas. Kalcifylaxi kännetecknas av förkalkning av små blodkärl och mikrotrombos. Travoprost har kärlpåverkande egenskaper, men inget i data stöder att dessa skulle påverka sjukdomsprocessen. Dessutom ger ögondroppar mycket låg systemisk exponering, vilket gör en effekt i inre organ osannolik.

Den höga poängen (nära 1,0) bör därför tolkas försiktigt. Flera andra förutsägelser för samma läkemedel gäller kärl- eller tryckrelaterade tillstånd (till exempel thoracic outlet-syndrom, blue toe-syndrom och spontan koronarartärdissektion). De har likaså saknat studier och en trolig mekanistisk grund, vilket tyder på ett generellt mönster i modellen snarare än ett specifikt samband.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande för visceral kalcifylaxi.

*Anmärkning:* För den bredare förutsägelsen "kärlsjukdom" (rang 5) finns tio prövningar. Nästan alla gäller glaukom och okulär hypertension, alltså den ursprungliga indikationen. Den enda med kärlmått är NCT00308945 (fas 4, 20 deltagare), som mätte retinala kärldiametrar och blodflöde i åderhinnan. Det är en fysiologisk studie och inte en behandlingsstudie för kärlsjukdom.

---

## Marknadsinformation Sverige

Samtliga 10 godkännanden är indragna. Indikationstexter saknas i registret.

| Godkännandenummer | Produktnamn | Beredningsform | Status |
|---------|------|------|-----------|
| 48021 | Travoprost STADA | Ögondroppar, lösning | Indragen |
| 64362 | Trevicopto | Ögondroppar, lösning i endosbehållare | Indragen |
| 48012 | Travoprost Medical Valley | Ögondroppar, lösning | Indragen |
| 48062 | Travoprost Sandoz | Ögondroppar, lösning | Indragen |
| 51223 | Bondulc | Ögondroppar, lösning | Indragen |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): uveit, irissjukdom, sjukdom i ciliarkroppen, panuveit, irit, cystoidt makulaödem och makulaödem i näthinnan.
- **Läkemedelsinteraktioner:** 49 interaktioner hittades. De som visas i data (bland annat kalcitriol, pantoprazol, sukralfat, morfin, metformin, omeprazol, prednison och acetylsalicylsyra) saknar klassificerad allvarlighetsgrad.
- **Observation från litteraturen:** En fallrapport (PMID 19107053) beskriver uveal effusion med exudativ näthinneavlossning efter topikal travoprost hos en patient med Sturge-Webers syndrom, en kärlmissbildningssjukdom. Detta tyder på att försiktighet krävs hos patienter med kärlanomalier.

Se produktresumén för fullständig information om varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för visceral kalcifylaxi bygger enbart på modellen, utan studier eller litteratur, och ett rimligt mekanistiskt samband saknas. Dessutom är samtliga svenska godkännanden indragna och ögondroppar ger låg systemisk exponering.

**För att gå vidare krävs:**
- Hämta och granska produktresumé med varningar och kontraindikationer.
- Hämta verkningsmekanismdata från DrugBank och analysera ett eventuellt samband med kalcifylaxins patologi (kärlförkalkning, mikrotrombos).
- Prekliniska studier (cell- eller djurmodeller) som visar att FP-receptoragonism påverkar kärlförkalkning.
- Utvärdera om en systemisk beredningsform vore nödvändig, eftersom ögondroppar inte ger relevant systemisk exponering.
- Klargöra läkemedlets nuvarande regulatoriska status i Sverige, eftersom alla godkännanden är indragna.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

