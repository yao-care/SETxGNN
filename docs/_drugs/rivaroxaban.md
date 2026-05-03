---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **4** st
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

Jag använder **txgnn-pipeline**-skickligheten för att guida rapportgenereringen. Nu skriver jag utvärderingsrapporten baserat på Evidence Pack-datan.

---

# Rivaroxaban: Från venös tromboembolibehandling till reumatoid artrit

## Sammanfattning

Rivaroxaban är en direktverkande oral faktor Xa-hämmare som ursprungligen används för förebyggande och behandling av venös tromboembolism (DVT/lungembolism) samt strokeprevention vid förmaksflimmer. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **reumatoid artrit**, baserat på ett hypotetiskt samband mellan koagulationssystemets aktivering och synovial inflammation. Förutsägelsen stöds i nuläget av **0 kliniska prövningar** och **4 publikationer** – varav ingen är direkt utformad för att testa rivaroxaban som behandling mot reumatoid artrit.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej registrerad i Sverige (data ej tillgänglig i regulatorisk källa) |
| Förutsagd ny indikation | Reumatoid artrit |
| TxGNN-förutsägelsepoäng | 99,57 % |
| Evidensnivå | L4 – Mekanismstudier och indirekt litteratur |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata (MOA) saknas i nuvarande dataset (datakvalitetsbrist DG002). Baserat på tillgänglig information är rivaroxaban en direktverkande faktor Xa-hämmare. Faktor Xa är ett centralt enzym i koagulationskaskaden vars aktivering genererar trombin – ett enzym som inte enbart driver blodkoagulation, utan också binder till proteasaktiverade receptorer (PAR-1 och PAR-2) på immunceller och synoviala fibroblaster. Via PAR-2-signalering kan trombin förstärka lokal ledinflammation, vilket är patofysiologiskt relevant vid reumatoid artrit (RA).

Hos patienter med autoimmuna sjukdomar, däribland RA, har ett hyperkoagulerbart tillstånd dokumenterats med förhöjd trombingenerering (PMID 34175144). Den teoretiska grunden för återanvändning är att faktor Xa-hämning kan dämpa PAR-2-medierad synovialt inflammation utöver sin antitrombotiska effekt. Sambandet mellan den ursprungliga indikationen (tromboembolism) och den nya (RA) är således en gemensam biologisk aktör – trombin och koagulationssystemets inflammatoriska korsaktivering.

Det är viktigt att betona att detta resonemang är mekanistiskt och spekulativt. Ingen av de fyra identifierade publikationerna är utformad för att studera rivaroxaban specifikt vid reumatoid artrit. Förutsägelsen bör betraktas som en hypotesgenerande signal och kräver ytterligare preklinisk och klinisk validering innan den kan omvandlas till en konkret forskningsfråga.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|-----|-----------|--------------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Översikt av diagnos och behandling av DVT/lungembolism; incidens 88–112/100 000 personår, recidivfrekvens 20–36 % på 10 år – kontextuell bakgrund för rivaroxabans ursprungliga indikation |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Mekanistisk/Review | La Revue de médecine interne | Trombingenerationsanalys (TGA) vid autoimmuna sjukdomar; visar hyperkoagulerbarhet och förhöjd kardiovaskulär risk vid bl.a. antifosfolipidsyndrom – ger indirekt mekanistiskt stöd för koagulationssystemets roll vid autoimmun sjukdom |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Observationsstudie | PLoS ONE | Jämförelse av följsamhet till rivaroxaban vs. apixaban vid icke-valvulärt förmaksflimmer; belyser reala skillnader i behandlingsutfall mellan NOAK-preparat |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Fallrapport | Cureus | 88-årig kvinna med RA på orala steroider som drabbades av multipla emboliska händelser (ben och cerebralt) trots pågående antikoagulationsbehandling – illustrerar det komplexa samspelet mellan RA, trombosrisk och antikoagulationshantering |

---

## Marknadsinformation Sverige

Rivaroxaban är inte registrerat i Sverige enligt den regulatoriska källa som användes för detta Evidence Pack. Inga godkännanden eller produktresumér finns tillgängliga i dataunderlaget.

> **OBS:** Rivaroxaban (Xarelto®) är i klinisk praxis känt som ett etablerat läkemedel i Europa. Avsaknaden av data i detta underlag återspeglar sannolikt en begränsning i den datakälla som användes (TW-fokuserad regulatorisk databas), inte ett faktiskt marknadsstatus i Sverige. Manuell verifiering mot Läkemedelsverkets databas rekommenderas.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Varningsdata och kontraindikationer kunde inte hämtas från nuvarande datakälla (datakvalitetsbrist DG001: TFDA-produktresumé saknas). Läkemedelsinteraktionsdata kunde inte identifieras (DDI-sökning: inga träffar). Fullständig säkerhetsgranskning är ett krav innan klinisk utvärdering kan inledas.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån är L4 – det finns enbart mekanistiska resonemang och indirekt litteratur som stöd. Det saknas helt kliniska prövningar som direkt utvärderar rivaroxaban vid reumatoid artrit, och inget av de publicerade underlagen är utformat för detta ändamål. TxGNN-signalen (99,57 %) är stark men kan inte ensam motivera klinisk framryckning.

**För att gå vidare krävs:**
- Hämtning av fullständig produktresumé och säkerhetsdata via TFDA/Läkemedelsverket (åtgärda DG001) innan säkerhetsinledande utvärdering (S1) kan genomföras
- Verifiering av MOA-data via DrugBank API (åtgärda DG002) för att stärka mekanistisk analys
- Systematisk litteratursökning med utvidgade söktermer, t.ex. *"factor Xa inhibitor AND arthritis"*, *"PAR-2 AND synovial inflammation"*
- Identifiering av eventuella prekliniska djurstudier som direkt testar faktor Xa-hämning i artritmodeller
- Bedömning av om en explorativ fas 2-prövning kan motiveras om prekliniska fynd är tillräckligt robusta
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

