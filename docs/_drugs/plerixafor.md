---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **7** st
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

The txgnn-pipeline skill is focused on pipeline management, not report generation. The system prompt contains all necessary instructions. Proceeding directly with the report.

---

# Plerixafor: Från stamcellsmobilisering till inert plasmacellsmyelom

## Sammanfattning

Plerixafor är en CXCR4-receptorantagonist som ursprungligen godkänts internationellt för mobilisering av hematopoetiska stamceller hos patienter med multipelt myelom och non-Hodgkin-lymfom inför autolog transplantation. TxGNN-modellen förutsäger med en poäng på **99,97%** att läkemedlet kan vara effektivt mot **inert plasmacellsmyelom (smoldering myeloma)**, baserat på biologisk plausibilitet via CXCL12–CXCR4-axeln. För närvarande finns varken **kliniska prövningar** eller **publicerade studier** som direkt stödjer denna specifika behandlingsindikation, och evidensnivån stannar vid L5.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Stamcellsmobilisering vid multipelt myelom och non-Hodgkin-lymfom (internationellt godkänd; ej registrerad i Sverige) |
| Förutsagd ny indikation | Inert plasmacellsmyelom (indolent plasma cell myeloma / smoldering myeloma) |
| TxGNN-förutsägelsepoäng | 99,97% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Ej marknadsförd |
| Antal godkännanden i Sverige | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande saknas detaljerad verkningsmekanismdata i det tillgängliga underlaget. Baserat på känd farmakologi är Plerixafor (AMD3100) en selektiv antagonist mot CXCR4-receptorn som blockerar bindningen av CXCL12 (även kallat SDF-1α). Dess godkända effekt vid stamcellsmobilisering har väl bevisats: blockad av CXCR4 lösgör hematopoetiska stamceller från benmärgens nischer och driver dem ut i perifert blod för skörd.

Det biologiska sambandet med inert plasmacellsmyelom grundar sig på att plasmacellsmyelomceller i hög grad uttrycker CXCR4. CXCL12–CXCR4-axeln driver deras hemning till benmärgens skyddande mikromiljö och bidrar till deras överlevnad och kemoterapiresistens. Teoretiskt kan CXCR4-blockad med Plerixafor störa detta skyddande mikromiljöberoende, på samma sätt som vid AML-strategin där läkemedlet mobiliserar leukemiceller för att göra dem känsligare för cytotoxisk behandling.

Dock är inert plasmacellsmyelom (SMM) ett distinkt förstadium som skiljer sig väsentligt från aktivt multipelt myelom: SMM-patienter behandlas i dag vanligen med "watch and wait"-strategi eller riskbaserad intervention. Det finns inga publicerade kliniska prövningar eller litteratur som specifikt undersöker Plerixafor som direkt behandlingsmedel vid SMM. Sambandet stannar vid mekanistisk plausibilitet och modellförutsägelse – klinisk validering saknas helt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande för indikationen inert plasmacellsmyelom.

---

## Litteraturbevis

Ingen relaterad litteratur tillgänglig för närvarande för indikationen inert plasmacellsmyelom.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Evidensnivån är L5 – det finns varken kliniska prövningar eller publicerade studier som stödjer Plerixafor som direkt behandling vid inert plasmacellsmyelom. Den höga TxGNN-poängen (99,97%) speglar stark bioinformatisk plausibilitet via CXCR4-mekanismen, men utan klinisk eller preklinisk evidens specifikt för SMM kan rekommendation om framsteg inte ges.

**För att gå vidare krävs:**
- Prekliniska studier (in vitro och in vivo) som specifikt undersöker Plerixafor mot SMM-celler och deras benmärgs­mikromiljö
- Bedömning av om SMM som population lämpar sig för CXCR4-riktad behandling jämfört med aktiv intervention
- Insamling av fullständig säkerhetsdata (MOA-profil via DrugBank, produktresumé från EMA/FDA)
- Klargörande av om effekten vid SMM skiljer sig mekanistiskt från den redan bevisade stamcells­mobiliserings­indikationen, för att undvika konceptuell sammanblandning
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

