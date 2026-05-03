---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

Skill tillhör TxGNN-pipeline-infrastrukturen, ej rapportgenerering — detta täcks av systemprompten (v5). Skriver rapporten direkt utifrån Evidence Pack.

---

# Treprostinil: Från pulmonell arteriell hypertension till lungartäriovenös missbildning

---

## Sammanfattning

Treprostinil är ett syntetiskt prostacyklinanalogon som globalt används för behandling av pulmonell arteriell hypertension (PAH), men som ännu inte är godkänt eller marknadsförd i Sverige. TxGNN-modellen förutsäger att läkemedlet potentiellt kan vara effektivt mot **lungartäriovenös missbildning** (pulmonary arteriovenous malformation, PAVM), med ett förutsägelsepoäng på 99,70%. Evidensunderlaget för denna riktning är dock begränsat till enbart modellförutsägelsen — varken kliniska prövningar eller relevanta publikationer finns tillgängliga som direkt stöd, och den mekanistiska kopplingen bedöms som svag med potentiell risk för negativ effekt.

---

## Snabböversikt

| Post | Innehåll |
|---|---|
| Ursprunglig indikation | Pulmonell arteriell hypertension (PAH) – inte godkänd i Sverige |
| Förutsagd ny indikation | Lungartäriovenös missbildning (pulmonary arteriovenous malformation) |
| TxGNN-förutsägelsepoäng | 99,70% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd farmakologisk information är Treprostinil ett prostacyklinanalogon (PGI₂-analog) som verkar genom aktivering av IP-, DP₁-, EP₂- och FP-receptorer i lungkärlen. Läkemedlets effekt vid PAH bygger på tre verkningsmekanismer: vasodilation av lungartärerna, hämning av trombocytaggregation, samt antiproliferativa effekter på glatta muskelceller i kärlväggen.

Lungartäriovenös missbildning (PAVM) är strukturellt och patofysiologiskt fundamentalt annorlunda jämfört med PAH. PAVM innebär direkta, onormala förbindelser mellan lungartärer och lungvener som kringgår kapillärerna, vilket skapar ett höger-till-vänster-shunt med hypoxemi som konsekvens. Sjukdomsmekanismen beror på anatomisk kärlmissbildning — inte på förhöjt lungkärlsmotstånd eller kärlremodellering som vid PAH.

Den mekanistiska kopplingen bedöms som svag och potentiellt kontraindikerad: ett vasodilaterande läkemedel som Treprostinil kan teoretiskt öka shuntflödet vid PAVM och därigenom förvärra hypoxi snarare än lindra den. TxGNN:s höga förutsägelsepoäng förklaras sannolikt av att PAVM och PAH är grannskapsnoder i kunskapsgrafen (båda under lungkärls-sjukdomar), snarare än av en direkt mekanistisk koppling.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Treprostinil är inte godkänt eller marknadsförd i Sverige. Inga läkemedelsgodkännanden finns registrerade hos Läkemedelsverket (MPA).

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensunderlaget är begränsat till enbart modellförutsägelse (L5) utan stöd från kliniska prövningar eller publicerad litteratur. Dessutom pekar den mekanistiska analysen på att Treprostinils vasodilaterande verkningsmekanism kan vara kontraproduktiv vid PAVM, där ökad shuntning teoretiskt förvärrar hypoxemin — den centrala komplikationen vid denna sjukdom.

**För att gå vidare krävs:**
- Prekliniska mekanistiska studier som undersöker om IP-receptoragonister påverkar PAVM-shuntdynamik positivt eller negativt
- Uteslutande av risken för försämrad syresättning vid vasodilatoranvändning hos PAVM-patienter
- Sökning i specialiserad radiologisk och interventionell litteratur (PAVM behandlas primärt med embolisering, inte farmakologiskt)
- Fullständig produktresumé (FASS/EMA/FDA) för komplett säkerhetsprofil avseende Treprostinil
- Grundlig verifiering av TxGNN-modellens kunskapsgrafstruktur för att bekräfta om förutsägelsen baseras på mekanistisk likhet eller enbart topologisk grannskapsnärhet
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

