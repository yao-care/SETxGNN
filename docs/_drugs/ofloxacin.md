---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

Använder `txgnn-pipeline`-riktlinjerna och systemprompten för rapporten. Analyserar Evidence Pack och genererar rapporten nu.

---

# Ofloxacin: Från bakteriella infektioner till polyklonal hyperviskositetssyndrom

## Sammanfattning

Ofloxacin är ett bredspektrumantibiotikum inom fluorokinolonklassen som ursprungligen används för att behandla bakteriella infektioner i urinvägar, luftvägar, hud och ögon. TxGNN-modellen förutsäger att det kan vara effektivt mot **polyklonal hyperviskositetssyndrom** med ett förutsägelsepoäng på 99,91 %, men **inga kliniska prövningar och inga publikationer** stöder för närvarande denna indikation – förutsägelsen grundar sig uteslutande på modellberäkning (evidensnivå L5).

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Bakteriella infektioner (urinvägsinfektion, luftvägsinfektion, ögoninfektion, hud- och mjukdelsinfektioner) |
| Förutsagd ny indikation | Polyklonal hyperviskositetssyndrom |
| TxGNN-förutsägelsepoäng | 99,91 % |
| Evidensnivå | L5 – enbart modellförutsägelse, inga kliniska studier |
| Marknadsstatus i Sverige | Ej godkänd, ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd farmakologi är ofloxacin ett fluorokinolonantibiotikum vars verkningsmekanism bygger på hämning av bakteriellt DNA-gyras (topoisomeras II) och topoisomeras IV. Enzymhämningen förhindrar bakteriell DNA-replikation och transkription, vilket ger baktericid effekt mot ett brett spektrum av organismer – däribland *Enterobacteriaceae*, *Staphylococcus aureus*, *Chlamydia* och *Yersinia pestis*.

Polyklonal hyperviskositetssyndrom uppstår när flera B-cellskloner reaktivt producerar stora mängder immunoglobuliner, vilket höjer plasmaviskositeten och kan leda till cirkulationssvikt. Det finns ingen känd biologisk koppling mellan hämning av bakteriellt DNA-gyras och reglering av immunoglobulinproduktion, B-cellsaktivering eller blodviskositet. Sambandet mellan ofloxacins primära verkningsmekanism och den förutsagda sjukdomsmekanismen saknas därmed på molekylär nivå.

Modellförutsägelsen baseras på kunskapsgrafassociationer som kan spegla indirekta nätverkskopplingar snarare än direkt biologisk aktivitet. Prognosen för polyklonal hyperviskositetssyndrom bedöms som biologiskt osannolik och kräver grundläggande mekanistisk validering innan vidare överväganden är motiverade.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Marknadsinformation Sverige

Ofloxacin är inte godkänt och marknadsförs inte i Sverige. Inga produktlicenser är registrerade hos Läkemedelsverket.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivå L5 innebär att enbart TxGNN-modellförutsägelsen stöder indikationen polyklonal hyperviskositetssyndrom. Ingen biologiskt trovärdig verkningsmekanism har identifierats och inga kliniska studier finns tillgängliga för denna indikationskombination – vidare utredning är inte motiverad utan föregående mekanistisk validering.

> **Notering om övriga förutsägelser i detta evidenspaket:** Två andra indikationer uppvisar avsevärt starkare stöd och kan vara mer lämpliga för prioritering. *Septikemisk pest* (rang 8, evidensnivå L3) har direkta djurdata med ofloxacin mot *Yersinia pestis* och rekommenderas "Proceed with Guardrails". *Monoklonal gammopati* (rang 6, evidensnivå L3) stöds av en Fas 3 RCT (TEAMM-studien) med levofloxacin – ofloxacins L-enantiomer med identisk verkningsmekanism – och rekommenderas "Research Question".

**För att gå vidare krävs:**
- Formulering av en biologiskt trovärdig hypotes som kopplar fluorokinoloner till immunoglobulinreglering eller plasmaviskositet
- Prekliniska studier (in vitro/in vivo) för att bekräfta eventuell biologisk aktivitet mot polyklonal hyperviskositetssyndrom
- Inhämtning av fullständig säkerhetsprofil via produktresumén (SmPC): varningar, kontraindikationer och kliniskt relevanta läkemedelsinteraktioner
- Komplettering av MOA-data via DrugBank-API (åtgärda datagap DG002) och hämtning av TFDA-produktresumé (DG001)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

