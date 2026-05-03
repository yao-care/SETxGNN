---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

Använder **txgnn-pipeline** för att säkerställa korrekt rapportstruktur för TxGNN-förutsägelser.

Skillet bekräftade projektkontexten. Nu analyserar jag Evidence Pack och genererar rapporten:

---

**Nyckelobs i data:**
- Rifaximin saknar godkännande i Sverige (0 licenser)
- Alla 6 förutsagda indikationer rör orala/lokala tillstånd → troligt klusterartefakt i kunskapsgrafen
- Den enda litteraturfyndet (PMID 34180023) är ett **negativt signal** – visar att Rifaximin *ökar* Candida-risk
- MOA och säkerhetsdata saknas ([Data Gap])
- Samtliga indikationer: evidensnivå L4–L5, rekommendation "Hold"

---

# Rifaximin: Från tarminfektioner till oral candidiasis

## Sammanfattning

Rifaximin är ett icke-absorberbart oralt bredspektrumantibiotikum som internationellt används för behandling av tarmrelaterade tillstånd som resenärsdiarré, hepatisk encefalopati och irritabel tarm med diarré. TxGNN-modellen förutsäger med 99,7 % poäng att det kan vara verksamt mot **oral candidiasis**, men den enda befintliga publikationen visar det *motsatta* – Rifaximin-användning är associerad med ökad risk för Candida-infektion. Läkemedlet är inte godkänt i Sverige och inga kliniska prövningar för denna indikation finns registrerade.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ej godkänd i Sverige; internationellt: tarminfektioner, hepatisk encefalopati, IBS-D |
| Förutsagd ny indikation | Oral candidiasis |
| TxGNN-förutsägelsepoäng | 99,7 % |
| Evidensnivå | L4 – men med negativ association (signal i fel riktning) |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | **Avvakta** |

---

## Varför är denna förutsägelse rimlig?

Detaljerad MOA-data saknas i det aktuella Evidence Pack. Baserat på etablerad farmakologi är Rifaximin ett rifamycinderivat med bred antibakteriell verkan som verkar uteslutande lokalt i tarmen – det absorberas minimalt (\<0,4 %) och uppnår inga systemiska plasmakoncentrationer av klinisk relevans.

Oral candidiasis orsakas av svamporganismer (*Candida albicans* m.fl.) och behandlas med antifungala läkemedel. Rifaximin har **ingen antifungal aktivitet** och kan inte rimligen förväntas verka mot ett svamptillstånd i munhålan. Läkemedlets antibakteriella mekanism – hämning av bakteriellt RNA-polymeras – saknar relevans för Candida.

Det enda befintliga vetenskapliga underlaget (PMID 34180023) visar faktiskt att Rifaximin-användning hos patienter som genomgick allogen stamcellstransplantation var associerad med *ökad* förekomst av mikafunginresistenta Candida-infektioner. Detta utgör ett **omvänt kausalitetssignal** – inte ett terapeutiskt stöd. Förutsägelsens höga TxGNN-poäng bedöms bero på att Candida-noder och orala sjukdomsnoder klustrar tätt i kunskapsgrafen, vilket ger en topologisk falsk positiv.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Retrospektiv observationsstudie | Annals of Hematology | Rifaximin-profylax hos allogen HSCT-patienter associerades med ökad förekomst av mikafunginresistenta Candida-infektioner – omvänt kausalitetssignal, inte terapeutiskt stöd |

> ⚠️ **Tolkningsvarning:** Denna studie stödjer **inte** Rifaximin som behandling mot oral candidiasis. Fyndet visar att Rifaximin-exposition ökar, inte minskar, Candida-risken.

---

## Säkerhetsaspekter

Säkerhetsdata (varningar, kontraindikationer, läkemedelsinteraktioner) saknas i det aktuella Evidence Pack. Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
TxGNN:s förutsägelse om Rifaximin mot oral candidiasis bedöms vara en **topologisk falsk positiv** i kunskapsgrafen – Rifaximin saknar antifungal aktivitet och den enda tillgängliga evidensen visar att läkemedlet ökar snarare än minskar risken för Candida-infektioner. Farmakologiska förutsättningar för vidare utredning saknas.

> **Mönsterobservation:** Samtliga 6 förutsagda indikationer i detta Evidence Pack (oral candidiasis, commissural lip fistula, osteoradionecrosis of mandible, oral leukoedema, burning mouth syndrome, candidiasis) rör orala/lokala tillstånd och erhåller alla rekommendationen "Hold" med evidensnivå L4–L5. Detta tyder på ett systematiskt klusterfel i kunskapsgrafen snarare än genuina återanvändningskandidater för ett tarmverkande antibiotikum.

**För att gå vidare krävs:**
- Ny förutsägelsekörning med omviktade nod-embeddings för att reducera oral-cluster-effekten
- Komplettering av MOA-data via DrugBank API (DG002)
- Komplettering av säkerhetsdata via Läkemedelsverkets produktresumé (DG001)
- Sökning mot Rifaximin:s faktiska indikationsdomäner (hepatisk encefalopati, IBS-D, tarmdekolonisering) för att identifiera mer plausibla återanvändningskandidater
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

