---
layout: default
title: Procaine
parent: Måttlig evidens (L3-L4)
nav_order: 366
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Procaine: predikterad ny indikation Metemoglobinemi (evidensnivå L4). Ursprunglig indikation: Ej angiven (godkännandet saknar indikationstext)"
monitor_inn: "procaine"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis"]
---

# Procaine
{: .fs-9 }

Evidensnivå: **L4** | Förutsagda indikationer: **10** st
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

## Prokain: Från ej angiven ursprunglig indikation till metemoglobinemi
{: .text-alpha }

---

### Sammanfattning

Prokain är ett lokalbedövningsmedel (en ester av para-aminobensoesyra). I Sverige finns endast ett avregistrerat godkännande, Cardioplexol, en lösning för kardioplegi. Någon godkänd indikationstext finns inte angiven.
TxGNN-modellen förutsäger att prokain kan vara effektivt mot **metemoglobinemi**, men det finns **inga kliniska prövningar** och endast **5 publikationer**. Litteraturen visar dessutom att prokain *orsakar* metemoglobinemi snarare än behandlar den, så förutsägelsen är sannolikt en artefakt i kunskapsgrafen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven (godkännandet saknar indikationstext) |
| Förutsagd ny indikation | Metemoglobinemi |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L4 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 1 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Prokain är ett lokalbedövningsmedel av estertyp, och det är allmänt känt att sådana läkemedel blockerar natriumkanaler. Farmakologiska data pekar på möjlig koppling till ryanodinreceptorerna RyR1 och RyR2, men underlag för bioaktivitet vid dessa mål saknas.

Det finns ingen rimlig mekanism som talar för en behandlande effekt vid metemoglobinemi. Publicerade fallrapporter visar tvärtom att prokain (bland annat givet intravenöst) kan **orsaka** metemoglobinemi. Det höga modellvärdet speglar därför troligen ett samband mellan läkemedel och sjukdom i kunskapsgrafen som rör en biverkan, inte en terapeutisk effekt. Säkerhetssignalen går alltså i motsatt riktning mot den föreslagna användningen.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Fallrapport | Acta physiologica latino americana | Metemoglobinemi orsakad av intravenöst prokain |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Klinisk studie | Zhonghua wai ke za zhi | Studie av hur intravenös prokainanestesi påverkar metemoglobinnivåer |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Fallrapport | Lancet | Metemoglobinemi efter lignokain (annat lokalbedövningsmedel) |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Översikt | Drugs | Översikt om rationell användning av lokalbedövningsmedel |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Farmakokinetisk studie | American Journal of Obstetrics and Gynecology | Passage av prokain och para-aminobensoesyra över human placenta |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 54736 | Cardioplexol | Lösning för kardioplegi | Ej angiven (avregistrerad) |

---

### Säkerhetsaspekter

- **Möjliga sjukdomsrelaterade kontraindikationer (från kunskapsgrafen, inte produkttext)**: långt QT-syndrom och torsades de pointes, hjärt-kärlsjukdom och AV-block, njur- och leversjukdom, trombocytopeni, neutropeni och agranulocytos, systemisk lupus erytematosus, kaliumbrist, lågt blodtryck, myasthenia gravis, butyrylkolinesterasbrist samt Clostridium difficile-kolit.
- **Läkemedelsinteraktioner** (17 poster, varav de viktigaste):
  - **Allvarlig**: nitrit (salpetersyrlighet).
  - **Måttlig**: sulfasalazin samt andra lokalbedövningsmedel (lidokain, bensokain, kokain, tetrakain, oxibuprokain, cinkokain).
  - **Lindrig**: laronidas, hyaluronidas, doxorubicin (inklusive liposomal form).
- **Farmakologiska mål**: RyR1 och RyR2 (ryanodinreceptorer), utan bekräftad bioaktivitet.

Uppgifter om varningar och kontraindikationer från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds inte av någon klinisk prövning, och litteraturen visar att prokain kan orsaka metemoglobinemi, vilket är motsatt effekt mot den önskade. Evidensen är L4 och mekanistiskt stöd saknas.

**För att gå vidare krävs:**
- Uppgifter om verkningsmekanism från DrugBank för att kunna analysera mekanistiska samband.
- Varningar och kontraindikationer från produktresumén hos Läkemedelsverket.
- Ett tydligt skäl att tro att det finns ett terapeutiskt (inte skadligt) samband, annars bör förutsägelsen förkastas.
- Andra förutsagda indikationer är mer rimliga att utreda, framför allt **tendinit** (evidensnivå L3). Där finns en modern studie från 2022 om prokaininjektion vid supraspinatustendinopati (PMID 35480510) samt en randomiserad jämförelse av lokalbedövning och kortikosteroid vid lateral epikondylit (PMID 23494116, lokalbedövning som jämförelse, inte prokain specifikt). Även **fibromyalgi** kan utredas som en forskningsfråga för symtomlindrande lokal användning, men underlaget består av gamla, okontrollerade rapporter och inga prövningar är registrerade.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

