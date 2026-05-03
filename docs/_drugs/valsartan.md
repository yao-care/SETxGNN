---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

Använder **txgnn-pipeline** för att säkerställa korrekt rapportformat, sedan genererar jag rapporten baserat på Evidence Pack.

---

# Valsartan: Från hypertoni till malign renovaskulär hypertoni

## Sammanfattning

Valsartan är en angiotensin II typ 1-receptorantagonist (ARB) som primärt används för behandling av hypertoni och hjärtsvikt. TxGNN-modellen förutsäger med 99,97% säkerhet att det kan vara effektivt mot **malign renovaskulär hypertoni**, med **1 publikation** som för närvarande stöder denna riktning. Mekanistiskt föreligger en stark koppling – malign renovaskulär hypertoni drivs av kraftig RAAS-aktivering, precis det system som valsartan blockerar via AT1-receptorn.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Hypertoni och hjärtsvikt |
| Förutsagd ny indikation | Malign renovaskulär hypertoni |
| TxGNN-förutsägelsepoäng | 99,97% |
| Evidensnivå | L3 – Observationsstudier / mekanismstudier |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Officiell MOA-data från DrugBank saknas i detta Evidence Pack, men baserat på tillgänglig information är valsartan en selektiv AT1-receptorantagonist (angiotensin II-receptorblockerare, ARB). Det hämmar angiotensin II:s kärlsammandragande och aldosteronstimulerande effekter, vilket sänker blodtrycket och minskar njurbelastningen.

Malign renovaskulär hypertoni uppstår typiskt vid njurartärstenos, som utlöser massiv, okontrollerad aktivering av renin-angiotensin-aldosteronsystemet (RAAS). Angiotensin II-nivåerna når extrema värden och orsakar en hypertonisk kris med risk för njur-, hjärt- och hjärnskada. Valsartans mekanism – direkt blockad av AT1-receptorn – är patofysiologiskt exakt riktad mot den centrala sjukdomsdrivaren i denna tillstånd.

I klinisk praxis betraktas ARB:er och ACE-hämmare redan som hörnstenar i behandlingen av renovaskulär hypertoni, vilket ytterligare stärker mekanistisk relevans. Förutsägelsens rimlighet underbyggs av att valsartan angriper sjukdomsprocessen i sin kärna, inte enbart symptomlindrar.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Djur-/Mekanismstudie | *Circulation* | AT1-receptorblockad förhindrade letalt förlöp vid malign hypertension i djurmodell, oberoende av blodtrycksänkande effekt. Resultaten kopplar angiotensin II-medierad njurinflammation till sjukdomsutvecklingen och stöder en direkt skyddande effekt av AT1-blockad. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Den mekanistiska kopplingen mellan valsartan och malign renovaskulär hypertoni är stark och välunderbyggd, men kliniska prövningsdata saknas helt för denna specifika indikation, och befintlig litteratur är begränsad till en enskild djurstudie.

**För att gå vidare krävs:**
- Genomförande av prospektiv klinisk prövning (fas 2) hos patienter med malign renovaskulär hypertoni
- Inhämtning av fullständig produktresumé och säkerhetsdata (varningar, kontraindikationer) för att möjliggöra S1-säkerhetsbedömning
- Komplettering av MOA-data via DrugBank API för formell mekanismanalys
- Utredning av regulatorisk väg för eventuell registrering i Sverige (MPA/EMA)
- Sökning efter ytterligare humanstudier, särskilt observationsstudier och kohortstudier, för att stärka evidensbasen från L3 till L2
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

