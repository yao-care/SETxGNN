---
layout: default
title: Cyclopentolate
parent: Endast modellprediktion (L5)
nav_order: 116
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Cyclopentolate: predikterad ny indikation Kauda equina-syndrom (evidensnivå L5). Ursprunglig indikation: Cykloplegi (enligt TxGNN-kunskapsgrafen"
monitor_inn: "cyclopentolate"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

# Cyklopentolat: Från cykloplegi till kauda equina-syndrom

---

### Sammanfattning

Cyklopentolat är ett antimuskarint ögonläkemedel som ursprungligen användes för att framkalla cykloplegi (förlamning av ögats ackommodationsmuskel) vid ögonundersökningar. TxGNN-modellen förutsäger att det kan vara effektivt mot **kauda equina-syndrom**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder denna riktning. Förutsägelsen bygger enbart på modellberäkning (evidensnivå L5).

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Cykloplegi (enligt TxGNN-kunskapsgrafen; indikationstext saknas i de svenska godkännandena) |
| Förutsagd ny indikation | Kauda equina-syndrom |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 2 (båda indragna) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är cyklopentolat ett topikalt antimuskarint (antikolinergt) läkemedel. Dess effekt vid cykloplegi är väl känd, och mekanistiskt skulle klasseffekten på glatt muskulatur kunna vara tillämpbar på blåsrubbningar.

Kauda equina-syndrom orsakas främst av tryck på nervrötterna i ryggmärgskanalen och är ett akut tillstånd som kräver kirurgisk avlastning. Blåsdysfunktion är en av följderna. Modellens förutsägelse drivs sannolikt av antimuskarinernas effekt på blåsmuskeln (detrusorn). Ett sådant läkemedel skulle i bästa fall kunna lindra blåssymptom, men inte behandla den bakomliggande nervkompressionen.

Den biologiska rimligheten bedöms som svag. Cyklopentolat är utvecklat som ögondroppar och saknar etablerad systemisk användning. Det finns inga data om att läkemedlet når tillräcklig exponering i andra organ.

Modellen förutsade även två andra indikationer: neurogen blåsa (term som är markerad som föråldrad i ontologin) och irritabel tarm (IBS). Båda är klassmässigt rimliga för antimuskarina läkemedel, men det finns redan bättre dokumenterade och godkända alternativ.

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 10008 | Cyclopentolat Bausch & Lomb | Ögondroppar, lösning i endosbehållare | Indikationstext saknas (indragen) |
| 6001 | Cyclogyl | Ögondroppar, lösning | Indikationstext saknas (indragen) |

---

### Säkerhetsaspekter

Inga varningar eller kontraindikationer från produktresumén ingår i de data som sammanställts för rapporten. Se produktresumén för säkerhetsinformation.

Kunskapsgrafen (inte produkttext) kopplar läkemedlet till följande tillstånd där användning kan vara olämplig:

- **Ögon:** trångvinkelglaukom (sluten kammarvinkel)
- **Hjärt-kärl:** högt blodtryck, hjärtsjukdom, kranskärlssjukdom, plötsligt hjärtstopp, retledningsrubbningar i hjärtat, åderförkalkning
- **Ämnesomsättning:** diabetes, diabetisk ketoacidos, hypertyreos (Graves sjukdom, tyreotoxikos)
- **Urinvägar:** godartad prostataförstoring
- **Nervsystem:** hjärnskada, hjärnsjukdom, Downs syndrom

Dessa uppgifter bör verifieras mot produktresumén. Särskilt relevant vid systemisk användning är risken för antikolinerga biverkningar (påverkan på centrala nervsystemet, hjärtklappning, förstoppning).

Inga läkemedelsinteraktioner hittades i de sammanställda data.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen stöds enbart av modellen (L5), utan kliniska prövningar eller litteratur. Biologisk rimlighet är svag eftersom läkemedlet är ett ögonpreparat, och godkännandena i Sverige är indragna.
- Etablerade antimuskarina läkemedel finns redan för blåssymtom, och kauda equina-syndrom behandlas främst kirurgiskt.

**För att gå vidare krävs:**
- Verkningsmekanismdata från DrugBank.
- Produktresumé från Läkemedelsverket med varningar och kontraindikationer (blockerande dataluckor för säkerhetsscreening).
- Systematisk litteratur- och prövningssökning för kauda equina-syndrom och blåsdysfunktion.
- Mappning av den föråldrade sjukdomstermen till aktuell terminologi (neurogen detrusoröveraktivitet).
- Bedömning av administreringsväg och systemisk exponering, eftersom den nuvarande beredningen är ögondroppar.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

