---
layout: default
title: Parecoxib
parent: Måttlig evidens (L3-L4)
nav_order: 338
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-28
description: "Parecoxib: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L3). Ursprunglig indikation: Ej angiven i tillgängliga licensuppgifter"
monitor_inn: "parecoxib"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension"]
---

# Parecoxib
{: .fs-9 }

Evidensnivå: **L3** | Förutsagda indikationer: **3** st
{: .fs-6 .fw-300 }

---

## Innehållsförteckning
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Apotekarens bedömningsrapport

</div>

## Parecoxib: Från (ingen registrerad indikation) till migrän
{: .text-alpha }

---

## Sammanfattning

Parecoxib är en injicerbar, selektiv COX-2-hämmare (prodrug till valdecoxib). Det finns ingen godkänd ursprunglig indikation i de data som sammanställts för denna rapport, eftersom indikationstexten saknas i licensuppgifterna. TxGNN-modellen förutsäger att parecoxib kan vara effektivt mot **migrän**, med **0 kliniska prövningar** och **1 publikation** som för närvarande stöder denna riktning (ytterligare prekliniska studier stöder mekanismen).

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga licensuppgifter |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 99,5 % |
| Evidensnivå | L3 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 3 av 3) |
| Antal godkännanden | 3 (giltiga: 3) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i databasuppgifterna. Baserat på känd information är parecoxib en prodrug till valdecoxib, en selektiv COX-2-hämmare med smärtlindrande och antiinflammatoriska egenskaper.

Vid migrän bidrar COX-2-beroende bildning av prostaglandin E2 (PGE2) till neurogen inflammation och sensibilisering av trigeminusnerven. Att hämma COX-2 kan därför mekanistiskt minska smärtan under en akut attack.

Prekliniska studier stöder detta: IL-1β stimulerar COX-2-beroende PGE2-syntes och CGRP-frisättning i trigeminusganglieceller hos råtta, och parecoxib påverkar plasmaproteinläckage och c-fos-uttryck i råttmodeller av trigeminovaskulär aktivering. Den höga modellpoängen är förenlig med denna mekanism, men poängen är i sig inte evidens för klinisk effekt.

---

## Kliniska prövningar

Inga relaterade kliniska prövningar registrerade för närvarande.

---

## Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | Klinisk pilotstudie (jämförande effekt; design behöver verifieras) | Clinical Neuropharmacology | Jämför intravenöst parecoxib 40 mg med rizatriptan 10 mg (smälttablett) och sumatriptan (subkutan injektion) vid akuta migränattacker. |
| [16492237](https://pubmed.ncbi.nlm.nih.gov/16492237/) | 2006 | Preklinisk (råtta) | Headache | Undersökte parecoxibs effekt på plasmaproteinläckage i hjärnhinnorna och c-fos-uttryck i trigeminus i en djurmodell av migrän. |
| [21394197](https://pubmed.ncbi.nlm.nih.gov/21394197/) | 2011 | Preklinisk (in vitro) | PLoS One | IL-1β stimulerar COX-2-beroende PGE2-syntes och CGRP-frisättning i trigeminusganglieceller hos råtta. |

Observera att de två prekliniska studierna är kopplade till den relaterade posten "migrän, känslighet (susceptibility)" och ger indirekt mekanistiskt stöd.

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 60191 | Parecoxib Noridem | Pulver till injektionsvätska, lösning | Ej angiven (indraget) |
| 60190 | Parecoxib Noridem | Pulver och vätska till injektionsvätska, lösning | Ej angiven (indraget) |
| 65728 | Parecoxib Macure | Pulver till injektionsvätska, lösning | Ej angiven (indraget) |

---

## Säkerhetsaspekter

Se produktresumén för säkerhetsinformation.

Ett teoretiskt säkerhetsproblem gäller för de relaterade förutsägelserna: COX-2-hämning kan förskjuta balansen mellan prostacyklin och tromboxan mot kärlsammandragning och trombos.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Den kliniska evidensen består av en enda pilotstudie vars design inte är bekräftad, inga kliniska prövningar är registrerade, och alla svenska godkännanden är indragna. Mekanismen är rimlig, men underlaget räcker inte för att gå vidare.

**För att gå vidare krävs:**
- Genomgång av fulltexten till PMID 21996647 för att fastställa studiedesign och effektresultat (kan påverka evidensnivån om det är en randomiserad studie).
- Hämta verkningsmekanismdata från DrugBank.
- Hämta varningar och kontraindikationer från produktresumén hos Läkemedelsverket (MPA), vilket är en förutsättning för säkerhetsgranskning.
- Klargöra läkemedlets ursprungliga godkända indikation samt orsaken till att godkännandena dragits in.
- Bedöma administreringsvägens lämplighet (injektion) för akut migrän jämfört med nuvarande behandlingar.

---

### Övriga förutsägelser (kort)

- **Migrän med hjärnstammsaura:** Evidensnivå L5, endast modellförutsägelse och ingen subtypsspecifik evidens. Beslut: avvakta.
- **Migrän, känslighet (susceptibility):** Evidensnivå L4. Avser genetisk benägenhet snarare än ett behandlingsbart tillstånd och bör användas som mekanistiskt stöd för akut migrän.
- **Pulmonell hypertension:** Evidensnivå L4. Den enda studien (grisungar med sepsis) visade att parecoxib inte hämmar tromboxansyntesen, vilket inte ger stöd för behandlingsnytta. Beslut: avvakta.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

