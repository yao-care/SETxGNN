---
layout: default
title: Dobutamine
parent: Endast modellprediktion (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dobutamine: predikterad ny indikation Alopeci (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga godkännandedata"
monitor_inn: "dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
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

# Dobutamin: Från ej angiven ursprunglig indikation till alopeci

---

### Sammanfattning

Dobutamin (dobutamin) är en betaadrenerg inotrop substans som ges som intravenös infusion. De svenska godkännandena är båda avregistrerade och saknar angiven indikationstext i de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att dobutamin kan vara effektivt mot **alopeci**, men det finns **inga kliniska prövningar** och endast **en publikation** (en veterinär fallrapport om minoxidilförgiftning hos en katt, där dobutamin användes vid lågt blodtryck), som inte stöder en behandlingseffekt. Förutsägelsen bygger i praktiken enbart på modellen.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga godkännandedata |
| Förutsagd ny indikation | Alopeci |
| TxGNN-förutsägelsepoäng | 99,85 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 2 (båda avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts. Det är känt att dobutamin är en beta-1-adrenerg agonist som ökar hjärtats kontraktionskraft och används vid akut hjärtsvikt och som stöd av hjärtfunktionen. Någon tydlig koppling till hårfollikelbiologi finns inte.

Den höga poängen beror sannolikt på att dobutamin ligger nära minoxidil i modellens kunskapsgraf. Minoxidil är ett kärlvidgande läkemedel med hårväxtfrämjande effekt och hjärttoxicitet. Det är alltså närhet i nätverket, inte en gemensam mekanism, som driver förutsägelsen. Den enda funna publikationen beskriver just minoxidilförgiftning hos en katt, där dobutamin användes för att behandla lågt blodtryck, och visar ingen effekt på hårväxt.

Övriga förutsägelser pekar åt samma håll: hereditära och autoimmuna håravfallstillstånd (hypotrichosis simplex i hårbotten, medfödd hypotrichosis milia, diffus alopecia areata), glaukom, Raynauds sjukdom, huvudvärk och migrän, samt hypertrichos. Ingen av dem har någon rimlig mekanistisk förklaring. Hypertrichos är dessutom motsatsen till alopeci. Glaukom och Raynauds sjukdom har endast spekulativa samband.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Fallrapport (veterinär) | Journal of Veterinary Cardiology | En katt med hjärtsvikt orsakad av minoxidilförgiftning behandlades bland annat med dobutamin mot lågt blodtryck. Ingen effekt på håravfall beskrivs. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 22330 (avregistrerad) | Dobutamin Hameln | Koncentrat till infusionsvätska, lösning | Ej angiven |
| 65838 (avregistrerad) | Dobutamine Panpharma | Koncentrat till infusionsvätska, lösning | Ej angiven |

---

### Säkerhetsaspekter

- **Möjliga kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): högt blodtryck, kaliumbrist, förmaksflimmer, aortastenos (inklusive aortaklaffsjukdom och supravalvulär aortastenos), hjärtinfarkt och kranskärlstrombos, hemoglobinopati samt hypertrofisk kardiomyopati (inklusive familjär form).
- **Läkemedelsinteraktioner**: totalt 101 interaktioner identifierade. De som visas är alla av måttlig allvarlighetsgrad och gäller bland annat:
  - Diabetesläkemedel: acarbose, metformin, pioglitazon, repaglinid, kanagliflozin, dapagliflozin, empagliflozin, alogliptin, linagliptin, kloropropamid, insulin aspart, insulin degludec samt GLP-1-agonister (albiglutid, dulaglutid, liraglutid, semaglutid)
  - Cimetidin och vankomycin
  - Aptitdämpande medel: fentermin och dietylpropion

Se produktresumén för fullständig säkerhetsinformation om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar både kliniskt och mekanistiskt stöd (evidensnivå L5). Den höga poängen speglar sannolikt närhet till minoxidil i kunskapsgrafen, och dobutamin har dessutom en betydande kardiovaskulär riskprofil.

**För att gå vidare krävs:**
- Hämta verkningsmekanism från DrugBank och bedöm om det finns någon biologisk koppling till hårfollikeln.
- Hämta varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA). Detta är en blockerande datalucka.
- Klargöra den ursprungliga godkända indikationen, som saknas i godkännandedata.
- Genomföra prekliniska studier (till exempel i hårfollikelmodeller) innan kliniska studier övervägs.
- Notera att båda godkännandena är avregistrerade, vilket innebär att ingen produkt för närvarande finns på den svenska marknaden.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

