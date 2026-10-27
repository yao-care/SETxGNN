---
layout: default
title: Ivabradine
parent: Endast modellprediktion (L5)
nav_order: 241
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ivabradine: predikterad ny indikation Hypertrikos (hypertrichosis) (evidensnivå L5). Ursprunglig indikation: Ej angiven i tillgängliga data"
monitor_inn: "ivabradine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **6** st
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

## Ivabradin: Från hjärtsjukdom (indikation ej angiven i data) till hypertrikos
{: .text-alpha }

## Sammanfattning

Ivabradin är en hämmare av HCN-kanalen (If-strömmen, "funny current") i sinusknutan. I de data som sammanställts för denna rapport finns ingen godkänd indikationstext registrerad för läkemedlet. TxGNN-modellen förutsäger att ivabradin kan vara effektivt mot **hypertrikos** med en mycket hög modellpoäng (**99,8 %**), men det finns **0 kliniska prövningar** och **0 publikationer** som stöder förutsägelsen. Den är därmed en ren beräkningsmässig förutsägelse.

---

## Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Ej angiven i tillgängliga data |
| Förutsagd ny indikation | Hypertrikos (hypertrichosis) |
| TxGNN-förutsägelsepoäng | 99,8 % |
| Evidensnivå | L5 (endast modellförutsägelse) |
| Marknadsstatus i Sverige | Endast indragna godkännanden |
| Antal godkännanden | 6 (samtliga indragna) |
| Rekommenderat beslut | Avvakta |

---

## Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i de sammanställda uppgifterna. Baserat på känd information hämmar ivabradin HCN-kanalen, främst HCN4 i sinusknutan, vilket sänker hjärtfrekvensen. Någon dokumenterad koppling till reglering av hårväxt finns inte.

HCN-kanaler har beskrivits i vissa vävnader utanför hjärtat, men deras betydelse för hårfolliklar är spekulativ. Den höga poängen (0,998) är en kunskapsgrafsprediktion och stöds inte av mekanistiska eller kliniska data. Hypertrikos är dessutom en känd biverkan av vissa läkemedel (t.ex. minoxidil), så en substans som orsakar eller behandlar kraftig hårväxt skulle behöva en tydlig biologisk förklaring. Den saknas här.

### Övriga förutsägelser från modellen

Samtliga övriga förutsägelser har också evidensnivå L5, utan studier eller litteratur:

| Rang | Sjukdom | Poäng | Bedömning av mekanistisk koppling |
|------|---------|-------|------|
| 2 | Ambras typ av kongenital universell hypertrikos | 99,7 % | Genetiskt betingad (TRPS1-reglering); ingen känd koppling till HCN-blockad |
| 3 | Missbildningssyndrom med tand- och/eller tandköttskomponent | 99,7 % | Ingen trolig koppling; poängen kan spegla närhet till hypertrikos i grafen |
| 4 | Syndrom med Dandy-Walker-missbildning som huvuddrag | 99,7 % | Strukturell hjärnmissbildning; knappast behandlingsbar med läkemedel |
| 5 | Isolerad genetisk hårstråavvikelse | 99,7 % | Strukturella/keratinrelaterade defekter; ingen känd effekt av HCN-hämning |
| 6 | Nefrogent syndrom med inadekvat antidures (NSIAD) | 99,1 % | Orsakas av aktiverande mutationer i V2-receptorn; endast en svag teoretisk koppling via cAMP-moduleringen av HCN |

---

## Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 62662 | Ivabradin Medical Valley | Filmdragerad tablett | Ej angiven (indragen) |
| 53688 | Ivabradin Medical Valley | Filmdragerad tablett | Ej angiven (indragen) |
| 62663 | Ivabradin Medical Valley | Filmdragerad tablett | Ej angiven (indragen) |
| 53687 | Ivabradin Medical Valley | Filmdragerad tablett | Ej angiven (indragen) |
| 53641 | Ivabradin Krka | Filmdragerad tablett | Ej angiven (indragen) |

Ytterligare ett godkännande (53642, Ivabradin Krka) finns, totalt sex. Alla är indragna, och ingen är giltig för närvarande.

---

## Säkerhetsaspekter

**Läkemedelsinteraktioner**: Totalt 138 interaktioner är registrerade. Bland de som redovisats finns flera av allvarlig grad (Major), bland annat:

- Aprepitant
- Klaritromycin
- Cobicistat
- Cisaprid
- Klotrimazol
- Levofloxacin
- Papaverin
- Ondansetron, granisetron, dolasetron och palonosetron

Måttliga interaktioner (Moderate) rapporteras bland annat för famotidin, ranitidin, cimetidin, nizatidin, dexametason, mikonazol, metreleptin och troglitazon.

Se produktresumén för övrig säkerhetsinformation, inklusive varningar och kontraindikationer.

---

## Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen bygger enbart på en modellpoäng utan kliniska prövningar, litteratur eller en trovärdig mekanism. Dessutom saknas giltiga godkännanden i Sverige, och varnings- och kontraindikationsdata saknas.

**För att gå vidare krävs:**
- Hämta och granska produktresumén (varningar, kontraindikationer och godkänd indikation) från Läkemedelsverket.
- Komplettera verkningsmekanismdata, t.ex. via DrugBank.
- Utreda om HCN-kanaler har någon biologisk roll i hårfolliklar eller i de andra förutsagda sjukdomarna, med prekliniska studier.
- Göra en litteratur- och prövningssökning specifikt för ivabradin och hypertrikos.
- Bedöma administreringsväg och beredningsform (för närvarande endast oral tablett) i förhållande till den nya indikationen.
- Överväga att genetiskt betingade missbildningssyndrom (rang 2–5) har låg sannolikhet att svara på ett hjärtfrekvenssänkande läkemedel.
## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

