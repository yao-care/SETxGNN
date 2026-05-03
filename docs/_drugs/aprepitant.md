---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

Analyserar Evidence Pack för Aprepitant och genererar rapport enligt specifikation.

---

# Aprepitant: Från kemoterapi-inducerat illamående till nefrogt syndrom av inadekvat antidiures

## Sammanfattning

Aprepitant är en neurokinin-1-receptorantagonist (NK1-antagonist) som traditionellt används för att förebygga kemoterapi-inducerat illamående och kräkningar (CINV) samt postoperativt illamående. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **nefrogt syndrom av inadekvat antidiures (NSIAD)** – ett sällsynt tillstånd orsakat av aktiverande mutationer i vasopressinreceptorn AVPR2. Det finns för närvarande **inga kliniska prövningar** och **inga publikationer** som stöder denna riktning, och den mekanistiska kopplingen bedöms som mycket svag.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Förebyggande av kemoterapi-inducerat illamående och kräkningar (CINV) |
| Förutsagd ny indikation | Nefrogt syndrom av inadekvat antidiures (NSIAD) |
| TxGNN-förutsägelsepoäng | 99,97% |
| Evidensnivå | L5 – enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är Aprepitant en NK1-receptorantagonist som blockerar bindningen av Substance P till neurokinin-1-receptorn. Läkemedlet verkar primärt i centrala nervsystemets kräkningscentrum och mag-tarmkanalen, och dess effekt vid förebyggande av CINV är välbevisad kliniskt.

NSIAD (nefrogt syndrom av inadekvat antidiures) är en sällsynt genetisk sjukdom som orsakas av aktiverande (gain-of-function) mutationer i AVPR2-genen, vilken kodar för vasopressinreceptor typ 2 i njurens samlingsgång. Mutationen leder till konstitutiv receptoraktivering – njurarna retinerar vatten oberoende av ADH-nivåer – vilket resulterar i hyponatremi och inappropriat låg serumosmolalitet.

Den mekanistiska kopplingen är biologiskt svag. Substance P kan visserligen påverka ADH-frisättning från hypotalamus via NK1-receptorer, men i ett tillstånd där AVPR2 redan är konstitutivt aktiverat av en genetisk mutation är det inte rimligt att förvänta sig att en NK1-antagonist i hypotalamus kan ha klinisk effekt på den perifera receptornivå där sjukdomen manifesterar sig. TxGNN:s höga förutsägelsepoäng för NSIAD bör tolkas med stor försiktighet och beror sannolikt på indirekta nätverkskopplingar i kunskapsgrafen snarare än en direkt biologisk relation.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Aprepitant är inte godkänt och saknar registrerade produkter i Sverige. Inga licensuppgifter finns att redovisa.

---

## Säkerhetsaspekter

Detaljerad säkerhetsinformation (varningar, kontraindikationer, läkemedelsinteraktioner) kunde inte hämtas inom ramen för detta evidenspaket.

> Se produktresumén (SmPC) för fullständig säkerhetsinformation.

Noterbart: Aprepitant är en känd hämmare av CYP3A4, vilket kan ge kliniskt relevanta läkemedelsinteraktioner om det används i kombination med CYP3A4-substrat. Detta bör beaktas vid eventuell vidare utredning.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensunderlaget befinner sig på L5-nivå (enbart modellförutsägelse utan stödjande studier), och den mekanistiska bryggan mellan NK1-antagonism och NSIAD – ett tillstånd drivet av konstitutiv AVPR2-aktivering via genetisk mutation – bedöms som extremt svag. Aprepitant är dessutom ej godkänt i Sverige, vilket ytterligare ökar hinder för klinisk tillämpning.

**För att gå vidare krävs:**
- **Mekanistisk validering**: in vitro-studier som visar en konkret koppling mellan NK1-signalering och AVPR2-aktivering i njurvävnad
- **Prekliniska djurmodeller**: NSIAD-modell med NK1-antagonistintervention för proof-of-concept
- **Fullständig säkerhetsprofil**: MOA-data, kontraindikationer och varningstexter hämtade från EMA/FASS-godkänd produktresumé
- **Regulatorisk kartläggning**: Aprepitant är godkänt i EU (Emend®) via EMA – befintlig europeisk godkännandestruktur bör kartläggas inför eventuell ansökan om utvidgad indikation
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

