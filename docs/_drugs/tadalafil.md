---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **8** st
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

---

# Tadalafil: Från erektil dysfunktion till Ambras typ hypertrikosis universalis congenita

---

## Sammanfattning

Tadalafil är en selektiv PDE5-hämmare (fosfodiesteras typ 5) som globalt godkänts för erektil dysfunktion, benign prostatahyperplasi och pulmonell arteriell hypertension, men som saknar registrering i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **Ambras typ hypertrikosis universalis congenita** med en förutsägelsepoäng på **99,98%**. Det saknas dock helt kliniska prövningar och publicerad litteratur för denna indikation, och den mekanistiska analysen tyder på att modellens förutsägelse troligen grundas på ett omvänt kausalsamband – PDE5-hämmare är kända för att orsaka ökad hårtillväxt som biverkning, inte att behandla hypertrikosis.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Erektil dysfunktion, benign prostatahyperplasi, pulmonell arteriell hypertension (ej registrerat i Sverige) |
| Förutsagd ny indikation | Ambras typ hypertrikosis universalis congenita |
| TxGNN-förutsägelsepoäng | 99,98% |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Inte registrerat |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Tadalafil hämmar selektivt enzymet PDE5, som normalt bryter ned cGMP (cykliskt guanosinmonofosfat). Hämningen ökar cGMP-nivåerna i glatt muskulatur och kärlväggar via NO–cGMP-signalvägen, vilket leder till kärlvidgning. Denna mekanism ligger till grund för tadalafils godkända effekter vid erektil dysfunktion (avslappning av corpus cavernosum), pulmonell arteriell hypertension (sänkt lungkärlsmotstånd) och benign prostatahyperplasi (avslappning av prostata- och blåshalsmuskulatur).

PDE5/cGMP-signalering har en potentiell roll i hårfollikelns tillväxtcykel via NO–cGMP-vägen i de dermala papillcellerna – denna koppling är sannolikt grunden för att TxGNN-modellen förutsäger en association med hårtillväxtsjukdomar. Ambras typ hypertrikosis universalis congenita orsakas dock av en mutation i **TRPS1-genen** (tricho-rhino-phalangeal syndrome type 1) och är en genetisk strukturell avvikelse utan känt samband med PDE5-reglering uppströms. Det saknas i dagsläget evidens för att tadalafil påverkar TRPS1-genens expression eller funktion.

> **⚠️ Viktig metodologisk varning:** Flera av de högst rankade indikationerna i detta Evidence Pack (rank 1–2: hypertrikosis, rank 6: trichomegaly, rank 8: migrän med hjärnstamsaura) är kända **biverkningar** av PDE5-hämmare – inte potentiella behandlingsindikationer. TxGNN-modellen verkar ha fångat dessa kausalsamband i kunskapsgrafen utan att korrekt skilja på riktningen (läkemedlet *orsakar* tillståndet kontra läkemedlet *behandlar* tillståndet). Den mekanistiskt mest välgrundade förutsägelsen i detta pack är **kyfoskoliotisk hjärtsjukdom (rank 7)**, som ofta kompliceras av sekundär pulmonell arteriell hypertension – en faktisk godkänd indikation för tadalafil.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Tadalafil saknar godkännande i Sverige. Inga licensuppgifter finns registrerade (total_licenses = 0).

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivån är L5 – enbart modellförutsägelse utan stöd av kliniska prövningar eller litteratur. Den mekanistiska analysen pekar dessutom på att förutsägelsen sannolikt är en artefakt av omvänt kausalsamband i kunskapsgrafen: tadalafil *orsakar* hypertrikosis som biverkning via NO–cGMP-driven hårtillväxt, snarare än att vara en kandidat för behandling av tillståndet.

**För att gå vidare krävs:**
- Omprioritering av utvärderingen mot **rank 7 (kyfoskoliotisk hjärtsjukdom / PAH-koppling)**, som har starkare mekanistisk grund och ett direkt samband med tadalafils godkända indikation vid pulmonell arteriell hypertension
- Verifiering av om PDE5/cGMP-signalering har någon dokumenterad roll uppströms i TRPS1-genreglering, innan rank 1 kan anses mekanistiskt motiverad
- Inhämtning av fullständig SMPC-data (produktresumé) och säkerhetsinformation för Sverige
- Genomförande av en systematisk kausalitetsgranskning av kunskapsgrafens kant-riktningar för samtliga hårtillväxtrelaterade förutsägelser i detta pack
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

