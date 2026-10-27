---
layout: default
title: Theophylline
parent: Endast modellprediktion (L5)
nav_order: 421
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Theophylline: predikterad ny indikation Trombotisk sjukdom (evidensnivå L5). Ursprunglig indikation: Astma (enligt kunskapsgrafen…"
monitor_inn: "theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "acute laryngopharyngitis"]
---

# Theophylline
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

## Theophylline: Från astma till trombotisk sjukdom
{: .text-alpha }

---

### Sammanfattning

Theophylline (Theo-Dur) är en luftvägsvidgande substans som ursprungligen användes vid astma, bronkit och andra lungsjukdomar. TxGNN-modellen förutsäger att det kan vara effektivt mot **trombotisk sjukdom**. Förutsägelsen har dock **inga kliniska prövningar** och **ingen publikation som testar theophylline som blodproppshämmande läkemedel**, så den vilar enbart på en beräkningsmodell.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Astma (enligt kunskapsgrafen, eftersom godkännandena saknar indikationstext) |
| Förutsagd ny indikation | Trombotisk sjukdom |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 2 (båda avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

Theophylline hämmar fosfodiesteras (PDE) och blockerar adenosinreceptorer. När PDE hämmas stiger halten av cAMP i trombocyterna, och högre cAMP kan i princip minska trombocytaktiveringen. Detta är grunden till att modellen kopplar läkemedlet till blodproppssjukdom.

Sambandet mellan astma och trombos är indirekt. Mekanismen i luftvägarna (muskelavslappning och antiinflammatorisk effekt) är väl känd, men det finns inga data i underlaget som visar att samma mekanism ger en kliniskt meningsfull antitrombotisk effekt.

Den hämtade litteraturen handlar om ticlopidins farmakokinetik, analysmetoder för trombocytmarkörer, provhantering för mikro-RNA och en sensor för att mäta theophylline. Ingen av dessa studier prövar theophylline som behandling mot trombos. Den höga poängen är därför en beräkningsmässig förutsägelse och inte ett kliniskt belägg.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen av publikationerna prövar theophylline som behandling mot trombos. De mest relevanta, som mest rör trombocytbiologi, är:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratoriestudie | General pharmacology | Milrinon och adenosin hämmar trombocytaggregation via ökad cAMP. Studien gäller milrinon, inte theophylline. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Farmakokinetisk översikt | Clinical pharmacokinetics | Handlar om ticlopidin, ett trombocythämmande läkemedel, inte theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Översikt | CRC critical reviews in biochemistry | Beskriver prostaglandiners och trombocyters roll vid åderförkalkning. Cyklisk AMP nämns som mekanism. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Analysmetod | British journal of haematology | Theophylline används bara som tillsats i provrör för att förhindra trombocytaktivering vid mätning av trombocytfaktor 4. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Äldre klinisk rapport | Minerva cardioangiologica | Gäller en theophyllinderivat (nikotinat) vid kronisk perifer kärlsjukdom. Sammanfattning saknas. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 9445 | Theo-Dur (Karo Pharma AB) | Depottablett | Ingen indikationstext angiven (avregistrerad) |
| 9446 | Theo-Dur (Karo Pharma AB) | Depottablett | Ingen indikationstext angiven (avregistrerad) |

Båda godkännandena är avregistrerade. Det finns därför för närvarande inget giltigt godkännande för theophylline i Sverige.

---

### Säkerhetsaspekter

- **Sjukdomar där läkemedlet enligt kunskapsgrafen är kontraindicerat** (data från en kunskapsgraf, inte från produktresumé): bland annat högt blodttryck, leversvikt och leversjukdom, epilepsi, ångest- och psykossjukdomar, porfyri, njursjukdom, magsår, underfunktion av sköldkörteln, glaukom (öppenvinkel), diabetes och diabetesketoacidos, godartad prostataförstoring, trombocytopeni samt neutropeni och agranulocytos.
- **Läkemedelsinteraktioner**: 371 interaktioner är registrerade.
  - **Allvarlig:** bupropion.
  - **Måttliga (urval):** famotidin, ranitidin, cimetidin, omeprazol, rabeprazol, klaritromycin, doxycyklin, tetracyklin, minocyklin, hydrokortison, dexametason, betametason, triamcinolon, budesonid och aktivt kol.
  - **Lindriga:** efedrin.

För varningar och kontraindikationer enligt produktresumén, se produktresumén. Dessa uppgifter ingår inte i underlaget.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellen, utan kliniska prövningar och utan litteratur som testar theophylline mot trombos.
- Läkemedlet saknar dessutom giltigt godkännande i Sverige och har många interaktioner och kontraindikationer.

**För att gå vidare krävs:**
- Experimentella data som visar att theophylline hämmar trombocytaktivering eller proppbildning i relevanta modeller.
- Kliniska studier (minst fas 2) med trombosrelaterade utfallsmått.
- Produktresumé med fullständiga varningar och kontraindikationer samt en bedömning av tillgänglig beredning.
- En analys av nytta och risk jämfört med etablerade antitrombotiska läkemedel.

Bland övriga förutsägelser för theophylline har **sjukdom i nässlemhinnan** (allergisk rinit) och **trakealsjukdom** något starkare stöd (evidensnivå L3). Det gäller bland annat en fas 2-prövning på allergisk rinit (NCT01132781) som kan vara värd att utvärdera i en separat rapport.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

