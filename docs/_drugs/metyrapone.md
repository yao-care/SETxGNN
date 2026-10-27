---
layout: default
title: Metyrapone
parent: Endast modellprediktion (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metyrapone: predikterad ny indikation Ansträngningsutlöst malign hypertermi (evidensnivå L5). Ursprunglig indikation: Ej angiven i godkännandet"
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
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

## Metyrapon: Från ursprunglig indikation (ej angiven i godkännandet) till ansträngningsutlöst malign hypertermi
{: .text-alpha }

---

## Sammanfattning

Metyrapon hämmar enzymet 11-beta-hydroxylas (CYP11B1) och används som diagnostiskt test av hypotalamus–hypofys-funktionen samt ibland vid behandling av Cushings syndrom. Det svenska godkännandet innehåller ingen angiven indikationstext. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **ansträngningsutlöst malign hypertermi**, men det finns **inga kliniska prövningar** och **ingen publikation** som stöder denna riktning. Förutsägelsen är enbart beräkningsbaserad och saknar en rimlig mekanistisk grund.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i godkännandet (diagnostiskt test av hypotalamus–hypofys-funktion och ibland Cushings syndrom enligt farmakologidata) |
| Förutsagd ny indikation | Ansträngningsutlöst malign hypertermi |
| TxGNN-förutsägelsepoäng | 99,95 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 1 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för denna rapport. Enligt farmakologidata hämmar metyrapon CYP11B1 (11-beta-hydroxylas) och CYP11B2, vilket minskar bildningen av kortisol i binjurarna.

Sambandet mellan den ursprungliga användningen och den nya indikationen är svagt. Malign hypertermi är en störning i skelettmuskelns kalciumhantering, kopplad till generna RYR1 och CACNA1S, och har ingen känd koppling till binjurarnas steroidsyntes. Den höga poängen speglar sannolikt närheten mellan relaterade muskelsjukdomar i kunskapsgrafen snarare än en farmakologisk motivering.

Vi bedömer därför att förutsägelsen inte är mekanistiskt rimlig i nuläget. Standardbehandlingen vid malign hypertermi är dantrolen, som verkar direkt på kalciumfrisättningen i muskeln.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande för den högst rankade indikationen.

För fullständighetens skull: bland de lägre rankade förutsägelserna finns en enda publikation, kopplad till **familjär periodisk förlamning** (rank 8):

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Fysiologisk/mekanistisk studie (liten human studie) | The Journal of Clinical Investigation | Hos en 19-årig man med hyperkalemisk periodisk förlamning utlöstes attacker av kaliumklorid, kortikotropin och glukokortikoider, men inte av mineralokortikoider eller av ACTH i kombination med metyrapon. Metyrapon användes som ett fysiologiskt verktyg, inte som behandling. |

Denna studie visar inte att metyrapon behandlar sjukdomen. Sammandraget i underlaget är dessutom avkortat.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 49271 (indraget) | Metopirone | Kapsel, mjuk | Ingen indikationstext angiven |

Tillverkare: Esteve Pharmaceuticals S.A.

---

## Cytotoxicitet

Metyrapon är inte ett cytotoxiskt cancerläkemedel utan en steroidsynteshämmare, och därför redovisas ingen cytotoxicitetssektion.

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (ej hämtade från produktresumén): sjukdomar med nedsatt binjurefunktion, vilket är logiskt eftersom metyrapon minskar kortisolbildningen:
  - Addisons sjukdom
  - Kronisk primär binjurebarksinsufficiens
  - Binjurebarksinsufficiens
  - Medfödd binjurebarkshyperplasi
  - Familjär glukokortikoidbrist
  - X-bunden medfödd binjurehypoplasi
  - Familjär binjurehypoplasi med avsaknad av luteiniserande hormon från hypofysen
  - Ärftlig isolerad binjurebarksinsufficiens vid partiell CYP11A1-brist
- **Läkemedelsinteraktioner** (12 identifierade):
  - Måttlig interaktionsnivå med östrogener: etinylestradiol, estradiol, konjugerade östrogener, mestranol, förestrade östrogener, estronsulfat (även topikala former av estradiol, konjugerade östrogener och estronsulfat)
  - Måttlig interaktionsnivå med cyproheptadin
  - Farmakologisk målpåverkan på CYP11B1 och CYP11B2

Se produktresumén för fullständig säkerhetsinformation om varningar och kontraindikationer, då dessa uppgifter saknas i underlaget.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellberäkning (L5) utan kliniska prövningar eller publikationer, och det saknas en rimlig mekanistisk koppling mellan CYP11B1-hämning och störd kalciumhantering i muskeln.
- Samtliga tio förutsagda indikationer saknar stöd för behandlingseffekt. Den enda publikationen (familjär periodisk förlamning, 1971) beskriver metyrapon som ett fysiologiskt verktyg, inte som behandling. Dessutom är det enda svenska godkännandet indraget.

**För att gå vidare krävs:**
- Hämtning av produktresumé från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket för närvarande är ett blockerande datagap
- Komplettering av verkningsmekanismdata från DrugBank
- Ett tydligt prekliniskt eller mekanistiskt underlag som kopplar steroidsyntes till kalciumhomeostas i skelettmuskel
- Bedömning av om andra, mer relevanta indikationer inom endokrinologi bör prioriteras framför den förutsagda muskelsjukdomen
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

