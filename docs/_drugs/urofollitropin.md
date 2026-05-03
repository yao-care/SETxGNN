---
layout: default
title: Urofollitropin
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Urofollitropin
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

Nu genererar jag rapporten baserat på Evidence Pack. Urofollitropin (DB00094) är ett follikelstimulerande hormon (FSH) utan godkänd indikation i Sverige – systemprompten anger att `taiwan_regulatory` avser MPA-data (Sverige).

---

# Urofollitropin: Från fertilitetsbehandling till migrän

## Sammanfattning

Urofollitropin är ett renat follikelstimulerande hormon (FSH) som traditionellt används för ovulationsinduktion och kontrollerad ovariestimulering inom fertilitetsbehandling. TxGNN-modellen förutsäger att läkemedlet kan ha effekt mot **migrän**, baserat på en indirekt biologisk länk via FSH-driven estrogenproduktion och trigeminal neurovaskulär sensibilisering. Evidensbasen är dock ytterst svag – **inga kliniska prövningar** och **inga direkta publikationer** stödjer denna riktning, vilket ger lägsta möjliga evidensnivå (L5).

---

## Snabböversikt

| Post | Innehåll |
|------|----------|
| Ursprunglig indikation | Ovulationsinduktion och kontrollerad ovariestimulering (fertilitetsbehandling, FSH-baserad) |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,85 % |
| Evidensnivå | L5 – Endast modellförutsägelse, inga faktiska studier |
| Marknadsstatus i Sverige | Inte godkänt i Sverige |
| Antal godkännanden | 0 |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

Urofollitropin är ett renat FSH som stimulerar äggstockarnas follikeltillväxt och ökar estrogenproduktionen. Eftersom FSH inte verkar direkt på centrala nervsystemet, bygger TxGNN-förutsägelsen på en flerstegskedja i kunskapsgrafen: **FSH → ökad estrogensyntes → modulering av trigeminal neurovaskulär känslighet → migrän**.

Menstruationsmigrän är välkänt kopplad till cykliska estrogenfluktuationer – ett sjunkande estrogenläge inför menstruation sänker tröskeln för trigeminusaktivering och kortikalt spridande depolarisation. Teorin är att Urofollitropin, genom att stabilisera eller höja estrogenproduktionen, teoretiskt skulle kunna dämpa denna känslighet. Det finns dock **ingen klinisk eller preklinisk studie** som undersökt detta samband, och naturliga FSH-variationer under menstruationscykeln har inte förknippats med något migränskydd.

Sammantaget är mekanismlänken **höggradigt indirekt** och bedöms av analysen som sannolikt flerstegsbrus i kunskapsgrafen. Förutsägelsen ska inte tolkas som ett kliniskt meningsfullt fynd utan som en hypotesgenerande signal som kräver grundlig preklinisk validering innan man kan gå vidare.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

Ingen direkt relaterad litteratur tillgänglig för närvarande.

> **Viktig notering om kunskapsgrafbrus:** Vid sökning på den relaterade indikationen *"migraine with or without aura, susceptibility to"* (rank 9 i TxGNN) hittades 20 publikationer. Granskning visar att samtliga artiklar handlar om **genetisk överlappning mellan epilepsi och migrän** (SCN1A, CACNA1A, neuroinflammation m.m.) och saknar varje koppling till Urofollitropin. Dessa klassificeras som KG-sökbrus och inkluderas **inte** i evidensbedömningen.

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

> Säkerhetsdata (varningar, kontraindikationer, läkemedelsinteraktioner) saknas i detta Evidence Pack. Hämtning av fullständig produktresumé från EMA/Läkemedelsverket rekommenderas innan vidare utvärdering.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
Förutsägelsen grundar sig uteslutande på TxGNN-modellens kunskapsgrafflöde (FSH → estrogen → trigeminal neurovaskulär modulering) utan stöd från kliniska prövningar, observationsstudier eller direkta publikationer om Urofollitropin vid migrän. Den mekanistiska länken är flerstegsindirekt och bedöms med hög sannolikhet utgöra kunskapsgrafbrus.

**För att gå vidare krävs:**
- **Preklinisk validering** av FSH:s eventuella effekt på trigeminusaktivering i djurmodeller för menstruationsmigrän
- **MOA-data** från DrugBank (identifierat datahål DG002) för att stärka mekanismanalysen
- **Fullständig säkerhetsinformation** från EMA- eller MPA-produktresumé (identifierat datahål DG001) innan eventuell hypotestestning
- **Expertgranskning** av reproduktionsmedicinsk specialist och neurolog i samverkan, givet FSH:s hormonella verkningsprofil
- **Litteratursökning** specifikt inriktad på hormonell migrän och exogen FSH-behandling som komplement till TxGNN-signalen
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

