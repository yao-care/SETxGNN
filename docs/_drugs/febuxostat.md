---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

Använder **txgnn-pipeline**-skillet för att säkerställa korrekt rapportformat för Sverige-versionen (SeTxGNN).

---

# Febuxostat: Från hyperurikemi och gikt till renal hypourikemi

## Sammanfattning

Febuxostat är ett uratänkande läkemedel som internationellt används för behandling av kronisk hyperurikemi vid gikt. TxGNN-modellen förutsäger att det kan vara effektivt mot **renal hypourikemi**, en njurrelaterad störning i uratsyraömsättningen som kännetecknas av onormalt låga serumurathalter och ökad ursutsöndring. Evidensunderlaget för denna nya indikation är begränsat – det stöds av **1 klinisk prövning** (fas 4, okänd status) och **2 publikationer**, varav en fallrapport direkt beskriver febuxostats potentiella roll.

---

## Snabböversikt

| Post | Innehåll |
|---|---|
| Ursprunglig indikation | Hyperurikemi vid gikt (ej registrerat i Sverige) |
| Förutsagd ny indikation | Renal hypourikemi |
| TxGNN-förutsägelsepoäng | 99,99% |
| Evidensnivå | L4 – Fallrapport och narrativ översikt |
| Marknadsstatus i Sverige | Ej godkänt (0 registreringar) |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta Evidence Pack. Baserat på känd information är Febuxostat en selektiv icke-purin-hämmare av xantinoxidasreduktaset (XOR) – ett enzym som katalyserar oxidationen av hypoxantin till xantin och vidare till urinsyra. Dess förmåga att sänka serumuratnivåer vid hyperurikemi och gikt är väldokumenterad internationellt.

Kopplingen till renal hypourikemi är mekanistiskt intressant men paradoxal: tillståndet orsakas av defekter i njurtubulernas uratetransport (exempelvis URAT1-mutationer), vilket leder till onormalt låga serumurathalter och kraftigt ökad ursutsöndring. Denna höga uratkoncentration i njurtubulerna kan vid anaerob belastning utlösa träningsinducerad akut njurskada (EIAKI) via oxidativ stress. Litteraturen (PMID 36754409) tyder på att XOR-hämning med Febuxostat kan minska produktionen av fria syreradikaler i njurvävnaden och därigenom förebygga EIAKI – ett välkänt och allvarligt komplikation vid renal hypourikemi.

Titeln på PMID 36754409 namnger uttryckligen "Non-purine Selective Xanthine Oxidoreductase Inhibitors" i samband med renal hypourikemi, vilket ger en direkt mekanistisk grund för TxGNN:s förutsägelse. Det rör sig dock om ett enstaka fallrapport, och den kliniska generaliserbarheten är ännu oklar.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---|---|---|---|---|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fas 4 | Okänd | 100 | Prospektiv kontrollerad studie vid Shanghai Xu-hui Central Hospital. Undersöker hur uratkontroll påverkar återfall av njursten och njurfunktion hos patienter med hyperurikemi och njursten. Stöder indirekt relevansen av uratkontroll vid njurrelaterade tillstånd. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|---|---|---|---|---|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Fallrapport | Internal Medicine (Tokyo) | Beskriver en 16-årig fotbollsspelare med familjär renal hypourikemi (URAT1-mutation) och återkommande EIAKI. Febuxostat diskuteras som profylaktisk behandling när hydreringsåtgärder visat sig otillräckliga. Starkaste direkta evidens för förutsägelseriktningen. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrativ översikt | Clinical Rheumatology | Uppdatering om hypourikemi (serumurat <2 mg/dL) för reumatologer med genomgång av etiologi, inklusive renal hypourikemi. Ger kliniskt sammanhang men är inte specifik för Febuxostat. |

---

## Marknadsinformation Sverige

Febuxostat är för närvarande **inte godkänt eller registrerat** på den svenska läkemedelsmarknaden. Inga giltiga godkännandenummer finns att redovisa.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots en mycket hög TxGNN-förutsägelsepoäng (99,99 %) är det faktiska kliniska evidensunderlaget begränsat till ett enskilt fallrapport och en narrativ översikt. Den identifierade kliniska prövningen (NCT04398251) är dessutom inte specifikt utformad för Febuxostat vid renal hypourikemi. Bristen på svenska registreringsdata och de saknade säkerhetsuppgifterna gör att vidare utredning krävs innan ett positivt beslut kan fattas.

**För att gå vidare krävs:**
- Insamling av fullständig säkerhetsinformation: varningar, kontraindikationer och läkemedelsinteraktioner (via FASS/EMA-produktresumé)
- Bekräftelse av verkningsmekanism (MOA) via DrugBank API
- Identifiering av ytterligare kliniska studier eller fallserier specifikt om Febuxostat vid renal hypourikemi och EIAKI
- Utvärdering av om en prospektiv observationsstudie eller pilotstudie är genomförbar i patientgruppen (unga aktiva personer med URAT1-mutation)
- Kartläggning av eventuell off-label-användning i länder där Febuxostat är godkänt (t.ex. Japan, USA, EU) för detta tillstånd
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

