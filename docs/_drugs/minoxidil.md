---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

TxGNN-pipeline-skillet är mer inriktat på pipeline-förvaltning. Rapporten nedan genereras direkt enligt instruktionerna i systempromten (v5).

---

# Minoxidil: Från androgenetisk alopeci till hypotrichosis simplex of the scalp

## Sammanfattning

Minoxidil är ett kärlvidgande läkemedel som historiskt använts för behandling av svår hypertoni och – som biverkan som sedermera blev terapeutisk effekt – androgenetisk alopeci. TxGNN-modellen förutsäger att det kan vara effektivt mot **hypotrichosis simplex of the scalp** (ärftlig skalphypotricos), ett sällsynt genetiskt hårtillstånd med förkortad anagensfas. Förutsägelsen stöds av **3 publikationer**, samtliga fallrapporter eller småskaliga fallserier, varför ytterligare prospektiv klinisk utredning krävs innan klinisk tillämpning kan rekommenderas.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige |
| Förutsagd ny indikation | Hypotrichosis simplex of the scalp |
| TxGNN-förutsägelsepoäng | 99,9999 % |
| Evidensnivå | L3 – Observationsstudier / fallserier |
| Marknadsstatus i Sverige | Ej på marknaden |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta – prospektiv klinisk studie krävs |

---

## Varför är denna förutsägelse rimlig?

Minoxidil verkar via öppnande av ATP-känsliga kaliumkanaler (K-ATP-kanaler) i kärlväggens glatta muskelceller, vilket ger hyperpolarisering, minskat kalciumflöde och vasodilatation. I hårsäcksbiologin omsätts denna mekanism i tre parallella effekter: förlängning av anagensfasen (aktiv hårtillväxtfas), förbättrad mikrocirkulation kring hårsäckspappillan samt aktivering av Wnt/β-catenin-signalvägen som driver hårsäcksproliferation. Eftersom ingen detaljerad verkningsmekanismdata är tillgänglig i aktuellt datamaterial baseras beskrivningen på publicerad farmakologisk litteratur.

Hypotrichosis simplex of the scalp (HSS) orsakas av mutationer i genen *CDSN* (kodandes desmosomproteinet corneodesmosin), vilket stör häftningen mellan keratinocyter i hårsäckskanalen och leder till en förkortad anagen samt progressivt tunnare hår – utan ärrbildning och utan inflammatorisk komponent. Den patofysiologiska kärnan är alltså en *funktionellt defekt* hårsäck med kvarvarande biologisk aktivitet, vilket skapar en logisk ingångspunkt för minoxidil: läkemedlet kan potentiellt kompensera för den förkortade anagenperioden och stödja kvarvarande hårsäcksfunktion.

Det är dock avgörande att notera att minoxidil **inte kan korrigera den underliggande genmutationen**. Effekten är symtomatisk och förväntas inte vara kurativ. TxGNN-modellens extremt höga förutsägelsepoäng (≈100 %) återspeglar den nära biologiska likheten med tillstånd där minoxidil redan är välbelagt, snarare än att indikera starkt kliniskt bevis specifikt för HSS.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Fallrapport / Fallserie | *Dermatologic Therapy* | Behandling av ärftlig hypotrichosis simplex med oralt minoxidil kombinerat med tillväxtfaktorer; preliminär klinisk respons dokumenterades. |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Fallrapport | *Frontiers in Genetics* | Familjärt HSS-fall hos 8-åring med verifierad CDSN-mutation; kombination av botaniska extrakt och minoxidil gav förbättrad hårtäthet vid uppföljning. |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Fallrapport | *J Dermatological Treatment* | 14-årig patient med hypotrichosis simplex behandlad med PRP-injektion kombinerat med topikal minoxidil 2 %; positiv klinisk respons med ökad hårlängd och -densitet rapporterades. |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensbasen för minoxidil vid hypotrichosis simplex of the scalp består uteslutande av fallrapporter och småskaliga fallserier (L3), vilket är otillräckligt för att rekommendera klinisk implementering. Därtill saknas svensk marknadsregistrering, och ett eventuellt användande skulle kräva licenspreparat eller formell klinisk prövning.

**För att gå vidare krävs:**
- Prospektiv öppen fas 2-studie (n ≥ 20–30) med standardiserade utfallsmått: trikoskopi, hårräkning per cm², SALT-score samt subjektiv patientnöjdhet
- Jämförelse av beredningsformer: topikal minoxidil 2–5 % kontra oral lågdos (0,625–2,5 mg/dag) anpassad för HSS-patientpopulationen
- Särskild säkerhetsdata för pediatriska patienter, eftersom HSS debuterar i barn- och ungdomsåren
- Genotypning av *CDSN*- och *LPAR6*-mutationer för att identifiera eventuella responderprofiler och biomarkörer
- Dialog med Läkemedelsverket (MPA, Sverige) angående licensförfarande och eventuell klinisk prövningsdesign
- Komplettering av säkerhetsdatamaterialet: inhämtning av kontraindikationer, varningstext och interaktionsprofil från produktresumén
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

