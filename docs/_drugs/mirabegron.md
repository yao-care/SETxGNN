---
noindex: true
sitemap: false
layout: default
title: Mirabegron
parent: Endast modellprediktion (L5)
nav_order: 93
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-03
predicted_indications: []
---

# Mirabegron
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **0** st
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

## MIRABEGRON: Repositioneringsbedömning — otillräckliga data för fullständig bedömning
{: .text-alpha }

## Sammanfattning

MIRABEGRON (DB08893) bedöms för närvarande med avseende på potential för läkemedelsrepositionering; dock returnerades varken data om ursprunglig indikation eller TxGNN-förutsagda indikationer i detta underlag.
Kritiska dataluckor — däribland verkningsmekanism och säkerhetsinformation från den regulatoriska produktresumén — klassas som **blockerande** eller av **hög** allvarlighetsgrad, vilket för närvarande förhindrar en fullständig bedömning.
Beslutet **Avvakta** rekommenderas tills luckorna nedan har åtgärdats.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Inte tillgänglig i nuvarande data |
| Förutsagd ny indikation | Inga TxGNN-förutsägelser returnerades |
| TxGNN-förutsägelsepoäng | — |
| Evidensnivå | L5 (endast modellprediktion — inga förutsägelser tillgängliga) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 5 av 5) |
| Antal godkännanden | 5 (giltiga: 5) |
| Rekommenderat beslut | **Avvakta** |

---

## Verkningsmekanism

Detaljerade data om verkningsmekanism finns inte i detta underlag (datalucka DG002, allvarlighetsgrad: hög).
Utan information om verkningsmekanismen går det inte att bedöma den biologiska rimligheten i någon förutsagd repositioneringsriktning eller koppla MIRABEGRONs farmakologiska profil till en ny terapeutisk indikation.

**Åtgärd krävs:** Fråga DrugBanks API efter DB08893 för att hämta verkningsmekanism, farmakodynamik och målinformation innan arbetet fortsätter.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

Data från produktresumén hämtades 2026-03-29 (sök-ID 4, status: lyckad), men fälten för varningar och kontraindikationer har ännu inte tolkats in i underlaget (datalucka DG001, allvarlighetsgrad: **blockerande**).
Data om läkemedelsinteraktioner efterfrågades men gav inga resultat.

**Åtgärd krävs:** Ladda ner och tolka produktresuméns PDF från den regulatoriska myndigheten för att extrahera viktiga varningar och kontraindikationer innan säkerhetsscreeningens steg 1 påbörjas.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Underlaget för MIRABEGRON innehåller inga förutsagda repositioneringsindikationer, ingen kartläggning av ursprunglig indikation, ingen verkningsmekanism och inga tolkade säkerhetsdata — varav två klassas som blockerande eller av hög allvarlighetsgrad, vilket hindrar en meningsfull bedömning från att gå vidare.

**För att gå vidare krävs:**

- **[Blockerande — DG001]** Tolka produktresuméns PDF (redan hämtad 2026-03-29) för att extrahera viktiga varningar, kontraindikationer och vägledning för särskilda patientgrupper; detta krävs innan säkerhetsscreeningens steg 1 kan påbörjas
- **[Hög — DG002]** Fråga DrugBanks API efter DB08893 för att hämta verkningsmekanism, farmakologiska mål och läkemedelskategori; detta krävs för analys av mekanistisk rimlighet
- **[Krävs]** Kör om TxGNN-förutsägelseflödet för MIRABEGRON för att fylla `predicted_indications`; det nuvarande underlaget innehåller en tom förutsägelselista, vilket gör det omöjligt att bedöma repositioneringskandidater
- **[Krävs]** Bekräfta de ursprungligen godkända indikationerna från regulatoriska källor (t.ex. EMA eller FDA) och fyll `original_indications` för att fastställa utgångsläget för repositionering
- **[Uppföljning]** När förutsägelser finns tillgängliga, starta om evidensinsamlingen (kliniska prövningar, litteratur) för den eller de högst rankade förutsagda indikationerna
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

