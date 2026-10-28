---
layout: default
title: Metolazone
parent: Endast modellprediktion (L5)
nav_order: 288
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
monitor_inn: "metolazone"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Metolazone: predikterad ny indikation Malignant hypertensive renal disease (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Metolazone
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

## Metolazone: Malignant hypertensive renal disease
{: .text-alpha }

---

### Sammanfattning

Metolazon är ett tiazidliknande diuretikum som ursprungligen användes för att behandla högt blodtryck (hypertoni). Det finns dock **inga kliniska prövningar och ingen relevant litteratur** som stöder denna riktning, så förutsägelsen är i nuläget enbart en beräkningsbaserad hypotes.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Malignant hypertensive renal disease |
| TxGNN-förutsägelsepoäng | 0.9984 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Baserat på känd information är metolazon ett tiazidliknande diuretikum som hämmar natrium-klorid-kotransportören i distala tubuli i njuren. Effekten vid hypertoni är väl känd, och mekanistiskt kan volym- och blodtryckskontroll vara tillämpbar även vid andra blodtryckssjukdomar.

Kopplingen är dock svag. Malign renovaskulär hypertoni drivs främst av aktivering av renin-angiotensinsystemet vid förträngning av njurartären. Diuretikainducerad volymförlust kan i stället öka frisättningen av renin, vilket i värsta fall förvärrar tillståndet.

Övriga förutsägelser följer samma mönster:

- **Malign hypertensiv njursjukdom (99,8 %)**: Metolazon behåller effekt vid låg njurfunktion, så det finns ett teoretiskt skäl vid volymöverskott. Malign hypertoni är dock ett akut tillstånd som kräver kontrollerad intravenös behandling, och ett diuretikum är sällan förstahandsval.
- **Pulmonell hypertension (två former, 99,8 %)**: Diuretika används som stödbehandling vid högersidig hjärtsvikt och vätskeöverskott, ibland metolazon som tillägg till loopdiuretika vid diuretikaresistens. Det är symtomlindring och inte sjukdomsmodifierande. Kopplingen till systemisk hypertoni är sannolikt namnbaserad.
- **Braddocks syndrom (99,8 %)**: Mycket sällsynt tillstånd utan tydligt mekanistiskt stöd i underlaget.

---

### Litteraturbevis

För den främsta förutsägelsen (malign renovaskulär hypertoni) finns ingen litteratur. För en av de övriga förutsägelserna (pulmonell hypertension orsakad av lungsjukdom och/eller hypoxi) hittades en enda publikation, som endast är marginellt relevant:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Preklinisk grundforskning | The American Journal of Physiology | Studie på råtta som visar att antalet tiazidreceptorer i njurbarken (mätt med bindning av [3H]metolazon) minskade snabbt och reversibelt, med cirka 90 %, efter akut njurischemi. Studien rör inte pulmonell hypertension. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 41983 (indraget) | Metolazon Abcur | Tablett | Ingen indikationstext tillgänglig |

Det enda godkännandet (Abcur AB, oral tablett) är indraget, och läkemedlet finns därför för närvarande inte på den svenska marknaden.

---

### Säkerhetsaspekter

- **Möjliga kontraindikationer enligt kunskapsgrafen** (ej hämtade från produktresumén): multipel systematrofi, posturalt ortostatiskt takykardisyndrom (POTS), ortostatisk hypotension, leversvikt, pankreatit, systemisk lupus erythematosus (inklusive pediatrisk form), kaliumbrist, diabetes mellitus, diabetesketoacidos, leverkoma, hepatisk encefalopati, anuri, gikt, hyperkalcemi, nefrokalcinos, fosformetabolismrubbning samt HELLP-syndrom.
- **Läkemedelsinteraktioner**: Totalt 249 interaktioner är registrerade. Exempel på måttliga interaktioner:
  - Diabetesläkemedel: akarbos, alogliptin, albiglutid
  - Kortikosteroider: hydrokortison, dexametason, betametason, triamcinolon, beklometason
  - Protonpumpshämmare: omeprazol, rabeprazol
  - Amfotericin B (även lipidkomplex)
  - Bupropion, morfin, bisakodyl, kolekalciferol, kalciumfosfat
  
  Exempel på lindriga interaktioner: doxycyklin, hyoscyamin, atropin.

Varnings- och kontraindikationstext från produktresumén saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellens närhet till den ursprungliga hypertoniindikationen, utan kliniska prövningar eller stödjande litteratur (evidensnivå L5). Dessutom kan den farmakologiska effekten (reninstimulering vid volymförlust) i teorin vara ofördelaktig vid renovaskulär hypertoni, och läkemedlet är för närvarande indraget i Sverige.

**För att gå vidare krävs:**
- Hämta och analysera produktresumén (varningar och kontraindikationer) så att säkerhetsgranskning kan genomföras.
- Komplettera verkningsmekanismdata från DrugBank.
- Systematisk litteratursökning och kontroll av kliniska prövningar för metolazon vid renovaskulär och malign hypertoni.
- Klinisk bedömning av om ett diuretikum alls har en roll vid dessa tillstånd, med tanke på reninaktiveringen.
- Utreda om en ny marknadsföring eller ett nytt godkännande i Sverige är aktuellt, eftersom det befintliga godkännandet är indraget.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

