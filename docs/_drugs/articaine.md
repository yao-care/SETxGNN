---
layout: default
title: Articaine
parent: Endast modellprediktion (L5)
nav_order: 41
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Articaine: predikterad ny indikation Gikt (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext registrerad i godkännandena"
monitor_inn: "articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
---

# Articaine
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

# Artikain: Från lokalbedövning (indikationstext saknas) till gikt

---

### Sammanfattning

Artikain är ett amidtyp-lokalanestetikum som i Sverige har haft godkända injektionsprodukter (Septocaine, Septocaine forte och Nordanest), men inga av dessa godkännanden är längre giltiga. Det finns ingen registrerad indikationstext i de data som har sammanställts för denna rapport.
TxGNN-modellen förutsäger att artikain kan vara effektivt mot **gikt**, med **0 kliniska prövningar** och **0 publikationer** som stöder denna riktning. Förutsägelsen bygger enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext registrerad i godkännandena |
| Förutsagd ny indikation | Gikt |
| TxGNN-förutsägelsepoäng | 99,6 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 4 (0 giltiga, 4 indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som har sammanställts. Allmänt känt är att artikain är ett amidtyp-lokalanestetikum som blockerar spänningsstyrda natriumkanaler och därmed hindrar nervsignaler. Detta används framför allt för smärtlindring vid tandbehandling.

Det finns inget känt samband mellan natriumkanalblockad och urinsyrametabolism eller den inflammation som kännetecknar gikt. Den höga poängen (99,6 %) är en grafbaserad förutsägelse och stöds inte av mekanistiska eller kliniska data. Förutsägelsen bör därför ses som en hypotes av låg trovärdighet, inte som ett underbyggt förslag.

Övriga högt rankade förutsägelser är exostos (99,4 %), allergisk astma (99,4 %) och intrinsic astma (99,3 %). Inte heller för dessa finns någon rimlig mekanistisk koppling eller några kliniska studier. De två publikationer som hittades för allergisk astma handlar om överkänslighetsreaktioner mot lokalanestetika, inte om behandling av astma, och är sannolikt träffar på ordet "allergi".

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 14251 | Septocaine forte | Injektionsvätska, lösning | Ingen indikationstext registrerad (indragen) |
| 67433 | Nordanest | Injektionsvätska, lösning | Ingen indikationstext registrerad (indragen) |
| 67432 | Nordanest | Injektionsvätska, lösning | Ingen indikationstext registrerad (indragen) |
| 14380 | Septocaine | Injektionsvätska, lösning | Ingen indikationstext registrerad (indragen) |

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgraf (inte produkttext)**: Kunskapsgrafen kopplar artikain till bland annat följande tillstånd: högt blodttryck, njursjukdom, leversjukdom, gallblåsesjukdom, diabetes och diabetisk ketoacidos, kranskärlssjukdom, hjärtinfarkt, plötsligt hjärtstopp, retledningssjukdom i hjärtat, trångvinkelglaukom, myasthenia gravis och andra sjukdomar i nerv-muskelövergången, butyrylkolinesterasbrist, hemoglobinopati, hypertyreos (inklusive Graves sjukdom), parkinsonism/Parkinsons sjukdom samt dilaterad kardiomyopati. Dessa är relationer från en modell och ersätter inte kontraindikationer i produktresumén.
- **Läkemedelsinteraktioner** (10 identifierade; de viktigaste):
  - **Major**: Salpetersyrlighet (nitrit)
  - **Moderate**: Liposomalt morfin, bensokain (topikal), lidokain (ögon och topikal), oxibuprokain (ögon), cinkokain (topikal), tetrakain (ögon och topikal)
  - **Minor**: Hyaluronidas

Någon varnings- eller kontraindikationstext från produktresumén fanns inte tillgänglig. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för gikt bygger enbart på en modellpoäng. Det finns inga kliniska prövningar, ingen litteratur och ingen rimlig mekanism, och alla svenska godkännanden är indragna.

**För att gå vidare krävs:**
- Tydlig verkningsmekanism för artikain och en biologiskt rimlig koppling till urinsyrametabolism eller gikt-inflammation
- Prekliniska data som visar effekt i giktmodeller
- Produktresumé med varningar och kontraindikationer från Läkemedelsverket, eftersom säkerhetsgranskning annars inte kan genomföras
- Klargörande av administreringsväg, eftersom artikain ges som injektion för lokal bedövning och inte har någon känd systemisk användning vid gikt
- Förnyad bedömning av om en ny ansökan om godkännande i Sverige är aktuell
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

