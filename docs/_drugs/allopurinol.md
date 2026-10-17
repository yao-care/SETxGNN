---
layout: default
title: Allopurinol
parent: Endast modellprediktion (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Allopurinol: predikterad ny indikation Hepatisk porfyri (evidensnivå L5). Ursprunglig indikation: Gikt, hyperurikemi, akut uratnefropati (enligt kunskapsgrafen"
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

# Allopurinol: Från gikt till hepatisk porfyri

---

### Sammanfattning

Allopurinol är en xantinoxidashämmare som ursprungligen används för att behandla **gikt**, hyperurikemi och akut uratnefropati. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **hepatisk porfyri**, men förutsägelsen bygger enbart på en beräkningsmodell: det finns **0 kliniska prövningar** och endast **2 publikationer** (en hypotesartikel och en djurstudie), varav ingen visar klinisk nytta av allopurinol vid porfyri.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Gikt, hyperurikemi, akut uratnefropati (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Hepatisk porfyri |
| TxGNN-förutsägelsepoäng | 99,95 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast avregistrerade godkännanden |
| Antal godkännanden | 16 |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Allopurinol är känt som en hämmare av xantinoxidas, som minskar bildningen av urinsyra. Dess effekt vid gikt är väl belagd, men ett mekanistiskt samband med hepatisk porfyri är inte stött av underlaget.

Det underlag som hämtats pekar snarare åt motsatt håll. Allopurinol har rapporterats påverka hepatisk hemmetabolism, bland annat genom nedbrytning av hem i cytokrom P450 och inducering av 5-aminolevulinatsyntas (ALAS1). I princip kan detta förvärra snarare än lindra porfyri. Den högt rankade modellpoängen ska därför ses som ett beräkningsresultat, och effektens riktning är osäker och möjligen skadlig.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Översikt (hypotes) | Medical hypotheses | Föreslår metabolisk påverkan på ALAS1 via tryptofan och hämning av hemanvändning via tryptofan-2,3-dioxygenas som möjlig behandling av akut hepatisk porfyri. Behandlar inte allopurinol kliniskt. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Djurstudie | Biochemical pharmacology | Karbamazepin i mycket låg dos förvärrade hemförlust i råttlever, vilket belyser hur läkemedel kan utlösa porfyri. Handlar inte om allopurinol. |

---

### Marknadsinformation Sverige

Alla 16 godkännanden är avregistrerade och inga är giltiga. Indikationstext saknas i underlaget. Nedan visas fem av dem.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 9845 | Allopurinol Orifarm | Tablett | – |
| 56976 | Allopurinol Accord | Tablett | – |
| 11291 | Allopurinol Nordic Drugs | Tablett | – |
| 53057 | Allopurinol Sandoz | Tablett | – |
| 41980 | Allopurinol Teva | Tablett | – |

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): leversjukdom, gallblåsesjukdom, nedsatt njurfunktion, överkänslighetsvaskulit, kutan leukocytoklastisk angiit, allergisk kutan vaskulit samt anti-GBM-sjukdom.
- **Läkemedelsinteraktioner**: totalt 100 interaktioner identifierades. Av de som visas är följande klassade som måttliga: aluminiumhydroxid, attapulgit, kaolin, magaldrat och sukralfat (antacida och adsorbenter kan minska upptaget). Amoxicillin och klorpropamid klassas som mindre. Övriga visade interaktioner, bland annat metformin, omeprazol, pantoprazol, morfin och doxycyklin, har okänd allvarlighetsgrad.
- Allopurinol är känt för överkänslighetsreaktioner (t.ex. DRESS) och har enstaka fallrapporter om myopati, vilket är relevant för säkerhetsbedömning vid nya indikationer.

Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensen är på nivå L5: det finns endast en modellförutsägelse, inga kliniska prövningar och ingen litteratur som stöder allopurinol vid hepatisk porfyri. Dessutom tyder känd påverkan på hemmetabolismen på att läkemedlet kan förvärra sjukdomen.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata (t.ex. via DrugBank) och produktresumé med varningar och kontraindikationer från Läkemedelsverket.
- Gör en systematisk genomgång av om allopurinol anses säkert eller porfyrogent vid akut hepatisk porfyri.
- Genomför prekliniska studier av allopurinols effekt på ALAS1 och hemmetabolism innan kliniska studier övervägs.
- Notera att alla svenska godkännanden är avregistrerade, vilket påverkar en eventuell framtida utveckling.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

