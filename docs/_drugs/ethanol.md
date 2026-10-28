---
layout: default
title: Ethanol
parent: Endast modellprediktion (L5)
nav_order: 177
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Ethanol: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext angiven i godkännandedatan"
monitor_inn: "ethanol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Ethanol
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

## Etanol: Från ospecificerad indikation till migrän
{: .text-alpha }

---

### Sammanfattning

Etanol (varumärket Streplieve m.fl.) har inga angivna godkända indikationer i den svenska licensdatan, och läkemedlet marknadsförs med 20 giltiga godkännanden. TxGNN-modellen (deep learning) förutsäger att etanol kan vara effektivt mot **migrän** (poäng 0,9929), men det finns **inga kliniska prövningar** och ingen publikation som visar behandlingseffekt. Litteraturen beskriver tvärtom etanol som en **utlösande faktor** för migrän, och evidensen är därför på nivå L5.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext angiven i godkännandedatan |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 0,9929 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: minst 20) |
| Antal godkännanden | 20 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig för etanol i det data som sammanställts för denna rapport. Dessutom saknas en dokumenterad ursprunglig indikation, så sambandet mellan en befintlig och en ny användning går inte att beskriva.

Den höga poängen kommer från TxGNN-modellen (deep learning) och kan spegla likheter som modellen lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Publikationerna pekar åt motsatt håll: etanol är en känd utlösare av migränanfall. En prekliniktudie (PMID 37101198, 2023) visar att acetaldehyd, en nedbrytningsprodukt av etanol, verkar via CGRP-receptorn och TRPA1 i Schwann-celler och ger överkänslighet runt ögat hos möss. Det är en mekanism för att *framkalla* migrän, inte för att behandla den.

Det finns därför inget stöd för att etanol skulle fungera som migränbehandling. Den näst högst rankade förutsägelsen, migrän med hjärnstamsaura (poäng 0,9914), saknar också direkt evidens. Poängen verkar ärvd från den överordnade migränen, och träffarna i litteraturen är indirekta eller felmatchningar.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Flera av de hämtade publikationerna handlar om andra läkemedel eller är rena nyckelordsträffar. De mest relevanta för etanol och migrän är:

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Översikt | Headache | Beskriver det komplexa sambandet mellan alkohol och migrän, bland annat alkohol som utlösare |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preklinisk (djur) | Journal of biomedical science | Etanolinducerad överkänslighet via acetaldehyd, CGRP-receptor och TRPA1 hos möss; relevant för migrän som utlösande mekanism |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetisk associationsstudie | Headache | Undersöker ADH2-genotyp (alkoholdehydrogenas) och migränrisk |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | Preklinisk (mekanistisk) | Cephalalgia | Öppning av ATP-känsliga kaliumkanaler aktiverar nociceptorer i hjärnhinnorna; bakgrund till migränens uppkomst |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | Kohortstudie | Aerospace Medicine and Human Performance | Migränhistorik och utfall hos militärpiloter; ingen etanolbehandling studerad |
| [29299688](https://pubmed.ncbi.nlm.nih.gov/29299688/) | 2018 | Genetisk associationsstudie | Journal of Neural Transmission | GABA-receptorgener och migränrisk |
| [42153521](https://pubmed.ncbi.nlm.nih.gov/42153521/) | 2026 | Översikt (scoping) | Drug and Alcohol Review | CGRP-signalering vid alkoholberoende; kopplar samman CGRP och alkoholmekanismer |

Ingen av studierna utvärderar etanol som behandling mot migrän.

---

### Marknadsinformation Sverige

Samtliga 20 godkännanden är avregistrerade. Indikationstext saknas för alla. De fem första är:

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 63827 | Streplieve | Sirap | Ej angiven |
| 59205 | Hedexin | Sirap | Ej angiven |
| 27132 | Curbisal | Kapsel, mjuk | Ej angiven |
| 63720 | Strepmuco | Sirap | Ej angiven |
| 54946 | Sefitude | Dragerad tablett | Ej angiven |

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner:** Totalt 471 interaktioner är registrerade. Exempel:

- **Eluxadoline** – allvarlig (Major)
- **Måttliga (Moderate):** acarbos, albiglutid, acetohexamid, alogliptin, acetylsalicylsyra, atropin, bupropion, kanagliflozin, klorpropamid, dapagliflozin, dronabinol, dulaglutid, empagliflozin
- **Lindriga (Minor):** doxycyklin, cimetidin

Se produktresumén för information om varningar och kontraindikationer, eftersom sådana data saknas i det underlag som sammanställts.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Det finns ingen klinisk eller publicerad evidens för att etanol behandlar migrän. Den tillgängliga litteraturen beskriver snarare etanol som en utlösare, och den höga modellpoängen kommer från TxGNN-modellen (deep learning) och kan spegla likheter som modellen lärt sig mellan relaterade sjukdomar, inte biologisk evidens.
- Läkemedlet marknadsförs i Sverige med 20 giltiga godkännanden, och säkerhetsdata från produktresumén saknas.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket är ett blockerande datagap för säkerhetsgranskning
- Komplettera verkningsmekanismen från DrugBank
- Systematiskt granska om det finns några studier som visar terapeutisk effekt av etanol vid migrän, och bedöma om modellens poäng (TxGNN, deep learning) speglar likheter mellan relaterade sjukdomar snarare än en behandlande roll
- Därefter bör prekliniska och kliniska data finnas innan en ny bedömning görs
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

