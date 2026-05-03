---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

Jag har läst in TxGNN-pipeline-skillet och analyserar nu Evidence Pack:et för Fulvestrant. Rapporten genereras nedan.

---

# Fulvestrant: Från bröstcancer till HIV-infektion

## Sammanfattning

Fulvestrant är en selektiv östrogenreceptordegraderare (SERD) som globalt är godkänd för behandling av hormonreceptorpositiv (HR+) avancerad bröstcancer hos postmenopausala kvinnor, men som ännu inte är godkänd på den svenska marknaden. TxGNN-modellen rankar **HIV-infektion** som den högst förutsagda nya indikationen med en poäng på 99,91%. Evidensunderlaget är dock ytterst svagt – det finns **inga registrerade kliniska prövningar** och den enda identifierade publikationen handlar om HTLV-1 (ett annat retrovirus), inte HIV – vilket tyder på att förutsägelsen med stor sannolikhet är en modellbaserad **falsk positiv** snarare än ett biologiskt underbyggt terapeutiskt samband.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej godkänd i Sverige (globalt: HR+/HER2-negativ avancerad bröstcancer) |
| Förutsagd ny indikation | HIV-infektion |
| TxGNN-förutsägelsepoäng | 99,91% |
| Evidensnivå | L4 |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Fulvestrant verkar som en selektiv östrogenreceptordegraderare: det binder till östrogenreceptorn (ERα) med hög affinitet, inducerar en konformationsförändring som markerar receptorn för proteasomal nedbrytning och stänger av ER-beroende gentranskription. Denna mekanism är specifikt designad för att eliminera östrogenreceptorsignalering i hormonberoende cancerceller – vilket förklarar dess etablerade effekt vid HR+ bröstcancer.

HIV-infektion drivs av ett helt annat biologiskt program: viruset binder CD4-receptorn och CCR5/CXCR4-koreceptorerna på T-celler, transkriberar sitt RNA-genom med ett eget omvänt transkriptas och integrerar sig i värdcellens DNA via ett viralt integras. Fulvestrants SERD-mekanism saknar alla kända interventionspunkter mot dessa steg i HIV:s replikationscykel.

TxGNN:s höga poäng för denna kombination härrör med stor sannolikhet från en **grafpropagationsartefakt**: den enda tillgängliga publikationen (PMID 40343334) studerar HTLV-1-associerad myelopati – ett neurologiskt tillstånd orsakat av ett *annat* retrovirus – och nämner HIV-behandlingsstrategier enbart som inspirationskälla. I TxGNN:s kunskapsgraf ligger HTLV-1- och HIV-noder nära varandra, vilket har spridit signalen till HIV-noden. Förutsägelsen bedöms sakna biologisk plausibilitet och utgör ett falskt positivt fynd.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Multi-kohort cross-omics | Research Square (preprint) | Systembiologisk analys av HTLV-1-associerad myelopati (HAM) – en neurologisk sjukdom orsakad av HTLV-1, *inte HIV*. Studien identifierar patogenesmekanismer och terapeutiska mål vid HAM, med HIV- och MS-strategier som referenspunkter. Ingen direkt koppling till Fulvestrant eller HIV-behandling. |

---

## Cytotoxicitet

Fulvestrant klassificeras som ett antineoplastiskt läkemedel (endokrin behandling) baserat på läkemedelsklass (SERD) och dess globala användning inom cancerbehandling.

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Målriktad terapi – endokrin behandling (selektiv östrogenreceptordegraderare, SERD); ej konventionellt cytotoxiskt agens |
| Myelosuppressionsrisk | Se produktresumén för varningar och försiktighetsåtgärder |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Övervakningspunkter | Se produktresumén för varningar och försiktighetsåtgärder |
| Hanteringsskydd | Hanteras enligt gällande riktlinjer för antineoplastiska läkemedel |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- TxGNN:s toppförutsägelse (HIV-infektion, 99,91%) bedöms som ett falskt positivt resultat orsakat av grafnodsnärhet mellan HTLV-1 och HIV i kunskapsgrafen. Det saknas fullständigt biologisk plausibilitet för en SERD-intervention mot HIV:s replikationscykel, och inget direkt kliniskt eller prekliniskt stöd existerar.

**För att gå vidare krävs:**
- Omvärdering mot alternativa indikationer med starkare biologisk plausibilitet – exempelvis **multipel endokrin neoplasi** (rang 2, 99,85%), där ER-uttryck i pNET och prolaktinom ger en mekanistisk grund och 50 indirekta kliniska prövningar identifierats
- Komplettering av MOA-data via DrugBank API (åtgärdspost DG002)
- Inhämtning av säkerhetsinformation från produktresumé / TFDA (åtgärdspost DG001) innan säkerhetsbedömning kan genomföras
- Litteratursökning med specificerade söktermer kopplade till SERD + respektive ny indikation för att bekräfta eller avfärda biologisk plausibilitet
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

