---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

Använder **txgnn-pipeline** för rapportgenerering inom SeTxGNN-projektet. Genererar nu den svenska utvärderingsrapporten baserat på Evidence Pack för Dasatinib.

---

# Dasatinib: Från kronisk myeloisk leukemi till Ewing-sarkom

## Sammanfattning

Dasatinib är en oral multiriktad tyrosinkinashämmare som globalt är godkänd för behandling av kronisk myeloisk leukemi (KML) och Philadelphia-kromosom-positiv akut lymfoblastisk leukemi (Ph+ ALL), baserat på potent hämning av BCR-ABL-kinaskomplexet (325 gånger mer potent än imatinib). TxGNN-modellen förutsäger att Dasatinib kan vara effektivt mot **Ewing-sarkom**, med **3 kliniska prövningar** och **9 publikationer** som stöder denna riktning. Evidensnivån bedöms som L3 – det finns ett konsekvent prekliniskt mekanistiskt underlag och subgruppsdata från en avslutad fas 2-prövning, men klinisk bekräftelse saknas ännu.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Kronisk myeloisk leukemi / Ph+ ALL (globalt godkänt; ej registrerat i Sverige) |
| Förutsagd ny indikation | Ewing-sarkom |
| TxGNN-förutsägelsepoäng | 99,9% |
| Evidensnivå | L3 – Observationsstudier / Prekliniska mekanismstudier |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Detaljerad verkningsmekanismdata saknas i den aktuella datakällan. Baserat på känd information är Dasatinib en oral multiriktad tyrosinkinashämmare som hämmar BCR-ABL, Src-familjekinaser (Lck, Yes, Fyn), PDGFR-α/β samt c-Kit. Dess effekt vid KML och Ph+ ALL är väl dokumenterad, och mekanistiskt kan den vara tillämpbar på Ewing-sarkom genom samma Src/FAK-signalaxel.

Ewing-sarkom är en aggressiv bensarkom som drabbar framför allt barn och unga vuxna, med dålig prognos vid metastaserat stadium. Precliniska studier visar att tumörmikromiljöns stress aktiverar Src-kinaser i Ewing-sarkomceller och driver bildning av invadopodia, cellmigration och invasion via Src/FAK/Tenascin-C-axeln. Dasatinib hämmar denna axel direkt. Dessutom spelar c-Kit och PDGFR roll för Ewing-sarkomcellers proliferation och överlevnad – båda är erkända Dasatinib-mål.

Den mekanistiska kopplingen stöds av konsekventa prekliniska in vitro-fynd (inhibering av proliferation, migration och invadopodia-bildning i Ewing-sarkomcellinjer), men enkel-agent-aktivitet i kliniska fas 2-prövningar har hittills varit begränsad för sarkom totalt sett. Kombinationsstrategier och biomarkörbaserat patienturval identifieras som möjliga vägar framåt.

---

## Kliniska prövningar

| Prövningsnummer | Fas | Status | Deltagare | Viktiga fynd |
|-----------------|-----|--------|-----------|--------------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Fas 1/2 | Avslutad (förtidigt) | 7 | Dasatinib kombinerat med ifosfamid, karboplatin och etoposid för pediatriska sarkom inkl. Ewing-sarkom. Avbröts pga. rekryteringssvårigheter vid n=7. Ger inledande säkerhetssignaler men otillräckliga effektdata. Den hittills mest Ewing-specifika prövningen för Dasatinib. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Fas 2 | Avslutad | 366 | Den hittills störst Dasatinib-prövningen för avancerade sarkom, med Ewing-sarkom-subgrupp. Totalt sett begränsad enkel-agent-aktivitet (låg ORR för sarkom totalt). Specifika Ewing-subgruppsresultat kräver verifiering i originalpublikationen för att fastställa statistisk signifikans. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Fas 1 | Rekryterar | 41 | Autologa B7-H3 CAR-T-celler för refraktära solida tumörer inkl. Ewing-sarkom. Dasatinib används potentiellt som förstärkare av CAR-T-cellers minnesfenotup (hämning av tonic signaling). Dasatinib är sekundär intervention och direkta Ewing-sarkom-effektdata är begränsade. |

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preklinisk (in vitro) | Oncology Reports | Dasatinib hämmar proliferation och migration in vitro i neuroblastom- och Ewing-sarkomcellinjer via c-KIT- och PDGFR-inhibering. Direkta effektdata i Ewing-sarkomcellinjer. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preklinisk (in vitro) | Cancer Research | Dasatinib hämmar migration och invasion i multipla humana sarkomcellinjer och inducerar apoptos i bensarkomceller beroende av Src-kinaser. Grundläggande mechanistisk studie. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preklinisk/Translationell | Sarcoma | FAK-Src-komplexet som mål i DSRCT, Ewing-sarkom och rhabdomyosarkom. Enkel-agent Dasatinib misslyckades i fas 2; studien pekar mot kombinationsstrategier som lovande riktning. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preklinisk (mekanistisk) | Neoplasia | Tenascin C och Src samverkar för att driva invadopodia-bildning i Ewing-sarkom. Mikroenvironmentell stress aktiverar Src och ökar invasiv potential. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preklinisk (mekanistisk) | Neoplasia | Mikroenvironmentell stress inducerar Src-beroende aktivering av invadopodia och cellmigration i Ewing-sarkom – en potentiell central mekanism för metastasering. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Översikt | Oncology Letters | Src-kinasers roll i sarkombiologi och Src som potentiellt läkemedelsmål; diskuterar Dasatinibs tillämpbarhet vid sarkom. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preklinisk | Cell Communication and Signaling | CXCR4-antagonistbehandling i Ewing-sarkom aktiverar RTK-signalering. Ger bakgrundskontext för kombinationsstrategier riktade mot Ewing-sarkomets tumörbiologi. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Översikt | Current Treatment Options in Oncology | Systemisk behandling för kondrosarkom; Dasatinib nämns i bredare sarkomterapeutisk kontext. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Fallrapport | Case Reports in Oncology | Sällsynt kromosomabnormalitet vid KML-blastkris. Direkt relevans för Ewing-sarkom är begränsad; illustrerar Dasatinibs beteende vid komplexa hematologiska situationer. |

---

## Marknadsinformation Sverige

Dasatinib är för närvarande inte registrerat i Sverige (0 godkännanden). Läkemedlet marknadsförs globalt under handelsnamnet Sprycel® (Bristol Myers Squibb) för KML och Ph+ ALL, men saknar giltigt MPA-godkännande i Sverige per datainsamlingsdatum.

---

## Cytotoxicitet

Dasatinib klassificeras som ett antineoplastiskt läkemedel (tyrosinkinashämmare) och uppfyller kriterier för denna sektion baserat på indikation vid maligna hematologiska sjukdomar och Ewing-sarkom (malign bindvävstumör).

| Post | Innehåll |
|------|----------|
| Cytotoxicitetsklassificering | Målriktad terapi – andra generationens tyrosinkinashämmare (BCR-ABL / Src / PDGFR / c-Kit-hämmare) |
| Myelosuppressionsrisk | Medel – neutropeni, trombocytopeni och anemi rapporteras; grad 3–4 neutropeni förekommer hos ~30–50% i hematologiska indikationer; lägre risk förväntas vid solida tumörer |
| Emetogenicitetsklassificering | Låg (oral TKI; emetogenicitet klart lägre än konventionell cytotoxisk kemoterapi) |
| Övervakningspunkter | Komplett blodstatus (CBC) med differentialräkning, lever- och njurfunktionsprover, elektrolyter, EKG (QTc-förlängning), lungröntgen vid andningssymtom (pleural effusion rapporteras hos 14–35% av patienter under långtidsbehandling) |
| Hanteringsskydd | Standardförsiktighetsmått för cytotoxiska orala läkemedel; tabletter ska inte krossas eller delas av personal utan skyddsutrustning; gravida ska undvika hantering |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Notering: Varningar, kontraindikationer och läkemedelsinteraktioner (DDI) saknas i den aktuella datakällan. Officiell produktresumé (SmPC) för Sprycel® bör konsulteras för fullständig säkerhetsprofil innan kliniskt bruk.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån för Ewing-sarkom är L3 – det finns ett konsekvent och biologiskt trovärdigt prekliniskt underlag (Src/FAK/invadopodia-axeln), men den enda avslutade kliniska prövningen (NCT00464620, n=366) visade begränsad enkel-agent-aktivitet för sarkom totalt, och den mest direkta Ewing-specifika prövningen avbröts vid n=7. Klinisk bekräftelse är otillräcklig för att motivera vidare regulatorisk åtgärd i nuläget.

**För att gå vidare krävs:**
- Subgruppsanalys av Ewing-sarkom ur NCT00464620 för att fastställa specifika responsdata (ORR, PFS) i denna histologiska subtyp
- Biomarkörbaserat patienturval: kartläggning av Src/FAK-aktiveringsgrad som potentiell prediktiv faktor för behandlingssvar
- Prospektiv fas 1/2-prövning specifikt för Ewing-sarkom med kombinationsstrategi (Dasatinib + ifosfamid/karboplatin eller annan standardkemoterapi)
- Säkerhets- och farmakokinetikdata för den pediatriska populationen (majoriteten av Ewing-sarkomfall drabbar barn och unga vuxna)
- Inhämtning av fullständig säkerhetsinformation (varningar, kontraindikationer, DDI) från officiell produktresumé för komplett riskbedömning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

