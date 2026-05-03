---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Mannitol
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

Använder **txgnn-pipeline**-skillet för att säkerställa korrekt hantering av TxGNN-rapportgenerering i Se-projektkontexten. Nu genererar jag rapporten baserat på Evidence Pack:

---

# Mannitol: Från osmotisk diures till nefrogent syndrom av inadekvat antidiures

## Sammanfattning

Mannitol (DB00742) är ett osmotiskt aktivt diuretikum känt för sin förmåga att öka plasmaosmolatiteten och därigenom inducera vätskeomfördelning och fri vattenutskiljning via njurarna — kliniskt använt bland annat vid förhöjt intrakraniellt tryck och akut oliguri. TxGNN-modellen förutsäger att det kan vara effektivt mot **nefrogent syndrom av inadekvat antidiures (NSIAD)**, med **0 kliniska prövningar** och **1 publikation** som för närvarande stöder denna riktning. Evidensunderlaget är mycket begränsat och baseras i praktiken uteslutande på modellförutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ingen godkänd indikation registrerad i Sverige |
| Förutsagd ny indikation | Nefrogent syndrom av inadekvat antidiures (NSIAD) |
| TxGNN-förutsägelsepoäng | 99,97% |
| Evidensnivå | L5 – Enbart modellförutsägelse, inga direkta kliniska studier |
| Marknadsstatus i Sverige | Ej godkänd |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i detta datapaket. Baserat på känd information är mannitol ett osmotiskt diuretikum av polyolklassen — det verkar genom att höja plasmaosmolatiteten, vilket drar vätska från vävnaderna till den intravaskulära kompartmenten och ökar njurarnas utskiljning av fri vatten utan att aktivera hormonella mekanismer.

Nefrogent syndrom av inadekvat antidiures (NSIAD) orsakas av gain-of-function-mutationer i AVPR2-genen (V2-receptorn för antidiuretiskt hormon). Dessa mutationer leder till konstitutiv receptoraktivering oberoende av ADH-nivåer, vilket resulterar i kontinuerlig vattenretention och kronisk dilutionshyponatremi. Tillståndet diagnostiseras ofta sent och saknar väletablerade farmakologiska behandlingsalternativ.

Den mekanistiska kopplingen som TxGNN sannolikt identifierat är att mannitols osmotiska verkan teoretiskt kan motverka den patologiska vattenretentionen vid NSIAD: genom att öka den osmotiska belastningen i tubulusvätskan kan mannitol minska relativ fri vattenresorption och bidra till korrektion av hyponatremin. Kunskapsgrafens noder kring natriumbalans, osmolatitet och aquaporin-2-reglering delar sannolikt kanter med mannitols farmakologiska profil. Det saknas dock kliniska data som bekräftar denna hypotetiska koppling direkt, och kausaliteten är ännu inte validerad.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|----|-----|-----------|--------------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Översiktsartikel | European Journal of Internal Medicine | Beskriver de tio vanligaste fallgroparna vid utredning av hyponatremipatienter; lyfter fram NSIAD som en underdiagnostiserad differentialdiagnos och betonar vikten av korrekt etiologisk klassificering för att undvika behandlingskomplikationer vid felaktig hantering |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Evidensunderlaget för mannitol vid NSIAD baseras uteslutande på TxGNN-modellförutsägelse (L5) med ett enda indirekt litteraturreferens om hyponatremiutredning i allmänhet; det finns inga kliniska prövningar eller mekanistiska studier som direkt undersöker denna indikation.

**För att gå vidare krävs:**
- **Mekanistisk validering:** Bekräfta om mannitols osmotiska effekter faktiskt kan korrigera NSIAD-orsakad hyponatremi utan att orsaka volymöverbelastning eller förvärra elektrolytobalansen
- **Säkerhetsgranskning:** Inhämta fullständig produktresumé och SPC för att fastställa kontraindikationer, varningar och interaktionsprofil
- **Prekliniska studier:** In vitro- eller djurmodellstudier med AVPR2 gain-of-function-modeller för att undersöka potentiell effekt
- **Riktad litteratursökning:** Systematisk genomgång av mannitol vid hyponatremi och NSIAD i klinisk praxis för att identifiera eventuella fallrapporter eller observationsdata
- **Regulatorisk kartläggning:** Utred om mannitol kan registreras i Sverige som särläkemedel (orphan drug) för denna sällsynta diagnos
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

