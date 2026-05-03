---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

Skill kontrollerad – `txgnn-pipeline` gäller pipeline-hantering och träning, ej rapportgenerering. Rapportinstruktionerna är fullt specificerade i systempromptens v5. Jag genererar nu rapporten direkt baserat på Evidence Pack.

---

# Gefitinib: Från icke-småcellig lungcancer till gingival fibromatos

## Sammanfattning

Gefitinib (Iressa®) är en selektiv EGFR-tyrosinkinashämmare som är godkänd på flera marknader globalt för behandling av EGFR-mutationspositiv icke-småcellig lungcancer (NSCLC), men är ej registrerad i Sverige. TxGNN-modellen förutsäger att läkemedlet kan vara effektivt mot **gingival fibromatos**, med en förutsägelsepoäng på **99,89 %** – dock saknas helt stödjande kliniska prövningar och publicerad litteratur för just denna indikation, vilket begränsar denna förutsägelse till evidensnivå L5.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | EGFR-mutationspositiv icke-småcellig lungcancer (NSCLC) – godkänd på flera internationella marknader, ej registrerad i Sverige |
| Förutsagd ny indikation | Gingival fibromatos (fibromatosis, gingival) |
| TxGNN-förutsägelsepoäng | 99,89 % |
| Evidensnivå | L5 – Endast modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej registrerad |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta evidenspaket. Baserat på känd information är gefitinib en selektiv hämmare av EGFR-tyrosinkinaset (epidermal tillväxtfaktorreceptor), som blockerar nedströms signalkaskader involverade i cellproliferation, apoptos och angiogenes. Läkemedlets kliniska effekt vid EGFR-mutationspositiv NSCLC är väldokumenterad i internationell litteratur och klinisk praxis, där exon 19-deletioner och L858R-punktmutationer utgör de primära prediktiva biomarkörerna.

Den teoretiska kopplingen till gingival fibromatos utgår från att EGFR-signalering deltar i regleringen av fibroblastproliferation i bindväv. I teorin skulle EGFR-hämning kunna dämpa den fibroblastöverproliferation som är karaktäristisk för sjukdomen. Emellertid är gingival fibromatos primärt orsakad av mutationer i gener som *SOS1* och *REST* – EGFR utgör inte den huvudsakliga patogena drivkraften i denna sjukdomsmekanism.

TxGNN:s höga poäng (0,9989) härrör sannolikt från topologisk grannskap i kunskapsgrafen mellan noder för fibrös vävnadsökning och EGFR-signalering, snarare än en direkt terapeutisk effektförutsägelse. Det saknas helt preklinisk och klinisk validering för denna indikation, varför förutsägelsen i nuläget inte har ett tillräckligt mekanistiskt eller empiriskt stöd för att motivera vidare klinisk utvärdering.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande.

---

## Cytotoxicitet

| Post | Innehåll |
|------|------|
| Cytotoxicitetsklassificering | Målriktad terapi – EGFR-tyrosinkinashämmare (TKI); ej konventionellt cytotoxisk |
| Myelosuppressionsrisk | Låg – EGFR-TKI:er ger sällan kliniskt signifikant benmärgssuppression jämfört med konventionell kemoterapi |
| Emetogenicitetsklassificering | Låg – oralt administrerat läkemedel med låg emetogen potential enligt MASCC/ESMO-klassificering |
| Övervakningspunkter | Leverfunktion (ASAT, ALAT, bilirubin); lungfunktion (risk för interstitiell lungsjukdom/pneumonit); hudtoxicitet (akneiform exantem, paronyki, xeros); EKG-övervakning (QTc-förlängning) |
| Hanteringsskydd | Se produktresumén för varningar och försiktighetsåtgärder |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensnivån är L5 – förutsägelsen baseras uteslutande på TxGNN-modellens topologiska analys av kunskapsgrafen och saknar helt stöd från kliniska prövningar eller publicerad litteratur. EGFR är dessutom inte den primära patogena drivkraften vid gingival fibromatos, vilket allvarligt begränsar den biologiska rimligheten i denna förutsägelse.

**För att gå vidare krävs:**
- Prekliniska studier (in vitro/in vivo) som kartlägger EGFR-expressionsnivåer och signalvägsinblandning i gingival fibromatos-vävnad
- Molekylär validering av om EGFR-hämning påverkar de primära patogena drivarna (*SOS1*/*REST*-mutationer)
- Fullständig säkerhetsdata inklusive varningar, kontraindikationer och läkemedelsinteraktioner (hämta TFDA-produktresumé från TFDA officiella webbplats)
- Verifiering av detaljerad verkningsmekanismdata via DrugBank API (DB00317)
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

