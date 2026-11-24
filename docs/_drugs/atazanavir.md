---
layout: default
title: Atazanavir
parent: Endast modellprediktion (L5)
nav_order: 42
evidence_level: L5
indication_count: 4
monitor_inn: "atazanavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-24
description: "Atazanavir: predikterad ny indikation Felint immunbristsyndrom hos katt (feline acquired immunodeficiency syndrome) (evidensnivå L5). I Sverige, godkännanden (Läkemedelsverket): 2 (giltiga: 2)"
---

# Atazanavir
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

## Atazanavir: proteashämmare → felint immunbristsyndrom hos katt (feline acquired immunodeficiency syndrome)
{: .text-alpha }

---

### Sammanfattning

Atazanavir är en proteashämmare. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **felint immunbristsyndrom hos katt (feline acquired immunodeficiency syndrome)**, med poängen 0,9998. För denna förutsägelse finns **inga kliniska prövningar** och **ingen publicerad litteratur** i de data som sammanställts för rapporten, så underlaget består enbart av modellens förutsägelse.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Inte angiven i de lokala uppgifterna |
| Förutsagd ny indikation | Felint immunbristsyndrom hos katt (feline acquired immunodeficiency syndrome) |
| TxGNN-förutsägelsepoäng | 0,9998 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

Enligt avsnitten ”Mechanism of Action” och ”Microbiology” i den produktinformation som godkänts av amerikanska FDA (Prescribing Information) för Atazanavir (inofficiell översättning): ”Atazanavir är ett antiretroviralt läkemedel mot HIV-1. […] Atazanavir (ATV) är en azapeptidisk HIV-1-proteashämmare (PI). Substansen hämmar selektivt den virusspecifika processningen av virala Gag- och Gag-Pol-polyproteiner i HIV-1-infekterade celler och förhindrar därmed bildningen av mogna virioner.” Engelsk originaltext: "Atazanavir is an HIV-1 antiretroviral drug. […] Atazanavir (ATV) is an azapeptide HIV-1 protease inhibitor (PI). The compound selectively inhibits the virus-specific processing of viral Gag and Gag-Pol polyproteins in HIV-1-infected cells, thus preventing formation of mature virions." ([DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8), version från 2024-12-05; hämtad 2026-11-19). Atazanavir är en proteashämmare som används mot hivinfektion, och mekanistiskt kan den vara tillämpbar på felint immunbristsyndrom.

Felint immunbristvirus (FIV) är ett lentivirus med ett aspartylproteas som är besläktat med hiv-1-proteaset. Därför är det tänkbart att en proteashämmare som atazanavir kan påverka även detta virus. Den höga poängen speglar sannolikt likheten med hivsjukdom i modellens underliggande data.

Det finns dock en viktig begränsning: FIV-proteaset skiljer sig från hiv-1-proteaset i substratspecificitet, och känslighet för hämmaren kan därför inte antas. Förutsägelsen är i nuläget enbart en hypotes.

---

### Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

### Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

### Marknadsinformation Sverige

<!-- licenses:begin -->

| Godkännandenummer | Produktnamn | Beredningsform | Innehavare | Status |
|------|------|------|------|------|
| 56659 | Atazanavir STADA | Kapsel, hård | STADA Arzneimittel AG | Godkänd |
| 56658 | Atazanavir STADA | Kapsel, hård | STADA Arzneimittel AG | Godkänd |

Källa: Läkemedelsverket (godkännandenummer, läkemedelsnamn, läkemedelsform, innehavare och registreringsstatus enligt Läkemedelsverkets uppgifter).

<!-- licenses:end -->

Läkemedlet har enligt lokala data marknadsstatusen "Marknadsförd". Båda registrerade godkännandena avser enkelsubstansprodukter från STADA Arzneimittel AG.

---

### Säkerhetsaspekter

**Läkemedelsinteraktioner:** Totalt 277 interaktioner är registrerade. Bland de som listats finns följande med högre allvarlighetsgrad (Major):
- Famotidin
- Ranitidin
- Rabeprazol
- Omeprazol
- Loperamid
- Triamcinolon
- Budesonid

Flera interaktioner med måttlig allvarlighetsgrad (Moderate) finns också, bland annat med acarbos, metformin, pioglitazon, hydrokortison, aprepitant och kalciumkarbonat.

Produktresumén bör läsas för fullständig säkerhetsinformation, eftersom varnings- och kontraindikationstext inte finns i de sammanställda data.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på modellens poäng (0,9998), utan någon klinisk prövning eller publikation som studerar felint immunbristsyndrom. Skillnader mellan FIV- och hiv-proteas gör att effekt inte kan förutsättas.

**För att gå vidare krävs:**
- Laboratoriestudier av atazanavirs hämning av FIV-proteas
- Prekliniska eller veterinärmedicinska studier som visar antiviral effekt
- Kompletterande uppgifter om verkningsmekanism och säkerhet från produktresumén
- Bedömning av om humanläkemedel är lämpligt för veterinärt bruk ur regulatorisk synvinkel

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för denna sida. Meningen om att data om verkningsmekanismen inte var tillgängliga har ersatts med ett utdrag ur den angivna officiella produktinformationen (med inofficiell översättning); modellens förutsägelser, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-19 | Meningen ”data om verkningsmekanismen saknas” ersatt med utdrag ur amerikansk produktinformation | Mening om att data om verkningsmekanismen saknades ersatt med ett utdrag med källa | [DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

