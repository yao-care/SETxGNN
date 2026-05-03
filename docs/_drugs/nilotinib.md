---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 1
---

# Nilotinib
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **1** st
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

Använder `txgnn-pipeline`-skillet för kontext. Nu genererar jag rapporten baserat på Evidence Pack.

---

# Nilotinib: Från kronisk myeloisk leukemi till dermatofibrosarkom

## Sammanfattning

Nilotinib är en andra generationens tyrosinkinashämmare (BCR-ABL/PDGFR-β/c-Kit) som ursprungligen användes för behandling av kronisk myeloisk leukemi (KML). TxGNN-modellen förutsäger att det kan vara effektivt mot **dermatofibrosarkom (DFSP)**, med **0 kliniska prövningar** och **1 publikation** som för närvarande stöder denna riktning. Den mekanistiska kopplingen via PDGFR-β-hämning är biologiskt välgrundad, men direkt klinisk evidens för Nilotinib vid DFSP saknas i nuläget.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Kronisk myeloisk leukemi (KML) |
| Förutsagd ny indikation | Dermatofibrosarkom (DFSP) |
| TxGNN-förutsägelsepoäng | 99,3% |
| Evidensnivå | L4 – Mekanismstudier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i Evidence Pack. Baserat på känd information är Nilotinib en andra generationens tyrosinkinashämmare som riktar sig mot BCR-ABL, PDGFR-β och c-Kit – med starkare bindningsaffinitet och bättre resistensprofil jämfört med sin föregångare Imatinib.

Dermatofibrosarkom (DFSP) orsakas av en t(17;22)-kromosomtranslokation som bildar en COL1A1–PDGFB-fusionsgen. Denna mutation leder till kontinuerlig autokrin aktivering av PDGFR-β-signalvägen, vilket driver tumörtillväxt. Nilotinibs direkta hämning av just PDGFR-β skapar därmed en direkt mekanistisk koppling till DFSP:s drivande onkogena mekanism.

Stöd för signalvägens kliniska relevans ges av att Imatinib – ett äldre preparat med överlappande målprofil – redan 2006 godkändes av FDA för behandling av DFSP. Detta bekräftar att PDGFR-β-hämning är en kliniskt validerbar strategi vid denna diagnos. Nilotinib har dokumenterat starkare hämningseffekt mot Imatinib-resistenta mutanter, vilket gör det till en teoretiskt lovande andralinjekandidat vid Imatinib-svikt – men direkta kliniska prövningsdata för Nilotinib vid DFSP saknas.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Översiktsartikel | Pharmacological Research | Genomgång av småmolekylära PDGFR-hämmares roll vid neoplastiska tillstånd; PDGF-familjen spelar central roll i cellproliferation via PDGFR-aktivering, med implikationer för PDGFR-drivna tumörer inklusive DFSP |

---

## Cytotoxicitet

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Målriktad terapi – Tyrosinkinashämmare (TKI), andra generationen |
| Myelosuppressionsrisk | Se produktresumén för varningar och försiktighetsåtgärder |
| Emetogenicitetsklassificering | Se produktresumén för varningar och försiktighetsåtgärder |
| Övervakningspunkter | Se produktresumén för varningar och försiktighetsåtgärder |
| Hanteringsskydd | Bör hanteras enligt gällande rutiner för cytotoxiska läkemedel |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Trots att TxGNN-modellen ger ett mycket högt förutsägelsepoäng (99,3%) och den mekanistiska kopplingen via PDGFR-β är biologiskt välgrundad, saknas det i nuläget registrerade kliniska prövningar för Nilotinib vid DFSP. Befintlig evidens stannar vid en enstaka översiktsartikel om PDGFR-hämmare generellt (L4), vilket är otillräckligt för vidare klinisk planering utan ytterligare underlag.

**För att gå vidare krävs:**
- Systematisk litteraturgenomgång av fallrapporter och fallserier där Nilotinib använts vid DFSP (retrospektiva data)
- Säkerhetsdata: Inhämtning av fullständig produktresumé och TFDA-varningstext för Nilotinib
- Utredning om pågående eller planerade investigator-initierade prövningar (IIT) för Nilotinib vid solida tumörer med PDGFR-aktivering
- Konsultation med sarkomspecialister för att bedöma klinisk behovsbild och jämföra med befintlig Imatinib-indikation för DFSP
- Vid positivt utfall av ovanstående: Design av en fas 2-prövning (single-arm, historisk kontroll) för Nilotinib som andralinjebehandling vid Imatinib-refraktär DFSP
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

