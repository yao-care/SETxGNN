---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 5
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

<div id="pharmacist">

## Apotekarens bedömningsrapport

</div>

Använder **txgnn-pipeline** för kontext. Nu genererar jag rapporten baserat på Evidence Pack.

---

# Etonogestrel: Från preventivmedelsimplantat till amenorré

## Sammanfattning

Etonogestrel är ett syntetiskt gestagen som verksamt ämne i subkutana preventivmedelsimplantat (Implanon/Nexplanon), primärt avsett för att förhindra graviditet genom att hämma ägglossning och endometrieproliferation. TxGNN-modellen förutsäger att läkemedlet kan ha terapeutisk relevans vid **amenorré**, med **1 klinisk prövning** och **2 publikationer** som berör detta samband. Det är viktigt att notera att etonogestrel i nuläget är bättre dokumenterat som en *inducerare* av amenorré som biverkning, snarare än som behandling av patologisk amenorré — en begreppslig distinktion som är avgörande för återanvändningshypotesen.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Inga godkända indikationer registrerade i databasen (känd klinisk användning: hormonellt preventivmedelsimplantat) |
| Förutsagd ny indikation | Amenorré (amenorrhea disease) |
| TxGNN-förutsägelsepoäng | 99,84 % |
| Evidensnivå | L3 — Indirekt klinisk evidens / observationsstudier |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad MOA-data saknas för närvarande i databasen. Baserat på känd farmakologi är etonogestrel ett tredje generationens gestagen som är det verksamma ämnet i implantatet Implanon/Nexplanon, vars preventivmedelseffekt har väl dokumenterats i ett flertal kliniska studier.

Etonogestrel utövar sin effekt genom att supprimera LH-toppen och hämma ovulationen, samt dämpa endometrieproliferationen via bindning till progesteronreceptorer. I fas 3-studier av preventivmedelsimplantat har amenorré — definierat som fullständigt upphörande av menstruationsblödning — rapporterats hos 20–30 % av användarna och dokumenterats systematiskt som ett primärt blödningsmönster-utfall. Denna välbelagda amenorré-inducerande egenskap utgör den biologiska grunden för TxGNN:s förutsägelse.

Sambandet mellan den ursprungliga preventivmedelsindikationen och amenorré är mekanistiskt logiskt: etonogestrels förmåga att supprimera den endometriella cykeln kan i teorin utnyttjas terapeutiskt vid tillstånd som *kräver* kontrollerad amenorré, exempelvis menorragi (kraftig menstruationsblödning), endometrios eller funktionell livmodersblödning. Det finns dock en grundläggande riktningsambiguitet: om målindikationen "amenorrhea (disease)" avser *patologisk* primär eller sekundär amenorré — där utebliven menstruation är ett symptom på en underliggande sjukdom — kan etonogestrel snarare vara en bidragande orsak än ett botemedel. Klinisk återanvändning förutsätter att detta målscenario klargörs noga innan vidare utvärdering.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fas 3 | Avslutad | 498 | Fas 3-studie av etonogestrel-implantatets preventiveffekt och säkerhet vid utvidgad användning till 4–5 år (godkänd duration är 3 år). Amenorré registrerades som sekundärt utfallsmått inom blödningsmönster-analys, inte som primär indikation eller behandlingsmål. Studien bekräftar att implantatet förblir effektivt upp till 5 år. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | *Contraception* | Randomiserad multicenterstudie (n=200) i Kina som jämförde Implanon (enkelstav, etonogestrel) med Norplant (sex kapslar) under 2–4 år. Inga graviditeter noterades i någon grupp. Blödningsmönster — inklusive amenorré-frekvens per 90-dagarsreferensperiod — dokumenterades som centralt utfallsmått, vilket ger indirekt evidens för etonogestrels amenorré-inducerande förmåga. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT | *Trials* | Studieprotokoll för BIO101 (ett växtbaserat preparat) vid COVID-19-pneumoni för att förebygga andningssvikt. Denna publikation saknar direkt koppling till etonogestrel eller amenorré och bedöms vara en falsk positiv i evidensinhämtningen. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots ett mycket högt TxGNN-förutsägelsepoäng (99,84 %) präglas återanvändningshypotesen av en grundläggande riktningsambiguitet — etonogestrel *inducerar* amenorré som välkänd biverkning snarare än behandlar patologisk amenorré — och evidensnivån L3 baseras uteslutande på indirekta studier där amenorré är ett sekundärt utfallsmått i preventivmedelsstudier.

**För att gå vidare krävs:**
- Klargörande av målindikationen: avser återanvändningen (a) terapeutisk amenorréinduktion vid tillstånd som menorragi eller endometrios, eller (b) behandling av *patologisk* primär/sekundär amenorré — dessa scenarier kräver helt skilda utvärderingsvägar
- Direkta kliniska studier med amenorré som *primärt behandlingsutfall*, inte enbart biverkningsdokumentation
- MOA-data från DrugBank (åtgärda datagap DG002) för att stärka den mekanistiska analysen
- Säkerhetsdata från produktresumén — varningar och kontraindikationer (åtgärda datagap DG001) — innan säkerhetsinitialvärdering (S1) kan genomföras
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

