---
layout: default
title: Docusate
parent: Endast modellprediktion (L5)
nav_order: 147
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Docusate: predikterad ny indikation Plummer-Vinsons syndrom (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext registrerad i svenska godkännanden. Enligt kuns…"
monitor_inn: "docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
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

## Dokusat: Från järnbristanemi och förstoppning till Plummer-Vinsons syndrom
{: .text-alpha }

---

## Sammanfattning

Dokusat (docusate) är ett avföringsmjukgörande medel som i kunskapsgrafen är kopplat till förstoppning och flera typer av anemi, troligen genom användning i kombinationspreparat med järn. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Plummer-Vinsons syndrom**, men **inga kliniska prövningar och ingen litteratur** stöder denna riktning. Förutsägelsen bedöms som ett artefaktmönster i grafen snarare än en farmakologiskt grundad hypotes.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext registrerad i svenska godkännanden. Enligt kunskapsgrafen: förstoppning, järnbristanemi, folatbristanemi m.fl. |
| Förutsagd ny indikation | Plummer-Vinsons syndrom |
| TxGNN-förutsägelsepoäng | 99,2 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Dokusat är i allmänhet känt som ett anjoniskt ytaktivt ämne som verkar som avföringsmjukgörande. Det påverkar varken järnupptag, blodbildning eller slemhinnebildning i matstrupen.

Den höga poängen (0,992) speglar sannolikt närhet i kunskapsgrafen till läkemedlets anemirelaterade indikationer. Plummer-Vinsons syndrom kännetecknas av järnbristanemi, sväljsvårigheter och membran i matstrupen. De anemirelaterade indikationerna härrör troligen från kombinationspreparat med järn, där dokusat lindrar järnorsakad förstoppning.

Det finns därför ingen etablerad mekanistisk koppling. Sambandet är en association i kunskapsgrafen, inte en farmakologisk förklaring. Samma bedömning gäller den näst högst rankade förutsägelsen, vitamin B12- och folatoberoende konstitutionell megaloblastisk anemi (poäng 99,2 %), som sannolikt är en följd av att anemietiketter sprids i grafen.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation | Status |
|---------|------|------|-----------|------|
| 6514 | Klyx (Ferring Läkemedel AB) | Rektallösning | Ingen indikationstext registrerad | Indragen |
| 65612 | Dokusatnatrium/Sorbitol Evolan (Evolan Pharma AB) | Rektallösning | Ingen indikationstext registrerad | Indragen |

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
- Förutsägelsen bygger enbart på modellens poäng (evidensnivå L5). Inga kliniska prövningar eller publikationer finns, ingen mekanistisk koppling är etablerad, och båda svenska godkännandena är indragna. Dokusat har ingen känd effekt på järnbrist eller membran i matstrupen.

**För att gå vidare krävs:**
- Detaljerad verkningsmekanism från DrugBank.
- Produktresumé med varningar och kontraindikationer från Läkemedelsverket.
- Litteratur- eller prekliniska data som kan motivera en biologisk koppling mellan dokusat och Plummer-Vinsons syndrom.
- Bedömning av beredningsform och administreringsväg, eftersom de tidigare godkända produkterna är rektallösningar.
- Överväg att behandla förutsägelsen som en grafartefakt och prioritera andra kandidater.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

