---
layout: default
title: Dapoxetine
parent: Endast modellprediktion (L5)
nav_order: 123
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Dapoxetine: predikterad ny indikation Migrän (migraine disorder) (evidensnivå L5). Ursprunglig indikation: Prematur ejakulation"
monitor_inn: "dapoxetine"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
---

# Dapoxetine
{: .fs-9 }

Evidensnivå: **L5** | Förutsagda indikationer: **3** st
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

## Dapoxetin: Från prematur ejakulation till migrän
{: .text-alpha }

---

### Sammanfattning

Dapoxetin är en kortverkande selektiv serotoninåterupptagshämmare (SSRI) som ursprungligen användes för att behandla prematur ejakulation. TxGNN-modellen (deep learning) förutsäger att det kan vara effektivt mot **migrän** (migraine disorder), med poängen 0.9934. Poängen kommer från modellen och kan spegla likheter som modellen lärt sig mellan relaterade sjukdomar, inte biologisk evidens. Det finns **inga kliniska prövningar** och **2 publikationer** (en översikt och en kohortstudie) som endast indirekt berör frågan. Förutsägelsen bygger därmed i praktiken på modellen och på klassresonemang kring SSRI.

---

### Snabböversikt

| Post | Innehåll |
|------|------|
| Ursprunglig indikation | Prematur ejakulation (godkänd indikationstext saknas i licensdata) |
| Förutsagd ny indikation | Migrän (migraine disorder) |
| TxGNN-förutsägelsepoäng | 0,9934 |
| Evidensnivå | L5 |
| Marknadsstatus i Sverige | Marknadsförd (giltiga godkännanden: 2 av 2) |
| Antal godkännanden | 2 (giltiga: 2) |
| Rekommenderat beslut | Avvakta |

---

### Varför är denna förutsägelse rimlig?

För närvarande finns ingen detaljerad verkningsmekanismdata tillgänglig i det underlag som sammanställts för rapporten. Baserat på känd information är dapoxetin en kortverkande SSRI. Den hämmar serotonintransportören (SERT, kodad av genen SLC6A4), vilket ökar mängden serotonin i synapsen. Dess effekt vid prematur ejakulation är belagd, och mekanistiskt kan den vara tillämpbar på migrän.

Serotonin är inblandat i migränens patofysiologi, bland annat i aktiveringen av det trigeminovaskulära systemet och i kortikal spridande depression. Det är därför rimligt att en substans som påverkar serotoninsignalering kan ha en effekt. Kopplingen gäller dock hela SSRI-klassen och är indirekt. Det finns inga dapoxetinspecifika migrändata.

Dapoxetin är dessutom utformat för behovsstyrd användning och har en mycket kort halveringstid. Det passar sämre för långvarig, förebyggande behandling, som ofta är aktuell vid migrän. Den höga poängen (0,9934) är en datorberäknad förutsägelse och ska inte tolkas som kliniskt bevis.

<!-- review:begin se-lic-20261106-dapoxetine-1 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Båda godkännandena gäller Phoenix Labs Unlimited Company och är indragna. Det finns alltså inget giltigt godkännande i Sverige för närvarande.” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 2, varav giltiga: 2; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-dapoxetine-1 -->

---

### Litteraturbevis

| PMID | År | Typ | Tidskrift | Viktiga fynd |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Översikt | Current neuropharmacology | Genomgång av off-label-användning av SSRI-preparat, bland annat vid migrän. Handlar om SSRI som klass, inte om dapoxetin specifikt. |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Kohortstudie | Urologia | Behandlingsföljsamhet hos patienter med prematur ejakulation som behandlas med dapoxetin. Ingen koppling till migrän. |

---

### Marknadsinformation Sverige

| Godkännandenummer | Produktnamn | Beredningsform | Godkänd indikation |
|---------|------|------|-----------|
| 26320 | Priligy | Filmdragerad tablett | Ingen indikationstext tillgänglig |
| 26319 | Priligy | Filmdragerad tablett | Ingen indikationstext tillgänglig |

<!-- review:begin se-row-20261112-dapoxetine-1 -->

> **Granskningsrättelse (2026-11-12)**: Ursprungligen stod det: ”26320 / Priligy (indragen) / Filmdragerad tablett / Ingen indikationstext tillgänglig; 26319 / Priligy (indragen) / Filmdragerad tablett / Ingen indikationstext tillgänglig” Enligt Läkemedelsverkets registreringsstatus (2026-11-02) har 26320, 26319 status Godkänd; tabellen angav dem som indraget. Endast statusuppgiften i tabellen har ändrats. Källa: [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv).

<!-- review:end se-row-20261112-dapoxetine-1 -->

---

### Säkerhetsaspekter

- **Läkemedelsinteraktioner**: Data om interaktioner med specifika läkemedel saknas. Den enda posten som finns beskriver läkemedlets farmakologiska mål, serotonintransportören (SERT), och är ingen interaktion mellan läkemedel.

Som SSRI bör dapoxetin hanteras med särskild försiktighet vid samtidig användning av andra serotonerga läkemedel. Det är dock en klassbaserad slutsats och inte något som framgår av underlaget. Se produktresumén för fullständig säkerhetsinformation, inklusive varningar och kontraindikationer.

---

### Slutsats och nästa steg

**Beslut: Avvakta**

**Motivering:**
- Förutsägelsen för migrän bygger enbart på modellen och på ett indirekt klassresonemang kring SSRI. Det finns inga kliniska prövningar, ingen dapoxetinspecifik litteratur och ofullständiga säkerhetsdata. Läkemedlet är marknadsfört i Sverige med 2 giltiga godkännanden av 2.

**För att gå vidare krävs:**
- Säkerhetsinformation (varningar och kontraindikationer) från produktresumén hos Läkemedelsverket
- Uppgifter om verkningsmekanismen från DrugBank
- Dapoxetinspecifika prekliniska eller kliniska data för migrän
- En bedömning av om dapoxetins korta halveringstid och behovsstyrda dosering är förenliga med migränbehandling
- Klargörande av regulatorisk status

<!-- review:begin se-lic-20261106-dapoxetine-2 -->

> **Granskningsrättelse (2026-11-06)**: Ursprungligen stod det: ”Klargörande av regulatorisk status, eftersom båda godkännandena är indragna” Borttaget: uppgiften att godkännandena är avregistrerade eller att inget giltigt godkännande finns stämde inte med Läkemedelsverkets data (2026-11-06). Antal godkännanden enligt uppgifterna: 2, varav giltiga: 2; aktuella siffror finns i snabböversikten och tabellen under Marknadsinformation Sverige. Källa: [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/).

<!-- review:end se-lic-20261106-dapoxetine-2 -->

<!-- review:begin log -->

## Granskningslogg

Nedan finns granskningsloggen för den här sidan: uppgifter som kontrollerats mot Läkemedelsverkets data. Rättelser gäller endast grundläggande faktauppgifter; modellens prediktioner, evidensnivåer och slutsatser har inte skrivits om.

| Granskningsdatum | Punkt | Åtgärd | Källa |
|------|------|------|------|
| 2026-11-06 | Borttaget: ”Båda godkännandena gäller Phoenix Labs Unlimited Company och är indragna. Det finns alltså inget giltigt godkännande i Sverige för närvarand” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-06 | Borttaget: ”eftersom båda godkännandena är indragna” | Rättad | [Läkemedelsverket – export av godkända läkemedel](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv); [Läkemedelsverket](https://www.lakemedelsverket.se/) |
| 2026-11-12 | Tabell: 2 godkännanden (26320, 26319) är godkända, inte indragna | Rättad | [Läkemedelsverket – export av godkända läkemedel (registreringsstatus)](https://www.lakemedelsverket.se/api/lmfrest/exportmedprodcsv) |

<!-- review:end log -->

## Ansvarsfriskrivning

Detta innehåll är endast avsett för forskningsändamål och utgör inte medicinsk rådgivning.
Klinisk validering krävs före klinisk tillämpning.

---

