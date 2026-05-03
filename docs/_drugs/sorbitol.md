---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Skapar utvärderingsrapporten baserat på Evidence Pack JSON för Sorbitol. Data pekar på L5-evidens utan mekanistisk koppling, vilket ger beslutet "Avvakta".

---

# Sorbitol: Från osmotisk laxans till träningsinducerad malign hypertermi

## Sammanfattning

Sorbitol är en osmotiskt aktiv sockeralkohol som traditionellt används som laxans och hjälpämne i läkemedelsberedningar. TxGNN-modellen förutsäger med en poäng på 99,4 % att det kan vara effektivt mot **träningsinducerad malign hypertermi**, men detta stöds varken av kliniska prövningar eller vetenskaplig litteratur. Förutsägelsen saknar biokemiskt mekanistiskt stöd och bedöms med stor sannolikhet vara en strukturell falsk positiv i kunskapsgrafen.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerat som läkemedel i Sverige |
| Förutsagd ny indikation | Träningsinducerad malign hypertermi |
| TxGNN-förutsägelsepoäng | 99,4 % |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i datakällan. Baserat på känd farmakologi är sorbitol en sockeralkohol med osmotisk aktivitet: det drar vatten till tarmens lumen, ökar tarminnehållets volym och stimulerar tarmrörelser. Det används även som hjälpämne i läkemedelsberedningar och som sockerersättning vid diabetes.

Träningsinducerad malign hypertermi är ett sällsynt, potentiellt livshotande tillstånd vars patofysiologi är centrerad kring mutationer i ryanodinreceptorn 1 (RyR1). Dessa mutationer leder till okontrollerad frisättning av kalcium (Ca²⁺) från skelettmuskelns sarkoplasmatiska retikulum, vilket utlöser kraftig muskelrigiditet, hypertermi och metabolisk kris. Tillståndet behandlas i dag primärt med dantrolen, som direkt blockerar RyR1-receptorn.

Det finns ingen biologiskt plausibel koppling mellan sorbitols osmotiska verkningsmekanism och den kalciumkanalstörning som driver malign hypertermi. TxGNN:s höga poäng (99,4 %) härrör sannolikt från indirekta nodhopp i kunskapsgrafen – en länk via begreppen "hypertermi/cellsvullnad → osmotisk reglering" – snarare än en verklig farmakologisk effekt. Förutsägelsen klassificeras som en strukturell falsk positiv och saknar biokemiskt stöd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsen är klassad som L5 (enbart modellförutsägelse) och saknar stöd från kliniska prövningar, observationsstudier eller litteratur. Den mekanistiska länken mellan sorbitols osmotiska verkan och träningsinducerad malign hypertermi saknar biokemisk grund och bedöms vara ett artefakt från TxGNN:s kunskapsgrafstruktur snarare än en genuint läkemedelsterapi.

**För att gå vidare krävs:**
- Identifiering av en biologiskt plausibel verkningsmekanism som kopplar sorbitol till RyR1-medierad kalciumdysreglering i skelettmuskel
- Prekliniska in vitro- eller djurmodellstudier som påvisar effekt vid malign hypertermi
- Minst en fallrapport eller explorativ klinisk observation som stödjer hypotesen
- Inhämtning av fullständig produktinformation (SmPC) för säkerhets- och kontraindikationsbedömning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

