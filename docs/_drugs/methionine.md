---
layout: default
title: Methionine
parent: Endast modellprediktion (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
monitor_inn: "methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
last_modified_at: 2026-10-23
description: "Methionine: predikterad ny indikation Akne (evidensnivå L5). Ursprunglig indikation: Ingen indikationstext angiven i de svenska godkännandena i underlaget"
---

# Methionine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **10** st
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

## Metionin: Från ej angiven godkänd indikation till akne
{: .text-alpha }

---

## Sammanfattning

Metionin är en essentiell aminosyra som i Sverige ingår i flera godkända infusionsvätskor, bland annat Glavamin. Den insamlade informationen anger ingen godkänd indikationstext för dessa produkter. TxGNN-modellen förutsäger att metionin kan vara effektivt mot **akne**, men det finns **0 kliniska prövningar** och endast **2 publikationer** med ett indirekt samband. Ingen av dem prövar metionin som behandling.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ingen indikationstext angiven i de svenska godkännandena i underlaget |
| Förutsagd ny indikation | Akne |
| TxGNN-förutsägelsepoäng | 99,9996 % |
| Evidensnivå | L5 (endast modellförutsägelse, ingen studie som direkt prövar metionin vid akne) |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: minst 20) |
| Antal godkännanden | Minst 20 godkännanden (listan kan vara ofullständig) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig. Metionin är en svavelhaltig aminosyra som ingår i kroppens normala proteinomsättning. Den är också en förstadie till homocystein via metionincykeln. Mekanistiskt kan den därför tänkas påverka processer som rör enkolsmetabolism, men detta är inte belagt för akne.

Det enda stödet från litteraturen är en studie från 2001. Den visade förhöjda homocysteinnivåer hos patienter som behandlades med isotretinoin mot cystisk akne. Det kopplar aknebehandling till enkolsmetabolism, men bara indirekt. Studien visar inte att metionintillskott lindrar akne. Eftersom metionin kan höja homocystein är det dessutom ett möjligt säkerhetsproblem och inte en uppenbar fördel.

Den höga modellpoängen är en beräkningsmässig förutsägelse och bör inte tolkas som kliniskt stöd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Kohortstudie | International Journal of Dermatology | Förhöjda homocysteinnivåer i plasma hos patienter som behandlades med isotretinoin mot cystisk akne. Studien rör biverkningar av isotretinoin, inte metionin som behandling. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Fallrapport | BMJ Case Reports | Ny MTHFR-mutation hos en nyfödd med encefalopati, håravfall och marfanoida drag. Neonatal akne nämns som ett av flera hudfynd. Rapporten har ingen relevans för behandling av akne med metionin. |

---

## Marknadsinformation Sverige

Produkterna nedan innehåller metionin som en av flera komponenter i aminosyra- eller näringslösningar. De beskriver inte hur metionin som enskild substans är godkänt. Listan visar fem av minst 20 godkännanden och kan vara ofullständig. Indikationstext saknas i det insamlade underlaget.

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 12526 | Glavamin | Infusionsvätska, lösning | Ej angiven i underlaget |
| 18399 | StructoKabiven Elektrolytfri | Infusionsvätska, emulsion | Ej angiven i underlaget |
| 10096 | Vamin 18 g N/l elektrolytfri | Infusionsvätska, lösning | Ej angiven i underlaget |
| 10095 | Vamin 14 g N/l elektrolytfri | Infusionsvätska, lösning | Ej angiven i underlaget |
| 12423 | Nutrineal PD4 1,1 % Aminosyror | Peritonealdialysvätska | Ej angiven i underlaget |

---

## Säkerhetsaspekter

- **Relationer i kunskapsgrafen (inte produkttext):** I TxGNN:s kunskapsgraf finns kontraindikationsrelationer mellan metionin och bland annat hypertoni, njursjukdom (inklusive kronisk njursvikt och slutstadium), diabetes och diabetisk ketoacidos, hyperkalcemi, sarkoidos, hjärt-kärlsjukdom, hyperlipidemi, njursten, fenylketonuri och rubbningar i fenylalaninomsättningen. Digitalisförgiftning och kammarflimmer finns också bland dem. Detta är inte hämtat från läkemedelsinformation och måste verifieras mot produktresumén.
- **Läkemedelsinteraktioner (5 identifierade):**
  - **Aktivt kol:** måttlig
  - **Efedrin:** lindrig
  - **Pseudoefedrin:** lindrig
  - **Meciletin:** lindrig
  - **Flekainid:** lindrig
- **Homocystein:** Metionin ingår i omsättningen till homocystein. Förhöjt homocystein är kopplat till kärlsjukdom, vilket är relevant för all användning utanför nuvarande indikationer.

Se produktresumén för fullständig säkerhetsinformation. Varningar och kontraindikationer från produkttexten saknas i underlaget.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Det finns inga kliniska prövningar och ingen studie som undersöker metionin vid akne, så evidensnivån är L5. Det enda stödet är en modellpoäng och ett indirekt homocysteinfynd, och en höjning av homocystein kan vara ofördelaktig.
- Övriga förutsägelser (framför allt olika typer av katarakt och diabetesretinopati) har likaså ingen klinisk evidens. Det finns endast prekliniska eller mekanistiska arbeten, främst om oxidation och metioninsulfoxidreduktas i linsen. Inget av dem prövar metionin som behandling.

**För att gå vidare krävs:**
- Hämta produktresumé med varningar, kontraindikationer och godkända indikationer från Läkemedelsverket. Detta är ett blockerande underlag för säkerhetsbedömning.
- Komplettera verkningsmekanismen från DrugBank.
- Genomför prekliniska studier av om metionin påverkar aknerelaterade mekanismer, och i så fall i vilken riktning.
- Utvärdera homocysteinrisken och lämplig beredningsform och administreringsväg för akne. Nuvarande godkända produkter är infusions- och dialysvätskor.
- Först därefter kan en liten explorativ klinisk studie övervägas.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

