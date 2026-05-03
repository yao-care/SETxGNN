---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

Skillen är bekräftad. Nu genererar jag rapporten baserat på Evidence Pack JSON.

---

# Efavirenz: Från HIV-1-infektion till felint förvärvat immunbristsyndrom

## Sammanfattning

Efavirenz är ett non-nukleosidalt omvänt transkriptashämmare (NNRTI) som används för behandling av HIV-1-infektion hos människor. TxGNN-modellen förutsäger att det kan vara effektivt mot **felint förvärvat immunbristsyndrom** (feline acquired immunodeficiency syndrome, FIV-orsakad AIDS hos katter), med **1 direkt relevant publikation** som stöder denna riktning. Evidensbasen är dock begränsad till en enda in vitro-studie, och strukturella skillnader mellan FIV och HIV-1:s reversa transkriptas gör mekanistisk överförbarhet tveksam.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | HIV-1-infektion (känd klinisk indikation; läkemedlet är inte registrerat i Sverige och ingen godkänd indikationstext är tillgänglig i regulatorisk databas) |
| Förutsagd ny indikation | Felint förvärvat immunbristsyndrom (*feline acquired immunodeficiency syndrome*) |
| TxGNN-förutsägelsepoäng | 99,80 % |
| Evidensnivå | L4 – Preklinisk/in vitro-studie |
| Marknadsstatus i Sverige | Ej registrerat i Sverige |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande saknas detaljerad verkningsmekanismdata i den lokala databasen. Baserat på tillgänglig vetenskaplig information är efavirenz en NNRTI vars verkan är välkänd: läkemedlet binder till ett allosteriskt säte på HIV-1:s reversa transkriptas (RT) och blockerar därigenom viral DNA-syntes. Bindningsfickan på HIV-1 RT är beroende av nyckelkontaktrester, framför allt Tyr181 och Tyr188.

Felint immunbristvirus (FIV) är ett lentivirus som orsakar ett AIDS-liknande tillstånd hos katter och delar övergripande struktur med HIV-1. Trots denna ytliga likhet uppvisar FIV RT:s NNRTI-bindningsficka betydande strukturella skillnader jämfört med HIV-1 RT — de kritiska kontaktresterna Tyr181 och Tyr188 saknas i FIV RT. Detta innebär att majoriteten av NNRTI-preparat, inklusive efavirenz, förväntas ha minimal eller ingen aktivitet mot FIV.

Det höga TxGNN-förutsägelsepoänget (99,80 %) beror sannolikt på att modellens lokala kunskapsgraf saknar efavirenz dokumenterade godkända humanindikationer, vilket leder till en strukturell överskattning av kandidatens relevans. Den enda direkt relevanta publikationen (PMID 38031646, 2023) bekräftar just denna problematik genom biokemiska och strukturella jämförelser.

---

## Kliniska prövningar

Inga kliniska prövningar som direkt utvärderar efavirenz mot felint förvärvat immunbristsyndrom är registrerade. De två prövningar som identifierades vid sökning testar ett annat läkemedel (dolutegravir, GSK1349572) mot human HIV-1-infektion och har bedömts som ej relevanta (relevansnivå C) för denna indikation.

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fas 3 | Avslutad | 844 | Prövning av dolutegravir + abacavir/lamivudin jämfört med Atripla (efavirenz/emtricitabin/tenofovir) vid human HIV-1 hos antiretroviralt naiva vuxna. Testläkemedlet är dolutegravir, inte efavirenz, och indikationen är human HIV-1 — ej relevant för efavirenz vid katt-AIDS. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fas 2 | Avslutad | 208 | Dosurvalsstudie för dolutegravir vid human HIV-1-infektion. Samma begränsning som ovan — ej relevant för efavirenz vid katt-AIDS. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biokemisk och strukturell studie | *Journal of Veterinary Science* | Biokemiska och strukturella jämförelser av NNRTI (nevirapin, efavirenz, rilpivirin) mot FIV och HIV RT. Undersöker om NNRTI kan användas för behandling av FIV-infektion. Strukturella skillnader i NNRTI-bindningsfickan — avsaknad av nyckelkontaktrester i FIV RT — begränsar efavirenz aktivitet mot FIV. Enda direkt relevanta evidensen för denna indikation. |

---

## Marknadsinformation Sverige

Efavirenz är inte registrerat i Sverige och saknar godkänd produktinformation i tillgänglig regulatorisk databas. Inga licensuppgifter finns att redovisa.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån är L4 (en enda in vitro-studie) och den strukturella biologin talar aktivt *emot* efavirenz potential mot FIV — avsaknaden av nyckelkontaktrester i FIV RT:s bindningsficka innebär att NNRTI-klassen sannolikt saknar aktivitet mot det faktiska målviruset. Det höga TxGNN-poänget bedöms som ett modellartefakt.

**För att gå vidare krävs:**
- Farmakologisk bekräftelse av efavirenz aktivitet mot autentisk FIV RT (EC₅₀-mätning in vitro mot FIV-isolat, ej RT-SHIV-chimär)
- Strukturell analys av om modifierade NNRTI kan anpassas till FIV RT:s avvikande bindningsficka
- Djurexperimentella data i FIV-infekterade katter (ej SIV/RT-SHIV-modeller)
- Komplettering av efavirenz kända humanindikationer i TxGNN-kunskapsgraf för att korrigera modellartefakt och möjliggöra ny rankning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

