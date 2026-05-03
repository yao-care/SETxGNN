---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

Använder **txgnn-pipeline** för rapportgenerering av läkemedelsåteranvändning. Jag analyserar nu Evidence Pack för Ciprofloxacin och sammanställer rapporten enligt v5-mallen.

---

# Ciprofloxacin: Från bakterieinfektioner till diffus sklerodermi

## Sammanfattning

Ciprofloxacin är ett bredspektrumantibiotikum av fluorokinolonklassen som primärt används för behandling av bakterieinfektioner genom hämning av bakteriell DNA-replikation. TxGNN-modellen förutsäger att det kan vara effektivt mot **diffus sklerodermi** – en allvarlig autoimmun bindvävssjukdom med progressiv hudfibros och visceralt organengagemang. Evidensen stöds i nuläget av **inga registrerade kliniska prövningar** och **2 publikationer**, vilket placerar förutsägelsen på L4-nivå.

---

## Snabböversikt

| Post | Innehåll |
|------|---------|
| Ursprunglig indikation | Bakterieinfektioner (fluorokinolonantibiotikum) |
| Förutsagd ny indikation | Diffus sklerodermi |
| TxGNN-förutsägelsepoäng | 99,87% |
| Evidensnivå | L4 – Begränsad klinisk data / mekanistisk hypotes |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Ciprofloxacin verkar primärt bakteriedödande genom att hämma enzymen DNA-gyras (GyrA/GyrB) och topoisomeras IV (ParC/ParE) i bakterieceller, vilket stör bakteriell DNA-replikation och -reparation. Läkemedlet har lågt MIC-värde mot gramnegativa patogener, god oral biotillgänglighet (~70%) och bred vävnadspenetration.

Sambandet med diffus sklerodermi bygger på en **dubbel mekanismhypotes**. Den första är en möjlig **antifibrotisk effekt**: Ciprofloxacin kan potentiellt hämma MMP (matrismetalloproteinaser) samt TGF-β-nedströms signalvägar, vilket i teorin motverkar den karaktäristiska dermala fibrosen som driver sjukdomsförloppet vid sklerodermi. Den andra mekanismen är **tarminfektionskontroll**: patienter med systemisk skleros drabbas frekvent av SIBO (small intestinal bacterial overgrowth) som ett visceralengagemang, och Ciprofloxacin är ett välestablerat förstahandsalternativ vid SIBO – indirekt kan det lindra de gastrointestinala komplikationerna av sjukdomen.

Det är viktigt att understryka att den antifibrotiska mekanismen fortfarande är hypotetisk. Det finns ett enstaka dubbelblint pilot-RCT som specifikt undersökt oral Ciprofloxacin vid sklerodermi (Enríquez-Casillas et al., 2010), men evidensbasen är alltjämt begränsad. Ytterligare mekanistisk konfirmering och storskaliga kliniska studier krävs.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|-----------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Pilot-RCT | The Journal of Dermatology | Kontrollerad dubbelblind randomiserad pilotstudie som undersökte om oral Ciprofloxacin minskar svårighetsgraden vid sklerodermi – utvärderade antifibrotisk effekt i huden hos patienter med autoimmun bindvävssjukdom |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Diagnostisk/klinisk studie | British Journal of Rheumatology | Utredning av SIBO hos 24 patienter med systemisk skleros via jejunal aspiration; 20 patienter fick antibiotisk behandling – ger stöd för Ciprofloxacins roll vid tarmkomplikationer hos sklerodermi-patienter |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> ⚠️ **Kritisk säkerhetssignal från Evidence Pack:** FDA utfärdade 2016 ett obligatoriskt svart-ruta-varning för fluorokinoloner – inklusive Ciprofloxacin – avseende risk för **irreversibel perifer neuropati** (FQAD – Fluoroquinolone-Associated Disability). Eftersom patienter med diffus sklerodermi redan kan ha neuropatiska komplikationer som del av sjukdomsbilden, utgör detta en särskilt viktig säkerhetsaspekt som måste utredas noggrant vid eventuell vidare utvärdering.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Med enbart L4-evidens – ett enstaka pilot-RCT utan efterföljande konfirmering och en klinisk observationsstudie av SIBO-behandling – är evidensgrunden otillräcklig för att gå vidare till regulatorisk prövning. Den antifibrotiska mekanismen är biologiskt plausibel men inte styrkt i kontrollerade studier, och det kritiska säkerhetsproblemet med FQAD kräver särskild hänsyn för sklerodermi-populationen.

**För att gå vidare krävs:**
- Fullständig genomgång av pilotstudiens (PMID 20507401) primära utfall, effektstorlek och statistisk signifikans
- Prekliniska studier som direkt konfirmerar Ciprofloxacins MMP- och TGF-β-hämmande effekter i dermalt fibroskontext
- Inhämtning av fullständig produktresumé (SPC) med fokus på kontraindikationer, varningar och svart-ruta-data för FQAD
- Riskstratifiering för perifer neuropati specifikt för målpopulationen (sklerodermi-patienter)
- Registrering och genomförande av en prospektiv fas 2-studie dedikerad till diffus sklerodermi med fördefinierade effektmått
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

