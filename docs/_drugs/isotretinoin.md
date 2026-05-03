---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

Using `txgnn-pipeline` som kontext för att generera läkemedelsåteranvändningsrapport.

---

# Isotretinoin: Från svår akne till malign renovaskulär hypertoni

## Sammanfattning

Isotretinoin är ett retinoid (vitamin A-derivat) som sedan länge används för behandling av svår nodulär akne, med verkan via RAR/RXR-kärnreceptorer i retinoid-signalvägen. TxGNN-modellen förutsäger att det kan vara effektivt mot **malign renovaskulär hypertoni** – via en hypotetisk länk till renin-angiotensinsystemet – med ett förutsägelsepoäng på 99,01 %. Det finns dock för närvarande **inga kliniska prövningar** och **inga publikationer** som stöder denna indikation, och en känd biverkningsprofil med intrakraniell hypertension gör den föreslagna riktningen kontradiktorisk.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Svår nodulär akne (allmänt känd indikation; inga svenska godkännanden registrerade i datakällan) |
| Förutsagd ny indikation | Malign renovaskulär hypertoni (*malignant renovascular hypertension*) |
| TxGNN-förutsägelsepoäng | 99,01 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Isotretinoin verkar som agonist på RAR/RXR-kärnreceptorer (retinoidsignalvägen), vilket reglerar celldifferentiering och apoptos i bland annat talgkörtlar – grunden för dess effekt vid akne. Besläktade föreningar i retinoidklassen, särskilt all-trans-retinsyra (ATRA), har i djurexperiment visats kunna modulera renin-angiotensinsystemet (RAS): hämma reningenuttryck, dämpa TGF-β-medierad njurfibros och mildra ischemisk njurskada i gnagare. TxGNN-modellen verkar ha etablerat en länk via vägen **RAR-aktivering → RAS-hämning → kärlvidgning**, vilket teoretiskt kan vara relevant vid renovaskulär hypertoni.

Sambandet är dock genomgående indirekt. Befintliga data rör ATRA och liknande föreningar i djurmodeller – inte isotretinoin självt i kliniska eller humana njursjukdomssammanhang. Den patofysiologiska mekanismen vid malign renovaskulär hypertoni (kraftigt förhöjt blodtryck med ischemisk njurskada, fibrinoid vaskulär nekros) skiljer sig dessutom avsevärt från isotretinoins bevisade verkningsdomän.

En väsentlig säkerhetsparadox komplicerar bilden ytterligare: isotretinoin är känt för att kunna orsaka **intrakraniell hypertension (pseudotumor cerebri)** som biverkning, vilket direkt motverkar en hypertensiv indikation. TxGNN-modellens förutsägelse är mekanistiskt intressant men saknar klinisk förankring, och riktningen är potentiellt riskabel utan ytterligare säkerhetsdata. TxGNN-rankning 2 avser den nära besläktade indikationen *malignant hypertensive renal disease*, med identiskt förutsägelsepoäng och samma mekanistiska logik.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Isotretinoin har inga registrerade produktgodkännanden i den tillgängliga datakällan för Sverige (totalt 0 godkännanden). Produkten är klassad som **inte godkänd** på den svenska marknaden.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> **Viktig notering från återanvändningsanalysen:** Repurposing-rationalen i detta Evidence Pack lyfter explicit fram att isotretinoins kända biverkning – intrakraniell hypertension – utgör en direkt säkerhetskonflikt med en hypertensiv indikation. Detta bör beaktas redan i S0-fasen och inte vänta till formell säkerhetsgranskning.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsepoänget är högt (99,01 %), men förutsägelsen saknar helt kliniskt stöd (evidensnivå L5) och den hypotetiska mekanismen bygger uteslutande på djurdata för besläktade föreningar – inte för isotretinoin självt. Därtill skapar isotretinoins kända biverkningsprofil (intrakraniell hypertension) en principiell säkerhetskonflikt med hypertensiva indikationer som måste utredas innan vidare steg är motiverade.

**För att gå vidare krävs:**
- Strukturerade litteratursökningar: isotretinoin + renin-angiotensinsystem i humanstudier
- Formell säkerhetsgranskning av intrakraniell hypertension-risken i relation till den föreslagna indikationen
- Mekanistisk validering i relevanta cellulära eller djurmodeller för *malignant renovascular hypertension*
- Produktresumé/SPC för fullständig säkerhetsprofil (kontraindikationer, varningar, DDI)
- Utredning av om ATRA-data i djurmodeller är translaterbara till isotretinoin i klinisk kontext
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

