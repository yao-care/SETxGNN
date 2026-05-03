---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 7
---

# Ibuprofen
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

Använder **txgnn-pipeline** för att vägleda rapportgenerering. Analyserar Evidence Pack för Ibuprofen (DB01050) och sammanställer nu den svenska rapporten.

---

# Ibuprofen: Från smärtlindring och inflammation till akromesomelisk dysplasi (Hunter-Thompson typ)

## Sammanfattning

Ibuprofen är ett av världens mest välkända icke-steroida antiinflammatoriska läkemedel (NSAID), traditionellt använt för smärtlindring, febernedsättning och behandling av inflammatoriska tillstånd. TxGNN-modellen förutsäger att det kan ha effekt vid **akromesomelisk dysplasi av Hunter-Thompson typ (AMDH)** – en sällsynt genetisk skelettdysplasi orsakad av GDF5-mutation. Förutsägelsen saknar för närvarande stöd från kliniska prövningar eller publicerad litteratur och vilar **enbart på modellberäkning**.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Smärtlindring, febernedsättning och inflammationsbehandling (NSAID) |
| Förutsagd ny indikation | Akromesomelisk dysplasi, Hunter-Thompson typ |
| TxGNN-förutsägelsepoäng | 99,74% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte registrerat i datakällan |
| Antal godkännanden | 0 (enligt datakällan) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Ibuprofen verkar som en icke-selektiv COX-inhibitor (cyklooxygenashämmare) och blockerar syntesen av prostaglandiner – signalmolekyler som driver inflammation, smärta och feber. Läkemedlet hämmar både COX-1 och COX-2, vilket leder till sänkta nivåer av prostaglandin E₂ (PGE₂) i vävnaderna.

Akromesomelisk dysplasi av Hunter-Thompson typ orsakas av mutationer i GDF5-genen (Growth Differentiation Factor 5, även känd som CDMP1), vilket nedsätter BMP-signaleringen och leder till abnorm skelettbildning i framför allt extremiteternas distala delar. PGE₂ är känt för att kunna modulera BMP-2-inducerad osteogen differentiering, och COX-hämning kan teoretiskt förändra den parakrina BMP-miljön i benvävnaden – vilket utgör den mekanistiska bryggan i TxGNN:s förutsägelse.

Den mekanistiska länken bedöms dock som svag. AMDH är ett genetiskt strukturellt tillstånd där COX-hämning varken kan reparera det muterade GDF5-proteinet eller korrigera den underliggande genetiska defekten. Att hämma COX-enzymet förändrar den parakrina signalmiljön men adresserar inte den primära patofysiologin. Klinisk nytta bedöms som osannolik baserat på nuvarande farmakologisk förståelse.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Säkerhetsaspekter

> Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen baseras uteslutande på TxGNN-modellens beräkningsresultat (evidensnivå L5) utan stöd från kliniska prövningar, observationsstudier eller publicerad litteratur. Den mekanistiska länken mellan COX-hämning och GDF5-relaterad skelettdysplasi bedöms som biologiskt svag – COX-hämning kan inte kompensera för en strukturell genetisk defekt i BMP-signalvägen.

**För att gå vidare krävs:**
- Systematisk litteratursökning avseende COX-inhibitorer och BMP/GDF5-signalering vid skelettdysplasi
- Preklinisk in vitro- och in vivo-data för ibuprofen i AMDH-modeller (t.ex. Gdf5-knockout-möss)
- Bedömning av om inflammationskomponenten vid AMDH kan ge symptomlindrande effekt, även utan kurativt syfte
- Inhämtning av fullständig säkerhetsdata från produktresumén (varningar, kontraindikationer, interaktioner)
- Verifiering av marknadsstatus i Sverige via Läkemedelsverkets databas, då datakällan rapporterar 0 godkännanden för ett i övrigt välkänt läkemedel
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

