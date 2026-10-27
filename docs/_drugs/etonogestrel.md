---
layout: default
title: Etonogestrel
parent: Endast modellprediktion (L5)
nav_order: 181
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Etonogestrel: predikterad ny indikation Amenorré (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga data"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
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

## Etonogestrel: Från ej angiven indikation till amenorré
{: .text-alpha }

---

### Sammanfattning

Etonogestrel är ett gestagen (progestin) som i Sverige har funnits i preventivmedelsprodukter som implantat och vaginalinlägg. Någon godkänd indikationstext finns dock inte i de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **amenorré** med mycket hög modellpoäng, men det finns **inga kliniska prövningar** och endast **1 publikation** som inte är relevant för frågeställningen. Förutsägelsen bygger därmed enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga data |
| Förutsagd ny indikation | Amenorré |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 3 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Det är allmänt känt att etonogestrel är ett gestagen som hämmar ägglossning och gör slemhinnan i livmodern tunnare. Det är dessa effekter som gör att blödningarna ofta uppträder oregelbundet eller uteblir.

Här finns en viktig brasklapp: amenorré är en välkänd biverkan av etonogestrelimplantat och inte en sjukdom som behandlas. Att framkalla amenorré kan vara ett behandlingsmål vid till exempel kraftiga menstruationsblödningar eller endometrios, men det stöds inte av data i detta underlag. Den höga modellpoängen (0,998) är därför en förutsägelse och inte ett belägg för nytta.

Modellen pekar även på godartade bröstförändringar (fibrocystisk bröstsjukdom, "blunt duct adenosis", apokrin adenos och benign mammär dysplasi). Sambandet antas bero på gemensamma hormonella signalvägar. Det finns ingen etonogestrelspecifik evidens, och gestagenets effekter på bröstvävnad är dessutom blandade när det gäller bröstsäkerhet.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT-protokoll (ej relevant) | Trials | Studieprotokoll om BIO101 för att förebygga andningsförsämring vid covid-19-pneumoni. Handlar inte om etonogestrel eller amenorré. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 14924 | Nexplanon | Implantat | Ej angiven (avregistrerad) |
| 17179 | NuvaRing | Vaginalinlägg | Ej angiven (avregistrerad) |
| 54511 | Ornibel | Vaginalinlägg | Ej angiven (avregistrerad) |

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (härledda från TxGNN:s kunskapsgraf, inte från produkttext): sjukdomar som kan vara relevanta att beakta är bland annat högt blodtryck, epilepsi, lever- och njursjukdom, gallblåsesjukdom, porfyri, systemisk lupus erytematosus, astma, diabetes (inklusive ketoacidos), förhöjda blodfetter, bröstcancer, tromboflebit, migrän, kranskärlssjukdom, fetma samt ångest- och nervösa tillstånd.
- **Läkemedelsinteraktioner**: totalt 100 interaktioner har identifierats, alla av grad måttlig i de listade exemplen. De viktigaste grupperna är:
  - Diabetesläkemedel: akarbos, metformin, glimepirid, klorpropamid, kanagliflozin, dapagliflozin, empagliflozin, alogliptin, saxagliptin, albiglutid, dulaglutid, semaglutid samt flera insuliner (aspart, degludek, detemir, glargin, glulisin)
  - Aprepitant
  - Klaritromycin
  - Linaklotid

Varnings- och kontraindikationstext från produktresumén saknas. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellen (evidensnivå L5). Amenorré är en känd biverkan snarare än en behandlingsbar sjukdom, och inga kliniska prövningar eller relevant litteratur finns. Dessutom är alla svenska godkännanden avregistrerade.

**För att gå vidare krävs:**
- Att först definiera en kliniskt meningsfull indikation, till exempel kraftiga blödningar eller endometrios, där amenorré är ett behandlingsmål.
- Verkningsmekanismdata från DrugBank.
- Varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA), vilket är en förutsättning för säkerhetsgranskning.
- Relevanta kliniska prövningar och litteratur som specifikt rör etonogestrel för den valda indikationen.
- En bedömning av beredningsform och administreringsväg, som ännu inte är gjord.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

