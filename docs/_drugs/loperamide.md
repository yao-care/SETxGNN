---
layout: default
title: Loperamide
parent: Endast modellprediktion (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Loperamide: predikterad ny indikation Akut smittsam konjunktivit (evidensnivå L5). Ursprunglig indikation: Diarrésjukdom och dysenteri (enligt kunskapsgrafen"
monitor_inn: "loperamide"
predicted_indications: ["acute contagious conjunctivitis", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

# Loperamid: Från diarrésjukdom och dysenteri till akut smittsam konjunktivit

---

## Sammanfattning

Loperamid är ett symtomlindrande läkemedel mot diarré som ursprungligen användes vid diarrésjukdom och dysenteri. TxGNN-modellen förutsäger att det kan vara effektivt mot **akut smittsam konjunktivit** med mycket hög modellpoäng (99,97 %), men för denna indikation finns **inga kliniska prövningar och ingen publicerad litteratur**. Förutsägelsen bygger enbart på modellen. Bland de tio främsta förutsägelserna finns dessutom endast publikationer som pekar på **risker** (fallrapporter om toxisk megakolon och andningsdepression), inte på nytta.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Diarrésjukdom och dysenteri (enligt kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Akut smittsam konjunktivit |
| TxGNN-förutsägelsepoäng | 99,97 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 15 (alla indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de data som sammanställts för denna rapport. Det som är allmänt känt är att loperamid verkar som agonist på perifera my-opioidreceptorer i tarmens nervplexa, vilket minskar tarmens rörlighet och sekretion. Därför lindrar det diarré, men det behandlar inte orsaken till den.

Något rimligt samband med ögonens bindhinna har inte kunnat identifieras. Opioidsignalering finns på ögats yta, men inget kopplar den till infektiös konjunktivit. Loperamid saknar känd antiinfektiös eller antiinflammatorisk effekt på bindhinnan. Den höga poängen speglar sannolikt att modellen placerar sjukdomen nära infektions- och diarrénoder i kunskapsgrafen, inte läkemedelsspecifik biologi. Flera närliggande konjunktivittermer har dessutom exakt samma poäng (0,99648), vilket tyder på en artefakt från sjukdomsontologin.

Av samma skäl bedöms de andra konjunktivitrelaterade förutsägelserna (konjunktivit, pseudomembranös konjunktivit, kronisk follikulär konjunktivit, konjunktival folliculos, serös konjunktivit utom viral, parasitär konjunktivit och Angeluccis syndrom) sakna stöd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen litteratur finns för den främsta förutsägelsen (akut smittsam konjunktivit). Nedan redovisas den litteratur som finns för andra högt rankade förutsägelser. Den belyser främst säkerhetsrisker.

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Fallrapport | Journal of Travel Medicine | Fulminant amöbakolit med toxisk megakolon hos en patient med omfattande loperamidanvändning. Förloppet kan ha påverkats av loperamiden (förutsägelse: amöbadysenteri). |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Översikt | The American Journal of Medicine | Översikt av icke-vätskebaserad behandling av akut diarré. Beskriver symtomlindrande medel generellt, inte loperamid som behandling av amöbadysenteri. |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Fallrapport | Cureus | Loperamidutlöst andningsdepression vid svår mag-tarminflammation efter cytostatika. Inflammerad tarmslemhinna kan öka systemupptaget (förutsägelse: gastroduodenit). |

---

## Marknadsinformation Sverige

Alla 15 godkännanden är indragna och inget är giltigt. De fem första visas nedan. Indikationstext finns inte registrerad.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 43239 | Lopacut | Filmdragerad tablett | Ej angiven |
| 62733 | Loperamide Grindeks | Kapsel, hård | Ej angiven |
| 23069 | Imodium | Munsönderfallande tablett | Ej angiven |
| 12443 | Dimor | Filmdragerad tablett | Ej angiven |
| 56394 | Loperamid Brown | Kapsel, hård | Ej angiven |

---

## Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumé): leversjukdom, gallblåsesjukdom, paralytisk ileus, tarmobstruktion, familjär visceral myopati samt dysenteri, diarrésjukdom, infektiös diarrésjukdom och infektiös tarmsjukdom.
- **Signaler från litteraturen:**
  - Antimotilitetsmedel vid invasiv amöbakolit kan bidra till toxisk megakolon och fulminant sjukdom.
  - Vid svår tarminflammation kan systemupptaget öka, med risk för central opioideffekt såsom andningsdepression.
- **Läkemedelsinteraktioner:** 591 interaktioner registrerade. Exempel på allvarliga (Major): abirateron, ranitidin, fosamprenavir och gemfibrozil. Exempel på måttliga (Moderate): kodein, dihydrokodein, tramadol, etanol, cetirizin, klorfeniramin, galantamin och salbutamol.

Varningar och kontraindikationer från produktresumén saknas i underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den högt rankade förutsägelsen (akut smittsam konjunktivit) saknar både mekanistiskt stöd och kliniska data, och poängen verkar bero på ontologiartefakter. Den begränsade litteraturen för övriga förutsägelser pekar på skaderisker snarare än nytta.

**För att gå vidare krävs:**
- Hämta och analysera produktresumé för varningar och kontraindikationer, eftersom detta är ett blockerande datagap.
- Komplettera verkningsmekanismdata från DrugBank.
- Visa ett biologiskt samband mellan perifer my-opioidagonism och bindhinneinflammation eller infektion, till exempel genom prekliniska studier.
- Klargöra beredningsform och administreringsväg, eftersom de nuvarande godkännandena endast avser orala former.
- Notera att samtliga svenska godkännanden är indragna, vilket i sig är ett regulatoriskt hinder.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

