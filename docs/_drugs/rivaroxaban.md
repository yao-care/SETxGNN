---
layout: default
title: Rivaroxaban
parent: Endast modellprediktion (L5)
nav_order: 383
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
description: "Rivaroxaban: predikterad ny indikation Reumatoid artrit (rheumatoid arthritis) (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Rivaroxaban
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

## Rivaroxaban: Reumatoid artrit (rheumatoid arthritis)
{: .text-alpha }

---

## Sammanfattning

Rivaroxaban är en direkt hämmare av koagulationsfaktor Xa och används som blodförtunnande läkemedel. Den ursprungliga godkända indikationstexten finns inte i de data som sammanställts för denna rapport. TxGNN-modellen förutsäger att rivaroxaban kan vara effektivt mot **reumatoid artrit**, men det finns **inga kliniska prövningar** och endast **4 publikationer** (översikter, en kohortstudie och en fallrapport) som inte visar att läkemedlet behandlar sjukdomen. Förutsägelsen bygger i praktiken enbart på modellen.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Reumatoid artrit (rheumatoid arthritis) |
| TxGNN-förutsägelsepoäng | 0.9957 |
| Evidensnivå | L5 (endast modellförutsägelse, inga relevanta studier av effekt) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: minst 20) |
| Antal godkännanden | 20 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda data. Baserat på känd information är rivaroxaban en direkt hämmare av faktor Xa, ett centralt enzym i blodets koagulationskaskad. Läkemedlet förebygger och behandlar blodproppar.

Kopplingen till reumatoid artrit är svag och indirekt. Vid autoimmun inflammation förändras koagulationsaktiveringen och trombinbildningen, och personer med reumatoid artrit har en förhöjd risk för venös tromboembolism. Det skulle i teorin kunna finnas ett samband via inflammatorisk signalering som styrs av proteasaktiverade receptorer (PAR).

Det är dock spekulativt. Inga data visar att rivaroxaban påverkar sjukdomsaktiviteten vid reumatoid artrit. Den höga modellpoängen ska därför inte tolkas som stöd för effekt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Översikt | JAMA | Översikt om diagnos och behandling av venös tromboembolism i benen. Ingen koppling till reumatoid artrit som behandlingsmål. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Översikt | La Revue de médecine interne | Trombinbildningstest vid autoimmuna sjukdomar. Visar förändrad koagulation, men inte effekt av rivaroxaban. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Kohortstudie | PLoS ONE | Jämför följsamhet till rivaroxaban och apixaban vid förmaksflimmer. Inte relevant för reumatoid artrit. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Fallrapport | Cureus | Patient med reumatoid artrit (behandlad med orala steroider) och upprepade embolier trots antikoagulation. Beskriver samsjuklighet, inte behandling av artrit. |

---

## Marknadsinformation Sverige

Indikationstexter saknas i de sammanställda data. De första fem godkännandena:

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 59431 | Rivaroxaban Avansor | Filmdragerad tablett | Ej angiven |
| 62033 | Rivaroxaban STADA Arzneimittel AG | Filmdragerad tablett | Ej angiven |
| 59153 | Rivaroxaban Krka | Filmdragerad tablett | Ej angiven |
| 62327 | Blomensy | Filmdragerad tablett | Ej angiven |
| 61502 | Rivaroxaban Hexal | Filmdragerad tablett | Ej angiven |

---

## Säkerhetsaspekter

- **Sjukdomar kopplade till läkemedlet i kunskapsgrafen** (ej från produktresumétext): leversvikt, njursjukdom, pyoureter, leversjukdom, gallblåsesjukdom och blodkoagulationssjukdom. Dessa bör betraktas som signaler som måste verifieras mot produktresumén.
- **Läkemedelsinteraktioner**: 100 interaktioner identifierade. Bland de som listats är följande klassade som **allvarliga (Major)**:
  - acetylsalicylsyra
  - kobicistat
  - deferasirox
  - ibritumomab tiuxetan
  - tositumomab (I-131)

  Flera **måttliga (Moderate)** interaktioner finns också, bland annat med aprepitant, dexametason, cimetidin, klaritromycin, mikonazol och klotrimazol.
- Litteraturen visar dessutom att CYP3A4- och P-gp-hämmare, till exempel ritonavir och kobicistat, kan höja rivaroxabankoncentrationen och öka blödningsrisken.

Se produktresumén för fullständiga varningar och kontraindikationer, eftersom dessa inte fanns tillgängliga i de sammanställda data.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen är endast modellbaserad (L5) utan kliniska prövningar, och den tillgängliga litteraturen visar ingen terapeutisk effekt vid reumatoid artrit. Dessutom saknas giltiga godkännanden i Sverige och produktresumédata om varningar och kontraindikationer.

**För att gå vidare krävs:**
- Hämta produktresumé från Läkemedelsverket och komplettera varningar, kontraindikationer och godkända indikationer.
- Komplettera verkningsmekanismdata, till exempel via DrugBank.
- Genomföra en systematisk litteratursökning efter prekliniska och kliniska data om faktor Xa-hämning eller PAR-signalering vid reumatoid artrit.
- Fastställa om det finns en rimlig mekanistisk hypotes innan någon prövning planeras.
- Klargöra marknadsstatusen, eftersom alla godkännanden är indragna.

---

*Övriga förutsägelser i data (gikt, hiv-infektion, brakydaktyli-syndaktylisyndrom) har likaså endast evidensnivå L4–L5, saknar stöd för terapeutisk effekt och rekommenderas inte för vidare utvärdering i nuläget.*
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

