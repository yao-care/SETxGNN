---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **2** st
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

Jag har läst in `txgnn-pipeline`-skillet. Nu genererar jag rapporten baserat på Evidence Pack JSON:et.

---

# Biotin: Från biotinbrist till dyspepsi

## Sammanfattning

Biotin (vitamin B7) är ett vattenlösligt essentiellt vitamin som kliniskt används vid behandling av biotinbrist. TxGNN-modellen förutsäger att det kan vara effektivt mot **dyspepsi** (funktionell matsmältningsstörning), med **2 registrerade kliniska prövningar** och **7 publikationer** som för närvarande berör detta område. Evidensunderlaget är dock indirekt — ingen av de identifierade studierna undersöker Biotin som enskild behandling vid dyspepsi, och förutsägelsen kräver grundläggande experimentell validering.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Biotinbrist |
| Förutsagd ny indikation | Dyspepsi |
| TxGNN-förutsägelsepoäng | 99,43 % |
| Evidensnivå | L4 – Mekanismstudier / indirekt evidens |
| Marknadsstatus i Sverige | Inte godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata (MOA) saknas för närvarande i tillgängliga databaser. Baserat på känd information är Biotin (vitamin B7) ett essentiellt koenzym som deltar i flera karboxyleringsreaktioner centrala för energiomvandling, metabolism av fettsyror, aminosyror och glukos. Det är välkänt att biotin krävs för normal funktion hos celler i tarmepitelet, och att tarmfloran kan syntetisera begränsade mängder biotin.

Sambandet mellan biotin och dyspepsi bygger på ett indirekt mekanistiskt resonemang: biotinbrist har i fallrapporter associerats med gastrointestinala symtom, och gastrointestinal slemhinnans integritet kan teoretiskt påverkas av biotinstatus. En publikation (PMID 25384804) visade att patienter med funktionell dyspepsi efter H. pylori-eradikering hade nytta av ett kombinerat kosttillskott innehållande B-vitaminer, vilket utgör ett svagt indirekt mekanistiskt stöd.

Det saknas däremot helt verifierade hypoteser eller studier om Biotin som enskild behandlingsintervention vid dyspepsi. Förutsägelsen bör betraktas som ett tidigt explorativt signalspår och inte som evidens för klinisk tillämpning.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Avslutad | 99 | Studerade absorption av transdermala vitaminer (inkl. biotin) hos patienter efter bariatrisk kirurgi. Primärt utfall var serumkoncentrationer av mikronäringsämnen — ingen direkt koppling till dyspepsibehandling. Biotin ingick som ett passivt observationsmått. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Fas 2/3 | Okänd | 150 | Jämförelse av oxykodon vs. pregabalin som preemptiv analgesi vid postoperativ smärta. Ingen koppling till biotin eller dyspepsi — trolig felklassificering vid datamatchning. Prövningsstatus okänd, vilket sänker tillförlitligheten ytterligare. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Interventionsstudie | Minerva Gastroenterologica e Dietologica | Öppen multicenterstudie av patienter med funktionell dyspepsi efter H. pylori-eradikering. Kombinerat kosttillskott med B-vitaminer (inkl. biotin) visade positiv effekt på symtom och livskvalitet. Starkaste indirekta stödet i evidenspaketet, men biotin studerades inte isolerat. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Fallrapport | The Journal of Dermatology | Spädbarnsfall med biotinbrist hos patient med diagnostiserad dyspepsi som enbart matades med aminosyrabaserad formel. Serum- och urinbiotinnivåer under normalvärdet. Illustrerar en möjlig koppling mellan biotinstatus och gastrointestinala symtom. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Interventionsstudie | Experimental & Clinical Gastroenterology | Utvärderade effekt av kosttillskott innehållande bl.a. biotin, inulin och oligofruktos vid tarmmikrobiotarubbningar hos patienter med bronkopulmonell sjukdom under antibiotikabehandling. Biotin ingick som del av ett kombinerat preparat. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observationsstudie | International Journal of Molecular Medicine | Undersökte magsäckens antrum-endokrina celler hos IBS-patienter jämfört med friska kontroller. Ingen direkt koppling till biotin — inkluderades troligen pga. överlapp med dyspepsirelaterade GI-tillstånd. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observationsstudie | World Journal of Gastrointestinal Endoscopy | Studerade endokrina celltyper i magslemhinnans oxyntiska mukosa hos IBS-patienter. Ingen direkt koppling till biotin. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observationsstudie | Journal of Clinical Pathology | Undersökte IL-10 vid H. pylori-associerad gastrit och dess roll i reglering av proinflammatoriska cytokiner. Ingen direkt koppling till biotin. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observationsstudie | Kidney International | Studerade tunntarmsmukosa vid IgA-nefropati med fokus på inflammationstecken. Ingen direkt koppling till biotin eller dyspepsi. |

---

## Säkerhetsaspekter

> Se produktresumén för säkerhetsinformation. Inga kända läkemedelsinteraktioner identifierades vid sökning i tillgängliga interaktionsdatabaser.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensunderlaget är klassificerat som L4 och bygger uteslutande på indirekta mekanistiska kopplingar och studier där biotin ingår som en komponent i kombinationspreparat. Ingen klinisk prövning eller publikation undersöker biotin som enskild intervention mot dyspepsi, och modellförutsägelsen (TxGNN-poäng 99,43 %) kan ännu inte omvandlas till ett kliniskt beslut.

**För att gå vidare krävs:**
- Komplettering av biotins verkningsmekanism (MOA) via DrugBank API och litteraturanalys
- Inhämtning av fullständig produktresumé (SPC) och officiella säkerhetsdata för att möjliggöra S1 säkerhetsinitial­bedömning
- Identifiering eller design av en riktad preklinisk studie som undersöker biotins effekt specifikt på gastrointestinal slemhinna eller dyspepsisymtom
- Bedömning av biologisk plausibilitet i samråd med gastroenterologisk expertis, som underlag inför eventuell Fas 1/2-prövning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

