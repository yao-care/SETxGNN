---
layout: default
title: Dimenhydrinate
parent: Endast modellprediktion (L5)
nav_order: 142
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Dimenhydrinate: predikterad ny indikation Allergisk urtikaria (evidensnivå L5). Ursprunglig indikation: Yrsel av centralnervöst ursprung och åksjuka (enligt kunskapsgrafen"
monitor_inn: "dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
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

## Dimenhydrinat: Från yrsel av centralnervöst ursprung och åksjuka till allergisk urtikaria
{: .text-alpha }

---

### Sammanfattning

Dimenhydrinat används ursprungligen mot yrsel av centralnervöst ursprung och åksjuka. TxGNN-modellen förutsäger att det kan vara effektivt mot **allergisk urtikaria**, med **0 kliniska prövningar** och **1 publikation** (en farmakokinetisk pilotstudie på hund) som för närvarande stöder denna riktning. Evidensen är därmed mycket begränsad och bygger i huvudsak på modellens förutsägelse och en känd läkemedelsklasseffekt.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Yrsel av centralnervöst ursprung och åksjuka (enligt kunskapsgrafen; godkänd indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Allergisk urtikaria |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L4 (endast prekliniskt/farmakokinetiskt stöd) |
| Marknadsstatus i Sverige | Endast återkallade godkännanden |
| Antal godkännanden | 5 (alla avregistrerade) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det sammanställda underlaget. Baserat på känd information är dimenhydrinat ett salt av difenhydramin och 8-klorteofyllin. Difenhydramin är en första generationens H1-receptorantagonist.

Vid allergisk urtikaria frisätts histamin från mastceller och orsakar kläda, kvaddlar och rodnad. När difenhydramin frigörs efter intag blockerar det H1-receptorer och kan därmed lindra histamindrivna symtom. Mekanistiskt är det alltså rimligt att dimenhydrinat kan vara tillämpbart, även om den ursprungliga användningen mot yrsel och åksjuka bygger på en annan effekt (främst i det centrala nervsystemet).

Samma resonemang gäller för den näst högst rankade förutsägelsen, **kölduurtikaria** (poäng 99,2 %), där mastcellsdegranulering och histamin också spelar en central roll. Där finns dock ingen klinisk eller litterär evidens alls (evidensnivå L5).

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Farmakokinetisk pilotstudie (hund) | Veterinary Dermatology | Jämförde upptag av difenhydramin efter oral och intravenös dosering samt efter oralt dimenhydrinat hos friska hundar, och effekten på histaminframkallade kvaddlar. Dimenhydrinat har beskrivits ge bättre oralt upptag av difenhydramin. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 19880 | Calma | Medicinskt tuggummi | Ingen indikationstext angiven (avregistrerad) |
| 62058 | Cinnarizin/Dimenhydrinat Ebb | Tablett | Ingen indikationstext angiven (avregistrerad) |
| 54243 | Arlevert | Tablett | Ingen indikationstext angiven (avregistrerad) |
| 24919 | Arlevert | Tablett | Ingen indikationstext angiven (avregistrerad) |
| 57574 | Azalonum | Tablett | Ingen indikationstext angiven (avregistrerad) |

---

### Säkerhetsaspekter

- **Sjukdomar där läkemedlet enligt kunskapsgrafen är kontraindicerat** (inte hämtat från produkttext): bland annat högt blodtryck, lågt blodtryck, leversjukdom, gallblåsesjukdom, trombocytopeni, störd blodkoagulation, diabetes och diabetesketoacidos, hyperglykemi, magsår, godartad prostataförstoring, blåshalsobstruktion, gikt, substansmissbruk/beroende, hjärt-kärlsjukdom (akut kranskärlssyndrom, kranskärlssjukdom, hjärtinfarkt, koronar trombos), hemoglobinopati, okulär hypertension, trångvinkelglaukom, pylorusstenos, hypertyreos (Graves sjukdom, tyreotoxikos) och hypofosfatemi.
- **Läkemedelsinteraktioner**: totalt 67 interaktioner identifierade. De allvarligaste (grad Major) är:
  - Kaliumcitrat
  - Kaliumklorid
- Bland interaktionerna av måttlig grad finns flera antikolinerga läkemedel (hyoscyamin, atropin, skopolamin, glykopyrronium, dicyklomin, trospium, propantelin m.fl.) samt opioider (morfin, opium), loperamid, metoklopramid, prukaloprid, eluxadolin och nabilon.

Produktresumé med varningar och kontraindikationer saknas i det sammanställda underlaget. Se produktresumén för fullständig säkerhetsinformation.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den höga modellpoängen (99,7 %) stämmer med läkemedelsklassens kända effekt, men det finns inga kliniska prövningar och endast en farmakokinetisk djurstudie. Dessutom är alla svenska godkännanden avregistrerade.

**För att gå vidare krävs:**
- Kliniska data på människa för dimenhydrinat (eller difenhydramin) vid allergisk urtikaria
- Produktresumé med varningar och kontraindikationer från Läkemedelsverket (MPA)
- Detaljerad verkningsmekanismdata från DrugBank
- Bedömning av nyttan jämfört med nyare, mindre sederande antihistaminer, som redan är standardbehandling vid urtikaria
- Utredning av vilken beredningsform och administreringsväg som skulle kunna användas, eftersom inga aktiva godkännanden finns kvar
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

