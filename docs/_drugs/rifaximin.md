---
layout: default
title: Rifaximin
parent: Endast modellprediktion (L5)
nav_order: 379
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "RIFAXIMIN"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
description: "Rifaximin: predikterad ny indikation Oral candidiasis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Rifaximin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

## Rifaximin: Oral candidiasis
{: .text-alpha }

---

### Sammanfattning

Rifaximin är ett icke-absorberbart antibiotikum som verkar i tarmen och som ursprungligen användes vid hepatisk encefalopati (leverkoma). TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **oral candidiasis**, men det finns **inga kliniska prövningar** och endast **1 publikation** som berör ämnet. Den publikationen pekar dessutom på en risk snarare än en nytta: rifaximinanvändning var kopplad till svampinfektioner med resistenta Candida-arter.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Oral candidiasis |
| TxGNN-förutsägelsepoäng | 0.9975 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 3 av 3) |
| Antal godkännanden | 3 (giltiga: 3) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är rifaximin ett antibakteriellt läkemedel som knappt tas upp från tarmen och som påverkar tarmens bakterieflora. Dess effekt vid hepatisk encefalopati bygger på denna lokala verkan i tarmen.

Det finns dock ingen etablerad antisvampsmekanism som skulle förklara effekt mot oral candidiasis. Den enda tillgängliga publikationen (PMID 34180023) tyder på motsatsen: antibiotikapåverkan på tarmfloran kan gynna överväxt av Candida. Den höga modellpoängen stöds alltså inte av kliniska data och kan spegla likheter som TxGNN-modellen (djupinlärning) har lärt sig mellan relaterade sjukdomar, inte biologisk evidens.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Kohortstudie | Annals of Hematology | Hos patienter som genomgått allogen stamcellstransplantation var rifaximinanvändning kopplad till infektioner med micafunginresistenta Candida-arter. Det tyder på en risk, inte på behandlingsnytta. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 66409 | Xifaxan (Medartuum AB) | Filmdragerad tablett | Indragen |
| 46905 | Xifaxan (Norgine BV) | Filmdragerad tablett | Indragen |
| 68417 | Xifaxan (2care4 ApS) | Filmdragerad tablett | Indragen |

Alla tre godkännanden är indragna, och ingen indikationstext finns tillgänglig.

---

### Säkerhetsaspekter

- **Kontraindikationer enligt kunskapsgrafen** (inte hämtade från produktresumén): Clostridium difficile-kolit och nekrotiserande enterokolit hos nyfödda.
- **Läkemedelsinteraktioner**: Totalt 69 interaktioner identifierades. Bland de viktigaste:
  - **Allvarlig (Major)**: levande koleravaccin (Vibrio cholerae CVD 103-HgR)
  - **Måttlig (Moderate)**: ciklosporin, warfarin, tolvaptan, daklatasvir, ledipasvir, pikosulfat, kabozantinib, apalutamid, darolutamid, enkorafenib
- **Säkerhetssignal**: Observationsdata kopplar rifaximin till Candida-infektioner med resistens mot micafungin (se PMID 34180023). Candidemi är dessutom en känd risk hos patienter med levercirros (PMID 32360775), en grupp som ofta behandlas med rifaximin.

Se produktresumén för fullständig information om varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen saknar stöd i kliniska prövningar, och den enda relevanta publikationen visar en möjlig risk för Candida-infektion i stället för nytta. Mekanistiskt finns inget som talar för antisvampseffekt.

**För att gå vidare krävs:**
- Hämta verkningsmekanismdata från DrugBank för en ordentlig mekanistisk analys.
- Hämta varningar och kontraindikationer ur produktresumén från Läkemedelsverket (MPA), eftersom detta blockerar säkerhetsgranskningen.
- Prekliniska data (till exempel in vitro-test mot Candida) och kontrollerade studier som kan visa om det finns någon nytta alls.
- Utvärdering av om rifaximins påverkan på tarmfloran ökar risken för candidiasis.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

