---
layout: default
title: Metformin
parent: Endast modellprediktion (L5)
nav_order: 281
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: predikterad ny indikation Fokalt stelbenssyndrom (focal stiff limb syndrome) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Metformin
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

## Metformin: Fokalt stelbenssyndrom (focal stiff limb syndrome)
{: .text-alpha }

---

## Sammanfattning

Metformin är ett läkemedel som ursprungligen används för att behandla typ 2-diabetes. TxGNN-modellen förutsäger att det kan vara effektivt mot **fokalt stelbenssyndrom** (focal stiff limb syndrome), med en mycket hög modellpoäng. Det finns dock **inga kliniska prövningar och ingen publicerad litteratur** som stöder denna riktning, så förutsägelsen bygger enbart på en datormodell.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Fokalt stelbenssyndrom (focal stiff limb syndrome) |
| TxGNN-förutsägelsepoäng | 0.9945 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: minst 20) |
| Antal godkännanden | 20 (samtliga avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är metformin ett blodsockersänkande läkemedel vid typ 2-diabetes. Dess effekt vid den indikationen är väletablerad, och metformin har beskrivits påverka bland annat AMPK-signalering och inflammation. Mekanistiskt är det dock inte visat att detta kan tillämpas på fokalt stelbenssyndrom.

Fokalt stelbenssyndrom hör till spektrumet av stelhetssyndrom (stiff-person-spektrumet). Det anses vara autoimmunt och innebär nedsatt GABA-förmedlad hämning, ofta med antikroppar mot GAD65. Ingen direkt koppling till metforminets verkningssätt finns i underlaget.

Den höga poängen kommer från TxGNN-modellen (deep learning) och kan spegla likheter som modellen har lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Anti-GAD65-autoimmunitet är kopplad till autoimmun diabetes, vilket kan göra att ett diabetesläkemedel hamnar nära sjukdomen i modellens lärda samband. Det är sannolikt en effekt av dessa likheter snarare än ett terapeutiskt resonemang.

Övriga förutsagda indikationer har liknande svaga underlag:

| Förutsagd indikation | Poäng | Kommentar |
|------|------|------|
| Klassiskt stelmanssyndrom (classic stiff person syndrome) | 0,9940 | Autoimmun sjukdom; troligen grafartefakt via GAD65-kopplingen till diabetes |
| Opsismodysplasi | 0,9940 | Sällsynt skelettsjukdom med INPPL1-mutation (insulin-/PI3K-signalering); endast teoretisk koppling |
| Tiaminresponsivt dysfunktionssyndrom | 0,9940 | Metformin åtgärdar inte det underliggande tiaminrelaterade defekten |

---

## Marknadsinformation Sverige

Samtliga 20 godkännanden är avregistrerade. Inga godkännanden har en angiven indikationstext i de sammanställda data. Nedan visas fem av dem.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 27729 | Metformin Bluefish | Filmdragerad tablett | Ingen indikationstext angiven |
| 27669 | Metformin Aurobindo | Filmdragerad tablett | Ingen indikationstext angiven |
| 10799 | Glucophage | Filmdragerad tablett | Ingen indikationstext angiven |
| 41978 | Metformin Actavis | Filmdragerad tablett | Ingen indikationstext angiven |
| 53521 | Metformin Sandoz | Filmdragerad tablett | Ingen indikationstext angiven |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (hämtade från en kunskapsgraf, inte från produktresumén): leversvikt, leversjukdom, njursjukdom, pankreatit, gallblåsesjukdom, kronisk hjärtsvikt, adrenokortikal insufficiens, sjukdom i tymus samt hypofysär insufficiens och besläktade tillstånd (bl.a. hypogonadotrop hypogonadism, tillväxthormonbrist, Kallmanns syndrom och Sheehans syndrom).
- **Läkemedelsinteraktioner**: Totalt 642 interaktioner är registrerade. Bland dem som listats finns två av allvarlig grad (**Major**):
  - **Acetazolamid**
  - **Etanol (alkohol)**

  Flera interaktioner av måttlig grad (Moderate) finns också, bland annat med dolutegravir, abemaciklib, hydroklortiazid, ibuprofen, ketorolak, nifedipin, etinylestradiol, hydrokortison, adrenalin, salbutamol, formoterol, fenylefrin, pseudoefedrin och ranitidin. Interaktioner med acarbos och topikala kortikosteroider bedöms som lindriga (Minor).

Produktresumés varningar och kontraindikationer ingick inte i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen är enbart en modellprognos (evidensnivå L5) utan kliniska prövningar eller litteratur, och ingen mekanistisk koppling är känd. Dessutom saknas giltiga godkännanden i Sverige, och produktresuméns säkerhetsdata saknas.

**För att gå vidare krävs:**
- Hämta och granska produktresumén från Läkemedelsverket (varningar och kontraindikationer).
- Komplettera data om metforminets verkningsmekanism (t.ex. via DrugBank).
- Genomföra en systematisk litteratursökning och en sökning efter kliniska prövningar för fokalt stelbenssyndrom och klassiskt stelmanssyndrom.
- Undersöka om en biologiskt rimlig mekanism finns, till exempel via prekliniska studier, innan fortsatta steg övervägs.
- Klargöra marknadsläget: läkemedlet är marknadsfört och 20 giltiga godkännanden finns.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

