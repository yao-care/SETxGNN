---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Använder `txgnn-pipeline`-skillet för att vägleda rapportgenereringen. Nu analyserar jag Evidence Pack och producerar rapporten.

---

# Apixaban: Från tromboemboliprofylax till migrän

## Sammanfattning

Apixaban är en selektiv Factor Xa-hämmare som primärt används för att förebygga tromboemboliska komplikationer vid tillstånd som förmaksflimmer och venös tromboembolism. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **migrän**, med **1 klinisk prövning** och **4 publikationer** som undersöker detta samband. Befintliga bevis är emellertid svaga och motstridiga — enstaka fallrapporter tyder tvärtom på att Apixaban kan förvärra migrän jämfört med warfarin, vilket väcker allvarliga tvivel om den kliniska relevansen av denna förutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej tillgänglig (inga godkännanden registrerade) |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,0 % |
| Evidensnivå | L4 – Mekanismstudier och fallrapporter |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen formell verkningsmekanismdata tillgänglig från DrugBank för detta Evidence Pack. Baserat på befintlig information i utredningsunderlaget är Apixaban en selektiv direktverkande Factor Xa-hämmare som blockerar koagulationskaskaden och minskar trombinbildning.

Den teoretiska kopplingen till migrän bygger på hypotesen att patent foramen ovale (PFO) — ett hjärtfenomen som är överrepresenterat hos patienter med migrän med aura — kan skapa mikroemboli som utlöser kortikal spridningsdepolarisation (CSD), en känd neurofysiologisk mekanism bakom migränanfall. Genom att hämma koagulationen skulle Apixaban teoretiskt kunna minska frekvensen av dessa mikroemboli och därigenom minska anfallsfrekvensen.

Befintliga kliniska data talar dock emot denna hypotes. Fallrapporter beskriver hur patienter som uppnått fullständig migränremission på warfarin fick återfall inom veckor efter byte till Apixaban, med ny remission vid återinsättning av warfarin. En möjlig förklaring är att warfarins effekt beror på pleiotropa mekanismer — exempelvis hämning av Gas6/Protein S via VKORC1-vägen — med antiinflammatoriska och neuroprotektiva egenskaper som Apixaban saknar. Den mekanistiska kopplingen är därmed svag och uppvisar motstridiga tecken.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fas 3 | Avslutad | 664 | Randomiserad studie som jämförde PFO-stängning, antikoagulantia (primärt warfarin) och trombocythämmare för att förebygga återfall av ischemisk stroke hos patienter med PFO. Studien är indirekt relevant: PFO har en biologisk koppling till migrän, men Apixaban ingick inte som primär intervention och migränutfall utvärderades inte. Utgör inte direkt bevis för Apixaban vid migrän. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Liten klinisk studie | *Lupus* | Retrospektiv studie av 75 patienter med antifosfolipidantikroppar (aPL) och refraktär migrän behandlade med antitrombotisk terapi. En subgrupp visade symtomförbättring, vilket antyder att aPL-medierad migrän kan svara på antitrombotisk behandling. Apixaban utvärderades dock inte specifikt. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Fallrapport + Litteraturöversikt | *The Neurologist* | Rapporterar ett fall där migrän med aura förvärrades efter insättning av Apixaban. Litteraturöversikten konstaterar att effekten av direkta orala antikoagulantia på migrän är oklar och att befintlig litteratur är knapp och motsägelsefull. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Fallrapport | *Headache* | 55-årig kvinna med fullständig remission av migrän med aura under 12 år på warfarin. Symtomen återkom inom tre veckor efter byte till Apixaban och remitterade åter vid återinsättning av warfarin. Pekar starkt mot att Apixaban saknar warfarins migränlindrande egenskaper. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Fallrapport | *Headache* | Fallrapport om vestibulär migrän som remitterade vid behandling med warfarin och topiramat. Understryker en möjlig roll för antikoagulation vid specifika migränsubtyper, men involverar inte Apixaban. |

---

## Säkerhetsaspekter

> Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensen för Apixaban vid migrän befinner sig på L4-nivå och baseras uteslutande på fallrapporter och en indirekt fas 3-studie. Det som är mer avgörande är att de bäst tillgängliga fallrapporterna pekar i motsatt riktning — Apixaban verkar inte dela warfarins migränlindrande egenskaper och kan i vissa fall förvärra tillståndet, vilket i grunden underminerar repurposing-hypotesen.

**För att gå vidare krävs:**
- Direkta kliniska prövningar av Apixaban specifikt för migrän (inga sådana finns registrerade)
- Mekanismstudier som klarlägger skillnaderna i pleiotropa effekter mellan Apixaban och warfarin (t.ex. Gas6/Protein S-vägen)
- Prospektiva observationsstudier eller registerstudier i PFO-positiva migränpopulationer med specificerad antikoagulantiatyp
- Fullständig säkerhetsprofil och kontraindikationsdata (produktresumé från Läkemedelsverket)
- Godkännandedata för Apixaban på den svenska marknaden
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

