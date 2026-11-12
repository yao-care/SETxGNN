---
layout: default
title: Diphenhydramine
parent: Endast modellprediktion (L5)
nav_order: 143
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "diphenhydramine"
predicted_indications: ["rosacea conjunctivitis"]
description: "Diphenhydramine: predikterad ny indikation Rosacea conjunctivitis (evidensnivå L5). Ursprunglig indikation: Inte angiven i de lokala uppgifterna"
---

# Diphenhydramine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

## Diphenhydramine: Rosacea conjunctivitis
{: .text-alpha }

---

## Sammanfattning

TxGNN-modellen förutsäger att det kan vara effektivt mot **rosaceakonjunktivit**, men det finns **inga kliniska prövningar** och **ingen publicerad litteratur** som stöder förutsägelsen. Evidensen består därmed enbart av en modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Rosacea conjunctivitis |
| TxGNN-förutsägelsepoäng | 0.9920 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 1 av 1) |
| Antal godkännanden | 1 (giltiga: 1) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Baserat på känd information är difenhydramin ett H1-receptorantagonist av första generationen. Dess effekt vid allergisk konjunktivit och rinit är väl känd, och mekanistiskt kan den lindra histaminmedierad klåda, rodnad och hyperemi i ögat.

Sambandet i kunskapsgrafen härrör sannolikt från att difenhydramin redan används vid flera inflammatoriska tillstånd på ögats yta. Modellen verkar alltså dra slutsatsen att rosaceakonjunktivit liknar dessa tillstånd.

Mekanismen är dock troligen **dåligt tillämpbar** här. Okulär rosacea drivs främst av dysfunktion i meibomska körtlar, instabil tårfilm samt neurovaskulär och medfödd immunologisk dysreglering (bland annat MMP, IL-1 och Demodex). Histamin spelar en mindre roll, så antihistaminer träffar sannolikt inte kärnan i sjukdomen. Difenhydramins antikolinerga effekt kan dessutom förvärra torra ögon, vilket redan är vanligt vid okulär rosacea. Den ursprungliga verkningsmekanismen saknas i underlaget och kunde därför inte kontrolleras mot DrugBank.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 3866 | Desentol (Viatris AB) | Oral lösning | Ingen indikationstext registrerad. Status: indragen |

Den enda registrerade beredningsformen är oral, vilket också är en brist för en okulär indikation (se nedan).

<!-- review:begin se-lic-20261106-diphenhydramine-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Det enda godkännandet är indraget, och ingen giltig produkt finns på den svenska marknaden. Den enda registrerade beredningsformen är oral, vilket också är en brist för en okulär indikation (se nedan).” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 1, varav giltiga: 1; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-diphenhydramine-1 -->

---

## Säkerhetsaspekter

**Läkemedelsinteraktioner:** Totalt 394 interaktioner har identifierats. Exempel på de mest betydelsefulla:

- **Allvarliga (Major):** kaliumcitrat och eliglustat.
- **Måttliga (Moderate):** antikolinerga läkemedel (atropin, hyoscyamin, glykopyrronium, dicyklomin, klidinium, mepenzolat, metskopolamin), opioider och opioidliknande (morfin, loperamid, eluxadolin), bupropion, lorcaserin, dronabinol, nabilon, metoklopramid och glycerolfenylbutyrat.

Många av de måttliga interaktionerna rör additiva antikolinerga eller sederande effekter.

Varningar och kontraindikationer från produktresumén saknas i underlaget. Se produktresumén för övrig säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellpoäng (L5) utan kliniska eller publicerade belägg, och den biologiska rimligheten är låg eftersom histamin spelar liten roll vid okulär rosacea. Difenhydramins antikolinerga effekt kan dessutom förvärra torra ögon.

**För att gå vidare krävs:**
- Hämta produktresumén från Läkemedelsverket (MPA) för varningar och kontraindikationer, vilket för närvarande blockerar säkerhetsgranskningen.
- Hämta verkningsmekanismen från DrugBank för att kunna analysera det mekanistiska sambandet.
- Göra en systematisk litteratur- och prövningssökning på difenhydramin eller andra antihistaminer vid okulär rosacea.
- Utreda beredningsform och administreringsväg, eftersom endast oral lösning finns och den är indragen.
- Överväga alternativ med bättre mekanistisk koppling, till exempel behandling av meibomska körtlar och antiinflammatorisk behandling.

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Det enda godkännandet är indraget, och ingen giltig produkt finns på den svenska marknaden” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

