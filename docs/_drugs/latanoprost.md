---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

Jag använder **txgnn-pipeline**-skillet för att kontextualisera arbetsflödet. Uppgiften är att generera en fullständig utvärderingsrapport på svenska baserat på det angivna Evidence Pack. Jag går nu vidare och producerar rapporten direkt.

---

# Latanoprost: Från öppenvinkelglaukom till primärt hereditärt glaukom

---

## Sammanfattning

Latanoprost är ett prostaglandinanalogum som primärt används för att behandla öppenvinkelglaukom och okulär hypertension, genom att sänka det intraokulära trycket (IOP) via ökat uveoscleralt avflöde. TxGNN-modellen förutsäger att det kan vara effektivt mot **primärt hereditärt glaukom**, med **1 avslutad klinisk prövning** som ger indirekt stöd för denna riktning. Inga specifika publikationer för denna indikation har påträffats i litteratursökningen.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Öppenvinkelglaukom och okulär hypertension (ej registrerad i Sverige) |
| Förutsagd ny indikation | Primärt hereditärt glaukom |
| TxGNN-förutsägelsepoäng | 99,88% |
| Evidensnivå | L2 |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Fortsätt med försiktighet |

---

## Varför är denna förutsägelse rimlig?

Latanoprost verkar som en selektiv agonist mot FP-prostaglandinreceptorn i ögat. Genom att aktivera dessa receptorer ökar latanoprost det uveosclerala kammarvattensavflödet, vilket resulterar i en sänkning av det intraokulära trycket (IOP). Denna tryckreducerande effekt är väletablerad kliniskt och utgör grunden för läkemedlets användning vid glaukom.

Primärt hereditärt glaukom delar samma centrala patofysiologi som öppenvinkelglaukom: ett förhöjt IOP som, om det kvarstår obehandlat, leder till progressiv synnervsskada och synnedsättning. Trots att den hereditära formen orsakas av genetiska defekter – vanligtvis i gener som reglerar trabekelmeshverkens funktion – är den underliggande mekanismen för synnervsskada identisk med den vid förvärvat glaukom.

Prostaglandinanaloga preparat, inklusive latanoprost, räknas i dag till förstahandsvalet vid behandling av flera glaukomformer. Att denna mekanism är applicerbar på den hereditära subtypen stöds av att kliniska prövningar med prostaglandinanaloga redan har genomförts vid pediatriskt och genetiskt betingat glaukom (se NCT01527682 nedan). Förutsägelsens rimlighet är hög givet den direkta mekanistiska kopplingen.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fas 2 | Genomförd | 37 | Studien utvärderade den okulära trycksänkande effekten och säkerhetsprofilen hos latanoprost och dorzolamid vid primärt pediatriskt glaukom refraktärt mot kirurgiska ingrepp. Protokollet ändrades under studiens gång; slutligt inklusionsmål sänktes till 68 ögon (34–68 patienter). Resultat ger initialdata om prostaglandinanalogans effektivitet vid denna population. |

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Fortsätt med försiktighet**

**Motivering:**
- Latanoprostets välkända IOP-sänkande verkningsmekanism via FP-prostaglandinreceptorn är direkt relevant för primärt hereditärt glaukom, vars kärn­patofysiologi är identisk med andra glaukomformer. En avslutad fas 2-prövning med prostaglandinanaloga vid pediatriskt glaukom (NCT01527682) ger ett konkret kliniskt stöd, men specifika resultatdata för den hereditära subtypen behöver verifieras innan vidare beslut kan fattas.

**För att gå vidare krävs:**
- Granskning av publicerade resultat från NCT01527682 (primära effektmått, IOP-sänkning, säkerhetsutfall)
- Riktad litteratursökning med bredare söktermer (t.ex. "latanoprost hereditary glaucoma", "prostaglandin juvenile glaucoma") för att identifiera eventuella fallrapporter eller observationsstudier
- Inhämtning av fullständig säkerhetsinformation (varningar, kontraindikationer, biverkningsprofil) från godkänd produktresumé
- Komplettering av MOA-data via DrugBank API (DG002) för att stärka mekanismsanalysen
- Utredning av om pediatrisk dosering och administreringsväg kräver anpassning för den hereditärt drabbade populationen
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

