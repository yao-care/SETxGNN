---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

Jag använder `txgnn-pipeline`-skillet som guide och genererar nu rapporten baserat på Evidence Pack-data.

---

# Zanamivir: Från influensabehandling till pyelonefrit

## Sammanfattning

Zanamivir är ett antiviralt läkemedel inom klassen neuraminidashämmare, vars etablerade användning är behandling och profylax av influensa A och B. TxGNN-modellen förutsäger att det potentiellt kan vara effektivt mot **pyelonefrit** (njurbäckeninflammation) med en förutsägelsepoäng på **99,84 %**. Förutsägelsen saknar dock helt stöd från kliniska prövningar eller vetenskaplig litteratur, vilket innebär att evidensbasen uteslutande bygger på modellens grafstrukturella slutledning utan biologisk eller klinisk validering.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Influensa A och B – behandling och profylax (ej godkänd i Sverige; baserat på känd global användning) |
| Förutsagd ny indikation | Pyelonefrit (njurbäckeninflammation) |
| TxGNN-förutsägelsepoäng | 99,84 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta Evidence Pack. Baserat på känd information är Zanamivir en neuraminidashämmare vars antivirala effekt vid influensa A och B är väl dokumenterad globalt. Läkemedlet verkar genom att selektivt blockera influensavirusets neuraminidasenzym, vilket hindrar viruspartiklar från att frigöra sig från infekterade celler och sprida sig i kroppen.

Pyelonefrit är en bakteriell infektion i njurbäckenet och njurparenkymet, orsakad primärt av *Escherichia coli* och andra gramnegativa tarmbakterier. Eftersom Zanamivirs verkningsmekanism riktas mot ett virusspecifikt enzym (influensaneuraminidaset), utan känd aktivitet mot bakteriella patogener, saknas en biologiskt plausibel länk till bakteriell njurinfektion.

Den interna mekanistiska analysen bedömer att TxGNN:s höga poäng sannolikt utgör ett strukturellt falskt positivt resultat – modellen kan ha dragit slutsatsen via indirekta kopplingar mellan infektionssjukdomsnoder i kunskapsgrafen (delade grannar mellan "infektionssjukdomar" och "läkemedel"), snarare än via en reell biologisk mekanism. Det finns inget prekliniskt eller kliniskt underlag som stöder användning av Zanamivir vid pyelonefrit.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Zanamivir är inte godkänt eller marknadsfört i Sverige. Inga läkemedelsgodkännanden finns registrerade hos läkemedelsmyndigheten.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Trots att TxGNN-förutsägelsepoängen är mycket hög (99,84 %) saknas all biologisk och klinisk förankring. Zanamivir är ett antiviralt läkemedel utan känd antibakteriell effekt, och pyelonefrit orsakas av bakterier – det finns ingen etablerad mekanism som kan motivera vidare utredning i nuläget. Evidensnivån är L5, vilket innebär att förutsägelsen uteslutande bygger på modellens slutledning.

**För att gå vidare krävs:**
- Identifiering av en biologiskt plausibel mekanism som kopplar neuraminidashämning till effekt mot uropatogena bakterier
- Prekliniska data (in vitro eller djurmodell) som visar antibakteriell aktivitet av Zanamivir eller neuraminidashämmare mot relevanta patogener
- Minst en explorativ klinisk studie, fallserie eller fallrapport som stöder indikationen
- Fullständig säkerhetsdokumentation (MOA-data, varningar och kontraindikationer) för att möjliggöra en formell säkerhetsinitialutvärdering (S1)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

