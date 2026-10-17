---
layout: default
title: Buprenorphine
parent: Endast modellprediktion (L5)
nav_order: 71
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Buprenorphine: predikterad ny indikation Akut intermittent porfyri (evidensnivå L5). Ursprunglig indikation: Opioidberoende (enligt kunskapsgrafen"
monitor_inn: "buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

# Buprenorfin: Från opioidberoende till akut intermittent porfyri

---

## Sammanfattning

Buprenorfin användes ursprungligen för att behandla opioidberoende (inklusive morfinberoende och substansberoende i vidare mening). TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **akut intermittent porfyri**, men det finns **inga kliniska prövningar** och endast **1 publikation** (en fallrapport från 1993 om anestesihantering). Förutsägelsen bygger därför i praktiken på modellens poäng, utan stöd i kliniska data.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Opioidberoende (enligt kunskapsgrafen; ingen indikationstext finns i de svenska godkännandena) |
| Förutsagd ny indikation | Akut intermittent porfyri |
| TxGNN-förutsägelsepoäng | 99,4 % |
| Evidensnivå | L4 (endast en fallrapport, inga prövningar) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 20 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det insamlade underlaget. Baserat på känd information är buprenorfin en partiell agonist på my-opioidreceptorn och en antagonist på kappa-receptorn. Dess effekt vid opioidberoende är väl belagd.

Något trovärdigt mekanistiskt samband med akut intermittent porfyri har inte kunnat identifieras. Sjukdomen beror på en störning i hembiosyntesen (enzymerna ALAS1 och PBGD), och buprenorfin påverkar inte denna väg. Den enda litteraturen är en fallrapport om anestesi vid operation hos en patient med porfyri. Den visar på möjlig användning vid smärtlindring i samband med operation eller attacker, men det är symtomlindring och inte en behandling av sjukdomen.

Den höga modellpoängen (0,994) stöds alltså inte av klinisk evidens. Den bör tolkas som en hypotes från kunskapsgrafen och inte som ett belagt samband.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Fallrapport | Masui. The Japanese journal of anesthesiology | Anestesihantering hos en 40-årig kvinna med misstänkt akut intermittent porfyri som genomgick operation för äggstockscancer. Beskriver perioperativ hantering, inte behandling av porfyrin själv. |

---

## Marknadsinformation Sverige

Samtliga 20 godkännanden är indragna. Ingen godkänd indikationstext finns registrerad. Ett urval av de huvudsakliga godkännandena:

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 51208 | Espranor | Frystorkad tablett | Ingen indikationstext registrerad |
| 49410 | Norspan | Depotplåster | Ingen indikationstext registrerad |
| 42325 | Molterfin | Resoriblett, sublingual | Ingen indikationstext registrerad |
| 59799 | Buprefarm | Depotplåster | Ingen indikationstext registrerad |
| 42327 | Subuphine | Resoriblett, sublingual | Ingen indikationstext registrerad |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumétext): Tillstånd som kunskapsgrafen kopplar till kontraindikation är bland annat långt QT-syndrom och torsades de pointes, kronisk obstruktiv lungsjukdom, andningssvikt, leversjukdom (inklusive kronisk hepatit B och C), binjurebarksinsufficiens (Addisons sjukdom), hypotyreos, ortostatisk hypotension, paralytisk ileus och tarmobstruktion, godartad prostataförstoring, förhöjt intrakraniellt tryck samt substansberoende. Observera att den sista posten är intressant i sammanhanget, eftersom buprenorfin används vid opioidberoende.
- **Läkemedelsinteraktioner**: Totalt 264 interaktioner är registrerade. Bland de som klassas som **allvarliga (Major)** finns alvimopan, bupropion, morfin, cisaprid och dolasetron. Flera interaktioner med medelhög allvarlighetsgrad (Moderate) finns också, till exempel med klaritromycin, cimetidin, famotidin, aprepitant, dexametason, atropin och loperamid.

Se produktresumén för fullständig information om varningar och försiktighetsåtgärder, eftersom uppgifter från produktresumén inte har kunnat hämtas till denna rapport.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar både kliniska prövningar och ett trovärdigt mekanistiskt samband. Den enda litteraturen rör smärtlindring och anestesi, inte behandling av sjukdomen.
- Dessutom är samtliga svenska godkännanden för närvarande indragna.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata (till exempel via DrugBank) och produktresumétext för varningar och kontraindikationer från MPA.
- Prekliniska studier som kan visa en verklig effekt på hembiosyntes eller sjukdomsförlopp vid akut intermittent porfyri.
- Bedömning av om buprenorfin enbart är aktuellt för symtomatisk smärtlindring vid porfyriattacker, vilket i så fall inte är en egentlig ny indikation.
- Klargöra marknadsstatus och tillgängliga beredningsformer i Sverige, eftersom inget godkännande är giltigt för närvarande.

---

*Övriga förutsagda indikationer (lingual-facial-bukkal dyskinesi, kronisk tics, kontinuerliga spik-vågor under sömn, benigna skakningsattacker samt extrapyramidala rörelsesjukdomar) har också låg evidens (L4–L5) och rekommenderas likaså att avvaktas.*
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

